#!/usr/bin/env python3
"""Error-rate sweep for the nl18 judge at the 2077 (N=605) and 2061 (N=249) legend lengths (NL18-CORPUS, 3 Oct 2026).
Leave-one-file-out: held-out real prose corrupted at 0-35% (random letter substituted) -- PASS rate and median score
per rate, to place the readings' own scores (judge_nl18.out.tsv) against real prose at a bracketing error level
(CLAUDE.md rule 3, SALV-DIAG lesson). Writes judge/judge_nl18_sweep.out.tsv."""
import random, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools"))
from judge_plaintext import LANG_CORPORA, NgramModel, fold, pct, read_corpus  # noqa: E402
RATES = [0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35]; NS = {"2077_legend": 605, "2061_battery": 249}; S = 100


def main():
    files = LANG_CORPORA["nl18"]; texts = [read_corpus(p) for p in files]
    res = {}
    for k in range(len(files)):
        m = NgramModel([t for i, t in enumerate(texts) if i != k]); ht = fold(texts[k])
        for lg, N in NS.items():
            real, null, _ = m.controls(N, samples=200, seed=1); r05, n99 = pct(real, .05), pct(null, .99)
            rnd = random.Random(3)
            for r in RATES:
                for _ in range(S):
                    j = rnd.randrange(0, len(ht) - N)
                    w = "".join(rnd.choice("abcdefghijklmnopqrstuvwxyz") if rnd.random() < r else c for c in ht[j:j + N])
                    sc = m.score(w); res.setdefault((lg, r), []).append((sc > r05 and sc > n99, sc, k))
    with open(HERE / "judge" / "judge_nl18_sweep.out.tsv", "w") as fh:
        fh.write("legend\tN\terror_rate\tpass_rate_blended\tpass_rate_per_fold_min-max\tmedian_score\tp05_score\tp95_score\n")
        for (lg, r), v in sorted(res.items()):
            pf = [sum(x[0] for x in v if x[2] == k) / S for k in range(len(files))]
            sc = sorted(x[1] for x in v)
            line = f"{lg}\t{NS[lg]}\t{r:.2f}\t{sum(pf)/len(pf):.3f}\t{min(pf):.2f}-{max(pf):.2f}\t{pct(sc,.5):.3f}\t{pct(sc,.05):.3f}\t{pct(sc,.95):.3f}"
            fh.write(line + "\n"); print(line, flush=True)


if __name__ == "__main__":
    main()
