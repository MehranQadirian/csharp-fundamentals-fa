<div dir="rtl">

# مبانی کامپیوتر با C# — جزوه‌ی متن‌باز فارسی

[![Build PDF](https://github.com/mehranqadirian/csharp-fundamentals-fa/actions/workflows/build.yml/badge.svg)](https://github.com/mehranqadirian/csharp-fundamentals-fa/actions/workflows/build.yml)
[![Release](https://img.shields.io/github/v/release/mehranqadirian/csharp-fundamentals-fa?label=release)](https://github.com/mehranqadirian/csharp-fundamentals-fa/releases/latest)
[![License: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/content-CC%20BY--SA%204.0-lightgrey.svg)](LICENSE-CONTENT.md)

جزوه‌ی آموزشی **«مبانی کامپیوتر»** با زبان **C#** برای دانشجویانی که پیش از ورود به **برنامه‌نویسی شیءگرا (OOP)** می‌خواهند
پایه‌ها را محکم یاد بگیرند. این مخزن **سورس کامل جزوه** و ابزار ساخت PDF آن است؛ هر کسی می‌تواند در تکمیل آن مشارکت کند.

نویسنده: **مهران قدیریان** (Mehran Ghadirian)

## 📥 دانلود

آخرین نسخه‌ی PDF را از بخش **[Releases](https://github.com/mehranqadirian/csharp-fundamentals-fa/releases/latest)** دانلود کنید.

## 📚 فهرست فصل‌ها

| # | فصل | # | فصل |
|---|---|---|---|
| ۱ | آشنایی با سی‌شارپ و IDE | ۸ | تبدیل انواع، `char` و ASCII |
| ۲ | تعاریف پایه و ذهنیت حل مسئله | ۹ | تصمیم‌ها: `if`، `switch`، سه‌تایی |
| ۳ | اولین برنامه و `Console` | ۱۰ | حلقه‌ها |
| ۴ | کاراکترهای کنترلی | ۱۱ | متدها و بازگشتی |
| ۵ | متغیرها، انواع داده، ثابت‌ها | ۱۲ | آرایه‌ها |
| ۶ | عملگرهای ریاضی | ۱۳ | رشته‌ها (`string`) |
| ۷ | کلاس `Math` | ۱۴ | خطایابی (Debugging) |

به‌علاوه: **تمرین‌های بیشتر** (سه سطح) و **پاسخنامه‌ی کامل** با جدول جست‌وجوی سریع.

## ✨ ویژگی‌ها

- شکل و نمودار مفهومی در هر فصل، مثال با خروجی و تمرین در هر بخش
- کادرهای ویژه: نکته‌ی مهم، نگاه مفهومی، اشتباه رایج، نکته‌ی «خودمونی» و مطالعه‌ی بیشتر
- بدنه‌ی رنگی که در **چاپ سیاه‌وسفید** هم خوانا می‌ماند؛ جلد و پشت‌جلد رنگی
- ارجاع‌ها و شماره‌ی صفحه‌ی پاسخ‌ها **خودکار** ساخته می‌شود (نیازی به ویرایش دستی نیست)

## 🛠️ ساخت PDF روی کامپیوتر خودتان

نیازمندی‌ها: Python 3.10+ و اینترنت برای نصب یک‌باره‌ی Chromium.

```bash
git clone https://github.com/mehranqadirian/csharp-fundamentals-fa.git
cd csharp-fundamentals-fa

pip install -r requirements.txt
playwright install chromium

make pdf VERSION=dev        # یا دستی: cd book && python3 make_covers.py && python3 build.py
```

خروجی: `book/dist/C-Sharp-Fundamentals.pdf`

> برای نمایش درست شکلک‌ها در PDF، یک فونت emoji (مثلاً Noto Color Emoji) روی سیستم نصب باشد. فونت‌های فارسی و کد داخل مخزن هستند.

## 🗂️ ساختار مخزن

```text
.
├── book/
│   ├── chapters/         متن فصل‌ها (ch01.html … ch14.html) + final.html (تمرین‌های بیشتر) + answers.html
│   ├── front.html        فهرست، راهنمای استفاده و «درباره‌ی جزوه»
│   ├── figs*.py          شکل‌های SVG (هر شکل یک تابع پایتون)
│   ├── style.css         ظاهر صفحه‌ها
│   ├── build.py          ساخت بدنه‌ی PDF (فهرست، ارجاع‌ها، پاسخنامه)
│   ├── make_covers.py    جلد و پشت‌جلد
│   └── fonts/            فونت‌ها (OFL)
├── docs/                 راهنمای سبک نوشتن و یادداشت‌های انتشار
├── .github/workflows/    ساخت خودکار PDF و انتشار Release
└── CONTRIBUTING.md       راهنمای مشارکت
```

## 🚀 انتشار (Release)

با ساختن یک تگ نسخه، GitHub Actions خودش PDF را می‌سازد و در بخش Releases منتشر می‌کند:

```bash
git tag -a v1.0.0 -m "v1.0.0"
git push origin v1.0.0
```

توضیحات نسخه از فایل `docs/release-notes/<tag>.md` (Markdown) خوانده می‌شود؛ اگر نبود، GitHub خودش changelog می‌سازد.

## 🤝 مشارکت

از هر نوع کمکی استقبال می‌کنیم: گزارش اشتباه، پیشنهاد تمرین، بهبود شکل‌ها، ترجمه و نوشتن فصل‌های جدید.
لطفاً قبل از شروع [`CONTRIBUTING.md`](CONTRIBUTING.md) و [`docs/STYLE_GUIDE.md`](docs/STYLE_GUIDE.md) را بخوانید
و به [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) پایبند باشید.

## 🗺️ نقشه‌ی راه

- [x] ۱.۰ — مبانی C# (فصل‌های ۱ تا ۱۴)
- [ ] جزوه‌ی **برنامه‌نویسی شیءگرا (OOP)**: کلاس، شیء، سازنده، وراثت، چندریختی
- [ ] تمرین‌ها و پروژه‌های کوچک بیشتر
- [ ] نسخه‌ی وب (HTML) جزوه
- [ ] نسخه‌ی انگلیسی

برای پیشنهاد یا برداشتن یکی از این کارها، یک Issue باز کنید.

## 📄 مجوز

- **متن، شکل‌ها و تمرین‌ها:** [CC BY-SA 4.0](LICENSE-CONTENT.md)
- **کد (ابزار ساخت و نمونه‌کدها):** [MIT](LICENSE)
- **فونت‌ها و نشان C#:** [NOTICE.md](NOTICE.md)

</div>

---

# English

**Computer Fundamentals with C#** — an open-source, Persian (Farsi, right-to-left) handout for students who need solid
fundamentals before learning object-oriented programming. This repository contains the **complete source** of the book
and the toolchain that turns it into a print-ready PDF.

- **Download:** latest PDF from [Releases](https://github.com/mehranqadirian/csharp-fundamentals-fa/releases/latest).
- **Build locally:** `pip install -r requirements.txt && playwright install chromium && make pdf`
  → `book/dist/C-Sharp-Fundamentals.pdf`.
- **Contribute:** see [CONTRIBUTING.md](CONTRIBUTING.md) (issues, typo fixes, new exercises, new chapters).
- **Release:** push a tag like `v1.0.0`; the *Release* workflow builds the PDF and publishes it with Markdown notes
  from `docs/release-notes/<tag>.md`.
- **License:** text & figures CC BY-SA 4.0, code MIT, fonts OFL — see [NOTICE.md](NOTICE.md).

Author: Mehran Ghadirian.
