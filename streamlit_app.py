import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="INVESMATE - Stock Market Learning Platform",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit UI
st.markdown("""
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
    padding-left: 0rem;
    padding-right: 0rem;
    max-width: 100%;
}
iframe {
    border-radius: 0px !important;
}
</style>
""", unsafe_allow_html=True)

html_code = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>

<title>INVESMATE - Stock Market Learning Platform</title>

<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>

<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet"/>

<style>

:root{
    --bg:#fafaf8;
    --surface:#ffffff;
    --surface2:#f5f3ee;
    --surface3:#ede9e0;
    --text:#1a1208;
    --text2:#6b6150;
    --text3:#a09880;
    --accent:#d4601a;
    --accent2:#f08d3c;
    --accent3:#fbbf24;
    --border:#e6e0d4;
    --border2:#d4ccbe;
    --shadow:0 4px 24px rgba(26,18,8,0.08);
    --shadow2:0 16px 48px rgba(26,18,8,0.12);
    --radius:20px;
    --radius2:12px;
    --radius3:999px;
}

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

html{
    scroll-behavior:smooth;
}

body{
    font-family:'DM Sans',sans-serif;
    background:var(--bg);
    color:var(--text);
    overflow-x:hidden;
}

/* NAV */

nav{
    position:sticky;
    top:0;
    z-index:100;
    background:rgba(250,250,248,0.92);
    backdrop-filter:blur(20px);
    border-bottom:1px solid var(--border);
    padding:0 2rem;
    display:flex;
    justify-content:space-between;
    align-items:center;
    height:72px;
}

.nav-brand{
    display:flex;
    align-items:center;
    gap:14px;
}

.nav-logo{
    width:46px;
    height:46px;
    border-radius:14px;
    background:linear-gradient(135deg,var(--accent),var(--accent3));
    display:flex;
    align-items:center;
    justify-content:center;
    color:white;
    font-weight:800;
    font-family:'Syne',sans-serif;
}

.nav-title{
    font-family:'Syne',sans-serif;
    font-weight:800;
    font-size:20px;
}

.nav-tagline{
    font-size:11px;
    color:var(--accent);
    font-weight:700;
    letter-spacing:1px;
}

.nav-links{
    display:flex;
    align-items:center;
    gap:2rem;
}

.nav-links a{
    text-decoration:none;
    color:var(--text2);
    font-weight:500;
}

.nav-links a:hover{
    color:var(--text);
}

.nav-btn{
    background:var(--text);
    color:white!important;
    padding:12px 18px;
    border-radius:999px;
}

/* HERO */

.hero-section{
    max-width:1200px;
    margin:auto;
    padding:90px 30px 70px;
    display:grid;
    grid-template-columns:1fr 430px;
    gap:50px;
    align-items:center;
}

.hero-badge{
    display:inline-flex;
    align-items:center;
    gap:8px;
    background:var(--surface2);
    border:1px solid var(--border2);
    padding:8px 16px;
    border-radius:999px;
    font-size:13px;
    color:var(--accent);
    font-weight:700;
    margin-bottom:20px;
}

.hero h1{
    font-family:'Syne',sans-serif;
    font-size:78px;
    line-height:0.95;
    margin-bottom:24px;
    letter-spacing:-2px;
}

.hero h1 span{
    color:var(--accent);
}

.hero-sub{
    color:var(--text2);
    line-height:1.8;
    font-size:18px;
    margin-bottom:32px;
    max-width:650px;
}

.hero-actions{
    display:flex;
    gap:14px;
    flex-wrap:wrap;
}

.btn-primary{
    background:var(--accent);
    color:white;
    border:none;
    padding:15px 26px;
    border-radius:999px;
    font-weight:700;
    cursor:pointer;
    font-size:15px;
    box-shadow:0 8px 24px rgba(212,96,26,0.28);
}

.btn-outline{
    background:white;
    border:1px solid var(--border2);
    padding:15px 26px;
    border-radius:999px;
    font-weight:700;
    cursor:pointer;
    font-size:15px;
}

