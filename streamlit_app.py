import streamlit as st

st.set_page_config(
    page_title="INVESMATE",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed",
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
            "content": "Hi, I am your INVESMATE AI Advisor. Ask me about courses, pricing, INSIGNIA mentorship, enrollment, support, or course comparison.",
        }
    ]

# =========================================================
# DATA
# =========================================================

PRODUCTS = [
    {
        "title": "Power of Trading and Investing Combo Course",
        "category": "Beginner",
        "price": "Rs. 8,999 - Rs. 11,999",
        "duration": "2 Months / 26 Hours",
        "lessons": "57 Lessons",
        "desc": "Complete trading and investing roadmap for beginners.",
        "modules": ["Technical", "Fundamental", "Risk", "Practical"],
    },
    {
        "title": "Complete Intraday and Swing Trading Strategies",
        "category": "Technical",
        "price": "Rs. 9,999 - Rs. 12,999",
        "duration": "2 Months / 20 Hours",
        "lessons": "48 Lessons",
        "desc": "Advanced intraday and swing trading course.",
        "modules": ["SMC", "Indicators", "Price Action", "Risk"],
    },
    {
        "title": "Complete Future and Option Trading Strategies",
        "category": "Derivatives",
        "price": "Rs. 12,999 - Rs. 15,999",
        "duration": "2 Months / 26 Hours",
        "lessons": "25 Lessons",
        "desc": "Advanced futures and options training.",
        "modules": ["Options", "Greeks", "Hedging", "Futures"],
    },
    {
        "title": "Value Investing Using Advanced Fundamental Analysis",
        "category": "Investing",
        "price": "Rs. 8,999 - Rs. 11,999",
        "duration": "2 Months / 24 Hours",
        "lessons": "57 Lessons",
        "desc": "Long-term investing, business analysis, and valuation.",
        "modules": ["Valuation", "Financials", "Business", "Portfolio"],
    },
    {
        "title": "Introduction To Mutual Funds Investment",
        "category": "Mutual Funds",
        "price": "Rs. 3,999 - Rs. 6,999",
        "duration": "1 Month",
        "lessons": "24 Lessons",
        "desc": "Practical mutual fund and SIP learning course.",
        "modules": ["SIP", "Fund Selection", "Planning", "Wealth"],
    },
    {
        "title": "Dynamic Investment With Fixed Income Securities",
        "category": "Fixed Income",
        "price": "Rs. 10,999",
        "duration": "12 Hours",
        "lessons": "33 Lessons",
        "desc": "Recorded course on bonds, government securities, and income products.",
        "modules": ["Bonds", "Debt", "Income", "Diversification"],
    },
    {
        "title": "The Comprehensive Roadmap Of Commodity Market",
        "category": "Commodity",
        "price": "Rs. 14,999",
        "duration": "16 Hours",
        "lessons": "10 Lessons",
        "desc": "Commodity market course covering gold, silver, crude oil, and natural gas.",
        "modules": ["Gold", "Silver", "Crude Oil", "Natural Gas"],
    },
]

INSIGNIA = [
    {
        "title": "Equity Market Intelligence Matrix",
        "category": "INSIGNIA",
        "price": "Rs. 38,571 / Rs. 44,420",
        "duration": "3 - 5 Months",
        "desc": "Premium mentorship with technical and fundamental analysis.",
        "modules": ["1:1 Mentorship", "Market Trending", "Practical Sessions", "NISM Guidance"],
    },
    {
        "title": "Complete Equity and Derivative Dynasty",
        "category": "INSIGNIA",
        "price": "Rs. 62,305 / Rs. 44,420",
        "duration": "6 - 8 Months",
        "desc": "Advanced premium derivatives and technical mentorship.",
        "modules": ["Options", "Equity", "Fixed Income", "Academic Helpline"],
    },
    {
        "title": "Complete Global Capital Market Specialist",
        "category": "INSIGNIA",
        "price": "Rs. 1,07,689 / Rs. 44,420",
        "duration": "12 Months",
        "desc": "Global capital market specialist program with commodities and US stocks.",
        "modules": ["US Stocks", "Commodity", "Global Market", "Lifetime Recordings"],
    },
]

MENTORS = [
    "Arunava Chatterjee",
    "Sayan Ghosh",
    "Kunal Saha",
    "Suman Goswami",
    "Laboni Pallab Das",
    "Debarati Mukherjee",
    "Pratim Kumar Chakraborty",
    "Mihir Kanti Chakraborty",
]

# =========================================================
# LANGUAGE
# =========================================================

