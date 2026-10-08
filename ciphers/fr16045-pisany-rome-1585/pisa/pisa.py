#!/usr/bin/env python3
"""D4-PISA (8 Oct 2026, PREREG-D4-PISA.md): forced-choice word-tile read of the f.275v head gloss.
  python3 pisa/pisa.py --build CLEAN.png   cut pisa/tiles/*.png from the de-lined debug image (pisa/deline.py), write pisa/prompt.md
  python3 pisa/pisa.py                     score pisa/reader.txt -> pisa/pisa_result.json
  python3 pisa/pisa.py --check             exit 1 if the committed result is stale"""
import json, random, re, sys, os
H = os.path.dirname(os.path.abspath(__file__))
# name: (box in f275vGH_lines_debug.jpg pixels, true option, decoys); 'X' is the target (no true option)
TILES = {
 'X':           ((1100, 188, 1545, 268), None, ['tenir si cachee', 'tenir tres secrete', 'tenir tres secret', 'tenir si secrete',
                                                'tenir bien cachee', 'tenir fort secrete', 'tenir tres cachee', 'tenir si couuerte']),
 'communiquer': ((258, 50, 492, 112), 'communiquer', ['commencer', 'continuer', 'dominique', 'communier', 'commander', 'comminuer', 'commenique']),
 'entendre':    ((1208, 55, 1392, 116), 'entendre', ['attendre', 'estendre', 'entendu', 'pretendre', 'descendre', 'entrer', 'reprendre']),
 'lettres':     ((300, 108, 525, 165), 'par lettres', ['par Crisy', 'pour lettres', 'par lestres', 'par Cristy', 'par lettre', 'pour Crisy', 'par liures']),
 'personne':    ((1205, 128, 1465, 214), 'personne', ['prisonnier', 'presence', 'puissance', 'prouesse', 'pressance', 'prouence', 'pareillement']),
 'neantmoings': ((160, 203, 490, 286), 'neantmoings', ['nonobstant', 'maintenant', 'nommement', 'moyennant', 'nouuellement', 'mesmement', 'nullement']),
 'perpetuel':   ((12, 556, 210, 630), 'perpetuel', ['perpetrer', 'pourpoint', 'portatif', 'pupitre', 'propretel', 'pourtant', 'preterit']),
 'dilligence':  ((30, 346, 330, 422), 'dilligence', ['deliurance', 'dilection', 'delinquance', 'difference', 'dilatation', 'desolation', 'delicatesse']),
 'faisant':     ((1025, 42, 1210, 135), 'faisant', ['fuyant', 'faisoit', 'fussent', 'sachant', 'fermant', 'voyant', 'lisant']),
}
L = 'abcdefgh'
def plan():
    rnd = random.Random(4)
    names = list(TILES); rnd.shuffle(names)
    out = []
    for i, n in enumerate(names, 1):
        box, true, dec = TILES[n]
        opts = list(dec) if true is None else [true] + dec
        rnd.shuffle(opts)
        out.append({'label': 'T%02d' % i, 'name': n, 'box': box, 'options': opts, 'true': true})
    return out
def build(clean):
    from PIL import Image
    im = Image.open(clean)
    os.makedirs(os.path.join(H, 'tiles'), exist_ok=True)
    lines = ['Each image below is one tile cut from the same page: a 16th-century French secretary hand, a second-hand marginal',
             'decipherment written beside a cipher letter. Neighbouring ink may intrude at the edges. For each tile, first write your own',
             'free transcription of the main word or words (use [?] for what you cannot read), THEN pick exactly one option letter.',
             'Answer one line per tile, exactly: Txx | free: <your transcription> | choice: <letter> | confidence: high/medium/low', '']
    for t in plan():
        x0, y0, x1, y1 = t['box']
        Image.open(clean).crop((x0, y0, x1, y1)).resize(((x1 - x0) * 2, (y1 - y0) * 2), Image.LANCZOS).save(os.path.join(H, 'tiles', t['label'] + '.png'))
        lines.append('%s (pisa/tiles/%s.png): ' % (t['label'], t['label']) + '; '.join('%s) %s' % (L[i], o) for i, o in enumerate(t['options'])))
    open(os.path.join(H, 'prompt.md'), 'w').write('\n'.join(lines) + '\n')
def score():
    rep = open(os.path.join(H, 'reader.txt')).read()
    res = {'tiles': [], 'controls_correct': 0, 'controls_n': 0}
    for t in plan():
        m = re.search(r'%s\s*\|\s*free:\s*(.*?)\s*\|\s*choice:\s*([a-h])\b.*?(?:confidence:\s*(\w+))?\s*$' % t['label'], rep, re.M | re.I)
        free, ch, conf = (m.group(1), m.group(2).lower(), m.group(3)) if m else (None, None, None)
        pick = t['options'][L.index(ch)] if ch else None
        row = {'label': t['label'], 'name': t['name'], 'free': free, 'choice': pick, 'confidence': conf}
        if t['true'] is not None:
            row['correct'] = pick == t['true']; res['controls_n'] += 1; res['controls_correct'] += row['correct']
        res['tiles'].append(row)
    res['GC'] = 'PASS' if res['controls_correct'] >= 7 else 'FAIL'
    x = [r for r in res['tiles'] if r['name'] == 'X'][0]
    key = lambda s: (re.search(r'\b(si|tres|bien|fort)\b', s or '') or [None])[0], (re.search(r'(cache|secret|couuert|couvert)', s or '') or [None])[0]
    res['X_choice'] = x['choice']
    res['X_free_vs_choice'] = 'agree' if key((x['free'] or '').lower().replace('è', 'e').replace('é', 'e')) == key(x['choice']) else 'split'
    res['GT'] = ('reading: ' + x['choice'] if res['X_free_vs_choice'] == 'agree' else 'split -> M') if res['GC'] == 'PASS' else 'non-test (GC FAIL)'
    return res
if __name__ == '__main__':
    if '--build' in sys.argv: build(sys.argv[sys.argv.index('--build') + 1]); sys.exit(0)
    r = json.dumps(score(), indent=1, ensure_ascii=False) + '\n'
    p = os.path.join(H, 'pisa_result.json')
    if '--check' in sys.argv:
        ok = os.path.exists(p) and open(p).read() == r
        print('up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(p, 'w').write(r); print(r)
