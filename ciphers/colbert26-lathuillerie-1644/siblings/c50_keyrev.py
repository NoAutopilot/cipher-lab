"""COL26-KEY (account 4, LANE DEFAULT-A4-0437-15, 15 Oct 2026): the next key_f23 revision with canvas 50 folded in as a unit that
cleared. Pre-registered: this file and PREREG-COL26-KEY.md are committed and pushed BEFORE the first run (rule 3); nothing below the
docstring changes after the first run except a logged bug fix (NOTES.md, before/after output).

What is folded in. Only the 21 canvas 50 tokens VER-COL50 kept at C (siblings/verify_c50_out.txt, verdict 'C': key_f23 C code, value
located in its own gloss word by a blind word pairing). They are all codes already C in key_f23, so they cannot re-value anything;
what they add is POSITION: each fixes where its value sits inside its c50 gloss word. Canvas 51 (COL26-SIB FAIL) is not an input.

Derivation (the revision). For each of the two blind c50 word pairings already on disk (word_pairs_da1.tsv = DA1-COL,
word_pairs_col2.tsv = DA1-COL2; tokens from c5051_reconciled.tsv, as word_da1.py reads them), every c50 word span that contains at
least one of the 21 anchor tokens is cut at its anchors: the anchor's value is placed at the start s in {o-1, o, o+1} nearest
o = round(j * L / k) where the word has it (word_da1.py's hit rule; an anchor the pass does not place is skipped in that pass). The
codes between two anchors (or between a word edge and an anchor) form a segment of n slots (unsettled groups keep a slot) over the
segment's letters; slot i gets the chunk seg[round(i*len/n) : round((i+1)*len/n)]. Every OPEN code (not C in key_f23) with a non-empty
chunk is a candidate occurrence. Candidate value per code = its most frequent chunk over both passes (tie: the chunk seen in both
passes, then shorter, then alphabetical). Revision file: key_f23_c50rev.tsv (new, beside key_f23.tsv, which is never overwritten):
key_f23 rows copied, the 21 C codes' notes carry their c50 attestation count, each candidate code gets column rev_value = its candidate.

Held-out units (named now): the word-paired units outside c50 whose own instrument check cleared: c3940 and c47 (DA1-COL pass 1 and
DA1-COL2 pass 2), c54, c55, c56, c63 (DA1-COL3, one pass, used in both scorings); c62 excluded (its instrument FAILED, word_col3_out).
Statistic: H = word_da1.py's positional hits of the candidate codes, at their rev_value, over every occurrence in held-out spans.
Before/after: H_before = the same occurrences scored at key_f23's current value for those codes (M or U; a code with no key_f23 value
scores 0); gain = H_after - H_before (reported).
Control SP (shuffled pair; the axis is the code -> value pairing the revision proposes): the candidate values permuted among the
candidate codes, 10000 draws. Control W (pairing shuffle in held-out units, word texts permuted over that unit's spans), 10000 draws.
Both can differ from the target on H (H depends on which value each code gets and on which word lies over it).
GATE (per scoring, both scorings must pass): H_after > p95(SP) AND P_SP < 0.05 AND P_W < 0.05 AND hits from >= 2 held-out units.
Stage 0 (power, before the gate is read): the key_f23 C codes at their committed values, held-out occurrences subsampled to N codes =
the number of candidate codes with any held-out occurrence (1000 random code subsets), each scored against its own shuffled-pair
control (values permuted within the subset, 2000 draws); power = share with P_SP < 0.05. Power < 0.5 -> NON-TEST at this N
(reported, not a negative on c50); no further gate read.
Diagnostic (reported, not gating): the derivation's known-answer rate -- key_f23 C codes that fall at a non-anchor slot inside an
anchored c50 segment: share whose value is found in the segment within +-1 letter of the chunk start, vs the same with segment texts
permuted among anchored segments (2000 draws).
Merge rule: PASS -> rev_value enters key_f23_c50rev.tsv with grade M and note 'COL26-KEY unit gate PASS; per-code test owed' (a unit
gate places no single code: VER-COL50's ruling); key_f23.tsv, decode.json and every reading unchanged either way. FAIL / NON-TEST ->
rev_value column written with grade '-' (candidate only). Output: siblings/c50_keyrev_out.txt. Usage: python3 siblings/c50_keyrev.py
"""
import csv, os, re, collections, sys
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def norm(s): return re.sub(r'[^a-z]', '', re.sub(r'\[[^\]]*\]', '', s.lower())).replace('v', 'u').replace('j', 'i')
KROWS = list(csv.DictReader(open(f'{T}/key_f23.tsv'), delimiter='\t'))
key = {r['code']: (norm(r['value']), r['grade']) for r in KROWS}
C = {c: v for c, (v, g) in key.items() if g == 'C' and v}
out = []
def say(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)
# --- anchors: the 21 VER-COL50 C tokens
anch = set()
_vl = open(f'{H}/verify_c50_out.txt').read().splitlines()
_vl = _vl[next(i for i, l in enumerate(_vl) if l.startswith('line\tpos')):]
for r in csv.DictReader((l for l in _vl if '\t' in l), delimiter='\t'):
    if r.get('verdict') == 'C': anch.add((r['line'], int(r['pos']) - 1, r['code']))
