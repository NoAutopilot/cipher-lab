#!/usr/bin/env python3
"""H29 (29 Sept 2026): Bourdeau's independent read of passage No.9 (sources/bourdeau/cyphersolver-targets-debosnys/
n9_transcription.py, MIT, 25 lines = c2a lines 1-17 and c2b lines 1-8 in our numbering; his CLEAR_* initials dropped)
as a fourth witness for cryptogram 2's three-way splits. Recipe of H26 (h26_bourdeau_witness.py): per line, a
relative-position pairing seeds a his-code -> our-id concordance by majority co-occurrence, refined by two rounds of
Needleman-Wunsch (+2 concordant, 0 otherwise, -1 gap). Everything is HELD OUT: the concordance is fitted on one fold
of lines (odd / even) using only boxes that are NOT three-way splits, and applied to the other fold.
Outputs: (1) held-out concordance on the non-split boxes of the test fold (the witness quality number);
(2) for each three-way split in the test fold, his aligned code's mapped id; if it equals one of the three readings
(A = the draft's sign, B, C from the alt column) the split is 'resolved' to that reading, graded M, flagged
bourdeau-vote; (3) control: the same with his codes shuffled within each test line after alignment (breaks position,
keeps his line's code multiset), 200 draws -- a vote rule that resolves splits at the control's rate is not a witness.
Gate written before the run: the votes are applied to a variant draft only if the held-out concordance on non-split
known codes is >= 0.60 averaged over both folds AND the real resolution count exceeds the control's p97.5. The
settled draft and ciphertext.txt are never changed by this script. Also reports his line-initial pictogram count
(an independent witness for H31). Writes h29_votes.tsv and h29_bourdeau_n9.json."""
import os, sys, csv, json, random, collections
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here); repo = os.path.dirname(os.path.dirname(root))
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
sys.path.insert(0, os.path.join(repo, 'sources/bourdeau/cyphersolver-targets-debosnys')); import n9_transcription as n9
B = [[t for t in l.split() if not t.startswith('CLEAR')] for l in n9.N9]
rows = list(csv.DictReader(open(os.path.join(root, 'ciphertext_c2_draft.tsv')), delimiter='\t'))
by = collections.OrderedDict()
for r in rows: by.setdefault(r['line'], []).append(r)
keys = [f'c2a_L{i:02d}' for i in range(1, 18)] + [f'c2b_L{i:02d}' for i in range(1, 9)]
O = [[r for r in by[k] if r['sign'].rstrip('?') not in PUNCT] for k in keys]
assert len(O) == len(B) == 25
sig = lambda r: r['sign'].rstrip('?')
split = lambda r: r['why'] == 'three-way'

def nw(a, b, score):
    n, m = len(a), len(b); S = [[0] * (m + 1) for _ in range(n + 1)]; T = [[None] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): S[i][0] = -i; T[i][0] = 'u'
    for j in range(1, m + 1): S[0][j] = -j; T[0][j] = 'l'
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            d = S[i - 1][j - 1] + score(a[i - 1], b[j - 1]); u = S[i - 1][j] - 1; l = S[i][j - 1] - 1
            S[i][j] = max(d, u, l); T[i][j] = 'd' if S[i][j] == d else ('u' if S[i][j] == u else 'l')
    i, j = n, m; pairs = []
    while i > 0 or j > 0:
        t = T[i][j]
        if t == 'd': pairs.append((a[i - 1], b[j - 1])); i -= 1; j -= 1
        elif t == 'u': pairs.append((a[i - 1], None)); i -= 1
        else: pairs.append((None, b[j - 1])); j -= 1
    return pairs[::-1]
def concordance(co):
    best = {}
    for (bc, s), n in co.items():
        if bc not in best or n > best[bc][1]: best[bc] = (s, n)
    return {bc: s for bc, (s, n) in best.items()}
