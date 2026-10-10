#!/usr/bin/env python3
"""DUTCH-MORE folds, power check and OCR screen, exactly as PREREG-DUTCHMORE.md (pushed 1b786dc0b before any score).

  python3 dutchmore_score.py --ocr DJVU.txt   parse the OCR screen tokens once into ocr_screen_tokens.tsv (vol 1 djvu, sha1 ac831b5b...)
  python3 dutchmore_score.py                  compute and write dutchmore_score.json (numbers only)
  python3 dutchmore_score.py --check          recompute and exit 1 if dutchmore_score.json differs
Reuses gate_dutchkey.py's model, key permutations (seed 20261010, 1000 draws) and fold statistic unchanged.
"""
import csv, json, os, random, re, sys
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
import gate_dutchkey as G
SCREEN = {'p431': [38393], 'p454': [40264], 'p500': [43941, 43942] + list(range(43962, 43969)),
          'p521': list(range(45764, 45813)), 'p575': [50038, 50039], 'p581': list(range(50551, 50557))}
VANDEPERRE = ['p431', 'p500', 'p521', 'p575', 'p581']

def parse_ocr(path):
    L = open(path, encoding='utf-8', errors='ignore').read().split('\n')
    with open(os.path.join(H, 'ocr_screen_tokens.tsv'), 'w') as f:
        f.write('page\tdjvu_line\tpos\ttoken\n')
        for p, lines in SCREEN.items():
            k = 0
            for ln in lines:
                for t in re.findall(r'(?<![\w,])(\d{1,3})(?=[.,;:\s]|$)', L[ln - 1]):
                    if 1 <= int(t) <= 66:
                        k += 1; f.write(f'{p}\t{ln}\t{k}\t{t}\n')

def screen_runs():
    R = {}
    for r in csv.DictReader(open(os.path.join(H, 'ocr_screen_tokens.tsv')), delimiter='\t'):
        R.setdefault(r['page'], {}).setdefault((r['page'], int(r['djvu_line'])), []).append(int(r['token']))
    return R

def power(Q, codes, letters, P, n, draws=50):
    t108 = G.norm(G.html_text(os.path.join(H, 'edition', 'VAN_DEWITT_01_108.html')))
    rng = random.Random(20261011); inv = {}
    for c, l in zip(codes, letters): inv.setdefault(l, []).append(c)
    hits = 0
    for _ in range(draws):
        o = rng.randrange(0, len(t108) - n); src = [ch for ch in t108[o:o + n] if ch in inv]
        ct = [rng.choice(inv[ch]) for ch in src]
        f, _ = G.fold({('syn', 1): ct}, Q, codes, letters, P)
        hits += f['decode'] > f['ctrl_max']
    return round(hits / draws, 3)

def main():
    if '--ocr' in sys.argv:
        parse_ocr(sys.argv[sys.argv.index('--ocr') + 1]); print('wrote ocr_screen_tokens.tsv'); return
    codes, letters = G.keylist(); P = G.perms(letters); Q = G.model(); K = dict(zip(codes, letters))
    out = {'prereg': '1b786dc0b'}
    for n in ('p301', 'p418'):
        R = G.runs(n); f, nl = G.fold(R, Q, codes, letters, P)
        f.update({'letters': nl, 'supports': f['decode'] > f['ctrl_max'], 'power_50': power(Q, codes, letters, P, nl)})
        f['verdict'] = ('supports' if f['supports'] else 'does not beat control max') if f['power_50'] >= 0.80 else 'non-test at this N'
        out['fold_' + n] = f
    R = {}
    for n in ('p301', 'p418'): R.update(G.runs(n))
    f, nl = G.fold(R, Q, codes, letters, P); f.update({'letters': nl, 'supports': f['decode'] > f['ctrl_max'],
                                                       'power_50': power(Q, codes, letters, P, nl)})
    out['fold_p301_p418_pooled'] = f
    S = screen_runs()
    for p, R in S.items():
        f, nl = G.fold(R, Q, codes, letters, P); f.update({'letters': nl, 'beats_max': f['decode'] > f['ctrl_max']})
        out['ocr_screen_' + p] = f
    pooled = {k: v for p in VANDEPERRE for k, v in S[p].items()}
    f, nl = G.fold(pooled, Q, codes, letters, P); f.update({'letters': nl, 'beats_max': f['decode'] > f['ctrl_max'],
                                                            'power_50': power(Q, codes, letters, P, nl)})
    out['ocr_screen_vandeperre_pooled'] = f
    js = json.dumps(out, indent=1, sort_keys=True) + '\n'; p = os.path.join(H, 'dutchmore_score.json')
    if '--check' in sys.argv:
        ok = os.path.exists(p) and open(p).read() == js; print('OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(p, 'w').write(js); print(js)

if __name__ == '__main__':
    main()