assert len(anch) == 21, len(anch)
def load_toks(fns, strip):
    d = {}
    for fn in fns:
        for r in csv.DictReader(open(f'{H}/{fn}_reconciled.tsv'), delimiter='\t'):
            d[r['line']] = [x for x in r['tokens'].split() if not (strip and x == '|')]
    return d
TK1 = load_toks(('c5051', 'c3940', 'c4749'), False)
TK3 = load_toks(('c5456', 'c6263'), True)
for L, p, c in anch: assert TK1[L][p] == c, (L, p, c)
def unit_of(L):
    if L.startswith('50'): return 'c50'
    if L[:2] in ('39', '40'): return 'c3940'
    if L.startswith('47'): return 'c47'
    if L[:2] in ('54', '55', '56', '62', '63'): return 'c' + L[:2]
def read_pairs(fn, tk):
    sp = collections.defaultdict(list); last = {}
    for r in csv.DictReader(open(f'{H}/{fn}'), delimiter='\t'):
        L = r['line']; u = unit_of(L)
        if u is None or L not in tk: continue
        a, b = int(r['first']), int(r['last'])
        assert 0 <= a <= b < len(tk[L]) and a > last.get(L, -1), r; last[L] = b
        sp[u].append((L, a, norm(r['word']), tk[L][a:b + 1]))
    return sp
P1 = read_pairs('word_pairs_da1.tsv', TK1); P2 = read_pairs('word_pairs_col2.tsv', TK1); P3 = read_pairs('word_pairs_col3.tsv', TK3)
def place(t, j, k, v):
    L = len(t); o = round(j * L / k)
    ok = [s for s in (o, o - 1, o + 1) if 0 <= s and s + len(v) <= L and t[s:s + len(v)] == v]
    return ok[0] if ok else None
# --- derivation
cand = collections.defaultdict(collections.Counter); seen = collections.defaultdict(lambda: collections.defaultdict(set))
known = []  # (segment text, chunk start, value) for C codes at non-anchor slots
nanch_placed = {}
for pname, P in (('DA1-COL', P1), ('DA1-COL2', P2)):
    placed = 0
    for L, a, t, g in P['c50']:
        k = len(g)
        if not t: continue
        cuts = []
        for j, c in enumerate(g):
            if (L, a + j, c) in anch:
                s = place(t, j, k, C[c])
                if s is not None: cuts.append((j, s, s + len(C[c])))
        cuts.sort(); cuts = [x for i, x in enumerate(cuts) if i == 0 or x[1] >= cuts[i - 1][2]]
        if not cuts: continue
        placed += len(cuts)
        bounds = [(-1, 0)] + [(j, e) for j, s, e in cuts]; starts = [(j, s) for j, s, e in cuts] + [(k, len(t))]
        for (j0, e0), (j1, s1) in zip(bounds, starts):
            slots = list(range(j0 + 1, j1)); seg = t[e0:s1]; n = len(slots)
            if n == 0 or not seg: continue
            for i, j in enumerate(slots):
                c = g[j]; lo, hi = round(i * len(seg) / n), round((i + 1) * len(seg) / n); ch = seg[lo:hi]
                if not c.isdigit(): continue
                if c in C: known.append((seg, lo, C[c]))
                elif ch: cand[c][ch] += 1; seen[c][ch].add(pname)
    nanch_placed[pname] = placed
