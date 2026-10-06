"""R10-COL26D: pre-registered held-out test of the R10-COL26B leads 32 = u and 15 = e on the glossed two-digit sibling leaves
NOT among the 14 anchor_split units: canvas 51 (siblings/c5051_reconciled.tsv, lines 51L*; TOO-SHORT for its own C test in
A2-COL15, 13 C occurrences, not a failure; its letter 49-51 passes) and canvas 30 (ciphertext.tsv canvas 30 numerals with
siblings/c30_gloss_reconciled.tsv; did NOT clear its own length-matched key_f23 test, A2-COL6 P 0.18, beat shuffled-gloss P 0.015).
Neither unit was used to build key_f23, R10-COL26B's leads, or R10-COL26C's check. Canvas 31 is a duplicate capture of 30 (excluded).
Registered before the first run (this docstring is the registration; committed and pushed before running). Disk only.
Unit = one numeral line with its line gloss (letters only, lowercase, v->u, j->i, bracketed [..] dropped as in c30_test.py);
lines with an empty gloss give no span and are not counted.
Span (as margin/heldout_r10.py): walk the line's codes in order; every C-grade code of key_f23.tsv as committed (23 = n included)
is an anchor matched by the ordered greedy find; for each occurrence of a target code the span is the gloss from the end of the
last matched anchor before it (line start if none) to the start of the next anchor after it that matches at/after that point
(line end if none).
Statistic per code: H = occurrences whose span contains the lead value (32: 'u'; 15: 'e').
Control (can vary: changes the letters a span meets): per occurrence, a window of the same span length cut at random from the
f.23 main-text gloss bank (interlinear/f23w_pairs.tsv), 5000 draws, seed 1644. P = P(H_ctrl >= H_real).
Power check first, per code on the pooled set (51 + 30): P_min = P(H_ctrl >= occurrences). P_min >= 0.025 (Bonferroni over 2
codes) = UNDERPOWERED -> NON-TEST, logged as untestable here whatever H_real is.
Gate per code (pooled 51 + 30): PASS if H_real == occurrences and P < 0.025; FAIL if H_real < occurrences; else HELD.
Per-unit condition (CLAUDE.md rule 3, per-unit merge clause): a PASS licenses key_f23 M -> C only if canvas 51 alone (the unit
from a letter that cleared) also has H == its occurrences; canvas 30 did not clear its own length-matched control, so a PASS
resting on canvas 30 alone is reported as HELD (pending), not merged. Per-unit H/occ/P printed for both units.
Also reported, not gated: 32 with 'o' (its committed M value) on the same spans.
Key change only on PASS: key_f23.tsv value/grade -> C with a source note naming this check (32's committed value is 'o').
Usage: python3 siblings/heldout_sib_r10.py"""
import csv, random, re, os
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def norm(s): return re.sub(r'[^a-z]', '', re.sub(r'\[[^\]]*\]', '', s.lower())).replace('v', 'u').replace('j', 'i')
key = {r['code']: (norm(r['value']), r['grade']) for r in csv.DictReader(open(f'{T}/key_f23.tsv'), delimiter='\t')}
bank = norm(''.join(r['plain_raw'] for r in csv.DictReader(open(f'{T}/interlinear/f23w_pairs.tsv'), delimiter='\t')))
units = []
for r in csv.DictReader(open(f'{H}/c5051_reconciled.tsv'), delimiter='\t'):
    if r['line'].startswith('51'): units.append(('c51', r['line'], r['tokens'].split(), norm(r['gloss'])))
runs = {}
for r in csv.DictReader(open(f'{T}/ciphertext.tsv'), delimiter='\t'):
    if r['canvas'] == '30': runs.setdefault(int(r['line']), []).append(r['token'])
for r in csv.DictReader(open(f'{H}/c30_gloss_reconciled.tsv'), delimiter='\t'):
    units.append(('c30', r['line'], runs.get(int(r['line']), []), norm(r['gloss'])))
def spans(codes, g, target):
    out = []; p = 0
    for i, c in enumerate(codes):
        if c == target:
            q = p; end = len(g)
            for c2 in codes[i + 1:]:
                if c2 in key and key[c2][1] == 'C':
                    j = g.find(key[c2][0], q)
                    if j >= 0: end = j; break
            out.append(g[p:end])
        elif c in key and key[c][1] == 'C':
            j = g.find(key[c][0], p)
            if j >= 0: p = j + len(key[c][0])
    return out
def test(sp, val, rng):
    h = sum(val in s for _, s in sp); n = len(sp); ctrl = []
    for _ in range(5000):
        k = 0
        for _, s in sp:
            L = len(s); st = rng.randrange(0, len(bank) - L); k += val in bank[st:st + L]
        ctrl.append(k)
    ctrl.sort()
    return h, n, sum(ctrl) / 5000, ctrl[4750], ctrl[-1], sum(x >= h for x in ctrl) / 5000, sum(x >= n for x in ctrl) / 5000
print('code\tvalue\tset\tspans\tH_real\tocc\tctrl_mean\tp95\tmax\tP\tP_min\tgate')
for code, val in [('32', 'u'), ('15', 'e'), ('32', 'o')]:
    sp = [(u, l, s) for u, l, codes, g in units if g for s in spans(codes, g, code)]
    res = {}
    for name, sub in [('pooled', sp), ('c51', [x for x in sp if x[0] == 'c51']), ('c30', [x for x in sp if x[0] == 'c30'])]:
        r = test([(f'{u}:{l}', s) for u, l, s in sub], val, random.Random(1644)) if sub else (0, 0, 0, 0, 0, 1, 1)
        res[name] = r; h, n, m, p95, mx, P, Pmin = r
        if name == 'pooled':
            gate = ('UNDERPOWERED/NON-TEST' if Pmin >= 0.025 else 'FAIL' if h < n else 'PASS' if P < 0.025 else 'HELD')
            if gate == 'PASS' and res.get('c51') is None: pass
        else: gate = '-'
        if (code, val) == ('32', 'o'): gate = 'not gated'
        print(f"{code}\t{val}\t{name}\t{';'.join(f'{u}:{l}:{s}' for u, l, s in sub)}\t{h}\t{n}\t{m:.2f}\t{p95}\t{mx}\t{P:.4f}\t{Pmin:.4f}\t{gate}")
    if (code, val) != ('32', 'o'):
        h, n = res['pooled'][0], res['pooled'][1]; pooled_pass = n and res['pooled'][6] < 0.025 and h == n and res['pooled'][5] < 0.025
        c51ok = res['c51'][1] > 0 and res['c51'][0] == res['c51'][1]
        print(f"{code}\t{val}\tdecision\t{'MERGE (pooled PASS, c51 H==occ)' if pooled_pass and c51ok else 'HELD (pooled PASS, c51 not H==occ)' if pooled_pass else 'no key change'}")
