#!/usr/bin/env python3
"""F61-BRACKET (campaign step H22, 28 Sept 2026): are the bracket signs two glyphs (the table's E for f/s and squared C for l/y)?

Pre-registered before the call (prompt in scripts/PROMPTS.md). Positions and labels are computed here from the files on
disk: on f.61 the EBR signs of passA_classes.tsv on the span lines (L03/15, L07/5, L11/3) and of read_call_U.tsv (L10/1);
on f.108 the EBR and OTHER (I-shape) signs of the reconciled pass108A/B draft on bands L02 and L03. The letter under each
sign is Tomokiyo's, placed by scripts/f61cal.py's DP with the joint cell map (scripts/f61joint.py's fit on both leaves);
a sign under a dash or outside the references (L10, f.108 L05/L07) is listed but never scored. Pairing: per sheet in
order, as scripts/f61vbar.py rule 1 (sheets B do not overlap); a sheet whose count differs from the expected count is
dropped. Statistic: best group-to-letter match over the labelled positions, letters f/s versus l/y (the two cells);
exact null over all arrangements of the labels, plus 200 permutations (seed 1). Gate (H22): observed above the
permutation p95 with exact p < 0.05.

  python3 scripts/f61bracket.py expected          (prints the expected bracket positions and labels, before the call)
  python3 scripts/f61bracket.py score read_call_BR.tsv [--check]
"""
import csv, itertools, os, random, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from f61crib import load_read, load_spans, fit, align
from f61crib3 import load_cells, cell_map, values, OPTS
from f61crib4 import split_lines
from f61joint import f108_lines
SHEETS = ["f61sheetB_L03", "f61sheetB_L07", "f61sheetB_L11", "f61sheetB_L10", "f108sheetB_L02", "f108sheetB_L03", "f108sheetB_L05", "f108sheetB_L07"]
CLS = ("EBR", "OTHER")

def expected():
    lines = split_lines(load_read()); lines.update(f108_lines())
    u = {}
    for r in csv.DictReader((l for l in open(f"{HERE}/read_call_U.tsv") if not l.startswith("#")), delimiter="\t"):
        u.setdefault(r["line"], []).append(r["sign"])
    lines["L10"] = u["L10"]
    spans = load_spans() + [(s, "F108_" + ("L02" if s == "T1" else "L03"), m) for s, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{HERE}/tomokiyo_spans_3983.tsv") if l[0] == "T")]
    cm = values(cell_map(fit(spans, lines, "bracket", OPTS, keep_dashes=True), load_cells()))
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
                L = letter.get((line, j), "-"); lab = "f/s" if L in "fs" else ("l/y" if L in "ly" else "-")
                out.append((sheet, j + 1, c, L, lab))
    return out
def stat(groups, labels):
    gs = sorted(set(groups)); best = 0
    for lets in itertools.product(["f/s", "l/y"], repeat=len(gs)):
        m = dict(zip(gs, lets)); best = max(best, sum(1 for g, l in zip(groups, labels) if m[g] == l))
    return best
def score(path):
    exp = expected(); by_sheet = defaultdict(list)
    for e in exp: by_sheet[e[0]].append(e)
    rows = list(csv.DictReader((l for l in open(f"{HERE}/{path}") if not l.startswith("#")), delimiter="\t"))
    got = defaultdict(list)
    for r in rows: got[r["sheet"].replace(".jpg", "")].append(r)
    out = [f"{path}: {len(rows)} bracket signs listed; expected {len(exp)} ({sum(1 for e in exp if e[4] != '-')} labelled)"]
    groups, labels = [], []
    for sheet in SHEETS:
        g = sorted(got.get(sheet, []), key=lambda r: (int(r["segment"]), float(r["x_px"]))); e = by_sheet.get(sheet, [])
        if len(g) != len(e):
            out.append(f"  {sheet}: expected {len(e)}, listed {len(g)} -> NOT reconciled, dropped"); continue
        for r, ex in zip(g, e):
            out.append(f"  {sheet}/{ex[1]} {ex[2]}: group {r['group']}, letter {ex[3]} ({ex[4]})")
            if ex[4] != "-": groups.append(r["group"]); labels.append(ex[4])
    n = len(labels)
    if n < 5: out.append(f"scored {n} < 5: NON-TEST")
    else:
        obs = stat(groups, labels); nf = labels.count("f/s")
        exact = [stat(groups, ["f/s" if i in c else "l/y" for i in range(n)]) for c in itertools.combinations(range(n), nf)]
        p = sum(1 for e in exact if e >= obs) / len(exact)
        rng = random.Random(1); perm = []
        for _ in range(200):
            l2 = list(labels); rng.shuffle(l2); perm.append(stat(groups, l2))
        perm.sort(); p95 = perm[int(0.95 * 200) - 1]
        out.append(f"scored {n} (f/s {nf}, l/y {n - nf}); groups {len(set(groups))}; observed {obs}/{n}; exact P(>=obs) = {p:.3f} over {len(exact)}; permutation p95 {p95}/{n}")
        out.append(f"GATE H22: {'PASS' if obs > p95 and p < 0.05 else 'FAIL'}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/f61bracket_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    if sys.argv[1] == "expected":
        for e in expected(): print("\t".join(map(str, e)))
    else: score(sys.argv[2])