.hero-card{
    background:white;
    border-radius:24px;
    padding:30px;
    border:1px solid var(--border);
    box-shadow:var(--shadow2);
}

.hero-card-label{
    display:inline-block;
    background:var(--accent);
    color:white;
    padding:7px 14px;
    border-radius:999px;
    font-size:12px;
    font-weight:700;
    margin-bottom:18px;
}

.hero-card h3{
    font-size:24px;
    margin-bottom:12px;
    font-family:'Syne',sans-serif;
}

.hero-card p{
    color:var(--text2);
    margin-bottom:20px;
}

.info-row{
    background:var(--surface2);
    border-radius:14px;
    padding:14px;
    margin-top:12px;
}

/* STATS */

.stats-strip{
    background:#1a1208;
    color:white;
    display:grid;
    grid-template-columns:repeat(4,1fr);
    text-align:center;
    padding:34px 20px;
}

.stat-num{
    font-size:44px;
    font-weight:800;
    color:var(--accent2);
    font-family:'Syne',sans-serif;
}

.stat-label{
    color:rgba(255,255,255,0.65);
}

/* SECTIONS */

.section{
    max-width:1200px;
    margin:auto;
    padding:70px 30px;
}

.section-eyebrow{
    color:var(--accent);
    font-size:12px;
    font-weight:800;
    letter-spacing:2px;
    margin-bottom:10px;
}

.section-title{
    font-size:48px;
    font-family:'Syne',sans-serif;
    margin-bottom:12px;
}

.section-sub{
    color:var(--text2);
    line-height:1.8;
}

.divider{
    border:none;
    border-top:1px solid var(--border);
}

/* FILTER */

.filter-bar{
    display:flex;
    flex-wrap:wrap;
    gap:10px;
    margin-top:24px;
}

.filter-chip{
    padding:10px 16px;
    border-radius:999px;
    background:var(--surface2);
    border:1px solid var(--border);
    cursor:pointer;
    font-size:14px;
    font-weight:600;
}

.filter-chip.active{
    background:#1a1208;
    color:white;
}

.search-wrap{
    margin-top:22px;
    margin-bottom:30px;
}

.search-input{
    width:100%;
    max-width:420px;
    background:var(--surface2);
    border:1px solid var(--border);
    padding:16px 18px;
    border-radius:14px;
    font-size:15px;
}

/* PRODUCTS */

.products-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:24px;
}

.product-card{
    background:white;
    border:1px solid var(--border);
    border-radius:24px;
    padding:26px;
    box-shadow:var(--shadow);
    transition:0.25s;
}

.product-card:hover{
    transform:translateY(-5px);
    box-shadow:var(--shadow2);
}

.product-tag{
    display:inline-block;
    background:var(--surface2);
    color:var(--accent);
    padding:6px 12px;
    border-radius:999px;
    font-size:12px;
    font-weight:700;
    margin-bottom:14px;
}

.product-card h3{
    font-size:21px;
    margin-bottom:12px;
}

.product-card p{
    color:var(--text2);
    line-height:1.7;
}

.product-meta{
    margin-top:20px;
}

.meta-pill{
    background:var(--surface2);
    border-radius:12px;
    padding:12px;
    margin-top:10px;
    font-size:14px;
}

.modules-list{
    display:flex;
    flex-wrap:wrap;
    gap:8px;
    margin-top:16px;
}

.module-chip{
    background:var(--surface3);
    padding:6px 12px;
    border-radius:999px;
    font-size:12px;
}

/* PREMIUM */

.premium-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:24px;
    margin-top:28px;
}

.premium-card{
    background:#1a1208;
    color:white;
    border-radius:24px;
    padding:28px;
}

.premium-tier{
    color:var(--accent2);
    font-size:12px;
    letter-spacing:2px;
    margin-bottom:14px;
}

