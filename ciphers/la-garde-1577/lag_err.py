#!/usr/bin/env python3
"""LAG-ERR (8 Oct 2026): re-measure the pass-to-pass and pass-to-v2 disagreement of the la-garde-1577 transcription,
marks kept (literal sign) and marks stripped (base code), and list the sign pairs behind it. CPU only.
  python3 lag_err.py [--check]    writes lag_err.tsv (summary) and lag_err_pairs.tsv; --check exits 1 if stale.
Alignment is build_v2.py's own (tools/reconcile_passes.nw on literal signs, pass A as reference, per page or cipher run).
Units: each aligned A position vs one witness = one comparison; a gap (A position with no witness sign, or a witness
sign with no A position) is counted separately as an indel and is NOT in the substitution rate's numerator."""
import os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_v2 as b
rp = b.rp
a = b.default_args()
L = lambda f: b.load_rows(os.path.join(HERE, f))

def seq(rows):
    return [s[0] for (_, _, g, *_ ) in rows for s in [rp.norm_sign(g, a)] if s]

def base(s):
    d = b.base_digit(s)
    return d if d is not None else "MARK"

# (unit, page-or-run label, A rows, witness name, witness rows)
units = []
A79, B79, L79 = L("ciphertext_6179_passA.tsv"), L("ciphertext_6179_passB.tsv"), L("ciphertext_6179_L1.tsv")
for pg in ("p2", "p3"):
    fa = [r for r in A79 if r[0].startswith(pg)]
    units.append(("6179 " + pg, fa, "L1", [r for r in L79 if r[0].startswith(pg)]))
units.append(("6179 p2", [r for r in A79 if r[0].startswith("p2")], "B", [r for r in B79 if r[0].startswith("p2")]))
A67, L67 = L("ciphertext_6467_passA.tsv"), L("ciphertext_6467_L1.tsv")
units.append(("6467 run1", [r for r in A67 if r[0] in ("p2L6", "p2L7", "p2L8")], "L1", [r for r in L67 if r[0] in ("p2L1", "p2L2", "p2L3")]))
units.append(("6467 run2", [r for r in A67 if r[0] in ("p2L10", "p2L11")], "L1", [r for r in L67 if r[0] in ("p2L4", "p2L5")]))

CELLS = []
def compare(xs, ys, meta=None):
    """-> n aligned, literal mismatches, base mismatches, base mismatches excluding pure-mark tokens on both sides,
    indel A-side, indel witness-side, pair counter (base), literal pair counter."""
    n = lit = bs = bs_nomark = ia = iw = 0
    bp, lp = collections.Counter(), collections.Counter()
    for i, j in rp.nw(xs, ys):
        if i is None: iw += 1; continue
        if j is None: ia += 1; continue
        n += 1
        x, y = xs[i], ys[j]
        if x != y:
            lit += 1; lp[tuple(sorted((x, y)))] += 1
        bx, by = base(x), base(y)
        if bx != by:
            bs += 1; bp[tuple(sorted((bx, by)))] += 1
            if meta: CELLS.append((meta[0], meta[1][i], x, y))
            if bx != "MARK" and by != "MARK": bs_nomark += 1
    return n, lit, bs, bs_nomark, ia, iw, bp, lp

def v2_rows(f):
    out = []
    for l in open(os.path.join(HERE, f), encoding="utf-8").read().splitlines()[1:]:
        c = l.split("\t")
        if c[0]: out.append(c[2])
    return out
v2 = {"6179 p2": None}

lines = ["comparison\tn_aligned\tlit_mismatch\tlit_rate\tbase_mismatch\tbase_rate\tbase_mismatch_digit_only\tdigit_only_rate\tindel_A\tindel_wit"]
tot = collections.defaultdict(lambda: [0]*6)
allbp, alllp = collections.Counter(), collections.Counter()
for name, ar, wn, wr in units:
    keys = [f'{ln}.{pos}' for (ln, pos, g, *_ ) in ar if rp.norm_sign(g, a)]
    r = compare(seq(ar), seq(wr), (f'{name} A-vs-{wn}', keys))
    n, lit, bs, bn, ia, iw, bp, lp = r
    lines.append(f"{name} A-vs-{wn}\t{n}\t{lit}\t{lit/n:.3f}\t{bs}\t{bs/n:.3f}\t{bn}\t{bn/n:.3f}\t{ia}\t{iw}")
    for k, v in zip(range(6), (n, lit, bs, bn, ia, iw)): tot["pooled"][k] += v
    key = "A-vs-" + wn
    for k, v in zip(range(6), (n, lit, bs, bn, ia, iw)): tot[key][k] += v
    allbp.update(bp); alllp.update(lp)
for key in ("A-vs-B", "A-vs-L1", "pooled"):
    n, lit, bs, bn, ia, iw = tot[key]
    lines.append(f"TOTAL {key}\t{n}\t{lit}\t{lit/n:.3f}\t{bs}\t{bs/n:.3f}\t{bn}\t{bn/n:.3f}\t{ia}\t{iw}")

# pass vs committed v2 (not independent: v2 is built from the passes plus image settles)
def v2_vs(passf, v2f, filt):
    A = [r for r in L(passf) if filt(r[0])]
    v = [l.split("\t") for l in open(os.path.join(HERE, v2f), encoding="utf-8").read().splitlines()[1:]]
    v = [c[2] for c in v if c[0] and filt(c[0])]
    return compare(seq(A), v)
for lab, pf, vf, flt in (("6179 A-vs-v2", "ciphertext_6179_passA.tsv", "ciphertext_6179_v2.tsv", lambda l: True),
                         ("6467 A-vs-v2", "ciphertext_6467_passA.tsv", "ciphertext_6467_v2.tsv", lambda l: True)):
    n, lit, bs, bn, ia, iw, *_ = v2_vs(pf, vf, flt)
    lines.append(f"{lab}\t{n}\t{lit}\t{lit/n:.3f}\t{bs}\t{bs/n:.3f}\t{bn}\t{bn/n:.3f}\t{ia}\t{iw}")
out = "\n".join(lines) + "\n"
cells = "unit\tA_line.pos\tA_sign\twitness_sign\n" + "".join("\t".join(c)+"\n" for c in CELLS)
pairs = "kind\tpair\tcount\n" + "".join(f"base\t{x}|{y}\t{c}\n" for (x, y), c in allbp.most_common()) + \
        "".join(f"literal\t{x}|{y}\t{c}\n" for (x, y), c in alllp.most_common())
if "--check" in sys.argv:
    ok = open(os.path.join(HERE, "lag_err.tsv")).read() == out and open(os.path.join(HERE, "lag_err_cells.tsv")).read() == cells and open(os.path.join(HERE, "lag_err_pairs.tsv")).read() == pairs
    sys.exit(0 if ok else 1)
open(os.path.join(HERE, "lag_err.tsv"), "w").write(out); open(os.path.join(HERE, "lag_err_pairs.tsv"), "w").write(pairs); open(os.path.join(HERE, "lag_err_cells.tsv"), "w").write(cells)
print(out); print("top base pairs:"); [print(" ", p, c) for p, c in allbp.most_common(12)]
print("top literal pairs:"); [print(" ", p, c) for p, c in alllp.most_common(12)]
