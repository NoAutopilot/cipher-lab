#!/usr/bin/env python3
"""F61-FAMILY-6 (campaign row H52 widened, 28 Sept 2026, parent worker session_01TPNoYGTE6dLBPfyEgZTLAc): re-code the family
readers' merged classes on the glossed leaves f.101r and f.188r into the four splits the campaign runner's blind tile sorts
established (H65/H67 SBS b/o out of PHI; H69 4TRI = 4-over-triangle c/p vs the 4-with-hook forms a/n; H70 VBAR_A top bar
only = t vs VBAR_B second stroke = s; H77 LOOPS = SBS o + INF u), then rebuild the per-leaf period key rows for key v4.

Pre-registered here, before any call (pushed with the sheets):
  * Calls (blind Opus shape sorts, one per leaf and shape family, 5 in all, cap 6):
      f101r_loops  PHI + LOOPS tokens -> PHI (trefoil / stacked, stem through the loops) | SBS (two loops side by side, stem
                   from their junction) | INF (loops on / crossed by a bar, no stem)
      f101r_4tri   4TRI -> 4TRI (closed triangle on the stem under the crossbar) | 4HOOK (hook / r-stroke / loop beside the 4)
      f101r_vbar   VBAR_A -> VBAR_A (triangle with top bar only) | VBAR_B (second stroke from the point, Z-like)
      f188r_loops  PHI + LOOPS -> PHI | SBS | INF        f188r_4tri   4TRI -> 4TRI | 4HOOK
    (f.188r's readers already keep VBAR_A t 19 / VBAR_B s 27 apart: no VBAR sort there. f.274r: no align line equals its
    draft, so no x position -- its PHI/4TRI/VBAR/LOOPS rows are dropped from v4 as unsorted, its other rows kept.)
  * Anchors: the runner's H65/H67/H69/H70/H77 tiles of the same leaf whose blind group AND period letter agree (e.g. H65
    group A under o), re-cut exactly as the runner cut them, shown on an anchor sheet under neutral labels (form 1, 2, 3),
    never with letters. INF anchors for f.188r come from f.101r (H77 was f.101r only) and are marked as another hand.
  * Held-out check: per class, max(2, ceil(n/10)) anchors (seed 52) are withheld from the anchor sheet and mixed, unlabelled,
    among the query tiles. Gate per class: held-out accuracy >= 0.80, else that class is STOPPED (its split not used in v4;
    the tokens it would take stay in the merged class) and said so in KEY.md.
  * Query sample (the key is estimated, not every token re-read): tokens matched to pass A exactly as scripts/f61sbs.tokens
    does (pass A reads the same class), stratified by (leaf, source class, period letter; letters under 8% of the class
    pooled as 'other'), up to CAP per stratum (tokens already blind-sorted by H65/H67/H69/H70/H77 count toward the cap and are
    re-coded by their earlier group, unambiguous groups only: H67 B and H77 C/D stay unsorted; H71's groups follow the hand,
    not this split, so its tiles are not used). Key rows per split class per leaf: n = sum over strata of N_s / k_s x (sorted
    tokens of that letter in that class in stratum s), rounded; 'bands' carries 'est k/N' so a verifier sees the sample size.
  python3 family/recode_split.py build NATIVE_DIR        -> family/recode/<call>_{anchors,query}*.jpg + <call>_key.tsv
  python3 family/recode_split.py score                   -> family/recode/heldout.txt, passes/<leaf>_align_v4.tsv,
                                                            key_period_f101_v4.tsv, key_period_f188_v4.tsv
  python3 family/recode_split.py score --check           (exit 1 if any of those files is stale)
"""
import csv, difflib, json, math, os, random, sys
from collections import Counter, defaultdict
FAM = os.path.dirname(os.path.abspath(__file__)); TGT = os.path.dirname(FAM); SCR = f"{TGT}/scripts"; OUT = f"{FAM}/recode"
IMG = {"f101r": "3982_f101r.jpg", "f188r": "3984_f188r.jpg"}
CAP = 20; OTHER_FRAC = 0.08
RC = {"PHI": (30, (-15, 45)), "4TRI": (30, (-15, 45)), "LOOPS": (20, (-10, 35)), "VBAR_A": (20, (-20, 30))}
CALLS = {   # call -> (leaf, source classes, target classes in form order)
    "f101r_loops": ("f101r", ("PHI", "LOOPS"), ("PHI", "SBS", "INF")),
    "f101r_4tri": ("f101r", ("4TRI",), ("4TRI", "4HOOK")),
    "f101r_vbar": ("f101r", ("VBAR_A",), ("VBAR_A", "VBAR_B")),
    "f188r_loops": ("f188r", ("PHI", "LOOPS"), ("PHI", "SBS", "INF")),
    "f188r_4tri": ("f188r", ("4TRI",), ("4TRI", "4HOOK")),
}
# earlier runs: tile file, read_call file, source class, re-cut window, group -> target class (None = ambiguous, unsorted),
# and the letters under which a tile of that group is a clean anchor
PRIOR = [
    ("f61sbs_tiles.tsv", "read_call_SBS.tsv", "PHI", "PHI", {"A": "SBS", "B": "PHI"}, {"SBS": "bo", "PHI": "er"}),
    ("f61sbs_b_tiles.tsv", "read_call_SBSB.tsv", "PHI", "PHI", {"A": "SBS", "B": None, "C": "PHI"}, {"SBS": "bo", "PHI": "er"}),
    ("f61pair_h69_tiles.tsv", "read_call_H69.tsv", "4TRI", "4TRI", {"A": "4TRI", "B": "4HOOK", "C": "4HOOK", "D": "4HOOK"}, {"4TRI": "cp", "4HOOK": "an"}),
    ("f61pair_h70_tiles.tsv", "read_call_H70.tsv", "VBAR_A", "VBAR_A", {"A": "VBAR_A", "B": "VBAR_B", "C": "VBAR_A"}, {"VBAR_A": "t", "VBAR_B": "s"}),
    ("f61pair_h77_tiles.tsv", "read_call_H77.tsv", "LOOPS", "LOOPS", {"A": "SBS", "B": "INF", "C": None, "D": None}, {"SBS": "o", "INF": "u"}),
]
def rows(p): return list(csv.DictReader((l for l in open(p) if not l.startswith("#")), delimiter="\t"))
def tokens(leaf, cls):
    """scripts/f61sbs.tokens for one class, every letter (align line must equal the draft; pass A must read the class)."""
    al = rows(f"{FAM}/passes/{leaf}_align.tsv"); dr = rows(f"{FAM}/passes/rec{leaf}/ciphertext_draft.tsv"); A = rows(f"{FAM}/passes/{leaf}_signsA.tsv")
    dl, al_l, Al = defaultdict(list), defaultdict(list), defaultdict(list)
    for r in dr: dl[r["line"]].append(r)
    for r in al: al_l[r["cipher_line"]].append(r)
    for r in A: Al[r["line"]].append(r)
    out = []
    for L, ar in al_l.items():
        d = dl.get(L, []); a = Al.get(L, [])
        if [r["raw"].lstrip("@") for r in ar] != [r["sign"] for r in d]: continue
        sm = difflib.SequenceMatcher(None, [r["sign"] for r in d], [r["sign"] for r in a], autojunk=False)
        for blk in sm.get_matching_blocks():
            for k in range(blk.size):
                i, j = blk.a + k, blk.b + k
                if ar[i]["value"] == cls and a[j]["sign"] == cls:
                    out.append(dict(leaf=leaf, line=L, pos=i + 1, letter=ar[i]["plain_chunk"] or "-", seg=a[j]["segment"], x=float(a[j]["x_px"]), src=cls))
    return out