LANG = {
    "English": {
        "home": "Home",
        "products": "Products",
        "insignia": "INSIGNIA",
        "compare": "Course Compare",
        "mentors": "Mentors",
        "support": "Support",
        "advisor": "AI Advisor",
        "title": "Finest Stock Market Learning Experience",
        "sub": "Professional stock market learning with AI-guided mentorship, premium courses, multilingual support, and practical learning paths.",
        "search": "Search courses",
        "category": "Filter by category",
    },
    "Hindi": {
        "home": "होम",
        "products": "कोर्स",
        "insignia": "इंसिग्निया",
        "compare": "कोर्स तुलना",
        "mentors": "मेंटर्स",
        "support": "सपोर्ट",
        "advisor": "AI सलाहकार",
        "title": "सर्वश्रेष्ठ स्टॉक मार्केट लर्निंग अनुभव",
        "sub": "AI आधारित मार्गदर्शन, प्रीमियम कोर्स, बहुभाषी सपोर्ट और प्रैक्टिकल लर्निंग।",
        "search": "कोर्स खोजें",
        "category": "कैटेगरी चुनें",
    },
    "Bengali": {
        "home": "হোম",
        "products": "কোর্স",
        "insignia": "ইনসিগনিয়া",
        "compare": "কোর্স তুলনা",
        "mentors": "মেন্টর",
        "support": "সাপোর্ট",
        "advisor": "AI উপদেষ্টা",
        "title": "সেরা স্টক মার্কেট লার্নিং অভিজ্ঞতা",
        "sub": "AI গাইডেড মেন্টরশিপ, প্রিমিয়াম কোর্স, বহুভাষিক সাপোর্ট এবং প্র্যাকটিক্যাল লার্নিং।",
        "search": "কোর্স খুঁজুন",
        "category": "ক্যাটাগরি বেছে নিন",
    },
    "Odia": {
        "home": "ହୋମ",
        "products": "କୋର୍ସ",
        "insignia": "ଇନସିଗ୍ନିଆ",
        "compare": "କୋର୍ସ ତୁଳନା",
        "mentors": "ମେଣ୍ଟର",
        "support": "ସପୋର୍ଟ",
        "advisor": "AI ଉପଦେଷ୍ଟା",
        "title": "ସର୍ବଶ୍ରେଷ୍ଠ ଷ୍ଟକ୍ ମାର୍କେଟ ଲର୍ଣ୍ଣିଂ ଅନୁଭବ",
        "sub": "AI ଗାଇଡେଡ୍ ମେଣ୍ଟରଶିପ୍, ପ୍ରିମିୟମ୍ କୋର୍ସ, ବହୁଭାଷୀ ସପୋର୍ଟ ଏବଂ ପ୍ରାକ୍ଟିକାଲ୍ ଲର୍ଣ୍ଣିଂ।",
        "search": "କୋର୍ସ ଖୋଜନ୍ତୁ",
        "category": "କ୍ୟାଟେଗୋରୀ ବାଛନ୍ତୁ",
    },
}

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    st.title("INVESMATE")

    st.session_state.language = st.selectbox(
        "Language",
        ["English", "Hindi", "Bengali", "Odia"],
        index=["English", "Hindi", "Bengali", "Odia"].index(st.session_state.language),
    )

    st.session_state.theme = st.selectbox(
        "Theme",
        ["Light", "Dark"],
        index=["Light", "Dark"].index(st.session_state.theme),
    )

    T = LANG[st.session_state.language]

    page = st.radio(
        "Navigate",
        [
            T["home"],
            T["products"],
            T["insignia"],
            T["compare"],
            T["mentors"],
            T["support"],
            T["advisor"],
        ],
    )

# Reload translation after sidebar update
T = LANG[st.session_state.language]

# =========================================================
# THEME CSS
# =========================================================

if st.session_state.theme == "Light":
    bg = "#fafaf8"
    text = "#1a1208"
    text2 = "#6b6150"
    surface = "#ffffff"
    surface2 = "#f5f3ee"
    border = "#e6e0d4"
    accent = "#d4601a"
    hero_bg = "linear-gradient(135deg,#fff7ed,#ffffff)"
else:
    bg = "#0e1117"
    text = "#ffffff"
    text2 = "#d1d5db"
    surface = "#111827"
    surface2 = "#1f2937"
    border = "#374151"
    accent = "#f59e0b"
    hero_bg = "linear-gradient(135deg,#111827,#1f2937)"

