import math
from figbase import *

# ======================= فصل ۹ =======================
def f_if_flow():
    W, H = 680, 335
    o = [term(340, 20, 110, 30, "شروع"), L(340, 35, 340, 52, True), io(340, 70, 170, 34, "score را بخوان", F2, 12),
         L(340, 87, 340, 112, True), dia(340, 150, 190, 74, "score >= 50 ؟", F4, 13, True),
         L(435, 150, 540, 150, False), L(540, 150, 540, 224, True), T(488, 142, "بله", 12, "c", 700, S_GRN),
         L(245, 150, 140, 150, False), L(140, 150, 140, 224, True), T(192, 142, "خیر", 12, "c", 700, S_RED),
         proc(540, 248, 150, 40, 'چاپ "Pass"', F3, 12), proc(140, 248, 150, 40, 'چاپ "Fail"', F5, 12),
         P([(540, 268), (540, 300), (396, 300)], True), P([(140, 268), (140, 300), (284, 300)], True), term(340, 300, 110, 30, "پایان")]
    o.append(T(660, 110, "if ... else", 12, "r", 700, BR, True)); o.append(T(20, 110, "مسیر دوم", 10, "l", 400, MU)) if False else None
    return svg(W, H, "".join(o))

def f_elseif():
    W, H = 680, 300
    o = []
    xs = [570, 390, 210]
    labs = ["score >= 90", "score >= 80", "score >= 70"]
    res = ["A", "B", "C"]
    for i, x in enumerate(xs):
        o.append(dia(x, 60, 150, 66, labs[i] + " ؟", F4, 11.5, True))
        o.append(L(x, 93, x, 150, True)); o.append(T(x + 14, 125, "بله", 11.5, "l", 700, S_GRN))
        o.append(proc(x, 172, 90, 38, f'grade = "{res[i]}"', F3, 11, True))
        o.append(P([(x, 191), (x, 235)], False))
        if i < 2: o.append(L(x - 75, 60, xs[i + 1] + 75, 60, True)); o.append(T((x - 75 + xs[i + 1] + 75) / 2, 50, "خیر", 11.5, "c", 700, S_RED))
    o.append(L(135, 60, 90, 60, True)); o.append(T(112, 50, "خیر", 11.5, "c", 700, S_RED))
    o.append(proc(50, 60, 80, 40, 'grade = "F"', F5, 11, True)); o.append(T(50, 96, "else", 12, "c", 700, S_RED, True))
    o.append(P([(50, 82), (50, 235)], False))
    o.append(L(50, 235, 570, 235, False)); o.append(L(340, 235, 340, 262, True))
    o.append(term(340, 276, 160, 28, "ادامه‌ی برنامه"))
    o.append(T(670, 18, "از بالا به پایین، اولین شرطی که درست باشد انتخاب می‌شود؛ بقیه بررسی نمی‌شوند.", 10.5, "r", 500, BR))
    return svg(W, H, "".join(o))

def f_switch():
    W, H = 680, 275
    o = [box(250, 8, 180, 36, "switch (grade)", F1, BR, 14, True, 8, None, 700)]
    xs = [95, 250, 405, 560]
    labs = ["case 'A':", "case 'B':", "case 'C':", "default:"]
    notes = ["Excellent", "Good", "Fair", "Unknown"]
    for x, lb, nt in zip(xs, labs, notes):
        o.append(P([(340, 44), (340, 70), (x, 70), (x, 98)], True))
        o.append(R(x - 70, 100, 140, 70, F3 if lb != "default:" else F5, S_GRN if lb != "default:" else S_RED, 8, None, 1.8))
        o.append(T(x, 124, lb, 12.5, "c", 700, INK, True)); o.append(T(x, 145, f'print "{nt}"', 10.5, "c", 400, INK, True)); o.append(T(x, 162, "break;", 10.5, "c", 700, S_RED, True))
        o.append(P([(x, 170), (x, 205)], False))
    o.append(L(95, 205, 560, 205, False)); o.append(L(340, 205, 340, 232, True))
    o.append(term(340, 248, 170, 28, "ادامه‌ی برنامه بعد از switch"))
    o.append(T(670, 66, "فقط یک شاخه اجرا می‌شود", 10.5, "r", 700, BR))
    return svg(W, H, "".join(o))

def f_ternary():
    W, H = 680, 200
    o = [T(10, 52, "string result =", 13, "l", 700, INK, True)]
    o.append(box(150, 28, 150, 40, "score >= 50", F4, S_AMB, 13, True, 8)); o.append(T(325, 58, "?", 26, "c", 700, BR, True))
    o.append(box(345, 28, 130, 40, '"Pass"', F3, S_GRN, 13, True, 8)); o.append(T(497, 58, ":", 26, "c", 700, BR, True))
    o.append(box(520, 28, 130, 40, '"Fail"', F5, S_RED, 13, True, 8)); o.append(T(655, 58, ";", 16, "c", 700, INK, True))
    for x, t in [(225, "شرط (bool)"), (410, "اگر درست باشد"), (585, "اگر نادرست باشد")]: o.append(T(x, 90, t, 11, "c", 700, MU))
    o.append(R(40, 112, 600, 76, "#FAFAFD", "#8C82BF", 8, None, 1.3))
    o.append(T(60, 134, "معادل if-else:", 11, "l", 700, BR))
    o.append(T(60, 154, 'string result;', 11.5, "l", 400, INK, True))
    o.append(T(60, 172, 'if (score >= 50) result = "Pass"; else result = "Fail";', 11.5, "l", 400, INK, True))
    return svg(W, H, "".join(o))

