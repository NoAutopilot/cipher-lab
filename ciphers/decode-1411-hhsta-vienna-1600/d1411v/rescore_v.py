#!/usr/bin/env python3
"""AM-D1411V verifier re-score of AM-D1411P5 (d1411p5/PREREG-D1411P5.md statistic, controls and PASS rule, unchanged):
four material sets x two transcriptions, for T21r, T21r_h12, T21r_h22.
  transcriptions: 'merged' = committed d1411p5/numbers.tsv (two post-score crop-split merges applied);
                  'unmerged' = d1411p5/make_numbers.py logic re-run with the four merge rows of reconcile_notes.tsv removed
                  (the registered first run, N=268).
  sets: all p.5; p5R only (f.186); independent = p.5 minus every p5L number inside the span aligned (difflib blocks >= 4) to
        p.2's cipher text (residue/numbers.tsv p2L lines + def1411/numbers.tsv, page order); copy = that span.
Controls per set at its own N: 200 order shuffles (seed 1411) p99, 23 shifted rules max, leaf gloss cover (gaps150), de1600
real-window coverage p05; Addendum A gloss agreement (10,000 value-shuffled tables, seed 1411) on each set.
  python3 d1411v/rescore_v.py [--check]   writes/compares d1411v/rescore_v.json"""
import csv, difflib, json, os, random, sys
H = os.path.dirname(os.path.abspath(__file__)); P5 = os.path.join(H, "..", "d1411p5")
sys.path.insert(0, P5)
import score_p5 as S  # noqa: E402
J = S.J

def numbers(unmerged):
    src = open(os.path.join(P5, "make_numbers.py")).read().split('txt = "\\n".join')[0]
    if unmerged:
        src = src.replace('S = {(r["line"], r["col"]): r for r in rd("reconcile_notes.tsv")}',
                          'S = {(r["line"], r["col"]): r for r in rd("reconcile_notes.tsv") if "crop-step artefact" not in r["note"]'
                          ' and not r["note"].startswith("right half of")}')
        assert "crop-step artefact" in src
    ns = {"__file__": os.path.join(P5, "make_numbers.py")}
    exec(compile(src, "make_numbers", "exec"), ns)
    rs = []
    for ln, pos, tk, g, note, gl in ns["out"][1:]:
        if tk.isdigit() and "intext" not in note:
            rs.append((ln, int(tk), g, gl))
    return rs

def p2seq():
    out = []
    for f, pre in (("residue/numbers.tsv", "p2L_"), ("def1411/numbers.tsv", "p2")):
        for r in csv.DictReader(open(os.path.join(H, "..", f)), delimiter="\t"):
            t = r["token"].rstrip("?")
            if r["line"].startswith(pre) and t.isdigit() and "intext" not in (r.get("note") or ""):
                out.append(int(t))
    return out

def copy_mask(rs, p2):
    L = [i for i, r in enumerate(rs) if r[0].startswith("p5L")]
    sm = difflib.SequenceMatcher(None, p2, [rs[i][1] for i in L], autojunk=False)
    blocks = [b for b in sm.get_matching_blocks() if b.size >= 4]
    mask = set(); eq = sum(b.size for b in blocks)
    # every p5L index between consecutive >=4 blocks whose p.2 gap is small (<= 3 numbers either side) counts as copy
    spans, cur = [], None
    for b in blocks:
        if cur and b.a - cur[1] <= 3 and b.b - cur[3] <= 3:
            cur = [cur[0], b.a + b.size, cur[2], b.b + b.size]
        else:
            if cur: spans.append(cur)
            cur = [b.a, b.a + b.size, b.b, b.b + b.size]
    if cur: spans.append(cur)
    for a0, a1, b0, b1 in spans:
        mask.update(L[k] for k in range(b0, b1))
    return mask, {"blocks_ge4": len(blocks), "equal_in_blocks": eq,
                  "spans_p5L": [[rs[L[b0]][0], rs[L[b1 - 1]][0], b1 - b0] for _, _, b0, b1 in spans]}

def score(rs, model, g_cov):
    nums = [n for _, n, _, _ in rs]; N = len(nums); out = {"N": N}
    if N < 60:
        out["note"] = "N < 60: NON-TEST under the prereg's own floor (reported descriptively)"
    real, null, cov = model.controls(N, samples=200)
    out["de1600_real_cover_p05"] = round(J.pct(sorted(cov), .05), 4)
    for k, t in S.tabs().items():
        c = model.cover(S.dec(nums, t)); rnd = random.Random(S.SEED); sh = []
        for _ in range(200):
            x = nums[:]; rnd.shuffle(x); sh.append(model.cover(S.dec(x, t)))
        shifted = [model.cover(S.dec(nums, t, s)) for s in range(1, 24)]
        p99 = J.pct(sorted(sh), .99); beats = c > p99 and c > max(shifted)
        out[k] = {"cover": round(c, 4), "shuffled_p99": round(p99, 4), "shuffled_ge": sum(x >= c for x in sh),
                  "shifted_max": round(max(shifted), 4), "minus_gloss": round(c - g_cov, 4),
                  "verdict": "PASS" if beats and c >= g_cov else ("controls beaten, below gloss" if beats else "controls not beaten")}
    gp = [(n, gl.rstrip("?").lower().translate(S.EQ)) for _, n, _, gl in rs if gl and gl != "-"]
    t = S.tabs()["T21r"]; m = sum(t[n % 24][0].translate(S.EQ) == gl for n, gl in gp)
    rnd = random.Random(S.SEED); letters = [t[i][0] for i in range(24)]; ctl = []
    for _ in range(10000):
        rnd.shuffle(letters); ctl.append(sum(letters[n % 24].translate(S.EQ) == gl for n, gl in gp))
    out["gloss_T21r"] = {"n": len(gp), "matches": m, "control_p99": J.pct(sorted(ctl), .99),
                         "agrees": bool(len(gp) >= 8 and m > J.pct(sorted(ctl), .99))}
    return out

def main():
    model = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA["de1600"]])
    g_cov = round(model.cover(open(os.path.join(H, "..", "gaps150", "gloss_text.txt")).read().strip()), 4)
    res = {"gloss_cover": g_cov}; p2 = p2seq()
    for tr in ("merged", "unmerged"):
        rs = numbers(tr == "unmerged"); mask, info = copy_mask(rs, p2)
        sets = {"all": rs, "p5R": [r for r in rs if r[0].startswith("p5R")],
                "independent": [r for i, r in enumerate(rs) if i not in mask],
                "copy": [r for i, r in enumerate(rs) if i in mask]}
        res[tr] = {"copy_alignment": info, **{k: score(v, model, g_cov) for k, v in sets.items()}}
    txt = json.dumps(res, indent=1, ensure_ascii=False) + "\n"; p = os.path.join(H, "rescore_v.json")
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("rescore_v.json", "current" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt)

if __name__ == "__main__":
    main()
