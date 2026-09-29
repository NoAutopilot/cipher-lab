#!/usr/bin/env python3
"""VERIFY-F61-V8 (verifier, account 3, 29 Sept 2026): independent audit of two shape cells runner 9 posted after VERIFY-F61-V7
(ROOM 05:48 and 05:51 UTC; family/v6_shape_candidates.tsv):
  (1) ZHOOK = the 2# sign (H235 f.61, H254 f.108r)  -> would link f.61's ZHOOK to the period i/x sign (H24 cell) by glyph;
  (2) 4PI is two signs (H233/H239/H240/H255): the 4-head hash (d/q) on f.101r/f.108r, and on f.61 a '4 over a Pi' that Tomokiyo's S5 reads n (a/n).
Written and committed BEFORE any vision call and before the verifier has looked at any tile or sheet. Categories fixed here, from the brief and
from H233's wording, before any look.

 tiles SCRATCH  (natives SCRATCH/f188r.jpg and SCRATCH/f101r.jpg, sha1 = MANIFEST, fetched 08:16 UTC; f.274r from family/images)
   Every tile is a CIPHER-ROW window about +-60 native px around the sign, grey + autocontrast, 360 px wide, red triangles above and below.
   PERIOD (lettered by the runner's period alignments, same files as V7):
     f.274r  every H24/HASH4 row lettered i/x/j/y or d/q (21)                         -> GATE (letter class, not any earlier reader's answer)
     f.188r, f.101r  every 4PI row with a letter whose pass-A sign is in the 4-family (4PI/HASH4/4STEM/4TRI/C43)  -> test P1
     f.188r, f.101r  6 H24 i/x + 6 HASH4 d/q each (seed 808), 4 C43 a/n each (distractor for E)
   MAYENNE HAND (f.61, f.108r; no period letters in view):
     f.61   ZHOOK 3 (H235 positions), 4PI 2 + HASH4 1 (H233 positions), C43 3 (H235 positions); from images/f61sheet_<L>.jpg
     f.108r ZHOOK 7 and 4PI 5 on L02/L03 (pass108A, images/f108sheetB_<L>.jpg, segments joined end to end so boundary signs are whole),
            every 4STEM and 4TRI on L02/L03 and 5 C43 (seed 808) as in-hand distractors; 4PI 4 on L04-L06 (f61recon108r_draft, cut from
            the stitched native with the f108g/f108h band boxes)
   8 tiles shown twice (seed 808) = repeat control. Three sheet sets, separate shuffles and ids:
     setF  (R1) and setG (R2): A 4-head hash / D 2# / E figure-4 on stems not crossed by hash bars / B looped hash / N other
     setN  (R3): A / B / N only (no D, no E), N answers with a few words describing the sign
   Key verify_v8/v8_items.tsv written by this command (letters and codes never on a sheet).
 Calls: three fresh blind Opus subagents, one per set, each told to open only its own sheets; prompts verbatim in PROMPTS.md.
 score (pre-stated):
   GATE per call: f.274r tiles, i/x -> D and d/q -> A (setF/G); i/x -> not A and d/q -> A (setN); >= 0.8, else CONTROL FAIL (call not scored).
   REPEAT per call: duplicates identical >= 6 of 8, else 'unstable' (verdict capped at 'in part').
   (1) ZHOOK
     Z1 shape only (no letters): ZHOOK D-share over the 10 Mayenne-hand ZHOOK tiles; in-hand distractor D-share (C43, 4STEM, 4TRI, 4PI, HASH4);
        within-leaf label permutation (20000, over f.61 and f.108r tiles) of S = #(ZHOOK & D) + #(other & not D).
        Read-out 'ZHOOK sorts with the 2#' iff in BOTH setF and setG: gate PASS, ZHOOK D-share >= 0.7, distractor D-share <= 0.2, p < 0.01,
        and f.61's own ZHOOK D in >= 2 of 3. 'f.108r only' if the f.108r ZHOOK clear it and f.61's do not.
     Z2 setN: ZHOOK not-A share; the words given for them (descriptive).
     Z3 letters (rests on Tomokiyo's overlay alignment): f.108r lettered tiles (L02/L03), S = #(D & i/x/j/y) + #(A & d/q), within-leaf permutation.
        The alignment itself is re-checked without the two codes under audit (align_check below).
   (2) 4PI
     P1 period leaves (rests on the runner's period alignments of f.188r/f.184r and f.101r): S = #(A & d/q) + #(E & a/n) over the lettered 4PI
        tiles, within-leaf permutation. Read-out 'two signs on the period leaves' iff p < 0.01 in both setF and setG and >= 3 E tiles with
        a/n share >= 0.6; '4PI period rows are the 4-head' iff A share >= 0.7 and E share < 0.15 in both.
     P2 Mayenne hand, shape only: f.108r 4PI A-share (9 tiles) vs f.61's two 4PI answered E; exact probability of both f.61 tokens landing
        in E given the E rate among all 4PI tiles in that call. Read-out 'f.61's 4PI is a different sign from f.108r's' iff in both setF and
        setG: both f.61 4PI E, f.108r 4PI A-share >= 0.7.
     P3 the a/n value for f.61's form: from P1's E tiles (period letters) if any; else it rests on Tomokiyo S5 alone (reported, not tested here).
   Verdicts: endorse / in part / reject per cell, by the read-outs above (a cell whose value rests only on one published letter is 'in part').
  python3 v8_shape_sort.py tiles SCRATCH | align_check | score [--check]"""
