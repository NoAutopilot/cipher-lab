#!/usr/bin/env python3
"""LAG-MARKS (9 Oct 2026): list every marks-kept (literal-sign) split between pass A and its witness (L1 or B), the
cells LAG-ERR's 0.183 pooled / 0.107 A-vs-B figures count, with the committed v2 sign and v2 note beside each, so the
cells can be settled from the image. Same alignment as lag_err.py (build_v2.py's NW on literal signs). CPU only.
  python3 lag_marks_cells.py [--check]   writes lag_marks_cells.tsv; --check exits 1 if stale."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import contextlib, io
_argv, sys.argv = sys.argv, sys.argv[:1]   # LAG-V2 (9 Oct 2026): lag_err's own --check exits at import, which made
with contextlib.redirect_stdout(io.StringIO()):   # this script's --check always 0; import it without our flags
    import lag_err as le   # re-writes its own deterministic outputs (lag_err.py --check stays 0)
sys.argv = _argv
rp, a = le.rp, le.a

def v2map(f):
    m = {}
    for l in open(os.path.join(HERE, f), encoding="utf-8").read().splitlines()[1:]:
        c = l.split("\t") + [""] * 6
        if c[0]: m[f"{c[0]}.{c[1]}"] = (c[2], c[3], c[4], c[5])
    return m
V = {"6179": v2map("ciphertext_6179_v2.tsv"), "6467": v2map("ciphertext_6467_v2.tsv")}

rows = []
for name, ar, wn, wr in le.units:
    keys = [f'{ln}.{pos}' for (ln, pos, g, *_) in ar if rp.norm_sign(g, a)]
    xs, ys = le.seq(ar), le.seq(wr)
    for i, j in rp.nw(xs, ys):
        if i is None or j is None:
            continue
        x, y = xs[i], ys[j]
        if x == y:
            continue
        kind = "base" if le.base(x) != le.base(y) else "mark"
        v = V[name.split()[0]].get(keys[i], ("", "", "", ""))
        rows.append((f"{name} A-vs-{wn}", keys[i], x, y, kind) + v)
out = "unit\tA_line.pos\tA_sign\twitness_sign\tkind\tv2_sign\tv2_conf\tv2_alt\tv2_note\n" + \
      "".join("\t".join(r) + "\n" for r in rows)
p = os.path.join(HERE, "lag_marks_cells.tsv")
if "--check" in sys.argv:
    sys.exit(0 if os.path.exists(p) and open(p, encoding="utf-8").read() == out else 1)
open(p, "w", encoding="utf-8").write(out)
print(f"{len(rows)} split cells ({sum(r[4]=='mark' for r in rows)} mark-only, {sum(r[4]=='base' for r in rows)} base)")
