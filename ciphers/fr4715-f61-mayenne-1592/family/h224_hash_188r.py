#!/usr/bin/env python3
"""H224 (runner 9 session_012NTadgrCBftz3oRtgw5jFu, 29 Sept 2026): H212's hash forms at fr.3984 f.188r's HASH4 positions, whose alignment against the
separate decipherment (passes/f188r_align_v4.tsv) puts HASH4 under d 12 (all 'agrees'), q 3, i 10, x 3 (all 'conflict'). Written before the call.
 Caveat stated before the call: f.188r is Desportes's hand, where H214 found no looped hash on f.176; and the i/x rows are alignment conflicts (the letter
 placed opposite the sign disagrees with the key's d/q), so they may be misplaced letters. The test asks whether the i/x-conflict positions carry a
 different hash form (which would explain the conflicts) or the same form as the d rows (which would point to misalignment).
 tiles NATIVE SCRATCH: pool = align rows coded HASH4 whose letter is i/x or d/q, draft sign HASH4 and pass A HASH4 at that position (pass A's x).
   Sample (seed 224): all i/x (<= 12) and 12 d/q. Tiles at H222's matched scale: native window x +-60 by the band box (sheets/f188r_bands.json;
   x = box x0 + x_px/2), scaled 3x; anchors = 10 H212 tiles (A 5, B 5, tile 9 excluded) in H222's geometry. Red triangles above and below, numbered
   Y01.., shuffled, 20 per sheet, <scratch>/h224/. Key h224_items.tsv committed before the call.
 One blind Opus vision call, fixed categories: A 4-head on the hash; B two small loops on the hash; C a plain hash with nothing attached; D a
   2-shaped hook leading into the hash ("2#", H222's reader's group for f.101r's period i-sign H24; added after the runner's geometry look at sheet 1,
   before the call, disclosed in PROMPTS); N other / cannot tell. Inline reply, no tool use.
 score: GATE anchors >= 8 of 10 as their H212 group (A->A, B->B), else CONTROL FAIL. Then, as H220: B vs A by letter ({i,x} vs {d,q}), Fisher;
   read-out "f.188r's letters follow the hash forms (looped i/x, 4-head d/q)" iff p < 0.01 AND B >= 0.7 i/x AND A >= 0.7 d/q. Second pre-stated
   read-out (H162's note, a bare hash = i): the same rule with C in place of B. Third (H222/H220: f.101r's i-sign is "2#"): the same
   rule with D in place of B. Else "no form-letter link shown". Descriptive; no key change.
  python3 h224_hash_188r.py tiles NATIVE SCRATCH | score [--check]"""
import csv, json, os, random, sys
from collections import defaultdict, Counter
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; sys.path.insert(0, HERE)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def pool():
    S = defaultdict(list)
    for r in rd(f"{P}/recf188r/ciphertext_draft.tsv"):
        if r["sign"] != "DASH": S[r["line"]].append(r)
    A = {(r["line"], int(r["pos"])): r for r in rd(f"{P}/f188r_signsA.tsv")}; out = defaultdict(list)
    for r in rd(f"{P}/f188r_align_v4.tsv"):
        if r["kind"] != "code" or r["value"] != "HASH4" or r["plain_chunk"] not in ("i", "x", "d", "q"): continue
        s = S[r["cipher_line"]][int(r["idx"])]
        if s["sign"] != "HASH4": continue
        a = A.get((r["cipher_line"], int(s["position"])))
        if a and a["sign"] == "HASH4":
            out["IX" if r["plain_chunk"] in "ix" else "DQ"].append(dict(line=r["cipher_line"], idx=r["idx"], letter=r["plain_chunk"], status=r["status"], seg=a["segment"], x=int(a["x_px"])))
    return out
