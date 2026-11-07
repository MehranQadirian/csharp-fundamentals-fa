#!/usr/bin/env python3
"""Builds the C# fundamentals handout: HTML -> PDF (Chromium) -> merge with cover/back."""
import re, sys, html, glob, os, json, importlib
sys.path.insert(0, os.path.dirname(__file__))
ROOT = os.path.dirname(os.path.abspath(__file__))
VERSION = os.environ.get("BOOK_VERSION", "dev")
ZW = "‌"
PD = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
def pd(x): return str(x).translate(PD)

ICON = {
 "imp": '<svg viewBox="0 0 20 20"><path d="M10 2 19 18H1Z" fill="#fff"/><path d="M10 7.5v5M10 14.2v1.4" stroke="#7A4A00" stroke-width="2" stroke-linecap="round"/></svg>',
 "genz": '<svg viewBox="0 0 20 20"><path d="M3 3h14a1 1 0 0 1 1 1v9a1 1 0 0 1-1 1H9l-4 3.5V14H3a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1Z" fill="#fff"/><circle cx="7" cy="8.5" r="1.1" fill="#0A5F43"/><circle cx="10" cy="8.5" r="1.1" fill="#0A5F43"/><circle cx="13" cy="8.5" r="1.1" fill="#0A5F43"/></svg>',
 "concept": '<svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8" fill="none" stroke="#fff" stroke-width="1.8"/><path d="m13.5 6.5-2 5-5 2 2-5Z" fill="#fff"/></svg>',
 "pit": '<svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.2" fill="#fff"/><path d="m6.5 6.5 7 7m0-7-7 7" stroke="#8E1B1B" stroke-width="2.2" stroke-linecap="round"/></svg>',
 "more": '<svg viewBox="0 0 20 20"><path d="M3 4h6a1 1 0 0 1 1 1v11a2 2 0 0 0-2-2H3ZM17 4h-6a1 1 0 0 0-1 1v11a2 2 0 0 1 2-2h5Z" fill="#111"/></svg>',
 "ex": '<svg viewBox="0 0 20 20"><path d="m3 17 1-4L14 3l3 3L7 16Z" fill="#fff"/></svg>',
}
LABEL = {"imp": "نکته‌ی مهم", "genz": "نکته‌ی خودمونی", "concept": "نگاه مفهومی", "pit": "اشتباه رایج", "more": "مطالعه‌ی بیشتر"}

# ---------------------------------------------------------------- C# highlighter
KW = set("""abstract as base bool break byte case catch char checked class const continue decimal default delegate do double else enum
event explicit extern false finally fixed float for foreach goto if implicit in int interface internal is lock long namespace new null
object operator out override params private protected public readonly ref return sbyte sealed short sizeof stackalloc static string
struct switch this throw true try typeof uint ulong unchecked unsafe ushort using virtual void volatile while var when yield
record init required get set value nameof""".split())
TYPES = set("Console Math Convert Random String Char Int32 Int64 Double Decimal Boolean DateTime TimeSpan Program Environment Exception Array List MidpointRounding Single Byte Thread Stopwatch".split())
TOK = re.compile(r'''(?P<cm>//[^\n]*|/\*.*?\*/)
 |(?P<s>@\$?"(?:""|[^"])*"|\$@"(?:""|[^"])*"|\$?"(?:\\.|[^"\\\n])*"|'(?:\\.|[^'\\\n])+')
 |(?P<n>\b0[xXbB][0-9A-Fa-f_]+[uUlL]*\b|\b\d[\d_]*(?:\.\d+)?(?:[eE][+-]?\d+)?[fFmMdDuUlL]*\b)
 |(?P<w>[A-Za-z_]\w*)''', re.S | re.X)

def hi_cs(code):
    code = code.strip("\n").replace("\t", "    ")
    segs, pos = [], 0
    for m in TOK.finditer(code):
        if m.start() > pos: segs.append((None, code[pos:m.start()]))
        kind = m.lastgroup; txt = m.group()
        if kind == "w":
            nxt = code[m.end():m.end()+1]
            if txt in KW: cls = "k"
            elif txt in TYPES: cls = "t"
            elif nxt == "(" : cls = "m"
            elif txt[0].isupper() and nxt == "." : cls = "t"
            else: cls = None
        else:
            cls = {"cm": "cm", "s": "s", "n": "n"}[kind]
        segs.append((cls, txt)); pos = m.end()
    if pos < len(code): segs.append((None, code[pos:]))
    lines, cur = [], ""
    for cls, txt in segs:
        parts = txt.split("\n")
        for i, part in enumerate(parts):
            if i > 0: lines.append(cur); cur = ""
            e = html.escape(part, quote=False)
            cur += f'<span class="{cls}">{e}</span>' if cls and part else e
    lines.append(cur)
    return "".join(f'<span class="l">{l if l else " "}</span>' for l in lines)

