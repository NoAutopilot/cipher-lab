#!/usr/bin/env python3
"""VERIFY-F61-V4 step 5b: blind phrase control for the material OUTSIDE Tomokiyo's five spans (L01/7-12, L02, L03/1-3,
L04, L07/1-2, L10 -- as placed by twoway.py). Design fixed here before the call. 21 renderings in two-way form: the true
v4 sets (class -> set from family/f61_decode_period_v4_frac0.1_sbs.tsv) and 20 keys with those sets permuted across the
f.61 classes that carry one (seed 20260928); unread classes stay unread. Shuffled (seed 61), labelled R01..R21. One Opus
text call, no key, no hint which is true, asked for French words/phrases of >= 3 letters (a) with no choice inside a set
and (b) choosing one letter per set, each with confidence 1-3. Scoring (score): a word or phrase is RECOVERED only if the
reader gives it under the true rendering and gives the same string (as a substring of any listed item) in at most 1 of
the 20 permuted renderings; the true rendering's rank by the reader's own 'most French-like' order is also reported.
  python3 verify_v4/phrase_ctl.py build | score"""
import csv, os, random, re, sys
from collections import defaultdict
H = os.path.dirname(os.path.abspath(__file__)); F = os.path.abspath(f"{H}/../family"); OUT = f"{H}/phrase"
REG = {"L01": range(7, 13), "L02": range(1, 3), "L03": range(1, 4), "L04": range(1, 3), "L07": range(1, 3), "L10": range(1, 14)}
def load():
    d = defaultdict(list)
    for r in csv.DictReader(open(f"{F}/f61_decode_period_v4_frac0.1_sbs.tsv"), delimiter="\t"): d[r["line"]].append(r)
    return d
def render(d, cmap):
    out = []
    for line, rg in REG.items():
        toks = []
        for p in rg:
            c = d[line][p - 1]["class"]; s = cmap.get(c)
            toks.append("<?>" if not s else (s if "/" not in s else f"[{s}]"))
        out.append(f"{line}: " + " ".join(toks))
    return "\n".join(out)
def build():
    os.makedirs(OUT, exist_ok=True); d = load()
    cmap = {r["class"]: r["period_letters"] for rs in d.values() for r in rs if r["period_letters"] != "-"}
    labs = sorted(cmap); vals = [cmap[l] for l in labs]; rng = random.Random(20260928)
    rend = [("TRUE", render(d, cmap))]
    for k in range(20):
        v = list(vals); rng.shuffle(v); rend.append((f"P{k+1:02d}", render(d, dict(zip(labs, v)))))
    random.Random(61).shuffle(rend)
    with open(f"{OUT}/key.tsv", "w") as f:
        f.write("# answer key, never shown to the reader\nlabel\tsource\n")
        for i, (src, _) in enumerate(rend, 1): f.write(f"R{i:02d}\t{src}\n")
    body = "\n\n".join(f"== R{i:02d}\n{t}" for i, (_, t) in enumerate(rend, 1))
    open(f"{OUT}/renderings.txt", "w").write(body + "\n"); print(body[:600])
def score():
    key = {r["label"]: r["source"] for r in csv.DictReader((l for l in open(f"{OUT}/key.tsv") if not l.startswith("#")), delimiter="\t")}
    rows = list(csv.DictReader((l for l in open(f"{OUT}/read.tsv") if not l.startswith("#")), delimiter="\t"))
    true = [l for l, s in key.items() if s == "TRUE"][0]
    items = defaultdict(list)
    for r in rows: items[r["label"]].append((r["mode"], r["item"].strip().lower(), r["conf"]))
    norm = lambda s: re.sub(r"[^a-z]", "", s)
    out = [f"true rendering = {true}; reader listed items per rendering: " + " ".join(f"{l}:{len(items.get(l, []))}" for l in sorted(key))]
    for mode, it, conf in items.get(true, []):
        n = sum(1 for l in key if l != true and any(norm(it) in norm(x) or norm(x) == norm(it) for _, x, _ in items.get(l, [])))
        out.append(f"  TRUE item ({mode}, conf {conf}) '{it}': found in {n}/20 permuted renderings -> {'RECOVERED' if n <= 1 else 'not recovered'}")
    # rule-power control (added after the call, before the verdict): apply the same RECOVERED rule to each permuted
    # rendering as if it were the true one; a rule that passes most permuted renderings too has no power here.
    per = {}
    for lab in key:
        its = items.get(lab, []); rec = 0; best = 0
        for mode, it, conf in its:
            n = sum(1 for l in key if l != lab and any(norm(it) in norm(x) or norm(x) == norm(it) for _, x, _ in items.get(l, [])))
            if n <= 1: rec += 1; best = max(best, int(conf) if conf.isdigit() else 0)
        per[lab] = (rec, best)
    pr = [per[l] for l in key if l != true]
    out.append(f"rule-power control: true {true} 'recovered' {per[true][0]} (best conf {per[true][1]}); the 20 permuted renderings under the same rule: recovered " + " ".join(str(r) for r, _ in pr) + f" (mean {sum(r for r, _ in pr)/20:.1f}; {sum(1 for r, _ in pr if r >= per[true][0])}/20 at or above true); permuted renderings with a conf-3 item passing the rule: {sum(1 for _, b in pr if b == 3)}/20")
    rk = [r for r in rows if r["mode"] == "rank"]
    if rk: order = rk[0]["item"].split(); out.append(f"reader's French-likeness ranking: true at {order.index(true) + 1 if true in order else 'absent'} of {len(order)}")
    out.append(f"items with no choice (mode a) under true: {sum(1 for m, _, _ in items.get(true, []) if m == 'a')}; under the 20 permuted: {sum(1 for l in key if l != true for m, _, _ in items.get(l, []) if m == 'a')}")
    txt = "\n".join(out) + "\n"; open(f"{H}/phrase_result.txt", "w").write(txt); print(txt, end="")
{"build": build, "score": score}[sys.argv[1]]()
