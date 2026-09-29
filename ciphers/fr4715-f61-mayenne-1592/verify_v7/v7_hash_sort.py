#!/usr/bin/env python3
"""VERIFY-F61-V7 (verifier, account 3, 29 Sept 2026): independent audit of H224 ("f.188r's HASH4 i/x rows are the 2# sign; the 4-head
reads d/q"). Written and committed BEFORE any vision call; the verifier has not looked at any tile, sheet or leaf image before this commit.
Categories were fixed by the brief before any look: 4-head, 2-hook '2#', looped, other.

 tiles SCRATCH: targets = hash-family positions (align code HASH4 or H24, or draft sign HASH4/H24 where no letters) on
   f.188r (fr.3984, Desportes; letters from its separate decipherment f.184r, passes/f188r_align_v4.tsv),
   f.101r (fr.3982; letters from its interlined period decipherment, passes/f101r_align_v4.tsv),
   f.274r (fr.3984; letters from its interlined period gloss, passes/f274_align.tsv; H24 there came from a pass-A/pass-B code split, not a shape sort),
   f.106r (fr.3983, secretary; HELD gloss -> no letters, shape vs pass code only),
   f.108r/f.108v (f.61's hand; no letters) = the 24 H212 tiles, which double as the anchor set.
   Lettered pool: rows whose letter is in I = {i,x,j,y} or DQ = {d,q}; x from pass A where pass A wrote HASH4/4STEM/H24 at that draft position.
   Sample (seed 7007): f.188r every HASH4 I/DQ row + 10 H24 I rows + every H24 DQ row; f.101r 10 HASH4 DQ + all HASH4 I + 10 H24 I + every H24 DQ; f.274r every row; f.106r 5 HASH4 + 5 H24;
   f.108 all 24 H212 tiles (T09 included as target only). 8 duplicate tiles (random targets shown twice) = repeat control.
   Geometry: native window x +-60 around (box x0 + x_px/scale) of sheets/<leaf>_bands.json, CIPHER ROW ONLY (centre-55 .. centre+60, centre = box y0 + up)
   so no interlined gloss letter is visible; 3x; grey + autocontrast on every tile (anchors too) to hide leaf ink/paper. H212 tiles: H224's anchor geometry.
   Red triangles above/below the target, ids V001.., shuffled, 20 per sheet. Two sheet sets with separate shuffles and ids: setD (with 2-hook) and setN
   (without). Keys verify_v7/v7_items.tsv committed before the calls.
 Calls: two fresh blind Opus subagents (no repo access to keys), one per set. setD categories A 4-head / D 2-hook '2#' / B looped / N other-or-cannot-tell
   (plain hash goes to N). setN categories A 4-head / B looped / N other-or-cannot-tell. Same wording for A, B, N in both.
 score (pre-stated):
   GATE per call: the 23 H212 anchor tiles (T09 excluded) answered as their H212 group (A->A, B->B) >= 0.8 (runner's 8/10), else CONTROL FAIL.
   Repeat control per call: duplicates answered identically >= 6 of 8, else the call is reported "unstable" (results shown, verdict capped at 'in part').
   setD primary: S = #(D & I) + #(A & DQ) over lettered tiles (f.188r, f.101r, f.274r); null = 20000 permutations of the shape labels WITHIN each leaf;
     p = P(S_null >= S). Read-out "split holds (2# i/x, 4-head d/q)" iff GATE PASS, p < 0.01, D I-share >= 0.7 and A DQ-share >= 0.7 pooled,
     and on each lettered leaf with >= 3 D and >= 3 A tiles the D I-share exceeds the A I-share. Per-leaf and per-code tables reported.
     H224 replicate: f.188r HASH4-coded I rows -> share answered D (H224: 8 of 11).
   setN (without D): S' = #(notA & I) + #(A & DQ), same null. Read-out "split visible without D" iff p < 0.01 and the A share of I tiles <= 0.3;
     "without D the i/x rows fold into the 4-head" iff A share of I tiles >= 0.6.
   Descriptive: f.106r and f.108 answers by pass code; f.61's one HASH4 (L01, addendum before any call: decides the meter token); H224's own reply re-scored with D folded into N.
  python3 v7_hash_sort.py tiles SCRATCH | score [--check]"""
