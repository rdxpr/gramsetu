"""Seed content for GramSetu MVP.

Seed courses, lessons, and FAQs in Hindi, English, and Hinglish so the
offline-first frontend can ship with real demo content. Lessons are plain
text, small enough to sync over low bandwidth and cache in localStorage.
"""

COURSES = [
    {
        "id": "c1",
        "title": {"hi": "कक्षा 12 भौतिकी: गति", "en": "Class 12 Physics: Motion", "hinglish": "Class 12 Physics: Gati"},
        "subject": {"hi": "भौतिकी", "en": "Physics", "hinglish": "Physics"},
        "level": "12",
        "desc": {
            "hi": "गति, वेग और त्वरण की मूल बातें सरल उदाहरणों के साथ।",
            "en": "Basics of motion, velocity and acceleration with simple examples.",
            "hinglish": "Gati, veg aur tvaran ke basics simple examples ke saath.",
        },
        "lessons": [
            {
                "id": "c1l1",
                "title": {"hi": "गति क्या है?", "en": "What is motion?", "hinglish": "Gati kya hai?"},
                "minutes": 8,
                "size_kb": 18,
                "body": {
                    "hi": "जब कोई वस्तु समय के साथ अपनी स्थिति बदलती है, तो उसे गति कहते हैं। उदाहरण: चलती बस, उड़ता पक्षी।",
                    "en": "When an object changes its position with time, it is in motion. Examples: a moving bus, a flying bird.",
                    "hinglish": "Jab koi vastu samay ke saath apni jagah badalti hai, use gati kehte hain. Example: chalti bus, udta panchhi.",
                },
            },
            {
                "id": "c1l2",
                "title": {"hi": "वेग और त्वरण", "en": "Velocity and acceleration", "hinglish": "Veg aur tvaran"},
                "minutes": 10,
                "size_kb": 22,
                "body": {
                    "hi": "वेग = विस्थापन / समय। त्वरण = वेग में बदलाव / समय। इकाई: मी/से और मी/से²।",
                    "en": "Velocity = displacement / time. Acceleration = change in velocity / time. Units: m/s and m/s².",
                    "hinglish": "Veg = visthapan / samay. Tvaran = veg me badlav / samay. Unit: m/s aur m/s².",
                },
            },
            {
                "id": "c1l3",
                "title": {"hi": "अभ्यास प्रश्न", "en": "Practice questions", "hinglish": "Practice prashn"},
                "minutes": 12,
                "size_kb": 15,
                "body": {
                    "hi": "1. बस 2 घंटे में 120 किमी चली। औसत चाल क्या है? 2. वेग और चाल में अंतर लिखो।",
                    "en": "1. A bus travels 120 km in 2 hours. What is the average speed? 2. Write the difference between velocity and speed.",
                    "hinglish": "1. Bus 2 ghante me 120 km chali. Ausat chaal kya hai? 2. Veg aur chaal me antar likho.",
                },
            },
        ],
    },
    {
        "id": "c2",
        "title": {"hi": "कक्षा 10 गणित: बीजगणित", "en": "Class 10 Maths: Algebra", "hinglish": "Class 10 Maths: Beejganit"},
        "subject": {"hi": "गणित", "en": "Maths", "hinglish": "Maths"},
        "level": "10",
        "desc": {
            "hi": "रैखिक समीकरण और द्विघात समीकरण हल करना सीखो।",
            "en": "Learn to solve linear and quadratic equations.",
            "hinglish": "Rekhik samikaran aur dwighat samikaran hal karna seekho.",
        },
        "lessons": [
            {
                "id": "c2l1",
                "title": {"hi": "रैखिक समीकरण", "en": "Linear equations", "hinglish": "Rekhik samikaran"},
                "minutes": 9,
                "size_kb": 19,
                "body": {
                    "hi": "2x + 3 = 11 हो तो x = 4। दोनों पक्षों से समान संख्या घटाओ या जोड़ो।",
                    "en": "If 2x + 3 = 11 then x = 4. Add or subtract the same number from both sides.",
                    "hinglish": "Agar 2x + 3 = 11 ho to x = 4. Dono pakshon se barabar sankhya jodo ya ghatayo.",
                },
            },
            {
                "id": "c2l2",
                "title": {"hi": "द्विघात समीकरण", "en": "Quadratic equations", "hinglish": "Dwighat samikaran"},
                "minutes": 11,
                "size_kb": 24,
                "body": {
                    "hi": "x² - 5x + 6 = 0 के गुणनखंड (x-2)(x-3) हैं। इसलिए x = 2 या x = 3।",
                    "en": "x² - 5x + 6 = 0 factors into (x-2)(x-3). So x = 2 or x = 3.",
                    "hinglish": "x² - 5x + 6 = 0 ke gunankhand (x-2)(x-3) hain. Isliye x = 2 ya x = 3.",
                },
            },
        ],
    },
    {
        "id": "c3",
        "title": {"hi": "अंग्रेज़ी बोलना: रोज़मर्रा", "en": "Spoken English: Everyday", "hinglish": "Spoken English: Rozmarra"},
        "subject": {"hi": "अंग्रेज़ी", "en": "English", "hinglish": "English"},
        "level": "all",
        "desc": {
            "hi": "रोज़मर्रा की बातचीत के लिए 30 उपयोगी वाक्य।",
            "en": "30 useful sentences for daily conversation.",
            "hinglish": "Roz ki baatcheet ke liye 30 upyogi vakya.",
        },
        "lessons": [
            {
                "id": "c3l1",
                "title": {"hi": "परिचय देना", "en": "Introducing yourself", "hinglish": "Parichay dena"},
                "minutes": 7,
                "size_kb": 16,
                "body": {
                    "hi": "My name is... / मैं ... गाँव से हूँ। / I study in class... / मुझे ... बनना है।",
                    "en": "My name is... / I am from ... village. / I study in class... / I want to become a ...",
                    "hinglish": "My name is... / Main ... gaon se hoon. / I study in class... / Mujhe ... banna hai.",
                },
            },
            {
                "id": "c3l2",
                "title": {"hi": "बाज़ार में बातचीत", "en": "Talking at the market", "hinglish": "Bazaar me baatcheet"},
                "minutes": 8,
                "size_kb": 17,
                "body": {
                    "hi": "How much is this? / थोड़ा कम करो। / That is too costly. / मुझे यह चाहिए।",
                    "en": "How much is this? / Please reduce the price a little. / That is too costly. / I want this one.",
                    "hinglish": "How much is this? / Thoda kam karo. / That is too costly. / Mujhe yeh chahiye.",
                },
            },
        ],
    },
]

