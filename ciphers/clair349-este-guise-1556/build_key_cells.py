#!/usr/bin/env python3
"""ZX-KEY349 (25 Sept 2026): one crop per key cell of BnF fr.20974 p.57, the atlas extension S27+,
and key_alpha.tsv / key_nomen.tsv, all from one table of hand-measured boxes.

Frame: every box below is in the ROTATED p.57 frame
    R = Image.open('images/fr20974_p57_native.jpg').crop((3700, 450, 6750, 5500)).rotate(-90, expand=True)
(5050 x 3050 px; the key is written sideways on the leaf, so the crop is turned 90 deg clockwise to read).
Boxes were measured by eye from 1x-3x zooms of R (ZX-KEY349's own read); p.69 (same template, same hand)
was read as a cross-check and is cited in the notes, not cropped.

Usage: python3 build_key_cells.py            # writes crops + TSVs + sheet
       python3 build_key_cells.py --check    # exit 1 if the committed TSVs differ from what this table gives
Needs Pillow. Shape descriptions only in the atlas; values live only in the key TSVs.
"""
import csv, io, os, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "images")
CELLS = os.path.join(IMG, "atlas", "key_cells")
SCALE = 0.4  # key_cells crops are reference thumbnails; the atlas sign crops stay at native scale

ALPHA_Y = (430, 930)
# (letter, cell box x0,x1 on ALPHA_Y, [(code, kind, grade, note)])
ALPHA = [
    ("A", (970, 1200), [("12", "digit", "H", "row 1"), ("14", "digit", "H", "row 2"),
                        ("16", "void", "H", "row 3, struck through in ink on p57 and p69: cancelled, not a live homophone"),
                        ("28", "digit", "H", "row 4")]),
    ("B", (1220, 1400), [("S01", "sign", "H", "row 1, ornate N-like sign; same on p69"), ("3", "digit", "H", "row 2")]),
    ("C", (1380, 1480), [("9", "digit", "H", "single homophone")]),
    ("D", (1465, 1570), [("5", "digit", "M", "an s-form 5, same shape as L's row-2 '5' (the blind cross-read saw only a hook squiggle); one digit for two letters is a conflict in the key as drawn, not resolved; p69 cell blotted")]),
    ("E", (1590, 1730), [("26", "digit", "H", "row 1"), ("16", "digit", "H", "row 2 (not A's struck 16)"), ("62", "digit", "H", "row 3")]),
    ("F", (1700, 1840), [("S02", "sign", "H", "crossed x joined to t ('xt'); S02 re-cropped this session, the ZX-349 crop showed G's header instead")]),
    ("G", (1840, 1965), [("S03", "sign", "H", "e-like loop with long tail")]),
    ("H", (1960, 2080), [("17", "digit", "H", "single homophone, directly under the H header; p69 same")]),
    ("I", (2130, 2245), [("60", "digit", "H", "row 1"), ("64", "digit", "H", "row 2"), ("24", "digit", "H", "row 3")]),
    ("L", (2260, 2400), [("S27", "sign", "H", "row 1, tall doubled long-s with crossbar"), ("5", "digit", "H", "row 2, clear s-form 5 between the S27 descenders; see D")]),
    ("M", (2385, 2480), [("S28", "sign", "H", "row 1, c-hook + m"), ("S29", "sign", "M", "row 2, three-minim 'uu' sign; p69 reads 'uu' too")]),
    ("N", (2470, 2575), [("S30", "sign", "H", "row 1, c-hook + 'ma'/'na'"), ("15", "digit", "H", "row 2")]),
    ("O", (2575, 2685), [("82", "digit", "H", "row 1"), ("44", "digit", "H", "row 2; p69 has a struck number (18?) between 82 and 44")]),
    ("P", (2690, 2805), [("S31", "sign", "H", "circle over a cross")]),
    ("Q", (2860, 3000), [("S32", "sign", "H", "y-like sign with left hook")]),
    ("R", (3020, 3150), [("S33", "sign", "H", "row 1, R-like loop with two legs; the header's flourish runs into it"),
                         ("S34", "sign", "H", "row 2, capital A joined to small o ('Ao'); YX-TR349/ZX-349B read this cell as part of a 'to' cluster")]),
    ("S", (3150, 3265), [("S35", "sign", "M", "row 1, long s + small s"), ("S36", "sign", "M", "row 2, x drawn across the long descender of S35; p69 shows the same x; the blind cross-read saw S35+S36 as ONE tall crossed sign; but the ciphertext (line ~20) has the x standing alone, glossed s, so S36 is its own homophone")]),
    ("T", (3280, 3410), [("S37", "sign", "H", "row 1, crossed t + o ('to')"), ("S38", "sign", "M", "row 2, crossed t + c with a tick ('tc')")]),
    ("V", (3410, 3525), [("102", "digit", "H", "row 1"), ("7", "digit", "H", "row 2; a second small 7 written above it (correction or confirmation); p69 has a struck number here and 7 below"), ("104", "digit", "H", "row 3")]),
    ("X", (3530, 3635), [("S39", "sign", "H", "d-loop joined to long s")]),
    ("Y", (3660, 3785), [("73", "digit", "H", "single homophone")]),
    ("Z", (3790, 3905), [("S40", "sign", "H", "n with a closing loop (reversed-omega)")]),
    ("&", (3920, 4085), [("S04", "sign", "H", "row 1, hash of two by two strokes"), ("S05", "sign", "M", "row 2, a-like squiggle with tail")]),
]

