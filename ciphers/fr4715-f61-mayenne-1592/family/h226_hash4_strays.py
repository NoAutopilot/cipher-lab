#!/usr/bin/env python3
"""H226 (runner 9 session_012NTadgrCBftz3oRtgw5jFu, 29 Sept 2026): the HASH4 rows whose period letter is neither d/q nor i/x (v5's "strays": f.101r p 7,
s 5, b 4, f 4, n 3, t 3, a 2, c 2, o 2, r 2, y 2, e 1; f.188r e 2, n 2, o 2, u 2, a 1, s 1, y 1) -- are they other hash shapes, or the 4-head at letters
the alignment misplaced? Written before the call.
 tiles SCRATCH NATIVE101 NATIVE188: pool as h220_hash_101r.py / h224_hash_188r.py (draft sign HASH4, pass A HASH4 at that position), letter not in
   d q i x j and not empty. Sample (seed 226): all f.188r strays, then f.101r strays to 24 in all. Tiles at H222's matched scale (native x +-60 by the
   band box, 3x); anchors = 10 H212 tiles (A 5, B 5, tile 9 excluded). Numbered Z01.., shuffled, 20 per sheet, <scratch>/h226/. Key h226_items.tsv
   committed before the call. Letters are not shown; the runner does not look at the sheets before the call (the geometry is H222/H224's, unchanged).
 One blind Opus vision call, H224's prompt and five categories (A 4-head, B looped, C plain hash, D 2-hook, N), inline, no tool use.
 score: GATE anchors >= 8/10 as their H212 group. Reference = the d/q targets of H220 and H224 (A 23, non-A 3 of 26 answered: HASH4 d/q is the 4-head).
   Pre-stated read-outs on the strays: "the strays sit on other shapes" iff non-A share >= 0.5 AND Fisher (stray non-A/A vs reference 3/23) p < 0.01;
   "the strays are the 4-head (letters misplaced or a wider cell)" iff non-A share <= 0.2; else "mixed". Descriptive, for the verifier; no key change.
  python3 h226_hash4_strays.py tiles SCRATCH NATIVE101 NATIVE188 | score [--check]"""
import csv, json, os, random, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; sys.path.insert(0, HERE)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
BAD = set("dqixj")
def strays(prefix):
    from collections import defaultdict
    S = defaultdict(list)
    for r in rd(f"{P}/rec{prefix}/ciphertext_draft.tsv"):
        if r["sign"] != "DASH": S[r["line"]].append(r)
    A = {(r["line"], int(r["pos"])): r for r in rd(f"{P}/{prefix}_signsA.tsv")}; out = []
    for r in rd(f"{P}/{prefix}_align_v4.tsv"):
        L = r["plain_chunk"]
        if r["kind"] != "code" or r["value"] != "HASH4" or not L or L in BAD: continue
        s = S[r["cipher_line"]][int(r["idx"])]
        if s["sign"] != "HASH4": continue
        a = A.get((r["cipher_line"], int(s["position"])))
        if a and a["sign"] == "HASH4": out.append(dict(leaf=prefix, line=r["cipher_line"], idx=r["idx"], letter=L, status=r["status"], seg=a["segment"], x=int(a["x_px"])))
    return out