import csv, json, os, random, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); FAM = os.path.join(HERE, "..", "family"); P = f"{FAM}/passes"; sys.path.insert(0, FAM)
SCR = "/tmp/claude-0/-home-user-cipher-lab/92abe382-b55c-561f-98aa-4d22da422faa/scratchpad/v7"
I = set("ixjy"); DQ = set("dq")
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
LEAF = {"188r": dict(draft="recf188r", A="f188r_signsA", al="f188r_align_v4", bands="f188r", nat=f"{SCR}/f188r.jpg"),
        "101r": dict(draft="recf101r", A="f101r_signsA", al="f101r_align_v4", bands="f101r", nat=f"{SCR}/f101r.jpg"),
        "274r": dict(draft="recf274", A="f274_signsA", al="f274_align", bands="f274", nat=f"{FAM}/images/3984_f274r.jpg")}
def lettered(leaf):
    c = LEAF[leaf]; S = defaultdict(list)
    for r in rd(f"{P}/{c['draft']}/ciphertext_draft.tsv"):
        if r["sign"] != "DASH": S[r["line"]].append(r)
    A = {(r["line"], int(r["pos"])): r for r in rd(f"{P}/{c['A']}.tsv")}; out = []
    for r in rd(f"{P}/{c['al']}.tsv"):
        if r["kind"] != "code" or r["value"] not in ("HASH4", "H24"): continue
        L = r["plain_chunk"].strip().lower()
        if L not in I | DQ: continue
        try: s = S[r["cipher_line"]][int(r["idx"])]
        except IndexError: continue
        a = A.get((r["cipher_line"], int(s["position"])))
        if not a or a["sign"] not in ("HASH4", "4STEM", "H24"): continue
        out.append(dict(kind="T", leaf=leaf, code=r["value"], line=r["cipher_line"], ref=r["idx"], letter=L, cls="I" if L in I else "DQ",
                        status=r["status"], seg=a["segment"], x=int(a["x_px"])))
    return out
def f106():
    import h221_shapes_106r as h221
    return [dict(t, leaf="106r", letter="-", cls="-", status="held", ref=t["pos"]) for t in h221.targets() if t["code"] in ("HASH4", "H24")]
def sample():
    rng = random.Random(7007); its = []
    p = lettered("188r"); its += [t for t in p if t["code"] == "HASH4"] + rng.sample([t for t in p if t["code"] == "H24" and t["cls"] == "I"], 10) + [t for t in p if t["code"] == "H24" and t["cls"] == "DQ"]
    p = lettered("101r"); h = [t for t in p if t["code"] == "HASH4"]
    its += rng.sample([t for t in h if t["cls"] == "DQ"], 10) + [t for t in h if t["cls"] == "I"] + rng.sample([t for t in p if t["code"] == "H24" and t["cls"] == "I"], 10) + [t for t in p if t["code"] == "H24" and t["cls"] == "DQ"]
    its += lettered("274r")
    p = f106(); its += rng.sample([t for t in p if t["code"] == "HASH4"], 5) + rng.sample([t for t in p if t["code"] == "H24"], 5)
    import h212_hash_sort as h212
    grp = {f"T{int(r['tile'].split()[-1]):02d}": r["group"].strip() for r in rd(f"{P}/h212_sort.tsv")}
    k212 = {r["item"]: r for r in rd(f"{FAM}/h212_items.tsv")}; geo = {(t["leaf"], t["line"], t["seg"], t["x"]): t for t in h212.items()}
    for m, r in sorted(k212.items()):
        g = geo[(r["leaf"], r["line"], r["segment"], int(r["x_px"]))]
        its.append(dict(g, kind="C" if m != "T09" else "T", leaf=r["leaf"], code="HASH4", ref=m, letter="-", cls="-", status="-", group=grp.get(m, "-")))
    dup = rng.sample([t for t in its if t["kind"] == "T"], 8)
    # addendum (committed before any call): f.61's single HASH4 (L01, H233's eye-placed x 1917 on images/f61sheet_L01.jpg s2), descriptive only
    its.append(dict(kind="T", leaf="61", code="HASH4", line="L01", ref="L01s2x1917", letter="-", cls="-", status="-", seg="s2", x=1917))
    return its, dup
def cut(t, nat, bands):
    from PIL import Image, ImageOps
    if t["leaf"] in LEAF or t["leaf"] == "106r":
        B, meta = bands[t["leaf"]]; b = B[f"f{'274' if t['leaf'] == '274r' else t['leaf']}_{t['line']}_{t['seg']}.jpg"]
        x = b[0] + t["x"] / meta["scale"]; cy = b[1] + meta["up"]
        w = nat[t["leaf"]].crop((int(x - 60), int(cy - 55), int(x + 60), int(cy + 60))).resize((360, 345)); mx = 180
    elif t["leaf"] == "61":
        im = Image.open(f"{FAM}/../images/f61sheet_L01.jpg").convert("RGB"); h = im.size[1] / 2
        w = im.crop((t["x"] - 150, int(h) + 10, t["x"] + 150, int(2 * h) - 6)); w = w.resize((360, int(w.height * 360 / 300))); mx = 180
    else:
        im = Image.open(t["crop"]).convert("RGB"); x0 = max(0, min(im.width - 360, t["x"] - 180))
        w = im.crop((x0, 0, x0 + 360, im.height)); mx = t["x"] - x0
    return ImageOps.autocontrast(w.convert("L"), cutoff=1).convert("RGB"), mx
