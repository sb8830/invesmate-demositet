import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="INVESMATE - Stock Market Learning Platform",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# CSS
# -----------------------------
st.markdown(
    """
<style>
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

body {
    background: #fafaf8;
}

.main-title {
    font-size: 56px;
    font-weight: 900;
    line-height: 1.05;
    color: #1a1208;
    margin-bottom: 10px;
}

.highlight {
    color: #d4601a;
}

.hero-box {
    background: linear-gradient(135deg, #fff7ed, #ffffff);
    border: 1px solid #e6e0d4;
    border-radius: 28px;
    padding: 42px;
    box-shadow: 0 16px 48px rgba(26,18,8,0.08);
}

.badge {
    display: inline-block;
    background: #fff3ea;
    color: #d4601a;
    border: 1px solid #f6d4b4;
    border-radius: 999px;
    padding: 6px 14px;
    font-size: 13px;
    font-weight: 800;
    margin-bottom: 14px;
}

.subtext {
    color: #6b6150;
    font-size: 18px;
    line-height: 1.7;
    max-width: 760px;
}

.card {
    background: #ffffff;
    border: 1px solid #e6e0d4;
    border-radius: 22px;
    padding: 22px;
    box-shadow: 0 8px 28px rgba(26,18,8,0.07);
    height: 100%;
}

.dark-card {
    background: #1a1208;
    color: white;
    border-radius: 22px;
    padding: 24px;
    height: 100%;
}

.card h3, .dark-card h3 {
    margin-top: 0;
    font-size: 20px;
}

.price {
    color: #d4601a;
    font-size: 18px;
    font-weight: 800;
}

.dark-price {
    color: #f08d3c;
    font-size: 18px;
    font-weight: 800;
}

.small-muted {
    color: #6b6150;
    font-size: 14px;
}

.module-chip {
    display: inline-block;
    background: #f5f3ee;
    color: #6b6150;
    border-radius: 999px;
    padding: 5px 10px;
    margin: 3px;
    font-size: 12px;
}

.footer {
    background: #1a1208;
    color: rgba(255,255,255,0.78);
    padding: 28px;
    border-radius: 24px;
    text-align: center;
    line-height: 1.8;
    margin-top: 30px;
}

.support-box {
    background: #ffffff;
    border: 1px solid #e6e0d4;
    border-radius: 22px;
    padding: 24px;
    height: 100%;
}

.chat-box {
    background: #ffffff;
    border: 1px solid #e6e0d4;
    border-radius: 24px;
    padding: 22px;
    box-shadow: 0 8px 28px rgba(26,18,8,0.07);
}
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# DATA
# -----------------------------
PRODUCTS = [
    {
        "title": "Power of Trading and Investing Combo Course",
        "category": "Live Course",
        "tag": "Beginner",
        "price": "Rs. 8,999 - Rs. 11,999",
        "duration": "2 Months / 26 Hours",
        "lessons": "57 Lessons",
        "description": "A complete capital-market course covering trading and investing from basics to advanced level.",
        "modules": ["Market basics", "Technical analysis", "Investing foundation", "Real market practice"],
    },
    {
        "title": "Complete Intraday and Swing Trading Strategies",
        "category": "Live Course",
        "tag": "Technical Trading",
        "price": "Rs. 9,999 - Rs. 12,999",
        "duration": "2 Months / 20 Hours",
        "lessons": "48 Lessons",
        "description": "Advanced technical-analysis course for intraday and swing trading.",
        "modules": ["Chart patterns", "Indicators", "Smart Money Concepts", "Risk control"],
    },
    {
        "title": "Complete Future and Option Trading Strategies",
        "category": "Live Course",
        "tag": "Derivatives",
        "price": "Rs. 12,999 - Rs. 15,999",
        "duration": "2 Months / 26 Hours",
        "lessons": "25 Lessons",
        "description": "Futures and options training for learners who want derivatives strategy knowledge.",
        "modules": ["Futures basics", "Option buying", "Option selling", "Hedging"],
    },
    {
        "title": "Value Investing Using Advanced Fundamental Analysis",
        "category": "Live Course",
        "tag": "Investing",
        "price": "Rs. 8,999 - Rs. 11,999",
        "duration": "2 Months / 24 Hours",
        "lessons": "57 Lessons",
        "description": "Fundamental-analysis and value-investing roadmap for long-term equity investors.",
        "modules": ["Business analysis", "Financial statements", "Valuation", "Portfolio mindset"],
    },
    {
        "title": "Introduction To Mutual Funds Investment",
        "category": "Course",
        "tag": "Mutual Funds",
        "price": "Rs. 3,999 - Rs. 6,999",
        "duration": "1 Month",
        "lessons": "24 Lessons",
        "description": "Practical overview of mutual funds, SIPs, and fund selection.",
        "modules": ["MF basics", "SIP planning", "Fund selection", "Long-term wealth"],
    },
    {
        "title": "Dynamic Investment With Fixed Income Securities",
        "category": "Recorded Course",
        "tag": "Fixed Income",
        "price": "Rs. 10,999",
        "duration": "12 Hours",
        "lessons": "33 Lessons",
        "description": "Recorded course on bonds, government securities, income products, and diversification.",
        "modules": ["Bonds", "Government securities", "Income planning", "Diversification"],
    },
    {
        "title": "The Comprehensive Roadmap Of Commodity Market",
        "category": "Live Course",
        "tag": "Commodity",
        "price": "Rs. 14,999",
        "duration": "16 Hours",
        "lessons": "10 Lessons",
        "description": "Commodity-market course covering gold, silver, crude oil, natural gas, and risk management.",
        "modules": ["Gold and silver", "Crude oil", "Natural gas", "Technical view"],
    },
    {
        "title": "Power TI Masterclass",
        "category": "Free Entry Program",
        "tag": "Masterclass",
        "price": "Free / Registration",
        "duration": "Short Session",
        "lessons": "Live Session",
        "description": "Entry-level masterclass for learners starting their stock-market journey.",
        "modules": ["Orientation", "Counseling", "Beginner roadmap", "Q&A"],
    },
    {
        "title": "Share Samadhan",
        "category": "Newsletter & Research",
        "tag": "Market Study",
        "price": "Included in selected plans",
        "duration": "Weekly Access",
        "lessons": "Premium Study",
        "description": "Weekly Bengali stock-market study for cash, derivatives, IPOs, mutual funds, and trends.",
        "modules": ["Cash market", "Derivatives", "IPO study", "Mutual funds"],
    },
    {
        "title": "Market Trending All Segment",
        "category": "Premium Tool Access",
        "tag": "Market Intelligence",
        "price": "Included in INSIGNIA plans",
        "duration": "Plan-based Access",
        "lessons": "All Segment Access",
        "description": "Premium market-trending access included in selected INSIGNIA programs.",
        "modules": ["Cash", "Derivatives", "Commodity", "Fixed asset investment"],
    },
    {
        "title": "INVESMATE Learning App",
        "category": "Mobile App",
        "tag": "Learning Platform",
        "price": "App-based Access",
        "duration": "Anytime Learning",
        "lessons": "Course Library",
        "description": "Mobile app for classes, recordings, academic support, and My Insignia Help.",
        "modules": ["Live classes", "Recordings", "Support", "Course access"],
    },
    {
        "title": "Insights.Market",
        "category": "Research Brand",
        "tag": "SEBI RA Research",
        "price": "Separate research platform",
        "duration": "Research Access",
        "lessons": "Research Products",
        "description": "SEBI-registered equity research brand under INVESMATE INSIGHTS.",
        "modules": ["Equity research", "Investor charter", "Disclosures", "Compliance"],
    },
]

INSIGNIA = [
    {
        "title": "Equity Market Intelligence Matrix",
        "tag": "Premium Mentorship",
        "price": "Rs. 38,571 / Rs. 44,420",
        "duration": "3-5 Months",
        "description": "Premium mentorship combining advanced technical, techno-funda, and fundamental analysis.",
        "modules": ["Market Trending", "Share Samadhan", "1:1 mentorship", "4 practical sessions", "NISM guidance"],
    },
    {
        "title": "Complete Equity and Derivative Dynasty",
        "tag": "Options Premium",
        "price": "Rs. 62,305 / Rs. 44,420",
        "duration": "6-8 Months",
        "description": "Advanced premium pathway combining technical, fundamental, derivatives, and fixed-income learning.",
        "modules": ["Advanced Technical", "Complete Options", "Fixed Income", "8 practical sessions", "Academic helpline"],
    },
    {
        "title": "Complete Global Capital Market Specialist",
        "tag": "Global Premium",
        "price": "Rs. 1,07,689 / Rs. 44,420",
        "duration": "12 Months",
        "description": "Full-stack global capital-market specialist path including commodities, US stocks, mutual funds, and software training.",
        "modules": ["US stocks", "Commodity", "Advanced mutual fund", "3 mentorship sessions", "Lifetime recordings"],
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

# -----------------------------
# HELPERS
# -----------------------------
def chips(items):
    return " ".join([f'<span class="module-chip">{item}</span>' for item in items])


def course_card(item):
    return f"""
    <div class="card">
        <div class="badge">{item["tag"]}</div>
        <h3>{item["title"]}</h3>
        <p>{item["description"]}</p>
        <p class="price">{item["price"]}</p>
        <p class="small-muted">{item["duration"]} | {item.get("lessons", "")}</p>
        <div>{chips(item["modules"])}</div>
    </div>
    """


def insignia_card(item):
    return f"""
    <div class="dark-card">
        <div class="badge">{item["tag"]}</div>
        <h3>{item["title"]}</h3>
        <p>{item["description"]}</p>
        <p class="dark-price">{item["price"]}</p>
        <p>{item["duration"]}</p>
        <div>{chips(item["modules"])}</div>
    </div>
    """


def predict_course(goal, experience, budget):
    goal = goal.lower()
    budget = budget.lower()

    if "option" in goal or "derivative" in goal:
        return INSIGNIA[1] if "premium" in budget else PRODUCTS[2]
    if "commodity" in goal or "global" in goal:
        return INSIGNIA[2] if "premium" in budget else PRODUCTS[6]
    if "mutual" in goal or "sip" in goal:
        return PRODUCTS[4]
    if "intraday" in goal or "swing" in goal or "technical" in goal:
        return INSIGNIA[0] if "premium" in budget else PRODUCTS[1]
    if "long" in goal or "fundamental" in goal or "invest" in goal:
        return INSIGNIA[0] if "premium" in budget else PRODUCTS[3]

    return INSIGNIA[0] if "premium" in budget else PRODUCTS[0]


def advisor_reply(prompt):
    text = prompt.lower()

    if "price" in text or "fee" in text or "cost" in text:
        return (
            "Here is the pricing overview:\n\n"
            "- Beginner and live courses: Rs. 8,999 to Rs. 15,999 approximately\n"
            "- Mutual fund course: Rs. 3,999 to Rs. 6,999\n"
            "- INSIGNIA premium plans: Rs. 38,571 onwards\n\n"
            "For GST, EMI, discounts, and batch timing, please contact the counseling team."
        )

    if "insignia" in text or "premium" in text:
        return (
            "INSIGNIA is the premium mentorship journey from INVESMATE. It is suitable for learners who want structured guidance, "
            "live support, practical sessions, 1:1 mentorship, and advanced market learning.\n\n"
            "Top plans:\n"
            "- Equity Market Intelligence Matrix\n"
            "- Complete Equity and Derivative Dynasty\n"
            "- Complete Global Capital Market Specialist"
        )

    if "option" in text or "future" in text or "derivative" in text:
        return (
            "For options and derivatives, the best standard course is Complete Future and Option Trading Strategies. "
            "For premium mentorship, choose Complete Equity and Derivative Dynasty."
        )

    if "intraday" in text or "swing" in text or "technical" in text:
        return (
            "For intraday, swing trading, and technical analysis, choose Complete Intraday and Swing Trading Strategies. "
            "If you want premium guidance, Equity Market Intelligence Matrix is a better fit."
        )

    if "mutual" in text or "sip" in text:
        return (
            "For mutual funds and SIP learning, choose Introduction To Mutual Funds Investment. "
            "It is suitable for beginners and long-term investors."
        )

    if "enroll" in text or "join" in text or "admission" in text:
        return (
            "Enrollment flow:\n\n"
            "1. Choose your course or INSIGNIA plan\n"
            "2. Request counseling\n"
            "3. Confirm fee, GST, EMI, and batch timing\n"
            "4. Complete payment\n"
            "5. Access classes through the INVESMATE learning app"
        )

    if "contact" in text or "support" in text or "call" in text:
        return (
            "You can contact INVESMATE here:\n\n"
            "- +91 9016791791\n"
            "- +91 7596037781\n"
            "- +91 7003110622\n"
            "- support@invesmate.com\n"
            "- sales@invesmate.com"
        )

    if "mentor" in text:
        return (
            "INVESMATE mentors include Arunava Chatterjee, Sayan Ghosh, Kunal Saha, Suman Goswami, "
            "Laboni Pallab Das, Debarati Mukherjee, Pratim Kumar Chakraborty, and Mihir Kanti Chakraborty."
        )

    return (
        "For beginners, I recommend the Power of Trading and Investing Combo Course. "
        "For advanced learners, INSIGNIA mentorship is better. You can also use the Course Predictor below for a personalized recommendation."
    )


# -----------------------------
# NAVIGATION
# -----------------------------
st.sidebar.title("INVESMATE")
page = st.sidebar.radio(
    "Navigate",
    [
        "Home",
        "Courses",
        "INSIGNIA",
        "AI Advisor",
        "Mentors",
        "Support",
    ],
)

# -----------------------------
# HOME
# -----------------------------
if page == "Home":
    st.markdown(
        """
        <div class="hero-box">
            <div class="badge">SEBI Registered RA: INH000017985</div>
            <div class="main-title">
                Finest Stock Market <span class="highlight">Learning</span> Experience
            </div>
            <p class="subtext">
                A professional platform for INVESMATE and INSIGNIA with AI-guided course selection,
                multilingual support, and personalized mentorship plans for every learner.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Expert Courses", "20+")
    c2.metric("Certified Mentors", "8")
    c3.metric("Language Support", "3")
    c4.metric("Registration", "SEBI RA")

    st.divider()

    st.subheader("Recommended Learning Paths")
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(course_card(PRODUCTS[0]), unsafe_allow_html=True)
    with c2:
        st.markdown(course_card(PRODUCTS[1]), unsafe_allow_html=True)
    with c3:
        st.markdown(insignia_card(INSIGNIA[0]), unsafe_allow_html=True)

# -----------------------------
# COURSES
# -----------------------------
elif page == "Courses":
    st.title("Complete Product Ecosystem")

    search = st.text_input("Search courses, tools, or mentorship plans")
    categories = ["All"] + sorted(set(item["category"] for item in PRODUCTS))
    selected_category = st.selectbox("Filter by category", categories)

    filtered = PRODUCTS

    if selected_category != "All":
        filtered = [p for p in filtered if p["category"] == selected_category]

    if search:
        q = search.lower()
        filtered = [
            p for p in filtered
            if q in p["title"].lower()
            or q in p["description"].lower()
            or q in p["category"].lower()
            or q in p["tag"].lower()
        ]

    if not filtered:
        st.warning("No courses found. Try another search or category.")
    else:
        cols = st.columns(3)
        for i, product in enumerate(filtered):
            with cols[i % 3]:
                st.markdown(course_card(product), unsafe_allow_html=True)

# -----------------------------
# INSIGNIA
# -----------------------------
elif page == "INSIGNIA":
    st.title("INSIGNIA Premium Mentorship Plans")
    st.write(
        "Intensive, structured mentorship programs combining live sessions, 1:1 guidance, practical sessions, and premium learning support."
    )

    cols = st.columns(3)
    for i, plan in enumerate(INSIGNIA):
        with cols[i]:
            st.markdown(insignia_card(plan), unsafe_allow_html=True)

    st.divider()
    st.subheader("INSIGNIA Includes")
    st.write(
        "- 1:1 mentorship\n"
        "- Live classes and practical sessions\n"
        "- Academic helpline\n"
        "- Market Trending access\n"
        "- Share Samadhan access\n"
        "- Lifetime recordings in selected plans\n"
        "- NISM guidance in selected plans"
    )

# -----------------------------
# AI ADVISOR
# -----------------------------
elif page == "AI Advisor":
    st.title("INVESMATE AI Advisor")

    st.markdown('<div class="chat-box">', unsafe_allow_html=True)

    st.subheader("AI Course Predictor")

    c1, c2, c3 = st.columns(3)

    with c1:
        goal = st.selectbox(
            "Learning Goal",
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
            "Experience Level",
            ["Beginner", "Intermediate", "Advanced"],
        )

    with c3:
        budget = st.selectbox(
            "Budget Preference",
            ["Standard course", "Premium mentorship"],
        )

    if st.button("Predict Best Course", type="primary"):
        result = predict_course(goal, experience, budget)
        st.success("Recommended Course")
        if "modules" in result:
            if result in INSIGNIA:
                st.markdown(insignia_card(result), unsafe_allow_html=True)
            else:
                st.markdown(course_card(result), unsafe_allow_html=True)

    st.divider()
    st.subheader("Chat with AI Advisor")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Hi! I am your INVESMATE AI Advisor. "
                    "Ask me about courses, pricing, enrollment, INSIGNIA mentorship, or support."
                ),
            }
        ]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    prompt = st.chat_input("Ask about courses, pricing, enrollment...")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.write(prompt)

        reply = advisor_reply(prompt)
        reply += "\n\nNote: Investment in securities markets is subject to market risks."

        st.session_state.messages.append({"role": "assistant", "content": reply})

        with st.chat_message("assistant"):
            st.write(reply)

    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# MENTORS
