#!/usr/bin/env python3
"""H220 (runner 9 session_012NTadgrCBftz3oRtgw5jFu, 29 Sept 2026): H212's two hash forms against fr.3982 f.101r's period letters. Written before the call.
 Row as written asked for 10 i + 10 d/q positions under HASH4; the pool has HASH4 d 43, q 24, i only 4, because f.101r's readers coded this leaf's i/x
 sign H24 ("2 joined to a crossed 4", i 170; KEY.md). So the targets are drawn from both codes and the question is whether f.101r's period-read i/x sign
 (H24) is f.108's looped form B and its d/q sign (HASH4) the 4-headed form A.
 tiles NATIVE SCRATCH: pool = rows of passes/f101r_align_v4.tsv (grade C gloss alignment) coded HASH4 with letter d/q/i, or H24 with letter i; mapped to
   pass A's x as in h207_bowl_101r.py (kept only when the draft sign equals the code and pass A wrote the same code -- for H24, pass A's HASH4 or
   4STEM, since align_period.py builds H24 from pass A HASH4 + pass B 4STEM). Sample (seed 220): HASH4 d/q 12, HASH4 i all (<= 4), H24 i 12. Strips
   exactly as H207 (Gallica native btv1b9060543f f210, band box from sheets/f101r_bands.json, red triangles above and below). ANCHORS: 10 of H212's own
   tiles (f.108v/f.108r, geometry of h212_hash_sort.py), 5 from H212 group A and 5 from group B (tile 9, marked uncertain, excluded), seed 220.
   Targets and anchors shuffled together (seed 220), numbered V01.., 20 per sheet, <scratch>/h220/. Key h220_items.tsv committed before the call.
 One blind Opus vision call, fixed categories per tile: A = a figure-4 stroke rising above the hash (often one vertical running below the line);
   B = two small loops sitting on the hash, short verticals only; N = neither / not a hash-type sign / cannot tell. Inline reply, no tool use.
 score: GATE anchors >= 8 of 10 answered as their H212 group, else CONTROL FAIL and targets not scored. Then form (A/B, N left out) vs letter
   ({i} vs {d,q}), pooled and per code, Fisher exact. Pre-stated read-out: "f.101r's period letters follow the hash forms (looped i/x, 4-head d/q)"
   iff pooled p < 0.01 AND B answers >= 0.7 i AND A answers >= 0.7 d/q; else "no form-letter link shown by the registered rule". Also reported, not
   gated: the same table on rows whose align status carries no 'conflict'. Descriptive, for the verifier; no key change.
  python3 h220_hash_101r.py tiles NATIVE SCRATCH | score [--check]"""
import csv, json, os, random, sys
from collections import defaultdict, Counter
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; sys.path.insert(0, HERE)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def pool():
    S = defaultdict(list)
    for r in rd(f"{P}/recf101r/ciphertext_draft.tsv"):
        if r["sign"] != "DASH": S[r["line"]].append(r)
    A = {(r["line"], int(r["pos"])): r for r in rd(f"{P}/f101r_signsA.tsv")}; out = defaultdict(list)
    for r in rd(f"{P}/f101r_align_v4.tsv"):
        if r["kind"] != "code": continue
        v, L = r["value"], r["plain_chunk"]
        if not ((v == "HASH4" and L in ("d", "q", "i")) or (v == "H24" and L == "i")): continue
        s = S[r["cipher_line"]][int(r["idx"])]
        if s["sign"] != v: continue   # 21 H24 rows sit on a draft sign other than H24 (align_period.py recodes from the A/B pair); left out
        a = A.get((r["cipher_line"], int(s["position"])))
        # H24 is align_period.py's code for pass A HASH4 + pass B 4STEM, so pass A's sign there is HASH4 (or 4STEM); either marks this sign's x
        if a and (a["sign"] == v or (v == "H24" and a["sign"] in ("HASH4", "4STEM"))):
            out[(v, "I" if L == "i" else "DQ")].append(dict(line=r["cipher_line"], idx=r["idx"], code=v, letter=L, status=r["status"], seg=a["segment"], x=int(a["x_px"])))
    return out
