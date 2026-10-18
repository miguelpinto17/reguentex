"""Generates the static sites (v1..v5), assets/js/i18n.js and the chooser index.html.
Run from the repo root:  python tools/build.py   (needs Pillow for image sizes)
The output is plain HTML/CSS/JS — you can also edit the generated files directly."""
import json, os, sys
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import *

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C.update({
 "est": ("Est. 1998", "Desde 1998"),
 "mq": ("Men · Women · Kidswear · Sportswear · Sleepwear · Homewear", "Homem · Mulher · Criança · Roupa desportiva · Roupa de dormir · Roupa de casa"),
 "scroll": ("Scroll", "Deslizar"),
 "gallery": ("Gallery", "Galeria"),
 "cta_enquire": ("Quick enquiry", "Pedido rápido"),
 "cta_showroom": ("Request Virtual Showroom", "Pedir Showroom Virtual"),
 "enq_title": ("Quick enquiry", "Pedido rápido de contacto"),
 "toc_title": ("In this issue", "Neste número"),
 "cl1": ("Everything in-house, from pattern to packing", "Tudo internamente, do molde à embalagem"),
 "cl2": ("Plastic-free packing alternatives", "Alternativas às embalagens de plástico"),
 "cl3": ("Idalina Ribeiro: “My life is projecting the future”", "Idalina Ribeiro: “A minha vida é projetar o futuro”"),
 "cl4": ("A garden grown without pesticides", "Uma horta sem pesticidas"),
})
SHOW = SHOW[:3]
_sz = {}


def size(k):
    if k not in _sz:
        _sz[k] = Image.open(f"{ROOT}/assets/img/{k}.jpg").size
    return _sz[k]


def e(tag, key, cls="", extra=""):
    c = f' class="{cls}"' if cls else ""
    return f'<{tag}{c} data-i18n="{key}"{extra}>{C[key][0]}</{tag}>'


def img(k, cls="", eager=False):
    w, h = size(k)
    c = f' class="{cls}"' if cls else ""
    load = "" if eager else ' loading="lazy" decoding="async"'
    return f'<img{c} src="../assets/img/{k}.jpg" width="{w}" height="{h}" alt="{ALT[k][0]}" data-alt="{k}"{load}>'


def lb(k, group, cls="", style=""):
    c = f' class="{cls}"' if cls else ""
    s = f' style="{style}"' if style else ""
    return f'<a{c}{s} href="../assets/img/{k}.jpg" data-lb="{group}">{img(k)}</a>'


def gal(keys, group, cls="", cap=False):
    out = []
    for i, k in enumerate(keys):
        n = f'<span class="n">{i + 1:02d}</span>' if cap else ""
        out.append(lb(k, group, cls="g").replace("</a>", n + "</a>"))
    return "".join(out)


LOGO = '<img class="logo" src="../assets/img/logo-branco.png" width="971" height="117" alt="Reguentex">'
ICON = {
 "fb": '<path d="M13.5 21v-7.5h2.6l.4-3h-3V8.6c0-.9.3-1.5 1.5-1.5h1.6V4.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.8 1.4-3.8 3.9v2.3H7.9v3h2.6V21z"/>',
 "li": '<path d="M5 9h3v10H5zM6.5 4.5a1.75 1.75 0 110 3.5 1.75 1.75 0 010-3.5zM10 9h2.9v1.4c.4-.8 1.4-1.6 3-1.6 3.1 0 3.6 2 3.6 4.7V19h-3v-4.8c0-1.2 0-2.6-1.6-2.6s-1.9 1.2-1.9 2.5V19H10z"/>',
 "ig": '<rect x="4" y="4" width="16" height="16" rx="4.5" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="3.7" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="17" cy="7" r="1.1"/>',
 "tt": '<path d="M14 3h2.6c.2 1.9 1.4 3.3 3.4 3.5v2.7c-1.3 0-2.5-.4-3.4-1v6.2a5.4 5.4 0 11-5.4-5.4c.3 0 .6 0 .9.1v2.8a2.7 2.7 0 101.9 2.5z"/>',
}
NAMES = {"fb": "Facebook", "li": "LinkedIn", "ig": "Instagram", "tt": "TikTok"}


def social(cls="social"):
    a = "".join(f'<a href="{URL[k]}" target="_blank" rel="noopener" aria-label="{NAMES[k]}"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">{ICON[k]}</svg></a>' for k in ICON)
    return f'<div class="{cls}">{a}</div>'


def langsw(cls="lang"):
    return f'<div class="{cls}" role="group" aria-label="Language"><button type="button" data-lang-set="en">EN</button><button type="button" data-lang-set="pt">PT</button></div>'


def phones():
    return "".join(f'<a href="tel:{t}">{p}</a>' for p, t in PHONES)


def addr():
    return "<br>".join(ADDR)


def mail():
    return f'<a href="mailto:{EMAIL}">{EMAIL}</a>'


def navitems(page):
    b = "" if page == "home" else "index.html"
    return [
        ("nav_home", "#top" if page == "home" else "index.html"),
        ("nav_company", b + "#the-company"),
        ("nav_facility", b + "#production-facility"),
        ("nav_showroom", "showroom.html"),
        ("nav_sust", "sustainability.html"),
        ("nav_contacts", b + "#contacts"),
    ]


