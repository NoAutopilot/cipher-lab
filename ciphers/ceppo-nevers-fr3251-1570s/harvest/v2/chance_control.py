#!/usr/bin/env python3
"""VERIFY-CEPPO-2 chance control for f.11r (28 Sept 2026).

How often does a decode of the blind transcription (harvest/passD_blind_verify.tsv) show Italian words as long as
the ones claimed (presidente 10, mandato 7, curare 6, estitucio 9, chuni 5, ochi 4, sauoia 6) by chance?

Arms (each N decodes, printed key values only, no exceptions applied):
  K  shuffled keys: the value column of the 55-cell sheet permuted (same homophone counts), true sign order.
  T  true key on a shuffled transcription: the sign order permuted within each passage (letter frequencies kept).
  R  the real key on the real sequence (1 decode).
Metric (script, no model): the Italian lexicon is every word type of it16dip (tools/data) with corpus count >= 3,
folded, j->i, v->u; for each decode, the longest lexicon word found as a substring of any passage, and the number of
distinct lexicon words of length >= 6. Exits 0; writes chance_summary.tsv and a sample file for a blind reader.

Usage: python3 chance_control.py [--n 1000] [--seed 2028] [--sample 40]
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
        t = jp.fold(jp.read_corpus(p)) if False else jp.read_corpus(p).lower()
        t = t.replace("j", "i").replace("v", "u")
        c.update(re.findall(r"[a-z]+", t))
    return {w for w, n in c.items() if n >= 3 and len(w) >= 4}

def decode(seq, m):
    return "".join("_" if m.get(s) is None else ("" if m[s] == "null" else m[s]) for s in seq)

def words(texts, lex):
    found = set()
    for t in texts:
        for run in t.split("_"):
            for i in range(len(run)):
                for j in range(i + 4, min(len(run), i + 14) + 1):
                    if run[i:j] in lex:
                        found.add(run[i:j])
    return found

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--n", type=int, default=1000); ap.add_argument("--seed", type=int, default=2028)
    ap.add_argument("--sample", type=int, default=40)
    a = ap.parse_args(); rng = random.Random(a.seed)
    m = {e["id"]: e["value"] for e in json.load(open(H / "sign_id_map.json"))}
    P = {}
    for r in csv.DictReader(open(H / "passD_blind_verify.tsv"), delimiter="\t"):
        P.setdefault(r["passage"], []).append(r["sign_id"].strip())
    lex = lexicon()
    def stats(texts):
        f = words(texts, lex)
        L = max((len(w) for w in f), default=0)
        return L, sum(1 for w in f if len(w) >= 6), sorted(f, key=len, reverse=True)[:5]
    real = [decode(s, m) for s in P.values()]
    rL, r6, rtop = stats(real)
    rows = [("R", 0, rL, r6, " ".join(rtop), " | ".join(real))]
    ids = list(m); vals = [m[i] for i in ids]
    for k in range(a.n):
        rng.shuffle(vals); mk = dict(zip(ids, vals))
        t = [decode(s, mk) for s in P.values()]; L, n6, top = stats(t)
        rows.append(("K", k + 1, L, n6, " ".join(top), " | ".join(t)))
    for k in range(a.n):
        t = []
        for s in P.values():
            s2 = s[:]; rng.shuffle(s2); t.append(decode(s2, m))
        L, n6, top = stats(t)
        rows.append(("T", k + 1, L, n6, " ".join(top), " | ".join(t)))
    with open(HERE / "chance_summary.tsv", "w") as f:
        f.write("arm\ti\tlongest\tn_ge6\ttop_words\tdecode\n")
        for r in rows: f.write("\t".join(map(str, r)) + "\n")
    print(f"lexicon {len(lex)} types; REAL longest {rL} n>=6 {r6} top {rtop}")
    for arm in "KT":
        rs = [r for r in rows if r[0] == arm]
        ge = sum(1 for r in rs if r[2] >= rL); ge6 = sum(1 for r in rs if r[3] >= r6)
        dist = Counter(r[2] for r in rs)
        print(f"arm {arm}: n={len(rs)} longest>=real({rL}): {ge}; n_ge6>=real({r6}): {ge6}; longest dist {sorted(dist.items())}")
        best = sorted(rs, key=lambda r: (-r[2], -r[3]))[:5]
        for b in best: print("   best", b[1], b[2], b[3], b[4])
    # blind-reader sample: real + the top-scoring K and T decodes (adversarial) + random ones, shuffled
    Ks = [r for r in rows if r[0] == "K"]; Ts = [r for r in rows if r[0] == "T"]
    top = sorted(Ks, key=lambda r: (-r[2], -r[3]))[:8] + sorted(Ts, key=lambda r: (-r[2], -r[3]))[:8]
    rest = [r for r in Ks + Ts if r not in top]; rng.shuffle(rest)
    samp = top + rest[:a.sample - 1 - len(top)] + [rows[0]]; rng.shuffle(samp)
    ans = {}
    with open(HERE / "chance_reader_decodes.txt", "w") as f:
        for i, r in enumerate(samp, 1):
            f.write(f"TEXT {i:02d}\n" + "\n".join(r[5].split(" | ")) + "\n\n"); ans[i] = f"{r[0]}{r[1]}"
    json.dump(ans, open(HERE / "chance_reader_answer.json", "w"))
    print("reader sample", len(samp), "real at TEXT", [k for k, v in ans.items() if v == "R0"])

if __name__ == "__main__":
    main()
