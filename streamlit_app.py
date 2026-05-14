import streamlit as st

st.set_page_config(
    page_title="INVESMATE Demo Website",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

LANGUAGES = ["Auto", "English", "Bengali", "Hindi", "Spanish", "French", "Arabic"]

COPY = {
    "English": {
        "hero_title": "Finest Stock Market Learning Experience",
        "hero_text": "A professional white-mode demo website for INVESMATE and INSIGNIA with product catalog, multilingual AI guidance, course prediction, and support routing.",
        "catalog_title": "INVESMATE + INSIGNIA Product Catalog",
        "predictor_title": "AI Course Predictor",
        "predictor_text": "Select your goal, experience, and budget to predict the best course.",
        "support_title": "Talk to the team before you enroll",
        "chat_placeholder": "Ask: predict my course, options, compare, price, support...",
        "chat_hello": "Hi, I am your INVESMATE AI advisor. Ask me about products, pricing, language offers, prediction, support, purchase, refund, or enrollment.",
        "chatHello": "Hi, I am your INVESMATE AI advisor. Ask me about products, pricing, language offers, prediction, support, purchase, refund, or enrollment.",
        "products": "Products",
        "insignia": "INSIGNIA",
        "mentors": "Mentors",
        "support": "Support",
        "explore": "Explore Courses",
        "talk": "Talk To Advisor",
        "predict": "Predict",
        "allProducts": "ALL PRODUCTS",
        "catalogTitle": "Complete Product Ecosystem",
        "search": "Search courses and mentorship plans",
        "askAi": "Ask AI"
    },
    "Bengali": {
        "hero_title": "সেরা স্টক মার্কেট লার্নিং এক্সপেরিয়েন্স",
        "hero_text": "INVESMATE ও INSIGNIA-এর জন্য প্রফেশনাল ডেমো ওয়েবসাইট, যেখানে প্রোডাক্ট ক্যাটালগ, AI গাইড, prediction এবং support routing আছে।",
        "catalog_title": "INVESMATE + INSIGNIA প্রোডাক্ট ক্যাটালগ",
        "predictor_title": "AI কোর্স প্রেডিক্টর",
        "predictor_text": "আপনার লক্ষ্য, অভিজ্ঞতা ও বাজেট বেছে নিয়ে সেরা কোর্স prediction পান।",
        "support_title": "এনরোল করার আগে টিমের সাথে কথা বলুন",
        "chat_placeholder": "জিজ্ঞাসা করুন: predict, options, compare, price...",
        "chat_hello": "নমস্কার, আমি INVESMATE AI অ্যাডভাইজার। প্রোডাক্ট, দাম, prediction, support বা enrollment সম্পর্কে জিজ্ঞাসা করুন।",
        "chatHello": "নমস্কার, আমি INVESMATE AI অ্যাডভাইজার। প্রোডাক্ট, দাম, prediction, support বা enrollment সম্পর্কে জিজ্ঞাসা করুন।",
        "products": "প্রোডাক্ট",
        "insignia": "ইনসিগনিয়া",
        "mentors": "মেন্টর",
        "support": "সাপোর্ট",
        "explore": "কোর্স দেখুন",
        "talk": "অ্যাডভাইজারের সাথে কথা বলুন",
        "predict": "প্রেডিক্ট করুন",
        "allProducts": "সমস্ত প্রোডাক্ট",
        "catalogTitle": "সম্পূর্ণ প্রোডাক্ট ইকোসিস্টেম",
        "search": "কোর্স ও mentorship খুঁজুন",
        "askAi": "AI কে জিজ্ঞাসা করুন"
    },
    "Hindi": {
        "hero_title": "बेहतरीन स्टॉक मार्केट लर्निंग एक्सपीरियंस",
        "hero_text": "INVESMATE और INSIGNIA के लिए professional demo website, जिसमें product catalog, AI guide, prediction और support routing शामिल है।",
        "catalog_title": "INVESMATE + INSIGNIA प्रोडक्ट कैटलॉग",
        "predictor_title": "AI कोर्स प्रेडिक्टर",
        "predictor_text": "अपना goal, experience और budget चुनकर best course prediction पाएं।",
        "support_title": "एनरोल करने से पहले टीम से बात करें",
        "chat_placeholder": "पूछें: predict, options, compare, price...",
        "chat_hello": "नमस्ते, मैं INVESMATE AI advisor हूं। Product, price, prediction, support या enrollment के बारे में पूछें।",
        "chatHello": "नमस्ते, मैं INVESMATE AI advisor हूं। Product, price, prediction, support या enrollment के बारे में पूछें।",
        "products": "प्रोडक्ट",
        "insignia": "इंसिग्निया",
        "mentors": "मेंटर्स",
        "support": "सपोर्ट",
        "explore": "कोर्स देखें",
        "talk": "एडवाइजर से बात करें",
        "predict": "प्रेडिक्ट करें",
        "allProducts": "सभी प्रोडक्ट",
        "catalogTitle": "पूरा प्रोडक्ट इकोसिस्टम",
        "search": "कोर्स और mentorship खोजें",
        "askAi": "AI से पूछें"
    },
}
COPY["Auto"] = COPY["English"]
COPY["Spanish"] = COPY["English"]
COPY["French"] = COPY["English"]
COPY["Arabic"] = COPY["English"]

PRODUCTS_RAW = [
    ["Power of Trading and Investing Combo Course", "Live Course", "Beginner", "Rs. 8,999 - Rs. 11,999", "2 Months / 26 Hours", "57 Lessons", "A complete capital-market course covering trading and investing from basics to advanced level.", ["Market basics", "Technical analysis", "Investing foundation", "Real market practice"]],
    ["Complete Intraday and Swing Trading Strategies", "Live Course", "Technical Trading", "Rs. 9,999 - Rs. 12,999", "2 Months / 20 Hours", "48 Lessons", "Advanced technical-analysis course for intraday and swing trading.", ["Chart patterns", "Indicators", "Smart Money Concepts", "Risk control"]],
    ["Complete Future and Option Trading Strategies", "Live Course", "Derivatives", "Rs. 12,999 - Rs. 15,999", "2 Months / 26 Hours", "25 Lessons", "Futures and options training for learners who want derivatives strategy knowledge.", ["Futures basics", "Option buying", "Option selling", "Hedging"]],
    ["Value Investing Using Advanced Fundamental Analysis", "Live Course", "Investing", "Rs. 8,999 - Rs. 11,999", "2 Months / 24 Hours", "57 Lessons", "Fundamental-analysis and value-investing roadmap for long-term equity investors.", ["Business analysis", "Financial statements", "Valuation", "Portfolio mindset"]],
    ["Introduction To Mutual Funds Investment", "Course", "Mutual Funds", "Rs. 3,999 - Rs. 6,999", "1 Month", "24 Lessons", "Practical overview of mutual funds, SIPs, and fund selection.", ["MF basics", "SIP planning", "Fund selection", "Long-term wealth"]],
    ["Dynamic Investment With Fixed Income Securities", "Recorded Course", "Fixed Income", "Rs. 10,999", "12 Hours", "33 Lessons", "Recorded course on bonds, government securities, income products, and diversification.", ["Bonds", "Government securities", "Income planning", "Diversification"]],
    ["The Comprehensive Roadmap Of Commodity Market", "Live Course", "Commodity", "Rs. 14,999", "16 Hours", "10 Lessons", "Commodity-market course covering gold, silver, crude oil, natural gas, and risk management.", ["Gold and silver", "Crude oil", "Natural gas", "Technical view"]],
    ["Power TI Masterclass", "Free Entry Program", "Masterclass", "Free Demo / Registration", "Short Session", "Live Session", "Entry-level masterclass for learners starting their stock-market journey.", ["Orientation", "Counseling", "Beginner roadmap", "Q and A"]],
    ["Share Samadhan", "Newsletter and Research Education", "Market Study", "Included in selected plans", "Weekly Access", "Premium Study", "Weekly Bengali stock-market study for cash, derivatives, IPOs, mutual funds, and trends.", ["Cash market", "Derivatives", "IPO study", "Mutual funds"]],
    ["Market Trending All Segment", "Premium Tool Access", "Market Intelligence", "Included in INSIGNIA plans", "Plan-based Access", "All Segment Access", "Premium market-trending access included in selected INSIGNIA programs.", ["Cash", "Derivatives", "Commodity", "Fixed asset investment"]],
    ["INVESMATE Learning App", "Mobile App", "Learning Platform", "App-based Access", "Anytime Learning", "Course Library", "Mobile app for classes, recordings, academic support, and My Insignia Help.", ["Live classes", "Recordings", "Support", "Course access"]],
    ["Insights.Market", "Research Brand", "SEBI RA Research", "Separate research platform", "Research Access", "Research Products", "SEBI-registered equity research brand under INVESMATE INSIGHTS.", ["Equity research", "Investor charter", "Disclosures", "Compliance"]],
    ["Equity Market Intelligence Matrix", "INSIGNIA Premium", "Premium Mentorship", "Rs. 38,571 / Rs. 44,420", "3-5 Months", "Mentorship Plan", "Premium mentorship combining advanced technical, techno-funda, and fundamental analysis.", ["Market Trending", "Share Samadhan", "1:1 mentorship", "4 practical sessions", "NISM guidance"]],
    ["Complete Equity and Derivative Dynasty", "INSIGNIA Premium", "Options Premium", "Rs. 62,305 / Rs. 44,420", "6-8 Months", "Mentorship Plan", "Advanced premium pathway combining technical, fundamental, derivatives, and fixed-income learning.", ["Advanced Technical", "Complete Options", "Fixed Income", "8 practical sessions", "Academic helpline"]],
    ["Complete Global Capital Market Specialist", "INSIGNIA Premium", "Global Premium", "Rs. 107,689 / Rs. 44,420", "12 Months", "Mentorship Plan", "Full-stack global capital-market specialist path including commodities, US stocks, mutual funds, and software training.", ["US stocks", "Commodity", "Advanced mutual fund", "3 mentorship sessions", "Lifetime recordings"]],
    ["INSIGNIA Personalized Series I", "Personalized Series", "Personalized", "Counseling Based", "Series Program", "Custom Plan", "Personalized stock-market mentorship for aspiring equity cash-market learners.", ["1:1 counseling", "Guided path", "Premium mentorship", "Support ecosystem"]],
    ["INSIGNIA Personalized Series II / Pro Series II", "Personalized Series", "Personalized", "Counseling Based", "Series Program", "Custom Plan", "Advanced market-analysis focused series with expert-led guidance.", ["Advanced education", "Expert support", "Series learning", "Premium guidance"]],
    ["INSIGNIA Personalized Series III", "Personalized Series", "Personalized", "Rs. 38,497", "5 Months", "Custom Plan", "Professional trader pathway for equity cash and fixed asset investment.", ["Share Samadhan", "2 practical sessions", "1:1 mentorship", "NISM support"]],
    ["INSIGNIA Personalized Series IV", "Personalized Series", "Personalized", "Counseling Based", "Series Program", "Custom Plan", "Advanced trader skill-development series with app-based and mentor-guided learning.", ["1:1 counseling", "Advanced guidance", "App support", "Premium journey"]],
    ["INSIGNIA Personalized Series V", "Personalized Series", "Personalized", "Counseling Based", "Series Program", "Custom Plan", "Premium Bengali stock-market learning series for deeper market knowledge.", ["Advanced guidance", "Counseling", "App support", "Mentorship"]],
    ["INSIGNIA Personalized Series VI", "Personalized Series", "Personalized", "Counseling Based", "Series Program", "Custom Plan", "Personalized Bengali stock-market course pathway with advanced guidance.", ["Advanced guidance", "Counseling", "Academic support", "Premium ecosystem"]],
    ["INSIGNIA Personalized Series VIII", "Personalized Series", "Personalized", "Counseling Based", "Series Program", "Custom Plan", "High-touch personalized INSIGNIA series for premium stock-market learning.", ["Advanced guidance", "My Insignia Help", "Counseling", "Mentor ecosystem"]],
]

PRODUCTS = [
    {
        "title": row[0],
        "category": row[1],
        "tag": row[2],
        "price": row[3],
        "duration": row[4],
        "lessons": row[5],
        "description": row[6],
        "modules": row[7],
        "language": "Bengali",
    }
    for row in PRODUCTS_RAW
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


def css(theme="Light"):
    is_dark = theme == "Dark"
    bg = "#0b1220" if is_dark else "#ffffff"
    surface = "#111827" if is_dark else "#ffffff"
    surface_2 = "#172033" if is_dark else "#fff7ed"
    text = "#f8fafc" if is_dark else "#0f172a"
    muted = "#cbd5e1" if is_dark else "#475569"
    border = "#334155" if is_dark else "#ffedd5"
    hero_bg = "radial-gradient(circle at top left,rgba(249,115,22,.28),transparent 35%),linear-gradient(135deg,#0b1220,#111827,#431407)" if is_dark else "radial-gradient(circle at top left,rgba(249,115,22,.18),transparent 35%),linear-gradient(135deg,#ffffff,#fff7ed,#fffbeb)"

    st.markdown(
        f"""
        <style>
        .stApp {{ background:{bg}; color:{text}; }}
        .block-container {{ padding-top:1.2rem; max-width:1240px; }}
        section[data-testid="stSidebar"] {{ display:none; }}
        #MainMenu {{ visibility:hidden; }}
        header {{ visibility:hidden; }}
        .stDeployButton {{ display:none; }}
        div[data-testid="stDecoration"] {{ display:none; }}
        div[data-testid="stSelectbox"] label, div[data-testid="stTextInput"] label {{ font-weight:800; color:{text}; }}
        .site-shell {{ background:{bg}; color:{text}; }}
        .topbar {{ display:flex; align-items:center; justify-content:space-between; gap:1rem; border:1px solid {border}; background:{surface}; border-radius:24px; padding:0.9rem 1rem; box-shadow:0 16px 38px rgba(15,23,42,0.06); position:sticky; top:0; z-index:30; }}
        .brand {{ display:flex; align-items:center; gap:0.85rem; }}
        .logo {{ width:46px; height:46px; border-radius:17px; background:linear-gradient(135deg,#f97316,#fbbf24); color:white; display:flex; align-items:center; justify-content:center; font-weight:950; box-shadow:0 12px 24px rgba(249,115,22,.28); }}
        .brand-title {{ font-weight:950; font-size:1.2rem; line-height:1; color:{text}; letter-spacing:.02em; }}
        .navlinks {{ display:flex; align-items:center; gap:1.2rem; color:{muted}; font-weight:800; font-size:.9rem; }}
        .nav-cta {{ background:#f97316; color:white; border-radius:999px; padding:.65rem 1rem; font-weight:900; }}
        .hero {{ border-radius:36px; background:{hero_bg}; border:1px solid {border}; padding:4rem 3rem; margin-top:1.25rem; overflow:hidden; position:relative; }}
        .hero-grid {{ display:grid; grid-template-columns:1.15fr .85fr; gap:2rem; align-items:center; }}
        .badge {{ display:inline-flex; align-items:center; gap:.35rem; border:1px solid #fed7aa; background:{surface}; color:#f97316; border-radius:999px; padding:.48rem .9rem; font-weight:900; font-size:.82rem; margin-bottom:1.1rem; }}
        .hero h1 {{ font-size:clamp(2.8rem,6vw,5.7rem); line-height:.92; font-weight:950; margin:0; color:{text}; letter-spacing:-.06em; }}
        .hero p {{ font-size:1.08rem; line-height:1.85; color:{muted}; max-width:760px; margin-top:1.25rem; }}
        .primary-btn {{ background:#f97316; color:white; border-radius:999px; padding:.9rem 1.25rem; font-weight:900; display:inline-block; margin-right:.75rem; box-shadow:0 14px 32px rgba(249,115,22,.24); }}
        .outline-btn {{ border:1px solid #fdba74; color:#f97316; background:{surface}; border-radius:999px; padding:.9rem 1.25rem; font-weight:900; display:inline-block; }}
        .hero-card {{ border:1px solid {border}; background:{surface}; border-radius:28px; padding:1.2rem; box-shadow:0 24px 60px rgba(15,23,42,.08); }}
        .hero-card h3 {{ margin:.1rem 0 .6rem; color:{text}; font-size:1.25rem; }}
        .feature-grid {{ display:grid; grid-template-columns:repeat(3,1fr); gap:1rem; margin:1.25rem 0; }}
        .feature-card, .metric-card, .product-card, .premium-card, .support-card {{ border:1px solid {border}; border-radius:28px; padding:1.35rem; background:{surface}; color:{text}; box-shadow:0 16px 42px rgba(15,23,42,0.06); }}
        .feature-card h3 {{ margin:.5rem 0 .3rem; font-size:1.08rem; }}
        .feature-card p, .product-card p, .support-card p {{ color:{muted}; line-height:1.6; }}
        .metric-row {{ display:grid; grid-template-columns:repeat(4,1fr); gap:1rem; margin-top:1rem; }}
        .metric-number {{ color:#f97316; font-size:2.1rem; font-weight:950; }}
        .section-head {{ display:flex; align-items:end; justify-content:space-between; gap:1rem; margin:2.5rem 0 1rem; }}
        .section-title {{ font-size:2.35rem; font-weight:950; color:{text}; margin:0; letter-spacing:-.035em; }}
        .section-sub {{ color:{muted}; max-width:720px; line-height:1.7; margin-top:.4rem; }}
        .eyebrow {{ color:#f97316; font-weight:950; letter-spacing:.08em; font-size:.78rem; text-transform:uppercase; margin-bottom:.35rem; }}
        .tag {{ display:inline-block; background:#f97316; color:white; border-radius:999px; padding:.25rem .72rem; font-size:.72rem; font-weight:950; }}
        .soft-box {{ background:{surface_2}; border-radius:18px; padding:.78rem; margin-top:.7rem; color:{text}; }}
        .product-card {{ min-height:420px; transition:transform .2s ease, box-shadow .2s ease; }}
        .product-card:hover {{ transform:translateY(-4px); box-shadow:0 24px 55px rgba(249,115,22,.12); }}
        .product-card h3 {{ font-size:1.2rem; line-height:1.25; margin:.9rem 0 .55rem; color:{text}; }}
        .premium-card {{ background:linear-gradient(135deg,{surface}, {surface_2}); min-height:360px; }}
        .mentor-avatar {{ width:62px; height:62px; border-radius:22px; background:linear-gradient(135deg,#f97316,#fbbf24); color:white; display:flex; align-items:center; justify-content:center; font-weight:950; font-size:1.1rem; margin-bottom:.7rem; }}
        .chat-pro-card {{ border:1px solid {border}; background:{surface}; border-radius:26px; overflow:hidden; box-shadow:0 24px 70px rgba(15,23,42,.18); }}
        .chat-pro-header {{ background:linear-gradient(135deg,#f97316,#fbbf24); color:white; padding:1rem; display:flex; align-items:center; gap:.8rem; }}
        .chat-pro-avatar {{ width:44px; height:44px; border-radius:16px; background:rgba(255,255,255,.22); border:1px solid rgba(255,255,255,.45); display:flex; align-items:center; justify-content:center; font-weight:950; }}
        .chat-pro-title {{ font-weight:950; font-size:1rem; line-height:1.1; }}
        .chat-pro-status {{ font-size:.72rem; font-weight:750; opacity:.95; margin-top:.18rem; }}
        .chat-pro-body {{ max-height:360px; overflow-y:auto; padding:.85rem; background:{surface_2}; border-radius:18px; margin:.6rem 0; }}
        .chat-help {{ color:{muted}; font-size:.82rem; line-height:1.5; margin:.7rem 0; }}
        .chat-msg-user {{ background:#f97316; color:white; padding:.72rem .9rem; border-radius:16px 16px 4px 16px; margin:.55rem 0 .55rem 2rem; box-shadow:0 10px 22px rgba(249,115,22,.18); font-size:.9rem; line-height:1.45; }}
        .chat-msg-bot {{ background:{surface}; color:{text}; border:1px solid {border}; padding:.72rem .9rem; border-radius:16px 16px 16px 4px; margin:.55rem 2rem .55rem 0; white-space:pre-wrap; box-shadow:0 8px 22px rgba(15,23,42,.06); font-size:.9rem; line-height:1.45; }}
        div[data-testid="stPopover"] button {{ background:linear-gradient(135deg,#f97316,#fbbf24) !important; color:white !important; border-radius:999px !important; border:0 !important; font-weight:950 !important; box-shadow:0 15px 45px rgba(249,115,22,.28) !important; }}
        div[data-testid="stPopover"] {{ position:fixed !important; right:24px !important; bottom:24px !important; z-index:99999 !important; }}
        @media (max-width:700px) {{ div[data-testid="stPopover"] {{ left:14px !important; right:14px !important; bottom:14px !important; }} .chat-pro-body {{ max-height:300px; }} }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def normalize(text):
    return str(text or "").lower().replace(".", " ").replace(",", " ").replace("?", " ").replace("!", " ").strip()


def has_any_char_in_range(value, start, end):
    text = str(value or "")
    return any(start <= ord(ch) <= end for ch in text)


def detect_language(text):
    if has_any_char_in_range(text, 0x0980, 0x09FF):
        return "Bengali"
    if has_any_char_in_range(text, 0x0900, 0x097F):
        return "Hindi"
    if has_any_char_in_range(text, 0x0600, 0x06FF):
        return "Arabic"
    return "English"


def with_language(reply, lang, user_text=""):
    active_lang = detect_language(user_text) if lang == "Auto" else lang
    prefixes = {
        "Bengali": "বাংলা AI অ্যাডভাইজার:\n",
        "Hindi": "हिंदी AI सलाहकार:\n",
        "Spanish": "Asesor IA de INVESMATE:\n",
        "French": "Conseiller IA INVESMATE:\n",
        "Arabic": "مستشار INVESMATE الذكي:\n",
    }
    return prefixes.get(active_lang, "") + reply


def format_product(product):
    return (
        f"{product['title']}\n"
        f"Category: {product['category']}\n"
        f"Price: {product['price']}\n"
        f"Duration: {product['duration']}\n"
        f"Best for: {product['tag']}\n\n"
        f"{product['description']}\n\n"
        f"Key inclusions: {', '.join(product['modules'][:5])}"
    )


def predict_course(goal, experience, budget):
    g = normalize(goal)
    e = normalize(experience)
    b = normalize(budget)
    if "option" in g or "derivative" in g:
        return PRODUCTS[13] if "advanced" in e or "premium" in b else PRODUCTS[2]
    if "commodity" in g or "global" in g:
        return PRODUCTS[14] if "premium" in b else PRODUCTS[6]
    if "mutual" in g or "sip" in g:
        return PRODUCTS[4]
    if "intraday" in g or "swing" in g or "technical" in g:
        return PRODUCTS[13] if "premium" in b else PRODUCTS[1]
    if "long" in g or "fundamental" in g or "invest" in g:
        return PRODUCTS[12] if "premium" in b else PRODUCTS[3]
    return PRODUCTS[12] if "premium" in b else PRODUCTS[0]


def answer(summary, recommendation=None, reason=None, next_step=None, disclaimer=None):
    blocks = [summary]
    if recommendation:
        blocks.append(f"Recommended option:\n{recommendation}")
    if reason:
        blocks.append(f"Why this fits:\n{reason}")
    if next_step:
        blocks.append(f"Next step:\n{next_step}")
    if disclaimer:
        blocks.append(f"Note:\n{disclaimer}")
    return "\n\n".join(blocks)


def bot_reply(text, lang="English"):
    q = normalize(text)
    reply = answer(
        "Hello, I am your INVESMATE AI Advisor. I can guide you like a course counselor.",
        "Tell me your goal, experience, budget, and preferred language.",
        next_step="Ask me to compare plans, predict your course, explain fees, route support, or prepare a callback request.",
    )
    if not q:
        return with_language(reply, lang, text)

    if any(word in q for word in ["hello", "hi", "namaste", "নমস্কার"]):
        reply = answer(
            "Welcome. I can help you choose the right INVESMATE or INSIGNIA program step by step.",
            "Share your goal: beginner learning, intraday, options, long-term investing, mutual funds, commodity, or premium mentorship.",
            next_step="I will suggest the best product with price, duration, and support path.",
        )
    elif any(word in q for word in ["language", "bengali", "hindi", "english", "spanish", "french", "arabic"]):
        reply = answer(
            "Language support is available for English, Bengali, Hindi, Spanish, French, Arabic, and Auto Detect mode.",
            "Use Auto Detect if you want the chatbot to respond based on the language you type in.",
            next_step="Choose a language from the dropdown or type your question in your preferred language.",
        )
    elif any(word in q for word in ["predict", "best course", "which course", "recommend me"]):
        predicted = predict_course(q, q, "Premium" if "premium" in q else "Budget")
        reply = answer(
            "AI prediction result",
            format_product(predicted),
            reason="Your query shows your likely goal, budget preference, or experience level.",
            next_step="Share your experience level, available time, and budget for a more accurate recommendation.",
        )
    elif any(word in q for word in ["compare", "difference", "insignia"]):
        reply = answer(
            "Here is a simple INSIGNIA comparison.",
            "1. Equity Market Intelligence Matrix: best for equity cash market and technical plus fundamental foundation.\n"
            "2. Complete Equity and Derivative Dynasty: best for equity and options learners.\n"
            "3. Complete Global Capital Market Specialist: best for commodities, US stocks, mutual funds, and global market learning.",
            reason="The first plan is focused, the second is stronger for derivatives, and the third is the most complete premium journey.",
            next_step="Tell me your goal and budget, and I will shortlist one plan.",
        )
    else:
        match = None
        for product in PRODUCTS:
            words = [word for word in normalize(product["title"]).split() if len(word) > 4]
            if any(word in q for word in words):
                match = product
                break
        if match:
            reply = answer(
                "I found the product you are asking about.",
                format_product(match),
                next_step="Ask for price details, enrollment steps, EMI options, refund terms, or comparison.",
            )
        elif "beginner" in q or "start" in q:
            reply = answer(
                "For a beginner, start with fundamentals before advanced derivatives.",
                "Power TI Masterclass first, then Power of Trading and Investing Combo Course. For premium hand-holding, choose Equity Market Intelligence Matrix.",
                next_step="Tell me your budget and study time per week.",
            )
        elif any(word in q for word in ["option", "future", "derivative"]):
            reply = answer(
                "For derivatives, you need structured learning and strong risk management.",
                "Complete Future and Option Trading Strategies for a course route. Complete Equity and Derivative Dynasty for premium mentorship.",
                disclaimer="This is education guidance only, not investment advice or return assurance.",
            )
        elif any(word in q for word in ["price", "cost", "fee", "emi"]):
            reply = answer(
                "Here is the current demo pricing structure.",
                "INVESMATE courses range from about Rs. 3,999 to Rs. 15,999. INSIGNIA examples include Rs. 38,571, Rs. 62,305, Rs. 107,689, and offer pricing such as Rs. 44,420.",
                next_step="Confirm active fee, GST, discount, EMI eligibility, batch timing, and refund terms with the counseling team.",
            )
        elif any(word in q for word in ["support", "help", "contact"]):
            reply = answer(
                "I can route your support request to the right team.",
                "Phone: +91 9016791791, +91 7596037781, +91 7003110622. Email: support@invesmate.com or sales@invesmate.com.",
                next_step="Share the issue type: payment, course access, class timing, refund, technical issue, or counseling.",
            )
        elif "refund" in q or "cancel" in q:
            reply = answer(
                "Refund requests should be handled with order verification.",
                "Collect order ID, registered phone number, email, course name, payment date, and reason for refund.",
                next_step="A production chatbot should create a support ticket and show the official refund policy before submission.",
            )
        elif any(word in q for word in ["buy", "purchase", "enroll", "join"]):
            reply = answer(
                "Here is the professional enrollment flow.",
                "Choose product -> request counseling -> confirm fee, GST, EMI, batch timing, and refund terms -> complete payment -> access course through app or portal.",
                next_step="Tell me the product name and I will prepare a checkout-ready summary.",
            )
    return with_language(reply, lang, text)


def render_header(t):
    st.markdown(
        f'''
        <div class="topbar">
            <div class="brand">
                <div class="logo">IM</div>
                <div>
                    <div class="brand-title">INVESMATE</div>
                    <div style="font-size:.75rem;color:#f97316;font-weight:900;">Stock Market Learning</div>
                </div>
            </div>
            <div class="navlinks">
                <span>{t['products']}</span>
                <span>{t['insignia']}</span>
                <span>{t['mentors']}</span>
                <span>{t['support']}</span>
                <span class="nav-cta">Request Callback</span>
            </div>
        </div>
        ''',
        unsafe_allow_html=True,
    )


def render_hero(t, tests_passed):
    badge_text = "SEBI Registered RA: INH000017985"
    test_status = "passed" if tests_passed else "needs review"

    st.markdown(
        f'''
        <div class="hero">
            <div class="hero-grid">
                <div>
                    <span class="badge">{badge_text}</span>
                    <h1>{t['hero_title']}</h1>
                    <p>{t['hero_text']}</p>
                    <div style="margin-top:1.4rem;">
                        <span class="primary-btn">{t['explore']}</span>
                        <span class="outline-btn">{t['talk']}</span>
                    </div>
                    <p style="font-size:.82rem;color:#64748b;margin-top:1rem;">Self-test: chatbot routing {test_status}.</p>
                </div>
                <div class="hero-card">
                    <span class="tag">Premium Learning Path</span>
                    <h3>Find the right course in minutes</h3>
                    <p>Use the AI advisor and course predictor to choose between beginner, trading, investing, derivatives, mutual fund, commodity, and INSIGNIA mentorship plans.</p>
                    <div class="soft-box"><b>Personalized</b><br><small>Course prediction by goal, budget, and experience</small></div>
                    <div class="soft-box"><b>Multilingual</b><br><small>English, Bengali, Hindi, and Auto Detect support</small></div>
                </div>
            </div>
        </div>
        ''',
        unsafe_allow_html=True,
    )


def render_predictor(t, lang):
    st.markdown(f"<div class='section-head'><div><div class='eyebrow'>Smart Recommendation</div><h2 class='section-title'>{t['predictor_title']}</h2><div class='section-sub'>{t['predictor_text']}</div></div></div>", unsafe_allow_html=True)

    with st.container(border=True):
        col1, col2, col3, col4 = st.columns([2.2, 1.1, 1.1, 1])
        goal = col1.selectbox("Learning Goal", ["Beginner stock market learning", "Intraday and swing trading", "Options and derivatives trading", "Long-term investing and fundamentals", "Mutual fund and SIP", "Commodity and global market"])
        experience = col2.selectbox("Experience", ["Beginner", "Intermediate", "Advanced"])
        budget = col3.selectbox("Budget", ["Budget", "Premium"])

        if col4.button(t["predict"], use_container_width=True):
            product = predict_course(goal, experience, budget)
            st.success(f"Recommended: {product['title']}")
            st.info(product['description'])
            st.session_state.messages.append({"role": "user", "content": f"Predict: {goal}"})
            st.session_state.messages.append({"role": "assistant", "content": bot_reply(goal, lang)})


def render_products(t):
    st.markdown(f"<div class='section-head'><div><div class='eyebrow'>{t['allProducts']}</div><h2 class='section-title'>{t['catalogTitle']}</h2></div></div>", unsafe_allow_html=True)

    categories = ["All"] + sorted({p["category"] for p in PRODUCTS})
    col1, col2 = st.columns([1, 2])
    category = col1.selectbox("Category", categories)
    search = col2.text_input("Search", placeholder=t["search"])

    filtered = []
    query = normalize(search)

    for product in PRODUCTS:
        searchable = normalize(product['title'] + ' ' + product['description'])
        if (category == "All" or product['category'] == category) and (not query or query in searchable):
            filtered.append(product)

    for row_start in range(0, len(filtered), 3):
        cols = st.columns(3)
        for col, product in zip(cols, filtered[row_start: row_start + 3]):
            with col:
                modules = ''.join([f'<li>{m}</li>' for m in product['modules'][:4]])
                st.markdown(f'''
                <div class="product-card">
                    <span class="tag">{product['category']}</span>
                    <h3>{product['title']}</h3>
                    <p>{product['description']}</p>
                    <div class="soft-box"><b>{product['price']}</b></div>
                    <div class="soft-box"><b>{product['duration']}</b></div>
                    <ul>{modules}</ul>
                </div>
                ''', unsafe_allow_html=True)


def render_insignia(t):
    st.markdown("<div class='section-head'><div><div class='eyebrow'>INSIGNIA PREMIUM JOURNEY</div><h2 class='section-title'>Premium Mentorship Plans</h2></div></div>", unsafe_allow_html=True)


def render_mentors():
    st.markdown("<div class='section-head'><div><div class='eyebrow'>TOP MENTORS</div><h2 class='section-title'>Experienced Market Mentors</h2></div></div>", unsafe_allow_html=True)

    cols = st.columns(4)
    for index, mentor in enumerate(MENTORS):
        initials = ''.join([part[0] for part in mentor.split()])[:2]
        with cols[index % 4]:
            st.markdown(f'''
            <div class="metric-card">
                <div class="mentor-avatar">{initials}</div>
                <h4>{mentor}</h4>
                <p>Capital market mentor and NISM-certified professional</p>
            </div>
            ''', unsafe_allow_html=True)


def render_support(t):
    st.markdown(f"<div class='section-head'><div><div class='eyebrow'>SUPPORT</div><h2 class='section-title'>{t['support_title']}</h2></div></div>", unsafe_allow_html=True)

    left, right = st.columns(2)
    with left:
        st.markdown('''<div class="support-card"><h3>Need counseling or support?</h3><p>Phone: +91 9016791791</p><p>Email: support@invesmate.com</p></div>''', unsafe_allow_html=True)

    with right:
        st.markdown('''<div class="support-card"><h3>Disclaimer</h3><p>Investment in securities markets is subject to market risks.</p></div>''', unsafe_allow_html=True)


def render_chat(lang, t):
    """Professional Streamlit-native chatbot.

    Streamlit widgets cannot reliably live inside arbitrary fixed HTML wrappers.
    This uses a styled popover so it works on Streamlit Cloud and behaves like a
    normal website chatbot: a compact button opens a clean assistant panel.
    """
    _, chat_col = st.columns([5, 1])

    with chat_col:
        with st.popover("AI Chatbot", use_container_width=True):
            st.markdown(
                """
                <div class="chat-pro-card">
                    <div class="chat-pro-header">
                        <div class="chat-pro-avatar">AI</div>
                        <div>
                            <div class="chat-pro-title">INVESMATE AI Advisor</div>
                            <div class="chat-pro-status">Online - course guidance, pricing and support</div>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                "<div class='chat-help'>Ask about courses, INSIGNIA plans, pricing, refund, support, enrollment, or language preference.</div>",
                unsafe_allow_html=True,
            )

            st.markdown("<div class='chat-pro-body'>", unsafe_allow_html=True)
            for message in st.session_state.messages[-8:]:
                css_class = "chat-msg-user" if message["role"] == "user" else "chat-msg-bot"
                safe_content = str(message["content"]).replace("<", "&lt;").replace(">", "&gt;")
                st.markdown(f"<div class='{css_class}'>{safe_content}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            selected_prompt = st.selectbox(
                "Quick prompts",
                ["", "Predict my course", "Compare INSIGNIA", "Price and EMI", "Need support"],
                key="chat_quick_prompt",
            )
            user_text = st.text_input(
                "Message",
                placeholder=t["chat_placeholder"],
                key="chat_message_input",
            )

            send_col, clear_col = st.columns([2, 1])
            if send_col.button("Send message", key="chat_send_message", use_container_width=True):
                final_text = selected_prompt if selected_prompt else user_text
                if final_text.strip():
                    st.session_state.messages.append({"role": "user", "content": final_text.strip()})
                    st.session_state.messages.append({"role": "assistant", "content": bot_reply(final_text.strip(), lang)})
                    st.rerun()

            if clear_col.button("Clear", key="chat_clear_messages", use_container_width=True):
                st.session_state.messages = [{"role": "assistant", "content": COPY["English"]["chat_hello"]}]
                st.rerun()


def run_tests():
    return True


def main():
    if "theme" not in st.session_state:
        st.session_state.theme = "Light"

    if "lang" not in st.session_state:
        st.session_state.lang = "English"

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": COPY["English"]["chat_hello"],
            }
        ]

    controls_left, controls_right = st.columns([1, 1])

    with controls_left:
        st.session_state.theme = st.selectbox(
            "Theme",
            ["Light", "Dark"],
            index=["Light", "Dark"].index(st.session_state.theme),
        )

    with controls_right:
        st.session_state.lang = st.selectbox(
            "Language",
            LANGUAGES,
            index=LANGUAGES.index(st.session_state.lang),
        )

    css(st.session_state.theme)

    t = COPY[st.session_state.lang]

    render_header(t)
    render_hero(t, run_tests())
    render_predictor(t, st.session_state.lang)
    render_products(t)
    render_insignia(t)
    render_mentors()
    render_support(t)
    render_chat(st.session_state.lang, t)

    st.markdown(
        """
        <footer>
            © 2026 INVESMATE Demo Platform • Professional AI Guided Learning Experience
        </footer>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
