"""GramSetu (Ask Sarthi) API: one deep module behind a small interface.

Endpoints: courses, lessons, doubt solver, scholarships + eligibility check,
career quiz, mentor booking. All content is trilingual (hi/en/hinglish) and
plain text so it stays usable offline and on low bandwidth.
"""

import json
import os
import urllib.request
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from .seed import CAREERS, COURSES, DOUBTS, MENTORS, POINTS, SCHOLARSHIPS

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"

app = FastAPI(title="GramSetu API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def pick(text_map: dict, lang: str) -> str:
    if lang in text_map:
        return text_map[lang]
    return text_map.get("hi", next(iter(text_map.values())))


class DoubtIn(BaseModel):
    question: str = Field(min_length=2, max_length=500)
    lang: str = "hi"


class EligibleIn(BaseModel):
    class12_pct: float = 0
    board: str = "mp"  # mp | cbse | icse
    income_lakh: float = 0
    category: str = "general"  # general | sc | st | obc
    gender: str = ""  # female | male | other
    rural: bool = False
    lang: str = "hi"


class QuizIn(BaseModel):
    interests: str = Field(min_length=2, max_length=300)
    qualification: str = "12th"
    lang: str = "hi"


class BookingIn(BaseModel):
    mentor_id: str
    name: str = Field(min_length=2, max_length=80)
    topic: str = Field(min_length=2, max_length=200)


@app.get("/api/health")
def health():
    return {"ok": True, "service": "gramsetu"}


@app.get("/", include_in_schema=False)
def index():
    return FileResponse(FRONTEND_DIR / "index.html")


@app.get("/index.html", include_in_schema=False)
def index_html():
    return FileResponse(FRONTEND_DIR / "index.html")


app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")


@app.get("/api/courses")
def courses(lang: str = "hi"):
    out = []
    for c in COURSES:
        out.append(
            {
                "id": c["id"],
                "title": pick(c["title"], lang),
                "subject": pick(c["subject"], lang),
                "level": c["level"],
                "desc": pick(c["desc"], lang),
                "lessons": [
                    {"id": l["id"], "title": pick(l["title"], lang), "minutes": l["minutes"], "size_kb": l["size_kb"]}
                    for l in c["lessons"]
                ],
            }
        )
    return {"courses": out}


@app.get("/api/lesson/{lesson_id}")
def lesson(lesson_id: str, lang: str = "hi"):
    for c in COURSES:
        for l in c["lessons"]:
            if l["id"] == lesson_id:
                pts = POINTS.get(lesson_id, {})
                return {
                    "id": l["id"],
                    "course_id": c["id"],
                    "course": pick(c["title"], lang),
                    "title": pick(l["title"], lang),
                    "minutes": l["minutes"],
                    "size_kb": l["size_kb"],
                    "body": pick(l["body"], lang),
                    "points": pts.get(lang, pts.get("hi", [])),
                    "art": l["id"],
                }
    return {"error": "not found"}


GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
GEMINI_KEY = os.environ.get("GEMINI_API_KEY", "")


def _grounding_text() -> str:
    """Compact fact base fed to the LLM so answers stay grounded.

    Built from the same seed the keyword fallback and UI use, so the
    LLM and offline answers never contradict each other.
    """
    lines = []
    for c in COURSES:
        titles = " / ".join({c["title"].get(k, "") for k in ("hi", "en", "hinglish")})
        lines.append(f"Course {c['id']}: {titles} (Class {c['level']}).")
        for le in c["lessons"]:
            lt = " / ".join({le["title"].get(k, "") for k in ("hi", "en", "hinglish")})
            lines.append(f"  Lesson {le['id']}: {lt}.")
    for s in SCHOLARSHIPS:
        need_en = " | ".join(s["need"]["en"])
        docs_en = " | ".join(s["docs"]["en"])
        crit = ", ".join(f"{k}={v}" for k, v in s.get("criteria", {}).items())
        lines.append(f"Scholarship {s['id']}: {s['name']['en']}. Amount: {s['amount']['en']}. Portal: {s['portal']}. Rules: {crit}. Needs: {need_en}. Docs: {docs_en}.")
    for c in CAREERS:
        lines.append(f"Career {c['id']}: {c['title']['en']}. {c['desc']['en']}")
    for d in DOUBTS:
        lines.append(f"Fact: {d['answer']['en']} (keywords: {', '.join(d['keys'][:6])})")
    return "\n".join(lines)


def _sarthi_system(lang: str) -> str:
    lang_name = (
        "Hindi (Devanagari)" if lang == "hi" else "Hinglish (Roman Hindi)" if lang == "hinglish" else "simple English"
    )
    return (
        "You are Sarthi, a tutor for rural MP students (Classes 9 to 12, Hindi/Hinglish/English, often on 2G phones). "
        f"Always answer in {lang_name}.\n"
        "INSTRUCTIONS:\n"
        "1. Primary method is your own answer, but stay grounded in SOURCES below. For scholarships use ONLY the portal, amounts, percentages and income limits given there. Never invent a scheme, amount, or deadline.\n"
        "2. For studies (Motion, Algebra, English) explain in 2 to 4 short sentences plus one small everyday example, under 100 words total. Plain text, no markdown, no bullet symbols.\n"
        "3. If the question is outside your sources or you are unsure, say so in one line and point to the closest lesson, the teacher, or hescholarship.mp.gov.in.\n"
        "4. Never claim to book, apply, or pay for anything. Booking and forms happen in the app.\n"
        "SOURCES (same facts the app shows offline):\n" + _grounding_text()
    )


def _gemini_answer(question: str, lang: str) -> str | None:
    """Ask Gemini Flash with a grounded system prompt.

    Returns None when no key is configured or the call fails (no
    internet, bad key, timeout), so the caller can fall back to the
    offline keyword answers. stdlib only, no new dependency.
    """
    if not GEMINI_KEY:
        return None
    sys = _sarthi_system(lang)
    payload = json.dumps({"contents": [{"parts": [{"text": sys + "\n\nStudent question: " + question}]}]}).encode()
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={GEMINI_KEY}"
    try:
        req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=20) as r:
            data = json.loads(r.read().decode())
        parts = data.get("candidates", [{}])[0].get("content", {}).get("parts", [])
        text = "".join(p.get("text", "") for p in parts).strip()
        return text or None
    except Exception:
        return None