DOUBLES_Y = (1230, 1520)
DOUBLES = [  # (pair as written, x0, x1, code, grade, note)
    ("sc?", 1440, 1620, "22", "M", "digit H; the pair is a long-s/p-like letter + c, read sc or pc; 22 is also the code of 'pour' (Monosillabes)"),
    ("cc", 1650, 1760, "18", "H", ""), ("ff", 1780, 1900, "66", "H", "tall doubled f"),
    ("ll", 1950, 2060, "69", "H", ""), ("mm", 2120, 2250, "76", "H", ""), ("nn", 2250, 2450, "106", "H", ""),
    ("pp", 2500, 2660, "52", "H", ""),
    ("rr", 2710, 2830, "56", "M", "digit H; pair read rr (round r twice); YX-TR349 had qq"),
    ("ss(long)", 2880, 3020, "54", "M", "digit H; tall doubled long s, the second 'ff'-like column of YX-TR349"),
    ("tt", 3040, 3140, "58", "H", "YX-TR349 had st"),
    ("ss(round)", 3180, 3310, "9", "M", "digit read 9 (H on p57 and p69); pair drawn as two round/sigma s; 9 is also C's code"),
]

NULLS = [  # (id, box, code, grade, note)
    ("NULLES:1", (3930, 1270, 4070, 1410), "S06", "H", "row 1"), ("NULLES:2", (4140, 1270, 4240, 1440), "S07", "H", "row 1"),
    ("NULLES:3", (4320, 1280, 4540, 1400), "S08", "H", "row 1"), ("NULLES:4", (4620, 1270, 4720, 1420), "S09", "H", "row 1"),
    ("NULLES:5", (4770, 1260, 4940, 1460), "S10", "H", "row 1"),
    ("NULLES:6", (3925, 1385, 4125, 1490), "S41", "H", "row 2, capital A + minims, 'Auore'-like word shape"),
    ("NULLES:7", (4185, 1385, 4300, 1485), "S42", "H", "row 2, doubled looped S"),
    ("NULLES:8", (4350, 1390, 4430, 1485), "S43", "H", "row 2, 'or'/'cr'-like"),
    ("NULLES:9", (4460, 1375, 4540, 1510), "S44", "H", "row 2, p-like loop crossed on its stem"),
    ("NULLES:10", (4580, 1390, 4645, 1480), "S45", "H", "row 2, small reversed-3 curl"),
]
NULL_HEAD = ("heading p57 'Pour ... suivante sont ca pa[r]de[ssus?] nulle'; p69 'Pour lire suivante: sont la precedente "
             "nulle.' (M on the wording) -- value null either way")

