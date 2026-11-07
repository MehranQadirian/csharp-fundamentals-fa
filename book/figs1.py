from figbase import *

# ======================= فصل ۱ =======================
def f_pipeline():
    W, H = 680, 215
    o = []
    steps = [("کد منبع\nProgram.cs", F1, "شما می‌نویسید"),
             ("کامپایلر\nRoslyn", F4, "ترجمه و بررسی نوشتار"),
             ("کد میانی IL\nداخل فایل exe یا dll", F2, "مستقل از سخت‌افزار"),
             ("محیط اجرا\nCLR + JIT", F3, "ترجمه‌ی لحظه‌ای"),
             ("کد ماشین\nاجرا روی CPU", F5, "نتیجه روی کنسول")]
    bw, gap = 108, 30
    for i, (lab, fill, cap) in enumerate(steps):
        x = 672 - bw - i * (bw + gap)
        o.append(box(x, 60, bw, 70, lab, fill, BR, 11.5))
        o.append(T(x + bw / 2, 152, cap, 10, "c", 400, MU))
        o.append(badge(x + bw - 4, 60, i + 1, 10))
        if i < 4: o.append(L(x - 1, 95, x - gap + 2, 95, True))
    # brackets
    xr = 672; xm = 672 - 3 * (bw + gap) + gap  # end of step 3
    o.append(P([(xr, 38), (xr, 28), (xm, 28), (xm, 38)], False, None, 1.6, S_AMB))
    o.append(T((xr + xm) / 2, 20, "زمان کامپایل (Compile time) ؛ قبل از اجرا", 11.5, "c", 700, S_AMB))
    xr2 = 672 - 3 * (bw + gap); xl2 = 10
    o.append(P([(xr2, 38), (xr2, 28), (xl2, 28), (xl2, 38)], False, None, 1.6, S_GRN))
    o.append(T((xr2 + xl2) / 2, 20, "زمان اجرا (Runtime)", 11.5, "c", 700, S_GRN))
    o.append(T(340, 195, "خطای نوشتاری (Syntax) در مرحله‌ی ۲ گرفته می‌شود؛ خطای اجرا و منطق، بعد از شروع برنامه خودش را نشان می‌دهد.", 10.5, "c", 400, MU))
    return svg(W, H, "".join(o))

def f_ecosystem():
    W, H = 680, 330
    o = []
    nodes_r = [("وب و API", "ASP.NET Core", F2), ("دسکتاپ ویندوز", "WinForms · WPF · WinUI", F2),
               ("موبایل و چندسکویی", ".NET MAUI", F2), ("بازی‌سازی", "Unity (اسکریپت‌ها با C#)", F4)]
    nodes_l = [("ابر و سرور‌لس", "Azure Functions", F3), ("هوش مصنوعی و داده", "ML.NET", F3),
               ("اینترنت اشیا (IoT)", ".NET IoT Libraries", F3), ("برنامه‌ی کنسول", "← شروع ما اینجاست", F1)]
    cx, cy = 340, 165
    for i, (t, s, f) in enumerate(nodes_r):
        y = 12 + i * 80
        o.append(L(cx + 40, cy, 470, y + 28, False, None, 1.4, "#7C73AD"))
    for i, (t, s, f) in enumerate(nodes_l):
        y = 12 + i * 80
        o.append(L(cx - 40, cy, 210, y + 28, False, None, 1.4, "#7C73AD"))
    for i, (t, s, f) in enumerate(nodes_r):
        y = 12 + i * 80
        o.append(R(470, y, 200, 56, f, BR, 8)); o.append(T(570, y + 23, t, 12.5, "c", 700)); o.append(T(570, y + 42, s, 10, "c", 400, MU, True) if s.isascii() else T(570, y + 42, s, 10, "c", 400, MU))
    for i, (t, s, f) in enumerate(nodes_l):
        y = 12 + i * 80
        last = i == 3
        o.append(R(10, y, 200, 56, f, BR, 8, None, 3 if last else 1.6)); o.append(T(110, y + 23, t, 12.5, "c", 700))
        o.append(T(110, y + 42, s, 10, "c", 400 if not last else 700, MU if not last else BR, s.isascii()))
    o.append(f'<circle cx="{cx}" cy="{cy}" r="48" fill="{BR}"/>')
    o.append(T(cx, cy + 4, ".NET", 24, "c", 700, "#fff", True))
    o.append(T(cx, cy + 26, "C# · F# · VB", 9, "c", 400, "#E1D9FF", True))
    return svg(W, H, "".join(o))

