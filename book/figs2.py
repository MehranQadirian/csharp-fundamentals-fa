import math
from figbase import *

# ======================= فصل ۶ =======================
def f_intdiv():
    W, H = 680, 230
    o = [T(340, 20, "۱۷ آبنبات داریم و هر کیسه ۵ تا جا دارد", 13, "c", 700)]
    xs = [30, 170, 310]
    for k, x in enumerate(xs):
        o.append(R(x, 40, 120, 60, F3, S_GRN, 10, None, 2))
        for j in range(5): o.append(f'<circle cx="{x+18+j*21}" cy="70" r="8" fill="#fff" stroke="{S_GRN}" stroke-width="1.6"/>')
        o.append(T(x + 60, 118, f"کیسه‌ی {k+1}", 10.5, "c", 400, MU))
    o.append(R(470, 40, 90, 60, F5, S_RED, 10, "5 4", 2))
    for j in range(2): o.append(f'<circle cx="{500+j*28}" cy="70" r="8" fill="#fff" stroke="{S_RED}" stroke-width="1.6"/>')
    o.append(T(515, 118, "باقی‌مانده", 10.5, "c", 400, MU))
    o.append(R(60, 140, 300, 62, "#fff", S_GRN, 8, None, 1.6)); o.append(T(210, 164, "تعداد کیسه‌های کامل = خارج‌قسمت", 11.5, "c", 700, S_GRN))
    o.append(T(210, 190, "17 / 5  =  3", 15, "c", 700, INK, True))
    o.append(R(400, 140, 270, 62, "#fff", S_RED, 8, None, 1.6)); o.append(T(535, 164, "آبنبات‌های اضافه = باقی‌مانده", 11.5, "c", 700, S_RED))
    o.append(T(535, 190, "17 % 5  =  2", 15, "c", 700, INK, True))
    o.append(T(340, 224, "در تقسیم دو عدد صحیح، قسمت اعشاری حذف می‌شود (گرد نمی‌شود).", 10.5, "c", 400, MU))
    return svg(W, H + 8, "".join(o))

def f_clock():
    W, H = 680, 230
    cx, cy, r = 170, 112, 78
    o = [f'<circle cx="{cx}" cy="{cy}" r="{r+14}" fill="{F2}" stroke="{BR}" stroke-width="2.4"/>']
    for k in range(12):
        a = math.radians(k * 30 - 90)
        x, y = cx + (r) * math.cos(a), cy + (r) * math.sin(a)
        hl = k == 2
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="11" fill="{"#FFD24A" if hl else "#fff"}" stroke="{BR}" stroke-width="{2.2 if hl else 1.2}"/>')
        o.append(T(x, y + 4, str(k), 11.5, "c", 700, INK, True))
    a = math.radians(2 * 30 - 90)
    o.append(L(cx, cy, cx + 52 * math.cos(a), cy + 52 * math.sin(a), True, None, 3))
    o.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="{BR}"/>')
    o.append(T(cx, cy + 112, "ساعت ۱۲ تایی", 11, "c", 700, MU))
    ex = [("14 % 12 = 2", "ساعت ۱۴ روی ساعت ۱۲‌تایی، عدد ۲ را نشان می‌دهد"), ("(10 + 5) % 12 = 3", "پنج ساعت بعد از ۱۰، می‌شود ۳"),
          ("25 % 7 = 4", "۲۵ روز بعد از شنبه، چهارمین روز هفته (از ۰) است")]
    for i, (c, d) in enumerate(ex):
        y = 40 + i * 62
        o.append(R(330, y - 20, 340, 52, "#fff", BR, 8, None, 1.4))
        o.append(T(345, y + 3, c, 14, "l", 700, BR, True)); o.append(T(660, y + 24, d, 10.5, "r", 400, MU))
    o.append(T(500, 226, "باقی‌مانده یعنی «بعد از چند دور کامل، چقدر جلو رفتیم».", 11, "c", 500, BR))
    return svg(W, 235, "".join(o))

