"""BIRAGO-NUM-TOOLS (3 Oct 2026): matched positive control for tools/key_crossmatch.py on the Nov 1571 numerical
letters. Synthetic Italian (num/analyze.italian, it16dip), one two-digit homophonic key of NCELL cells over the
target's digits, 5% stray digits, ~250 pairs (one letter's length), runs cut like phase.control; tokens taken
(a) at the true phase and (b) at phase.em's recovered phase (the target's situation). Scored with the TRUE key by
key_crossmatch.pair_stats against the calibrated gate. python3 tools/xmatch_control.py (run from num/)"""
import sys, random
sys.path.insert(0, '.'); sys.path.insert(0, '../../../tools')
import analyze, phase
import key_crossmatch as kx
from collections import Counter

def synth(ncell, nlet, seed, stray_rate=0.05):
    rng = random.Random(seed)
    txt = analyze.italian(nlet, rng)
    letters = sorted(set(txt)); fr = Counter(txt); cells = analyze.CELLS[:]; rng.shuffle(cells)
    key = {l: [cells.pop()] for l in letters}; extra = ncell - len(letters)
    while extra > 0:
        l = max(letters, key=lambda l: fr[l] / len(key[l])); key[l].append(cells.pop()); extra -= 1
    toks = []
    for ch in txt:
        if rng.random() < stray_rate: toks.append(rng.choice('0123456789'))
        toks.append(rng.choice(key[ch]))
    runs, truth, cur, ct = [], [], '', []
    for t in toks:
        cur += t; ct.append(t)
        if len(cur) > 40 and rng.random() < 0.15: runs.append(cur); truth.append(ct); cur, ct = '', []
    if cur: runs.append(cur); truth.append(ct)
    inv = {c: {'value': l} for l, cs in key.items() for c in cs}
    return runs, truth, inv

gate = kx.load_gate(); model = kx.get_model('it')
print('gate stat_min', gate['stat_min'])
for ncell in (40, 55):
    for seed in (1, 2, 3):
        runs, truth, key = synth(ncell, 255, seed)
        true_signs = [x for t in truth for x in t if len(x) == 2]
        best = None
        for s in range(5):
            got = phase.em(runs, seed=s); sc = phase.summary(got)
            if best is None or sc['H'] < best[1]['H']: best = (got, sc)
        em_signs = [x for t in best[0] for x in t if len(x) == 2]
        def spans(ts):
            out, p = set(), 0
            for t in ts:
                if len(t) == 2: out.add((p, t))
                p += len(t)
            return out
        acc = sum(len(spans(a) & spans(b)) for a, b in zip(best[0], truth)) / sum(len(spans(b)) for b in truth)
        res = []
        for name, signs in (('true-phase', true_signs), ('em-phase', em_signs)):
            ps = kx.pair_stats(key, signs, model, n_shuffle=20, seed=0)['own']
            cov = kx.coverage_of(key, signs)
            v = kx.gate_verdict(ps['stat'], cov, len(signs), gate)
            res.append(f"{name} n={len(signs)} cov={cov:.2f} stat={ps['stat']:.2f} {v}")
        print(f'ncell={ncell} seed={seed} phase_acc={acc:.3f} | ' + ' | '.join(res), flush=True)
