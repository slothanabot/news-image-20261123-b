#!/usr/bin/env python3
"""Render the news-image-20261123 entry (account B / Slothana).

Atlas style: a large dot-grid world map with numbered pins for the top
stories, a lead strip on COP31, and 35 real stories -- first reported
Monday 23 November 2026 -- grouped into 7 region cards, plus a
"day in numbers" card.

Deterministic: no network, no clock, no randomness. Running this script
twice writes byte-identical entry.png. main.py (stdlib only) copies the
committed entry.png to the output directory at grade time, because the
grader runs with no network and installs nothing (so PIL is not
available there).

Sources for the stories: Reuters, AP, AFP, CNN, The Hindu, Al Jazeera
(wire reports of 23 November 2026). The full story list with sources
lives in README.md.
"""

import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
F_BOLD = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")
F_REG = os.path.join(FONT_DIR, "DejaVuSans.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


# ---------------------------------------------------------------- palette
BG = (12, 27, 46)          # deep navy page
OCEAN = (15, 38, 64)       # map ocean
LAND = (216, 201, 143)     # sand dots for land
GRAT = (31, 62, 96)        # graticule lines
CREAM = (245, 239, 224)    # headline cream
GOLD = (227, 200, 120)     # gold accent
CARD = (22, 41, 74)        # story card body
CARD_LINE = (42, 74, 107)  # card border
WHITE = (255, 255, 255)
DETAIL = (168, 191, 212)   # story detail grey-blue
MUTED = (122, 148, 175)    # footer grey
RED = (192, 57, 43)        # pins / lead strip
LEAD_BG = (123, 36, 28)
MAP_LABEL = (227, 200, 120)
OCEAN_LABEL = (74, 107, 138)

# ---------------------------------------------------------------- stories
# (number, headline, detail) -- 35 stories, 5 per region.
REGIONS = [
    ("CLIMATE & PLANET", (39, 174, 96), [
        (1, "COP31 collapses - no deal on fossil fuels",
         "No deal in Antalya; longest COP ever"),
        (2, "Guterres 'deeply disappointed' by failure",
         "UN chief: world must do much more"),
        (3, "Albanese blames 'difficult geopolitical times'",
         "Australia's PM reacts as co-host"),
        (4, "UN talks on lethal AI weapons to continue",
         "Nations agree to keep negotiating"),
        (5, "WHO: fighting disrupts Ebola response in Congo",
         "Chief pleads for peace near outbreak"),
    ]),
    ("MIDDLE EAST", (192, 57, 43), [
        (6, "Houthis claim strike on Saudi Rabigh refinery",
         "Coalition: missiles downed; 6 hurt"),
        (7, "Iran-linked attack hits Bahrain industrial site",
         "Two wounded; IRGC claims radar hits"),
        (8, "Saudi defences down Houthi missiles at Riyadh",
         "Drone intercepted over the capital"),
        (9, "Two tankers hit near Strait of Hormuz",
         "UKMTO: strikes off Oman"),
        (10, "Netanyahu-Eisenkot talks fail, no government",
         "Israel coalition talks end, no deal"),
    ]),
    ("EUROPE & UKRAINE", (36, 113, 163), [
        (11, "Russian drone hits Kyiv flats; 14 missing",
         "Dymer: rescuers dig through rubble"),
        (12, "Zelenskyy urges US to release Patriot missiles",
         "2,700 drones fired in a week"),
        (13, "Russian cargo ship ablaze off Finland",
         "Sparta II crew evacuated"),
        (14, "Jet drone crosses into Moldova twice",
         "Fell during attacks on Ukraine"),
        (15, "Thousands march in Lisbon over living costs",
         "Anger at prices fills the streets"),
    ]),
    ("THE AMERICAS", (214, 137, 16), [
        (16, "Mexico captures 'El Chapo Isidro'; 11 dead",
         "FBI most-wanted boss seized"),
        (17, "Democrats win 258 House seats, most since 1992",
         "Largest House majority since 1992"),
        (18, "Father and daughter held by ICE at Seattle airport",
         "Pair were bound for a baptism"),
        (19, "Nine shot at California concert; one critical",
         "Gunfire erupts at a concert"),
        (20, "US presses Nvidia over chips sold to China",
         "Bessent demands compliance chief"),
    ]),
    ("ASIA - PACIFIC", (125, 60, 152), [
        (21, "Nepal PM holds talks with Modi in Delhi",
         "Balendra Shah on state visit"),
        (22, "India post record 720/9d in Wellington",
         "Biggest Test total in New Zealand"),
        (23, "South Korea minister quits over AI exam cheating",
         "College-entrance chaos ends his job"),
        (24, "Myanmar junta calls ASEAN decision 'unfair'",
         "Army-backed government hits back"),
        (25, "Factory fire in Indonesia leaves dozens missing",
         "Seven bodies found; search goes on"),
    ]),
    ("AFRICA", (20, 143, 119), [
        (26, "24 civilians killed in fresh South Sudan violence",
         "SPLA-IO forces blamed"),
        (27, "35 Fulani killed in revenge attacks in Nigeria",
         "Violence flares in Kano state"),
        (28, "Drone strikes hit homes and UN building in Khartoum",
         "Sudan capital attacked, UN says"),
        (29, "UN urges probe into Benghazi attacks",
         "Warns Libya: don't be a battleground"),
        (30, "Somalia builds naval base with Turkish help",
         "Ankara deepens Horn of Africa role"),
    ]),
    ("SPORT & CULTURE", (169, 50, 107), [
        (31, "Liverpool thrash Man Utd 4-0 at Anfield",
         "Yoro sent off in 7 minutes"),
        (32, "Hull stun high-flying Brighton 2-0",
         "Late brace sinks the Seagulls"),
        (33, "Sindarov takes White in chess title Game 1",
         "2026 FIDE World Championship"),
        (34, "Anupama keeps world women's snooker crown",
         "Indian star defends IBSF title"),
        (35, "Jeweller Paolo Bulgari dies aged 89",
         "Luxury dynasty loses patriarch"),
    ]),
]

NUMBERS = [
    ("35", "stories in this image"),
    ("194", "nations at the COP31 talks"),
    ("2,700", "drones fired at Ukraine"),
    ("258", "House seats, Democrats"),
    ("720/9d", "India's Test record"),
    ("11", "dead in the Sinaloa cartel raid"),
    ("4-0", "Liverpool over Man Utd"),
    ("14", "missing in Kyiv-region strike"),
]

# (story number, lon, lat, dx, dy) pins on the map.
PINS = [
    (1, 30.7, 36.9, 0, 0),       # Antalya, COP31
    (6, 39.0, 22.8, 0, 0),       # Rabigh refinery
    (7, 50.6, 26.2, 12, -14),    # Bahrain
    (8, 46.7, 24.6, -14, 14),    # Riyadh
    (9, 56.5, 26.5, 16, 12),     # Strait of Hormuz
    (11, 30.5, 50.7, 12, 10),    # Dymer, Kyiv region
    (13, 27.0, 60.0, -18, -12),  # Gulf of Finland, Sparta II
    (16, -107.4, 25.6, 0, 0),    # Sinaloa
    (17, -77.0, 38.9, 0, 0),     # Washington DC
    (21, 77.2, 28.6, 0, 0),      # Delhi
    (22, 174.8, -41.3, 0, 0),    # Wellington
    (23, 127.0, 37.5, 0, 0),     # Seoul
    (27, 31.6, 4.85, 0, 0),      # Juba
    (28, 32.5, 15.6, 0, 0),      # Khartoum
    (31, -3.0, 53.4, 0, 0),      # Liverpool
]

# ---------------------------------------------------------------- map data
# Rough continent outlines in (lon, lat). Stylised atlas shapes.
POLYS = [
    # North America
    [(-168, 66), (-140, 70), (-125, 72), (-110, 73), (-95, 80), (-85, 70),
     (-75, 73), (-65, 62), (-55, 52), (-60, 47), (-70, 42), (-75, 35),
     (-80, 26), (-85, 30), (-90, 21), (-95, 19), (-105, 20), (-115, 28),
     (-125, 40), (-125, 49), (-140, 60), (-155, 58), (-165, 60)],
    # Greenland
    [(-58, 64), (-45, 60), (-30, 68), (-25, 76), (-40, 80), (-58, 76)],
    # South America
    [(-80, 10), (-75, 12), (-62, 10), (-52, 5), (-50, 0), (-40, -5),
     (-35, -8), (-40, -20), (-48, -28), (-58, -35), (-65, -45), (-70, -52),
     (-73, -40), (-73, -20), (-80, -5), (-81, 5)],
    # Africa
    [(-17, 15), (-10, 30), (0, 36), (10, 37), (20, 32), (32, 31), (35, 28),
     (43, 12), (51, 11), (48, 0), (40, -10), (35, -20), (32, -28),
     (20, -35), (12, -18), (9, -1), (9, 4), (-8, 5)],
    # Eurasia
    [(-10, 36), (-9, 43), (-2, 48), (0, 50), (5, 53), (8, 57), (18, 56),
     (21, 55), (28, 59), (30, 60), (28, 65), (35, 68), (45, 68), (55, 69),
     (70, 72), (80, 73), (100, 76), (120, 73), (140, 72), (160, 70),
     (178, 66), (170, 60), (162, 56), (158, 52), (142, 50), (140, 40),
     (135, 35), (130, 33), (127, 35), (122, 30), (120, 25), (110, 20),
     (105, 10), (100, 8), (97, 15), (92, 21), (88, 22), (80, 13),
     (75, 8), (72, 20), (66, 25), (60, 25), (57, 26), (52, 28), (48, 30),
     (44, 29), (40, 36), (36, 36), (30, 36), (26, 38), (22, 37), (18, 40),
     (12, 44), (8, 44), (3, 43), (-2, 37), (-9, 37)],
    # SE Asia islands
    [(95, 5), (105, 0), (115, -5), (125, -8), (135, -5), (140, -8),
     (130, -2), (120, 0), (110, 5)],
    # Australia
    [(113, -22), (114, -30), (115, -35), (124, -33), (132, -32), (137, -35),
     (140, -38), (147, -39), (150, -37), (153, -27), (150, -22), (146, -19),
     (142, -11), (136, -12), (132, -11), (126, -14), (122, -17)],
    # UK
    [(-5, 50), (-3, 53), (-5, 56), (-3, 58), (-1, 57), (0, 53), (1, 51)],
    # Japan
    [(130, 31), (132, 33), (135, 34), (137, 35), (139, 36), (140, 38),
     (141, 41), (142, 44), (140, 42), (138, 38)],
    # New Zealand
    [(167, -45), (170, -42), (174, -40), (177, -38), (175, -41), (172, -43)],
]

MAP_X0, MAP_Y0, MAP_X1, MAP_Y1 = 16, 108, 1008, 372
LAT_TOP, LAT_BOT = 75.0, -60.0


def lonlat_to_xy(lon, lat):
    x = MAP_X0 + (lon + 180.0) / 360.0 * (MAP_X1 - MAP_X0)
    y = MAP_Y0 + (LAT_TOP - lat) / (LAT_TOP - LAT_BOT) * (MAP_Y1 - MAP_Y0)
    return x, y


def point_in_poly(lon, lat, poly):
    inside = False
    n = len(poly)
    j = n - 1
    for i in range(n):
        xi, yi = poly[i]
        xj, yj = poly[j]
        if (yi > lat) != (yj > lat):
            xinters = (xj - xi) * (lat - yi) / (yj - yi) + xi
            if lon < xinters:
                inside = not inside
        j = i
    return inside


def on_land(lon, lat):
    return any(point_in_poly(lon, lat, p) for p in POLYS)


def wrap_text(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def ellipsize(draw, text, fnt, max_w):
    if draw.textlength(text, font=fnt) <= max_w:
        return text
    while text and draw.textlength(text + "...", font=fnt) > max_w:
        text = text[:-1]
    return text + "..."


def draw_map(draw):
    draw.rectangle([MAP_X0, MAP_Y0, MAP_X1, MAP_Y1], fill=OCEAN)
    # graticule every 30 degrees
    for lon in range(-150, 181, 30):
        x, _ = lonlat_to_xy(lon, 0)
        draw.line([(x, MAP_Y0), (x, MAP_Y1)], fill=GRAT, width=1)
    for lat in range(-60, 76, 30):
        _, y = lonlat_to_xy(0, lat)
        draw.line([(MAP_X0, y), (MAP_X1, y)], fill=GRAT, width=1)
    # dot-grid land
    step = 6
    x = MAP_X0 + 3
    while x < MAP_X1:
        y = MAP_Y0 + 3
        while y < MAP_Y1:
            lon = (x - MAP_X0) / (MAP_X1 - MAP_X0) * 360.0 - 180.0
            lat = LAT_TOP - (y - MAP_Y0) / (MAP_Y1 - MAP_Y0) * (LAT_TOP - LAT_BOT)
            if on_land(lon, lat):
                draw.ellipse([x - 2, y - 2, x + 2, y + 2], fill=LAND)
            y += step
        x += step
    # ocean labels
    f_ocean = font(F_REG, 13)
    for label, lon, lat in [("PACIFIC", -150, -25), ("ATLANTIC", -35, 5),
                            ("INDIAN OCEAN", 75, -30), ("PACIFIC", 150, 10)]:
        lx, ly = lonlat_to_xy(lon, lat)
        draw.text((lx, ly), label, font=f_ocean, fill=OCEAN_LABEL)
    # region labels (ocean-coloured backing so they read over the dots)
    f_reg = font(F_BOLD, 13)
    for label, lon, lat in [("NORTH AMERICA", -100, 58),
                            ("SOUTH AMERICA", -60, -18),
                            ("AFRICA", 8, 18),
                            ("ASIA", 100, 55),
                            ("OCEANIA", 138, -28)]:
        lx, ly = lonlat_to_xy(lon, lat)
        tw = draw.textlength(label, font=f_reg)
        draw.rectangle([lx - 3, ly - 2, lx + tw + 3, ly + 16], fill=OCEAN)
        draw.text((lx, ly), label, font=f_reg, fill=MAP_LABEL)
    # numbered pins
    f_pin = font(F_BOLD, 10)
    for num, lon, lat, dx, dy in PINS:
        px, py = lonlat_to_xy(lon, lat)
        cx, cy = px + dx, py + dy
        if dx or dy:
            draw.line([(px, py), (cx, cy)], fill=WHITE, width=1)
            draw.ellipse([px - 2, py - 2, px + 2, py + 2], fill=WHITE)
        draw.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], fill=RED,
                     outline=WHITE, width=1)
        tw = draw.textlength(str(num), font=f_pin)
        draw.text((cx - tw / 2, cy - 7), str(num), font=f_pin, fill=WHITE)


