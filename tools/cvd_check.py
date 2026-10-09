#!/usr/bin/env python3
"""cvd_check.py -- colour gate for any page, sheet or figure a person reads (MQS-SHEETS unit 1, 9 Oct 2026).

Functions: simulate(hex, kind, severity) -- Machado, Oliveira and Fernandes 2009 matrices (protan, deutan, tritan,
severity 1.0 table; intermediate severities interpolate linearly toward identity) applied to linear RGB;
de2000(lab1, lab2) -- CIEDE2000 (Sharma, Wu and Dalal 2005); contrast(a, b) -- WCAG 2.1 relative-luminance ratio;
check(marks, bg, tints=(), text=()) -- every failing pair and each vision's margin (worst pair minus the gate).

Gate: every pair of mark colours differs by CIEDE2000 >= GATE (20) in normal vision and in each simulation; every
mark reaches 3:1 against the background; every text colour 4.5:1; text drawn on a tint reaches 4.5:1 on that tint.
THE 20 IS A DECLARED DESIGN THRESHOLD, NOT A SOURCED ONE: no published CVD-palette minimum was cited, and the same
9 Oct 2026 pass chose both it and the palettes (so sorter_light's worst pair, 20.7, passes by 0.7). Verdicts:
PASS (exit 0) at >= 20; WARN (exit 2, "judgement call: under the declared gate by < 2") for 18 <= worst < 20;
FAIL (exit 1) below 18 or on any contrast failure.

Scope (Usage 8a). Meant to catch: a mark pair that collapses under a simulated vision (legacy sorter green vs red),
a mark colour under 3:1 on its background (#E69F00 on white), light text on a light tint (#ece6dc on yellow).
Must NOT flag: sheets_light, sorter_light and dark with their declared tint/text pairs; a palette whose worst pair is
only just over the gate (WARN is a judgement call, not a failure). Tests: tools/tests/test_cvd_check.py (offline).

Audit (--audit FILE..., MQS-CVD-AUDIT, 9 Oct 2026). Extracts colour literals from a tool's source or template: hex
#rgb/#rrggbb anywhere; 3-int tuples on lines that call cv2, in a file that imports cv2 and not PIL ImageDraw, or after --bgr, read as BGR, other tuples as RGB. Keeps the
chromatic ones (CIE LCh chroma >= 15; neutrals keep their lightness under CVD and are skipped) and flags each pair that
is distinct in normal vision (dE2000 >= GATE) but under COLLAPSE (10) under protan, deutan or tritan (CVD-COLLAPSE), and
each red/orange vs green hue pair (RED-GREEN, the project rule). COLLAPSE = 10 is a declared tuning on Okabe-Ito (its
21 pairs bottom out at 11.1 simulated, and 10 of them fall under the 18 WARN floor, so 18 cannot mean "collapse") plus
ten problem pairs; held-out control in tools/tests/PREREG-MQS-CVD-AUDIT.md. A lead list for a person, never a verdict:
it cannot see which colours share a page (a file with light and dark themes pairs across them), which carry meaning,
or what they sit on (contrast stays with --marks/--bg). Meant to catch: glyph_atlas's cv2 red vs green overlay; tab10
red vs green. Must NOT flag: Okabe-Ito (0 of 21 pairs); a neutral pair (#ffffff vs #24211c). Exit 0 no flags, 2 flags.

CLI: python3 tools/cvd_check.py --audit FILE [FILE ...] [--bgr] | --palette NAME | --marks '#a,#b' --bg '#fff' [--tints '#t'] [--text '#x'] [--tint-text T:X,...]
"""
import argparse, itertools, math, re, sys

GATE = 20.0
WARN_FLOOR = 18.0
MARK_CONTRAST = 3.0
TEXT_CONTRAST = 4.5

MATRICES = {  # Machado et al. 2009, severity 1.0
    'protan': ((0.152286, 1.052583, -0.204868), (0.114503, 0.786281, 0.099216), (-0.003882, -0.048116, 1.051998)),
    'deutan': ((0.367322, 0.860646, -0.227968), (0.280085, 0.672501, 0.047413), (-0.011820, 0.042940, 0.968881)),
    'tritan': ((1.255528, -0.076749, -0.178779), (-0.078411, 0.930809, 0.147602), (0.004733, 0.691367, 0.303900)),
}
VISIONS = ('normal', 'protan', 'deutan', 'tritan')