import csv, json, os, random, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); FAM = os.path.abspath(f"{HERE}/../family"); IM = os.path.abspath(f"{HERE}/../images")
SC = os.path.abspath(f"{HERE}/../scripts"); P = f"{FAM}/passes"
for p in (FAM, SC): sys.path.insert(0, p)
I = set("ixjy"); DQ = set("dq"); AN = set("an"); FAM4 = {"4PI", "HASH4", "4STEM", "4TRI", "C43", "H24"}
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
LEAF = {"188r": dict(draft="recf188r", A="f188r_signsA", al="f188r_align_v4", bands="f188r"),
        "101r": dict(draft="recf101r", A="f101r_signsA", al="f101r_align_v4", bands="f101r"),
        "274r": dict(draft="recf274", A="f274_signsA", al="f274_align", bands="f274")}
def lettered(leaf, codes):
    c = LEAF[leaf]; S = defaultdict(list)
    for r in rd(f"{P}/{c['draft']}/ciphertext_draft.tsv"):
        if r["sign"] != "DASH": S[r["line"]].append(r)
    A = {(r["line"], int(r["pos"])): r for r in rd(f"{P}/{c['A']}.tsv")}; out = []
    for r in rd(f"{P}/{c['al']}.tsv"):
        if r["kind"] != "code" or r["value"] not in codes: continue
        L = r["plain_chunk"].strip().lower()
        if len(L) != 1 or not L.isalpha(): continue
        try: s = S[r["cipher_line"]][int(r["idx"])]
        except IndexError: continue
        a = A.get((r["cipher_line"], int(s["position"])))
        if not a or a["sign"] not in FAM4: continue
        out.append(dict(src="P", leaf=leaf, code=r["value"], line=r["cipher_line"], ref=r["idx"], letter=L, seg=a["segment"], x=int(a["x_px"]), asign=a["sign"]))
    return out
def cls(L): return "I" if L in I else "DQ" if L in DQ else "AN" if L in AN else "-" if L in ("-", "") else "other"
F61 = [("ZHOOK", "L07", 2, 1430), ("ZHOOK", "L07", 3, 2080), ("ZHOOK", "L11", 2, 1500), ("C43", "L05", 1, 2310), ("C43", "L05", 2, 500),
       ("C43", "L11", 1, 1565), ("HASH4", "L01", 2, 1917), ("4PI", "L01", 2, 2214), ("4PI", "L11", 2, 864)]