# ---------------------------------------------------------------- state
EX = {}       # id -> title
ANS = []      # ids that have answers
TOC = []      # (level, id, title)
REFS = set()  # anchors that must be link targets
PAGES = {}    # anchor -> page number (from previous pass)
figs = importlib.import_module("figs")

def exlabel(i):
    if i[0] in "BIA" and i[1:].isdigit():
        return {"B": "مبتدی", "I": "متوسط", "A": "پیشرفته"}[i[0]] + " " + pd(i[1:])
    return pd(i)
def pgref(anchor):
    REFS.add(anchor)
    return pd(PAGES.get(anchor, "000"))

def proc_boxes(s):
    def box(m):
        k, t, body = m.group(1), m.group(2), m.group(3)
        title = t or LABEL[k]
        if t and k in LABEL and k != "more": title = LABEL[k] + " · " + t
        elif t: title = LABEL[k] + " · " + t
        return f'<div class="box {k}"><div class="bt">{ICON[k]}<span>{title}</span></div><div class="bb">{body}</div></div>'
    s = re.sub(r'<(imp|genz|concept|pit|more)(?: t="([^"]*)")?>(.*?)</\1>', box, s, flags=re.S)
    def ex(m):
        i, t, body = m.group(1), m.group(2), m.group(3)
        EX[i] = t
        a = f"ans-{i}"
        REFS.add(a)
        return (f'<div class="box ex" id="ex-{i}"><div class="bt"><span class="l">{ICON["ex"]}<span>تمرین {exlabel(i)} · {t}</span></span>'
                f'<a class="ans" href="#{a}">پاسخ ← ص {pgref(a)}</a></div><div class="bb">{body}</div></div>')
    s = re.sub(r'<ex id="([^"]+)" t="([^"]*)">(.*?)</ex>', ex, s, flags=re.S)
    return s

def proc_code(s):
    def cs(m):
        attrs, body = m.group(1), m.group(2)
        t = re.search(r't="([^"]*)"', attrs)
        nt = "" if t else " nt"
        title = f'<div class="ct">{t.group(1)}</div>' if t else ""
        return f'<div class="codebox{nt}">{title}<pre class="code">{hi_cs(body)}</pre></div>'
    s = re.sub(r'<cs([^>]*)>(.*?)</cs>', cs, s, flags=re.S)
    def out(m):
        attrs, body = m.group(1), m.group(2)
        t = re.search(r't="([^"]*)"', attrs)
        title = t.group(1) if t else "خروجی برنامه"
        return f'<div class="out"><div class="ot">{title}</div><pre>{html.escape(body.strip(chr(10)), quote=False)}</pre></div>'
    return re.sub(r'<out([^>]*)>(.*?)</out>', out, s, flags=re.S)

def proc_figs(s, ch):
    cnt = [0]
    def fig(m):
        name, cap = m.group(1), m.group(2)
        cnt[0] += 1
        svg = getattr(figs, name)()
        return f'<div class="fig">{svg}<div class="cap"><b>شکل {pd(ch)}-{pd(cnt[0])}</b> · {cap}</div></div>'
    return re.sub(r'<fig name="([^"]+)" cap="([^"]*)"\s*/>', fig, s)

def proc_headings(s, ch):
    n = [0]
    def h2(m):
        n[0] += 1
        i = f"ch{ch}-s{n[0]}"
        TOC.append((2, i, re.sub(r"<[^>]+>", "", m.group(1))))
        REFS.add(i)
        return f'<h2 id="{i}">{m.group(1)}</h2>'
    return re.sub(r'<h2>(.*?)</h2>', h2, s, flags=re.S)

