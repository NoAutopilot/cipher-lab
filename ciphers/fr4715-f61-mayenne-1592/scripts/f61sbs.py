#!/usr/bin/env python3
"""F61-SBS-PERIOD (campaign step H65, 28 Sept 2026, runner session_01NQpd6L9ZvLvjU1L7ttFmZs): does the period decipherer's
o under the readers' PHI sign on the family leaves go with a distinct glyph (H26's two-loops-SIDE-BY-SIDE form, b/o on
f.61/f.108r), i.e. is SBS = b/o attested by the period gloss and not only by our f.61/f.108r fit?

Pre-registered before the call (prompt in scripts/PROMPTS.md, H65). Positions from disk only: every PHI token of
family/passes/{f101r,f274,f188r}_align.tsv whose aligned period letter is a single o or e; its x from pass A
(family/passes/<leaf>_signsA.tsv, matched to the reconciled draft rec<leaf>/ciphertext_draft.tsv by difflib per line,
pass A's own sign must also read PHI); crop box from family/sheets/<leaf>_bands.json (native px = box x0 + x/scale).
Sample: seed 65, up to 20 o (spread over the three leaves, f.274's 7 o all taken if matched) and the same number of e
drawn from the same leaves in the same proportions. Each tile: the native crop from the heaviest ink row near the band centre
(re-centred per tile, x +-30, y -15..+45: the gloss sits above) -40 px to +55 px (the period gloss ABOVE the row is cut away, so no letter is shown), x +-55 px, upscaled 3x, two red ticks
above and below the target sign, a tile number; tiles in a shuffled order (seed 65) on contact sheets of 10.
Statistic (the H26 scorer): best group-to-letter match over the scored tiles (groups -> {e, o}); null exact over all
label arrangements if C(n,k) <= 200000, else 2000 permutations seed 1; 200-permutation p95. Gate H65: observed > p95
and P < 0.05 AND at least 30 tiles scored (a tile the reader marks 'no sign / not a loop sign' is listed, not scored).
A PASS licenses: the period gloss writes o under a glyph the blind reader separates from the e glyph -- SBS b/o gains a
period attestation (grade C) for the family worker to merge; a FAIL leaves SBS b/o at grade M (our fit only).
  python3 scripts/f61sbs.py build NATIVE_DIR     # tiles + sheets + scripts/f61sbs_tiles.tsv (answer key, not shown)
  python3 scripts/f61sbs.py score read_call_SBS.tsv [--check]
  python3 scripts/f61sbs.py build-b NATIVE_DIR ; python3 scripts/f61sbs.py score-b read_call_SBSB.tsv [--check]   (H67)
  python3 scripts/f61sbs.py build-pair NATIVE_DIR 4TRI a,n c,p 69 h69 ; python3 scripts/f61sbs.py score-pair h69 read_call_H69.tsv [--check]   (H69-H71)
"""
import csv, difflib, itertools, json, math, os, random, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); TGT = os.path.dirname(HERE); FAM = f"{TGT}/family"
LEAVES = [("f101r", "3982_f101r.jpg"), ("f274", "3984_f274r.jpg"), ("f188r", "3984_f188r.jpg")]
LETS = ("o", "e"); CLS = "PHI"
def rows(p): return list(csv.DictReader(open(p), delimiter="\t"))
def tokens(leaf):
    al = rows(f"{FAM}/passes/{leaf}_align.tsv"); dr = rows(f"{FAM}/passes/rec{leaf}/ciphertext_draft.tsv")
    A = rows(f"{FAM}/passes/{leaf}_signsA.tsv")
    dl, al_l, Al = defaultdict(list), defaultdict(list), defaultdict(list)
    for r in dr: dl[r["line"]].append(r)
    for r in al: al_l[r["cipher_line"]].append(r)
    for r in A: Al[r["line"]].append(r)
    out = []
    for L, ar in al_l.items():
        d = dl.get(L, []); a = Al.get(L, [])
        if [r["raw"].lstrip("@") for r in ar] != [r["sign"] for r in d]: continue   # align must be the draft
        sm = difflib.SequenceMatcher(None, [r["sign"] for r in d], [r["sign"] for r in a], autojunk=False)
        for blk in sm.get_matching_blocks():
            for k in range(blk.size):
                i, j = blk.a + k, blk.b + k
                if ar[i]["value"] == CLS and ar[i]["plain_chunk"] in LETS and a[j]["sign"] == CLS:
                    out.append((leaf, L, i + 1, ar[i]["plain_chunk"], a[j]["segment"], float(a[j]["x_px"])))
    return out
