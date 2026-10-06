"""R13-UNTOP: map each blind pass's free-text SIGN descriptions to one class label (worker's mapping, written
after both passes returned, applied identically to both), keep opening-27 lines only (crop C=L1, A=L2, D=L3;
crop B is the opening-11 control), and write the line/pos/sign/conf/note schema tools/reconcile_passes.py reads."""
import csv, sys
CROP2LINE = {"C": "L1", "A": "L2", "D": "L3"}
RULES = [  # first keyword hit wins; order matters
    ("theta", "TH"), ("phi", "PHI"), ("delta", "DLT"), ("diaeresis", "YD"), ("lambda", "LAM"),
    ("reversed c", "REVC"), ("c with inner dot", "C"), ("reversed 3", "EPS"), ("epsilon", "EPS"),
    ("c/d", "CDH"), ("a-like", "ATAIL"), ("long-s/h", "SH"), ("r-like", "RBAR"), ("7-like", "Z7T"), ("z", "ZH"), ("7", "ZH"),
]
def norm(s):
    if not s.startswith("SIGN:"):
        return s
    d = s[5:].lower()
    for k, v in RULES:
        if k in d:
            return v
    return "UNK"
src, out = sys.argv[1], sys.argv[2]
rows = [r for r in csv.DictReader(open(src), delimiter="\t") if r["line"] in CROP2LINE]
with open(out, "w") as f:
    f.write("line\tpos\tsign\tconf\tnote\n")
    for r in rows:
        f.write(f"{CROP2LINE[r['line']]}\t{r['pos']}\t{norm(r['sign'])}\t{r['conf']}\t{r['sign'][:60]}\n")