.premium-price{
    color:var(--accent2);
    font-size:26px;
    font-weight:800;
    margin-top:18px;
}

.premium-features{
    margin-top:18px;
}

.premium-features li{
    margin-top:8px;
}

/* MENTORS */

.mentors-grid{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:22px;
    margin-top:28px;
}

.mentor-card{
    background:white;
    border:1px solid var(--border);
    border-radius:24px;
    padding:26px;
    text-align:center;
}

.mentor-avatar{
    width:70px;
    height:70px;
    border-radius:20px;
    background:linear-gradient(135deg,var(--accent),var(--accent3));
    display:flex;
    align-items:center;
    justify-content:center;
    color:white;
    font-size:24px;
    font-weight:800;
    margin:auto;
    margin-bottom:16px;
}

/* SUPPORT */

.support-grid{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:24px;
    margin-top:28px;
}

.support-card{
    background:white;
    border:1px solid var(--border);
    border-radius:24px;
    padding:28px;
}

/* CHAT */

.chat-fab{
    position:fixed;
    bottom:24px;
    right:24px;
    width:68px;
    height:68px;
    border:none;
    border-radius:50%;
    background:linear-gradient(135deg,var(--accent),var(--accent3));
    color:white;
    font-size:28px;
    cursor:pointer;
    box-shadow:0 12px 34px rgba(212,96,26,0.4);
    z-index:999;
}

.chat-window{
    position:fixed;
    bottom:110px;
    right:24px;
    width:390px;
    max-height:620px;
    background:white;
    border-radius:24px;
    border:1px solid var(--border);
    overflow:hidden;
    box-shadow:0 24px 64px rgba(0,0,0,0.15);
    display:none;
    flex-direction:column;
    z-index:999;
}

.chat-window.open{
    display:flex;
}

.chat-header{
    background:#1a1208;
    color:white;
    padding:18px;
    display:flex;
    justify-content:space-between;
    align-items:center;
}

.chat-messages{
    height:360px;
    overflow:auto;
    padding:18px;
    background:#fafaf8;
}

.msg{
    margin-bottom:14px;
}

.msg-bubble{
    background:white;
    padding:12px 16px;
    border-radius:16px;
    border:1px solid var(--border);
    line-height:1.7;
}

.msg.user .msg-bubble{
    background:var(--accent);
    color:white;
}

.quick-chips{
    display:flex;
    flex-wrap:wrap;
    gap:10px;
    padding:16px;
}

.quick-chip{
    background:var(--surface2);
    border:1px solid var(--border);
    padding:8px 14px;
    border-radius:999px;
    cursor:pointer;
    font-size:13px;
}

.chat-input-bar{
    display:flex;
    gap:10px;
    padding:16px;
    border-top:1px solid var(--border);
}

.chat-textarea{
    flex:1;
    border:1px solid var(--border);
    border-radius:14px;
    padding:14px;
    resize:none;
}

.chat-send{
    background:var(--accent);
    color:white;
    border:none;
    width:48px;
    border-radius:14px;
    cursor:pointer;
}

/* FOOTER */

footer{
    background:#1a1208;
    color:rgba(255,255,255,0.75);
    text-align:center;
    padding:44px;
    margin-top:40px;
    line-height:1.8;
}

@media(max-width:900px){

.hero-section{
    grid-template-columns:1fr;
}

.hero-card{
    display:none;
}

.products-grid{
    grid-template-columns:1fr;
}

.premium-grid{
    grid-template-columns:1fr;
}

.mentors-grid{
    grid-template-columns:1fr 1fr;
}

.support-grid{
    grid-template-columns:1fr;
}

.stats-strip{
    grid-template-columns:1fr 1fr;
    gap:24px;
}

.nav-links{
    display:none;
}

.chat-window{
    width:95%;
    right:2.5%;
}

.hero h1{
    font-size:54px;
}

}

</style>
</head>

<body>

<nav>

