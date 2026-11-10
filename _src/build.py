#!/usr/bin/env python3
"""codex magna: build park.attainable.systems from _src/notes.

    python3 _src/build.py          (run from the repo root, or anywhere)

Reads   _src/notes/notebook/*.md   writing (essays, field notes, poems, fiction, craft)
        _src/notes/garden/*.md     vault notes (systems, blockchain, privacy, ...)
        _src/site.json             the status block
        _src/shelf.json            the reading shelf
Writes  index.html and every section folder at the repo root. deck/ and drafts/
are never touched.
"""
import html, json, os, re, shutil, datetime
import markdown

SRC = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SRC)
SITE = "https://park.attainable.systems"
OWNED = ["notebook", "notes", "systems", "vault", "photography", "library", "about", "shelf",
         "figment", "guestbook"]   # folders this script owns and rebuilds

FOLDERS = {  # vault folder -> (dewey, label)
    "1000 Living and Loving": ("1000", "living and loving"),
    "1010 Faith and Coordination": ("1010", "faith and coordination"),
    "1011 Endurance": ("1011", "endurance"),
    "1017 Running": ("1017", "running"),
    "1005 Identity": ("1005", "identity"),
    "1008 Loneliness": ("1008", "loneliness"),
    "1025 The Speed Project": ("1025", "the speed project"),
    "1050 Writing": ("1050", "writing"),
    "1052 Observation vs Advocacy": ("1052", "observation vs advocacy"),
    "1060 Photography": ("1060", "photography"),
    "1075 Grad School": ("1075", "grad school"),
    "1112 Community as Technology": ("1112", "community as technology"),
    "1150 Management": ("1150", "management"),
    "1151 Exec Coaching": ("1151", "exec coaching"),
    "1055 Critique": ("1055", "critique"),
    "1100 Intelligence and Learning": ("1100", "intelligence and learning"),
    "1115 Society and its structure": ("1115", "society and its structure"),
    "1125 Quantum Computing": ("1125", "quantum computing"),
    "1155 Figment": ("1155", "figment"),
    "1166 Heliax": ("1166", "heliax / namada"),
    "2000 Blockchain": ("2000", "blockchain"),
    "2100 Privacy": ("2100", "privacy"),
    "2222 Systems": ("2222", "systems"),
    "2266 Technology": ("2266", "technology"),
    "0000 Home": ("0000", "home"),
}
KINDS = ["essay", "memoir", "journal", "field note", "poem", "fiction", "craft"]

NAV = [("0000", "index", "/"), ("0100", "photography", "/photography/"), ("0200", "writing", "/notebook/"),
       ("2222", "systems", "/systems/"), ("0300", "library", "/library/"), ("0400", "about", "/about/"),
       ("0500", "deck", "/deck/")]

PHOTOS = [  # file, title, line, series, shape (v = tall, h = wide)
    ("coal-stacks", "Four Corners", "3 July 2017. Colorado Plateau.", "four corners, 2017", "h"),
    ("herm-raft", "Herm Hoops", "1 June 2017. Colorado Plateau.", "four corners, 2017", "v"),
    ("window-rock-wave", "Window Rock", "26 June 2017.", "four corners, 2017", "h"),
    ("kendra", "Kendra Pinto", "22 June 2017.", "four corners, 2017", "v"),
    ("billboard", "billboard", "desert.", "four corners, 2017", "h"),
    ("tree-tunnel", "Vol State 500k", "2018. Rhoda Smoker, first woman, second overall.", "running", "h"),
    ("rhr-ramps", "Red Hook Race", "Orchard Street Runners.", "running", "h"),
    ("bread-route", "Bread Route", "Orchard Street Runners.", "running", "h"),
    ("snow-runner", "Prospect Park", "Brooklyn, during the January 2018 snowstorm.", "running", "h"),
    ("kg-ridge", "Kyrgyzstan", "September 2025. Transmission towers on the ridge.", "kyrgyzstan and hong kong, 2025", "h"),
    ("hk-delivery", "Hong Kong", "November 2025.", "kyrgyzstan and hong kong, 2025", "v"),
    ("kg-horses", "Kyrgyzstan", "September 2025.", "kyrgyzstan and hong kong, 2025", "h"),
    ("hk-desk", "Hong Kong", "November 2025. A desk.", "kyrgyzstan and hong kong, 2025", "v"),
    ("lalv-road", "The Speed Project", "Los Angeles → Las Vegas, April 2026. Still from video.", "the speed project, 2026", "v"),
    ("pyr-ridge", "The Speed Project", "the Pyrénées, October 2026. Still from video.", "the speed project, 2026", "v"),
    ("lalv-roof", "The Speed Project", "Los Angeles → Las Vegas, April 2026. Still from video.", "the speed project, 2026", "v"),
    ("japan-climb", "Japan", "May 2018. Bicycling, January 2020.", "elsewhere", "h"),
    ("water", "Water", "March 2017.", "elsewhere", "v"),
]
# the archive picks (Photos on Drive), made 2026-11-06; same shape as PHOTOS
_pj = os.path.join(os.path.dirname(os.path.abspath(__file__)), "photos.json")
if os.path.exists(_pj):
    PHOTOS += [tuple(x) for x in json.load(open(_pj))]
PHOTO_COVER = "kg-ridge"  # the large photo at the top of /photography/

SERIES = ["colorado plateau, 2017", "four corners, 2017", "montana, 2018", "montana, 2021", "kyrgyzstan and hong kong, 2025",
          "australia, 2025", "san francisco, 2025", "vol state 500k, 2018", "running", "prospect park, january 2018",
          "the speed project, 2026", "skygazer, 2016", "portraits, 2016", "water", "elsewhere"]

