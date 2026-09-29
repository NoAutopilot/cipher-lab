#!/usr/bin/env python3
"""H371 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026), written before the calls: H370 found f.97r's agreed 4TRI 0.59 no-bowl (gate 19/20),
so H360's full split on fr.3982 f.97r (de Diou, HELD leaf with an order signal for v7, H342/H344) -- a second held-leaf replication of H360.
 tiles SCRATCH NATIVE: h370_bowl_97r.pool()'s 4TRI tokens (recut rows L17-L43, agreed or agreed-flagged, pass A matching, drop crops excluded) minus
   H370's 50, cut exactly as H370/H359 (marker above), shuffled (seed 371), split into 2 chunks (c1, c2), R01.. per chunk, 20 per sheet, into
   SCRATCH/h371_cK/; key h371_items.tsv. Each chunk is one blind Opus call with H359's prompt (H193's 60 strips as part 1). Native canvas 202, sha1 87d4236c.
 score: H360's scoring code unchanged except the leaf (recf97r) and H370's answers in place of H359's: per chunk GATE >= 17/20; the split draft
   passes/recf97r_split/ciphertext_draft.tsv relabels every answered-'no' 4TRI token as C43 (rows L01-L16 were not bowl-read and stay as transcribed);
   H342's order gain for v7 on the split vs the as-transcribed draft, three within-run shuffle seeds (342/343/344), and H344's shuffled-target control
   on the split draft. Pre-stated as H360: 'the split raises the order gain' iff higher under all three seeds AND the shuffled targets show no order
   signal; 'lowers' iff lower under all three; else 'unclear'. A transcription test; no cell change.
   python3 h371_97r_4tri_split.py tiles SCRATCH NATIVE | score [--check]"""
import csv, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; sys.path.insert(0, HERE)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def pool():
    import h370_bowl_97r as h
    done = {(r["line"], r["pos"]) for r in rd(f"{HERE}/h370_items.tsv")}
    rest = [t for t in h.pool() if t[0] == "4TRI" and (t[1], t[2]) not in done]; random.Random(371).shuffle(rest); return rest