def strata(toks):
    """(src, letter-or-other) -> tokens; letters under OTHER_FRAC of the source class (and '-') pooled as 'other'."""
    by = defaultdict(list); tot = Counter(t["src"] for t in toks); cnt = Counter((t["src"], t["letter"]) for t in toks)
    for t in toks:
        k = t["letter"] if t["letter"] != "-" and cnt[(t["src"], t["letter"])] >= OTHER_FRAC * tot[t["src"]] else "other"
        by[(t["src"], k)].append(t)
    return by
def prior(leaf):
    """(line, pos) -> dict(target, group, run, letter, tile row, rc) for earlier blind-sorted tiles of this leaf."""
    out = {}
    for tf, rf, src, rcc, gmap, clean in PRIOR:
        key = {r["tile"]: r for r in rows(f"{SCR}/{tf}")}
        for r in rows(f"{SCR}/{rf}"):
            k = key.get(r["tile"]); g = r["group"].strip()
            if not k or k["leaf"] != leaf or g.lower() in ("", "none", "-", "x"): continue
            tgt = gmap.get(g); p = (k["line"], int(k["draft_pos"]))
            ent = dict(target=tgt, group=g, run=rf.replace("read_call_", "").replace(".tsv", ""), letter=k["period_letter"], src=src,
                       seg=k["segment"], x=float(k["x_px"]), rc=rcc, anchor=bool(tgt and k["period_letter"] in clean.get(tgt, "")))
            if p in out and out[p]["target"] != tgt: out[p]["conflict"] = True; continue
            out.setdefault(p, ent)
    return {p: e for p, e in out.items() if not e.get("conflict")}
