import os

OUT = os.path.dirname(os.path.abspath(__file__))

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
    <nav class="main-nav">
      <ul>
        {links}
      </ul>
    </nav>
  </div>
</header>
"""

FOOTER = """<div class="acknowledgement">
  <div class="container">
    IRAAC acknowledges the Traditional Custodians of the lands on which we work, live and gather, and pays respect to Elders past, present and emerging.
  </div>
</div>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <h4>IRAAC</h4>
        <ul>
          <li><a href="about.html">Our Story</a></li>
          <li><a href="governance.html">Governance &amp; Reporting</a></li>
          <li><a href="contact.html">Contact Us</a></li>
        </ul>
      </div>
      <div>
        <h4>Our Programs</h4>
        <ul>
          <li><a href="programs.html#mcc">MCC &mdash; Mob and Country Connections</a></li>
          <li><a href="programs.html#youthscape">YouthScape</a></li>
          <li><a href="programs.html#thecrew">The Crew</a></li>
          <li><a href="programs.html#darc">DARC</a></li>
        </ul>
      </div>
      <div>
        <h4>Get Involved</h4>
        <ul>
          <li><a href="support.html">Support for Aboriginal Community Organisations</a></li>
          <li><a href="news.html">Latest Updates</a></li>
          <li><a href="contact.html">Get in Touch</a></li>
        </ul>
      </div>
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
<link rel="stylesheet" href="css/style.css" />
</head>
<body>
{header(active)}
{body}
{FOOTER}
<script src="js/main.js"></script>
</body>
</html>
"""

# ---------------------------------------------------------------------------
# INDEX
# ---------------------------------------------------------------------------
index_body = """
<section class="hero">
  <div class="container">
    <div class="eyebrow">Local Decision Making &middot; Aboriginal Community Organisation</div>
    <h1>Strong governance. Strong programs. Strong community.</h1>
    <p>IRAAC supports Aboriginal community, culture and self&#8209;determination through Local Decision Making &mdash; delivering programs, building governance capability, and helping other Aboriginal Community Organisations do the same.</p>
    <a href="programs.html" class="btn btn-primary">Explore Our Programs</a>
    <a href="contact.html" class="btn btn-outline">Get in Touch</a>
  </div>
</section>

