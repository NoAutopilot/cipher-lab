#!/usr/bin/env python3
"""H193 (runner 7, 29 Sept 2026): a shape attribute for the 4-family, validated by the period decipherment on a second leaf. Written before the call.
 tiles: consensus columns keep pass A's (segment, x_px). f.176v (clear fol. 177v V06-, build_f176v_key design): ANCHORS = 10 agreed-4TRI columns the
   DP pairs with c or p (group CP) and 10 A|B = 4TRI|C43 columns paired with a or n (group AN), seed 193. f.176r (clear fol. 177r L01 - 177v V05, h183
   design): TARGETS = 40 agreed-4TRI columns, seed 193, whatever their letter. Each item is a 300-px strip with a red triangle under the sign
   (h189's format), shuffled, numbered Q01..Q60, sheets in <scratch>/h193/. Key h193_items.tsv (group, leaf, letter) committed before the call.
 The runner looks ONLY at the 20 anchor strips (labels known) to name one yes/no shape attribute that separates CP from AN, writes it into
   PROMPTS_f176_f175.md section H193, and commits before the call. The reader answers the yes/no question for all 60 items (blind to group and leaf).
 score: GATE (anchors) >= 17 of 20 items answer in their group's direction. If it passes, f.176r's 40 targets are split by the answer, and the
   letters the DP pairs them with are counted {c,p} vs {a,n} per answer; Fisher exact test; descriptive of whether the attribute carries the letter
   split on a second leaf.
  python3 h193_attr.py tiles SCRATCH | score [--check]"""
import difflib, os, random, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import build_f176_key as b, build_f176v_key as v, h190_4fam as h190
from f61crib import align
g = b.g; import glob
def rows_full(pattern):
    R = defaultdict(list)
    for f in sorted(glob.glob(f"{b.P}/{pattern}")):
        for r in g.rd(f):
            s = {"EBR_A": "EBR", "EBR_B": "EBR"}.get(r["sign"].strip(), r["sign"].strip())
            if s != "PLAIN": R[r["line"]].append((s, r["segment"], int(r["x_px"])))
    return R
def cons_origin(A, B, rows):
    seq, org = [], []
    for l in rows:
        a = [x[0] for x in A[l]]; bb = [x[0] for x in B[l]]
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, bb, autojunk=False).get_opcodes():
            if op == "equal": seq += a[i1:i2]; org += [(l, *A[l][k][1:]) for k in range(i1, i2)]
            elif op == "replace" and i2 - i1 == j2 - j1: seq += [f"?{x}|{y}" for x, y in zip(a[i1:i2], bb[j1:j2])]; org += [(l, *A[l][k][1:]) for k in range(i1, i2)]
            else: n = max(i2 - i1, j2 - j1); seq += ["?"] * n; org += [None] * n
    return seq, org
def paired(seq, org, text):
    _, pairs = align(text, seq, g.load_key()); return [(seq[j], org[j], text[i]) for i, j in pairs if org[j]]
def data():
    lines = {}
    for f in sorted(glob.glob(f"{b.P}/f177v_clearA_*.tsv")):
        for r in g.rd(f): lines.setdefault("V" + r["line"].lstrip("LV"), r["text"])
    sv, ov = cons_origin(rows_full("f176v_signsA_*.tsv"), rows_full("f176v_signsB_*.tsv"), [f"L{k:02d}" for k in range(1, 46)])
    tv = v.clear("V06")[0][:int(0.8 * len(sv))]
    sr, orr = cons_origin(rows_full("f176r_signsA_*.tsv"), rows_full("f176r_signsB_*.tsv"), [f"L{k:02d}" for k in range(1, 48)])
    tr = v.clear177r() + "".join(g.fold(lines[f"V{k:02d}"]) for k in range(1, 6)); tr = tr[:len(sr)]
    return paired(sv, ov, tv), paired(sr, orr, tr)
