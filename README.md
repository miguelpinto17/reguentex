# Reguentex — website redesign (5 static directions)

Static HTML/CSS/JS rebuild of https://www.reguentex.pt/ (Home, Showroom, Sustainability) in five design directions.
Open `index.html` to compare them; each variant has its own folder with `index.html`, `showroom.html`, `sustainability.html`, `style.css`.

| Folder | Direction |
|---|---|
| `v1-ivory` | **Vogue cover-story editorial** (the chosen direction) — contact bar, quick-enquiry panel, sticky showroom tab, contents page, pull-quotes, parallax; brown/cream/green/charcoal |
| `v2-noir` | Dark atelier — fixed rail, brass, scroll strips |
| `v3-verde` | Organic luxury — arches, pill nav, green/terracotta |
| `v4-grid` | Technical spec sheet — ruled grid, mono labels, red thread |
| `v5-cinema` | Full-bleed film — sticky split, italic serif, overlay menu |

## Shared
- `assets/img` — all images downloaded from the Squarespace site (1500px wide).
- `assets/js/site.js` — EN/PT toggle, lightbox, reveal, menu, request form.
- `assets/js/i18n.js` — generated copy (EN + PT).
- `tools/content.py` — **all copy, alt texts and links live here**. `tools/build.py` regenerates the five sites (`pip install pillow`, `python tools/build.py`).

## Virtual Showroom form
Set `data-endpoint="https://formspree.io/f/XXXX"` (or any endpoint accepting a POST) on the `<form data-request>` to submit to a service.
Without it, the form opens the visitor's email client addressed to geral@reguentex.pt.

## Content notes
- Portuguese translations were written for this project — have a native speaker review them.
- Legal name unified to "Reguentex Confeções Têxteis Unipessoal, Lda." — confirm against the company registration.
- Removed the broken `file:///C:/...` link from the original contacts section; added alt text and a map link/embed for the GPS coordinates.
