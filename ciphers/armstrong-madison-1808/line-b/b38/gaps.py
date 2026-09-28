"""B38: label-free unit segmentation from the column ink profile.
Images on disk are already binarised (0/255). An ink column has >= MINROWS ink pixels; runs narrower than MINRUN px
are dropped as specks; gaps narrower than MINGAP px are bridged (broken strokes). Gap widths are collected per crop.
Bimodality: 1- vs 2-component Gaussian mixture on log gap width, fitted by EM, BIC difference. Unit split: a gap is a
unit boundary if it exceeds the 2-component crossover (or, fallback, the mixture's larger-component mean minus 1 sd).
Known-answer control: numeral lines images/crops_0030/f0030_L01-17.jpg -> runs-per-unit distribution compared with the
transcription's digit-count distribution (1:17, 2:115, 3:119, 4:118 of 369). Target: the pure-glyph crops from B35.
Usage: python3 gaps.py"""
import glob, math, sys, json
import numpy as np
from PIL import Image
ROOT = "/home/user/cipher-lab/ciphers/armstrong-madison-1808"
MINROWS, MINRUN, MINGAP = 2, 3, 1
DOTW, DOTH = 12, 16  # a period: narrow and short; a thin glyph stroke is narrow but tall  # MINGAP 1: no bridging (bridging at 3 px merged nothing useful, see gaps_out.txt)
PURE = ["page1_L03_seq2-2_1marks", "page1_L12_seq106-121_16marks", "page1_L13_seq122-141_19marks", "page2_L01_seq188-197_1marks",
        "page2_L02_seq198-212_15marks", "page2_L03_seq213-226_9marks", "page3_L13_seq511-528_18marks"]
def runs_gaps(path):
    im = np.asarray(Image.open(path).convert("L")) < 128
    col = im.sum(0) >= MINROWS
    r = np.diff(np.r_[0, col.astype(int), 0]); starts = np.where(r == 1)[0]; ends = np.where(r == -1)[0]
    runs = [(a, b) for a, b in zip(starts, ends) if b - a >= MINRUN]
    # v2 (B39's control, 28 Sept 2026): the hand writes a period after each group; a dot (under DOTW px wide and under
    # DOTH px tall) sits inside the between-group gap and split it into two short gaps, merging neighbouring groups
    # into one unit while the dot itself counted as a unit (unit widths 4 px and 442 px on line L16, see b39/). Dots
    # are removed and the gap measured between the real runs on either side.
    def height(a, b):
        rows = np.where(im[:, a:b].sum(1) > 0)[0]; return rows[-1] - rows[0] + 1 if len(rows) else 0
    runs = [(a, b) for a, b in runs if not (b - a < DOTW and height(a, b) < DOTH)]
    merged = []
    for a, b in runs:
        if merged and a - merged[-1][1] < MINGAP: merged[-1] = (merged[-1][0], b)
        else: merged.append((a, b))
    gaps = [merged[i+1][0] - merged[i][1] for i in range(len(merged) - 1)]
    return merged, gaps
def em2(x, iters=200):
    x = np.asarray(x, float); mu = np.percentile(x, [25, 75]); sd = np.array([x.std(), x.std()]) + 1e-6; w = np.array([.5, .5])
    for _ in range(iters):
        ll = np.stack([w[k] * np.exp(-(x - mu[k])**2 / (2 * sd[k]**2)) / (sd[k] * math.sqrt(2 * math.pi)) for k in range(2)])
        r = ll / ll.sum(0, keepdims=True); n = r.sum(1); w = n / len(x); mu = (r * x).sum(1) / n
        sd = np.sqrt((r * (x - mu[:, None])**2).sum(1) / n) + 1e-3
    lik = np.log(ll.sum(0)).sum(); return mu, sd, w, lik
def bic_1v2(x):
    x = np.log(np.asarray(x, float)); n = len(x)
    l1 = -0.5 * n * (1 + math.log(2 * math.pi * x.var() + 1e-12)); bic1 = -2 * l1 + 2 * math.log(n)
    mu, sd, w, l2 = em2(x); bic2 = -2 * l2 + 5 * math.log(n)
    o = np.argsort(mu); mu, sd, w = mu[o], sd[o], w[o]
    # crossover: point between the means where the two weighted densities are equal (grid search)
    g = np.linspace(mu[0], mu[1], 400)
    d = [w[k] * np.exp(-(g - mu[k])**2 / (2 * sd[k]**2)) / sd[k] for k in range(2)]
    cross = g[np.argmin(np.abs(d[0] - d[1]))]
    return bic1 - bic2, math.exp(mu[0]), math.exp(mu[1]), w[1], math.exp(cross)
def units(paths, thresh):
    per_unit = []
    for p in paths:
        merged, gaps = runs_gaps(p); n = 1
        for g in gaps:
            if g > thresh: per_unit.append(n); n = 1
            else: n += 1
        per_unit.append(n)
    return per_unit
