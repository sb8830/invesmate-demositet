<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>INVESMATE – Stock Market Learning Platform</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,300&display=swap" rel="stylesheet" />
<style>
  :root {
    --bg: #fafaf8;
    --surface: #ffffff;
    --surface2: #f5f3ee;
    --surface3: #ede9e0;
    --text: #1a1208;
    --text2: #6b6150;
    --text3: #a09880;
    --accent: #d4601a;
    --accent2: #f08d3c;
    --accent3: #fbbf24;
    --border: #e6e0d4;
    --border2: #d4ccbe;
    --shadow: 0 4px 24px rgba(26,18,8,0.08);
    --shadow2: 0 16px 48px rgba(26,18,8,0.12);
    --radius: 20px;
    --radius2: 12px;
    --radius3: 999px;
  }
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  html { scroll-behavior: smooth; }
  body { font-family: 'DM Sans', sans-serif; background: var(--bg); color: var(--text); font-size: 16px; line-height: 1.6; overflow-x: hidden; }

  /* NAV */
  nav { position: sticky; top: 0; z-index: 100; background: rgba(250,250,248,0.9); backdrop-filter: blur(20px); border-bottom: 1px solid var(--border); padding: 0 2rem; display: flex; align-items: center; justify-content: space-between; height: 68px; }
  .nav-brand { display: flex; align-items: center; gap: 0.75rem; text-decoration: none; }
  .nav-logo { width: 42px; height: 42px; border-radius: 14px; background: linear-gradient(135deg, var(--accent), var(--accent3)); display: flex; align-items: center; justify-content: center; font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1rem; color: #fff; box-shadow: 0 6px 20px rgba(212,96,26,0.3); }
  .nav-title { font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.15rem; color: var(--text); }
  .nav-tagline { font-size: 0.7rem; color: var(--accent); font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; }
  .nav-links { display: flex; align-items: center; gap: 2rem; }
  .nav-links a { color: var(--text2); font-weight: 500; text-decoration: none; font-size: 0.9rem; transition: color 0.2s; }
  .nav-links a:hover { color: var(--text); }
  .nav-cta { background: var(--text) !important; color: #fff !important; padding: 0.55rem 1.2rem !important; border-radius: var(--radius3) !important; font-weight: 600 !important; font-size: 0.85rem !important; }
  .nav-cta:hover { background: var(--accent) !important; color: #fff !important; }

  /* HERO */
  .hero-section { padding: 5rem 2rem 4rem; max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1fr 420px; gap: 3rem; align-items: center; animation: fadeUp 0.8s ease both; }
  .hero-badge { display: inline-flex; align-items: center; gap: 0.5rem; background: var(--surface2); border: 1px solid var(--border2); border-radius: var(--radius3); padding: 0.35rem 0.9rem; font-size: 0.75rem; font-weight: 600; color: var(--accent); letter-spacing: 0.06em; text-transform: uppercase; margin-bottom: 1.2rem; }
  .hero h1 { font-family: 'Syne', sans-serif; font-size: clamp(2.8rem, 5.5vw, 5rem); font-weight: 800; line-height: 0.95; letter-spacing: -0.05em; color: var(--text); margin-bottom: 1.25rem; }
  .hero h1 em { font-style: normal; color: var(--accent); }
  .hero-sub { font-size: 1.05rem; color: var(--text2); line-height: 1.75; max-width: 540px; margin-bottom: 2rem; }
  .hero-actions { display: flex; gap: 0.75rem; flex-wrap: wrap; }
  .btn-primary { background: var(--accent); color: #fff; padding: 0.85rem 1.6rem; border-radius: var(--radius3); font-weight: 600; font-size: 0.95rem; border: none; cursor: pointer; text-decoration: none; display: inline-flex; align-items: center; gap: 0.4rem; box-shadow: 0 8px 24px rgba(212,96,26,0.28); transition: transform 0.2s, box-shadow 0.2s; }
  .btn-primary:hover { transform: translateY(-2px); box-shadow: 0 14px 36px rgba(212,96,26,0.36); }
  .btn-outline { background: transparent; color: var(--text); padding: 0.85rem 1.6rem; border-radius: var(--radius3); font-weight: 600; font-size: 0.95rem; border: 1.5px solid var(--border2); cursor: pointer; text-decoration: none; display: inline-flex; align-items: center; gap: 0.4rem; transition: border-color 0.2s, background 0.2s; }
  .btn-outline:hover { border-color: var(--accent); background: var(--surface2); }
  .hero-card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 1.75rem; box-shadow: var(--shadow2); animation: fadeUp 0.9s ease 0.1s both; }
  .hero-card-label { display: inline-block; background: var(--accent); color: #fff; border-radius: var(--radius3); padding: 0.25rem 0.75rem; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; margin-bottom: 1rem; }
  .hero-card h3 { font-family: 'Syne', sans-serif; font-size: 1.2rem; font-weight: 700; margin-bottom: 0.5rem; }
  .hero-card p { color: var(--text2); font-size: 0.88rem; margin-bottom: 1.25rem; }
  .info-row { background: var(--surface2); border-radius: var(--radius2); padding: 0.85rem 1rem; margin-bottom: 0.6rem; border: 1px solid var(--border); }
  .info-row strong { display: block; font-size: 0.88rem; color: var(--text); margin-bottom: 0.2rem; }
  .info-row small { color: var(--text2); font-size: 0.8rem; }

  /* STATS */
  .stats-strip { background: var(--text); color: #fff; padding: 2rem; display: flex; justify-content: center; }
  .stat-item { flex: 1; max-width: 220px; text-align: center; padding: 0 2rem; border-right: 1px solid rgba(255,255,255,0.12); }
  .stat-item:last-child { border-right: none; }
  .stat-num { font-family: 'Syne', sans-serif; font-size: 2.5rem; font-weight: 800; color: var(--accent2); }
  .stat-label { font-size: 0.82rem; color: rgba(255,255,255,0.6); margin-top: 0.2rem; }

  /* SECTION */
  .section { padding: 4rem 2rem; max-width: 1200px; margin: 0 auto; }
  .section-eyebrow { font-size: 0.72rem; font-weight: 700; color: var(--accent); letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.5rem; }
  .section-title { font-family: 'Syne', sans-serif; font-size: clamp(1.8rem, 3.5vw, 2.8rem); font-weight: 800; letter-spacing: -0.04em; color: var(--text); margin-bottom: 0.5rem; }
  .section-sub { color: var(--text2); font-size: 1rem; max-width: 600px; line-height: 1.7; }
  .divider { border: none; border-top: 1px solid var(--border); margin: 0; }

  /* IN-CHAT PREDICTOR WIDGET */
  .chat-predictor-card { background: var(--surface); border: 1.5px solid var(--border2); border-radius: 16px 16px 16px 4px; padding: 1rem 1.1rem; max-width: 95%; display: flex; flex-direction: column; gap: 0.65rem; }
  .chat-predictor-card .pred-title { font-family: 'Syne', sans-serif; font-weight: 700; font-size: 0.88rem; color: var(--text); display: flex; align-items: center; gap: 0.4rem; }
  .chat-pred-row { display: flex; flex-direction: column; gap: 0.25rem; }
  .chat-pred-row label { font-size: 0.68rem; font-weight: 700; color: var(--text3); letter-spacing: 0.07em; text-transform: uppercase; }
  .chat-pred-row select { background: var(--surface2); border: 1.5px solid var(--border); border-radius: var(--radius2); padding: 0.5rem 0.7rem; font-family: 'DM Sans', sans-serif; font-size: 0.82rem; color: var(--text); outline: none; cursor: pointer; width: 100%; appearance: none; transition: border-color 0.2s; }
  .chat-pred-row select:focus { border-color: var(--accent); }
  .chat-pred-btn { background: var(--accent); color: #fff; border: none; border-radius: var(--radius2); padding: 0.6rem 1rem; font-family: 'DM Sans', sans-serif; font-size: 0.85rem; font-weight: 600; cursor: pointer; transition: background 0.2s, transform 0.15s; display: flex; align-items: center; justify-content: center; gap: 0.4rem; }
  .chat-pred-btn:hover { background: #c0531a; transform: scale(1.02); }
  .chat-pred-btn:disabled { background: var(--border2); cursor: not-allowed; transform: none; }
  .pred-result-card { background: linear-gradient(135deg, #fff8f4, #fff3ea); border: 1.5px solid #f6d4b4; border-radius: 16px 16px 16px 4px; padding: 0.9rem 1rem; max-width: 95%; display: flex; flex-direction: column; gap: 0.45rem; animation: fadeUp 0.35s ease; }
  .pred-result-card .pred-result-label { font-size: 0.68rem; font-weight: 700; color: var(--accent); letter-spacing: 0.08em; text-transform: uppercase; }
  .pred-result-card h4 { font-family: 'Syne', sans-serif; font-size: 0.92rem; font-weight: 800; color: var(--text); line-height: 1.3; }
  .pred-result-card p { font-size: 0.8rem; color: var(--text2); line-height: 1.55; }
  .pred-result-chips { display: flex; gap: 0.4rem; flex-wrap: wrap; }
  .pred-result-chips span { background: #fff; border: 1px solid #f6d4b4; border-radius: var(--radius3); padding: 0.2rem 0.65rem; font-size: 0.72rem; font-weight: 600; color: var(--accent); }

  /* PRODUCTS */
  .filter-bar { display: flex; gap: 0.6rem; flex-wrap: wrap; margin: 1.5rem 0 0.5rem; }
  .filter-chip { background: var(--surface2); border: 1.5px solid var(--border); border-radius: var(--radius3); padding: 0.4rem 1rem; font-size: 0.8rem; font-weight: 600; color: var(--text2); cursor: pointer; transition: all 0.2s; white-space: nowrap; }
  .filter-chip.active, .filter-chip:hover { background: var(--text); color: #fff; border-color: var(--text); }
  .search-wrap { position: relative; display: inline-block; width: 100%; max-width: 380px; margin-bottom: 1.5rem; }
  .search-icon { position: absolute; left: 0.8rem; top: 50%; transform: translateY(-50%); color: var(--text3); font-size: 0.9rem; pointer-events: none; }
  .search-input { background: var(--surface2); border: 1.5px solid var(--border); border-radius: var(--radius2); padding: 0.65rem 1rem 0.65rem 2.5rem; font-family: 'DM Sans', sans-serif; font-size: 0.9rem; color: var(--text); outline: none; width: 100%; transition: border-color 0.2s; }
  .search-input:focus { border-color: var(--accent); }
  .products-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.25rem; }
  .product-card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 1.5rem; box-shadow: var(--shadow); transition: transform 0.25s, box-shadow 0.25s; display: flex; flex-direction: column; }
  .product-card:hover { transform: translateY(-4px); box-shadow: var(--shadow2); }
  .product-tag { display: inline-block; background: var(--surface2); color: var(--accent); border: 1px solid var(--border2); border-radius: var(--radius3); padding: 0.2rem 0.65rem; font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 0.85rem; }
  .product-card h3 { font-family: 'Syne', sans-serif; font-size: 1rem; font-weight: 700; line-height: 1.3; margin-bottom: 0.5rem; color: var(--text); }
  .product-card p { color: var(--text2); font-size: 0.83rem; line-height: 1.6; flex: 1; margin-bottom: 1rem; }
  .product-meta { display: flex; flex-direction: column; gap: 0.5rem; margin-top: auto; }
  .meta-pill { background: var(--surface2); border-radius: var(--radius2); padding: 0.5rem 0.75rem; font-size: 0.8rem; color: var(--text); display: flex; justify-content: space-between; }
  .modules-list { display: flex; flex-wrap: wrap; gap: 0.35rem; margin-top: 0.75rem; }
  .module-chip { background: var(--surface3); border-radius: var(--radius3); padding: 0.2rem 0.6rem; font-size: 0.7rem; color: var(--text2); }
  .no-results { text-align: center; color: var(--text3); padding: 3rem; font-size: 0.95rem; }

  /* PREMIUM */
  .premium-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.25rem; margin-top: 1.5rem; }
  .premium-card { background: var(--text); color: #fff; border-radius: var(--radius); padding: 1.75rem; position: relative; overflow: hidden; transition: transform 0.25s; }
  .premium-card::before { content: ''; position: absolute; top: -40px; right: -40px; width: 140px; height: 140px; background: radial-gradient(circle, rgba(212,96,26,0.35), transparent 70%); pointer-events: none; }
  .premium-card:hover { transform: translateY(-4px); }
  .premium-tier { font-size: 0.7rem; font-weight: 700; letter-spacing: 0.1em; color: var(--accent2); text-transform: uppercase; margin-bottom: 0.75rem; }
  .premium-card h3 { font-family: 'Syne', sans-serif; font-size: 1.05rem; font-weight: 800; margin-bottom: 0.5rem; line-height: 1.3; }
  .premium-card p { color: rgba(255,255,255,0.6); font-size: 0.83rem; line-height: 1.6; margin-bottom: 1rem; }
  .premium-price { font-family: 'Syne', sans-serif; font-size: 1.35rem; font-weight: 800; color: var(--accent2); margin-bottom: 0.25rem; }
  .premium-duration { font-size: 0.78rem; color: rgba(255,255,255,0.5); }
  .premium-features { list-style: none; margin-top: 1rem; display: flex; flex-direction: column; gap: 0.4rem; }
  .premium-features li { font-size: 0.8rem; color: rgba(255,255,255,0.75); display: flex; align-items: center; gap: 0.5rem; }
  .premium-features li::before { content: '✓'; color: var(--accent2); font-weight: 700; flex-shrink: 0; }

  /* MENTORS */
  .mentors-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; margin-top: 1.5rem; }
  .mentor-card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 1.25rem; text-align: center; box-shadow: var(--shadow); transition: transform 0.2s; }
  .mentor-card:hover { transform: translateY(-3px); }
  .mentor-avatar { width: 58px; height: 58px; border-radius: 18px; background: linear-gradient(135deg, var(--accent), var(--accent3)); color: #fff; display: flex; align-items: center; justify-content: center; font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.05rem; margin: 0 auto 0.75rem; }
  .mentor-name { font-weight: 600; font-size: 0.88rem; color: var(--text); margin-bottom: 0.2rem; }
  .mentor-role { font-size: 0.76rem; color: var(--text3); }

  /* SUPPORT */
  .support-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; margin-top: 1.5rem; }
  .support-card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 1.75rem; box-shadow: var(--shadow); }
  .support-icon { font-size: 1.75rem; margin-bottom: 0.75rem; }
  .support-card h3 { font-family: 'Syne', sans-serif; font-size: 1.1rem; font-weight: 700; margin-bottom: 0.75rem; }
  .contact-item { display: flex; align-items: center; gap: 0.6rem; margin-bottom: 0.5rem; color: var(--text2); font-size: 0.9rem; }
  .contact-item a { color: var(--accent); text-decoration: none; font-weight: 500; }

  /* CHATBOT */
  .chat-fab { position: fixed; bottom: 1.75rem; right: 1.75rem; z-index: 200; width: 62px; height: 62px; border-radius: 50%; background: linear-gradient(135deg, var(--accent), var(--accent3)); color: #fff; border: none; cursor: pointer; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; box-shadow: 0 8px 28px rgba(212,96,26,0.4); transition: transform 0.2s, box-shadow 0.2s; }
  .chat-fab:hover { transform: scale(1.08); box-shadow: 0 14px 40px rgba(212,96,26,0.5); }
  .chat-badge { position: absolute; top: -4px; right: -4px; background: #22c55e; border: 2px solid var(--bg); width: 16px; height: 16px; border-radius: 50%; animation: pulse 2s infinite; }
  .chat-window { position: fixed; bottom: 5.5rem; right: 1.75rem; z-index: 200; width: 390px; max-height: 590px; background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); box-shadow: 0 24px 64px rgba(26,18,8,0.18); display: flex; flex-direction: column; transform: scale(0.92) translateY(16px); opacity: 0; pointer-events: none; transition: transform 0.25s cubic-bezier(0.34,1.56,0.64,1), opacity 0.2s; overflow: hidden; }
  .chat-window.open { transform: scale(1) translateY(0); opacity: 1; pointer-events: all; }
  .chat-header { background: var(--text); color: #fff; padding: 1rem 1.25rem; display: flex; align-items: center; gap: 0.75rem; }
  .chat-header-avatar { width: 38px; height: 38px; border-radius: 12px; background: linear-gradient(135deg, var(--accent), var(--accent3)); display: flex; align-items: center; justify-content: center; font-size: 1rem; flex-shrink: 0; }
  .chat-header-info { flex: 1; }
  .chat-header-name { font-family: 'Syne', sans-serif; font-weight: 700; font-size: 0.95rem; }
  .chat-header-status { font-size: 0.72rem; color: rgba(255,255,255,0.55); }
  .chat-close { background: rgba(255,255,255,0.12); border: none; color: #fff; width: 30px; height: 30px; border-radius: 8px; cursor: pointer; font-size: 1rem; transition: background 0.2s; flex-shrink: 0; }
  .chat-close:hover { background: rgba(255,255,255,0.22); }
  .chat-lang-bar { padding: 0.6rem 1rem; background: var(--surface2); border-bottom: 1px solid var(--border); display: flex; align-items: center; gap: 0.5rem; flex-wrap: wrap; }
  .chat-lang-bar span { font-size: 0.7rem; color: var(--text2); font-weight: 600; }
  .lang-btn { background: transparent; border: 1px solid var(--border2); border-radius: var(--radius3); padding: 0.18rem 0.6rem; font-size: 0.7rem; font-weight: 600; color: var(--text2); cursor: pointer; transition: all 0.15s; }
  .lang-btn.active, .lang-btn:hover { background: var(--accent); color: #fff; border-color: var(--accent); }
  .chat-messages { flex: 1; overflow-y: auto; padding: 1rem; display: flex; flex-direction: column; gap: 0.75rem; scroll-behavior: smooth; }
  .chat-messages::-webkit-scrollbar { width: 4px; }
  .chat-messages::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 2px; }
  .msg { max-width: 82%; display: flex; flex-direction: column; gap: 0.2rem; }
  .msg.user { align-self: flex-end; align-items: flex-end; }
  .msg.bot { align-self: flex-start; align-items: flex-start; }
  .msg-bubble { padding: 0.7rem 1rem; border-radius: 16px; font-size: 0.87rem; line-height: 1.6; white-space: pre-wrap; }
  .msg.user .msg-bubble { background: var(--accent); color: #fff; border-radius: 16px 16px 4px 16px; }
  .msg.bot .msg-bubble { background: var(--surface2); color: var(--text); border: 1px solid var(--border); border-radius: 16px 16px 16px 4px; }
  .msg-time { font-size: 0.68rem; color: var(--text3); }
  .chat-typing { display: flex; gap: 0.3rem; align-items: center; padding: 0.7rem 1rem; background: var(--surface2); border: 1px solid var(--border); border-radius: 16px 16px 16px 4px; width: fit-content; }
  .typing-dot { width: 6px; height: 6px; border-radius: 50%; background: var(--text3); animation: typing 1.2s infinite; }
  .typing-dot:nth-child(2) { animation-delay: 0.2s; }
  .typing-dot:nth-child(3) { animation-delay: 0.4s; }
  .quick-chips { padding: 0 1rem 0.75rem; display: flex; gap: 0.4rem; flex-wrap: wrap; }
  .quick-chip { background: var(--surface2); border: 1px solid var(--border2); border-radius: var(--radius3); padding: 0.3rem 0.8rem; font-size: 0.74rem; font-weight: 500; color: var(--text2); cursor: pointer; transition: all 0.15s; white-space: nowrap; }
  .quick-chip:hover { background: var(--surface3); border-color: var(--accent); color: var(--accent); }
  .chat-input-bar { padding: 0.85rem 1rem; border-top: 1px solid var(--border); display: flex; gap: 0.6rem; align-items: flex-end; background: var(--surface); }
  .chat-textarea { flex: 1; background: var(--surface2); border: 1.5px solid var(--border); border-radius: var(--radius2); padding: 0.65rem 0.9rem; font-family: 'DM Sans', sans-serif; font-size: 0.88rem; color: var(--text); outline: none; resize: none; min-height: 42px; max-height: 120px; transition: border-color 0.2s; line-height: 1.5; }
  .chat-textarea:focus { border-color: var(--accent); }
  .chat-textarea::placeholder { color: var(--text3); }
  .chat-send { background: var(--accent); color: #fff; border: none; width: 42px; height: 42px; border-radius: 12px; cursor: pointer; display: flex; align-items: center; justify-content: center; font-size: 1rem; flex-shrink: 0; transition: background 0.2s, transform 0.15s; }
  .chat-send:hover { background: #c0531a; transform: scale(1.05); }
  .chat-send:disabled { background: var(--border2); cursor: not-allowed; transform: none; }

  /* FOOTER */
  footer { background: var(--text); color: rgba(255,255,255,0.55); text-align: center; padding: 2rem; font-size: 0.82rem; line-height: 1.8; margin-top: 2rem; }
  footer strong { color: rgba(255,255,255,0.8); }

  @keyframes fadeUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
  @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.4; } }
  @keyframes typing { 0%, 80%, 100% { transform: translateY(0); opacity: 0.4; } 40% { transform: translateY(-5px); opacity: 1; } }

  @media (max-width: 900px) {
    .hero-section { grid-template-columns: 1fr; }
    .hero-card { display: none; }
    .products-grid { grid-template-columns: 1fr 1fr; }
    .premium-grid { grid-template-columns: 1fr; }
    .mentors-grid { grid-template-columns: 1fr 1fr; }
    .support-grid { grid-template-columns: 1fr; }
    .predictor-grid { grid-template-columns: 1fr 1fr; }
    .nav-links { display: none; }
    .chat-window { width: calc(100vw - 2rem); right: 1rem; }
  }
  @media (max-width: 600px) { .products-grid { grid-template-columns: 1fr; } }
</style>
</head>
<body>

<nav>
  <a class="nav-brand" href="#">
    <div class="nav-logo">IM</div>
    <div>
      <div class="nav-title">INVESMATE</div>
      <div class="nav-tagline">Stock Market Learning</div>
    </div>
  </a>
  <div class="nav-links">
    <a href="#products">Products</a>
    <a href="#insignia">INSIGNIA</a>
    <a href="#mentors">Mentors</a>
    <a href="#support">Support</a>
    <a href="#support" class="nav-cta">Request Callback</a>
  </div>
</nav>

<div class="hero-section">
  <div>
    <div class="hero-badge">&#9679; SEBI Registered RA: INH000017985</div>
    <h1>Finest Stock Market <em>Learning</em> Experience</h1>
    <p class="hero-sub">A professional platform for INVESMATE and INSIGNIA — with AI-guided course selection, multilingual support, and personalized mentorship plans for every learner.</p>
    <div class="hero-actions">
      <a href="#products" class="btn-primary">Explore Courses &darr;</a>
      <a href="#" class="btn-outline" onclick="openChat(); return false;">Talk to AI Advisor</a>
    </div>
  </div>
  <div class="hero-card">
    <span class="hero-card-label">Premium Learning Path</span>
    <h3>Find the right course in minutes</h3>
    <p>Use our AI advisor and course predictor to choose between beginner, trading, investing, derivatives, and INSIGNIA mentorship plans.</p>
    <div class="info-row"><strong>Personalized Prediction</strong><small>Course recommendation by goal, budget &amp; experience</small></div>
    <div class="info-row"><strong>Multilingual Support</strong><small>English, Bengali, Hindi &amp; Auto-Detect</small></div>
    <div class="info-row"><strong>INSIGNIA Premium</strong><small>1:1 mentorship, live sessions &amp; lifetime recordings</small></div>
  </div>
</div>

<div class="stats-strip">
  <div class="stat-item"><div class="stat-num">20+</div><div class="stat-label">Expert Courses</div></div>
  <div class="stat-item"><div class="stat-num">8</div><div class="stat-label">Certified Mentors</div></div>
  <div class="stat-item"><div class="stat-num">3</div><div class="stat-label">Language Support</div></div>
  <div class="stat-item"><div class="stat-num">SEBI</div><div class="stat-label">Registered RA</div></div>
</div>



<!-- PRODUCTS -->
<div class="section" id="products">
  <div class="section-eyebrow">All Products</div>
  <div class="section-title">Complete Product Ecosystem</div>
  <div class="filter-bar" id="filter-bar"></div>
  <div class="search-wrap">
    <span class="search-icon">&#9906;</span>
    <input class="search-input" id="search-input" type="text" placeholder="Search courses and mentorship plans&hellip;" oninput="renderProducts()" />
  </div>
  <div class="products-grid" id="products-grid"></div>
</div>

<hr class="divider"/>

<!-- INSIGNIA -->
<div class="section" id="insignia">
  <div class="section-eyebrow">INSIGNIA Premium Journey</div>
  <div class="section-title">Premium Mentorship Plans</div>
  <div class="section-sub">Intensive, structured mentorship programs combining live sessions, 1:1 guidance, and real market practice.</div>
  <div class="premium-grid" id="premium-grid"></div>
</div>

<hr class="divider"/>

<!-- MENTORS -->
<div class="section" id="mentors">
  <div class="section-eyebrow">Top Mentors</div>
  <div class="section-title">Experienced Market Mentors</div>
  <div class="mentors-grid" id="mentors-grid"></div>
</div>

<hr class="divider"/>

<!-- SUPPORT -->
<div class="section" id="support">
  <div class="section-eyebrow">Support</div>
  <div class="section-title">Talk to the team before you enroll</div>
  <div class="support-grid">
    <div class="support-card">
      <div class="support-icon">&#128222;</div>
      <h3>Counseling &amp; Support</h3>
      <div class="contact-item">&#128241; <a href="tel:+919016791791">+91 9016791791</a></div>
      <div class="contact-item">&#128241; <a href="tel:+917596037781">+91 7596037781</a></div>
      <div class="contact-item">&#128241; <a href="tel:+917003110622">+91 7003110622</a></div>
      <div class="contact-item">&#9993; <a href="mailto:support@invesmate.com">support@invesmate.com</a></div>
      <div class="contact-item">&#9993; <a href="mailto:sales@invesmate.com">sales@invesmate.com</a></div>
    </div>
    <div class="support-card">
      <div class="support-icon">&#9888;</div>
      <h3>Disclaimer</h3>
      <p style="color:var(--text2);font-size:0.88rem;line-height:1.7;">Investment in securities markets is subject to market risks. Read all the related documents carefully before investing. Registration granted by SEBI and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors.<br/><br/>INVESMATE INSIGHTS — SEBI Registered Research Analyst (INH000017985). This platform is for educational purposes only.</p>
    </div>
  </div>
</div>

<footer>
  <strong>INVESMATE</strong> — Stock Market Learning Platform<br/>
  SEBI Registered RA: INH000017985 &nbsp;|&nbsp; support@invesmate.com<br/>
  &copy; 2026 INVESMATE. All rights reserved. For educational purposes only.
</footer>

<!-- CHAT FAB -->
<button class="chat-fab" onclick="toggleChat()" id="chat-fab" title="AI Advisor">
  &#128172;
  <span class="chat-badge"></span>
</button>

<!-- CHAT WINDOW -->
<div class="chat-window" id="chat-window">
  <div class="chat-header">
    <div class="chat-header-avatar">&#129302;</div>
    <div class="chat-header-info">
      <div class="chat-header-name">INVESMATE AI Advisor</div>
      <div class="chat-header-status">&#9679; Online &mdash; Powered by Claude AI</div>
    </div>
    <button class="chat-close" onclick="toggleChat()">&times;</button>
  </div>
  <div class="chat-lang-bar">
    <span>Language:</span>
    <button class="lang-btn active" onclick="setLang('English',this)">EN</button>
    <button class="lang-btn" onclick="setLang('Bengali',this)">&#2476;&#2494;&#2434;&#2482;&#2494;</button>
    <button class="lang-btn" onclick="setLang('Hindi',this)">&#2361;&#2367;&#2306;&#2342;&#2368;</button>
    <button class="lang-btn" onclick="setLang('Auto',this)">Auto</button>
  </div>
  <div class="chat-messages" id="chat-messages"></div>
  <div class="quick-chips" id="quick-chips">
    <button class="quick-chip" onclick="showPredictorWidget()">🎯 Course Predictor</button>
    <button class="quick-chip" onclick="sendQuick('Compare INSIGNIA plans')">INSIGNIA plans</button>
    <button class="quick-chip" onclick="sendQuick('What are the fees and pricing?')">Pricing</button>
    <button class="quick-chip" onclick="sendQuick('How do I enroll?')">Enrollment</button>
  </div>
  <div class="chat-input-bar">
    <textarea class="chat-textarea" id="chat-input" placeholder="Ask about courses, pricing, enrollment&hellip;" rows="1" onkeydown="handleChatKey(event)" oninput="autoResize(this)"></textarea>
    <button class="chat-send" id="send-btn" onclick="sendMessage()">&#10148;</button>
  </div>
</div>

<script>
const PRODUCTS_DATA = [
  {title:"Power of Trading and Investing Combo Course",category:"Live Course",tag:"Beginner",price:"Rs. 8,999 – Rs. 11,999",duration:"2 Months / 26 Hours",lessons:"57 Lessons",description:"A complete capital-market course covering trading and investing from basics to advanced level.",modules:["Market basics","Technical analysis","Investing foundation","Real market practice"]},
  {title:"Complete Intraday and Swing Trading Strategies",category:"Live Course",tag:"Technical Trading",price:"Rs. 9,999 – Rs. 12,999",duration:"2 Months / 20 Hours",lessons:"48 Lessons",description:"Advanced technical-analysis course for intraday and swing trading.",modules:["Chart patterns","Indicators","Smart Money Concepts","Risk control"]},
  {title:"Complete Future and Option Trading Strategies",category:"Live Course",tag:"Derivatives",price:"Rs. 12,999 – Rs. 15,999",duration:"2 Months / 26 Hours",lessons:"25 Lessons",description:"Futures and options training for learners who want derivatives strategy knowledge.",modules:["Futures basics","Option buying","Option selling","Hedging"]},
  {title:"Value Investing Using Advanced Fundamental Analysis",category:"Live Course",tag:"Investing",price:"Rs. 8,999 – Rs. 11,999",duration:"2 Months / 24 Hours",lessons:"57 Lessons",description:"Fundamental-analysis and value-investing roadmap for long-term equity investors.",modules:["Business analysis","Financial statements","Valuation","Portfolio mindset"]},
  {title:"Introduction To Mutual Funds Investment",category:"Course",tag:"Mutual Funds",price:"Rs. 3,999 – Rs. 6,999",duration:"1 Month",lessons:"24 Lessons",description:"Practical overview of mutual funds, SIPs, and fund selection.",modules:["MF basics","SIP planning","Fund selection","Long-term wealth"]},
  {title:"Dynamic Investment With Fixed Income Securities",category:"Recorded Course",tag:"Fixed Income",price:"Rs. 10,999",duration:"12 Hours",lessons:"33 Lessons",description:"Recorded course on bonds, government securities, income products, and diversification.",modules:["Bonds","Government securities","Income planning","Diversification"]},
  {title:"The Comprehensive Roadmap Of Commodity Market",category:"Live Course",tag:"Commodity",price:"Rs. 14,999",duration:"16 Hours",lessons:"10 Lessons",description:"Commodity-market course covering gold, silver, crude oil, natural gas, and risk management.",modules:["Gold and silver","Crude oil","Natural gas","Technical view"]},
  {title:"Power TI Masterclass",category:"Free Entry Program",tag:"Masterclass",price:"Free / Registration",duration:"Short Session",lessons:"Live Session",description:"Entry-level masterclass for learners starting their stock-market journey.",modules:["Orientation","Counseling","Beginner roadmap","Q&A"]},
  {title:"Share Samadhan",category:"Newsletter & Research",tag:"Market Study",price:"Included in selected plans",duration:"Weekly Access",lessons:"Premium Study",description:"Weekly Bengali stock-market study for cash, derivatives, IPOs, mutual funds, and trends.",modules:["Cash market","Derivatives","IPO study","Mutual funds"]},
  {title:"Market Trending All Segment",category:"Premium Tool Access",tag:"Market Intelligence",price:"Included in INSIGNIA plans",duration:"Plan-based Access",lessons:"All Segment Access",description:"Premium market-trending access included in selected INSIGNIA programs.",modules:["Cash","Derivatives","Commodity","Fixed asset investment"]},
  {title:"INVESMATE Learning App",category:"Mobile App",tag:"Learning Platform",price:"App-based Access",duration:"Anytime Learning",lessons:"Course Library",description:"Mobile app for classes, recordings, academic support, and My Insignia Help.",modules:["Live classes","Recordings","Support","Course access"]},
  {title:"Insights.Market",category:"Research Brand",tag:"SEBI RA Research",price:"Separate research platform",duration:"Research Access",lessons:"Research Products",description:"SEBI-registered equity research brand under INVESMATE INSIGHTS.",modules:["Equity research","Investor charter","Disclosures","Compliance"]},
];

const INSIGNIA_DATA = [
  {title:"Equity Market Intelligence Matrix",tag:"Premium Mentorship",price:"Rs. 38,571 / Rs. 44,420",duration:"3–5 Months",description:"Premium mentorship combining advanced technical, techno-funda, and fundamental analysis.",modules:["Market Trending","Share Samadhan","1:1 mentorship","4 practical sessions","NISM guidance"]},
  {title:"Complete Equity and Derivative Dynasty",tag:"Options Premium",price:"Rs. 62,305 / Rs. 44,420",duration:"6–8 Months",description:"Advanced premium pathway combining technical, fundamental, derivatives, and fixed-income learning.",modules:["Advanced Technical","Complete Options","Fixed Income","8 practical sessions","Academic helpline"]},
  {title:"Complete Global Capital Market Specialist",tag:"Global Premium",price:"Rs. 1,07,689 / Rs. 44,420",duration:"12 Months",description:"Full-stack global capital-market specialist path including commodities, US stocks, mutual funds, and software training.",modules:["US stocks","Commodity","Advanced mutual fund","3 mentorship sessions","Lifetime recordings"]},
];

const MENTORS_LIST = ["Arunava Chatterjee","Sayan Ghosh","Kunal Saha","Suman Goswami","Laboni Pallab Das","Debarati Mukherjee","Pratim Kumar Chakraborty","Mihir Kanti Chakraborty"];

// ── FILTER & RENDER ──
let activeCategory = 'All';
const allCategories = ['All', ...new Set(PRODUCTS_DATA.map(p => p.category))];

function initFilters() {
  document.getElementById('filter-bar').innerHTML = allCategories.map(c =>
    `<button class="filter-chip ${c==='All'?'active':''}" onclick="setCategory('${c.replace(/'/g,"\\'")}',this)">${c}</button>`
  ).join('');
}

function setCategory(cat, el) {
  activeCategory = cat;
  document.querySelectorAll('.filter-chip').forEach(b => b.classList.remove('active'));
  el.classList.add('active');
  renderProducts();
}

function norm(t) { return (t||'').toLowerCase(); }

function renderProducts() {
  const q = norm(document.getElementById('search-input').value);
  const grid = document.getElementById('products-grid');
  const filtered = PRODUCTS_DATA.filter(p => {
    const catOk = activeCategory === 'All' || p.category === activeCategory;
    const qOk = !q || norm(p.title + ' ' + p.description).includes(q);
    return catOk && qOk;
  });
  if (!filtered.length) {
    grid.innerHTML = `<div class="no-results" style="grid-column:1/-1">No courses found. Try a different search or category.</div>`;
    return;
  }
  grid.innerHTML = filtered.map(p => `
    <div class="product-card">
      <span class="product-tag">${esc(p.category)}</span>
      <h3>${esc(p.title)}</h3>
      <p>${esc(p.description)}</p>
      <div class="product-meta">
        <div class="meta-pill"><span>${esc(p.price)}</span></div>
        <div class="meta-pill"><span>&#9201; ${esc(p.duration)}</span><span>${esc(p.lessons)}</span></div>
      </div>
      <div class="modules-list">${p.modules.slice(0,4).map(m=>`<span class="module-chip">${esc(m)}</span>`).join('')}</div>
    </div>`).join('');
}

function renderInsignia() {
  document.getElementById('premium-grid').innerHTML = INSIGNIA_DATA.map(p => `
    <div class="premium-card">
      <div class="premium-tier">${esc(p.tag)}</div>
      <h3>${esc(p.title)}</h3>
      <p>${esc(p.description)}</p>
      <div class="premium-price">${esc(p.price)}</div>
      <div class="premium-duration">&#9201; ${esc(p.duration)}</div>
      <ul class="premium-features">${p.modules.map(m=>`<li>${esc(m)}</li>`).join('')}</ul>
    </div>`).join('');
}

function renderMentors() {
  document.getElementById('mentors-grid').innerHTML = MENTORS_LIST.map(m => {
    const initials = m.split(' ').map(w=>w[0]).slice(0,2).join('');
    return `<div class="mentor-card"><div class="mentor-avatar">${esc(initials)}</div><div class="mentor-name">${esc(m)}</div><div class="mentor-role">Capital market mentor &amp; NISM-certified professional</div></div>`;
  }).join('');
}

// ── PREDICTOR ──
function predictCourse(goal, exp, budget) {
  const g = norm(goal), b = norm(budget);
  if (g.includes('option') || g.includes('derivative')) return b.includes('premium') ? {...INSIGNIA_DATA[1]} : PRODUCTS_DATA[2];
  if (g.includes('commodity') || g.includes('global')) return b.includes('premium') ? {...INSIGNIA_DATA[2]} : PRODUCTS_DATA[6];
  if (g.includes('mutual') || g.includes('sip')) return PRODUCTS_DATA[4];
  if (g.includes('intraday') || g.includes('swing') || g.includes('technical')) return b.includes('premium') ? {...INSIGNIA_DATA[0]} : PRODUCTS_DATA[1];
  if (g.includes('long') || g.includes('fundamental') || g.includes('invest')) return b.includes('premium') ? {...INSIGNIA_DATA[0]} : PRODUCTS_DATA[3];
  return b.includes('premium') ? {...INSIGNIA_DATA[0]} : PRODUCTS_DATA[0];
}

// ── CHATBOT ──
let chatOpen = false, chatLang = 'English', chatHistory = [], isTyping = false;

const SYSTEM_PROMPT = `You are the INVESMATE AI Advisor — a knowledgeable, warm, and professional stock market learning advisor for INVESMATE, a SEBI-registered Research Analyst platform (INH000017985) in India.

Your role:
- Help users choose the right INVESMATE or INSIGNIA course based on their goals, experience, budget, and language.
- Answer questions about courses, pricing, enrollment, mentors, features, refunds, EMI, and support clearly and helpfully.
- Be concise and friendly. Use bullet points when listing multiple items.
- Always add a brief risk disclaimer when discussing trading or investments.

INVESMATE Courses:
• Power of Trading and Investing Combo — Live, Beginner, Rs. 8,999–11,999, 2 months/26 hrs, 57 lessons
• Complete Intraday and Swing Trading Strategies — Live, Rs. 9,999–12,999, 2 months/20 hrs
• Complete Future and Option Trading Strategies — Live, Rs. 12,999–15,999, 2 months/26 hrs
• Value Investing Using Advanced Fundamental Analysis — Live, Rs. 8,999–11,999, 2 months/24 hrs
• Introduction To Mutual Funds Investment — Rs. 3,999–6,999, 1 month
• Dynamic Investment With Fixed Income Securities — Recorded, Rs. 10,999, 12 hrs
• The Comprehensive Roadmap Of Commodity Market — Live, Rs. 14,999, 16 hrs
• Power TI Masterclass — Free entry program

INSIGNIA Premium Mentorship:
• Equity Market Intelligence Matrix — Rs. 38,571/44,420, 3–5 months, technical + fundamental, 1:1 mentorship, 4 practical sessions
• Complete Equity and Derivative Dynasty — Rs. 62,305/44,420, 6–8 months, equity + options + fixed income
• Complete Global Capital Market Specialist — Rs. 1,07,689/44,420, 12 months, US stocks, commodities, global markets

INSIGNIA Personalized Series (I–VIII): Counseling-based pricing, personalized mentorship paths.

Mentors: Arunava Chatterjee, Sayan Ghosh, Kunal Saha, Suman Goswami, Laboni Pallab Das, Debarati Mukherjee, Pratim Kumar Chakraborty, Mihir Kanti Chakraborty — all NISM-certified.

Support: +91 9016791791, +91 7596037781, +91 7003110622 | support@invesmate.com | sales@invesmate.com

Enrollment flow: Choose product → request counseling → confirm fee/GST/EMI/batch timing → complete payment → access via app.

Language: Current selected language is {{LANG}}. If user writes in Bengali, reply in Bengali. If Hindi, reply in Hindi. Otherwise use English.

Important: Always include "Note: Investment in securities markets is subject to market risks." when discussing trading strategies or returns.`;

function toggleChat() {
  chatOpen = !chatOpen;
  const win = document.getElementById('chat-window');
  win.classList.toggle('open', chatOpen);
  document.getElementById('chat-fab').innerHTML = chatOpen
    ? '&times;<span class="chat-badge"></span>'
    : '&#128172;<span class="chat-badge"></span>';
  if (chatOpen && chatHistory.length === 0) {
    addBotMsg("Hi! I'm your INVESMATE AI Advisor 👋\n\nI can help you:\n• Choose the right course for your goals\n• Compare INSIGNIA mentorship plans\n• Get pricing and enrollment details\n• Route your support request\n\nWhat would you like to know?");
  }
}

function openChat() { if (!chatOpen) toggleChat(); }

function setLang(lang, el) {
  chatLang = lang;
  document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
  el.classList.add('active');
}

function esc(t) {
  return String(t||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

function addMsg(text, role) {
  const msgs = document.getElementById('chat-messages');
  const now = new Date().toLocaleTimeString([],{hour:'2-digit',minute:'2-digit'});
  const div = document.createElement('div');
  div.className = 'msg ' + role;
  div.innerHTML = `<div class="msg-bubble">${esc(text)}</div><span class="msg-time">${now}</span>`;
  msgs.appendChild(div);
  msgs.scrollTop = msgs.scrollHeight;
  chatHistory.push({role: role === 'user' ? 'user' : 'assistant', content: text});
}

function addBotMsg(t) { addMsg(t, 'bot'); }
function addUserMsg(t) { addMsg(t, 'user'); }

function showTyping() {
  const msgs = document.getElementById('chat-messages');
  const div = document.createElement('div');
  div.className = 'msg bot'; div.id = 'typing-indicator';
  div.innerHTML = `<div class="chat-typing"><span class="typing-dot"></span><span class="typing-dot"></span><span class="typing-dot"></span></div>`;
  msgs.appendChild(div);
  msgs.scrollTop = msgs.scrollHeight;
}

function removeTyping() { const t = document.getElementById('typing-indicator'); if(t) t.remove(); }

async function sendMessage() {
  const input = document.getElementById('chat-input');
  const text = input.value.trim();
  if (!text || isTyping) return;
  input.value = ''; autoResize(input);
  addUserMsg(text);
  document.getElementById('send-btn').disabled = true;
  isTyping = true;
  showTyping();

  try {
    const system = SYSTEM_PROMPT.replace('{{LANG}}', chatLang);
    const apiMsgs = chatHistory.slice(-20);

    const res = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        model: 'claude-sonnet-4-20250514',
        max_tokens: 1000,
        system: system,
        messages: apiMsgs,
      })
    });

    removeTyping();
    const data = await res.json();

    if (data.content && data.content[0] && data.content[0].text) {
      addBotMsg(data.content[0].text);
    } else if (data.error) {
      addBotMsg('API error: ' + (data.error.message || 'Unknown error') + '\n\nPlease contact: support@invesmate.com');
    } else {
      addBotMsg('Sorry, I could not process your request. Please try again.');
    }
  } catch(err) {
    removeTyping();
    addBotMsg('Connection error. Please check your network.\n\nFor immediate help:\n📞 +91 9016791791\n✉️ support@invesmate.com');
  }

  isTyping = false;
  document.getElementById('send-btn').disabled = false;
  document.getElementById('chat-input').focus();
}

function sendQuick(text) { document.getElementById('chat-input').value = text; sendMessage(); }
function handleChatKey(e) { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); } }
function autoResize(el) { el.style.height = 'auto'; el.style.height = Math.min(el.scrollHeight, 120) + 'px'; }

// ── INIT ──
initFilters();
renderProducts();
renderInsignia();
renderMentors();
</script>
</body>
</html>