# ======================= فصل ۱۰ =======================
def f_for_flow():
    W, H = 680, 320
    cx = 280
    o = [proc(cx, 36, 190, 40, "int i = 1", F1, 13, True), badge(cx + 108, 22, 1), L(cx, 56, cx, 82, True),
         dia(cx, 128, 190, 74, "i <= 3 ؟", F4, 13, True), badge(cx + 108, 100, 2),
         L(cx, 165, cx, 198, True), T(cx + 14, 186, "بله", 11.5, "l", 700, S_GRN),
         proc(cx, 220, 190, 40, "بدنه‌ی حلقه", F3, 13), badge(cx + 108, 206, 3), L(cx, 240, cx, 262, True),
         proc(cx, 282, 190, 40, "i++", F2, 13, True), badge(cx + 108, 268, 4),
         P([(cx + 95, 282), (470, 282), (470, 128), (cx + 95, 128)], True),
         L(cx - 95, 128, 110, 128, True), T(150, 118, "خیر", 11.5, "c", 700, S_RED), term(70, 128, 80, 30, "خروج")]
    items = [("1", "مقدار اولیه: فقط یک‌بار، در شروع"), ("2", "شرط: پیش از هر دور بررسی می‌شود"), ("3", "بدنه: اگر شرط درست بود اجرا می‌شود"), ("4", "به‌روزرسانی: بعد از هر بار اجرای بدنه")]
    for i, (n, t) in enumerate(items):
        y = 60 + i * 44
        o.append(badge(655, y, n)); o.append(T(638, y + 4, t, 10.5, "r", 400))
    o.append(T(560, 240, "ترتیب اجرا:\n1 ← 2 ← 3 ← 4 ← 2 ← 3 ← 4 ← ... ← 2(خیر)", 10.5, "c", 700, BR))
    return svg(W, H, "".join(o))

def f_while_do():
    W, H = 680, 290
    o = [T(170, 18, "while  ؛ اول شرط، بعد بدنه", 12.5, "c", 700, BR, False), T(510, 18, "do-while  ؛ اول بدنه، بعد شرط", 12.5, "c", 700, BR, False)]
    # while
    x = 175
    o += [dia(x, 76, 150, 60, "cond ؟", F4, 12, True), L(x, 106, x, 150, True), T(x + 14, 132, "بله", 11, "l", 700, S_GRN),
          proc(x, 170, 140, 36, "بدنه", F3, 12), P([(x + 70, 170), (x + 130, 170), (x + 130, 76), (x + 75, 76)], True),
          P([(x - 75, 76), (30, 76), (30, 245), (x - 40, 245)], True), T(52, 66, "خیر", 11, "c", 700, S_RED), term(x, 245, 90, 28, "خروج")]
    o.append(T(x, 212, "ممکن است حتی یک‌بار هم اجرا نشود", 10, "c", 400, MU))
    # do-while
    x = 515
    o += [proc(x, 56, 140, 36, "بدنه", F3, 12), L(x, 74, x, 112, True), dia(x, 142, 150, 60, "cond ؟", F4, 12, True),
          P([(x + 75, 142), (x + 130, 142), (x + 130, 56), (x + 70, 56)], True), T(x + 108, 132, "بله", 11, "l", 700, S_GRN),
          L(x, 172, x, 230, True), T(x + 14, 200, "خیر", 11, "l", 700, S_RED), term(x, 245, 90, 28, "خروج")]
    o.append(T(x - 5, 100, "حداقل یک‌بار اجرا می‌شود", 10, "r", 400, MU)) if False else None
    o.append(T(380, 100, "همیشه حداقل\nیک‌بار اجرا می‌شود", 10, "c", 400, MU))
    o.append(L(340, 30, 340, 270, False, "4 4", 1.2, "#B9B3D1"))
    return svg(W, H, "".join(o))

def f_accum():
    W, H = 680, 235
    o = [T(340, 18, "int sum = 0;  for (int i = 1; i <= 4; i++)  sum = sum + i;", 12.5, "c", 700, INK, True)]
    vals = [0, 1, 3, 6, 10]
    labs = ["قبل از حلقه", "دور ۱ (i=1)", "دور ۲ (i=2)", "دور ۳ (i=3)", "دور ۴ (i=4)"]
    bw, gap = 104, 30
    for k, (v, lb) in enumerate(zip(vals, labs)):
        x = 676 - bw - k * (bw + gap)
        o.append(R(x, 56, bw, 62, F3 if k == 4 else F1, S_GRN if k == 4 else BR, 8, None, 2))
        o.append(T(x + bw / 2, 80, "sum", 11, "c", 400, MU, True)); o.append(T(x + bw / 2, 106, str(v), 22, "c", 700, INK, True))
        o.append(T(x + bw / 2, 140, lb, 10.5, "c", 400, MU))
        if k < 4:
            o.append(L(x - 2, 87, x - gap + 4, 87, True, None, 2.2)); o.append(T(x - gap / 2 + 1, 76, f"+{k+1}", 11, "c", 700, S_RED, True))
    o.append(R(40, 165, 600, 56, F2, S_BLUE, 8, None, 1.4))
    o.append(T(340, 188, "حلقه یک «ماشین انباشت» است: هر دور، مقدار قبلی را برمی‌دارد، چیزی به آن اضافه می‌کند و دوباره ذخیره می‌کند.", 11, "c", 500))
    o.append(T(340, 208, "برای همین مقدار اولیه‌ی sum باید قبل از حلقه صفر شود.", 11, "c", 700, S_BLUE))
    return svg(W, H, "".join(o))

