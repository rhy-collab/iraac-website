# IRAAC Website

A working draft of a public website for IRAAC, covering the organisation, its programs (MCC, YouthScape, The Crew, DARC), governance and reporting, MCC support for other Aboriginal Community Organisations, news and contact details.

This is a plain static site (HTML/CSS/JS, no build step) so it's easy to edit and deploys directly on Vercel with zero configuration.

## Editing

Each page is a standalone HTML file generated from `build.py`. To make sitewide changes (e.g. nav links, footer), edit `build.py` and run:

```
python3 build.py
```

To change styling, edit `css/style.css` directly.

## Still to do

Sections marked with a highlighted note box (e.g. on the About, Programs and Governance pages) are placeholders — replace them with real content: Board Member names and photos, program outcomes, links to public reports, and real contact details.