<div class="nav-brand">
    <div class="nav-logo">IM</div>

    <div>
        <div class="nav-title">INVESMATE</div>
        <div class="nav-tagline">
            Stock Market Learning
        </div>
    </div>
</div>

<div class="nav-links">
    <a href="#products">Products</a>
    <a href="#insignia">INSIGNIA</a>
    <a href="#mentors">Mentors</a>
    <a href="#support">Support</a>
    <a href="#support" class="nav-btn">Request Callback</a>
</div>

</nav>

<section class="hero-section">

<div class="hero">

<div class="hero-badge">
● SEBI Registered RA: INH000017985
</div>

<h1>
Finest Stock Market
<span>Learning</span>
Experience
</h1>

<p class="hero-sub">
A professional platform for INVESMATE and INSIGNIA with AI-guided course selection,
multilingual support, and personalized mentorship plans for every learner.
</p>

<div class="hero-actions">
<button class="btn-primary">
Explore Courses ↓
</button>

<button class="btn-outline" onclick="toggleChat()">
Talk to AI Advisor
</button>
</div>

</div>

<div class="hero-card">

<div class="hero-card-label">
Premium Learning Path
</div>

<h3>
Find the right course in minutes
</h3>

<p>
Use our AI advisor and course predictor to choose between beginner,
trading, investing, derivatives, and INSIGNIA mentorship plans.
</p>

<div class="info-row">
<strong>Personalized Prediction</strong><br>
Course recommendation by goal, budget & experience
</div>

<div class="info-row">
<strong>Multilingual Support</strong><br>
English, Bengali, Hindi & Auto-Detect
</div>

<div class="info-row">
<strong>INSIGNIA Premium</strong><br>
1:1 mentorship, live sessions & lifetime recordings
</div>

</div>

</section>

<div class="stats-strip">

<div>
<div class="stat-num">20+</div>
<div class="stat-label">Expert Courses</div>
</div>

<div>
<div class="stat-num">8</div>
<div class="stat-label">Certified Mentors</div>
</div>

<div>
<div class="stat-num">3</div>
<div class="stat-label">Language Support</div>
</div>

<div>
<div class="stat-num">SEBI</div>
<div class="stat-label">Registered RA</div>
</div>

</div>

<section class="section" id="products">

<div class="section-eyebrow">
ALL PRODUCTS
</div>

<div class="section-title">
Complete Product Ecosystem
</div>

<div class="section-sub">
Professional stock market learning programs for every level.
</div>

<div class="filter-bar">

<div class="filter-chip active">
All
</div>

<div class="filter-chip">
Live Course
</div>

<div class="filter-chip">
Recorded
</div>

<div class="filter-chip">
Mentorship
</div>

</div>

<div class="search-wrap">
<input class="search-input" placeholder="Search courses and mentorship plans...">
</div>

<div class="products-grid">

<div class="product-card">

<div class="product-tag">
Beginner
</div>

<h3>
Power of Trading and Investing Combo Course
</h3>

<p>
Complete capital-market course covering trading and investing from basics to advanced level.
</p>

<div class="product-meta">
<div class="meta-pill">
Rs. 8,999 - Rs. 11,999
</div>

<div class="meta-pill">
2 Months / 26 Hours • 57 Lessons
</div>
</div>

<div class="modules-list">
<div class="module-chip">Market Basics</div>
<div class="module-chip">Technical Analysis</div>
<div class="module-chip">Investing</div>
</div>

</div>

<div class="product-card">

<div class="product-tag">
Technical Trading
</div>

<h3>
Complete Intraday and Swing Trading Strategies
</h3>

<p>
Advanced technical-analysis course for intraday and swing trading.
</p>

<div class="product-meta">
<div class="meta-pill">
Rs. 9,999 - Rs. 12,999
</div>

<div class="meta-pill">
2 Months / 20 Hours • 48 Lessons
</div>
</div>

<div class="modules-list">
<div class="module-chip">Indicators</div>
<div class="module-chip">Chart Patterns</div>
<div class="module-chip">Risk Control</div>
</div>

