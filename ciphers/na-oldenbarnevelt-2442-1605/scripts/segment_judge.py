#!/usr/bin/env python3
"""R13-OLDSEG (6 Oct 2026): per-segment es1600 judge of the committed B/C1 reading, pre-registered in
transcription/PREREG_R13-OLDSEG.md. Four token-boundary windows; judge() per window; held-out real windows (holdout(),
200 per fold) and shuffled-decode windows as matched controls; low-confidence load per window. Writes nothing.
Run from the repository root or anywhere:  python3 ciphers/na-oldenbarnevelt-2442-1605/scripts/segment_judge.py
"""
import csv, json, math, os, random, statistics, subprocess, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__)); TGT = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(TGT))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import judge_plaintext as jp  # noqa: E402

LANG, SAMPLES, HOLD = "es1600", 400, 200


def main():
    rows = [r for r in csv.DictReader(open(os.path.join(TGT, "reading_tokens.tsv"), encoding="utf-8"), delimiter="\t")
            if r["block"] in ("B", "C1")]
    ct = [r for r in csv.DictReader(open(os.path.join(TGT, "ciphertext.tsv"), encoding="utf-8"), delimiter="\t")
          if r["block"] in ("B", "C1")]
    assert len(ct) == len(rows) and all(a["raw_token"] == b["raw_token"] for a, b in zip(ct, rows)), "token order mismatch"
    out = subprocess.run([sys.executable, os.path.join(TGT, "transcription", "diff_pass2.py"), os.path.join(TGT, "ciphertext.tsv"),
                          os.path.join(TGT, "transcription", "passE_blind_OLDPASS2.tsv")], capture_output=True, text=True,
                         check=True).stdout
    rate = {}
    for ln in out.splitlines():
        p = ln.split("\t")
        if len(p) >= 3 and "/" in p[2]:
            e, n = map(int, p[2].split("/")); rate[(p[0], int(p[1]))] = e / n if n else 0.0
    letters = [len(jp.fold(r["value"])) for r in rows]
    total = sum(letters); off = 0; win = []
    for L in letters:
        win.append(min(3, 4 * off // total)); off += L
    # shuffled decodes, committed key (as scripts/es17a_rejudge.py)
    key = json.load(open(os.path.join(TGT, "digit_key.json")))
    toks = [r["raw_used"] for r in rows]; chars = [c for t in toks for c in t]
    shuf = {}
    for seed in (1, 2, 3):
        c = chars[:]; random.Random(seed).shuffle(c); sh, i = [], 0
        for t in toks:
            sh.append("".join(c[i:i + len(t)])); i += len(t)
        shuf[seed] = ["".join(key.get(ch, ch) for ch in t) for t in sh]
    files = [str(p) for p in jp.LANG_CORPORA[LANG]]
    model = jp.NgramModel([jp.read_corpus(p) for p in files])
    res = []
    for k in range(4):
        idx = [i for i, w in enumerate(win) if w == k]
        text = " ".join(rows[i]["value"] for i in idx)
        r = jp.judge({"judge": {"language": LANG, "control_samples": SAMPLES, "min_word_cover": 0.5}}, text)
        Lc = r["checks"]["language"]; N = Lc["N"]
        hrows, blend, hs = jp.holdout(files, N, HOLD)
        sc = Lc["score"]
        fn_pos = sum(1 for x in hs if x <= sc) / len(hs)
        sd = statistics.pstdev(hs)
        shs = [round(model.score(" ".join(shuf[s][i] for i in idx)), 3) for s in (1, 2, 3)]
        wl = sum(letters[i] for i in idx)
        low = sum(letters[i] for i in idx if rows[i]["grade"] in ("M", "I")) / wl
        # per-token line rate from ciphertext.tsv's line column (same order as reading_tokens)
        clen = sum(len(rows[i]["raw_used"]) for i in idx)
        dis = sum(len(rows[i]["raw_used"]) * rate[(ct[i]["block"], int(ct[i]["line"]))] for i in idx) / clen
        span = f"{ct[idx[0]]['block']}{ct[idx[0]]['line']}-{ct[idx[-1]]['block']}{ct[idx[-1]]['line']}"
        res.append(dict(window=k, span=span, tokens=len(idx), N=N, verdict="PASS" if r["checks"]["language"]["pass"] else "FAIL",
                        score=sc, real_p05=Lc["real_p05"], real_median=Lc["real_median"], null_p99=Lc["null_p99"],
                        gap_real05_null99=round(Lc["real_p05"] - Lc["null_p99"], 3),
                        heldout_p05=round(jp.pct(hs, 0.05), 3), heldout_p95=round(jp.pct(hs, 0.95), 3), heldout_sd=round(sd, 3),
                        heldout_fn_blend_pct=round(blend, 1), heldout_share_at_or_below=round(fn_pos, 4),
                        heldout_fold_fn=[(h["file"][14:16], h.get("fn_pct")) for h in hrows],
                        shuffled_committed_key=shs, cover=r["checks"]["words"]["cover"],
                        low_MI_letter_share=round(low, 3), pass2_disagreement=round(dis, 3), text=text))
        print(json.dumps(res[-1], ensure_ascii=False), flush=True)
    # pre-registered call (item 6)
    P = [x for x in res if x["verdict"] == "PASS"]; F = [x for x in res if x["verdict"] == "FAIL"]
    lowest = [x for x in res if x["low_MI_letter_share"] == min(y["low_MI_letter_share"] for y in res)
              and x["pass2_disagreement"] == min(y["pass2_disagreement"] for y in res)]
    if P and F and all(f[m] > p[m] for f in F for p in P for m in ("low_MI_letter_share", "pass2_disagreement")):
        call = "FAIL concentrates in the low-confidence lines"
    elif not P or any(x["verdict"] == "FAIL" for x in lowest):
        call = "not concentrated"
    else:
        call = "mixed / undecided"
    print("CALL:", call, "| lowest-load-on-both window(s):", [x["window"] for x in lowest] or "none")
    # descriptive (item 7): per-letter log-prob in full-text context
    full = " ".join(r["value"] for r in rows); fl = jp.fold(full); tag = []; line_tag = []
    for i, r in enumerate(rows):
        L = len(jp.fold(r["value"])); tag += [r["grade"] in ("M", "I")] * L
        line_tag += [rate[(ct[i]["block"], int(ct[i]["line"]))]] * L
    med = statistics.median(sorted(set(rate.values())))
    lp = {True: [], False: []}; lr = {True: [], False: []}
    for j in range(3, len(fl)):
        g = fl[j - 3:j + 1]
        v = math.log10((model.c.get(g, 0) + model.k) / (model.ctx.get(g[:-1], 0) + model.V * model.k))
        lp[tag[j]].append(v); lr[line_tag[j] > med].append(v)
    print(f"DESCRIPTIVE per-letter log10P: M/I-token letters {statistics.mean(lp[True]):.3f} (n={len(lp[True])}) vs S-token "
          f"letters {statistics.mean(lp[False]):.3f} (n={len(lp[False])}); lines above median PASS2 rate ({med:.3f}) "
          f"{statistics.mean(lr[True]):.3f} (n={len(lr[True])}) vs at/below {statistics.mean(lr[False]):.3f} (n={len(lr[False])})")


if __name__ == "__main__":
    main()
