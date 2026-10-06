#!/usr/bin/env python3
"""R9-MANTPOOL (6 Oct 2026): pooled multi-code-run aligner gate per PREREG-R9-MANTPOOL.md.
Every glossed multi-code run of the 7 transcribed glossed leaves (0502, 0501, 0527, 0528, 0574/0575, 0529, 0530) is one pair;
tools/interlinear_align.py's hard-EM DP aligns them all together with --fix ../key.tsv (every key.tsv code held at its value).
Statistic: number of FREE codes (absent from key.tsv) whose aligned chunk is identical (folded, non-empty) in >= 2 distinct runs.
Controls: gloss strings shuffled among runs of the same code-count bin (DRAWS draws), and a known-answer run with 5 C codes unfixed.
Usage: pooled_multi.py [--draws N] [--time-one]   (writes runs_r9.tsv, codes_r9.tsv, shuffle_r9.tsv, known_answer_r9.tsv here)"""
import csv, os, re, sys, random, importlib.util, time
from collections import Counter, defaultdict
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(HERE, '..'); ROOT = os.path.join(T, '..', '..')
spec = importlib.util.spec_from_file_location('ia', os.path.join(ROOT, 'tools', 'interlinear_align.py'))
ia = importlib.util.module_from_spec(spec); spec.loader.exec_module(ia)
LEAVES = [('0502', 'f0500_0502/pairs_0502.tsv'), ('0501', 'f0501/pairs.tsv'), ('0527', 'f422v_0527/pairs.tsv'),
          ('0528', 'f423_0528/pairs.tsv'), ('0574', 'f463_0574/pairs.tsv'), ('0529', 'f424v_0529/pairs.tsv'),
          ('0530', 'f425v_0530/pairs.tsv')]
BINS = [(2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 8), (9, 9), (10, 11), (12, 12), (13, 17), (18, 999)]
SEED, DRAWS, NHIDE = 9501, 1000, 5
NORM = {r['token']: r['expansion'] for r in csv.DictReader(open(os.path.join(T, 'f0500_0502/gloss_norm.tsv')), delimiter='\t')}
norm = lambda g: ' '.join(NORM.get(t, t) for t in re.sub(r"[.,;:'\"]", ' ', g.lower()).split())
rd = lambda p: [r for r in csv.DictReader((l for l in open(os.path.join(T, p)) if not l.startswith('#')), delimiter='\t')]
KEY = {r['code']: r for r in rd('key.tsv')}
ALLFIX = ia.load_fixed(os.path.join(T, 'key.tsv'))

def load():
    runs, seen = [], set()
    for leaf, p in LEAVES:
        for r in rd(p):
            c = r['cipher_raw'].split()
            if len(c) < 2 or tuple(c) in seen:
                continue
            seen.add(tuple(c))
            runs.append({'leaf': leaf, 'line': r['cipher_line'], 'codes': ' '.join(c), 'gloss': norm(r['plain_raw'])})
    return runs

def align(runs, glosses, fixed):
    ia.FIXED.clear(); ia.FIXED.update(fixed)
    pairs = [{'plain_line': str(i), 'plain_raw': g, 'cipher_line': str(i), 'cipher_raw': r['codes']} for i, (r, g) in enumerate(zip(runs, glosses))]
    prepared, results, counts, shown = ia.run_align(pairs, floor=1)
    per = defaultdict(lambda: defaultdict(set))   # code -> chunk -> set(run idx)
    for i, ((p, raw, toks, letters, *_), chunks) in enumerate(zip(prepared, results)):
        for (kind, val), c in zip(toks, chunks):
            if kind == 'num':
                per[val][ia.fold(letters[c[0]:c[1]]) if c else ''].add(i)
    return per

def score(per, free):
    rec, agree = [], {}
    for v, d in per.items():
        if v not in free: continue
        runs = set().union(*d.values())
        if len(runs) < 2: continue
        rec.append(v)
        best = max(((len(s), ch) for ch, s in d.items() if ch), default=(0, ''))
        if best[0] >= 2: agree[v] = best[1]
    return rec, agree

def free_of(per, fixed):
    return {v for v in per if v not in fixed}