def tiles(scratch, n101, n188):
    from PIL import Image, ImageDraw
    import h212_hash_sort as h212
    rng = random.Random(226); s188 = strays("f188r"); s101 = strays("f101r")
    its = [dict(t, kind="T") for t in s188] + [dict(t, kind="T") for t in rng.sample(s101, min(len(s101), 24 - len(s188)))]
    k212 = {r["item"]: r for r in rd(f"{HERE}/h212_items.tsv")}
    grp = {f"T{int(r['tile'].split()[-1]):02d}": r["group"].strip() for r in rd(f"{P}/h212_sort.tsv")}
    geo = {(t["leaf"], t["line"], t["seg"], t["x"]): t for t in h212.items()}; anc = {"A": [], "B": []}
    for m, r in sorted(k212.items()):
        if m == "T09" or grp.get(m) not in anc: continue
        anc[grp[m]].append(dict(geo[(r["leaf"], r["line"], r["segment"], int(r["x_px"]))], kind="C", h212=m, group=grp[m]))
    for G in ("A", "B"): its += rng.sample(anc[G], 5)
    rng.shuffle(its); os.makedirs(f"{scratch}/h226", exist_ok=True)
    nat = {"f101r": Image.open(n101).convert("RGB"), "f188r": Image.open(n188).convert("RGB")}
    bands = {lf: json.load(open(f"{HERE}/sheets/{lf}_bands.json"))["boxes"] for lf in nat}
    ims = []; key = ["item\tkind\tref\tline\tidx\tletter\tstatus\tgroup"]
    for n, t in enumerate(its, 1):
        c = Image.new("RGB", (370, 470), "white"); d = ImageDraw.Draw(c)
        if t["kind"] == "T":
            b = bands[t["leaf"]][f"{t['leaf']}_{t['line']}_{t['seg']}.jpg"]; x = b[0] + t["x"] // 2
            w = nat[t["leaf"]].crop((x - 60, b[1], x + 60, b[3])).resize((360, 3 * (b[3] - b[1]))); mx = 5 + 180
            key.append(f"Z{n:02d}\tT\t{t['leaf']}\t{t['line']}\t{t['idx']}\t{t['letter']}\t{t['status']}\tSTRAY")
        else:
            im = Image.open(t["crop"]).convert("RGB"); x0 = max(0, min(im.width - 360, t["x"] - 180))
            w = im.crop((x0, 0, x0 + 360, im.height)); mx = 5 + (t["x"] - x0)
            key.append(f"Z{n:02d}\tC\t{t['h212']}\t{t['line']}\t-\t-\t-\t{t['group']}")
        c.paste(w, (5, 20)); y = 20 + w.height
        d.polygon([(mx - 8, 2), (mx + 8, 2), (mx, 17)], fill=(220, 0, 0)); d.polygon([(mx - 8, y + 18), (mx + 8, y + 18), (mx, y + 3)], fill=(220, 0, 0))
        d.text((330, 4), f"Z{n:02d}", fill=(0, 0, 0)); ims.append(c)
    for s0 in range(0, len(ims), 20):
        sh = Image.new("RGB", (4 * 370, 5 * 470), "white")
        for k, c in enumerate(ims[s0:s0 + 20]): sh.paste(c, ((k % 4) * 370, (k // 4) * 470))
        sh.save(f"{scratch}/h226/sheet_{s0 // 20 + 1:02d}.jpg", quality=88)
    open(f"{HERE}/h226_items.tsv", "w").write("\n".join(key) + "\n")
    print(len(its), "tiles; strays f188r", len(s188), "f101r", len(s101), Counter(t["kind"] for t in its))
def score():
    import h190_4fam as h190
    its = rd(f"{HERE}/h226_items.tsv"); ans = {r["id"]: r["answer"].strip().upper() for r in rd(f"{P}/h226_reply.tsv")}
    C = [r for r in its if r["kind"] == "C"]; hit = sum(ans.get(r["item"]) == r["group"] for r in C)
    out = [f"anchor control: {hit} of {len(C)} H212 tiles answered as their H212 group (gate >= 8): {'PASS' if hit >= 8 else 'CONTROL FAIL'}",
           "anchor answers: A " + " ".join(ans.get(r["item"], "-") for r in C if r["group"] == "A") + " | B " + " ".join(ans.get(r["item"], "-") for r in C if r["group"] == "B")]
    if hit >= 8:
        T = [r for r in its if r["kind"] == "T"]
        for leaf in ("f101r", "f188r", None):
            rows = [r for r in T if leaf is None or r["ref"] == leaf]; c = Counter(ans.get(r["item"], "N") for r in rows)
            out.append(f"strays {leaf or 'pooled'}: " + " ".join(f"{k} {c.get(k, 0)}" for k in "ABCDN") + "  by letter: " +
                       " ".join(f"{r['letter']}:{ans.get(r['item'], 'N')}" for r in sorted(rows, key=lambda r: r["letter"])))
        c = Counter(ans.get(r["item"], "N") for r in T); a = c.get("A", 0); na = len(T) - a; share = na / max(1, len(T))
        p = h190.fisher(na, a, 3, 23)
        verdict = ("the strays sit on other shapes" if share >= 0.5 and p < 0.01 else "the strays are the 4-head (letters misplaced or a wider cell)" if share <= 0.2 else "mixed")
        out.append(f"read-out: stray non-A share {share:.2f} ({na}/{len(T)}), reference d/q non-A 3/26; Fisher p {p:.2g} -> {verdict}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h226_hash4_strays_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(*sys.argv[2:5]) if sys.argv[1] == "tiles" else score()