def f_nested():
    W, H = 680, 285
    o = [T(340, 16, "for (i = 1..3)  { for (j = 1..4)  { ... } }", 12.5, "c", 700, INK, True)]
    x0, y0, cw, ch = 130, 40, 100, 62
    n = 0
    for i in range(3):
        o.append(T(x0 - 14, y0 + i * ch + 38, f"i = {i+1}", 12, "r", 700, BR, True))
        for j in range(4):
            n += 1
            o.append(R(x0 + j * cw, y0 + i * ch, cw - 8, ch - 8, F1 if (i + j) % 2 == 0 else F2, BR, 6, None, 1.5))
            o.append(T(x0 + j * cw + (cw - 8) / 2, y0 + i * ch + 36, f"({i+1},{j+1})", 13, "c", 700, INK, True))
            o.append(badge(x0 + j * cw + 14, y0 + i * ch + 14, n, 9))
            if j < 3: o.append(L(x0 + j * cw + cw - 6, y0 + i * ch + 27, x0 + j * cw + cw + 4, y0 + i * ch + 27, True, None, 1.6))
        if i < 2: o.append(P([(x0 + 3 * cw + 46, y0 + i * ch + 54), (x0 + 3 * cw + 46, y0 + i * ch + 62), (x0 + 46, y0 + i * ch + 62), (x0 + 46, y0 + i * ch + 66)], True, "4 3", 1.5, S_RED, True))
    for j in range(4): o.append(T(x0 + j * cw + 46, y0 + 3 * ch + 8, f"j = {j+1}", 11, "c", 700, BR, True))
    o.append(T(340, 270, "حلقه‌ی درونی در هر دورِ حلقه‌ی بیرونی، «کامل» اجرا می‌شود: در مجموع 3 × 4 = 12 بار.", 11, "c", 700, BR))
    return svg(W, H, "".join(o))

def f_offbyone():
    W, H = 680, 245
    o = []
    def row(y, title, n_ok, extra, bad):
        out = [T(10, y, title, 13, "l", 700, INK, True)]
        for i in range(n_ok):
            out.append(R(10 + i * 62, y + 12, 56, 40, F3, S_GRN, 6, None, 1.8)); out.append(T(38 + i * 62, y + 38, f"i={i}", 12, "c", 700, INK, True))
        if extra is not None:
            out.append(R(10 + n_ok * 62, y + 12, 56, 40, F5 if bad else "#fff", S_RED, 6, "4 3" if not bad else None, 1.8))
            out.append(T(38 + n_ok * 62, y + 38, f"i={extra}", 12, "c", 700, S_RED, True))
        return "".join(out)
    o.append(row(26, "for (int i = 0; i < 5; i++)", 5, 5, False))
    o.append(T(660, 72, "پنج بار اجرا شد (0 تا 4)؛ i = 5 شرط را شکست می‌دهد", 11, "r", 700, S_GRN))
    o.append(row(120, "for (int i = 0; i <= 5; i++)", 5, 5, True))
    o.append(T(660, 166, "شش بار اجرا شد! (0 تا 5)؛ یکی بیشتر از چیزی که می‌خواستیم", 11, "r", 700, S_RED))
    o.append(T(340, 220, "اشتباه «یکی کم یا یکی زیاد» (Off-by-one) شایع‌ترین خطای حلقه‌هاست؛ همیشه اولین و آخرین دور را ردیابی کنید.", 11, "c", 500, BR))
    return svg(W, H, "".join(o))

def f_loop_choose():
    W, H = 680, 305
    o = [dia(340, 55, 300, 80, "تعداد تکرار از قبل مشخص است؟", F4, 12.5),
         L(490, 55, 560, 55, True), T(525, 46, "بله", 12, "c", 700, S_GRN), box(560, 33, 100, 44, "for", F3, S_GRN, 16, True, 8, None, 700),
         L(340, 95, 340, 130, True), T(354, 118, "خیر", 12, "l", 700, S_RED),
         dia(340, 170, 300, 80, "حداقل یک‌بار باید اجرا شود؟", F4, 12.5),
         L(490, 170, 560, 170, True), T(525, 161, "بله", 12, "c", 700, S_GRN), box(560, 148, 100, 44, "do-while", F3, S_GRN, 14, True, 8, None, 700),
         L(340, 210, 340, 242, True), T(354, 230, "خیر", 12, "l", 700, S_RED), box(290, 244, 100, 44, "while", F3, S_GRN, 16, True, 8, None, 700),
         T(670, 100, "مثلاً: چاپ ۱ تا ۱۰", 10.5, "r", 400, MU), T(670, 215, "مثلاً: دریافت ورودی معتبر", 10.5, "r", 400, MU),
         T(190, 268, "مثلاً: تا وقتی کاربر «خروج» نزده", 10.5, "r", 400, MU)]
    return svg(W, H, "".join(o))