def f_precedence():
    W, H = 680, 300
    rows = [("۱", "( )", "پرانتز", F3), ("۲", "x++  x--  +x  -x  !", "یکانی (یک عملوندی)", F2), ("۳", "*    /    %", "ضرب، تقسیم، باقی‌مانده", F4),
            ("۴", "+    -", "جمع و تفریق", F1), ("۵", "=   +=   -=   *=   /=   %=", "تخصیص (آخرین کار)", F6)]
    o = [T(660, 16, "اولویت بالا (اول انجام می‌شود)", 10.5, "r", 700, S_GRN), T(660, 285, "اولویت پایین (آخر انجام می‌شود)", 10.5, "r", 700, S_RED)]
    o.append(L(40, 30, 40, 270, True, None, 2.4))
    for i, (n, op, nm, f) in enumerate(rows):
        y = 28 + i * 48
        o.append(R(60, y, 600, 40, f, BR, 8, None, 1.6)); o.append(badge(640, y + 20, n, 11))
        o.append(T(110, y + 26, op, 14, "l", 700, INK, True)); o.append(T(620, y + 25, nm, 12, "r", 500))
    return svg(W, H, "".join(o))

def f_incr():
    W, H = 680, 235
    o = []
    def panel(x0, title, code, steps, res):
        out = [R(x0, 6, 325, 215, "#FAFAFD", "#8C82BF", 8, None, 1.3), T(x0 + 162, 30, title, 12.5, "c", 700, BR), T(x0 + 162, 52, code, 12, "c", 700, INK, True)]
        for i, s in enumerate(steps):
            y = 80 + i * 40
            out.append(badge(x0 + 300, y, i + 1, 10)); out.append(R(x0 + 20, y - 17, 260, 34, F4 if i == 0 else F3, BR, 6, None, 1.3))
            out.append(T(x0 + 150, y + 4, s, 10.5, "c", 400))
            if i < len(steps) - 1: out.append(L(x0 + 150, y + 17, x0 + 150, y + 23, True))
        out.append(R(x0 + 40, 168, 220, 40, F1, BR, 6, None, 2)); out.append(T(x0 + 150, 194, res, 13, "c", 700, INK, True))
        return "".join(out)
    o.append(panel(345, "پسوندی (Postfix)", "int y = x++;", ["مقدار فعلی x (یعنی 5) به y می‌رود", "بعد از آن، x یکی زیاد می‌شود"], "x = 6    y = 5"))
    o.append(panel(10, "پیشوندی (Prefix)", "int y = ++x;", ["اول x یکی زیاد می‌شود (6)", "بعد مقدار جدید به y می‌رود"], "x = 6    y = 6"))
    return svg(W, H, "".join(o))

# ======================= فصل ۷ =======================
def f_roundline():
    W, H = 680, 270
    o = []
    def line(y, a, b, val, title, res):
        x0, x1 = 100, 580
        out = [L(x0 - 30, y, x1 + 30, y, False, None, 2.6, "#7C73AD")]
        for x, lab in [(x0, a), (x1, b)]:
            out.append(f'<circle cx="{x}" cy="{y}" r="6" fill="{BR}"/>'); out.append(T(x, y + 26, lab, 13, "c", 700, INK, True))
        t = (val - a) / (b - a)
        vx = x0 + (x1 - x0) * t
        out.append(f'<circle cx="{vx}" cy="{y}" r="8" fill="#FFD24A" stroke="{BR}" stroke-width="2.4"/>')
        out.append(T(vx, y - 16, str(val), 13, "c", 700, BR, True))
        out.append(T(660, y - 60, title, 12, "r", 700, BR))
        for k, (nm, tgt) in enumerate(res):
            tx = x0 if tgt == a else x1
            yy = y + 52 + (k % 2) * 0
        return "".join(out)
    o.append(line(75, 2, 3, 2.7, "عدد 2.7", []))
    o.append(line(205, -3, -2, -2.7, "عدد -2.7", []))
    o.append(T(100, 118, "Floor → 2\nTruncate → 2", 11, "c", 700, S_GRN, True)); o.append(T(580, 118, "Ceiling → 3\nRound → 3", 11, "c", 700, S_AMB, True))
    o.append(T(100, 248, "Floor → -3\nRound → -3", 11, "c", 700, S_GRN, True)); o.append(T(580, 248, "Ceiling → -2\nTruncate → -2", 11, "c", 700, S_AMB, True))
    return svg(W, H + 20, "".join(o))