def f_timeline():
    W, H = 680, 240
    ev = [(2000, "معرفی C#\nتوسط مایکروسافت", "اندرس هیلزبرگ"), (2002, "C# 1.0 و\n.NET Framework 1.0", ""),
          (2012, "C# 5\nasync / await", ""), (2016, ".NET Core\nمتن‌باز و چندسکویی", ""),
          (2020, ".NET 5\nیکپارچه‌سازی", ""), (2023, ".NET 8\nنسخه‌ی LTS", ""), (2025, ".NET 10 و C# 14\nنسخه‌ی LTS", "")]
    o = [L(665, 120, 15, 120, True, None, 3)]
    n = len(ev)
    for i, (yr, lab, sub) in enumerate(ev):
        x = 640 - i * (610 / (n - 1))
        up = i % 2 == 0
        o.append(f'<circle cx="{x}" cy="120" r="8" fill="#fff" stroke="{BR}" stroke-width="3"/>')
        if up:
            o.append(L(x, 112, x, 80, False, None, 1.3)); o.append(T(x, 70, str(yr), 15, "c", 700, BR, True)); o.append(T(x, 38, lab, 10.5, "c", 400))
            o[-1] = T(x, 50 - (lab.count("\n")) * 0 , lab, 10.5, "c", 400) if False else T(x, 26, lab, 10.5, "c", 400)
        else:
            o.append(L(x, 128, x, 160, False, None, 1.3)); o.append(T(x, 178, str(yr), 15, "c", 700, BR, True)); o.append(T(x, 198, lab, 10.5, "c", 400))
    o.append(T(340, 232, "نسخه‌ی جدید دات‌نت هر سال در ماه نوامبر منتشر می‌شود؛ نسخه‌های زوج معمولاً LTS (پشتیبانی بلندمدت) هستند.", 10, "c", 400, MU))
    return svg(W, H, "".join(o))

GREEN = "#5FE07A"
WH = "#F4F4F8"
def _tri(x, y, open_):
    if open_: return f'<path d="M{x} {y-4} h13 l-6.5 9 z" fill="none" stroke="{WH}" stroke-width="1.8" stroke-linejoin="round"/>'
    return f'<path d="M{x+2} {y-8} v16 l10 -8 z" fill="none" stroke="{WH}" stroke-width="1.8" stroke-linejoin="round"/>'

def _ic_solution(x, y):
    return (f'<rect x="{x}" y="{y-13}" width="26" height="25" rx="3" fill="none" stroke="#A97BFF" stroke-width="2.4"/>'
            f'<path d="M{x} {y-6} h26" stroke="#A97BFF" stroke-width="2"/><path d="M{x+4} {y-9.5} h8" stroke="#A97BFF" stroke-width="1.6"/>'
            f'<path d="M{x+9} {y+2} l8 -6 v14 l-8 -6 l-4 3 l-1 -3 l1 -3 z" fill="#2B1B52" stroke="#A97BFF" stroke-width="2" stroke-linejoin="round"/>'
            f'<path d="M{x+22} {y+14} l-5 -4" stroke="#A97BFF" stroke-width="2"/>')

def _ic_project(x, y):
    return (f'<rect x="{x}" y="{y-14}" width="28" height="28" rx="3" fill="#102A18" stroke="{GREEN}" stroke-width="2.6"/>'
            + T(x + 14, y + 5.5, "C#", 14, "c", 700, WH, True))