def proc_chapter(s, ch, fid):
    m = re.match(r'\s*<chapter ([^>]*)/?>', s)
    a = dict(re.findall(r'(\w+)="([^"]*)"', m.group(1)))
    s = s[m.end():]
    lab = a.get("label", f"فصل {pd(a['n'])}")
    num = a["n"] if not a["n"].isdigit() else pd(a["n"])
    TOC.append((1, fid, f'{lab}: {a["title"]}' if "label" not in a else a["title"]))
    REFS.add(fid)
    s = re.sub(r'<goals>(.*?)</goals>', lambda g: f'<div class="goals"><div class="gt">در این فصل یاد می‌گیرید</div><ul>{g.group(1)}</ul></div>', s, flags=re.S)
    head = (f'<div class="ch-head"><div class="ch-num">{num}</div><div><div class="lab">{lab}</div>'
            f'<h1>{a["title"]}</h1><div class="sub">{a.get("sub","")}</div></div></div>')
    s = proc_headings(s, fid)
    return f'<section class="chapter" id="{fid}">{head}{s}</section>'

def proc_answers(s):
    def ans(m):
        i, body = m.group(1), m.group(2)
        REFS.add(f"ex-{i}"); ANS.append(i)
        back = f'<a href="#ex-{i}">↩ تمرین (ص {pgref("ex-"+i)})</a>'
        return (f'<div class="ans-item" id="ans-{i}"><div class="ah"><span>پاسخ تمرین {exlabel(i)} · {EX.get(i,"")}</span>{back}</div>'
                f'<div class="ab">{body}</div></div>')
    return re.sub(r'<ans id="([^"]+)">(.*?)</ans>', ans, s, flags=re.S)

LAT = re.compile(r'(\.NET(?: Framework| Core| MAUI| IoT| \d+)?|VB\.NET|C# \d+|C#|F#)')
LRI, PDI = "\u2066", "\u2069"
def persian_fix(s):
    parts = re.split(r'(<pre.*?</pre>|<c>.*?</c>|<svg.*?</svg>)', s, flags=re.S)
    FA = "\u0600-\u06FF"
    for i, t in enumerate(parts):
        if i % 2 == 1:
            if t.startswith("<svg"):
                parts[i] = re.sub(r'(>)([^<>]*)(<)', lambda m: m.group(1) + LAT.sub(lambda k: LRI + k.group(1) + PDI, m.group(2)) + m.group(3), t)
            continue
        t = re.sub(rf'(?<![{FA}])(ن?می) (?=[{FA}])', lambda m: m.group(1) + ZW, t)
        t = re.sub(rf'(?<=[{FA}]) (ها|های|هایی|تر|ترین)(?![{FA}])', lambda m: ZW + m.group(1), t)
        t = re.sub(r'(>)([^<>]*)(<)', lambda m: m.group(1) + LAT.sub(lambda k: LRI + k.group(1) + PDI, m.group(2)) + m.group(3), t)
        parts[i] = t
    return "".join(parts)

def build_body():
    global EX, ANS, TOC
    EX.clear(); ANS.clear(); TOC.clear()
    files = sorted(glob.glob(f"{ROOT}/chapters/*.html"))
    secs, final_idx = [], []
    for f in files:
        raw = open(f, encoding="utf-8").read()
        mm = re.match(r'\s*<chapter ([^>]*)/?>', raw)
        n = re.search(r'n="([^"]*)"', mm.group(1)).group(1)
        fid = f"ch{n}" if n.isdigit() else os.path.basename(f).split(".")[0]
        ch = n if n.isdigit() else {"final": "ف", "answers": "پ"}.get(fid, "؟")
        secs.append((fid, ch, raw))
    # pass A: exercises/answers need registry -> process exercises first by stripping order dependence
    out = []
    for fid, ch, raw in secs:
        if fid == "answers": continue
        s = proc_chapter(raw, ch if ch.isdigit() else fid, fid)
        s = proc_code(proc_boxes(s))
        s = proc_figs(s, ch if ch.isdigit() else "ف")
        out.append(s)
    for fid, ch, raw in secs:
        if fid != "answers": continue
        s = proc_chapter(raw, fid, fid)
        s = proc_answers(s)
        s = proc_code(proc_boxes(s))
        # quick index
        groups = {}
        for i in ANS: groups.setdefault(i.split(".")[0] if "." in i else i[0], []).append(i)
        out.append(s)
    body = "\n".join(out)
    return body

def toc_html():
    rows = ['<div class="toc">']
    for lvl, i, t in TOC:
        REFS.add(i)
        rows.append(f'<a class="c{lvl}" href="#{i}"><span>{t}</span><span class="dots"></span><span class="pn">{pd(PAGES.get(i,"0"))}</span></a>')
    rows.append('</div>')
    return "\n".join(rows)

