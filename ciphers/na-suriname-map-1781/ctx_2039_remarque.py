#!/usr/bin/env python3
"""SUR-CTX (13 Oct 2026): pre-registered context test of the 2039 Remarque's unkeyed sign classes K x4, O x2, & x2,
[J-rev] x2 in the Remarque's own words (PREREG-SUR-CTX.md). The SUR-ALIGN shape (word-anchor scan, value- and
letter-shuffle controls), with a Dutch vocabulary frozen from tools/data/nl18 instead of a sibling crib, and a known-answer
power check run BEFORE any target class is scored.

Anchor: a vocabulary word w of length L (4..12) covering the tested slot, all L slots inside one segment (segments cut at
non-letter tokens and position gaps), every keyed slot agreeing (H/C/single-valued M exact; two-valued M g|l, k|i either
letter), at most one other U slot (wildcard), keyed agreements >= max(3, L-2). The letter w puts at the tested slot is
that instance's candidate. Per class: A(v) = number of the class's tested instances with >= 1 anchor giving v;
v* = argmax A, licensed iff A(v*) = k (all k tested instances), v* unique, its anchors from >= 2 distinct words, and both
controls reject at p <= 0.0025 (0.01 / 4 classes): value-shuffle (keyed values permuted among the Remarque's sign classes)
and letter-shuffle (letters permuted within each vocabulary word); null statistic = max_v A(v) with the same uniqueness
and >= 2-word conditions; p = share of draws licensing at A >= the real A(v*).

Usage: python3 ctx_2039_remarque.py --dry | --calib [--n 200] | --score [--n 1000]   (seed 20391013)
"""
import collections, csv, glob, gzip, os, random, re, sys, unicodedata
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, '..', '..'))
args = sys.argv[1:]
N = int(args[args.index('--n') + 1]) if '--n' in args else (200 if '--calib' in args else 1000)
SEED = 20391013
TARGETS = ['K', 'O', '&', '[J-rev]']
ALPHA = set('abcdefghiklnopqrstvwyz')   # letters the Nieuw key's values produce (key_period_codes_nieuw.tsv)
P_GATE = 0.0025