def _ic_wrench(x, y):
    return (f'<path d="M{x+4} {y+12} L{x+15} {y+1}" stroke="{WH}" stroke-width="4.5" stroke-linecap="round"/>'
            f'<path d="M{x+13} {y-1} a7.5 7.5 0 1 1 8 -9 l-4 4 l1 3 l3 1 l4 -4 a7.5 7.5 0 0 1 -9 8 z" fill="{WH}" stroke="{WH}" stroke-width="1" stroke-linejoin="round" transform="translate(-4,3)"/>')

def _ic_gear(x, y):
    cx, cy = x + 14, y
    teeth = "".join(f'<rect x="{cx-2.8}" y="{cy-13}" width="5.6" height="6.5" rx="1" fill="{WH}" transform="rotate({a} {cx} {cy})"/>' for a in range(0, 360, 45))
    return teeth + f'<circle cx="{cx}" cy="{cy}" r="9" fill="{WH}"/><circle cx="{cx}" cy="{cy}" r="4" fill="#1B1B1F"/>'

def _ic_cs(x, y):
    return T(x + 14, y + 7, "C#", 20, "c", 700, GREEN, True)

def _ic_json(x, y):
    return T(x + 14, y + 7, "{ }", 19, "c", 500, WH, True)

def f_projtree():
    W, H = 680, 300
    o = [R(4, 4, 672, 292, "#1B1B1F", "#17132B", 12, None, 2)]
    rows = [(0, True, _ic_solution, "Solution 'ConsoleApp' (1 of 1 project)", False),
            (1, True, _ic_project, "ConsoleApp", True),
            (2, False, _ic_wrench, "Dependencies", False),
            (2, False, _ic_gear, "Properties", False),
            (2, None, _ic_cs, "Program.cs", False),
            (2, None, _ic_json, "appsettings.json", False),
            (2, None, _ic_cs, "ConsoleApp.csproj", False)]
    y0 = 38
    for k, (lvl, ex, ic, name, bold) in enumerate(rows):
        y = y0 + k * 37
        x = 30 + lvl * 38
        if ex is not None: o.append(_tri(x, y, ex))
        o.append(ic(x + 28 if lvl < 2 else x + 30, y))
        tx = x + 28 + 40 if lvl < 2 else x + 30 + 44
        o.append(T(tx, y + 6, name, 19, "l", 700 if bold else 400, WH, False))
    return svg(W, H, "".join(o))

# ======================= فصل ۲ =======================
def f_ipo():
    W, H = 680, 215
    o = []
    cols = [("ورودی (Input)", "داده‌هایی که برنامه می‌گیرد", F2, S_BLUE, "۱۲ و ۱۸"), ("پردازش (Process)", "کاری که روی داده‌ها انجام می‌شود", F4, S_AMB, "(a + b) / 2"),
            ("خروجی (Output)", "نتیجه‌ای که به کاربر نشان می‌دهیم", F3, S_GRN, "۱۵")]
    for i, (t, s, f, st, ex) in enumerate(cols):
        x = 680 - 10 - 200 - i * 235
        o.append(R(x, 20, 200, 100, f, st, 10, None, 2.2))
        o.append(T(x + 100, 52, t, 14, "c", 700)); o.append(T(x + 100, 75, s, 10.5, "c", 400, MU))
        o.append(T(x + 100, 104, ex, 13, "c", 700, st, True) if ex[0] in "(" else T(x + 100, 104, ex, 14, "c", 700, st))
        if i < 2: o.append(L(x - 3, 70, x - 32, 70, True, None, 2.4))
    o.append(T(340, 158, "هر برنامه‌ای در دنیا، از ماشین‌حساب تا اینستاگرام، همین سه مرحله را دارد.", 12, "c", 500, BR))
    o.append(T(340, 184, "قبل از نوشتن کد از خودتان بپرسید: ورودی من چیست؟ باید با آن چه کار کنم؟ خروجی دقیقاً چه شکلی است؟", 10.5, "c", 400, MU))
    return svg(W, H, "".join(o))

