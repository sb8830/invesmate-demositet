import streamlit as st

st.set_page_config(
    page_title="INVESMATE - Stock Market Learning Platform",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: Arial, sans-serif;
}

.main {
    background: #fafaf8;
}

.hero {
    padding: 60px 30px;
    background: linear-gradient(135deg, #fff7ed, #ffffff);
    border-radius: 24px;
    margin-bottom: 30px;
}

.hero h1 {
    font-size: 56px;
    font-weight: 800;
    color: #1a1208;
    line-height: 1.05;
}

.hero span {
    color: #d4601a;
}

.subtext {
    font-size: 19px;
    color: #6b6150;
    max-width: 700px;
}

.card {
    background: white;
    border: 1px solid #e6e0d4;
    border-radius: 20px;
    padding: 22px;
    box-shadow: 0 6px 24px rgba(26,18,8,0.08);
    height: 100%;
}

.badge {
    display: inline-block;
    background: #fff3ea;
    color: #d4601a;
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 14px;
}

.price {
    color: #d4601a;
    font-weight: 700;
}

.footer {
    background: #1a1208;
    color: rgba(255,255,255,0.75);
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)


PRODUCTS = [
    {
        "title": "Power of Trading and Investing Combo Course",
        "category": "Beginner",
        "price": "Rs. 8,999 - Rs. 11,999",
        "duration": "2 Months / 26 Hours",
        "description": "Complete capital-market course covering trading and investing from basics to advanced level."
    },
    {
        "title": "Complete Intraday and Swing Trading Strategies",
        "category": "Technical Trading",
        "price": "Rs. 9,999 - Rs. 12,999",
        "duration": "2 Months / 20 Hours",
        "description": "Advanced technical-analysis course for intraday and swing trading."
    },
    {
        "title": "Complete Future and Option Trading Strategies",
        "category": "Derivatives",
        "price": "Rs. 12,999 - Rs. 15,999",
        "duration": "2 Months / 26 Hours",
        "description": "Futures and options training for learners who want derivatives strategy knowledge."
    },
    {
        "title": "Value Investing Using Advanced Fundamental Analysis",
        "category": "Investing",
        "price": "Rs. 8,999 - Rs. 11,999",
        "duration": "2 Months / 24 Hours",
        "description": "Fundamental-analysis and value-investing roadmap for long-term equity investors."
    },
    {
        "title": "Introduction To Mutual Funds Investment",
        "category": "Mutual Funds",
        "price": "Rs. 3,999 - Rs. 6,999",
        "duration": "1 Month",
        "description": "Practical overview of mutual funds, SIPs, and fund selection."
    },
    {
        "title": "The Comprehensive Roadmap Of Commodity Market",
        "category": "Commodity",
        "price": "Rs. 14,999",
        "duration": "16 Hours",
        "description": "Commodity-market course covering gold, silver, crude oil, natural gas, and risk management."
    },
]

INSIGNIA = [
    {
        "title": "Equity Market Intelligence Matrix",
        "price": "Rs. 38,571 / Rs. 44,420",
        "duration": "3-5 Months",
        "description": "Premium mentorship combining advanced technical, techno-funda, and fundamental analysis."
    },
    {
        "title": "Complete Equity and Derivative Dynasty",
        "price": "Rs. 62,305 / Rs. 44,420",
        "duration": "6-8 Months",
        "description": "Advanced premium pathway combining technical, fundamental, derivatives, and fixed-income learning."
    },
    {
        "title": "Complete Global Capital Market Specialist",
        "price": "Rs. 1,07,689 / Rs. 44,420",
        "duration": "12 Months",
        "description": "Full-stack global capital-market specialist path including commodities, US stocks, and global markets."
    },
]


def predict_course(goal, experience, budget):
    goal = goal.lower()
    budget = budget.lower()

    if "option" in goal or "derivative" in goal:
        return INSIGNIA[1] if "premium" in budget else PRODUCTS[2]

    if "commodity" in goal or "global" in goal:
        return INSIGNIA[2] if "premium" in budget else PRODUCTS[5]

    if "mutual" in goal or "sip" in goal:
        return PRODUCTS[4]

    if "intraday" in goal or "swing" in goal or "technical" in goal:
        return INSIGNIA[0] if "premium" in budget else PRODUCTS[1]

    if "long" in goal or "fundamental" in goal or "invest" in goal:
        return INSIGNIA[0] if "premium" in budget else PRODUCTS[3]

    return INSIGNIA[0] if "premium" in budget else PRODUCTS[0]


st.markdown("""
<div class="hero">
    <div class="badge">SEBI Registered RA: INH000017985</div>
    <h1>Finest Stock Market <span>Learning</span> Experience</h1>
    <p class="subtext">
        A professional platform for INVESMATE and INSIGNIA with AI-guided course selection,
        multilingual support, and personalized mentorship plans for every learner.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Courses", "20+")
col2.metric("Mentors", "8")
col3.metric("Languages", "3")
col4.metric("Registration", "SEBI RA")

st.divider()

st.header("AI Course Predictor")

c1, c2, c3 = st.columns(3)

with c1:
    goal = st.selectbox(
        "Learning Goal",
        [
            "Beginner trading and investing",
            "Intraday and swing trading",
            "Options and derivatives",
            "Long-term investing",
            "Mutual funds and SIP",
            "Commodity or global market"
        ]
    )

with c2:
    experience = st.selectbox(
        "Experience Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

with c3:
    budget = st.selectbox(
        "Budget Preference",
        ["Standard course", "Premium mentorship"]
    )

if st.button("Predict Best Course", type="primary"):
    result = predict_course(goal, experience, budget)

    st.success("Recommended Course")
    st.markdown(f"""
    <div class="card">
        <h3>{result["title"]}</h3>
        <p>{result["description"]}</p>
        <p class="price">{result["price"]}</p>
        <p>{result["duration"]}</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.header("All Courses")

search = st.text_input("Search courses")
categories = ["All"] + sorted(set(item["category"] for item in PRODUCTS))
selected_category = st.selectbox("Filter by category", categories)

filtered_products = PRODUCTS

if selected_category != "All":
    filtered_products = [
        item for item in filtered_products
        if item["category"] == selected_category
    ]

if search:
    filtered_products = [
        item for item in filtered_products
        if search.lower() in item["title"].lower()
        or search.lower() in item["description"].lower()
        or search.lower() in item["category"].lower()
    ]

cols = st.columns(3)

for index, product in enumerate(filtered_products):
    with cols[index % 3]:
        st.markdown(f"""
        <div class="card">
            <div class="badge">{product["category"]}</div>
            <h3>{product["title"]}</h3>
            <p>{product["description"]}</p>
            <p class="price">{product["price"]}</p>
            <p>{product["duration"]}</p>
        </div>
        """, unsafe_allow_html=True)

st.divider()

st.header("INSIGNIA Premium Mentorship")

cols = st.columns(3)

for index, plan in enumerate(INSIGNIA):
    with cols[index]:
        st.markdown(f"""
        <div class="card">
            <div class="badge">Premium Mentorship</div>
            <h3>{plan["title"]}</h3>
            <p>{plan["description"]}</p>
            <p class="price">{plan["price"]}</p>
            <p>{plan["duration"]}</p>
        </div>
        """, unsafe_allow_html=True)

st.divider()

st.header("INVESMATE AI Advisor")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! I am your INVESMATE AI Advisor. Ask me about courses, pricing, enrollment, or INSIGNIA mentorship."
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

    user_text = prompt.lower()

    if "price" in user_text or "fee" in user_text:
        reply = (
            "Course pricing starts from Rs. 3,999 and goes up depending on the program. "
            "INSIGNIA premium mentorship plans start from Rs. 38,571. "
            "For exact GST, EMI, and batch details, contact the counseling team."
        )
    elif "insignia" in user_text:
        reply = (
            "INSIGNIA is INVESMATE's premium mentorship journey. It includes structured learning, "
            "practical sessions, 1:1 mentorship, academic support, and premium market access."
        )
    elif "enroll" in user_text or "join" in user_text:
        reply = (
            "Enrollment flow: choose a product, request counseling, confirm fee/GST/EMI/batch timing, "
            "complete payment, then access classes through the learning app."
        )
    elif "contact" in user_text or "support" in user_text:
        reply = (
            "You can contact INVESMATE at +91 9016791791, +91 7596037781, "
            "+91 7003110622, or email support@invesmate.com."
        )
    else:
        reply = (
            "Based on your query, I recommend using the AI Course Predictor above. "
            "For beginners, the Power of Trading and Investing Combo Course is a good starting point. "
            "For advanced learners, INSIGNIA mentorship is better."
        )

    reply += "\n\nNote: Investment in securities markets is subject to market risks."

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.write(reply)

st.markdown("""
<div class="footer">
    <strong>INVESMATE</strong><br>
    Stock Market Learning Platform<br>
    SEBI Registered RA: INH000017985<br>
    support@invesmate.com | sales@invesmate.com<br><br>
    Investment in securities markets is subject to market risks.
</div>
""", unsafe_allow_html=True)
