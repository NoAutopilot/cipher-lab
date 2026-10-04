#!/usr/bin/env python3
"""N8-NV05B scorer for key no.54 on fr.15575 f.228 batch B2 (L05-L08), as PREREG-ADDENDUM-N8B.md registers it.

  python3 score_b2.py [--out score_b2.tsv] [--check]

Gated: S on L05-L08 (ciphertext_b2.tsv vs gloss_b2.tsv). Reported, ungated: pooled L01-L08 (ciphertext.tsv +
ciphertext_b2.tsv vs gloss_v2.tsv + gloss_b2.tsv). Statistic ../control_fr3641/score_control.py score() (imported);
control = values permuted among the 95 coded syllable rows, 1000 draws, seed 1, for each of the two sets.
Gate PASS iff S > control p99 AND S >= 0.60. --check exits 1 if score_b2.tsv differs from a regeneration (rule 7).
"""
import argparse, csv, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "control_fr3641"))
import score_control as sc  # noqa: E402


def load_cipher(name):
    lines = {}
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            lines.setdefault(r["line"], []).append(r["sign"].rstrip("?"))
    return lines


def load_gloss(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        return {r["line"]: sc.norm(r["text"]) for r in csv.DictReader(f, delimiter="\t")}


def run(tag, lines, gloss, real):
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
    out = [f"{tag}_S_real\t{S:.4f}", f"{tag}_matched\t{m}", f"{tag}_scored_tokens\t{n}",
           f"{tag}_letter_agreement_real\t{L:.4f}", f"{tag}_control_mean\t{mean:.4f}", f"{tag}_control_p99\t{p99:.4f}",
           f"{tag}_control_max\t{ctrl[-1]:.4f}", f"{tag}_control_ge_real\t{ge}", f"{tag}_gate\t{gate}"]
    return out + [f"{tag}_line_{ln}\t{a_}/{b_} tokens; {c_}/{d_} gloss letters" for ln, a_, b_, c_, d_ in per]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=os.path.join(HERE, "score_b2.tsv"))
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    real = {c: v for c, (v, _) in sc.load_key().items()}
    b2, g2 = load_cipher("ciphertext_b2.tsv"), load_gloss("gloss_b2.tsv")
    pool = dict(load_cipher("ciphertext.tsv"), **b2); gpool = dict(load_gloss("gloss_v2.tsv"), **g2)
    out = ["metric\tvalue", "control_draws\t1000", "control_seed\t1"]
    out += run("B2_L05-L08", b2, g2, real)
    out += [r.replace("POOL", "pooled_L01-L08_ungated") for r in run("POOL", pool, gpool, real)]
    text = "\n".join(out) + "\n"
    if a.check:
        old = open(a.out, encoding="utf-8").read() if os.path.exists(a.out) else ""
        if old != text:
            print("score_b2.tsv is stale"); sys.exit(1)
        print("score_b2.tsv up to date"); return
    open(a.out, "w", encoding="utf-8").write(text)
    print(text, end="")


if __name__ == "__main__":
    main()
