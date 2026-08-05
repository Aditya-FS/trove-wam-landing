from pathlib import Path

try:
    from PIL import Image
except ImportError:
    raise SystemExit("pip install pillow  (then re-run this script)")

ICONS = Path(__file__).resolve().parent / "assets" / "Icons"
BLACK_T = 30


def knock_out_black(im: Image.Image) -> Image.Image:
    im = im.convert("RGBA")
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if r <= BLACK_T and g <= BLACK_T and b <= BLACK_T:
                px[x, y] = (0, 0, 0, 0)
    return im


def is_mostly_black_or_empty(path: Path) -> bool:
    if not path.exists():
        return True
    im = Image.open(path).convert("RGBA")
    px = im.load()
    w, h = im.size
    visible = 0
    for y in range(0, h, max(1, h // 64)):
        for x in range(0, w, max(1, w // 64)):
            r, g, b, a = px[x, y]
            if a > 20 and (r > BLACK_T or g > BLACK_T or b > BLACK_T):
                visible += 1
    return visible < 8


def red_to_dark_gray(im: Image.Image) -> Image.Image:
    im = im.convert("RGBA")
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a < 10:
                continue
            if r > 80 and r >= g * 1.4 and r >= b * 1.4:
                px[x, y] = (55, 55, 55, a)
            elif r > BLACK_T or g > BLACK_T or b > BLACK_T:
                lum = int(0.3 * r + 0.59 * g + 0.11 * b)
                v = max(40, min(90, lum))
                px[x, y] = (v, v, v, a)
    return im


def save(im: Image.Image, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    im.save(dest, "PNG")
    print(f"wrote {dest.name}")


def main() -> None:
    if not ICONS.exists():
        raise SystemExit(f"Missing {ICONS}")

    cap_jpg = ICONS / "Capital_S.jpg"
    cap_png = ICONS / "Capital_S.png"
    if cap_jpg.exists() and (not cap_png.exists() or is_mostly_black_or_empty(cap_png)):
        save(knock_out_black(Image.open(cap_jpg)), cap_png)

    pairs = [
        ("Home_R.png", "Home_S.png"),
        ("Strategy_R.png", "Strategy_S.png"),
        ("Capital_R.png", "Capital_S.png"),
        ("PI_R.png", "PI_S.png"),
        ("ET_R.png", "ET_S.png"),
        ("Customer_R.png", "Customer_S.png"),
    ]

    for r_name, s_name in pairs:
        r_path = ICONS / r_name
        s_path = ICONS / s_name
        if not r_path.exists():
            print(f"skip missing {r_name}")
            continue

        r_im = knock_out_black(Image.open(r_path))
        save(r_im, r_path)

        if s_name == "Home_S.png" and s_path.exists() and not is_mostly_black_or_empty(s_path):
            save(knock_out_black(Image.open(s_path)), s_path)
            continue

        if s_name == "Capital_S.png" and s_path.exists() and not is_mostly_black_or_empty(s_path):
            save(knock_out_black(Image.open(s_path)), s_path)
            continue

        if is_mostly_black_or_empty(s_path) or not s_path.exists():
            s_im = red_to_dark_gray(r_im.copy())
            save(s_im, s_path)
        else:
            save(knock_out_black(Image.open(s_path)), s_path)

    print("Done.")


if __name__ == "__main__":
    main()
