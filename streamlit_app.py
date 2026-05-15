import streamlit as st
from datetime import datetime

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="INVESMATE",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# SESSION STATE
# =========================================================

if "theme" not in st.session_state:
    st.session_state.theme = "Light"

if "language" not in st.session_state:
    st.session_state.language = "English"

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi 👋 I am your INVESMATE AI Advisor. Ask me about courses, pricing, INSIGNIA mentorship, enrollment, support, or course comparison."
        }
    ]

# =========================================================
# THEME
# =========================================================

LIGHT_THEME = """
<style>

html, body, [class*="css"]{
    font-family: 'Arial', sans-serif;
}

.stApp{
    background:#fafaf8;
    color:#1a1208;
}

.hero{
    background:linear-gradient(135deg,#fff7ed,#ffffff);
    border:1px solid #e6e0d4;
    padding:55px;
    border-radius:30px;
}

.hero h1{
    font-size:64px;
    font-weight:900;
    line-height:1;
    color:#1a1208;
}

.hero h1 span{
    color:#d4601a;
}

.hero p{
    color:#6b6150;
    font-size:18px;
    line-height:1.8;
}

.badge{
    background:#fff3ea;
    color:#d4601a;
    padding:8px 14px;
    border-radius:999px;
    display:inline-block;
    font-size:13px;
    font-weight:700;
}

.card{
    background:white;
    border:1px solid #e6e0d4;
    border-radius:24px;
    padding:24px;
    height:100%;
    box-shadow:0 8px 24px rgba(0,0,0,0.06);
}

.card h3{
    margin-top:0;
}

.price{
    color:#d4601a;
    font-weight:800;
    font-size:20px;
}

.chip{
    background:#f5f3ee;
    border-radius:999px;
    padding:6px 12px;
    display:inline-block;
    margin:4px;
    font-size:12px;
}

.footer{
    background:#1a1208;
    color:rgba(255,255,255,0.75);
    padding:35px;
    border-radius:26px;
    text-align:center;
}

</style>
"""

DARK_THEME = """
<style>

html, body, [class*="css"]{
    font-family: 'Arial', sans-serif;
}

.stApp{
    background:#0e1117;
    color:white;
}

.hero{
    background:linear-gradient(135deg,#111827,#1f2937);
    border:1px solid #374151;
    padding:55px;
    border-radius:30px;
}

.hero h1{
    font-size:64px;
    font-weight:900;
    line-height:1;
    color:white;
}

.hero h1 span{
    color:#f59e0b;
}

.hero p{
    color:#d1d5db;
    font-size:18px;
    line-height:1.8;
}

.badge{
    background:#1f2937;
    color:#f59e0b;
    padding:8px 14px;
    border-radius:999px;
    display:inline-block;
    font-size:13px;
    font-weight:700;
}

.card{
    background:#111827;
    border:1px solid #374151;
    border-radius:24px;
    padding:24px;
    height:100%;
}

.price{
    color:#f59e0b;
    font-weight:800;
    font-size:20px;
}

.chip{
    background:#1f2937;
    border-radius:999px;
    padding:6px 12px;
    display:inline-block;
    margin:4px;
    font-size:12px;
}

.footer{
    background:#111827;
    color:#d1d5db;
    padding:35px;
    border-radius:26px;
    text-align:center;
}

</style>
"""

if st.session_state.theme == "Light":
    st.markdown(LIGHT_THEME, unsafe_allow_html=True)
else:
    st.markdown(DARK_THEME, unsafe_allow_html=True)

# =========================================================
# LANGUAGE TRANSLATIONS
# =========================================================

