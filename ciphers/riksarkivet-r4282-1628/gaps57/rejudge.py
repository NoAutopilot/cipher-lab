#!/usr/bin/env python3
"""GAPS57 (3 Oct 2026, account-4): re-judge the committed GAPS42/GAPS50 homophonic decodes of R4282 and their
shuffled-target decodes under la17 (1590-1649 Latin letters, era-matched) and la18 (Zaluski 1709-11, the solver's corpus).

No new solve: the decodes are read from ../families/ as committed. Caveat for the reading: every decode was annealed
against la18 n-grams, so la18 is the corpus it was fitted to; a la17 score is not an independent re-solve.
Writes rejudge.tsv; --check recomputes and exits 1 if the committed TSV is stale.
"""
import argparse, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "tools"))
import judge_plaintext as jp  # noqa: E402

FAM = HERE.parent / "families"
DECODES = [("GAPS42 target", "homophonic-1-profile=target,noise=0.034-gaps42targetla18.txt"),
           ("GAPS42 shuffle 1", "homophonic-1-shuffle1-profile=target,noise=0.034-gaps42shuffledta.txt"),
           ("GAPS42 shuffle 2", "homophonic-1-shuffle2-profile=target,noise=0.034-gaps42shuffledta.txt"),
           ("GAPS50 target (nulls 0.1)", "homophonic-1-nulls=0.1,noise=0.034-gaps50targetnull.txt"),
           ("GAPS50 shuffle 1 (nulls 0.1)", "homophonic-1-shuffle1-nulls=0.1,noise=0.034-gaps50shuffledta.txt")]
CORPORA = ["la17", "la18"]


def rows():
    out = []
    for lang in CORPORA:
        spec = {"judge": {"language": lang}}
        for label, fn in DECODES:
            text = "\n".join(l for l in (FAM / fn).read_text().splitlines() if not l.startswith("#"))
            r = jp.judge(spec, text)["checks"]["language"]
            out.append([lang, label, str(len(jp.fold(text))), "PASS" if r["pass"] else "FAIL", f"{r['score']:.3f}",
                        f"{r['real_p05']:.3f}", f"{r['null_p99']:.3f}", f"{r['score'] - r['real_p05']:+.3f}"])
    return out


def render(rs):
    return "\n".join(["\t".join(["corpus", "decode", "letters", "verdict", "score", "real_p05", "null_p99", "score_minus_p05"])]
                     + ["\t".join(r) for r in rs]) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    txt = render(rows())
    tsv = HERE / "rejudge.tsv"
    if a.check:
        ok = tsv.exists() and tsv.read_text() == txt
        print("rejudge.tsv up to date" if ok else "rejudge.tsv STALE")
        sys.exit(0 if ok else 1)
    tsv.write_text(txt)
    print(txt, end="")


if __name__ == "__main__":
    main()