def answer_index():
    # grouped quick-find table of every exercise -> answer page
    names = [("chapter", "تمرین‌های داخل فصل‌ها"), ("B", "تمرین‌های بیشتر · مبتدی"), ("I", "تمرین‌های بیشتر · متوسط"), ("A", "تمرین‌های بیشتر · پیشرفته")]
    def grp(i): return "chapter" if i[0].isdigit() else i[0]
    h = []
    for key, title in names:
        ids = [i for i in ANS if grp(i) == key]
        if not ids: continue
        h.append(f'<h3>{title}</h3><div class="idx">')
        for i in ids:
            h.append(f'<a href="#ans-{i}"><span>{exlabel(i)}</span><span class="pn">ص {pd(PAGES.get("ans-"+i,"0"))}</span></a>')
        h.append('</div>')
    return "\n".join(h)

def proc_boxes_front(s):
    keep = dict(EX)
    r = proc_boxes(s)
    return r

def assemble():
    body = build_body()
    front = open(f"{ROOT}/front.html", encoding="utf-8").read()
    front = proc_boxes_front(front).replace("{{TOC}}", toc_html()).replace("{{VERSION}}", VERSION)
    body = body.replace("{{ANSINDEX}}", answer_index())
    # page refs inside front/body outside exercises are not used further
    doc = (f'<!doctype html><html lang="fa" dir="rtl"><head><meta charset="utf-8"><title>مبانی کامپیوتر - سی‌شارپ</title>'
           f'<link rel="stylesheet" href="style.css"></head><body><div class="blankpg"></div><div class="blankpg"></div>{front}{body}<div class="blankpg end"></div><div class="blankpg end"></div></body></html>')
    # link targets: wrap anchors that are referenced but only exist as ids -> ensure at least one <a href> exists (already via REFS users)
    doc = persian_fix(doc)
    return doc

def render(htmlp, pdfp, footer=True):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page()
        pg.goto("file://" + htmlp); pg.wait_for_load_state("networkidle")
        pg.evaluate("document.fonts.ready")
        kw = dict(path=pdfp, format="A4", print_background=True)
        if footer:
            kw.update(display_header_footer=True, margin=dict(top="15mm", bottom="17mm", left="15mm", right="15mm"),
                      header_template="<span></span>",
                      footer_template='<div style="width:100%;font-family:Vazirmatn,sans-serif;font-size:8px;color:#333;padding:0 15mm;display:flex;justify-content:space-between;direction:ltr"><span>C# Fundamentals</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>')
        else:
            kw.update(margin=dict(top="0", bottom="0", left="0", right="0"), prefer_css_page_size=True)
        pg.pdf(**kw); b.close()

def get_pages(pdfp):
    from pypdf import PdfReader
    r = PdfReader(pdfp)
    return {k.lstrip("/"): r.get_destination_page_number(v) + 1 for k, v in r.named_destinations.items()}

if __name__ == "__main__":
    global_pages = {}
    for it in range(3):
        PAGES.clear(); PAGES.update(global_pages)
        REFS.clear()
        doc = assemble()
        open(f"{ROOT}/body.html", "w", encoding="utf-8").write(doc)
        render(f"{ROOT}/body.html", f"{ROOT}/body.pdf")
        new = get_pages(f"{ROOT}/body.pdf")
        missing = [r for r in REFS if r not in new]
        print(f"pass {it}: dests={len(new)} missing={missing[:8]}")
        if new == global_pages: break
        global_pages = new
    from pypdf import PdfReader, PdfWriter
    w = PdfWriter()
    for f in ["cover.pdf", "body.pdf", "back.pdf"]:
        p = f"{ROOT}/{f}"
        if os.path.exists(p):
            pgs = list(PdfReader(p).pages)
            if f == "body.pdf": pgs = pgs[2:-2]   # drop placeholders (they only keep numbering = viewer page number)
            if f == "back.pdf": w.add_blank_page(width=595.28, height=841.89)   # blank page before the back cover
            for pg in pgs: w.add_page(pg)
            if f == "cover.pdf": w.add_blank_page(width=595.28, height=841.89)  # blank page after the cover
    w.add_metadata({"/Title": "مبانی کامپیوتر - زبان برنامه‌نویسی سی‌شارپ", "/Author": "Mehran Ghadirian", "/Subject": "C# Fundamentals (Persian) - v" + VERSION, "/Keywords": "C#, programming, Persian, handout"})
    os.makedirs(f"{ROOT}/dist", exist_ok=True)
    with open(f"{ROOT}/dist/C-Sharp-Fundamentals.pdf", "wb") as fh: w.write(fh)
    print("pages:", len(w.pages))