def tiles(scratch):
    from PIL import Image, ImageDraw
    its, dup = sample(); nat = {k: Image.open(c["nat"]).convert("RGB") for k, c in LEAF.items()}; nat["106r"] = Image.open(f"{SCR}/f106r.jpg").convert("RGB")
    bands = {}
    for k, f in (("188r", "f188r"), ("101r", "f101r"), ("274r", "f274"), ("106r", "f106r")):
        j = json.load(open(f"{FAM}/sheets/{f}_bands.json")); bands[k] = (j["boxes"], j)
    key = ["set\tid\tkind\tleaf\tcode\tline\tref\tletter\tcls\tstatus\tgroup\tdup_of"]
    for tag, seed in (("setD", 71), ("setN", 72)):
        rows = [dict(t, dup="") for t in its] + [dict(t, dup="dup") for t in dup]; random.Random(seed).shuffle(rows); ims = []; first = {}
        os.makedirs(f"{scratch}/{tag}", exist_ok=True)
        for n, t in enumerate(rows, 1):
            tid = f"{'V' if tag == 'setD' else 'W'}{n:03d}"; w, mx = cut(t, nat, bands)
            c = Image.new("RGB", (370, 420), "white"); d = ImageDraw.Draw(c); c.paste(w, (5, 22)); y = 22 + w.height; mx += 5
            d.polygon([(mx - 8, 2), (mx + 8, 2), (mx, 18)], fill=(220, 0, 0)); d.polygon([(mx - 8, y + 19), (mx + 8, y + 19), (mx, y + 3)], fill=(220, 0, 0))
            d.text((315, 4), tid, fill=(0, 0, 0)); ims.append(c)
            k = (t["leaf"], t["line"], t.get("seg"), t["x"])
            if t["dup"]: dof = first[k]
            else: first[k] = tid; dof = ""
            key.append("\t".join([tag, tid, t["kind"], t["leaf"], t["code"], t["line"], str(t["ref"]), t["letter"], t["cls"], t["status"], t.get("group", "-"), dof]))
        for s0 in range(0, len(ims), 20):
            sh = Image.new("RGB", (4 * 370, 5 * 420), "white")
            for k2, c in enumerate(ims[s0:s0 + 20]): sh.paste(c, ((k2 % 4) * 370, (k2 // 4) * 420))
            sh.save(f"{scratch}/{tag}/sheet_{s0 // 20 + 1:02d}.jpg", quality=90)
    open(f"{HERE}/v7_items.tsv", "w").write("\n".join(key) + "\n")
    print(len(its), "tiles +", len(dup), "dups;", Counter((t["leaf"], t["code"], t["cls"]) for t in its if t["kind"] == "T"))
def S_stat(rows, lab, conc):
    return sum(conc(lab[i], r["cls"]) for i, r in enumerate(rows))
def perm(rows, ans, conc, n=20000, seed=77):
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
    its = rd(f"{HERE}/v7_items.tsv"); out = []
    for tag, rep in (("setD", "v7_reply_setD.tsv"), ("setN", "v7_reply_setN.tsv")):
        ans = {r["id"].strip(): r["answer"].strip().upper()[:1] for r in rd(f"{HERE}/{rep}")}
        R = [dict(r) for r in its if r["set"] == tag]; [r.update(ans=ans.get(r["id"], "N")) for r in R]
        C = [r for r in R if r["kind"] == "C"]; hit = sum(r["ans"] == r["group"] for r in C); gate = hit >= 0.8 * len(C)
        D = [r for r in R if r["dup_of"]]; same = sum(r["ans"] == ans.get(r["dup_of"], "?") for r in D)
        out.append(f"== {tag}: anchor gate {hit}/{len(C)} H212 tiles as their group (>= 0.8) -> {'PASS' if gate else 'CONTROL FAIL'}; "
                   f"anchor A answered {Counter(r['ans'] for r in C if r['group']=='A')}, B answered {Counter(r['ans'] for r in C if r['group']=='B')}")
        out.append(f"   repeat control: {same}/{len(D)} duplicates identical (>= 6) -> {'stable' if same >= 6 else 'unstable'}")
        T = [r for r in R if r["kind"] == "T" and not r["dup_of"]]; lt = [r for r in T if r["cls"] in ("I", "DQ")]
        for leaf in ("188r", "101r", "274r", "106r", "108r", "108v", "61"):
            for code in ("HASH4", "H24"):
                g = [r for r in T if r["leaf"] == leaf and r["code"] == code]
                if not g: continue
                if leaf in ("188r", "101r", "274r"):
                    out.append(f"   f.{leaf} {code}: " + "; ".join(f"{cl} " + " ".join(f"{k}{v}" for k, v in sorted(Counter(r['ans'] for r in g if r['cls'] == cl).items())) for cl in ("I", "DQ") if any(r['cls'] == cl for r in g)))
                else:
                    out.append(f"   f.{leaf} {code}: " + " ".join(f"{k}{v}" for k, v in sorted(Counter(r['ans'] for r in g).items())))
        if tag == "setD":
            conc = lambda a, c: (a == "D" and c == "I") or (a == "A" and c == "DQ")
            obs, p = perm(lt, {r["id"]: r["ans"] for r in lt}, conc)
            dI = sum(r["ans"] == "D" and r["cls"] == "I" for r in lt); dn = sum(r["ans"] == "D" for r in lt)
            aD = sum(r["ans"] == "A" and r["cls"] == "DQ" for r in lt); an = sum(r["ans"] == "A" for r in lt)
            ok_leaf = True; pl = []
            for leaf in ("188r", "101r", "274r"):
                g = [r for r in lt if r["leaf"] == leaf]; dd = [r for r in g if r["ans"] == "D"]; aa = [r for r in g if r["ans"] == "A"]
                si = lambda x: sum(r["cls"] == "I" for r in x) / max(1, len(x))
                pl.append(f"f.{leaf} D {len(dd)} (I-share {si(dd):.2f}) A {len(aa)} (I-share {si(aa):.2f})")
                if len(dd) >= 3 and len(aa) >= 3 and not si(dd) > si(aa): ok_leaf = False
            h = [r for r in lt if r["leaf"] == "188r" and r["code"] == "HASH4" and r["cls"] == "I"]
            out.append(f"   primary S = {obs} of {len(lt)} lettered; within-leaf permutation p = {p:.2g}; D I-share {dI}/{dn} = {dI/max(1,dn):.2f}; A DQ-share {aD}/{an} = {aD/max(1,an):.2f}")
            out.append("   per leaf: " + "; ".join(pl))
            out.append(f"   H224 replicate: f.188r HASH4-coded I rows answered D {sum(r['ans']=='D' for r in h)}/{len(h)} ({Counter(r['ans'] for r in h)}) (H224: 8 of 11)")
            ok = gate and p < 0.01 and dI / max(1, dn) >= 0.7 and aD / max(1, an) >= 0.7 and ok_leaf
            out.append("   read-out: " + ("split holds (2# i/x, 4-head d/q)" if ok else "split not shown by the registered rule"))
        else:
            conc = lambda a, c: (a != "A" and c == "I") or (a == "A" and c == "DQ")
            obs, p = perm(lt, {r["id"]: r["ans"] for r in lt}, conc)
            Ir = [r for r in lt if r["cls"] == "I"]; ash = sum(r["ans"] == "A" for r in Ir) / max(1, len(Ir))
            out.append(f"   S' = {obs} of {len(lt)}; within-leaf permutation p = {p:.2g}; A share of I tiles {ash:.2f} (n {len(Ir)}); I answered {Counter(r['ans'] for r in Ir)}")
            out.append("   read-out: " + ("split visible without D" if gate and p < 0.01 and ash <= 0.3 else
                                          "without D the i/x rows fold into the 4-head" if ash >= 0.6 else "without D: mixed"))
    h = {r["item"]: r for r in rd(f"{FAM}/h224_items.tsv")}; a = {r["id"]: r["answer"].strip().upper() for r in rd(f"{P}/h224_reply.tsv")}
    t = Counter((("N" if a.get(k) in ("D", "C") else a.get(k, "N")), r["group"]) for k, r in h.items() if r["kind"] == "T")
    out.append(f"== H224 reply with D (and C) folded into 'other': {dict(t)} -- i.e. without its post-look category the runner's own call says only 'the i/x rows are not the 4-head' (2 of 11 A)")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/v7_hash_sort_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(sys.argv[2]) if sys.argv[1] == "tiles" else score()