say('COL26-KEY c50 key revision; anchors 21; placed per pass', nanch_placed)
REV = {}
for c, cnt in cand.items():
    best = sorted(cnt.items(), key=lambda kv: (-kv[1], -len(seen[c][kv[0]]), len(kv[0]), kv[0]))[0][0]
    REV[c] = best
say(f'candidate codes {len(REV)}:', ' '.join(f'{c}={REV[c]}({sum(cand[c].values())})' for c in sorted(REV, key=int)))
rng = np.random.default_rng(20261015 + 437)
# --- diagnostic: derivation known-answer
def ka(segs):
    return sum(any(0 <= s and t[s:s + len(v)] == v for s in (lo - 1, lo, lo + 1)) for t, (lo, v) in zip(segs, [(x[1], x[2]) for x in known]))
if known:
    realk = ka([x[0] for x in known]); texts = [x[0] for x in known]
    ck = np.array([ka(list(rng.permutation(texts))) for _ in range(2000)])
    say(f'diagnostic known-answer: C codes at non-anchor slots {len(known)}, value at chunk +-1 {realk}; segment-permuted mean {ck.mean():.2f} '
        f'p95 {np.percentile(ck, 95):.0f} P {(ck >= realk).mean():.4f}')
# --- held-out scoring
def hit(t, j, k, v):
    if not v: return False
    L = len(t); o = round(j * L / k)
    return any(0 <= s and s + len(v) <= L and t[s:s + len(v)] == v for s in (o - 1, o, o + 1))
HELD = ['c3940', 'c47', 'c54', 'c55', 'c56', 'c63']
def scoring(name, src):
    spans = {u: [(t, g) for L, a, t, g in src[u] if t and any(x.isdigit() for x in g)] for u in HELD}
    occ = [(u, i, j, len(g), c) for u in HELD for i, (t, g) in enumerate(spans[u]) for j, c in enumerate(g) if c in REV]
    codes = sorted({o[4] for o in occ}, key=int)
    def H_of(val, perm=None):
        h = 0; units = set()
        for u, i, j, k, c in occ:
            ii = perm[u][i] if perm else i
            if hit(spans[u][ii][0], j, k, val.get(c, '')): h += 1; units.add(u)
        return h, units
    Ha, ua = H_of(REV); Hb, _ = H_of({c: key[c][0] for c in REV if c in key})
    say(f'[{name}] held-out spans', {u: len(spans[u]) for u in HELD}, f'candidate occurrences {len(occ)} over {len(codes)} codes')
    say(f'[{name}] H_after {Ha} (units {sorted(ua)})  H_before {Hb}  gain {Ha - Hb}')
    # stage 0 power with C codes
    occC = [(u, i, j, len(g), c) for u in HELD for i, (t, g) in enumerate(spans[u]) for j, c in enumerate(g) if c in C]
    Ccodes = sorted({o[4] for o in occC}, key=int); N = len(codes); good = 0; R0 = np.random.default_rng(20261015 + 1)
    byc = collections.defaultdict(list)
    for o in occC: byc[o[4]].append(o)
    for _ in range(1000):
        sub = list(R0.choice(Ccodes, size=min(N, len(Ccodes)), replace=False))
        oc = [o for c in sub for o in byc[c]]; vals = [C[c] for c in sub]
        def hh(m): return sum(hit(spans[u][i][0], j, k, m[c]) for u, i, j, k, c in oc)
        r = hh(dict(zip(sub, vals)))
        cc = [hh(dict(zip(sub, R0.permutation(vals)))) for _ in range(200)]
        good += (np.array(cc) >= r).mean() < 0.05
    power = good / 1000
    say(f'[{name}] stage 0 power at N={N} codes (C codes, shuffled-pair, 1000 subsets x 200 draws): {power:.3f}')
    if power < 0.5:
        say(f'[{name}] NON-TEST at this N (power < 0.5); gate not read'); return 'NON-TEST'
    vals = [REV[c] for c in codes]
    sp = np.array([H_of(dict(zip(codes, rng.permutation(vals))))[0] for _ in range(10000)])
    w = np.array([H_of(REV, {u: rng.permutation(len(spans[u])) for u in HELD})[0] for _ in range(10000)])
    p95 = np.percentile(sp, 95); Psp = (sp >= Ha).mean(); Pw = (w >= Ha).mean()
    ok = Ha > p95 and Psp < 0.05 and Pw < 0.05 and len(ua) >= 2
    say(f'[{name}] SP mean {sp.mean():.2f} p95 {p95:.0f} max {sp.max()} P_SP {Psp:.4f} | W mean {w.mean():.2f} p95 {np.percentile(w, 95):.0f} '
        f'P_W {Pw:.4f} -> {"PASS" if ok else "FAIL"}')
    pc = collections.Counter(); pn = collections.Counter()
    for u, i, j, k, c in occ:
        pn[c] += 1; pc[c] += hit(spans[u][i][0], j, k, REV[c])
    say(f'[{name}] per code (not gating):', ' '.join(f'{c}={REV[c]}:{pc[c]}/{pn[c]}' for c in codes))
    return 'PASS' if ok else 'FAIL'