# ======================= فصل ۱۱ =======================
def f_blackbox():
    W, H = 680, 230
    o = [T(60, 20, "ورودی‌ها (آرگومان‌ها)", 11.5, "c", 700, S_BLUE)]
    for i, v in enumerate(["3", "4"]):
        y = 60 + i * 56
        o.append(box(30, y - 18, 56, 36, v, F2, S_BLUE, 16, True, 8, None, 700)); o.append(L(88, y, 190, 100 + (i - .5) * 30, True, None, 2.2))
    o.append(R(190, 40, 300, 130, F1, BR, 12, None, 2.4)); o.append(T(340, 28, "بدنه‌ی متد؛ جعبه‌ی سیاه", 11.5, "c", 700, BR))
    o.append(T(340, 78, "int Add(int a, int b)", 15, "c", 700, INK, True)); o.append(T(340, 112, "{ return a + b; }", 15, "c", 400, INK, True))
    o.append(T(340, 148, "استفاده‌کننده فقط ورودی و خروجی را می‌بیند", 10.5, "c", 400, MU))
    o.append(L(492, 105, 590, 105, True, None, 2.4)); o.append(box(592, 87, 58, 36, "7", F3, S_GRN, 18, True, 8, None, 700))
    o.append(T(620, 20, "خروجی (مقدار بازگشتی)", 11.5, "c", 700, S_GRN))
    o.append(T(340, 205, "int r = Add(3, 4);      ←      r = 7", 14, "c", 700, INK, True))
    return svg(W, H, "".join(o))

def f_param_arg():
    W, H = 680, 250
    cw = 8.4
    o = [R(24, 38, 300, 44, "#F5F3FB", "#8C82BF", 6, None, 1.3), T(40, 66, "int r = Add(3, 4);", 14, "l", 400, INK, True),
         R(24, 150, 400, 44, "#F5F3FB", "#8C82BF", 6, None, 1.3), T(40, 178, "static int Add(int a, int b)", 14, "l", 400, INK, True)]
    xa, xb = 40 + 19 * cw + 4, 40 + 26 * cw + 4
    o += [L(40 + 12 * cw + 4, 74, xa, 142, True, None, 2.2, S_BLUE), L(40 + 15 * cw + 4, 74, xb, 142, True, None, 2.2, S_BLUE),
          P([(424, 172), (470, 172), (470, 24), (78, 24), (78, 36)], True, None, 2.2, S_GRN)]
    o.append(T(484, 100, "مقدار بازگشتی\n(return a + b ← 7)", 11, "l", 700, S_GRN))
    o.append(T(670, 66, "فراخوانی (Call)", 12, "r", 700, BR)); o.append(T(670, 190, "تعریف (Definition)", 12, "r", 700, BR))
    o.append(T(340, 232, "آرگومان‌ها (3 و 4) = مقدارهای واقعی هنگام فراخوانی  ·  پارامترها (a و b) = متغیرهای ورودیِ تعریف متد", 11, "c", 500, BR))
    return svg(W, H, "".join(o))

def f_callstack():
    W, H = 680, 318
    o = [T(170, 16, "رفت: هر فراخوانی یک قاب تازه روی پشته می‌سازد", 11.5, "c", 700, BR), T(510, 16, "برگشت: قاب‌ها یکی‌یکی بسته می‌شوند", 11.5, "c", 700, S_GRN)]
    names = ["Main()", "Factorial(4)", "Factorial(3)", "Factorial(2)", "Factorial(1)"]
    waits = ["result = ؟", "4 * Factorial(3)", "3 * Factorial(2)", "2 * Factorial(1)", "n == 1 → پایه!"]
    rets = ["result = 24", "return 4 * 6 = 24", "return 3 * 2 = 6", "return 2 * 1 = 2", "return 1"]
    for i in range(5):
        y = 258 - i * 52
        top = i == 4
        o.append(R(40, y, 260, 42, F4 if top else F1, S_AMB if top else BR, 6, None, 2.2 if top else 1.6))
        o.append(T(170, y + 18, names[i], 12.5, "c", 700, INK, True)); o.append(T(170, y + 34, waits[i], 10.5, "c", 400, MU, i < 4 and i > 0))
        if i < 4: o.append(L(170, y - 1, 170, y - 9, True, None, 2))
        o.append(R(380, y, 260, 42, F3 if i else F2, S_GRN, 6, None, 1.8))
        o.append(T(510, y + 18, names[i], 12, "c", 700, INK, True)); o.append(T(510, y + 34, rets[i], 11, "c", 700, S_GRN, True))
        if i < 4: o.append(L(510, y - 9, 510, y - 1, True, None, 2, S_GRN, True)) if False else o.append(L(510, y - 1, 510, y - 9, True, None, 2, S_GRN))
    o.append(T(340, 290, "", 1))
    o.append(T(340, 312, "کم‌کم به پایین‌ترین قاب (پایه) می‌رسیم؛ جواب از آنجا شروع به برگشتن و ضرب‌شدن می‌کند.", 10.5, "c", 400, MU))
    return svg(W, H, "".join(o))

