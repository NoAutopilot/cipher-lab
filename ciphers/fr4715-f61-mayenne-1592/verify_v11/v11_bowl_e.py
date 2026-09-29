#!/usr/bin/env python3
"""VERIFY-F61-V11 addendum E (PREREG.md E): letter-stratified supplementary bowl read on f.101r, same tile/prompt/anchor/repeat design as v11_bowl.py.
  python3 v11_bowl_e.py tiles SCRATCH | score [--check]"""
import os, random, string, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import v11_bowl as B, v11_crosstab as X
def plan():
    done = {(r["line"], r["pos_or_seg"]) for r in B.rd(f"{HERE}/v11_items.tsv") if r["leaf"] == "f101r"}
    lm = X.letter_map("f101r"); pool = [t for t in B.pool("f101r", 80) if (t[1], t[2]) not in done and (t[1], t[2]) in lm]
    rng = random.Random(1115); pick = []
    for want in ("c/p/t", "a/n"):
        cand = [t for t in pool if X.cls(lm[(t[1], t[2])][0]) == want]; rng.shuffle(cand)
        cand.sort(key=lambda t: not lm[(t[1], t[2])][2]); pick += cand[:20]
    rng.shuffle(pick)
    anc = [r for r in B.rd(f"{B.FAM}/h193_items.tsv") if r["group"] in ("CP", "AN")]; cp = [a for a in anc if a["group"] == "CP"]; an = [a for a in anc if a["group"] == "AN"]
    return {"c4": (pick[:20], pick[:6], cp[1:6] + an[1:6]), "c5": (pick[20:], pick[20:26], cp[4:9] + an[4:9])}
def tiles(scratch):
    from PIL import Image
    calls = plan(); nat = {"f101r": Image.open(f"{B.FAM}/images/3982_f101r.jpg").convert("RGB")}
    used = {r["id"] for r in B.rd(f"{HERE}/v11_items.tsv")}; rid = random.Random(1116); key = ["call\tid\trole\tleaf\tline\tpos_or_seg\tx\tgroup\trepeat_of"]
    def nid():
        while True:
            s = "".join(rid.choice(string.ascii_uppercase) for _ in range(3))
            if s not in used: used.add(s); return s
    for c, (tg, rep, an) in calls.items():
        items = [("T", t, "") for t in tg] + [("R", t, "") for t in rep] + [("A", a, a["group"]) for a in an]; random.Random(1114 + int(c[1:])).shuffle(items)
        ims = []; first = {}
        for role, it, grp in items:
            i = nid()
            if role == "A":
                im = Image.open(f"{scratch}/f176v/f176v_{it['line']}_{it['segment']}.jpg").convert("RGB"); x = max(110, min(im.width - 110, int(it["x_px"])))
                cv, d = B.tile(im, x, 0, im.height); key.append(f"{c}\t{i}\tanchor\t176v\t{it['line']}\t{it['segment']}\t{it['x_px']}\t{grp}\t")
            else:
                leaf, line, pos, x, yc = it; cv, d = B.tile(nat[leaf], x, yc - 75, yc + 60); k = (leaf, line, pos)
                rep_of = first.get(k, "") if k in first else ""
                if k not in first: first[k] = i
                key.append(f"{c}\t{i}\ttarget\t{leaf}\t{line}\t{pos}\t{x}\t\t{rep_of}")
            d.text((8, 6), i, fill=(0, 0, 0)); ims.append(cv)
        os.makedirs(f"{scratch}/{c}", exist_ok=True)
        for s in range(0, len(ims), 12):
            sh = Image.new("RGB", (4 * 360, 3 * 262), "white")
            for j, cv in enumerate(ims[s:s + 12]): sh.paste(cv, ((j % 4) * 360, (j // 4) * 262))
            sh.save(f"{scratch}/{c}/sheet_{s // 12 + 1:02d}.jpg", quality=90)
    open(f"{HERE}/v11e_items.tsv", "w").write("\n".join(key) + "\n"); print("items", len(key) - 1)
def score():
    out = []; mine = {}
    for items_f, calls in ((f"{HERE}/v11_items.tsv", ("c1", "c2")), (f"{HERE}/v11e_items.tsv", ("c4", "c5"))):
        items = B.rd(items_f)
        for c in calls:
            ans = {r["id"]: r["answer"].strip().lower() for r in B.rd(f"{HERE}/v11_reply_{c}.tsv")}; its = [r for r in items if r["call"] == c]
            anc = [r for r in its if r["role"] == "anchor"]; ah = sum((ans.get(r["id"]) == "yes") == (r["group"] == "CP") and ans.get(r["id"]) in ("yes", "no") for r in anc)
            reps = [r for r in its if r["repeat_of"]]; rh = sum(ans.get(r["id"]) == ans.get(r["repeat_of"]) for r in reps); ok = ah >= 8 and rh >= 5
            if c in ("c4", "c5"): out.append(f"{c}: anchors {ah}/{len(anc)}; repeats {rh}/{len(reps)} -> {'PASS' if ok else 'FAIL (answers not used)'}")
            if ok:
                for r in its:
                    if r["role"] == "target" and not r["repeat_of"]: mine[(c, r["line"], r["pos_or_seg"])] = ans.get(r["id"], "missing")
    lm = X.letter_map("f101r")
    for nm, sel in (("E alone (c4+c5)", ("c4", "c5")), ("pooled B+E (c1,c2,c4,c5)", ("c1", "c2", "c4", "c5"))):
        pairs = [(b, X.cls(lm[(l, p)][0])) for (c, l, p), b in mine.items() if c in sel and (l, p) in lm]
        r = X.test(pairs, perms=10000)
        ro = "n < 20" if r is None or r["n"] < 20 else "tracks" if r["share"] >= 0.75 and r["p"] < 0.01 else "does not track" if r["share"] < 0.6 or r["p"] > 0.05 else "unclear"
        out.append(X.fmt(nm, r).split(" -> ")[0] + f" -> {ro}")
    run = X.runner_labels(); sh = [(b, run[(l, p)]) for (c, l, p), b in mine.items() if c in ("c4", "c5") and (l, p) in run and b in ("yes", "no") and run[(l, p)] in ("yes", "no")]
    if sh:
        n = len(sh); po = sum(a == b for a, b in sh) / n; pa = sum(a == "yes" for a, _ in sh) / n; pb = sum(b == "yes" for _, b in sh) / n; pe = pa * pb + (1 - pa) * (1 - pb)
        out.append(f"E my vs runner's labels on {n}: agreement {po:.2f}, kappa {(po - pe) / (1 - pe):.2f}")
        pairs = [(b, X.cls(lm[(l, p)][0])) for (c, l, p), b in mine.items() if c in ("c4", "c5") and (l, p) in lm]
        rp = [(run[(l, p)], X.cls(lm[(l, p)][0])) for (c, l, p), b in mine.items() if c in ("c4", "c5") and (l, p) in lm and (l, p) in run]
        out.append(X.fmt("runner's labels on the same E tokens", X.test(rp)).split(" -> ")[0])
    txt = "\n".join(out) + "\n"; res = f"{HERE}/v11_bowl_e_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(sys.argv[2]) if sys.argv[1] == "tiles" else score()
