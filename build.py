# -*- coding: utf-8 -*-
# Builds the flat, multi-page IRAAC website (7 self-contained HTML files,
# CSS/JS inlined in each) with hero photography and the "charity, not
# government" + multi-channel contact content added after the clickable
# prototype review.

IMG = {
    "hero": "https://picsum.photos/seed/iraac-hero/1800/1000",
    "art": "https://picsum.photos/seed/iraac-art-placeholder/900/900",
    "about": "https://picsum.photos/seed/iraac-community/1200/900",
    "mcc": "https://picsum.photos/seed/iraac-mcc/900/650",
    "youthscape": "https://picsum.photos/seed/iraac-youth/900/650",
    "thecrew": "https://picsum.photos/seed/iraac-crew/900/650",
    "darc": "https://picsum.photos/seed/iraac-darc/900/650",
    "governance": "https://picsum.photos/seed/iraac-meeting/1200/800",
    "support": "https://picsum.photos/seed/iraac-support/1200/800",
    "office": "https://picsum.photos/seed/iraac-office/700/500",
    "news1": "https://picsum.photos/seed/iraac-news1/700/500",
    "news2": "https://picsum.photos/seed/iraac-news2/700/500",
}

CSS = """
:root {
  --charcoal: #201c1a;
  --charcoal-soft: #322b26;
  --cream: #faf6ef;
  --sand: #f0e6d6;
  --ochre: #c1631f;
  --ochre-dark: #8f4416;
  --text: #2b2724;
  --muted: #6b625a;
  --max-width: 1120px;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { margin: 0; font-family: "Segoe UI", -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif; color: var(--text); background: var(--cream); line-height: 1.6; }
a { color: inherit; }
img { max-width: 100%; display: block; }
.container { max-width: var(--max-width); margin: 0 auto; padding: 0 24px; }
header.site-header { background: var(--charcoal); color: var(--cream); position: sticky; top: 0; z-index: 50; }
.header-inner { display: flex; align-items: center; justify-content: space-between; padding: 16px 24px; max-width: var(--max-width); margin: 0 auto; }
.wordmark { font-size: 1.5rem; font-weight: 700; letter-spacing: 0.06em; text-decoration: none; color: var(--cream); }
.wordmark span { color: var(--ochre); }
nav.main-nav ul { list-style: none; display: flex; gap: 22px; margin: 0; padding: 0; flex-wrap: wrap; }
nav.main-nav a { text-decoration: none; color: var(--sand); font-size: 0.92rem; font-weight: 500; border-bottom: 2px solid transparent; padding-bottom: 4px; }
nav.main-nav a:hover, nav.main-nav a.active { color: var(--ochre); border-bottom-color: var(--ochre); }
.nav-toggle { display: none; background: none; border: none; color: var(--cream); font-size: 1.6rem; cursor: pointer; }
@media (max-width: 860px) {
  nav.main-nav { display: none; width: 100%; padding: 0 0 14px; }
  nav.main-nav.open { display: block; }
  nav.main-nav ul { flex-direction: column; gap: 12px; }
  .header-inner { flex-wrap: wrap; }
  .nav-toggle { display: block; }
}
.hero { position: relative; color: var(--cream); padding: 110px 0 90px; background-size: cover; background-position: center; isolation: isolate; }
.hero::before { content: ""; position: absolute; inset: 0; background: linear-gradient(120deg, rgba(20,16,14,0.88) 10%, rgba(32,28,26,0.55) 65%, rgba(32,28,26,0.35) 100%); z-index: -1; }
.hero .container { max-width: 760px; }
.eyebrow { color: var(--ochre); text-transform: uppercase; letter-spacing: 0.14em; font-size: 0.8rem; font-weight: 700; margin-bottom: 14px; }
.hero h1 { font-size: 2.7rem; line-height: 1.15; margin: 0 0 20px; }
.hero p { font-size: 1.15rem; color: var(--sand); max-width: 620px; }
.page-hero { position: relative; color: var(--cream); padding: 70px 0 60px; background-size: cover; background-position: center; isolation: isolate; }
.page-hero::before { content: ""; position: absolute; inset: 0; background: linear-gradient(120deg, rgba(20,16,14,0.90) 20%, rgba(32,28,26,0.6) 100%); z-index: -1; }
.page-hero h1 { font-size: 2.2rem; margin: 0 0 12px; }
.page-hero p { color: var(--sand); max-width: 640px; font-size: 1.05rem; }
.btn { display: inline-block; padding: 13px 26px; border-radius: 4px; text-decoration: none; font-weight: 600; font-size: 0.95rem; margin-right: 14px; margin-top: 10px; }
.btn-primary { background: var(--ochre); color: var(--cream); }
.btn-primary:hover { background: var(--ochre-dark); }
.btn-outline { background: transparent; color: var(--cream); border: 1px solid rgba(250,246,239,0.5); }
.btn-outline:hover { border-color: var(--ochre); color: var(--ochre); }
section { padding: 64px 0; }
section.alt { background: var(--sand); }
h2.section-title { font-size: 1.9rem; margin: 0 0 14px; }
p.section-lead { color: var(--muted); max-width: 680px; font-size: 1.05rem; margin-bottom: 40px; }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 28px; }
.card { background: #fff; border: 1px solid rgba(0,0,0,0.06); border-radius: 10px; overflow: hidden; }
.card img { width: 100%; height: 160px; object-fit: cover; }
.card .card-body { padding: 22px; }
.card h3 { margin: 0 0 10px; font-size: 1.15rem; color: var(--ochre-dark); }
.card p { color: var(--muted); font-size: 0.96rem; margin: 0; }
.card a.card-link { display: inline-block; margin-top: 14px; font-weight: 600; color: var(--ochre); text-decoration: none; font-size: 0.9rem; }
.two-col { display: grid; grid-template-columns: 1.05fr 0.95fr; gap: 48px; align-items: center; }
.two-col img { border-radius: 10px; width: 100%; height: 340px; object-fit: cover; }
@media (max-width: 860px) { .two-col { grid-template-columns: 1fr; } .two-col img { height: 220px; } }
.program-block { padding: 48px 0; border-bottom: 1px solid rgba(0,0,0,0.08); }
.program-block:last-child { border-bottom: none; }
.program-hero { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center; margin-bottom: 6px; }
.program-hero img { border-radius: 10px; height: 280px; width: 100%; object-fit: cover; }
@media (max-width: 860px) { .program-hero { grid-template-columns: 1fr; } .program-hero img { height: 200px; } }
.program-block .tag { display: inline-block; background: var(--sand); color: var(--charcoal); font-size: 0.75rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; padding: 4px 10px; border-radius: 3px; margin-bottom: 12px; }
.program-block h2 { font-size: 1.7rem; color: var(--ochre-dark); margin: 0 0 12px; }
.note-box { background: var(--sand); border-left: 4px solid var(--ochre); padding: 18px 22px; border-radius: 4px; font-size: 0.95rem; color: var(--charcoal-soft); margin: 24px 0; }
.contact-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 24px; }
.contact-card { background: #fff; border: 1px solid rgba(0,0,0,0.06); border-radius: 10px; padding: 26px; }
.contact-card .icon { font-size: 1.8rem; margin-bottom: 10px; }
.contact-card h3 { margin: 0 0 8px; font-size: 1.1rem; color: var(--ochre-dark); }
.contact-card p { color: var(--muted); font-size: 0.93rem; margin: 0 0 14px; }
form.contact-form { display: grid; gap: 16px; max-width: 560px; }
form.contact-form label { font-weight: 600; font-size: 0.9rem; display: block; margin-bottom: 6px; }
form.contact-form input, form.contact-form select, form.contact-form textarea { width: 100%; padding: 12px 14px; border: 1px solid rgba(0,0,0,0.15); border-radius: 4px; font-size: 0.95rem; font-family: inherit; }
.news-item { display: grid; grid-template-columns: 220px 1fr; gap: 24px; padding: 26px 0; border-bottom: 1px solid rgba(0,0,0,0.08); align-items: center; }
.news-item img { border-radius: 8px; height: 130px; width: 100%; object-fit: cover; }
@media (max-width: 700px) { .news-item { grid-template-columns: 1fr; } .news-item img { height: 160px; } }
.news-item .date { font-size: 0.8rem; color: var(--ochre); font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; }
.news-item h3 { margin: 6px 0 8px; }
.acknowledgement { background: var(--charcoal-soft); color: var(--sand); font-size: 0.88rem; padding: 16px 0; }
footer.site-footer { background: var(--charcoal); color: var(--sand); padding: 48px 0 28px; margin-top: 40px; }
.footer-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 30px; margin-bottom: 30px; }
.footer-grid h4 { color: var(--cream); margin: 0 0 12px; font-size: 0.95rem; }
.footer-grid ul { list-style: none; padding: 0; margin: 0; }
.footer-grid li { margin-bottom: 8px; }
.footer-grid a { color: var(--sand); text-decoration: none; font-size: 0.92rem; }
.footer-grid a:hover { color: var(--ochre); }
.footer-bottom { border-top: 1px solid rgba(250,246,239,0.12); padding-top: 20px; font-size: 0.82rem; color: rgba(250,246,239,0.6); display: flex; justify-content: space-between; flex-wrap: wrap; gap: 10px; }

/* Quick actions bar — the primary conversion bar, sticky right under the header */
.quickbar { background: var(--sand); border-bottom: 1px solid rgba(0,0,0,0.08); position: sticky; top: 61px; z-index: 40; }
.quickbar-inner { max-width: var(--max-width); margin: 0 auto; padding: 12px 24px; display: flex; gap: 10px; flex-wrap: wrap; align-items: center; }
.quickbar-label { font-size: 0.78rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); margin-right: 4px; }
.qbtn { display: inline-flex; align-items: center; gap: 7px; padding: 9px 16px; border-radius: 999px; font-size: 0.88rem; font-weight: 600; text-decoration: none; border: 1px solid rgba(0,0,0,0.12); background: #fff; color: var(--text); }
.qbtn:hover { border-color: var(--ochre); color: var(--ochre-dark); }
.qbtn.qbtn-primary { background: var(--ochre); color: #fff; border-color: var(--ochre); }
.qbtn.qbtn-primary:hover { background: var(--ochre-dark); border-color: var(--ochre-dark); }
@media (max-width: 700px) { .quickbar-inner { padding: 10px 16px; } .quickbar-label { display: none; } }

/* Hero with artwork panel */
.hero-flex { position: relative; background: linear-gradient(120deg, var(--charcoal) 0%, var(--charcoal-soft) 100%); color: var(--cream); isolation: isolate; }
.hero-flex .container { display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 40px; align-items: center; padding-top: 70px; padding-bottom: 70px; max-width: var(--max-width); }
.hero-flex .art-panel { border-radius: 14px; overflow: hidden; position: relative; height: 340px; }
.hero-flex .art-panel img { width: 100%; height: 100%; object-fit: cover; }
.hero-flex .art-panel .art-caption { position: absolute; left: 0; right: 0; bottom: 0; background: rgba(20,16,14,0.72); color: var(--sand); font-size: 0.72rem; padding: 8px 12px; }
@media (max-width: 900px) { .hero-flex .container { grid-template-columns: 1fr; } .hero-flex .art-panel { height: 220px; } }
.hero-flex h1 { font-size: 2.5rem; line-height: 1.15; margin: 0 0 18px; }
.hero-flex p { font-size: 1.1rem; color: var(--sand); max-width: 560px; }

/* Survey */
.survey-shell { background: #fff; border: 1px solid rgba(0,0,0,0.08); border-radius: 12px; padding: 36px; max-width: 640px; }
.survey-step-label { font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.06em; color: var(--ochre); font-weight: 700; margin-bottom: 8px; }
.q-block { margin-bottom: 28px; }
.q-block > label.q-title { display: block; font-weight: 700; margin-bottom: 10px; font-size: 1rem; }
.q-help { font-size: 0.85rem; color: var(--muted); margin: -6px 0 10px; }
.option-row { display: flex; flex-wrap: wrap; gap: 10px; }
.option-pill { border: 1px solid rgba(0,0,0,0.15); border-radius: 8px; padding: 10px 14px; font-size: 0.9rem; cursor: pointer; background: #fff; }
.option-pill input { margin-right: 8px; }
.option-pill:has(input:checked) { border-color: var(--ochre); background: var(--sand); }
.consent-box { background: var(--sand); border-radius: 8px; padding: 16px 18px; font-size: 0.85rem; color: var(--charcoal-soft); margin-top: 6px; }

/* Office locator */
.map-embed { width: 100%; height: 420px; border: 0; border-radius: 12px; }
.office-list { display: grid; gap: 14px; margin-top: 24px; }
.office-item { background: #fff; border: 1px solid rgba(0,0,0,0.08); border-radius: 10px; padding: 18px 20px; display: flex; justify-content: space-between; align-items: center; gap: 16px; flex-wrap: wrap; }
.office-item h4 { margin: 0 0 4px; color: var(--ochre-dark); }
.office-item p { margin: 0; color: var(--muted); font-size: 0.9rem; }

/* Sector / system explainer */
.system-block { padding: 40px 0; border-bottom: 1px solid rgba(0,0,0,0.08); }
.system-block:last-child { border-bottom: none; }
.system-block .system-kicker { display: inline-block; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; padding: 4px 10px; border-radius: 3px; margin-bottom: 10px; background: var(--sand); color: var(--charcoal); }
.system-block .system-kicker.is-emerging { background: rgba(193,99,31,0.14); color: var(--ochre-dark); }
.system-block h3 { font-size: 1.35rem; color: var(--ochre-dark); margin: 0 0 12px; }
.system-block p { color: var(--charcoal-soft); max-width: 760px; }
.system-block p + p { margin-top: 12px; }

/* Book a call */
.call-card { background: #fff; border: 1px solid rgba(0,0,0,0.08); border-radius: 12px; padding: 36px; max-width: 560px; }
.call-card .duration { display:inline-block; background: var(--sand); color: var(--charcoal); font-weight:700; font-size:0.8rem; padding:5px 12px; border-radius:999px; margin-bottom:16px; }
"""