def f_steps():
    W, H = 680, 215
    o = []
    st = [("۱. فهمیدن مسئله", "ورودی/خروجی را بنویس"), ("۲. حل با دست", "یک مثال کوچک را روی کاغذ حل کن"),
          ("۳. الگوریتم", "گام‌ها را به زبان ساده یا فلوچارت بنویس"), ("۴. کدنویسی", "هر گام را به یک خط کد تبدیل کن"),
          ("۵. آزمون", "با ورودی‌های عادی و مرزی تست کن")]
    bw = 120; gap = 20
    for i, (t, s) in enumerate(st):
        x = 670 - bw - i * (bw + gap)
        f = [F2, F2, F4, F1, F3][i]
        o.append(R(x, 20, bw, 92, f, BR, 8)); o.append(badge(x + bw / 2, 20, i + 1, 11))
        o.append(T(x + bw / 2, 52, t[3:], 12.5, "c", 700)); o.append(T(x + bw / 2, 72, s.replace(" ", " ", 1), 9.2, "c", 400, MU))
        if i < 4: o.append(L(x - 1, 66, x - gap + 1, 66, True))
    x5 = 670 - bw - 4 * (bw + gap) + bw / 2; x3 = 670 - bw - 2 * (bw + gap) + bw / 2
    o.append(P([(x5, 114), (x5, 150), (x3, 150), (x3, 116)], True, "6 4", 1.8, S_RED, True))
    o.append(T((x5 + x3) / 2, 170, "جواب غلط یا خطا؟ نترسید! برگردید به الگوریتم و دوباره دنبال کنید", 11, "c", 700, S_RED))
    o.append(T(340, 200, "برنامه‌نویس حرفه‌ای هم همین چرخه را دارد؛ فقط سریع‌تر می‌چرخد.", 10.5, "c", 400, MU))
    return svg(W, H, "".join(o))

def f_symbols():
    W, H = 680, 140
    o = [term(590, 45, 100, 38, "شروع / پایان"), proc(450, 45, 100, 38, "پردازش"), io(310, 45, 100, 38, "ورودی/خروجی"), dia(170, 45, 110, 54, "شرط؟"),
         L(100, 45, 40, 45, True), T(590, 100, "ترمینال", 11, "c", 400, MU), T(450, 100, "محاسبه و تخصیص", 11, "c", 400, MU),
         T(310, 100, "خواندن/چاپ", 11, "c", 400, MU), T(170, 100, "تصمیم (بله/خیر)", 11, "c", 400, MU), T(70, 100, "جهت جریان", 11, "c", 400, MU)]
    return svg(W, H, "".join(o))

def f_errors():
    W, H = 680, 245
    o = [L(670, 22, 10, 22, True, None, 2.4), T(668, 15, "زمان", 10, "r", 700, MU), ]
    cards = [("خطای کامپایل", "Compile-time", F5, S_RED, "قبل از اجرا؛ کامپایلر برنامه را قبول نمی‌کند", 'int x = "hi";', "برنامه اصلاً اجرا نمی‌شود"),
             ("استثنای زمان اجرا", "Runtime", F4, S_AMB, "برنامه شروع می‌شود و وسط کار می‌افتد", "int z = 0; 10 / z", "ارور قرمز و توقف برنامه"),
             ("خطای منطقی", "Logic", F2, S_BLUE, "همه چیز اجرا می‌شود ولی جواب غلط است", "(a + b / 2)", "بی‌صدا خطرناک‌ترین نوع!")]
    for i, (t, en, f, st, d, code, res) in enumerate(cards):
        x = 680 - 10 - 212 - i * 224
        o.append(R(x, 40, 212, 190, f, st, 10, None, 2))
        o.append(T(x + 106, 66, t, 14, "c", 700)); o.append(T(x + 106, 84, en, 10.5, "c", 400, MU, True))
        o.append(T(x + 106, 112, d.replace("؛ ", "؛\n") if len(d) > 28 else d, 10.5, "c", 400))
        o.append(R(x + 14, 148, 184, 26, "#fff", st, 5, None, 1.2)); o.append(T(x + 106, 166, code, 11, "c", 400, INK, True))
        o.append(T(x + 106, 204, res, 11, "c", 700, st))
    return svg(W, H, "".join(o))