LANG = {
    "English": {
        "title": "Finest Stock Market Learning Experience",
        "sub": "Professional stock market learning with AI-guided mentorship.",
        "products": "Products",
        "insignia": "INSIGNIA",
        "mentors": "Mentors",
        "support": "Support",
        "advisor": "AI Advisor",
    },
    "Hindi": {
        "title": "सर्वश्रेष्ठ स्टॉक मार्केट लर्निंग अनुभव",
        "sub": "AI आधारित मार्गदर्शन के साथ प्रोफेशनल स्टॉक मार्केट शिक्षा।",
        "products": "कोर्स",
        "insignia": "इंसिग्निया",
        "mentors": "मेंटर्स",
        "support": "सपोर्ट",
        "advisor": "AI सलाहकार",
    },
    "Bengali": {
        "title": "সেরা স্টক মার্কেট লার্নিং অভিজ্ঞতা",
        "sub": "AI গাইডেড প্রফেশনাল স্টক মার্কেট শিক্ষা।",
        "products": "কোর্স",
        "insignia": "ইনসিগনিয়া",
        "mentors": "মেন্টর",
        "support": "সাপোর্ট",
        "advisor": "AI উপদেষ্টা",
    },
    "Odia": {
        "title": "ସର୍ବଶ୍ରେଷ୍ଠ ଷ୍ଟକ୍ ମାର୍କେଟ ଲର୍ଣ୍ଣିଂ ଅନୁଭବ",
        "sub": "AI ଗାଇଡେଡ୍ ପ୍ରଫେସନାଲ ଷ୍ଟକ୍ ମାର୍କେଟ ଶିକ୍ଷା।",
        "products": "କୋର୍ସ",
        "insignia": "ଇନସିଗ୍ନିଆ",
        "mentors": "ମେଣ୍ଟର",
        "support": "ସପୋର୍ଟ",
        "advisor": "AI ଉପଦେଷ୍ଟା",
    }
}

T = LANG[st.session_state.language]

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("INVESMATE")

    st.session_state.language = st.selectbox(
        "Language",
        ["English", "Hindi", "Bengali", "Odia"],
        index=["English", "Hindi", "Bengali", "Odia"].index(st.session_state.language)
    )

    st.session_state.theme = st.selectbox(
        "Theme",
        ["Light", "Dark"],
        index=["Light", "Dark"].index(st.session_state.theme)
    )

    page = st.radio(
        "Navigate",
        [
            "Home",
            "Products",
            "INSIGNIA",
            "Course Compare",
            "Mentors",
            "Support",
            "AI Advisor"
        ]
    )

# =========================================================
# DATA
# =========================================================

PRODUCTS = [
    {
        "title":"Power of Trading and Investing Combo Course",
        "category":"Beginner",
        "price":"Rs. 8,999 - 11,999",
        "duration":"2 Months",
        "desc":"Complete trading and investing roadmap.",
        "modules":["Technical","Fundamental","Risk","Practical"]
    },
    {
        "title":"Complete Intraday and Swing Trading Strategies",
        "category":"Technical",
        "price":"Rs. 9,999 - 12,999",
        "duration":"2 Months",
        "desc":"Advanced intraday and swing trading.",
        "modules":["SMC","Indicators","Price Action","Risk"]
    },
    {
        "title":"Complete Future and Option Trading Strategies",
        "category":"Derivatives",
        "price":"Rs. 12,999 - 15,999",
        "duration":"2 Months",
        "desc":"Advanced options and futures training.",
        "modules":["Options","Greeks","Hedging","Futures"]
    },
    {
        "title":"Value Investing Using Advanced Fundamental Analysis",
        "category":"Investing",
        "price":"Rs. 8,999 - 11,999",
        "duration":"2 Months",
        "desc":"Long-term investing and valuation.",
        "modules":["Valuation","Financials","Business","Portfolio"]
    }
]

INSIGNIA = [
    {
        "title":"Equity Market Intelligence Matrix",
        "price":"Rs. 38,571",
        "duration":"3-5 Months",
        "desc":"Premium mentorship with technical and fundamental analysis."
    },
    {
        "title":"Complete Equity and Derivative Dynasty",
        "price":"Rs. 62,305",
        "duration":"6-8 Months",
        "desc":"Advanced derivatives and technical mentorship."
    },
    {
        "title":"Complete Global Capital Market Specialist",
        "price":"Rs. 1,07,689",
        "duration":"12 Months",
        "desc":"Global capital market specialist program."
    }
]