def f_unitcircle():
    W, H = 680, 245
    cx, cy, r = 160, 125, 90
    th = math.radians(40)
    px, py = cx + r * math.cos(th), cy - r * math.sin(th)
    o = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{F2}" stroke="{BR}" stroke-width="2"/>',
         L(cx - r - 18, cy, cx + r + 18, cy, True, None, 1.4), L(cx, cy + r + 18, cx, cy - r - 18, True, None, 1.4),
         L(cx, cy, px, py, False, None, 3), L(px, py, px, cy, False, "4 3", 2, S_RED), L(cx, cy, px, cy, False, None, 3.4, S_GRN),
         f'<path d="M {cx+30} {cy} A 30 30 0 0 0 {cx+30*math.cos(th):.1f} {cy-30*math.sin(th):.1f}" fill="none" stroke="{S_AMB}" stroke-width="2.2"/>',
         f'<circle cx="{px:.1f}" cy="{py:.1f}" r="5.5" fill="{BR}"/>',
         T(cx + 38, cy - 8, "θ", 14, "l", 700, S_AMB, True), T(cx + r * math.cos(th) / 2, cy + 18, "cos θ", 12, "c", 700, S_GRN, True),
         T(px + 8, (py + cy) / 2 + 4, "sin θ", 12, "l", 700, S_RED, True), T(px + 8, py - 8, "(cos θ , sin θ)", 10, "l", 400, MU, True)]
    o.append(R(330, 20, 340, 205, "#fff", BR, 8, None, 1.4))
    o.append(T(500, 45, "درجه ← رادیان (توابع مثلثاتی رادیان می‌خواهند)", 11.5, "c", 700, BR))
    o.append(T(500, 70, "radians = degrees × Math.PI / 180", 12, "c", 700, INK, True))
    rows = [("0°", "0"), ("30°", "π/6 ≈ 0.5236"), ("45°", "π/4 ≈ 0.7854"), ("90°", "π/2 ≈ 1.5708"), ("180°", "π ≈ 3.1416"), ("360°", "2π ≈ 6.2832")]
    for i, (d, rad) in enumerate(rows):
        y = 98 + i * 21
        o.append(T(380, y, d, 12, "l", 700, INK, True)); o.append(T(640, y, rad + " rad", 12, "r", 400, INK, True))
        o.append(L(375, y + 6, 645, y + 6, False, None, 0.7, "#B9B3D1"))
    return svg(W, H, "".join(o))

# ======================= فصل ۸ =======================
def f_castchain():
    W, H = 680, 245
    names = ["byte", "short", "int", "long", "float", "double"]
    o = [T(340, 18, "تبدیل ضمنی (امن، خودکار) →", 12, "c", 700, S_GRN)]
    xs = [20 + i * 108 for i in range(6)]
    for i, (n, x) in enumerate(zip(names, xs)):
        o.append(box(x, 40, 78, 38, n, [F2, F2, F2, F2, F4, F4][i], BR, 13, True, 6, None, 700))
        if i < 5: o.append(L(x + 80, 59, xs[i + 1] - 2, 59, True, None, 2.4, S_GRN))
    o.append(box(xs[2], 100, 78, 34, "char", F1, BR, 12, True)); o.append(L(xs[2] + 39, 100, xs[2] + 39, 80, True, None, 2.2, S_GRN))
    o.append(box(xs[3], 100, 78, 34, "decimal", F3, BR, 12, True, 6, "4 3")); o.append(L(xs[3] + 39, 78, xs[3] + 39, 100, True, "4 3", 1.8, S_GRN))
    o.append(T(xs[3] + 39 + 52, 122, "از صحیح‌ها", 10, "l", 400, MU) if False else T(xs[3] + 100, 122, "فقط از صحیح‌ها", 10, "l", 400, MU))
    o.append(T(340, 168, "تبدیل صریح (Cast) لازم است؛ ممکن است داده از دست برود", 12, "c", 700, S_RED))
    o.append(P([(xs[5] + 39, 84), (xs[5] + 39, 150), (xs[0] + 39, 150), (xs[0] + 39, 86)], True, "6 4", 2, S_RED, True))
    o.append(T(340, 205, "مثال ضمنی:  long x = 5;   double d = x;       مثال صریح:  int n = (int)3.99;", 11.5, "c", 400, INK, True))
    o.append(T(340, 232, "قانون: از جعبه‌ی کوچک به بزرگ بدون زحمت؛ از بزرگ به کوچک فقط با اجازه‌ی صریح برنامه‌نویس.", 11, "c", 500, BR))
    return svg(W, H, "".join(o))