# -----------------------------
elif page == "Mentors":
    st.title("Experienced Market Mentors")

    cols = st.columns(4)
    for i, mentor in enumerate(MENTORS):
        initials = "".join([x[0] for x in mentor.split()[:2]])
        with cols[i % 4]:
            st.markdown(
                f"""
                <div class="card" style="text-align:center;">
                    <div style="
                        width:64px;
                        height:64px;
                        background:linear-gradient(135deg,#d4601a,#fbbf24);
                        color:white;
                        border-radius:20px;
                        display:flex;
                        align-items:center;
                        justify-content:center;
                        font-weight:900;
                        font-size:20px;
                        margin:0 auto 14px auto;">
                        {initials}
                    </div>
                    <h3>{mentor}</h3>
                    <p class="small-muted">Capital market mentor and NISM-certified professional</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

# -----------------------------
# SUPPORT
# -----------------------------
elif page == "Support":
    st.title("Support and Counseling")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(
            """
            <div class="support-box">
                <h3>Counseling and Support</h3>
                <p><b>Phone:</b></p>
                <p>+91 9016791791</p>
                <p>+91 7596037781</p>
                <p>+91 7003110622</p>
                <p><b>Email:</b></p>
                <p>support@invesmate.com</p>
                <p>sales@invesmate.com</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            """
            <div class="support-box">
                <h3>Disclaimer</h3>
                <p>
                Investment in securities markets is subject to market risks.
                Read all related documents carefully before investing.
                Registration granted by SEBI and certification from NISM in no way guarantee performance
                of the intermediary or provide any assurance of returns to investors.
                </p>
                <p>
                INVESMATE INSIGHTS is a SEBI Registered Research Analyst platform.
                This app is for educational purposes only.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# -----------------------------
# FOOTER
# -----------------------------
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