MENTORS = [
    "Arunava Chatterjee",
    "Sayan Ghosh",
    "Kunal Saha",
    "Suman Goswami",
    "Laboni Pallab Das",
    "Debarati Mukherjee",
    "Pratim Kumar Chakraborty",
    "Mihir Kanti Chakraborty"
]

# =========================================================
# HELPERS
# =========================================================

def card(product):

    chips = ""

    for m in product["modules"]:
        chips += f"<span class='chip'>{m}</span>"

    return f"""
    <div class='card'>
        <div class='badge'>{product["category"]}</div>
        <h3>{product["title"]}</h3>
        <p>{product["desc"]}</p>

        <p class='price'>{product["price"]}</p>

        <p>{product["duration"]}</p>

        <div>{chips}</div>
    </div>
    """

def insignia_card(item):

    return f"""
    <div class='card'>
        <div class='badge'>Premium Mentorship</div>

        <h3>{item["title"]}</h3>

        <p>{item["desc"]}</p>

        <p class='price'>{item["price"]}</p>

        <p>{item["duration"]}</p>
    </div>
    """

def advisor_response(prompt):

    p = prompt.lower()

    if "beginner" in p:
        return "Recommended: Power of Trading and Investing Combo Course."

    if "option" in p or "future" in p:
        return "Recommended: Complete Future and Option Trading Strategies."

    if "intraday" in p or "swing" in p:
        return "Recommended: Complete Intraday and Swing Trading Strategies."

    if "invest" in p or "fundamental" in p:
        return "Recommended: Value Investing Using Advanced Fundamental Analysis."

    if "insignia" in p:
        return "INSIGNIA is INVESMATE's premium mentorship ecosystem."

    if "mentor" in p:
        return "INVESMATE mentors include Arunava Chatterjee, Sayan Ghosh, Kunal Saha, and more."

    if "support" in p or "contact" in p:
        return "Call +91 9016791791 or mail support@invesmate.com."

    if "price" in p:
        return "Courses start from Rs. 3,999 and INSIGNIA starts from Rs. 38,571."

    return "Please tell me your goal, experience, and budget for better recommendation."

# =========================================================
# HOME
# =========================================================