JS = """
document.addEventListener("DOMContentLoaded", function () {
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".main-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () { nav.classList.toggle("open"); });
  }
  var form = document.querySelector(".contact-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var note = document.getElementById("form-note");
      if (note) { note.textContent = "Thanks \\u2014 this demo form doesn't send yet. Connect it to an email address or form service to go live."; note.style.display = "block"; }
    });
  }
  var survey = document.getElementById("iraac-survey");
  if (survey) {
    survey.addEventListener("submit", function (e) {
      e.preventDefault();
      survey.style.display = "none";
      var thanks = document.getElementById("survey-thanks");
      if (thanks) { thanks.style.display = "block"; thanks.scrollIntoView({behavior: "smooth", block: "start"}); }
    });
  }
});
"""

NAV_ITEMS = [
    ("index.html", "Home"),
    ("about.html", "Our Story"),
    ("programs.html", "Our Programs"),
    ("governance.html", "Governance & Reporting"),
    ("support.html", "Supporting Other Organisations"),
    ("news.html", "News"),
    ("contact.html", "Contact"),
]

def header(active):
    links = ""
    for href, label in NAV_ITEMS:
        cls = ' class="active"' if href == active else ""
        links += f'<li><a href="{href}"{cls}>{label}</a></li>\n'
    return f"""<header class="site-header">
  <div class="header-inner">
    <a href="index.html" class="wordmark">IRAAC<span>.</span></a>
    <button class="nav-toggle" aria-label="Toggle menu">&#9776;</button>
    <nav class="main-nav"><ul>{links}</ul></nav>
  </div>
</header>
"""