TEARSHEETS = [
    ("rw-sam", "Runner's World", "May 2018 · the cover"),
    ("clip-goldsprints", "Bicycling", "November/December 2016 · goldsprints at Sacred Tattoo, New York"),
    ("clip-bicycling", "Bicycling", "7 January 2020 · In Japan, the People, the Riding, and the Roads Are Poetry"),
    ("ng-naledi", "National Geographic", "with Robert Clark · Homo naledi"),
    ("ng-trujillo", "National Geographic", "with Robert Clark · the child sacrifices near Trujillo"),
    ("ng-abusir", "National Geographic", "with Robert Clark · Egypt's looted tombs"),
]
ELSEWHERE = [
    ("2021", "Managing the Cosmic Commons", "keynote, decentralized governance", "https://youtu.be/H7UDxFxvOlM"),
    ("2023", "Discussing the Community Builder Epoch 1 RPGF results", "namada blog", "https://namada.net/blog/discussing-the-community-builder-epoch-1-rpgf-results"),
    ("2023", "Proposing a Namada Community Architecture Based on RPGF Funding", "namada forum", "https://forum.namada.net/t/proposing-a-namada-community-architecture-based-on-rpgf-funding/427"),
    ("2023", "Bringing Namada to the Interchain", "talk", "https://www.youtube.com/watch?v=l5V9kNv6xm4&t=6s"),
    ("2024", "Governing Penumbra: Private Staking, delUM, and Private Governance", "penumbra blog", "https://www.penumbra.zone/blog/governing-penumbra-private-staking-delum-and-private-governance"),
    ("2018", "Vol State Ultra", "runner's world", "https://www.runnersworld.com/races-places/a27228860/vol-state-ultra-monday-motivation/"),
    ("2018", "How Running Replaced Partying for this NYC Bartender", "runner's world · cover", "https://www.runnersworld.com/runners-stories/a20055214/how-running-replaced-partying-for-this-nyc-bartender/"),
]

esc = html.escape


# ───────────────────────── notes ─────────────────────────

def slugify(s):
    s = s.lower().replace("&", " and ")
    s = re.sub(r"['’]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:70].strip("-") or "note"


class Note:
    pass


def load():
    notes = []
    for sub in ("notebook", "garden"):
        d = os.path.join(SRC, "notes", sub)
        for f in sorted(os.listdir(d)):
            t = open(os.path.join(d, f)).read()
            _, fm, body = t.split("---\n", 2)
            m = json.loads(fm)
            n = Note()
            n.__dict__.update(m)
            n.body = body
            n.notebook = sub == "notebook"
            n.kind = m.get("kind")
            n.url_out = m.get("url")
            notes.append(n)
    used = set()
    for n in sorted(notes, key=lambda n: (not n.notebook, n.title.lower())):
        s = slugify(n.title if n.notebook else n.stem)
        base, i = s, 2
        while s in used:
            s, i = f"{base}-{i}", i + 1
        used.add(s)
        n.slug = s
        n.href = f"/notebook/{s}/" if n.notebook else f"/notes/{s}/"
        n.dewey, n.flabel = FOLDERS.get(n.folder, ("0000", n.folder.lower()))
    by_folder = {}
    for n in notes:
        by_folder.setdefault(n.dewey, []).append(n)
    for k, lst in by_folder.items():
        for i, n in enumerate(sorted(lst, key=lambda n: ((n.date or "9999"), n.title.lower())), 1):
            n.id = f"{k}.{i:03d}"
    return notes


def build_index(notes):
    idx = {}
    for n in notes:
        for key in (n.stem, n.title):
            idx.setdefault(key.lower().strip(), n)
    return idx


WIKI = re.compile(r"\[\[([^\]]+?)\]\]")


def resolve(target, idx):
    t = target.split("#")[0].strip()
    base = t.split("/")[-1].strip().lower()
    if base in idx:
        return idx[base]
    for fk, (dw, lab) in FOLDERS.items():
        if base == fk.lower():
            return ("folder", dw, lab)
    return None


def link_html(target, alias, idx, me=None):
    r = resolve(target, idx)
    label = esc(alias or target.split("/")[-1].split("#")[0])
    if isinstance(r, Note):
        if me is not None and r is not me:
            me.out.add(r)
        return f'<a class="wl" href="{r.href}">{label}</a>'
    if isinstance(r, tuple):
        return f'<a class="wl" href="/vault/{r[1]}/">{label}</a>'
    return f'<span class="ul" title="not published">{label}</span>'


def render_body(n, idx):
    text = n.body
    # protect code spans/blocks from wikilink processing
    keep = []
    def stash(m):
        keep.append(m.group(0)); return f"\x00{len(keep)-1}\x00"
    text = re.sub(r"```.*?```|`[^`\n]+`", stash, text, flags=re.S)
    def wl(m):
        inner = m.group(1)
        target, _, alias = inner.partition("|")
        return link_html(target, alias or None, idx, n)
    text = re.sub(r"\]\]\s*\[\[", "]] · [[", text)
    text = WIKI.sub(wl, text)
    text = re.sub(r"==([^=\n]+)==", r"<mark>\1</mark>", text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], text)
    md = markdown.Markdown(extensions=["extra", "sane_lists", "nl2br"], output_format="html5")
    out = md.convert(text)
    out = re.sub(r'<a href="(https?://[^"]+)"', r'<a class="ext" href="\1" rel="noopener"', out)
    return out


MENTION_STOP = {
    "system", "public", "writing", "protocol", "intent", "primitive", "primitives", "quality", "walker",
    "the figure", "cosmos", "stellar", "uncommon", "threshold", "dao", "ibc", "evm", "mev", "masp", "nam", "prover", "gnosis", "candor",
}


def mention_terms(notes):
    terms = {}
    for g in notes:
        if g.notebook:
            continue
        t = g.stem.lower().strip()
        if len(t) < 4 or t in MENTION_STOP or len(t) > 40 or re.search(r"[?()_*\d]", t) or t.startswith(("what ", "why ")):
            continue
        terms.setdefault(t, g)
    return terms


SKIP_TAGS = re.compile(r"^<(/?)(a|code|pre|h[1-6]|mark|span)\b", re.I)


