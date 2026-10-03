#!/usr/bin/env python3
"""Judge the na-suriname-map-1781 legend readings against tools/data/nl18 (NL18-CORPUS, 3 Oct 2026).

Per legend: extract the DECODED cipher letters only (drop {plain} entries written in clear on the sheet, drop
[codeword] groups, drop '·' unread), resolve the two-valued [x|y] signs three ways (first value / second value /
dropped), and report
  - the judge (tools/data/nl18 model, real_p05 and null_p99 at the legend's own N);
  - shuffled-reading controls: 200 letter shuffles of the same reading (= the decode of a shuffled ciphertext under
    this per-token key, so this is also the shuffled-target check) and how many PASS;
  - leave-one-file-out false-negative rate at the legend's N, per fold and blended, on clean held-out real prose AND
    on held-out prose corrupted at the legend's own M+U token rate (random letter substituted), i.e. whether the
    judge has power at this N and this error level.
Writes judge/<legend>_<mode>.txt (input for tools/judge_plaintext.py --file) and judge/judge_nl18.out.tsv.
Usage: python3 ciphers/na-suriname-map-1781/judge_nl18.py
"""
import random, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools"))
from judge_plaintext import LANG_CORPORA, NgramModel, fold, pct, read_corpus  # noqa: E402

LEGENDS = ["2039_legend", "2039_remarque", "2046_legend", "2061_battery", "2077_legend"]
SAMPLES = 200


def extract(path, mode):
    out = []
    for ln in Path(path).read_text(encoding="utf-8").splitlines():
        if ln.startswith("#") or "|" not in ln:
            continue
        s = ln.split("|", 1)[1]
        s = re.sub(r"\{[^}]*\}", " ", s)
        s = re.sub(r"\[([a-z])\|([a-z])\]", {"first": r"\1", "second": r"\2", "drop": ""}[mode], s)
        s = re.sub(r"\[[^\]]*\]", " ", s)
        out.append(fold(s))
    return "\n".join(x for x in out if x)


def err_rate(path):
    m = re.search(r"tokens (\d+): H (\d+), C (\d+), S (\d+), M (\d+), I (\d+), U (\d+)", Path(path).read_text())
    t, mm, u = int(m.group(1)), int(m.group(5)), int(m.group(7))
    return (mm + u) / t


def corrupt(w, rate, rnd):
    return "".join(rnd.choice("abcdefghijklmnopqrstuvwxyz") if rnd.random() < rate else ch for ch in w)


def main():
    files = LANG_CORPORA["nl18"]
    texts = [read_corpus(p) for p in files]
    full = NgramModel(texts)
    (HERE / "judge").mkdir(exist_ok=True)
    rows, legends = [], {}
    for lg in LEGENDS:
        src = HERE / f"reading_{lg}_nieuw.txt"
        er = err_rate(src)
        for mode in ("first", "second", "drop"):
            t = extract(src, mode)
            (HERE / "judge" / f"{lg}_{mode}.txt").write_text(f"# {lg} cipher letters only, [x|y] -> {mode}; from {src.name}\n{t}\n")
            letters = fold(t); N = len(letters)
            real, null, _ = full.controls(N, samples=SAMPLES, seed=1)
            r05, n99 = pct(real, 0.05), pct(null, 0.99)
            sc = full.score(letters)
            rnd = random.Random(5); sh = []
            for _ in range(SAMPLES):
                l = list(letters); rnd.shuffle(l); sh.append(full.score("".join(l)))
            sh_pass = sum(1 for x in sh if x > r05 and x > n99)
            legends.setdefault(lg, (N, er))
            rows.append(dict(legend=lg, mode=mode, N=N, err=round(er, 3), score=round(sc, 3), real_p05=round(r05, 3),
                             real_median=round(pct(real, .5), 3), null_p99=round(n99, 3),
                             verdict="PASS" if sc > r05 and sc > n99 else "FAIL",
                             shuf_max=round(max(sh), 3), shuf_pass=f"{sh_pass}/{SAMPLES}"))
            print("\t".join(f"{k}={v}" for k, v in rows[-1].items()), flush=True)
    # leave-one-file-out, at each legend's N (first-mode N) and error rate
    fold_rows = []
    for k, held in enumerate(files):
        model = NgramModel([t for i, t in enumerate(texts) if i != k])
        ht = fold(texts[k])
        for lg, (N0, er) in legends.items():
            N = len(fold(extract(HERE / f"reading_{lg}_nieuw.txt", "first")))
            real, null, _ = model.controls(N, samples=SAMPLES, seed=1)
            r05, n99 = pct(real, 0.05), pct(null, 0.99)
            rnd = random.Random(2); fn = fnc = 0
            for _ in range(SAMPLES):
                j = rnd.randrange(0, len(ht) - N); w = ht[j:j + N]
                s1 = model.score(w); s2 = model.score(corrupt(w, er, rnd))
                fn += not (s1 > r05 and s1 > n99); fnc += not (s2 > r05 and s2 > n99)
            fold_rows.append((held.name, lg, N, er, fn, fnc))
            print(f"LOFO held_out={held.name} legend={lg} N={N} clean_FN={fn}/{SAMPLES} corrupt{er:.2f}_FN={fnc}/{SAMPLES}", flush=True)
    with open(HERE / "judge" / "judge_nl18.out.tsv", "w") as fh:
        fh.write("\t".join(rows[0].keys()) + "\n")
        for r in rows:
            fh.write("\t".join(str(v) for v in r.values()) + "\n")
        fh.write("\nheld_out\tlegend\tN\terr\tclean_FN\tcorrupt_FN\tof\n")
        for r in fold_rows:
            fh.write("\t".join(str(x) for x in r) + f"\t{SAMPLES}\n")
        fh.write("\nlegend\tN\tclean_FN_blended\tclean_FN_per_fold\tcorrupt_FN_blended\tcorrupt_FN_per_fold\n")
        for lg in legends:
            fr = [r for r in fold_rows if r[1] == lg]
            pf = [r[4] / SAMPLES for r in fr]; pc = [r[5] / SAMPLES for r in fr]
            line = (f"{lg}\t{fr[0][2]}\t{sum(pf)/len(pf):.3f}\t{min(pf):.3f}-{max(pf):.3f}\t"
                    f"{sum(pc)/len(pc):.3f}\t{min(pc):.3f}-{max(pc):.3f}")
            fh.write(line + "\n"); print("SUMMARY", line)


if __name__ == "__main__":
    main()