QUICKBAR = """<div class="quickbar">
  <div class="quickbar-inner">
    <span class="quickbar-label">Need support?</span>
    <a class="qbtn qbtn-primary" href="book-a-call.html">&#128197; Book a Free 15-Min Call</a>
    <a class="qbtn" href="offices.html">&#127968; Visit a Local Office</a>
    <a class="qbtn" href="contact.html#home-visit">&#128100; Request a Home Visit</a>
    <a class="qbtn" href="survey.html">&#128203; Complete a Survey</a>
  </div>
</div>
"""

FOOTER = """<div class="acknowledgement">
  <div class="container">IRAAC acknowledges the Traditional Custodians of the lands on which we work, live and gather, and pays respect to Elders past, present and emerging.</div>
</div>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div><h4>IRAAC</h4><ul>
        <li><a href="about.html">Our Story</a></li>
        <li><a href="governance.html">Governance &amp; Reporting</a></li>
        <li><a href="contact.html">Contact Us</a></li>
      </ul></div>
      <div><h4>Our Programs</h4><ul>
        <li><a href="programs.html#mcc">MCC &mdash; Mob and Country Connections</a></li>
        <li><a href="programs.html#youthscape">YouthScape</a></li>
        <li><a href="programs.html#thecrew">The Crew</a></li>
        <li><a href="programs.html#darc">DARC</a></li>
      </ul></div>
      <div><h4>Get Involved</h4><ul>
        <li><a href="support.html">Support for Aboriginal Community Organisations</a></li>
        <li><a href="news.html">Latest Updates</a></li>
        <li><a href="contact.html">Get in Touch</a></li>
      </ul></div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 IRAAC. All rights reserved.</span>
      <span>Site content is a working draft &mdash; contact the Secretary to update.</span>
    </div>
  </div>
</footer>
"""