if page == "Home":

    st.markdown(f"""
    <div class='hero'>

        <div class='badge'>
        SEBI Registered RA: INH000017985
        </div>

        <h1>
        {T["title"].split()[0]}
        <span>Learning</span>
        Experience
        </h1>

        <p>
        {T["sub"]}
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("Courses","20+")
    c2.metric("Mentors","8")
    c3.metric("Language","4")
    c4.metric("SEBI","Registered")

# =========================================================
# PRODUCTS
# =========================================================

elif page == "Products":

    st.title(T["products"])

    search = st.text_input("Search Courses")

    cols = st.columns(2)

    filtered = PRODUCTS

    if search:
        filtered = [
            p for p in PRODUCTS
            if search.lower() in p["title"].lower()
        ]

    for i, product in enumerate(filtered):

        with cols[i % 2]:
            st.markdown(card(product), unsafe_allow_html=True)

# =========================================================
# INSIGNIA
# =========================================================

elif page == "INSIGNIA":

    st.title(T["insignia"])

    cols = st.columns(3)

    for i, item in enumerate(INSIGNIA):

        with cols[i]:
            st.markdown(insignia_card(item), unsafe_allow_html=True)

# =========================================================
# COURSE COMPARE
# =========================================================

elif page == "Course Compare":

    st.title("Course Compare")

    c1,c2 = st.columns(2)

    titles = [p["title"] for p in PRODUCTS]

    with c1:
        course1 = st.selectbox("Select Course 1", titles)

    with c2:
        course2 = st.selectbox("Select Course 2", titles, index=1)

    p1 = next(x for x in PRODUCTS if x["title"] == course1)
    p2 = next(x for x in PRODUCTS if x["title"] == course2)

    col1,col2 = st.columns(2)

    with col1:
        st.markdown(card(p1), unsafe_allow_html=True)

    with col2:
        st.markdown(card(p2), unsafe_allow_html=True)

# =========================================================
# MENTORS
# =========================================================

elif page == "Mentors":

    st.title(T["mentors"])

    cols = st.columns(4)

    for i, mentor in enumerate(MENTORS):

        initials = "".join([x[0] for x in mentor.split()[:2]])

        with cols[i % 4]:

            st.markdown(f"""
            <div class='card' style='text-align:center;'>

            <div style='
            width:70px;
            height:70px;
            border-radius:20px;
            background:linear-gradient(135deg,#d4601a,#f59e0b);
            margin:auto;
            color:white;
            font-weight:800;
            display:flex;
            align-items:center;
            justify-content:center;
            font-size:24px;
            '>
            {initials}
            </div>

            <h3>{mentor}</h3>

            <p>Capital Market Mentor</p>

            </div>
            """, unsafe_allow_html=True)

# =========================================================
# SUPPORT
# =========================================================

elif page == "Support":

    st.title(T["support"])

    c1,c2 = st.columns(2)

    with c1:

        st.markdown("""
        <div class='card'>

        <h3>Contact Team</h3>

        <p>📞 +91 9016791791</p>
        <p>📞 +91 7596037781</p>
        <p>📞 +91 7003110622</p>

        <br>

        <p>✉️ support@invesmate.com</p>

        </div>
        """, unsafe_allow_html=True)

    with c2:

        st.markdown("""
        <div class='card'>

        <h3>Disclaimer</h3>

        <p>
        Investment in securities markets are subject to market risks.
        </p>

        </div>
        """, unsafe_allow_html=True)

# =========================================================
# AI ADVISOR
# =========================================================

elif page == "AI Advisor":

    st.title(T["advisor"])

    st.subheader("AI Course Predictor")

    c1,c2,c3 = st.columns(3)

    with c1:
        goal = st.selectbox(
            "Goal",
            [
                "Beginner",
                "Intraday",
                "Options",
                "Investing"
            ]
        )

    with c2:
        experience = st.selectbox(
            "Experience",
            [
                "Beginner",
                "Intermediate",
                "Advanced"
            ]
        )

    with c3:
        budget = st.selectbox(
            "Budget",
            [
                "Standard",
                "Premium"
            ]
        )

    if st.button("Predict Best Course"):

        if goal == "Options":
            st.success("Recommended: Complete Future and Option Trading Strategies")

        elif goal == "Intraday":
            st.success("Recommended: Complete Intraday and Swing Trading Strategies")

        elif goal == "Investing":
            st.success("Recommended: Value Investing Using Advanced Fundamental Analysis")

        else:
            st.success("Recommended: Power of Trading and Investing Combo Course")

    st.divider()

    st.subheader("INVESMATE AI Chatbot")

    quick = st.columns(4)

    if quick[0].button("Beginner Course"):
        st.session_state.messages.append({
            "role":"assistant",
            "content":"Recommended: Power of Trading and Investing Combo Course."
        })

    if quick[1].button("Compare INSIGNIA"):
        st.session_state.messages.append({
            "role":"assistant",
            "content":"INSIGNIA offers premium mentorship with practical learning."
        })

    if quick[2].button("Pricing"):
        st.session_state.messages.append({
            "role":"assistant",
            "content":"Courses start from Rs. 3,999."
        })

    if quick[3].button("Support"):
        st.session_state.messages.append({
            "role":"assistant",
            "content":"Contact support@invesmate.com"
        })

    for msg in st.session_state.messages:

        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    prompt = st.chat_input("Ask anything about INVESMATE")

    if prompt:

        st.session_state.messages.append({
            "role":"user",
            "content":prompt
        })

        reply = advisor_response(prompt)

        st.session_state.messages.append({
            "role":"assistant",
            "content":reply
        })

        st.rerun()

# =========================================================
# FOOTER
# =========================================================

st.write("")

st.markdown("""
<div class='footer'>

<strong>INVESMATE</strong><br>

Stock Market Learning Platform<br>

SEBI Registered RA: INH000017985<br>

support@invesmate.com<br><br>

Investment in securities markets are subject to market risks.

</div>
""", unsafe_allow_html=True)