def _keyword_answer(question: str, lang: str) -> str | None:
    """Offline keyword fallback. Used only when the LLM is unreachable."""
    q = question.lower()
    for d in DOUBTS:
        if any(k in q for k in d["keys"]):
            return pick(d["answer"], lang)
    return None


@app.get("/api/doubt/status")
def doubt_status():
    return {"llm": bool(GEMINI_KEY), "model": GEMINI_MODEL, "mode": "gemini" if GEMINI_KEY else "offline"}


@app.post("/api/doubt")
def doubt(body: DoubtIn):
    """LLM-first: try Gemini, fall back to keywords only when offline.

    The keyword answers double as grounding sources inside the system
    prompt, so primary and fallback answers agree.
    """
    ai = _gemini_answer(body.question, body.lang)
    if ai:
        return {"answer": ai, "matched": True, "source": "gemini"}
    kw = _keyword_answer(body.question, body.lang)
    if kw:
        return {"answer": kw, "matched": True, "source": "offline"}
    fallback = {
        "hi": "अच्छा सवाल है! इसका जवाब मैं अभी सीख रहा हूँ। तब तक अपना सवाल अपने शिक्षक से पूछो, या कोर्स लेसन देखो।",
        "en": "Good question! I am still learning this answer. Meanwhile ask your teacher, or check the course lessons.",
        "hinglish": "Achha sawal hai! Iska jawab main abhi seekh raha hoon. Tab tak apne teacher se puchho, ya course lesson dekho.",
    }
    return {"answer": pick(fallback, body.lang), "matched": False, "source": "offline"}


