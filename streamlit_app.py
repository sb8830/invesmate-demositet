<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>INVESMATE – Stock Market Learning Platform</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&display=swap" rel="stylesheet"/>
<style>
:root{
  --bg:#fafaf8;--surface:#fff;--s2:#f5f3ee;--s3:#ede9e0;
  --txt:#1a1208;--txt2:#6b6150;--txt3:#a09880;
  --acc:#d4601a;--acc2:#f08d3c;--acc3:#fbbf24;
  --bdr:#e6e0d4;--bdr2:#d4ccbe;
  --sh:0 4px 24px rgba(26,18,8,.08);--sh2:0 16px 48px rgba(26,18,8,.13);
  --r:20px;--r2:12px;--r3:999px;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:'DM Sans',sans-serif;background:var(--bg);color:var(--txt);font-size:16px;line-height:1.6;overflow-x:hidden}

/* ── NAV ── */
nav{position:sticky;top:0;z-index:100;background:rgba(250,250,248,.92);backdrop-filter:blur(20px);border-bottom:1px solid var(--bdr);padding:0 2rem;display:flex;align-items:center;justify-content:space-between;height:68px}
.nav-brand{display:flex;align-items:center;gap:.75rem;text-decoration:none}
.nav-logo{width:42px;height:42px;border-radius:14px;background:linear-gradient(135deg,var(--acc),var(--acc3));display:flex;align-items:center;justify-content:center;font-family:'Syne',sans-serif;font-weight:800;font-size:1rem;color:#fff;box-shadow:0 6px 20px rgba(212,96,26,.3)}
.nav-title{font-family:'Syne',sans-serif;font-weight:800;font-size:1.15rem;color:var(--txt)}
.nav-tagline{font-size:.7rem;color:var(--acc);font-weight:600;letter-spacing:.08em;text-transform:uppercase}
.nav-links{display:flex;align-items:center;gap:2rem}
.nav-links a{color:var(--txt2);font-weight:500;text-decoration:none;font-size:.9rem;transition:color .2s}
.nav-links a:hover{color:var(--txt)}
.nav-cta{background:var(--txt)!important;color:#fff!important;padding:.5rem 1.2rem;border-radius:var(--r3);font-weight:600!important;font-size:.85rem!important}
.nav-cta:hover{background:var(--acc)!important}

/* ── HERO ── */
.hero-wrap{padding:5rem 2rem 4rem;max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1fr 420px;gap:3rem;align-items:center;animation:fadeUp .7s ease both}
.hero-badge{display:inline-flex;align-items:center;gap:.5rem;background:var(--s2);border:1px solid var(--bdr2);border-radius:var(--r3);padding:.35rem .9rem;font-size:.75rem;font-weight:600;color:var(--acc);letter-spacing:.06em;text-transform:uppercase;margin-bottom:1.2rem}
.hero-badge::before{content:'●';font-size:.5rem;animation:pulse 2s infinite}
.hero-wrap h1{font-family:'Syne',sans-serif;font-size:clamp(2.8rem,5.5vw,4.8rem);font-weight:800;line-height:.96;letter-spacing:-.05em;margin-bottom:1.25rem}
.hero-wrap h1 em{font-style:normal;color:var(--acc)}
.hero-sub{font-size:1.05rem;color:var(--txt2);line-height:1.75;max-width:520px;margin-bottom:2rem}
.hero-actions{display:flex;gap:.75rem;flex-wrap:wrap}
.btn-pri{background:var(--acc);color:#fff;padding:.85rem 1.6rem;border-radius:var(--r3);font-weight:600;font-size:.95rem;border:none;cursor:pointer;text-decoration:none;display:inline-flex;align-items:center;gap:.4rem;box-shadow:0 8px 24px rgba(212,96,26,.28);transition:transform .2s,box-shadow .2s}
.btn-pri:hover{transform:translateY(-2px);box-shadow:0 14px 36px rgba(212,96,26,.36)}
.btn-out{background:transparent;color:var(--txt);padding:.85rem 1.6rem;border-radius:var(--r3);font-weight:600;font-size:.95rem;border:1.5px solid var(--bdr2);cursor:pointer;text-decoration:none;display:inline-flex;align-items:center;gap:.4rem;transition:border-color .2s,background .2s}
.btn-out:hover{border-color:var(--acc);background:var(--s2)}
.hero-card{background:var(--surface);border:1px solid var(--bdr);border-radius:var(--r);padding:1.75rem;box-shadow:var(--sh2)}
.hc-label{display:inline-block;background:var(--acc);color:#fff;border-radius:var(--r3);padding:.25rem .75rem;font-size:.72rem;font-weight:700;letter-spacing:.04em;text-transform:uppercase;margin-bottom:1rem}
.hero-card h3{font-family:'Syne',sans-serif;font-size:1.2rem;font-weight:700;margin-bottom:.5rem}
.hero-card p{color:var(--txt2);font-size:.88rem;margin-bottom:1.25rem}
.info-row{background:var(--s2);border-radius:var(--r2);padding:.85rem 1rem;margin-bottom:.6rem;border:1px solid var(--bdr)}
.info-row strong{display:block;font-size:.88rem;margin-bottom:.2rem}
.info-row small{color:var(--txt2);font-size:.8rem}

/* ── STATS ── */
.stats{background:var(--txt);color:#fff;padding:2rem;display:flex;justify-content:center}
.stat{flex:1;max-width:220px;text-align:center;padding:0 2rem;border-right:1px solid rgba(255,255,255,.12)}
.stat:last-child{border-right:none}
.stat-n{font-family:'Syne',sans-serif;font-size:2.5rem;font-weight:800;color:var(--acc2)}
.stat-l{font-size:.82rem;color:rgba(255,255,255,.6);margin-top:.2rem}

/* ── SECTIONS ── */
.sec{padding:4rem 2rem;max-width:1200px;margin:0 auto}
.eyebrow{font-size:.72rem;font-weight:700;color:var(--acc);letter-spacing:.1em;text-transform:uppercase;margin-bottom:.5rem}
.sec-title{font-family:'Syne',sans-serif;font-size:clamp(1.8rem,3.5vw,2.8rem);font-weight:800;letter-spacing:-.04em;margin-bottom:.5rem}
.sec-sub{color:var(--txt2);font-size:1rem;max-width:600px;line-height:1.7}
.divider{border:none;border-top:1px solid var(--bdr)}

/* ── PRODUCTS ── */
.filter-bar{display:flex;gap:.6rem;flex-wrap:wrap;margin:1.5rem 0 .5rem}
.fchip{background:var(--s2);border:1.5px solid var(--bdr);border-radius:var(--r3);padding:.4rem 1rem;font-size:.8rem;font-weight:600;color:var(--txt2);cursor:pointer;transition:all .2s;white-space:nowrap}
.fchip.active,.fchip:hover{background:var(--txt);color:#fff;border-color:var(--txt)}
.search-wrap{position:relative;display:inline-block;width:100%;max-width:380px;margin-bottom:1.5rem}
.search-icon{position:absolute;left:.8rem;top:50%;transform:translateY(-50%);color:var(--txt3);pointer-events:none}
.search-inp{background:var(--s2);border:1.5px solid var(--bdr);border-radius:var(--r2);padding:.65rem 1rem .65rem 2.5rem;font-family:'DM Sans',sans-serif;font-size:.9rem;color:var(--txt);outline:none;width:100%;transition:border-color .2s}
.search-inp:focus{border-color:var(--acc)}
.pgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.25rem}
.pcard{background:var(--surface);border:1px solid var(--bdr);border-radius:var(--r);padding:1.5rem;box-shadow:var(--sh);transition:transform .25s,box-shadow .25s;display:flex;flex-direction:column}
.pcard:hover{transform:translateY(-4px);box-shadow:var(--sh2)}
.ptag{display:inline-block;background:var(--s2);color:var(--acc);border:1px solid var(--bdr2);border-radius:var(--r3);padding:.2rem .65rem;font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:.85rem}
.pcard h3{font-family:'Syne',sans-serif;font-size:1rem;font-weight:700;line-height:1.3;margin-bottom:.5rem}
.pcard p{color:var(--txt2);font-size:.83rem;line-height:1.6;flex:1;margin-bottom:1rem}
.pmeta{display:flex;flex-direction:column;gap:.5rem;margin-top:auto}
.mpill{background:var(--s2);border-radius:var(--r2);padding:.5rem .75rem;font-size:.8rem;display:flex;justify-content:space-between}
.mods{display:flex;flex-wrap:wrap;gap:.35rem;margin-top:.75rem}
.mchip{background:var(--s3);border-radius:var(--r3);padding:.2rem .6rem;font-size:.7rem;color:var(--txt2)}
.no-res{text-align:center;color:var(--txt3);padding:3rem;font-size:.95rem;grid-column:1/-1}

/* ── PREMIUM ── */
.prem-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.25rem;margin-top:1.5rem}
.prem-card{background:var(--txt);color:#fff;border-radius:var(--r);padding:1.75rem;position:relative;overflow:hidden;transition:transform .25s}
.prem-card::before{content:'';position:absolute;top:-40px;right:-40px;width:140px;height:140px;background:radial-gradient(circle,rgba(212,96,26,.35),transparent 70%);pointer-events:none}
.prem-card:hover{transform:translateY(-4px)}
.prem-tier{font-size:.7rem;font-weight:700;letter-spacing:.1em;color:var(--acc2);text-transform:uppercase;margin-bottom:.75rem}
.prem-card h3{font-family:'Syne',sans-serif;font-size:1.05rem;font-weight:800;margin-bottom:.5rem;line-height:1.3}
.prem-card p{color:rgba(255,255,255,.6);font-size:.83rem;line-height:1.6;margin-bottom:1rem}
.prem-price{font-family:'Syne',sans-serif;font-size:1.35rem;font-weight:800;color:var(--acc2);margin-bottom:.25rem}
.prem-dur{font-size:.78rem;color:rgba(255,255,255,.5)}
.prem-feats{list-style:none;margin-top:1rem;display:flex;flex-direction:column;gap:.4rem}
.prem-feats li{font-size:.8rem;color:rgba(255,255,255,.75);display:flex;align-items:center;gap:.5rem}
.prem-feats li::before{content:'✓';color:var(--acc2);font-weight:700;flex-shrink:0}

/* ── MENTORS ── */
.mgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;margin-top:1.5rem}
.mcard{background:var(--surface);border:1px solid var(--bdr);border-radius:var(--r);padding:1.25rem;text-align:center;box-shadow:var(--sh);transition:transform .2s}
.mcard:hover{transform:translateY(-3px)}
.mavatar{width:58px;height:58px;border-radius:18px;background:linear-gradient(135deg,var(--acc),var(--acc3));color:#fff;display:flex;align-items:center;justify-content:center;font-family:'Syne',sans-serif;font-weight:800;font-size:1.05rem;margin:0 auto .75rem}
.mname{font-weight:600;font-size:.88rem;margin-bottom:.2rem}
.mrole{font-size:.76rem;color:var(--txt3)}

/* ── SUPPORT ── */
.sup-grid{display:grid;grid-template-columns:1fr 1fr;gap:1.25rem;margin-top:1.5rem}
.sup-card{background:var(--surface);border:1px solid var(--bdr);border-radius:var(--r);padding:1.75rem;box-shadow:var(--sh)}
.sup-icon{font-size:1.75rem;margin-bottom:.75rem}
.sup-card h3{font-family:'Syne',sans-serif;font-size:1.1rem;font-weight:700;margin-bottom:.75rem}
.c-item{display:flex;align-items:center;gap:.6rem;margin-bottom:.5rem;color:var(--txt2);font-size:.9rem}
.c-item a{color:var(--acc);text-decoration:none;font-weight:500}

/* ── CHATBOT ── */
.chat-fab{position:fixed;bottom:1.75rem;right:1.75rem;z-index:500;width:62px;height:62px;border-radius:50%;background:linear-gradient(135deg,var(--acc),var(--acc3));color:#fff;border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:1.5rem;box-shadow:0 8px 28px rgba(212,96,26,.4);transition:transform .2s,box-shadow .2s}
.chat-fab:hover{transform:scale(1.08);box-shadow:0 14px 40px rgba(212,96,26,.5)}
.chat-badge{position:absolute;top:-4px;right:-4px;background:#22c55e;border:2px solid var(--bg);width:16px;height:16px;border-radius:50%;animation:pulse 2s infinite}

.chat-win{position:fixed;bottom:5.5rem;right:1.75rem;z-index:500;width:400px;height:600px;background:var(--surface);border:1px solid var(--bdr);border-radius:24px;box-shadow:0 24px 64px rgba(26,18,8,.2);display:flex;flex-direction:column;transform:scale(.93) translateY(18px);opacity:0;pointer-events:none;transition:transform .28s cubic-bezier(.34,1.56,.64,1),opacity .2s;overflow:hidden}
.chat-win.open{transform:scale(1) translateY(0);opacity:1;pointer-events:all}

/* Chat Header */
.chat-head{background:var(--txt);color:#fff;padding:1rem 1.25rem;display:flex;align-items:center;gap:.75rem;flex-shrink:0}
.ch-ava{width:40px;height:40px;border-radius:12px;background:linear-gradient(135deg,var(--acc),var(--acc3));display:flex;align-items:center;justify-content:center;font-size:1.1rem;flex-shrink:0}
.ch-info{flex:1}
.ch-name{font-family:'Syne',sans-serif;font-weight:700;font-size:.95rem}
.ch-status{font-size:.7rem;color:rgba(255,255,255,.55);display:flex;align-items:center;gap:.3rem}
.ch-status::before{content:'●';color:#22c55e;font-size:.55rem;animation:pulse 2s infinite}
.ch-close{background:rgba(255,255,255,.12);border:none;color:#fff;width:30px;height:30px;border-radius:8px;cursor:pointer;font-size:1rem;transition:background .2s;flex-shrink:0;display:flex;align-items:center;justify-content:center}
.ch-close:hover{background:rgba(255,255,255,.22)}

/* Chat Tabs */
.chat-tabs{display:flex;background:var(--s2);border-bottom:1px solid var(--bdr);flex-shrink:0;overflow-x:auto}
.chat-tabs::-webkit-scrollbar{display:none}
.ctab{flex:1;min-width:0;padding:.6rem .3rem;font-size:.7rem;font-weight:600;color:var(--txt3);border:none;background:transparent;cursor:pointer;transition:all .2s;white-space:nowrap;display:flex;align-items:center;justify-content:center;gap:.25rem;border-bottom:2px solid transparent}
.ctab:hover{color:var(--txt2);background:rgba(0,0,0,.03)}
.ctab.active{color:var(--acc);border-bottom-color:var(--acc);background:var(--surface)}

/* Chat Lang Bar */
.lang-bar{padding:.5rem 1rem;background:var(--s2);border-bottom:1px solid var(--bdr);display:flex;align-items:center;gap:.4rem;flex-shrink:0;flex-wrap:wrap}
.lang-bar span{font-size:.68rem;color:var(--txt3);font-weight:600}
.lbtn{background:transparent;border:1px solid var(--bdr2);border-radius:var(--r3);padding:.15rem .55rem;font-size:.68rem;font-weight:600;color:var(--txt2);cursor:pointer;transition:all .15s}
.lbtn.active,.lbtn:hover{background:var(--acc);color:#fff;border-color:var(--acc)}

/* Chat Panels */
.chat-panels{flex:1;overflow:hidden;position:relative;min-height:0}
.cpanel{position:absolute;inset:0;overflow-y:auto;display:none;flex-direction:column}
.cpanel.active{display:flex}
.cpanel::-webkit-scrollbar{width:4px}
.cpanel::-webkit-scrollbar-thumb{background:var(--bdr2);border-radius:2px}

/* Messages panel */
#panel-chat{padding:.75rem;gap:.65rem}

/* Generic scrollable panel content */
.panel-body{padding:1rem}

/* Msg bubbles */
.msg{max-width:86%;display:flex;flex-direction:column;gap:.2rem}
.msg.user{align-self:flex-end;align-items:flex-end}
.msg.bot{align-self:flex-start;align-items:flex-start}
.bubble{padding:.65rem .95rem;border-radius:16px;font-size:.85rem;line-height:1.6;white-space:pre-wrap;word-break:break-word}
.msg.user .bubble{background:var(--acc);color:#fff;border-radius:16px 16px 4px 16px}
.msg.bot .bubble{background:var(--s2);color:var(--txt);border:1px solid var(--bdr);border-radius:16px 16px 16px 4px}
.msg-time{font-size:.65rem;color:var(--txt3)}
.typing-row{align-self:flex-start}
.typing-bub{display:flex;gap:.3rem;align-items:center;padding:.65rem .95rem;background:var(--s2);border:1px solid var(--bdr);border-radius:16px 16px 16px 4px;width:fit-content}
.tdot{width:6px;height:6px;border-radius:50%;background:var(--txt3);animation:typing 1.2s infinite}
.tdot:nth-child(2){animation-delay:.2s}
.tdot:nth-child(3){animation-delay:.4s}

/* Quick chips at bottom of chat */
.qchips{padding:.5rem .75rem;border-top:1px solid var(--bdr);display:flex;gap:.35rem;flex-wrap:wrap;background:var(--surface);flex-shrink:0}
.qchip{background:var(--s2);border:1px solid var(--bdr2);border-radius:var(--r3);padding:.25rem .7rem;font-size:.72rem;font-weight:500;color:var(--txt2);cursor:pointer;transition:all .15s;white-space:nowrap}
.qchip:hover{background:var(--s3);border-color:var(--acc);color:var(--acc)}

/* Input bar */
.chat-inp-bar{padding:.75rem 1rem;border-top:1px solid var(--bdr);display:flex;gap:.5rem;align-items:flex-end;background:var(--surface);flex-shrink:0}
.chat-textarea{flex:1;background:var(--s2);border:1.5px solid var(--bdr);border-radius:var(--r2);padding:.6rem .85rem;font-family:'DM Sans',sans-serif;font-size:.86rem;color:var(--txt);outline:none;resize:none;min-height:40px;max-height:110px;transition:border-color .2s;line-height:1.5}
.chat-textarea:focus{border-color:var(--acc)}
.chat-textarea::placeholder{color:var(--txt3)}
.chat-send{background:var(--acc);color:#fff;border:none;width:40px;height:40px;border-radius:11px;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:.95rem;flex-shrink:0;transition:background .2s,transform .15s}
.chat-send:hover{background:#c0531a;transform:scale(1.05)}
.chat-send:disabled{background:var(--bdr2);cursor:not-allowed;transform:none}

/* ── IN-CHAT WIDGETS ── */
/* Predictor */
.pred-widget{background:var(--surface);border:1.5px solid var(--bdr2);border-radius:16px 16px 16px 4px;padding:1rem 1.1rem;max-width:95%;display:flex;flex-direction:column;gap:.6rem;align-self:flex-start}
.pw-title{font-family:'Syne',sans-serif;font-weight:700;font-size:.86rem;color:var(--txt);display:flex;align-items:center;gap:.35rem}
.pw-row{display:flex;flex-direction:column;gap:.2rem}
.pw-row label{font-size:.66rem;font-weight:700;color:var(--txt3);letter-spacing:.07em;text-transform:uppercase}
.pw-sel{background:var(--s2);border:1.5px solid var(--bdr);border-radius:var(--r2);padding:.48rem .7rem;font-family:'DM Sans',sans-serif;font-size:.82rem;color:var(--txt);outline:none;cursor:pointer;width:100%;appearance:none;transition:border-color .2s}
.pw-sel:focus{border-color:var(--acc)}
.pw-btn{background:var(--acc);color:#fff;border:none;border-radius:var(--r2);padding:.58rem 1rem;font-family:'DM Sans',sans-serif;font-size:.84rem;font-weight:600;cursor:pointer;transition:background .2s,transform .15s}
.pw-btn:hover{background:#c0531a;transform:scale(1.01)}
/* Predictor result */
.pred-res{background:linear-gradient(135deg,#fff8f4,#fff3ea);border:1.5px solid #f6d4b4;border-radius:16px 16px 16px 4px;padding:.9rem 1rem;max-width:95%;display:flex;flex-direction:column;gap:.4rem;align-self:flex-start;animation:fadeUp .35s ease}
.pr-label{font-size:.66rem;font-weight:700;color:var(--acc);letter-spacing:.08em;text-transform:uppercase}
.pred-res h4{font-family:'Syne',sans-serif;font-size:.9rem;font-weight:800;color:var(--txt);line-height:1.3}
.pred-res p{font-size:.8rem;color:var(--txt2);line-height:1.55}
.pr-chips{display:flex;gap:.35rem;flex-wrap:wrap;margin-top:.2rem}
.pr-chip{background:#fff;border:1px solid #f6d4b4;border-radius:var(--r3);padding:.18rem .6rem;font-size:.7rem;font-weight:600;color:var(--acc)}

/* Compare widget */
.cmp-widget{background:var(--surface);border:1.5px solid var(--bdr2);border-radius:16px 16px 16px 4px;padding:1rem 1.1rem;max-width:100%;width:100%;display:flex;flex-direction:column;gap:.6rem;align-self:flex-start}
.cmp-selects{display:grid;grid-template-columns:1fr 1fr;gap:.5rem}
.cmp-table{width:100%;border-collapse:collapse;font-size:.75rem;margin-top:.25rem}
.cmp-table th{background:var(--txt);color:#fff;padding:.5rem .6rem;text-align:left;font-weight:600}
.cmp-table td{padding:.45rem .6rem;border-bottom:1px solid var(--bdr);vertical-align:top}
.cmp-table tr:nth-child(even) td{background:var(--s2)}
.cmp-table .row-label{font-weight:600;color:var(--txt2);white-space:nowrap}

/* Panel cards for Products / INSIGNIA / Mentors / Support */
.pc-card{background:var(--surface);border:1px solid var(--bdr);border-radius:var(--r2);padding:1rem;box-shadow:var(--sh);margin-bottom:.75rem}
.pc-card:last-child{margin-bottom:0}
.pc-tag{display:inline-block;background:var(--s2);color:var(--acc);border:1px solid var(--bdr2);border-radius:var(--r3);padding:.15rem .55rem;font-size:.66rem;font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-bottom:.5rem}
.pc-card h4{font-family:'Syne',sans-serif;font-size:.88rem;font-weight:700;line-height:1.3;margin-bottom:.3rem}
.pc-card p{font-size:.78rem;color:var(--txt2);line-height:1.55;margin-bottom:.55rem}
.pc-row{display:flex;justify-content:space-between;font-size:.76rem;padding:.35rem .5rem;background:var(--s2);border-radius:8px;margin-bottom:.3rem}
.pc-row strong{color:var(--acc)}
.pc-mods{display:flex;flex-wrap:wrap;gap:.3rem;margin-top:.4rem}
.pc-mod{background:var(--s3);border-radius:var(--r3);padding:.15rem .55rem;font-size:.68rem;color:var(--txt2)}

/* Mentor panel card */
.mc-card{display:flex;align-items:center;gap:.85rem;padding:.85rem 1rem;background:var(--surface);border:1px solid var(--bdr);border-radius:var(--r2);box-shadow:var(--sh);margin-bottom:.6rem}
.mc-ava{width:46px;height:46px;border-radius:14px;background:linear-gradient(135deg,var(--acc),var(--acc3));color:#fff;display:flex;align-items:center;justify-content:center;font-family:'Syne',sans-serif;font-weight:800;font-size:.9rem;flex-shrink:0}
.mc-info h4{font-weight:600;font-size:.88rem;margin-bottom:.15rem}
.mc-info p{font-size:.76rem;color:var(--txt3)}

/* Support panel */
.sup-section{margin-bottom:1.25rem}
.sup-section h4{font-family:'Syne',sans-serif;font-weight:700;font-size:.9rem;margin-bottom:.6rem;color:var(--txt)}
.sup-btn{display:flex;align-items:center;gap:.6rem;padding:.75rem 1rem;background:var(--surface);border:1px solid var(--bdr);border-radius:var(--r2);text-decoration:none;color:var(--txt);margin-bottom:.5rem;transition:border-color .2s,background .2s;box-shadow:var(--sh)}
.sup-btn:hover{border-color:var(--acc);background:var(--s2)}
.sup-btn-icon{font-size:1.1rem}
.sup-btn-text strong{display:block;font-size:.84rem;font-weight:600}
.sup-btn-text span{font-size:.75rem;color:var(--txt3)}
.disc-box{background:linear-gradient(135deg,#fff8f4,#fff3ea);border:1.5px solid #f6d4b4;border-radius:var(--r2);padding:1rem;font-size:.78rem;color:var(--txt2);line-height:1.65}

/* Section search/filter in panel */
.panel-search{width:100%;background:var(--s2);border:1.5px solid var(--bdr);border-radius:var(--r2);padding:.5rem .8rem;font-family:'DM Sans',sans-serif;font-size:.83rem;color:var(--txt);outline:none;margin-bottom:.85rem;transition:border-color .2s}
.panel-search:focus{border-color:var(--acc)}
.panel-filter{display:flex;gap:.4rem;flex-wrap:wrap;margin-bottom:.85rem}
.pfchip{background:var(--s2);border:1px solid var(--bdr);border-radius:var(--r3);padding:.25rem .7rem;font-size:.72rem;font-weight:600;color:var(--txt2);cursor:pointer;transition:all .15s}
.pfchip.active,.pfchip:hover{background:var(--txt);color:#fff;border-color:var(--txt)}

/* FOOTER */
footer{background:var(--txt);color:rgba(255,255,255,.55);text-align:center;padding:2rem;font-size:.82rem;line-height:1.8;margin-top:2rem}
footer strong{color:rgba(255,255,255,.8)}

/* ANIMATIONS */
@keyframes fadeUp{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}
@keyframes typing{0%,80%,100%{transform:translateY(0);opacity:.4}40%{transform:translateY(-5px);opacity:1}}

/* RESPONSIVE */
@media(max-width:900px){
  .hero-wrap{grid-template-columns:1fr}
  .hero-card{display:none}
  .pgrid{grid-template-columns:1fr 1fr}
  .prem-grid{grid-template-columns:1fr}
  .mgrid{grid-template-columns:1fr 1fr}
  .sup-grid{grid-template-columns:1fr}
  .nav-links{display:none}
  .chat-win{width:calc(100vw - 2rem);right:1rem;height:580px}
}
@media(max-width:600px){.pgrid{grid-template-columns:1fr}}
</style>
</head>
<body>

<!-- NAV -->
<nav>
  <a class="nav-brand" href="#">
    <div class="nav-logo">IM</div>
    <div><div class="nav-title">INVESMATE</div><div class="nav-tagline">Stock Market Learning</div></div>
  </a>
  <div class="nav-links">
    <a href="#products">Products</a>
    <a href="#insignia">INSIGNIA</a>
    <a href="#mentors">Mentors</a>
    <a href="#support">Support</a>
    <a href="#support" class="nav-cta">Request Callback</a>
  </div>
</nav>

<!-- HERO -->
<div class="hero-wrap">
  <div>
    <div class="hero-badge">SEBI Registered RA: INH000017985</div>
    <h1>Finest Stock Market <em>Learning</em> Experience</h1>
    <p class="hero-sub">A professional platform for INVESMATE and INSIGNIA — with AI-guided course selection, multilingual support, and personalized mentorship plans for every learner.</p>
    <div class="hero-actions">
      <a href="#products" class="btn-pri">Explore Courses ↓</a>
      <a href="#" class="btn-out" onclick="openChat();return false;">Talk to AI Advisor</a>
    </div>
  </div>
  <div class="hero-card">
    <span class="hc-label">Premium Learning Path</span>
    <h3>Find the right course in minutes</h3>
    <p>Use our AI advisor and course predictor to choose between beginner, trading, investing, derivatives, and INSIGNIA mentorship plans.</p>
    <div class="info-row"><strong>Personalized Prediction</strong><small>Course recommendation by goal, budget &amp; experience</small></div>
    <div class="info-row"><strong>Multilingual Support</strong><small>English, Bengali, Hindi &amp; Auto-Detect</small></div>
    <div class="info-row"><strong>INSIGNIA Premium</strong><small>1:1 mentorship, live sessions &amp; lifetime recordings</small></div>
  </div>
</div>

<!-- STATS -->
<div class="stats">
  <div class="stat"><div class="stat-n">20+</div><div class="stat-l">Expert Courses</div></div>
  <div class="stat"><div class="stat-n">8</div><div class="stat-l">Certified Mentors</div></div>
  <div class="stat"><div class="stat-n">3</div><div class="stat-l">Language Support</div></div>
  <div class="stat"><div class="stat-n">SEBI</div><div class="stat-l">Registered RA</div></div>
</div>

<!-- PRODUCTS -->
<div class="sec" id="products">
  <div class="eyebrow">All Products</div>
  <div class="sec-title">Complete Product Ecosystem</div>
  <div class="filter-bar" id="filter-bar"></div>
  <div class="search-wrap">
    <span class="search-icon">⌕</span>
    <input class="search-inp" id="search-inp" type="text" placeholder="Search courses…" oninput="renderProducts()"/>
  </div>
  <div class="pgrid" id="pgrid"></div>
</div>
<hr class="divider"/>

<!-- INSIGNIA -->
<div class="sec" id="insignia">
  <div class="eyebrow">INSIGNIA Premium Journey</div>
  <div class="sec-title">Premium Mentorship Plans</div>
  <div class="sec-sub">Intensive mentorship combining live sessions, 1:1 guidance, and real market practice.</div>
  <div class="prem-grid" id="prem-grid"></div>
</div>
<hr class="divider"/>

<!-- MENTORS -->
<div class="sec" id="mentors">
  <div class="eyebrow">Top Mentors</div>
  <div class="sec-title">Experienced Market Mentors</div>
  <div class="mgrid" id="mgrid"></div>
</div>
<hr class="divider"/>

<!-- SUPPORT -->
<div class="sec" id="support">
  <div class="eyebrow">Support</div>
  <div class="sec-title">Talk to the team before you enroll</div>
  <div class="sup-grid">
    <div class="sup-card">
      <div class="sup-icon">📞</div>
      <h3>Counseling &amp; Support</h3>
      <div class="c-item">📱 <a href="tel:+919016791791">+91 9016791791</a></div>
      <div class="c-item">📱 <a href="tel:+917596037781">+91 7596037781</a></div>
      <div class="c-item">📱 <a href="tel:+917003110622">+91 7003110622</a></div>
      <div class="c-item">✉️ <a href="mailto:support@invesmate.com">support@invesmate.com</a></div>
      <div class="c-item">✉️ <a href="mailto:sales@invesmate.com">sales@invesmate.com</a></div>
    </div>
    <div class="sup-card">
      <div class="sup-icon">⚠️</div>
      <h3>Disclaimer</h3>
      <p style="color:var(--txt2);font-size:.88rem;line-height:1.7">Investment in securities markets is subject to market risks. Read all related documents carefully before investing. Registration granted by SEBI and certification from NISM in no way guarantee performance or assurance of returns.<br><br>INVESMATE INSIGHTS — SEBI Registered Research Analyst (INH000017985). This platform is for educational purposes only.</p>
    </div>
  </div>
</div>

<footer>
  <strong>INVESMATE</strong> — Stock Market Learning Platform<br/>
  SEBI Registered RA: INH000017985 &nbsp;|&nbsp; support@invesmate.com<br/>
  © 2026 INVESMATE. All rights reserved. Educational purposes only.
</footer>

<!-- CHAT FAB -->
<button class="chat-fab" id="chat-fab" onclick="toggleChat()" title="AI Advisor">
  💬<span class="chat-badge"></span>
</button>

<!-- CHAT WINDOW -->
<div class="chat-win" id="chat-win">

  <!-- Header -->
  <div class="chat-head">
    <div class="ch-ava">🤖</div>
    <div class="ch-info">
      <div class="ch-name">INVESMATE AI Advisor</div>
      <div class="ch-status">Online — Powered by Claude AI</div>
    </div>
    <button class="ch-close" onclick="toggleChat()">✕</button>
  </div>

  <!-- Tabs -->
  <div class="chat-tabs">
    <button class="ctab active" onclick="switchTab('chat',this)"      >💬 Chat</button>
    <button class="ctab"        onclick="switchTab('predictor',this)" >🎯 Predict</button>
    <button class="ctab"        onclick="switchTab('compare',this)"   >⚖️ Compare</button>
    <button class="ctab"        onclick="switchTab('products',this)"  >📚 Courses</button>
    <button class="ctab"        onclick="switchTab('insignia',this)"  >👑 INSIGNIA</button>
    <button class="ctab"        onclick="switchTab('mentors',this)"   >🧑‍🏫 Mentors</button>
    <button class="ctab"        onclick="switchTab('support',this)"   >🆘 Support</button>
  </div>

  <!-- Lang bar (only on chat panel) -->
  <div class="lang-bar" id="lang-bar">
    <span>Lang:</span>
    <button class="lbtn active" onclick="setLang('English',this)">EN</button>
    <button class="lbtn" onclick="setLang('Bengali',this)">বাংলা</button>
    <button class="lbtn" onclick="setLang('Hindi',this)">हिंदी</button>
    <button class="lbtn" onclick="setLang('Auto',this)">Auto</button>
  </div>

  <!-- Panels container -->
  <div class="chat-panels">

    <!-- ① CHAT -->
    <div class="cpanel active" id="panel-chat"></div>

    <!-- ② PREDICTOR -->
    <div class="cpanel" id="panel-predictor">
      <div class="panel-body">
        <div class="eyebrow">AI Course Predictor</div>
        <p style="font-size:.83rem;color:var(--txt2);margin-bottom:1rem;line-height:1.6">Answer 3 questions and get an instant AI-powered course recommendation.</p>
        <div style="display:flex;flex-direction:column;gap:.65rem;">
          <div class="pw-row">
            <label>Learning Goal</label>
            <select class="pw-sel" id="p-goal">
              <option value="beginner stock market">Beginner stock market learning</option>
              <option value="intraday swing trading">Intraday &amp; swing trading</option>
              <option value="options derivatives">Options &amp; derivatives trading</option>
              <option value="long term investing fundamentals">Long-term investing &amp; fundamentals</option>
              <option value="mutual fund sip">Mutual fund &amp; SIP</option>
              <option value="commodity global market">Commodity &amp; global market</option>
            </select>
          </div>
          <div class="pw-row">
            <label>Experience Level</label>
            <select class="pw-sel" id="p-exp">
              <option>Beginner</option><option>Intermediate</option><option>Advanced</option>
            </select>
          </div>
          <div class="pw-row">
            <label>Budget Preference</label>
            <select class="pw-sel" id="p-budget">
              <option value="budget">Budget-friendly</option>
              <option value="premium">Premium / Best value</option>
            </select>
          </div>
          <button class="pw-btn" onclick="runPredictor()">Get Recommendation →</button>
        </div>
        <div id="pred-output" style="margin-top:1rem"></div>
      </div>
    </div>

    <!-- ③ COMPARE -->
    <div class="cpanel" id="panel-compare">
      <div class="panel-body">
        <div class="eyebrow">Course Compare</div>
        <p style="font-size:.83rem;color:var(--txt2);margin-bottom:.85rem;line-height:1.6">Select two courses to compare side-by-side.</p>
        <div class="cmp-selects" style="margin-bottom:.85rem">
          <div class="pw-row">
            <label>Course A</label>
            <select class="pw-sel" id="cmp-a" onchange="renderCompare()"></select>
          </div>
          <div class="pw-row">
            <label>Course B</label>
            <select class="pw-sel" id="cmp-b" onchange="renderCompare()"></select>
          </div>
        </div>
        <div id="cmp-output"></div>
        <div style="margin-top:.85rem">
          <button class="pw-btn" style="width:100%" onclick="askAICompare()">🤖 Ask AI to compare these →</button>
        </div>
      </div>
    </div>

    <!-- ④ PRODUCTS -->
    <div class="cpanel" id="panel-products">
      <div class="panel-body">
        <div class="eyebrow">All Courses</div>
        <input class="panel-search" id="prod-search" placeholder="Search courses…" oninput="renderProdPanel()"/>
        <div class="panel-filter" id="prod-filter"></div>
        <div id="prod-list"></div>
      </div>
    </div>

    <!-- ⑤ INSIGNIA -->
    <div class="cpanel" id="panel-insignia">
      <div class="panel-body">
        <div class="eyebrow">INSIGNIA Premium Plans</div>
        <p style="font-size:.83rem;color:var(--txt2);margin-bottom:1rem;line-height:1.6">Intensive mentorship programs with live sessions, 1:1 guidance, and real market practice.</p>
        <div id="insig-list"></div>
      </div>
    </div>

    <!-- ⑥ MENTORS -->
    <div class="cpanel" id="panel-mentors">
      <div class="panel-body">
        <div class="eyebrow">Our Mentors</div>
        <p style="font-size:.83rem;color:var(--txt2);margin-bottom:1rem;line-height:1.6">All mentors are NISM-certified capital market professionals.</p>
        <div id="mentor-list"></div>
      </div>
    </div>

    <!-- ⑦ SUPPORT -->
    <div class="cpanel" id="panel-support">
      <div class="panel-body">
        <div class="eyebrow">Support &amp; Contact</div>
        <div class="sup-section">
          <h4>📞 Call / WhatsApp</h4>
          <a class="sup-btn" href="tel:+919016791791"><span class="sup-btn-icon">📱</span><div class="sup-btn-text"><strong>+91 9016791791</strong><span>Primary support line</span></div></a>
          <a class="sup-btn" href="tel:+917596037781"><span class="sup-btn-icon">📱</span><div class="sup-btn-text"><strong>+91 7596037781</strong><span>Sales &amp; enrollment</span></div></a>
          <a class="sup-btn" href="tel:+917003110622"><span class="sup-btn-icon">📱</span><div class="sup-btn-text"><strong>+91 7003110622</strong><span>Academic support</span></div></a>
        </div>
        <div class="sup-section">
          <h4>✉️ Email</h4>
          <a class="sup-btn" href="mailto:support@invesmate.com"><span class="sup-btn-icon">📧</span><div class="sup-btn-text"><strong>support@invesmate.com</strong><span>General support</span></div></a>
          <a class="sup-btn" href="mailto:sales@invesmate.com"><span class="sup-btn-icon">📧</span><div class="sup-btn-text"><strong>sales@invesmate.com</strong><span>Enrollment &amp; fees</span></div></a>
        </div>
        <div class="sup-section">
          <h4>⚠️ Disclaimer</h4>
          <div class="disc-box">Investment in securities markets is subject to market risks. Read all related documents carefully before investing. SEBI registration and NISM certification do not guarantee performance or assurance of returns.<br><br><strong>INVESMATE INSIGHTS</strong> — SEBI Registered RA: <strong>INH000017985</strong>. For educational purposes only.</div>
        </div>
        <div style="margin-top:.85rem">
          <button class="pw-btn" style="width:100%" onclick="switchTab('chat',document.querySelectorAll('.ctab')[0]);addBotMsg('How can I help you with support today?')">💬 Chat with AI Advisor</button>
        </div>
      </div>
    </div>

  </div><!-- /chat-panels -->

  <!-- Quick chips (only shown on chat tab) -->
  <div class="qchips" id="qchips">
    <button class="qchip" onclick="switchTab('predictor',document.querySelectorAll('.ctab')[1])">🎯 Predict my course</button>
    <button class="qchip" onclick="sendQuick('What are the INSIGNIA mentorship plans?')">👑 INSIGNIA</button>
    <button class="qchip" onclick="sendQuick('What are the fees and pricing?')">💰 Pricing</button>
    <button class="qchip" onclick="sendQuick('How do I enroll?')">📝 Enroll</button>
  </div>

  <!-- Input bar -->
  <div class="chat-inp-bar" id="chat-inp-bar">
    <textarea class="chat-textarea" id="chat-input" placeholder="Ask about courses, pricing, enrollment…" rows="1"
      onkeydown="handleKey(event)" oninput="autoResize(this)"></textarea>
    <button class="chat-send" id="send-btn" onclick="sendMsg()">➤</button>
  </div>

</div><!-- /chat-win -->

<script>
// ════════════════════════════════════════
//  DATA
// ════════════════════════════════════════
const PRODUCTS = [
  {id:0,title:"Power of Trading and Investing Combo Course",cat:"Live Course",tag:"Beginner",price:"Rs. 8,999 – 11,999",duration:"2 Months / 26 Hrs",lessons:"57 Lessons",desc:"Complete capital-market course covering trading and investing from basics to advanced level.",modules:["Market basics","Technical analysis","Investing foundation","Real market practice"]},
  {id:1,title:"Complete Intraday and Swing Trading Strategies",cat:"Live Course",tag:"Technical Trading",price:"Rs. 9,999 – 12,999",duration:"2 Months / 20 Hrs",lessons:"48 Lessons",desc:"Advanced technical-analysis course for intraday and swing traders.",modules:["Chart patterns","Indicators","Smart Money Concepts","Risk control"]},
  {id:2,title:"Complete Future and Option Trading Strategies",cat:"Live Course",tag:"Derivatives",price:"Rs. 12,999 – 15,999",duration:"2 Months / 26 Hrs",lessons:"25 Lessons",desc:"Futures and options training covering derivatives strategy from basics to advanced.",modules:["Futures basics","Option buying","Option selling","Hedging"]},
  {id:3,title:"Value Investing Using Advanced Fundamental Analysis",cat:"Live Course",tag:"Investing",price:"Rs. 8,999 – 11,999",duration:"2 Months / 24 Hrs",lessons:"57 Lessons",desc:"Fundamental-analysis and value-investing roadmap for long-term equity investors.",modules:["Business analysis","Financial statements","Valuation","Portfolio mindset"]},
  {id:4,title:"Introduction To Mutual Funds Investment",cat:"Course",tag:"Mutual Funds",price:"Rs. 3,999 – 6,999",duration:"1 Month",lessons:"24 Lessons",desc:"Practical overview of mutual funds, SIPs, and fund selection for long-term wealth.",modules:["MF basics","SIP planning","Fund selection","Long-term wealth"]},
  {id:5,title:"Dynamic Investment With Fixed Income Securities",cat:"Recorded Course",tag:"Fixed Income",price:"Rs. 10,999",duration:"12 Hours",lessons:"33 Lessons",desc:"Recorded course on bonds, government securities, income products, and diversification.",modules:["Bonds","Government securities","Income planning","Diversification"]},
  {id:6,title:"The Comprehensive Roadmap Of Commodity Market",cat:"Live Course",tag:"Commodity",price:"Rs. 14,999",duration:"16 Hours",lessons:"10 Lessons",desc:"Commodity-market course covering gold, silver, crude oil, natural gas, and risk management.",modules:["Gold and silver","Crude oil","Natural gas","Technical view"]},
  {id:7,title:"Power TI Masterclass",cat:"Free Program",tag:"Masterclass",price:"Free / Registration",duration:"Short Session",lessons:"Live Session",desc:"Entry-level masterclass for learners starting their stock-market journey.",modules:["Orientation","Counseling","Beginner roadmap","Q&A"]},
  {id:8,title:"Share Samadhan",cat:"Newsletter",tag:"Market Study",price:"Included in plans",duration:"Weekly",lessons:"Premium Study",desc:"Weekly Bengali stock-market study for cash, derivatives, IPOs, mutual funds, and trends.",modules:["Cash market","Derivatives","IPO study","Mutual funds"]},
  {id:9,title:"Market Trending All Segment",cat:"Premium Tool",tag:"Market Intel",price:"INSIGNIA plans",duration:"Plan-based",lessons:"All Segments",desc:"Premium market-trending access included in selected INSIGNIA programs.",modules:["Cash","Derivatives","Commodity","Fixed assets"]},
  {id:10,title:"INVESMATE Learning App",cat:"Mobile App",tag:"Platform",price:"App-based",duration:"Anytime",lessons:"Course Library",desc:"Mobile app for live classes, recordings, academic support, and My Insignia Help.",modules:["Live classes","Recordings","Support","Course access"]},
  {id:11,title:"Insights.Market",cat:"Research Brand",tag:"SEBI RA",price:"Separate platform",duration:"Research Access",lessons:"Research Products",desc:"SEBI-registered equity research brand under INVESMATE INSIGHTS.",modules:["Equity research","Investor charter","Disclosures","Compliance"]},
];

const INSIGNIA = [
  {id:0,title:"Equity Market Intelligence Matrix",tag:"Premium Mentorship",price:"Rs. 38,571 / 44,420",duration:"3–5 Months",desc:"Premium mentorship combining advanced technical, techno-funda, and fundamental analysis with 1:1 support.",modules:["Market Trending","Share Samadhan","1:1 mentorship","4 practical sessions","NISM guidance"]},
  {id:1,title:"Complete Equity and Derivative Dynasty",tag:"Options Premium",price:"Rs. 62,305 / 44,420",duration:"6–8 Months",desc:"Advanced pathway combining technical, fundamental, derivatives, and fixed-income learning with 8 practical sessions.",modules:["Advanced Technical","Complete Options","Fixed Income","8 practical sessions","Academic helpline"]},
  {id:2,title:"Complete Global Capital Market Specialist",tag:"Global Premium",price:"Rs. 1,07,689 / 44,420",duration:"12 Months",desc:"Full-stack global specialist path: US stocks, commodities, mutual funds, and software training with lifetime recordings.",modules:["US stocks","Commodity","Advanced MF","3 mentorship sessions","Lifetime recordings"]},
];

const MENTORS = [
  {name:"Arunava Chatterjee",spec:"Technical Analysis & Trading"},
  {name:"Sayan Ghosh",spec:"Options & Derivatives"},
  {name:"Kunal Saha",spec:"Fundamental Analysis"},
  {name:"Suman Goswami",spec:"Commodity Markets"},
  {name:"Laboni Pallab Das",spec:"Mutual Funds & SIP"},
  {name:"Debarati Mukherjee",spec:"Fixed Income"},
  {name:"Pratim Kumar Chakraborty",spec:"Global Markets"},
  {name:"Mihir Kanti Chakraborty",spec:"Value Investing"},
];

// ════════════════════════════════════════
//  PAGE RENDER
// ════════════════════════════════════════
let activeCat = 'All';
function initPage(){
  // Filter bar
  const cats = ['All',...new Set(PRODUCTS.map(p=>p.cat))];
  document.getElementById('filter-bar').innerHTML = cats.map(c=>
    `<button class="fchip${c==='All'?' active':''}" onclick="setCat('${c.replace(/'/g,"\\'")}',this)">${c}</button>`
  ).join('');
  renderProducts();

  // INSIGNIA grid
  document.getElementById('prem-grid').innerHTML = INSIGNIA.map(p=>`
    <div class="prem-card">
      <div class="prem-tier">${p.tag}</div>
      <h3>${p.title}</h3>
      <p>${p.desc}</p>
      <div class="prem-price">${p.price}</div>
      <div class="prem-dur">⏱ ${p.duration}</div>
      <ul class="prem-feats">${p.modules.map(m=>`<li>${m}</li>`).join('')}</ul>
    </div>`).join('');

  // Mentors grid
  document.getElementById('mgrid').innerHTML = MENTORS.map(m=>{
    const ini = m.name.split(' ').map(w=>w[0]).slice(0,2).join('');
    return `<div class="mcard"><div class="mavatar">${ini}</div><div class="mname">${m.name}</div><div class="mrole">${m.spec}</div></div>`;
  }).join('');

  initChatPanels();
  initCompareSelects();
}

function setCat(c,el){
  activeCat=c;
  document.querySelectorAll('.fchip').forEach(b=>b.classList.remove('active'));
  el.classList.add('active');
  renderProducts();
}

function renderProducts(){
  const q=(document.getElementById('search-inp').value||'').toLowerCase();
  const list=PRODUCTS.filter(p=>(activeCat==='All'||p.cat===activeCat)&&(!q||p.title.toLowerCase().includes(q)||p.desc.toLowerCase().includes(q)));
  document.getElementById('pgrid').innerHTML=list.length
    ?list.map(p=>`
      <div class="pcard">
        <span class="ptag">${p.cat}</span>
        <h3>${p.title}</h3>
        <p>${p.desc}</p>
        <div class="pmeta">
          <div class="mpill"><span>💰 ${p.price}</span></div>
          <div class="mpill"><span>⏱ ${p.duration}</span><span>${p.lessons}</span></div>
        </div>
        <div class="mods">${p.modules.map(m=>`<span class="mchip">${m}</span>`).join('')}</div>
      </div>`).join('')
    :`<div class="no-res">No courses found. Try different keywords.</div>`;
}

// ════════════════════════════════════════
//  CHAT PANEL INIT
// ════════════════════════════════════════
function initChatPanels(){
  // Products panel
  const cats=['All',...new Set(PRODUCTS.map(p=>p.cat))];
  document.getElementById('prod-filter').innerHTML=cats.map(c=>
    `<button class="pfchip${c==='All'?' active':''}" onclick="setProdCat('${c.replace(/'/g,"\\'")}',this)">${c}</button>`
  ).join('');
  renderProdPanel();

  // INSIGNIA panel
  document.getElementById('insig-list').innerHTML=INSIGNIA.map(p=>`
    <div class="pc-card">
      <span class="pc-tag">${p.tag}</span>
      <h4>${p.title}</h4>
      <p>${p.desc}</p>
      <div class="pc-row"><span>💰 Price</span><strong>${p.price}</strong></div>
      <div class="pc-row"><span>⏱ Duration</span><strong>${p.duration}</strong></div>
      <div class="pc-mods">${p.modules.map(m=>`<span class="pc-mod">${m}</span>`).join('')}</div>
    </div>`).join('');

  // Mentors panel
  document.getElementById('mentor-list').innerHTML=MENTORS.map(m=>{
    const ini=m.name.split(' ').map(w=>w[0]).slice(0,2).join('');
    return `<div class="mc-card"><div class="mc-ava">${ini}</div><div class="mc-info"><h4>${m.name}</h4><p>${m.spec} · NISM Certified</p></div></div>`;
  }).join('');
}

let prodPanelCat='All';
function setProdCat(c,el){
  prodPanelCat=c;
  document.querySelectorAll('#prod-filter .pfchip').forEach(b=>b.classList.remove('active'));
  el.classList.add('active');
  renderProdPanel();
}
function renderProdPanel(){
  const q=(document.getElementById('prod-search').value||'').toLowerCase();
  const list=PRODUCTS.filter(p=>(prodPanelCat==='All'||p.cat===prodPanelCat)&&(!q||p.title.toLowerCase().includes(q)||p.desc.toLowerCase().includes(q)));
  document.getElementById('prod-list').innerHTML=list.length
    ?list.map(p=>`
      <div class="pc-card">
        <span class="pc-tag">${p.cat}</span>
        <h4>${p.title}</h4>
        <p>${p.desc}</p>
        <div class="pc-row"><span>💰</span><strong>${p.price}</strong></div>
        <div class="pc-row"><span>⏱ ${p.duration}</span><span>${p.lessons}</span></div>
        <div class="pc-mods">${p.modules.map(m=>`<span class="pc-mod">${m}</span>`).join('')}</div>
      </div>`).join('')
    :`<div style="text-align:center;color:var(--txt3);padding:2rem;font-size:.85rem">No results found.</div>`;
}

// ════════════════════════════════════════
//  PREDICTOR
// ════════════════════════════════════════
function runPredictor(){
  const goal=document.getElementById('p-goal').value;
  const exp=document.getElementById('p-exp').value;
  const budget=document.getElementById('p-budget').value;
  const g=goal.toLowerCase(), b=budget.toLowerCase();
  let rec;
  if(g.includes('option')||g.includes('derivative')) rec=b==='premium'?{type:'insignia',item:INSIGNIA[1]}:{type:'product',item:PRODUCTS[2]};
  else if(g.includes('commodity')||g.includes('global')) rec=b==='premium'?{type:'insignia',item:INSIGNIA[2]}:{type:'product',item:PRODUCTS[6]};
  else if(g.includes('mutual')||g.includes('sip')) rec={type:'product',item:PRODUCTS[4]};
  else if(g.includes('intraday')||g.includes('swing')||g.includes('trading')) rec=b==='premium'?{type:'insignia',item:INSIGNIA[0]}:{type:'product',item:PRODUCTS[1]};
  else if(g.includes('long')||g.includes('fundamental')||g.includes('investing')) rec=b==='premium'?{type:'insignia',item:INSIGNIA[0]}:{type:'product',item:PRODUCTS[3]};
  else rec=b==='premium'?{type:'insignia',item:INSIGNIA[0]}:{type:'product',item:PRODUCTS[0]};

  const {item}=rec;
  document.getElementById('pred-output').innerHTML=`
    <div class="pred-res">
      <div class="pr-label">✅ Recommended for ${exp} · ${budget}</div>
      <h4>${item.title}</h4>
      <p>${item.desc}</p>
      <div class="pr-chips">
        <span class="pr-chip">💰 ${item.price}</span>
        <span class="pr-chip">⏱ ${item.duration}</span>
        ${item.lessons?`<span class="pr-chip">${item.lessons}</span>`:''}
      </div>
      <button class="pw-btn" style="margin-top:.65rem;width:100%" onclick="sendQuick('Tell me more about ${item.title.replace(/'/g,"\\'")} — pricing, EMI options, and how to enroll.');switchTab('chat',document.querySelectorAll('.ctab')[0])">💬 Ask AI about this course →</button>
    </div>`;
}

// ════════════════════════════════════════
//  COMPARE
// ════════════════════════════════════════
const ALL_COURSES=[...PRODUCTS,...INSIGNIA.map(i=>({...i,cat:'INSIGNIA Plan'}))];

function initCompareSelects(){
  const opts=ALL_COURSES.map((c,i)=>`<option value="${i}">${c.title}</option>`).join('');
  document.getElementById('cmp-a').innerHTML=opts;
  document.getElementById('cmp-b').innerHTML=opts;
  document.getElementById('cmp-b').selectedIndex=1;
  renderCompare();
}

function renderCompare(){
  const a=ALL_COURSES[+document.getElementById('cmp-a').value];
  const b=ALL_COURSES[+document.getElementById('cmp-b').value];
  const rows=[
    ['Category',a.cat||'INSIGNIA',b.cat||'INSIGNIA'],
    ['Price',a.price,b.price],
    ['Duration',a.duration,b.duration],
    ['Lessons / Format',a.lessons||'Mentorship',b.lessons||'Mentorship'],
    ['Key modules',a.modules.slice(0,3).join(', '),b.modules.slice(0,3).join(', ')],
  ];
  document.getElementById('cmp-output').innerHTML=`
    <table class="cmp-table">
      <tr><th>Feature</th><th style="color:var(--acc2)">${a.title.length>28?a.title.slice(0,28)+'…':a.title}</th><th style="color:var(--acc2)">${b.title.length>28?b.title.slice(0,28)+'…':b.title}</th></tr>
      ${rows.map(r=>`<tr><td class="row-label">${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td></tr>`).join('')}
    </table>`;
}

function askAICompare(){
  const a=ALL_COURSES[+document.getElementById('cmp-a').value];
  const b=ALL_COURSES[+document.getElementById('cmp-b').value];
  sendQuick(`Compare "${a.title}" vs "${b.title}" — which is better for me and why?`);
  switchTab('chat',document.querySelectorAll('.ctab')[0]);
}

// ════════════════════════════════════════
//  CHAT ENGINE
// ════════════════════════════════════════
let chatOpen=false, chatLang='English', chatHistory=[], isTyping=false;

const SYS=`You are the INVESMATE AI Advisor — knowledgeable, warm, professional. You help users of INVESMATE, a SEBI-registered Research Analyst platform (INH000017985) in India.

Capabilities:
- Recommend courses based on goals, experience, budget
- Compare courses in detail
- Explain INSIGNIA mentorship plans
- Provide pricing, EMI, enrollment steps
- Introduce mentors and their specializations
- Handle support queries
- Answer in Bengali or Hindi when requested

INVESMATE Courses:
1. Power of Trading and Investing Combo — Live, Beginner, Rs.8,999–11,999, 2mo/26hrs, 57 lessons
2. Complete Intraday and Swing Trading — Live, Rs.9,999–12,999, 2mo/20hrs, 48 lessons
3. Complete Future and Option Trading — Live, Rs.12,999–15,999, 2mo/26hrs
4. Value Investing Advanced Fundamental Analysis — Live, Rs.8,999–11,999, 2mo/24hrs
5. Introduction To Mutual Funds — Rs.3,999–6,999, 1 month
6. Dynamic Investment Fixed Income Securities — Recorded, Rs.10,999, 12hrs
7. Comprehensive Roadmap Commodity Market — Live, Rs.14,999, 16hrs
8. Power TI Masterclass — Free entry program
9. Share Samadhan — Bengali weekly newsletter, included in plans
10. Market Trending All Segment — Premium tool, INSIGNIA plans
11. INVESMATE Learning App — Mobile platform
12. Insights.Market — SEBI RA research brand

INSIGNIA Premium Mentorship:
A. Equity Market Intelligence Matrix — Rs.38,571/44,420, 3–5 months, technical+fundamental, 1:1 mentorship, 4 practical sessions
B. Complete Equity and Derivative Dynasty — Rs.62,305/44,420, 6–8 months, equity+options+fixed income, 8 sessions
C. Complete Global Capital Market Specialist — Rs.1,07,689/44,420, 12 months, US stocks+commodity+advanced MF, lifetime recordings

Mentors (all NISM-certified): Arunava Chatterjee (Technical), Sayan Ghosh (Options), Kunal Saha (Fundamentals), Suman Goswami (Commodity), Laboni Pallab Das (MF), Debarati Mukherjee (Fixed Income), Pratim Kumar Chakraborty (Global), Mihir Kanti Chakraborty (Value Investing)

Support: +91 9016791791, +91 7596037781, +91 7003110622 | support@invesmate.com | sales@invesmate.com

Enrollment: Select course → request counseling call → confirm batch/timing/EMI → pay → app access

Respond in: {{LANG}}. If user writes Bengali → reply Bengali; Hindi → reply Hindi; otherwise English.
Add "Note: Investment in securities markets is subject to market risks." for trading/returns topics.
Be concise, helpful, and use bullet points for structured info.`;

function toggleChat(){
  chatOpen=!chatOpen;
  document.getElementById('chat-win').classList.toggle('open',chatOpen);
  document.getElementById('chat-fab').innerHTML=chatOpen?'✕<span class="chat-badge"></span>':'💬<span class="chat-badge"></span>';
  if(chatOpen&&chatHistory.length===0){
    addBot("Hi! 👋 I'm your INVESMATE AI Advisor.\n\nI can help you with:\n• 🎯 Course recommendations\n• ⚖️ Compare any two courses\n• 👑 INSIGNIA mentorship plans\n• 💰 Pricing &amp; EMI options\n• 📝 Enrollment steps\n• 🆘 Support &amp; contact\n\nUse the tabs above or just ask me anything!");
  }
}
function openChat(){if(!chatOpen)toggleChat();}

function switchTab(name,el){
  document.querySelectorAll('.ctab').forEach(t=>t.classList.remove('active'));
  document.querySelectorAll('.cpanel').forEach(p=>p.classList.remove('active'));
  el.classList.add('active');
  document.getElementById('panel-'+name).classList.add('active');
  // Show/hide lang bar and input bar only on chat tab
  const isChat=name==='chat';
  document.getElementById('lang-bar').style.display=isChat?'':'none';
  document.getElementById('qchips').style.display=isChat?'':'none';
  document.getElementById('chat-inp-bar').style.display=isChat?'':'none';
}

function setLang(l,el){
  chatLang=l;
  document.querySelectorAll('.lbtn').forEach(b=>b.classList.remove('active'));
  el.classList.add('active');
}

function addBot(html){
  const panel=document.getElementById('panel-chat');
  const now=new Date().toLocaleTimeString([],{hour:'2-digit',minute:'2-digit'});
  const d=document.createElement('div');
  d.className='msg bot';
  d.innerHTML=`<div class="bubble">${html}</div><span class="msg-time">${now}</span>`;
  panel.appendChild(d);
  panel.scrollTop=panel.scrollHeight;
  chatHistory.push({role:'assistant',content:html.replace(/<[^>]+>/g,'')});
}

function addUser(text){
  const panel=document.getElementById('panel-chat');
  const now=new Date().toLocaleTimeString([],{hour:'2-digit',minute:'2-digit'});
  const d=document.createElement('div');
  d.className='msg user';
  d.innerHTML=`<div class="bubble">${esc(text)}</div><span class="msg-time">${now}</span>`;
  panel.appendChild(d);
  panel.scrollTop=panel.scrollHeight;
  chatHistory.push({role:'user',content:text});
}

function showTyping(){
  const panel=document.getElementById('panel-chat');
  const d=document.createElement('div');
  d.className='msg bot typing-row';d.id='typing-ind';
  d.innerHTML=`<div class="typing-bub"><span class="tdot"></span><span class="tdot"></span><span class="tdot"></span></div>`;
  panel.appendChild(d);panel.scrollTop=panel.scrollHeight;
}
function removeTyping(){const t=document.getElementById('typing-ind');if(t)t.remove();}

async function sendMsg(){
  const inp=document.getElementById('chat-input');
  const text=inp.value.trim();
  if(!text||isTyping)return;
  inp.value='';autoResize(inp);
  addUser(text);
  document.getElementById('send-btn').disabled=true;
  isTyping=true;
  showTyping();

  try{
    const msgs=chatHistory.slice(-22);
    const res=await fetch('https://api.anthropic.com/v1/messages',{
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify({
        model:'claude-sonnet-4-20250514',
        max_tokens:1000,
        system:SYS.replace('{{LANG}}',chatLang),
        messages:msgs,
      })
    });
    removeTyping();
    const data=await res.json();
    if(data.content&&data.content[0]&&data.content[0].text){
      addBot(esc(data.content[0].text));
    }else if(data.error){
      addBot('⚠️ API error: '+esc(data.error.message||'Unknown')+'\n\nContact: support@invesmate.com');
    }else{
      addBot('Sorry, something went wrong. Please try again.');
    }
  }catch(e){
    removeTyping();
    addBot('⚠️ Connection error.\n\nFor immediate help:\n📞 +91 9016791791\n✉️ support@invesmate.com');
  }
  isTyping=false;
  document.getElementById('send-btn').disabled=false;
  document.getElementById('chat-input').focus();
}

function sendQuick(text){
  // Switch to chat tab first
  const chatTab=document.querySelectorAll('.ctab')[0];
  switchTab('chat',chatTab);
  document.getElementById('chat-input').value=text;
  sendMsg();
}

function handleKey(e){if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();sendMsg();}}
function autoResize(el){el.style.height='auto';el.style.height=Math.min(el.scrollHeight,110)+'px';}
function esc(t){return String(t||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/\n/g,'<br>');}

// ════════════════════════════════════════
//  INIT
// ════════════════════════════════════════
initPage();
</script>
</body>
</html>
