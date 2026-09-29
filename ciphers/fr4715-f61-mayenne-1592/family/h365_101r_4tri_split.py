#!/usr/bin/env python3
"""H365 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), written before the calls: H360's full split on fr.3982 f.101r -- H360's
code with the leaf swapped (f101r_signsA.tsv, sheets/f101r_bands.json, row centre box top + 80, native images/3982_f101r.jpg, recf101r) and H362's
70 items as the already-answered set (gate 17/20 passed). tiles: the other agreed 4TRI tokens, seed 365, 4 chunks, SCRATCH/h365_cK; key h365_items.tsv;
replies passes/h365_reply_cK.tsv. score adds H364's cross-tab (period letter by bowl answer) at full N before H360's split order gain and H344
shuffled-target control. Pre-stated: as H360 (the split raises the order gain iff higher under all three seeds AND 0/3 shuffled targets signal) and
as H364 (bowl-letter agreement >= 0.75 tracks). No cell change.   python3 h365_101r_4tri_split.py tiles SCRATCH | score [--check]"""
import csv, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; sys.path.insert(0, HERE)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def pool():
    import h359_bowl_124r as h
    drop = set(); A = {(r["line"], r["pos"]): r for r in rd(f"{P}/f101r_signsA.tsv")}
    import json; B = json.load(open(f"{HERE}/sheets/f101r_bands.json"))["boxes"]; out = []
    for r in rd(f"{P}/recf101r/ciphertext_draft.tsv"):
        if r["sign"] != "4TRI" or not r["why"].startswith("agree"): continue
        a = A.get((r["line"], r["position"]))
        if not a or a["sign"] != "4TRI" or (a["line"], a["segment"]) in drop: continue
        bx = B[f"f101r_{a['line']}_{a['segment']}.jpg"]; out.append(("4TRI", r["line"], r["position"], bx[0] + int(float(a["x_px"])) // 2, bx[1] + 80))
    done = {(r["line"], r["pos"]) for r in rd(f"{HERE}/h362_items.tsv")}
    rest = [t for t in out if (t[1], t[2]) not in done]; random.Random(365).shuffle(rest); return rest
def tiles(scratch):
    from PIL import Image, ImageDraw
    rest = pool(); nat = Image.open(f"{HERE}/images/3982_f101r.jpg").convert("RGB"); k = 4; size = -(-len(rest) // k)
    key = ["chunk\titem\tcode\tline\tpos\tx_native\ty_centre"]
    for c in range(k):
        its = rest[c * size:(c + 1) * size]; d0 = f"{scratch}/h365_c{c + 1}"; os.makedirs(d0, exist_ok=True); ims = []
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
    open(f"{HERE}/h365_items.tsv", "w").write("\n".join(key) + "\n")
def gate(ans):
    ctl = {r["item"]: r for r in rd(f"{HERE}/h193_items.tsv")}
    return sum((ans.get(m) == "yes") == (r["group"] == "CP") and ans.get(m) in ("yes", "no") for m, r in ctl.items() if r["group"] in ("CP", "AN"))
def score():
    out = []; lab = {}
    a359 = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h362_reply.tsv")}
    for r in rd(f"{HERE}/h362_items.tsv"):
        if r["code"] == "4TRI": lab[(r["line"], r["pos"])] = a359.get(r["item"], "missing")
    items = rd(f"{HERE}/h365_items.tsv")
    for c in sorted({r["chunk"] for r in items}):
        f = f"{P}/h365_reply_{c}.tsv"
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
    out.append(f"4TRI answers used (H362 + passing chunks): {len(lab)}; {' '.join(f'{k} {v}' for k, v in sorted(tot.items()))}")
    os.makedirs(f"{P}/recf101r_split", exist_ok=True); rows = list(open(f"{P}/recf101r/ciphertext_draft.tsv")); hdr = rows[0]; new = [hdr]; nrel = 0
    for l in rows[1:]:
        c = l.rstrip("\n").split("\t")
        if c[2] == "4TRI" and lab.get((c[0], c[1])) == "no": c[2] = "C43"; nrel += 1
        new.append("\t".join(c) + "\n")
    open(f"{P}/recf101r_split/ciphertext_draft.tsv", "w").write("".join(new)); out.append(f"split draft: {nrel} 4TRI tokens relabelled C43")
    h364 = open(f"{HERE}/h364_101r_bowl_letter.py").read(); h364 = h364[:h364.index("ans = {r")]
    gl = {"__file__": f"{HERE}/h364_101r_bowl_letter.py", "__name__": "h365l"}; exec(compile(h364, "h364_prefix", "exec"), gl); letter = gl["letter"]
    cls = lambda L: "c/p/t" if L in ("c", "p", "t") else "a/n" if L in ("a", "n") else "other"; tab = {}
    for k, a_ in lab.items():
        L = letter.get(k); kk = (a_, cls(L) if L else "none"); tab[kk] = tab.get(kk, 0) + 1
    out.append("period letter by bowl (all answered 4TRI): " + " ".join(f"{a_}:{c_} {v}" for (a_, c_), v in sorted(tab.items())))
    ag = tab.get(("yes", "c/p/t"), 0) + tab.get(("no", "a/n"), 0); nn = sum(v for (a_, c_), v in tab.items() if a_ in ("yes", "no") and c_ in ("c/p/t", "a/n"))
    out.append(f"bowl-letter agreement over 4TRI {ag}/{nn} = {ag / nn if nn else 0:.2f} (H364's bar 0.75 tracks, < 0.6 does not)")
    h347 = open(f"{HERE}/h347_seqgain_v6v7.py").read(); src = open(f"{HERE}/h335_106r_v7_beam.py").read(); src = src[:src.index("real = score(cell)")]
    def gains(prefix):
        g = {"__file__": f"{HERE}/h335_106r_v7_beam.py", "__name__": "h360"}; sys.argv = [sys.argv[0]]
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
    g0, g1 = gains("recf101r"), gains("recf101r_split"); d = [b - a for a, b in zip(g0, g1)]
    h344 = open(f"{HERE}/h344_seqgain_shuftarget.py").read().replace('("recf101r", "recf188r", "recf124r", "recf97r", "rec108v", "recf108vg")', '("recf101r_split",)')
    h344 = h344[:h344.index('txt = "\\n".join(out)')]; g2 = {"__file__": f"{HERE}/h344_seqgain_shuftarget.py", "__name__": "h360b"}; sys.argv = [sys.argv[0]]
    exec(compile(h344, "h344_on_split", "exec"), g2); clean = not g2["void"]
    f = lambda v: "/".join(f"{x:.4f}" for x in v)
    out.append(f"order gain v7: as transcribed {f(g0)}; split {f(g1)}; H344 on split: {g2['out'][0].split(': ', 1)[1]}")
    ro = "the split raises the order gain" if all(x > 0 for x in d) and clean else "lowers" if all(x < 0 for x in d) else "unclear"
    out.append(f"read-out: {ro}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h365_101r_4tri_split_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(sys.argv[2]) if sys.argv[1] == "tiles" else score()
