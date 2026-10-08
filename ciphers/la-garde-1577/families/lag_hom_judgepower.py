#!/usr/bin/env python3
"""LAG-HOM (8 Oct 2026): judge power on the homophonic control decodes (prereg Amendment 2).

Re-creates the family_run.py homophonic controls for la-garde-1577 (profile=target, noise p, restarts 8) with the same
make_control/solve calls and seeds, writes each control decode to a temp file and scores it with the spec judge
(tools/judge_plaintext.py), printing seed, noise, recovery, judge verdict. Output -> families/lag_hom_judgepower.tsv.
--check re-runs and exits 1 if the committed TSV differs.
"""
import os, sys, json, subprocess, tempfile
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import family_run as fr  # noqa: E402
import families  # noqa: E402
import judge_plaintext as jp  # noqa: E402

SPEC = os.path.join(ROOT, "specs", "la-garde-1577.json")
CIPHER = os.path.join(ROOT, "ciphers", "la-garde-1577", "families", "basecode_cipher.txt")
OUT = os.path.join(os.path.dirname(__file__), "lag_hom_judgepower.tsv")
RUNS = [("0.055", s) for s in range(1, 10)] + [("0.084", s) for s in range(1, 4)]


def main():
    os.chdir(ROOT)  # run_judge resolves spec corpora relative to the repository root
    spec = json.load(open(SPEC, encoding="utf-8"))
    msgs, mode = fr.read_cipher_file(CIPHER, "space")
    toks = [t for m in msgs for t in m]
    fam = families.load("homophonic")
    corpora = [jp.read_corpus(p) for p in fr.corpus_paths(spec, None)]
    rows = ["noise\tseed\trecovery\tjudge_score\tverdict"]
    for noise, s in RUNS:
        params = {"profile": "target", "noise": noise, "N": len(toks), "K": len(set(toks)),
                  "lengths": [len(m) for m in msgs], "target_msgs": msgs, "messages_independent": "separate" in mode}
        cm, plain, train = fam.make_control(spec, s, corpora, dict(params))
        dec, sc, info = fam.solve(cm, spec, s, 8, train, dict(params))
        rec = fam.score_recovery(dec, plain)
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as f:
            f.write(dec if isinstance(dec, str) else "".join(dec)); path = f.name
        v = fr.run_judge(SPEC, path); os.unlink(path)
        score = v.split("score=")[1].split(",")[0] if "score=" in v else "-"
        verdict = v.split()[0] if v else "-"
        rows.append(f"{noise}\t{s}\t{rec:.3f}\t{score}\t{verdict}")
        print(rows[-1], flush=True)
    text = "\n".join(rows) + "\n"
    if "--check" in sys.argv:
        old = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        sys.exit(0 if old == text else 1)
    open(OUT, "w", encoding="utf-8").write(text)


if __name__ == "__main__":
    main()