def draw_region_card(draw, x, y, w, h, name, color, stories):
    draw.rectangle([x, y, x + w, y + h], fill=CARD, outline=CARD_LINE, width=1)
    draw.rectangle([x, y, x + w, y + 30], fill=color)
    f_head = font(F_BOLD, 14)
    f_range = font(F_BOLD, 12)
    draw.text((x + 8, y + 8), name, font=f_head, fill=WHITE)
    rng = "%d-%d" % (stories[0][0], stories[-1][0])
    rw = draw.textlength(rng, font=f_range)
    draw.text((x + w - rw - 8, y + 9), rng, font=f_range, fill=WHITE)
    f_num = font(F_BOLD, 13)
    f_headline = font(F_BOLD, 12)
    f_detail = font(F_REG, 10)
    sy = y + 38
    for num, headline, detail in stories:
        draw.text((x + 8, sy), "%d." % num, font=f_num, fill=GOLD)
        tx = x + 30
        tw = w - 38
        lines = wrap_text(draw, headline, f_headline, tw)[:2]
        ly = sy
        for ln in lines:
            draw.text((tx, ly), ln, font=f_headline, fill=CREAM)
            ly += 15
        draw.text((tx, ly + 1), ellipsize(draw, detail, f_detail, tw),
                  font=f_detail, fill=DETAIL)
        sy += 44


