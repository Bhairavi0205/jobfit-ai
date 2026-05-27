html = open('templates/index.html', 'w', encoding='utf-8')
html.write("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>JobFit AI</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#0a0a0f;--s1:#12111a;--s2:#1a1828;--border:#252338;--p:#7c3aed;--pl:#a78bfa;--pk:#f472b6;--t:#e8e6f0;--tm:#8b8399;--ok:#10b981;--err:#ef4444}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--t);min-height:100vh}
::-webkit-scrollbar{width:5px}::-webkit-scrollbar-thumb{background:var(--p);border-radius:3px}
nav{background:rgba(18,17,26,0.95);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);padding:16px 40px;position:sticky;top:0;z-index:100;display:flex;align-items:center;justify-content:space-between}
.nav-logo{font-size:1.2rem;font-weight:800;background:linear-gradient(135deg,var(--pl),var(--pk));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.nav-sub{font-size:0.75rem;color:var(--tm)}
.main{max-width:1050px;margin:0 auto;padding:40px 20px}
.hero{text-align:center;margin-bottom:44px}
.hero h1{font-size:2.4rem;font-weight:800;letter-spacing:-1px;margin-bottom:12px;background:linear-gradient(135deg,#fff 30%,var(--pl));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero p{color:var(--tm);font-size:1rem;max-width:600px;margin:0 auto}
.tabs{display:flex;gap:4px;background:var(--s1);border:1px solid var(--border);border-radius:12px;padding:4px;width:fit-content;margin:0 auto 36px;flex-wrap:wrap;justify-content:center}
.tab{padding:10px 22px;border-radius:8px;border:none;cursor:pointer;font-weight:500;font-size:0.88rem;color:var(--tm);background:transparent;font-family:'Inter',sans-serif;transition:all 0.2s}
.tab.active{background:linear-gradient(135deg,var(--p),#9d174d);color:#fff;box-shadow:0 4px 15px rgba(124,58,237,0.35)}
.tc{display:none}.tc.active{display:block}
.card{background:var(--s1);border-radius:16px;padding:28px;margin-bottom:20px;border:1px solid var(--border);transition:border-color 0.2s}
.card:hover{border-color:rgba(124,58,237,0.4)}
.ct{font-size:0.68rem;font-weight:700;color:var(--pl);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:20px;display:flex;align-items:center;gap:10px}
.ct::after{content:'';flex:1;height:1px;background:var(--border)}
.fg{margin-bottom:18px}
.fl{display:block;font-weight:500;color:var(--tm);margin-bottom:7px;font-size:0.84rem}
.ub{border:1.5px dashed var(--border);border-radius:12px;padding:28px;text-align:center;background:var(--s2);transition:all 0.2s}
.ub:hover{border-color:var(--pl)}
.ub .fi{font-size:1.8rem;margin-bottom:8px}
.ub p{color:var(--tm);font-size:0.86rem;margin-bottom:10px}
.ub p b{color:var(--pl)}
input[type=file]{display:block;width:100%;padding:9px 12px;background:rgba(124,58,237,0.1);border:1px solid rgba(124,58,237,0.3);border-radius:8px;color:var(--t);font-size:0.84rem;cursor:pointer;font-family:'Inter',sans-serif}
input[type=file]::-webkit-file-upload-button{background:linear-gradient(135deg,var(--p),#9d174d);color:#fff;border:none;padding:7px 14px;border-radius:6px;cursor:pointer;font-family:'Inter',sans-serif;font-size:0.8rem;font-weight:600;margin-right:10px}
textarea{width:100%;padding:13px 15px;border:1.5px solid var(--border);border-radius:10px;font-size:0.9rem;resize:vertical;min-height:120px;font-family:'Inter',sans-serif;background:var(--s2);color:var(--t);outline:none;transition:border 0.2s;line-height:1.6}
textarea:focus{border-color:var(--p);box-shadow:0 0 0 3px rgba(124,58,237,0.1)}
textarea::placeholder{color:var(--tm)}
.inp{width:100%;padding:13px 15px;border:1.5px solid var(--border);border-radius:10px;font-size:0.9rem;font-family:'Inter',sans-serif;background:var(--s2);color:var(--t);outline:none;transition:border 0.2s}
.inp:focus{border-color:var(--p);box-shadow:0 0 0 3px rgba(124,58,237,0.1)}
.inp::placeholder{color:var(--tm)}
.fn{color:var(--ok);font-size:0.83rem;font-weight:500;margin-top:8px}
.bp{width:100%;padding:13px;background:linear-gradient(135deg,var(--p),#9d174d);color:#fff;border:none;border-radius:10px;font-size:0.95rem;font-weight:600;cursor:pointer;font-family:'Inter',sans-serif;transition:all 0.2s;margin-top:4px}
.bp:hover{opacity:0.9;transform:translateY(-1px);box-shadow:0 6px 20px rgba(124,58,237,0.35)}
.bp:disabled{opacity:0.5;cursor:not-allowed;transform:none}
.bsm{padding:6px 14px;background:rgba(124,58,237,0.12);color:var(--pl);border:1px solid rgba(124,58,237,0.3);border-radius:6px;font-size:0.78rem;font-weight:500;cursor:pointer;font-family:'Inter',sans-serif;transition:all 0.2s}
.bsm:hover{background:rgba(124,58,237,0.2)}
.bo{width:100%;padding:12px;background:transparent;color:var(--pl);border:1.5px solid var(--p);border-radius:10px;font-size:0.9rem;font-weight:600;cursor:pointer;font-family:'Inter',sans-serif;transition:all 0.2s;margin-top:10px}
.bo:hover{background:rgba(124,58,237,0.08)}
.ld{display:none;text-align:center;padding:50px}
.sp{width:44px;height:44px;border:3px solid var(--border);border-top:3px solid var(--p);border-radius:50%;animation:spin 0.7s linear infinite;margin:0 auto 14px}
@keyframes spin{to{transform:rotate(360deg)}}
.ld p{color:var(--tm);font-size:0.9rem}
.res{display:none}
.sg{display:flex;gap:18px;flex-wrap:wrap;justify-content:center;padding:12px 0}
.si{text-align:center}
.sr{position:relative;margin:0 auto 8px}
.sr svg{transform:rotate(-90deg)}
.sr circle.tr{fill:none;stroke:var(--border);stroke-width:7}
.sr circle.fl{fill:none;stroke-width:7;stroke-dasharray:251.2;stroke-dashoffset:251.2;stroke-linecap:round;transition:stroke-dashoffset 1.2s ease,stroke 0.3s ease}
.sn{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);font-weight:700;color:var(--t);transition:color 0.3s}
.sl{font-size:0.74rem;color:var(--tm);font-weight:500}
.badge{display:inline-flex;background:rgba(124,58,237,0.12);color:var(--pl);padding:5px 12px;border-radius:20px;margin:3px;font-size:0.8rem;font-weight:500;border:1px solid rgba(124,58,237,0.25)}
.ri{display:flex;gap:12px;align-items:flex-start;padding:13px 15px;background:rgba(239,68,68,0.06);border:1px solid rgba(239,68,68,0.2);border-radius:10px;margin-bottom:8px}
.rd{width:7px;height:7px;background:var(--err);border-radius:50%;margin-top:6px;flex-shrink:0}
.ri p{font-size:0.86rem;color:var(--t);line-height:1.6}
.fc{background:var(--s2);border:1px solid var(--border);border-radius:10px;padding:15px;margin-bottom:10px}
.fb{font-size:0.82rem;color:#f87171;margin-bottom:7px;line-height:1.5}
.fa{font-size:0.82rem;color:#4ade80;line-height:1.5}
.fb span,.fa span{font-weight:600}
.qs{margin-bottom:20px}
.ql{font-size:0.72rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:5px 14px;border-radius:20px;display:inline-block;margin-bottom:10px}
.ql.tech{background:rgba(124,58,237,0.15);color:var(--pl);border:1px solid rgba(124,58,237,0.3)}
.ql.proj{background:rgba(16,185,129,0.12);color:#34d399;border:1px solid rgba(16,185,129,0.25)}
.ql.beh{background:rgba(245,158,11,0.12);color:#fbbf24;border:1px solid rgba(245,158,11,0.25)}
.ql.hr{background:rgba(244,114,182,0.12);color:var(--pk);border:1px solid rgba(244,114,182,0.25)}
.qi{display:flex;gap:11px;padding:13px 15px;background:var(--s2);border:1px solid var(--border);border-radius:10px;margin-bottom:7px;align-items:flex-start;transition:border-color 0.2s}
.qi:hover{border-color:var(--p)}
.qn{width:25px;height:25px;border-radius:7px;display:flex;align-items:center;justify-content:center;font-size:0.7rem;font-weight:700;flex-shrink:0}
.qn.tech{background:rgba(124,58,237,0.2);color:var(--pl)}
.qn.proj{background:rgba(16,185,129,0.15);color:#34d399}
.qn.beh{background:rgba(245,158,11,0.15);color:#fbbf24}
.qn.hr{background:rgba(244,114,182,0.15);color:var(--pk)}
.qi p{font-size:0.86rem;color:var(--t);line-height:1.6;font-weight:500}
.qt{font-size:0.74rem;color:var(--tm);margin-top:3px;font-style:italic}
.co-card{background:var(--s2);border:1px solid var(--border);border-radius:12px;padding:20px;margin-bottom:12px}
.co-card h4{font-size:0.92rem;font-weight:600;color:var(--t);margin-bottom:8px}
.co-card p{font-size:0.84rem;color:var(--tm);line-height:1.6}
.co-tag{display:inline-block;background:rgba(124,58,237,0.1);color:var(--pl);padding:3px 10px;border-radius:12px;font-size:0.78rem;margin:3px}
.co-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px}
.co-stat{background:var(--s2);border:1px solid var(--border);border-radius:10px;padding:14px}
.co-stat .label{font-size:0.72rem;color:var(--tm);text-transform:uppercase;letter-spacing:0.8px;margin-bottom:4px}
.co-stat .val{font-size:0.95rem;font-weight:600;color:var(--t)}
.co-section{margin-bottom:14px}
.co-section h5{font-size:0.78rem;font-weight:700;color:var(--pl);text-transform:uppercase;letter-spacing:0.8px;margin-bottom:8px}
.co-item{display:flex;gap:8px;align-items:flex-start;padding:8px 12px;background:var(--s2);border:1px solid var(--border);border-radius:8px;margin-bottom:6px;font-size:0.84rem;color:var(--t);line-height:1.5}
.co-dot{width:6px;height:6px;border-radius:50%;background:var(--pl);margin-top:6px;flex-shrink:0}
.co-dot.green{background:var(--ok)}
.co-dot.yellow{background:#fbbf24}
.co-dot.red{background:var(--err)}
.em{background:var(--s2);border:1px solid var(--border);border-radius:10px;padding:20px;font-size:0.87rem;line-height:1.9;color:var(--t);white-space:pre-wrap;font-family:'Inter',sans-serif}
.rk{background:var(--s2);border:1px solid var(--border);border-radius:12px;padding:18px 20px;margin-bottom:12px;display:flex;gap:15px;align-items:flex-start;transition:all 0.2s}
.rk:hover{border-color:var(--p);transform:translateX(3px)}
.rk.best{border-color:var(--p);background:rgba(124,58,237,0.07)}
.rn{width:44px;height:44px;border-radius:10px;background:var(--border);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:1rem;color:var(--tm);flex-shrink:0}
.rk.best .rn{background:linear-gradient(135deg,var(--p),#9d174d);color:#fff}
.ri2{flex:1}
.ri2 h4{font-size:0.93rem;font-weight:600;color:var(--t);margin-bottom:4px}
.ri2 p{font-size:0.83rem;color:var(--tm);line-height:1.5}
.rs{font-size:1.4rem;font-weight:800;flex-shrink:0}
.bb{background:linear-gradient(135deg,var(--p),#9d174d);color:#fff;font-size:0.7rem;font-weight:600;padding:2px 10px;border-radius:10px;margin-left:8px;vertical-align:middle}
.chat-wrap{position:fixed;bottom:24px;right:24px;z-index:200}
.chat-tog{width:54px;height:54px;border-radius:50%;background:linear-gradient(135deg,var(--p),#9d174d);border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:1.3rem;box-shadow:0 4px 20px rgba(124,58,237,0.45);transition:all 0.2s}
.chat-tog:hover{transform:scale(1.08)}
.chat-box{position:absolute;bottom:64px;right:0;width:360px;background:var(--s1);border:1px solid var(--border);border-radius:16px;overflow:hidden;display:none;box-shadow:0 20px 50px rgba(0,0,0,0.6)}
.chat-box.open{display:flex;flex-direction:column}
.ch{padding:15px 18px;background:linear-gradient(135deg,var(--p),#9d174d);display:flex;justify-content:space-between;align-items:center}
.ch h4{color:#fff;font-size:0.9rem;font-weight:600}
.ch span{color:rgba(255,255,255,0.75);font-size:0.73rem}
.cx{background:none;border:none;color:#fff;cursor:pointer;font-size:1rem}
.cm{height:290px;overflow-y:auto;padding:14px;display:flex;flex-direction:column;gap:9px}
.msg{max-width:84%;padding:9px 13px;border-radius:11px;font-size:0.84rem;line-height:1.5}
.msg.bot{background:var(--s2);color:var(--t);align-self:flex-start;border:1px solid var(--border);border-bottom-left-radius:3px}
.msg.user{background:linear-gradient(135deg,var(--p),#9d174d);color:#fff;align-self:flex-end;border-bottom-right-radius:3px}
.cty{color:var(--tm);font-size:0.78rem;font-style:italic;padding:3px 14px;display:none}
.ciw{padding:11px;border-top:1px solid var(--border);display:flex;gap:7px}
.ci{flex:1;background:var(--s2);border:1px solid var(--border);border-radius:8px;padding:9px 12px;color:var(--t);font-size:0.84rem;font-family:'Inter',sans-serif;outline:none}
.ci:focus{border-color:var(--p)}
.ci::placeholder{color:var(--tm)}
.cs{background:linear-gradient(135deg,var(--p),#9d174d);border:none;border-radius:8px;padding:9px 13px;color:#fff;cursor:pointer;font-size:0.88rem}
.kyc-companies{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:20px}
.kyc-chip{padding:8px 16px;background:var(--s2);border:1px solid var(--border);border-radius:20px;font-size:0.84rem;color:var(--tm);cursor:pointer;transition:all 0.2s;font-family:'Inter',sans-serif}
.kyc-chip:hover{border-color:var(--pl);color:var(--pl)}
</style>
</head>
<body>
<nav>
  <div>
    <div class="nav-logo">JobFit AI</div>
    <div class="nav-sub">Smart resume analysis powered by AI</div>
  </div>
</nav>
<div class="main">
  <div class="hero">
    <h1>Land Your Dream Job</h1>
    <p>Upload your resume and any job description to get instant ATS analysis, interview prep, and personalized insights</p>
  </div>
  <div class="tabs">
    <button class="tab active" onclick="switchTab('analyze')">Resume Analyzer</button>
    <button class="tab" onclick="switchTab('compare')">Multi-JD Comparator</button>
    <button class="tab" onclick="switchTab('kyc')">Know Your Company</button>
  </div>

  <!-- TAB 1: ANALYZE -->
  <div class="tc active" id="tab-analyze">
    <div class="card">
      <div class="fg">
        <label class="fl">Resume (PDF)</label>
        <div class="ub">
          <div class="fi">📄</div>
          <p><b>Select your resume PDF</b></p>
          <input type="file" id="r1" accept=".pdf" onchange="showFile(this,'fn1')">
          <div class="fn" id="fn1"></div>
        </div>
      </div>
      <div class="fg">
        <label class="fl">Job Description</label>
        <textarea id="jd1" placeholder="Paste the complete job description here..."></textarea>
      </div>
      <button class="bp" id="btn1" onclick="doAnalyze()">Analyze My Resume</button>
      <div class="ld" id="l1"><div class="sp"></div><p>Analyzing your resume...</p></div>
    </div>

    <div class="res" id="res1">
      <div class="card">
        <div class="ct">ATS Match Score</div>
        <div class="sg">
          <div class="si"><div class="sr" style="width:110px;height:110px"><svg viewBox="0 0 100 100" width="110" height="110"><circle class="tr" cx="50" cy="50" r="40"/><circle class="fl" id="arc-t" cx="50" cy="50" r="40" stroke="#7c3aed"/></svg><div class="sn" style="font-size:1.6rem" id="sc-t">--</div></div><div class="sl">Overall</div></div>
          <div class="si"><div class="sr" style="width:82px;height:82px"><svg viewBox="0 0 100 100" width="82" height="82"><circle class="tr" cx="50" cy="50" r="40"/><circle class="fl" id="arc-sk" cx="50" cy="50" r="40" stroke="#f472b6"/></svg><div class="sn" style="font-size:1rem" id="sc-sk">--</div></div><div class="sl">Skills</div></div>
          <div class="si"><div class="sr" style="width:82px;height:82px"><svg viewBox="0 0 100 100" width="82" height="82"><circle class="tr" cx="50" cy="50" r="40"/><circle class="fl" id="arc-ex" cx="50" cy="50" r="40" stroke="#a78bfa"/></svg><div class="sn" style="font-size:1rem" id="sc-ex">--</div></div><div class="sl">Experience</div></div>
          <div class="si"><div class="sr" style="width:82px;height:82px"><svg viewBox="0 0 100 100" width="82" height="82"><circle class="tr" cx="50" cy="50" r="40"/><circle class="fl" id="arc-kw" cx="50" cy="50" r="40" stroke="#34d399"/></svg><div class="sn" style="font-size:1rem" id="sc-kw">--</div></div><div class="sl">Keywords</div></div>
          <div class="si"><div class="sr" style="width:82px;height:82px"><svg viewBox="0 0 100 100" width="82" height="82"><circle class="tr" cx="50" cy="50" r="40"/><circle class="fl" id="arc-ed" cx="50" cy="50" r="40" stroke="#fbbf24"/></svg><div class="sn" style="font-size:1rem" id="sc-ed">--</div></div><div class="sl">Education</div></div>
        </div>
      </div>
      <div class="card"><div class="ct">Missing Keywords</div><div id="kw"></div></div>
      <div class="card"><div class="ct">Rejection Risk Factors</div><div id="rr"></div></div>
      <div class="card"><div class="ct">Resume Rewriter — Copy Ready</div><div id="rw"></div></div>
      <div class="card"><div class="ct">Interview Preparation</div><div id="iq"></div></div>
      <div class="card"><div class="ct">Company Research</div><div id="co"></div></div>
      <div class="card">
        <div class="ct">Cold Email to Recruiter</div>
        <button class="bsm" onclick="copyEmail()" style="margin-bottom:12px">Copy Email</button>
        <div class="em" id="em"></div>
        <button class="bo" onclick="dlPDF()">Download Full Report as PDF</button>
      </div>
    </div>
  </div>

  <!-- TAB 2: COMPARE -->
  <div class="tc" id="tab-compare">
    <div class="card">
      <div class="fg">
        <label class="fl">Resume (PDF)</label>
        <div class="ub">
          <div class="fi">📄</div>
          <p><b>Select your resume PDF</b></p>
          <input type="file" id="r2" accept=".pdf" onchange="showFile(this,'fn2')">
          <div class="fn" id="fn2"></div>
        </div>
      </div>
      <div class="fg"><label class="fl">Job Description 1</label><textarea id="cj1" placeholder="Paste first JD..."></textarea></div>
      <div class="fg"><label class="fl">Job Description 2</label><textarea id="cj2" placeholder="Paste second JD..."></textarea></div>
      <div class="fg"><label class="fl">Job Description 3 (Optional)</label><textarea id="cj3" placeholder="Paste third JD..."></textarea></div>
      <button class="bp" id="btn2" onclick="doCompare()">Compare All JDs</button>
      <div class="ld" id="l2"><div class="sp"></div><p>Comparing job descriptions...</p></div>
    </div>
    <div class="res" id="res2">
      <div class="card"><div class="ct">Best Match Ranking</div><div id="ranks"></div></div>
    </div>
  </div>

  <!-- TAB 3: KYC -->
  <div class="tc" id="tab-kyc">
    <div class="card">
      <div class="ct">Know Your Company</div>
      <p style="color:var(--tm);font-size:0.88rem;margin-bottom:16px">Research any company before your interview — get key facts, culture, interview tips and recent updates</p>
      <div class="kyc-companies">
        <div class="kyc-chip" onclick="setCompany('TCS')">TCS</div>
        <div class="kyc-chip" onclick="setCompany('Infosys')">Infosys</div>
        <div class="kyc-chip" onclick="setCompany('Wipro')">Wipro</div>
        <div class="kyc-chip" onclick="setCompany('Cognizant')">Cognizant</div>
        <div class="kyc-chip" onclick="setCompany('Accenture')">Accenture</div>
        <div class="kyc-chip" onclick="setCompany('Google')">Google</div>
        <div class="kyc-chip" onclick="setCompany('Microsoft')">Microsoft</div>
        <div class="kyc-chip" onclick="setCompany('Amazon')">Amazon</div>
        <div class="kyc-chip" onclick="setCompany('IBM')">IBM</div>
        <div class="kyc-chip" onclick="setCompany('Capgemini')">Capgemini</div>
        <div class="kyc-chip" onclick="setCompany('HCL Technologies')">HCL</div>
        <div class="kyc-chip" onclick="setCompany('Tech Mahindra')">Tech Mahindra</div>
      </div>
      <div class="fg">
        <label class="fl">Or type any company name</label>
        <input class="inp" id="kyc-input" placeholder="e.g. Janooma, Impressico, Zoho..." onkeydown="if(event.key==='Enter')doKYC()">
      </div>
      <button class="bp" id="btn3" onclick="doKYC()">Research This Company</button>
      <div class="ld" id="l3"><div class="sp"></div><p>Fetching company information...</p></div>
    </div>
    <div class="res" id="res3">
      <div class="card" id="kyc-result"></div>
    </div>
  </div>
</div>

<div class="chat-wrap">
  <div class="chat-box" id="chatBox">
    <div class="ch">
      <div><h4>Interview Coach</h4><span>Powered by AI</span></div>
      <button class="cx" onclick="toggleChat()">X</button>
    </div>
    <div class="cm" id="chatMsgs">
      <div class="msg bot">Hi! I am your interview coach. Analyze your resume first, then ask me anything about interview preparation!</div>
    </div>
    <div class="cty" id="cty">Coach is typing...</div>
    <div class="ciw">
      <input class="ci" id="ci" placeholder="Ask about interview prep..." onkeydown="if(event.key==='Enter')sendChat()">
      <button class="cs" onclick="sendChat()">Send</button>
    </div>
  </div>
  <button class="chat-tog" onclick="toggleChat()">💬</button>
</div>

<script>
let ctx = '';
let chatOpen = false;

function getColor(val) {
  if(val >= 75) return '#10b981';
  if(val >= 50) return '#fbbf24';
  return '#ef4444';
}

function switchTab(t) {
  document.querySelectorAll('.tab').forEach((e,i) => e.classList.toggle('active', ['analyze','compare','kyc'][i] === t));
  document.querySelectorAll('.tc').forEach(e => e.classList.remove('active'));
  document.getElementById('tab-' + t).classList.add('active');
}

function showFile(input, id) {
  if(input.files[0]) document.getElementById(id).textContent = '✓ ' + input.files[0].name;
}

function arc(id, val) {
  const el = document.getElementById('arc-' + id);
  const sn = document.getElementById('sc-' + id);
  if(!el || isNaN(val)) return;
  const color = getColor(val);
  el.style.stroke = color;
  if(sn) sn.style.color = color;
  setTimeout(() => { el.style.strokeDashoffset = 251.2 - (251.2 * Math.min(val,100) / 100); }, 300);
}

function gv(text, label) {
  const idx = text.indexOf(label);
  if(idx === -1) return null;
  const sub = text.substring(idx, idx + 50);
  const m = sub.match(/(\d+)/);
  return m ? parseInt(m[1]) : null;
}

function parseResult(text) {
  ctx = text.substring(0, 1500);
  const scores = {t:'ATS_SCORE', sk:'Skills', ex:'Experience', kw:'Keywords', ed:'Education'};
  Object.entries(scores).forEach(([id, label]) => {
    const v = gv(text, label);
    if(v !== null) { document.getElementById('sc-'+id).textContent = v; arc(id, v); }
  });

  const km = text.match(/MISSING_KEYWORDS:(.*?)(?=REJECTION_REASONS:|$)/si);
  if(km) document.getElementById('kw').innerHTML = km[1].trim().split('\\n').filter(k=>k.trim().startsWith('-')).map(k=>'<span class="badge">'+k.replace(/^-\\s*/,'').trim()+'</span>').join('');

  const rm = text.match(/REJECTION_REASONS:(.*?)(?=RESUME_REWRITER:|$)/si);
  if(rm) document.getElementById('rr').innerHTML = rm[1].trim().split('\\n').filter(r=>r.trim().startsWith('-')).map(r=>'<div class="ri"><div class="rd"></div><p>'+r.replace(/^-\\s*/,'').trim()+'</p></div>').join('');

  const rwm = text.match(/RESUME_REWRITER:(.*?)(?=INTERVIEW_QUESTIONS:|$)/si);
  if(rwm) document.getElementById('rw').innerHTML = rwm[1].trim().split('\\n').filter(r=>r.includes('Original:')).map(r=>{const p=r.split('|');return '<div class="fc"><div class="fb"><span>Before:</span> '+(p[0]||'').replace(/.*Original:/i,'').trim()+'</div><div class="fa"><span>After:</span> '+(p[1]||'').replace(/Rewritten:/i,'').trim()+'</div></div>';}).join('');

  const iqm = text.match(/INTERVIEW_QUESTIONS:(.*?)(?=COMPANY_RESEARCH:|$)/si);
  if(iqm){
    const iq = iqm[1];
    const secs = [
      {k:'TECHNICAL',l:'Technical',c:'tech',t:'Prepare with code examples and demos'},
      {k:'PROJECT_BASED',l:'Project Based',c:'proj',t:'Walk through challenges, solutions, results'},
      {k:'BEHAVIORAL',l:'Behavioral',c:'beh',t:'Use STAR: Situation Task Action Result'},
      {k:'HR',l:'HR Round',c:'hr',t:'Research the company, be honest'}
    ];
    let html = '';
    secs.forEach(s => {
      const sm = iq.match(new RegExp(s.k+':(.*?)(?=TECHNICAL:|PROJECT_BASED:|BEHAVIORAL:|HR:|$)','si'));
      if(sm){
        const qs = sm[1].trim().split('\\n').filter(q=>q.trim().startsWith('-'));
        if(qs.length){
          html += '<div class="qs"><span class="ql '+s.c+'">'+s.l+'</span>';
          html += qs.map((q,i)=>'<div class="qi"><div class="qn '+s.c+'">'+(i+1)+'</div><div><p>'+q.replace(/^-\\s*/,'').trim()+'</p><div class="qt">'+s.t+'</div></div></div>').join('');
          html += '</div>';
        }
      }
    });
    document.getElementById('iq').innerHTML = html;
  }

  const com = text.match(/COMPANY_RESEARCH:(.*?)(?=COLD_EMAIL:|$)/si);
  if(com){
    const ct = com[1];
    const cn = ct.match(/Company Name:(.*)/i);
    const ind = ct.match(/Industry:(.*)/i);
    const rt = ct.match(/Role Type:(.*)/i);
    const kf = ct.match(/Key Focus Areas:(.*)/i);
    const tp = ct.match(/Talking Points:(.*)/si);
    document.getElementById('co').innerHTML =
      '<div class="co-card"><h4>'+(cn?cn[1].trim():'Company')+'</h4>'+
      (ind?'<span class="co-tag">'+ind[1].trim()+'</span>':'')+
      (rt?'<span class="co-tag">'+rt[1].trim()+'</span>':'')+
      (kf?'<p style="margin-top:10px"><b style="color:var(--t)">Key Focus:</b> '+kf[1].trim()+'</p>':'')+
      (tp?'<p style="margin-top:8px"><b style="color:var(--t)">Mention in interview:</b> '+tp[1].trim()+'</p>':'')+
      '</div>';
  }

  const em = text.match(/COLD_EMAIL:([\s\S]*)/i);
  if(em) document.getElementById('em').textContent = em[1].trim();
}

function parseKYC(text, company) {
  const get = (label) => { const m = text.match(new RegExp(label+':\\s*(.+)')); return m ? m[1].trim() : 'N/A'; };
  const getSection = (label, next) => {
    const m = text.match(new RegExp(label+':(.*?)(?='+next+':|$)','si'));
    return m ? m[1].trim().split('\\n').filter(l=>l.trim().startsWith('-')).map(l=>l.replace(/^-\\s*/,'').trim()) : [];
  };
  const getBlock = (label, next) => {
    const m = text.match(new RegExp(label+':(.*?)(?='+next+':|$)','si'));
    return m ? m[1].trim() : '';
  };

  const stats = [
    {l:'Founded', v:get('FOUNDED')},
    {l:'HQ', v:get('HEADQUARTERS')},
    {l:'Employees', v:get('EMPLOYEES')},
    {l:'CEO', v:get('CEO')},
    {l:'Revenue', v:get('REVENUE')},
    {l:'Industry', v:get('INDUSTRY')}
  ];

  const about = getBlock('ABOUT','PRODUCTS_SERVICES');
  const products = getSection('PRODUCTS_SERVICES','CULTURE_VALUES');
  const culture = getSection('CULTURE_VALUES','INTERVIEW_TIPS');
  const tips = getSection('INTERVIEW_TIPS','RECENT_NEWS');
  const news = getSection('RECENT_NEWS','WHY_JOIN');
  const why = getBlock('WHY_JOIN','WATCH_OUT');
  const watch = getBlock('WATCH_OUT','$');

  let html = '<div class="ct">'+company+' — Company Research</div>';

  html += '<div class="co-grid">';
  stats.forEach(s => { html += '<div class="co-stat"><div class="label">'+s.l+'</div><div class="val">'+s.v+'</div></div>'; });
  html += '</div>';

  if(about) html += '<div class="co-section"><h5>About</h5><div class="co-card"><p>'+about+'</p></div></div>';

  if(products.length) {
    html += '<div class="co-section"><h5>Products & Services</h5>';
    products.forEach(p => { html += '<div class="co-item"><div class="co-dot"></div>'+p+'</div>'; });
    html += '</div>';
  }

  if(culture.length) {
    html += '<div class="co-section"><h5>Culture & Values</h5>';
    culture.forEach(c => { html += '<div class="co-item"><div class="co-dot green"></div>'+c+'</div>'; });
    html += '</div>';
  }

  if(tips.length) {
    html += '<div class="co-section"><h5>Interview Tips for '+company+'</h5>';
    tips.forEach(t => { html += '<div class="co-item"><div class="co-dot yellow"></div>'+t+'</div>'; });
    html += '</div>';
  }

  if(news.length) {
    html += '<div class="co-section"><h5>Recent News & Updates</h5>';
    news.forEach(n => { html += '<div class="co-item"><div class="co-dot"></div>'+n+'</div>'; });
    html += '</div>';
  }

  if(why) html += '<div class="co-section"><h5>Why Join</h5><div class="co-card" style="border-color:rgba(16,185,129,0.3)"><p style="color:#4ade80">'+why+'</p></div></div>';
  if(watch) html += '<div class="co-section"><h5>Watch Out For</h5><div class="co-card" style="border-color:rgba(239,68,68,0.3)"><p style="color:#f87171">'+watch+'</p></div></div>';

  document.getElementById('kyc-result').innerHTML = html;
}

function parseCompare(text) {
  const blocks = text.match(/JD_RANK_\\d+:([\\s\\S]*?)(?=JD_RANK_\\d+:|$)/gi) || [];
  document.getElementById('ranks').innerHTML = blocks.map((b,i)=>{
    const sc=b.match(/Match Score:\\s*(\\d+)/i);
    const ro=b.match(/Company\\/Role:\\s*(.+)/i);
    const wh=b.match(/Why Best Fit:\\s*(.+)/i);
    const sk=b.match(/Key Matching Skills:\\s*(.+)/i);
    const gp=b.match(/Gap:\\s*(.+)/i);
    const best=i===0;
    const score=sc?parseInt(sc[1]):0;
    const color=getColor(score);
    return '<div class="rk'+(best?' best':'')+'"><div class="rn">'+(i+1)+'</div><div class="ri2"><h4>'+(ro?ro[1].trim():'JD '+(i+1))+(best?'<span class="bb">Best Match</span>':'')+'</h4><p>'+(wh?wh[1].trim():'')+'</p>'+(sk?'<p style="margin-top:5px;font-size:0.78rem;color:var(--pl)">'+sk[1].trim()+'</p>':'')+(gp?'<p style="font-size:0.78rem;color:var(--err);margin-top:3px">Gap: '+gp[1].trim()+'</p>':'')+'</div><div class="rs" style="color:'+color+';">'+(sc?sc[1]:'--')+'%</div></div>';
  }).join('');
}

function copyEmail() { navigator.clipboard.writeText(document.getElementById('em').textContent); alert('Email copied!'); }

async function dlPDF() {
  const fd = new FormData();
  fd.append('content', document.getElementById('res1').innerText);
  fd.append('name', 'Candidate');
  const r = await fetch('/download-pdf', {method:'POST', body:fd});
  const blob = await r.blob();
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'JobFitAI_Report.pdf';
  a.click();
}

function setCompany(name) {
  document.getElementById('kyc-input').value = name;
  doKYC();
}

async function doKYC() {
  const company = document.getElementById('kyc-input').value.trim();
  if(!company) { alert('Please enter a company name!'); return; }
  document.getElementById('btn3').disabled = true;
  document.getElementById('l3').style.display = 'block';
  document.getElementById('res3').style.display = 'none';
  const fd = new FormData();
  fd.append('company', company);
  try {
    const r = await fetch('/company-info', {method:'POST', body:fd});
    const d = await r.json();
    document.getElementById('l3').style.display = 'none';
    document.getElementById('res3').style.display = 'block';
    parseKYC(d.result, company);
    document.getElementById('res3').scrollIntoView({behavior:'smooth', block:'start'});
  } catch(e) {
    document.getElementById('l3').style.display = 'none';
    alert('Error: ' + e.message);
  }
  document.getElementById('btn3').disabled = false;
}

async function doAnalyze() {
  const f = document.getElementById('r1');
  const jd = document.getElementById('jd1').value.trim();
  if(!f.files[0]) { alert('Please select a PDF file!'); return; }
  if(!jd) { alert('Please paste a job description!'); return; }
  document.getElementById('btn1').disabled = true;
  document.getElementById('l1').style.display = 'block';
  document.getElementById('res1').style.display = 'none';
  const fd = new FormData();
  fd.append('resume', f.files[0]);
  fd.append('jd', jd);
  try {
    const r = await fetch('/analyze', {method:'POST', body:fd});
    const d = await r.json();
    document.getElementById('l1').style.display = 'none';
    document.getElementById('res1').style.display = 'block';
    parseResult(d.result);
    document.getElementById('res1').scrollIntoView({behavior:'smooth', block:'start'});
  } catch(e) {
    document.getElementById('l1').style.display = 'none';
    alert('Error: ' + e.message);
  }
  document.getElementById('btn1').disabled = false;
}

async function doCompare() {
  const f = document.getElementById('r2');
  const j1 = document.getElementById('cj1').value.trim();
  const j2 = document.getElementById('cj2').value.trim();
  const j3 = document.getElementById('cj3').value.trim();
  if(!f.files[0]) { alert('Please select a PDF file!'); return; }
  if(!j1||!j2) { alert('Please paste at least 2 job descriptions!'); return; }
  document.getElementById('btn2').disabled = true;
  document.getElementById('l2').style.display = 'block';
  document.getElementById('res2').style.display = 'none';
  const fd = new FormData();
  fd.append('resume', f.files[0]);
  fd.append('jds', [j1,j2,j3].filter(Boolean).join('\\n---\\n'));
  try {
    const r = await fetch('/compare', {method:'POST', body:fd});
    const d = await r.json();
    document.getElementById('l2').style.display = 'none';
    document.getElementById('res2').style.display = 'block';
    parseCompare(d.result);
  } catch(e) {
    document.getElementById('l2').style.display = 'none';
    alert('Error: ' + e.message);
  }
  document.getElementById('btn2').disabled = false;
}

function toggleChat() {
  chatOpen = !chatOpen;
  document.getElementById('chatBox').classList.toggle('open', chatOpen);
}

async function sendChat() {
  const inp = document.getElementById('ci');
  const msg = inp.value.trim();
  if(!msg) return;
  addMsg(msg, 'user');
  inp.value = '';
  document.getElementById('cty').style.display = 'block';
  const fd = new FormData();
  fd.append('message', msg);
  fd.append('context', ctx || 'No analysis yet.');
  try {
    const r = await fetch('/chat', {method:'POST', body:fd});
    const d = await r.json();
    document.getElementById('cty').style.display = 'none';
    addMsg(d.response, 'bot');
  } catch(e) {
    document.getElementById('cty').style.display = 'none';
    addMsg('Something went wrong.', 'bot');
  }
}

function addMsg(text, type) {
  const m = document.getElementById('chatMsgs');
  const d = document.createElement('div');
  d.className = 'msg ' + type;
  d.textContent = text;
  m.appendChild(d);
  m.scrollTop = m.scrollHeight;
}
</script>
</body>
</html>""")
html.close()
print("Done!")