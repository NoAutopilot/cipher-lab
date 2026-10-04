#!/usr/bin/env python3
"""NEAR3-C1SPLIT (4 Oct 2026): look-alike split test with a placebo-split control (pre-registered in split/PREREG_split.md).

  python3 split/split.py merged            # baseline: the 924-sign stream as in ciphertext.tsv
  python3 split/split.py qls               # the 9 q that pass B read as ls -> new symbol qL (split/assign.tsv)
  python3 split/split.py S                 # the 7 open 5-like S in the c186R block -> new symbol S5 (split/assign.tsv)
  python3 split/split.py placebo-qls --seed K   # K=1..5: sign PLACEBO_QLS[K-1], 9 random c185R occurrences -> new symbol
  python3 split/split.py placebo-S --seed K     # K=1..5: sign PLACEBO_S[K-1], 7 random c186R-block occurrences -> new symbol

Recipe (every run): homophonic_anneal.solve(stream, fr16 order-3 model from the spec's judge corpora, restarts 32,
iters 40000, seed 1, uni_weight 1.0), blind (no fixed signs). Statistics: gloss match of the c186R block decode
(glossctl.stat, as glossctl/glossctl.py) and tools/judge_plaintext.py language score on the c185R decode (704 signs).
Rows append to split/results.tsv. ciphertext.tsv and key.tsv are never edited.
"""
import argparse, csv, json, os, random, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, os.path.join(ROOT, "tools")); sys.path.insert(0, os.path.join(T, "glossctl"))
from glossctl import gloss_letters, stat

PLACEBO_QLS = ["w", "o", "e", "9", "p"]     # c185R counts 19, 19, 16, 16, 25 (q: 18 in c185R, 9 moved)
PLACEBO_S = ["+", "7", "4", "th", "qb"]     # block counts 18, 14, 12, 12, 14 (S: 14 in the block, 7 moved)

def stream():
    rows = [r for r in csv.DictReader(open(os.path.join(T, "ciphertext.tsv")), delimiter="\t")
            if r["sign"] != "/" and not r["sign"].startswith("[")]
    return rows

def variant(mode, seed):
    rows = stream()
    toks = [r["sign"] for r in rows]
    if mode == "merged":
        return toks, "-"
    if mode in ("qls", "S"):
        ass = [a for a in csv.DictReader(open(os.path.join(HERE, "assign.tsv")), delimiter="\t") if a["pair"] == mode]
        if mode == "qls":
            want = {(a["line"], a["pos_in_line_tokens"]): a["split_symbol"] for a in ass}
            n = 0
            for i, r in enumerate(rows):
                if (r["line"], r["pos"]) in want:
                    assert r["sign"] == "q"; toks[i] = want[(r["line"], r["pos"])]; n += 1
        else:  # S: occurrences in line order within each block line
            order = {"1st": 0, "2nd": 1, "3rd": 2, "-": 0}
            want = {(a["line"], order[a["pos_in_line_tokens"]]): a["split_symbol"] for a in ass}
            seen, n = {}, 0
            for i, r in enumerate(rows):
                if r["line"].startswith("c186R") and r["sign"] == "S":
                    k = seen.get(r["line"], 0); seen[r["line"]] = k + 1
                    toks[i] = want[(r["line"], k)]; n += toks[i] != "S"
        return toks, f"{n} moved"
    sign = (PLACEBO_QLS if mode == "placebo-qls" else PLACEBO_S)[seed - 1]
    leaf, k = ("c185R", 9) if mode == "placebo-qls" else ("c186R", 7)
    idx = [i for i, r in enumerate(rows) if r["line"].startswith(leaf) and r["sign"] == sign]
    pick = random.Random(seed).sample(idx, k)
    for i in pick:
        toks[i] = sign + "_P"
    return toks, f"sign {sign}: {k} of {len(idx)} {leaf} occurrences -> {sign}_P"

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("mode", choices=["merged", "qls", "S", "placebo-qls", "placebo-S"])
    ap.add_argument("--seed", type=int, default=1); a = ap.parse_args()
    import judge_plaintext as jp, family_run as fr, homophonic_anneal as ha
    spec_path = os.path.join(ROOT, "specs", "clair1161-avis-flandre-1688.json"); spec = json.load(open(spec_path))
    msgs, _ = fr.read_spec_cipher(spec, "space"); spec_seq = [t for m in msgs for t in m]
    rows = stream()
    assert [r["sign"] for r in rows] == spec_seq, "ciphertext.tsv stream differs from the spec stream"
    seq, note = variant(a.mode, a.seed)
    nblk = sum(1 for r in rows if r["line"].startswith("c186R"))
    t0 = time.time()
    model = ha.Model([jp.read_corpus(p) for p in fr.corpus_paths(spec, None)], 3)
    sc, key = ha.solve(seq, model, 32, 40000, 1, 1.0)[0]
    dec = "".join(key[x] for x in seq)
    tag = a.mode if a.mode in ("merged", "qls", "S") else f"{a.mode}{a.seed}"
    out = os.path.join(HERE, f"{tag}_c185R.txt"); open(out, "w").write(dec[:-nblk] + "\n")
    with open(os.path.join(HERE, f"{tag}_key.tsv"), "w") as f:
        f.write("sign\tvalue\n" + "".join(f"{s}\t{v}\n" for s, v in sorted(key.items())))
    j = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "judge_plaintext.py"), spec_path, "--file", out, "--json"],
                       capture_output=True, text=True, cwd=ROOT).stdout
    L = json.loads(j)["checks"]["language"]
    row = [time.strftime("%Y-%m-%d %H:%M", time.gmtime()), tag, a.seed, len(set(seq)), f"{sc:.1f}",
           f"{stat(dec[-nblk:], gloss_letters()):.4f}", L["score"], f"{time.time()-t0:.0f}s", note]
    p = os.path.join(HERE, "results.tsv"); new = not os.path.exists(p)
    with open(p, "a") as f:
        if new: f.write("utc\trun\tseed\tK\tanneal_score\tgloss_match\tc185R_judge\ttime\tnote\n")
        f.write("\t".join(str(x) for x in row) + "\n")
    print("\t".join(str(x) for x in row))
    print("split symbols:", {s: key[s] for s in key if s in ("qL", "S5", "q", "S", "ls") or s.endswith("_P")})

if __name__ == "__main__":
    main()
