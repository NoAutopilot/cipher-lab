#!/usr/bin/env python3
"""
FAIR-CRED, 14 Oct 2026 (account 4). fair-game-2010 full-credit-text marker schemes (C1-C10 and sequence variants),
extending D2-FAIR's marker/marker_sweep.py (its judge, sequence variants, Pride windows and word pool are imported, not
copied). Data: cred/credit_lines.tsv (two blind passes on line crops, reconciled by cred/reconcile_credits.py).
Pre-registered in cred/PREREG-FAIR-CRED.md before any target score. Planted-message control first, family-wise null,
then the target in both credit-block orders.

Usage:
  python3 cred_sweep.py            run; write cred/results.json and cred/results.tsv
  python3 cred_sweep.py --check    re-run and exit 1 if results.json differs (rule 7)
"""
import csv
import json
import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "marker"))
import marker_sweep as ms  # noqa: E402

# the marked word occurs twice in the cell: which occurrence carries the mark (read from the crop)
OCCURRENCE = {11: 1}  # "...HAIR STYLIST TO NAOMI WATTS AND HAIR DEPT. HEAD": the second HAIR


def words(s):
    return [] if s in ("", "-") else re.findall(r"[A-Z]+", re.sub(r"[^A-Za-z]+", " ", re.sub(r"['’.\-]", "", s)).upper())


def first(s):
    w = words(s)
    return w[0][0] if w else ""


def load_records():
    rows, _ = ms.load_rows()
    byidx = {r["idx"]: r for r in rows}
    recs = []
    for c in csv.DictReader(open(HERE / "credit_lines.tsv"), delimiter="\t"):
        k = int(c["idx"])
        if k not in byidx:
            continue
        r = dict(byidx[k])
        ws = words(c["cell"])
        w = r["word"]
        hits = [j for j, x in enumerate(ws) if w in x]
        if len(hits) > 1 and k not in OCCURRENCE:
            raise SystemExit(f"idx {k}: {w} occurs {len(hits)}x in cell, no OCCURRENCE entry")
        wj = hits[OCCURRENCE.get(k, 0)]
        sub = ws[wj].index(w)  # e.g. NEWSVIDEOSOURCE inside ABCNEWSVIDEOSOURCE
        p = sum(len(x) for x in ws[:wj]) + sub + r["i"]
        nxt_same = c["next_role"] if c["cell_col"] == "role" else c["next_name"]
        r.update({"cell_words": ws, "wj": wj, "p": p, "other": c["other"], "next_role": c["next_role"],
                  "next_name": c["next_name"], "next_same": nxt_same})
        assert "".join(ws)[p] == r["scroll"], (k, "".join(ws), p)
        recs.append(r)
    return recs


def st(r):
    return "".join(r["cell_words"])


def at(s, j):
    return s[j] if 0 <= j < len(s) else ""


CRED = {
    "C1_nextcredit_first": lambda r: first(r["next_name"]) or first(r["next_role"]),
    "C2_cell_first": lambda r: st(r)[0],
    "C3_next_x": lambda r: at(st(r), r["p"] + 1),
    "C4_prev_x": lambda r: at(st(r), r["p"] - 1),
    "C5_other_first": lambda r: first(r["other"]),
    "C6_next_role_first": lambda r: first(r["next_role"]),
    "C7_nextword_first": lambda r: r["cell_words"][r["wj"] + 1][0] if r["wj"] + 1 < len(r["cell_words"]) else "",
    "C8_lastword_first": lambda r: r["cell_words"][-1][0],
    "C9_cell_last": lambda r: st(r)[-1],
    "C10_below": lambda r: at("".join(words(r["next_same"])), r["p"]),
}
SEQ_BASES = ("C1_nextcredit_first", "C3_next_x")
PLANT = list(CRED) + ["C1_nextcredit_first+S10_reverse", "C1_nextcredit_first+S12_interleave",
                      "C3_next_x+S11_decim2"]


def sweep(recs):
    cands = {k: "".join(f(r) for r in recs) for k, f in CRED.items()}
    for base in SEQ_BASES:
        sp = sum(1 for r in recs if r["line"] == 1 and CRED[base](r))
        for k, v in ms.seq_variants(cands[base], sp).items():
            cands[f"{base}+{k}"] = v
    return [(k, v, ms.judge(v)) for k, v in cands.items()]


def rand_rec(pool, rnd, line):
    def phrase(a, b):
        return " ".join(rnd.choice(pool) for _ in range(rnd.randint(a, b)))
    ws = phrase(1, 4).split()
    wj = rnd.randrange(len(ws))
    p = sum(len(x) for x in ws[:wj]) + rnd.randrange(len(ws[wj]))
    nr = phrase(1, 3) if rnd.random() < 0.6 else "-"
    nn = phrase(1, 3) if rnd.random() < 0.8 else "-"
    return {"cell_words": ws, "wj": wj, "p": p, "other": phrase(1, 3) if rnd.random() < 0.6 else "-",
            "next_role": nr, "next_name": nn, "next_same": rnd.choice([nr, nn]), "line": line}