def page(title, description, active, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title} | IRAAC</title>
<meta name="description" content="{description}" />
<style>{CSS}</style>
</head>
<body>
{header(active)}
{QUICKBAR}
{body}
{FOOTER}
<script>{JS}</script>
</body>
</html>
"""

INDEX = f"""
<section class="hero-flex">
  <div class="container">
    <div>
      <div class="eyebrow">Aboriginal Community Organisation &middot; Local Decision Making</div>
      <h1>Strong governance. Strong programs. Strong community.</h1>
      <p>IRAAC is a community organisation working with and for community through Local Decision Making. We deliver programs, build governance capability, and help other Aboriginal Community Organisations do the same.</p>
      <a href="book-a-call.html" class="btn btn-primary">&#128197; Book a Free 15-Min Call</a>
      <a href="programs.html" class="btn btn-outline">See Our Programs</a>
    </div>
    <div class="art-panel">
      <img src="{IMG['art']}" alt="" />
      <div class="art-caption">Placeholder artwork &mdash; to be replaced with a commissioned piece from an Aboriginal artist. See note to Rhys below.</div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <h2 class="section-title">What We Do</h2>
    <p class="section-lead">IRAAC runs a small group of community programs and is building the governance and reporting systems that show funders and community alike that IRAAC is well run.</p>
    <div class="grid">
      <div class="card"><img src="{IMG['mcc']}" alt="" /><div class="card-body"><h3>MCC &mdash; Mob and Country Connections</h3><p>IRAAC supports other Aboriginal Community Organisations to build their own governance and reporting capability.</p><a class="card-link" href="programs.html#mcc">Learn more &rarr;</a></div></div>
      <div class="card"><img src="{IMG['youthscape']}" alt="" /><div class="card-body"><h3>YouthScape</h3><p>Connecting young people in the community with culture, opportunity and support.</p><a class="card-link" href="programs.html#youthscape">Learn more &rarr;</a></div></div>
      <div class="card"><img src="{IMG['thecrew']}" alt="" /><div class="card-body"><h3>The Crew</h3><p>A community-facing program building skills, connection and participation.</p><a class="card-link" href="programs.html#thecrew">Learn more &rarr;</a></div></div>
      <div class="card"><img src="{IMG['darc']}" alt="" /><div class="card-body"><h3>DARC</h3><p>Part of IRAAC's program suite, supporting community outcomes alongside our other programs.</p><a class="card-link" href="programs.html#darc">Learn more &rarr;</a></div></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="container two-col">
    <div>
      <h2 class="section-title">Governed Well, Reported Openly</h2>
      <p>IRAAC is building the systems that let it show &mdash; clearly and consistently &mdash; that it meets the governance and reporting standards expected by Local Decision Making, Aboriginal Affairs NSW, ORIC and other funding bodies.</p>
      <a href="governance.html" class="btn btn-primary">See Our Governance</a>
    </div>
    <img src="{IMG['governance']}" alt="" />
  </div>
</section>
"""

ABOUT = f"""
<section class="page-hero" style="background-image:url('{IMG['about']}');">
  <div class="container">
    <div class="eyebrow">About Us</div>
    <h1>Our Story</h1>
    <p>IRAAC is an Aboriginal Community Organisation and registered charity, working under the NSW Local Decision Making Framework.</p>
  </div>
</section>

<section>
  <div class="container two-col">
    <div>
      <h2 class="section-title">Who We Are</h2>
      <p>IRAAC represents and serves its community through a set of programs and a growing focus on governance and organisational capability. We are a charity, run by and for community &mdash; independent of government, though we work alongside Aboriginal Affairs NSW, Alliances and Assemblies to progress the priorities community identifies for itself.</p>
      <p>This page is a starting point &mdash; the Secretary and Board should expand it with IRAAC's founding story, the community and Country it represents, and the people who lead it.</p>
    </div>
    <img src="{IMG['office']}" alt="" />
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2 class="section-title">Local Decision Making, in Brief</h2>
    <p class="section-lead">Local Decision Making is the NSW framework that gives Aboriginal communities a stronger say in decisions that affect them, delivered through regional Alliances and Assemblies working with Aboriginal Affairs NSW. IRAAC's programs and governance work all sit within this framework.</p>
    <div class="grid">
      <div class="card"><div class="card-body"><h3>Aboriginal Affairs NSW</h3><p>The NSW Government agency responsible for Aboriginal affairs policy and the Local Decision Making Framework &mdash; IRAAC's government partner, not its owner.</p></div></div>
      <div class="card"><div class="card-body"><h3>Alliances &amp; Assemblies</h3><p>The regional, community-led structures through which priorities are identified under Local Decision Making.</p></div></div>
      <div class="card"><div class="card-body"><h3>ORIC &amp; ACNC</h3><p>The regulators IRAAC reports to as a registered Aboriginal Community Organisation and charity.</p></div></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <h2 class="section-title">Our Board</h2>
    <p class="section-lead">IRAAC is led by a Board of community members, meeting regularly using a standard agenda, minutes, decisions and actions framework so every meeting is run and recorded consistently.</p>
    <div class="grid">
      <div class="card"><div class="card-body"><h3>Geoff Maher</h3><p>Chairperson</p></div></div>
      <div class="card"><div class="card-body"><h3>Maria Maher</h3><p>Secretary</p></div></div>
    </div>
    <div class="note-box" style="margin-top:24px;">Add remaining Board Member names, photos and short bios here once confirmed &mdash; this builds trust with funders and community alike.</div>
  </div>
</section>
"""

def program_detail(key, tag, title, img, body):
    return f"""
<div class="program-block" id="{key}">
  <div class="program-hero">
    <img src="{img}" alt="" />
    <div><span class="tag">{tag}</span><h2>{title}</h2><p>{body}</p></div>
  </div>
  <div class="note-box">Add real photos, outcomes and stories for {title} here once available.</div>
