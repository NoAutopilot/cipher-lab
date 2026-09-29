#!/usr/bin/env python3
"""H227 (runner 9 session_012NTadgrCBftz3oRtgw5jFu, 29 Sept 2026): every remaining fr.3982 f.101r HASH4 position (pass-A-mapped as h220/h226, with a
period letter, not tiled in H220 or H226: 32) shape-read with H224's five categories, so the looped form B's period letters can be tabled across H220 +
H226 + this step. Written before the call.
 tiles SCRATCH NATIVE101: H222/H224 geometry unchanged (native x +-60 by the band box, 3x); anchors 10 H212 tiles (A 5, B 5, tile 9 excluded); shuffled
   (seed 227), X01.., 20 per sheet, <scratch>/h227/. Key h227_items.tsv committed before the call; the runner does not look at the sheets.
 One blind Opus vision call, H224's prompt (tile range X01-X42), inline, no tool use.
 score: GATE anchors >= 8/10. Then B's letters over H220's HASH4 targets, H226's f.101r strays and this step (H220 used A/B/N only; its B answers count).
   Letter cells as KEY.md's table: d/q, i/x, c/p, a/n, other. Pre-stated read-out: "looped B carries a letter set of its own" iff B >= 6 and one cell
   holds >= 0.7 of B's letters and that cell is not d/q; "looped B reads as HASH4 (d/q)" iff B >= 6 and d/q >= 0.7; else "too few or mixed".
  python3 h227_loop_101r_all.py tiles SCRATCH NATIVE101 | score [--check]"""
import json, os, random, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; sys.path.insert(0, HERE)
from h226_hash4_strays import rd
def remaining():
    S = defaultdict(list)
    for r in rd(f"{P}/recf101r/ciphertext_draft.tsv"):
        if r["sign"] != "DASH": S[r["line"]].append(r)
    A = {(r["line"], int(r["pos"])): r for r in rd(f"{P}/f101r_signsA.tsv")}
    done = {(r["line"], r["idx"]) for r in rd(f"{HERE}/h220_items.tsv") if r["kind"] == "T" and r["code"] == "HASH4"} | \
           {(r["line"], r["idx"]) for r in rd(f"{HERE}/h226_items.tsv") if r["kind"] == "T" and r["ref"] == "f101r"}
    out = []
    for r in rd(f"{P}/f101r_align_v4.tsv"):
        if r["kind"] != "code" or r["value"] != "HASH4" or not r["plain_chunk"]: continue
        s = S[r["cipher_line"]][int(r["idx"])]
        if s["sign"] != "HASH4": continue
        a = A.get((r["cipher_line"], int(s["position"])))
        if a and a["sign"] == "HASH4" and (r["cipher_line"], r["idx"]) not in done:
            out.append(dict(line=r["cipher_line"], idx=r["idx"], letter=r["plain_chunk"], status=r["status"], seg=a["segment"], x=int(a["x_px"]), kind="T"))
    return out