def navlinks(page, cls="", wrap=None):
    cur = {"showroom": "showroom.html", "sust": "sustainability.html"}.get(page)
    out = []
    for k, h in navitems(page):
        cc = ' aria-current="page"' if h == cur else ""
        a = f'<a href="{h}" data-i18n="{k}"{cc}>{C[k][0]}</a>'
        out.append(f"<{wrap}>{a}</{wrap}>" if wrap else a)
    return "".join(out)


def form(cls="req"):
    return f'''<form class="{cls}" data-request data-endpoint="" data-mailto="{EMAIL}">
  <label><span data-i18n="f_name">Name</span><input name="name" required autocomplete="name"></label>
  <label><span data-i18n="f_company">Company</span><input name="company" autocomplete="organization"></label>
  <label class="wide"><span data-i18n="f_email">Email</span><input name="email" type="email" required autocomplete="email"></label>
  <label class="wide"><span data-i18n="f_message">Message</span><textarea name="message" rows="4"></textarea></label>
  <button type="submit" class="btn" data-i18n="f_send">Request access</button>
  <p class="form-status" data-status role="status" aria-live="polite"></p>
</form>'''


def legal_line():
    return f'{LEGAL}<br>{addr().replace("<br>", ", ")}'


def copyright_():
    return f'© {LEGAL} <span data-i18n="rights">All rights reserved.</span>'


def mapframe(cls="map"):
    return f'<iframe class="{cls}" title="Map" loading="lazy" src="{URL["osm"]}"></iframe>'


FONTS = {
 1: "family=Rozha+One&family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..700;1,6..96,400..700&family=Hanken+Grotesk:wght@300;400;500;600",
 2: "family=Marcellus&family=Karla:wght@300..700",
 3: "family=Fraunces:ital,opsz,wght@0,9..144,300..700;1,9..144,300..700&family=Instrument+Sans:wght@400..600",
 4: "family=Familjen+Grotesk:wght@400..700&family=DM+Mono:wght@400;500",
 5: "family=Cormorant:ital,wght@0,300..600;1,300..600&family=Schibsted+Grotesk:wght@400..600",
}
THEME = {1: "#EDE8DA", 2: "#0e0d0c", 3: "#ece7da", 4: "#fbfbf9", 5: "#12161c"}
TKEY = {"home": "title_home", "showroom": "title_showroom", "sust": "title_sust"}
FILE = {"home": "index.html", "showroom": "showroom.html", "sust": "sustainability.html"}


def shell(v, page, body):
    desc = C["hero_text"][0][:155].rsplit(" ", 1)[0] + "…"
    return f'''<!doctype html>
<html lang="en" data-title-key="{TKEY[page]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{C[TKEY[page]][0]}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="{THEME[v]}">
<link rel="icon" href="../assets/img/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{FONTS[v]}&display=swap">
<link rel="stylesheet" href="../assets/css/base.css">
<link rel="stylesheet" href="style.css">
</head>
<body id="top" class="v{v} page-{page}">
<a class="sr" href="#main">Skip to content</a>
{body}
<script src="../assets/js/i18n.js"></script>
<script src="../assets/js/site.js"></script>
</body>
</html>
'''


def press_links():
    return (f'<a class="lnk" href="{URL["article"]}" target="_blank" rel="noopener" data-i18n="int_link">{C["int_link"][0]}</a>',
            f'<a class="lnk" href="{URL["post"]}" target="_blank" rel="noopener" data-i18n="inaug_link">{C["inaug_link"][0]}</a>')


def gpsline():
    return f'<a href="{URL["map"]}" target="_blank" rel="noopener">{GPS}</a>'


# ============================================================ V1 — VOGUE (cover-story editorial)
def v1_header(p):
    return f'''<div class="cta-bar"><div class="cta-in">
  <span class="cta-est" data-i18n="est">Est. 1998</span>
  <a class="cta-mail" href="mailto:{EMAIL}">{EMAIL}</a>
  <button type="button" class="cta-btn ghost" data-open="enq" data-i18n="cta_enquire">Quick enquiry</button>
  <a class="cta-btn solid" href="showroom.html#request" data-i18n="cta_showroom">Request Virtual Showroom</a>
  {langsw()}
</div></div>
<header class="nav">
  <a class="nav-logo" href="index.html" aria-label="Reguentex">{LOGO}</a>
  <button class="burger" data-menu-toggle aria-expanded="false"><span data-i18n="menu">Menu</span></button>
  <nav data-nav aria-label="Main">{navlinks(p)}</nav>
</header>
<a class="tab" href="showroom.html#request" data-i18n="cta_showroom">Request Virtual Showroom</a>
<div class="enq-scrim" data-close="enq"></div>
<aside class="enq" id="enq" aria-hidden="true" aria-label="Quick enquiry">
  <button class="enq-x" type="button" data-close="enq" aria-label="Close">×</button>
  {e("h2", "enq_title")}
  {form()}
</aside>'''


def v1_footer():
    return f'''<footer class="foot">
  <div class="foot-in">
    <a class="foot-logo" href="index.html">{LOGO}</a>
    <p>{legal_line()}</p>
    <p>{phones()}<br>{mail()}</p>
    {social()}
    <a class="up" href="#top" data-i18n="back_top">Voltar ao topo</a>
  </div>
  <p class="copy">{copyright_()}</p>
</footer>'''


