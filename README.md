# GramSetu (Ask Sarthi) - MVP

Digital inclusion for rural higher education in Madhya Pradesh.
Offline-first, trilingual (Hindi / Hinglish / English), low-bandwidth, voice-enabled.

## Run

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python -m uvicorn backend.main:app --port 8000
# then open frontend/index.html in a browser
```

API at `http://localhost:8000` (`/api/health`, `/api/courses`,
`/api/lesson/{id}`, `/api/doubt`, `/api/scholarships`,
`/api/scholarships/check`, `/api/career/quiz`, `/api/mentors`,
`/api/mentors/book`).

## Problem statement coverage

| Challenge feature | MVP |
|---|---|
| Offline-first learning | Lessons cached in localStorage after first open; every lesson <25KB; offline pill + fallback |
| Regional language support | Full Hindi / Hinglish / English UI + content switcher |
| AI-powered doubt resolution | Keyword Sarthi over Physics/Maths/English/scholarship/career + graceful fallback |
| Voice-based interaction | Web Speech STT (hi-IN/en-IN mic) + speechSynthesis read-aloud on answers and lessons |
| Low-bandwidth optimization | Text-only JSON API, single static HTML file, no frameworks, no images |
| Scholarship discovery | 6 real MP schemes (MMVY, Gaon Ki Beti, Pratibha Kiran, Post-Matric SC/ST/OBC) with 2026 rules + eligibility checker + document lists |
| Digital mentoring | 3 MP mentors with booking flow |
| Career counseling | Interest quiz mapping to 6 MP-relevant paths (nursing, ITI, teacher, polytechnic, agri, competitive exams) |

## Design

Reading this as: public-service learning product for rural students and judges, with a warm trust-first language, leaning toward earthy editorial (paper + leaf green + marigold) with native CSS only.
Dials: VARIANCE 5, MOTION 2, DENSITY 4. No frameworks so the page loads on 2G.
Zero em-dashes shipped.

## Files

- `backend/main.py` - FastAPI app (one deep module, small interface)
- `backend/seed.py` - trilingual seed content
- `frontend/index.html` - entire product (single file, offline cache via localStorage)
- `requirements.txt` - fastapi + uvicorn
