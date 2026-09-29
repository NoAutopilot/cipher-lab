"""Step 2(a) on Debosnys, descriptive only (no key, no score.py): word-length KL (pipeline.wl_kl, the languages'
held-out curve) of gaps left by candidate space classes -- X alone, and the six best context clusters -- beside the
Copiale's TRUE space class at the same lengths, clean and with 15 pct noise, and a within-text shuffle of X.
Writes space_class_debosnys.json."""
import json, random, sys, os
sys.argv = sys.argv[:1]
import pipeline as P
sys.path.insert(0, os.path.join(P.HERE, '..')); import score
out = {}
for tid in ['c2', 'c1+c2']:
    seq = score.flat(score.load_text(tid)); n = len(seq)
    rng = random.Random(1); nulls = []
    for _ in range(200):
        s = seq[:]; rng.shuffle(s); nulls.append(P.wl_kl(s, {'X'}))
    nulls.sort()
    cands, _ = P.step_a(seq)
    out[tid] = {'n': n, 'X_share': round(seq.count('X') / n, 3), 'X_kl': round(P.wl_kl(seq, {'X'}), 3),
                'X_kl_shuffled_p05_p50': [round(nulls[10], 3), round(nulls[100], 3)],
                'clusters': [{'kl': round(k, 3), 'share': round(sh, 3), 'signs': sorted(c)} for k, sh, v, c in cands[:6]]}
for n in (658, 790):
    for nz in (0.0, 0.15):
        v = []
        for st in (3000, 30000, 60000):
            w = P.copiale_window(n, st); rng = random.Random(st)
            seq = [t for t, g in w]; true = {t for t, g in w if g == '_'}
            if nz: pool = seq[:]; seq = [rng.choice(pool) if rng.random() < nz else t for t in seq]
            v.append(round(P.wl_kl(seq, true), 3))
        out[f'copiale_true_space_n{n}_noise{nz}'] = v
print(json.dumps(out, indent=1)); json.dump(out, open('space_class_debosnys.json', 'w'), indent=1)