# (section, word, cell box, code, kind, grade, note)
NOMEN = [
    ("MONOSYL1", "dict", (1020, 1800, 1250, 2150), "S46", "sign", "M", "word read Dict (first of two 'dict' in the row; may be another word); code t-with-j tail"),
    ("MONOSYL1", "fist", (1300, 1800, 1500, 2150), "S17", "sign", "M", "word fist/fust; code two crossed t, same shape as the Monsr code S17 on the list"),
    ("MONOSYL1", "fit", (1530, 1800, 1680, 2150), "S37", "sign", "M", "code 'to', same shape as T's row-1 homophone S37"),
    ("MONOSYL1", "n'est", (1680, 1800, 1910, 2150), "S47", "sign", "H", "code h with long loop + o"),
    ("MONOSYL1", "n'aye", (1960, 1800, 2120, 2150), "S32", "sign", "M", "word naye/n'aye (M); code same shape as Q's S32"),
    ("MONOSYL1", "quel", (2200, 1800, 2370, 2150), "S48", "sign", "H", "code c-hook + l"),
    ("MONOSYL1", "quil", (2410, 1800, 2570, 2150), "S49", "sign", "H", "code m with tail"),
    ("MONOSYL1", "fait", (2630, 1800, 2840, 2200), "S50", "sign", "H", "code z with long looped tail"),
    ("MONOSYL1", "pour", (2900, 1800, 3100, 2150), "22", "digit", "H", "same digits as the Doubles 'sc?' code; ciphertext line 3 has |22| glossed 'pour'"),
    ("MONOSYL1", "vous", (3130, 1800, 3390, 2150), "S51", "sign", "H", "word vous (V with flourish); code long s with closed loop"),
    ("MONOSYL1", "ne", (3470, 1800, 3600, 2150), "S52", "sign", "H", "code lattice of three by three strokes (heavier than S04)"),
    ("MONOSYL1", "dict", (3640, 1800, 3840, 2160), "S53", "sign", "H", "code 3/8-like curl with tail"),
    ("MONOSYL1", "il", (3900, 1800, 4030, 2160), "S54", "sign", "H", "word Jl = il; code f with loop"),
    ("MONOSYL1", "est", (4110, 1800, 4340, 2160), "S55", "sign", "H", "code long s + i"),
    ("MONOSYL2", "avec", (1000, 2250, 1215, 2560), "S56", "sign", "M", "word avec (M, first letters blotted); code looped ascender with crossbar and tail; was '8' in YX-TR349"),
    ("MONOSYL2", "tout", (1320, 2250, 1520, 2560), "S57", "sign", "H", "code small c-curl with hook; was '2' in YX-TR349"),
    ("MONOSYL2", "fault", (1580, 2250, 1780, 2560), "S58", "sign", "H", "code long s crossed + 2"),
    ("MONOSYL2", "hault", (1800, 2250, 2000, 2560), "S59", "sign", "H", "code small looped l with crossbar"),
    ("MONOSYL2", "vne?", (2100, 2250, 2240, 2560), "S60", "sign", "M", "word une/vue/ine (M); code y/yogh-like"),
    ("MONOSYL2", "cy?", (2270, 2250, 2400, 2560), "S61", "sign", "M", "word cy/oy (M); code 8-like with open top loop"),
    ("MONOSYL2", "par", (2430, 2250, 2580, 2560), "S62", "sign", "H", "code delta with slash"),
    ("MONOSYL2", "tant", (2610, 2250, 2780, 2560), "S63", "sign", "H", "code q with crossed descender"),
    ("MONOSYL2", "quant", (2850, 2250, 3060, 2560), "S64", "sign", "H", "code 3-shape"),
    ("MONOSYL2", "mon?", (3130, 2250, 3360, 2570), "S65", "sign", "M", "word mon/mem (M); code tall leaf-shaped loop"),
    ("MONOSYL2", "mont", (3380, 2250, 3580, 2560), "S11", "sign", "H", "code circle with bar"),
    ("MONOSYL2", "vne", (3650, 2250, 3830, 2570), "S12", "sign", "H", "word une; code long cross with circle at crossing"),
    ("LASTWORD", "de", (1040, 2580, 1190, 2900), "S66", "sign", "H", "code plain letter h"),
    ("LASTWORD", "florin(s)", (1200, 2580, 1530, 2900), "S67", "sign", "H", "word 'floren' + abbreviation mark; blind cross-read: florin / sa (agrees)"),
    ("LASTWORD", "douze?", (1610, 2580, 1880, 2900), "S68", "sign", "M", "word douze (YX-TR349 and the blind cross-read) or Venize (this worker); code a written cluster 'Soule' (blind: Souk)"),
    ("LASTWORD", "arm.", (1980, 2580, 2180, 2900), "S69", "sign", "M", "word arm./armee (M); code capital A with hooked v -- close to S34 (Ao) and to S76 (A); passes must separate them"),
    ("LASTWORD", "mil", (2270, 2580, 2450, 2900), "S70", "sign", "H", "code script capital M"),
    ("LASTWORD", "escus", (2570, 2580, 2850, 2900), "S71", "sign", "M", "word escu(s) (M); code 8-like loop open at top"),
    ("LASTWORD", "artillerie", (2920, 2580, 3260, 2900), "S13", "sign", "H", "code plus"),
    ("LASTWORD", "ligue", (3370, 2580, 3580, 2900), "99", "digit", "H", ""),
    ("LASTWORD", "beaute", (3660, 2580, 3860, 2900), "S72", "sign", "H", "blind cross-read beaute / T (agrees)"),
    ("LASTWORD", "leurs", (3960, 2580, 4200, 2900), "S14", "sign", "H", ""),
    ("LASTWORD", "munitions?", (4210, 2580, 4670, 2900), "S73", "sign", "M", "word 'mumstois'-like, munitions? (M); code a written cluster 'Sou'"),
    ("LEFTLIST", "Le Roy mre", (200, 30, 700, 120), "S74", "sign", "M", "code a 4-shape with extra hooked stroke, hard to tell from digit 4"),
    ("LEFTLIST", "L'Empereur", (220, 130, 830, 240), "S75", "sign", "H", "code bold capital H"),
    ("LEFTLIST", "Le Roy de Boheme", (210, 240, 850, 340), "S15", "sign", "H", ""),
    ("LEFTLIST", "Le Roy", (190, 360, 850, 440), "?", "none", "H", "no code on the line on p57; p69 has 'Le Roy d[Angleterre]' struck, with a word written in the code column"),
    ("LEFTLIST", "Le Duc de Guyse", (190, 440, 860, 580), "S16", "sign", "H", ""),
    ("LEFTLIST", "Le Duc d'Aumale", (180, 580, 820, 680), "S76", "sign", "H", "code plain capital A; distinct from S34/S69 only by the absent o/v"),
    ("LEFTLIST", "Monsr [ ]", (190, 670, 800, 800), "S17", "sign", "H", "name after Monsr is a long-s flourish, unread; code two crossed t (also the 'fist' code)"),
    ("LEFTLIST", "Nemours", (190, 800, 800, 870), "?", "none", "M", "word Nemours (M); no code"),
    ("LEFTLIST", "aumalle", (190, 890, 800, 980), "?", "none", "H", "no code; struck on p69"),
    ("LEFTLIST", "Espagnols?", (170, 990, 800, 1090), "?", "none", "M", "word 'Espuore'-like (M); no code"),
    ("LEFTLIST", "France", (160, 1090, 800, 1210), "S18", "sign", "H", ""),
    ("LEFTLIST", "Suisses", (190, 1230, 720, 1330), "S19", "sign", "H", "word Suisses (long ss), not Savoie"),
    ("LEFTLIST", "gendarmerie", (190, 1340, 730, 1500), "S20", "sign", "H", "code looped R with tail; compare S33 (R row 1)"),
    ("LEFTLIST", "haulte ligue", (180, 1470, 700, 1590), "S21", "sign", "H", ""),
    ("LEFTLIST", "gens de pied", (140, 1580, 720, 1700), "S22", "sign", "H", ""),
    ("LEFTLIST", "armee de mer", (180, 1700, 720, 1800), "S23", "sign", "H", ""),
    ("LEFTLIST", "cardinal de [L.]", (190, 1820, 770, 1920), "S24", "sign", "H", "p69 'car. de L' -- Lorraine likely (I, not read)"),
    ("LEFTLIST", "Rome", (190, 1950, 730, 2060), "S25", "sign", "H", ""),
    ("LEFTLIST", "Naples", (190, 2080, 720, 2200), "S77", "sign", "H", "code small c"),
    ("LEFTLIST", "Millan", (190, 2200, 720, 2330), "S78", "sign", "H", "code two reversed c ('dd')"),
    ("LEFTLIST", "Florence", (180, 2340, 700, 2470), "S79", "sign", "H", "code y"),
    ("LEFTLIST", "Ferrare", (160, 2450, 800, 2570), "S26", "sign", "H", ""),
    ("LEFTLIST", "Sienne?", (170, 2580, 820, 2700), "S80", "sign", "M", "word Sienne/Bienne (M); code a written cluster 'de sire'"),
]

