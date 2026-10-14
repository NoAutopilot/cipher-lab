"""COL26-SIB (account 1, LANE DEFAULT-A1-1840-14, 14 Oct 2026): the f.23 key (key_f23.tsv C codes, f.23 + sibling gloss values) applied
to ONE glossed sibling leaf at word grain, beside a shuffled-key control, a word-shuffle control and a synthetic two-digit code control at
the leaf's own N. Pre-registered with PREREG-COL26-SIB.md: this file is pushed BEFORE stage 0 is run and before any pairing of the leaf
exists; nothing below the docstring changes after the first run except a logged bug fix.

LEAF CHOICE (fixed here, before any number): canvas 51 first (rows 51L01-51L06 of siblings/c5051_reconciled.tsv; crops cut from
  images/crops/canvas51_full.jpg on disk). Fallback canvas 32 (siblings/c32_reconciled.tsv) only if c51 is TOO-SHORT at stage 0.
  canvas 30 is not eligible: it failed its own line-grain control (A2-COL6, D2-COL26), and a unit that failed its own control is not used.
SCORED KEY K: the codes graded C in key_f23.tsv (as committed at registration), minus every code whose C grade used the leaf itself:
  c51 -> minus 30 (D2-COL26 used c51 4/4 for 30 = s); c32 -> minus 23 and 12 (R9-COL26's 14 units include c32) and 30 is kept (D2-COL26
  did not use c32). Values normalised as word_c33.py (lowercase, letters only, v->u, j->i).
STATISTIC (word_da1.py / word_c33.py hit rule, unchanged): a code c_j at slot j of a span of k groups under gloss word t (L letters) is
  predicted at o_j = round(j*L/k); HIT iff its value v starts at s in {o_j-1, o_j, o_j+1}, 0 <= s, s+len(v) <= L. H = hits over every
  occurrence of a K code inside a paired span. N = number of such occurrences.
CONTROLS on the leaf (10000 draws, seed 20261014 + 1840):
  SK (shuffled key) -- the values of K permuted among the codes of K (same value multiset, same occurrences, same spans);
  W  (shuffled words) -- the gloss words permuted over the leaf's spans (word_c33.py's Control W).
GATE (per pass): PASS_pass iff H > p95(SK) and P_SK < 0.05 and P_W < 0.05. Leaf PASS iff PASS on BOTH blind passes. Else FAIL, or
  FAIL-LOWPOWER if the stage-0 power at the leaf's realised N (nearest bin) is < 0.5.
STAGE 0 (before any pairing, no vision): SYNTHETIC CONTROL at the leaf's N. Plaintext = the gloss words of every OTHER glossed sibling
  unit on disk (c33, c3536, c3940, c4749, c5051 minus the leaf, c5456, c6263, c32 unless it is the leaf), consecutive runs from a random
  start. Synthetic key = key_f23.tsv's own code -> value map (all 71 codes) plus one extra code per letter a-z that no single-letter
  value covers (codes 1-9, then unused two-digit numbers); each word is enciphered left to right by the longest key value matching at
  that point (homophones chosen uniformly). The synthetic leaf has the target's gloss-word count per row; true word spans are known;
  reader error = each internal boundary of a row moves by one group (left or right, equal odds, never emptying a span) with probability
  q = 0.25. Scored with the same K, statistic, SK and W controls (1000 draws each) and the same per-pass gate, applied to two
  independent noisy pairings of the same synthetic leaf (both must pass). Power = share of 300 synthetic leaves whose realised N lies
  within +-3 of the target's ideal N (the K occurrences inside glossed rows) that PASS. Sensitivity q = 0 and q = 0.4 printed, not
  gated. Gate: power >= 0.5 -> live (vision for this leaf); else TOO-SHORT -> try the fallback leaf; both TOO-SHORT -> stop, no vision.
STAGE 1: siblings/word_pairs_sib_<leaf>_p1.tsv, _p2.tsv (two blind Sonnet passes on line crops; groups with indices and gloss words per
  row, no key value, no other pass's spans; horizontal placement only), mechanical reconciliation as word_c33.py (in-row, ordered,
  non-overlapping; offending row dropped). Reader agreement printed (diagnostic).
MERGE RULE: this script edits no key file. On a leaf PASS the worker adds a decode job for the leaf (key_f23.tsv; K codes read at their key
  grade, every other token M) and runs tools/decode_key.py --check; on FAIL no key or reading file is touched.
Usage: python3 siblings/word_sib.py --stage 0|1 [--leaf c51|c32]
"""
import csv, os, re, sys
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def norm(s): return re.sub(r'[^a-z]', '', re.sub(r'\[[^\]]*\]', '', s.lower())).replace('v', 'u').replace('j', 'i')
KEY = list(csv.DictReader(open(f'{T}/key_f23.tsv'), delimiter='\t'))
CALL = {r['code']: norm(r['value']) for r in KEY if r['grade'] == 'C' and norm(r['value'])}
EXCL = {'c51': {'30'}, 'c32': {'23', '12'}}
LEAF = {'c51': ('c5051_reconciled.tsv', '51'), 'c32': ('c32_reconciled.tsv', None)}
OTHER = ['c33_reconciled.tsv', 'c3536_reconciled.tsv', 'c3940_reconciled.tsv', 'c4749_reconciled.tsv', 'c5051_reconciled.tsv',
         'c5456_reconciled.tsv', 'c6263_reconciled.tsv', 'c32_reconciled.tsv']