def f_fibtree():
    W, H = 680, 300
    nodes = {"a": (340, 28, "F(4)", 0), "b": (210, 92, "F(3)", 0), "c": (470, 92, "F(2)", 1),
             "d": (130, 160, "F(2)", 1), "e": (290, 160, "F(1)", 2), "f": (420, 160, "F(1)", 2), "g": (520, 160, "F(0)", 2),
             "h": (80, 230, "F(1)", 2), "i": (180, 230, "F(0)", 2)}
    edges = [("a", "b"), ("a", "c"), ("b", "d"), ("b", "e"), ("c", "f"), ("c", "g"), ("d", "h"), ("d", "i")]
    o = []
    for p, q in edges:
        o.append(L(nodes[p][0], nodes[p][1] + 18, nodes[q][0], nodes[q][1] - 18, False, None, 1.8))
    for k, (x, y, t, kind) in nodes.items():
        fill = {0: F1, 1: "url(#hatch)", 2: "url(#dots)"}[kind]
        o.append(f'<circle cx="{x}" cy="{y}" r="22" fill="{fill}" stroke="{BR}" stroke-width="2"/>')
        o.append(T(x, y + 4.5, t, 11.5, "c", 700, INK, True))
    o.append(R(560, 190, 112, 96, "#fff", BR, 8, None, 1.4))
    o.append(R(570, 202, 14, 10, "url(#hatch)", BR, 1)); o.append(T(664, 211, "تکراری", 10.5, "r", 400))
    o.append(R(570, 224, 14, 10, "url(#dots)", BR, 1)); o.append(T(664, 233, "حالت پایه", 10.5, "r", 400))
    o.append(R(570, 246, 14, 10, F1, BR, 1)); o.append(T(664, 255, "فراخوانی عادی", 10.5, "r", 400))
    o.append(T(340, 282, "F(2) دو بار محاسبه شد! برای n های بزرگ‌تر این تکرارها به‌صورت نمایی زیاد می‌شود؛ پس همیشه بازگشتی بهترین راه نیست.", 10.5, "c", 700, S_RED))
    return svg(W, H, "".join(o))

def f_scope():
    W, H = 680, 230
    o = [T(340, 18, "هر متغیر فقط داخل آکولادهایی که در آن تعریف شده «زنده» است", 12, "c", 700, BR)]
    o.append(R(30, 36, 290, 140, F1, BR, 10, None, 2)); o.append(T(175, 56, "static void Main()", 12.5, "c", 700, INK, True))
    o.append(R(60, 72, 230, 34, "#fff", S_GRN, 6, None, 1.6)); o.append(T(175, 94, "int x = 5;", 14, "c", 700, INK, True))
    o.append(T(175, 134, "x اینجا شناخته است ✔", 11.5, "c", 700, S_GRN)); o.append(T(175, 154, "(x فقط تا پایان Main زنده است)", 10, "c", 400, MU))
    o.append(R(360, 36, 290, 140, F2, BR, 10, None, 2)); o.append(T(505, 56, "static int Add(int a, int b)", 12.5, "c", 700, INK, True))
    o.append(R(390, 72, 230, 34, "#fff", S_RED, 6, "4 3", 1.6)); o.append(T(505, 94, "return x + a;   // error", 13, "c", 700, S_RED, True))
    o.append(T(505, 134, "x اینجا ناشناخته است ✘", 11.5, "c", 700, S_RED)); o.append(T(505, 154, "CS0103: The name 'x' does not exist", 10, "c", 400, MU, True))
    o.append(P([(390, 90), (340, 90), (292, 90)], True, "5 4", 2.2, S_RED, True))
    o.append(T(340, 205, "برای فرستادن مقدار به متدی دیگر باید آن را «آرگومان» بدهید، نه اینکه انتظار داشته باشید متد x را ببیند.", 11, "c", 500, BR))
    return svg(W, H, "".join(o))

# ======================= فصل ۱۲ =======================
def f_errtypes3():
    W, H = 680, 235
    cols = [("خطای کامپایل", "قبل از اجرا", "کامپایلر برنامه را قبول نمی‌کند", "CS1002: ; expected", F4, S_AMB, "Console.WriteLine(1)"),
            ("خطای زمان اجرا", "وسط اجرا", "برنامه شروع می‌شود و ناگهان می‌ایستد", "DivideByZeroException", "url(#hatch)", S_RED, "int r = 10 / zero;"),
            ("خطای منطقی", "بعد از اجرا", "برنامه کامل اجرا می‌شود، ولی جواب غلط است", "بدون هیچ پیام خطایی!", F2, S_BLUE, "a + b / 2")]
    o = []
    for i, (t, when, desc, ex, f, st, code) in enumerate(cols):
        x = 680 - 10 - 210 - i * 225
        o.append(R(x, 10, 210, 205, f, st, 10, None, 2.2))
        o.append(T(x + 105, 38, t, 15, "c", 700))
        o.append(R(x + 45, 50, 120, 22, "#fff", st, 11, None, 1.4)); o.append(T(x + 105, 66, when, 11.5, "c", 700, st))
        o.append(T(x + 105, 98, desc, 10.5, "c", 400))
        o.append(R(x + 12, 118, 186, 32, "#fff", BR, 5, None, 1.3)); o.append(T(x + 105, 139, code, 11, "c", 700, INK, True))
        o.append(R(x + 12, 162, 186, 34, "#fff", st, 5, "4 3", 1.4)); o.append(T(x + 105, 183, ex, 10.5 if i < 2 else 11, "c", 700, st, i < 2))
    o.append(T(340, 232, "پیدا کردنِ خطای کامپایل آسان‌تر از زمان اجرا، و آن هم آسان‌تر از خطای منطقی است.", 11, "c", 500, BR))
    return svg(W, 242, "".join(o))