def f_funnel():
    W, H = 680, 250
    o = [T(170, 20, "(int)9.99  ← حذف قسمت اعشاری", 12.5, "c", 700, BR)]
    o.append(box(30, 40, 100, 40, "9.99", F4, BR, 16, True, 8, None, 700)); o.append(T(80, 98, "double", 10.5, "c", 400, MU, True))
    o.append(L(132, 60, 188, 60, True, None, 2.4)); o.append(T(160, 50, "(int)", 11, "c", 700, BR, True))
    o.append(box(190, 40, 80, 40, "9", F3, S_GRN, 16, True, 8, None, 700)); o.append(T(230, 98, "int", 10.5, "c", 400, MU, True))
    o.append(P([(90, 82), (90, 130), (110, 130)], True, "4 3", 1.8, S_RED, True)); o.append(T(180, 136, ".99 دور ریخته می‌شود\n(گرد نمی‌شود!)", 10.5, "c", 700, S_RED))
    o.append(T(520, 20, "(byte)300  ← فقط ۸ بیت پایین می‌ماند", 12.5, "c", 700, BR))
    bits = "100101100"
    for i, bch in enumerate(bits):
        x = 370 + i * 32
        drop = i == 0
        o.append(R(x, 38, 28, 32, "#fff" if drop else F1, S_RED if drop else BR, 4, "3 2" if drop else None, 1.6))
        o.append(T(x + 14, 60, bch, 15, "c", 700, S_RED if drop else INK, True))
    o.append(T(384, 88, "بیت نهم\nبیرون می‌افتد", 9.5, "c", 700, S_RED))
    o.append(P([(530, 74), (530, 108)], False)) if False else None
    o.append(T(520, 128, "00101100₂ = 44", 15, "c", 700, INK, True))
    o.append(T(520, 150, "300 در ۸ بیت جا نمی‌شود، پس جواب ۴۴ می‌شود", 10.5, "c", 400, MU))
    o.append(R(20, 175, 640, 62, F5, S_RED, 8, "5 4", 1.8))
    o.append(T(340, 200, "هر وقت از نوع بزرگ‌تر به کوچک‌تر Cast می‌کنید، خودتان مسئول درست‌بودنِ مقدار هستید؛", 11.5, "c", 700, S_RED))
    o.append(T(340, 222, "کامپایلر هشدار نمی‌دهد و خطای اجرا هم رخ نمی‌دهد (مگر در بلوک checked).", 11, "c", 400, INK))
    return svg(W, H, "".join(o))

def f_ascii():
    W, H = 680, 300
    o = [T(340, 16, "جدول اسکی (ASCII) نویسه‌های قابل چاپ؛ ردیف = رقم ۱۶تایی بالا، ستون = رقم ۱۶تایی پایین (کد دهدهی زیر هر نویسه)", 10.5, "c", 500, BR)]
    x0, y0, cw, ch = 34, 38, 39, 38
    for c in range(16):
        o.append(T(x0 + c * cw + cw / 2, y0 - 4, f"_{c:X}", 9.5, "c", 700, MU, True))
    hot = {32: "sp", 48: "", 65: "", 97: ""}
    for r in range(2, 8):
        y = y0 + (r - 2) * ch
        o.append(T(x0 - 6, y + 22, f"{r:X}_", 10, "r", 700, MU, True))
        for c in range(16):
            code = r * 16 + c
            if code > 127: continue
            ch_ = chr(code) if 32 <= code <= 126 else "DEL"
            if code == 32: ch_ = "␣"
            fill = "url(#hatch)" if code in hot else "#fff"
            o.append(R(x0 + c * cw, y, cw, ch, fill, BR if code in hot else "#B9B3D1", 0, None, 1.8 if code in hot else 1))
            o.append(T(x0 + c * cw + cw / 2, y + 19, ch_.replace("&", "&"), 14 if ch_ != "DEL" else 9, "c", 700, INK, True))
            o.append(T(x0 + c * cw + cw / 2, y + 33, str(code), 8, "c", 400, MU, True))
    o.append(T(340, 278, "'A' = 65   ·   'a' = 97   ·   '0' = 48   ·   فاصله = 32   ·   اختلاف حرف بزرگ و کوچک همان حرف = 32", 11, "c", 700, BR, True))
    o.append(T(340, 296, "کدهای ۰ تا ۳۱ نویسه‌های کنترلی‌اند (مثل \\n = 10 و \\t = 9) و قابل چاپ نیستند.", 10, "c", 400, MU))
    return svg(W, H, "".join(o))