def fit(train):
    co = collections.Counter()
    for i in train:
        o, b = O[i], B[i]
        for k, r in enumerate(o):
            if split(r): continue
            j = round(k * (len(b) - 1) / max(1, len(o) - 1)) if len(o) > 1 else 0; co[(b[j], sig(r))] += 1
    c = concordance(co)
    for _ in range(2):
        co = collections.Counter()
        for i in train:
            for x, y in nw(O[i], B[i], lambda x, y: 2 if c.get(y) == sig(x) else 0):
                if x and y and not split(x): co[(y, sig(x))] += 1
        c = concordance(co)
    return c
def readings(r):
    alt = dict(a.split(':', 1) for a in r['alt'].split(';') if ':' in a)
    return {'A': sig(r), 'B': alt.get('B', ''), 'C': alt.get('C', '')}

out = dict(folds=[]); votes = []; ctrl_counts = [0] * 200; rng = random.Random(29)
for fold in (0, 1):
    train = [i for i in range(25) if i % 2 == fold]; test = [i for i in range(25) if i % 2 != fold]
    c = fit(train)
    n = m = a = 0; nsplit = res = 0
    for i in test:
        pairs = nw(O[i], B[i], lambda x, y: 2 if c.get(y) == sig(x) else 0)
        for x, y in pairs:
            if not x: continue
            if split(x):
                nsplit += 1; rd = readings(x); mapped = c.get(y) if y else None
                who = [k for k, v in rd.items() if v and v == mapped]
                if who: res += 1
                votes.append(dict(line=x['line'], position=x['position'], A=rd['A'], B=rd['B'], C=rd['C'], bourdeau_code=y or '',
                                  mapped_id=mapped or '', vote_for=','.join(who), fold=fold))
            elif y:
                n += 1
                if y in c: m += 1; a += c[y] == sig(x)
        # control: his codes shuffled within the line, same alignment slots
        for t in range(200):
            codes = [y for x, y in pairs if y]; rng.shuffle(codes); it = iter(codes); cnt = 0
            for x, y in pairs:
                yy = next(it) if y else None
                if x and split(x) and yy:
                    rd = readings(x); mp = c.get(yy)
                    cnt += any(v and v == mp for v in rd.values())
            ctrl_counts[t] += cnt
    out['folds'].append(dict(fold=fold, test_nonsplit_aligned=n, known=m, concordant=a, rate_known=round(a / max(1, m), 3),
                             rate_all=round(a / max(1, n), 3), splits=nsplit, resolved=res))
    print(out['folds'][-1])
tot_res = sum(f['resolved'] for f in out['folds']); tot_split = sum(f['splits'] for f in out['folds'])
cs = sorted(ctrl_counts); rate = sum(f['concordant'] for f in out['folds']) / max(1, sum(f['known'] for f in out['folds']))
out.update(splits_seen=tot_split, resolved=tot_res, control_mean=round(sum(cs) / 200, 1), control_p975=cs[194],
           mean_rate_known=round(rate, 3), gate_pass=rate >= 0.60 and tot_res > cs[194],
           vote_for_counts=dict(collections.Counter(v['vote_for'] or 'none' for v in votes)))
# his line-initial pictograms (H31 witness): observed vs within-line-shuffle expectation
ini = sum(l[0].startswith('PIC') for l in B if l); exp = sum(sum(t.startswith('PIC') for t in l) / len(l) for l in B if l)
fin = sum(l[-1].startswith('PIC') for l in B if l)
null = []
for _ in range(10000):
    null.append(sum(rng.random() < sum(t.startswith('PIC') for t in l) / len(l) for l in B if l))
out['h31_witness'] = dict(line_initial_pict=ini, line_final_pict=fin, expected=round(exp, 2), p_ge=sum(x >= ini for x in null) / 10000)
print({k: v for k, v in out.items() if k != 'folds'})
with open(os.path.join(root, 'h29_votes.tsv'), 'w') as f:
    w = csv.DictWriter(f, fieldnames=list(votes[0]), delimiter='\t'); w.writeheader(); w.writerows(votes)
json.dump(out, open(os.path.join(root, 'h29_bourdeau_n9.json'), 'w'), indent=1)