# ======================= فصل ۳ =======================
def f_anatomy():
    W, H = 680, 275
    lines = ["using System;", "", "class Program", "{", "    static void Main()", "    {", '        Console.WriteLine("Hello, C#!");', "    }", "}"]
    cb, h = codeblock(10, 14, lines, 13, 26, 350)
    o = [cb]
    notes = [(0, "1", "کتابخانه‌ی System را وارد می‌کند\n(کلاس Console داخل آن است)"), (2, "2", "ظرفی برای کد؛ فعلاً یک قالب ثابت\n(در جزوه‌ی OOP کامل می‌شود)"),
             (4, "3", "Main = نقطه‌ی شروع برنامه\nاجرا دقیقاً از اینجا آغاز می‌شود"), (6, "4", "یک دستور (Statement)؛ متن را چاپ\nمی‌کند و به خط بعد می‌رود")]
    for ln, num, txt in notes:
        y = 14 + 22 + ln * 26 - 4
        o.append(L(366, y - 5, 396, y - 5, True, "4 3", 1.4, "#7C73AD"))
        o.append(badge(410, y - 5, num, 11))
        o.append(T(668, y - 9, txt, 11, "r", 400))
    o.append(T(668, 14 + 22 + 8 * 26 - 4, "هر دستور با ; تمام می‌شود  ·  هر { باید یک } جفت داشته باشد", 11, "r", 700, S_RED))
    return svg(W, H, "".join(o))

def f_cursor():
    W, H = 680, 215
    o = []
    def grid(x0, rows, cursor_rc, title, code):
        out = [T(x0 + 150, 18, title, 12.5, "c", 700), T(x0 + 150, 38, code, 10.5, "c", 400, MU, True)]
        out.append(R(x0, 48, 300, 100, "#1E1B2E", "#1E1B2E", 6, None, 1))
        for r, txt in enumerate(rows):
            for c, chv in enumerate(txt):
                out.append(R(x0 + 12 + c * 22, 56 + r * 26, 20, 22, "#ECEBF1", "#ECEBF1", 2, None, 1))
                out.append(T(x0 + 22 + c * 22, 72 + r * 26, chv, 13, "c", 700, INK, True))
        r, c = cursor_rc
        out.append(R(x0 + 12 + c * 22, 56 + r * 26, 20, 22, "none", "#FFD24A", 2, "3 2", 2.2))
        return "".join(out)
    o.append(grid(20, ["ABC"], (0, 3), "Console.Write × ۳", 'Write("A"); Write("B"); Write("C");'))
    o.append(grid(360, ["A", "B", "C"], (3, 0), "Console.WriteLine × ۳", 'WriteLine("A"); ... ("B"); ... ("C");'))
    o.append(T(170, 172, "مکان‌نما بعد از C می‌ماند", 11, "c", 700, S_AMB)); o.append(T(510, 172, "بعد از هر خط، مکان‌نما به خط جدید می‌رود", 11, "c", 700, S_AMB))
    o.append(T(340, 205, "کادر زردِ خط‌چین = جایی که حرف بعدی چاپ می‌شود", 10, "c", 400, MU))
    return svg(W, H, "".join(o))

