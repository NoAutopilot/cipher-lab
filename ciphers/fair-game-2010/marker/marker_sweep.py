#!/usr/bin/env python3
"""
D2-FAIR, 8 Oct 2026 (account 2). fair-game-2010 marker-scheme sweep with a planted-message control and a
family-wise null, pre-registered in PREREG-D2-FAIR.md (this folder). Our own code; the marker-scheme idea is
cited from aaymeloglu/unsolved-ciphers SHORTLIST.md (no licence, nothing copied).

Usage:
  python3 marker_sweep.py            run controls, null and target; write results.json and results.tsv here
  python3 marker_sweep.py --check    re-run and exit 1 if results.json differs (rule 7)
"""
import csv
import math
import json
import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "tools"))
sys.path.insert(0, str(REPO / "specs" / "cheap-tests" / "fair-game-2010"))
import judge_plaintext as jp  # noqa: E402
from credits_words import TOKENS  # noqa: E402

SPEC = json.load(open(REPO / "specs" / "fair-game-2010.json"))
J = SPEC["judge"]
MODEL = jp.NgramModel([jp.read_corpus(p) for p in jp.LANG_CORPORA["en"]])
_CTRL = {}


def judge(s):
    """Same logic as tools/judge_plaintext.py _judge (language + words), minus the length check."""
    s = jp.fold(s)
    N = max(len(s), 20)
    if N not in _CTRL:
        real, null, cov = MODEL.controls(N, samples=int(J.get("control_samples", 200)))
        _CTRL[N] = (jp.pct(null, 0.99), jp.pct(real, 0.05))
    n99, r05 = _CTRL[N]
    sc = MODEL.score(s) if len(s) >= 4 else -9.9
    cv = MODEL.cover(s)
    return {"score": round(sc, 3), "null_p99": round(n99, 3), "real_p05": round(r05, 3), "cover": round(cv, 3),
            "pass": bool(sc > n99 and sc > r05 and cv >= J["min_word_cover"])}


# ---------------- data ----------------
def letters_only(w):
    return re.sub(r"[^A-Z]", "", w.upper())


def load_rows():
    toks = [(t.upper(), [i for i, c in enumerate(t) if c.isupper()]) for t in TOKENS]
    usedtok = set()
    rows, amb = [], 0
    with open(HERE.parent / "reconcile_2026-10-03.tsv") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            if r["image_letter"] == "?":
                continue
            w = letters_only(r["credit_word"])
            ch = r["spec_ATS"]
            occ = [i for i, c in enumerate(w) if c == ch]
            idx = None
            for k, (tw, caps) in enumerate(toks):  # Mulliss's capital, first unused matching (token, capital)
                for i in caps:
                    if tw == w and (k, i) not in usedtok and w[i] == ch:
                        idx = i
                        usedtok.add((k, i))
                        break
                if idx is not None:
                    break
            if idx is None:
                if not occ:
                    raise SystemExit(f"letter {ch} not in {w}")
                idx = occ[0]
                if len(occ) > 1:
                    amb += 1
            rows.append({"idx": int(r["idx"]), "line": int(r["line"]), "word": w, "i": idx, "scroll": ch,
                         "column": r["schmeh_2026"]})
    return rows, amb


def order_rows(rows, order):
    """scroll order = table order; column order = rows permuted so that marked letters read as Schmeh 2026."""
    if order == "scroll":
        return list(rows)
    out, pool = [], list(rows)
    blk = [r for r in rows if r["scroll"] != r["column"]]
    for r in rows:
        if r["scroll"] == r["column"]:
            out.append(r)
        else:
            m = next(b for b in blk if b["scroll"] == r["column"])
            blk.remove(m)
            out.append(m)
    return out


# ---------------- schemes ----------------
def off(k):
    def f(w, i):
        j = i + k
        return w[j] if 0 <= j < len(w) else ""
    return f


def a1z26(n):
    return chr(64 + n) if 1 <= n <= 26 else ""


PER_MARK = {
    "S0_marked": off(0), "S1_next": off(1), "S2_prev": off(-1), "S3_plus2": off(2), "S4_minus2": off(-2),
    "S5_word_first": lambda w, i: w[0], "S6_word_last": lambda w, i: w[-1],
    "S7_index_a1z26": lambda w, i: a1z26(i + 1), "S8_index_from_end_a1z26": lambda w, i: a1z26(len(w) - i),
    "S9_wordlen_a1z26": lambda w, i: a1z26(len(w)),
}
PLANTABLE_PM = ["S0_marked", "S1_next", "S2_prev", "S3_plus2", "S4_minus2", "S5_word_first", "S6_word_last"]


def decimate(s, n):
    L = len(s)
    return "".join(s[(k * n) % L] for k in range(L))


def seq_variants(s, split):
    """S10 reverse, S11 decimations n=2..L-1, S12 interleave of the two lines (split = letters in line 1)."""
    out = {"S10_reverse": s[::-1]}
    L = len(s)
    for n in range(2, L):
        if L % n and math.gcd(n, L) == 1:
            out[f"S11_decim{n}"] = decimate(s, n)
    a, b = s[:split], s[split:]
    out["S12_interleave"] = "".join(x + y for x, y in zip(a, b)) + a[len(b):] + b[len(a):]
    return out