def tiles(scratch, native):
    from PIL import Image, ImageDraw
    rest = pool(); nat = Image.open(native).convert("RGB"); k = 2; size = -(-len(rest) // k)
    key = ["chunk\titem\tcode\tline\tpos\tx_native\ty_centre"]
    for c in range(k):
        its = rest[c * size:(c + 1) * size]; d0 = f"{scratch}/h371_c{c + 1}"; os.makedirs(d0, exist_ok=True); ims = []
        for n, (code, line, pos, x, yc) in enumerate(its, 1):
            t = nat.crop((x - 150, yc - 60, x + 150, yc + 55)); t = t.resize((360, int(t.height * 1.2)))
            cv = Image.new("RGB", (370, 190), "white"); cv.paste(t.crop((0, 0, 360, min(t.height, 165))), (5, 22)); d = ImageDraw.Draw(cv); mx = 5 + int(150 * 1.2)
            d.polygon([(mx - 9, 2), (mx + 9, 2), (mx, 18)], fill=(220, 0, 0)); d.text((330, 4), f"R{n:02d}", fill=(0, 0, 0)); ims.append(cv)
            key.append(f"c{c + 1}\tR{n:02d}\t{code}\t{line}\t{pos}\t{x}\t{yc}")
        for s in range(0, len(ims), 20):
            sh = Image.new("RGB", (4 * 370, 5 * 190), "white")
            for j, cv in enumerate(ims[s:s + 20]): sh.paste(cv, ((j % 4) * 370, (j // 4) * 190))
            sh.save(f"{d0}/sheet_{s // 20 + 1:02d}.jpg", quality=88)
        print(f"c{c + 1}: {len(its)} targets, {-(-len(its) // 20)} sheets")
    open(f"{HERE}/h371_items.tsv", "w").write("\n".join(key) + "\n")
def gate(ans):
    ctl = {r["item"]: r for r in rd(f"{HERE}/h193_items.tsv")}
    return sum((ans.get(m) == "yes") == (r["group"] == "CP") and ans.get(m) in ("yes", "no") for m, r in ctl.items() if r["group"] in ("CP", "AN"))
def score():
    out = []; lab = {}
    a370 = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h370_reply.tsv")}
    for r in rd(f"{HERE}/h370_items.tsv"):
        if r["code"] == "4TRI": lab[(r["line"], r["pos"])] = a370.get(r["item"], "missing")
    items = rd(f"{HERE}/h371_items.tsv")
    for c in sorted({r["chunk"] for r in items}):
        f = f"{P}/h371_reply_{c}.tsv"
        if not os.path.exists(f): out.append(f"{c}: no reply"); continue
        ans = {r["id"]: r["answer"].strip().lower() for r in rd(f)}; g = gate(ans); ok = g >= 17
        cnt = {}
        for r in items:
            if r["chunk"] == c:
                a = ans.get(r["item"], "missing"); cnt[a] = cnt.get(a, 0) + 1
                if ok: lab[(r["line"], r["pos"])] = a
        out.append(f"{c}: control {g}/20 {'PASS' if ok else 'CONTROL FAIL (answers not used)'}; answers {' '.join(f'{k} {v}' for k, v in sorted(cnt.items()))}")
    tot = {}
    for v in lab.values(): tot[v] = tot.get(v, 0) + 1
    out.append(f"4TRI answers used (H370 + passing chunks): {len(lab)}; {' '.join(f'{k} {v}' for k, v in sorted(tot.items()))}")
    os.makedirs(f"{P}/recf97r_split", exist_ok=True); rows = list(open(f"{P}/recf97r/ciphertext_draft.tsv")); hdr = rows[0]; new = [hdr]; nrel = 0
    for l in rows[1:]:
        c = l.rstrip("\n").split("\t")
        if c[2] == "4TRI" and lab.get((c[0], c[1])) == "no": c[2] = "C43"; nrel += 1
        new.append("\t".join(c) + "\n")
    open(f"{P}/recf97r_split/ciphertext_draft.tsv", "w").write("".join(new)); out.append(f"split draft: {nrel} 4TRI tokens relabelled C43")
    h347 = open(f"{HERE}/h347_seqgain_v6v7.py").read(); src = open(f"{HERE}/h335_106r_v7_beam.py").read(); src = src[:src.index("real = score(cell)")]
    def gains(prefix):
        g = {"__file__": f"{HERE}/h335_106r_v7_beam.py", "__name__": "h371"}; sys.argv = [sys.argv[0]]
        exec(compile(src.replace("recf106rall/", f"{prefix}/"), f"h335_on_{prefix}", "exec"), g)
        runs, cell, score_ = g["runs"], g["cell"], g["score"]; res = []
        for seed in (342, 343, 344):
            rng = random.Random(seed); ss = []
            for _ in range(10):
                s = []
                for r in runs: r2 = r[:]; rng.shuffle(r2); s.append(r2)
                ss.append(s)
            g["runs"] = runs; real = score_(cell); sh = []
            for s in ss: g["runs"] = s; sh.append(score_(cell))
            res.append(real - sum(sh) / len(sh))
        return res
    g0, g1 = gains("recf97r"), gains("recf97r_split"); d = [b - a for a, b in zip(g0, g1)]
    h344 = open(f"{HERE}/h344_seqgain_shuftarget.py").read().replace('("recf101r", "recf188r", "recf124r", "recf97r", "rec108v", "recf108vg")', '("recf97r_split",)')
    h344 = h344[:h344.index('txt = "\\n".join(out)')]; g2 = {"__file__": f"{HERE}/h344_seqgain_shuftarget.py", "__name__": "h371b"}; sys.argv = [sys.argv[0]]
    exec(compile(h344, "h344_on_split", "exec"), g2); clean = not g2["void"]
    f = lambda v: "/".join(f"{x:.4f}" for x in v)
    out.append(f"order gain v7: as transcribed {f(g0)}; split {f(g1)}; H344 on split: {g2['out'][0].split(': ', 1)[1]}")
    ro = "the split raises the order gain" if all(x > 0 for x in d) and clean else "lowers" if all(x < 0 for x in d) else "unclear"
    out.append(f"read-out: {ro}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h371_97r_4tri_split_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(sys.argv[2], sys.argv[3]) if sys.argv[1] == "tiles" else score()