OVL = {"L02": "satisfaireungseulauprejudicedeplusieurs", "L03": "aultresquimeprenentagarentdeleursjacommoditez"}
def overlay_letters(blank=("ZHOOK", "4PI")):
    import build_key_v6 as bk
    from f61crib import align
    k = {c: v for c, v in bk.load_key_v6(ebr="A").items() if c not in blank}; A = defaultdict(list); let = {}
    for r in rd(f"{SC}/pass108A_classes.tsv"): A[r["line"]].append(r)
    for L, m in OVL.items():
        for i, j in align(m, [r["sign"] for r in A[L]], k)[1]: let[(L, A[L][j]["pos"])] = m[i]
    return A, let
def sample():
    rng = random.Random(808); its = []
    for t in lettered("274r", ("H24", "HASH4")):
        if cls(t["letter"]) in ("I", "DQ"): its.append(dict(t, kind="G", role="gate"))
    for leaf in ("188r", "101r"):
        its += [dict(t, kind="T", role="P1") for t in lettered(leaf, ("4PI",))]
        p = lettered(leaf, ("H24", "HASH4"))
        its += [dict(t, kind="T", role="anchor") for t in rng.sample([t for t in p if t["code"] == "H24" and cls(t["letter"]) == "I"], 6)]
        its += [dict(t, kind="T", role="anchor") for t in rng.sample([t for t in p if t["code"] == "HASH4" and cls(t["letter"]) == "DQ"], 6)]
        its += [dict(t, kind="T", role="distr") for t in rng.sample([t for t in lettered(leaf, ("C43",)) if cls(t["letter"]) == "AN"], 4)]
    for code, line, seg, x in F61:
        its.append(dict(src="S61", leaf="61", code=code, line=line, ref=f"{line}s{seg}x{x}", letter="-", seg=seg, x=x, asign=code, kind="T",
                        role="Z" if code == "ZHOOK" else "P2" if code == "4PI" else "distr"))
    A, let = overlay_letters()
    rows = [r for L in ("L02", "L03") for r in A[L]]
    pick = [r for r in rows if r["sign"] in ("ZHOOK", "4PI", "4STEM", "4TRI")] + rng.sample([r for r in rows if r["sign"] == "C43"], 5)
    for r in pick:
        its.append(dict(src="S108", leaf="108r", code=r["sign"], line=r["line"], ref=f"{r['line']}p{r['pos']}", letter=let.get((r["line"], r["pos"]), "-"),
                        seg=int(r["segment"]), x=int(r["x_px"]), asign=r["sign"], kind="T",
                        role="Z" if r["sign"] == "ZHOOK" else "P2" if r["sign"] == "4PI" else "distr"))
    for r in rd(f"{SC}/f61recon108r_draft.tsv"):
        if r["sign"] == "4PI":
            its.append(dict(src="S108n", leaf="108r", code="4PI", line=r["line"], ref=f"{r['line']}p{r['position']}", letter="-",
                            seg=r["segment"], x=int(r["x_px"]), asign="4PI", kind="T", role="P2"))
    dup = rng.sample([t for t in its if t["kind"] == "T"], 8)
    return its, dup