# Rule-based doubt answers (keyword -> answer). Kept tiny on purpose: the
# point is instant answers on low bandwidth, not a real LLM.
DOUBTS = [
    {
        "keys": ["newton", "न्यूटन", "gati", "गति", "motion", "velocity", "वेग", "acceleration", "त्वरण"],
        "answer": {
            "hi": "न्यूटन का पहला नियम: स्थिर वस्तु स्थिर रहती है और गतिमान वस्तु समान वेग से चलती रहती है, जब तक कोई बाहरी बल न लगे।",
            "en": "Newton's first law: an object at rest stays at rest and a moving object keeps the same velocity unless an external force acts.",
            "hinglish": "Newton ka pehla niyam: sthir vastu sthir rehti hai, chalti vastu same veg se chalti rehti hai jab tak bahari bal na lage.",
        },
    },
    {
        "keys": ["equation", "समीकरण", "beejganit", "बीज", "quadratic", "द्विघात", "linear", "रैखिक", "algebra", "x²", "maths", "गणित", "ganit"],
        "answer": {
            "hi": "समीकरण हल करने के लिए दोनों पक्षों पर एक जैसी क्रिया करो। द्विघात समीकरण के लिए गुणनखंड बनाओ या सूत्र x = (-b ± √(b²-4ac)) / 2a लगाओ।",
            "en": "To solve an equation, do the same operation on both sides. For quadratics, factorise or use x = (-b ± √(b²-4ac)) / 2a.",
            "hinglish": "Samikaran hal karne ke liye dono taraf same kriya karo. Dwighat ke liye gunankhand banao ya formula x = (-b ± √(b²-4ac)) / 2a lagao.",
        },
    },
    {
        "keys": ["english", "अंग्रेज़ी", "angrezi", "spoken", "sentence", "वाक्य", "grammar"],
        "answer": {
            "hi": "रोज़ एक वाक्य बोलकर अभ्यास करो: 'My name is...' से शुरू करो, फिर 'I am from...' जोड़ो। गलती से डरो मत।",
            "en": "Practise by speaking one sentence daily: start with 'My name is...', then add 'I am from...'. Do not fear mistakes.",
            "hinglish": "Roz ek vakya bolkar practice karo: 'My name is...' se shuru karo, phir 'I am from...' jodo. Galti se daro mat.",
        },
    },
    {
        "keys": ["scholarship", "छात्रवृत्ति", "chatravritti", "mmvy", "medhavi", "gaon ki beti", "form", "फॉर्म", "portal", "पोर्टल", "kyc", "income", "आय"],
        "answer": {
            "hi": "छात्रवृत्ति के लिए hescholarship.mp.gov.in पर आवेदन होता है। MMVY में 12वीं में 70% (MP बोर्ड) चाहिए और आय 6 लाख तक। दस्तावेज़: domicile, marksheet, आय प्रमाण, Aadhaar।",
            "en": "Scholarships are applied for at hescholarship.mp.gov.in. MMVY needs 70% in Class 12 (MP board) and income up to 6 lakh. Documents: domicile, marksheet, income proof, Aadhaar.",
            "hinglish": "Scholarship ke liye hescholarship.mp.gov.in par apply hota hai. MMVY me 12th me 70% (MP board) chahiye aur aay 6 lakh tak. Document: domicile, marksheet, aay praman, Aadhaar.",
        },
    },
    {
        "keys": ["career", "करियर", "naukri", "नौकरी", "iti", "polytechnic", "पॉलिटेक्निक", "nurse", "teacher", "शिक्षक", "course", "कोर्स"],
        "answer": {
            "hi": "12वीं के बाद विकल्प: ITI (इलेक्ट्रीशियन), पॉलिटेक्निक डिप्लोमा, B.Sc नर्सिंग, D.El.Ed (शिक्षक), या B.A./B.Sc. करके प्रतियोगी परीक्षा। अपनी रुचि चुनो, हम रोडमैप देंगे।",
            "en": "After Class 12: ITI (electrician), polytechnic diploma, B.Sc nursing, D.El.Ed (teacher), or B.A./B.Sc. followed by competitive exams. Pick your interest and we will give a roadmap.",
            "hinglish": "12th ke baad vikalp: ITI (electrician), polytechnic diploma, B.Sc nursing, D.El.Ed (teacher), ya B.A./B.Sc. karke competitive exam. Apni ruchi chuno, hum roadmap denge.",
        },
    },
]