def cut_tile(img, leaf, line, seg, x, rcc):
    from PIL import ImageDraw
    import numpy as np
    bj = json.load(open(f"{FAM}/sheets/{leaf}_bands.json")); box = bj["boxes"][f"{leaf}_{line}_{seg}.jpg"]
    rx, ry = RC[rcc]; cx = box[0] + x / bj["scale"]; cy = box[1] + bj["up"]
    g = np.asarray(img.crop((int(cx - rx), int(cy + ry[0]), int(cx + rx), int(cy + ry[1]))).convert("L"))
    pr = np.convolve((g < 140).sum(axis=1), np.ones(9) / 9, "same"); cy = cy + ry[0] + int(pr.argmax())
    t = img.crop((int(cx - 55), int(cy - 40), int(cx + 55), int(cy + 55))).resize((330, 285)); d = ImageDraw.Draw(t)
    d.line([(165, 0), (165, 14)], fill=(220, 0, 0), width=3); d.line([(165, t.height - 14), (165, t.height)], fill=(220, 0, 0), width=3)
    return t
def sheets(tiles, path_stem, label):
    from PIL import Image, ImageDraw
    W, H = 330, 285 + 34; n = 0
    for s in range(0, len(tiles), 10):
        sh = Image.new("RGB", (5 * (W + 10), 2 * (H + 10)), "white"); d = ImageDraw.Draw(sh)
        for k, (lab, t) in enumerate(tiles[s:s + 10]):
            X, Y = (k % 5) * (W + 10), (k // 5) * (H + 10); sh.paste(t, (X, Y + 34)); d.text((X + 6, Y + 6), label(lab), fill=(0, 0, 200))
            d.rectangle([X, Y + 34, X + W - 1, Y + 34 + t.height - 1], outline=(0, 0, 0))
        n += 1; sh.save(f"{path_stem}{n}.jpg", quality=86)
    return n
def plan(call):
    leaf, srcs, tgts = CALLS[call]; pr = prior(leaf); rng = random.Random(52)
    toks = [t for c in srcs for t in tokens(leaf, c)]; st = strata(toks)
    # anchors per target class, from the prior tiles of this leaf whose source class is in this call
    anc = defaultdict(list)
    for p, e in sorted(pr.items()):
        if e["anchor"] and e["src"] in srcs and e["target"] in tgts: anc[e["target"]].append((p, e))
    if call == "f188r_loops":   # H77 was f.101r only: INF anchors from the other hand
        for p, e in sorted(prior("f101r").items()):
            if e["anchor"] and e["target"] == "INF": anc["INF"].append((("f101r",) + p, e))
    held = {}
    for c in tgts:
        a = list(anc[c]); rng.shuffle(a); h = max(2, math.ceil(len(a) / 10)) if len(a) >= 4 else 0
        held[c] = a[:h]; anc[c] = a[h:]
    query = []
    for (src, lk), ts in sorted(st.items()):
        done = [t for t in ts if (t["line"], t["pos"]) in pr and pr[(t["line"], t["pos"])]["src"] == src]
        rest = [t for t in ts if (t["line"], t["pos"]) not in pr]
        need = max(0, min(CAP, len(ts)) - len(done)); query += rng.sample(rest, min(need, len(rest)))
    return leaf, srcs, tgts, toks, st, pr, anc, held, query
def build(native):
    from PIL import Image
    os.makedirs(OUT, exist_ok=True); imgs = {lf: Image.open(f"{native}/{f}").convert("RGB") for lf, f in IMG.items()}
    rng = random.Random(520); summary = []
    for call in CALLS:
        leaf, srcs, tgts, toks, st, pr, anc, held, query = plan(call)
        form = {c: i + 1 for i, c in enumerate(tgts)}
        at = []
        for c in tgts:
            for p, e in anc[c]:
                lf = p[0] if len(p) == 3 else leaf; line, pos = p[-2], p[-1]
                at.append((form[c], cut_tile(imgs[lf], lf, line, e["seg"], e["x"], e["rc"])))
        na = sheets(at, f"{OUT}/{call}_anchors", lambda lab: f"form {lab}")
        q = [("query", t["leaf"], t["line"], t["pos"], t["src"], t["letter"], "-", t["seg"], t["x"], RC_of(t["src"])) for t in query]
        for c in tgts:
            for p, e in held[c]:
                lf = p[0] if len(p) == 3 else leaf
                q.append(("heldout", lf, p[-2], p[-1], e["src"], e["letter"], c, e["seg"], e["x"], e["rc"]))
        rng.shuffle(q)
        qt = [(i + 1, cut_tile(imgs[r[1]], r[1], r[2], r[7], r[8], r[9])) for i, r in enumerate(q)]
        nq = sheets(qt, f"{OUT}/{call}_query", lambda lab: f"tile {lab}")
        with open(f"{OUT}/{call}_key.tsv", "w") as f:
            f.write("# answer key -- never shown to the reader. forms: " + ", ".join(f"form {form[c]} = {c}" for c in tgts) + "\n")
            f.write("tile\tkind\tleaf\tline\tpos\tsrc\tperiod_letter\theld_class\tsegment\tx_px\n")
            for i, r in enumerate(q, 1): f.write("\t".join(map(str, (i,) + r[:9])) + "\n")
        summary.append(f"{call}: anchors " + ", ".join(f"form {form[c]} {c} {len(anc[c])}" for c in tgts) + f" ({na} sheet(s)); query {len(query)} + held-out " + ", ".join(f"{c} {len(held[c])}" for c in tgts) + f" = {len(q)} tiles ({nq} sheets)")
    open(f"{OUT}/build.txt", "w").write("\n".join(summary) + "\n"); print("\n".join(summary))
def RC_of(src): return src if src in RC else "PHI"
def score():
    out = ["# F61-FAMILY-6 held-out check (gate 0.80 per class) and per-stratum sample sizes; recode_split.py score"]; stopped = set()
    got_all = {}
    for call in CALLS:
        leaf, srcs, tgts, toks, st, pr, anc, held, query = plan(call)
        form = {str(i + 1): c for i, c in enumerate(tgts)}
        key = rows(f"{OUT}/{call}_key.tsv"); rp = f"{OUT}/{call}_read.tsv"
        if not os.path.exists(rp): out.append(f"{call}: no read file"); continue
        rd = {r["tile"]: r["form"].strip() for r in rows(rp)}
        acc = defaultdict(lambda: [0, 0])
        for k in key:
            f_ = rd.get(k["tile"], "none"); c = form.get(f_)
            if k["kind"] == "heldout":
                acc[k["held_class"]][1] += 1; acc[k["held_class"]][0] += int(c == k["held_class"])
            else: got_all[(leaf, k["line"], int(k["pos"]))] = (c, k["src"], call)
        for c in tgts:
            a, n = acc[c]; ok = n > 0 and a / n >= 0.8
            if not ok: stopped.add((leaf, c))
            out.append(f"{call}: held-out {c} {a}/{n}" + (f" = {a/n:.2f}" if n else "") + (" PASS" if ok else " -- STOPPED (below 0.80 or no held-out tiles)"))
        nq = sum(1 for k in key if k["kind"] == "query"); nn = sum(1 for k in key if k["kind"] == "query" and form.get(rd.get(k["tile"], "none")) is None)
        out.append(f"{call}: query tiles {nq}, read 'none' {nn}")
    # per-leaf: recoded tokens and weighted key rows
    for leaf, keyname in (("f101r", "key_period_f101"), ("f188r", "key_period_f188")):
        srcs = sorted({s for c, (lf, ss, _) in CALLS.items() if lf == leaf for s in ss}); pr = prior(leaf)
        toks = [t for c in srcs for t in tokens(leaf, c)]; st = strata(toks)
        est = defaultdict(float); samp = defaultdict(int); tot = defaultdict(int)
        rec = {}
        for (src, lk), ts in st.items():
            sorted_ = []
            for t in ts:
                p = (t["line"], t["pos"]); c = None
                if (leaf,) + p in got_all and got_all[(leaf,) + p][1] == src: c = got_all[(leaf,) + p][0]
                elif p in pr and pr[p]["src"] == src and pr[p]["target"]: c = pr[p]["target"]
                if c and (leaf, c) in stopped: c = None
                rec[p] = c
                if c: sorted_.append((t, c))
            if not sorted_: continue
            w = len(ts) / len(sorted_)
            for t, c in sorted_:
                if t["letter"] != "-": est[(c, t["letter"])] += w; samp[c] += 1
            for c in {c for _, c in sorted_}: tot[c] = tot.get(c, 0)
        # write the recoded align file
        al = rows(f"{FAM}/passes/{leaf}_align.tsv"); hdr = list(al[0].keys()) + ["split_v4", "split_source"]
        with open(f"{FAM}/passes/{leaf}_align_v4.tsv", "w") as f:
            f.write("# F61-FAMILY-6 (28 Sept 2026): split_v4 = the class after the blind shape sort (recode_split.py); 'unsorted' = a PHI/4TRI/VBAR_A/LOOPS token not in the sample (the key estimates it by stratum weight); '=' = class not affected\n")
            f.write("\t".join(hdr) + "\n")
            for r in al:
                p = (r["cipher_line"], int(r["idx"]) + 1)
                if r["value"] in ("PHI", "4TRI", "VBAR_A", "LOOPS"):
                    c = rec.get(p); srcv = "v4 sort" if (leaf,) + p in got_all else ("H65-H77 tile" if p in pr else "")
                    sp = c if c else "unsorted"
                else: sp, srcv = "=", ""
                f.write("\t".join(list(r.values()) + [sp, srcv]) + "\n")
        # key rows: unaffected classes copied from the v3 per-leaf file; affected source classes replaced by the estimate
        base = rows(f"{FAM}/{keyname}.tsv"); affected = set(srcs) | ({"VBAR_A"} if leaf == "f101r" else set())
        new = [r for r in base if r["class"] not in affected]
        for (c, l), v in sorted(est.items()):
            n = int(round(v))
            if n >= 1: new.append(dict(**{"class": c, "letter": l, "n": str(n), "leaf": base[0]["leaf"], "bands": f"est from {samp[c]} sorted tokens"}))
        # classes that the readers already coded apart (INF, VBAR_B on f.101r; INF on f.188r) keep their own rows and gain the sorted share
        merged = defaultdict(int); info = {}
        for r in new:
            merged[(r["class"], r["letter"])] += int(r["n"]); info[(r["class"], r["letter"])] = r
        with open(f"{FAM}/{keyname}_v4.tsv", "w") as f:
            f.write(f"# {keyname}_v4.tsv -- F61-FAMILY-6, 28 Sept 2026: {keyname}.tsv with PHI/4TRI/LOOPS" + ("/VBAR_A" if leaf == "f101r" else "") + " replaced by the blind-sort estimate (recode_split.py); readers' own classes of the same name summed in. Key source: period.\n")
            f.write("class\tletter\tn\tleaf\tbands\n")
            for (c, l), n in sorted(merged.items(), key=lambda kv: (kv[0][0], -kv[1], kv[0][1])):
                f.write(f"{c}\t{l}\t{n}\t{info[(c, l)]['leaf']}\t{info[(c, l)]['bands']}\n")
        out.append(f"{leaf}: tokens in affected classes {len(toks)}, sorted (v4 call or earlier tile) {sum(1 for v in rec.values() if v)}; strata {len(st)}")
        for c in sorted({c for c, _ in est}):
            top = sorted(((l, v) for (cc, l), v in est.items() if cc == c), key=lambda kv: -kv[1])
            out.append(f"  {leaf} {c}: " + ", ".join(f"{l} {v:.0f}" for l, v in top if v >= 0.5) + f"  (from {samp[c]} sorted tokens)")
    txt = "\n".join(out) + "\n"; res = f"{OUT}/heldout.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt)
if __name__ == "__main__":
    {"build": lambda: build(sys.argv[2]), "score": score, "plan": lambda: [print(c, {k: len(v) for k, v in plan(c)[4].items()}, "query", len(plan(c)[8])) for c in CALLS]}[sys.argv[1]]()
