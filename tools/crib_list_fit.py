#!/usr/bin/env python3
"""crib_list_fit.py: rank every word of a list, built BEFORE scoring, by how well it fits a stretch of a keyed code
stream, with the list itself as the null (campaign espagnol142-mercy-1648 H41-H48, 28 Sept 2026).

A word is aligned whole and contiguously to the tokens of a window: a token whose key grade is S (or --fixed-grades)
consumes one letter and scores +1 if its key letter equals it, -1 if not; a wildcard token (any other grade, the
key's '_' letter, or a --wild-codes code) consumes one or two letters at 0 (a nomenclature or syllable code, or an
uncertain value). --anchor start fixes the word's first letter at --start, --anchor end fixes its last letter at
--end, --anchor free takes the best start in the window. The list is the null: P = share of list words fitting at
least as well as the best. Rule (all must hold for a candidate): the best word is the list's UNIQUE best, P < --p-max,
at least --min-agree of its letters agree at fixed tokens, and at most --max-mismatch disagree. The minimum-fit terms
were added after H46, where a list's unique best fitted 0 (two letters agreeing, two disagreeing) and would have passed
on uniqueness and P alone.

Catches (tests/test_crib_list_fit.py): the Mercy H41 case -- "burgsdorf" is the unique best on r16:2-r18 against
distractors, 7 of 9 letters agreeing, no mismatch, rule met. Must NOT pass: the H46 case -- v04 with a list whose best
is "poca" at fit 0 (unique, but under the minimum fit).

A candidate is a crib to test further, never a reading; this tool never writes solved, new or first.

  python3 tools/crib_list_fit.py --codes ciphers/<t>/cipher_codes_522.tsv --key ciphers/<t>/key.tsv \\
      --words LIST.tsv --start r16:2 --end r18:21 [--anchor free|start|end] [--forms '{w}' '{w}de'] [--top 12]
"""
import argparse, csv, sys
from functools import lru_cache


def load_window(codes, key, start, end, fixed_grades=("S",), wild_codes=()):
    kmap = {r["code"]: (r["letter"], r["grade"]) for r in csv.DictReader(open(key), delimiter="\t")}
    toks, on = [], start is None
    for r in csv.DictReader(open(codes), delimiter="\t"):
        loc = f"{r['line']}:{r['position']}"
        if not on and loc == start:
            on = True
        if on:
            l, g = kmap.get(r["sign"], ("_", "M"))
            wild = g not in fixed_grades or l == "_" or r["sign"] in wild_codes
            toks.append((l, wild, loc))
        if end is not None and loc == end:
            break
    return toks


def fit(word, toks, anchor="free"):
    """(score, agree, mismatch, start_loc) of the best whole alignment of word to toks."""
    seq = toks[::-1] if anchor == "end" else toks
    w = word[::-1] if anchor == "end" else word

    @lru_cache(None)
    def f(i, j, st):
        if j == len(w):
            return (0, 0, 0)
        if st + i >= len(seq):
            return (-99, 0, 0)
        l, wild, _ = seq[st + i]
        if wild:
            return max(f(i + 1, j + k, st) for k in (1, 2) if j + k <= len(w))
        s, a, m = f(i + 1, j + 1, st)
        eq = l == w[j]
        return (s + (1 if eq else -1), a + eq, m + (not eq))

    starts = [0] if anchor in ("start", "end") else range(len(seq))
    best = None
    for st in starts:
        r = f(0, 0, st)
        if best is None or r > best[:3]:
            best = r + (seq[st][2],)
    return best


def rank(words, toks, anchor="free", forms=("{w}",)):
    res = []
    for word in words:
        for form in forms:
            ww = form.format(w=word)
            res.append(fit(ww, toks, anchor) + (ww,))
    res.sort(key=lambda r: (-r[0], r[4]))
    return res


def verdict(res, p_max=0.05, min_agree=0.6, max_mismatch=1):
    best = res[0]
    ties = sum(1 for r in res if r[0] == best[0])
    p = sum(1 for r in res if r[0] >= best[0]) / len(res)
    ok = ties == 1 and p < p_max and best[1] >= min_agree * len(best[4]) and best[2] <= max_mismatch
    return {"best": best[4], "score": best[0], "agree": best[1], "mismatch": best[2], "at": best[3], "ties": ties,
            "P": p, "candidate": ok}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--codes", required=True, help="line/position/sign TSV")
    ap.add_argument("--key", required=True, help="code/letter/grade TSV")
    ap.add_argument("--words", required=True, help="word list, first column, built before scoring")
    ap.add_argument("--start"); ap.add_argument("--end")
    ap.add_argument("--anchor", choices=["free", "start", "end"], default="free")
    ap.add_argument("--forms", nargs="+", default=["{w}"], help="e.g. '{w}' '{w}de' 'su{w}mayor'")
    ap.add_argument("--fixed-grades", nargs="+", default=["S"])
    ap.add_argument("--wild-codes", nargs="*", default=[])
    ap.add_argument("--p-max", type=float, default=0.05)
    ap.add_argument("--min-agree", type=float, default=0.6)
    ap.add_argument("--max-mismatch", type=int, default=1)
    ap.add_argument("--top", type=int, default=12)
    a = ap.parse_args()
    words = [l.split("\t")[0].strip() for l in open(a.words) if l.strip()]
    toks = load_window(a.codes, a.key, a.start, a.end, tuple(a.fixed_grades), tuple(a.wild_codes))
    res = rank(words, toks, a.anchor, tuple(a.forms))
    v = verdict(res, a.p_max, a.min_agree, a.max_mismatch)
    print("window:", "".join("?" if w else l for l, w, _ in toks))
    print(f"{len(res)} forms; best {v['best']} fit {v['score']} ({v['agree']} agree, {v['mismatch']} disagree) at "
          f"{v['at']}; ties {v['ties']}; P {v['P']:.3f}; candidate: {v['candidate']}")
    for r in res[:a.top]:
        print(f"  {r[4]}\t{r[0]}\t{r[1]}/{r[2]}\t{r[3]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
