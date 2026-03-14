from PIL import Image, ImageDraw, ImageFont


def load_korean_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    """Load a Korean-capable font with graceful fallback."""
    candidates = [
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc",
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def create_dragon_art(output_path: str = "dragon_fire_yuyongjun.png") -> None:
    w, h = 1400, 900
    image = Image.new("RGBA", (w, h), (255, 255, 255, 255))
    draw = ImageDraw.Draw(image)

    outline = (20, 25, 30, 255)
    body = (143, 203, 117, 255)
    body_shadow = (118, 176, 96, 255)
    horn = (245, 231, 141, 255)
    ear = (240, 212, 134, 255)
    belly = (248, 238, 177, 255)

    # Tail (behind body)
    tail = [(1060, 620), (1170, 570), (1240, 640), (1130, 700)]
    draw.polygon(tail, fill=body, outline=outline, width=10)

    # Wings (behind body)
    left_wing = [(280, 480), (200, 390), (300, 310), (400, 390), (365, 480)]
    right_wing = [(900, 470), (1020, 360), (1110, 430), (1050, 540), (930, 550)]
    draw.polygon(left_wing, fill=body, outline=outline, width=10)
    draw.polygon(right_wing, fill=body, outline=outline, width=10)
    draw.polygon(
        [(245, 420), (300, 365), (345, 415), (300, 445)],
        fill=(177, 223, 157, 255),
        outline=outline,
        width=6,
    )
    draw.polygon(
        [(965, 450), (1025, 400), (1065, 445), (1010, 500)],
        fill=(177, 223, 157, 255),
        outline=outline,
        width=6,
    )

    # Body and head
    draw.ellipse((300, 250, 980, 840), fill=body, outline=outline, width=12)
    draw.ellipse((370, 160, 920, 660), fill=body, outline=outline, width=12)
    draw.ellipse((380, 430, 900, 860), fill=body_shadow, outline=None)

    # Horns
    horns = [
        [(450, 190), (510, 90), (560, 200)],
        [(560, 170), (630, 70), (680, 185)],
        [(690, 160), (760, 80), (810, 190)],
        [(790, 200), (845, 110), (900, 230)],
    ]
    for points in horns:
        draw.polygon(points, fill=horn, outline=outline, width=8)

    # Ears
    draw.polygon([(340, 430), (280, 360), (355, 325), (420, 380)], fill=ear, outline=outline, width=8)
    draw.polygon([(960, 410), (1040, 335), (1110, 395), (1015, 470)], fill=ear, outline=outline, width=8)

    # Face
    draw.ellipse((510, 430, 575, 495), fill=outline)
    draw.ellipse((690, 430, 755, 495), fill=outline)
    draw.ellipse((598, 560, 622, 585), fill=outline)
    draw.ellipse((668, 560, 692, 585), fill=outline)
    draw.ellipse((560, 620, 710, 760), fill=outline)
    draw.ellipse((592, 650, 675, 733), fill=(221, 128, 112, 255))

    # Belly
    draw.ellipse((545, 690, 760, 885), fill=belly, outline=outline, width=8)
    for y in [736, 772, 808, 844]:
        draw.arc((565, y - 20, 740, y + 20), start=180, end=360, fill=(214, 197, 138, 255), width=4)

    # Arms / feet
    draw.polygon([(470, 700), (360, 760), (455, 815), (570, 760)], fill=body, outline=outline, width=10)
    draw.polygon([(790, 720), (875, 790), (990, 755), (900, 680)], fill=body, outline=outline, width=10)

    # Fire breath
    outer_fire = [
        (740, 675), (835, 620), (940, 585), (1030, 550), (1130, 500),
        (1200, 530), (1265, 470), (1300, 545), (1270, 605), (1320, 665),
        (1260, 715), (1180, 695), (1100, 740), (990, 760), (880, 730), (790, 700),
    ]
    inner_fire = [
        (845, 670), (935, 630), (1020, 605), (1100, 570), (1170, 585),
        (1215, 560), (1245, 610), (1210, 645), (1245, 675), (1190, 700),
        (1120, 680), (1040, 720), (950, 725), (890, 705),
    ]
    draw.polygon(outer_fire, fill=(255, 146, 52, 255), outline=outline, width=8)
    draw.polygon(inner_fire, fill=(255, 235, 107, 255), outline=(230, 140, 48, 255), width=5)

    # Fire particles
    for cx, cy, r in [(1090, 470, 14), (1175, 760, 13), (980, 535, 9), (1265, 620, 10)]:
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(255, 203, 82, 255), outline=(230, 140, 48, 255), width=3)

    # Korean text on top of fire
    text = "유용준"
    font = load_korean_font(96)
    tx, ty = 1020, 620
    # Stroke effect for readability on bright fire
    for ox in [-4, -2, 0, 2, 4]:
        for oy in [-4, -2, 0, 2, 4]:
            if ox == 0 and oy == 0:
                continue
            draw.text((tx + ox, ty + oy), text, font=font, fill=(26, 34, 40, 255))
    draw.text((tx, ty), text, font=font, fill=(255, 255, 255, 255))

    image.save(output_path)


if __name__ == "__main__":
    create_dragon_art()
