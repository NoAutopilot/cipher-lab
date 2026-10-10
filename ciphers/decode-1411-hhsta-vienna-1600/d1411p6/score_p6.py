#!/usr/bin/env python3
"""D1411P6 gate (d1411p6/PREREG-D1411P6.md; a copy of d1411p5/score_p5.py, paths changed, plus the AM-D1411V copy mask):
decode d1411p6/numbers.tsv (p.6 numerals, never read before) minus every number aligned to an already-read page, with frozen T21r and
two h variants (residue 12 = h; residue 22 = h); word coverage (tools/judge_plaintext.py NgramModel.cover, de1600 lexicon)
against shuffled-target (200, seed 1411) and shifted-rule controls and the leaf's own gloss coverage; letter tests at
residues 12, 21, 22 (coverage and 4-gram); Addendum A gloss-agreement test against value-shuffled tables.

  python3 d1411p6/score_p6.py                  write decode_*.txt and score_p6.json; print the verdict
  python3 d1411p6/score_p6.py --check          exit 1 if committed decodes or score_p6.json are stale (rule 7)
  python3 d1411p6/score_p6.py --reproduce-p5   p.5 numbers, mask against p.2 only (as d1411v/rescore_v.py); must give
                                               independent N=136, T21r cover 0.5882 (AM-D1411V); prints, writes nothing
Copy mask (copy_mask below, d1411v/rescore_v.py's rule generalised to every prior page and every p.6 line): for each
already-read page sequence (p.1 p1L, p.1 gloss lines, p.2 p2L+p2Lb+p2R, p.3, p.4, p.5; each in its numbers.tsv order),
difflib.SequenceMatcher(autojunk=False) against the whole p.6 sequence; matching blocks of >= 4 numbers; consecutive
blocks whose gaps are <= 3 numbers on both sides merge into one span; every p.6 number inside a span is masked. The union
over pages is excluded; the remaining 'independent' numbers are the registered material.
"""
import csv, difflib, json, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
FOLDER = os.path.join(HERE, "..")
NUMBERS = os.path.join(HERE, "numbers.tsv")
ROOT = os.path.join(HERE, "..", "..", "..")
sys.path.insert(0, os.path.join(HERE, "..", "def1411")); sys.path.insert(0, os.path.join(ROOT, "tools"))
import tables  # noqa: E402
import judge_plaintext as J  # noqa: E402

ALPHA = "abcdefghiklmnopqrstuwxyz"
SEED = 1411
EQ = str.maketrans({"v": "u", "j": "i", "ů": "u"})


def tabs():
    t = tables.tables()["T21r"]
    h12 = dict(t); h12[12] = ("h",) + t[12][1:]
    h22 = dict(t); h22[22] = ("h",) + t[22][1:]
    return {"T21r": t, "T21r_h12": h12, "T21r_h22": h22}


def rows():
    out = []
    for r in csv.DictReader(open(NUMBERS), delimiter="\t"):
        tk = r["token"].rstrip("?")
        if tk.isdigit() and "intext" not in r.get("note", ""):
            out.append((r["line"], int(tk), r["grade"], (r.get("gloss") or "").strip()))
    return out


def dec(nums, tab, shift=0):
    return "".join(tab[(n + shift) % 24][0] for n in nums)


def decode_text(rs, tab):
    out, cur, line = [], [], None
    for ln, n, g, _ in rs:
        if ln != line and cur:
            out.append(f"{line}\t{''.join(cur)}"); cur = []
        line = ln; c = tab[n % 24][0]; cur.append(c.upper() if g == "M" else c)
    if cur:
        out.append(f"{line}\t{''.join(cur)}")
    return "\n".join(out) + "\n"


def seq(f, pre=""):
    out = []
    for r in csv.DictReader(open(os.path.join(FOLDER, f)), delimiter="\t"):
        t = r["token"].rstrip("?")
        if r["line"].startswith(pre) and t.isdigit() and "intext" not in (r.get("note") or ""):
            out.append(int(t))
    return out


def prior_pages(only_p2=False):
    p2 = seq("residue/numbers.tsv", "p2L_") + seq("def1411/numbers.tsv", "p2")
    if only_p2:
        return {"p2": p2}
    return {"p1": seq("residue/numbers.tsv", "p1L"), "p1gloss": seq("gloss/pairs.tsv"), "p2": p2,
            "p3": seq("d4p3/numbers.tsv"), "p4": seq("d1411p4/numbers.tsv"), "p5": seq("d1411p5/numbers.tsv")}