<section>
  <div class="container">
    <h2 class="section-title">What We Do</h2>
    <p class="section-lead">IRAAC runs a small group of community programs and is building the governance, reporting and administrative systems that prove strong, accountable leadership to funders, government and community alike.</p>
    <div class="grid">
      <div class="card">
        <h3>MCC &mdash; Mob and Country Connections</h3>
        <p>IRAAC supports other Aboriginal Community Organisations to build their own governance, administration and reporting capability, organisation to organisation.</p>
        <a class="card-link" href="programs.html#mcc">Learn more &rarr;</a>
      </div>
      <div class="card">
        <h3>YouthScape</h3>
        <p>A program focused on young people in the community &mdash; connecting them with culture, opportunity and support.</p>
        <a class="card-link" href="programs.html#youthscape">Learn more &rarr;</a>
      </div>
      <div class="card">
        <h3>The Crew</h3>
        <p>A community-facing program building skills, connection and participation.</p>
        <a class="card-link" href="programs.html#thecrew">Learn more &rarr;</a>
      </div>
      <div class="card">
        <h3>DARC</h3>
        <p>Part of IRAAC's program suite, supporting community outcomes alongside MCC, YouthScape and The Crew.</p>
        <a class="card-link" href="programs.html#darc">Learn more &rarr;</a>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="container two-col">
    <div>
      <h2 class="section-title">Governed Well, Reported Openly</h2>
      <p>IRAAC is building the systems that let it show &mdash; clearly and consistently &mdash; that it meets the governance, reporting and administration standards expected by Local Decision Making, Aboriginal Affairs NSW, ORIC and other funding bodies.</p>
      <p>That means a standing Board reporting framework, an annual independent Board evaluation, and a clear external reporting calendar covering quarterly reports, acquittals and audits.</p>
      <a href="governance.html" class="btn btn-primary" style="margin-top: 6px;">See Our Governance</a>
    </div>
    <div class="card">
      <h3>Why it matters</h3>
      <p>Stronger Aboriginal Community Organisations produce better reporting, better financial management, better accountability and better Local Decision Making outcomes &mdash; for IRAAC and for the organisations IRAAC supports through MCC.</p>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <h2 class="section-title">Supporting the Wider Sector</h2>
    <p class="section-lead">Through the MCC Program, IRAAC works alongside other Aboriginal Community Organisations &mdash; at their invitation &mdash; to share the systems, templates and training IRAAC has already built for itself.</p>
    <a href="support.html" class="btn btn-primary">How We Support Other Organisations</a>
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------
about_body = """
<section class="page-hero">
  <div class="container">
    <div class="eyebrow">About Us</div>
    <h1>Our Story</h1>
    <p>IRAAC is an Aboriginal Community Organisation operating under the NSW Local Decision Making Framework, working to strengthen community, culture and self&#8209;determination.</p>
  </div>
</section>

<section>
  <div class="container two-col">
    <div>
      <h2 class="section-title">Who We Are</h2>
      <p>IRAAC represents and serves its community through a set of programs and a growing focus on governance and organisational capability. IRAAC operates within the NSW Local Decision Making (LDM) system, working alongside Aboriginal Affairs NSW, Alliances and Assemblies to progress the priorities identified by community.</p>
      <p>This page is a starting point &mdash; the Secretary and Board should expand it with IRAAC's founding story, the community and Country it represents, and the people who lead it.</p>

      <h2 class="section-title" style="margin-top: 40px;">Local Decision Making, in Brief</h2>
      <p>Local Decision Making is the NSW framework that gives Aboriginal communities a stronger say in decisions that affect them, delivered through regional Alliances and Assemblies working with Aboriginal Affairs NSW and the broader Accord arrangements. IRAAC's programs and governance work all sit within this framework, and are part of how IRAAC demonstrates it is ready to take on more responsibility within it.</p>
    </div>
    <div class="card">
      <h3>Our Board</h3>
      <p>IRAAC is led by a Board of community members, chaired by the Chairperson and supported by the Secretary. A full list of current Board Members should be added here, along with a short note on how Board Members are elected or appointed.</p>
      <div class="note-box">Add Board Member names, photos and short bios here once confirmed &mdash; this builds trust with funders and community alike.</div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2 class="section-title">Where We Sit</h2>
    <p class="section-lead">IRAAC's programs and governance work connect to the wider Aboriginal Affairs NSW and Local Decision Making system.</p>
    <div class="grid">
      <div class="card">
        <h3>Aboriginal Affairs NSW</h3>
        <p>The NSW Government agency responsible for Aboriginal affairs policy, OCHRE and the Local Decision Making Framework.</p>
      </div>
      <div class="card">
        <h3>Alliances &amp; Assemblies</h3>
        <p>The regional structures through which community priorities are identified and progressed under Local Decision Making.</p>
      </div>
      <div class="card">
        <h3>ORIC &amp; ACNC</h3>
        <p>The regulators IRAAC reports to as a registered Aboriginal Community Organisation, covering corporate and charity compliance.</p>
      </div>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# PROGRAMS
# ---------------------------------------------------------------------------
programs_body = """
<section class="page-hero">
  <div class="container">
    <div class="eyebrow">What We Deliver</div>
    <h1>Our Programs</h1>
    <p>IRAAC runs four programs that support community, culture, young people and organisational capability across the sector.</p>
  </div>
</section>

<section>
  <div class="container">

    <div class="program-block" id="mcc">
      <span class="tag">Sector Capability</span>
      <h2>MCC &mdash; Mob and Country Connections</h2>
      <p>MCC is IRAAC's program for supporting other Aboriginal Community Organisations to build the governance, administration and reporting capability they need &mdash; sharing the systems, templates and training IRAAC has developed for itself. Support is provided at the invitation of the organisation receiving it, making it a peer&#8209;to&#8209;peer, relationship&#8209;based model rather than a top&#8209;down service.</p>
      <div class="note-box">Add specific MCC achievements, partner organisations and outcomes here once available.</div>
    </div>

    <div class="program-block" id="youthscape">
      <span class="tag">Young People</span>
      <h2>YouthScape</h2>
      <p>YouthScape is IRAAC's program for young people in the community, connecting them with culture, opportunity and support. This section should be expanded with YouthScape's specific activities, age groups and outcomes.</p>
      <div class="note-box">Add YouthScape program details, activities and outcomes here once available.</div>
    </div>

    <div class="program-block" id="thecrew">
      <span class="tag">Community</span>
      <h2>The Crew</h2>
      <p>The Crew is a community-facing IRAAC program building skills, connection and participation. This section should be expanded with The Crew's specific activities and who it supports.</p>
      <div class="note-box">Add The Crew program details, activities and outcomes here once available.</div>
    </div>

    <div class="program-block" id="darc">
      <span class="tag">Community</span>
      <h2>DARC</h2>
      <p>DARC is part of IRAAC's program suite, working alongside MCC, YouthScape and The Crew to support community outcomes. This section should be expanded with DARC's specific focus and activities.</p>
      <div class="note-box">Add DARC program details, activities and outcomes here once available.</div>
    </div>

  </div>