def f_errmsg():
    W, H = 680, 170
    o = [R(10, 20, 660, 46, "#1B1736", "#17132B", 8, None, 1.5)]
    o.append(T(24, 49, "Program.cs(7,32): error CS1002: ; expected", 17, "l", 700, "#FFE9A8", True))
    ax = [75, 157, 304, 406]
    bx = [90, 240, 390, 560]
    labs = [("نام فایل", "کدام فایل؟"), ("خط ۷ و ستون ۳۲", "کجا؟"), ("کد خطا: CS1002", "چه نوع؟"), ("توضیح کامپایلر", "چه چیزی کم است؟")]
    for a_, b_, (t1, t2) in zip(ax, bx, labs):
        o.append(P([(a_, 68), (a_, 80), (b_, 80), (b_, 94)], True, None, 1.8, BR, False))
        o.append(R(b_ - 68, 96, 136, 44, "#fff", BR, 6, None, 1.5)); o.append(T(b_, 115, t1, 11.5, "c", 700)); o.append(T(b_, 132, t2, 10.5, "c", 400, MU))
    o.append(T(340, 160, "همیشه اول «شماره‌ی خط» و «کد خطا» را بخوانید؛ بیشتر مواقع همان خط یا خط قبل از آن مشکل دارد.", 11.5, "c", 500, BR))
    return svg(W, H, "".join(o))

def f_debugloop():
    W, H = 680, 185
    steps = [("۱. تکرار کن", "با کدام ورودی خراب می‌شود؟", F4), ("۲. محدود کن", "با print یا breakpoint ببین از کجا غلط شد", F2),
             ("۳. حدس بزن", "چرا؟ مقدار واقعی را با مقدار انتظار مقایسه کن", F1), ("۴. اصلاح کن", "فقط یک چیز را عوض کن", F3), ("۵. دوباره آزمون کن", "ورودی قبلی + ورودی‌های مرزی", F5)]
    o = []
    bw, gap = 118, 17
    for i, (t, s, f) in enumerate(steps):
        x = 680 - 10 - bw - i * (bw + gap)
        o.append(R(x, 30, bw, 100, f, BR, 8, None, 2))
        o.append(T(x + bw / 2, 56, t, 12.5, "c", 700))
        words = s.split(" ")
        line, y, lines = "", 80, []
        for w_ in words:
            if len(line + " " + w_) > 17 and line: lines.append(line); line = w_
            else: line = (line + " " + w_).strip()
        lines.append(line)
        for k, ln in enumerate(lines[:3]): o.append(T(x + bw / 2, 80 + k * 15, ln, 10, "c", 400, MU))
        if i < 4: o.append(L(x - 2, 80, x - gap + 2, 80, True, None, 2.2))
    o.append(P([(60, 138), (60, 172), (620, 172), (620, 138)], True, "5 4", 2, S_RED, True))
    o.append(T(340, 166, "اگر هنوز درست نشد، برگرد به گام ۲ ✎", 11.5, "c", 700, S_RED))
    return svg(W, H, "".join(o))

# ======================= فصل ۱۲ (رشته‌ها) =======================
def f_strindex():
    W, H = 680, 225
    o = []
    ch = "Hello"; cw = 70; x0 = (W - cw * 5) / 2
    o.append(T(x0 - 14, 52, "از ابتدا", 11, "r", 700, BR)); o.append(T(x0 - 14, 124, "از انتها", 11, "r", 700, BR))
    for i, c in enumerate(ch):
        x = x0 + i * cw
        fill = "url(#hatch)" if 1 <= i <= 3 else F2
        o.append(R(x, 60, cw, 44, fill, BR, 4, None, 2))
        o.append(T(x + cw / 2, 90, c, 22, "c", 700, INK, True))
        o.append(T(x + cw / 2, 48, str(i), 13, "c", 700, S_BLUE, True))
        o.append(T(x + cw / 2, 124, "^" + str(5 - i), 13, "c", 700, S_RED, True))
    o.append(P([(x0 + cw, 146), (x0 + cw, 156), (x0 + 4 * cw, 156), (x0 + 4 * cw, 146)], False, None, 2, BR))
    o.append(T(340, 176, 's.Substring(1, 3)  ==  s[1..4]  ==  "ell"', 13, "c", 700, INK, True))
    o.append(T(340, 198, "شروع از اندیس ۱، به طول ۳ — در بازه‌ی [a..b] اندیس b شامل نمی‌شود", 11, "c", 400, MU))
    o.append(T(340, 18, 'string s = "Hello";    s.Length == 5', 12.5, "c", 700, INK, True))
    return svg(W, H, "".join(o))