st.markdown(
    f"""
<style>
.stApp {{
    background: {bg};
    color: {text};
}}

.block-container {{
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}}

.hero {{
    background: {hero_bg};
    border: 1px solid {border};
    padding: 48px;
    border-radius: 30px;
    box-shadow: 0 12px 34px rgba(0,0,0,0.08);
}}

.hero h1 {{
    font-size: clamp(38px, 6vw, 68px);
    font-weight: 900;
    line-height: 1.02;
    color: {text};
    margin-bottom: 18px;
}}

.hero h1 span {{
    color: {accent};
}}

.hero p {{
    color: {text2};
    font-size: 18px;
    line-height: 1.8;
    max-width: 850px;
}}

.badge {{
    display: inline-block;
    background: {surface2};
    color: {accent};
    border: 1px solid {border};
    padding: 8px 14px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 800;
    margin-bottom: 16px;
}}

.card {{
    background: {surface};
    color: {text};
    border: 1px solid {border};
    border-radius: 24px;
    padding: 24px;
    height: 100%;
    box-shadow: 0 8px 24px rgba(0,0,0,0.06);
}}

.card h3 {{
    margin-top: 0;
    margin-bottom: 10px;
}}

.card p {{
    color: {text2};
    line-height: 1.65;
}}

.price {{
    color: {accent};
    font-weight: 900;
    font-size: 18px;
}}

.chip {{
    background: {surface2};
    color: {text2};
    border: 1px solid {border};
    border-radius: 999px;
    padding: 6px 12px;
    display: inline-block;
    margin: 4px 4px 0 0;
    font-size: 12px;
}}

.footer {{
    background: {surface};
    color: {text2};
    border: 1px solid {border};
    padding: 35px;
    border-radius: 26px;
    text-align: center;
    line-height: 1.8;
    margin-top: 28px;
}}

.small-note {{
    color: {text2};
    font-size: 14px;
}}

.metric-card {{
    background: {surface};
    border: 1px solid {border};
    border-radius: 20px;
    padding: 18px;
    text-align: center;
}}

.metric-card h2 {{
    color: {accent};
    margin-bottom: 4px;
}}
</style>
""",
    unsafe_allow_html=True,
)

# =========================================================
# HELPERS
# =========================================================

def module_chips(modules):
    return "".join([f"<span class='chip'>{m}</span>" for m in modules])


def product_card(product):
    return f"""
    <div class="card">
        <div class="badge">{product["category"]}</div>
        <h3>{product["title"]}</h3>
        <p>{product["desc"]}</p>
        <p class="price">{product["price"]}</p>
        <p>{product["duration"]} | {product["lessons"]}</p>
        <div>{module_chips(product["modules"])}</div>
    </div>
    """


def insignia_card(item):
    return f"""
    <div class="card">
        <div class="badge">Premium Mentorship</div>
        <h3>{item["title"]}</h3>
        <p>{item["desc"]}</p>
        <p class="price">{item["price"]}</p>
        <p>{item["duration"]}</p>
        <div>{module_chips(item["modules"])}</div>
    </div>
    """


def predict_course(goal, experience, budget):
    goal = goal.lower()
    budget = budget.lower()

    if "option" in goal or "derivative" in goal:
        return INSIGNIA[1] if "premium" in budget else PRODUCTS[2]

    if "intraday" in goal or "swing" in goal or "technical" in goal:
        return INSIGNIA[0] if "premium" in budget else PRODUCTS[1]

    if "invest" in goal or "fundamental" in goal or "long" in goal:
        return INSIGNIA[0] if "premium" in budget else PRODUCTS[3]

    if "mutual" in goal or "sip" in goal:
        return PRODUCTS[4]

    if "commodity" in goal or "global" in goal:
        return INSIGNIA[2] if "premium" in budget else PRODUCTS[6]

    return INSIGNIA[0] if "premium" in budget else PRODUCTS[0]


