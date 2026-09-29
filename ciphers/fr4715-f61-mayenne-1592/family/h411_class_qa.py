#!/usr/bin/env python3
"""H411, adapted from H410 (runner 15 session_01BDhspZ38TdrrXYSvLPTpjc, 29 Sept 2026), written before the call: H410's design on f.61's other
out-of-span signs -- L01/1-2, L01/7-12, L03/1-3, L05/1-2, L11/8 (no position data exists for L02 or L04) -- against 12 references from f.61
(H410's 8 plus CROSS L07/10, 4PI L11/9, C43 L03/8, LOOPBAR L03/12). Classes with no second token on f.61 (ELOOP, HASH4, 4STEM, LOOPSTEM1, CH)
have no reference: for them the pre-stated confirmation is 'none'. H367 tile geometry (300 native px, x1.2, marker ABOVE, window -45/+92) from the native region image.
 references R1..R12 (fixed order): EBR L03/15, PHI L01/5, VBAR_A L03/6, SBS L03/14, VBAR_B L03/5, INF L01/4, C6 L03/11, CA L05/7, CROSS L07/10,
   4PI L11/9, C43 L03/8, LOOPBAR L03/12.
 known (2 per class): EBR L07/5 L11/3; PHI L05/15 L08/6; VBAR_A L05/3 L11/6; SBS L05/5 L08/5; VBAR_B L05/18 L07/9; INF L05/10 L08/4; C6 L05/12 L08/3;
   CA L03/9 L08/10 (H410's 16) + C43 L05/9 L08/2 = 18.  items shuffled (seed 411), I01..I32.
 score -- GATE >= 16/18 known items name their class's reference. Pre-stated per target: the reference of its reader code -> 'confirmed';
   another reference -> 'flagged <class>'; none -> 'flagged none'; n -> 'unclear'. Read-out: counts. Transcription QA; no key/grade change.
 python3 h411_class_qa.py tiles SCRATCH | score [--check]"""
import csv, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.abspath(f"{HERE}/.."); P = f"{HERE}/passes"; sys.path.insert(0, f"{T}/verify_v9"); sys.path.insert(0, HERE)
CHECK = "--check" in sys.argv
REFS = [("EBR", "L03", "15"), ("PHI", "L01", "5"), ("VBAR_A", "L03", "6"), ("SBS", "L03", "14"), ("VBAR_B", "L03", "5"), ("INF", "L01", "4"), ("C6", "L03", "11"), ("CA", "L05", "7"),
        ("CROSS", "L07", "10"), ("4PI", "L11", "9"), ("C43", "L03", "8"), ("LOOPBAR", "L03", "12")]
TARGETS = [("L01", "1"), ("L01", "2"), ("L01", "7"), ("L01", "8"), ("L01", "9"), ("L01", "10"), ("L01", "11"), ("L01", "12"), ("L03", "1"), ("L03", "2"), ("L03", "3"),
           ("L05", "1"), ("L05", "2"), ("L11", "8")]
KNOWN = [("EBR", "L07", "5"), ("EBR", "L11", "3"), ("PHI", "L05", "15"), ("PHI", "L08", "6"), ("VBAR_A", "L05", "3"), ("VBAR_A", "L11", "6"), ("SBS", "L05", "5"), ("SBS", "L08", "5"),
         ("VBAR_B", "L05", "18"), ("VBAR_B", "L07", "9"), ("INF", "L05", "10"), ("INF", "L08", "4"), ("C6", "L05", "12"), ("C6", "L08", "3"), ("CA", "L03", "9"), ("CA", "L08", "10"), ("C43", "L05", "9"), ("C43", "L08", "2")]
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def geo():
    import v9_ca_sort as v
    B = v.bands(); out = {}
    for f, sh in (("f61_positions_all.tsv", "A"), ("f61_positions_L10.tsv", "B")):
        for r in rd(f"{T}/scripts/{f}"):
            x = round(v.nat_x(sh, r["line"], int(r["segment"]), int(r["x"]))); b = v.band_of(B, r["line"], x); out[(r["line"], r["pos"])] = (r["class"], x, (b[1] + b[3]) // 2)
    return out
def tiles(scratch):
    from PIL import Image
    import h407_span_miss as h
    G = geo(); im = Image.open(h.REG).convert("RGB"); os.makedirs(f"{scratch}/h411", exist_ok=True)
    for c, l, p in REFS: assert G[(l, p)][0] == c, (c, l, p, G[(l, p)][0])
    for c, l, p in KNOWN: assert G[(l, p)][0] == c, (c, l, p, G[(l, p)][0])
    refs = [h.strip(im, G[(l, p)][1], G[(l, p)][2], 45, 92, f"R{k}") for k, (c, l, p) in enumerate(REFS, 1)]
    sh = Image.new("RGB", (4 * 370, 3 * 190), "white"); [sh.paste(c, ((k % 4) * 370, (k // 4) * 190)) for k, c in enumerate(refs)]; sh.save(f"{scratch}/h411/references.jpg", quality=90)
    its = [("T", G[k][0], *k) for k in TARGETS] + [("K", c, l, p) for c, l, p in KNOWN]; random.Random(411).shuffle(its)
    key = ["item\tkind\tcode\tline\tpos\tref"]; ims = []
    for n, (kind, c, l, p) in enumerate(its, 1):
        _, x, yc = G[(l, p)]; ims.append(h.strip(im, x, yc, 45, 92, f"I{n:02d}")); cl = [r[0] for r in REFS]; key.append(f"I{n:02d}\t{kind}\t{c}\t{l}\t{p}\t{'R' + str(cl.index(c) + 1) if c in cl else 'NONE'}")
    for s in range(0, len(ims), 20):
        sh = Image.new("RGB", (4 * 370, 5 * 190), "white"); [sh.paste(c, ((k % 4) * 370, (k // 4) * 190)) for k, c in enumerate(ims[s:s + 20])]; sh.save(f"{scratch}/h411/items_{s // 20 + 1:02d}.jpg", quality=90)
    open(f"{HERE}/h411_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "items")
def score():
    ans = {r["id"]: r["answer"].strip().upper() for r in rd(f"{P}/h411_reply.tsv")}; it = rd(f"{HERE}/h411_items.tsv")
    kn = [r for r in it if r["kind"] == "K"]; g = sum(ans.get(r["item"]) == r["ref"] for r in kn)
    out = [f"gate: {g}/18 known in-span items name their class's reference (>= 16)"]
    if g < 16: out.append("CONTROL FAIL -- nothing scored")
    else:
        names = {f"R{k}": c for k, (c, _, _) in enumerate(REFS, 1)}; res = []
        for r in sorted((r for r in it if r["kind"] == "T"), key=lambda r: (r["line"], int(r["pos"]))):
            a = ans.get(r["item"], "missing"); ro = "confirmed" if a == r["ref"] else "unclear" if a == "N" else f"flagged {names.get(a, a.lower())}"
            res.append((r["line"] + "/" + r["pos"], r["code"], a, ro))
        from collections import Counter
        cnt = Counter(x[3].split()[0] for x in res)
        out.append("targets: " + " ".join(f"{p}:{c}>{a}({ro})" for p, c, a, ro in res))
        out.append(f"read-out: confirmed {cnt['confirmed']}, flagged {cnt['flagged']}, unclear {cnt['unclear']} of {len(res)}")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h411_class_qa_result.txt"
    if CHECK:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    a = sys.argv[1:]
    tiles(a[1]) if a[0] == "tiles" else score()
