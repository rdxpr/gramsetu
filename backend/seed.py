"""Seed content for GramSetu MVP.

Seed courses, lessons, and FAQs in Hindi, English, and Hinglish so the
offline-first frontend can ship with real demo content. Lessons are plain
text, small enough to sync over low bandwidth and cache in localStorage.
"""

COURSES = [
    {
        "id": "c1",
        "title": {"hi": "कक्षा 9 विज्ञान: गति", "en": "Class 9 Science: Motion", "hinglish": "Class 9 Science: Gati"},
        "subject": {"hi": "भौतिकी", "en": "Physics", "hinglish": "Physics"},
        "level": "9",
        "desc": {
            "hi": "NCERT आधारित पूरा अध्याय: दूरी, वेग, त्वरण, ग्राफ, गति के समीकरण और 7 पाठों में अभ्यास।",
            "en": "Full NCERT-based chapter: distance, velocity, acceleration, graphs, equations of motion in 7 lessons with practice.",
            "hinglish": "Poora NCERT-based chapter: doori, veg, tvaran, graph, gati ke samikaran, 7 lesson me practice ke saath.",
        },
        "lessons": [
            {
                "id": "c1l1",
                "title": {"hi": "गति और संदर्भ बिंदु", "en": "Motion and reference point", "hinglish": "Gati aur reference point"},
                "minutes": 8,
                "size_kb": 9,
                "body": {
                    "hi": "गति का मतलब है समय के साथ जगह बदलना। जगह बताने के लिए एक स्थिर बिंदु चाहिए, उसे मूलबिंदु कहते हैं। बस में बैठे यात्री को साथ वाला स्थिर लगता है, पर बाहर खड़े व्यक्ति को वही यात्री चलता दिखता है। इसलिए गति हमेशा संदर्भ के हिसाब से बताई जाती है। गति तीन तरह की होती है: सीधी रेखा में जैसे रेल, गोल घेरे में जैसे पंखा, और झूले जैसी दोलन गति। जो वस्तु जगह न बदले वह विराम में कहलाती है।",
                    "en": "Motion means changing position with time. To tell position we need a fixed reference point or origin. A passenger in a bus looks still to a fellow passenger but moving to a person outside. So motion is always told with a reference. There are three common types: straight line like a train, circular like a fan blade, and swinging like a jhula. An object that does not change place is at rest.",
                    "hinglish": "Gati ka matlab hai samay ke saath jagah badalna. Jagah batane ke liye ek fixed reference point chahiye. Bus me baitha yatri saath wale ko sthir lagta hai, par bahar khade aadmi ko wahi yatri chalta dikhta hai. Isliye gati hamesha reference ke hisab se batai jaati hai. Teen aam prakar: seedhi rekha jaise rail, gol ghumav jaise pankha, aur jhoole jaisi dolan gati. Jo vastu jagah na badle use viram me kehte hain.",
                },
            },
            {
                "id": "c1l2",
                "title": {"hi": "दूरी और विस्थापन", "en": "Distance and displacement", "hinglish": "Doori aur visthapan"},
                "minutes": 9,
                "size_kb": 10,
                "body": {
                    "hi": "दूरी वह पूरा रास्ता है जो वस्तु चलती है। इसमें दिशा नहीं होती, इसलिए यह अदिश राशि है। विस्थापन शुरू और आखिरी बिंदु के बीच की सबसे छोटी सीधी दूरी है, दिशा के साथ। इसलिए यह सदिश राशि है। उदाहरण: घर से स्कूल घूमकर 2 किमी गए और सीधी दूरी 1.2 किमी है, तो दूरी 2 किमी और विस्थापन 1.2 किमी स्कूल की ओर। गोल चक्कर लगाकर वापस आने पर दूरी कुछ होगी पर विस्थापन शून्य होगा। दूरी कभी शून्य नहीं होती, विस्थापन हो सकता है।",
                    "en": "Distance is the full path an object walks. It has no direction, so it is a scalar. Displacement is the shortest straight line from start to end, with direction, so it is a vector. Example: you walk 2 km to school by a long road but the straight gap is 1.2 km, so distance is 2 km and displacement is 1.2 km toward school. If you walk a full circle back home, distance is something but displacement is zero. Distance is never zero, displacement can be.",
                    "hinglish": "Doori wo poora rasta hai jo vastu chalti hai. Isme disha nahi hoti, isliye ye scalar hai. Visthapan shuru aur aakhiri point ke beech sabse chhoti seedhi doori hai, disha ke saath, isliye ye vector hai. Example: ghar se school ghoomkar 2 km gaye aur seedhi doori 1.2 km hai, to doori 2 km aur visthapan 1.2 km school ki taraf. Gol chakkar lagakar wapas aane par doori kuch hogi par visthapan zero hoga. Doori kabhi zero nahi hoti, visthapan ho sakta hai.",
                },
            },
            {
                "id": "c1l3",
                "title": {"hi": "चाल और वेग", "en": "Speed and velocity", "hinglish": "Chaal aur veg"},
                "minutes": 10,
                "size_kb": 11,
                "body": {
                    "hi": "चाल बराबर दूरी भाग समय। इकाई मी/से या किमी/घंटा। औसत चाल बराबर कुल दूरी भाग कुल समय। उदाहरण: बस 2 घंटे में 120 किमी चली तो औसत चाल 60 किमी/घंटा। एक समान गति में वस्तु बराबर समय में बराबर दूरी चलती है, जैसे बिना रुके पंखा। असमान गति में बराबर समय में अलग दूरी, जैसे भीड़ में बस। वेग बराबर विस्थापन भाग समय, इसमें दिशा भी बतानी पड़ती है। औसत वेग बराबर शुरू और आखिरी वेग का औसत। वेग का स्पीडोमीटर जैसा हर पल का मान तात्क्षणिक वेग कहलाता है।",
                    "en": "Speed equals distance divided by time. Unit is m/s or km/h. Average speed equals total distance divided by total time. Example: a bus covers 120 km in 2 hours, so average speed is 60 km/h. In uniform motion the object covers equal gaps in equal time, like a steady fan. In non-uniform motion gaps differ, like a bus in traffic. Velocity equals displacement divided by time, with direction. Average velocity is the mean of start and end velocity. The value at one instant, as on a speedometer, is called instantaneous velocity.",
                    "hinglish": "Chaal barabar doori divided by samay. Unit m/s ya km/h. Ausat chaal barabar kul doori divided by kul samay. Example: bus 2 ghante me 120 km chali to ausat chaal 60 km/h. Ek samaan gati me vastu barabar samay me barabar doori chalti hai, jaise steady pankha. Asamaan gati me barabar samay me alag doori, jaise bheed me bus. Veg barabar visthapan divided by samay, isme disha bhi batani padti hai. Ausat veg shuru aur aakhiri veg ka ausat hai. Har pal ka maan, jaise speedometer par, tatkshanik veg kehlata hai.",
                },
            },
            {
                "id": "c1l4",
                "title": {"hi": "त्वरण", "en": "Acceleration", "hinglish": "Tvaran"},
                "minutes": 9,
                "size_kb": 10,
                "body": {
                    "hi": "वेग के बदलने की दर को त्वरण कहते हैं। सूत्र: त्वरण बराबर आखिरी वेग घटा शुरू वेग, भाग समय। इकाई मी/से2। उदाहरण: कार 0 से 20 मी/से 5 सेकंड में पकड़े तो त्वरण 4 मी/से2। जब वेग बढ़े तो धन त्वरण, घटे तो मंदन। एक समान त्वरण में हर सेकंड बराबर बढ़त होती है। असमान गति में वेग हर पल बदलता है, इसलिए त्वरण भी बदलता है। दिशा बदलने से भी त्वरण पैदा होता है, जैसे गोल घूमती गेंद।",
                    "en": "The rate of change of velocity is called acceleration. Formula: acceleration equals final velocity minus initial velocity, divided by time. Unit is m/s2. Example: a car goes from 0 to 20 m/s in 5 seconds, so acceleration is 4 m/s2. Rising velocity is positive acceleration, falling velocity is retardation. In uniform acceleration the rise is equal every second. In non-uniform motion velocity changes each moment, so acceleration also changes. Even a change of direction alone makes acceleration, like a ball going in a circle.",
                    "hinglish": "Veg ke badalne ki dar ko tvaran kehte hain. Sutra: tvaran barabar aakhiri veg minus shuru veg, divided by samay. Unit m/s2. Example: car 0 se 20 m/s 5 second me pakde to tvaran 4 m/s2. Veg badhe to dhana tvaran, ghate to mandan. Ek samaan tvaran me har second barabar badhat hoti hai. Asamaan gati me veg har pal badalta hai, isliye tvaran bhi badalta hai. Disha badalne se bhi tvaran banta hai, jaise gol ghoomti gend.",
                },
            },
            {
                "id": "c1l5",
                "title": {"hi": "गति के ग्राफ", "en": "Graphs of motion", "hinglish": "Gati ke graph"},
                "minutes": 11,
                "size_kb": 12,
                "body": {
                    "hi": "दूरी समय ग्राफ में समय नीचे और दूरी ऊपर लेते हैं। सीधी चढ़ती रेखा का मतलब एक समान गति, ढलान से चाल मिलती है। समतल रेखा का मतलब वस्तु रुकी है। टेढ़ी मेढ़ी रेखा असमान गति दिखाती है। वेग समय ग्राफ में ढलान से त्वरण मिलता है और रेखा के नीचे का क्षेत्रफल विस्थापन देता है। इसमें ऊपर चढ़ती रेखा तेज होती गाड़ी, समतल रेखा एक समान वेग, और नीचे उतरती रेखा मंदन दिखाती है। ग्राफ देखकर पूरी यात्रा एक नजर में समझ आती है।",
                    "en": "In a distance time graph time is below and distance is above. A straight rising line means uniform motion, and the slope gives speed. A flat line means the object is resting. A curvy line shows non-uniform motion. In a velocity time graph the slope gives acceleration and the area under the line gives displacement. Here a rising line is a speeding car, a flat line is uniform velocity, and a falling line is retardation. One look at the graph tells the full journey.",
                    "hinglish": "Doori samay graph me samay neeche aur doori upar lete hain. Seedhi chadhti rekha ka matlab ek samaan gati, dhalan se chaal milti hai. Samtal rekha ka matlab vastu ruki hai. Tedhi medhi rekha asamaan gati dikhati hai. Veg samay graph me dhalan se tvaran milta hai aur rekha ke neeche ka kshetrafal visthapan deta hai. Isme upar chadhti rekha tez hoti gaadi, samtal rekha ek samaan veg, aur neeche utarti rekha mandan dikhati hai. Graph dekhkar poori yatra ek nazar me samajh aati hai.",
                },
            },
            {
                "id": "c1l6",
                "title": {"hi": "गति के समीकरण", "en": "Equations of motion", "hinglish": "Gati ke samikaran"},
                "minutes": 12,
                "size_kb": 12,
                "body": {
                    "hi": "एक समान त्वरण वाली गति तीन समीकरणों से बताई जाती है। पहला: आखिरी वेग बराबर शुरू वेग जमा त्वरण गुणा समय। दूसरा: दूरी बराबर शुरू वेग गुणा समय जमा आधा गुणा त्वरण गुणा समय2। तीसरा: आखिरी वेग2 घटा शुरू वेग2 बराबर 2 गुणा त्वरण गुणा दूरी। हल: कार शुरू वेग 5, त्वरण 2, समय 4 सेकंड तो आखिरी वेग 5 जमा 8 बराबर 13 मी/से। दूसरा हल: शुरू वेग 0, त्वरण 2, समय 3 तो दूरी 0 जमा 9 बराबर 9 मी। पहले सूत्र याद करो, फिर मान रखकर हल करो।",
                    "en": "Motion with uniform acceleration follows three equations. First: final velocity equals initial velocity plus acceleration times time. Second: distance equals initial velocity times time plus half times acceleration times time2. Third: final velocity2 minus initial velocity2 equals 2 times acceleration times distance. Solved 1: car starts at 5, acceleration 2, time 4, so final is 5 plus 8 equals 13 m/s. Solved 2: start 0, acceleration 2, time 3, so distance is 0 plus 9 equals 9 m. Remember the first formula, then put values and solve.",
                    "hinglish": "Ek samaan tvaran wali gati teen samikaran se batai jaati hai. Pehla: aakhiri veg barabar shuru veg plus tvaran guna samay. Doosra: doori barabar shuru veg guna samay plus aadha guna tvaran guna samay2. Teesra: aakhiri veg2 minus shuru veg2 barabar 2 guna tvaran guna doori. Hal 1: car shuru veg 5, tvaran 2, samay 4, to aakhiri veg 5 plus 8 barabar 13 m/s. Hal 2: shuru 0, tvaran 2, samay 3, to doori 0 plus 9 barabar 9 m. Pehle sutra yaad karo, phir maan rakhkar hal karo.",
                },
            },
            {
                "id": "c1l7",
                "title": {"hi": "गोल गति और अभ्यास", "en": "Circular motion and practice", "hinglish": "Gol gati aur abhyas"},
                "minutes": 12,
                "size_kb": 11,
                "body": {
                    "hi": "गोल रास्ते पर एक समान चाल से चलना एक समान गोल गति कहलाता है। चाल एक सी रहती है पर दिशा हर पल बदलती है, इसलिए वेग बदलता है और त्वरण बना रहता है। उदाहरण: पृथ्वी के घूमते उपग्रह, घड़ी की सुई की नोक, पवनचक्की की ब्लेड। अभ्यास: 1. दूरी और विस्थापन में दो अंतर लिखो। 2. बस 120 किमी 2 घंटे में, औसत चाल निकालो। 3. शुरू वेग 10, त्वरण 3, समय 5, आखिरी वेग निकालो। 4. दूरी समय ग्राफ में समतल रेखा का क्या मतलब है। उत्तर: 60 किमी/घंटा, 25 मी/से, वस्तु विराम में।",
                    "en": "Moving on a circular path with steady speed is called uniform circular motion. Speed stays same but direction changes each moment, so velocity changes and acceleration stays. Examples: satellites around earth, tip of a watch needle, windmill blades. Practice: 1. Write two differences between distance and displacement. 2. A bus covers 120 km in 2 hours, find average speed. 3. Start 10, acceleration 3, time 5, find final velocity. 4. What does a flat line mean in a distance time graph. Answers: 60 km/h, 25 m/s, object at rest.",
                    "hinglish": "Gol raste par ek samaan chaal se chalna ek samaan gol gati kehlata hai. Chaal ek si rehti hai par disha har pal badalti hai, isliye veg badalta hai aur tvaran bana rehta hai. Example: prithvi ke ghoomte upagrah, ghadi ki sui ki nok, pavanchakki ki blade. Abhyas: 1. Doori aur visthapan me do antar likho. 2. Bus 120 km 2 ghante me, ausat chaal nikalo. 3. Shuru veg 10, tvaran 3, samay 5, aakhiri veg nikalo. 4. Doori samay graph me samtal rekha ka kya matlab. Uttar: 60 km/h, 25 m/s, vastu viram me.",
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

# Takeaway points per lesson (trilingual). Shown in the immersive lesson
# viewer under "Yaad rakho". Still plain text, still tiny.
POINTS = {
    "c1l1": {
        "hi": ["Gati hamesha reference point se batao", "Bus wala andar sthir, bahar se chalti dikhti hai", "Teen prakar: seedhi, gol, dolan"],
        "en": ["Always tell motion with a reference point", "Bus looks still inside, moving from outside", "Three types: straight, circular, swinging"],
        "hinglish": ["Gati hamesha reference point se batao", "Bus andar sthir, bahar se chalti", "Teen prakar: seedhi, gol, dolan"],
    },
    "c1l2": {
        "hi": ["Doori poora rasta, visthapan seedhi doori disha ke saath", "Wapas aane par visthapan zero ho sakta hai", "Doori scalar, visthapan vector"],
        "en": ["Distance is full path, displacement is straight gap with direction", "Coming back can make displacement zero", "Distance is scalar, displacement is vector"],
        "hinglish": ["Doori poora rasta, visthapan seedhi doori disha ke saath", "Wapas aane par visthapan zero", "Doori scalar, visthapan vector"],
    },
    "c1l3": {
        "hi": ["Chaal me disha nahi, veg me hoti hai", "120 km in 2 ghante equals 60 km/h", "Pankha samaan, bheed wali bus asamaan gati"],
        "en": ["Speed has no direction, velocity has", "120 km in 2 hours equals 60 km/h", "Fan is uniform, bus in traffic is not"],
        "hinglish": ["Chaal me disha nahi, veg me hoti hai", "120 km in 2 ghante equals 60 km/h", "Pankha samaan, bheed bus asamaan"],
    },
    "c1l4": {
        "hi": ["Tvaran equals veg badlav divided by samay", "0 se 20 in 5 second equals 4 m/s2", "Disha badalne se bhi tvaran banta hai"],
        "en": ["Acceleration equals velocity change divided by time", "0 to 20 in 5 seconds equals 4 m/s2", "Direction change alone makes acceleration"],
        "hinglish": ["Tvaran equals veg badlav divided by samay", "0 se 20 in 5 second equals 4 m/s2", "Disha badle to bhi tvaran"],
    },
    "c1l5": {
        "hi": ["Doori graph me dhalan se chaal milti hai", "Samtal rekha ka matlab viram", "Veg graph ke neeche kshetra equals visthapan"],
        "en": ["Distance graph slope gives speed", "Flat line means rest", "Area under velocity graph equals displacement"],
        "hinglish": ["Doori graph dhalan se chaal", "Samtal rekha equals viram", "Veg graph neeche kshetra equals visthapan"],
    },
    "c1l6": {
        "hi": ["Pehla samikaran: aakhiri veg equals shuru plus tvaran guna samay", "5 plus 8 equals 13 m/s wala hal yaad karo", "Pehle sutra, phir maan rakho"],
        "en": ["First equation: final equals start plus acceleration times time", "Remember the 5 plus 8 equals 13 m/s sum", "Formula first, values after"],
        "hinglish": ["Pehla samikaran: aakhiri equals shuru plus tvaran guna samay", "5 plus 8 equals 13 m/s yaad karo", "Pehle sutra, phir maan"],
    },
    "c1l7": {
        "hi": ["Gol gati me chaal same, disha badle, tvaran bane", "60 km/h aur 25 m/s wale hal khud karo", "Samtal graph rekha equals viram"],
        "en": ["In circular motion speed same, direction changes, acceleration stays", "Do the 60 km/h and 25 m/s sums yourself", "Flat graph line equals rest"],
        "hinglish": ["Gol gati me chaal same, disha badle, tvaran bane", "60 km/h aur 25 m/s khud hal karo", "Samtal rekha equals viram"],
    },
    "c2l1": {
        "hi": ["Dono taraf same kriya karo", "2x plus 3 equals 11 me x equals 4", "Jawab rakhkar janch karo"],
        "en": ["Do the same step on both sides", "In 2x plus 3 equals 11, x equals 4", "Check by putting the answer back"],
        "hinglish": ["Dono taraf same step karo", "2x plus 3 equals 11 me x equals 4", "Jawab rakhkar check karo"],
    },
    "c2l2": {
        "hi": ["Pehle gunankhand dhoondo", "Factors se x equals 2 ya 3", "Sutra bhi kaam karta hai"],
        "en": ["Try factors first", "Factors give x equals 2 or 3", "The formula works too"],
        "hinglish": ["Pehle gunankhand try karo", "Factors se x equals 2 ya 3", "Formula bhi kaam karta hai"],
    },
    "c3l1": {
        "hi": ["My name is se shuru karo", "Gaon ka naam jodo", "Roz ek baar zor se bolo"],
        "en": ["Start with My name is", "Add your village name", "Say it aloud once daily"],
        "hinglish": ["My name is se start karo", "Gaon ka naam jodo", "Roz ek baar zor se bolo"],
    },
    "c3l2": {
        "hi": ["How much is this puchho", "Daam zyada lage to Too costly kaho", "Muskurakar baat karo"],
        "en": ["Ask How much is this", "Say Too costly if the price is high", "Speak with a smile"],
        "hinglish": ["How much is this puchho", "Daam zyada ho to Too costly kaho", "Muskurakar baat karo"],
    },
}
