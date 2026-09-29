#!/usr/bin/env python3
"""H243 (runner 9 session_012NTadgrCBftz3oRtgw5jFu, 29 Sept 2026): desk pack (H96's recipe) for a person's read of fr.3983 f.106r's period gloss above the
HASH4 signs H221 shape-read (looped B 13, 4-head A 4). For each cut row with such a sign: the native band (sheets/f106r_bands.json, union of the row's
segment boxes, from 60 px above the box top to its bottom, so the interlined gloss shows), scaled 1.5, every HASH4 marked by a blue arrow just under the sign with a guide line down to its number (N01..; the
key images/person_pack_106r/key.tsv says which are looped; the README does not). No reading.  python3 h243_pack_106r.py NATIVE106"""
import csv, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; sys.path.insert(0, HERE)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def main(native):
    from PIL import Image, ImageDraw
    import h221_shapes_106r as h221
    T = {(t["line"], t["pos"]): t for t in h221.targets()}; B = json.load(open(f"{HERE}/sheets/f106r_bands.json"))["boxes"]
    pos = [r for r in rd(f"{HERE}/h221_positions.tsv") if r["set"] == "h221h" and r["code"] == "HASH4" and r["answer"] in ("A", "B")]
    from PIL import ImageFont
    try: F = ImageFont.load_default(size=26)
    except TypeError: F = ImageFont.load_default()
    out = f"{HERE}/images/person_pack_106r"; os.makedirs(out, exist_ok=True); nat = Image.open(native).convert("RGB"); key = ["number\tline\tpos\tform"]; n = 0
    for line in sorted({r["line"] for r in pos}):
        bx = [v for k, v in B.items() if k.startswith(f"f106r_{line}_")]; x0 = min(b[0] for b in bx); x1 = max(b[2] for b in bx); y0 = min(b[1] for b in bx) - 60; y1 = max(b[3] for b in bx)
        s = 1.5; im = nat.crop((x0, y0, x1, y1)); im = im.resize((int(im.width * s), int(im.height * s))); c = Image.new("RGB", (im.width, im.height + 40), "white"); c.paste(im, (0, 0)); d = ImageDraw.Draw(c)
        for r in sorted((r for r in pos if r["line"] == line), key=lambda r: T[(r["line"], r["pos"])]["x"] // 3 + B[f"f106r_{line}_{T[(r['line'], r['pos'])]['seg']}.jpg"][0]):
            t = T[(r["line"], r["pos"])]; b = B[f"f106r_{line}_{t['seg']}.jpg"]; x = int((b[0] + t["x"] // 3 - x0) * s); n += 1
            ys = int((b[1] + 78 - y0) * s)   # the sign row's centre (cut_bands --up 78)
            d.line([(x, ys + 25), (x, im.height + 4)], fill=(0, 0, 220), width=2); d.polygon([(x - 9, ys + 40), (x + 9, ys + 40), (x, ys + 24)], fill=(0, 0, 220))
            d.text((x - 16, im.height + 8), f"N{n:02d}", fill=(0, 0, 220), font=F)
            key.append(f"N{n:02d}\t{line}\t{r['pos']}\t{'looped' if r['answer'] == 'B' else '4-head'}")
        c.save(f"{out}/f106r_{line}.jpg", quality=82)
    open(f"{out}/key.tsv", "w").write("\n".join(key) + "\n"); print(n, "numbered signs")
if __name__ == "__main__": main(sys.argv[1])