def cut(t, nat, bands):
    from PIL import Image, ImageOps
    if t["src"] == "P":
        B, meta = bands[t["leaf"]]; b = B[f"f{'274' if t['leaf'] == '274r' else t['leaf']}_{t['line']}_{t['seg']}.jpg"]
        x = b[0] + t["x"] / meta["scale"]; cy = b[1] + meta["up"]
        w = nat[t["leaf"]].crop((int(x - 60), int(cy - 55), int(x + 60), int(cy + 60)))
    elif t["src"] == "S61":
        im = Image.open(f"{IM}/f61sheet_{t['line']}.jpg").convert("RGB"); n = {"L01": 2, "L05": 3, "L07": 3, "L11": 2}[t["line"]]
        st = (im.height - 12 * (n - 1)) / n; y0 = int((t["seg"] - 1) * (st + 12)); w = im.crop((t["x"] - 180, y0, t["x"] + 180, int(y0 + st)))
    elif t["src"] == "S108":
        im = Image.open(f"{IM}/f108sheetB_{t['line']}.jpg").convert("RGB"); st = (im.height + 12) // 4 - 12
        strip = Image.new("RGB", (4 * im.width, st), "white")
        for k in range(4): strip.paste(im.crop((0, k * (st + 12), im.width, k * (st + 12) + st)), (k * im.width, 0))
        gx = (t["seg"] - 1) * im.width + t["x"]; w = strip.crop((gx - 180, 0, gx + 180, st))
    else:
        d = "f108g" if t["line"] in ("L04", "L05") else "f108h"; j = json.load(open(f"{IM}/{d}/{d}_bands.json"))
        b = j["boxes"][f"{d}_{t['line']}_{t['seg']}.jpg"]; src = nat.setdefault(d, Image.open(f"{IM}/{os.path.basename(j['image'])}").convert("RGB"))
        x = b[0] + t["x"] / j["scale"]; w = src.crop((int(x - 60), b[1], int(x + 60), b[3]))
    w = w.resize((360, max(1, int(w.height * 360 / w.width))))
    return ImageOps.autocontrast(w.convert("L"), cutoff=1).convert("RGB"), 180
