"""NZ-UNT27: map each blind pass's free-text SIGN descriptions to one class label (worker's mapping, written after both
passes returned, applied identically to both); keep tablet/scroll lines only (crop C=S1, A=S2, F=S3 scroll; B=T1, G=T2,
E=T3 tablet, read with the tablet rotated 90 deg counter-clockwise); crop D is the opening-11 control. Writes the
line/pos/sign/conf/note schema tools/reconcile_passes.py reads. The underline dash (scroll S2) is dropped as not a sign."""
import csv, sys
CROP2LINE = {"C": "S1", "A": "S2", "F": "S3", "B": "T1", "G": "T2", "E": "T3"}
RULES = [  # first keyword hit wins; order matters
    ("underline", None), ("omega", "EPS"), ("epsilon", "EPS"), ("3 reversed", "EPS"), ("reversed 3", "EPS"),
    ("6", "SIX"), ("open c", "c"), ("c open", "c"), ("+", "PLUS"), ("cross/x", "XST"), ("x/cross", "XST"),
    ("x with long", "XST"), ("x-like curled", "XC"), ("x/z", "XC"), ("z", "Z"), ("n/a", "VN"), ("v/n", "VN"),
    ("y", "Y"), ("7", "SEVH"), ("r with", "RH"), ("r-like", "RH"), ("t-like", "TH"), ("t/h", "TH"),
    ("t-like with sloping", "T"), ("circle", "o"), ("o-like", "o"), ("ff", "FF"), ("n-like", "NH"),
    ("d with looped", "DL"), ("d-like, tall stem", "DL"), ("tall d-like", "DH"), ("g-like", "G"),
    ("long s", "LS"), ("tall s", "SH"), ("s with hooked", "SH"), ("e/s", "ES"), ("e-like loop", "ELP"),
    ("e/p", "ELP"), ("l/p", "LP"), ("p-like", "LP"), ("e-like", "e"), ("u/s", "u"), ("l-like", "l"), ("n", "N"),
]
def norm(s):
    if not s.startswith("SIGN:"):
        return "PLUS" if s == "+" else s
    d = s[5:].lower()
    if d.startswith("t-like with sloping"):
        return "T"
    for k, v in RULES:
        if k in d:
            return v
    return "UNK"
src, out = sys.argv[1], sys.argv[2]
rows = [r for r in csv.DictReader(open(src), delimiter="\t") if r["line"] in CROP2LINE]
with open(out, "w") as f:
    f.write("line\tpos\tsign\tconf\tnote\n")
    n = {}
    for r in sorted(rows, key=lambda r: (list(CROP2LINE).index(r["line"]), int(r["pos"]))):
        lab = norm(r["sign"])
        if lab is None:
            continue
        L = CROP2LINE[r["line"]]; n[L] = n.get(L, 0) + 1
        f.write(f"{L}\t{n[L]}\t{lab}\t{r['conf']}\t{r['sign'][:60]}\n")
