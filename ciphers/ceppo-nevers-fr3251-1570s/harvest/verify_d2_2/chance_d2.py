#!/usr/bin/env python3
"""VERIFY-CEPPO-D2-2 chance control for f.21v and f.87 (29 Sept 2026).

Model: harvest/v2/chance_control.py (the f.11r second audit). Transcription: the verifier's value-blind D
(harvest/verify_d2/<folio>/passD.tsv). Key: Tomokiyo's printed values (sign_id_map.json) plus X_THETA2 = r, as the
first audit read; X_POUND and X_NEW unkeyed.
Arms: R real key, real order (1); K 1,000 keys with the value column permuted (homophone counts kept), real order;
T real key on the sign order permuted within each line (1,000).
Metric (script, no model): Italian lexicon = it16dip word types, count >= 3, length >= 4 (j->i, v->u); per decode the
longest lexicon word inside any line, the number of distinct lexicon words of 6+ letters, the number of distinct
5+ words, and 'pairs' = lines carrying two or more distinct lexicon words of 5+ letters that do not overlap.
Also writes a 40-text blind-reader sample (real + 8 best K + 8 best T + random) with its answer key.

Usage: python3 chance_d2.py f21v|f87 [--n 1000] [--seed 2129] [--sample 40]
"""
import argparse, csv, json, random, re, sys
from collections import Counter
from pathlib import Path
HERE = Path(__file__).resolve().parent
H = HERE.parent
sys.path.insert(0, str(H.parents[2] / "tools"))
import judge_plaintext as jp  # noqa

def lexicon():
    c = Counter()
    for p in jp.LANG_CORPORA["it16dip"]:
        t = jp.read_corpus(p).lower().replace("j", "i").replace("v", "u")
        c.update(re.findall(r"[a-z]+", t))
    return {w for w, n in c.items() if n >= 3 and len(w) >= 4}

def decode(seq, m):
    return "".join("_" if m.get(s) is None else ("" if m[s] == "null" else ("&" if m[s] == "et" else m[s])) for s in seq)

def hits(run, lex):
    out = []
    for i in range(len(run)):
        for j in range(i + 4, min(len(run), i + 14) + 1):
            if run[i:j] in lex:
                out.append((i, j, run[i:j]))
    return out

def stats(texts, lex):
    found = set(); pairs = 0
    for t in texts:
        line5 = []
        for run in re.split(r"[_&]", t):
            h = hits(run, lex); found.update(w for _, _, w in h)
            line5 += [(i, j, w) for i, j, w in h if len(w) >= 5]
        # two non-overlapping distinct 5+ words in one line (positions are per run; runs rarely share)
        ws = sorted(set(line5), key=lambda x: -(x[1] - x[0]))
        if len({w for _, _, w in ws}) >= 2:
            pairs += 1
    L = max((len(w) for w in found), default=0)
    return L, sum(1 for w in found if len(w) >= 6), sum(1 for w in found if len(w) >= 5), pairs, \
        sorted(found, key=len, reverse=True)[:6]

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folio"); ap.add_argument("--n", type=int, default=1000)
    ap.add_argument("--seed", type=int, default=2129); ap.add_argument("--sample", type=int, default=40)
    a = ap.parse_args(); rng = random.Random(a.seed)
    m = {e["id"]: e["value"] for e in json.load(open(H / "sign_id_map.json"))}
    m["X_THETA2"] = "r"
    P = {}
    for r in csv.DictReader(open(H / "verify_d2" / a.folio / "passD.tsv"), delimiter="\t"):
        P.setdefault(r["passage"], []).append(r["sign_id"].strip())
    lex = lexicon()
    real = [decode(s, m) for s in P.values()]
    R = stats(real, lex)
    rows = [("R", 0) + R + (" | ".join(real),)]
    ids = list(m); vals = [m[i] for i in ids]
    for k in range(a.n):
        rng.shuffle(vals); mk = dict(zip(ids, vals))
        t = [decode(s, mk) for s in P.values()]
        rows.append(("K", k + 1) + stats(t, lex) + (" | ".join(t),))
    for k in range(a.n):
        t = []
        for s in P.values():
            s2 = s[:]; rng.shuffle(s2); t.append(decode(s2, m))
        rows.append(("T", k + 1) + stats(t, lex) + (" | ".join(t),))
    out = HERE / a.folio; out.mkdir(exist_ok=True)
    with open(out / "chance_summary.tsv", "w") as f:
        f.write("arm\ti\tlongest\tn_ge6\tn_ge5\tpair_lines\ttop_words\tdecode\n")
        for r in rows: f.write("\t".join(map(str, r[:6])) + "\t" + " ".join(r[6]) + "\t" + r[7] + "\n")
    print(f"{a.folio}: lexicon {len(lex)}; REAL longest {R[0]} n>=6 {R[1]} n>=5 {R[2]} pair_lines {R[3]} top {R[4]}")
    for arm in "KT":
        rs = [r for r in rows if r[0] == arm]
        print(f" arm {arm} n={len(rs)}: longest>=real {sum(r[2] >= R[0] for r in rs)}; n_ge6>=real "
              f"{sum(r[3] >= R[1] for r in rs)}; n_ge5>=real {sum(r[4] >= R[2] for r in rs)}; pair_lines>=real "
              f"{sum(r[5] >= R[3] for r in rs)}; max n_ge6 {max(r[3] for r in rs)} max n_ge5 {max(r[4] for r in rs)} "
              f"max pairs {max(r[5] for r in rs)}; longest dist {sorted(Counter(r[2] for r in rs).items())}")
        for b in sorted(rs, key=lambda r: (-r[3], -r[2], -r[4]))[:4]:
            print("   best", b[1], b[2], b[3], b[4], b[5], b[6])
    Ks = [r for r in rows if r[0] == "K"]; Ts = [r for r in rows if r[0] == "T"]
    key = lambda r: (-r[3], -r[4], -r[2])
    top = sorted(Ks, key=key)[:8] + sorted(Ts, key=key)[:8]
    rest = [r for r in Ks + Ts if r not in top]; rng.shuffle(rest)
    samp = top + rest[:a.sample - 1 - len(top)] + [rows[0]]; rng.shuffle(samp)
    ans = {}
    with open(out / "reader_decodes.txt", "w") as f:
        for i, r in enumerate(samp, 1):
            f.write(f"TEXT {i:02d}\n" + "\n".join(r[7].split(" | ")) + "\n\n"); ans[f"{i:02d}"] = f"{r[0]}{r[1]}"
    json.dump(ans, open(out / "reader_answer.json", "w"))
    print(" reader sample", len(samp), "real at TEXT", [k for k, v in ans.items() if v == "R0"])

if __name__ == "__main__":
    main()