# Research note MARY-STUART-TALK-2026-10-09.md section f. 'pairs' are (tint, text-on-tint).
PALETTES = {
    'sorter_light': dict(marks=['#24211c', '#0072B2', '#B35900', '#767676'], bg='#f3f1ec',
                         text=['#24211c'], tints=['#F0E442', '#56B4E9'],
                         pairs=[('#F0E442', '#24211c'), ('#56B4E9', '#24211c')]),
    'sheets_light': dict(marks=['#000000', '#0072B2', '#B35900', '#595959'], bg='#ffffff',
                         text=['#000000'], tints=['#F0E442', '#56B4E9'],
                         pairs=[('#F0E442', '#000000'), ('#56B4E9', '#000000')]),
    'dark': dict(marks=['#ece6dc', '#56B4E9', '#E69F00'], bg='#1b1916',
                 text=['#ece6dc'], tints=['#F0E442', '#56B4E9'],
                 pairs=[('#F0E442', '#1b1916'), ('#56B4E9', '#1b1916')]),
}


def parse_hex(h):
    h = h.strip().lstrip('#')
    if len(h) == 3:
        h = ''.join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4))


def to_hex(rgb):
    return '#' + ''.join('%02x' % max(0, min(255, round(c * 255))) for c in rgb)


def lin(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def delin(c):
    c = max(0.0, min(1.0, c))
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def simulate(hexcol, kind, severity=1.0):
    """Return the hex colour as seen with the given deficiency ('normal' returns it unchanged)."""
    rgb = parse_hex(hexcol)
    if kind == 'normal':
        return to_hex(rgb)
    m = MATRICES[kind]
    ident = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    m = [[(1 - severity) * ident[i][j] + severity * m[i][j] for j in range(3)] for i in range(3)]
    l = [lin(c) for c in rgb]
    out = [sum(m[i][j] * l[j] for j in range(3)) for i in range(3)]
    return to_hex([delin(c) for c in out])


def rgb_to_lab(hexcol):
    r, g, b = (lin(c) for c in parse_hex(hexcol))
    x = 0.4124564 * r + 0.3575761 * g + 0.1804375 * b
    y = 0.2126729 * r + 0.7151522 * g + 0.0721750 * b
    z = 0.0193339 * r + 0.1191920 * g + 0.9503041 * b
    xn, yn, zn = 0.95047, 1.0, 1.08883

    def f(t):
        return t ** (1 / 3) if t > 216 / 24389 else (24389 / 27 * t + 16) / 116
    fx, fy, fz = f(x / xn), f(y / yn), f(z / zn)
    return (116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz))


def de2000(lab1, lab2, kL=1.0, kC=1.0, kH=1.0):
    L1, a1, b1 = lab1
    L2, a2, b2 = lab2
    C1, C2 = math.hypot(a1, b1), math.hypot(a2, b2)
    Cb = (C1 + C2) / 2
    G = 0.5 * (1 - math.sqrt(Cb ** 7 / (Cb ** 7 + 25 ** 7)))
    a1p, a2p = (1 + G) * a1, (1 + G) * a2
    C1p, C2p = math.hypot(a1p, b1), math.hypot(a2p, b2)
    h1p = math.degrees(math.atan2(b1, a1p)) % 360 if (b1 or a1p) else 0.0
    h2p = math.degrees(math.atan2(b2, a2p)) % 360 if (b2 or a2p) else 0.0
    dLp, dCp = L2 - L1, C2p - C1p
    if C1p * C2p == 0:
        dhp = 0.0
    else:
        d = h2p - h1p
        dhp = d - 360 if d > 180 else d + 360 if d < -180 else d
    dHp = 2 * math.sqrt(C1p * C2p) * math.sin(math.radians(dhp / 2))
    Lbp, Cbp = (L1 + L2) / 2, (C1p + C2p) / 2
    if C1p * C2p == 0:
        hbp = h1p + h2p
    elif abs(h1p - h2p) <= 180:
        hbp = (h1p + h2p) / 2
    else:
        hbp = (h1p + h2p + 360) / 2 if h1p + h2p < 360 else (h1p + h2p - 360) / 2
    T = (1 - 0.17 * math.cos(math.radians(hbp - 30)) + 0.24 * math.cos(math.radians(2 * hbp))
         + 0.32 * math.cos(math.radians(3 * hbp + 6)) - 0.20 * math.cos(math.radians(4 * hbp - 63)))
    dth = 30 * math.exp(-((hbp - 275) / 25) ** 2)
    Rc = 2 * math.sqrt(Cbp ** 7 / (Cbp ** 7 + 25 ** 7))
    Sl = 1 + 0.015 * (Lbp - 50) ** 2 / math.sqrt(20 + (Lbp - 50) ** 2)
    Sc, Sh = 1 + 0.045 * Cbp, 1 + 0.015 * Cbp * T
    Rt = -math.sin(math.radians(2 * dth)) * Rc
    return math.sqrt((dLp / (kL * Sl)) ** 2 + (dCp / (kC * Sc)) ** 2 + (dHp / (kH * Sh)) ** 2
                     + Rt * (dCp / (kC * Sc)) * (dHp / (kH * Sh)))


