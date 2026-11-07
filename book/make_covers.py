import random, os
random.seed(7)
ROOT = os.path.dirname(os.path.abspath(__file__))
VERSION = os.environ.get("BOOK_VERSION", "dev")
cols = ["#2A1766","#3B1F96","#512BD4","#6B4BE0","#8B6FE8","#B9A7F2","#DCD3F9","#0078D4","#2B9BE8","#9ED0F5","#00B7C3"]
# mosaic: 7 x 7, only a staircase triangle is filled
cells = []
for r in range(7):
    for c in range(7):
        if c + r < 8 and random.random() > 0.18:
            col = random.choice(cols)
            cells.append(f'<i style="grid-row:{r+1};grid-column:{c+1};background:{col}"></i>')
mosaic = "".join(cells)

chapters = ["آشنایی با سی‌شارپ","تعاریف و ذهن برنامه‌نویس","اولین برنامه و Console","کاراکترهای کنترلی","متغیرها و انواع داده","عملگرهای ریاضی",
            "کلاس Math","تبدیل انواع و ASCII","ساختارهای تصمیم","حلقه‌ها","متدها و بازگشتی","آرایه‌ها","رشته‌ها (string)","خطایابی"]
fa = "۱۲۳۴۵۶۷۸۹"
def num(i): return str(i) if i < 10 else "".join(fa[int(d)-1] if d != "0" else "۰" for d in str(i))
fadig = {"0":"۰","1":"۱","2":"۲","3":"۳","4":"۴","5":"۵","6":"۶","7":"۷","8":"۸","9":"۹"}
def pnum(i): return "".join(fadig[d] for d in str(i))
tiles = "".join(f'<div class="t t{(i%4)}"><b>{pnum(i+1)}</b><span>{t}</span></div>' for i, t in enumerate(chapters))

