#!/usr/bin/env python3
"""PIS-275V (15 Oct 2026, PREREG-PIS-275V.md): the D4-PISA forced-choice word tiles re-cut at NATIVE resolution from the f.275v head
region (openapi.bnf.fr btv1b9060906j f563, region 550,490,2475,1060, max), read by two blind Sonnet passes.
Boxes are D4-PISA's (pisa/pisa.py TILES, in f275vGH_lines_debug.jpg pixels, 1600 px wide) x 2475/1600, then nudged by the per-tile
offsets in NUDGE (set by eye on the native montage BEFORE any read, target and controls alike); tiles are upscaled 1.5x.
  python3 pisa/pisa_native.py --build NATIVE.jpg   cut pisa/tiles_native/{A,B}/*.png and write pisa/prompt_native_{A,B}.md
  python3 pisa/pisa_native.py                      score pisa/reader_native_{A,B}.txt -> pisa/pisa_native_result.json
  python3 pisa/pisa_native.py --check              exit 1 if the committed result is stale
Regenerate NATIVE.jpg: curl -A 'cipher-lab research script (contact via repository)' -o NATIVE.jpg \\
  'https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060906j/f563/550,490,2475,1060/max/0/default.jpg'   (2475x1060)"""
import json, os, random, re, sys
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
from pisa import TILES, L
S = 2475 / 1600
NUDGE = {}   # name: (dx0, dy0, dx1, dy1) in native px; filled before any read
SEEDS = {'A': 4, 'B': 5}
def nbox(name):
    x0, y0, x1, y1 = TILES[name][0]; d = NUDGE.get(name, (0, 0, 0, 0))
    return (round(x0 * S) + d[0], round(y0 * S) + d[1], round(x1 * S) + d[2], round(y1 * S) + d[3])
def plan(p):
    rnd = random.Random(SEEDS[p]); names = list(TILES); rnd.shuffle(names); out = []
    for i, n in enumerate(names, 1):
        _, true, dec = TILES[n]; opts = list(dec) if true is None else [true] + dec; rnd.shuffle(opts)
        out.append({'label': 'T%02d' % i, 'name': n, 'box': nbox(n), 'options': opts, 'true': true})
    return out
def build(src):
    from PIL import Image
    im = Image.open(src).convert('L')
    for p in SEEDS:
        d = os.path.join(H, 'tiles_native', p); os.makedirs(d, exist_ok=True)
        lines = ['Each image below is one tile cut from the same page: a 16th-century French secretary hand, a second-hand marginal',
                 'decipherment written beside a cipher letter. Neighbouring ink may intrude at the edges. For each tile, first write your own',
                 'free transcription of the main word or words (use [?] for what you cannot read), THEN pick exactly one option letter.',
                 'Answer one line per tile, exactly: Txx | free: <your transcription> | choice: <letter> | confidence: high/medium/low', '']
        for t in plan(p):
            x0, y0, x1, y1 = t['box']
            im.crop((x0, y0, x1, y1)).resize((round((x1 - x0) * 1.5), round((y1 - y0) * 1.5)), Image.LANCZOS).save(os.path.join(d, t['label'] + '.png'))
            lines.append('%s: ' % t['label'] + '; '.join('%s) %s' % (L[i], o) for i, o in enumerate(t['options'])))
        open(os.path.join(H, 'prompt_native_%s.md' % p), 'w').write('\n'.join(lines) + '\n')
def norm(s): return (s or '').lower().replace('è', 'e').replace('é', 'e')
def key(s):
    s = norm(s)
    return ((re.search(r'\b(si|tres|bien|fort)\b', s) or [None])[0], (re.search(r'(cache|secret|couuert|couvert)', s) or [None])[0])
def score_pass(p):
    rep = open(os.path.join(H, 'reader_native_%s.txt' % p)).read()
    res = {'tiles': [], 'controls_correct': 0, 'controls_n': 0}
    for t in plan(p):
        m = re.search(r'%s\s*\|\s*free:\s*(.*?)\s*\|\s*choice:\s*([a-h])\b.*?(?:confidence:\s*(\w+))?\s*$' % t['label'], rep, re.M | re.I)
        free, ch, conf = (m.group(1), m.group(2).lower(), m.group(3)) if m else (None, None, None)
        pick = t['options'][L.index(ch)] if ch else None
        row = {'label': t['label'], 'name': t['name'], 'free': free, 'choice': pick, 'confidence': conf}
        if t['true'] is not None:
            row['correct'] = pick == t['true']; res['controls_n'] += 1; res['controls_correct'] += row['correct']
        res['tiles'].append(row)
    res['GC'] = 'PASS' if res['controls_correct'] >= 7 else 'FAIL'
    x = [r for r in res['tiles'] if r['name'] == 'X'][0]
    res['X_choice'] = x['choice']; res['X_free_vs_choice'] = 'agree' if key(x['free']) == key(x['choice']) else 'split'
    return res
def score():
    r = {p: score_pass(p) for p in SEEDS}
    a, b = r['A'], r['B']
    ok = [p for p in SEEDS if r[p]['GC'] == 'PASS' and r[p]['X_free_vs_choice'] == 'agree']
    if len(ok) == 2 and a['X_choice'] == b['X_choice']:
        gt = 'reading (S): ' + a['X_choice']
    elif len(ok) == 2:
        gt = 'split between passes -> M'
    elif len(ok) == 1:
        gt = 'one control-backed pass only (%s: %s) -> M' % (ok[0], r[ok[0]]['X_choice'])
    else:
        gt = 'non-test (no pass with GC PASS and free/choice agreement) -> M'
    r['GT'] = gt
    return r
if __name__ == '__main__':
    if '--build' in sys.argv: build(sys.argv[sys.argv.index('--build') + 1]); sys.exit(0)
    out = json.dumps(score(), indent=1, ensure_ascii=False) + '\n'; p = os.path.join(H, 'pisa_native_result.json')
    if '--check' in sys.argv:
        ok = os.path.exists(p) and open(p).read() == out; print('up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(p, 'w').write(out); print(out)