def luminance(hexcol):
    r, g, b = (lin(c) for c in parse_hex(hexcol))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def check(marks, bg, tints=(), text=(), pairs=(), gate=GATE):
    """Return dict: failures (list of strings), worst {vision: (de, a, b)}, margin {vision: worst-gate},
    verdict PASS|WARN|FAIL, exit code. `pairs` are (tint, text-on-tint) pairs; `tints` alone are fills with no
    text checked; `text` colours are checked against bg."""
    fails = []
    worst, margin = {}, {}
    for v in VISIONS:
        sim = [simulate(m, v) if v != 'normal' else m.lower() for m in marks]
        w = (None, None, None)
        for (i, a), (j, b) in itertools.combinations(list(enumerate(sim)), 2):
            d = de2000(rgb_to_lab(a), rgb_to_lab(b))
            if w[0] is None or d < w[0]:
                w = (d, marks[i], marks[j])
        worst[v] = w
        margin[v] = (w[0] - gate) if w[0] is not None else None
    wmin = min((w[0] for w in worst.values() if w[0] is not None), default=None)
    hard = False
    if wmin is not None and wmin < gate:
        for v in VISIONS:
            if worst[v][0] is not None and worst[v][0] < gate:
                fails.append('pair %s vs %s: dE2000 %.1f < %g under %s' % (worst[v][1], worst[v][2], worst[v][0], gate, v))
        if wmin < WARN_FLOOR:
            hard = True
    for m in marks:
        c = contrast(m, bg)
        if c < MARK_CONTRAST:
            fails.append('mark %s on %s: contrast %.2f < %g' % (m, bg, c, MARK_CONTRAST)); hard = True
    for t in text:
        c = contrast(t, bg)
        if c < TEXT_CONTRAST:
            fails.append('text %s on %s: contrast %.2f < %g' % (t, bg, c, TEXT_CONTRAST)); hard = True
    for tint, tx in pairs:
        c = contrast(tx, tint)
        if c < TEXT_CONTRAST:
            fails.append('text %s on tint %s: contrast %.2f < %g' % (tx, tint, c, TEXT_CONTRAST)); hard = True
    if hard:
        verdict, code = 'FAIL', 1
    elif fails:
        verdict, code = 'WARN', 2
        fails.append('judgement call: under the declared gate by < %g' % (gate - WARN_FLOOR))
    else:
        verdict, code = 'PASS', 0
    return dict(failures=fails, worst=worst, margin=margin, verdict=verdict, code=code, min_de=wmin)


def check_palette(name):
    p = PALETTES[name]
    return check(p['marks'], p['bg'], p.get('tints', ()), p.get('text', ()), p.get('pairs', ()))


def report(res, label=''):
    lines = []
    for v in VISIONS:
        d, a, b = res['worst'][v]
        if d is None:
            lines.append('%-7s (fewer than two marks)' % v)
        else:
            lines.append('%-7s worst pair %s vs %s  dE2000 %.1f  margin %+.1f' % (v, a, b, d, res['margin'][v]))
    for f in res['failures']:
        lines.append('  ! ' + f)
    lines.append('%s%s' % (label + ': ' if label else '', res['verdict']))
    return '\n'.join(lines)