# ---- vocabulary (frozen rule: nl18, fold, len 4..12, count >= 5, letters in ALPHA) ----
def fold(s):
    s = unicodedata.normalize('NFKD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return s.replace('ij', 'y').replace('u', 'v').replace('j', 'i')
cnt = collections.Counter()
for fn in sorted(glob.glob(os.path.join(root, 'tools/data/nl18/*.txt.gz'))):
    cnt.update(re.findall(r'[a-z]+', fold(gzip.open(fn, 'rt', encoding='utf-8', errors='ignore').read())))
VOCAB = sorted(w for w, c in cnt.items() if 4 <= len(w) <= 12 and c >= 5 and set(w) <= ALPHA)

# ---- target slots ----
rows = [r for r in csv.DictReader((l for l in open(os.path.join(here, 'reading_2039_remarque_nieuw_tokens.tsv'),
        encoding='utf-8') if not l.startswith('#')), delimiter='\t') if '_rem_' in r['line']]
segs = []   # list of lists of dict(sign, value, grade, id)
for ln in dict.fromkeys(r['line'] for r in rows):
    cur, last = [], None
    for r in sorted((r for r in rows if r['line'] == ln), key=lambda r: int(r['pos'])):
        p = int(r['pos']); v = r['value']
        ok = r['grade'] == 'U' or re.fullmatch(r'[a-z](\|[a-z])?', v)
        if not ok or (last is not None and p != last + 1):
            if cur: segs.append(cur)
            cur = []
        if ok: cur.append(dict(sign=r['sign'], value=v, grade=r['grade'], id=f"{ln}:{p}"))
        last = p
    if cur: segs.append(cur)

def slot_re(t, value):
    if t['grade'] == 'U': return None
    return '[' + value.replace('|', '') + ']' if '|' in value else value

def candidates(masked, test_ids, vmap, vocab_by_len):
    """For each tested id: dict letter -> set(words). masked: sign classes treated as U; vmap: sign -> value override."""
    out = {}
    for seg in segs:
        for i, t in enumerate(seg):
            if t['id'] not in test_ids: continue
            got = collections.defaultdict(set)
            for L in range(4, 13):
                for off in range(L):
                    a = i - off
                    if a < 0 or a + L > len(seg): continue
                    pat, nwild, nkey = [], 0, 0
                    for j in range(a, a + L):
                        s = seg[j]
                        if j == i: pat.append('(.)'); continue
                        if s['grade'] == 'U' or s['sign'] in masked:
                            nwild += 1; pat.append('.')
                        else:
                            v = vmap.get(s['sign'], s['value']) if vmap else s['value']
                            nkey += 1; pat.append(slot_re(s, v))
                    if nwild > 1 or nkey < max(3, L - 2): continue
                    rx = re.compile('^' + ''.join(pat) + '$', re.M)
                    for m in rx.finditer(vocab_by_len[L]):
                        got[m.group(1)].add(m.group(0))
            out[t['id']] = got
    return out

def decide(cands, ids):
    A = collections.Counter(); words = collections.defaultdict(set)
    for i in ids:
        for v, ws in cands.get(i, {}).items():
            A[v] += 1; words[v] |= ws
    if not A: return None, 0, set()
    top = A.most_common()
    v, a = top[0]
    if len(top) > 1 and top[1][1] == a: return None, a, set()
    return v, a, words[v]

def licensed(v, a, ws, k):
    return v is not None and a == k and len(ws) >= 2

def by_len(vocab):
    d = collections.defaultdict(list)
    for w in vocab: d[len(w)].append(w)
    return {L: '\n'.join(d[L]) for L in range(4, 13)}

REAL = by_len(VOCAB)
keyed_signs = sorted({t['sign'] for s in segs for t in s if t['grade'] != 'U' and '|' not in t['value']})

def null_draws(masked, ids, k, rng, n):
    """Return (value-shuffle list, letter-shuffle list) of null (v, a, ws) licensing A values (0 if not licensed)."""
    vs, ls = [], []
    vals = [next(t['value'] for s in segs for t in s if t['sign'] == g and t['grade'] != 'U') for g in keyed_signs]
    for _ in range(n):
        perm = vals[:]; rng.shuffle(perm)
        v, a, ws = decide(candidates(masked, ids, dict(zip(keyed_signs, perm)), REAL), ids)
        vs.append(a if licensed(v, a, ws, k) else 0)
        sh = [''.join(rng.sample(w, len(w))) for w in VOCAB]
        v, a, ws = decide(candidates(masked, ids, None, by_len(sh)), ids)
        ls.append(a if licensed(v, a, ws, k) else 0)
    return vs, ls

def run_class(masked, ids, k, rng, n):
    c = candidates(masked, ids, None, REAL)
    v, a, ws = decide(c, ids)
    lic = licensed(v, a, ws, k)
    pv = pl = None
    if lic:
        vs, ls = null_draws(masked, ids, k, rng, n)
        pv = sum(x >= a for x in vs) / n; pl = sum(x >= a for x in ls) / n
        lic = pv <= P_GATE and pl <= P_GATE
    return v, a, sorted(ws), pv, pl, lic, c

if __name__ == '__main__':
    allt = [t for s in segs for t in s]
    if '--dry' in args:
        print(f"vocab {len(VOCAB)} words (nl18, len 4-12, count>=5, letters in ALPHA); segments {len(segs)}; slots {len(allt)}")
        for g in TARGETS: print(g, [t['id'] for t in allt if t['sign'] == g])
        hc = collections.Counter(t['sign'] for t in allt if t['grade'] in 'HC')
        print('calibration classes (H/C, >=2 instances):', {g: c for g, c in hc.items() if c >= 2})
        sys.exit(0)
    rng = random.Random(SEED)
    if '--calib' in args:
        hc = collections.Counter(t['sign'] for t in allt if t['grade'] in 'HC')
        print('class\tk\ttested\ttrue\tv*\tA\twords\tp_value\tp_letter\tlicensed\tcorrect')
        for g in sorted(c for c, n in hc.items() if n >= 2):
            inst = [t for t in allt if t['sign'] == g]
            true = next(t['value'] for t in inst if t['grade'] in 'HC')
            for k in (2, 4):
                if len(inst) < k: continue
                ids = {t['id'] for t in rng.sample(inst, k)}
                v, a, ws, pv, pl, lic, _ = run_class({g}, ids, k, rng, N)
                print(f"{g}\t{k}\t{','.join(sorted(ids))}\t{true}\t{v}\t{a}\t{len(ws)}\t{pv}\t{pl}\t{int(lic)}\t{int(lic and v == true)}")
        sys.exit(0)
    if '--score' in args:
        print('class\tk\tv*\tA\twords\tp_value\tp_letter\tlicensed\tper-instance candidates')
        for g in TARGETS:
            ids = {t['id'] for t in allt if t['sign'] == g}
            v, a, ws, pv, pl, lic, c = run_class(set(), ids, len(ids), rng, N)
            per = '; '.join(f"{i}:{''.join(sorted(c.get(i, {})))}" for i in sorted(ids))
            print(f"{g}\t{len(ids)}\t{v}\t{a}\t{','.join(ws[:8])}\t{pv}\t{pl}\t{int(lic)}\t{per}")
        sys.exit(0)
    print(__doc__)