def shuffle_glosses(runs, rng):
    g = [r['gloss'] for r in runs]
    for lo, hi in BINS:
        idx = [i for i, r in enumerate(runs) if lo <= len(r['codes'].split()) <= hi]
        vals = [g[i] for i in idx]; rng.shuffle(vals)
        for i, v in zip(idx, vals): g[i] = v
    return g

def one_draw(d):
    runs = load(); rng = random.Random(SEED + d)
    per = align(runs, shuffle_glosses(runs, rng), ALLFIX)
    return len(score(per, free_of(per, ALLFIX))[1])

def alts(code):
    return {ia.fold(re.sub(r'[^a-z]', '', ia.fold_accents(a).lower())) for a in KEY[code]['value'].split('|')}

def main():
    a = sys.argv[1:]; draws = int(a[a.index('--draws') + 1]) if '--draws' in a else DRAWS
    runs = load()
    if '--time-one' in a:
        t = time.time(); print('one shuffled draw S =', one_draw(0), 'in %.1f s' % (time.time() - t)); return
    print('runs', len(runs), 'bins', [sum(lo <= len(r['codes'].split()) <= hi for r in runs) for lo, hi in BINS])
    per = align(runs, [r['gloss'] for r in runs], ALLFIX)
    free = free_of(per, ALLFIX); rec, agree = score(per, free)
    with Pool(4) as pool:
        sh = sorted(pool.map(one_draw, range(draws)))
    p95 = sh[int(0.95 * draws) - 1]; mean = sum(sh) / draws
    # known-answer: the NHIDE grade-C codes with a non-null value in the most distinct runs (ties: lower code)
    cand = []
    for v, d in per.items():
        k = KEY.get(str(v))
        if not k or k['grade'] != 'C' or not k['value'].strip(): continue
        cand.append((-len(set().union(*d.values())), v))
    hide = [v for _, v in sorted(cand)[:NHIDE]]
    fx = {k: c for k, c in ALLFIX.items() if k not in hide}
    perk = align(runs, [r['gloss'] for r in runs], fx)
    _, agk = score(perk, set(hide))
    ka = []
    for v in hide:
        d = perk[v]; best = max(((len(s), ch) for ch, s in d.items() if ch), default=(0, ''))
        ok = v in agk and agk[v] in alts(str(v))
        ka.append([v, KEY[str(v)]['value'], len(set().union(*d.values())), best[1], best[0], 'yes' if ok else 'no'])
    nka = sum(r[-1] == 'yes' for r in ka)
    S = len(agree); passed = S > p95 and nka >= 3
    print(f'REAL: free codes recurring in >=2 runs {len(rec)}, agreeing S = {S}')
    print(f'SHUFFLE ({draws} draws, bins): mean {mean:.2f}, p95 {p95}, max {sh[-1]}')
    print(f'KNOWN-ANSWER: {nka}/{NHIDE} recovered: ' + '; '.join(f'{r[0]}={r[1]!r} -> {r[3]!r} x{r[4]} ({r[5]})' for r in ka))
    print('GATE (S > p95 AND known-answer >= 3/5):', 'PASS' if passed else 'FAIL')
    with open(os.path.join(HERE, 'runs_r9.tsv'), 'w') as f:
        w = csv.DictWriter(f, ['leaf', 'line', 'codes', 'gloss'], delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(runs)
    with open(os.path.join(HERE, 'codes_r9.tsv'), 'w') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n'); w.writerow(['code', 'n_runs', 'chunks(runs)', 'agree_chunk', 'licence'])
        for v in sorted(rec):
            d = per[v]; ch = ' | '.join(f'{c or "-"}({len(s)})' for c, s in sorted(d.items(), key=lambda kv: -len(kv[1])))
            w.writerow([v, len(set().union(*d.values())), ch, agree.get(v, ''), ('M' if passed else 'gate-failed') if v in agree else 'disagree'])
    with open(os.path.join(HERE, 'shuffle_r9.tsv'), 'w') as f:
        f.write('draw_sorted\tS\n' + ''.join(f'{i}\t{x}\n' for i, x in enumerate(sh)))
    with open(os.path.join(HERE, 'known_answer_r9.tsv'), 'w') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n'); w.writerow(['code', 'key_value', 'n_runs', 'top_chunk', 'top_runs', 'recovered']); w.writerows(ka)

if __name__ == '__main__':
    main()
