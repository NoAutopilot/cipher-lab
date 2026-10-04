#!/usr/bin/env python3
"""NV05E scorer for key no.54 on fr.15575 f.228 L01-L04 (statistic, controls and gates as in PREREG.md).

  python3 score_f228.py [--gloss gloss.tsv] [--out score.tsv] [--check]
  (N8-NV05 re-score: --gloss gloss_v2.tsv --out score_v2.tsv, PREREG-ADDENDUM-N8.md)

Known-answer gate: ../control_fr3641/score_control.py's score() (imported, not re-derived) on this folder's
ciphertext.tsv + gloss.tsv; control = values permuted among the 95 coded syllable rows, 1000 draws, seed 1.
Language judge (secondary): tools/judge_plaintext.py's NgramModel on judge_spec.json's corpora; the judged string is
the syllable-code values only (other tokens dropped). Controls: value-shuffled key, 200 draws, seed 2; token order
shuffled within each line, 20 draws, seed 3. --check exits 1 if score.tsv differs from a regeneration (rule 7).
"""
import argparse, csv, json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..", "..")
sys.path.insert(0, os.path.join(HERE, "..", "control_fr3641"))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import score_control as sc  # noqa: E402
from judge_plaintext import NgramModel, read_corpus, pct  # noqa: E402


def load_cipher():
    lines = {}
    with open(os.path.join(HERE, "ciphertext.tsv"), encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            lines.setdefault(r["line"], []).append(r["sign"].rstrip("?"))
    return lines


def load_gloss(name="gloss.tsv"):
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        return {r["line"]: sc.norm(r["text"]) for r in csv.DictReader(f, delimiter="\t")}


def dec_string(lines, values):
    return "".join(sc.norm(values[t]) for ln in sorted(lines) for t in lines[ln] if t in values)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--gloss", default="gloss.tsv")
    ap.add_argument("--out", default=os.path.join(HERE, "score.tsv"))
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    key = sc.load_key(); lines = load_cipher(); gloss = load_gloss(a.gloss)
    real = {c: v for c, (v, _) in key.items()}
    S, m, n, L, per = sc.score(lines, gloss, real)
    codes = sorted(real); vals = [real[c] for c in codes]
    rng = random.Random(1); ctrl = []
    for _ in range(1000):
        vv = vals[:]; rng.shuffle(vv)
        ctrl.append(sc.score(lines, gloss, dict(zip(codes, vv)))[0])
    ctrl.sort()
    p99 = ctrl[int(0.99 * len(ctrl)) - 1]; mean = sum(ctrl) / len(ctrl)
    ge = sum(1 for c in ctrl if c >= S)
    gate = "PASS" if (S > p99 and S >= 0.60) else "FAIL"

    spec = json.load(open(os.path.join(HERE, "judge_spec.json"), encoding="utf-8"))
    model = NgramModel([read_corpus(os.path.join(ROOT, p)) for p in spec["judge"]["corpora"]])
    txt = dec_string(lines, real); N = max(len(txt), 20)
    rtext, null, _ = model.controls(N, samples=200)
    null99, real05 = pct(null, 0.99), pct(rtext, 0.05)
    passes = lambda s: s > null99 and s > real05  # noqa: E731
    jr = model.score(txt)
    rng2 = random.Random(2); vsh = []
    for _ in range(200):
        vv = vals[:]; rng2.shuffle(vv)
        vsh.append(model.score(dec_string(lines, dict(zip(codes, vv)))))
    rng3 = random.Random(3); osh = []
    for _ in range(20):
        sh = {ln: rng3.sample(t, len(t)) for ln, t in lines.items()}
        osh.append(model.score(dec_string(sh, real)))
    out = ["metric\tvalue",
           f"S_real\t{S:.4f}", f"matched\t{m}", f"scored_tokens\t{n}", f"letter_agreement_real\t{L:.4f}",
           "control_draws\t1000", "control_seed\t1", f"control_mean\t{mean:.4f}",
           f"control_p99\t{p99:.4f}", f"control_max\t{ctrl[-1]:.4f}", f"control_ge_real\t{ge}", f"gate\t{gate}"]
    out += [f"line_{ln}\t{a_}/{b_} tokens; {c_}/{d_} gloss letters" for ln, a_, b_, c_, d_ in per]
    out += [f"judge_letters\t{len(txt)}", f"judge_score_real\t{jr:.3f}", f"judge_null_p99\t{null99:.3f}",
            f"judge_real_p05\t{real05:.3f}", f"judge_verdict_real\t{'PASS' if passes(jr) else 'FAIL'}",
            f"judge_valueshuffled_mean\t{sum(vsh) / len(vsh):.3f}",
            f"judge_valueshuffled_pass\t{sum(map(passes, vsh))}/200",
            f"judge_valueshuffled_ge_real\t{sum(1 for v in vsh if v >= jr)}/200",
            f"judge_ordershuffled_mean\t{sum(osh) / len(osh):.3f}",
            f"judge_ordershuffled_pass\t{sum(map(passes, osh))}/20"]
    text = "\n".join(out) + "\n"
    if a.check:
        old = open(a.out, encoding="utf-8").read() if os.path.exists(a.out) else ""
        if old != text:
            print("score.tsv is stale"); sys.exit(1)
        print("score.tsv up to date"); return
    open(a.out, "w", encoding="utf-8").write(text)
    print(text, end="")


if __name__ == "__main__":
    main()
