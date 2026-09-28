"""Line B step B33(a) -- error tolerance of the B32 instrument: the same three controls with 10/15/20 percent of
the signs replaced by a random other sign, words right per level (3 controls each). The mark transcriptions
disagree by about 16 percent (H3), so B32's negative is a design negative only if the instrument still reads its
controls above the 60 percent gate at that error level (CLAUDE.md rule 3, SALV-DIAG)."""
import random, sys
sys.argv = ["x"]; import dict_solver as D
rng = random.Random(31)
for err in (0.10, 0.15, 0.20):
    for k in range(3):
        words, segs = D.synth(random.Random(100 + k)); r = random.Random(500 + k)
        noisy = [[(r.choice(D.SIGNS) if r.random() < err else g) for g in s] for s in segs]
        sc, m = D.solve(noisy, D.SIGNS, rng, 24, 25000)
        dec = ["".join(m[g] for g in s) for s in noisy]; right = sum(1 for d, w in zip(dec, words) if d == w)
        print(f"error {int(err*100)}% control {k}: words right {right}/54 = {100*right/54:.0f}%  e.g. {' '.join(dec[:8])}", flush=True)
