#!/usr/bin/env python3
"""P10 p.620 line 10: align the 14 groups Birch's print leaves unglossed against the English that
Powell, Letters of Robert Blake (NRS 76, 1937) prints for the same passage (be-api snippet quoted in
AUDIT.md, "P10 L10 groups" s.4). Rule pre-registered in PREREG-R7-THURP10.md (pushed 06f758dc first).

Usage: python3 align_p10_l10_powell.py [--check]
--check exits 1 if the committed reading_P10_L10_powell.tsv differs from a fresh run.
"""
import csv
import io
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from common import load_key

READING = os.path.join(HERE, 'reading_P10_L10.tsv')
BLAKE_KEY = os.path.join(TARGET, 'key_blake_extended.tsv')
OUT = os.path.join(HERE, 'reading_P10_L10_powell.tsv')

POWELL = "to set forth a force of ships to secure the Plate fleet and to that end divers Holland"
BEFORE, AFTER = "set for", "ecure the"   # Birch's own gloss on either side of the gap
SEED, NSEEDS = 20261006, 1000
# Post-hoc hold (stricter than the prereg, found after the scored run): code 67 reads 's' in three printed
# places outside key_blake's one vote -- P9 p.612 L5 "gives" (26 28 39 24 67) and P8 "of Cape Maries"
# (33 25 22 20 34 24 61 50 66 28 54 67) and "...use" (30 30 39 67 54), P8_pairs.tsv lines 11 and 22 -- so
# Powell's "to s" over 68 67 95 is not fixed letter by letter (the cipher may read t-s-? with 'o' omitted).
# Positions 13 and 14 are held at M; the prereg rule alone would give C.
HOLD = {13: '67=s in P8 x2 + P9 x1 (printed)', 14: 'follows the 67 conflict; segmentation not fixed'}


def units(span):
    out = []
    for word in span.split():
        if word == 'ships':
            out.append('fhips')            # code 121's printed form
        else:
            out.extend(word)
    return out


def run():
    rows = list(csv.DictReader(open(READING), delimiter='\t'))
    gap = [r for r in rows if r['status'] == 'unglossed_in_print']
    tail = [r for r in rows if r['status'] == 'glossed_in_print']
    s = POWELL.index(BEFORE) + len(BEFORE)
    e = POWELL.index(AFTER)
    span = POWELL[s:e]
    u = units(span)
    blake = load_key(BLAKE_KEY)
    lines = [f"Powell span between {BEFORE!r} and {AFTER!r}: {span.strip()!r} -> {len(u)} units"]
    out = []
    if len(u) != len(gap):
        lines.append(f"COUNT GATE FAIL: {len(u)} units vs {len(gap)} groups; no regrade")
        return out, lines, False
    lines.append("count gate PASS")
    hc = [i for i, r in enumerate(gap) if blake.get(r['value']) and blake[r['value']]['grade'] in ('H', 'C')]
    def stat(seq):
        return sum(1 for i in hc if seq[i] == blake[gap[i]['value']]['meaning'])
    real = stat(u)
    rng = random.Random(SEED)
    ctl = []
    for _ in range(NSEEDS):
        p = u[:]
        rng.shuffle(p)
        ctl.append(stat(p))
    ctl.sort()
    p95 = ctl[int(0.95 * NSEEDS) - 1]
    mean = sum(ctl) / NSEEDS
    ok = real >= 0.8 * len(hc) and real > p95
    lines.append(f"agreement on key_blake H/C positions: real {real}/{len(hc)}; shuffled-Powell control "
                 f"mean {mean:.2f}, p95 {p95} ({NSEEDS} seeds) -> {'PASS' if ok else 'FAIL'}")
    for i, r in enumerate(gap):
        v, p = r['value'], u[i]
        b = blake.get(v)
        bm, bg = (b['meaning'], b['grade']) if b else ('', 'U')
        if not ok:
            g, note = '', 'gate FAIL, not regraded'
        elif bg == 'U' or bm == p:
            g, note = 'C', ('agrees key_blake' if bm == p else 'key_blake has no value')
        elif bg in ('H', 'C'):
            g, note = 'M', f'CONFLICT key_blake {bm}({bg})'
        else:
            g, note = 'C', f'conflict key_blake {bm}(M, one vote) logged'
        pre = g
        if ok and int(r['pos']) in HOLD:
            g, note = 'M', note + '; post-hoc hold: ' + HOLD[int(r['pos'])]
        mm = r['montagu_meaning']
        mnote = '' if not mm else ('montagu agrees' if mm == p else f'montagu {mm}({r["montagu_grade"]}) differs')
        out.append({'pos': r['pos'], 'value': v, 'powell': p, 'blake': bm, 'blake_grade': bg,
                    'prereg_grade': pre, 'grade': g, 'note': note, 'montagu': mnote})
    # glossed tail: Powell vs Birch's printed letters (listed only)
    tl = list(AFTER.replace(' ', ''))
    for r, p in zip(tail, tl):
        if r['printed_gloss'] != p:
            lines.append(f"tail pos {r['pos']} value {r['value']}: Birch prints {r['printed_gloss']!r}, "
                         f"Powell {p!r}, key_blake {r['blake_meaning']!r}({r['blake_grade']}) -- listed, not regraded")
    return out, lines, ok


def render(out):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=['pos', 'value', 'powell', 'blake', 'blake_grade', 'prereg_grade', 'grade', 'note',
                                        'montagu'], delimiter='\t', lineterminator='\n')
    w.writeheader()
    for r in out:
        w.writerow(r)
    return buf.getvalue()


def main():
    out, lines, ok = run()
    text = render(out)
    for l in lines:
        print(l)
    from collections import Counter
    c = Counter(r['grade'] for r in out)
    print("prereg-rule grades:", dict(Counter(r['prereg_grade'] for r in out)),
          "| final grades of the 14 gap groups:", dict(c))
    for r in out:
        print(f"  {r['pos']:>2} {r['value']:>3} -> {r['powell']:<6} {r['grade'] or '-'}  {r['note']}"
              + (f"; {r['montagu']}" if r['montagu'] else ''))
    if '--check' in sys.argv:
        if not os.path.exists(OUT) or open(OUT).read() != text:
            print("FAIL: reading_P10_L10_powell.tsv is stale", file=sys.stderr)
            sys.exit(1)
        print("check OK")
    else:
        open(OUT, 'w').write(text)


if __name__ == '__main__':
    main()
