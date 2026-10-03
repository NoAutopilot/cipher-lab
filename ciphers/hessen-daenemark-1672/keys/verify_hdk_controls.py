#!/usr/bin/env python3
"""VERIFY-HDK (account-4 verifier, 3 Oct 2026): two control audits, from committed files only.
(1) Pair-level breakdown of keys/gloss_heldout.py: the leave-one-out score counts each agreeing pair of
    occurrences twice; report per code, per pair, and the exact chance that a random pair of glosses agrees.
(2) Selection-free re-test of key 255's letter table: decode EVERY token of the two f.4 runs (ciphertext.tsv,
    p3_15-17 and p3_20-21, nomenclator groups dropped) and score the longest common subsequence against the
    gloss strings, so no (token, gloss-letter) pair is chosen by anyone who has seen the key.  Control: the
    same 24-label permutation as keys/key255_gloss_test.py, same LCS, 20000 draws.
Usage: python3 keys/verify_hdk_controls.py [--seed N]"""
import csv, itertools, os, random, re, sys
sys.path.insert(0, os.path.dirname(__file__))
D = os.path.join(os.path.dirname(__file__), '..')
seed = int(sys.argv[sys.argv.index('--seed') + 1]) if '--seed' in sys.argv else 4
# (1) pairs
rows = list(csv.DictReader(open(os.path.join(D, 'transcription', 'gloss_pairs.tsv'), encoding='utf-8'), delimiter='\t'))
gl = [re.sub(r'[^a-z?]', '', r['plain_raw'].lower()) for r in rows]
def same(a, b):
    k = min(8, len(a), len(b)); return k > 0 and all(x == y or '?' in (x, y) for x, y in zip(a[:k], b[:k]))
by = {}
for r, g in zip(rows, gl): by.setdefault(r['cipher_raw'], []).append((r['cipher_line'], g))
print("(1) recurring codes:")
for c, occ in by.items():
    if len(occ) > 1: print(f"  {c}: " + " | ".join(f"{l}={g}" for l, g in occ) + f"  agree={same(occ[0][1], occ[1][1])}")
allp = list(itertools.combinations(range(len(gl)), 2)); m = sum(same(gl[i], gl[j]) for i, j in allp)
p = m / len(allp)
print(f"  gloss pairs agreeing by chance: {m}/{len(allp)} = {p:.4f} per pair; "
      f"independent agreeing pairs 4 (3 without the 690 override) -> chance p^4 = {p**4:.2e}, p^3 = {p**3:.2e}")
# (2) LCS
import contextlib, io
with contextlib.redirect_stdout(io.StringIO()):  # the test script prints at import
    from key255_gloss_test import L, table
ct = list(csv.DictReader(open(os.path.join(D, 'ciphertext.tsv'), encoding='utf-8'), delimiter='\t'))
cols = list(ct[0].keys())
def toks(lines):
    out = []
    for r in ct:
        if r[cols[0]] in lines:
            s = r[cols[2]] if len(cols) > 2 else ''
            if re.fullmatch(r'[A-Z]{2}|\d{1,3}', s) and not (s.isdigit() and int(s) > 179): out.append(s)
    return out
def lcs(a, b):
    prev = [0] * (len(b) + 1)
    for x in a:
        cur = [0]
        for j, y in enumerate(b): cur.append(prev[j] + 1 if x == y else max(prev[j + 1], cur[j]))
        prev = cur
    return prev[-1]
runs = {'run1': (toks({'p3_15', 'p3_16', 'p3_17'}), ['disgustirtundertanin', 'disgustirtunvertanin']),
        'run2': (toks({'p3_20', 'p3_21'}), ['gottgebdasammwoablaut'])}
rng = random.Random(seed)
for name, (tk, gls) in runs.items():
    for g in gls:
        real = lcs([table(L).get(t, '.').lower() for t in tk], g)
        ctrl = []
        for _ in range(20000):
            pm = list(L); rng.shuffle(pm); t = table(pm); ctrl.append(lcs([t.get(x, '.').lower() for x in tk], g))
        ctrl.sort()
        print(f"(2) {name} {len(tk)} tokens vs '{g}' ({len(g)}): LCS {real}; control mean {sum(ctrl)/len(ctrl):.2f}, "
              f"p99 {ctrl[int(.99*len(ctrl))]}, max {ctrl[-1]}, P(ctrl>=real) {sum(c >= real for c in ctrl)/len(ctrl):.5f}")
