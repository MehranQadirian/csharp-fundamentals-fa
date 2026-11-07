"""SVG drawing helpers. Fills are light tints, strokes/text are dark -> readable in black & white print."""
import html
INK = "#14121F"; BR = "#2A1766"; AC = "#5B2FD0"; MU = "#454059"
F1 = "#EEE8FC"; F2 = "#E1EDFB"; F3 = "#DFF2E7"; F4 = "#FFEFC4"; F5 = "#FBE1E1"; F6 = "#F1F1F4"
S_BLUE = "#0B4A85"; S_GRN = "#0A5F43"; S_AMB = "#7A4A00"; S_RED = "#8E1B1B"

DEFS = f'''<defs>
<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="{BR}"/></marker>
<marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="{S_RED}"/></marker>
<pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="6" height="6" fill="{F4}"/><line x1="0" y1="0" x2="0" y2="6" stroke="#B58A2A" stroke-width="2"/></pattern>
<pattern id="dots" width="7" height="7" patternUnits="userSpaceOnUse"><rect width="7" height="7" fill="{F3}"/><circle cx="3.5" cy="3.5" r="1.3" fill="#3C8F6B"/></pattern>
</defs>'''

def svg(w, h, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{DEFS}{body}</svg>'

def T(x, y, s, size=12, a="c", w=400, fill=INK, mono=False, extra=""):
    """a: c=center, l=left edge, r=right edge (visual, independent of direction)."""
    anchor = {"c": "middle", "l": "start", "r": "end"}[a]
    d = "ltr" if mono else "rtl"
    # in rtl, svg 'start' means right edge, so swap
    if not mono and a in "lr": anchor = {"l": "end", "r": "start"}[a]
    cls = ' class="mono"' if mono else ""
    lines = str(s).split("\n")
    out = []
    for i, ln in enumerate(lines):
        out.append(f'<text x="{x}" y="{y + i * size * 1.5:.1f}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}" direction="{d}"{cls} style="white-space:pre" {extra}>{html.escape(ln, quote=False)}</text>')
    return "".join(out)

def R(x, y, w, h, fill=F1, stroke=BR, rx=6, dash=None, sw=1.6):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{da}/>'

def L(x1, y1, x2, y2, arrow=False, dash=None, sw=1.6, color=BR, back=False, red=False):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    mk = ""
    m = "arr" if red else "ar"
    if arrow: mk = f' marker-end="url(#{m})"'
    if back: mk += f' marker-start="url(#{m})"'
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}"{da}{mk}/>'

def P(pts, arrow=True, dash=None, sw=1.6, color=BR, red=False):
    d = "M" + " L".join(f"{x} {y}" for x, y in pts)
    da = f' stroke-dasharray="{dash}"' if dash else ""
    m = "arr" if red else "ar"
    mk = f' marker-end="url(#{m})"' if arrow else ""
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}"{da}{mk} stroke-linejoin="round"/>'

def box(x, y, w, h, label, fill=F1, stroke=BR, size=12, mono=False, rx=6, dash=None, w_=400, sw=1.6):
    n = label.count("\n") + 1
    ty = y + h / 2 + size * 0.35 - (n - 1) * size * 0.75
    return R(x, y, w, h, fill, stroke, rx, dash, sw) + T(x + w / 2, ty, label, size, "c", w_, INK, mono)

def term(cx, cy, w, h, label, fill=F3, size=12, mono=False):
    return box(cx - w / 2, cy - h / 2, w, h, label, fill, S_GRN, size, mono, rx=h / 2)

def dia(cx, cy, w, h, label, fill=F4, size=11.5, mono=False):
    pts = f"{cx},{cy-h/2} {cx+w/2},{cy} {cx},{cy+h/2} {cx-w/2},{cy}"
    n = label.count("\n") + 1
    ty = cy + size * 0.35 - (n - 1) * size * 0.75
    return f'<polygon points="{pts}" fill="{fill}" stroke="{S_AMB}" stroke-width="1.6"/>' + T(cx, ty, label, size, "c", 500, INK, mono)

def io(cx, cy, w, h, label, fill=F2, size=12, mono=False):
    k = 14
    pts = f"{cx-w/2+k},{cy-h/2} {cx+w/2+k},{cy-h/2} {cx+w/2-k},{cy+h/2} {cx-w/2-k},{cy+h/2}"
    n = label.count("\n") + 1
    ty = cy + size * 0.35 - (n - 1) * size * 0.75
    return f'<polygon points="{pts}" fill="{fill}" stroke="{S_BLUE}" stroke-width="1.6"/>' + T(cx, ty, label, size, "c", 400, INK, mono)

def proc(cx, cy, w, h, label, fill=F1, size=12, mono=False):
    return box(cx - w / 2, cy - h / 2, w, h, label, fill, BR, size, mono, rx=4)

def badge(cx, cy, n, r=11, fill=BR, color="#fff"):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"/>' + T(cx, cy + 4.3, str(n), 12, "c", 700, color, mono=True)

def codeblock(x, y, lines, size=12.5, lh=22, w=None, fill="#F5F3FB"):
    """lines: list of str (mono, LTR). returns svg and bottom y"""
    w = w or max(len(l) for l in lines) * size * 0.6 + 24
    h = len(lines) * lh + 14
    out = [R(x, y, w, h, fill, "#8C82BF", 6, None, 1.3)]
    for i, l in enumerate(lines):
        out.append(T(x + 12, y + 22 + i * lh - 4, l, size, "l", 400, INK, True))
    return "".join(out), h
