"""B39 step 2: split-half cluster stability of the unit boxes. Features: 16x16 box (256) + log aspect + log width, PCA to
8 dims; Ward agglomerative clustering at k = 2..16. Stability at k: 200 pairs of 70 percent subsamples, adjusted Rand
index between the two clusterings on their shared items. Null: the same on features whose columns are permuted
independently across items (marginals kept, shape structure destroyed). Positive control: the 30 numeral group boxes,
whose digit-count class (1-4 digits) is known -- reported as ARI between the k=4 clustering and the digit-count labels,
and the same stability curve."""
import numpy as np
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import pdist
rng = np.random.default_rng(1)
d = np.load("boxes.npz"); X, src, lab, wh = d["X"], d["src"], d["lab"], d["wh"]
def feats(idx):
    F = X[idx].reshape(len(idx), -1); F = np.c_[F, np.log(wh[idx, 0] / wh[idx, 1]) * 3, np.log(wh[idx, 0]) * 3]  # v2 boxes keep aspect, see boxes.py
    F = (F - F.mean(0)) / (F.std(0) + 1e-6); U, S, Vt = np.linalg.svd(F, full_matrices=False); return F @ Vt[:8].T
def ari(a, b):
    from collections import Counter
    n = len(a); pairs = lambda c: sum(v * (v - 1) / 2 for v in c.values())
    ab = pairs(Counter(zip(a, b))); A = pairs(Counter(a)); B = pairs(Counter(b)); tot = n * (n - 1) / 2
    exp = A * B / tot; mx = (A + B) / 2; return (ab - exp) / (mx - exp + 1e-12)
def clus(F, k): return fcluster(linkage(F, "ward"), k, "maxclust")
def stability(F, k, reps=200):
    n = len(F); out = []
    for _ in range(reps):
        a = rng.choice(n, int(.7 * n), replace=False); b = rng.choice(n, int(.7 * n), replace=False); sh = np.intersect1d(a, b)
        ca = dict(zip(a, clus(F[a], k))); cb = dict(zip(b, clus(F[b], k))); out.append(ari([ca[i] for i in sh], [cb[i] for i in sh]))
    return np.mean(out)
def permuted(F): return np.column_stack([rng.permutation(F[:, j]) for j in range(F.shape[1])])
for name, idx in (("glyph units (59)", np.where([s.startswith("glyph") for s in src])[0]), ("numeral groups (30)", np.where([s.startswith("numeral") for s in src])[0])):
    F = feats(idx); print(name)
    if name.startswith("numeral"):
        dc = np.array([len(l) for l in lab[idx]]); print("  positive control: ARI(k=4 clustering, digit count) =", round(ari(clus(F, 4), dc), 3), "; digit-count classes", dict(zip(*np.unique(dc, return_counts=True))))
    nulls = [permuted(F) for _ in range(20)]
    for k in (2, 3, 4, 6, 8, 10, 12, 16):
        s = stability(F, k, 100); ns = [stability(N, k, 20) for N in nulls]
        print(f"  k={k:2d}: stability ARI {s:.3f} | permuted-feature null mean {np.mean(ns):.3f}, p95 {np.percentile(ns,95):.3f} -> {'ABOVE' if s > np.percentile(ns,95) else 'within null'}")
