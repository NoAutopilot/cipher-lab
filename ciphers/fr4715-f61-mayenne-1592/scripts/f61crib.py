#!/usr/bin/env python3
"""F61-CRIB (campaign step H1, 27 Sept 2026): class-to-letter map from the reader's own shape notes.

Uses read_call_A.tsv's 'marks' column only (never its S0x table-drawing labels, which F61-CAL found wrong for 8 of
10 classes). Each sign is put in a shape class by the string rules in CLASS_RULES (written before any score was
looked at). The map class -> letters is FIT by tools/interlinear_align.py (--code-prefix mode: every class is a
code taking 0 or 1 letters of Tomokiyo's markup with the dashes removed; hard-EM DP, 6 iterations) on four of
Tomokiyo's five spans (S4a/S4b are one span, L07+L08), and SCORED on the withheld fifth by the F61-CAL DP
(align() copied from scripts/f61cal.py: markup chars vs value sets, match +1, mismatch 0, gap -1). A class's value
set is its top-2 letters by count (the Mayenne table pairs two letters per symbol); a class never seen under a
letter is a null and matches nothing. Leave-one-span-out over all five spans, pooled over the 55 letters.

Controls: 20 shuffled class-maps, seed 1 -- for each fold the fitted value sets are permuted across the classes
(same set sizes, same coverage), so the k-th control is pooled across folds the same way the target is.
Gate (H1, CAMPAIGN.md): pooled held-out match above every one of the 20 pooled shuffled-map values. The F61-CAL
absolute level (0.85) is printed beside it, not gated on here.

  python3 scripts/f61crib.py [--check]     (from the target folder; --check exits 1 if f61crib_result.txt is stale)
Writes scripts/f61crib_result.txt and scripts/f61crib_map.tsv (the map fitted on all five spans, for H4).
"""
import csv, os, random, re, subprocess, sys, tempfile
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(f"{HERE}/../../..")
TOOL = f"{ROOT}/tools/interlinear_align.py"

# (regex on the lowercased marks text, class). First rule that matches wins. Written from the marks column's own
# wording before scoring; 'run-break' and confidence are ignored.
CLASS_RULES = [
    (r"phi", "PHI"),                          # 'phi: loops on long stem', 'phi-like loop on stem, cut' (partial)
    (r"loop on stem with bar at foot", "LOOPBAR"),
    (r"double loop on stem", "DBL"),
    (r"dark e-loop", "ELOOP"),
    (r"^loop on long stem", "LOOPSTEM1"),     # L05/1: the reader did not call it phi -- kept apart
    (r"43-shape", "C43"),
    (r"6-shape", "C6"),
    (r"a-shape", "CA"),
    (r"h-shape", "CH"),
    (r"ll-shape", "LL"),
    (r"4 over triangle", "4TRI"),
    (r"4 over pi", "4PI"),
    (r"4 with long crossed stem", "4STEM"),
    (r"dense crossed 4", "HASH4"),
    (r"\bv\b|v/triangle", "VBAR"),            # 'V with bar', 'heavy V with bar', 'V/triangle with bar', 'V/triangle'
    (r"infinity", "INF"),
    (r"7/z hook", "ZHOOK"),
    (r"e-like bracket", "EBR"),
    (r"beta", "BETA"),
    (r"cross", "CROSS"),                      # 'cross, stroke rising to upper right', 'plus/cross'
]
def classify(marks):
    m = marks.lower()
    for pat, cls in CLASS_RULES:
        if re.search(pat, m): return cls
    raise SystemExit(f"unclassified mark: {marks!r}")

def load_read(path=f"{HERE}/read_call_A.tsv"):
    lines = defaultdict(list)
    for r in csv.DictReader(open(path), delimiter="\t"):
        lines[r["line"]].append(classify(r["marks"]))
    return lines
def load_spans():
    out = []
    for l in open(f"{HERE}/tomokiyo_spans.tsv"):
        if l.startswith("#") or l.startswith("span\t"): continue
        s, line, markup, letters = l.rstrip("\n").split("\t")
        out.append((s, line, markup))
    return out
# five folds: S4a+S4b (L07, L08) are one span, Tomokiyo's 'jalousie au beau-pere'
FOLDS = [("S1",), ("S2",), ("S3",), ("S4a", "S4b"), ("S5",)]

def fit(train, lines, tag):
    """class -> Counter(letter) from tools/interlinear_align.py on the training spans."""
    d = tempfile.mkdtemp(prefix=f"f61crib_{tag}_")
    pairs = f"{d}/pairs.tsv"
    with open(pairs, "w") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["plain_line", "plain_raw", "cipher_line", "cipher_raw"])
        for s, line, markup in train:
            w.writerow([s, markup.replace("-", ""), line, " ".join("@" + c for c in lines[line])])
    out_a, out_k = f"{d}/align.tsv", f"{d}/key.tsv"
    subprocess.run([sys.executable, TOOL, "align", pairs, out_a, out_k, "--code-prefix", "@"],
                   check=True, capture_output=True)
    counts = defaultdict(Counter)
    for r in csv.DictReader(open(out_k), delimiter="\t"):
        if len(r["meaning"]) == 1: counts[r["value"]][r["meaning"]] += int(r["agree"])
        for o in filter(None, r["others"].split(",")):
            m, n = o.rsplit(":", 1)
            if len(m) == 1: counts[r["value"]][m] += int(n)
    return counts
def to_map(counts, cap=2):
    return {c: tuple(l for l, _ in sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))[:cap]) for c, cnt in counts.items()}