@app.get("/api/scholarships")
def scholarships(lang: str = "hi"):
    return {
        "scholarships": [
            {
                "id": s["id"],
                "name": pick(s["name"], lang),
                "amount": pick(s["amount"], lang),
                "portal": s["portal"],
                "need": [pick({"hi": x, "en": y, "hinglish": z}, lang) for x, y, z in zip(s["need"]["hi"], s["need"]["en"], s["need"]["hinglish"])] if isinstance(s["need"], dict) else s["need"],
                "docs": [pick({"hi": x, "en": y, "hinglish": z}, lang) for x, y, z in zip(s["docs"]["hi"], s["docs"]["en"], s["docs"]["hinglish"])] if isinstance(s["docs"], dict) else s["docs"],
            }
            for s in SCHOLARSHIPS
        ]
    }


def _eligible(sid: str, p: EligibleIn) -> tuple[bool, str]:
    if sid == "mmvy":
        need = p.board == "mp" and p.class12_pct >= 70 or p.board in ("cbse", "icse") and p.class12_pct >= 85
        if need and p.income_lakh <= 6:
            return True, "12th % + income fit MMVY"
        return False, "MMVY needs 70% (MP board) or 85% (CBSE/ICSE), income to 6L"
    if sid == "gaon-ki-beti":
        if p.gender == "female" and p.rural and p.class12_pct >= 60:
            return True, "Rural girl, 60%+ in 12th"
        return False, "Needs: rural girl student, 60%+ in 12th"
    if sid == "pratibha-kiran":
        if p.gender == "female" and not p.rural and p.class12_pct >= 60:
            return True, "Urban girl, 60%+ in 12th (BPL)"
        return False, "Needs: urban BPL girl student, 60%+ in 12th"
    if sid == "post-matric-sc":
        if p.category == "sc" and p.income_lakh <= 2.5:
            return True, "SC + income to 2.5L"
        return False, "Needs: SC category, income to 2.5L"
    if sid == "post-matric-st":
        if p.category == "st" and p.income_lakh <= 6:
            return True, "ST + income to 6L"
        return False, "Needs: ST category, income to 6L"
    if sid == "post-matric-obc":
        if p.category == "obc" and p.income_lakh <= 1:
            return True, "OBC + income to 1L"
        return False, "Needs: OBC category, income to 1L"
    return False, "Unknown scheme"


@app.post("/api/scholarships/check")
def check_eligibility(p: EligibleIn):
    results = []
    for s in SCHOLARSHIPS:
        ok, why = _eligible(s["id"], p)
        results.append(
            {"id": s["id"], "name": pick(s["name"], p.lang), "amount": pick(s["amount"], p.lang), "portal": s["portal"], "eligible": ok, "reason": why}
        )
    results.sort(key=lambda r: (not r["eligible"], r["id"]))
    return {"results": results}


@app.post("/api/career/quiz")
def career_quiz(q: QuizIn):
    text = (q.interests + " " + q.qualification).lower()
    scored = []
    for c in CAREERS:
        score = sum(1 for f in c["fit"] if f in text)
        scored.append((score, c))
    scored.sort(key=lambda t: -t[0])
    top = [c for _, c in scored[:3]] if scored[0][0] > 0 else [c for _, c in scored[:3]]
    return {
        "recommendations": [
            {"id": c["id"], "title": pick(c["title"], q.lang), "desc": pick(c["desc"], q.lang)} for c in top
        ]
    }


@app.get("/api/mentors")
def mentors(lang: str = "hi"):
    return {"mentors": [{"id": m["id"], "name": m["name"], "role": pick({"hi": m["role_hi"], "en": m["role_en"], "hinglish": m["role_en"]}, lang), "tags": m["tags"]} for m in MENTORS]}


@app.post("/api/mentors/book")
def book(b: BookingIn):
    m = next((x for x in MENTORS if x["id"] == b.mentor_id), None)
    if not m:
        return {"error": "mentor not found"}
    return {
        "confirmed": True,
        "message": f"{b.name}, {m['name']} se '{b.topic}' par baat pakki! Samay SMS par milega (demo).",
        "booking": {"mentor": m["name"], "student": b.name, "topic": b.topic},
    }