def copy_mask(rs, pages, line_prefix=""):
    L = [i for i, r in enumerate(rs) if r[0].startswith(line_prefix)]
    mask, info = set(), {}
    for name, pg in pages.items():
        sm = difflib.SequenceMatcher(None, pg, [rs[i][1] for i in L], autojunk=False)
        blocks = [b for b in sm.get_matching_blocks() if b.size >= 4]
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
        info[name] = {"blocks_ge4": len(blocks), "equal_in_blocks": sum(b.size for b in blocks),
                      "spans": [[rs[L[b0]][0], rs[L[b1 - 1]][0], b1 - b0] for _, _, b0, b1 in spans]}
    return mask, info


def reproduce_p5():
    global NUMBERS
    NUMBERS = os.path.join(FOLDER, "d1411p5", "numbers.tsv")
    rs = rows(); mask, info = copy_mask(rs, prior_pages(only_p2=True), "p5L")
    ind = [n for i, (_, n, _, _) in enumerate(rs) if i not in mask]
    model = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA["de1600"]])
    out = {"N_all": len(rs), "N_independent": len(ind), "spans": info["p2"]["spans"]}
    for k, t in tabs().items():
        out[k] = round(model.cover(dec(ind, t)), 4)
    print(json.dumps(out)); ok = out["N_independent"] == 136 and out["T21r"] == 0.5882
    print("reproduce p.5 (AM-D1411V independent N=136, T21r 0.5882):", "OK" if ok else "DIFFERS"); sys.exit(0 if ok else 1)