</div>
"""

PROGRAMS = f"""
<section class="page-hero" style="background-image:url('{IMG['mcc']}');">
  <div class="container">
    <div class="eyebrow">What We Deliver</div>
    <h1>Our Programs</h1>
    <p>Four programs, each supporting community in a different way.</p>
  </div>
</section>

<section>
  <div class="container">
    {program_detail("mcc", "Sector Capability", "MCC &mdash; Mob and Country Connections", IMG['mcc'],
        "MCC is IRAAC's program for supporting other Aboriginal Community Organisations to build the governance, administration and reporting capability they need &mdash; sharing the systems, templates and training IRAAC has developed for itself. Support is provided at the invitation of the organisation receiving it, making it a peer&#8209;to&#8209;peer, relationship&#8209;based model rather than a top&#8209;down service. It's also a chance for IRAAC to test, in practice, whether this kind of Aboriginal&#8209;led, peer&#8209;to&#8209;peer capability building genuinely lifts outcomes for other organisations across the sector &mdash; and to refine the approach as it goes.")}
    {program_detail("youthscape", "Young People", "YouthScape", IMG['youthscape'],
        "YouthScape is IRAAC's program for young people in the community, connecting them with culture, opportunity and support. This section should be expanded with YouthScape's specific activities, age groups and outcomes.")}
    {program_detail("thecrew", "Community", "The Crew", IMG['thecrew'],
        "The Crew is a community-facing IRAAC program building skills, connection and participation. This section should be expanded with The Crew's specific activities and who it supports.")}
    {program_detail("darc", "Community", "DARC", IMG['darc'],
        "DARC is part of IRAAC's program suite, working alongside MCC, YouthScape and The Crew to support community outcomes. This section should be expanded with DARC's specific focus and activities.")}
  </div>
</section>
"""

GOVERNANCE = f"""
<section class="page-hero" style="background-image:url('{IMG['governance']}');">
  <div class="container">
    <div class="eyebrow">Accountability &amp; Transparency</div>
    <h1>Governance &amp; Reporting</h1>
    <p>IRAAC is a charity, independently governed by its Board &mdash; here's how we run ourselves and report to funders and regulators.</p>
  </div>
</section>

<section>
  <div class="container two-col">
    <div>
      <h2 class="section-title">How IRAAC is Governed</h2>
      <p>IRAAC is governed by a Board, chaired by the Chairperson and supported by the Secretary, meeting regularly using a standard agenda, minutes, decisions and actions framework.</p>
      <p>An annual independent Board evaluation process checks and improves IRAAC's governance every year, and Board Members, staff and community members all receive governance training relevant to their role.</p>
    </div>
    <div class="card"><div class="card-body">
      <h3>What We Report On</h3>
      <ul style="padding-left: 18px; color: var(--muted); margin:0;">
        <li>Quarterly progress reports</li><li>Annual reports</li><li>Program acquittals</li>
        <li>Audit reports</li><li>ORIC &amp; ACNC reports</li><li>Funding body reports</li>
      </ul>
    </div></div>
  </div>
</section>