def draw_numbers_card(draw, x, y, w, h):
    color = (183, 149, 11)
    draw.rectangle([x, y, x + w, y + h], fill=CARD, outline=CARD_LINE, width=1)
    draw.rectangle([x, y, x + w, y + 30], fill=color)
    f_head = font(F_BOLD, 14)
    draw.text((x + 8, y + 8), "THE DAY IN NUMBERS", font=f_head, fill=WHITE)
    f_num = font(F_BOLD, 19)
    f_lab = font(F_REG, 12)
    sy = y + 40
    for num, label in NUMBERS:
        draw.text((x + 10, sy), num, font=f_num, fill=GOLD)
        nw = draw.textlength(num, font=f_num)
        lx = x + 12 + nw + 8
        draw.text((lx, sy + 4),
                  ellipsize(draw, label, f_lab, x + w - lx - 8),
                  font=f_lab, fill=CREAM)
        sy += 27


def main():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # ---- header
    draw.rectangle([0, 0, W, 4], fill=GOLD)
    f_title = font(F_BOLD, 46)
    title = "THE WORLD IN ONE MAP"
    tw = draw.textlength(title, font=f_title)
    draw.text(((W - tw) / 2, 14), title, font=f_title, fill=CREAM)
    f_sub = font(F_BOLD, 20)
    sub = "MONDAY 23 NOVEMBER 2026  ·  35 STORIES  ·  7 REGIONS"
    sw = draw.textlength(sub, font=f_sub)
    draw.text(((W - sw) / 2, 66), sub, font=f_sub, fill=GOLD)

    # ---- map
    draw_map(draw)
    draw.rectangle([MAP_X0, MAP_Y0, MAP_X1, MAP_Y1], outline=GOLD, width=2)

    # ---- lead strip
    draw.rectangle([16, 380, 1008, 428], fill=LEAD_BG)
    f_lead = font(F_BOLD, 15)
    lead1 = "LEAD — COP31 COLLAPSES: the longest climate summit ever ends with no deal,"
    lead2 = "after the EU rejects a draft that never names fossil fuels."
    draw.text((28, 386), lead1, font=f_lead, fill=WHITE)
    draw.text((28, 405), lead2, font=f_lead, fill=WHITE)

    # ---- region grid: 4 columns x 2 rows
    cw, ch, gap = 239, 272, 12
    gx, gy = 16, 436
    cards = REGIONS + [None]  # 8th slot: numbers card
    for i, region in enumerate(cards):
        cx = gx + (i % 4) * (cw + gap)
        cy = gy + (i // 4) * (ch + 16)
        if region is None:
            draw_numbers_card(draw, cx, cy, cw, ch)
        else:
            name, color, stories = region
            draw_region_card(draw, cx, cy, cw, ch, name, color, stories)

    # ---- footer
    f_foot = font(F_REG, 11)
    foot = ("Every story first reported Monday 23 November 2026  ·  Sources: Reuters, AP, AFP, "
            "CNN, The Hindu, Al Jazeera  ·  Full story list in README.md")
    fw = draw.textlength(foot, font=f_foot)
    draw.text(((W - fw) / 2, 1005), foot, font=f_foot, fill=MUTED)

    img.save(OUT, format="PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