Q = 0.25; NSYN = 300; DSYN = 1000; DT = 10000

def rows_of(fn, pre=None):
    rs = list(csv.DictReader(open(f'{H}/{fn}'), delimiter='\t'))
    return [r for r in rs if pre is None or r['line'].startswith(pre)]

def hit(t, j, k, v):
    L = len(t); o = round(j * L / k)
    return any(0 <= s and s + len(v) <= L and t[s:s + len(v)] == v for s in (o - 1, o, o + 1))

def score(spans, K, rng, D):
    """spans: list of (word, [(slot, code)], k). Returns H, N, SK p95, P_SK, P_W."""
    occ = [(i, j, k, c) for i, (t, cs, k) in enumerate(spans) for j, c in cs if c in K]
    N = len(occ)
    if N == 0: return 0, 0, 0.0, 1.0, 1.0
    W = [s[0] for s in spans]
    h = sum(hit(W[i], j, k, K[c]) for i, j, k, c in occ)
    codes = sorted(K); vals = [K[c] for c in codes]
    sk = np.empty(D, int); cw = np.empty(D, int)
    for d in range(D):
        pv = dict(zip(codes, rng.permutation(vals)))
        sk[d] = sum(hit(W[i], j, k, pv[c]) for i, j, k, c in occ)
        pw = rng.permutation(len(W))
        cw[d] = sum(hit(W[pw[i]], j, k, K[c]) for i, j, k, c in occ)
    return h, N, float(np.percentile(sk, 95)), float((sk >= h).mean()), float((cw >= h).mean())

def passes(r): h, N, p95, psk, pw = r; return N > 0 and h > p95 and psk < 0.05 and pw < 0.05

# ---------- synthetic two-digit code control ----------
def synth_key():
    m = {r['code']: norm(r['value']) for r in KEY if norm(r['value'])}
    single = {v for v in m.values() if len(v) == 1}
    used = set(m); free = [str(x) for x in range(1, 100) if str(x) not in used]
    for ch in 'abcdefghilmnopqrstuxyz':
        if ch not in single: m[free.pop(0)] = ch
    inv = {}
    for c, v in m.items(): inv.setdefault(v, []).append(c)
    return inv

def encipher(word, inv, rng):
    out, p = [], 0
    vals = sorted(inv, key=len, reverse=True)
    while p < len(word):
        for v in vals:
            if word.startswith(v, p):
                out.append(inv[v][rng.integers(len(inv[v]))]); p += len(v); break
        else: p += 1  # letter not in the inventory (k, w): skipped
    return out

def noisy_spans(lens, q, rng):
    """lens: groups per word in one row. Returns (first,last) per word after boundary noise."""
    b = np.cumsum([0] + lens)  # boundaries b[0]=0 .. b[n]=total
    nb = b.copy()
    for i in range(1, len(lens)):
        if rng.random() < q:
            nb[i] += 1 if rng.random() < 0.5 else -1
            if nb[i] <= nb[i - 1] or nb[i] >= b[i + 1]: nb[i] = b[i]
    return [(nb[i], nb[i + 1] - 1) for i in range(len(lens))]

def synth_power(target_rows, K, nideal, q, rng, pool):
    wpr = [len([w for w in (norm(x) for x in r['gloss'].split()) if w]) for r in target_rows]
    wpr = [n for n in wpr if n]; tot = sum(wpr)
    inv = synth_key(); res = []; tries = 0
    while len(res) < NSYN and tries < NSYN * 40:
        tries += 1
        st = rng.integers(0, len(pool) - tot); words = pool[st:st + tot]
        groups = [encipher(w, inv, rng) for w in words]
        if any(len(g) == 0 for g in groups): continue
        n = sum(c in K for g in groups for c in g)
        if abs(n - nideal) > 3: continue
        ok = []
        for _ in range(2):
            spans, wi = [], 0
            for nw in wpr:
                rw = words[wi:wi + nw]; rg = groups[wi:wi + nw]; wi += nw
                flat = [c for g in rg for c in g]
                for t, (a, bb) in zip(rw, noisy_spans([len(g) for g in rg], q, rng)):
                    seg = flat[a:bb + 1]; spans.append((t, list(enumerate(seg)), len(seg)))
            ok.append(passes(score(spans, K, rng, DSYN)))
        res.append(all(ok))
    return (float(np.mean(res)) if res else 0.0), len(res)