def link_mentions(n, terms):
    """Obsidian-style unlinked mentions: find vault notes named in a piece of
    writing, link the first occurrence inline, and remember the pair."""
    found = {}
    low = plain(n.body, 10**9).lower()
    cands = [t for t in terms if re.search(r"(?<![\w-])" + re.escape(t) + r"(?:s|es)?(?![\w-])", low)]
    cands = [t for t in cands if terms[t] not in n.out and terms[t] is not n]
    if not cands:
        return
    rx = re.compile(r"(?<![\w-])((" + "|".join(re.escape(t) for t in sorted(cands, key=len, reverse=True)) + r")(?:s|es)?)(?![\w-])", re.I)
    parts = re.split(r"(<[^>]+>)", n.html)
    depth = 0
    for i, part in enumerate(parts):
        if part.startswith("<"):
            m = SKIP_TAGS.match(part)
            if m:
                depth += -1 if m.group(1) else 1
            continue
        if depth > 0 or not part.strip():
            continue
        def sub(m):
            key = m.group(2).lower()
            if key in found:
                return m.group(0)
            g = terms[key]
            found[key] = g
            return f'<a class="ml" href="{g.href}" title="in the vault: {esc(g.title)}">{m.group(1)}</a>'
        parts[i] = rx.sub(sub, part)
    n.html = "".join(parts)
    for g in found.values():
        n.mentions.add(g)
        g.mentioned_in.add(n)


def plain(text, n=220):
    t = WIKI.sub(lambda m: (m.group(1).split("|")[-1]).split("/")[-1], text)
    t = re.sub(r"```.*?```", " ", t, flags=re.S)
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", t)
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"^#+\s.*$", " ", t, flags=re.M)
    t = re.sub(r"^\s*[-*>]\s+", " ", t, flags=re.M)
    t = re.sub(r"[*_`#>|]|\$+", "", t)
    t = re.sub(r"\[\^\d+\]", "", t)
    t = re.sub(r"\s+", " ", t).strip()
    if len(t) <= n:
        return t
    cut = t[:n].rsplit(" ", 1)[0]
    return cut.rstrip(",;:-–—") + " …"


def fmt_date(n):
    if getattr(n, "date_label", None):
        return n.date_label
    if n.date:
        return n.date.replace("-", ".")
    return "undated"


# ───────────────────────── layout ─────────────────────────

def page(title, body, active=None, desc=None, path="/", extra_head=""):
    nav = "".join(
        f'<a href="{h}"{" class=on" if active == num else ""}><span class="n">{num}</span>{lab}</a>'
        for num, lab, h in NAV)
    t = "codex magna" if title is None else f"{esc(title)} · codex magna"
    d = esc(desc or "Park Feierbach. Photography, writing and systems research, from the vault called Codex Magna.")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{SITE}{path}">
