#!/usr/bin/env python3
"""MANT-0290W word/syllable-code gloss gate for 694/08 0290 (PREREG-MANT0290W.md).

For each gloss-bearing code token on 0290 (per blind gloss pass, gloss_spans_A/B.tsv), ask whether the 0290 note
over it shares a content word with any note or clear word standing over the SAME code on another leaf on disk
(the frozen witness file list below; 0290 itself excluded). Control: the 0290 notes permuted across the pass's
gloss-bearing tokens (code-gloss pairing shuffled), 1000 draws, seed 2900; per-class S, mean, p99, min, max.

Classes (key.tsv first alternative): letter = value of <= 3 letters; keyed-word = longer value (names, words);
unkeyed = code absent from key.tsv (the word/syllable codes the brief asks about). A class with K < 5 tokens that
have a witness elsewhere is untestable. PASS for a class: S > p99 and S >= 0.5 x K. A class whose control
min == max (the shuffle cannot move the statistic) is a non-test by construction (rule 3).

Usage: python3 word_gate.py [--pass A|B] [--witnesses]   (run from anywhere; paths are relative to this file)
"""
import argparse, csv, os, random, re, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SEED, DRAWS, KMIN = 2900, 1000, 5

# Frozen witness list (PREREG-MANT0290W.md). Gloss spans (columns gloss + codes) and the CUC clear-under-code strips.
GLOSS_FILES = [
    "f0136_08/gloss_spans.tsv", "f0312_08/spans_G1.tsv", "f0312_08/spans_G2.tsv", "f0314_08/spans_G1.tsv",
    "f0314_08/spans_G2.tsv", "f0474_08/gloss.tsv", "f0494_08/gloss.tsv", "f0089_08/gloss_spans.tsv",
    "f0136_09/gloss_A.tsv", "f0136_09/gloss_B.tsv", "f0136_09/gloss_A1A.tsv", "f0136_09/gloss_A1B.tsv",
    "f0007_09/gloss.tsv", "f0008_09/gloss.tsv", "f0056_09/gloss.tsv", "f0063_09/gloss.tsv",
]
CUC_PAIRS = [("mant0608/cuc/agreed.tsv", "mant0608/cuc/clear_blind.tsv"),
             ("mant0608/cuc/cuc3_agreed.tsv", "mant0608/cuc/cuc3_clear_blind.tsv")]

STOP = set("le la les de du des au aux et en un une que qui il ils ne se sa son ses nous vous ou par pour sur ce cet "
           "cette est sont lui leur dans pas plus mais avec item".split())


def norm_words(text):
    t = unicodedata.normalize("NFD", text.lower())
    t = "".join(ch for ch in t if not unicodedata.combining(ch))
    t = t.replace("v", "u").replace("j", "i").replace("y", "i")
    out = []
    for w in re.split(r"[^a-z]+", t):
        if len(w) >= 3 and w not in STOP:
            out.append(w)
    return out


def words_match(a, b):
    """Shared content word: equal, one a prefix of the other (abbreviation), or the same first 4 letters."""
    if a == b or a.startswith(b) or b.startswith(a):
        return True
    return len(a) >= 4 and len(b) >= 4 and a[:4] == b[:4]


def read_tsv(path):
    with open(path, newline="") as f:
        rows = [l for l in f if not l.startswith("#")]
    return list(csv.DictReader(rows, delimiter="\t"))


def split_codes(s):
    return [c for c in re.split(r"[ .]+", (s or "").strip()) if c and c != "?"]


def witnesses():
    """code -> {leaf: set(words)} from every frozen witness file (0290 never included)."""
    wit = {}
    for rel in GLOSS_FILES:
        leaf = rel.split("/")[0]
        for r in read_tsv(os.path.join(ROOT, rel)):
            for c in split_codes(r.get("codes")):
                wit.setdefault(c, {}).setdefault(leaf, set()).update(norm_words(r.get("gloss", "")))
    for codes_rel, clear_rel in CUC_PAIRS:
        clear = {(r["leaf"], r["strip"]): r["clear"] for r in read_tsv(os.path.join(ROOT, clear_rel))}
        for r in read_tsv(os.path.join(ROOT, codes_rel)):
            txt = clear.get((r["leaf"], r["strip"]), "")
            for c in split_codes(r["codes"]):
                wit.setdefault(c, {}).setdefault("cuc" + r["leaf"], set()).update(norm_words(txt))
    return wit