cover = f'''<!doctype html><html lang="fa" dir="rtl"><head><meta charset="utf-8"><style>
@font-face{{font-family:Vz;src:url(fonts/Vazirmatn-Regular.ttf);font-weight:400}}
@font-face{{font-family:Vz;src:url(fonts/Vazirmatn-Medium.ttf);font-weight:500}}
@font-face{{font-family:Vz;src:url(fonts/Vazirmatn-Bold.ttf);font-weight:700}}
@font-face{{font-family:JB;src:url(fonts/JetBrainsMono-Regular.ttf);font-weight:400}}
@font-face{{font-family:JB;src:url(fonts/JetBrainsMono-Bold.ttf);font-weight:700}}
@page{{size:210mm 297mm;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:210mm;height:297mm}}
body{{font-family:Vz;color:#1B1240;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{position:relative;width:210mm;height:297mm;overflow:hidden;background:linear-gradient(180deg,#FFFFFF 0%,#F5F2FD 55%,#EAE4FB 100%)}}
.mosaic{{position:absolute;left:-24px;top:-24px;display:grid;grid-template-columns:repeat(7,64px);grid-template-rows:repeat(7,64px);gap:8px;direction:ltr}}
.mosaic i{{border-radius:10px;display:block}}
.top{{position:absolute;right:16mm;top:14mm;text-align:right}}
.top .en{{font-family:JB;font-size:10.5px;letter-spacing:2.5px;color:#512BD4;font-weight:700}}
.top .dt{{font-size:12px;color:#4A4660;margin-top:3px}}
.logo{{position:absolute;right:16mm;top:40mm;width:38mm}}
.logo img{{width:100%;display:block}}
.title{{position:absolute;right:16mm;left:16mm;top:82mm}}
.title .lab{{font-family:JB;font-size:11px;letter-spacing:3px;color:#0078D4;font-weight:700;margin-bottom:6px}}
.title h1{{font-size:78px;line-height:1.15;font-weight:700;color:#1F1147}}
.title h1 span{{color:#512BD4}}
.row{{position:absolute;right:16mm;left:16mm;top:140mm;display:flex;justify-content:space-between;align-items:flex-end;gap:20px}}
.author .k{{font-size:11px;color:#6A6488;letter-spacing:.5px}}
.author .n{{font-size:28px;font-weight:700;color:#1B1240;line-height:1.5}}
.author .r{{font-size:11.5px;color:#4A4660}}
.author .bar{{width:46px;height:5px;background:#512BD4;border-radius:3px;margin-bottom:8px}}
.quote{{direction:rtl;border-left:5px solid #0078D4;padding:2px 0 2px 16px;max-width:300px;text-align:left}}
.quote .q{{font-size:44px;line-height:.6;color:#0078D4;font-family:serif;height:20px;text-align:left}}
.quote .t{{font-size:19px;font-weight:500;color:#2A1766;text-align:left;line-height:1.7;direction:rtl}}
.win{{position:absolute;left:16mm;right:16mm;top:172mm;background:#1B1736;border-radius:12px;overflow:hidden;box-shadow:0 14px 0 -4px #CFC4F4;direction:ltr}}
.win .bar{{background:#2E2860;padding:7px 14px;display:flex;gap:6px;align-items:center}}
.win .bar b{{width:10px;height:10px;border-radius:50%;display:block}}
.win .bar span{{margin-left:10px;font-family:JB;font-size:10.5px;color:#C9C0F2}}
.win pre{{font-family:JB;font-size:13px;line-height:1.65;color:#EDEAFB;padding:14px 20px 16px;margin:0}}
.kw{{color:#B79DFF}}.ty{{color:#6FD3FF}}.st{{color:#FFC98B}}.fn{{color:#8BE9B4}}.cm{{color:#9A93C9;font-style:italic}}
.chips{{position:absolute;left:16mm;right:16mm;top:240mm;display:grid;grid-template-columns:repeat(5,1fr);gap:7px}}
.t{{border-radius:8px;padding:6px 10px 7px;display:flex;align-items:center;gap:8px;color:#fff;min-height:36px}}
.t b{{font-size:17px;font-weight:700;min-width:20px;text-align:center}}
.t span{{font-size:10.5px;line-height:1.35}}
.t0{{background:#2A1766}}.t1{{background:#512BD4}}.t2{{background:#0B5FA5}}.t3{{background:#00717A}}
.foot{{position:absolute;left:16mm;right:16mm;bottom:11mm;display:flex;justify-content:space-between;font-size:11px;color:#4A4660;border-top:1.5px solid #CFC4F4;padding-top:7px}}
.foot .ltr{{direction:ltr;font-family:JB;font-size:10px}}
</style></head><body><div class="page">
<div class="mosaic">{mosaic}</div>
<div class="top"><div class="en">COMPUTER FUNDAMENTALS</div><div class="dt">جزوه‌ی آموزشی · آبان ۱۴۰۵</div></div>
<div class="logo"><img src="logo.png"></div>
<div class="title"><div class="lab">CONSOLE · TYPES · LOGIC · LOOPS · METHODS</div><h1>مبانی<br><span>کامپیوتر</span></h1></div>
<div class="row">
 <div class="author"><div class="bar"></div><div class="k">نویسنده</div><div class="n">مهران قدیریان</div></div>
 <div class="quote"><div class="q">“</div><div class="t">زبان برنامه‌نویسی سی‌شارپ</div></div>
</div>
<div class="win"><div class="bar"><b style="background:#FF6B6B"></b><b style="background:#FFD166"></b><b style="background:#5CD6A0"></b><span>Program.cs</span></div>
<pre><span class="kw">class</span> <span class="ty">Program</span>
{{
    <span class="kw">static void</span> <span class="fn">Main</span>()
    {{
        <span class="ty">Console</span>.<span class="fn">WriteLine</span>(<span class="st">"Hello, C#!"</span>);  <span class="cm">// let's begin</span>
    }}
}}</pre></div>
<div class="chips">{tiles}</div>
<div class="foot"><span>۱۴ فصل · مثال و شکل · تمرین و پاسخنامه</span><span class="ltr">Console · Operators · Math · Loops · Methods</span></div>
</div></body></html>'''
open(f"{ROOT}/cover.html","w",encoding="utf-8").write(cover)

