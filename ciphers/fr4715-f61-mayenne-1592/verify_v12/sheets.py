#!/usr/bin/env python3
"""VERIFY-F61-V12: build the reader's sheets from my own tiles (cut.py) with random item ids, seed fixed.
Calls: C1 (claims 1, 2-class, 4, L05/1; anchors, repeats; Part B = no-BETA panel), C2 (out-of-span QA, claim 3).
The answer key is written OUTSIDE the repository (scratchpad) until the replies are in, and its sha256 is recorded in PREREG.md;
it is copied into verify_v12/ after scoring.  python3 sheets.py KEYDIR"""
import csv, hashlib, os, random, sys
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); T = f"{HERE}/tiles"; OUT = f"{HERE}/sheets"
REFS = [("L11", "1", "BETA"), ("L03", "8", "C43"), ("L11", "11", "ZHOOK"), ("L08", "11", "4TRI"), ("L08", "3", "C6"), ("L08", "1", "PHI"),
        ("L11", "3", "EBR"), ("L08", "5", "SBS"), ("L03", "12", "LOOPBAR"), ("L11", "6", "VBAR_A"), ("L08", "10", "CA"), ("L08", "4", "INF"),
        ("L03", "5", "VBAR_B"), ("L07", "10", "CROSS"), ("L11", "9", "4PI")]
RID = {c: f"R{i+1}" for i, (_, _, c) in enumerate(REFS)}
def rows(): return [r for r in csv.DictReader((l for l in open(f"{HERE}/v12_positions.tsv") if not l.startswith("#")), delimiter="\t")]
def expect(r):
    if r["code"] == "PUNCT": return "P"
    return RID.get(r["code"], "N")
def sheet(items, path, cols=5, label_fn=lambda i: i[0]):
    ims = [Image.open(f"{T}/{it[1]}.png") for it in items]; w = 230; h = 245
    s = Image.new("RGB", (cols * w, ((len(items) + cols - 1) // cols) * h), "white"); d = ImageDraw.Draw(s)
    for k, (it, im) in enumerate(zip(items, ims)):
        im = im.resize((min(220, int(im.width * 190 / im.height)), 190)); x = (k % cols) * w; y = (k // cols) * h
        s.paste(im, (x + 5, y + 5)); d.rectangle((x + 4, y + 4, x + 5 + im.width, y + 195), outline="grey")
        d.text((x + 8, y + 205), label_fn(it), fill="black")
    s = s.resize((s.width * 1, s.height * 1)); s.save(path)
def main():
    keydir = sys.argv[1]; os.makedirs(OUT, exist_ok=True); os.makedirs(keydir, exist_ok=True)
    rng = random.Random(20260929 + 12); R = {(r["line"], r["pos"]): r for r in rows()}
    sheet([(RID[c], f"{l}_{p}_W1") for l, p, c in REFS], f"{OUT}/C_refs.png", cols=5)
    ids = set()
    def nid():
        while True:
            s = "".join(rng.choice("BCDFGHJKLMNPQRSTVWXZ") for _ in range(3))
            if s not in ids: ids.add(s); return s
    key = []
    # C1 part A
    a = []
    for (l, p), tg in ((("L07", "4"), "T1"), (("L03", "16"), "T2"), (("L05", "1"), "T3"), (("L02", "2"), "T4"), (("L04", "2"), "T4")):
        for w in ("W1", "W2", "W3"): a.append((tg, l, p, w, "?"))
    anc = [r for r in rows() if r["role"] == "anchor"]
    for i, r in enumerate(anc): a.append(("anchor", r["line"], r["pos"], "W1" if i % 2 == 0 else "W2", expect(r)))
    for l, p in (("L05", "9"), ("L03", "4"), ("L07", "5"), ("L03", "14")): a.append(("repeat", l, p, "W3", expect(R[(l, p)])))
    for w in ("W2", "W3"): a.append(("betactl", "L11", "1", w, "R1"))
    rng.shuffle(a); a = [(nid(),) + x for x in a]
    b = [("partB", "L07", "4", "W2", "?"), ("partB", "L11", "1", "W3", "not R2"), ("partB", "L05", "9", "W3", "R2")]; rng.shuffle(b); b = [(nid(),) + x for x in b]
    for n in range(0, len(a), 10): sheet([(x[0], f"{x[2]}_{x[3]}_{x[4]}") for x in a[n:n + 10]], f"{OUT}/C1_A{n // 10 + 1}.png")
    sheet([(x[0], f"{x[2]}_{x[3]}_{x[4]}") for x in b], f"{OUT}/C1_B.png")
    key += [("C1A",) + x for x in a] + [("C1B",) + x for x in b]
    # C2
    c = [("oos", r["line"], r["pos"], "W1", expect(r)) for r in rows() if r["role"] == "oos"]
    anc2 = [r for r in anc if r["code"] != "PUNCT"]; rng.shuffle(anc2)
    c += [("anchor", r["line"], r["pos"], "W3", expect(r)) for r in anc2[:8]]
    c += [("t3", "L05", "1", "W2", "?")]
    c += [("repeat", r["line"], r["pos"], "W2", expect(r)) for r in rows() if (r["line"], r["pos"]) in (("L10", "3"), ("L01", "8"), ("L10", "8"))]
    rng.shuffle(c); c = [(nid(),) + x for x in c]
    for n in range(0, len(c), 10): sheet([(x[0], f"{x[2]}_{x[3]}_{x[4]}") for x in c[n:n + 10]], f"{OUT}/C2_{n // 10 + 1}.png")
    key += [("C2",) + x for x in c]
    kp = f"{keydir}/v12_key.tsv"
    with open(kp, "w") as f:
        f.write("call\tid\trole\tline\tpos\twindow\texpected\n")
        for k in key: f.write("\t".join(k) + "\n")
    print("items C1A", len(a), "C1B", len(b), "C2", len(c), "key sha256", hashlib.sha256(open(kp, "rb").read()).hexdigest())
if __name__ == "__main__": main()