def key_classes():
    cls = {}
    for r in read_tsv(os.path.join(ROOT, "key.tsv")):
        v = r["value"].split("|")[0]
        cls[r["code"]] = "letter" if len(re.sub(r"[^A-Za-z]", "", v)) <= 3 else "keyed-word"
    return cls


def consistent(gloss_words, wit_leaves):
    return any(words_match(a, b) for ws in wit_leaves.values() for b in ws for a in gloss_words)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--pass", dest="p", choices=["A", "B"], required=True)
    ap.add_argument("--witnesses", action="store_true", help="list each 0290 code's witnesses elsewhere")
    a = ap.parse_args()
    wit, kcls = witnesses(), key_classes()
    toks = []  # (code, class, gloss_words)
    for r in read_tsv(os.path.join(HERE, f"gloss_spans_{a.p}.tsv")):
        for c in split_codes(r["codes"]):
            toks.append((c, kcls.get(c, "unkeyed"), norm_words(r["gloss"]), r["gloss"]))
    classes = ["letter", "keyed-word", "unkeyed"]
    print(f"pass {a.p}: {len(toks)} gloss-bearing code tokens; witness codes on disk: {len(wit)}")
    if a.witnesses:
        for c in sorted({t[0] for t in toks}, key=int):
            w = wit.get(c, {})
            print(f"  {c} [{kcls.get(c, 'unkeyed')}]: " + ("; ".join(f"{l}:{' '.join(sorted(s)) or '-'}" for l, s in sorted(w.items())) or "(no witness elsewhere)"))

    def score(glosses):
        s = {k: 0 for k in classes}
        for (c, k, _, _), g in zip(toks, glosses):
            if c in wit and consistent(g, wit[c]):
                s[k] += 1
        return s

    K = {k: sum(1 for t in toks if t[1] == k and t[0] in wit) for k in classes}
    N = {k: sum(1 for t in toks if t[1] == k) for k in classes}
    real = score([t[2] for t in toks])
    rng = random.Random(SEED)
    draws = {k: [] for k in classes}
    pool = [t[2] for t in toks]
    for _ in range(DRAWS):
        perm = pool[:]
        rng.shuffle(perm)
        s = score(perm)
        for k in classes:
            draws[k].append(s[k])
    tot_real, tot_draws = sum(real.values()), [sum(draws[k][i] for k in classes) for i in range(DRAWS)]
    rows = [(k, N[k], K[k], real[k], draws[k]) for k in classes] + [("pooled", sum(N.values()), sum(K.values()), tot_real, tot_draws)]
    print("class\tN_tokens\tK_with_witness\tS\tctrl_mean\tctrl_p99\tctrl_min\tctrl_max\tctrl>=real\tverdict")
    for k, n, kk, s, d in rows:
        ds = sorted(d)
        p99 = ds[int(0.99 * DRAWS) - 1]
        ge = sum(1 for x in d if x >= s)
        if ds[0] == ds[-1]:
            v = "non-test (control cannot move)"
        elif kk < KMIN:
            v = f"untestable (K<{KMIN})"
        else:
            v = "PASS" if (s > p99 and s >= 0.5 * kk) else "FAIL"
        print(f"{k}\t{n}\t{kk}\t{s}\t{sum(d)/DRAWS:.2f}\t{p99}\t{ds[0]}\t{ds[-1]}\t{ge}/{DRAWS}\t{v}")
    print("per token (code class gloss -> consistent?):")
    for c, k, g, raw in toks:
        print(f"  {c}\t{k}\t{raw}\t{'witness' if c in wit else 'no-witness'}\t{int(c in wit and consistent(g, wit[c]))}")


if __name__ == "__main__":
    sys.exit(main())
