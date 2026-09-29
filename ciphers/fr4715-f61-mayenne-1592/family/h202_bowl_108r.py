#!/usr/bin/env python3
"""H202 (runner 8 session_011Taenrv3JSdk7VjpiBjids, 29 Sept 2026): H193's bowl question at fr.3983 f.108r's 4-family positions whose letter is
known from the leaf's own period interlinear decipherment (Tomokiyo's overlay reprint, scripts/tomokiyo_spans_3983.tsv, grade C for this test).
Written before the call.
 tiles SCRATCH: the overlay letters (T1 -> row L02, T2 -> row L03) are aligned to pass A's sign sequence (scripts/pass108A_classes.tsv) with
   f61crib.align under key v5 form A (build_key_v5.load_key_v5(ebr='A')), as build_key_v5's f.108r check does. Targets: every aligned pair whose
   pass-A code is a 4-family code (4TRI, C43, 4STEM, 4PI), whatever its letter (dry run: 20 pairs, 16 with c/p/a/n, 4 with d). Each is a 300-px
   window of images/f108sheetB_<row>.jpg at pass A's (segment, x_px) (the sheet stacks four segment bands with 12-px black separators; the bands
   keep the descenders), scaled 1.2, red triangle UNDER the sign (as the H193 strips), numbered S01.., shuffled (seed 202), one sheet
   <scratch>/h202/sheet_01.jpg. Key h202_items.tsv (item, row, pos, code, letter) committed before the call. Repeat control = H193's 60 strips.
 score: GATE repeat control >= 17 of 20 f.176v anchors in their group's direction, else CONTROL FAIL. Then bowl yes/no vs letter {c,p} vs {a,n},
   Fisher exact test; 'd' positions (4PI) listed apart. Pre-stated read-out: "bowl = c/p holds at f.108r's period letters" iff every answered c/p
   position is yes, at most one answered a/n position is yes, and Fisher p < 0.05. Skip if fewer than 6 c/p/a/n positions. Caveat: the
   alignment is made under a key whose 4-family cells follow the readers' codes, so pairs can follow codes; the bowl answer is blind to both.
  python3 h202_bowl_108r.py tiles SCRATCH | score [--check]"""
import csv, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); S = os.path.abspath(f"{HERE}/../scripts"); IM = os.path.abspath(f"{HERE}/../images")
sys.path.insert(0, HERE); sys.path.insert(0, S)
FAM = ("4TRI", "C43", "4STEM", "4PI")
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def pairs():
    import build_key_v5 as b
    from f61crib import align
    k = b.load_key_v5(ebr="A"); A = {}
    for r in rd(f"{S}/pass108A_classes.tsv"): A.setdefault(r["line"], []).append(r)
    out = []
    for s, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{S}/tomokiyo_spans_3983.tsv") if l[0] == "T"):
        row = "L02" if s == "T1" else "L03"; seq = [r["sign"] for r in A[row]]; mm = m.translate(b.FOLD)
        for i, j in align(mm, seq, k)[1]:
            if seq[j] in FAM: out.append(dict(row=row, pos=A[row][j]["pos"], code=seq[j], letter=mm[i], seg=int(A[row][j]["segment"]), x=int(A[row][j]["x_px"])))
    return out
def tiles(scratch):
    from PIL import Image, ImageDraw
    ts = pairs(); random.Random(202).shuffle(ts); os.makedirs(f"{scratch}/h202", exist_ok=True); ims = []; key = ["item\trow\tpos\tcode\tletter"]
    for n, t in enumerate(ts, 1):
        im = Image.open(f"{IM}/f108sheetB_{t['row']}.jpg").convert("RGB"); st = (im.height + 12) // 4; y0 = (t["seg"] - 1) * st; y1 = y0 + st - 12
        x0 = max(0, min(im.width - 300, t["x"] - 150)); w = im.crop((x0, y0, x0 + 300, y1)); s = 150 / w.height if w.height * 1.2 > 150 else 1.2
        w = w.resize((int(300 * s), int(w.height * s)))
        c = Image.new("RGB", (370, 190), "white"); c.paste(w, (5, 0)); d = ImageDraw.Draw(c); mx = 5 + int((t["x"] - x0) * s); y = w.height
        d.polygon([(mx - 9, y + 16), (mx + 9, y + 16), (mx, y + 2)], fill=(220, 0, 0)); d.text((6, y + 20), f"S{n:02d}", fill=(0, 0, 0))
        ims.append(c); key.append(f"S{n:02d}\t{t['row']}\t{t['pos']}\t{t['code']}\t{t['letter']}")
    sh = Image.new("RGB", (4 * 370, 5 * 190), "white")
    for k, c in enumerate(ims): sh.paste(c, ((k % 4) * 370, (k // 4) * 190))
    sh.save(f"{scratch}/h202/sheet_01.jpg", quality=88)
    open(f"{HERE}/h202_items.tsv", "w").write("\n".join(key) + "\n"); print(len(ts), "targets")
def score():
    import h190_4fam as h190
    ctl = {r["item"]: r for r in rd(f"{HERE}/h193_items.tsv")}; ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{HERE}/passes/h202_reply.tsv")}
    hit = sum((ans.get(m) == "yes") == (r["group"] == "CP") and ans.get(m) in ("yes", "no") for m, r in ctl.items() if r["group"] in ("CP", "AN"))
    out = [f"repeat control: {hit} of 20 f.176v anchors in their group's direction (gate >= 17): {'PASS' if hit >= 17 else 'CONTROL FAIL'}"]
    if hit >= 17:
        its = rd(f"{HERE}/h202_items.tsv"); out.append("item\trow\tpos\tcode\tletter\tbowl")
        tab = {"yes": [0, 0], "no": [0, 0]}
        for r in sorted(its, key=lambda r: (r["row"], int(r["pos"]))):
            a = ans.get(r["item"], "missing"); out.append(f"{r['item']}\t{r['row']}\t{r['pos']}\t{r['code']}\t{r['letter']}\t{a}")
            if a in tab and r["letter"] in "cpan": tab[a][0 if r["letter"] in "cp" else 1] += 1
        ncpan = sum(1 for r in its if r["letter"] in "cpan")
        if ncpan < 6: out.append(f"fewer than 6 c/p/a/n positions ({ncpan}): not tested")
        else:
            p = h190.fisher(tab["yes"][0], tab["yes"][1], tab["no"][0], tab["no"][1])
            out.append(f"bowl yes: c/p {tab['yes'][0]} a/n {tab['yes'][1]}; bowl no: c/p {tab['no'][0]} a/n {tab['no'][1]}; Fisher p {p:.2g}")
            ok = tab["no"][0] == 0 and tab["yes"][1] <= 1 and p < 0.05
            out.append("read-out: " + ("bowl = c/p holds at f.108r's period letters" if ok else "bowl = c/p not shown at f.108r's period letters"))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h202_bowl_108r_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(sys.argv[2]) if sys.argv[1] == "tiles" else score()
