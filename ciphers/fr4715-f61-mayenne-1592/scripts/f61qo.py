#!/usr/bin/env python3
"""F61-QO (campaign step H26, 28 Sept 2026, runner session_01J8hunWPcE7QYcpCx59CUHV): the audit's 'qo' question -- the atlas
folds every loops-on-a-stem sign into PHI (e/r) except the stacked o-T-o form (DBL, b/o); audit 1 saw on L10 a two-loops-
SIDE-BY-SIDE form (positions 6 and 11) that pass 1 itself flagged 'could be DBL-like'. Is the loop family two (or three)
glyphs, and does the side-by-side form go with the e/r trefoils or with the b/o stacked pairs?

Pre-registered before the call (prompt in scripts/PROMPTS.md, H26). Same design as scripts/f61bracket.py (H22): expected
positions and labels from disk -- the PHI and DBL signs of passA_classes.tsv on the six span lines and of read_call_U.tsv
on L10 (f.61), and of the reconciled pass108A/B draft on f.108 bands L02/L03; the letter under each sign is Tomokiyo's,
placed by the F61-CAL DP with the joint cell map; label e/r for e, r and b/o for b, o; a sign under a dash, another letter
or outside the references is listed, never scored. Pairing per sheet in reading order (sheets B do not overlap); a sheet
whose listed count differs from the expected count is dropped. Statistic: best group-to-cell match over the labelled
positions (groups -> {e/r, b/o}); null: exact over all label arrangements when C(n, k) <= 200000, else 2000 permutations,
seed 1, plus the 200-permutation p95 as in H22. Gate (H26): observed above the permutation p95 with p < 0.05. Reported
whatever the gate: which group the L10 side-by-side signs (positions 6, 11) fall in.

  python3 scripts/f61qo.py expected
  python3 scripts/f61qo.py score read_call_QO.tsv [--check]
"""
import csv, itertools, math, os, random, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from f61crib import load_read, load_spans, fit, align
from f61crib3 import load_cells, cell_map, values, OPTS
from f61crib4 import split_lines
from f61joint import f108_lines
SHEETS = ["f61sheetB_L01", "f61sheetB_L03", "f61sheetB_L05", "f61sheetB_L07", "f61sheetB_L08", "f61sheetB_L11", "f61sheetB_L10", "f108sheetB_L02", "f108sheetB_L03"]
CLS = ("PHI", "DBL"); CELLS = ("e/r", "b/o")
def expected():
    lines = split_lines(load_read()); lines.update(f108_lines())
    u = {}
    for r in csv.DictReader((l for l in open(f"{HERE}/read_call_U.tsv") if not l.startswith("#")), delimiter="\t"):
        u.setdefault(r["line"], []).append(r["sign"])
    lines["L10"] = u["L10"]
    spans = load_spans() + [(s, "F108_" + ("L02" if s == "T1" else "L03"), m) for s, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{HERE}/tomokiyo_spans_3983.tsv") if l[0] == "T")]
    cm = values(cell_map(fit(spans, lines, "qo", OPTS, keep_dashes=True), load_cells()))
    letter = {}
    for s, line, markup in spans:
        _, pairs = align(markup, lines[line], cm)
        for mi, sj in pairs:
            if markup[mi] != "-": letter[(line, sj)] = markup[mi]
    out = []
    for sheet in SHEETS:
        line = ("F108_" if sheet.startswith("f108") else "") + sheet.split("_")[1]
        for j, c in enumerate(lines.get(line, [])):
            if c in CLS:
                L = letter.get((line, j), "-"); lab = "e/r" if L in "er" else ("b/o" if L in "bo" else "-")
                out.append((sheet, j + 1, c, L, lab))
    return out
def stat(groups, labels):
    gs = sorted(set(groups)); best = 0
    for lets in itertools.product(CELLS, repeat=len(gs)):
        m = dict(zip(gs, lets)); best = max(best, sum(1 for g, l in zip(groups, labels) if m[g] == l))
    return best
def score(path):
    exp = expected(); by_sheet = defaultdict(list)
    for e in exp: by_sheet[e[0]].append(e)
    rows = list(csv.DictReader((l for l in open(f"{HERE}/{path}") if not l.startswith("#")), delimiter="\t"))
    got = defaultdict(list)
    for r in rows: got[r["sheet"].replace(".jpg", "")].append(r)
    out = [f"{path}: {len(rows)} loop signs listed; expected {len(exp)} ({sum(1 for e in exp if e[4] != '-')} labelled)"]
    groups, labels = [], []; qo = []
    for sheet in SHEETS:
        g = sorted(got.get(sheet, []), key=lambda r: (int(r["segment"]), float(r["x_px"]))); e = by_sheet.get(sheet, [])
        if len(g) != len(e):
            out.append(f"  {sheet}: expected {len(e)}, listed {len(g)} -> NOT reconciled, dropped"); continue
        for r, ex in zip(g, e):
            out.append(f"  {sheet}/{ex[1]} {ex[2]}: group {r['group']} ({r.get('arrangement', '')}), letter {ex[3]} ({ex[4]})")
            if sheet == "f61sheetB_L10" and ex[1] in (6, 11): qo.append((ex[1], r["group"], r.get("arrangement", "")))
            if ex[4] != "-": groups.append(r["group"]); labels.append(ex[4])
    n = len(labels)
    if n < 5: out.append(f"scored {n} < 5: NON-TEST")
    else:
        obs = stat(groups, labels); k = labels.count("b/o")
        if math.comb(n, k) <= 200000:
            exact = [stat(groups, ["b/o" if i in c else "e/r" for i in range(n)]) for c in itertools.combinations(range(n), k)]
            p = sum(1 for e in exact if e >= obs) / len(exact); pnote = f"exact P(>=obs) = {p:.4f} over {len(exact)} arrangements"
        else:
            rng = random.Random(1); cnt = 0
            for _ in range(2000):
                l2 = list(labels); rng.shuffle(l2); cnt += stat(groups, l2) >= obs
            p = cnt / 2000; pnote = f"permutation P(>=obs) = {p:.4f} over 2000 (seed 1)"
        rng = random.Random(1); perm = []
        for _ in range(200):
            l2 = list(labels); rng.shuffle(l2); perm.append(stat(groups, l2))
        perm.sort(); p95 = perm[int(0.95 * 200) - 1]
        out.append(f"scored {n} (e/r {n - k}, b/o {k}); groups {len(set(groups))}; observed {obs}/{n}; {pnote}; permutation p95 {p95}/{n}")
        out.append(f"GATE H26: {'PASS' if obs > p95 and p < 0.05 else 'FAIL'}")
    out.append("L10 side-by-side signs (audit's qo form, positions 6 and 11): " + ("; ".join(f"pos {p} group {g} {a}" for p, g, a in qo) or "not reconciled"))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/f61qo_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    if sys.argv[1] == "expected":
        for e in expected(): print("\t".join(map(str, e)))
    else: score(sys.argv[2])
