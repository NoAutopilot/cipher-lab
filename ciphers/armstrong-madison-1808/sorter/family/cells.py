"""Per-letter cells of each period alphabet chart (SHORTHAND-PAGE, 5 Oct 2026, account 3).

Row grids were read by eye from ruler overlays of the specimen images; rows are evenly spaced between the first and
last row centre, or given as an explicit list of centres (Byrom). Each cell is a horizontal band holding the chart's own letter and its sign. System letters A-E are
BLIND labels for the owner's page; the key is in ../../NOTES.md "Owner which-shorthand family check".
"""
ROOT = 'ciphers/armstrong-madison-1808/'
SPEC = 'images/shorthand/specimens/'
# Coordinates are in the pixels of the archive.org w1800 fetch; the committed copies were shrunk to 1100 px wide
# (folder size rule), so cut_cells scales by actual width / REF_W.
REF_W = {'gurney1752_alphabet_p7.jpg': 2243, 'byrom1796_alphabet_plate_n6.jpg': 2556}
SYSTEMS = {
  # label: (file, [(x0, x1, y_first_centre, y_last_centre, band_h, [row labels])...])
  'A': ('weston1727_alphabet_p1.jpg', [(195, 365, 412, 1700, 50,
        'a b c d e f g h i/j k l m n o p p qu r s s t u/v w x y z &c'.split())]),
  'B': ('byrom1796_alphabet_plate_n6.jpg', [(520, 925, [830, 919, 1003, 1085, 1156, 1266, 1353, 1445, 1555, 1660, 1781, 1870, 1957, 2062, 2141, 2238, 2346, 2438, 2530, 2622, 2719, 2811], None, 92,
        'b d f/v g h j k l m n p q r s/z t w x y ch sh th &c'.split())]),   # explicit row centres (uneven rows)
  'C': ('gurney1752_alphabet_p7.jpg', [(255, 640, 668, 2777, 80,
        'a b c/k d e f g h i i l m n o p q r s s t u v w x y z &c'.split())]),
  'D': ('mavor1792_alphabet_plateI.jpg', [(195, 375, 755, 2205, 58,
        'a b c d e f g/j h i k l m n o p q r s t v u w x y z'.split())]),
  'E': ('macaulay1747_alphabet_p3.jpg', [
        (95, 400, 1281, 3092, 132, 'a b c d e f g h i/j k l m n o'.split()),
        (865, 1160, 1281, 3092, 132, 'o p qu r s t u u v w x y z &c'.split())]),
}


def cut_cells(key):
    """Return [(row label, PIL cell image)] for system `key`, cut from the specimen on disk."""
    from PIL import Image
    f, cols = SYSTEMS[key]
    im = Image.open(ROOT + SPEC + f).convert('L')
    k = im.width / REF_W.get(f, im.width)
    out = []
    for x0, x1, ya, yb, h, labs in cols:
        ys = ya if isinstance(ya, list) else [ya + i * (yb - ya) / (len(labs) - 1) for i in range(len(labs))]
        for lab, y in zip(labs, ys):
            out.append((lab, im.crop((round(x0 * k), round((y - h / 2) * k), round(x1 * k), round((y + h / 2) * k)))))
    return out