def leaf_material(leaf):
    fn, pre = LEAF[leaf]; rows = rows_of(fn, pre)
    K = {c: v for c, v in CALL.items() if c not in EXCL[leaf]}
    nideal = sum(c in K for r in rows if any(norm(x) for x in r['gloss'].split()) for c in r['tokens'].split())
    pool = []
    for f in OTHER:
        if f == fn and leaf == 'c32': continue
        rs = rows_of(f)
        if f == 'c5051_reconciled.tsv' and leaf == 'c51': rs = [r for r in rs if not r['line'].startswith('51')]
        pool += [w for r in rs for w in (norm(x) for x in r['gloss'].split()) if w]
    return rows, K, nideal, pool

def stage0(leaf):
    rows, K, nideal, pool = leaf_material(leaf)
    print(f'{leaf}: {len(rows)} rows, gloss words {sum(len([w for w in (norm(x) for x in r["gloss"].split()) if w]) for r in rows)}, '
          f'K = {len(K)} codes (excluded {sorted(EXCL[leaf])}), ideal N (K occurrences in glossed rows) {nideal}, pool {len(pool)} words')
    out = {}
    for q in (Q, 0.0, 0.4):
        pw, n = synth_power(rows, K, nideal, q, np.random.default_rng(20261014 + 1840 + int(q * 100)), pool)
        out[q] = pw
        print(f'{leaf}: synthetic power q={q:.2f}: {pw:.3f} over {n} synthetic leaves (N within +-3 of {nideal})'
              + ('  <- gated' if q == Q else '  (sensitivity, not gated)'))
    v = 'live' if out[Q] >= 0.5 else 'TOO-SHORT'
    print(f'{leaf}: STAGE 0 VERDICT {v}')
    return v

def load_pairs(leaf, tag):
    fn, pre = LEAF[leaf]; toks = {r['line']: r['tokens'].split() for r in rows_of(fn, pre)}
    spans, last, dropped, raw = [], {}, 0, []
    for r in csv.DictReader(open(f'{H}/word_pairs_sib_{leaf}_{tag}.tsv'), delimiter='\t'):
        L = r['line']; tk = toks.get(L)
        try: a, b = int(r['first']), int(r['last'])
        except ValueError: dropped += 1; continue
        if tk is None or not (0 <= a <= b < len(tk)) or a <= last.get(L, -1): dropped += 1; continue
        last[L] = b; t = norm(r['word']); g = tk[a:b + 1]
        cs = [(j, c) for j, c in enumerate(g) if c.isdigit()]
        if t and cs: spans.append((t, cs, len(g))); raw.append((L, t, a, b))
    return spans, dropped, raw

if __name__ == '__main__':
    stage = sys.argv[sys.argv.index('--stage') + 1] if '--stage' in sys.argv else '0'
    print(f'COL26-SIB word-grain test of key_f23 C on one sibling leaf; key_f23 C codes {len(CALL)}: {" ".join(sorted(CALL, key=int))}')
    if stage == '0':
        if stage0('c51') != 'live':
            print('c51 TOO-SHORT: fallback c32');
            if stage0('c32') != 'live': print('STOP: both leaves TOO-SHORT, no vision.')
        raise SystemExit(0)
    leaf = sys.argv[sys.argv.index('--leaf') + 1]
    rows, K, nideal, pool = leaf_material(leaf)
    rng = np.random.default_rng(20261014 + 1840)
    res = {}
    for tag in ('p1', 'p2'):
        spans, dropped, raw = load_pairs(leaf, tag)
        r = score(spans, K, rng, DT); res[tag] = (r, raw)
        h, N, p95, psk, pw = r
        print(f'{tag}: {len(spans)} spans ({dropped} rows dropped); K occ N {N} H {h} SK p95 {p95:.0f} P_SK {psk:.4f} P_W {pw:.4f} '
              f'-> {"PASS" if passes(r) else "FAIL"}')
    if all(passes(r) for r, _ in res.values()): print(f'VERDICT {leaf}: PASS (both passes)')
    else: print(f'VERDICT {leaf}: FAIL (FAIL-LOWPOWER if the stage-0 power at the realised N is < 0.5; see stage-0 output)')
    w1 = {(L, t): (a, b) for L, t, a, b in res['p1'][1]}; w2 = {(L, t): (a, b) for L, t, a, b in res['p2'][1]}
    both = set(w1) & set(w2); ex = sum(w1[x] == w2[x] for x in both)
    near = sum(abs(w1[x][0] - w2[x][0]) <= 1 and abs(w1[x][1] - w2[x][1]) <= 1 for x in both)
    print(f'diagnostic: words placed by both passes {len(both)}, exact span agreement {ex}, within one group each end {near}')