# atlas sign crops, native scale, from R: code -> (box, shape description)
ATLAS_NEW = {
    "S02": ((1715, 575, 1810, 690), "crossed x joined to a t (re-crop; replaces the ZX-349 S02 crop, which showed a neighbouring header)"),
    "S27": ((2265, 595, 2365, 720), "tall doubled long-s with a crossbar, both stems descending"),
    "S28": ((2385, 610, 2460, 700), "c-hook joined to an m"),
    "S29": ((2385, 705, 2465, 765), "three minims, like 'uu'"),
    "S30": ((2465, 610, 2565, 700), "c-hook joined to 'ma'/'na'"),
    "S31": ((2705, 610, 2785, 740), "small circle standing on a cross"),
    "S32": ((2880, 610, 2995, 730), "y-like stroke with a hook at top left"),
    "S33": ((3020, 590, 3120, 700), "R-like shape: loop on top, two legs"),
    "S34": ((3020, 715, 3125, 800), "capital A joined to a small closed o"),
    "S35": ((3180, 600, 3265, 700), "long s followed by a small s"),
    "S36": ((3160, 720, 3250, 810), "x crossed over a long descender"),
    "S37": ((3310, 600, 3405, 700), "crossed t joined to o"),
    "S38": ((3300, 715, 3385, 805), "crossed t joined to c, with a tick"),
    "S39": ((3535, 620, 3630, 740), "d-like loop joined to a long s"),
    "S40": ((3810, 660, 3900, 740), "n-shape whose right leg closes into a loop (reversed omega)"),
    "S41": ((3925, 1385, 4125, 1490), "capital A followed by minims, a word-like 'Auore' shape"),
    "S42": ((4185, 1385, 4300, 1485), "two looped S side by side"),
    "S43": ((4350, 1390, 4430, 1485), "'or'/'cr'-like pair"),
    "S44": ((4460, 1375, 4540, 1510), "p-like loop with its stem crossed"),
    "S45": ((4580, 1390, 4645, 1480), "small reversed-3 curl"),
    "S46": ((1070, 1990, 1160, 2090), "crossed t with a j-like tail"),
    "S47": ((1685, 1990, 1845, 2130), "h with a long looping tail, followed by o"),
    "S48": ((2235, 2010, 2320, 2075), "c-hook joined to l"),
    "S49": ((2450, 2010, 2540, 2105), "m with a descending tail"),
    "S50": ((2690, 2015, 2835, 2195), "z with a long looped tail"),
    "S51": ((3205, 2010, 3325, 2135), "long s closed into a loop (beta-like)"),
    "S52": ((3485, 2035, 3590, 2130), "lattice, three strokes across three"),
    "S53": ((3665, 2055, 3765, 2160), "3/8-like curl with a tail"),
    "S54": ((3920, 2025, 4015, 2155), "f with a closed loop"),
    "S55": ((4200, 2010, 4330, 2150), "long s followed by i"),
    "S56": ((1000, 2395, 1200, 2560), "looped ascender with a crossbar and a curling tail"),
    "S57": ((1330, 2425, 1415, 2485), "small c-curl with a hook"),
    "S58": ((1595, 2395, 1730, 2545), "crossed long s followed by a 2-shape"),
    "S59": ((1865, 2415, 1945, 2495), "small looped l with a crossbar"),
    "S60": ((2115, 2415, 2215, 2505), "y/yogh-like curl"),
    "S61": ((2305, 2365, 2385, 2475), "8-like with an open top loop"),
    "S62": ((2445, 2415, 2525, 2475), "delta with a slash"),
    "S63": ((2635, 2435, 2715, 2545), "q with a crossed descender"),
    "S64": ((2885, 2425, 2975, 2495), "3-shape"),
    "S65": ((3140, 2395, 3240, 2560), "tall leaf-shaped loop"),
    "S66": ((1075, 2765, 1145, 2855), "plain letter h"),
    "S67": ((1315, 2795, 1415, 2855), "3-shape followed by a (sa-like)"),
    "S68": ((1655, 2765, 1845, 2865), "written cluster 'Soule'"),
    "S69": ((1995, 2775, 2105, 2865), "capital A with a hooked v after it"),
    "S70": ((2280, 2785, 2380, 2855), "script capital M"),
    "S71": ((2580, 2775, 2665, 2865), "8-like loop open at top"),
    "S72": ((3695, 2785, 3795, 2875), "script capital T"),
    "S73": ((4375, 2735, 4625, 2885), "written cluster 'Sou' with a long descender"),
    "S74": ((585, 35, 685, 115), "4-shape with an extra hooked stroke"),
    "S75": ((710, 135, 820, 225), "bold capital H"),
    "S76": ((710, 585, 805, 685), "plain capital A"),
    "S77": ((630, 2105, 705, 2175), "small c"),
    "S78": ((590, 2225, 695, 2285), "two reversed c"),
    "S79": ((570, 2375, 675, 2470), "y"),
    "S80": ((570, 2605, 815, 2695), "written cluster 'de sire'"),
}


