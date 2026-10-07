#!/usr/bin/env python3
"""AM-D1411P5 post-hoc (seen after the pre-registered score; licenses nothing on its own): (1) p.5 left page repeats the
cipher text of p.2 (def1411/numbers.tsv): align the two number sequences (difflib, blocks >= 4) and count agreement in the
aligned span, an independent-copy check of both transcriptions; (2) coverage of the p.5 left (copy) and right (not a copy)
pages separately under T21r and T21r_h12, each against 200 shuffles (seed 1411), descriptive only.
  python3 d1411p5/posthoc_copy.py   -> prints; writes d1411p5/posthoc_copy.json"""
import csv, difflib, json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import score_p5 as S  # noqa: E402
J = S.J
def load(p):
    out = []
    for r in csv.DictReader(open(os.path.join(HERE, "..", p)), delimiter="\t"):
        t = r["token"].rstrip("?")
        if t.isdigit() and "intext" not in (r.get("note") or ""):
            out.append((r["line"], int(t), r["grade"]))
    return out
p2, p5 = load("def1411/numbers.tsv"), load("d1411p5/numbers.tsv")
L = [x for x in p5 if x[0].startswith("p5L")]; R = [x for x in p5 if x[0].startswith("p5R")]
sm = difflib.SequenceMatcher(None, [x[1] for x in p2], [x[1] for x in L], autojunk=False)
ops = sm.get_opcodes(); blocks = [b for b in sm.get_matching_blocks() if b.size >= 4]
a0, a1 = blocks[0].a, blocks[-1].a + blocks[-1].size; b0, b1 = blocks[0].b, blocks[-1].b + blocks[-1].size
span = [o for o in ops if o[1] >= a0 and o[2] <= a1 and o[3] >= b0 and o[4] <= b1]
eq = sum(o[2] - o[1] for o in span if o[0] == "equal"); rep = [o for o in span if o[0] == "replace"]
res = {"p2_n": len(p2), "p5L_n": len(L), "p5R_n": len(R), "aligned_span_p2": [p2[a0][0], p2[a1 - 1][0], a1 - a0],
       "aligned_span_p5L": [L[b0][0], L[b1 - 1][0], b1 - b0], "equal_tokens": eq,
       "replace_ops": [[p2[o[1]][0], [x[1] for x in p2[o[1]:o[2]]], L[o[3]][0], [x[1] for x in L[o[3]:o[4]]]] for o in rep],
       "insert_delete": [[o[0], o[2] - o[1], o[4] - o[3]] for o in span if o[0] in ("insert", "delete")]}
T = S.tabs()
S_model = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA["de1600"]])
def cover(nums, t):
    return S_model.cover(S.dec(nums, t))
res["by_page"] = {}
if S_model is not None:
    for nm, part in (("p5L", L), ("p5R", R)):
        nums = [x[1] for x in part]; d = {}
        for k in ("T21r", "T21r_h12"):
            real = cover(nums, T[k]); rnd = random.Random(S.SEED); ctl = []
            for _ in range(200):
                q = nums[:]; rnd.shuffle(q); ctl.append(cover(q, T[k]))
            d[k] = {"cover": round(real, 4), "shuffled_p99": round(J.pct(sorted(ctl), .99), 4)}
        res["by_page"][nm] = d
json.dump(res, open(os.path.join(HERE, "posthoc_copy.json"), "w"), indent=1)
print(json.dumps(res, indent=1))