def advisor_response(prompt):
    p = prompt.lower()

    if "beginner" in p:
        return "Recommended: Power of Trading and Investing Combo Course. It is best for new learners who want both trading and investing basics."

    if "option" in p or "future" in p or "derivative" in p:
        return "Recommended: Complete Future and Option Trading Strategies. Premium alternative: Complete Equity and Derivative Dynasty."

    if "intraday" in p or "swing" in p or "technical" in p:
        return "Recommended: Complete Intraday and Swing Trading Strategies. It focuses on chart patterns, indicators, SMC, and risk control."

    if "invest" in p or "fundamental" in p or "long term" in p:
        return "Recommended: Value Investing Using Advanced Fundamental Analysis. Premium alternative: Equity Market Intelligence Matrix."

    if "mutual" in p or "sip" in p:
        return "Recommended: Introduction To Mutual Funds Investment."

    if "commodity" in p or "global" in p:
        return "Recommended: The Comprehensive Roadmap Of Commodity Market. Premium alternative: Complete Global Capital Market Specialist."

    if "insignia" in p or "premium" in p:
        return "INSIGNIA is INVESMATE's premium mentorship ecosystem with live sessions, 1:1 mentorship, practical support, and advanced learning paths."

    if "mentor" in p:
        return "INVESMATE mentors include Arunava Chatterjee, Sayan Ghosh, Kunal Saha, Suman Goswami, Laboni Pallab Das, Debarati Mukherjee, Pratim Kumar Chakraborty, and Mihir Kanti Chakraborty."

    if "support" in p or "contact" in p or "call" in p:
        return "Support: +91 9016791791, +91 7596037781, +91 7003110622, or email support@invesmate.com."

    if "price" in p or "fee" in p or "cost" in p:
        return "Courses start from Rs. 3,999 and INSIGNIA premium plans start from Rs. 38,571. Final pricing may vary by batch, GST, EMI, and offer."

    if "compare" in p:
        return "Use the Course Compare page to compare two courses side by side by price, duration, category, modules, and suitability."

    return "Please share your goal, experience level, and budget. I will recommend the best INVESMATE or INSIGNIA course for you."


def show_risk_note():
    st.caption("Note: Investment in securities markets is subject to market risks. This app is for educational purposes only.")


# =========================================================
# PAGE ROUTING
# =========================================================