<section>
  <div class="container">
    <h2 class="section-title">The Wider System IRAAC Works Within</h2>
    <p class="section-lead">IRAAC doesn't operate in isolation &mdash; it sits inside a wider network of government partners, regulators and community structures. Understanding how these fit together helps explain why IRAAC reports the way it does, and who it's ultimately accountable to.</p>

    <div class="system-block">
      <span class="system-kicker">Policy Framework</span>
      <h3>OCHRE &amp; Local Decision Making</h3>
      <p>OCHRE is the NSW Government's overarching policy framework for Aboriginal affairs, and Local Decision Making (LDM) is the specific part of that framework designed to give Aboriginal communities a stronger say in decisions that affect them. Rather than government deciding priorities on communities' behalf, LDM is meant to shift that decision&#8209;making outward, through structures like Alliances and Assemblies, so that Aboriginal people set the agenda for their own communities.</p>
      <p>Every other entity on this page &mdash; IRAAC included &mdash; sits somewhere inside this framework. It's the shared backdrop that explains why IRAAC reports the way it does, who it's accountable to, and why building strong governance and reporting capability matters so much: it's what lets IRAAC show, clearly, that it can be trusted with more local decision&#8209;making authority over time.</p>
    </div>

    <div class="system-block">
      <span class="system-kicker">Government Partner</span>
      <h3>Aboriginal Affairs NSW</h3>
      <p>Aboriginal Affairs NSW is the NSW Government agency responsible for Aboriginal affairs policy, and the government partner IRAAC ultimately reports up to. It holds Ministerial advice, funding assurance and compliance oversight responsibilities across the OCHRE and Local Decision Making framework, and works alongside Aboriginal Community Organisations like IRAAC rather than directing them day to day.</p>
      <p>It's important to be clear about what this relationship is and isn't: Aboriginal Affairs NSW is IRAAC's government partner and one of its funders, not its owner. IRAAC remains an independent, community&#8209;governed organisation that reports to Aboriginal Affairs NSW on how it uses public funding and what outcomes it delivers, in the same way any funded charity reports to government.</p>
    </div>

    <div class="system-block">
      <span class="system-kicker is-emerging">Emerging &middot; Not Yet Established</span>
      <h3>NCARA</h3>
      <p>NCARA is a proposed statewide Aboriginal coordinating structure that has been discussed as a way of connecting Aboriginal Affairs NSW with the regional Alliances and Assemblies described below. The idea is coordination, shared learning and a stronger collective voice across the sector &mdash; not direct control over any individual organisation's funding or decisions.</p>
      <p>NCARA's exact role is still being worked through, and IRAAC doesn't have a settled relationship with it yet. We've included it here for completeness, because it comes up often in sector&#8209;wide conversations about how Local Decision Making could be organised in future &mdash; but it should be read as an idea under discussion, not an established part of how IRAAC currently operates.</p>
    </div>

    <div class="system-block">
      <span class="system-kicker">Regional Participation</span>
      <h3>Alliances &amp; Assemblies</h3>
      <p>Alliances and Assemblies are the regional structures through which Local Decision Making actually happens on the ground. Alliances are regional Aboriginal governance structures that support engagement, priority&#8209;setting and planning across a region. Assemblies are community forums that support local participation, so that the priorities an Alliance takes forward genuinely reflect what community members themselves have said matters to them.</p>
      <p>Together, they're the participatory architecture that gives Local Decision Making its meaning &mdash; the channel through which Aboriginal communities identify their own priorities, rather than having them set from Sydney or Canberra. IRAAC works alongside its regional Alliance and Assembly to make sure its own programs and priorities stay grounded in what community has actually said it needs.</p>
    </div>

    <div class="system-block">
      <span class="system-kicker">Corporate Regulator</span>
      <h3>ORIC &mdash; Office of the Registrar of Indigenous Corporations</h3>
      <p>ORIC is the national regulator for Aboriginal and Torres Strait Islander corporations, and it's one of two regulators IRAAC reports to as a registered Aboriginal Community Organisation. ORIC's focus is corporate governance and compliance &mdash; making sure organisations like IRAAC are run properly under the rules that apply to Indigenous corporations specifically, separately from the Local Decision Making relationship with Aboriginal Affairs NSW.</p>
      <p>IRAAC's Board Members and staff receive training on ORIC's expectations as part of building the organisation's governance capability, and ORIC reporting sits alongside quarterly reports, annual reports and audits as one of the regular compliance obligations IRAAC keeps on top of.</p>
    </div>

    <div class="system-block">
      <span class="system-kicker">Charity Regulator</span>
      <h3>ACNC &mdash; Australian Charities and Not-for-profits Commission</h3>
      <p>ACNC is the federal regulator for Australian charities, and the second of the two regulators IRAAC reports to &mdash; this time covering IRAAC's obligations as a registered charity rather than as a corporation. Where ORIC looks at corporate compliance, ACNC looks at charitable purpose, governance standards and public accountability.</p>
      <p>Because IRAAC needs to satisfy both regulators at once, its reporting calendar and governance training are built to cover ORIC and ACNC requirements together, rather than treating them as two separate, unrelated obligations. Meeting both consistently is one of the clearest, most concrete ways IRAAC can demonstrate good governance to funders.</p>
    </div>

    <div class="system-block">
      <span class="system-kicker">Capability Partner</span>
      <h3>Governance &amp; Capability Support</h3>
      <p>Building all of the above into everyday practice &mdash; digital systems, board reporting, training, external reporting, financial procedures and on&#8209;the&#8209;job capability development &mdash; is ongoing work. IRAAC draws on external governance and capability advisors to help design and embed these systems, so that good governance becomes something the organisation runs day to day, not just something it demonstrates when a report is due.</p>
    </div>
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2 class="section-title">Reports &amp; Policies</h2>
    <p class="section-lead">Publicly appropriate reports and key policies will be listed here as they're confirmed for release.</p>
    <div class="grid">
      <div class="card"><div class="card-body"><h3>Annual Report</h3><p>Add a link once available.</p></div></div>
      <div class="card"><div class="card-body"><h3>Board Charter</h3><p>Add a link once confirmed for public release.</p></div></div>
      <div class="card"><div class="card-body"><h3>Strategic Plan</h3><p>Add a link once available.</p></div></div>
    </div>
    <div class="note-box">These documents should only be published once the Secretary and Board have confirmed they're appropriate for public release.</div>
  </div>
</section>
"""

SUPPORT = f"""
<section class="page-hero" style="background-image:url('{IMG['support']}');">
  <div class="container">
    <div class="eyebrow">MCC Program</div>
    <h1>Supporting Other Aboriginal Community Organisations</h1>
    <p>IRAAC shares the systems, templates and training it has built for its own governance, administration and reporting.</p>
  </div>
</section>

<section>
  <div class="container two-col">
    <div>
      <h2 class="section-title">How It Works</h2>
      <p>Support is offered at your organisation's invitation &mdash; IRAAC doesn't impose a model, it shares one, and works alongside your organisation until it can manage its own administration, governance and reporting with confidence.</p>
    </div>
    <div class="card"><div class="card-body">
      <h3>What's on Offer</h3>
      <ul style="padding-left: 18px; color: var(--muted); margin:0;">
        <li>Digital office set up and training</li><li>Board reporting templates</li>
        <li>Governance training and evaluation</li><li>External reporting frameworks</li>
        <li>On&#8209;the&#8209;job capability support</li>
      </ul>
    </div></div>
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2 class="section-title">Reach Out</h2>
    <p class="section-lead">If your organisation is interested in MCC support, get in touch and IRAAC will follow up.</p>
    <a href="contact.html" class="btn btn-primary">Contact IRAAC</a>
  </div>
</section>
"""

NEWS = f"""
<section class="page-hero" style="background-image:url('{IMG['news1']}');">
  <div class="container">
    <div class="eyebrow">Updates</div>
    <h1>News &amp; Updates</h1>
    <p>Short updates on IRAAC's programs, governance milestones and community news.</p>
  </div>
</section>

<section>
  <div class="container" style="max-width: 780px;">
    <div class="news-item"><img src="{IMG['news1']}" alt="" /><div><div class="date">Placeholder</div><h3>Website launched</h3><p>This is a placeholder update &mdash; replace it with IRAAC's first real news post.</p></div></div>
    <div class="news-item"><img src="{IMG['news2']}" alt="" /><div><div class="date">Placeholder</div><h3>Add your next update here</h3><p>Use this space for programme milestones, funding news, events or governance updates.</p></div></div>
  </div>