def f_immut():
    W, H = 680, 215
    o = []
    # left panel
    o.append(R(10, 10, 325, 195, F1, BR, 10, None, 2)); o.append(T(172, 32, "s.ToUpper();   ← بدون انتساب", 12, "c", 700, S_RED, True))
    o.append(T(60, 70, "s", 13, "c", 700, INK, True)); o.append(L(72, 66, 112, 66, True, None, 2))
    o.append(R(116, 50, 80, 32, "#fff", BR, 5, None, 2)); o.append(T(156, 72, '"abc"', 14, "c", 700, INK, True))
    o.append(R(116, 108, 80, 32, "#fff", S_RED, 5, "4 3", 1.8)); o.append(T(156, 130, '"ABC"', 14, "c", 700, S_RED, True))
    o.append(L(156, 82, 156, 106, True, "4 3", 1.6, S_RED)); o.append(T(236, 92, "نسخه‌ی جدید", 11, "l", 500, S_RED))
    o.append(T(236, 130, "گم می‌شود", 11, "l", 500, S_RED))
    o.append(T(172, 175, "مقدار s همچنان  abc  است", 12, "c", 700, INK))
    # right panel
    o.append(R(345, 10, 325, 195, F3, BR, 10, None, 2)); o.append(T(507, 32, "s = s.ToUpper();", 12, "c", 700, S_GRN, True))
    o.append(T(395, 70, "s", 13, "c", 700, INK, True)); o.append(P([(407, 70), (440, 70), (440, 124), (470, 124)], True, None, 2))
    o.append(R(470, 50, 80, 32, "#eee", MU, 5, "4 3", 1.4)); o.append(T(510, 72, '"abc"', 14, "c", 400, MU, True))
    o.append(R(470, 108, 80, 32, "#fff", BR, 5, None, 2)); o.append(T(510, 130, '"ABC"', 14, "c", 700, INK, True))
    o.append(T(590, 72, "قدیمی", 11, "l", 400, MU))
    o.append(T(507, 175, "s حالا به نسخه‌ی جدید اشاره می‌کند", 12, "c", 700, INK))
    return svg(W, H, "".join(o))

def f_splitjoin():
    W, H = 680, 205
    o = []
    o.append(R(215, 12, 250, 38, F2, BR, 6, None, 2)); o.append(T(340, 37, '"Ali,Sara,Reza"', 15, "c", 700, INK, True))
    o.append(L(340, 52, 340, 80, True, None, 2)); o.append(T(352, 71, "Split(',')", 12, "l", 700, S_BLUE, True))
    for i, w_ in enumerate(["Ali", "Sara", "Reza"]):
        x = 150 + i * 135
        o.append(R(x, 84, 110, 40, F4, BR, 6, None, 2)); o.append(T(x + 55, 110, '"' + w_ + '"', 14, "c", 700, INK, True))
        o.append(T(x + 55, 140, f"parts[{i}]", 11, "c", 500, MU, True))
    o.append(T(60, 108, "string[]", 12, "c", 700, BR, True))
    o.append(L(340, 148, 340, 168, True, None, 2)); o.append(T(352, 162, 'string.Join(" - ", parts)', 12, "l", 700, S_GRN, True))
    o.append(R(190, 170, 300, 30, F3, BR, 6, None, 2)); o.append(T(340, 191, '"Ali - Sara - Reza"', 14, "c", 700, INK, True))
    return svg(W, 205, "".join(o))

# ======================= فصل ۱۲ (آرایه‌ها) =======================
def f_arrmem():
    W, H = 680, 215
    o = []
    vals = [12, 7, 19, 3, 15]; cw = 84; x0 = (W - cw * 5) / 2
    o.append(T(340, 20, "int[] a = { 12, 7, 19, 3, 15 };      a.Length == 5", 12.5, "c", 700, INK, True))
    for i, v in enumerate(vals):
        x = x0 + i * cw
        o.append(R(x, 62, cw, 50, F2 if i % 2 == 0 else F4, BR, 3, None, 2))
        o.append(T(x + cw / 2, 94, v, 20, "c", 700, INK, True))
        o.append(T(x + cw / 2, 52, f"a[{i}]", 12.5, "c", 700, S_BLUE, True))
        o.append(T(x + cw / 2, 130, f"0x{0x2000 + 4 * i:X}", 9.5, "c", 400, MU, True))
    o.append(T(x0 - 10, 92, "a", 15, "r", 700, INK, True))
    o.append(P([(x0, 150), (x0, 160), (x0 + 5 * cw, 160), (x0 + 5 * cw, 150)], False, None, 2, BR))
    o.append(T(340, 180, "۵ خانه‌ی هم‌نوع و پشت‌سرهم در حافظه؛ شماره‌ی خانه‌ها از ۰ شروع می‌شود", 11.5, "c", 500, BR))
    o.append(T(340, 202, "اندیس مجاز: ۰ تا a.Length - 1  (یعنی ۰ تا ۴)", 11.5, "c", 700, S_RED))
    return svg(W, H, "".join(o))