</section>

<section class="alt">
  <div class="container">
    <h2 class="section-title">Funded Through</h2>
    <p class="section-lead">IRAAC's programs are supported through Local Decision Making and Aboriginal Affairs NSW funding arrangements, with governance and capability work built into each program budget.</p>
    <a href="governance.html" class="btn btn-primary">See How We Report</a>
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# GOVERNANCE
# ---------------------------------------------------------------------------
governance_body = """
<section class="page-hero">
  <div class="container">
    <div class="eyebrow">Accountability &amp; Transparency</div>
    <h1>Governance &amp; Reporting</h1>
    <p>IRAAC is building consistent, evidence-based governance and reporting systems &mdash; so funders, regulators and community can see, clearly, that IRAAC is well run.</p>
  </div>
</section>

<section>
  <div class="container two-col">
    <div>
      <h2 class="section-title">How IRAAC is Governed</h2>
      <p>IRAAC is governed by a Board, chaired by the Chairperson and supported by the Secretary, meeting regularly using a standard agenda, minutes, decisions and actions framework. This consistency makes it easier for the Board to track decisions and easier for IRAAC to prove &mdash; to Aboriginal Affairs NSW, ORIC, ACNC and other funders &mdash; that governance is being taken seriously.</p>
      <p>An annual independent Board evaluation process checks and improves IRAAC's governance every year, and Board Members, staff and community members all receive governance training relevant to their role.</p>
    </div>
    <div class="card">
      <h3>What We Report On</h3>
      <ul style="padding-left: 18px; color: var(--muted);">
        <li>Quarterly progress reports</li>
        <li>Annual reports</li>
        <li>Program acquittals</li>
        <li>Audit reports</li>
        <li>ORIC reports</li>
        <li>ACNC reports</li>
        <li>Funding body reports</li>
      </ul>
    </div>
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2 class="section-title">Reports &amp; Policies</h2>
    <p class="section-lead">Publicly appropriate reports and key policies will be listed here as they're confirmed for release.</p>
    <div class="grid">
      <div class="card">
        <h3>Annual Report</h3>
        <p>Add a link to IRAAC's most recent annual report once available.</p>
      </div>
      <div class="card">
        <h3>Board Charter</h3>
        <p>Add a link to IRAAC's Board Charter or governance policy once confirmed for public release.</p>
      </div>
      <div class="card">
        <h3>Strategic Plan</h3>
        <p>Add a link to IRAAC's current strategic plan once available.</p>
      </div>
    </div>
    <div class="note-box">These documents should only be published once the Secretary and Board have confirmed they're appropriate for public release.</div>
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# SUPPORT
# ---------------------------------------------------------------------------
support_body = """
<section class="page-hero">
  <div class="container">
    <div class="eyebrow">MCC Program</div>
    <h1>Supporting Other Aboriginal Community Organisations</h1>
    <p>IRAAC shares the systems, templates and training it has built for its own governance, administration and reporting &mdash; helping other Aboriginal Community Organisations build the same capability.</p>
  </div>
</section>

