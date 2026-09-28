#!/usr/bin/env python3
"""H42: check that each blind reading tiles its text exactly, then score it: letter-units in words read unchanged
(kept, >=2 letters), in emended/cont words, and unread; edits (supplied [x], dropped {x}, changed {x>y}); and a
per-word grade (H if kept and every letter H, M if kept with any M, I if any edit -- rule 4). Writes
reading_words.tsv from the REAL text's output (B, passes/h42_blind_map.json). Exit 1 if a tiling fails."""
import csv, json, re, sys
from pathlib import Path
D = Path(__file__).resolve().parent.parent
def units(s):  # 'que' and '?' are one unit each
    return re.findall(r"que|\?|[a-z]", s)
def load_text(name):
    L = {}
    for ln in open(D / f"passes/h42_text_{name}.txt"):
        lab, body = ln.rstrip("\n").split("\t")
        if lab.endswith("grades"): L[lab[:-7]]["g"] = body.split()
        else: L[lab] = {"u": body.split()}
    return L
def score(label, name, write=None):
    T = load_text(name); rows = list(csv.DictReader(open(D / f"passes/h42_out_{label}.tsv"), delimiter="\t"))
    ok = True; pos = {k: 0 for k in T}; S = {"kept": 0, "emended": 0, "unread": 0, "edits": 0, "words_kept3": 0}
    out = []
    for r in rows:
        lab = r["line"]; u = units(r["span"]); i = pos[lab]
        if T[lab]["u"][i:i + len(u)] != u: print(f"{label}: tiling fault at {lab} unit {i}: {r['span']}"); ok = False
        g = T[lab]["g"][i:i + len(u)]; pos[lab] = i + len(u)
        edits = len(re.findall(r"\[[^\]]*\]|\{[^}]*\}", r["reading"]))
        k = r["kind"]
        if k == "unread": S["unread"] += len(u); grade = "-"
        elif edits == 0 and k in ("kept", "cont"):
            S["kept"] += len(u); grade = "H" if all(x == "H" for x in g) else "M"
            if len(u) >= 3: S["words_kept3"] += 1
        else: S["emended"] += len(u); S["edits"] += edits; grade = "I"
        out.append([lab, r["span"], r["reading"], k, grade, "".join(g), r["gloss"]])
    for lab in T:
        if pos[lab] != len(T[lab]["u"]): print(f"{label}: {lab} not fully tiled ({pos[lab]}/{len(T[lab]['u'])})"); ok = False
    tot = sum(len(T[k]["u"]) for k in T); S["units"] = tot
    S.update({f"{k}_share": round(S[k] / tot, 3) for k in ("kept", "emended", "unread")})
    if write:
        with open(write, "w") as f:
            f.write("# H42 (28 Sept 2026): word-segmented reading of the v6 decode (reading.txt) by one blind Opus call, scored by passes/h42_score.py.\n"
                    "# grade: H = word read unchanged from letters all graded H; M = unchanged but a letter graded M; I = inferred/repaired (any supplied, dropped or changed letter, rule 4); - = unread.\n"
                    "# Matched control: the same call on a shuffled-key decode (passes/h42_out_A.tsv). NOT verified; rule 10 wording.\n")
            f.write("line\tspan\treading\tkind\tgrade\tletter_grades\tgloss\n")
            for o in out: f.write("\t".join(o) + "\n")
    from collections import Counter
    S["word_grades"] = dict(Counter(o[4] for o in out if o[4] != "-"))
    return ok, S
m = json.load(open(D / "passes/h42_blind_map.json"))
res = {}
for lab in ("A", "B"):
    ok, S = score(lab, m[lab], write=(D / "reading_words.tsv") if m[lab] == "real" else None)
    res[m[lab]] = S; print(m[lab], lab, "tiling ok" if ok else "TILING FAULT", json.dumps(S))
    if not ok: sys.exit(1)
json.dump(res, open(D / "passes/h42_score.json", "w"), indent=1)