</div>

<div class="product-card">

<div class="product-tag">
Derivatives
</div>

<h3>
Complete Future and Option Trading Strategies
</h3>

<p>
Futures and options training for learners who want derivatives strategy knowledge.
</p>

<div class="product-meta">
<div class="meta-pill">
Rs. 12,999 - Rs. 15,999
</div>

<div class="meta-pill">
2 Months / 26 Hours • 25 Lessons
</div>
</div>

<div class="modules-list">
<div class="module-chip">Options</div>
<div class="module-chip">Hedging</div>
<div class="module-chip">Futures</div>
</div>

</div>

</div>

</section>

<hr class="divider">

<section class="section" id="insignia">

<div class="section-eyebrow">
INSIGNIA PREMIUM JOURNEY
</div>

<div class="section-title">
Premium Mentorship Plans
</div>

<div class="section-sub">
Structured mentorship programs with live sessions and practical market learning.
</div>

<div class="premium-grid">

<div class="premium-card">

<div class="premium-tier">
PREMIUM MENTORSHIP
</div>

<h3>
Equity Market Intelligence Matrix
</h3>

<p>
Premium mentorship combining advanced technical and fundamental analysis.
</p>

<div class="premium-price">
Rs. 38,571 / Rs. 44,420
</div>

<ul class="premium-features">
<li>1:1 Mentorship</li>
<li>4 Practical Sessions</li>
<li>NISM Guidance</li>
</ul>

</div>

<div class="premium-card">

<div class="premium-tier">
OPTIONS PREMIUM
</div>

<h3>
Complete Equity and Derivative Dynasty
</h3>

<p>
Advanced premium pathway for derivatives and technical mastery.
</p>

<div class="premium-price">
Rs. 62,305 / Rs. 44,420
</div>

<ul class="premium-features">
<li>Advanced Technical</li>
<li>Options Mastery</li>
<li>Academic Helpline</li>
</ul>

</div>

<div class="premium-card">

<div class="premium-tier">
GLOBAL PREMIUM
</div>

<h3>
Complete Global Capital Market Specialist
</h3>

<p>
Global market specialist path including US stocks and commodities.
</p>

<div class="premium-price">
Rs. 1,07,689 / Rs. 44,420
</div>

<ul class="premium-features">
<li>US Stocks</li>
<li>Commodity Market</li>
<li>Lifetime Recordings</li>
</ul>

</div>

</div>

</section>

<hr class="divider">

<section class="section" id="mentors">

<div class="section-eyebrow">
TOP MENTORS
</div>

<div class="section-title">
Experienced Market Mentors
</div>

<div class="mentors-grid">

<div class="mentor-card">
<div class="mentor-avatar">AC</div>
<h3>Arunava Chatterjee</h3>
<p>Capital market mentor</p>
</div>

<div class="mentor-card">
<div class="mentor-avatar">SG</div>
<h3>Sayan Ghosh</h3>
<p>Capital market mentor</p>
</div>

<div class="mentor-card">
<div class="mentor-avatar">KS</div>
<h3>Kunal Saha</h3>
<p>Capital market mentor</p>
</div>

<div class="mentor-card">
<div class="mentor-avatar">SM</div>
<h3>Suman Goswami</h3>
<p>Capital market mentor</p>
</div>

</div>

</section>

<hr class="divider">

<section class="section" id="support">

<div class="section-eyebrow">
SUPPORT
</div>

<div class="section-title">
Talk to the team before you enroll
</div>

<div class="support-grid">

<div class="support-card">

<h3>
Counseling & Support
</h3>

<p>📞 +91 9016791791</p>
<p>📞 +91 7596037781</p>
<p>📞 +91 7003110622</p>

<br>

<p>✉️ support@invesmate.com</p>
<p>✉️ sales@invesmate.com</p>

</div>

<div class="support-card">

<h3>
Disclaimer
</h3>

<p>
Investment in securities markets is subject to market risks.
Read all the related documents carefully before investing.
</p>