def load_R():
    Image.MAX_IMAGE_PIXELS = None
    im = Image.open(os.path.join(IMG, "fr20974_p57_native.jpg"))
    return im.crop((3700, 450, 6750, 5500)).rotate(-90, expand=True).convert("L")


def save_cell(R, box, name):
    c = R.crop(box)
    c = c.resize((max(1, int(c.width * SCALE)), max(1, int(c.height * SCALE))))
    c.save(os.path.join(CELLS, name), quality=70)
    return "atlas/key_cells/" + name


def tables(R=None):
    alpha, nomen = [], []
    for letter, (x0, x1), codes in ALPHA:
        crop = "atlas/key_cells/alpha_%s.jpg" % ("amp" if letter == "&" else letter)
        if R is not None:
            save_cell(R, (x0, ALPHA_Y[0], x1, ALPHA_Y[1]), os.path.basename(crop))
        for code, kind, grade, note in codes:
            alpha.append([letter, code, kind, grade, crop, note])
    for pair, x0, x1, code, grade, note in DOUBLES:
        name = "dbl_%s.jpg" % pair.replace("?", "").replace("(", "_").replace(")", "")
        if R is not None:
            save_cell(R, (x0, DOUBLES_Y[0], x1, DOUBLES_Y[1]), name)
        alpha.append(["DOUBLES:" + pair, code, "digit", grade, "atlas/key_cells/" + name, note])
    for nid, box, code, grade, note in NULLS:
        name = nid.replace(":", "_").lower() + ".jpg"
        if R is not None:
            save_cell(R, box, name)
        alpha.append([nid, code, "sign", grade, "atlas/key_cells/" + name, note + "; " + NULL_HEAD])
    for i, (sec, word, box, code, kind, grade, note) in enumerate(NOMEN):
        name = "%s_%02d.jpg" % (sec.lower(), i)
        if R is not None:
            save_cell(R, box, name)
        nomen.append([sec, word, code, kind, grade, "atlas/key_cells/" + name, note])
    return alpha, nomen