if page == T["home"]:
    st.markdown(
        f"""
        <div class="hero">
            <div class="badge">SEBI Registered RA: INH000017985</div>
            <h1>{T["title"].replace("Learning", "<span>Learning</span>")}</h1>
            <p>{T["sub"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("<div class='metric-card'><h2>20+</h2><p>Expert Courses</p></div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='metric-card'><h2>8</h2><p>Certified Mentors</p></div>", unsafe_allow_html=True)

    with c3:
        st.markdown("<div class='metric-card'><h2>4</h2><p>Languages</p></div>", unsafe_allow_html=True)

    with c4:
        st.markdown("<div class='metric-card'><h2>SEBI</h2><p>Registered RA</p></div>", unsafe_allow_html=True)

    st.divider()
    st.subheader("Featured Courses")

    cols = st.columns(3)
    for i, item in enumerate([PRODUCTS[0], PRODUCTS[1], INSIGNIA[0]]):
        with cols[i]:
            if item in PRODUCTS:
                st.markdown(product_card(item), unsafe_allow_html=True)
            else:
                st.markdown(insignia_card(item), unsafe_allow_html=True)

    show_risk_note()


elif page == T["products"]:
    st.title(T["products"])

    search = st.text_input(T["search"])
    categories = ["All"] + sorted(set(p["category"] for p in PRODUCTS))
    category = st.selectbox(T["category"], categories)

    filtered = PRODUCTS

    if category != "All":
        filtered = [p for p in filtered if p["category"] == category]

    if search:
        q = search.lower()
        filtered = [
            p for p in filtered
            if q in p["title"].lower()
            or q in p["desc"].lower()
            or q in p["category"].lower()
            or any(q in m.lower() for m in p["modules"])
        ]

    if not filtered:
        st.warning("No course found. Try another search or category.")
    else:
        cols = st.columns(3)
        for i, product in enumerate(filtered):
            with cols[i % 3]:
                st.markdown(product_card(product), unsafe_allow_html=True)

    show_risk_note()


elif page == T["insignia"]:
    st.title(T["insignia"])
    st.write("Premium mentorship plans with structured guidance, live sessions, practical support, and advanced learning.")

    cols = st.columns(3)
    for i, item in enumerate(INSIGNIA):
        with cols[i]:
            st.markdown(insignia_card(item), unsafe_allow_html=True)

    show_risk_note()


elif page == T["compare"]:
    st.title(T["compare"])

    all_courses = PRODUCTS + INSIGNIA
    titles = [c["title"] for c in all_courses]

    c1, c2 = st.columns(2)

    with c1:
        course1 = st.selectbox("Select Course 1", titles, index=0)

    with c2:
        default_index = 1 if len(titles) > 1 else 0
        course2 = st.selectbox("Select Course 2", titles, index=default_index)

    p1 = next(c for c in all_courses if c["title"] == course1)
    p2 = next(c for c in all_courses if c["title"] == course2)

    col1, col2 = st.columns(2)

    with col1:
        if p1 in PRODUCTS:
            st.markdown(product_card(p1), unsafe_allow_html=True)
        else:
            st.markdown(insignia_card(p1), unsafe_allow_html=True)

    with col2:
        if p2 in PRODUCTS:
            st.markdown(product_card(p2), unsafe_allow_html=True)
        else:
            st.markdown(insignia_card(p2), unsafe_allow_html=True)

    st.divider()

    st.subheader("Comparison Summary")
    st.table(
        {
            "Feature": ["Category", "Price", "Duration", "Best For"],
            course1: [
                p1["category"],
                p1["price"],
                p1["duration"],
                p1["desc"],
            ],
            course2: [
                p2["category"],
                p2["price"],
                p2["duration"],
                p2["desc"],
            ],
        }
    )

    show_risk_note()


elif page == T["mentors"]:
    st.title(T["mentors"])

    cols = st.columns(4)

    for i, mentor in enumerate(MENTORS):
        initials = "".join([part[0] for part in mentor.split()[:2]])

        with cols[i % 4]:
            st.markdown(
                f"""
                <div class="card" style="text-align:center;">
                    <div style="
                        width:70px;
                        height:70px;
                        border-radius:20px;
                        background:linear-gradient(135deg,#d4601a,#f59e0b);
                        margin:0 auto 16px auto;
                        color:white;
                        font-weight:900;
                        display:flex;
                        align-items:center;
                        justify-content:center;
                        font-size:24px;">
                        {initials}
                    </div>
                    <h3>{mentor}</h3>
                    <p>Capital Market Mentor and NISM-certified professional</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


elif page == T["support"]:
    st.title(T["support"])

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(
            """
            <div class="card">
                <h3>Contact Team</h3>
                <p><b>Phone</b></p>
                <p>+91 9016791791</p>
                <p>+91 7596037781</p>
                <p>+91 7003110622</p>
                <br>
                <p><b>Email</b></p>
                <p>support@invesmate.com</p>
                <p>sales@invesmate.com</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            """
            <div class="card">
                <h3>Disclaimer</h3>
                <p>
                    Investment in securities markets is subject to market risks.
                    Read all related documents carefully before investing.
                </p>
                <p>
                    Registration granted by SEBI and certification from NISM do not guarantee performance
                    or provide assurance of returns.
                </p>
                <p>
                    INVESMATE INSIGHTS is a SEBI Registered Research Analyst platform.
                    This app is for educational purposes only.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )


elif page == T["advisor"]:
    st.title(T["advisor"])

    st.subheader("AI Course Predictor")

    c1, c2, c3 = st.columns(3)

    with c1:
        goal = st.selectbox(
            "Goal",
            [
                "Beginner trading and investing",
                "Intraday and swing trading",
                "Options and derivatives",
                "Long-term investing and fundamentals",
                "Mutual funds and SIP",
                "Commodity or global market",
            ],
        )

    with c2:
        experience = st.selectbox(
            "Experience",
            ["Beginner", "Intermediate", "Advanced"],
        )

    with c3:
        budget = st.selectbox(
            "Budget",
            ["Standard course", "Premium mentorship"],
        )

    if st.button("Predict Best Course", type="primary"):
        result = predict_course(goal, experience, budget)
        st.success(f"Recommended: {result['title']}")

        if result in PRODUCTS:
            st.markdown(product_card(result), unsafe_allow_html=True)
        else:
            st.markdown(insignia_card(result), unsafe_allow_html=True)

    st.divider()

    st.subheader("INVESMATE AI Chatbot")

    q1, q2, q3, q4 = st.columns(4)

    if q1.button("Beginner Course"):
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": advisor_response("beginner"),
            }
        )

    if q2.button("Compare INSIGNIA"):
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": advisor_response("insignia"),
            }
        )

    if q3.button("Pricing"):
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": advisor_response("price"),
            }
        )

    if q4.button("Support"):
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": advisor_response("support"),
            }
        )

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    prompt = st.chat_input("Ask anything about INVESMATE")

    if prompt:
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        reply = advisor_response(prompt)
        reply += "\n\nNote: Investment in securities markets is subject to market risks."

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": reply,
            }
        )

        st.rerun()

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        <strong>INVESMATE</strong><br>
        Stock Market Learning Platform<br>
        SEBI Registered RA: INH000017985<br>
        support@invesmate.com | sales@invesmate.com<br><br>
        Investment in securities markets is subject to market risks.
    </div>
    """,
    unsafe_allow_html=True,
)