# ======================= فصل ۴ =======================
def f_tabs():
    W, H = 680, 235
    o = [T(340, 18, 'Console.WriteLine("ab\\tcd\\tef");', 13, "c", 700, INK, True)]
    x0 = 30; cw = 20
    def ruler(y, text_cells):
        out = []
        for i in range(25):
            x = x0 + i * cw
            stop = i % 8 == 0
            out.append(R(x, y, cw, 26, F4 if stop else "#fff", BR if stop else "#B9B3D1", 0, None, 1.3 if stop else 1))
        for pos, ch, red in text_cells:
            out.append(T(x0 + pos * cw + cw / 2, y + 19, ch, 12.5, "c", 700, S_RED if red else INK, True))
        return "".join(out)
    for i in range(25): o.append(T(x0 + i * cw + cw / 2, 46, str(i), 8.5, "c", 400, MU, True))
    o.append(ruler(52, [(0, "a", 0), (1, "b", 0), (8, "c", 0), (9, "d", 0), (16, "e", 0), (17, "f", 0)]))
    o.append(T(340, 100, "تب (Tab) مکان‌نما را به ابتدای «ستون توقف» بعدی می‌برد (هر ۸ خانه)؛ نه اینکه فقط ۸ فاصله بگذارد.", 10.5, "c", 500, BR))
    o.append(T(340, 130, 'abcdef\\tX', 12, "c", 700, INK, True))
    for i in range(25): o.append(T(x0 + i * cw + cw / 2, 158, str(i), 8.5, "c", 400, MU, True))
    o.append(ruler(164, [(i, ch, 0) for i, ch in enumerate("abcdef")] + [(8, "X", 1)]))
    o.append(T(340, 220, "هر اندازه حرف‌های قبلی باشند، X روی ستون توقف بعدی می‌نشیند؛ برای همین جدول‌های تب‌دار مرتب می‌شوند.", 10.5, "c", 400, MU))
    return svg(W, H, "".join(o))

# ======================= فصل ۵ =======================
def f_boxes():
    W, H = 680, 215
    o = []
    vs = [("int", "age", "20", "4 بایت", F2), ("float", "temp", "36.6f", "4 بایت", F4), ("double", "price", "19.5", "8 بایت", F4),
          ("char", "grade", "'A'", "2 بایت", F1), ("bool", "isOk", "true", "1 بایت", F3), ("string", "name", '"Sara"', "متغیر", F5)]
    w, gap = 100, 12
    x = (W - (len(vs) * w + (len(vs) - 1) * gap)) / 2
    addr = 1000
    for i, (t, n, v, sz, f) in enumerate(vs):
        o.append(R(x, 38, w, 108, f, BR, 8, None, 2))
        o.append(T(x + w / 2, 30, t, 13, "c", 700, S_BLUE, True))
        o.append(R(x + 8, 54, w - 16, 44, "#fff", BR, 4, None, 1.4)); o.append(T(x + w / 2, 83, v, 15, "c", 700, INK, True))
        o.append(T(x + w / 2, 119, n, 13, "c", 700, INK, True)); o.append(T(x + w / 2, 138, sz, 9.5, "c", 400, MU))
        o.append(T(x + w / 2, 164, f"0x{addr + i * 8:X}", 9, "c", 400, MU, True))
        x += w + gap
    o.append(T(340, 195, "نوع (بالا) · مقدار (داخل جعبه) · نام (برچسب روی جعبه) · آدرس در حافظه (پایین)", 11, "c", 500, BR))
    return svg(W, H, "".join(o))

