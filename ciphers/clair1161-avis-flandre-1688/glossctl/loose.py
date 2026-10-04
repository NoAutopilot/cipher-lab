#!/usr/bin/env python3
"""NEAR3-C1LOOSE: looser gloss-seeded key repair with a 10-shuffle gloss control (pre-registered in tx/PREREG_loose.md).

  python3 loose.py --gloss real|shufS [--restarts 32] [--dry]

Same alignment as repair.py (cost key = the unrepaired READ2-C1161 key, rebuilt from key.tsv's "was 'x'" sources);
rule: >= 3 aligned occurrences and the majority gloss letter holds >= 60% of them; same re-anneal and c185R judge.
--dry prints the fixed signs and exits without annealing.
"""
import argparse, csv, json, os, random, re, subprocess, sys, time
from collections import defaultdict, Counter
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, os.path.join(ROOT, "tools")); sys.path.insert(0, HERE)
from glossctl import block_tokens, gloss_letters, stat, decode
from repair import align

def unrepaired_key():
    k = {}
    for r in csv.DictReader(open(os.path.join(T, "key.tsv")), delimiter="\t"):
        m = re.search(r"READ2-C1161B re-anneal.*was '([^']*)'", r["source"])
        k[r["sign"]] = m.group(1) if m else r["value"]
    return k

def fixed_signs(toks, key, g):
    occ = defaultdict(list)
    for i, j in align(toks, key, g): occ[toks[i]].append(g[j])
    out = {}
    for s, L in occ.items():
        if len(L) >= 3:
            v, n = Counter(L).most_common(1)[0]
            if n / len(L) >= 0.60: out[s] = (v, n, len(L))
    return out

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--gloss", default="real"); ap.add_argument("--restarts", type=int, default=32)
    ap.add_argument("--dry", action="store_true"); a = ap.parse_args()
    import judge_plaintext as jp, family_run as fr, homophonic_anneal as ha
    spec_path = os.path.join(ROOT, "specs", "clair1161-avis-flandre-1688.json"); spec = json.load(open(spec_path))
    msgs, _ = fr.read_spec_cipher(spec, "space"); seq = [t for m in msgs for t in m]
    toks, g0, key = block_tokens(), gloss_letters(), unrepaired_key()
    assert seq[-len(toks):] == toks, "block is not the tail of the spec stream"
    base = stat(decode(key, toks), g0)
    assert abs(base - 0.594) < 0.0006, f"unrepaired key check failed: {base:.4f}"
    g = g0
    if a.gloss != "real":
        gl = list(g); random.Random(int(a.gloss[4:])).shuffle(gl); g = "".join(gl)
    fx = fixed_signs(toks, key, g)
    fixed = {s: v for s, (v, n, m) in fx.items()}
    detail = ",".join(f"{s}={v}({n}/{m}{'' if key.get(s) == v else ';was ' + key.get(s, '?')})" for s, (v, n, m) in sorted(fx.items()))
    if a.dry:
        print(a.gloss, len(fixed), detail); return
    t0 = time.time()
    model = ha.Model([jp.read_corpus(p) for p in fr.corpus_paths(spec, None)], 3)
    sc, k2 = ha.solve(seq, model, a.restarts, 40000, 1, 1.0, fixed=fixed)[0]
    dec = "".join(k2[x] for x in seq)
    c185 = dec[:len(seq) - len(toks)]
    out = os.path.join(HERE, f"loose_{a.gloss}_c185R.txt"); open(out, "w").write(c185 + "\n")
    with open(os.path.join(HERE, f"loose_{a.gloss}_key.tsv"), "w") as f:
        f.write("sign\tvalue\tfixed\tunrepaired\n" + "".join(
            f"{s}\t{v}\t{'C' if s in fixed else 'S'}\t{key.get(s, '')}\n" for s, v in sorted(k2.items())))
    j = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "judge_plaintext.py"), spec_path, "--file", out, "--json"],
                       capture_output=True, text=True, cwd=ROOT).stdout
    try:
        c = json.loads(j)["checks"]; L, W = c["language"], c["words"]
        lang, js = L["score"], (f"{'PASS' if L['pass'] else 'FAIL'} language {L['score']} (null_p99 {L['null_p99']}, "
                                f"real_p05 {L['real_p05']}, N {L['N']}); words cover {W['cover']}")
    except Exception:
        lang, js = "", j.strip().replace("\n", " | ")[:600]
    moved = ",".join(f"{s}:{key.get(s)}->{v}" for s, v in sorted(k2.items()) if key.get(s) != v)
    row = [time.strftime("%Y-%m-%d %H:%M", time.gmtime()), a.gloss, len(fixed),
           sum(1 for s, v in fixed.items() if key.get(s) != v), f"{sc:.1f}",
           f"{stat(dec[-len(toks):], g0):.4f}", lang, f"{time.time()-t0:.0f}s", js, detail, moved]
    p = os.path.join(HERE, "loose.tsv"); new = not os.path.exists(p)
    with open(p, "a") as f:
        if new: f.write("utc\tgloss\tfixed_signs\tfixed_differs_from_unrepaired\tanneal_score\tblock_vs_real_gloss\t"
                        "c185R_lang\ttime\tjudge_c185R\tfixed_detail\tmoved_vs_unrepaired\n")
        f.write("\t".join(str(x) for x in row) + "\n")
    print("\t".join(str(x) for x in row[:9]))

if __name__ == "__main__":
    main()