</section>
"""

CONTACT = f"""
<section class="page-hero" style="background-image:url('{IMG['office']}');">
  <div class="container">
    <div class="eyebrow">Get in Touch</div>
    <h1>Contact IRAAC</h1>
    <p>There's no wrong door &mdash; reach us however suits you best.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="contact-grid" style="margin-bottom: 48px;">
      <div class="contact-card"><div class="icon">&#128203;</div><h3>Complete a Survey</h3><p>Tell us a bit about what you need and we'll follow up.</p><a class="btn btn-primary" style="margin:0;" href="survey.html">Start Survey</a></div>
      <div class="contact-card"><div class="icon">&#127968;</div><h3>Visit a Local Office</h3><p>Drop in and speak with your local IRAAC officer in person.</p><a class="btn btn-primary" style="margin:0;" href="offices.html">Find an Office</a></div>
      <div class="contact-card" id="home-visit"><div class="icon">&#128100;</div><h3>Request a Home Visit</h3><p>Ask an IRAAC officer to come to you, at a time that works.</p><a class="btn btn-primary" style="margin:0;" href="#home-visit-form">Request a Visit</a></div>
      <div class="contact-card"><div class="icon">&#128197;</div><h3>Book a Call</h3><p>Pick a time that suits you &mdash; we'll call you.</p><a class="btn btn-primary" style="margin:0;" href="book-a-call.html">Book a Time</a></div>
    </div>

    <div class="two-col">
      <div>
        <h2 class="section-title">Who to Contact</h2>
        <ul style="list-style:none;padding:0;margin:0;">
          <li style="padding:16px 0;border-bottom:1px solid rgba(0,0,0,0.08);"><b style="color:var(--ochre-dark);display:block;">General Enquiries</b>Add general contact email / phone here.</li>
          <li style="padding:16px 0;border-bottom:1px solid rgba(0,0,0,0.08);"><b style="color:var(--ochre-dark);display:block;">Program Enquiries</b>Add program contact details here.</li>
          <li style="padding:16px 0;border-bottom:1px solid rgba(0,0,0,0.08);"><b style="color:var(--ochre-dark);display:block;">MCC &amp; Partnership Enquiries</b>Add MCC contact details for other Aboriginal Community Organisations.</li>
        </ul>
      </div>
      <div class="card" id="home-visit-form"><div class="card-body">
        <h3>Send a Message / Request a Home Visit</h3>
        <form class="contact-form">
          <div><label for="name">Name</label><input type="text" id="name" required /></div>
          <div><label for="email">Email</label><input type="email" id="email" required /></div>
          <div><label for="message">Message</label><textarea id="message" rows="4" required placeholder="Let us know if you'd like an IRAAC officer to visit you at home, and a good time to reach you."></textarea></div>
          <button type="submit" class="btn btn-primary" style="margin-top:4px;">Send Message</button>
          <p id="form-note" style="display:none; color: var(--muted); font-size: 0.88rem;"></p>
        </form>
      </div></div>
    </div>
  </div>
</section>
"""

SURVEY = f"""
<section class="page-hero" style="background-image:url('{IMG['support']}');">
  <div class="container">
    <div class="eyebrow">Tell Us About You</div>
    <h1>Complete a Survey</h1>
    <p>This short survey helps IRAAC understand who's reaching out and connect you with the right support. It takes about two minutes.</p>
  </div>
</section>

<section>
  <div class="container">
    <div id="survey-form-wrap">
    <form class="survey-shell" id="iraac-survey">
      <div class="survey-step-label">Step 1 of 1 &middot; About You</div>

      <div class="q-block">
        <label class="q-title">What age group are you in?</label>
        <div class="option-row">
          <label class="option-pill"><input type="radio" name="age" value="under18" /> Under 18</label>
          <label class="option-pill"><input type="radio" name="age" value="18-24" /> 18&ndash;24</label>
          <label class="option-pill"><input type="radio" name="age" value="25-44" /> 25&ndash;44</label>
          <label class="option-pill"><input type="radio" name="age" value="45-64" /> 45&ndash;64</label>
          <label class="option-pill"><input type="radio" name="age" value="65plus" /> 65+</label>
          <label class="option-pill"><input type="radio" name="age" value="prefer-not" /> Prefer not to say</label>
        </div>
      </div>

      <div class="q-block">
        <label class="q-title">Do you identify as Aboriginal and/or Torres Strait Islander?</label>
        <p class="q-help">This helps IRAAC understand who it's reaching. It's always your choice whether to answer.</p>
        <div class="option-row">
          <label class="option-pill"><input type="radio" name="identity" value="aboriginal" /> Aboriginal</label>
          <label class="option-pill"><input type="radio" name="identity" value="torres-strait" /> Torres Strait Islander</label>
          <label class="option-pill"><input type="radio" name="identity" value="both" /> Both Aboriginal and Torres Strait Islander</label>
          <label class="option-pill"><input type="radio" name="identity" value="neither" /> Neither</label>
          <label class="option-pill"><input type="radio" name="identity" value="prefer-not" /> Prefer not to say</label>
        </div>
      </div>

      <div class="q-block">
        <label class="q-title" for="ethnicity">Ethnicity or cultural background (optional)</label>
        <p class="q-help">Only answer if you're comfortable &mdash; this is entirely optional.</p>
        <input type="text" id="ethnicity" name="ethnicity" placeholder="e.g. a specific community, nation or cultural background" style="width:100%;padding:12px 14px;border:1px solid rgba(0,0,0,0.15);border-radius:4px;font-size:0.95rem;font-family:inherit;" />
      </div>

      <div class="q-block">
        <label class="q-title" for="religion">Religion or spiritual belief (optional)</label>
        <p class="q-help">Only answer if you're comfortable &mdash; this is entirely optional.</p>
        <input type="text" id="religion" name="religion" style="width:100%;padding:12px 14px;border:1px solid rgba(0,0,0,0.15);border-radius:4px;font-size:0.95rem;font-family:inherit;" />
      </div>

      <div class="q-block">
        <label class="q-title">What would you like help with?</label>
        <div class="option-row">
          <label class="option-pill"><input type="checkbox" name="need" value="programs" /> Our programs (MCC, YouthScape, The Crew, DARC)</label>
          <label class="option-pill"><input type="checkbox" name="need" value="governance" /> Governance / MCC support for my organisation</label>
          <label class="option-pill"><input type="checkbox" name="need" value="general" /> General information</label>
          <label class="option-pill"><input type="checkbox" name="need" value="other" /> Something else</label>
        </div>
      </div>

      <div class="consent-box">
        This is a demonstration survey. Your answers are not being stored or sent anywhere yet. Once IRAAC is ready to launch it, this note will be replaced with a proper privacy statement explaining exactly how your information is collected, stored and used, in line with the Privacy Act and community expectations around sensitive information such as Indigenous status, ethnicity and religion.
      </div>

      <button type="submit" class="btn btn-primary" style="margin-top:20px;">Submit Survey</button>
    </form>
    <div id="survey-thanks" class="survey-shell" style="display:none;">
      <h2 class="section-title" style="margin-top:0;">Thank you</h2>
      <p>Thanks for completing the survey. In the live version, an IRAAC officer would follow up based on what you told us. In the meantime, you're welcome to <a href="book-a-call.html" style="color:var(--ochre);font-weight:600;">book a free 15&#8209;minute call</a> or <a href="offices.html" style="color:var(--ochre);font-weight:600;">visit a local office</a>.</p>
    </div>
    </div>
  </div>
