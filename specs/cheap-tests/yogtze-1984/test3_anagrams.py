#!/usr/bin/env python3
"""yogtze-1984 spec test 3 (R8-YOG3, 6 Oct 2026): anagram enumeration of YOGTZE.

A lexical search, not a reading. Pre-registration: PREREG-test3.md (this folder), committed
before this script was run. Enumerates every distinct ordering of the letters of each string in
the reading set and counts one-word (S1) and two-word (S2) anagrams against a corpus word list
(words with corpus count >= 2), per language. Control: 1000 draws of 6 distinct letters sampled
from the list's own token-weighted letter frequency, given the same reading-set freedom.

Usage: python3 test3_anagrams.py [--draws 1000] [--out test3_output.json]
"""
import argparse, collections, gzip, itertools, json, random, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
D = ROOT / "tools" / "data"
CORPORA = {
    "de": sorted((D / "de20").glob("*.txt.gz")) + sorted((D / "de19").glob("*.txt.gz")),
    "en": sorted((D / "en").glob("*.txt")) + [D / "pg1661_holmes.txt", D / "pg2701_mobydick.txt"],
}
LOOK = {"y": "v", "g": "c", "t": "f", "z": "s", "e": "f", "o": "d"}
FOLD = {"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"}
TARGET = "yogtze"
SEED = 20261006


def read(p):
    return (gzip.open(p, "rt", encoding="utf-8", errors="ignore") if p.suffix == ".gz" else open(p, encoding="utf-8", errors="ignore")).read()


def wordlist(lang):
    c = collections.Counter()
    for p in CORPORA[lang]:
        t = read(p).lower()
        for k, v in FOLD.items():
            t = t.replace(k, v)
        c.update(re.findall(r"[a-z]+", t))
    return {w for w, n in c.items() if n >= 2}, c


def reading_set(s6):
    """base, struck 4th letter, and one look-alike swap per letter in the map's domain."""
    out = [s6, s6[:3] + s6[4:]]
    for i, ch in enumerate(s6):
        if ch in LOOK:
            out.append(s6[:i] + LOOK[ch] + s6[i + 1:])
    return out


def score(s, words):
    perms = {"".join(p) for p in itertools.permutations(s)}
    one = sorted(p for p in perms if p in words)
    two = sorted(f"{p[:k]} {p[k:]}" for p in perms for k in range(2, len(p) - 1)
                 if p[:k] in words and p[k:] in words)
    return one, two


def H(s6, words, keep=False):
    tot, hits = 0, {}
    for s in reading_set(s6):
        one, two = score(s, words)
        tot += len(one) + len(two)
        if keep:
            hits[s] = {"one_word": one, "two_word": two}
    return tot, hits


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--draws", type=int, default=1000)
    ap.add_argument("--out", default=str(Path(__file__).with_name("test3_output.json")))
    a = ap.parse_args()
    res = {"prereg": "PREREG-test3.md", "seed": SEED, "draws": a.draws, "target": TARGET, "langs": {}}
    for lang in ("de", "en"):
        words, cnt = wordlist(lang)
        lf = collections.Counter()
        for w, n in cnt.items():
            for ch in w:
                lf[ch] += n
        letters, weights = zip(*sorted(lf.items()))
        rng = random.Random(SEED)
        th, hits = H(TARGET, words, keep=True)
        ctrl = []
        for _ in range(a.draws):
            pool, wts, draw = list(letters), list(weights), []
            for _ in range(6):
                ch = rng.choices(pool, wts)[0]
                i = pool.index(ch); pool.pop(i); wts.pop(i); draw.append(ch)
            ctrl.append(H("".join(draw), words)[0])
        cs = sorted(ctrl)
        res["langs"][lang] = {
            "list_size": len(words), "sources": [p.name for p in CORPORA[lang]],
            "target_H": th, "target_hits": hits,
            "control": {"mean": round(sum(cs) / len(cs), 2), "median": cs[len(cs) // 2],
                        "p05": cs[int(0.05 * len(cs))], "p95": cs[int(0.95 * len(cs))],
                        "min": cs[0], "max": cs[-1], "frac_zero": round(sum(1 for x in cs if x == 0) / len(cs), 3)},
            "P_le": round(sum(1 for x in cs if x <= th) / len(cs), 3),
            "P_lt": round(sum(1 for x in cs if x < th) / len(cs), 3),
        }
        print(lang, len(words), "target H", th, "control", res["langs"][lang]["control"], "P<=", res["langs"][lang]["P_le"], file=sys.stderr)
    Path(a.out).write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
