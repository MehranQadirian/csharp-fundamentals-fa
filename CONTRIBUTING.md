# راهنمای مشارکت · Contributing

ممنون که می‌خواهید در تکمیل این جزوه کمک کنید! 🙌 این سند می‌گوید چطور.

## انواع مشارکت

| کار | چطور |
|---|---|
| 🐞 غلط املایی، اشتباه علمی، خطای کد یا پاسخ نادرست | یک [Issue](../../issues/new/choose) بسازید (فصل، شماره‌ی صفحه و پیشنهاد اصلاح را بنویسید) یا مستقیم Pull Request بدهید |
| ✏️ تمرین یا مثال بهتر | Pull Request؛ تمرین جدید حتماً **پاسخ** هم داشته باشد |
| 🎨 شکل تازه یا بهبود شکل | Pull Request؛ شکل‌ها در `book/figs*.py` هستند (راهنما در `docs/STYLE_GUIDE.md`) |
| 📖 فصل یا جزوه‌ی تازه (مثلاً OOP) | **اول یک Issue بسازید** تا هماهنگ شویم و کار تکراری نشود |
| 🌍 ترجمه، نسخه‌ی وب، ابزار ساخت | Issue + بحث؛ سپس Pull Request |

## شروع سریع

```bash
git clone https://github.com/<your-user>/csharp-fundamentals-fa.git   # از Fork خودتان
cd csharp-fundamentals-fa
pip install -r requirements.txt && playwright install chromium
git checkout -b fix/chapter-5-typo
# ... ویرایش فایل‌ها ...
make pdf VERSION=dev              # خروجی: book/dist/C-Sharp-Fundamentals.pdf
git commit -am "fix(ch05): غلط املایی در بخش ثابت‌ها"
git push origin fix/chapter-5-typo     # بعد Pull Request بسازید
```

## قواعد مهم نوشتن

۱. **کدها را اجرا کنید.** هر مثال و هر خروجی را واقعاً اجرا کنید (ترجیحاً با .NET 8 یا جدیدتر)؛ خروجی نوشته‌شده باید عیناً درست باشد.
۲. **پیش‌نیاز را رعایت کنید.** در هر فصل فقط از چیزهایی استفاده کنید که قبلاً در جزوه آمده‌اند. اگر چیز جدیدی لازم است، آن را در همان‌جا کوتاه توضیح دهید یا در «مطالعه‌ی بیشتر» بیاورید.
۳. **لحن را حفظ کنید:** رسمی برای تعریف‌ها، گفت‌وگویی برای مفاهیم، «خودمونی» فقط در کادرهای نکته. جزئیات در [`docs/STYLE_GUIDE.md`](docs/STYLE_GUIDE.md).
۴. **سیاه‌وسفید-امن:** معنی کادرها و شکل‌ها نباید فقط به رنگ وابسته باشد (برچسب، آیکون، الگو و حاشیه هم بگذارید).
۵. **شماره‌ی صفحه‌ها را دستی ننویسید.** ارجاع‌ها خودکار ساخته می‌شوند.
۶. **ابتدا ساخت محلی:** قبل از Pull Request، `make pdf` را اجرا کنید و صفحه‌های تغییرکرده را در PDF ببینید. خروجی build نباید `missing=['...']` داشته باشد.
۷. **تغییرات کوچک و متمرکز.** هر Pull Request یک موضوع؛ فایل‌های تولیدشده (`book/dist`, `body.*`, ...) را کامیت نکنید.

## پیام کامیت

از قالب ساده‌ی [Conventional Commits](https://www.conventionalcommits.org/) استفاده می‌کنیم:

```text
fix(ch05): اصلاح جدول اندازه‌ی انواع داده
feat(ch12): افزودن تمرین ۱۲.۱۱ درباره‌ی آرایه‌ی دوبعدی
docs: به‌روزرسانی README
```

نوع‌ها: `feat` (محتوای تازه)، `fix` (اصلاح)، `docs`، `style` (ظاهر/CSS)، `build`، `ci`، `chore`.

## بررسی و پذیرش

- ساخت خودکار PDF روی هر Pull Request اجرا می‌شود؛ خروجی را از بخش *Artifacts* همان اجرا می‌توانید بگیرید.
- نویسنده یا مسئول مخزن بازبینی می‌کند؛ ممکن است تغییراتی بخواهد. بازبینی‌ها درباره‌ی «متن» است، نه «شخص».
- پذیرش به معنی موافقت با مجوزهاست: **محتوا CC BY-SA 4.0** و **کد MIT** ([توضیح](LICENSE-CONTENT.md)).
- نام شما می‌تواند در بخش «مشارکت‌کنندگان» یادداشت‌های هر نسخه بیاید.

## رفتار

با احترام و حرفه‌ای باشید؛ [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) را ببینید.

---

## English summary

- **Report problems** via Issues (chapter + page number + suggested fix). **Small fixes** can go straight to a Pull Request.
- **New chapters:** open an issue first to coordinate.
- Run every code sample and make sure the printed output is exact; only use concepts introduced earlier in the book.
- Follow `docs/STYLE_GUIDE.md` (tone, boxes, exercise ids, figures). Don't hard-code page numbers.
- Build locally with `make pdf`; the CI also builds a PDF for each PR.
- Contributions are licensed CC BY-SA 4.0 (content) and MIT (code). Use Conventional Commit messages.
