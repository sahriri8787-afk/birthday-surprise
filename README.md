# Birthday Surprise — Termux Edition

نسخه‌ی آماده‌ی اجرای پروژه تولد با فضای دریایی، انیمیشن ماهی و لاک‌پشت، هدیه آبی، ژورنال ورق‌زدنی، CD چرخان، کارت‌های پیش‌بینی، کیک، نامه و هدیه نهایی.

در این نسخه یک **دکمه‌ی آبی گرد و بامزه با مثلث پخش** هم به صفحه ورود و صفحه موسیقی اضافه شده است.

## نصب در Termux

```bash
termux-setup-storage
pkg update
pkg install python unzip
cd ~
unzip -o ~/storage/downloads/Birthday-Surprise-Blue-Buttons-Termux.zip
cd birthday-surprise-starter
bash install-termux.sh
bash ~/birthday-surprise/start.sh
```

بعد در مرورگر باز کن:

`http://127.0.0.1:8080`

اگر اسم ZIP متفاوت بود، اسم واقعی فایل را جایگزین کن.

## Update — Journal photo replacements
- Journal page 1 replaced with the new uploaded design.
- Journal page 2 replaced with the new uploaded design.
- Old standalone journal-photo-1.jpg and journal-photo-2.jpg assets were removed.