def chapter1(num, tk, ps, keys, grp):
    paras = "".join(f'<p data-i18n="{p}">{C[p][0]}</p>' for p in ps)
    return f'''<article class="chap">
  <div class="chap-t rv"><span class="roman">{num}</span>{e("h3", tk)}{paras}</div>
  <div class="chap-g">{gal(keys, grp)}</div>
</article>'''


def v1_home():
    a, b = press_links()
    toc = [("01", "nav_company", "#the-company"), ("02", "nav_facility", "#production-facility"), ("03", "press_title", "#press"),
           ("04", "nav_showroom", "showroom.html"), ("05", "nav_sust", "sustainability.html"), ("06", "nav_contacts", "#contacts")]
    toc_li = "".join(f'<li class="rv" style="--d:{i * .05}s"><a href="{h}"><b>{n}</b><span data-i18n="{k}">{C[k][0]}</span></a></li>' for i, (n, k, h) in enumerate(toc))
    return f'''{v1_header("home")}
<main id="main">
<section class="cover">
  <div class="cover-img" data-parallax>{img("prateleiras-roupas", eager=True)}</div>
  <div class="cover-top">
    <p class="masthead rv" aria-hidden="true">REGUENTEX</p>
    <div class="dateline"><span data-i18n="est">Est. 1998</span><span>São Tomé de Negrelos · Portugal</span></div>
  </div>
  <div class="cover-mid">
    <div class="cl-col">
      <a class="cl rv" href="#production-facility"><b>01</b><span data-i18n="cl1">{C["cl1"][0]}</span></a>
      <a class="cl rv" style="--d:.1s" href="#production-facility"><b>02</b><span data-i18n="cl2">{C["cl2"][0]}</span></a>
    </div>
    <div class="cl-col r">
      <a class="cl rv" style="--d:.15s" href="#press"><b>03</b><span data-i18n="cl3">{C["cl3"][0]}</span></a>
      <a class="cl rv" style="--d:.25s" href="sustainability.html"><b>04</b><span data-i18n="cl4">{C["cl4"][0]}</span></a>
    </div>
  </div>
  <div class="cover-foot">
    <div class="cover-t">
      <h1 class="rv" data-i18n="hero_title">{C["hero_title"][0]}</h1>
      <p class="deck rv" style="--d:.15s" data-i18n="hero_text">{C["hero_text"][0]}</p>
      <div class="btns rv" style="--d:.25s"><a class="btn solid" href="#production-facility" data-i18n="hero_cta">See our work</a><a class="btn line" href="showroom.html#request" data-i18n="cta_showroom">Request Virtual Showroom</a></div>
    </div>
    <div class="barcode rv" aria-hidden="true"><b>Reguentex</b><span>{ADDR[0]}</span><span>{ADDR[2]}</span><i class="bars"></i></div>
  </div>
</section>

<section class="toc">
  <div class="toc-h rv"><p class="kicker" data-i18n="est">Est. 1998</p>{e("h2", "toc_title")}</div>
  <ol>{toc_li}</ol>
  <figure class="toc-i rv" data-parallax>{img("tecidos-embrulhados")}</figure>
</section>

<section class="company" id="the-company">
  <figure class="co-i rv" data-parallax>{img("fabrica-exterior")}</figure>
  <div class="co-t">
    <p class="kicker rv">01 — 1998</p>
    {e("h2", "company_title", "rv")}
    <p class="drop rv" data-i18n="company_p1">{C["company_p1"][0]}</p>
    <p class="rv" data-i18n="company_p2">{C["company_p2"][0]}</p>
  </div>
  <blockquote class="pull rv" data-i18n="company_p3">{C["company_p3"][0]}</blockquote>
  <p class="names rv">Idalina Ribeiro <b>·</b> José Coutinho <b>·</b> Alberto Gonçalves</p>
  <a class="btn solid rv" href="#production-facility" data-i18n="company_cta">See our production facility</a>
</section>

<section class="facility" id="production-facility">
  <div class="fac-head">
    <figure class="rv" data-parallax>{img("editada4")}</figure>
    <div><p class="kicker rv">02</p>{e("h2", "fac_title", "rv")}<p class="big rv" data-i18n="fac_intro">{C["fac_intro"][0]}</p></div>
  </div>
  {chapter1("I", "pm_title", ["pm_p1", "pm_p2"], PM, "pm")}
  {chapter1("II", "pl_title", ["pl_p1", "pl_p2"], PL, "pl")}
  {chapter1("III", "pq_title", ["pq_p1", "pq_p2"], PQ, "pq")}
</section>

<section class="press" id="press">
  <p class="kicker rv">03</p>{e("h2", "press_title", "rv")}
  <div class="spread">
    <figure class="rv" data-parallax>{img("entrevista")}</figure>
    <div class="rv"><h3 data-i18n="int_label">{C["int_label"][0]}</h3><p class="who" data-i18n="int_name">Idalina Ribeiro</p>
      <blockquote class="quote" data-i18n="int_quote">{C["int_quote"][0]}</blockquote>{a}</div>
  </div>
  <div class="press-2"><figure class="rv">{img("image00003")}</figure>
    <div class="inaug"><div class="inaug-h">{e("h3", "inaug_title")}{b}</div><div class="inaug-g">{gal(INAUG, "inaug")}</div></div></div>
</section>

<section class="contacts" id="contacts">
  <div class="ct-l">
    <p class="kicker rv">06</p>{e("h2", "contacts_title", "rv")}
    <div class="cols">
      <div>{e("h4", "addr_label")}<p>{addr()}</p>{e("h4", "gps_label")}<p>{gpsline()}</p></div>
      <div>{e("h4", "contacts_label")}<p>{phones()}<br>{mail()}</p>{e("h4", "social_label")}{social()}</div>
    </div>
    <figure class="ct-i">{img("dsc_0170")}</figure>
  </div>
  <div class="ct-r">
    <div class="ct-form">{e("h3", "enq_title")}{form()}</div>
    {mapframe()}
  </div>
</section>
</main>
{v1_footer()}'''


