#!/usr/bin/env python3
"""segmenter.py: divide an undivided decode into words from an era lexicon, and list the plausible fragments in it.

MQS-SEGMENTER (LANE MQS-2, 9 Oct 2026; research/MARY-STUART-TALK-2026-10-09.tsv rows M18 and M24). Method after CTTS
(Lasry) and Lasry, Biermann and Tomokiyo 2023 (Cryptologia 47:2), pp.113-115 (fragments highlighted in solver output)
and p.190 n.344 (word division as a separate last step: 'Renous Banque' vs 'entre nous Banque'). Starts from
judge_plaintext.NgramModel.cover's greedy longest-word segmentation, replaced here by a unigram Viterbi over the same
corpus's word counts so one bad greedy choice does not wreck the rest of the line.

Usage:
  python3 tools/segmenter.py --lexicon fr --text "entrenousbanque"           divided text
  python3 tools/segmenter.py --lexicon fr --file decode.txt --fragments 12   fragments (offset, letters, words) as TSV
  python3 tools/segmenter.py --selftest

Lexicon: a judge_plaintext corpus code (fr, en, fr17, ...) or a text file. Word types with count >= 2, length >= 2,
plus the language's single-letter words (French a, y; English a, i; others a). A letter outside every word costs
UNK = 2 x the rarest word's cost per letter.

What each part is meant to catch, and what it must NOT flag (Usage 8a; offline tests in tools/tests/test_segmenter.py):
  segment()    catches: word boundaries in undivided prose of the lexicon's language and era (control A in
               tools/tests/PREREG-MQS-SEGMENTER.md). Must NOT: invent a lexicon word over letters that spell none --
               such letters come back as one-letter unknown tokens (in_lexicon False).
  fragments()  catches: runs of >= K letters that segment entirely into lexicon words of >= 2 letters and contain one
               word of >= 5 letters (control B: a decode with a key wrong on 8 of 26 types). Must NOT flag: a decode
               under a wholly wrong key (control B0), nor a run built only of short function words ('de la le en').
A fragment is a lead for a person or a verifier, never a reading (rule 10); its null is the same list from the decode
of the shuffled target (ARM-C1 rule), which judge_plaintext.py --fragments takes as --fragments-null FILE.
"""
import argparse, math, re, sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_plaintext as jp  # noqa: E402

SINGLE = {"fr": {"a", "y"}, "en": {"a", "i"}}


class Lexicon:
    def __init__(self, counts, singles=("a",)):
        self.counts = {w: n for w, n in counts.items() if n >= 2 and (len(w) >= 2 or w in singles)}
        tot = sum(self.counts.values()) or 1
        self.cost = {w: -math.log10(n / tot) for w, n in self.counts.items()}
        self.maxw = max((len(w) for w in self.cost), default=1)
        self.unk = 2 * max(self.cost.values(), default=1.0)

    @classmethod
    def from_texts(cls, texts, singles=("a",)):
        c = Counter()
        for t in texts:
            t = re.sub(r"-\s*\n\s*", "", t)  # line-end hyphenation joined
            c.update(jp.fold(w) for w in re.findall(r"[^\W\d_]+", t))
        c.pop("", None)
        return cls(c, singles)

    @classmethod
    def load(cls, spec):
        if Path(spec).exists():
            return cls.from_texts([Path(spec).read_text(encoding="utf-8", errors="replace")])
        if spec not in jp.LANG_CORPORA:
            raise SystemExit(f"lexicon {spec!r}: neither a file nor a corpus code in judge_plaintext.LANG_CORPORA")
        return cls.from_texts([jp.read_corpus(p) for p in jp.LANG_CORPORA[spec]],
                              SINGLE.get(spec[:2], {"a"}))


def segment(s, lex):
    """[(token, in_lexicon)] for folded s: min-cost division into lexicon words and one-letter unknowns."""
    s = jp.fold(s); n = len(s)
    best = [0.0] + [math.inf] * n; back = [(0, False)] * (n + 1)
    for i in range(1, n + 1):
        c = best[i - 1] + lex.unk
        if c < best[i]:
            best[i], back[i] = c, (i - 1, False)
        for L in range(1, min(lex.maxw, i) + 1):
            w = s[i - L:i]
            if w in lex.cost:
                c = best[i - L] + lex.cost[w]
                if c < best[i]:
                    best[i], back[i] = c, (i - L, True)
    out, i = [], n
    while i > 0:
        j, ok = back[i]; out.append((s[j:i], ok)); i = j
    return out[::-1]


def fragments(s, lex, K=12, min_long=5):
    """[(offset, letters, words)] maximal runs of lexicon words >= 2 letters (a one-letter word inside a run is kept
    only between two such words), >= K letters, with one word >= min_long letters."""
    toks = segment(s, lex)
    good = [ok and len(t) >= 2 for t, ok in toks]
    for i, (t, ok) in enumerate(toks):  # single-letter lexicon word bridging two good words
        if ok and len(t) == 1 and 0 < i < len(toks) - 1 and good[i - 1] and good[i + 1]:
            good[i] = True
    out, off, i = [], 0, 0
    offs = []
    for t, _ in toks:
        offs.append(off); off += len(t)
    while i < len(toks):
        if not good[i]:
            i += 1; continue
        j = i
        while j < len(toks) and good[j]:
            j += 1
        ws = [toks[k][0] for k in range(i, j)]
        L = sum(map(len, ws))
        if L >= K and max(map(len, ws)) >= min_long:
            out.append((offs[i], L, ws))
        i = j
    return out


def divided(s, lex):
    return " ".join(t for t, _ in segment(s, lex))


def selftest():
    lex = Lexicon(Counter({"entre": 50, "nous": 80, "banque": 5, "de": 900, "la": 700, "le": 800, "en": 400,
                           "roi": 60, "lettre": 30, "a": 300, "votre": 40, "majeste": 20}), singles=("a",))
    assert divided("entrenousbanque", lex) == "entre nous banque", divided("entrenousbanque", lex)
    assert all(not ok for t, ok in segment("qxzkw", lex))
    f = fragments("qxzkwvotremajestealettreduroiqxzk", lex, K=12)
    assert f and f[0][2][:2] == ["votre", "majeste"], f
    assert not fragments("delaleendelaleen", lex, K=12)  # function words only: no word >= 5 letters
    print("selftest ok: entre nous banque; unknown letters stay unknown; fragment found; function-word run not flagged")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lexicon", default="fr"); ap.add_argument("--text"); ap.add_argument("--file")
    ap.add_argument("--fragments", type=int, metavar="K", help="list fragments of >= K letters instead of dividing")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest(); return
    if not (a.text or a.file):
        ap.error("--text or --file")
    t = a.text if a.text else "\n".join(l for l in Path(a.file).read_text(encoding="utf-8").splitlines()
                                         if not l.lstrip().startswith("#"))
    lex = Lexicon.load(a.lexicon)
    if a.fragments:
        print("offset\tletters\twords")
        for o, L, ws in fragments(t, lex, a.fragments):
            print(f"{o}\t{L}\t{' '.join(ws)}")
    else:
        print(divided(t, lex))


if __name__ == "__main__":
    main()
