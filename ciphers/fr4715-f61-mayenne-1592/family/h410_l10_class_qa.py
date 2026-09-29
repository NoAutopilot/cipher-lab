#!/usr/bin/env python3
"""H410 (runner 15 session_01BDhspZ38TdrrXYSvLPTpjc, 29 Sept 2026), written before the call: a class check of f.61 L10's 13 signs (outside every
Tomokiyo span; positions scripts/f61_positions_L10.tsv, sheet-B x mapping) by forced choice against 8 reference signs cut from f.61's in-span
positions, with 16 known in-span items as the gate. H367 tile geometry (300 native px, x1.2, marker ABOVE, window -45/+92) from the native region image.
 references R1..R8 (fixed order): EBR L03/15, PHI L01/5, VBAR_A L03/6, SBS L03/14, VBAR_B L03/5, INF L01/4, C6 L03/11, CA L05/7.
 known (2 per class): EBR L07/5 L11/3; PHI L05/15 L08/6; VBAR_A L05/3 L11/6; SBS L05/5 L08/5; VBAR_B L05/18 L07/9; INF L05/10 L08/4; C6 L05/12 L08/3;
   CA L03/9 L08/10.  items shuffled (seed 410), I01..I29.
 score -- GATE >= 14/16 known items name their class's reference. Pre-stated per L10 position: the reference of its reader code -> 'confirmed';
   another reference -> 'flagged <class>'; none -> 'flagged none'; n -> 'unclear'. Read-out: counts. Transcription QA; no key/grade change.
 python3 h410_l10_class_qa.py tiles SCRATCH | score [--check]"""
import csv, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.abspath(f"{HERE}/.."); P = f"{HERE}/passes"; sys.path.insert(0, f"{T}/verify_v9"); sys.path.insert(0, HERE)
CHECK = "--check" in sys.argv
REFS = [("EBR", "L03", "15"), ("PHI", "L01", "5"), ("VBAR_A", "L03", "6"), ("SBS", "L03", "14"), ("VBAR_B", "L03", "5"), ("INF", "L01", "4"), ("C6", "L03", "11"), ("CA", "L05", "7")]
KNOWN = [("EBR", "L07", "5"), ("EBR", "L11", "3"), ("PHI", "L05", "15"), ("PHI", "L08", "6"), ("VBAR_A", "L05", "3"), ("VBAR_A", "L11", "6"), ("SBS", "L05", "5"), ("SBS", "L08", "5"),
         ("VBAR_B", "L05", "18"), ("VBAR_B", "L07", "9"), ("INF", "L05", "10"), ("INF", "L08", "4"), ("C6", "L05", "12"), ("C6", "L08", "3"), ("CA", "L03", "9"), ("CA", "L08", "10")]
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
    G = geo(); im = Image.open(h.REG).convert("RGB"); os.makedirs(f"{scratch}/h410", exist_ok=True)
    for c, l, p in REFS: assert G[(l, p)][0] == c, (c, l, p, G[(l, p)][0])
    for c, l, p in KNOWN: assert G[(l, p)][0] == c, (c, l, p, G[(l, p)][0])
    refs = [h.strip(im, G[(l, p)][1], G[(l, p)][2], 45, 92, f"R{k}") for k, (c, l, p) in enumerate(REFS, 1)]
    sh = Image.new("RGB", (4 * 370, 2 * 190), "white"); [sh.paste(c, ((k % 4) * 370, (k // 4) * 190)) for k, c in enumerate(refs)]; sh.save(f"{scratch}/h410/references.jpg", quality=90)
    its = [("T", G[("L10", str(p))][0], "L10", str(p)) for p in range(1, 14)] + [("K", c, l, p) for c, l, p in KNOWN]; random.Random(410).shuffle(its)
    key = ["item\tkind\tcode\tline\tpos\tref"]; ims = []
    for n, (kind, c, l, p) in enumerate(its, 1):
        _, x, yc = G[(l, p)]; ims.append(h.strip(im, x, yc, 45, 92, f"I{n:02d}")); key.append(f"I{n:02d}\t{kind}\t{c}\t{l}\t{p}\tR{[r[0] for r in REFS].index(c) + 1}")
    for s in range(0, len(ims), 20):
        sh = Image.new("RGB", (4 * 370, 5 * 190), "white"); [sh.paste(c, ((k % 4) * 370, (k // 4) * 190)) for k, c in enumerate(ims[s:s + 20])]; sh.save(f"{scratch}/h410/items_{s // 20 + 1:02d}.jpg", quality=90)
    open(f"{HERE}/h410_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "items")
def score():
    ans = {r["id"]: r["answer"].strip().upper() for r in rd(f"{P}/h410_reply.tsv")}; it = rd(f"{HERE}/h410_items.tsv")
    kn = [r for r in it if r["kind"] == "K"]; g = sum(ans.get(r["item"]) == r["ref"] for r in kn)
    out = [f"gate: {g}/16 known in-span items name their class's reference (>= 14)"]
    if g < 14: out.append("CONTROL FAIL -- nothing scored")
    else:
        names = {f"R{k}": c for k, (c, _, _) in enumerate(REFS, 1)}; res = []
        for r in sorted((r for r in it if r["kind"] == "T"), key=lambda r: int(r["pos"])):
            a = ans.get(r["item"], "missing"); ro = "confirmed" if a == r["ref"] else "unclear" if a == "N" else f"flagged {names.get(a, a.lower())}"
            res.append((r["pos"], r["code"], a, ro))
        from collections import Counter
        cnt = Counter(x[3].split()[0] for x in res)
        out.append("L10: " + " ".join(f"{p}:{c}>{a}({ro})" for p, c, a, ro in res))
        out.append(f"read-out: confirmed {cnt['confirmed']}, flagged {cnt['flagged']}, unclear {cnt['unclear']} of 13")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h410_l10_class_qa_result.txt"
    if CHECK:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    a = sys.argv[1:]
    tiles(a[1]) if a[0] == "tiles" else score()
