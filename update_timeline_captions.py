from pathlib import Path
import re
from datetime import datetime

file_path = Path("index.html")
html = file_path.read_text(encoding="utf-8")

captions = [
    "نینی رورو در اولین روز مدرسه",
    "رورو گوسفند کودک",
    "رورو با گذر زمان داف تر میشه(جونحح)",
    "رگیه موهاشو چتری کرد",
    "گوسفند خانم توی کمد نشسته",
    "رگیه گاث شده جونح بابا",
    "ندزدنت خوشگله......",
    "روگیه جذاب",
    "چه دافی...بوخوریمت",
]

section_match = re.search(
    r'(<section id="timeline" class="screen">)(.*?)(</section>)',
    html,
    flags=re.S
)

if not section_match:
    raise SystemExit("بخش timeline پیدا نشد.")

section_start, section_body, section_end = section_match.groups()

pattern = re.compile(r'(<figcaption class="polaroid-caption">)(.*?)(</figcaption>)', re.S)
matches = list(pattern.finditer(section_body))

if len(matches) < 9:
    raise SystemExit(f"فقط {len(matches)} کپشن پیدا شد. باید حداقل 9 تا باشد.")

def repl(match_iter):
    i = repl.counter
    repl.counter += 1
    old = match_iter.group(0)
    if i < 9:
        return f'<figcaption class="polaroid-caption">{captions[i]}</figcaption>'
    return old

repl.counter = 0
new_section_body = pattern.sub(repl, section_body)

new_html = html[:section_match.start()] + section_start + new_section_body + section_end + html[section_match.end():]

backup_dir = Path(".backups")
backup_dir.mkdir(exist_ok=True)
stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
backup_file = backup_dir / f"index.html.before-caption-update-{stamp}"
backup_file.write_text(html, encoding="utf-8")

file_path.write_text(new_html, encoding="utf-8")

print("✅ کپشن‌ها با موفقیت عوض شدند.")
print(f"📦 بکاپ: {backup_file}")