def v1_showroom():
    return f'''{v1_header("showroom")}
<main id="main">
<section class="sub-hero">
  <div class="sub-t"><p class="kicker rv">04</p>{e("h1", "sh_title", "rv")}<p class="big rv" data-i18n="sh_p">{C["sh_p"][0]}</p></div>
  <figure class="rv" data-parallax>{img("prateleiras-roupas", eager=True)}</figure>
</section>
<section class="sub-body">
  <div class="req-wrap" id="request"><h2 data-i18n="sh_form_title">{C["sh_form_title"][0]}</h2>{form()}</div>
  <div class="sub-g">{gal(SHOW, "show")}</div>
</section>
</main>
{v1_footer()}'''


def v1_sust():
    return f'''{v1_header("sust")}
<main id="main">
<section class="sub-hero">
  <div class="sub-t"><p class="kicker rv">05</p>{e("h1", "sust_title", "rv")}{e("h2", "sust_sub", "rv sub2")}<p class="big rv" data-i18n="sust_p">{C["sust_p"][0]}</p></div>
  <figure class="rv" data-parallax>{img("dsc_0529", eager=True)}</figure>
</section>
<section class="sub-body"><div class="sub-g wide">{gal(GARDEN, "garden")}</div></section>
</main>
{v1_footer()}'''


# ============================================================ V2 — NOIR (dark rail, brass)
def v2_rail(p):
    return f'''<aside class="rail">
  <a class="rail-logo" href="{FILE['home']}" aria-label="Reguentex">{LOGO}</a>
  <button class="burger" data-menu-toggle aria-expanded="false"><span data-i18n="menu">Menu</span></button>
  <nav class="rail-nav" data-nav aria-label="Main">{navlinks(p)}</nav>
  <div class="rail-foot">{langsw()}{social()}<span class="est" data-i18n="est">Est. 1998</span></div>
</aside>'''


def v2_footer():
    return f'''<footer class="foot">
  <div><p>{legal_line()}</p></div>
  <div><p>{phones()}<br>{mail()}</p></div>
  <div>{social()}<a class="up" href="#top" data-i18n="back_top">Voltar ao topo</a></div>
  <p class="copy">{copyright_()}</p>
</footer>'''


def chapter2(num, tk, ps, keys, grp):
    paras = "".join(f'<p data-i18n="{p}">{C[p][0]}</p>' for p in ps)
    return f'''<article class="chap">
  <div class="chap-t rv"><span class="num">{num}</span>{e("h3", tk)}<div class="two">{paras}</div></div>
  <div class="strip" tabindex="0">{gal(keys, grp, cap=True)}</div>
</article>'''


def v2_home():
    a, b = press_links()
    return f'''{v2_rail("home")}
<div class="canvas"><main id="main">
<section class="hero">
  {img("prateleiras-roupas", "bg", eager=True)}
  <div class="hero-t"><p class="kicker rv">Reguentex</p><h1 class="rv" style="--d:.12s" data-i18n="hero_title">{C["hero_title"][0]}</h1>
  <p class="rv" style="--d:.28s" data-i18n="hero_text">{C["hero_text"][0]}</p>
  <a class="btn rv" style="--d:.4s" href="#production-facility" data-i18n="hero_cta">See our work</a></div>
</section>

<section class="company" id="the-company">
  <div class="co-t"><span class="num rv">01</span>{e("h2", "company_title", "rv")}
    <p class="rv" data-i18n="company_p1">{C["company_p1"][0]}</p><p class="rv" data-i18n="company_p2">{C["company_p2"][0]}</p><p class="rv" data-i18n="company_p3">{C["company_p3"][0]}</p>
    <a class="btn rv" href="#production-facility" data-i18n="company_cta">See our production facility</a></div>
  <figure class="co-i rv">{img("fabrica-exterior")}</figure>
</section>

<section class="facility" id="production-facility">
  <div class="fac-head"><span class="num rv">02</span>{e("h2", "fac_title", "rv")}<p class="rv" data-i18n="fac_intro">{C["fac_intro"][0]}</p></div>
  <figure class="fac-i rv">{img("editada4")}</figure>
  {chapter2("2.1", "pm_title", ["pm_p1", "pm_p2"], PM, "pm")}
  {chapter2("2.2", "pl_title", ["pl_p1", "pl_p2"], PL, "pl")}
  {chapter2("2.3", "pq_title", ["pq_p1", "pq_p2"], PQ, "pq")}
</section>

<section class="press" id="press"><span class="num rv">03</span>{e("h2", "press_title", "rv")}
  <div class="press-grid">
    <figure class="rv">{img("entrevista")}<figcaption>{e("h3", "int_label")}<p class="who" data-i18n="int_name">Idalina Ribeiro</p></figcaption></figure>
    <div class="quote rv"><blockquote data-i18n="int_quote">{C["int_quote"][0]}</blockquote>{a}</div>
    <figure class="rv">{img("image00003")}</figure>
  </div>
  <div class="inaug">{e("h3", "inaug_title")}{b}<div class="strip" tabindex="0">{gal(INAUG, "inaug", cap=True)}</div></div>
</section>

<section class="contacts" id="contacts"><span class="num rv">04</span>{e("h2", "contacts_title", "rv")}
  <div class="ct-grid">
    <div>{e("h4", "addr_label")}<p>{addr()}</p>{e("h4", "gps_label")}<p>{gpsline()}</p>{e("h4", "contacts_label")}<p>{phones()}<br>{mail()}</p>{e("h4", "social_label")}{social()}</div>
    {mapframe()}
    <figure>{img("dsc_0170")}</figure>
  </div>
</section>
</main>{v2_footer()}</div>'''


