#!/usr/bin/env python3
"""H324 (runner 12 session_012eShPsWwW3quuzzUNV7nW5, 29 Sept 2026): is fr.3983 f.211r's DBL (5 of the run's 18 signs, H315) the glyph of key v7's
DBL cell (e/r/u, built from fr.3982 f.101r alone, H323) or the SBS glyph (b/o) drawn taller, as the readers' DBL code was on f.176r? A per-tile
forced choice in H310's format by a fresh blind Opus reader: STACKED (two loops one above the other on the stem), SIDEBYSIDE (two loops side by side at
the stem's head), NEITHER, unclear. 20 tiles, ids D01..D20, seed 324:
  known STACKED: f.101r DBL 2 -- rows of passes/f101r_align_v4.tsv coded DBL whose period letter is e, r or u and status 'agrees', located by pass A's x
    as H220 does; of the 9 such rows only L10 idx 23 and L11 idx 26 (both e) could be centred cleanly on this dense page, by hand-set
    offsets from the runner's eye on 1:1 band crops (automatic centroid centring failed: gloss and neighbouring rows) (Gallica native btv1b9060543f f210, scratch only; band boxes sheets/f101r_bands.json);
  known SIDEBYSIDE: f.61 SBS 4 (scripts/f61_positions_all.tsv: L03 14, L05 5, L11 10, L08 5 on the f61sheet_L* sheets, centroid-recentred);
  NEITHER: f.61 C43 2 (H298's tiles) and VBAR_A 2 (positions_all L01 10, L03 6);
  REF_PHI: f.61 PHI 2 (H298's tiles), reported only -- PHI is also loops on a long stem, so a STACKED answer there would make STACKED ambiguous;
  targets: f.211r DBL 5 and SBS 3 (H315's reconciled columns, x = the two passes' mean on the 2x strip images/person_pack_211r/f211r_run.jpg).
Gate, fixed before the call: >= 5 of the 6 STACKED/SIDEBYSIDE known answers right AND 4/4 NEITHER, else CONTROL FAIL. Read-out: f.211r's DBL tiles
'are the stacked (f.101r DBL) glyph' iff >= 4 of 5 answer STACKED AND neither PHI reference answers STACKED (else 'stacked, but PHI also reads
stacked: not decisive between DBL and PHI'); 'are the side-by-side (SBS) glyph' iff >= 4 of 5 answer SIDEBYSIDE; else mixed/no
read-out. The f.211r SBS tiles are reported as a check on the strip (SIDEBYSIDE expected). Descriptive, for H317's scoring rule; no key change.
python3 h324_dbl_forced.py tiles SCRATCH | score [--check]   (tiles needs SCRATCH/f101r_native.jpg)"""
import csv, json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; sys.path.insert(0, HERE)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def f101_pool():
    S = {}
    for r in rd(f"{P}/recf101r/ciphertext_draft.tsv"):
        if r["sign"] != "DASH": S.setdefault(r["line"], []).append(r)
    A = {(r["line"], int(r["pos"])): r for r in rd(f"{P}/f101r_signsA.tsv")}; out = []
    for r in rd(f"{P}/f101r_align_v4.tsv"):
        if r["kind"] != "code" or r["value"] != "DBL" or r["plain_chunk"] not in ("e", "r", "u") or r["status"] != "agrees": continue
        s = S[r["cipher_line"]][int(r["idx"])]
        if s["sign"] != "DBL": continue
        a = A.get((r["cipher_line"], int(s["position"])))
        if a and a["sign"] == "DBL": out.append(dict(line=r["cipher_line"], idx=r["idx"], letter=r["plain_chunk"], seg=a["segment"], x=int(a["x_px"])))
    return out