def tiles(scratch, native):
    from PIL import Image, ImageDraw
    import h212_hash_sort as h212
    rng = random.Random(227); its = remaining()
    k212 = {r["item"]: r for r in rd(f"{HERE}/h212_items.tsv")}
    grp = {f"T{int(r['tile'].split()[-1]):02d}": r["group"].strip() for r in rd(f"{P}/h212_sort.tsv")}
    geo = {(t["leaf"], t["line"], t["seg"], t["x"]): t for t in h212.items()}; anc = {"A": [], "B": []}
    for m, r in sorted(k212.items()):
        if m == "T09" or grp.get(m) not in anc: continue
        anc[grp[m]].append(dict(geo[(r["leaf"], r["line"], r["segment"], int(r["x_px"]))], kind="C", h212=m, group=grp[m]))
    for G in ("A", "B"): its += rng.sample(anc[G], 5)
    rng.shuffle(its); os.makedirs(f"{scratch}/h227", exist_ok=True); nat = Image.open(native).convert("RGB")
    B = json.load(open(f"{HERE}/sheets/f101r_bands.json"))["boxes"]; ims = []; key = ["item\tkind\tref\tline\tidx\tletter\tstatus\tgroup"]
    for n, t in enumerate(its, 1):
        c = Image.new("RGB", (370, 470), "white"); d = ImageDraw.Draw(c)
        if t["kind"] == "T":
            b = B[f"f101r_{t['line']}_{t['seg']}.jpg"]; x = b[0] + t["x"] // 2
            w = nat.crop((x - 60, b[1], x + 60, b[3])).resize((360, 3 * (b[3] - b[1]))); mx = 5 + 180
            key.append(f"X{n:02d}\tT\tf101r\t{t['line']}\t{t['idx']}\t{t['letter']}\t{t['status']}\t-")
        else:
            im = Image.open(t["crop"]).convert("RGB"); x0 = max(0, min(im.width - 360, t["x"] - 180))
            w = im.crop((x0, 0, x0 + 360, im.height)); mx = 5 + (t["x"] - x0)
            key.append(f"X{n:02d}\tC\t{t['h212']}\t{t['line']}\t-\t-\t-\t{t['group']}")
        c.paste(w, (5, 20)); y = 20 + w.height
        d.polygon([(mx - 8, 2), (mx + 8, 2), (mx, 17)], fill=(220, 0, 0)); d.polygon([(mx - 8, y + 18), (mx + 8, y + 18), (mx, y + 3)], fill=(220, 0, 0))
        d.text((330, 4), f"X{n:02d}", fill=(0, 0, 0)); ims.append(c)
    for s0 in range(0, len(ims), 20):
        sh = Image.new("RGB", (4 * 370, 5 * 470), "white")
        for k, c in enumerate(ims[s0:s0 + 20]): sh.paste(c, ((k % 4) * 370, (k // 4) * 470))
        sh.save(f"{scratch}/h227/sheet_{s0 // 20 + 1:02d}.jpg", quality=88)
    open(f"{HERE}/h227_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "tiles", Counter(t["kind"] for t in its))
CELLS = (("d/q", "dq"), ("i/x", "ixj"), ("c/p", "cp"), ("a/n", "an"))
def cell(L): return next((n for n, s in CELLS if L in s), "other")
def score():
    its = rd(f"{HERE}/h227_items.tsv"); ans = {r["id"]: r["answer"].strip().upper() for r in rd(f"{P}/h227_reply.tsv")}
    C = [r for r in its if r["kind"] == "C"]; hit = sum(ans.get(r["item"]) == r["group"] for r in C)
    out = [f"anchor control: {hit} of {len(C)} H212 tiles answered as their H212 group (gate >= 8): {'PASS' if hit >= 8 else 'CONTROL FAIL'}"]
    if hit >= 8:
        T = [r for r in its if r["kind"] == "T"]; c = Counter(ans.get(r["item"], "N") for r in T)
        out.append("this step: " + " ".join(f"{k} {c.get(k, 0)}" for k in "ABCDN") + "  B letters: " + " ".join(r["letter"] for r in T if ans.get(r["item"]) == "B"))
        tab = defaultdict(Counter)
        a220 = {r["id"]: r["answer"].strip().upper() for r in rd(f"{P}/h220_reply.tsv")}; a226 = {r["id"]: r["answer"].strip().upper() for r in rd(f"{P}/h226_reply.tsv")}
        for r in rd(f"{HERE}/h220_items.tsv"):
            if r["kind"] == "T" and r["code"] == "HASH4": tab[a220.get(r["item"], "N")][cell(r["letter"])] += 1
        for r in rd(f"{HERE}/h226_items.tsv"):
            if r["kind"] == "T" and r["ref"] == "f101r": tab[a226.get(r["item"], "N")][cell(r["letter"])] += 1
        for r in T: tab[ans.get(r["item"], "N")][cell(r["letter"])] += 1
        for f in "ABCDN":
            out.append(f"f.101r HASH4 all steps, form {f}: " + " ".join(f"{n} {tab[f].get(n, 0)}" for n in [x for x, _ in CELLS] + ["other"]) + f" (n {sum(tab[f].values())})")
        b = tab["B"]; nb = sum(b.values()); top, tv = (b.most_common(1)[0] if nb else ("-", 0))
        v = ("looped B carries a letter set of its own" if nb >= 6 and tv / nb >= 0.7 and top != "d/q" else
             "looped B reads as HASH4 (d/q)" if nb >= 6 and b.get("d/q", 0) / nb >= 0.7 else "too few or mixed")
        out.append(f"read-out: B n {nb}, top cell {top} {tv}/{max(1, nb)} -> {v}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h227_loop_101r_all_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(*sys.argv[2:4]) if sys.argv[1] == "tiles" else score()
