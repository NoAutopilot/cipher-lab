"""R10-COL26C: pre-registered held-out check of the R10-COL26B leads 32 = u and 15 = e on the f.23 rotated margin postscript
(margin/f23m_reconciled.tsv, A2-COL4; not among the 14 anchor_split units, never used to build key_f23 or either lead).
Registered before the first run (this docstring is the registration; committed and pushed before running).
Span: in each margin unit (gloss letters only, lowercase, v->u, j->i, as margin/kat.py), walk ALL codes in order; every
C-grade code of key_f23.tsv as committed (23 = n included) is an anchor matched by kat.py's ordered greedy find. For each
occurrence of a target code, the span is the gloss from the end of the last matched anchor before it (unit start if none) to
the start of the next anchor after it that matches at or after that point (unit end if none).
Statistic per code: H = number of its occurrences whose span contains the lead value (32: 'u'; 15: 'e').
Control (can vary: it changes the letters a span meets, not the positions): for each occurrence, a window of the same span
length cut at random from the f.23 main-text gloss (interlinear/f23w_pairs.tsv, concatenated), 5000 draws, same seed 1644;
H_ctrl counted the same way. P = P(H_ctrl >= H_real).
Power check, done first: P_min = P(H_ctrl >= number of occurrences), the best P the code could reach. If P_min >= 0.05 the code
is UNDERPOWERED at this N and the outcome is logged as untestable here, whatever H_real is.
Gate per code: PASS if H_real == occurrences and P < 0.05 (no Bonferroni needed: 2 codes, report P against 0.025 too); FAIL if
H_real < occurrences; otherwise HELD. key_f23.tsv changes only on PASS (grade M -> C for that value, source note naming this
check); 32's committed value is 'o' (M), so a PASS for u also changes the value.
Also reported, not gated: the same walk for 32 with value 'o' (its committed M value), so the u/o split is visible.
Usage: python3 margin/heldout_r10.py"""
import csv, random, re, os
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def norm(s): return re.sub(r'[^a-z]', '', s.lower()).replace('v', 'u').replace('j', 'i')
key = {r['code']: (norm(r['value']), r['grade']) for r in csv.DictReader(open(f'{T}/key_f23.tsv'), delimiter='\t')}
units = list(csv.DictReader(open(f'{H}/f23m_reconciled.tsv'), delimiter='\t'))
bank = norm(''.join(r['plain_raw'] for r in csv.DictReader(open(f'{T}/interlinear/f23w_pairs.tsv'), delimiter='\t')))
LEADS = [('32', 'u'), ('15', 'e'), ('32', 'o')]
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
rng = random.Random(1644)
print('code\tvalue\tunit_spans\tH_real\tocc\tctrl_mean\tp95\tmax\tP\tP_min\tgate')
for code, val in LEADS:
    sp = []
    for u in units:
        for s in spans(u['codes'].split(), norm(u['gloss']), code): sp.append((u['unit'], s))
    h = sum(val in s for _, s in sp); n = len(sp)
    ctrl = []
    for _ in range(5000):
        k = 0
        for _, s in sp:
            L = max(len(s), 0); st = rng.randrange(0, len(bank) - L); k += val in bank[st:st + L]
        ctrl.append(k)
    ctrl.sort(); P = sum(x >= h for x in ctrl) / 5000; Pmin = sum(x >= n for x in ctrl) / 5000
    gate = ('UNDERPOWERED' if Pmin >= 0.05 else 'FAIL' if h < n else 'PASS' if P < 0.05 else 'HELD')
    if (code, val) == ('32', 'o'): gate = 'not gated'
    print(f"{code}\t{val}\t{';'.join(f'{u}:{s}' for u, s in sp)}\t{h}\t{n}\t{sum(ctrl)/5000:.2f}\t{ctrl[4750]}\t{ctrl[-1]}\t{P:.4f}\t{Pmin:.4f}\t{gate}")