def f_arralias():
    W, H = 680, 250
    o = []
    # left: alias
    o.append(R(10, 10, 325, 230, F1, BR, 10, None, 2)); o.append(T(172, 32, "b = a;     (هر دو یک آرایه‌اند)", 12.5, "c", 700, S_RED, True))
    o.append(T(46, 82, "a", 14, "c", 700, INK, True)); o.append(T(46, 142, "b", 14, "c", 700, INK, True))
    o.append(P([(60, 80), (120, 80), (120, 104)], True, None, 2)); o.append(P([(60, 140), (120, 140), (120, 124)], True, None, 2))
    for i, v in enumerate([10, 2, 3]):
        o.append(R(100 + i * 60, 104, 60, 40, "#fff", BR, 3, None, 2)); o.append(T(130 + i * 60, 131, v, 17, "c", 700, INK, True))
    o.append(T(172, 180, "b[0] = 10;", 12, "c", 700, INK, True))
    o.append(T(172, 204, "a[0] هم ۱۰ شد!", 12, "c", 700, S_RED))
    # right: clone
    o.append(R(345, 10, 325, 230, F3, BR, 10, None, 2)); o.append(T(507, 32, "c = (int[])a.Clone();     (کپی مستقل)", 12.5, "c", 700, S_GRN, True))
    o.append(T(380, 76, "a", 14, "c", 700, INK, True)); o.append(P([(394, 74), (420, 74), (420, 88)], True, None, 2))
    for i, v in enumerate([10, 2, 3]):
        o.append(R(400 + i * 50, 88, 50, 34, "#fff", BR, 3, None, 2)); o.append(T(425 + i * 50, 111, v, 15, "c", 700, INK, True))
    o.append(T(380, 156, "c", 14, "c", 700, INK, True)); o.append(P([(394, 154), (420, 154), (420, 168)], True, None, 2))
    for i, v in enumerate([10, 20, 3]):
        o.append(R(400 + i * 50, 168, 50, 34, "#fff", S_GRN if i == 1 else BR, 3, None, 2)); o.append(T(425 + i * 50, 191, v, 15, "c", 700, INK, True))
    o.append(T(507, 226, "c[1] = 20  ←  a تغییر نکرد", 11.5, "c", 700, S_GRN, True))
    return svg(W, H, "".join(o))

def f_arrswap():
    W, H = 680, 215
    o = []
    vals = [1, 2, 3, 4, 5]; cw = 70; x0 = (W - 5 * cw) / 2
    o.append(T(340, 20, "برعکس‌کردن در جا: دو اشاره‌گر i و j به هم نزدیک می‌شوند", 12.5, "c", 700, BR))
    for row, (lab, arr, ij) in enumerate([("شروع", [1, 2, 3, 4, 5], (0, 4)), ("بعد از ۱ تعویض", [5, 2, 3, 4, 1], (1, 3)), ("بعد از ۲ تعویض", [5, 4, 3, 2, 1], (2, 2))]):
        y = 38 + row * 60
        for i, v in enumerate(arr):
            x = x0 + i * cw
            f = "url(#hatch)" if i in ij and row < 2 else F2
            o.append(R(x, y, cw, 34, f, BR, 3, None, 2)); o.append(T(x + cw / 2, y + 23, v, 16, "c", 700, INK, True))
        if row < 2:
            o.append(T(x0 + ij[0] * cw + cw / 2, y + 50, "i", 12, "c", 700, S_BLUE, True)); o.append(T(x0 + ij[1] * cw + cw / 2, y + 50, "j", 12, "c", 700, S_RED, True))
        else:
            o.append(T(x0 + 2 * cw + cw / 2, y + 50, "i = j  → توقف", 11, "c", 700, S_GRN))
        o.append(T(x0 - 12, y + 22, lab, 11, "r", 500, MU))
    return svg(W, H, "".join(o))

def f_arr2d():
    W, H = 680, 215
    o = []
    m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    cw, ch = 72, 42; x0 = (W - 4 * cw) / 2 - 20; y0 = 56
    o.append(T(340, 18, "int[,] m = new int[3, 4];      m.GetLength(0) == 3     m.GetLength(1) == 4", 12, "c", 700, INK, True))
    for c in range(4): o.append(T(x0 + c * cw + cw / 2, y0 - 8, f"ستون {c}", 10.5, "c", 700, S_BLUE))
    for r in range(3):
        o.append(T(x0 - 8, y0 + r * ch + 26, f"سطر {r}", 10.5, "r", 700, S_RED))
        for c in range(4):
            f = "url(#hatch)" if (r == 1 and c == 2) else (F2 if (r + c) % 2 == 0 else F4)
            o.append(R(x0 + c * cw, y0 + r * ch, cw, ch, f, BR, 2, None, 2))
            o.append(T(x0 + c * cw + cw / 2, y0 + r * ch + 17, m[r][c], 15, "c", 700, INK, True))
            o.append(T(x0 + c * cw + cw / 2, y0 + r * ch + 34, f"[{r},{c}]", 9, "c", 400, MU, True))
    o.append(T(340, 200, "m[1, 2] == 7  (هاشور) — اول سطر، بعد ستون", 11.5, "c", 700, BR))
    return svg(W, 215, "".join(o))
