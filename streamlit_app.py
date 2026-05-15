import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="INVESMATE - Stock Market Learning Platform",
    layout="wide",
    initial_sidebar_state="collapsed"
)

html_code = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>INVESMATE - Stock Market Learning Platform</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">

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
    --border:#e6e0d4;
    --radius:20px;
}

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    font-family:'DM Sans',sans-serif;
    background:var(--bg);
    color:var(--text);
    overflow-x:hidden;
}

nav{
    position:sticky;
    top:0;
    z-index:999;
    background:rgba(250,250,248,0.95);
    backdrop-filter:blur(20px);
    border-bottom:1px solid var(--border);
    padding:18px 40px;
    display:flex;
    justify-content:space-between;
    align-items:center;
}

.nav-brand{
    display:flex;
    align-items:center;
    gap:12px;
}

.logo{
    width:48px;
    height:48px;
    border-radius:16px;
    background:linear-gradient(135deg,var(--accent),#fbbf24);
    display:flex;
    align-items:center;
    justify-content:center;
    color:#fff;
    font-weight:800;
    font-family:'Syne',sans-serif;
}

.nav-title{
    font-family:'Syne',sans-serif;
    font-size:20px;
    font-weight:800;
}

.hero{
    max-width:1200px;
    margin:auto;
    padding:80px 30px;
    display:grid;
    grid-template-columns:1fr 420px;
    gap:40px;
    align-items:center;
}

.hero-badge{
    display:inline-block;
    padding:8px 18px;
    background:#fff3ea;
    border:1px solid #f6d4b4;
    color:var(--accent);
    border-radius:999px;
    font-size:13px;
    font-weight:700;
    margin-bottom:18px;
}

.hero h1{
    font-family:'Syne',sans-serif;
    font-size:70px;
    line-height:0.95;
    margin-bottom:20px;
}

.hero h1 span{
    color:var(--accent);
}

.hero p{
    color:var(--text2);
    line-height:1.8;
    font-size:18px;
    margin-bottom:30px;
}

.hero-buttons{
    display:flex;
    gap:14px;
    flex-wrap:wrap;
}

.btn-primary{
    background:var(--accent);
    color:white;
    border:none;
    padding:14px 28px;
    border-radius:999px;
    font-weight:700;
    cursor:pointer;
}

.btn-secondary{
    background:white;
    border:1px solid var(--border);
    padding:14px 28px;
    border-radius:999px;
    font-weight:700;
    cursor:pointer;
}

.hero-card{
    background:white;
    border-radius:var(--radius);
    border:1px solid var(--border);
    padding:28px;
    box-shadow:0 18px 48px rgba(0,0,0,0.08);
}

.hero-card h3{
    font-family:'Syne',sans-serif;
    margin-bottom:10px;
}

.info-box{
    background:var(--surface2);
    padding:14px;
    border-radius:14px;
    margin-top:12px;
}

.stats{
    background:#1a1208;
    color:white;
    display:grid;
    grid-template-columns:repeat(4,1fr);
    text-align:center;
    padding:30px;
}

.stat-number{
    font-size:40px;
    font-weight:800;
    color:var(--accent2);
}

.section{
    max-width:1200px;
    margin:auto;
    padding:70px 30px;
}

.section h2{
    font-family:'Syne',sans-serif;
    font-size:42px;
    margin-bottom:10px;
}

.section p{
    color:var(--text2);
}

.search-box{
    margin-top:30px;
    margin-bottom:30px;
}

.search-box input{
    width:100%;
    padding:16px;
    border-radius:14px;
    border:1px solid var(--border);
    background:white;
}

.grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:22px;
}

.card{
    background:white;
    border:1px solid var(--border);
    border-radius:22px;
    padding:24px;
    transition:0.3s;
}

.card:hover{
    transform:translateY(-5px);
    box-shadow:0 18px 38px rgba(0,0,0,0.08);
}