def tiles(native, scratch):
    from PIL import Image, ImageDraw
    import h212_hash_sort as h212
    pl = pool(); rng = random.Random(220); its = []
    for k, n in ((("HASH4", "DQ"), 12), (("HASH4", "I"), 4), (("H24", "I"), 12)): its += rng.sample(pl[k], min(n, len(pl[k])))
    for t in its: t["kind"] = "T"
    # anchors: H212 tiles by the reader's group, geometry recomputed from h212's own item list (same order as h212_items.tsv's key)
    k212 = {r["item"]: r for r in rd(f"{HERE}/h212_items.tsv")}
    grp = {f"T{int(r['tile'].split()[-1]):02d}": r["group"].strip() for r in rd(f"{P}/h212_sort.tsv")}
    geo = {(t["leaf"], t["line"], t["seg"], t["x"]): t for t in h212.items()}
    anc = {"A": [], "B": []}
    for m, r in sorted(k212.items()):
        if m == "T09" or grp.get(m) not in anc: continue
        g = geo[(r["leaf"], r["line"], r["segment"], int(r["x_px"]))]; anc[grp[m]].append(dict(g, kind="C", h212=m, group=grp[m]))
    for G in ("A", "B"): its += rng.sample(anc[G], 5)
    rng.shuffle(its); os.makedirs(f"{scratch}/h220", exist_ok=True); B = json.load(open(f"{HERE}/sheets/f101r_bands.json"))["boxes"]
    nat = Image.open(native).convert("RGB"); ims = []; key = ["item\tkind\tref\tline\tidx\tcode\tletter\tstatus\tgroup"]
    for n, t in enumerate(its, 1):
        c = Image.new("RGB", (370, 220), "white"); d = ImageDraw.Draw(c)
        if t["kind"] == "T":   # H207's strip geometry, unchanged
            b = B[f"f101r_{t['line']}_{t['seg']}.jpg"]; x = b[0] + t["x"] // 2; y0, y1 = b[1], b[3]; s = 1.1
            w = nat.crop((x - 125, y0, x + 125, y1)); w = w.resize((int(250 * s), int((y1 - y0) * s)))
            c.paste(w, (5, 18)); mx = 5 + int(125 * s); y = 18 + w.height
            key.append(f"V{n:02d}\tT\tf101r\t{t['line']}\t{t['idx']}\t{t['code']}\t{t['letter']}\t{t['status']}\t-")
        else:                  # H212's tile geometry, unchanged
            im = Image.open(t["crop"]).convert("RGB"); W, s = t["W"], t["s"]; x0 = max(0, min(im.width - W, t["x"] - W // 2))
            w = im.crop((x0, 0, x0 + W, im.height)); w = w.resize((int(W * s), int(im.height * s)))
            c.paste(w, (5, 18)); mx = 5 + int((t["x"] - x0) * s); y = 18 + w.height
            key.append(f"V{n:02d}\tC\t{t['h212']}\t{t['line']}\t-\tHASH4\t-\t-\t{t['group']}")
        d.polygon([(mx - 8, 1), (mx + 8, 1), (mx, 15)], fill=(220, 0, 0)); d.polygon([(mx - 8, y + 16), (mx + 8, y + 16), (mx, y + 2)], fill=(220, 0, 0))
        d.text((300, 4), f"V{n:02d}", fill=(0, 0, 0)); ims.append(c)
    for s0 in range(0, len(ims), 20):
        sh = Image.new("RGB", (4 * 370, 5 * 220), "white")
        for k, c in enumerate(ims[s0:s0 + 20]): sh.paste(c, ((k % 4) * 370, (k // 4) * 220))
        sh.save(f"{scratch}/h220/sheet_{s0 // 20 + 1:02d}.jpg", quality=88)
    open(f"{HERE}/h220_items.tsv", "w").write("\n".join(key) + "\n")
    print(len(its), "tiles; pool", {k: len(v) for k, v in pl.items()}, Counter(t["kind"] for t in its))
def score():
    import h190_4fam as h190
    its = rd(f"{HERE}/h220_items.tsv"); ans = {r["id"]: r["answer"].strip().upper() for r in rd(f"{P}/h220_reply.tsv")}
    C = [r for r in its if r["kind"] == "C"]; hit = sum(ans.get(r["item"]) == r["group"] for r in C)
    out = [f"anchor control: {hit} of {len(C)} H212 tiles answered as their H212 group (gate >= 8): {'PASS' if hit >= 8 else 'CONTROL FAIL'}",
           "anchor answers: A " + " ".join(ans.get(r["item"], "-") for r in C if r["group"] == "A") + " | B " + " ".join(ans.get(r["item"], "-") for r in C if r["group"] == "B")]
    if hit >= 8:
        T = [r for r in its if r["kind"] == "T"]
        def tab(rows):
            t = {"A": [0, 0], "B": [0, 0], "N": [0, 0]}
            for r in rows: t.setdefault(ans.get(r["item"], "N"), [0, 0])[0 if r["letter"] == "i" else 1] += 1
            return t
        for name, rows in (("HASH4 d/q", [r for r in T if r["code"] == "HASH4" and r["letter"] != "i"]), ("HASH4 i", [r for r in T if r["code"] == "HASH4" and r["letter"] == "i"]),
                           ("H24 i", [r for r in T if r["code"] == "H24"]), ("pooled", T), ("pooled, no-conflict rows", [r for r in T if "conflict" not in r["status"]])):
            t = tab(rows); p = h190.fisher(t["B"][0], t["B"][1], t["A"][0], t["A"][1])
            out.append(f"{name}: B (looped) i {t['B'][0]} d/q {t['B'][1]}; A (4-head) i {t['A'][0]} d/q {t['A'][1]}; N i {t['N'][0]} d/q {t['N'][1]}; Fisher p {p:.2g}")
        t = tab(T); p = h190.fisher(t["B"][0], t["B"][1], t["A"][0], t["A"][1])
        bs = t["B"][0] / max(1, sum(t["B"])); as_ = t["A"][1] / max(1, sum(t["A"]))
        ok = p < 0.01 and bs >= 0.7 and as_ >= 0.7
        out.append(f"read-out: B i-share {bs:.2f}, A d/q-share {as_:.2f}, p {p:.2g} -> " + ("f.101r's period letters follow the hash forms (looped i/x, 4-head d/q)" if ok else "no form-letter link shown by the registered rule"))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h220_hash_101r_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(sys.argv[2], sys.argv[3]) if sys.argv[1] == "tiles" else score()