SCHOLARSHIPS = [
    {
        "id": "mmvy",
        "name": {"hi": "मुख्यमंत्री मेधावी विद्यार्थी योजना", "en": "Mukhyamantri Medhavi Vidyarthi Yojana (MMVY)", "hinglish": "MMVY Medhavi scholarship"},
        "amount": {"hi": "पूरी ट्यूशन फीस", "en": "Full tuition fees", "hinglish": "Poori tuition fees"},
        "portal": "hescholarship.mp.gov.in",
        "criteria": {
            "min_class12_pct_mp_board": 70,
            "min_class12_pct_cbse_icse": 85,
            "max_income_lakh": 6,
            "domicile": "MP",
        },
        "need": {
            "hi": ["MP का domicile", "12वीं 70%+ (MP बोर्ड) या 85%+ (CBSE/ICSE)", "परिवार आय 6 लाख तक", "मान्यता प्राप्त कॉलेज में प्रवेश"],
            "en": ["MP domicile", "Class 12 70%+ (MP board) or 85%+ (CBSE/ICSE)", "Family income up to 6 lakh", "Admission in a recognised college"],
            "hinglish": ["MP domicile", "12th 70%+ (MP board) ya 85%+ (CBSE/ICSE)", "Parivar aay 6 lakh tak", "Recognised college me admission"],
        },
        "docs": {
            "hi": ["Domicile प्रमाणपत्र", "12वीं marksheet", "आय प्रमाणपत्र", "Aadhaar + bank खाता (DBT)"],
            "en": ["Domicile certificate", "Class 12 marksheet", "Income certificate", "Aadhaar + bank account (DBT)"],
            "hinglish": ["Domicile certificate", "12th marksheet", "Aay pramanpatra", "Aadhaar + bank khata (DBT)"],
        },
    },
    {
        "id": "gaon-ki-beti",
        "name": {"hi": "गाँव की बेटी योजना", "en": "Gaon Ki Beti Yojana", "hinglish": "Gaon Ki Beti Yojana"},
        "amount": {"hi": "₹500/माह (₹5,000/वर्ष)", "en": "₹500/month (₹5,000/year)", "hinglish": "₹500/mahina (₹5,000/saal)"},
        "portal": "highereducation.mp.gov.in",
        "criteria": {"min_class12_pct_any": 60, "domicile": "MP", "gender": "female", "rural": True},
        "need": {
            "hi": ["MP की ग्रामीण बेटी", "12वीं में 60%+", "UG में प्रवेश"],
            "en": ["Rural girl student of MP", "60%+ in Class 12", "Admission in UG"],
            "hinglish": ["MP ki grameen beti", "12th me 60%+", "UG me admission"],
        },
        "docs": {
            "hi": ["Domicile", "12वीं marksheet", "कॉलेज प्रवेश रसीद", "Aadhaar + bank खाता"],
            "en": ["Domicile", "Class 12 marksheet", "College admission receipt", "Aadhaar + bank account"],
            "hinglish": ["Domicile", "12th marksheet", "College admission receipt", "Aadhaar + bank khata"],
        },
    },
    {
        "id": "pratibha-kiran",
        "name": {"hi": "प्रतिभा किरण योजना", "en": "Pratibha Kiran Yojana", "hinglish": "Pratibha Kiran Yojana"},
        "amount": {"hi": "₹500/माह (शहरी बेटियाँ)", "en": "₹500/month (urban girls)", "hinglish": "₹500/mahina (shehri betiyan)"},
        "portal": "highereducation.mp.gov.in",
        "criteria": {"min_class12_pct_any": 60, "domicile": "MP", "gender": "female", "urban_bpl": True},
        "need": {
            "hi": ["शहर की BPL बेटी", "12वीं में 60%+", "UG में प्रवेश"],
            "en": ["Urban BPL girl student", "60%+ in Class 12", "Admission in UG"],
            "hinglish": ["Sheher ki BPL beti", "12th me 60%+", "UG me admission"],
        },
        "docs": {
            "hi": ["BPL कार्ड", "12वीं marksheet", "प्रवेश रसीद", "Aadhaar + bank खाता"],
            "en": ["BPL card", "Class 12 marksheet", "Admission receipt", "Aadhaar + bank account"],
            "hinglish": ["BPL card", "12th marksheet", "Admission receipt", "Aadhaar + bank khata"],
        },
    },
    {
        "id": "post-matric-sc",
        "name": {"hi": "पोस्ट-मैट्रिक छात्रवृत्ति (SC)", "en": "Post-Matric Scholarship (SC)", "hinglish": "Post-matric scholarship (SC)"},
        "amount": {"hi": "फीस + भत्ता (आय अनुसार)", "en": "Fees + allowance (as per income)", "hinglish": "Fees + bhatta (aay ke hisab se)"},
        "portal": "hescholarship.mp.gov.in",
        "criteria": {"domicile": "MP", "category": "SC", "max_income_lakh": 2.5},
        "need": {
            "hi": ["SC वर्ग", "10वीं के बाद पढ़ाई", "आय 2.5 लाख तक"],
            "en": ["SC category", "Studying after Class 10", "Income up to 2.5 lakh"],
            "hinglish": ["SC varg", "10th ke baad padhai", "Aay 2.5 lakh tak"],
        },
        "docs": {
            "hi": ["जाति प्रमाणपत्र", "आय प्रमाणपत्र", "Marksheet", "Aadhaar + bank खाता"],
            "en": ["Caste certificate", "Income certificate", "Marksheet", "Aadhaar + bank account"],
            "hinglish": ["Jaati pramanpatra", "Aay pramanpatra", "Marksheet", "Aadhaar + bank khata"],
        },
    },
    {
        "id": "post-matric-st",
        "name": {"hi": "पोस्ट-मैट्रिक छात्रवृत्ति (ST)", "en": "Post-Matric Scholarship (ST)", "hinglish": "Post-matric scholarship (ST)"},
        "amount": {"hi": "पूरी फीस (आय 2.5L तक), आधी (6L तक)", "en": "Full fees (income to 2.5L), half (to 6L)", "hinglish": "Poori fees (aay 2.5L tak), aadhi (6L tak)"},
        "portal": "hescholarship.mp.gov.in",
        "criteria": {"domicile": "MP", "category": "ST", "max_income_lakh": 6},
        "need": {
            "hi": ["ST वर्ग", "10वीं के बाद पढ़ाई", "आय 6 लाख तक"],
            "en": ["ST category", "Studying after Class 10", "Income up to 6 lakh"],
            "hinglish": ["ST varg", "10th ke baad padhai", "Aay 6 lakh tak"],
        },
        "docs": {
            "hi": ["जाति प्रमाणपत्र", "आय प्रमाणपत्र", "Marksheet", "Aadhaar + bank खाता"],
            "en": ["Caste certificate", "Income certificate", "Marksheet", "Aadhaar + bank account"],
            "hinglish": ["Jaati pramanpatra", "Aay pramanpatra", "Marksheet", "Aadhaar + bank khata"],
        },
    },
    {
        "id": "post-matric-obc",
        "name": {"hi": "पोस्ट-मैट्रिक छात्रवृत्ति (OBC)", "en": "Post-Matric Scholarship (OBC)", "hinglish": "Post-matric scholarship (OBC)"},
        "amount": {"hi": "पूरी (आय 75k तक), आधी (1L तक)", "en": "Full (income to 75k), half (to 1L)", "hinglish": "Poori (aay 75k tak), aadhi (1L tak)"},
        "portal": "hescholarship.mp.gov.in",
        "criteria": {"domicile": "MP", "category": "OBC", "max_income_lakh": 1},
        "need": {
            "hi": ["OBC वर्ग", "10वीं के बाद पढ़ाई", "आय 1 लाख तक"],
            "en": ["OBC category", "Studying after Class 10", "Income up to 1 lakh"],
            "hinglish": ["OBC varg", "10th ke baad padhai", "Aay 1 lakh tak"],
        },
        "docs": {
            "hi": ["जाति प्रमाणपत्र", "आय प्रमाणपत्र", "Marksheet", "Aadhaar + bank खाता"],
            "en": ["Caste certificate", "Income certificate", "Marksheet", "Aadhaar + bank account"],
            "hinglish": ["Jaati pramanpatra", "Aay pramanpatra", "Marksheet", "Aadhaar + bank khata"],
        },
    },
]