def align(markup, seq, key):
    """copied from scripts/f61cal.py (F61-CAL's DP), unchanged: local DP, match +1, mismatch 0, gap -1."""
    n, m = len(markup), len(seq)
    NEG = -10**9
    D = [[NEG] * (m + 1) for _ in range(n + 1)]; P = {}
    for j in range(m + 1): D[0][j] = 0
    for i in range(1, n + 1):
        D[i][0] = -i
        for j in range(1, m + 1):
            best, arg = D[i-1][j] - 1, ("gapM",)
            if D[i][j-1] - 1 > best: best, arg = D[i][j-1] - 1, ("gapS",)
            vs = key.get(seq[j-1], ())
            c = markup[i-1]
            sc = 1 if (c != "-" and c in vs) else 0
            if D[i-1][j-1] + sc > best: best, arg = D[i-1][j-1] + sc, ("m", sc)
            for w in vs:
                if len(w) > 1 and i >= len(w) and markup[i-len(w):i] == w and D[i-len(w)][j-1] + len(w) > best:
                    best, arg = D[i-len(w)][j-1] + len(w), ("w", len(w))
            D[i][j], P[i, j] = best, arg
    j = max(range(m + 1), key=lambda j: D[n][j])
    i, jj, matched, pairs = n, j, 0, []
    while i > 0:
        if jj == 0: i -= 1; continue
        a = P[i, jj]
        if a[0] == "gapM": i -= 1
        elif a[0] == "gapS": jj -= 1
        elif a[0] == "m": matched += a[1]; pairs.append((i-1, jj-1)); i -= 1; jj -= 1
        else: matched += a[1]; pairs.append((i-1, jj-1)); i -= a[1]; jj -= 1
    return matched, pairs[::-1]
def score(key, lines, spans):
    mat = tot = 0
    for s, line, markup in spans:
        mt, _ = align(markup, lines[line], key)
        mat += mt; tot += sum(1 for c in markup if c != "-")
    return mat, tot

def main():
    lines, spans = load_read(), load_spans()
    by = {s: (s, l, m) for s, l, m in spans}
    out = ["reader file: read_call_A.tsv (marks column only); fit: tools/interlinear_align.py --code-prefix; score: f61cal.py DP"]
    classes = Counter(c for l in lines.values() for c in l)
    out.append("classes (" + str(len(classes)) + "): " + " ".join(f"{c}:{n}" for c, n in classes.most_common()))
    rng = random.Random(1)
    NC = 20
    pooled = tot_all = 0; ctrl = [0] * NC; ctrl_tot = 0
    for held in FOLDS:
        train = [by[s] for s in by if s not in held]
        test = [by[s] for s in held]
        kmap = to_map(fit(train, lines, "".join(held)))
        mt, tot = score(kmap, lines, test)
        pooled += mt; tot_all += tot
        labs = sorted(kmap); vals = [kmap[l] for l in labs]
        cs = []
        for k in range(NC):
            v = list(vals); rng.shuffle(v)
            cm, _ = score(dict(zip(labs, v)), lines, test); ctrl[k] += cm; cs.append(cm)
        out.append(f"held-out {'+'.join(held)}\t{test[0][1]}{'+' + test[1][1] if len(test) > 1 else ''}\tmatched {mt}/{tot}"
                   f"\tshuffled max {max(cs)}/{tot} mean {sum(cs)/NC:.2f}\tmap {' '.join(l + '=' + ''.join(kmap[l]) for l in labs)}")
    out.append(f"POOLED held-out\t{pooled}/{tot_all} = {pooled/tot_all:.3f}  (F61-CAL level 0.85; F61-CAL's own 8/55 = 0.145)")
    pc = [c / tot_all for c in ctrl]
    out.append("controls (20 shuffled class-maps pooled across folds, seed 1): " + " ".join(f"{c:.3f}" for c in pc))
    out.append(f"control mean {sum(pc)/NC:.3f} max {max(pc):.3f}")
    out.append("GATE (H1: pooled above every shuffled-map value): " + ("PASS" if pooled / tot_all > max(pc) else "FAIL"))
    # sensitivity, non-gating: uncapped value sets (every letter seen under a class)
    p2 = 0
    for held in FOLDS:
        train = [by[s] for s in by if s not in held]; test = [by[s] for s in held]
        p2 += score(to_map(fit(train, lines, "u" + "".join(held)), cap=99), lines, test)[0]
    out.append(f"sensitivity (non-gating), uncapped sets: pooled held-out {p2}/{tot_all} = {p2/tot_all:.3f}")
    # the map fitted on all five spans, for H4 (grade M: from Tomokiyo's own 'Solution Incomplete' markup)
    full = fit(spans, lines, "all")
    with open(f"{HERE}/f61crib_map.tsv", "w") as f:
        f.write("# F61-CRIB map fitted on all five Tomokiyo spans (tools/interlinear_align.py --code-prefix), 27 Sept 2026.\n"
                "# value set = top-2 letters by count; a class absent here or with n=0 letters is a null under this map.\n"
                "class\tn_signs\tvalues\tcounts\n")
        for c, n in classes.most_common():
            cnt = full.get(c, Counter())
            f.write(f"{c}\t{n}\t{'/'.join(to_map({c: cnt})[c]) if cnt else '-'}\t{' '.join(f'{l}:{k}' for l, k in cnt.most_common())}\n")
    out.append("map on all five spans -> scripts/f61crib_map.tsv")
    txt = "\n".join(out) + "\n"
    res = f"{HERE}/f61crib_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt
        print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
main()