def sweep(rows):
    """rows: ordered list of dicts with word, i, line. Returns list of (name, text, judge)."""
    cands = {}
    for name, f in PER_MARK.items():
        cands[name] = "".join(f(r["word"], r["i"]) for r in rows)
    split = sum(1 for r in rows if r["line"] == 1)
    for base in ("S0_marked", "S1_next"):
        s = cands[base]
        sp = sum(1 for r in rows if r["line"] == 1 and PER_MARK[base](r["word"], r["i"]))
        for k, v in seq_variants(s, sp).items():
            cands[f"{base}+{k}"] = v
    return [(k, v, judge(v)) for k, v in cands.items()]


# ---------------- controls ----------------
def pride_windows(n, k, seed):
    raw = jp.fold(jp.read_corpus(REPO / "tools" / "data" / "en" / "pg1342_pride.txt"))
    rnd = random.Random(seed)
    return [raw[(j := rnd.randrange(0, len(raw) - n)):j + n].upper() for _ in range(k)]


def word_pool(rows):
    t = jp.read_corpus(REPO / "tools" / "data" / "en" / "pg1342_pride.txt")
    ws = {w.upper() for w in re.findall(r"[A-Za-z]{3,12}", t)}
    return sorted(ws | {r["word"] for r in rows})


def plant(scheme, plain, pool, rows, rnd):
    """Decoy rows (word, i, line) whose scheme letters spell plain."""
    out = []
    split = sum(1 for r in rows if r["line"] == 1)
    if scheme.startswith("S0_marked+"):
        seq_name = scheme.split("+")[1]
        L = len(plain)
        # find marked string m with seq_variant(m) == plain via the permutation on indices
        idxs = seq_variants("".join(chr(0x100 + i) for i in range(L)), split)[seq_name]
        m = [""] * L
        for pos, c in enumerate(idxs):
            m[ord(c) - 0x100] = plain[pos]
        target_letters, f = "".join(m), PER_MARK["S0_marked"]
    else:
        target_letters, f = plain, PER_MARK[scheme]
    for k, ch in enumerate(target_letters):
        for _ in range(10000):
            w = rnd.choice(pool)
            opts = [i for i in range(len(w)) if f(w, i) == ch]
            if opts:
                out.append({"word": w, "i": rnd.choice(opts), "line": 1 if k < split else 2})
                break
        else:
            raise SystemExit(f"cannot plant {ch} under {scheme}")
    return out


def main(check=False):
    rows, amb = load_rows()
    N = len(rows)
    pool = word_pool(rows)
    res = {"N": N, "ambiguous_index": amb, "control": {}, "null": {}, "target": {}}

    # (a) planted control
    plant_schemes = PLANTABLE_PM + ["S0_marked+S10_reverse", "S0_marked+S11_decim2", "S0_marked+S11_decim5",
                                    "S0_marked+S11_decim17", "S0_marked+S12_interleave"]
    texts = pride_windows(N, 5, 20261008)
    for sc in plant_schemes:
        hits, top = 0, 0
        for t, plain in enumerate(texts):
            rnd = random.Random(1000 * t + len(sc))
            dec = plant(sc, plain, pool, rows, rnd)
            out = sweep(dec)
            d = {k: (v, j) for k, v, j in out}
            assert d[sc][0] == plain, (sc, d[sc][0][:20], plain[:20])
            hits += d[sc][1]["pass"]
            best = max(out, key=lambda x: x[2]["score"])[0]
            top += best == sc
        res["control"][sc] = {"recovered": hits, "trials": len(texts), "top_ranked": top}
        print("control", sc, hits, "/", len(texts), "top", top, flush=True)
    res["control"]["non_plantable"] = ["S7_index_a1z26", "S8_index_from_end_a1z26", "S9_wordlen_a1z26"]

    # (b) null
    fp = []
    for s in range(1, 21):
        r2 = list(rows)
        random.Random(s).shuffle(r2)
        out = sweep(r2)
        fp.append(any(j["pass"] for _, _, j in out))
    for s in range(101, 121):
        rnd = random.Random(s)
        dec = []
        for r in rows:
            w = rnd.choice(pool)
            dec.append({"word": w, "i": rnd.randrange(len(w)), "line": r["line"]})
        out = sweep(dec)
        fp.append(any(j["pass"] for _, _, j in out))
    res["null"] = {"sweeps": len(fp), "false_pass": sum(fp), "rate": round(sum(fp) / len(fp), 3),
                   "candidates_per_sweep": len(out)}
    print("null", res["null"], flush=True)

    # target
    for order in ("scroll", "column"):
        out = sweep(order_rows(rows, order))
        out.sort(key=lambda x: -x[2]["score"])
        res["target"][order] = {
            "n_pass": sum(j["pass"] for _, _, j in out),
            "top": [{"scheme": k, "text": v, **j} for k, v, j in out[:5]],
            "per_mark": {k: {"text": v, **j} for k, v, j in out if "+" not in k},
        }
        print("target", order, res["target"][order]["n_pass"], [(x["scheme"], x["score"]) for x in res["target"][order]["top"]])
    path = HERE / "results.json"
    new = json.dumps(res, indent=1, sort_keys=True)
    if check:
        ok = path.exists() and path.read_text() == new + "\n"
        print("CHECK", "OK" if ok else "STALE")
        return 0 if ok else 1
    path.write_text(new + "\n")
    with open(HERE / "results.tsv", "w") as f:
        f.write("order\tscheme\tscore\tnull_p99\treal_p05\tcover\tpass\ttext\n")
        for order in ("scroll", "column"):
            for k, d in res["target"][order]["per_mark"].items():
                f.write(f"{order}\t{k}\t{d['score']}\t{d['null_p99']}\t{d['real_p05']}\t{d['cover']}\t{d['pass']}\t{d['text']}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main("--check" in sys.argv))