def tiles(native, scratch):
    from PIL import Image, ImageDraw
    import h212_hash_sort as h212
    rng = random.Random(224); pl = pool(); its = []
    for k, n in (("IX", 12), ("DQ", 12)): its += [dict(t, kind="T") for t in rng.sample(pl[k], min(n, len(pl[k])))]
    k212 = {r["item"]: r for r in rd(f"{HERE}/h212_items.tsv")}
    grp = {f"T{int(r['tile'].split()[-1]):02d}": r["group"].strip() for r in rd(f"{P}/h212_sort.tsv")}
    geo = {(t["leaf"], t["line"], t["seg"], t["x"]): t for t in h212.items()}; anc = {"A": [], "B": []}
    for m, r in sorted(k212.items()):
        if m == "T09" or grp.get(m) not in anc: continue
        anc[grp[m]].append(dict(geo[(r["leaf"], r["line"], r["segment"], int(r["x_px"]))], kind="C", h212=m, group=grp[m]))
    for G in ("A", "B"): its += rng.sample(anc[G], 5)
    rng.shuffle(its); os.makedirs(f"{scratch}/h224", exist_ok=True); B = json.load(open(f"{HERE}/sheets/f188r_bands.json"))["boxes"]
    nat = Image.open(native).convert("RGB"); ims = []; key = ["item\tkind\tref\tline\tidx\tletter\tstatus\tgroup"]
    for n, t in enumerate(its, 1):
        c = Image.new("RGB", (370, 400), "white"); d = ImageDraw.Draw(c)
        if t["kind"] == "T":
            b = B[f"f188r_{t['line']}_{t['seg']}.jpg"]; x = b[0] + t["x"] // 2
            w = nat.crop((x - 60, b[1], x + 60, b[3])).resize((360, 3 * (b[3] - b[1]))); mx = 5 + 180
            key.append(f"Y{n:02d}\tT\tf188r\t{t['line']}\t{t['idx']}\t{t['letter']}\t{t['status']}\t{'IX' if t['letter'] in 'ix' else 'DQ'}")
        else:
            im = Image.open(t["crop"]).convert("RGB"); x0 = max(0, min(im.width - 360, t["x"] - 180))
            w = im.crop((x0, 0, x0 + 360, im.height)); mx = 5 + (t["x"] - x0)
            key.append(f"Y{n:02d}\tC\t{t['h212']}\t{t['line']}\t-\t-\t-\t{t['group']}")
        c.paste(w, (5, 20)); y = 20 + w.height
        d.polygon([(mx - 8, 2), (mx + 8, 2), (mx, 17)], fill=(220, 0, 0)); d.polygon([(mx - 8, y + 18), (mx + 8, y + 18), (mx, y + 3)], fill=(220, 0, 0))
        d.text((330, 4), f"Y{n:02d}", fill=(0, 0, 0)); ims.append(c)
    for s0 in range(0, len(ims), 20):
        sh = Image.new("RGB", (4 * 370, 5 * 400), "white")
        for k, c in enumerate(ims[s0:s0 + 20]): sh.paste(c, ((k % 4) * 370, (k // 4) * 400))
        sh.save(f"{scratch}/h224/sheet_{s0 // 20 + 1:02d}.jpg", quality=88)
    open(f"{HERE}/h224_items.tsv", "w").write("\n".join(key) + "\n")
    print(len(its), "tiles; pool", {k: len(v) for k, v in pl.items()}, Counter(t["kind"] for t in its))
def score():
    import h190_4fam as h190
    its = rd(f"{HERE}/h224_items.tsv"); ans = {r["id"]: r["answer"].strip().upper() for r in rd(f"{P}/h224_reply.tsv")}
    C = [r for r in its if r["kind"] == "C"]; hit = sum(ans.get(r["item"]) == r["group"] for r in C)
    out = [f"anchor control: {hit} of {len(C)} H212 tiles answered as their H212 group (gate >= 8): {'PASS' if hit >= 8 else 'CONTROL FAIL'}",
           "anchor answers: A " + " ".join(ans.get(r["item"], "-") for r in C if r["group"] == "A") + " | B " + " ".join(ans.get(r["item"], "-") for r in C if r["group"] == "B")]
    if hit >= 8:
        T = [r for r in its if r["kind"] == "T"]; t = {k: [0, 0] for k in "ABCDN"}
        for r in T: t.setdefault(ans.get(r["item"], "N"), [0, 0])[0 if r["group"] == "IX" else 1] += 1
        out.append("targets: " + "; ".join(f"{k} i/x {v[0]} d/q {v[1]}" for k, v in sorted(t.items())))
        for alt, name in (("B", "looped"), ("C", "plain hash"), ("D", "2-hook")):
            p = h190.fisher(t[alt][0], t[alt][1], t["A"][0], t["A"][1]); xs = t[alt][0] / max(1, sum(t[alt])); as_ = t["A"][1] / max(1, sum(t["A"]))
            ok = p < 0.01 and xs >= 0.7 and as_ >= 0.7
            out.append(f"read-out {alt} ({name}) vs A: {alt} i/x-share {xs:.2f} (n {sum(t[alt])}), A d/q-share {as_:.2f}, Fisher p {p:.2g} -> " +
                       (f"f.188r's letters follow the hash forms ({name} i/x, 4-head d/q)" if ok else "no form-letter link shown"))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h224_hash_188r_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(sys.argv[2], sys.argv[3]) if sys.argv[1] == "tiles" else score()