def main():
    if "--reproduce-p5" in sys.argv:
        reproduce_p5()
    allrs = rows(); mask, mask_info = copy_mask(allrs, prior_pages())
    rs = [r for i, r in enumerate(allrs) if i not in mask]; nums = [n for _, n, _, _ in rs]; T = tabs()
    texts = {k: decode_text(rs, t) for k, t in T.items()}
    if "--check" in sys.argv:
        ok = all(os.path.exists(os.path.join(HERE, f"decode_{k}.txt")) and
                 open(os.path.join(HERE, f"decode_{k}.txt")).read() == v for k, v in texts.items())
        ok = ok and os.path.exists(os.path.join(HERE, "score_p6.json"))
        print("d1411p6", "current" if ok else "STALE"); sys.exit(0 if ok else 1)
    for k, v in texts.items():
        open(os.path.join(HERE, f"decode_{k}.txt"), "w").write(v)
    N = len(nums)
    res = {"N_all_p6": len(allrs), "N_masked": len(mask), "copy_mask": mask_info, "N": N, "n_M": sum(g == "M" for _, _, g, _ in rs),
           "residue_counts": {str(R): sum(n % 24 == R for n in nums) for R in (12, 21, 22)}}
    if N < 60:
        res["verdict"] = "NON-TEST (N < 60)"
        json.dump(res, open(os.path.join(HERE, "score_p6.json"), "w"), indent=1); print(json.dumps(res, indent=1)); return
    model = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA["de1600"]])
    p = lambda a, q: round(J.pct(sorted(a), q), 4)
    gloss = open(os.path.join(HERE, "..", "gaps150", "gloss_text.txt")).read().strip()
    g_cov = round(model.cover(gloss), 4)
    real, null, cov = model.controls(N, samples=200)
    res["calibration"] = {"lexicon_words": len(model.words), "gloss_cover": g_cov, "real_cover_p05": p(cov, .05),
                          "real_cover_median": p(cov, .5), "real_p05_4gram": p(real, .05), "null_p99_4gram": p(null, .99)}
    for k, t in T.items():
        c = model.cover(dec(nums, t)); rnd = random.Random(SEED); shuf = []
        for _ in range(200):
            x = nums[:]; rnd.shuffle(x); shuf.append(model.cover(dec(x, t)))
        shifted = [model.cover(dec(nums, t, s)) for s in range(1, 24)]
        r = {"cover": round(c, 4), "shuffled_p99": p(shuf, .99), "shuffled_mean": round(sum(shuf) / 200, 4),
             "shuffled_ge": sum(x >= c for x in shuf), "shifted_max": round(max(shifted), 4),
             "shifted_ge": sum(x >= c for x in shifted), "minus_gloss": round(c - g_cov, 4),
             "fourgram": round(model.score(dec(nums, t)), 4)}
        r["beats_controls"] = bool(c > r["shuffled_p99"] and c > r["shifted_max"])
        r["PASS"] = bool(r["beats_controls"] and c >= g_cov)
        r["verdict"] = ("PASS" if r["PASS"] else "controls beaten, coverage below the leaf's own gloss" if r["beats_controls"]
                        else "not supported on p.6 (conditional on the transcription)")
        res[k] = r
    base = T["T21r"]; lt = {}
    for R in (12, 21, 22):
        cv, fg = {}, {}
        for L in ALPHA:
            t = dict(base); t[R] = (L,) + base[R][1:]; d = dec(nums, t)
            cv[L] = round(model.cover(d), 4); fg[L] = round(model.score(d), 4)
        oc = sorted(ALPHA, key=lambda L: (-cv[L], L)); of = sorted(ALPHA, key=lambda L: (-fg[L], L))
        n_R = res["residue_counts"][str(R)]
        want = {12: ("h", "s"), 21: ("r", "z"), 22: ("h", "s")}[R]
        v = "undecided"
        if n_R >= 5:
            for L in want:
                if oc[0] == L and of[0] == L:
                    v = f"{L} favoured"
        lt[str(R)] = {"n": n_R, "cover_top5": oc[:5], "fourgram_top5": of[:5],
                      "rank_cover": {L: oc.index(L) + 1 for L in want}, "rank_fourgram": {L: of.index(L) + 1 for L in want},
                      "verdict": v}
    res["letter_tests"] = lt
    # prereg secondary, descriptive only: pooled p.3 + p.4 + p.5 + p.6 (independent) h-vs-s ranks at residues 12 and 22
    p3 = []
    for src in (("d4p3", "numbers.tsv"), ("d1411p4", "numbers.tsv"), ("d1411p5", "numbers.tsv")):
        for r in csv.DictReader(open(os.path.join(HERE, "..", *src)), delimiter="\t"):
            tk = r["token"].rstrip("?")
            if tk.isdigit() and "intext" not in r.get("note", ""):
                p3.append(int(tk))
    pool = p3 + nums; pl = {"N": len(pool)}
    for R in (12, 22):
        cv, fg = {}, {}
        for L in ALPHA:
            t = dict(base); t[R] = (L,) + base[R][1:]; d = dec(pool, t)
            cv[L] = model.cover(d); fg[L] = model.score(d)
        oc = sorted(ALPHA, key=lambda L: (-cv[L], L)); of = sorted(ALPHA, key=lambda L: (-fg[L], L))
        pl[str(R)] = {"n": sum(n % 24 == R for n in pool), "cover_top5": oc[:5], "fourgram_top5": of[:5],
                      "rank_cover": {L: oc.index(L) + 1 for L in "hs"}, "rank_fourgram": {L: of.index(L) + 1 for L in "hs"}}
    res["pooled_p3_p4_p5_p6_descriptive"] = pl
    # Addendum A: gloss agreement
    gp = [(n, gl.rstrip("?").lower().translate(EQ)) for _, n, g, gl in rs if gl and gl not in ("-",)]
    ga = {"n_glossed": len(gp)}
    if len(gp) >= 8:
        for k, t in T.items():
            m = sum(t[n % 24][0].translate(EQ) == gl for n, gl in gp)
            rnd = random.Random(SEED); letters = [t[i][0] for i in range(24)]; ctl = []
            for _ in range(10000):
                rnd.shuffle(letters); ctl.append(sum(letters[n % 24].translate(EQ) == gl for n, gl in gp))
            ga[k] = {"matches": m, "rate": round(m / len(gp), 4), "control_p99": p(ctl, .99),
                     "control_ge": sum(x >= m for x in ctl), "agrees": bool(m > J.pct(sorted(ctl), .99))}
        ga["pairs"] = [[n, gl, T["T21r"][n % 24][0]] for n, gl in gp]
    else:
        ga["verdict"] = "NON-TEST (< 8 glossed numbers)"
    res["gloss_agreement"] = ga
    an = [n for _, n, _, _ in allrs]; res["all_p6_descriptive"] = {"N": len(an)}
    for k, t in T.items():
        res["all_p6_descriptive"][k] = round(model.cover(dec(an, t)), 4)
    json.dump(res, open(os.path.join(HERE, "score_p6.json"), "w"), indent=1)
    print(json.dumps({k: v for k, v in res.items() if k not in ("letter_tests", "gloss_agreement")}, indent=1))
    print("letter_tests:", json.dumps(lt))
    print("gloss_agreement:", json.dumps({k: v for k, v in ga.items() if k != "pairs"}))


if __name__ == "__main__":
    main()