def v2_showroom():
    return f'''{v2_rail("showroom")}
<div class="canvas"><main id="main">
<section class="sub-hero">{img("prateleiras-roupas", "bg", eager=True)}<div class="hero-t">{e("h1", "sh_title", "rv")}<p class="rv" data-i18n="sh_p">{C["sh_p"][0]}</p></div></section>
<section class="sub-body"><div class="req-wrap"><h2 data-i18n="sh_form_title">{C["sh_form_title"][0]}</h2>{form()}</div><div class="strip" tabindex="0">{gal(SHOW, "show", cap=True)}</div></section>
</main>{v2_footer()}</div>'''


def v2_sust():
    return f'''{v2_rail("sust")}
<div class="canvas"><main id="main">
<section class="sub-hero">{img("dsc_0529", "bg", eager=True)}<div class="hero-t">{e("h1", "sust_title", "rv")}{e("h2", "sust_sub", "rv sub2")}<p class="rv" data-i18n="sust_p">{C["sust_p"][0]}</p></div></section>
<section class="sub-body"><div class="strip" tabindex="0">{gal(GARDEN, "garden", cap=True)}</div></section>
</main>{v2_footer()}</div>'''


# ============================================================ V3 — VERDE (organic, arches)
BADGE = '''<svg class="badge" viewBox="0 0 120 120" aria-hidden="true"><defs><path id="c" d="M60 60m-46 0a46 46 0 1 1 92 0a46 46 0 1 1-92 0"/></defs><text><textPath href="#c">Reguentex · 1998 · Slow Fashion · Portugal · </textPath></text><circle cx="60" cy="60" r="5"/></svg>'''


def v3_header(p):
    return f'''<header class="pill">
  <a class="pill-logo" href="{FILE['home']}" aria-label="Reguentex">{LOGO}</a>
  <nav data-nav aria-label="Main">{navlinks(p)}</nav>
  {langsw()}
  <button class="burger" data-menu-toggle aria-expanded="false"><span data-i18n="menu">Menu</span></button>
</header>'''


def marquee():
    t = f'<span data-i18n="mq">{C["mq"][0]}</span>'
    return f'<div class="marq" aria-hidden="true"><div class="marq-in">{(t + "<i>✦</i>") * 4}</div></div>'


def v3_footer():
    return f'''<footer class="foot">
  <div class="foot-top"><a class="foot-logo" href="{FILE['home']}">{LOGO}</a><a class="up" href="#top" data-i18n="back_top">Voltar ao topo</a></div>
  <div class="foot-cols"><p>{legal_line()}</p><p>{phones()}<br>{mail()}</p>{social()}</div>
  <p class="copy">{copyright_()}</p>
</footer>'''


def chapter3(num, tk, ps, keys, grp, cls):
    paras = "".join(f'<p data-i18n="{p}">{C[p][0]}</p>' for p in ps)
    return f'''<article class="chap {cls}">
  <div class="chap-t rv"><span class="num">{num}</span>{e("h3", tk)}{paras}</div>
  <div class="chap-g">{gal(keys, grp)}</div>
</article>'''