def build(native):
    from PIL import Image, ImageDraw
    rng = random.Random(65); pool = {lf: tokens(lf) for lf, _ in LEAVES}
    o = {lf: [t for t in v if t[3] == "o"] for lf, v in pool.items()}; e = {lf: [t for t in v if t[3] == "e"] for lf, v in pool.items()}
    print("matched tokens:", {lf: (len(o[lf]), len(e[lf])) for lf in o})
    quota = {"f274": min(7, len(o["f274"]))}; rest = 20 - quota["f274"]
    quota["f188r"] = min(len(o["f188r"]), rest // 2); quota["f101r"] = min(len(o["f101r"]), 20 - quota["f274"] - quota["f188r"])
    pick = []
    for lf in quota:
        pick += rng.sample(o[lf], quota[lf]) + rng.sample(e[lf], min(quota[lf], len(e[lf])))
    rng.shuffle(pick); cut(pick, native, "h65", "f61sbs_tiles.tsv")
def cut(pick, native, tag, keyname, sheet_name="sbs_sheet"):
    from PIL import Image, ImageDraw
    os.makedirs(f"{TGT}/images/{tag}", exist_ok=True); tiles = []; ims = {}
    for n, (lf, L, pos, let, seg, x) in enumerate(pick, 1):
        bj = json.load(open(f"{FAM}/sheets/{lf}_bands.json")); box = bj["boxes"][f"{lf}_{L}_{seg}.jpg"]
        sc, up, down = bj["scale"], bj["up"], bj["down"]; cx = box[0] + x / sc; cy = box[1] + up
        img = ims.setdefault(lf, Image.open(f"{native}/{dict(LEAVES)[lf]}").convert("RGB"))
        import numpy as np   # re-centre on the heaviest ink row within +-45 px of the band centre, x +-30 (rows drift down the page)
        g = np.asarray(img.crop((int(cx - 30), int(cy - 15), int(cx + 30), int(cy + 45))).convert("L")); pr = np.convolve((g < 140).sum(axis=1), np.ones(9) / 9, "same")
        cy = cy - 15 + int(pr.argmax())
        t = img.crop((int(cx - 55), int(cy - 40), int(cx + 55), int(cy + 55))).resize((330, 285))
        d = ImageDraw.Draw(t); d.line([(165, 0), (165, 14)], fill=(220, 0, 0), width=3); d.line([(165, t.height - 14), (165, t.height)], fill=(220, 0, 0), width=3)
        tiles.append((n, lf, L, pos, let, seg, x, t))
    W, H = 330, max(t[7].height for t in tiles) + 34
    for s in range(0, len(tiles), 10):
        sheet = Image.new("RGB", (5 * (W + 10), 2 * (H + 10)), "white"); d = ImageDraw.Draw(sheet)
        for k, tt in enumerate(tiles[s:s + 10]):
            X, Y = (k % 5) * (W + 10), (k // 5) * (H + 10); sheet.paste(tt[7], (X, Y + 34)); d.text((X + 6, Y + 6), f"tile {tt[0]}", fill=(0, 0, 200))
            d.rectangle([X, Y + 34, X + W - 1, Y + 34 + tt[7].height - 1], outline=(0, 0, 0))
        sheet.save(f"{TGT}/images/{tag}/{sheet_name}{s // 10 + 1}.jpg", quality=88)
    with open(f"{HERE}/{keyname}", "w") as f:
        f.write("tile\tleaf\tline\tdraft_pos\tperiod_letter\tsegment\tx_px\n")
        for tt in tiles: f.write("\t".join(map(str, tt[:7])) + "\n")
    from collections import Counter
    print(len(tiles), "tiles;", dict(Counter(t[4] for t in tiles)))
def build_b(native):
    """H67 (pre-registered with the call's prompt, scripts/PROMPTS.md 'H67'): every matched PHI token under a period b on
    f.101r and f.188r, plus per leaf the same number of e and of o tokens (seed 67; the o tiles anchor which group is the
    side-by-side glyph), cut exactly as H65, key scripts/f61sbs_b_tiles.tsv, sheets images/h67/sbsb_sheet*.jpg."""
    global LETS
    LETS = ("b", "e", "o"); rng = random.Random(67); pick = []
    for lf in ("f101r", "f188r"):
        t = tokens(lf); b = [x for x in t if x[3] == "b"]; n = len(b)
        e = rng.sample([x for x in t if x[3] == "e"], n); o = rng.sample([x for x in t if x[3] == "o"], n)
        print(lf, "matched b", n); pick += b + e + o
    rng.shuffle(pick); cut(pick, native, "h67", "f61sbs_b_tiles.tsv", "sbsb_sheet")
def score_b(path):
    """H67 gate: the SBS group = the group holding the most o tiles (ties: no SBS group, non-test). 2x2 Fisher exact,
    one-sided, b tiles vs e tiles in / out of the SBS group; PASS if P < 0.05 AND the b share in the SBS group is at least
    half the o share (b behaves like o, not merely more than e); FAIL otherwise; NON-TEST if under 10 b tiles scored or
    the o anchor is not recovered (o share in the SBS group under 0.7)."""
    key = {int(r["tile"]): r for r in rows(f"{HERE}/f61sbs_b_tiles.tsv")}
    got = list(csv.DictReader((l for l in open(f"{HERE}/{path}") if not l.startswith("#")), delimiter="\t"))
    tab = defaultdict(lambda: defaultdict(int)); out = [f"{path}: {len(got)} rows; {len(key)} tiles"]
    for r in got:
        k = key.get(int(r["tile"])); g = r["group"].strip()
        if k is None: continue
        if g.lower() in ("", "none", "-", "x"): out.append(f"  tile {r['tile']} ({k['leaf']} {k['period_letter']}): not scored"); continue
        tab[g][k["period_letter"]] += 1; tab[g][k["leaf"] + ":" + k["period_letter"]] += 1
    for g in sorted(tab): out.append(f"  group {g}: " + ", ".join(f"{l} {tab[g][l]}" for l in ("b", "e", "o")) + "  (" + ", ".join(f"{k} {v}" for k, v in sorted(tab[g].items()) if ":" in k) + ")")
    tot = {l: sum(tab[g][l] for g in tab) for l in "beo"}
    og = sorted(tab, key=lambda g: -tab[g]["o"])
    if not og or (len(og) > 1 and tab[og[0]]["o"] == tab[og[1]]["o"]): out.append("GATE H67: NON-TEST (no SBS group)")
    else:
        S = og[0]; sh = {l: tab[S][l] / tot[l] if tot[l] else 0 for l in "beo"}
        a, b_, c, d = tab[S]["b"], tot["b"] - tab[S]["b"], tab[S]["e"], tot["e"] - tab[S]["e"]
        def hyp(x): return math.comb(a + b_, x) * math.comb(c + d, a + c - x) / math.comb(a + b_ + c + d, a + c)
        p = sum(hyp(x) for x in range(a, min(a + b_, a + c) + 1))
        out.append(f"SBS group {S}: share of o {sh['o']:.2f} ({tab[S]['o']}/{tot['o']}), b {sh['b']:.2f} ({a}/{tot['b']}), e {sh['e']:.2f} ({c}/{tot['e']}); Fisher one-sided b vs e P = {p:.4g}")
        if tot["b"] < 10 or sh["o"] < 0.7: out.append("GATE H67: NON-TEST (b under 10 or o anchor not recovered)")
        else: out.append(f"GATE H67: {'PASS' if p < 0.05 and sh['b'] >= 0.5 * sh['o'] else 'FAIL'}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/f61sbs_b_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt)
def stat(groups, labels):
    gs = sorted(set(groups)); return max(sum(1 for g, l in zip(groups, labels) if dict(zip(gs, lets))[g] == l) for lets in itertools.product("eo", repeat=len(gs)))
def score(path):
    key = {int(r["tile"]): r for r in rows(f"{HERE}/f61sbs_tiles.tsv")}
    src = path if path.startswith("/") else f"{HERE}/{path}"
    got = list(csv.DictReader((l for l in open(src) if not l.startswith("#")), delimiter="\t")); out = [f"{path}: {len(got)} rows; {len(key)} tiles"]
    groups, labels, tab = [], [], defaultdict(lambda: defaultdict(int))
    for r in got:
        t = int(r["tile"]); k = key.get(t)
        if k is None: continue
        g = r["group"].strip()
        if g.lower() in ("", "none", "-", "x"): out.append(f"  tile {t}: not scored ({r.get('note', '')})"); continue
        groups.append(g); labels.append(k["period_letter"]); tab[g][k["period_letter"]] += 1
    for g in sorted(tab): out.append(f"  group {g}: e {tab[g]['e']}, o {tab[g]['o']}")
    n = len(labels); k = labels.count("o")
    if n < 30: out.append(f"scored {n} < 30: NON-TEST"); out.append("GATE H65: FAIL (non-test)")
    else:
        obs = stat(groups, labels)
        if math.comb(n, k) <= 200000:
            ex = [stat(groups, ["o" if i in c else "e" for i in range(n)]) for c in itertools.combinations(range(n), k)]
            p = sum(v >= obs for v in ex) / len(ex); pn = f"exact P = {p:.4f} over {len(ex)}"
        else:
            rng = random.Random(1); c = 0
            for _ in range(2000):
                l2 = list(labels); rng.shuffle(l2); c += stat(groups, l2) >= obs
            p = c / 2000; pn = f"permutation P = {p:.4f} over 2000 (seed 1)"
        rng = random.Random(1); perm = []
        for _ in range(200):
            l2 = list(labels); rng.shuffle(l2); perm.append(stat(groups, l2))
        perm.sort(); p95 = perm[189]
        out.append(f"scored {n} (e {n - k}, o {k}); groups {len(tab)}; observed {obs}/{n}; {pn}; p95 {p95}/{n}")
        out.append(f"GATE H65: {'PASS' if obs > p95 and p < 0.05 else 'FAIL'}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/f61sbs_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt)
def build_pair(native, cls, ga, gb, seed, tag, cap=10):
    """H69-H71 (the H65 recipe for any reader class and two letter groups; each run pre-registered in scripts/PROMPTS.md
    before its call): tokens of CLS whose period letter is in group A (ga) or group B (gb), pass A agreeing on CLS; per
    leaf n = min(#A, #B, cap) of each, seed SEED; tiles cut exactly as H65; key scripts/f61pair_<tag>_tiles.tsv with the
    period letter and its group (A/B), sheets images/<tag>/pair_sheet*.jpg."""
    global LETS, CLS
    CLS = cls; LETS = tuple(ga + gb); rng = random.Random(seed); pick = []
    for lf in ("f101r", "f188r"):
        t = tokens(lf); A = [x for x in t if x[3] in ga]; B = [x for x in t if x[3] in gb]; n = min(len(A), len(B), cap)
        print(lf, cls, "matched", len(A), "A", len(B), "B -> take", n, "each"); pick += rng.sample(A, n) + rng.sample(B, n)
    rng.shuffle(pick); cut(pick, native, tag, f"f61pair_{tag}_tiles.tsv", "pair_sheet")
    k = f"{HERE}/f61pair_{tag}_tiles.tsv"; rs = rows(k)
    with open(k, "w") as f:
        f.write("tile\tleaf\tline\tdraft_pos\tperiod_letter\tsegment\tx_px\tset\n")
        for r in rs: f.write("\t".join(r[c] for c in ("tile", "leaf", "line", "draft_pos", "period_letter", "segment", "x_px")) + "\t" + ("A" if r["period_letter"] in ga else "B") + "\n")
def score_pair(tag, path):
    """The H65 statistic on the letter-group labels (A/B): best group-to-set match, 2000 permutations seed 1, p95 of 200;
    gate: observed > p95 and P < 0.05 with at least 30 tiles scored; per leaf reported."""
    key = {int(r["tile"]): r for r in rows(f"{HERE}/f61pair_{tag}_tiles.tsv")}
    got = list(csv.DictReader((l for l in open(f"{HERE}/{path}") if not l.startswith("#")), delimiter="\t"))
    groups, labels, tab = [], [], defaultdict(lambda: defaultdict(int)); out = [f"{path}: {len(got)} rows; {len(key)} tiles"]
    for r in got:
        k = key.get(int(r["tile"])); g = r["group"].strip()
        if k is None: continue
        if g.lower() in ("", "none", "-", "x"): out.append(f"  tile {r['tile']} ({k['leaf']} {k['period_letter']}): not scored"); continue
        groups.append(g); labels.append(k["set"]); tab[g][k["set"]] += 1; tab[g][k["leaf"] + ":" + k["set"]] += 1; tab[g]["let:" + k["period_letter"]] += 1
    for g in sorted(tab): out.append(f"  group {g}: set A {tab[g]['A']}, set B {tab[g]['B']}  (" + ", ".join(f"{k} {v}" for k, v in sorted(tab[g].items()) if ":" in k) + ")")
    n = len(labels)
    if n < 30: out.append(f"scored {n} < 30: NON-TEST"); out.append("GATE: FAIL (non-test)")
    else:
        def st(gr, lb):
            gs = sorted(set(gr)); return max(sum(1 for g, l in zip(gr, lb) if dict(zip(gs, ls))[g] == l) for ls in itertools.product("AB", repeat=len(gs)))
        obs = st(groups, labels); rng = random.Random(1); c = 0
        for _ in range(2000):
            l2 = list(labels); rng.shuffle(l2); c += st(groups, l2) >= obs
        p = c / 2000; rng = random.Random(1); perm = []
        for _ in range(200):
            l2 = list(labels); rng.shuffle(l2); perm.append(st(groups, l2))
        perm.sort(); p95 = perm[189]
        out.append(f"scored {n} (A {labels.count('A')}, B {labels.count('B')}); groups {len(tab)}; observed {obs}/{n}; permutation P = {p:.4f} over 2000 (seed 1); p95 {p95}/{n}")
        out.append(f"GATE: {'PASS' if obs > p95 and p < 0.05 else 'FAIL'}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/f61pair_{tag}_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt)
if __name__ == "__main__":
    if sys.argv[1] == "build-pair":   # build-pair NATIVE CLASS a,n c,p SEED TAG
        build_pair(sys.argv[2], sys.argv[3], sys.argv[4].split(","), sys.argv[5].split(","), int(sys.argv[6]), sys.argv[7]); sys.exit(0)
    if sys.argv[1] == "score-pair":   # score-pair TAG read_call.tsv [--check]
        score_pair(sys.argv[2], sys.argv[3]); sys.exit(0)
    {"build": lambda: build(sys.argv[2]), "score": lambda: score(sys.argv[2]), "build-b": lambda: build_b(sys.argv[2]), "score-b": lambda: score_b(sys.argv[2])}[sys.argv[1]]()