</section>
"""

OFFICES = f"""
<section class="page-hero" style="background-image:url('{IMG['office']}');">
  <div class="container">
    <div class="eyebrow">In Person</div>
    <h1>Visit a Local Office</h1>
    <p>Drop in and speak with an IRAAC officer face to face. Locations below are placeholders &mdash; real office addresses need to be added by the Secretary.</p>
  </div>
</section>

<section>
  <div class="container">
    <iframe class="map-embed" loading="lazy" src="https://www.openstreetmap.org/export/embed.html?bbox=140.9%2C-37.6%2C153.6%2C-28.1&amp;layer=mapnik&amp;marker=-33.8,151.2" title="Map of placeholder IRAAC office locations across NSW"></iframe>
    <div class="note-box" style="margin-top:18px;">This map and the office list below use placeholder locations so the page can be reviewed. Please confirm IRAAC's real office addresses (and whether IRAAC's remit is NSW-wide or a specific region) so they can be added &mdash; and so the map can be centred correctly.</div>

    <div class="office-list">
      <div class="office-item"><div><h4>Placeholder Office &mdash; Sydney / Metro</h4><p>Address to be confirmed &middot; Open weekdays</p></div><a class="btn btn-outline" style="margin:0;color:var(--ochre-dark);border-color:var(--ochre-dark);" href="book-a-call.html">Book Ahead</a></div>
      <div class="office-item"><div><h4>Placeholder Office &mdash; Regional NSW</h4><p>Address to be confirmed &middot; Open weekdays</p></div><a class="btn btn-outline" style="margin:0;color:var(--ochre-dark);border-color:var(--ochre-dark);" href="book-a-call.html">Book Ahead</a></div>
      <div class="office-item"><div><h4>Placeholder Office &mdash; Additional Location</h4><p>Address to be confirmed &middot; Open weekdays</p></div><a class="btn btn-outline" style="margin:0;color:var(--ochre-dark);border-color:var(--ochre-dark);" href="book-a-call.html">Book Ahead</a></div>
    </div>
  </div>
</section>
"""

BOOKCALL = f"""
<section class="page-hero" style="background-image:url('{IMG['governance']}');">
  <div class="container">
    <div class="eyebrow">Free &middot; 15 Minutes &middot; No Obligation</div>
    <h1>Book a Free 15-Minute Call</h1>
    <p>Speak with an experienced IRAAC officer about anything &mdash; a program, a governance question, or just to find out more. Open to community members, other organisations and government contacts alike.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="call-card">
      <span class="duration">&#9200; 15 minutes &middot; Free</span>
      <h2 class="section-title" style="margin-top:0;">Pick a Time</h2>
      <p style="color:var(--muted);">This call will be booked through Calendly once IRAAC provides a scheduling link. For now, this is a placeholder so the flow can be reviewed end to end.</p>
      <div class="note-box">Calendly embed goes here &mdash; please share the IRAAC officer's Calendly link (or set one up) and it will be embedded directly on this page so visitors can pick a time without leaving the site.</div>
      <a href="contact.html" class="btn btn-primary">Request a Call Instead</a>
    </div>
  </div>
</section>
"""

pages = [
    ("index.html", "Home", "IRAAC supports Aboriginal community, culture and self-determination through Local Decision Making.", "index.html", INDEX),
    ("about.html", "Our Story", "Who IRAAC is and how it fits within the NSW Local Decision Making Framework.", "about.html", ABOUT),
    ("programs.html", "Our Programs", "MCC, YouthScape, The Crew and DARC — IRAAC's community programs.", "programs.html", PROGRAMS),
    ("governance.html", "Governance & Reporting", "How IRAAC is governed and how it reports to funders and regulators.", "governance.html", GOVERNANCE),
    ("support.html", "Supporting Other Organisations", "How IRAAC supports other Aboriginal Community Organisations through MCC.", "support.html", SUPPORT),
    ("news.html", "News", "Latest updates from IRAAC.", "news.html", NEWS),
    ("contact.html", "Contact", "Get in touch with IRAAC.", "contact.html", CONTACT),
    ("survey.html", "Complete a Survey", "A short survey to help IRAAC connect you with the right support.", "contact.html", SURVEY),
    ("offices.html", "Visit a Local Office", "Find an IRAAC office to visit in person.", "contact.html", OFFICES),
    ("book-a-call.html", "Book a Free 15-Minute Call", "Book a free 15-minute call with an experienced IRAAC officer.", "contact.html", BOOKCALL),
]

import os
OUT = os.path.dirname(os.path.abspath(__file__))
for filename, title, desc, active, body in pages:
    with open(os.path.join(OUT, filename), "w") as f:
        f.write(page(title, desc, active, body))

print("Built", len(pages), "pages")