def v3_home():
    a, b = press_links()
    return f'''{v3_header("home")}
<main id="main">
<section class="hero">
  <div class="hero-t"><p class="kicker rv">Reguentex</p><h1 class="rv" style="--d:.1s" data-i18n="hero_title">{C["hero_title"][0]}</h1>
  <p class="rv" style="--d:.22s" data-i18n="hero_text">{C["hero_text"][0]}</p><a class="btn rv" style="--d:.34s" href="#production-facility" data-i18n="hero_cta">See our work</a></div>
  <div class="hero-i rv" style="--d:.2s">{img("prateleiras-roupas", "arch", eager=True)}{BADGE}</div>
</section>
{marquee()}
<section class="company" id="the-company">
  <figure class="co-i rv">{img("fabrica-exterior", "arch")}</figure>
  <div class="co-t card">{e("h2", "company_title", "rv")}<p class="rv" data-i18n="company_p1">{C["company_p1"][0]}</p><p class="rv" data-i18n="company_p2">{C["company_p2"][0]}</p><p class="rv" data-i18n="company_p3">{C["company_p3"][0]}</p>
  <a class="btn light rv" href="#production-facility" data-i18n="company_cta">See our production facility</a></div>
</section>
<section class="facility" id="production-facility">
  <div class="fac-head">{e("h2", "fac_title", "rv")}<p class="rv" data-i18n="fac_intro">{C["fac_intro"][0]}</p><figure class="rv">{img("editada4", "pebble")}</figure></div>
  {chapter3("01", "pm_title", ["pm_p1", "pm_p2"], PM, "pm", "")}
  {chapter3("02", "pl_title", ["pl_p1", "pl_p2"], PL, "pl", "flip")}
  {chapter3("03", "pq_title", ["pq_p1", "pq_p2"], PQ, "pq", "")}
</section>
<section class="press" id="press">
  <div class="press-card">{e("h2", "press_title", "rv")}
    <figure class="rv">{img("entrevista", "pebble")}</figure>
    <div class="rv">{e("h3", "int_label")}<p class="who" data-i18n="int_name">Idalina Ribeiro</p><blockquote data-i18n="int_quote">{C["int_quote"][0]}</blockquote>{a}</div>
    <figure class="rv np">{img("image00003", "arch")}</figure>
  </div>
  <div class="inaug">{e("h3", "inaug_title")}{b}<div class="inaug-g">{gal(INAUG, "inaug")}</div></div>
</section>
<section class="contacts" id="contacts">
  <div class="ct-t">{e("h2", "contacts_title", "rv")}
    {e("h4", "addr_label")}<p>{addr()}</p>{e("h4", "gps_label")}<p>{gpsline()}</p>{e("h4", "contacts_label")}<p>{phones()}<br>{mail()}</p>{e("h4", "social_label")}{social()}</div>
  <div class="ct-m">{mapframe()}<figure>{img("dsc_0170", "arch")}</figure></div>
</section>
</main>{v3_footer()}'''


def v3_showroom():
    return f'''{v3_header("showroom")}
<main id="main">
<section class="sub-hero"><div class="sub-t">{e("h1", "sh_title", "rv")}<p class="rv" data-i18n="sh_p">{C["sh_p"][0]}</p></div><figure class="rv">{img("prateleiras-roupas", "arch", eager=True)}</figure></section>
<section class="sub-body"><div class="req-wrap card"><h2 data-i18n="sh_form_title">{C["sh_form_title"][0]}</h2>{form()}</div><div class="sub-g">{gal(SHOW, "show")}</div></section>
</main>{v3_footer()}'''


def v3_sust():
    return f'''{v3_header("sust")}
<main id="main">
<section class="sub-hero"><div class="sub-t">{e("h1", "sust_title", "rv")}{e("h2", "sust_sub", "rv sub2")}<p class="rv" data-i18n="sust_p">{C["sust_p"][0]}</p></div><figure class="rv">{img("dsc_0529", "arch", eager=True)}</figure></section>
<section class="sub-body"><div class="bento">{gal(GARDEN, "garden")}</div></section>
</main>{v3_footer()}'''


# ============================================================ V4 — GRID (technical spec sheet)
def v4_header(p):
    return f'''<header class="bar">
  <a class="bar-logo" href="{FILE['home']}" aria-label="Reguentex">{LOGO}</a>
  <nav data-nav aria-label="Main">{navlinks(p)}</nav>
  {langsw()}
  <button class="burger" data-menu-toggle aria-expanded="false"><span data-i18n="menu">Menu</span></button>
</header>'''


def tick():
    t = f'<span data-i18n="mq">{C["mq"][0]}</span>'
    return f'<div class="tick" aria-hidden="true"><div class="tick-in">{(t + "<i>/</i>") * 4}</div></div>'


def v4_footer():
    return f'''<footer class="foot">
  <div class="cell"><p>{legal_line()}</p></div>
  <div class="cell"><p>{phones()}<br>{mail()}</p></div>
  <div class="cell">{social()}</div>
  <div class="cell"><a class="up" href="#top" data-i18n="back_top">Voltar ao topo</a></div>
  <p class="copy">{copyright_()}</p>
</footer>'''


def chapter4(num, tk, ps, keys, grp):
    paras = "".join(f'<p data-i18n="{p}">{C[p][0]}</p>' for p in ps)
    return f'''<article class="chap">
  <div class="chap-t rv"><span class="tag">SPEC {num}</span>{e("h3", tk)}{paras}</div>
  <div class="sheet">{gal(keys, grp, cap=True)}</div>
</article>'''


