#!/usr/bin/env python3
"""READ2-C1161B step 2: gloss-seeded key repair with a shuffled-gloss control (pre-registered in tx/PREREG_glossctl.md).

  python3 repair.py --gloss real|shufS [--restarts 32]

1. Global alignment (edit-distance DP; cost 0 when key.tsv's letter for the sign equals the gloss letter, 1 for a
   mismatch or a gap) of the 220-sign c186R block to the 170 gloss letters (or the gloss letters shuffled, seed S).
2. Fixed signs (grade C for the real gloss): every aligned occurrence carries the same gloss letter and there are
   >= 2 aligned occurrences, or 1 when the sign occurs only in the block.
3. Re-anneal the full 924-sign stream (homophonic_anneal.solve, fr16 order-3 model from the spec's judge corpora,
   seed 1, uni_weight 1.0, iters 40000) with those signs held fixed.
4. Decode c185R (first 704 signs), score with tools/judge_plaintext.py on the spec; append to glossctl/repair.tsv.
"""
import argparse, csv, json, os, random, subprocess, sys, time
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, os.path.join(ROOT, "tools")); sys.path.insert(0, HERE)
from glossctl import block_tokens, gloss_letters, real_key, stat, decode

def align(toks, key, g):
    n, m = len(toks), len(g)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): D[i][0] = i
    for j in range(m + 1): D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i-1][j-1] + (key.get(toks[i-1]) != g[j-1]), D[i-1][j] + 1, D[i][j-1] + 1)
    i, j, pairs = n, m, []
    while i and j:
        if D[i][j] == D[i-1][j-1] + (key.get(toks[i-1]) != g[j-1]):
            pairs.append((i-1, j-1)); i -= 1; j -= 1
        elif D[i][j] == D[i-1][j] + 1: i -= 1
        else: j -= 1
    return pairs[::-1]

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--gloss", default="real"); ap.add_argument("--restarts", type=int, default=32)
    a = ap.parse_args()
    import judge_plaintext as jp, family_run as fr, homophonic_anneal as ha
    spec_path = os.path.join(ROOT, "specs", "clair1161-avis-flandre-1688.json"); spec = json.load(open(spec_path))
    msgs, _ = fr.read_spec_cipher(spec, "space"); seq = [t for m in msgs for t in m]
    toks, g, key = block_tokens(), gloss_letters(), real_key()
    assert seq[-len(toks):] == toks, "block is not the tail of the spec stream"
    if a.gloss != "real":
        gl = list(g); random.Random(int(a.gloss[4:])).shuffle(gl); g = "".join(gl)
    pairs = align(toks, key, g)
    occ = defaultdict(list)
    for i, j in pairs: occ[toks[i]].append(g[j])
    outside = set(seq[:-len(toks)])
    fixed = {s: L[0] for s, L in occ.items() if len(set(L)) == 1 and (len(L) >= 2 or s not in outside)}
    changed = sum(1 for s, v in fixed.items() if key.get(s) != v)
    t0 = time.time()
    model = ha.Model([jp.read_corpus(p) for p in fr.corpus_paths(spec, None)], 3)
    sc, k2 = ha.solve(seq, model, a.restarts, 40000, 1, 1.0, fixed=fixed)[0]
    dec = "".join(k2[x] for x in seq)
    c185 = dec[:len(seq) - len(toks)]
    out = os.path.join(HERE, f"repair_{a.gloss}_c185R.txt"); open(out, "w").write(c185 + "\n")
    with open(os.path.join(HERE, f"repair_{a.gloss}_key.tsv"), "w") as f:
        f.write("sign\tvalue\tfixed\n" + "".join(f"{s}\t{v}\t{'C' if s in fixed else 'S'}\n" for s, v in sorted(k2.items())))
    j = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "judge_plaintext.py"), spec_path, "--file", out, "--json"],
                       capture_output=True, text=True, cwd=ROOT).stdout
    try:
        c = json.loads(j)["checks"]; L, W = c["language"], c["words"]
        js = (f"{'PASS' if L['pass'] else 'FAIL'} language {L['score']} (null_p99 {L['null_p99']}, real_p05 {L['real_p05']}, "
              f"N {L['N']}); words cover {W['cover']}")
    except Exception:
        js = j.strip().replace("\n", " | ")[:600]
    row = [time.strftime("%Y-%m-%d %H:%M", time.gmtime()), a.gloss, len(fixed), changed, f"{sc:.1f}",
           f"{stat(dec[-len(toks):], gloss_letters()):.4f}", f"{time.time()-t0:.0f}s", js]
    p = os.path.join(HERE, "repair.tsv"); new = not os.path.exists(p)
    with open(p, "a") as f:
        if new: f.write("utc\tgloss\tfixed_signs\tfixed_differs_from_keytsv\tanneal_score\tblock_vs_real_gloss\ttime\tjudge_c185R\n")
        f.write("\t".join(str(x) for x in row) + "\n")
    print("\t".join(str(x) for x in row))

if __name__ == "__main__":
    main()