def f_typesize():
    W, H = 680, 330
    rows = [("byte", 8, "0 تا 255", 0), ("short", 16, "±32,767", 0), ("int", 32, "±2.1 میلیارد", 0), ("long", 64, "±9.2×10^18", 0),
            ("float", 32, "≈ 7 رقم دقت", 1), ("double", 64, "≈ 15 رقم دقت", 1), ("decimal", 128, "28–29 رقم · مالی", 1),
            ("char", 16, "یک نویسه (UTF-16)", 2), ("bool", 8, "true / false", 2)]
    o = [T(10, 16, "اندازه بر حسب بیت", 10, "l", 400, MU), T(670, 16, "گستره / ویژگی", 10, "r", 700, MU)]
    for i, (n, bits, rng, g) in enumerate(rows):
        y = 28 + i * 32
        fill = {0: F2, 1: "url(#hatch)", 2: "url(#dots)"}[g]
        w = bits * 2.45
        o.append(T(78, y + 17, n, 13, "r", 700, INK, True))
        o.append(R(88, y, w, 24, fill, BR, 3, None, 1.5)); o.append(T(88 + w + 6, y + 17, str(bits), 10, "l", 700, MU, True))
        o.append(T(670, y + 17, rng, 11, "r", 400, INK))
    o.append(R(60, 322, 12, 8, F2, BR, 1)); o.append(T(78, 330, "صحیح", 9.5, "l", 400, MU))
    o.append(R(150, 322, 12, 8, "url(#hatch)", BR, 1)); o.append(T(168, 330, "اعشاری", 9.5, "l", 400, MU))
    o.append(R(240, 322, 12, 8, "url(#dots)", BR, 1)); o.append(T(258, 330, "سایر", 9.5, "l", 400, MU))
    return svg(W, 340, "".join(o))

def f_assign():
    W, H = 680, 215
    o = []
    panels = [("گام ۱", "int a = 5;", [("a", "5")]), ("گام ۲", "int b = a;", [("a", "5"), ("b", "5")]), ("گام ۳", "a = 9;", [("a", "9"), ("b", "5")])]
    for i, (t, code, vars_) in enumerate(panels):
        x = 680 - 10 - 210 - i * 225
        o.append(R(x, 10, 210, 150, "#FAFAFD", "#8C82BF", 8, None, 1.3))
        o.append(T(x + 105, 32, t, 12, "c", 700, BR)); o.append(T(x + 105, 54, code, 13, "c", 700, INK, True))
        for j, (n, v) in enumerate(vars_):
            bx = x + 105 - 70 + j * 76 if len(vars_) == 2 else x + 105 - 32
            changed = (i == 2 and n == "a")
            o.append(R(bx, 78, 64, 40, F3 if changed else F1, S_GRN if changed else BR, 6, None, 2.6 if changed else 1.6)); o.append(T(bx + 32, 105, v, 18, "c", 700, INK, True))
            o.append(T(bx + 32, 138, n, 12, "c", 700, INK, True))
        if i == 1: o.append(P([(x + 105 - 38, 74), (x + 105 + 38, 74)], True, "3 3", 1.4)) if False else o.append(T(x + 105, 70, "کپی مقدار", 9.5, "c", 400, MU))
    o.append(T(340, 190, "b یک نسخه‌ی کپی از مقدار a گرفت؛ تغییر بعدیِ a روی b اثری ندارد.", 11.5, "c", 700, BR))
    return svg(W, H, "".join(o))

def f_overflow():
    W, H = 680, 215
    o = [L(40, 100, 640, 100, False, None, 4, "#7C73AD")]
    for x, lab, v in [(40, "int.MinValue", "-2,147,483,648"), (340, "0", "0"), (640, "int.MaxValue", "2,147,483,647")]:
        o.append(f'<circle cx="{x}" cy="100" r="7" fill="{BR}"/>'); o.append(T(x, 128, lab, 11.5, "c", 700, INK, True)); o.append(T(x, 146, v, 10.5, "c", 400, MU, True))
    o.append(P([(640, 88), (640, 40), (40, 40), (40, 86)], True, "6 4", 2.2, S_RED, True))
    o.append(T(340, 32, "+ 1   →   دور می‌زند و به کوچک‌ترین مقدار می‌رسد!", 13, "c", 700, S_RED))
    o.append(T(340, 190, "مثل کیلومترشمارِ ماشین که بعد از ۹۹۹۹۹ دوباره ۰۰۰۰۰ می‌شود؛ ظرفیت جعبه‌ی int فقط ۳۲ بیت است.", 11, "c", 400, MU))
    return svg(W, H, "".join(o))