def v4_home():
    a, b = press_links()
    return f'''{v4_header("home")}
<main id="main">
<section class="hero">
  <h1 class="rv" data-i18n="hero_title">{C["hero_title"][0]}</h1>
  <div class="hero-row">
    <figure class="rv" style="--d:.1s"><span class="tag">FIG. 01</span>{img("prateleiras-roupas", eager=True)}</figure>
    <div class="hero-t"><p class="rv" style="--d:.2s" data-i18n="hero_text">{C["hero_text"][0]}</p><a class="btn rv" style="--d:.3s" href="#production-facility"><span data-i18n="hero_cta">See our work</span> ↘</a></div>
  </div>
</section>
{tick()}
<section class="company" id="the-company">
  <div class="co-head"><span class="tag">00 / 1998</span>{e("h2", "company_title", "rv")}</div>
  <div class="co-body"><p class="rv" data-i18n="company_p1">{C["company_p1"][0]}</p><p class="rv" data-i18n="company_p2">{C["company_p2"][0]}</p><p class="rv" data-i18n="company_p3">{C["company_p3"][0]}</p>
    <a class="btn rv" href="#production-facility"><span data-i18n="company_cta">See our production facility</span> ↘</a></div>
  <figure class="co-i rv"><span class="tag">FIG. 02</span>{img("fabrica-exterior")}</figure>
</section>
<section class="facility" id="production-facility">
  <div class="fac-head"><div>{e("h2", "fac_title", "rv")}<p class="rv" data-i18n="fac_intro">{C["fac_intro"][0]}</p></div><figure class="rv">{img("editada4")}</figure></div>
  {chapter4("01", "pm_title", ["pm_p1", "pm_p2"], PM, "pm")}
  {chapter4("02", "pl_title", ["pl_p1", "pl_p2"], PL, "pl")}
  {chapter4("03", "pq_title", ["pq_p1", "pq_p2"], PQ, "pq")}
</section>
<section class="press" id="press">
  <div class="press-h"><span class="tag">PRESS</span>{e("h2", "press_title", "rv")}</div>
  <div class="press-grid">
    <figure class="rv">{img("entrevista")}</figure>
    <div class="rv">{e("h3", "int_label")}<p class="who" data-i18n="int_name">Idalina Ribeiro</p><blockquote data-i18n="int_quote">{C["int_quote"][0]}</blockquote>{a}</div>
    <figure class="rv">{img("image00003")}</figure>
  </div>
  <div class="inaug"><div class="inaug-h">{e("h3", "inaug_title")}{b}</div><div class="sheet six">{gal(INAUG, "inaug", cap=True)}</div></div>
</section>
<section class="contacts" id="contacts">
  <div class="ct-h">{e("h2", "contacts_title", "rv")}</div>
  <div class="ct-grid">
    <div class="cell">{e("h4", "addr_label")}<p>{addr()}</p></div>
    <div class="cell">{e("h4", "gps_label")}<p>{gpsline()}</p></div>
    <div class="cell">{e("h4", "contacts_label")}<p>{phones()}<br>{mail()}</p></div>
    <div class="cell">{e("h4", "social_label")}{social()}</div>
    <figure class="cell img">{img("dsc_0170")}</figure>
    <div class="cell map">{mapframe()}</div>
  </div>
</section>
</main>{v4_footer()}'''


def v4_showroom():
    return f'''{v4_header("showroom")}
<main id="main">
<section class="sub-hero"><h1 class="rv" data-i18n="sh_title">{C["sh_title"][0]}</h1><div class="sub-row"><p class="rv" data-i18n="sh_p">{C["sh_p"][0]}</p><figure class="rv">{img("prateleiras-roupas", eager=True)}</figure></div></section>
<section class="sub-body"><div class="req-wrap"><h2 data-i18n="sh_form_title">{C["sh_form_title"][0]}</h2>{form()}</div><div class="sheet">{gal(SHOW, "show", cap=True)}</div></section>
</main>{v4_footer()}'''


def v4_sust():
    return f'''{v4_header("sust")}
<main id="main">
<section class="sub-hero"><h1 class="rv" data-i18n="sust_title">{C["sust_title"][0]}</h1><div class="sub-row"><div>{e("h2", "sust_sub", "rv sub2")}<p class="rv" data-i18n="sust_p">{C["sust_p"][0]}</p></div><figure class="rv">{img("dsc_0529", eager=True)}</figure></div></section>
<section class="sub-body"><div class="sheet">{gal(GARDEN, "garden", cap=True)}</div></section>
</main>{v4_footer()}'''


# ============================================================ V5 — CINEMA (full-bleed, serif italic)
def v5_header(p):
    return f'''<header class="top">
  <a class="top-logo" href="{FILE['home']}" aria-label="Reguentex">{LOGO}</a>
  <div class="top-r">{langsw()}<button class="burger" data-menu-toggle aria-expanded="false"><span data-i18n="menu">Menu</span><i></i></button></div>
</header>
<div class="overlay" data-nav><button class="x" data-menu-toggle aria-label="Close">×</button><nav aria-label="Main">{navlinks(p)}</nav><div class="ov-foot">{social()}<p>{phones()}</p></div></div>'''


def v5_footer():
    return f'''<footer class="foot">
  <a class="foot-logo" href="{FILE['home']}">{LOGO}</a>
  <p>{legal_line()}</p><p>{phones()}<br>{mail()}</p>{social()}
  <a class="up" href="#top" data-i18n="back_top">Voltar ao topo</a>
  <p class="copy">{copyright_()}</p>
</footer>'''


def panel5(num, tk, ps, keys, grp):
    paras = "".join(f'<p data-i18n="{p}">{C[p][0]}</p>' for p in ps)
    return f'''<article class="panel">
  {img(keys[0], "bg")}
  <div class="panel-t rv"><span class="num">{num}</span>{e("h3", tk)}{paras}</div>
  <div class="film" tabindex="0">{gal(keys, grp)}</div>
</article>'''


