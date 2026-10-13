#!/usr/bin/env python3
"""BAL167-GSEQ (13 Oct 2026, LANE DEFAULT-A2-2013): word-level key-anchored sequence settle of the f.124 'gt' gloss letter
(PREREG-BAL-GSEQ.md). Disk only. Reads balshape/gseq/runs.tsv and key.tsv; prints the target result, the known-answer control and
the shuffled-key false-settle control. Usage (target folder): python3 balshape/gseq/settle_gseq.py [n_shuffles]"""
import csv, random, sys
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
TOL = 1  # max mismatched letters per word, over H-consumed letters only
key = {}
for r in csv.reader(open('key.tsv'), delimiter='\t'):
    if not r or r[0].startswith('#') or r[0] == 'code': continue
    if len(r) >= 3 and r[2] == 'H' and r[0].endswith("'"): key[r[0]] = r[1].lower()
runs = [r for r in csv.DictReader((l for l in open('balshape/gseq/runs.tsv') if not l.startswith('#')), delimiter='\t')]

def align(signs, word, k, target_idx, target_len=1, lf=False):
    """Consume word left to right from the anchor. Returns leftover string under signs[target_idx] or None."""
    # anchor: first sign (left to right) whose H value is an exact prefix of the word
    start = next((i for i, s in enumerate(signs) if s in k and word.startswith(k[s])), None)
    if start is None or start > target_idx: return None
    pos, mism, got = 0, 0, None
    for i in range(start, len(signs)):
        s = signs[i]
        if pos == len(word): break
        if s == '|':
            return got if (lf and got is not None and i > target_idx) else None   # line end: word may continue (line-final only)
        if i == target_idx: n = target_len
        elif s in k: n = len(k[s])
        else: n = 1                                                       # non-H sign (letter sign, unread): one letter
        if pos + n > len(word): return None
        seg = word[pos:pos + n]
        if i == target_idx: got = seg
        elif s in k: mism += sum(a != b for a, b in zip(seg, k[s]))
        if mism > TOL: return None
        pos += n
    return got if pos == len(word) and got is not None else None

def token_letter(row, k):
    signs = row['signs'].split()
    occ = [i for i, s in enumerate(signs) if s == 'gt']
    ti = occ[0] if row['token'] in ('c131_gt1', 'c132_gt') else occ[1]
    res = set()
    for w in row['words'].split('/'):
        if row['line_final'] == '1':
            g = align_lf(signs, w, k, ti)
        else:
            g = align(signs, w, k, ti)
        if g is not None: res.add(g)
    return res

def align_lf(signs, word, k, ti):
    # line-final token: the word may run past the strip's end; consume up to and including the target, then stop at '|'
    return align(signs[:ti + 1] + ['|'], word, k, ti, lf=True)

def settle(k):
    per = {}
    for r in runs:
        per[(r['read'], r['token'])] = token_letter(r, k)
    letters = [next(iter(v)) if len(v) == 1 else None for v in per.values()]
    ok = all(l is not None for l in letters) and len(set(letters)) == 1
    return ok, (letters[0] if ok else None), per

ok, val, per = settle(key)
print('TARGET (gt as 1-letter unknown):')
for (rd, tok), v in per.items(): print(f'  read {rd} {tok}: {sorted(v) or "no alignment"}')
print(f'  SETTLED={ok} value={val}')

# Known-answer control: each H-valued non-anchor sign inside an aligned run, blanked to an unknown of its own length; gt as 1-letter wildcard
ka_n = ka_ok = 0
for r in runs:
    signs = r['signs'].split()
    occ = [i for i, s in enumerate(signs) if s == 'gt']
    gi = occ[0] if r['token'] in ('c131_gt1', 'c132_gt') else occ[1]
    for w in r['words'].split('/'):
        start = next((i for i, s in enumerate(signs) if s in key and w.startswith(key[s])), None)
        if start is None: continue
        for j in range(start + 1, gi):
            s = signs[j]
            if s not in key: continue
            k2 = dict(key); v = k2.pop(s); sig = list(signs); sig[j] = 'UNK'
            if r['line_final'] == '1': sig = sig[:gi + 1] + ['|']
            got = align(sig, w, k2, j, len(v), lf=r['line_final'] == '1')
            ka_n += 1; ka_ok += (got is not None and sum(a != b for a, b in zip(got, v)) <= TOL)
            print(f'  KA read {r["read"]} {r["token"]} word {w}: blank {s} (H {v}) -> {got}')
print(f'KNOWN-ANSWER recovery: {ka_ok}/{ka_n} = {ka_ok / max(ka_n, 1):.3f}')

# Shuffled-key control: permute values among the acute H codes; run the full settle rule
codes = sorted(key); vals = [key[c] for c in codes]
rnd = random.Random(20261013); fs = 0; tokc = 0; tokn = 0
for _ in range(N):
    p = vals[:]; rnd.shuffle(p); k = dict(zip(codes, p))
    o, v, pr = settle(k); fs += o
    for x in pr.values(): tokn += 1; tokc += (len(x) == 1)
print(f'SHUFFLED-KEY ({N} permutations of {len(codes)} acute H values, seed 20261013): false-settle {fs}/{N} = {fs / N:.4f}; '
      f'token-reads with a single word-consistent leftover {tokc}/{tokn} = {tokc / tokn:.4f}')
