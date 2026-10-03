#!/usr/bin/env python3
"""NV05C known-answer control scorer for key no.54 on fr.3641 f.111r (statistic and control as in PREREG.md).

  python3 score_control.py [--draws 1000] [--seed 1] [--out score.tsv] [--check]

Reads ciphertext.tsv (line pos sign conf), gloss.tsv (line text), ../key_no54.tsv. Per line, the decoded stream
(syllable-code values; any other token -> '_') is LCS-aligned to the normalised gloss (tools/decode_witness.lcs_align).
S = scored 2-digit key-coded tokens whose every letter is matched / scored tokens. Control: values permuted among
the coded syllable rows, --draws times. --check exits 1 if score.tsv differs from a regeneration (rule 7).
"""
import argparse, csv, os, random, re, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "tools"))
from decode_witness import lcs_align  # noqa: E402

ABBR = [(r"\bduqz?\b", "duque"), (r"\bq~?\b", "que"), (r"\bqs\b", "ques"),
        (r"\bv\.?\s?m\.?\b", "vuestramagestad"), (r"\bs\.?\s?m\.?\b", "sumagestad")]


def norm(text):
    t = text.lower()
    for pat, rep in ABBR:
        t = re.sub(pat, rep, t)
    t = "".join(c for c in unicodedata.normalize("NFD", t) if unicodedata.category(c) != "Mn")
    t = t.translate(str.maketrans({"j": "i", "v": "u", "y": "i"}))
    return "".join(c for c in t if c.isalpha())


def load_key():
    key = {}
    with open(os.path.join(HERE, "..", "key_no54.tsv"), encoding="utf-8") as f:
        rows = [l.rstrip("\n").split("\t") for l in f if not l.startswith("#")]
    for r in rows[1:]:
        if len(r) >= 3 and r[2] == "syllable" and re.fullmatch(r"\d\d", r[0]):
            key[r[0]] = (r[1], r[3])
    return key


def load_cipher():
    lines = {}
    with open(os.path.join(HERE, "ciphertext.tsv"), encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            lines.setdefault(r["line"], []).append(r["sign"].rstrip("?"))
    return lines


def load_gloss():
    with open(os.path.join(HERE, "gloss.tsv"), encoding="utf-8") as f:
        return {r["line"]: norm(r["text"]) for r in csv.DictReader(f, delimiter="\t")}


def score(lines, gloss, values):
    m = n = lm = gl = 0
    per = []
    for ln in sorted(lines):
        dec, owner = [], []
        for i, tok in enumerate(lines[ln]):
            v = norm(values[tok]) if tok in values else "_"
            v = v or "_"
            for ch in v:
                dec.append(ch)
                owner.append(i if tok in values else None)
        g = list(gloss.get(ln, ""))
        k, pairs = lcs_align(dec, g) if g else (0, [])
        matched = {d for d, _ in pairs}
        ok = {}
        for d, o in enumerate(owner):
            if o is not None:
                ok[o] = ok.get(o, True) and d in matched
        lm_, ln_ = sum(ok.values()), len(ok)
        m += lm_; n += ln_; lm += k; gl += len(g)
        per.append((ln, lm_, ln_, k, len(g)))
    return (m / n if n else 0.0), m, n, (lm / gl if gl else 0.0), per


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--draws", type=int, default=1000)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--out", default=os.path.join(HERE, "score.tsv"))
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    key = load_key(); lines = load_cipher(); gloss = load_gloss()
    real = {c: v for c, (v, _) in key.items()}
    S, m, n, L, per = score(lines, gloss, real)
    codes = sorted(real); vals = [real[c] for c in codes]
    rng = random.Random(a.seed); ctrl = []
    for _ in range(a.draws):
        vv = vals[:]; rng.shuffle(vv)
        ctrl.append(score(lines, gloss, dict(zip(codes, vv)))[0])
    ctrl.sort()
    p99 = ctrl[int(0.99 * len(ctrl)) - 1]; mean = sum(ctrl) / len(ctrl)
    ge = sum(1 for c in ctrl if c >= S)
    verdict = "PASS" if (S > p99 and S >= 0.60) else "FAIL"
    out = ["metric\tvalue",
           f"S_real\t{S:.4f}", f"matched\t{m}", f"scored_tokens\t{n}", f"letter_agreement_real\t{L:.4f}",
           f"control_draws\t{a.draws}", f"control_seed\t{a.seed}", f"control_mean\t{mean:.4f}",
           f"control_p99\t{p99:.4f}", f"control_max\t{ctrl[-1]:.4f}", f"control_ge_real\t{ge}", f"gate\t{verdict}"]
    out += [f"line_{ln}\t{a_}/{b_} tokens; {c_}/{d_} gloss letters" for ln, a_, b_, c_, d_ in per]
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