def v5_home():
    a, b = press_links()
    return f'''{v5_header("home")}
<main id="main">
<section class="hero">
  {img("prateleiras-roupas", "bg", eager=True)}
  <div class="hero-t"><p class="kicker rv">Reguentex</p><h1 class="rv" style="--d:.1s" data-i18n="hero_title">{C["hero_title"][0]}</h1>
  <div class="hero-b"><p class="rv" style="--d:.3s" data-i18n="hero_text">{C["hero_text"][0]}</p><a class="btn rv" style="--d:.4s" href="#production-facility" data-i18n="hero_cta">See our work</a></div></div>
  <a class="cue" href="#the-company"><span data-i18n="scroll">Scroll</span><i></i></a>
</section>
<section class="company" id="the-company">
  <figure class="co-i">{img("fabrica-exterior")}</figure>
  <div class="co-t">{e("h2", "company_title", "rv")}<p class="rv" data-i18n="company_p1">{C["company_p1"][0]}</p><p class="rv" data-i18n="company_p2">{C["company_p2"][0]}</p><p class="rv" data-i18n="company_p3">{C["company_p3"][0]}</p>
    <a class="btn rv" href="#production-facility" data-i18n="company_cta">See our production facility</a></div>
</section>
<section class="facility" id="production-facility">
  <div class="fac-head">{img("editada4", "bg")}<div class="fac-t">{e("h2", "fac_title", "rv")}<p class="rv" data-i18n="fac_intro">{C["fac_intro"][0]}</p></div></div>
  {panel5("I", "pm_title", ["pm_p1", "pm_p2"], PM, "pm")}
  {panel5("II", "pl_title", ["pl_p1", "pl_p2"], PL, "pl")}
  {panel5("III", "pq_title", ["pq_p1", "pq_p2"], PQ, "pq")}
</section>
<section class="press" id="press">
  <div class="press-h">{e("h2", "press_title", "rv")}</div>
  <div class="press-grid">
    <figure class="rv">{img("entrevista")}</figure>
    <div class="rv">{e("h3", "int_label")}<p class="who" data-i18n="int_name">Idalina Ribeiro</p><blockquote data-i18n="int_quote">{C["int_quote"][0]}</blockquote>{a}</div>
    <figure class="rv np">{img("image00003")}</figure>
  </div>
  <div class="inaug">{e("h3", "inaug_title")}{b}<div class="film" tabindex="0">{gal(INAUG, "inaug")}</div></div>
</section>
<section class="contacts" id="contacts">
  <figure class="ct-i">{img("dsc_0170")}</figure>
  <div class="ct-t">{e("h2", "contacts_title", "rv")}<div class="cols"><div>{e("h4", "addr_label")}<p>{addr()}</p>{e("h4", "gps_label")}<p>{gpsline()}</p></div>
    <div>{e("h4", "contacts_label")}<p>{phones()}<br>{mail()}</p>{e("h4", "social_label")}{social()}</div></div>{mapframe()}</div>
</section>
</main>{v5_footer()}'''


def v5_showroom():
    return f'''{v5_header("showroom")}
<main id="main">
<section class="sub-hero">{img("prateleiras-roupas", "bg", eager=True)}<div class="hero-t">{e("h1", "sh_title", "rv")}<p class="rv" data-i18n="sh_p">{C["sh_p"][0]}</p></div></section>
<section class="sub-body"><div class="req-wrap"><h2 data-i18n="sh_form_title">{C["sh_form_title"][0]}</h2>{form()}</div><div class="film" tabindex="0">{gal(SHOW, "show")}</div></section>
</main>{v5_footer()}'''


def v5_sust():
    return f'''{v5_header("sust")}
<main id="main">
<section class="sub-hero">{img("dsc_0529", "bg", eager=True)}<div class="hero-t">{e("h1", "sust_title", "rv")}{e("h2", "sust_sub", "rv sub2")}<p class="rv" data-i18n="sust_p">{C["sust_p"][0]}</p></div></section>
<section class="sub-body"><div class="film" tabindex="0">{gal(GARDEN, "garden")}</div></section>
</main>{v5_footer()}'''


VARIANTS = {
 1: ("v1-ivory", v1_home, v1_showroom, v1_sust),
 2: ("v2-noir", v2_home, v2_showroom, v2_sust),
 3: ("v3-verde", v3_home, v3_showroom, v3_sust),
 4: ("v4-grid", v4_home, v4_showroom, v4_sust),
 5: ("v5-cinema", v5_home, v5_showroom, v5_sust),
}

if __name__ == "__main__":
    for v, (folder, *fns) in VARIANTS.items():
        os.makedirs(f"{ROOT}/{folder}", exist_ok=True)
        for page, fn in zip(["home", "showroom", "sust"], fns):
            with open(f"{ROOT}/{folder}/{FILE[page]}", "w", encoding="utf8", newline="\n") as f:
                f.write(shell(v, page, fn()))
    with open(f"{ROOT}/assets/js/i18n.js", "w", encoding="utf8", newline="\n") as f:
        f.write("/* Generated by tools/build.py from tools/content.py — edit the copy there. */\nwindow.RGX_I18N = "
                + json.dumps({"c": C, "alt": ALT}, ensure_ascii=False, indent=1) + ";\n")
    print("built", len(VARIANTS), "variants")