.tag{
    display:inline-block;
    padding:6px 12px;
    border-radius:999px;
    background:#fff3ea;
    color:var(--accent);
    font-size:12px;
    font-weight:700;
    margin-bottom:12px;
}

.card h3{
    margin-bottom:12px;
    font-size:20px;
}

.card p{
    color:var(--text2);
    line-height:1.7;
    margin-bottom:18px;
}

.price{
    color:var(--accent);
    font-weight:800;
    margin-bottom:6px;
}

.modules{
    display:flex;
    flex-wrap:wrap;
    gap:8px;
    margin-top:16px;
}

.module{
    background:#f5f3ee;
    padding:6px 12px;
    border-radius:999px;
    font-size:12px;
}

.premium-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:22px;
    margin-top:30px;
}

.premium-card{
    background:#1a1208;
    color:white;
    border-radius:24px;
    padding:28px;
}

.premium-card p{
    color:rgba(255,255,255,0.75);
}

.premium-price{
    color:#f08d3c;
    font-size:22px;
    font-weight:800;
    margin-top:16px;
}

.mentor-grid{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:20px;
    margin-top:30px;
}

.mentor-card{
    background:white;
    border:1px solid var(--border);
    border-radius:20px;
    padding:22px;
    text-align:center;
}

.avatar{
    width:70px;
    height:70px;
    border-radius:20px;
    margin:auto;
    margin-bottom:14px;
    background:linear-gradient(135deg,var(--accent),#fbbf24);
    display:flex;
    align-items:center;
    justify-content:center;
    color:white;
    font-weight:800;
    font-size:24px;
}

.support-grid{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:24px;
    margin-top:30px;
}

.support-card{
    background:white;
    border:1px solid var(--border);
    border-radius:22px;
    padding:28px;
}

.chatbot{
    position:fixed;
    bottom:20px;
    right:20px;
    width:380px;
    background:white;
    border-radius:24px;
    overflow:hidden;
    border:1px solid var(--border);
    box-shadow:0 24px 64px rgba(0,0,0,0.15);
}

.chat-header{
    background:#1a1208;
    color:white;
    padding:18px;
    font-weight:700;
}

.chat-messages{
    height:320px;
    overflow:auto;
    padding:18px;
    background:#fafaf8;
}

.message{
    background:white;
    padding:12px 16px;
    border-radius:14px;
    margin-bottom:12px;
    border:1px solid var(--border);
}

.chat-input{
    display:flex;
    border-top:1px solid var(--border);
}

.chat-input input{
    flex:1;
    border:none;
    padding:16px;
    outline:none;
}

.chat-input button{
    background:var(--accent);
    color:white;
    border:none;
    padding:16px 20px;
    cursor:pointer;
}

footer{
    margin-top:60px;
    background:#1a1208;
    color:rgba(255,255,255,0.75);
    text-align:center;
    padding:40px;
}

@media(max-width:900px){

.hero{
    grid-template-columns:1fr;
}

.grid{
    grid-template-columns:1fr;
}

.premium-grid{
    grid-template-columns:1fr;
}

.mentor-grid{
    grid-template-columns:1fr 1fr;
}

.support-grid{
    grid-template-columns:1fr;
}

.stats{
    grid-template-columns:1fr 1fr;
    gap:20px;
}

.chatbot{
    width:95%;
    right:2.5%;
}

.hero h1{
    font-size:48px;
}

}

</style>
</head>

<body>

<nav>
    <div class="nav-brand">
        <div class="logo">IM</div>
        <div>
            <div class="nav-title">INVESMATE</div>
            <div style="font-size:12px;color:#d4601a;font-weight:700;">
                Stock Market Learning
            </div>
        </div>
    </div>
</nav>

<section class="hero">

<div>
    <div class="hero-badge">
        SEBI Registered RA: INH000017985
    </div>

    <h1>
        Finest Stock Market
        <span>Learning</span>
        Experience
    </h1>

    <p>
        A professional platform for INVESMATE and INSIGNIA with AI-guided course selection,
        multilingual support, and personalized mentorship plans for every learner.
    </p>

    <div class="hero-buttons">
        <button class="btn-primary">Explore Courses</button>
        <button class="btn-secondary">Talk to AI Advisor</button>
    </div>
</div>

<div class="hero-card">

    <div class="tag">Premium Learning Path</div>

    <h3>Find the right course in minutes</h3>

    <p style="color:#6b6150;">
        Use our AI advisor and course predictor to choose between beginner,
        trading, investing, derivatives, and INSIGNIA mentorship plans.
    </p>

    <div class="info-box">
        <b>Personalized Prediction</b><br>
        Course recommendation by goal, budget and experience
    </div>

    <div class="info-box">
        <b>Multilingual Support</b><br>
        English, Bengali and Hindi support
    </div>

    <div class="info-box">
        <b>INSIGNIA Premium</b><br>
        1:1 mentorship and live practical sessions
    </div>

</div>

</section>

<section class="stats">

<div>
    <div class="stat-number">20+</div>
    <div>Expert Courses</div>
</div>

<div>
    <div class="stat-number">8</div>
    <div>Certified Mentors</div>
</div>

<div>
    <div class="stat-number">3</div>
    <div>Language Support</div>
</div>

<div>
    <div class="stat-number">SEBI</div>
    <div>Registered RA</div>
</div>

</section>

<section class="section">

<h2>Complete Product Ecosystem</h2>

<p>
Professional stock market learning programs for every level.
</p>

<div class="search-box">
    <input type="text" placeholder="Search courses and mentorship plans...">
</div>

<div class="grid">

<div class="card">
    <div class="tag">Beginner</div>
    <h3>Power of Trading and Investing Combo Course</h3>
    <p>
        Complete capital-market course covering trading and investing
        from basics to advanced level.
    </p>

    <div class="price">
        Rs. 8,999 - Rs. 11,999
    </div>

    <div>2 Months / 26 Hours</div>

    <div class="modules">
        <div class="module">Market basics</div>
        <div class="module">Technical analysis</div>
        <div class="module">Investing</div>
    </div>
</div>

<div class="card">
    <div class="tag">Technical Trading</div>
    <h3>Complete Intraday and Swing Trading Strategies</h3>
    <p>
        Advanced technical-analysis course for intraday and swing trading.
    </p>

    <div class="price">
        Rs. 9,999 - Rs. 12,999
    </div>

    <div>2 Months / 20 Hours</div>

    <div class="modules">
        <div class="module">Chart patterns</div>
        <div class="module">Indicators</div>
        <div class="module">Risk control</div>
    </div>
</div>

<div class="card">
    <div class="tag">Derivatives</div>
    <h3>Complete Future and Option Trading Strategies</h3>

    <p>
        Futures and options training for learners who want derivatives strategy knowledge.
    </p>

    <div class="price">
        Rs. 12,999 - Rs. 15,999
    </div>

    <div>2 Months / 26 Hours</div>

    <div class="modules">
        <div class="module">Options</div>
        <div class="module">Hedging</div>
        <div class="module">Futures</div>
    </div>
</div>

</div>

</section>

<section class="section">

<h2>INSIGNIA Premium Mentorship Plans</h2>

<p>
Intensive mentorship with practical market learning.
</p>

<div class="premium-grid">

<div class="premium-card">
    <div class="tag">Premium Mentorship</div>

    <h3>Equity Market Intelligence Matrix</h3>

    <p>
        Advanced technical and fundamental mentorship with live practical sessions.
    </p>

    <div class="premium-price">
        Rs. 38,571 / Rs. 44,420
    </div>
</div>

<div class="premium-card">
    <div class="tag">Options Premium</div>

    <h3>Complete Equity and Derivative Dynasty</h3>

    <p>
        Complete derivatives and technical mastery pathway.
    </p>

    <div class="premium-price">
        Rs. 62,305 / Rs. 44,420
    </div>
</div>

<div class="premium-card">
    <div class="tag">Global Premium</div>

    <h3>Complete Global Capital Market Specialist</h3>

    <p>
        Global market specialist path including US stocks and commodities.
    </p>

    <div class="premium-price">
        Rs. 1,07,689 / Rs. 44,420
    </div>
</div>

</div>

</section>

<section class="section">

<h2>Experienced Market Mentors</h2>

<div class="mentor-grid">

<div class="mentor-card">
    <div class="avatar">AC</div>
    <h3>Arunava Chatterjee</h3>
    <p>NISM-certified market mentor</p>
</div>

<div class="mentor-card">
    <div class="avatar">SG</div>
    <h3>Sayan Ghosh</h3>
    <p>NISM-certified market mentor</p>
</div>

<div class="mentor-card">
    <div class="avatar">KS</div>
    <h3>Kunal Saha</h3>
    <p>NISM-certified market mentor</p>
</div>

<div class="mentor-card">
    <div class="avatar">SM</div>
    <h3>Suman Goswami</h3>
    <p>NISM-certified market mentor</p>
</div>

</div>

</section>

<section class="section">

<h2>Support and Counseling</h2>

<div class="support-grid">

<div class="support-card">
    <h3>Contact Team</h3>

    <p>+91 9016791791</p>
    <p>+91 7596037781</p>
    <p>+91 7003110622</p>

    <br>

    <p>support@invesmate.com</p>
    <p>sales@invesmate.com</p>
</div>

<div class="support-card">
    <h3>Disclaimer</h3>

    <p>
        Investment in securities markets is subject to market risks.
        Read all related documents carefully before investing.
    </p>

    <br>

    <p>
        INVESMATE INSIGHTS is a SEBI Registered Research Analyst platform.
        This platform is for educational purposes only.
    </p>
</div>

</div>

</section>

<div class="chatbot">

<div class="chat-header">
    INVESMATE AI Advisor
</div>

<div class="chat-messages" id="chatMessages">

<div class="message">
    Hi! I am your INVESMATE AI Advisor 👋
</div>

<div class="message">
    Ask me about:
    <br><br>
    • Course recommendations
    <br>
    • INSIGNIA mentorship
    <br>
    • Pricing and enrollment
    <br>
    • Support and counseling
</div>

</div>

<div class="chat-input">

<input
    type="text"
    id="chatInput"
    placeholder="Ask about courses, pricing, enrollment..."
>

<button onclick="sendMessage()">
➜
</button>

</div>

</div>

<footer>

<strong>INVESMATE</strong>
<br>

Stock Market Learning Platform
<br>

SEBI Registered RA: INH000017985
<br>

support@invesmate.com

<br><br>

Investment in securities markets is subject to market risks.

</footer>

<script>

function sendMessage(){

    const input = document.getElementById("chatInput");
    const value = input.value.trim();

    if(!value) return;

    const box = document.getElementById("chatMessages");

    box.innerHTML += `
        <div class="message">
            <b>You:</b><br>${value}
        </div>
    `;

    let reply = `
        Based on your interest, our advisor recommends:
        <br><br>
        • Beginners → Power of Trading and Investing Combo
        <br>
        • Technical traders → Intraday & Swing Trading
        <br>
        • Advanced learners → INSIGNIA Mentorship
        <br><br>
        Note: Investment in securities markets is subject to market risks.
    `;

    if(value.toLowerCase().includes("option")){
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

    if(value.toLowerCase().includes("price")){
        reply = `
            Course pricing starts from Rs. 3,999 and goes up depending on the program.
            <br><br>
            INSIGNIA plans start from Rs. 38,571.
        `;
    }

    setTimeout(()=>{
        box.innerHTML += `
            <div class="message">
                <b>Advisor:</b><br>${reply}
            </div>
        `;

        box.scrollTop = box.scrollHeight;

    },600);

    input.value = "";
}

</script>

</body>
</html>
"""

components.html(html_code, height=4200, scrolling=True)