def plant(scheme, plain, pool, recs, rnd):
    split = sum(1 for r in recs if r["line"] == 1)
    if "+" in scheme:
        base, seq = scheme.split("+")
        L = len(plain)
        idxs = ms.seq_variants("".join(chr(0x100 + i) for i in range(L)), split)[seq]
        m = [""] * L
        for pos, c in enumerate(idxs):
            m[ord(c) - 0x100] = plain[pos]
        letters, f = "".join(m), CRED[base]
    else:
        letters, f = plain, CRED[scheme]
    out = []
    for k, ch in enumerate(letters):
        for _ in range(200000):
            r = rand_rec(pool, rnd, 1 if k < split else 2)
            if f(r) == ch:
                out.append(r)
                break
        else:
            raise ValueError(f"cannot plant {ch} under {scheme}")
    return out


def main(check=False):
    recs = load_records()
    N = len(recs)
    pool = ms.word_pool(recs)
    # deviation logged in NOTES (before any score): add every transcribed credit word, so Z-initial words exist (ZEYAD)
    extra = set()
    for c in csv.DictReader(open(HERE / "credit_lines.tsv"), delimiter="\t"):
        for f in ("cell", "other", "next_role", "next_name"):
            extra |= {w for w in words(c[f]) if len(w) >= 2}
    pool = sorted(set(pool) | extra)
    res = {"N": N, "control": {}, "null": {}, "target": {}}
    texts = ms.pride_windows(N, 5, 20261014)
    for sc in PLANT:
        hits = top = 0
        bad = None
        for t, plain in enumerate(texts):
            try:
                dec = plant(sc, plain, pool, recs, random.Random(1000 * t + len(sc)))
            except ValueError as e:  # the scheme cannot spell this window (D2-FAIR's S7-S9 precedent): non-test
                bad = str(e)
                break
            out = sweep(dec)
            d = {k: (v, j) for k, v, j in out}
            assert d[sc][0] == plain, (sc, d[sc][0][:20], plain[:20])
            hits += d[sc][1]["pass"]
            top += max(out, key=lambda x: x[2]["score"])[0] == sc
        if bad:
            res["control"][sc] = {"recovered": 0, "trials": len(texts), "top_ranked": 0, "non_plantable": bad}
            print("control", sc, "NON-PLANTABLE", bad, flush=True)
            continue
        res["control"][sc] = {"recovered": hits, "trials": len(texts), "top_ranked": top}
        print("control", sc, hits, "/", len(texts), "top", top, flush=True)
    fp = []
    for s in range(1, 21):
        r2 = list(recs)
        random.Random(s).shuffle(r2)
        fp.append(any(j["pass"] for _, _, j in sweep(r2)))
    for s in range(101, 121):
        rnd = random.Random(s)
        out = sweep([rand_rec(pool, rnd, r["line"]) for r in recs])
        fp.append(any(j["pass"] for _, _, j in out))
    res["null"] = {"sweeps": len(fp), "false_pass": sum(fp), "rate": round(sum(fp) / len(fp), 3),
                   "candidates_per_sweep": len(out)}
    print("null", res["null"], flush=True)
    g1 = all(v["recovered"] >= 4 for v in res["control"].values())
    g2 = res["null"]["rate"] <= 0.10
    res["gates"] = {"G1_all_schemes": g1, "G1_failing": [k for k, v in res["control"].items() if v["recovered"] < 4],
                    "G2": g2}
    if g2:
        for order in ("scroll", "column"):
            out = sweep(ms.order_rows(recs, order))
            out.sort(key=lambda x: -x[2]["score"])
            res["target"][order] = {"n_pass": sum(j["pass"] for _, _, j in out),
                                    "passing": [k for k, _, j in out if j["pass"]],
                                    "top": [{"scheme": k, "text": v, **j} for k, v, j in out[:5]],
                                    "per_mark": {k: {"text": v, **j} for k, v, j in out if "+" not in k}}
            print("target", order, res["target"][order]["n_pass"],
                  [(x["scheme"], x["score"]) for x in res["target"][order]["top"]])
    else:
        res["target"] = "not run: G2 failed"
    path = HERE / "results.json"
    new = json.dumps(res, indent=1, sort_keys=True) + "\n"
    if check:
        ok = path.exists() and path.read_text() == new
        print("CHECK", "OK" if ok else "STALE")
        return 0 if ok else 1
    path.write_text(new)
    if isinstance(res["target"], dict):
        with open(HERE / "results.tsv", "w") as f:
            f.write("order\tscheme\tscore\tnull_p99\treal_p05\tcover\tpass\ttext\n")
            for order in ("scroll", "column"):
                for k, d in res["target"][order]["per_mark"].items():
                    f.write(f"{order}\t{k}\t{d['score']}\t{d['null_p99']}\t{d['real_p05']}\t{d['cover']}\t{d['pass']}\t{d['text']}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main("--check" in sys.argv))
