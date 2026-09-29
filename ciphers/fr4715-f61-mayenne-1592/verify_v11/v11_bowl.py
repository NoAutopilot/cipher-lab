#!/usr/bin/env python3
"""VERIFY-F61-V11 part B (29 Sept 2026, written before the calls): fresh stem-foot bowl reads on fr.3982 f.101r and f.124r 4TRI tokens, tiles cut
by this verifier from the Gallica natives (btv1b9060543f f210 / f256; fr.3984 btv1b9060633d f328 for anchors, bands regenerated with cut_bands.py
per sheets/f176v_full/README.md), own tile format and own prompt (PREREG.md B). Anchors: h193_items.tsv CP/AN coordinates on f.176v (Desportes's hand,
known answer = period letter group). Pools: f.101r agreed 4TRI (recf101r draft, f101r_signsA geometry, as h365's pool incl. the H362 items);
f.124r agreed 4TRI (recf124r, f124r_signsA, f124r_drop excluded).
  python3 v11_bowl.py tiles SCRATCH      -> SCRATCH/cK/sheet_NN.jpg, v11_items.tsv
  python3 v11_bowl.py score [--check]    -> v11_bowl_result.txt (needs replies v11_reply_cK.tsv: id<TAB>answer)"""
import csv, json, os, random, string, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); FAM = f"{HERE}/../family"; P = f"{FAM}/passes"
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def pool(leaf, dy, drop_file=None):
    drop = {(r["line"], r["segment"]) for r in rd(f"{P}/{drop_file}")} if drop_file else set()
    A = {(r["line"], r["pos"]): r for r in rd(f"{P}/{leaf}_signsA.tsv")}; B = json.load(open(f"{FAM}/sheets/{leaf}_bands.json"))["boxes"]; out = []
    for r in rd(f"{P}/rec{leaf}/ciphertext_draft.tsv"):
        if r["sign"] != "4TRI" or not r["why"].startswith("agree"): continue
        a = A.get((r["line"], r["position"]))
        if not a or a["sign"] != "4TRI" or (a["line"], a["segment"]) in drop: continue
        bx = B[f"{leaf}_{a['line']}_{a['segment']}.jpg"]; out.append((leaf, r["line"], r["position"], bx[0] + int(float(a["x_px"])) // 2, bx[1] + dy))
    return out
def plan():
    t1 = pool("f101r", 80); t2 = pool("f124r", 70, "f124r_drop.tsv")
    r1 = random.Random(1111); r2 = random.Random(1112); T = r1.sample(t1, 40); U = r2.sample(t2, 24)
    anc = [r for r in rd(f"{FAM}/h193_items.tsv") if r["group"] in ("CP", "AN")]; cp = [a for a in anc if a["group"] == "CP"]; an = [a for a in anc if a["group"] == "AN"]
    calls = {"c1": (T[:20], T[:6], cp[:5] + an[:5]), "c2": (T[20:40], T[20:26], cp[5:] + an[5:]), "c3": (U, U[:6], cp[2:7] + an[2:7])}
    return calls, len(t1), len(t2)
def tile(img, x, y0, y1, w=110, sc=1.6):
    from PIL import Image, ImageDraw
    t = img.crop((x - w, y0, x + w, y1)); t = t.resize((int(t.width * sc), int(t.height * sc)))
    c = Image.new("RGB", (360, 262), "white"); c.paste(t.crop((0, 0, 352, min(t.height, 222))), (4, 36)); d = ImageDraw.Draw(c)
    mx = 4 + int(w * sc); d.polygon([(mx - 8, 16), (mx + 8, 16), (mx, 32)], fill=(0, 60, 220)); d.rectangle((0, 0, 359, 261), outline=(160, 160, 160))
    return c, d
def tiles(scratch):
    from PIL import Image, ImageDraw
    calls, n1, n2 = plan(); nat = {"f101r": Image.open(f"{FAM}/images/3982_f101r.jpg").convert("RGB"), "f124r": Image.open(f"{FAM}/images/3982_f124r.jpg").convert("RGB")}
    rid = random.Random(1113); used = set(); key = ["call\tid\trole\tleaf\tline\tpos_or_seg\tx\tgroup\trepeat_of"]
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
                im = Image.open(f"{scratch}/f176v/f176v_{it['line']}_{it['segment']}.jpg").convert("RGB"); x = int(it["x_px"])
                x = max(110, min(im.width - 110, x)); cv, d = tile(im, x, 0, im.height); key.append(f"{c}\t{i}\tanchor\t176v\t{it['line']}\t{it['segment']}\t{it['x_px']}\t{grp}\t")
            else:
                leaf, line, pos, x, yc = it; cv, d = tile(nat[leaf], x, yc - 75, yc + 60)
                k = (leaf, line, pos); rep_of = first.get(k, "") if role == "R" or k in first else ""
                if k not in first: first[k] = i
                key.append(f"{c}\t{i}\ttarget\t{leaf}\t{line}\t{pos}\t{x}\t\t{rep_of}")
            d.text((8, 6), i, fill=(0, 0, 0)); ims.append(cv)
        os.makedirs(f"{scratch}/{c}", exist_ok=True)
        for s in range(0, len(ims), 12):
            sh = Image.new("RGB", (4 * 360, 3 * 262), "white")
            for j, cv in enumerate(ims[s:s + 12]): sh.paste(cv, ((j % 4) * 360, (j // 4) * 262))
            sh.save(f"{scratch}/{c}/sheet_{s // 12 + 1:02d}.jpg", quality=90)
    open(f"{HERE}/v11_items.tsv", "w").write("\n".join(key) + "\n"); print("pools f101r", n1, "f124r", n2, "items", len(key) - 1)
if __name__ == "__main__":
    if sys.argv[1] == "tiles": tiles(sys.argv[2])
def score():
    sys.path.insert(0, HERE); import v11_crosstab as X
    items = rd(f"{HERE}/v11_items.tsv"); out = []; mine = {}
    for c in ("c1", "c2", "c3"):
        ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{HERE}/v11_reply_{c}.tsv")}; its = [r for r in items if r["call"] == c]
        anc = [r for r in its if r["role"] == "anchor"]; ahit = sum((ans.get(r["id"]) == "yes") == (r["group"] == "CP") and ans.get(r["id"]) in ("yes", "no") for r in anc)
        byid = {r["id"]: r for r in its}; reps = [r for r in its if r["repeat_of"]]
        rhit = sum(ans.get(r["id"]) == ans.get(r["repeat_of"]) for r in reps)
        ok = ahit >= 8 and rhit >= 5
        acc = " ".join(f"{g}:{'/'.join(ans.get(r['id'], '?') for r in anc if r['group'] == g)}" for g in ("CP", "AN"))
        out.append(f"{c}: anchors {ahit}/{len(anc)} (gate 8) [{acc}]; repeats {rhit}/{len(reps)} (gate 5) -> {'PASS' if ok else 'FAIL (answers not used)'}")
        if ok:
            for r in its:
                if r["role"] == "target" and not r["repeat_of"]: mine[(r["leaf"], r["line"], r["pos_or_seg"])] = ans.get(r["id"], "missing")
    for leaf in ("f101r", "f124r"):
        lab = {(l, p): a for (lf, l, p), a in mine.items() if lf == leaf}
        out.append(f"{leaf}: my labels {len(lab)} ({' '.join(f'{k} {v}' for k, v in sorted(Counter(lab.values()).items()))})")
        lm = X.letter_map(leaf)
        for nm, f in (("all", lambda v: True), ("neighbour-anchored", lambda v: v[2])):
            pairs = [(b, X.cls(lm[k][0])) for k, b in lab.items() if k in lm and f(lm[k])]
            r = X.test(pairs, perms=10000)
            ro = ("n < 20" if r is None or r["n"] < 20 else "tracks" if r["share"] >= 0.75 and r["p"] < 0.01 else "does not track" if r["share"] < 0.6 or r["p"] > 0.05 else "unclear")
            out.append("  B(i/iii) " + X.fmt(nm, r).split(" -> ")[0] + f" -> {ro}")
        lets = defaultdict(Counter)
        for k, b in lab.items():
            if k in lm: lets[b][lm[k][0]] += 1
        out.append("  letters by my answer: " + "; ".join(f"{b}: " + " ".join(f"{x} {y}" for x, y in lets[b].most_common(8)) for b in sorted(lets)))
        if leaf == "f101r":
            run = X.runner_labels(); sh = [(lab[k], run[k]) for k in lab if k in run and lab[k] in ("yes", "no") and run[k] in ("yes", "no")]
            n = len(sh); po = sum(a == b for a, b in sh) / n; pa = sum(a == "yes" for a, _ in sh) / n; pb = sum(b == "yes" for _, b in sh) / n
            pe = pa * pb + (1 - pa) * (1 - pb); kap = (po - pe) / (1 - pe) if pe < 1 else float("nan")
            out.append(f"  B(ii) my vs runner's labels on {n} shared tokens: agreement {po:.2f}, Cohen's kappa {kap:.2f} -> "
                       + ("the runner's reads replicate" if kap >= 0.6 else "they do not replicate" if kap < 0.4 else "partly"))
    sp = {(r["line"], r["position"]): r["sign"] for r in csv.DictReader(open(f"{P}/recf124r_split/ciphertext_draft.tsv"), delimiter="\t")}
    lab = {(l, p): a for (lf, l, p), a in mine.items() if lf == "f124r"}
    sh = [(a, "no" if sp.get(k) == "C43" else "yes/n") for k, a in lab.items() if a in ("yes", "no")]; t = Counter(sh)
    out.append(f"  B(ii) f124r my vs runner's (split draft: relabelled C43 = runner 'no'; else 'yes' or 'n') on {len(sh)}: "
               + " ".join(f"mine {a}/runner {b} {v}" for (a, b), v in sorted(t.items()))
               + f"; agreement {sum(v for (a, b), v in t.items() if (a == 'no') == (b == 'no')) / max(1, len(sh)):.2f}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/v11_bowl_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__" and sys.argv[1] == "score": score()