COLLAPSE = 10.0
CHROMA_MIN = 15.0
HEX_RE = re.compile(r'(?<![0-9A-Za-z&])#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})(?![0-9A-Za-z])')
TUP_RE = re.compile(r'\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)')


def lch(hexcol):
    L, a, b = rgb_to_lab(hexcol)
    return L, math.hypot(a, b), math.degrees(math.atan2(b, a)) % 360


def extract(text, bgr=False):
    """Return {hex_lower: [line numbers]} for every colour literal in text."""
    out = {}
    if 'import cv2' in text and 'ImageDraw' not in text:
        bgr = True  # a cv2-only file: every colour tuple is BGR
    for n, line in enumerate(text.splitlines(), 1):
        for m in HEX_RE.finditer(line):
            out.setdefault(to_hex(parse_hex(m.group(1))), []).append(n)
        if 'cv2.' in line or 'col' in line.lower() or 'fill' in line or 'outline' in line:
            for m in TUP_RE.finditer(line):
                v = [int(x) for x in m.groups()]
                if max(v) > 255:
                    continue
                if bgr or 'cv2.' in line:
                    v = v[::-1]
                out.setdefault('#%02x%02x%02x' % tuple(v), []).append(n)
    return out


def _hue_class(h):
    if h >= 345 or h < 60:
        return 'red'
    if 100 <= h < 175:
        return 'green'
    return None


def audit_colours(cols):
    """cols: iterable of hex. Return list of (a, b, kind, detail) flags among chromatic colours."""
    chrom = sorted({c.lower() for c in cols if lch(c)[1] >= CHROMA_MIN})
    flags = []
    for a, b in itertools.combinations(chrom, 2):
        dn = de2000(rgb_to_lab(a), rgb_to_lab(b))
        if dn >= GATE:
            sims = {v: de2000(rgb_to_lab(simulate(a, v)), rgb_to_lab(simulate(b, v))) for v in VISIONS[1:]}
            v = min(sims, key=sims.get)
            if sims[v] < COLLAPSE:
                flags.append((a, b, 'CVD-COLLAPSE', 'normal %.1f, %s %.1f' % (dn, v, sims[v])))
        ha, hb = _hue_class(lch(a)[2]), _hue_class(lch(b)[2])
        if {ha, hb} == {'red', 'green'}:
            flags.append((a, b, 'RED-GREEN', 'hues %.0f / %.0f' % (lch(a)[2], lch(b)[2])))
    return chrom, flags


def audit_file(path, bgr=False):
    with open(path, encoding='utf-8', errors='replace') as f:
        found = extract(f.read(), bgr)
    chrom, flags = audit_colours(found)
    lines = ['%s: %d colour literals, %d chromatic, %d flags' % (path, len(found), len(chrom), len(flags))]
    for a, b, k, d in flags:
        lines.append('  %s %s (line %s) vs %s (line %s): %s' % (k, a, found[a][0], b, found[b][0], d))
    return flags, '\n'.join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--palette', choices=sorted(PALETTES))
    ap.add_argument('--marks'); ap.add_argument('--bg'); ap.add_argument('--tints', default='')
    ap.add_argument('--text', default='')
    ap.add_argument('--tint-text', default='', help='TINT:TEXT,TINT:TEXT pairs checked at 4.5:1')
    ap.add_argument('--audit', nargs='+', metavar='FILE', help='lead list of CVD-collapsing / red-green colour pairs')
    ap.add_argument('--bgr', action='store_true', help='read every 3-int tuple as BGR (cv2)')
    a = ap.parse_args(argv)
    if a.audit:
        n = 0
        for p in a.audit:
            fl, txt = audit_file(p, a.bgr)
            n += len(fl)
            print(txt)
        return 2 if n else 0
    if a.palette:
        res = check_palette(a.palette)
    else:
        if not (a.marks and a.bg):
            ap.error('give --palette or --marks and --bg')
        sp = lambda s: [x.strip() for x in s.split(',') if x.strip()]
        pairs = [tuple(x.split(':')) for x in sp(a.tint_text)]
        res = check(sp(a.marks), a.bg, sp(a.tints), sp(a.text), pairs)
    print(report(res, a.palette or ''))
    return res['code']


if __name__ == '__main__':
    sys.exit(main())