def tiles(scratch):
    from PIL import Image, ImageDraw
    pv, pr = data(); rng = random.Random(193)
    cp = [p for p in pv if p[0] == "4TRI" and p[2] in "cp"]; an = [p for p in pv if p[0] in ("?4TRI|C43", "?C43|4TRI") and p[2] in "an"]
    tg = [p for p in pr if p[0] == "4TRI"]
    its = [("CP", "176v", p) for p in rng.sample(cp, 10)] + [("AN", "176v", p) for p in rng.sample(an, 10)] + [("T", "176r", p) for p in rng.sample(tg, 40)]
    rng.shuffle(its); os.makedirs(f"{scratch}/h193", exist_ok=True); key = ["item\tgroup\tleaf\tline\tsegment\tx_px\tletter"]; ims = []
    for n, (grp, leaf, (s, (l, sg, x), L)) in enumerate(its, 1):
        f = f"{scratch}/f176v/f176v_{l}_{sg}.jpg" if leaf == "176v" else f"{scratch}/f176r/f176_{l}_{sg}.jpg"
        im = Image.open(f).convert("RGB"); x0 = max(0, min(im.width - 300, x - 150)); t = im.crop((x0, 0, x0 + 300, im.height)).resize((360, int(im.height * 1.2)))
        c = Image.new("RGB", (370, 190), "white"); c.paste(t, (5, 0)); d = ImageDraw.Draw(c); mx = 5 + int((x - x0) * 1.2); y = min(t.height, 150)
        d.polygon([(mx - 9, y + 16), (mx + 9, y + 16), (mx, y + 2)], fill=(220, 0, 0)); d.text((6, y + 22), f"Q{n:02d}", fill=(0, 0, 0))
        ims.append(c); key.append(f"Q{n:02d}\t{grp}\t{leaf}\t{l}\t{sg}\t{x}\t{L}")
    for s in range(0, len(ims), 20):
        sh = Image.new("RGB", (4 * 370, 5 * 190), "white")
        for k, c in enumerate(ims[s:s + 20]): sh.paste(c, ((k % 4) * 370, (k // 4) * 190))
        sh.save(f"{scratch}/h193/sheet_{s // 20 + 1:02d}.jpg", quality=88)
    anc = Image.new("RGB", (4 * 370, 5 * 190 * 2), "white"); k = 0   # the runner's first look: anchors only, by group
    for grp in ("CP", "AN"):
        for n, it in enumerate(its, 1):
            if it[0] == grp: anc.paste(ims[n - 1], ((k % 4) * 370, (k // 4) * 190)); k += 1
        k = 20
    anc.save(f"{scratch}/h193/anchors_by_group.jpg", quality=88)
    open(f"{HERE}/h193_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "items; CP pool", len(cp), "AN pool", len(an), "target pool", len(tg))
def score():
    key = {r["item"]: r for r in g.rd(f"{HERE}/h193_items.tsv")}; ans = {r["item"]: r["answer"].strip().lower() for r in g.rd(f"{b.P}/h193_attribute.tsv")}
    yes_group = open(f"{HERE}/h193_yes_group.txt").read().strip()   # which anchor group the attribute's 'yes' names (CP or AN), fixed before the call
    anc = [m for m, r in key.items() if r["group"] in ("CP", "AN")]
    hit = sum((ans.get(m) == "yes") == (key[m]["group"] == yes_group) and ans.get(m) in ("yes", "no") for m in anc)
    out = [f"anchors: {hit} of {len(anc)} answer in their group's direction (gate >= 17): {'PASS' if hit >= 17 else 'CONTROL FAIL'}"]
    if hit >= 17:
        c = {"yes": [0, 0], "no": [0, 0]}
        for m, r in key.items():
            if r["group"] == "T" and ans.get(m) in c and r["letter"] in "cpan": c[ans[m]][0 if r["letter"] in "cp" else 1] += 1
        p = h190.fisher(c["yes"][0], c["yes"][1], c["no"][0], c["no"][1])
        out.append(f"f.176r targets: answer yes ({yes_group}-like) c/p {c['yes'][0]} a/n {c['yes'][1]}; answer no c/p {c['no'][0]} a/n {c['no'][1]}; Fisher p {p:.2g}")
    txt = "\n".join(out) + "\n"; p_ = f"{HERE}/h193_attr_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p_) and open(p_).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p_, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(sys.argv[2]) if sys.argv[1] == "tiles" else score()