def summarise(name, paths):
    allg = [g for p in paths for g in runs_gaps(p)[1]]; nr = sum(len(runs_gaps(p)[0]) for p in paths)
    dbic, m1, m2, w2, cross = bic_1v2(allg)
    print(f"{name}: {len(paths)} crops, {nr} ink runs, {len(allg)} gaps; median gap {np.median(allg):.0f} px, p10 {np.percentile(allg,10):.0f}, p90 {np.percentile(allg,90):.0f}")
    print(f"  log-gap mixture: BIC(1)-BIC(2) = {dbic:.1f} (positive favours two components); component means {m1:.1f} px and {m2:.1f} px, large-gap weight {w2:.2f}, crossover {cross:.1f} px")
    return allg, cross
def items(path):
    """known answer per manuscript line: numeral groups and glyph marks in tr/page1_pass*.tsv (one line per row)"""
    d = {}
    for l in open(path):
        p = l.rstrip("\n").split("\t"); toks = p[1].split() if len(p) > 1 else []
        d[p[0]] = (sum(t.isdigit() for t in toks), sum(1 for t in toks if set(t) == {"*"}))
    return d
if __name__ == "__main__":
    from collections import Counter
    numer = sorted(glob.glob(f"{ROOT}/images/crops_0030/f0030_L*.jpg")); line = lambda p: p.split("_")[-1][:3]
    kA = items(f"{ROOT}/tr/page1_passA.tsv"); kB = items(f"{ROOT}/tr/page1_passB_norm.tsv")
    numonly = [k for k in kA if kA[k][0] >= 5 and kA[k][1] == 0 and kB[k][1] == 0]
    print("known-answer control, page 1 (frame 0030), per manuscript line: units = ink runs split at gaps > threshold")
    print("  numeral-only lines", numonly, "groups", [kA[k][0] for k in numonly])
    best = None
    for thr in range(15, 61, 5):
        u = {line(p): len([g for g in runs_gaps(p)[1] if g > thr]) + 1 for p in numer}
        x = np.array([kA[k][0] for k in numonly]); y = np.array([u[k] for k in numonly])
        ks = [k for k in kA if kA[k][0] + kA[k][1] >= 5]; xa = np.array([kA[k][0] + kA[k][1] for k in ks]); ya = np.array([u[k] for k in ks])
        print(f"  >{thr} px: numeral-only lines units {y.tolist()} vs groups {x.tolist()}, MAE {np.abs(x-y).mean():.2f}; all lines with >=5 items (groups+marks): MAE {np.abs(xa-ya).mean():.2f}, r {np.corrcoef(xa,ya)[0,1]:.2f}, sum {ya.sum()} vs {xa.sum()}")
        if best is None or np.abs(x-y).mean() < best[0]: best = (np.abs(x-y).mean(), thr)
    thr = best[1]; print(f"  calibrated threshold (min MAE on numeral-only lines): {thr} px")
    # gap populations on the numeral-only lines: within-group vs between-group, using the transcription's group count per line
    within, between = [], []
    for p in numer:
        if line(p) in numonly:
            g = sorted(runs_gaps(p)[1], reverse=True); n = kA[line(p)][0] - 1
            between += g[:n]; within += g[n:]
    print(f"  numeral-only lines: the {len(between)} largest gaps per line (= group boundaries by count) median {np.median(between):.0f} px, p10 {np.percentile(between,10):.0f}; the remaining {len(within)} within-group gaps median {np.median(within):.0f} px, p90 {np.percentile(within,90):.0f}")
    pure = [f"{ROOT}/images/shorthand/{n}.jpg" for n in PURE]; marks = [1, 16, 19, 1, 15, 9, 18]  # index.tsv mark counts = B35 reader A glyph counts
    gP = [g for p in pure for g in runs_gaps(p)[1]]; print(f"pure-glyph lines: {sum(len(runs_gaps(p)[0]) for p in pure)} ink runs for {sum(marks)} glyphs; gaps median {np.median(gP):.0f} px, p10 {np.percentile(gP,10):.0f}, p90 {np.percentile(gP,90):.0f}")
    u = [len([g for g in runs_gaps(p)[1] if g > thr]) + 1 for p in pure]
    print(f"  units at the calibrated {thr} px: {u} for mark counts {marks}; glyphs per unit {sum(marks)/sum(u):.2f} (en18 letters per word about 4.2; a one-glyph-per-unit design gives 1.0)")
    for name, g in (("numeral-only lines, all gaps", [x for p in numer if line(p) in numonly for x in runs_gaps(p)[1]]), ("pure-glyph lines", gP)):
        g = [x for x in g if x < 200]; dbic, m1, m2, w2, cross = bic_1v2(g)
        print(f"  log-gap mixture, {name} (gaps < 200 px, n={len(g)}): BIC(1)-BIC(2) = {dbic:.1f}; means {m1:.0f} / {m2:.0f} px, large weight {w2:.2f}, crossover {cross:.0f} px")
    json.dump({"threshold_px": thr, "pure_units": u, "pure_marks": marks}, open("gaps.json", "w"))
