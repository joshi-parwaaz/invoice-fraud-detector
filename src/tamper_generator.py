# scripts/tamper_generator.py

import os
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Paths
REAL_DIR = 'data/real'
TAMPERED_DIR = 'data/tampered'
os.makedirs(TAMPERED_DIR, exist_ok=True)

# --- Existing tampering functions ---
def apply_black_box(img):
    draw = ImageDraw.Draw(img)
    w, h = img.size
    x1 = random.randint(50, w // 2)
    y1 = random.randint(50, h // 2)
    x2 = x1 + random.randint(50, 150)
    y2 = y1 + random.randint(20, 50)
    draw.rectangle([x1, y1, x2, y2], fill='black')
    return img

def apply_fake_text(img):
    draw = ImageDraw.Draw(img)
    w, h = img.size
    try:
        font = ImageFont.truetype("arial.ttf", size=22)
    except:
        font = ImageFont.load_default()
    x = random.randint(100, w - 150)
    y = random.randint(100, h - 50)
    draw.text((x, y), "FAKE $999", fill='red', font=font)
    return img

def apply_blur_patch(img):
    w, h = img.size
    x = random.randint(50, w - 200)
    y = random.randint(50, h - 100)
    patch = img.crop((x, y, x + 150, y + 50)).filter(ImageFilter.GaussianBlur(radius=5))
    img.paste(patch, (x, y))
    return img

# --- NEW tampering functions ---
def apply_whiteout(img):
    draw = ImageDraw.Draw(img)
    w, h = img.size
    x1 = random.randint(100, w - 200)
    y1 = random.randint(100, h - 100)
    x2 = x1 + random.randint(80, 150)
    y2 = y1 + random.randint(20, 40)
    draw.rectangle([x1, y1, x2, y2], fill='white')
    return img

def overlay_random_shape(img):
    draw = ImageDraw.Draw(img)
    w, h = img.size
    x = random.randint(50, w - 100)
    y = random.randint(50, h - 100)
    size = random.randint(30, 60)
    shape = random.choice(['ellipse', 'rectangle'])
    color = random.choice(['blue', 'purple', 'grey'])
    if shape == 'ellipse':
        draw.ellipse([x, y, x + size, y + size], fill=color)
    else:
        draw.rectangle([x, y, x + size, y + size], fill=color)
    return img

def apply_fake_signature(img):
    draw = ImageDraw.Draw(img)
    w, h = img.size
    x = random.randint(100, w - 200)
    y = random.randint(h - 150, h - 80)
    for _ in range(3):
        curve = [(x + i * 15, y + random.randint(-10, 10)) for i in range(5)]
        draw.line(curve, fill='black', width=2)
    return img

# --- Main tampering function ---
def tamper_image(img_path, save_path):
    img = Image.open(img_path).convert("RGB")
    tamper_methods = [
        apply_black_box,
        apply_fake_text,
        apply_blur_patch,
        apply_whiteout,
        overlay_random_shape,
        apply_fake_signature
    ]
    method = random.choice(tamper_methods)
    tampered_img = method(img)
    tampered_img.save(save_path)

def generate_tampered_images(n=600):
    real_imgs = os.listdir(REAL_DIR)
    selected = random.sample(real_imgs, min(n, len(real_imgs)))
    for i, filename in enumerate(selected):
        real_path = os.path.join(REAL_DIR, filename)
        tamper_path = os.path.join(TAMPERED_DIR, f"tampered_{i}.jpg")
        tamper_image(real_path, tamper_path)
    print(f"✅ Generated {len(selected)} tampered images in {TAMPERED_DIR}/")

if __name__ == "__main__":
    generate_tampered_images(n=600)
