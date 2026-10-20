#!/usr/bin/env python3
"""MONL-KING2 (20 Oct 2026): gated decode statistics for f.133 (c258) L01-L10 under key.tsv (PREREG-MONL-KING2.md).

Statistics on the straight key decode (keyed tokens only; W:, ? and unkeyed tokens break a run and add no letter):
  run   longest run, in letters, of fr16 lexicon words >= 2 letters (tools/segmenter.py segment(); a one-letter
        lexicon word counts only between two such words, as segmenter.fragments())
  lm    mean log10 4-gram probability per letter under the judge's fr corpus (judge_plaintext NgramModel.score)
Null: the same tokens under 20 value-shuffled keys (plain column permuted over the key ids), p95.
Positive control: the f.138r-v decode (ciphertext_c268.tsv then ciphertext_c269.tsv, sign column) in non-overlapping windows
of the target's keyed-token count N; window 1 (c268 from L01) must beat its own null on both statistics; [min, max] over all
windows is the true-key range. Noise variant: window 1 with a share r of keyed tokens replaced by random key ids (r = the
target's measured pass disagreement), 20 draws, median.

  python3 king2_score.py --control-only            control at N = c268 L01-L10's keyed count (before any target line exists)
  python3 king2_score.py --target ../ciphertext_c258.tsv --noise R   full gated run, writes results_king2.json
"""
import argparse, json, random, statistics, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import judge_plaintext as jp
import segmenter as sg

def load_key():
    k = {}
    for ln in (HERE.parent / "key.tsv").read_text().splitlines()[1:]:
        f = ln.split("\t")
        if len(f) >= 3 and f[2]:
            k[f[0]] = f[2]
    return k

def load_tokens(p, lines=None):
    rows = (HERE.parent / p if not Path(p).is_absolute() else Path(p)).read_text().splitlines()
    hdr = rows[0].split("\t"); i_line, i_sign = hdr.index("line"), hdr.index("sign")
    out = []
    for r in rows[1:]:
        f = r.split("\t")
        if lines and f[i_line] not in lines:
            continue
        out.append(f[i_sign])
    return out

def decode(toks, key):
    segs, cur = [], ""
    for t in toks:
        if t in key:
            cur += key[t]
        else:
            if cur: segs.append(cur)
            cur = ""
    if cur: segs.append(cur)
    return segs

def longest_run(segs, lex):
    best = 0
    for s in segs:
        toks = sg.segment(s, lex)
        good = [ok and len(t) >= 2 for t, ok in toks]
        for i, (t, ok) in enumerate(toks):
            if ok and len(t) == 1 and 0 < i < len(toks) - 1 and good[i - 1] and good[i + 1]:
                good[i] = True
        run = 0
        for (t, _), g in zip(toks, good):
            run = run + len(t) if g else 0
            best = max(best, run)
    return best

def stats(toks, key, lex, lm):
    segs = decode(toks, key)
    return {"run": longest_run(segs, lex), "lm": round(lm.score("".join(segs)), 4), "letters": sum(map(len, segs))}

def shuffled_keys(key, n, seed):
    ids = sorted(key); vals = [key[i] for i in ids]; out = []
    for d in range(n):
        r = random.Random(seed + d); v = vals[:]; r.shuffle(v); out.append(dict(zip(ids, v)))
    return out

def p95(xs):
    return jp.pct(xs, 0.95)

def vs_null(toks, key, lex, lm, seed):
    s = stats(toks, key, lex, lm)
    nulls = [stats(toks, k, lex, lm) for k in shuffled_keys(key, 20, seed)]
    s["run_p95"] = p95([x["run"] for x in nulls]); s["lm_p95"] = round(p95([x["lm"] for x in nulls]), 4)
    s["beats_null"] = s["run"] > s["run_p95"] and s["lm"] > s["lm_p95"]
    return s

def keyed(toks, key):
    return [t for t in toks if t in key]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--control-only", action="store_true")
    ap.add_argument("--target")
    ap.add_argument("--noise", type=float, default=0.0)
    ap.add_argument("--out", default=str(HERE / "results_king2.json"))
    a = ap.parse_args()
    key = load_key(); lex = sg.Lexicon.load("fr") if hasattr(sg, "Lexicon") else None
    if lex is None:
        cls = [v for v in vars(sg).values() if isinstance(v, type) and hasattr(v, "load")][0]
        lex = cls.load("fr")
    lm = jp.NgramModel([jp.read_corpus(p) for p in jp.LANG_CORPORA["fr"]])
    ctl_all = load_tokens("ciphertext_c268.tsv") + load_tokens("ciphertext_c269.tsv")
    c268_10 = load_tokens("ciphertext_c268.tsv", {f"L{i:02d}" for i in range(1, 11)})
    if a.target:
        tgt = load_tokens(a.target); N = len(keyed(tgt, key))
    else:
        tgt = None; N = len(keyed(c268_10, key))
    # windows of N keyed tokens over the f.138r-v sequence (unkeyed tokens kept in place as run breaks)
    wins, cur, n = [], [], 0
    for t in ctl_all:
        cur.append(t); n += t in key
        if n == N:
            wins.append(cur); cur, n = [], 0
    res = {"N_keyed": N, "windows": []}
    for w_i, w in enumerate(wins):
        res["windows"].append(vs_null(w, key, lex, lm, 1000 + 100 * w_i))
    w1 = res["windows"][0]
    res["control_pass"] = w1["beats_null"]
    res["range"] = {"run": [min(x["run"] for x in res["windows"]), max(x["run"] for x in res["windows"])],
                    "lm": [min(x["lm"] for x in res["windows"]), max(x["lm"] for x in res["windows"])]}
    if a.noise > 0:
        ids = sorted(key); nz = []
        for d in range(20):
            r = random.Random(500 + d)
            w = [(r.choice(ids) if (t in key and r.random() < a.noise) else t) for t in wins[0]]
            nz.append(vs_null(w, key, lex, lm, 1000))
        res["noise"] = {"rate": a.noise, "run_median": statistics.median(x["run"] for x in nz),
                        "lm_median": round(statistics.median(x["lm"] for x in nz), 4),
                        "beats_null_share": sum(x["beats_null"] for x in nz) / 20}
    if tgt is not None:
        t = vs_null(tgt, key, lex, lm, 133)
        t["in_range"] = t["run"] >= res["range"]["run"][0] and t["lm"] >= res["range"]["lm"][0]
        t["decode"] = " | ".join(decode(tgt, key))
        res["target"] = t
        res["gate"] = bool(res["control_pass"] and t["beats_null"] and t["in_range"])
    print(json.dumps({k: v for k, v in res.items() if k != "windows"}, indent=1, ensure_ascii=False))
    print("windows:", [(x["run"], x["lm"], x["run_p95"], x["lm_p95"], x["beats_null"]) for x in res["windows"]])
    if not a.control_only:
        Path(a.out).write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    main()