SC1 = {u: P1[u] for u in ('c3940', 'c47')}; SC1.update({u: P3[u] for u in ('c54', 'c55', 'c56', 'c63')})
SC2 = {u: P2[u] for u in ('c3940', 'c47')}; SC2.update({u: P3[u] for u in ('c54', 'c55', 'c56', 'c63')})
v1 = scoring('scoring 1: DA1-COL + DA1-COL3', SC1); v2 = scoring('scoring 2: DA1-COL2 + DA1-COL3', SC2)
verdict = 'PASS' if v1 == v2 == 'PASS' else 'NON-TEST' if 'NON-TEST' in (v1, v2) else 'FAIL'
say('UNIT GATE:', verdict)
att = collections.Counter(c for _, _, c in anch)
with open(f'{T}/key_f23_c50rev.tsv', 'w', newline='') as f:
    w_ = csv.writer(f, delimiter='\t', lineterminator='\n')
    w_.writerow(list(KROWS[0].keys()) + ['rev_value', 'rev_grade', 'rev_note'])
    for r in KROWS:
        c = r['code']
        if c in att: rv, rg, rn = '', '', f'c50 word-grain attestation {att[c]} (VER-COL50 C tokens, COL26-KEY)'
        elif c in REV:
            rv = REV[c]; rg = 'M' if verdict == 'PASS' else '-'
            rn = (f'c50 anchored-segment candidate, chunks {dict(cand[c])}; ' +
                  ('COL26-KEY unit gate PASS; per-code test owed' if verdict == 'PASS' else f'COL26-KEY unit gate {verdict}; candidate only'))
        else: rv, rg, rn = '', '', ''
        w_.writerow(list(r.values()) + [rv, rg, rn])
    for c in sorted(set(REV) - set(key), key=int):
        w_.writerow([c, '', '', '', ''][:len(KROWS[0])] + [REV[c], 'M' if verdict == 'PASS' else '-',
                    f'not in key_f23; c50 anchored-segment candidate, chunks {dict(cand[c])}; COL26-KEY unit gate {verdict}'])
open(f'{H}/c50_keyrev_out.txt', 'w').write('\n'.join(out) + '\n')