CAREERS = [
    {
        "id": "nursing",
        "title": {"hi": "B.Sc नर्सिंग", "en": "B.Sc Nursing", "hinglish": "B.Sc Nursing"},
        "fit": ["bio", "seva", "helping", "doctor", "hospital", "नर्स", "जीव"],
        "desc": {
            "hi": "अस्पताल और स्वास्थ्य सेवा में स्थिर करियर। 12वीं (Bio) + NEET/कॉलेज प्रवेश। अवधि 4 साल।",
            "en": "Stable career in hospitals and healthcare. Class 12 (Bio) + NEET/college admission. 4 years.",
            "hinglish": "Hospital aur health me stable career. 12th (Bio) + NEET/college admission. 4 saal.",
        },
    },
    {
        "id": "iti-electrician",
        "title": {"hi": "ITI इलेक्ट्रीशियन", "en": "ITI Electrician", "hinglish": "ITI Electrician"},
        "fit": ["bijli", "बिजली", "hand", "technical", "mistri", "machine", "मशीन", "job jaldi"],
        "desc": {
            "hi": "10वीं के बाद 2 साल का कोर्स। रेलवे, MPSEB, ठेकेदारी में काम। कम खर्च, जल्दी नौकरी।",
            "en": "2-year course after Class 10. Work in railways, MPSEB, contracting. Low cost, quick job.",
            "hinglish": "10th ke baad 2 saal ka course. Railway, MPSEB, thekedari me kaam. Kam kharch, jaldi naukri.",
        },
    },
    {
        "id": "teacher",
        "title": {"hi": "शिक्षक (D.El.Ed)", "en": "Teacher (D.El.Ed)", "hinglish": "Shikshak (D.El.Ed)"},
        "fit": ["padhana", "पढ़ाना", "teacher", "school", "स्कूल", "bachche", "बच्चे"],
        "desc": {
            "hi": "12वीं के बाद 2 साल D.El.Ed। प्राइमरी शिक्षक भर्ती (MPTET) की तैयारी।",
            "en": "2-year D.El.Ed after Class 12. Prepare for primary teacher recruitment (MPTET).",
            "hinglish": "12th ke baad 2 saal D.El.Ed. Primary teacher bharti (MPTET) ki taiyari.",
        },
    },
    {
        "id": "polytechnic",
        "title": {"hi": "पॉलिटेक्निक डिप्लोमा", "en": "Polytechnic Diploma", "hinglish": "Polytechnic Diploma"},
        "fit": ["diploma", "डिप्लोमा", "engineering", "इंजीनियर", "civil", "mechanical", "technical"],
        "desc": {
            "hi": "10वीं के बाद 3 साल। सिविल/मैकेनिकल/इलेक्ट्रिकल। JE भर्ती और लेटरल B.Tech का रास्ता।",
            "en": "3 years after Class 10. Civil/mechanical/electrical. Path to JE jobs and lateral B.Tech.",
            "hinglish": "10th ke baad 3 saal. Civil/mechanical/electrical. JE bharti aur lateral B.Tech ka rasta.",
        },
    },
    {
        "id": "agri",
        "title": {"hi": "B.Sc कृषि", "en": "B.Sc Agriculture", "hinglish": "B.Sc Krishi"},
        "fit": ["kheti", "खेती", "kisan", "किसान", "agri", "fasal", "फसल", "gaon"],
        "desc": {
            "hi": "खेती परिवारों के लिए सबसे काम का कोर्स। PAT परीक्षा से प्रवेश। सरकारी कृषि अधिकारी का रास्ता।",
            "en": "Most useful course for farming families. Admission via PAT exam. Path to govt agriculture officer.",
            "hinglish": "Kheti parivaron ke liye sabse kaam ka course. PAT exam se admission. Sarkari krishi adhikari ka rasta.",
        },
    },
    {
        "id": "bsc-ba",
        "title": {"hi": "B.A./B.Sc. + प्रतियोगी परीक्षा", "en": "B.A./B.Sc. + Competitive exams", "hinglish": "B.A./B.Sc. + Competitive exam"},
        "fit": ["sarkari", "सरकारी", "upsc", "mppsc", "ssc", "police", "पुलिस", "patwari", "पटवारी"],
        "desc": {
            "hi": "ग्रेजुएशन के साथ MPPSC, SSC, पुलिस, पटवारी की तैयारी। सबसे कम खर्च वाला रास्ता।",
            "en": "Graduation alongside MPPSC, SSC, police, patwari prep. Lowest-cost path.",
            "hinglish": "Graduation ke saath MPPSC, SSC, police, patwari ki taiyari. Sabse kam kharch wala rasta.",
        },
    },
]

MENTORS = [
    {"id": "m1", "name": "Sunita Verma", "role_hi": "B.Sc नर्सिंग, भोपाल", "role_en": "B.Sc Nursing, Bhopal", "tags": ["nursing", "bio", "girl"]},
    {"id": "m2", "name": "Ravi Uikey", "role_hi": "ITI इलेक्ट्रीशियन, छिंदवाड़ा", "role_en": "ITI Electrician, Chhindwara", "tags": ["iti", "technical", "tribal"]},
    {"id": "m3", "name": "Pooja Maravi", "role_hi": "प्राइमरी शिक्षक, मंडला", "role_en": "Primary teacher, Mandla", "tags": ["teacher", "tribal", "girl"]},
]
