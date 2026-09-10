import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
STATIC_IMG = BASE_DIR / 'work' / 'static' / 'img'
MEDIA_ANIME = BASE_DIR / 'media' / 'anime'

STATIC_IMG.mkdir(parents=True, exist_ok=True)

# Copy generated hero and background
brain_dir = Path(r"C:\Users\Harsh\.gemini\antigravity-ide\brain\5be38b6a-33c3-47e4-bbce-deb10f504731")
landing_img = brain_dir / "anime_landing_hero_1789015497603.jpg"
dark_bg = brain_dir / "anime_dark_background_1789015516434.jpg"

if landing_img.exists():
    shutil.copy2(landing_img, STATIC_IMG / "new.webp")
    shutil.copy2(landing_img, STATIC_IMG / "new.jpg")
    print("Copied landing image to static/img/new.webp")

if dark_bg.exists():
    shutil.copy2(dark_bg, STATIC_IMG / "back.jpg")
    print("Copied dark background to static/img/back.jpg")

# Also copy first.jpg, secound.jpg, third.jpg, fourth.jpg, fifth.jpg to static/img just in case
for fname in ["first.jpg", "secound.jpg", "third.jpg", "fourth.jpg", "fifth.jpg", "sixth.jpg", "seventh.jpg", "eighth.jpg", "nineth.jpg", "tenth.jpg", "eleventh.jpg", "tewlth.jpg"]:
    src = MEDIA_ANIME / fname
    if src.exists():
        shutil.copy2(src, STATIC_IMG / fname)
        print(f"Copied {fname} to static/img/")

print("Asset sync completed successfully!")
