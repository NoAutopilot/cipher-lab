#!/usr/bin/env python3
"""Control 2 for family C (design-mismatched; family_C_spec.md): solve Armstrong's 15 Feb 1808 letter to Madison
(Founders 99-01-02-2703, 243 groups, THE=972) BLIND with tools/families/nomenclator.py and the same prior, without
the THE=972 key, and score it against the H/C-graded entries of tools/data/uscodes-1800/THE972_bourdeau.tsv.
The group list is the one ARM-CODES embedded in tools/data/uscodes-1800/stats.py (THE972_USAGE["1808-02-15"]).
Design-mismatched by construction: THE=972 is contiguously numbered, spells with syllables, and keeps particles
inside the main list, so this says only whether the solver reads Armstrong's idiolect at this N; it does not license
the target. Word-level recovery is reported over all known groups and, separately, over known groups whose entry is
a whole word of >= 3 letters in the LM vocabulary (a word solver cannot emit a syllable fragment such as "ac").
Offline. Run: python3 ciphers/armstrong-madison-1808/families/control2_feb15.py [--sweeps 60 --restarts 3 --seed 1]
Writes control2_feb15-<seed>.txt beside this script and prints the summary line for HYPOTHESES.md."""
import argparse, io, contextlib, os, re, sys, time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import judge_plaintext as jp  # noqa: E402
from families import nomenclator as nm  # noqa: E402

STATS = os.path.join(ROOT, "tools", "data", "uscodes-1800", "stats.py")
TABLE = os.path.join(ROOT, "tools", "data", "uscodes-1800", "THE972_bourdeau.tsv")


def groups():
    src = open(STATS, encoding="utf-8").read()
    m = re.search(r'"1808-02-15":\s*"([^"]+)"', src)
    return m.group(1).split()


def truth_table():
    t = {}
    for line in open(TABLE, encoding="utf-8"):
        f = line.rstrip("\n").split("\t")
        if len(f) >= 3 and f[0].isdigit() and f[2] in ("H", "C"):
            t[f[0]] = " ".join(nm.words_of(f[1]))
    return t


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sweeps", type=int, default=60)
    ap.add_argument("--restarts", type=int, default=3)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--shuffle", type=int, default=None, help="permute the group order first (floor for this control)")
    a = ap.parse_args()
    g = groups()
    if a.shuffle is not None:
        import random
        random.Random(a.shuffle).shuffle(g)
    truth = truth_table()
    corpora = [jp.read_corpus(str(p)) for p in jp.LANG_CORPORA["en18"]]
    t0 = time.time()
    dec, sc, info = nm.solve([g], {}, a.seed, a.restarts, corpora, {"sweeps": a.sweeps, "N": len(g), "K": len(set(g))})
    words = dec.split()
    lm = nm.get_lm(corpora, 3)
    known = [(i, truth[v]) for i, v in enumerate(g) if v in truth]
    wordlike = [(i, w) for i, w in known if " " not in w and len(w) >= 3 and w in lm.vocab]
    hit_all = sum(words[i] == w for i, w in known)
    hit_word = sum(words[i] == w for i, w in wordlike)
    n = len(g)
    tag = f"-shuffle{a.shuffle}" if a.shuffle is not None else ""
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"control2_feb15-{a.seed}{tag}.txt")
    line = (f"CONTROL 2 (design-mismatched, 15 Feb 1808 THE=972 blind): N={n} K={len(set(g))} known(H/C)={len(known)} "
            f"recovery all-known {hit_all}/{len(known)} ({hit_all / max(1, len(known)):.3f}); whole-word entries "
            f"{hit_word}/{len(wordlike)} ({hit_word / max(1, len(wordlike)):.3f}); score {sc:.1f} "
            f"({sc / n:.3f}/token); sweeps {a.sweeps} restarts {a.restarts} seed {a.seed}{tag}; {time.time() - t0:.0f}s")
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"# {line}\n# {info}\n# salad, not a reading (rule 10); truth from THE972_bourdeau.tsv H/C rows\n")
        for i, (v, w) in enumerate(zip(g, words)):
            f.write(f"{i}\t{v}\t{w}\t{truth.get(v, '')}\n")
    print(line)
    print("first 40 (salad):", " ".join(words[:40]))
    print("decode ->", os.path.relpath(out, ROOT))


if __name__ == "__main__":
    main()