<br>

<p>
INVESMATE INSIGHTS - SEBI Registered Research Analyst.
This platform is for educational purposes only.
</p>

</div>

</div>

</section>

<footer>

<strong>INVESMATE</strong><br>

Stock Market Learning Platform<br>

SEBI Registered RA: INH000017985<br>

support@invesmate.com<br><br>

© 2026 INVESMATE. All rights reserved.

</footer>

<!-- CHAT -->

<button class="chat-fab" onclick="toggleChat()">
💬
</button>

<div class="chat-window" id="chatWindow">

<div class="chat-header">
<div>INVESMATE AI Advisor</div>
<button onclick="toggleChat()" style="background:none;border:none;color:white;font-size:20px;cursor:pointer;">×</button>
</div>

<div class="chat-messages" id="chatMessages">

<div class="msg">
<div class="msg-bubble">
Hi! I'm your INVESMATE AI Advisor 👋
</div>
</div>

<div class="msg">
<div class="msg-bubble">
I can help you choose the right course, compare INSIGNIA plans, and answer pricing or enrollment questions.
</div>
</div>

</div>

<div class="quick-chips">

<div class="quick-chip" onclick="quickMsg('Recommend beginner course')">
Beginner Course
</div>

<div class="quick-chip" onclick="quickMsg('Compare INSIGNIA plans')">
INSIGNIA Plans
</div>

<div class="quick-chip" onclick="quickMsg('Pricing details')">
Pricing
</div>

</div>

<div class="chat-input-bar">

<textarea
class="chat-textarea"
id="chatInput"
placeholder="Ask about courses, pricing, enrollment..."
></textarea>

<button class="chat-send" onclick="sendMessage()">
➜
</button>

</div>

</div>

<script>

let chatOpen = false;

function toggleChat(){

    const win = document.getElementById("chatWindow");

    chatOpen = !chatOpen;

    if(chatOpen){
        win.classList.add("open");
    }else{
        win.classList.remove("open");
    }
}

function addMessage(text, role="bot"){

    const messages = document.getElementById("chatMessages");

    const div = document.createElement("div");

    div.className = "msg " + role;

    div.innerHTML = `
        <div class="msg-bubble">${text}</div>
    `;

    messages.appendChild(div);

    messages.scrollTop = messages.scrollHeight;
}

function quickMsg(text){

    document.getElementById("chatInput").value = text;

    sendMessage();
}

function sendMessage(){

    const input = document.getElementById("chatInput");

    const text = input.value.trim();

    if(!text) return;

    addMessage(text,"user");

    input.value = "";

    let reply = `
        Based on your query, I recommend:
        <br><br>
        • Beginners → Power of Trading and Investing Combo Course
        <br>
        • Technical traders → Intraday & Swing Trading
        <br>
        • Advanced learners → INSIGNIA Mentorship
        <br><br>
        Note: Investment in securities markets is subject to market risks.
    `;

    const q = text.toLowerCase();

    if(q.includes("option") || q.includes("future")){
        reply = `
            Best recommendation:
            <br><br>
            Complete Future and Option Trading Strategies
            <br><br>
            Premium Alternative:
            <br>
            Complete Equity and Derivative Dynasty
        `;
    }

    if(q.includes("price") || q.includes("fee")){
        reply = `
            Course pricing starts from Rs. 3,999 and goes up depending on the program.
            <br><br>
            INSIGNIA mentorship plans start from Rs. 38,571.
        `;
    }

    if(q.includes("enroll")){
        reply = `
            Enrollment flow:
            <br><br>
            1. Choose course
            <br>
            2. Request counseling
            <br>
            3. Confirm fee and batch
            <br>
            4. Complete payment
            <br>
            5. Access classes through the learning app
        `;
    }

    setTimeout(()=>{
        addMessage(reply,"bot");
    },600);
}

</script>

</body>
</html>
"""

components.html(
    html_code,
    height=5200,
    scrolling=True
)