back = '''<!doctype html><html lang="fa" dir="rtl"><head><meta charset="utf-8"><style>
@font-face{font-family:Vz;src:url(fonts/Vazirmatn-Regular.ttf);font-weight:400}
@font-face{font-family:Vz;src:url(fonts/Vazirmatn-Medium.ttf);font-weight:500}
@font-face{font-family:Vz;src:url(fonts/Vazirmatn-Bold.ttf);font-weight:700}
@font-face{font-family:JB;src:url(fonts/JetBrainsMono-Regular.ttf);font-weight:400}
@font-face{font-family:JB;src:url(fonts/JetBrainsMono-Bold.ttf);font-weight:700}
@page{size:210mm 297mm;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:210mm;height:297mm}
body{font-family:Vz;color:#fff;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{position:relative;width:210mm;height:297mm;overflow:hidden;background:linear-gradient(160deg,#2A1766 0%,#3B1F96 45%,#512BD4 100%)}
.g{opacity:.55;z-index:0;position:absolute;right:-30px;bottom:-30px;display:grid;grid-template-columns:repeat(6,48px);grid-template-rows:repeat(6,48px);gap:8px;direction:ltr}
.g i{display:block;border-radius:10px}
.wrap{z-index:2;position:absolute;right:18mm;left:18mm;top:26mm}
.kick{direction:ltr;text-align:right;font-family:JB;font-size:11px;letter-spacing:3px;color:#BFB0FF;font-weight:700}
h1{font-size:50px;line-height:1.35;margin:8px 0 18px;font-weight:700}
h1 span{color:#FFD24A}
p{font-size:15.5px;line-height:2.15;color:#F1EDFF;margin-bottom:12px;text-align:justify}
.big{margin-top:22px;border-right:6px solid #FFD24A;padding-right:16px;font-size:25px;line-height:1.7;font-weight:700;color:#fff}
.code{margin-top:26px;background:#1E1050;border:1.5px solid #8B6FE8;border-radius:12px;padding:14px 20px;direction:ltr;font-family:JB;font-size:15px;line-height:1.8;color:#EDEAFB}
.k{color:#B79DFF}.f{color:#8BE9B4}.c{color:#9A93C9;font-style:italic}
.next{margin-top:22px;display:flex;gap:12px;align-items:center}
.next .tag{background:#FFD24A;color:#2A1766;font-weight:700;border-radius:8px;padding:2px 14px;font-size:13px}
.next .tx{font-size:14px;color:#E4DCFF}
.sig{z-index:3;position:absolute;right:18mm;left:18mm;bottom:14mm;display:flex;justify-content:space-between;align-items:flex-end;border-top:1.5px solid #8B6FE8;padding-top:10px}
.sig .n{font-size:19px;font-weight:700}.sig .r{font-size:12px;color:#CFC4F4}
.sig .ltr{direction:ltr;font-family:JB;font-size:11px;color:#CFC4F4}
</style></head><body><div class="page">
<div class="g">GRID</div>
<div class="wrap">
<div class="kick">WHY PROGRAMMING?</div>
<h1>همین حالا <span>شروع</span> می‌شود</h1>
<p>هر نرم‌افزاری که امروز از آن استفاده می‌کنید؛ از پیام‌رسان گوشی‌تان تا بازی‌ای که شب‌ها سرگرمتان می‌کند، روزی فقط یک پنجره‌ی خالی و یک خط کد بود. کسی که آن را نوشت، نه نابغه بود و نه جادوگر؛ فقط شروع کرد، خطا دید، اصلاح کرد و ادامه داد.</p>
<p>برنامه‌نویسی به شما یاد می‌دهد مسئله‌های بزرگ را به قطعه‌های کوچک تقسیم کنید، اشتباه را دشمن ندانید و صبورانه دنبال دلیلش بگردید. مهارتی که فقط پشت کامپیوتر نمی‌ماند و در تمام زندگی همراهتان می‌شود، و در عین حال، دری به سوی ساختن بازی، اپلیکیشن، سایت و هوش مصنوعی است.</p>
<p>اگر امروز یک حلقه برایتان گنگ است یا یک خطای قرمز کلافه‌تان کرده، بدانید همه‌ی کسانی که امروز حرفه‌ای‌اند، روزی دقیقاً همین‌جا ایستاده بودند. فاصله‌ی «تازه‌کار» تا «برنامه‌نویس» چیزی جز تمرین روزانه و کنجکاوی نیست.</p>
<div class="big">کدی که امروز می‌نویسید،<br>دنیای فردای شماست.</div>
<div class="code"><span class="k">while</span> (<span class="k">true</span>)<br>{<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="f">Learn</span>();&nbsp; <span class="f">Practice</span>();&nbsp; <span class="f">Grow</span>();&nbsp; <span class="c">// no break needed :)</span><br>}</div>
<div class="next"><span class="tag">جزوه‌ی بعدی</span><span class="tx">برنامه‌نویسی شیءگرا (OOP)؛ کلاس‌ها، شیءها و طراحی نرم‌افزار</span></div>
</div>
<div class="sig"><div><div class="n">مهران قدیریان</div></div><div class="ltr">github.com/mehranqadirian/csharp-fundamentals-fa<br>C# Fundamentals · vVERSION_TOKEN</div></div>
</div></body></html>'''
random.seed(3)
gc = ["#6B4BE0","#8B6FE8","#B9A7F2","#2B9BE8","#0078D4","#FFD24A","#3B1F96","#00B7C3"]
gcell = ""
for r in range(6):
    for c in range(6):
        if (5-r) + (5-c) < 7 and random.random() > 0.2:
            gcell += f'<i style="grid-row:{r+1};grid-column:{c+1};background:{random.choice(gc)};opacity:{random.choice([.35,.5,.7,.9])}"></i>'
back = back.replace("GRID", gcell).replace("VERSION_TOKEN", VERSION)
open(f"{ROOT}/back.html","w",encoding="utf-8").write(back)

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch()
    for n in ["cover","back"]:
        pg = b.new_page(); pg.goto(f"file://{ROOT}/{n}.html"); pg.wait_for_load_state("networkidle"); pg.evaluate("document.fonts.ready")
        pg.pdf(path=f"{ROOT}/{n}.pdf", prefer_css_page_size=True, print_background=True)
    b.close()
print("covers ok")