SETS = (("setF", "F", 81), ("setG", "G", 82), ("setN", "N", 83))
def tiles(scratch):
    from PIL import Image, ImageDraw
    its, dup = sample(); nat = {k: Image.open(f"{scratch}/f{k}.jpg").convert("RGB") for k in ("188r", "101r")}
    nat["274r"] = Image.open(f"{FAM}/images/3984_f274r.jpg").convert("RGB"); bands = {}
    for k, f in (("188r", "f188r"), ("101r", "f101r"), ("274r", "f274")):
        j = json.load(open(f"{FAM}/sheets/{f}_bands.json")); bands[k] = (j["boxes"], j)
    key = ["set\tid\tkind\trole\tleaf\tcode\tasign\tline\tref\tletter\tcls\tdup_of"]
    for tag, pre, seed in SETS:
        rows = [dict(t, dup="") for t in its] + [dict(t, dup="dup") for t in dup]; random.Random(seed).shuffle(rows); ims = []; first = {}
        os.makedirs(f"{scratch}/{tag}", exist_ok=True)
        for n, t in enumerate(rows, 1):
            if not t["dup"]: first[(t["leaf"], t["line"], str(t["seg"]), t["x"])] = f"{pre}{n:03d}"
        for n, t in enumerate(rows, 1):
            tid = f"{pre}{n:03d}"; w, mx = cut(t, nat, bands)
            c = Image.new("RGB", (370, 420), "white"); d = ImageDraw.Draw(c); c.paste(w, (5, 22)); y = 22 + w.height; mx += 5
            d.polygon([(mx - 8, 2), (mx + 8, 2), (mx, 18)], fill=(220, 0, 0)); d.polygon([(mx - 8, y + 19), (mx + 8, y + 19), (mx, y + 3)], fill=(220, 0, 0))
            d.text((315, 4), tid, fill=(0, 0, 0)); ims.append(c)
            dof = first[(t["leaf"], t["line"], str(t["seg"]), t["x"])] if t["dup"] else ""
            key.append("\t".join(map(str, [tag, tid, t["kind"], t["role"], t["leaf"], t["code"], t["asign"], t["line"], t["ref"], t["letter"], cls(t["letter"]), dof])))
        for s0 in range(0, len(ims), 20):
            sh = Image.new("RGB", (4 * 370, 5 * 420), "white")
            for k2, c in enumerate(ims[s0:s0 + 20]): sh.paste(c, ((k2 % 4) * 370, (k2 // 4) * 420))
            sh.save(f"{scratch}/{tag}/sheet_{s0 // 20 + 1:02d}.jpg", quality=90)
    open(f"{HERE}/v8_items.tsv", "w").write("\n".join(key) + "\n")
    print(len(its), "tiles +", len(dup), "dups;", Counter((t["role"], t["leaf"], t["code"]) for t in its))
def align_check():
    """Z3/P2 alignment: f.108r overlay letters at ZHOOK/4PI with (a) key v6 as is, (b) ZHOOK and 4PI removed from the key, (c) position only
    (sign k = letter k, where the line's sign count equals the overlay's letter count). Written before any call; no vision."""
    out = []
    for tag, blank in (("key v6", ()), ("key v6 without ZHOOK, 4PI", ("ZHOOK", "4PI"))):
        A, let = overlay_letters(blank)
        for L in OVL:
            out.append(f"{tag} {L}: " + " ".join(f"{r['sign']}@{r['pos']}={let.get((L, r['pos']), '-')}" for r in A[L] if r["sign"] in ("ZHOOK", "4PI")))
    A, _ = overlay_letters()
    for L, m in OVL.items():
        if len(A[L]) == len(m):
            out.append(f"position only {L} ({len(m)} signs = {len(m)} letters): " + " ".join(f"{r['sign']}@{r['pos']}={m[k]}" for k, r in enumerate(A[L]) if r["sign"] in ("ZHOOK", "4PI")))
        else: out.append(f"position only {L}: {len(A[L])} signs vs {len(m)} letters, not applicable")
    return out
def S_stat(rows, lab, conc): return sum(conc(lab[i], r) for i, r in enumerate(rows))
def perm(rows, ans, conc, n=20000, seed=88):
    lab = [ans[r["id"]] for r in rows]; obs = S_stat(rows, lab, conc); rng = random.Random(seed); byleaf = defaultdict(list)
    for i, r in enumerate(rows): byleaf[r["leaf"]].append(i)
    ge = 0
    for _ in range(n):
        L = lab[:]
        for idx in byleaf.values():
            v = [lab[i] for i in idx]; rng.shuffle(v)
            for i, x in zip(idx, v): L[i] = x
        ge += S_stat(rows, L, conc) >= obs
    return obs, (ge + 1) / (n + 1)
def score():
    K = rd(f"{HERE}/v8_items.tsv"); out = ["align_check (no vision):"] + ["  " + l for l in align_check()]; ro = {}
    for tag, pre, _ in SETS:
        f = f"{HERE}/v8_reply_{tag}.tsv"
        if not os.path.exists(f): out.append(f"{tag}: no reply"); continue
        ans = {r["id"]: r["answer"].strip().upper()[:1] for r in rd(f)}; rows = [dict(r, ans=ans.get(r["id"], "N")) for r in K if r["set"] == tag]
        base = [r for r in rows if not r["dup_of"]]; dup = [r for r in rows if r["dup_of"]]
        G = [r for r in base if r["kind"] == "G"]
        if tag == "setN": gh = sum((r["ans"] == "A") == (r["cls"] == "DQ") for r in G)
        else: gh = sum(r["ans"] == ("D" if r["cls"] == "I" else "A") for r in G)
        gate = gh >= 0.8 * len(G); rep = sum(ans.get(r["id"]) == ans.get(r["dup_of"]) for r in dup)
        out.append(f"{tag}: GATE f.274r {gh}/{len(G)} {'PASS' if gate else 'CONTROL FAIL'}; repeat {rep}/{len(dup)} {'stable' if rep >= 6 else 'unstable'}")
        if not gate: continue
        T = [r for r in base if r["kind"] == "T"]
        tab = defaultdict(Counter)
        for r in T: tab[(r["role"], r["leaf"], r["code"], r["cls"])][r["ans"]] += 1
        for k in sorted(tab): out.append(f"  {'/'.join(k)}: " + " ".join(f"{a} {n}" for a, n in sorted(tab[k].items())))
        M = [r for r in T if r["leaf"] in ("61", "108r")]; Z = [r for r in M if r["code"] == "ZHOOK"]; Dz = [r for r in M if r["code"] != "ZHOOK"]
        z61 = sum(r["ans"] == "D" for r in Z if r["leaf"] == "61")
        if tag != "setN":
            zs = sum(r["ans"] == "D" for r in Z) / len(Z); ds = sum(r["ans"] == "D" for r in Dz) / len(Dz)
            obs, p = perm(M, {r["id"]: r["ans"] for r in M}, lambda a, r: (r["code"] == "ZHOOK") == (a == "D"))
            z108 = sum(r["ans"] == "D" for r in Z if r["leaf"] == "108r")
            out.append(f"  Z1: ZHOOK D {sum(r['ans'] == 'D' for r in Z)}/{len(Z)} = {zs:.2f} (f.61 {z61}/3, f.108r {z108}/7); in-hand distractors D {ds:.2f} ({len(Dz)}); S {obs} p {p:.2g}")
            ro[(tag, "Z")] = zs >= 0.7 and ds <= 0.2 and p < 0.01 and z61 >= 2; ro[(tag, "Z108")] = z108 / 7 >= 0.7 and ds <= 0.2 and p < 0.01
            L8 = [r for r in T if r["leaf"] == "108r" and r["cls"] in ("I", "DQ", "AN", "other")]
            obs, p = perm(L8, {r["id"]: r["ans"] for r in L8}, lambda a, r: (a == "D" and r["cls"] == "I") + (a == "A" and r["cls"] == "DQ"))
            out.append(f"  Z3 (overlay letters, f.108r {len(L8)} lettered tiles): S {obs} p {p:.2g}")
            P1 = [r for r in T if r["role"] == "P1"]; E = [r for r in P1 if r["ans"] == "E"]; Ae = [r for r in P1 if r["ans"] == "A"]
            obs, p = perm(P1, {r["id"]: r["ans"] for r in P1}, lambda a, r: (a == "A" and r["cls"] == "DQ") + (a == "E" and r["cls"] == "AN"))
            ean = sum(r["cls"] == "AN" for r in E) / max(1, len(E))
            out.append(f"  P1 (period 4PI, {len(P1)} tiles): A {len(Ae)} (d/q {sum(r['cls'] == 'DQ' for r in Ae)}, a/n {sum(r['cls'] == 'AN' for r in Ae)}); "
                       f"E {len(E)} (d/q {sum(r['cls'] == 'DQ' for r in E)}, a/n {sum(r['cls'] == 'AN' for r in E)}); S {obs} p {p:.2g}")
            ro[(tag, "P1two")] = p < 0.01 and len(E) >= 3 and ean >= 0.6
            ro[(tag, "P1head")] = len(Ae) / len(P1) >= 0.7 and len(E) / len(P1) < 0.15
            Q = [r for r in T if r["code"] == "4PI"]; e = sum(r["ans"] == "E" for r in Q) / len(Q)
            f61 = [r["ans"] for r in Q if r["leaf"] == "61"]; f108 = [r for r in Q if r["leaf"] == "108r"]; a108 = sum(r["ans"] == "A" for r in f108) / len(f108)
            out.append(f"  P2: f.61 4PI {'/'.join(f61)}; f.108r 4PI A {sum(r['ans'] == 'A' for r in f108)}/{len(f108)} = {a108:.2f}; "
                       f"E rate over all {len(Q)} 4PI tiles {e:.2f}, chance both f.61 E ~ {e * e:.3f}")
            ro[(tag, "P2")] = f61 == ["E", "E"] and a108 >= 0.7
        else:
            zna = sum(r["ans"] != "A" for r in Z) / len(Z)
            out.append(f"  Z2: ZHOOK not-A {zna:.2f}; f.61 4PI " + "/".join(r["ans"] for r in T if r["code"] == "4PI" and r["leaf"] == "61"))
    both = lambda k: all(ro.get((t, k)) for t in ("setF", "setG"))
    if ro:
        out.append("read-outs (both setF and setG): " + "; ".join(f"{k} {'yes' if both(k) else 'no'}" for k in ("Z", "Z108", "P1two", "P1head", "P2")))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/v8_shape_sort_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    {"tiles": lambda: tiles(sys.argv[2]), "align_check": lambda: print("\n".join(align_check())), "score": score}[sys.argv[1]]()