<section>
  <div class="container two-col">
    <div>
      <h2 class="section-title">How It Works</h2>
      <p>Support is offered at your organisation's invitation &mdash; IRAAC doesn't impose a model, it shares one, and works alongside your organisation until it can manage its own administration, governance and reporting with confidence.</p>
      <p>This can include a digital office setup, board reporting templates, governance training, external reporting frameworks, financial and operational procedures, and practical on&#8209;the&#8209;job support &mdash; delivered remotely or on site, for as long as it's useful.</p>
    </div>
    <div class="card">
      <h3>What's on Offer</h3>
      <ul style="padding-left: 18px; color: var(--muted);">
        <li>Digital office set up and training</li>
        <li>Board reporting templates</li>
        <li>Governance training and evaluation</li>
        <li>External reporting frameworks</li>
        <li>Financial and operational procedures</li>
        <li>On&#8209;the&#8209;job capability support</li>
      </ul>
    </div>
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2 class="section-title">Reach Out</h2>
    <p class="section-lead">If your organisation is interested in MCC support, get in touch and IRAAC will follow up to talk through what's needed.</p>
    <a href="contact.html" class="btn btn-primary">Contact IRAAC</a>
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# NEWS
# ---------------------------------------------------------------------------
news_body = """
<section class="page-hero">
  <div class="container">
    <div class="eyebrow">Updates</div>
    <h1>News &amp; Updates</h1>
    <p>Short updates on IRAAC's programs, governance milestones and community news.</p>
  </div>
</section>

<section>
  <div class="container" style="max-width: 780px;">

    <div class="news-item">
      <div class="date">Placeholder</div>
      <h3>Website launched</h3>
      <p>This is a placeholder update &mdash; replace it with IRAAC's first real news post. Updates don't need to be long; a few sentences written the way IRAAC would update its Board is enough.</p>
    </div>

    <div class="news-item">
      <div class="date">Placeholder</div>
      <h3>Add your next update here</h3>
      <p>Use this space for programme milestones, funding news, events or governance updates as they happen.</p>
    </div>

  </div>
</section>
"""

# ---------------------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------------------
contact_body = """
<section class="page-hero">
  <div class="container">
    <div class="eyebrow">Get in Touch</div>
    <h1>Contact IRAAC</h1>
    <p>Reach out for general enquiries, program questions, media requests, or MCC partnership enquiries from other Aboriginal Community Organisations.</p>
  </div>
</section>

<section>
  <div class="container two-col">
    <div>
      <h2 class="section-title">Who to Contact</h2>
      <ul class="contact-list">
        <li><span class="role">General Enquiries</span>Add general contact email / phone here.</li>
        <li><span class="role">Program Enquiries</span>Add program contact details here.</li>
        <li><span class="role">MCC &amp; Partnership Enquiries</span>Add MCC contact details here for other Aboriginal Community Organisations.</li>
        <li><span class="role">Media</span>Add media contact details here.</li>
      </ul>
    </div>
    <div class="card">
      <h3>Send a Message</h3>
      <form class="contact-form">
        <div>
          <label for="name">Name</label>
          <input type="text" id="name" name="name" required />
        </div>
        <div>
          <label for="email">Email</label>
          <input type="email" id="email" name="email" required />
        </div>
        <div>
          <label for="reason">Reason for contact</label>
          <select id="reason" name="reason">
            <option>General enquiry</option>
            <option>Program enquiry</option>
            <option>MCC / partnership enquiry</option>
            <option>Media</option>
          </select>
        </div>
        <div>
          <label for="message">Message</label>
          <textarea id="message" name="message" rows="4" required></textarea>
        </div>
        <button type="submit" class="btn btn-primary" style="margin-top: 4px;">Send Message</button>
        <p id="form-note" style="display:none; color: var(--muted); font-size: 0.88rem;"></p>
      </form>
    </div>
  </div>
</section>
"""

pages = [
    ("index.html", "Home", "IRAAC supports Aboriginal community, culture and self-determination through Local Decision Making.", "index.html", index_body),
    ("about.html", "Our Story", "Who IRAAC is and how it fits within the NSW Local Decision Making Framework.", "about.html", about_body),
    ("programs.html", "Our Programs", "MCC, YouthScape, The Crew and DARC — IRAAC's community programs.", "programs.html", programs_body),
    ("governance.html", "Governance & Reporting", "How IRAAC is governed and how it reports to funders and regulators.", "governance.html", governance_body),
    ("support.html", "Supporting Other Organisations", "How IRAAC supports other Aboriginal Community Organisations through MCC.", "support.html", support_body),
    ("news.html", "News", "Latest updates from IRAAC.", "news.html", news_body),
    ("contact.html", "Contact", "Get in touch with IRAAC.", "contact.html", contact_body),
]

for filename, title, desc, active, body in pages:
    with open(os.path.join(OUT, filename), "w") as f:
        f.write(page(title, desc, active, body))

print("Built", len(pages), "pages")
