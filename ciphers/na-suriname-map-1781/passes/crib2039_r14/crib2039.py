#!/usr/bin/env python3
"""R14-SUR2039 (6 Oct 2026): place inv. 373 gloss words as cribs on 4.VEL 2039's legend under the rule in PREREG.md
(pushed first, 91f6069ab), with a within-entry shuffle control (a) and a matched-length gloss-word control (b).
Usage: python3 crib2039.py [--seeds 1000]  -> prints the report (score.out). Exit 0 always."""
import csv, os, re, sys, random, math, statistics
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(os.path.dirname(H))
SEEDS = int(sys.argv[sys.argv.index('--seeds')+1]) if '--seeds' in sys.argv else 1000
CRIBS = "smeedery affuyten affuyt beslag geschut fortres fortificatie werken linie verstopping boom touwen wal".split()
def canon(w):
    w = w.lower().replace('ij', 'y').replace('ÿ', 'y').replace('j', 'i').replace('u', 'v')
    return re.sub(r'[^a-z]', '', w)
CRIBS = [canon(c) for c in CRIBS]
ents = {}
for r in csv.DictReader((l for l in open(os.path.join(T, 'reading_2039_legend_nieuw_tokens.tsv')) if not l.startswith('#')), delimiter='\t'):
    lab = r['line'].replace('2039_leg_', '')
    if lab == 'head': continue
    v = r['value']
    if len(v) > 1 and '|' not in v: tok = ('BAR', None)            # code word: barrier
    elif r['grade'] in ('H', 'C'): tok = ('K', set(canon(x) for x in v.split('|')))
    else: tok = ('F', set(canon(x) for x in v.split('|')) if v != '?' else set())
    ents.setdefault(lab, []).append(tok)
def place(toks, w):
    L = len(w); need = max(3, math.ceil(L/2)); out = []
    for off in range(0, len(toks)-L+1):
        win = toks[off:off+L]
        if any(t[0] == 'BAR' for t in win): continue
        A = sum(1 for t, c in zip(win, w) if t[0] == 'K' and c in t[1])
        mis = sum(1 for t, c in zip(win, w) if t[0] == 'K' and c not in t[1])
        free = sum(1 for t in win if t[0] == 'F')
        magree = sum(1 for t, c in zip(win, w) if t[0] == 'F' and c in t[1])
        if free >= 1 and A >= need and mis <= 1:
            out.append((1 if mis == 0 else 2, off, A, free, magree))
    return out
def totals(E):
    t = {1: 0, 2: 0}
    for w in CRIBS:
        for lab, toks in E.items():
            for p in place(toks, w): t[p[0]] += 1
    return t
# control vocabulary
P = os.path.join(T, 'passes'); vocab = set()
for r in csv.DictReader((l for l in open(os.path.join(P, 'inv373_0693_r10/align_words.tsv')) if not l.startswith('#')), delimiter='\t'):
    vocab.add(canon(r['plain']))
for s in ('0702_r13', '0730_r13', '0746_r14', '0758_r14'):
    for r in csv.DictReader((l for l in open(os.path.join(P, f'inv373_{s}/gloss_reconciled.tsv')) if not l.startswith('#')), delimiter='\t'):
        for w in re.split(r'[\s\-]+', r['gloss'] or ''): vocab.add(canon(w))
vocab = sorted(w for w in vocab if len(w) >= 3 and w not in CRIBS)
print(f"entries {len(ents)} ({' '.join(ents)}), tokens {sum(len(v) for v in ents.values())}; cribs {len(CRIBS)}; control vocabulary {len(vocab)} words")
real = totals(ents)
print(f"\nREAL totals: tier1 {real[1]}  tier2 {real[2]}")
print("\nplacements (crib entry@off tier A free M-agree | window values | p_b n_ctrl verdict):")
surv = []
for w in CRIBS:
    for lab, toks in ents.items():
        for tier, off, A, free, mag in place(toks, w):
            win = ''.join((sorted(t[1])[0] if t[1] else '?') if t[0] != 'BAR' else '#' for t in toks[off:off+len(w)])
            grd = ''.join('K' if t[0] == 'K' else 'f' for t in toks[off:off+len(w)])
            ctrl = [c for c in vocab if len(c) == len(w)]
            hit = sum(1 for c in ctrl if any(p[0] <= tier and p[2] >= A for p in place(toks, c)))
            pb = hit/len(ctrl) if ctrl else float('nan')
            verdict = 'untestable(<20)' if len(ctrl) < 20 else ('SURVIVES' if pb <= 0.05 else 'fails')
            if verdict == 'SURVIVES': surv.append((w, lab, off, tier))
            print(f"  {w} {lab}@{off} t{tier} A{A} free{free} M-agree{mag} | {win} {grd} | p_b {pb:.3f} ({hit}/{len(ctrl)}) {verdict}")
rng = random.Random(); ct = {1: [], 2: []}
for s in range(2039, 2039+SEEDS):
    rng.seed(s); E = {}
    for lab, toks in ents.items():
        idx = [i for i, t in enumerate(toks) if t[0] != 'BAR']; vals = [toks[i] for i in idx]; rng.shuffle(vals)
        nt = list(toks)
        for i, v in zip(idx, vals): nt[i] = v
        E[lab] = nt
    t = totals(E); ct[1].append(t[1]); ct[2].append(t[2])
for k in (1, 2):
    xs = sorted(ct[k]); p95 = xs[int(0.95*len(xs))-1]; ge = sum(1 for x in xs if x >= real[k])/len(xs)
    print(f"\ncontrol (a) within-entry shuffle, {SEEDS} seeds, tier{k}: mean {statistics.mean(xs):.2f}, p95 {p95}, real {real[k]}, frac seeds >= real {ge:.3f}")
print(f"\nsurvivors (p_b <= 0.05): {surv if surv else 'none'}")
