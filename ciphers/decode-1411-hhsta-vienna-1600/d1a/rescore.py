#!/usr/bin/env python3
"""D1A-D1411 descriptive re-score (PREREG-D1A-D1411.md; in-sample for T21r, no grades move): coverage of def1411's p.2 numbers
+ the p.5 copy span (d1411p5/posthoc_copy.py alignment span p5L_L11_b-L31_a) under T21r and T21r_h12, as transcribed vs with the
S1/S2 values of d1a/settled.tsv substituted, each against 200 order shuffles (seed 1411) p99. The copy span is scored on both
copies (it is one text twice), as the brief asks for "p.2+p.5".
  python3 d1a/rescore.py [--check]   writes/compares d1a/rescore.json"""
import csv, difflib, json, os, random, sys
H = os.path.dirname(os.path.abspath(__file__)); P5 = os.path.join(H, "..", "d1411p5")
sys.path.insert(0, P5)
import score_p5 as S  # noqa: E402
J = S.J
def load(p):
    out = []
    for r in csv.DictReader(open(os.path.join(H, "..", p)), delimiter="\t"):
        t = r["token"].rstrip("?")
        if t.isdigit() and "intext" not in (r.get("note") or ""):
            out.append([r["line"], r["pos"], int(t)])
    return out
p2, p5 = load("def1411/numbers.tsv"), load("d1411p5/numbers.tsv")
L = [x for x in p5 if x[0].startswith("p5L")]
sm = difflib.SequenceMatcher(None, [x[2] for x in p2], [x[2] for x in L], autojunk=False)
bl = [b for b in sm.get_matching_blocks() if b.size >= 4]
copy = L[bl[0].b: bl[-1].b + bl[-1].size]
sett = [r for r in csv.DictReader([l for l in open(os.path.join(H, "settled.tsv")) if not l.startswith("#")], delimiter="\t")
        if r["class"] in ("S1", "S2")]
def settled(seq, cp):
    out = [x[:] for x in seq]
    for r in sett:
        for x in out:
            if x[0] == r[cp + "_line"] and x[1] == r[cp + "_pos"]: x[2] = int(r["settled"])
    return out
M = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA["de1600"]]); T = S.tabs(); res = {"n_settled_ops": len(sett)}
for nm, a, b in (("as_transcribed", p2, copy), ("settled", settled(p2, "p2"), settled(copy, "p5"))):
    nums = [x[2] for x in a] + [x[2] for x in b]; d = {"N": len(nums)}
    for k in ("T21r", "T21r_h12"):
        real = M.cover(S.dec(nums, T[k])); rnd = random.Random(S.SEED); ctl = []
        for _ in range(200):
            q = nums[:]; rnd.shuffle(q); ctl.append(M.cover(S.dec(q, T[k])))
        d[k] = {"cover": round(real, 4), "shuffled_p99": round(J.pct(sorted(ctl), .99), 4)}
    res[nm] = d
txt = json.dumps(res, indent=1) + "\n"; out = os.path.join(H, "rescore.json")
if "--check" in sys.argv:
    sys.exit(0 if open(out).read() == txt else (print("STALE rescore.json") or 1))
open(out, "w").write(txt); print(txt)
