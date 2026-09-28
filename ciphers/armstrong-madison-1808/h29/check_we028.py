#!/usr/bin/env python3
"""H29: merge the four blind page reads of Erving to Monroe, Madrid 5 Feb 1806 (LOC Monroe Papers reel 3 frames
0741-0743, h29/reads/*.tsv: crop, pos, group, gloss, conf, note) into one group stream in reading order, check every
glossed group against tools/data/uscodes-1800/WE028.tsv, and print the signature numbers. Writes h29/erving_groups.tsv
(frame, crop, pos, group, gloss, we028, match) and h29/summary.txt. A gloss matches when, after folding, it equals the
table's plaintext, or is a prefix/suffix of it or it of the gloss (the letter's hand writes syllables and clips words).
usage: check_we028.py [--reads DIR]"""
import os, re, sys, json
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
ORDER = ["f0741R", "f0742L", "f0742R", "f0743L"]
fold = lambda s: re.sub(r"[^a-z]", "", s.lower().replace("&", "and"))
we = {}
for line in open(os.path.join(ROOT, "tools/data/uscodes-1800/WE028.tsv"), encoding="utf-8"):
    p = line.rstrip("\n").split("\t")
    if p[0].isdigit():
        we[int(p[0])] = p[1]
rows = []
for fr in ORDER:
    f = os.path.join(HERE, "reads", fr + ".tsv")
    if not os.path.exists(f):
        print("missing", f); continue
    for line in open(f, encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        if len(p) < 4 or p[0] == "crop" or p[0].startswith("#"):
            continue
        crop, pos, group, gloss = p[0], p[1], p[2].strip().rstrip("."), p[3].strip()
        if group.upper() == "NONE" or not group:
            continue
        rows.append({"frame": fr, "crop": int(re.sub(r"\D", "", crop) or 0), "pos": pos, "group": group, "gloss": gloss,
                     "conf": p[4] if len(p) > 4 else "", "note": p[5] if len(p) > 5 else ""})
# fixed-pitch bands can straddle one line twice (0743L crops 13/14, the reader's own flag): a crop whose group
# sequence equals the previous crop's on the same page is dropped as a duplicate band
dedup, dropped = [], []
for r in rows:
    prev = [x for x in dedup if x["frame"] == r["frame"] and x["crop"] == r["crop"] - 1]
    same = [x for x in dedup if x["frame"] == r["frame"] and x["crop"] == r["crop"]]
    if prev and not same:
        cur = [x["group"] for x in rows if x["frame"] == r["frame"] and x["crop"] == r["crop"]]
        if cur == [x["group"] for x in prev] and len(cur) >= 2:
            if (r["frame"], r["crop"], len(cur)) not in dropped:
                dropped.append((r["frame"], r["crop"], len(cur)))
            continue
    if any(d[0] == r["frame"] and d[1] == r["crop"] for d in dropped):
        continue
    dedup.append(r)
rows = dedup


def match(gloss, plain):
    g, t = fold(gloss), fold(plain)
    if not g or g == "-":
        return "nogloss"
    if g == t:
        return "exact"
    if len(g) >= 3 and (t.startswith(g) or g.startswith(t) or t.endswith(g)):
        return "partial"
    return "miss"
out = []
for r in rows:
    g = r["group"]
    v = int(g) if g.isdigit() else None
    plain = we.get(v, "") if v is not None else ""
    m = ("unread" if v is None else "notintable" if v not in we else match(r["gloss"], plain))
    out.append({**r, "we028": plain, "match": m})
with open(os.path.join(HERE, "erving_groups.tsv"), "w") as fh:
    fh.write("frame\tcrop\tpos\tgroup\tgloss\tconf\twe028\tmatch\tnote\n")
    for r in out:
        fh.write("\t".join(str(r[k]) for k in ("frame", "crop", "pos", "group", "gloss", "conf", "we028", "match", "note")) + "\n")
# a miss whose gloss matches the WE028 entry of the neighbouring group (the interline word sits between two groups in
# dense lines) is a one-group shift of the gloss assignment, not a value mismatch: counted separately
for i, r in enumerate(out):
    if r["match"] != "miss":
        continue
    for j in (i - 1, i + 1):
        if 0 <= j < len(out) and out[j]["frame"] == r["frame"] and out[j]["we028"] and match(r["gloss"], out[j]["we028"]) in ("exact", "partial"):
            r["match"] = "shifted"; break
c = Counter(r["match"] for r in out)
toks = [int(r["group"]) for r in out if r["group"].isdigit()]
hi = [v for v in toks if v >= 100]
u = Counter(v % 10 for v in hi)
lines = [f"duplicate bands dropped: {dropped}", f"groups read {len(out)} (per frame: " + ", ".join(f"{fr} {sum(1 for r in out if r['frame']==fr)}" for fr in ORDER) + ")",
         f"digits clean {len(toks)}, unread digit {c['unread']}, value not in WE028 (>1596 or 0) {c['notintable']}",
         f"glossed {sum(1 for r in out if r['match'] in ('exact','partial','miss','shifted'))}: exact {c['exact']}, partial {c['partial']}, shifted to a neighbour {c['shifted']}, miss {c['miss']}; no gloss {c['nogloss']}",
         f"distinct values {len(set(toks))}, values >= 100: {len(hi)} tokens, units 0/1 share {(u[0]+u[1])/max(1,len(hi)):.3f}, units 2/3/5/9 share {(u[2]+u[3]+u[5]+u[9])/max(1,len(hi)):.3f}, max value {max(toks) if toks else 0}",
         f"top values: " + ", ".join(f"{v}x{n}" for v, n in Counter(toks).most_common(12))]
# the same stream through design/design_stats.py's stats() (the target and the four THE=972 letters use it)
sys.path.insert(0, os.path.join(HERE, "..", "design"))
import random
try:
    import design_stats as ds
    st = ds.stats(toks, random.Random(7), 1600)
    lines.append("design_stats: " + " ".join(f"{k}={ds.fmt(v)}" for k, v in st.items()))
    with open(os.path.join(HERE, "..", "design", "real_extra.tsv"), "w") as fh:
        fh.write("dataset\ttokens\n" + "REAL WE028 usage erving-monroe_1806-02-05\t" + " ".join(map(str, toks)) + "\n")
except Exception as e:
    lines.append(f"design_stats: not computed ({e})")
open(os.path.join(HERE, "summary.txt"), "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
misses = [r for r in out if r["match"] == "miss"]
print("misses (group gloss | WE028):", "; ".join(f"{r['group']} {r['gloss']} | {r['we028']}" for r in misses[:40]))