VB = (("VBAR_A", "f61sheet_L01", 2, 1640), ("VBAR_A", "f61sheet_L03", 2, 1780))
def items():
    rng = random.Random(324); its = []
    HAND = {("L10", "23"): (5, 75), ("L11", "26"): (10, 75)}   # hand-set centre offsets (dx from the mapped x, dy from the band top), runner's eye
    for t in f101_pool():
        if (t["line"], t["idx"]) in HAND: its.append(("STACKED", f"f101r {t['line']} idx {t['idx']} {t['letter']}", ("f101r", t["line"], t["seg"], (t["x"], HAND[(t["line"], t["idx"])]))))
    for L, seg, x in (("L03", 3, 2140), ("L05", 1, 1140), ("L11", 2, 1200), ("L08", 1, 1680)): its.append(("SIDEBYSIDE", f"f61 SBS {L}", ("f61", f"f61sheet_{L}", seg, x)))
    for cls, sh, seg, x in (("C43", "f61sheet_L03", 2, 2320), ("C43", "f61sheet_L08", 1, 770)) + VB:
        its.append(("NEITHER", f"f61 {cls}", ("f61", sh, seg, x)))
    for cls, sh, seg, x in (("PHI", "f61sheet_L11", 1, 660), ("PHI", "f61sheet_L08", 1, 450)):
        its.append(("REF_PHI", f"f61 {cls}", ("f61", sh, seg, x)))
    dr = rd(f"{P}/f211r_rec/ciphertext_draft.tsv"); xa = rd(f"{P}/f211r_passA.tsv"); xb = rd(f"{P}/f211r_passB.tsv")
    for r, a, b in zip(dr, xa, xb):
        if r["sign"] in ("DBL", "SBS"): its.append(("T_" + r["sign"], f"f211r col {r['position']}", ("f211r", "", 0, (int(a["x_sheet"]) + int(b["x_sheet"])) // 2)))
    rng.shuffle(its); return its
def crop(src, scratch):
    from PIL import Image
    kind, a, b, x = src
    if kind == "f101r":
        B = json.load(open(f"{HERE}/sheets/f101r_bands.json"))["boxes"][f"f101r_{a}_{b}.jpg"]; nat = Image.open(f"{scratch}/f101r_native.jpg").convert("L")
        (x, (dx, dy)) = x; X = B[0] + x // 2; cx, cy = X + dx, B[1] + dy
        return nat.crop((cx - 90, cy - 75, cx + 90, cy + 75))
    if kind == "f211r":
        im = Image.open(f"{HERE}/../images/person_pack_211r/f211r_run.jpg").convert("L"); return im.crop((x - 110, 140, x + 110, 420))
    import h302_ll_text as h; return h.crop("CIPHER", "", a, b, x)
def tiles(scratch):
    import h302_ll_text as h
    its = items(); ims = [(k, crop(src, scratch)) for k, _, src in its]; os.makedirs(f"{scratch}/h324", exist_ok=True)
    h.sheet(ims, f"{scratch}/h324/sheet_01.jpg", "D")
    key = ["item\tkind\tref"] + [f"D{n:02d}\t{k}\t{ref}" for n, (k, ref, _) in enumerate(its, 1)]
    open(f"{HERE}/h324_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "tiles")
def score():
    its = {r["item"]: r for r in rd(f"{HERE}/h324_items.tsv")}; a = {r["tile"].strip(): r["answer"].strip().upper() for r in rd(f"{P}/h324_forced.tsv")}
    of = lambda k: [m for m, r in its.items() if r["kind"] == k]; out = []
    for k in ("STACKED", "SIDEBYSIDE", "NEITHER", "REF_PHI", "T_DBL", "T_SBS"):
        out.append(f"{k}: " + " ".join(f"{m}={a.get(m, '-')}" for m in of(k)))
    kn = sum(a.get(m) == "STACKED" for m in of("STACKED")) + sum(a.get(m) == "SIDEBYSIDE" for m in of("SIDEBYSIDE")); ne = sum(a.get(m) == "NEITHER" for m in of("NEITHER"))
    if kn < 5 or ne < 4: out.append(f"gate: CONTROL FAIL (known {kn}/6, NEITHER {ne}/4); nothing read out")
    else:
        st = sum(a.get(m) == "STACKED" for m in of("T_DBL")); sb = sum(a.get(m) == "SIDEBYSIDE" for m in of("T_DBL")); n = len(of("T_DBL"))
        out.append(f"gate passes (known {kn}/6, NEITHER {ne}/4); f.211r DBL: STACKED {st}/{n}, SIDEBYSIDE {sb}/{n}; f.211r SBS SIDEBYSIDE {sum(a.get(m) == 'SIDEBYSIDE' for m in of('T_SBS'))}/{len(of('T_SBS'))}")
        ph = sum(a.get(m) == "STACKED" for m in of("REF_PHI")); out.append(f"PHI references STACKED {ph}/{len(of('REF_PHI'))}")
        out.append("read-out: " + (("f.211r's DBL are the stacked (f.101r DBL) glyph" if ph == 0 else "stacked, but PHI also reads stacked: not decisive between DBL and PHI") if st >= 4 else "f.211r's DBL are the side-by-side (SBS) glyph" if sb >= 4 else "mixed, no read-out"))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h324_dbl_forced_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(sys.argv[2]) if sys.argv[1] == "tiles" else score()