def tsv(rows, header):
    b = io.StringIO()
    w = csv.writer(b, delimiter="\t", lineterminator="\n")
    w.writerow(header)
    w.writerows(rows)
    return b.getvalue()


AH = ["letter", "code", "kind", "grade", "crop", "note"]
NH = ["section", "word_or_phrase", "code", "kind", "grade", "crop", "note"]


def main():
    if "--check" in sys.argv:
        a, n = tables()
        ok = open(os.path.join(HERE, "key_alpha.tsv")).read() == tsv(a, AH) and \
            open(os.path.join(HERE, "key_nomen.tsv")).read() == tsv(n, NH)
        print("key TSVs current" if ok else "key TSVs STALE")
        sys.exit(0 if ok else 1)
    os.makedirs(CELLS, exist_ok=True)
    R = load_R()
    a, n = tables(R)
    open(os.path.join(HERE, "key_alpha.tsv"), "w").write(tsv(a, AH))
    open(os.path.join(HERE, "key_nomen.tsv"), "w").write(tsv(n, NH))
    # atlas: crops for S27+ (and S02 re-crop), then rewrite atlas.tsv and sheet.jpg
    atl = os.path.join(IMG, "atlas", "atlas.tsv")
    rows = [r for r in csv.reader(open(atl), delimiter="\t")]
    head, body = rows[0], rows[1:]
    byc = {r[0]: r for r in body}
    for code, (box, desc) in ATLAS_NEW.items():
        name = "%s_sign.jpg" % code
        R.crop(box).save(os.path.join(IMG, "atlas", name), quality=85)
        byc[code] = [code, "atlas/" + name, desc]
    order = sorted([c for c in byc if c.startswith("S")], key=lambda c: int(c[1:])) + [c for c in byc if not c.startswith("S")]
    open(atl, "w").write(tsv([byc[c] for c in order], head))
    signs = [byc[c] for c in order if c.startswith("S")]
    cw, ch, cols = 160, 190, 8
    sheet = Image.new("L", (cw * cols, ch * ((len(signs) + cols - 1) // cols)), 255)
    d = ImageDraw.Draw(sheet)
    for i, (code, crop, _) in enumerate(signs):
        im = Image.open(os.path.join(IMG, crop)).convert("L")
        im.thumbnail((cw - 10, ch - 30))
        x, y = (i % cols) * cw, (i // cols) * ch
        sheet.paste(im, (x + 5, y + 22))
        d.text((x + 5, y + 4), code, fill=0)
    sheet.save(os.path.join(IMG, "atlas", "sheet.jpg"), quality=80)
    print("cells", len(os.listdir(CELLS)), "alpha rows", len(a), "nomen rows", len(n), "atlas signs", len(signs))


if __name__ == "__main__":
    main()