<link rel="alternate" type="application/rss+xml" title="codex magna · notebook" href="/rss.xml">
<link rel="stylesheet" href="/assets/site.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Crect width='16' height='16' fill='%231f0f2b'/%3E%3Crect x='4' y='4' width='8' height='8' fill='%23ff5f38'/%3E%3C/svg%3E">
<script>try{{var t=localStorage.getItem("cm-theme");if(t)document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
{extra_head}</head>
<body>
<header>
  <h1><a href="/">codex magna</a></h1>
  <button class="eclipse" type="button" aria-label="switch to light mode" title="light / dark">
    <svg viewBox="0 0 64 64" aria-hidden="true" focusable="false">
      <defs>
        <radialGradient id="cm-halo" cx="32" cy="32" r="31" gradientUnits="userSpaceOnUse"><stop offset="0.48" stop-color="#fff4e0" stop-opacity="0.9"/><stop offset="0.58" stop-color="currentColor" stop-opacity="0.5"/><stop offset="0.78" stop-color="currentColor" stop-opacity="0.14"/><stop offset="1" stop-color="currentColor" stop-opacity="0"/></radialGradient>
        <radialGradient id="cm-stream" cx="32" cy="32" r="31" gradientUnits="userSpaceOnUse"><stop offset="0.48" stop-color="#fffaf0" stop-opacity="0.95"/><stop offset="0.7" stop-color="#ffe9c8" stop-opacity="0.45"/><stop offset="1" stop-color="#ffe9c8" stop-opacity="0"/></radialGradient>
        <filter id="cm-soft" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="0.55"/></filter>
        <filter id="cm-bloom" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="1.1"/></filter>
      </defs>
      <circle class="halo" cx="32" cy="32" r="31" fill="url(#cm-halo)"/>
      <g class="corona" fill="url(#cm-stream)" filter="url(#cm-soft)"><g class="st a"><path d="M47.20 31.62 Q53.06 33.69 59.75 35.83 Q52.73 36.07 46.52 36.48 Z"/><path d="M42.41 43.08 Q43.35 45.90 44.63 48.69 Q42.29 46.70 39.83 45.03 Z"/><path d="M35.17 46.87 Q34.39 49.91 33.94 53.12 Q32.90 50.05 31.58 47.19 Z"/><path d="M24.73 45.35 Q20.16 49.18 15.19 53.67 Q18.30 47.74 20.88 42.36 Z"/><path d="M17.31 35.89 Q10.28 34.95 2.30 34.03 Q10.08 32.04 16.91 30.15 Z"/><path d="M17.42 27.71 Q14.07 24.36 10.22 21.07 Q15.16 22.18 19.84 22.87 Z"/><path d="M25.18 18.41 Q25.53 15.30 25.48 12.19 Q27.28 14.72 29.41 17.02 Z"/><path d="M33.82 16.91 Q36.04 13.72 38.04 10.16 Q37.93 14.24 38.19 18.12 Z"/><path d="M43.10 21.61 Q49.49 19.56 56.58 17.07 Q51.10 22.21 46.33 26.94 Z"/></g><g class="st b"><path d="M46.23 37.33 Q49.88 40.42 54.10 43.63 Q49.07 41.96 44.46 40.71 Z"/><path d="M36.55 46.50 Q35.87 48.74 35.56 50.90 Q34.48 49.00 33.05 47.16 Z"/><path d="M24.77 45.37 Q20.54 48.44 16.12 52.06 Q18.63 46.92 20.65 42.10 Z"/><path d="M18.18 38.33 Q10.78 38.79 2.36 39.42 Q10.09 36.00 16.83 32.93 Z"/><path d="M17.73 26.75 Q14.16 23.76 10.02 20.66 Q14.94 22.24 19.45 23.42 Z"/><path d="M25.83 18.11 Q26.29 15.89 26.39 13.80 Q27.64 15.47 29.27 17.05 Z"/><path d="M37.65 17.89 Q41.19 14.18 44.90 9.87 Q42.98 15.22 41.50 20.13 Z"/><path d="M44.98 24.09 Q52.30 23.30 60.53 22.29 Q53.40 26.51 47.11 30.35 Z"/></g></g>
      <circle class="sun" cx="32" cy="32" r="15.4"/>
      <g class="moon-pos"><circle class="moon" cx="32" cy="32" r="16"/></g>
      <circle class="ring" cx="32" cy="32" r="16.3"/>
      <g class="glint g1"><path d="M43.88 18.33 L44.43 21.19 L47.28 21.73 L44.43 22.28 L43.88 25.13 L43.34 22.28 L40.48 21.73 L43.34 21.19 Z"/></g>
      <g class="glint g2"><path d="M17.59 23.08 L17.94 24.93 L19.79 25.28 L17.94 25.63 L17.59 27.48 L17.24 25.63 L15.39 25.28 L17.24 24.93 Z"/></g>
      <g class="diamond" style="transform-origin:43.88px 21.73px"><circle cx="43.88" cy="21.73" r="3.2" filter="url(#cm-bloom)"/><path d="M43.88 14.73 L45.00 20.61 L50.88 21.73 L45.00 22.85 L43.88 28.73 L42.76 22.85 L36.88 21.73 L42.76 20.61 Z"/></g>
    </svg>
  </button>
  <div class="signal">park feierbach &mdash; sapere aude</div>
</header>
<nav>{nav}</nav>
{body}
<footer>
  <div>© park feierbach 2026 · hand-built · <a href="/vault/">the stacks</a> · <a href="/rss.xml">rss</a> · <a href="https://github.com/attainable-sys/park-attainable-systems">source</a></div>
  <div>built {BUILT} from {NCOUNT} notes</div>
</footer>
<script src="/assets/site.js" defer></script>
</body>
</html>
"""


def entry(n, idx_back):
    tags = [n.kind] if n.kind else []
    tags.append(f"{n.dewey} {n.flabel}")
    bl = sorted(n.back, key=lambda x: x.title.lower())[:4]
    ol = sorted(n.out, key=lambda x: x.title.lower())[:4]
    links = "".join(f'<a class="bl" href="{b.href}">← {esc(b.title)}</a>' for b in bl)
    links += "".join(f'<a class="bl out" href="{o.href}">→ {esc(o.title)}</a>' for o in ol if o not in bl)
    links += "".join(f'<a class="bl out" href="{o.href}">↘ {esc(o.title)}</a>' for o in sorted(n.mentions, key=lambda x: x.title.lower())[:5])
    return f"""<div class="ent" data-kind="{esc(n.kind or '')}">
    <div class="dt">{fmt_date(n)} <span class="id">{n.id}</span></div>
    <h3><a href="{n.href}">{esc(n.title)}</a></h3>
    <div class="ex">{esc(plain(n.body, 300))}</div>
    <div class="tags">{''.join(f'<span class="tg">{esc(t)}</span>' for t in tags)}</div>
    {f'<div class="bls">{links}</div>' if links else ''}
  </div>"""


def node_card(n, big=False):
    c = len(n.out | n.back | n.mentioned_in)
    return f"""<a class="nd" href="{n.href}">
      <div class="id">{n.id}</div>
      <h3>{esc(n.title)}</h3>
      <p>{esc(plain(n.body, 150 if big else 110))}</p>
      <div class="cn">↔ {c} connection{'s' if c != 1 else ''}</div>
    </a>"""


def note_list(lst):
    rows = []
    for n in lst:
        c = len(n.out | n.back | n.mentioned_in | n.mentions)
        rows.append(f'<a href="{n.href}"><span class="n">{n.id}</span>{esc(n.title)}'
                    f'<span class="desc">{"↔ " + str(c) if c else ""}</span></a>')
    return f'<div class="idx">{"".join(rows)}</div>'


# ───────────────────────── pages ─────────────────────────

def write(rel, content):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(content)


def note_page(n, idx):
    body_html = n.html
    meta = [f'<span>{n.id}</span>', f'<a href="/vault/{n.dewey}/">{n.dewey} {esc(n.flabel)}</a>']
    if n.kind:
        meta.append(f'<a href="/notebook/#{slugify(n.kind)}">{esc(n.kind)}</a>')
    if n.date or getattr(n, "date_label", None):
        meta.append(f"<span>{fmt_date(n)}</span>")
    orig = (f'<p class="quiet orig">first published at <a class="ext" href="{esc(n.url_out)}" rel="noopener">'
            f'{esc(re.sub(r"^https?://(www\.)?", "", n.url_out).split("/")[0])}</a></p>') if n.url_out else ""
    def lst(items, arrow):
        return "".join(f'<a class="bl" href="{x.href}">{arrow} {esc(x.title)}</a>' for x in sorted(items, key=lambda x: x.title.lower()))
    side = ""
    if n.back:
        side += f'<div class="links"><div class="lbl">linked from · {len(n.back)}</div><div class="bls">{lst(n.back, "←")}</div></div>'
    outs = n.out - n.back
    if outs:
        side += f'<div class="links"><div class="lbl">links to · {len(outs)}</div><div class="bls">{lst(outs, "→")}</div></div>'
    mi = n.mentioned_in - n.back
    if mi:
        side += f'<div class="links"><div class="lbl">in the writing · {len(mi)}</div><div class="bls">{lst(mi, "¶")}</div></div>'
    if n.mentions:
        side += f'<div class="links"><div class="lbl">in the vault · {len(n.mentions)}</div><div class="bls">{lst(n.mentions, "↘")}</div></div>'
    # neighbours in the same folder
    sib = [x for x in FOLDER_LISTS[n.dewey] if x is not n]
    pos = FOLDER_LISTS[n.dewey].index(n)
    prev_n = FOLDER_LISTS[n.dewey][pos - 1] if pos > 0 else None
    next_n = FOLDER_LISTS[n.dewey][pos + 1] if pos + 1 < len(FOLDER_LISTS[n.dewey]) else None
    pn = '<div class="pn">'
    pn += f'<a href="{prev_n.href}">← {prev_n.id} {esc(prev_n.title)}</a>' if prev_n else "<span></span>"
    pn += f'<a href="{next_n.href}">{next_n.id} {esc(next_n.title)} →</a>' if next_n else "<span></span>"
    pn += "</div>"
    body = f"""<main class="s note">
  <div class="s-head crumb"><a href="/vault/">stacks</a> / <a href="/vault/{n.dewey}/">{n.dewey} {esc(n.flabel)}</a> / {n.id}</div>
  <h2 class="title">{esc(n.title)}</h2>
  <div class="meta">{' · '.join(meta)}</div>
  {orig}
  <article class="prose">
{body_html}
  </article>
  {side}
  {pn}
</main>"""
    sec = "0200" if n.notebook else ("2222" if n.dewey in ("2222", "2266") else None)
    write(n.href.strip("/") + "/index.html", page(n.title, body, sec, plain(n.body, 160), n.href))


def main():
    global BUILT, NCOUNT, FOLDER_LISTS
    BUILT = datetime.date.today().strftime("%Y.%m.%d")
    notes = load()
    NCOUNT = len(notes)
    idx = build_index(notes)
    for n in notes:
        n.out, n.back = set(), set()
        n.mentions, n.mentioned_in = set(), set()
    for n in notes:
        n.html = render_body(n, idx)
        for r in n.related:
            x = resolve(r, idx)
            if isinstance(x, Note) and x is not n:
                n.out.add(x)
    for n in notes:
        for o in n.out:
            o.back.add(n)
    for n in notes:
        n.mentions, n.mentioned_in = set(), set()
    terms = mention_terms(notes)
    for n in notes:
        if n.notebook:
            link_mentions(n, terms)
    FOLDER_LISTS = {}
    for n in sorted(notes, key=lambda n: n.id):
        FOLDER_LISTS.setdefault(n.dewey, []).append(n)

    for d in OWNED:
        shutil.rmtree(os.path.join(ROOT, d), ignore_errors=True)
    for n in notes:
        note_page(n, idx)

    site = json.load(open(os.path.join(SRC, "site.json")))
    shelf = json.load(open(os.path.join(SRC, "shelf.json")))
    nb = sorted([n for n in notes if n.notebook], key=lambda n: n.date or "0000", reverse=True)
    systems = [n for n in notes if n.dewey in ("2222", "2266")]
    systems.sort(key=lambda n: (-len(n.out | n.back | n.mentioned_in), n.title.lower()))

    def status_row():
        cells = []
        for s in site["status"]:
            v = esc(s["value"])
            if s.get("href"):
                v = f'<a href="{s["href"]}">{v}</a>'
            cells.append(f'<div class="cell"><div class="lbl">{esc(s["label"])}</div><div class="val">{v}</div></div>')
        return f'<div class="aside-row">{"".join(cells)}</div>'

    def folder_count(dw):
        return len(FOLDER_LISTS.get(dw, []))

    grid = [
        ("/photography/", "0100", "photography", "bach.photo"),
        ("/notebook/", "0200", "writing", f"notebook · {len(nb)}"),
        ("/library/", "0300", "the private library", "conversation"),
        ("/about/", "0400", "about", "colophon"),
        ("/deck/", "0500", "¿a qué te dedicas?", "the deck"),
        ("/vault/1100/", "1100", "intelligence and learning", f"{folder_count('1100')} notes"),
        ("/figment/", "1155", "figment archive", "2021–22"),
        ("/vault/1166/", "1166", "namada", "2022–23"),
        ("/vault/2000/", "2000", "blockchain", f"research · {folder_count('2000')}"),
        ("/vault/2100/", "2100", "privacy", f"{folder_count('2100')} notes"),
        ("/systems/", "2222", "systems", f"emergence · {folder_count('2222')}"),
        ("/vault/2266/", "2266", "technology", f"{folder_count('2266')} notes"),
        ("/shelf/", "3000", "reading shelf", f"{len(shelf)} books"),
        ("/vault/", "—", "the stacks", f"all {len(notes)} notes"),
        ("/guestbook/", "—", "guestbook", ""),
        ("/rss.xml", "—", "rss", "feed"),
    ]
    grid_html = '<div class="idx">' + "".join(
        f'<a href="{h}"><span class="n">{num}</span>{lab}<span class="desc">{d}</span></a>' for h, num, lab, d in grid) + "</div>"

    recent = " · ".join(f'{fmt_date(n)}: <a href="{n.href}">{esc(n.title)}</a>' for n in nb[:3])

    hero = PHOTOS[0]
    P = {p[0]: p for p in PHOTOS}
    def ph(p, cls=""):
        f, t, line, series, shape = p
        return (f'<a class="ph {shape} {cls}" href="/photography/#{f}"><img src="/img/photo/{f}.jpg" alt="{esc(t)}, {esc(line)}" loading="lazy">'
                f'<span class="inf"><span class="t">{esc(t)}</span><span class="d">{esc(line)}</span></span></a>')

    home = f"""<div class="s" id="index">
  <div class="s-head">0000 &mdash; index</div>
  <p>Photographer, systems thinker, writer. Making complex systems intelligible. This site is the public face of the vault. Everything connects.</p>
  {status_row()}
  {grid_html}
  <p class="quiet" style="margin-top:14px;">{recent}</p>
</div>

<div class="s" id="photo">
  <div class="s-head">0100 &mdash; photography</div>
  <h2>bach.photo</h2>
  <p>Film and digital. Processed in Capture One. Published in National Geographic, The New York Times. Three books.</p>
  <div class="gallery">
    <figure class="photo-full"><img src="/img/photo/{hero[0]}.jpg" alt="{esc(hero[1])}, {esc(hero[2])}"><figcaption class="cap"><strong>{esc(hero[1])}</strong> &middot; {esc(hero[2])}</figcaption></figure>
    <div class="photo-grid">{''.join(ph(p) for p in [P[k] for k in ('herm-raft', 'kg-ridge', 'kendra', 'rhr-ramps', 'hk-delivery', 'japan-climb')])}</div>
  </div>
  <p class="mobile-only quiet">The gallery is made for a larger screen.</p>
  <p class="quiet"><a href="/photography/">→ the full gallery, series and tear sheets</a></p>
</div>

<div class="s" id="writing">
  <div class="s-head">0200 &mdash; writing</div>
  <h2>The Notebook</h2>
  {''.join(entry(n, None) for n in nb[:5])}
  <p class="quiet" style="margin-top:14px;"><a href="/notebook/">→ all {len(nb)} entries: essays, field notes, poems, fiction</a></p>
</div>

<div class="s" id="systems">
  <div class="s-head">2222 &mdash; systems</div>
  <h2>Emergence &amp; Networks</h2>
  <p>Research notes on complex adaptive systems, network dynamics, and the structures that hold worlds together. Toward a book on emergence and the growth of networks.</p>
  <div class="nodes">{''.join(node_card(n, True) for n in systems[:6])}</div>
  <p class="quiet" style="margin-top:14px;"><a href="/systems/">→ all {len(systems)} nodes</a> · <a href="/vault/2000/">2000 blockchain</a> · <a href="/vault/2100/">2100 privacy</a></p>
</div>

<div class="s" id="library">
  <div class="s-head">0300 &mdash; the private library</div>
  <h2>The Private Library</h2>
  <p>Recurring conversation about privacy, systems, and the structures we build to live together. No logs kept — that's the point.</p>
  <p class="quiet"><a href="/library/">→ the room, and past sessions</a></p>
</div>

<div class="s" id="about">
  <div class="s-head">0400 &mdash; about</div>
  <h2>About</h2>
  <div class="about-block">
    <img class="portrait" src="/img/park.jpg" alt="Park Feierbach" width="900" height="1200">
    <p>I'm Park Feierbach. I photograph, write, and study systems — the kind that emerge from networks, from ecologies, from people building things together. The throughline: <em>how does information move through a system, and what does it change?</em></p>
    <p class="quiet"><a href="/about/">→ more</a> · <a href="/deck/">→ the deck: ¿a qué te dedicas?</a></p>
  </div>
</div>"""
    write("index.html", page(None, home, "0000", path="/"))

    # ── notebook
    counts = {k: sum(1 for n in nb if n.kind == k) for k in KINDS}
    filt = '<div class="filters"><a href="#all" data-k="" class="on">all · ' + str(len(nb)) + "</a>" + "".join(
        f'<a href="#{slugify(k)}" data-k="{k}">{k} · {counts[k]}</a>' for k in KINDS if counts[k]) + "</div>"
    nbp = f"""<div class="s">
  <div class="s-head">0200 &mdash; writing</div>
  <h2>The Notebook</h2>
  <p>Essays, field notes, poems and fiction, pulled from the vault as they are. These aren't separate blogs — they're all part of the same notebook.</p>
  {filt}
  <div class="entries">{''.join(entry(n, None) for n in nb)}</div>
</div>"""
    write("notebook/index.html", page("writing", nbp, "0200", path="/notebook/"))

    # ── systems
    sysp = f"""<div class="s">
  <div class="s-head">2222 &mdash; systems</div>
  <h2>Emergence &amp; Networks</h2>
  <p>Research notes on complex adaptive systems, network dynamics, and the structures that hold worlds together. Toward a book on emergence and the growth of networks.</p>
  <p class="quiet">{len(systems)} nodes from 2222 systems and 2266 technology, ordered by how connected they are. Dimmed words inside a note are links to notes that are not published yet.</p>
  <div class="nodes">{''.join(node_card(n) for n in systems)}</div>
  <p class="quiet" style="margin-top:18px;">nearby in the stacks: <a href="/vault/1100/">1100 intelligence and learning</a> · <a href="/vault/2000/">2000 blockchain</a> · <a href="/vault/2100/">2100 privacy</a> · <a href="/vault/1000/">1000 living and loving</a></p>
</div>"""
    write("systems/index.html", page("systems", sysp, "2222", path="/systems/"))

    # ── vault / folders
    stacks = []
    for dw in sorted(FOLDER_LISTS):
        lst = FOLDER_LISTS[dw]
        lab = lst[0].flabel
        stacks.append(f'<a href="/vault/{dw}/"><span class="n">{dw}</span>{esc(lab)}<span class="desc">{len(lst)}</span></a>')
        fp = f"""<div class="s">
  <div class="s-head"><a href="/vault/">stacks</a> / {dw}</div>
  <h2>{dw} {esc(lab)}</h2>
  <p class="quiet">{len(lst)} published note{'s' if len(lst) != 1 else ''}. Numbers follow the folder the note lives in inside the vault.</p>
  {note_list(lst)}
</div>"""
        write(f"vault/{dw}/index.html", page(f"{dw} {lab}", fp, "2222" if dw == "2222" else None, path=f"/vault/{dw}/"))
    vp = f"""<div class="s">
  <div class="s-head">—— &mdash; the stacks</div>
  <h2>The Stacks</h2>
  <p>Codex Magna is an Obsidian vault, numbered like a library. This is the part of it that is public: {len(notes)} notes across {len(FOLDER_LISTS)} folders, every link between them kept. Start anywhere.</p>
  <p><a class="graph-link" href="/vault/graph/">see the stacks in three dimensions &rarr;</a></p>
  <div class="idx">{''.join(stacks)}</div>
  <div class="s-head" style="margin-top:36px;">all notes, a–z</div>
  <div class="az">{''.join(f'<a href="{n.href}"><span class="n">{n.id}</span>{esc(n.title)}</a>' for n in sorted(notes, key=lambda n: n.title.lower().lstrip("'\"¿")))}</div>
</div>"""
    write("vault/index.html", page("the stacks", vp, None, path="/vault/"))

    # ── the graph: every note and link, for vault/graph/ (template in _src/graph.html)
    gn = sorted(notes, key=lambda n: n.id)
    gi = {id(n): i for i, n in enumerate(gn)}
    gf = sorted({(n.dewey, n.flabel) for n in gn})
    gfi = {d: i for i, (d, _) in enumerate(gf)}
    ge = {}
    for n in gn:
        for o in n.out:
            ge[tuple(sorted((gi[id(n)], gi[id(o)])))] = 0
    for n in gn:
        for o in n.mentions:
            ge.setdefault(tuple(sorted((gi[id(n)], gi[id(o)]))), 1)
    gdata = {"folders": [{"d": d, "l": l} for d, l in gf],
             "nodes": [[n.title, gfi[n.dewey], n.href, 1 if n.notebook else 0, n.id] for n in gn],
             "edges": [[a, b, m] for (a, b), m in sorted(ge.items())]}
    gjson = json.dumps(gdata, separators=(",", ":"), ensure_ascii=False).replace("</", "<\\/")
    write("vault/graph/index.html", open(os.path.join(SRC, "graph.html")).read().replace("__DATA__", gjson))

    # ── photography
    cover = next(p for p in PHOTOS if p[0] == PHOTO_COVER)
    series = []
    MONTHS = {m: i for i, m in enumerate(["january", "february", "march", "april", "may", "june", "july", "august",
                                         "september", "october", "november", "december"], 1)}
    def latest(sname):  # newest photo in a series, from the dates in its captions
        best = (0, 0)
        for p in PHOTOS:
            if p[3] != sname:
                continue
            t = f"{p[1]} {p[2]}".lower()
            for y in re.finditer(r"(?:([a-z]+)\s+)?(?:\d{1,2}\s+)?(20\d\d)", t):
                best = max(best, (int(y.group(2)), MONTHS.get(y.group(1) or "", 0)))
        return best
    for sname in sorted(SERIES, key=latest, reverse=True):
        ps = [p for p in PHOTOS if p[3] == sname and p is not cover]
        from PIL import Image
        def ar(f):
            w, h = Image.open(os.path.join(ROOT, "img/photo", f + ".jpg")).size
            return w / h
        if not ps:
            continue
        row = len(ps) <= 3
        cells = "".join(
            f'<figure class="ph {p[4]}" id="{p[0]}"' + (f' style="flex:{ar(p[0]):.3f}"' if row else "") + f'><img src="/img/photo/{p[0]}.jpg" alt="{esc(p[1])}, {esc(p[2])}" loading="lazy">'
            f'<figcaption class="inf"><span class="t">{esc(p[1])}</span><span class="d">{esc(p[2])}</span></figcaption></figure>' for p in ps)
        cols = "row" if row else ("two" if len(ps) <= 4 else "three")
        series.append(f'<div class="s-head series">{esc(sname)}</div><div class="photo-grid {cols}">{cells}</div>')
    tears = "".join(
        f'<figure class="ph tear"><img src="/img/photo/{f}.jpg" alt="{esc(t)}, {esc(d)}" loading="lazy">'
        f'<figcaption class="inf"><span class="t">{esc(t)}</span><span class="d">{esc(d)}</span></figcaption></figure>' for f, t, d in TEARSHEETS)
    pp = f"""<div class="s">
  <div class="s-head">0100 &mdash; photography</div>
  <h2>bach.photo</h2>
  <p>Film and digital. Processed in Capture One. Published in National Geographic, The New York Times. Three books.</p>
  <p class="quiet">Studio manager for Robert Clark, National Geographic photographer, two years. Every scientific caption in <em>Feathers: Displays of Brilliant Plumage</em> (Chronicle, 2016).</p>
  <div class="gallery">
    <figure class="photo-full"><img src="/img/photo/{cover[0]}.jpg" alt="{esc(cover[1])}, {esc(cover[2])}"><figcaption class="cap"><strong>{esc(cover[1])}</strong> &middot; {esc(cover[2])}</figcaption></figure>
    {''.join(series)}
    <div class="s-head series">tear sheets</div>
    <div class="photo-grid tears">{tears}</div>
  </div>
  <p class="mobile-only quiet">The gallery is made for a larger screen. Come back to it at a desk.</p>
  <p class="quiet" style="margin-top:16px;">More of the work, with the story around it: <a href="/deck/">the deck</a>. Field notes from the road: <a href="/notebook/#field-note">0200 field notes</a>.</p>
</div>"""
    write("photography/index.html", page("photography", pp, "0100", path="/photography/"))

    # ── library
    lib_notes = [n for n in notes if n.title.startswith("Private Library")]
    privacy = idx.get("privacy")
    lp = f"""<div class="s">
  <div class="s-head">0300 &mdash; the private library</div>
  <h2>The Private Library</h2>
  <p>Recurring conversation about privacy, systems, and the structures we build to live together. No logs kept — that's the point.</p>
  <p>Named for the discussion series I ran at Namada on privacy as social infrastructure.</p>
  <div class="chat">
    <div class="chat-bar"><span class="rm">#private-library</span><span>closed · opens in 0.3</span></div>
    <div class="chat-log">
      <div class="m"><span class="ts">[——:——] </span><span class="nk nk-s">*sys*</span> <span class="tx sys">the room isn't open yet. when it is: no login, pick a name on the way in, logs clear every week, encrypted.</span></div>
    </div>
    <div class="chat-in"><input type="text" placeholder="say something..." disabled aria-label="chat input, disabled"><button disabled>send</button></div>
  </div>
  <div class="s-head" style="margin-top:36px;">past sessions</div>
  {note_list(sorted(lib_notes, key=lambda n: n.date or ""))}
  <p class="quiet" style="margin-top:14px;">background reading: {link_html('Privacy', 'privacy', idx)} · {link_html('anatomy of privacy', None, idx)} · {link_html('privacy in crypto as an ethos', None, idx)} · <a href="/vault/2100/">2100 privacy</a></p>
</div>"""
    write("library/index.html", page("the private library", lp, "0300", path="/library/"))

    # ── shelf
    def short(t):
        t = re.sub(r"\s*\([^)]*\)\s*$", "", t)
        return t.split(":")[0].strip()
    books = sorted(shelf, key=lambda b: (b.get("year") or "0000", short(b["title"]).lower()), reverse=True)
    rows = []
    for b in books:
        three = f'<div class="three">{esc(b["three"])}</div>' if b.get("three") else ""
        hl = f' · {b["highlights"]} highlights' if b.get("highlights") else ""
        rows.append(f'<div class="book"><span class="yr">{b.get("year") or "—"}</span><span class="bt">{esc(short(b["title"]))}</span>'
                    f'<span class="ba">{esc(b.get("author", ""))}{hl}</span>{three}</div>')
    notes_on_books = [x for x in (idx.get(k) for k in ["the mushroom at the end of the world", "the structure of scientific revolutions",
                      "benasayag-miguel-the tyranny of algorithms", "thinking in systems", "present shock", "aniara"]) if isinstance(x, Note)]
    sp = f"""<div class="s">
  <div class="s-head">3000 &mdash; reading shelf</div>
  <h2>Reading Shelf</h2>
  <p class="quiet">From the vault's book notes, most recent year first.</p>
  <div class="shelf">{''.join(rows)}</div>
  <div class="s-head" style="margin-top:36px;">longer notes on books</div>
  {note_list(notes_on_books)}
</div>"""
    write("shelf/index.html", page("reading shelf", sp, None, path="/shelf/"))

    # ── figment
    blk = [x for x in FOLDER_LISTS.get("2000", [])]
    blk.sort(key=lambda n: (-len(n.out | n.back | n.mentioned_in), n.title.lower()))
    fp = f"""<div class="s">
  <div class="s-head">1155 &mdash; figment archive</div>
  <h2>Figment, 2021–2022</h2>
  <div class="career">Protocol Research Manager. Led 11 analysts through 70+ networks. Built "Codex," the knowledge system that became our performance reports.</div>
  <p>I learned everything I could about crypto, and learned that I have a researcher's mind. I began to write technical documents.</p>
  <p class="quiet">Most of what came out of those years lives in <a href="/vault/2000/">2000 blockchain</a>: protocol notes, governance, validators, canary networks. The most connected:</p>
  <div class="nodes">{''.join(node_card(n) for n in blk[:9])}</div>
  <div class="s-head" style="margin-top:36px;">after figment</div>
  <div class="career">Namada, Community Research Manager, 2022–2023 · Radiant Commons (Penumbra), Chief Executive Officer, 2023–2025. Wound down completely, December 2025.</div>
  {note_list(FOLDER_LISTS.get("1166", []))}
  <div class="s-head" style="margin-top:36px;">published elsewhere</div>
  <div class="idx">{''.join(f'<a class="ext" href="{u}" rel="noopener"><span class="n">{y}</span>{esc(t)}<span class="desc">{esc(w)}</span></a>' for y, t, w, u in ELSEWHERE[:5])}</div>
</div>"""
    write("figment/index.html", page("figment archive", fp, None, path="/figment/"))

    # ── about
    ap = f"""<div class="s">
  <div class="s-head">0400 &mdash; about</div>
  <h2>About</h2>
  <div class="about-block">
    <img class="portrait" src="/img/park.jpg" alt="Park Feierbach" width="900" height="1200">
    <p>I'm Park Feierbach. I photograph, write, and study systems — the kind that emerge from networks, from ecologies, from people building things together. The throughline: <em>how does information move through a system, and what does it change?</em></p>
    <div class="career">Anthropology (UGA, 2012) → photographer &amp; archivist (National Geographic, three books) → Protocol Research (Figment) → Community Research (Namada) → CEO, Radiant Commons (Penumbra) → writing</div>
    <p id="now">I am dedicated to stories. What I do is examine what is happening and help people understand it.</p>
    <p>Writing my novel is the most meaningful thing I have ever done, even though it is not finished. <em>Los Cielos Desaparecen.</em></p>
    <p class="quiet">The long version, in forty slides: <a href="/deck/">¿a qué te dedicas?</a></p>
    <p>The name pantalaimon is a daemon who never settled. This site is hand-coded, tracks nothing, and mirrors the structure of the vault it grew from.</p>
    <div class="s-head" style="margin-top:28px;">published elsewhere</div>
    <div class="idx one">{''.join(f'<a class="ext" href="{u}" rel="noopener"><span class="n">{y}</span>{esc(t)}<span class="desc">{esc(w)}</span></a>' for y, t, w, u in ELSEWHERE)}</div>
    <div class="colophon">
      IBM Plex Mono, served from this site. Written in Obsidian, built by a small Python script into plain HTML, hosted on GitHub Pages. No cookies, no analytics, no third-party requests; AI crawlers are asked to stay out in <a href="/robots.txt">robots.txt</a>. Source on <a href="https://github.com/attainable-sys/park-attainable-systems">GitHub</a>. Inspired by <a href="https://32bit.cafe">32-Bit Cafe</a> and <a href="https://wiki.xxiivv.com">XXIIVV</a>.
    </div>
    <div class="badges"><div class="b88">codex magna</div><div class="b88">sapere aude</div><div class="b88">indie web</div><div class="b88">no tracking</div><div class="b88">made by hand</div></div>
  </div>
</div>"""
    write("about/index.html", page("about", ap, "0400", path="/about/"))

    # ── guestbook
    gp = """<div class="s">
  <div class="s-head">—— &mdash; guestbook</div>
  <h2>Guestbook</h2>
  <p>The guestbook opens with the private library. Until then, write to <a href="mailto:park@attainable.systems">park@attainable.systems</a>.</p>
</div>"""
    write("guestbook/index.html", page("guestbook", gp, None, path="/guestbook/"))

    # ── 404
    write("404.html", page("not found", f"""<div class="s"><div class="s-head">404</div><h2>Not in the stacks.</h2>
  <p>That page isn't here. Try <a href="/vault/">the stacks</a> or <a href="/">the index</a>.</p></div>""", None, path="/404.html"))

    # ── rss
    items = []
    for n in nb:
        d = datetime.datetime.strptime(n.date, "%Y-%m-%d") if n.date else datetime.datetime(2026, 11, 6)
        items.append(f"""<item><title>{esc(n.title)}</title><link>{SITE}{n.href}</link><guid>{SITE}{n.href}</guid>
<pubDate>{d.strftime('%a, %d %b %Y 12:00:00 +0000')}</pubDate><category>{esc(n.kind or '')}</category>
<description>{esc(n.html)}</description></item>""")
    write("rss.xml", f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel><title>codex magna · notebook</title><link>{SITE}/notebook/</link>
<description>Park Feierbach's notebook.</description><language>en</language>
{''.join(items)}
</channel></rss>
""")
    # ── sitemap
    urls = ["/", "/photography/", "/notebook/", "/systems/", "/library/", "/about/", "/shelf/", "/figment/", "/vault/", "/vault/graph/", "/deck/"]
    urls += [f"/vault/{d}/" for d in sorted(FOLDER_LISTS)] + [n.href for n in notes]
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join(f"<url><loc>{SITE}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    print(f"built {len(notes)} notes, {len(nb)} notebook entries, {len(FOLDER_LISTS)} folders")


if __name__ == "__main__":
    main()
