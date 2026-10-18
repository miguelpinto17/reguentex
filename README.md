# Reguentex — website

Static HTML/CSS/JS rebuild of https://www.reguentex.pt/ in a Vogue-style editorial design.
Pages: `index.html` (Home), `showroom.html` (Virtual Showroom), `sustainability.html`.
Live (GitHub Pages): https://miguelpinto17.github.io/reguentex/

## Structure
- `assets/css/base.css` — reset, lightbox, reveal. `assets/css/style.css` — the design (palette: brown #45311C · cream #EDE8DA · green #486649 · charcoal #363636).
- `assets/js/site.js` — EN/PT toggle (English by default), lightbox, menu, enquiry panel, parallax, request form.
- `assets/js/i18n.js` — generated copy (EN + PT).
- `assets/img` — images downloaded from the Squarespace site.
- `tools/content.py` — **all copy, alt texts and links live here**. `tools/build.py` regenerates the three pages and `i18n.js` (`pip install pillow`, `python tools/build.py`). The generated HTML/CSS can also be edited by hand.

## Request forms
Set `data-endpoint="https://formspree.io/f/XXXX"` (or any POST endpoint) on each `<form data-request>` to submit to a service.
Without it, the form opens the visitor's email client addressed to geral@reguentex.pt.

## Content notes
- Portuguese translations were written for this project — have a native speaker review them.
- Legal name unified to "Reguentex Confeções Têxteis Unipessoal, Lda." — confirm against the company registration.
- Removed the broken `file:///C:/...` link from the original Contacts section; added alt text and a map link/embed for the GPS coordinates.
