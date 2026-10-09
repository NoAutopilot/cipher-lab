#!/usr/bin/env python3
"""Token frequency analysis for a ciphertext file.

Usage: python3 tools/freq.py FILE [--sep REGEX] [--top N] [--strip-clear]
       python3 tools/freq.py FILE --contacts K
       python3 tools/freq.py FILE --kwic TOKEN [--width W] [--sort left|right]
       python3 tools/freq.py FILE --repeats N
       python3 tools/freq.py FILE --split-at N
       python3 tools/freq.py FILE --split-at auto
       python3 tools/freq.py FILE --contacts K --vowels
       python3 tools/freq.py FILE --onepart-dict LANG [--onepart-range MIN,MAX] [--top N]
       python3 tools/freq.py POOL --tail N [--tail-end end|start|both] [--tail-reps R] [--tail-seed S]

Tokens are split on ';' and whitespace by default. Lines starting with '#'
are ignored. --strip-clear drops tokens that contain no digit, which removes
interleaved cleartext words from mixed letters (but also drops pure-letter
cipher symbols, so don't use it on symbol ciphers).

With none of --contacts/--kwic/--repeats/--split-at given, reports: token
count, distinct tokens, index of coincidence, the most frequent tokens, the
most frequent bigrams, and the numeric range (unchanged from before 27 Sept
2026). Giving one or more of the four new options prints only their TSV
table(s) (one per line, tab-separated, a header row first) instead of the
default report, so each can be piped straight to its own file.

--contacts K (Tomokiyo codebreaking.htm "Statistical Analysis", contact.htm,
kwic.htm): for each of the K most frequent tokens, its count and share, the
tokens that precede and follow it with their counts, its self-succession
count (how many times it is immediately followed by another instance of
itself -- necessarily the same as how many times it is immediately preceded
by one, since both count the same adjacent same-token pairs), and a
prefix-like/suffix-like/neither tag. The tag is NOT computed from
self-succession (which cannot by itself distinguish the two directions --
see above), but from the actual finding in Yardley's own account of code
group 42635 (codebreaking.htm: "it was often preceded by the same group but
was always followed by a different group"): left-context CONCENTRATION (one
particular preceding token accounts for >= --tag-threshold, default 0.4, of
all occurrences) together with right-context DIVERSITY (every following
token distinct) tags a token suffix-like; the mirror (right-context
concentrated, left-context all-distinct) tags it prefix-like. Tokens with
fewer than --tag-min (default 3) occurrences are always tagged "neither"
(too little context to judge concentration/diversity).

--vowels (with --contacts; TT-FREQ, 8 Oct 2026): Tomokiyo's own contact chart
on the Ormonde cipher (ormonde.htm, "Contact Chart and First Findings") showed
"78 does not appear together with other high-frequency letters", which made 78
a vowel ("o"); contact.htm cites Kahn pp.100-102 for the method. --vowels
runs Sukhotin's contact-matrix vowel algorithm on the K most frequent tokens
(symmetric adjacency counts, self-contacts zeroed) and prints each token's
class (V vowel-like / C consonant-like) and its remaining contact sum when
it was promoted. Meant to catch: the vowel group of a letter cipher, even a
homophonic one, from contacts alone. Must NOT flag: a shuffled-order copy of
the same stream (contacts carry no order then; the class/key agreement falls
to chance -- tools/tests/test_freq.py and tools/tests/PREREG-TT-FREQ.md).

--kwic TOKEN --width W --sort left|right: every occurrence of TOKEN with W
tokens of context each side, one row per occurrence, sorted on the left
context (immediate left neighbour first, then outward) or the right context
(immediate right neighbour first).

--repeats N: every token n-gram of length >= N that recurs (two or more
times), for each length starting at N and increasing until a length has no
repeats at all; each row gives the n-gram, its count and its start
positions, then (TT-FREQ, 8 Oct 2026) the gaps between successive
positions (Tomokiyo polygram.htm, "Polygram Script": list every recurring
n-gram of length >= 10 and inspect it; the gaps are what a period or a
re-used formula shows up in). Lengths are grown by refining the previous
length's repeat groups by one following token, so each length costs
O(positions still repeating) and the whole run is not O(N * L^2): 20,000
tokens run in well under a few seconds (test_freq.py times it). Meant to
catch: a word or formula enciphered the same way twice. --maximal keeps only
repeats that cannot be extended left or right with the same positions (one
row per long repeated block instead of every sub-window; linear in the
block length). Must NOT flag: a length-N window that occurs once (the
fixture's "9 8 6"). When N <= 3, a separate "near-repeats" table follows: every pair
of length-3 windows that differ in exactly one of their three positions
(a Bazeries-style variably-spelled probable phrase), excluding exact
repeats (already in the table above).

--split-at N: reports token count, distinct count and index of coincidence
separately for the tokens below N and at-or-above N.

--split-at auto (TT-FREQ, 8 Oct 2026; Tomokiyo practice 1, LESSONS-TOMOKIYO.md
C1: codebreaking.htm "Cipher in Code"; wallisdecipher.htm "Cipher used in the
First Letter", "low numbers up to about 64 being reserved for single
letters"; ormonde.htm "Reduction of the Problem", letters in "the range from
40 to 90", nulls below 40, words above): PROPOSES N, the value where the
dense low letter band of a nomenclator ends. Counts per integer value over
the numeric range are fitted as piecewise-constant Poisson rates: (1) the
best single change point (low dense / high sparse, low-side rate must be the
higher), reported with the top 3 candidates and their log-likelihood gain
over one flat rate; (2) the best dense band [A, B) with sparse values on both
sides (nulls below a letter band, as on Ormonde); (3) the largest numeric gap
between successive distinct values. Each proposal prints the low block's
size (distinct values, tokens) and IC beside the high block's. Meant to
catch: a letter band of frequent, densely used low values under a sparse
code range. Must NOT flag (prints "no break" when the best gain is under
--split-min-gain, default 10 nats): values drawn uniformly over the range
(a shuffled-VALUE null), test_freq.py. A proposal is a hypothesis for
--split-at N, not a key.

--onepart-dict LANG (Tomokiyo codebreaking.htm "Partial Encoding", "Andre
Langie's Example"; LESSONS-TOMOKIYO.md C2): a one-part code lists its
vocabulary alphabetically, so a frequent group's numeric position within the
code's own range should fall in the initial-letter band a period
dictionary's headwords occupy at that same relative position. LANG is a
language key from tools/judge_plaintext.py's LANG_CORPORA (e.g. "fr18");
this option builds cumulative initial-letter bands (a-z) from the DISTINCT
folded word TYPES found in that corpus (a running-text corpus's raw word
TOKENS are dominated by a handful of function words -- BER-KWIC, 27 Sept
2026, found "je" alone at 3.8 pct of tokens in one sample -- so counting
distinct types is closer to a dictionary headword list, though still not
a real period dictionary's own page layout; see berthier-napoleon-1812
NOTES.md). Prints the a-z band table (letter, cumulative-fraction start,
end, distinct-type count) and then, for the --top N most frequent numeric
tokens in FILE, each one's relative position in --onepart-range MIN,MAX
(default: the file's own min/max numeric token) and the band it lands in.
This prints the band mapping only -- the hypothesis test (does the target
land more often in a band consistent with a chosen word list than a
shuffled-range control does, CLAUDE.md rule 3) is run by a separate script
that calls onepart_dict_bands()/band_for_frac() below, the same way
period_code_test.py sits beside this tool for a different family (see
ciphers/destaing-gerard-1779/onepart_test.py for a worked example).

--tail N (MQS-TAIL, 9 Oct 2026; Lasry, Biermann and Tomokiyo 2023, Cryptologia
47:2, pp.124-125 Fig. 12 and p.137 n.99: month, date, place and enclosure signs
form one positional class at the close of the Mary Stuart letters): FILE is a
POOL, one letter per non-blank, non-'#' line. Per sign, its count in the edge
window of every letter (--tail-end end: the last N tokens; start: the first N;
both: both) against a shuffled-letter-end null: each letter's window is swapped
for a random window of the same length elsewhere in the pool (a start whose
window avoids that letter's own edge windows), --tail-reps replicates
(default 2000, --tail-seed 1). Prints one TSV row per sign with total >=
--tail-min-total (default 2): rank, sign, total, edge count, null mean, null
p95, one-sided p, flag (edge > p95, edge >= 2, p <= 0.05), ranked by p then
excess. Meant to catch: dateline, place and sign-off signs that concentrate at
letter ends (Janssens 1811 pool, tools/tests/PREREG-MQS-TAIL.md). Must NOT
flag: the same pool with each letter shuffled in place (test_freq.py). A flag
says "positional class candidate", never a value; the Janssens dateline sits at
the HEAD of several letters, so try --tail-end both before reading a miss.
"""
import argparse
import math
import random
import re
import signal
import sys
from collections import Counter


def load_tokens(path, sep, strip_clear):
    lines = [l for l in open(path, encoding="utf-8", errors="replace") if not l.startswith("#")]
    toks = [t for t in re.split(sep, "".join(lines)) if t]
    if strip_clear:
        toks = [t for t in toks if re.search(r"\d", t)]
    return toks


def index_of_coincidence(toks):
    n = len(toks)
    if n <= 1:
        return 0.0
    c = Counter(toks)
    return sum(v * (v - 1) for v in c.values()) / (n * (n - 1))


def contacts_table(toks, k, tag_min=3, tag_threshold=0.4):
    """Return a list of dicts for the k most frequent tokens: token, count, pct,
    self_succession, tag, preceders (Counter), followers (Counter). See the
    module docstring for the exact tag rule."""
    n = len(toks)
    c = Counter(toks)
    rows = []
    for tok, cnt in c.most_common(k):
        idxs = [i for i, t in enumerate(toks) if t == tok]
        left = Counter(toks[i - 1] for i in idxs if i > 0)
        right = Counter(toks[i + 1] for i in idxs if i < n - 1)
        self_succ = sum(1 for i in idxs if i + 1 < n and toks[i + 1] == tok)
        tag = "neither"
        if cnt >= tag_min:
            left_total, right_total = sum(left.values()), sum(right.values())
            left_conc = max(left.values()) / left_total if left_total else 0.0
            right_conc = max(right.values()) / right_total if right_total else 0.0
            left_all_distinct = left_total > 0 and len(left) == left_total
            right_all_distinct = right_total > 0 and len(right) == right_total
            if left_conc >= tag_threshold and right_all_distinct:
                tag = "suffix-like"
            elif right_conc >= tag_threshold and left_all_distinct:
                tag = "prefix-like"
        rows.append({
            "token": tok, "count": cnt, "pct": 100 * cnt / n,
            "self_succession": self_succ, "tag": tag,
            "preceders": left, "followers": right,
        })
    return rows


def kwic_rows(toks, token, width, sort):
    idxs = [i for i, t in enumerate(toks) if t == token]
    rows = []
    for i in idxs:
        left = toks[max(0, i - width):i]
        right = toks[i + 1:i + 1 + width]
        rows.append({"pos": i, "left": left, "right": right})
    if sort == "left":
        rows.sort(key=lambda r: list(reversed(r["left"])))
    else:
        rows.sort(key=lambda r: r["right"])
    return rows


def ngram_repeats(toks, length):
    """distinct n-grams of this length occurring >=2 times, mapped to their start positions"""
    grams = {}
    for i in range(len(toks) - length + 1):
        g = tuple(toks[i:i + length])
        grams.setdefault(g, []).append(i)
    return {g: pos for g, pos in grams.items() if len(pos) >= 2}


def near_repeats_length3(toks):
    """pairs of (non-identical) length-3 windows differing in exactly one position"""
    grams = [(i, tuple(toks[i:i + 3])) for i in range(len(toks) - 2)]
    pairs = []
    seen = set()
    for a in range(len(grams)):
        i, ga = grams[a]
        for b in range(a + 1, len(grams)):
            j, gb = grams[b]
            if ga == gb:
                continue
            if sum(1 for x, y in zip(ga, gb) if x != y) == 1:
                key = (i, j)
                if key not in seen:
                    seen.add(key)
                    pairs.append((i, ga, j, gb))
    return pairs


def split_stats(toks, split_at):
    def side(sub):
        return {"tokens": len(sub), "distinct": len(set(sub)), "ic": index_of_coincidence(sub)}
    low = [t for t in toks if re.match(r"^\d+$", t) and int(t) < split_at]
    high = [t for t in toks if re.match(r"^\d+$", t) and int(t) >= split_at]
    return {"low": side(low), "high": side(high)}


def repeat_groups(toks, n_min, maximal=False):
    """[(length, positions)] for every repeated n-gram of length >= n_min, grown
    by refinement: a length-(L+1) group is a length-L group split by the token
    at offset L, so each length costs O(positions still repeating), never
    O(N * L) tuple building (TT-FREQ, 8 Oct 2026; polygram.htm). With
    maximal=True only left- and right-maximal repeats are kept, and a group
    that is not left-maximal (every occurrence preceded by the same token) is
    dropped at once with all its extensions, so one long repeated block costs
    O(L), not O(L^2)."""
    n = len(toks)
    if n_min < 1 or n_min > n:
        return []

    def left_max(pos):
        return pos[0] == 0 or len({toks[i - 1] for i in pos}) > 1

    groups = list(ngram_repeats(toks, n_min).values())
    if maximal:
        groups = [g for g in groups if left_max(g)]
    out = []
    length = n_min
    while groups:
        nxt = []
        for pos in groups:
            by = {}
            for i in pos:
                if i + length < n:
                    by.setdefault(toks[i + length], []).append(i)
            kids = [v for v in by.values() if len(v) >= 2]
            if maximal:
                if not any(len(k) == len(pos) for k in kids):
                    out.append((length, pos))
                nxt.extend(kids)
            else:
                out.append((length, pos))
                nxt.extend(kids)
        groups = nxt
        length += 1
    return out


def ngram_repeats_all(toks, n_min, maximal=False):
    """{length: {ngram tuple: [start positions]}} built from repeat_groups()."""
    out = {}
    for length, pos in repeat_groups(toks, n_min, maximal):
        out.setdefault(length, {})[tuple(toks[pos[0]:pos[0] + length])] = pos
    return out


def position_gaps(pos):
    return [b - a for a, b in zip(pos, pos[1:])]


def near_repeats_length3_fast(toks):
    """Same pairs, same order, as near_repeats_length3(), by masking one
    position at a time and bucketing (linear in N, not quadratic)."""
    grams = [tuple(toks[i:i + 3]) for i in range(len(toks) - 2)]
    found = set()
    for m in range(3):
        buckets = {}
        for i, g in enumerate(grams):
            buckets.setdefault(g[:m] + g[m + 1:], []).append(i)
        for idx in buckets.values():
            if len(idx) < 2:
                continue
            for a in range(len(idx)):
                for b in range(a + 1, len(idx)):
                    i, j = idx[a], idx[b]
                    if grams[i] != grams[j]:
                        found.add((i, j))
    return [(i, grams[i], j, grams[j]) for i, j in sorted(found)]


def _seg_ll(c, length):
    """Poisson log-likelihood (up to a data-only constant) of c events over
    `length` integer values at the MLE rate c/length."""
    if c <= 0 or length <= 0:
        return 0.0
    return c * math.log(c / length) - c


def split_auto(toks, min_side=5, top=3):
    """Proposed letter-band edges for --split-at auto (see the module
    docstring). Returns a dict: lo, hi, flat_ll, singles (list of
    (gain, N)), band ((gain, A, B) or None), gap ((size, below, above) or
    None). N/A/B are integer values: low block = values < N."""
    vals = [int(t) for t in toks if re.match(r"^\d+$", t)]
    res = {"lo": None, "hi": None, "singles": [], "band": None, "gap": None, "n": len(vals)}
    if len(vals) < 2:
        return res
    c = Counter(vals)
    lo, hi = min(vals), max(vals)
    res["lo"], res["hi"] = lo, hi
    distinct = sorted(c)
    # prefix sums over distinct values; a boundary is "values < d" for d in distinct
    cum = [0]
    for d in distinct:
        cum.append(cum[-1] + c[d])
    total = cum[-1]
    flat = _seg_ll(total, hi - lo + 1)
    res["flat_ll"] = flat
    singles = []
    for k in range(min_side, len(distinct) - min_side + 1):
        nb = distinct[k]
        cl, ch = cum[k], total - cum[k]
        ll_, lh_ = nb - lo, hi - nb + 1
        if cl / ll_ <= ch / lh_:
            continue
        singles.append((_seg_ll(cl, ll_) + _seg_ll(ch, lh_) - flat, nb))
    singles.sort(reverse=True)
    res["singles"] = singles[:top]
    best_band = None
    D = len(distinct)
    for a in range(0, D - min_side + 1):
        A = distinct[a]
        for b in range(a + min_side, D + 1):
            B = distinct[b] if b < D else hi + 1
            cm = cum[b] - cum[a]
            cl, ch = cum[a], total - cum[b]
            lm, ll_, lh_ = B - A, A - lo, hi + 1 - B
            rm = cm / lm
            if (ll_ and cl / ll_ >= rm) or (lh_ and ch / lh_ >= rm):
                continue
            g = _seg_ll(cl, ll_) + _seg_ll(cm, lm) + _seg_ll(ch, lh_) - flat
            if best_band is None or g > best_band[0]:
                best_band = (g, A, B)
    res["band"] = best_band
    gaps = [(distinct[i + 1] - distinct[i], distinct[i], distinct[i + 1]) for i in range(D - 1)]
    if gaps:
        res["gap"] = max(gaps)
    return res


FOLD_ACCENTS = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss", "é": "e", "è": "e", "ê": "e", "à": "a",
                               "ç": "c", "ù": "u", "û": "u", "î": "i", "ô": "o", "â": "a", "ë": "e", "ï": "i",
                               "á": "a", "ã": "a", "í": "i", "ó": "o", "õ": "o", "ú": "u", "ñ": "n"})


def fold_word(w):
    """lowercase, fold accents to plain a-z, drop anything else -- same convention as
    tools/judge_plaintext.py's fold(), duplicated here so this module has no import-time
    dependency on it (see the --onepart-dict docstring)."""
    w = w.lower().translate(FOLD_ACCENTS)
    return re.sub(r"[^a-z]", "", w)


def word_type_bands(texts):
    """Cumulative initial-letter (a-z) bands over the DISTINCT folded word TYPES found in
    texts (an iterable of raw strings). Returns (bands, total) where bands is a list of
    (letter, start_frac, end_frac) covering [0,1) in alphabetical order, and total is the
    number of distinct types found. A one-part code lists entries in this same alphabetical
    order, so a group's relative position in the code's numeric range should fall in the
    band its intended word's initial letter occupies here (Langie/Mansfield, LESSONS-
    TOMOKIYO.md C2)."""
    types = set()
    for t in texts:
        for w in re.findall(r"[A-Za-zÀ-ÿ]+", t):
            fw = fold_word(w)
            if fw:
                types.add(fw)
    counts = Counter(w[0] for w in types)
    total = len(types)
    bands = []
    cum = 0
    for letter in "abcdefghijklmnopqrstuvwxyz":
        start = cum / total if total else 0.0
        cum += counts.get(letter, 0)
        end = cum / total if total else 0.0
        bands.append((letter, start, end))
    return bands, total


def band_for_frac(bands, frac):
    """The letter whose cumulative band [start, end) contains frac (clamped to [0, 1))."""
    frac = min(max(frac, 0.0), 0.999999)
    for letter, start, end in bands:
        if start <= frac < end:
            return letter
    return bands[-1][0]


def onepart_dict_bands(lang):
    """word_type_bands() built from tools/judge_plaintext.py's LANG_CORPORA[lang] (gzip-aware).
    Imported lazily so a caller that never uses --onepart-dict pays no cost and no other
    freq.py option depends on judge_plaintext.py existing."""
    import gzip
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from judge_plaintext import LANG_CORPORA  # noqa: E402
    paths = LANG_CORPORA.get(lang)
    if not paths:
        raise SystemExit(f"--onepart-dict: no corpus for language {lang!r} in "
                          f"tools/judge_plaintext.py's LANG_CORPORA")
    texts = []
    for p in paths:
        p = Path(p)
        if p.suffix == ".gz":
            texts.append(gzip.open(p, "rt", encoding="utf-8", errors="replace").read())
        else:
            texts.append(p.read_text(encoding="utf-8", errors="replace"))
    return word_type_bands(texts)


def print_onepart(toks, lang, top_n, rng):
    bands, total = onepart_dict_bands(lang)
    print(f"# onepart-dict {lang}: {total} distinct word types, bands a-z "
          f"(cumulative fraction of distinct types)")
    print("letter\tstart\tend")
    for letter, start, end in bands:
        print(f"{letter}\t{start:.4f}\t{end:.4f}")
    print()
    nums = [t for t in toks if re.match(r"^\d+$", t)]
    if rng:
        lo, hi = rng
    else:
        vals = [int(t) for t in nums]
        lo, hi = (min(vals), max(vals)) if vals else (0, 1)
    c = Counter(nums)
    print(f"# range {lo}-{hi}")
    print("token\tcount\tfrac\tband")
    for tok, cnt in c.most_common(top_n):
        v = int(tok)
        frac = (v - lo) / (hi - lo) if hi > lo else 0.0
        band = band_for_frac(bands, frac)
        print(f"{tok}\t{cnt}\t{frac:.4f}\t{band}")


def print_contacts(toks, k, tag_min, tag_threshold):
    print("token\tcount\tpct\tself_succession\ttag\tpreceders\tfollowers")
    for r in contacts_table(toks, k, tag_min, tag_threshold):
        pre = ";".join(f"{t}:{ct}" for t, ct in r["preceders"].most_common())
        fol = ";".join(f"{t}:{ct}" for t, ct in r["followers"].most_common())
        print(f"{r['token']}\t{r['count']}\t{r['pct']:.1f}\t{r['self_succession']}\t{r['tag']}\t{pre}\t{fol}")


def sukhotin_classes(toks, k):
    """Sukhotin's vowel algorithm on the contact matrix of the k most frequent
    tokens (symmetric adjacency, diagonal zeroed). Returns [(token, 'V'|'C',
    row_sum_at_promotion_or_final)] in frequency order (TT-FREQ, 8 Oct 2026;
    contact.htm, ormonde.htm "Contact Chart and First Findings")."""
    top = [t for t, _ in Counter(toks).most_common(k)]
    ix = {t: i for i, t in enumerate(top)}
    m = [[0] * len(top) for _ in top]
    for a, b in zip(toks, toks[1:]):
        if a in ix and b in ix and a != b:
            m[ix[a]][ix[b]] += 1
            m[ix[b]][ix[a]] += 1
    sums = [sum(r) for r in m]
    cls = ["C"] * len(top)
    when = list(sums)
    while True:
        cand = [i for i in range(len(top)) if cls[i] == "C"]
        if not cand:
            break
        i = max(cand, key=lambda j: sums[j])
        if sums[i] <= 0:
            break
        cls[i] = "V"
        when[i] = sums[i]
        for j in range(len(top)):
            if cls[j] == "C":
                sums[j] -= 2 * m[j][i]
    return [(top[i], cls[i], when[i]) for i in range(len(top))]


def print_vowels(toks, k):
    print("token\tsukhotin_class\tcontact_sum")
    for t, c, w in sukhotin_classes(toks, k):
        print(f"{t}\t{c}\t{w}")


def print_kwic(toks, token, width, sort):
    print("pos\tleft_context\ttoken\tright_context")
    for r in kwic_rows(toks, token, width, sort):
        print(f"{r['pos']}\t{' '.join(r['left'])}\t{token}\t{' '.join(r['right'])}")


def print_repeats(toks, n_min, maximal=False):
    print("length\tngram\tcount\tpositions\tgaps")
    allr = ngram_repeats_all(toks, n_min, maximal)
    for length in sorted(allr):
        reps = allr[length]
        for g, pos in sorted(reps.items(), key=lambda kv: (-len(kv[1]), kv[0])):
            print(f"{length}\t{' '.join(g)}\t{len(pos)}\t{','.join(map(str, pos))}\t"
                  f"{','.join(map(str, position_gaps(pos)))}")
    if not allr:
        print(f"(no recurring {n_min}-gram or longer found)")
    if n_min <= 3:
        print("\nnear-repeats (length 3, differ in exactly one position):")
        near = near_repeats_length3_fast(toks)
        if not near:
            print("(none)")
        for i, ga, j, gb in near:
            print(f"{i}\t{' '.join(ga)}\t~\t{j}\t{' '.join(gb)}")


def print_split(toks, split_at):
    s = split_stats(toks, split_at)
    print(f"split at {split_at}")
    print("side\ttokens\tdistinct\tIC")
    print(f"low(<{split_at})\t{s['low']['tokens']}\t{s['low']['distinct']}\t{s['low']['ic']:.4f}")
    print(f"high(>={split_at})\t{s['high']['tokens']}\t{s['high']['distinct']}\t{s['high']['ic']:.4f}")


def print_split_auto(toks, min_gain, min_side):
    r = split_auto(toks, min_side=min_side)
    if r["lo"] is None:
        print("split auto: fewer than 2 numeric tokens")
        return None
    print(f"split auto: {r['n']} numeric tokens, range {r['lo']}..{r['hi']}")
    print("kind\tN\tgain_nats\tlow_distinct\tlow_tokens\tlow_IC\thigh_distinct\thigh_tokens\thigh_IC")
    rows = [("single", g, n) for g, n in r["singles"]]
    if r["band"]:
        g, A, B = r["band"]
        rows.append((f"band[{A},{B})", g, B))
    if r["gap"]:
        size, below, above = r["gap"]
        rows.append((f"gap{size}({below}|{above})", float("nan"), above))
    for kind, g, n in rows:
        s = split_stats(toks, n)
        print(f"{kind}\t{n}\t{g:.1f}\t{s['low']['distinct']}\t{s['low']['tokens']}\t{s['low']['ic']:.4f}\t"
              f"{s['high']['distinct']}\t{s['high']['tokens']}\t{s['high']['ic']:.4f}")
    best = r["singles"][0] if r["singles"] else None
    if best is None or best[0] < min_gain:
        print(f"proposal: no break (best single-split gain {best[0] if best else 0:.1f} < {min_gain})")
        return None
    print(f"proposal: N = {best[1]} (best single split, gain {best[0]:.1f} nats)")
    return best[1]


def load_pool(path, sep, strip_clear):
    """One letter per non-blank, non-'#' line; returns a list of token lists."""
    letters = []
    for line in open(path, encoding="utf-8", errors="replace"):
        if line.startswith("#") or not line.strip():
            continue
        toks = [t for t in re.split(sep, line) if t]
        if strip_clear:
            toks = [t for t in toks if re.search(r"\d", t)]
        if toks:
            letters.append(toks)
    return letters


def _edge_spans(length, n, end):
    """(start, stop) windows of letter positions counted as its edge."""
    w = min(n, length)
    if end == "end":
        return [(length - w, length)]
    if end == "start":
        return [(0, w)]
    if length <= 2 * n:
        return [(0, length)]
    return [(0, n), (length - n, length)]


def tail_stats(letters, n, end="end", reps=2000, seed=1, min_total=2):
    """Edge-window count per sign vs the shuffled-letter-end null (see --tail in the docstring).

    Returns rows (sign, total, obs, null_mean, null_p95, p, flag) sorted by p then excess."""
    rng = random.Random(seed)
    total = Counter(t for L in letters for t in L)
    obs = Counter()
    spans = [_edge_spans(len(L), n, end) for L in letters]
    for L, sp in zip(letters, spans):
        for a, b in sp:
            obs.update(L[a:b])
    # candidate null starts per window length: (letter, start) whose window avoids that letter's edges
    cand = {}
    def starts_for(w):
        if w not in cand:
            c = []
            for j, L in enumerate(letters):
                for st in range(0, len(L) - w + 1):
                    if all(st + w <= a or st >= b for a, b in spans[j]):
                        c.append((j, st))
            if not c:  # pool too short to avoid edges: fall back to any window
                c = [(j, st) for j, L in enumerate(letters) for st in range(0, len(L) - w + 1)]
            cand[w] = c
        return cand[w]
    widths = [b - a for sp in spans for a, b in sp]
    signs = [s for s, k in total.items() if k >= min_total]
    sidx = {s: i for i, s in enumerate(signs)}
    null = [[0] * reps for _ in signs]
    for r in range(reps):
        cnt = Counter()
        for w in widths:
            j, st = rng.choice(starts_for(w))
            cnt.update(letters[j][st:st + w])
        for s, k in cnt.items():
            i = sidx.get(s)
            if i is not None:
                null[i][r] = k
    rows = []
    for s in signs:
        v = sorted(null[sidx[s]])
        o = obs.get(s, 0)
        mean = sum(v) / reps
        p95 = v[min(reps - 1, int(math.ceil(0.95 * reps)) - 1)]
        p = sum(1 for x in v if x >= o) / reps
        flag = o > p95 and o >= 2 and p <= 0.05
        rows.append((s, total[s], o, mean, p95, p, flag))
    rows.sort(key=lambda r: (r[5], -(r[2] - r[3]), r[0]))
    return rows


def print_tail(letters, n, end, reps, seed, min_total, top):
    rows = tail_stats(letters, n, end, reps, seed, min_total)
    print(f"# --tail {n} --tail-end {end}: {len(letters)} letters, {sum(len(L) for L in letters)} tokens, "
          f"reps {reps}, seed {seed}; flagged {sum(1 for r in rows if r[6])} of {len(rows)} signs tested")
    print("rank\tsign\ttotal\tedge\tnull_mean\tnull_p95\tp\tflag")
    for i, (s, t, o, m, q, p, f) in enumerate(rows[:top] if top else rows, 1):
        print(f"{i}\t{s}\t{t}\t{o}\t{m:.2f}\t{q}\t{p:.4f}\t{'FLAG' if f else ''}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--sep", default=r"[;\s]+", help="regex used to split tokens")
    ap.add_argument("--top", type=int, default=25)
    ap.add_argument("--strip-clear", action="store_true")
    ap.add_argument("--contacts", type=int, metavar="K",
                     help="contact table of the K most frequent tokens, left/right neighbour counts "
                          "(Tomokiyo practice 5: contact.htm, kwic.htm, codebreaking.htm 'Statistical Analysis')")
    ap.add_argument("--kwic", metavar="TOKEN", help="KWIC listing of every occurrence of TOKEN (Tomokiyo practice 5: kwic.htm 'Sorting a KWIC Index')")
    ap.add_argument("--width", type=int, default=5, help="KWIC context width, tokens each side (default 5)")
    ap.add_argument("--sort", choices=["left", "right"], default="left", help="KWIC sort key (default left)")
    ap.add_argument("--repeats", type=int, metavar="N", help="recurring token n-grams of length >= N, with positions and gaps "
                          "(Tomokiyo practice 6: polygram.htm 'Polygram Script')")
    ap.add_argument("--split-at", dest="split_at", metavar="N|auto",
                     help="report token/distinct/IC separately for groups < N and >= N; 'auto' proposes N "
                          "(Tomokiyo practice 1: codebreaking.htm 'Cipher in Code', wallisdecipher.htm, ormonde.htm)")
    ap.add_argument("--split-min-gain", type=float, default=10.0, dest="split_min_gain",
                     help="--split-at auto: min log-likelihood gain (nats) to propose a break (default 10)")
    ap.add_argument("--split-min-side", type=int, default=5, dest="split_min_side",
                     help="--split-at auto: min distinct values on each side (default 5)")
    ap.add_argument("--maximal", action="store_true",
                     help="with --repeats N: list only maximal repeats (not extendable left or right with the same "
                          "positions); use on long texts with long repeated blocks")
    ap.add_argument("--vowels", action="store_true",
                     help="with --contacts K: Sukhotin vowel/consonant class of the K top tokens from contacts "
                          "(Tomokiyo contact.htm; ormonde.htm 'Contact Chart and First Findings')")
    ap.add_argument("--tag-min", type=int, default=3, dest="tag_min",
                     help="min count for a --contacts prefix/suffix-like tag (default 3)")
    ap.add_argument("--tag-threshold", type=float, default=0.4, dest="tag_threshold",
                     help="context-concentration threshold for a --contacts tag (default 0.4)")
    ap.add_argument("--onepart-dict", metavar="LANG", dest="onepart_dict",
                     help="map --top frequent tokens' range position to a LANG period-vocabulary initial-letter band")
    ap.add_argument("--onepart-range", metavar="MIN,MAX", dest="onepart_range",
                     help="value range for --onepart-dict position mapping (default: file's own min/max numeric token)")
    ap.add_argument("--tail", type=int, metavar="N",
                     help="POOL mode (one letter per line): rank signs concentrated in the last N tokens of each "
                          "letter against a shuffled-letter-end null (MQS-TAIL; Lasry, Biermann and Tomokiyo 2023 Fig. 12)")
    ap.add_argument("--tail-end", choices=["end", "start", "both"], default="end", dest="tail_end",
                     help="--tail: which edge of each letter is counted (default end)")
    ap.add_argument("--tail-reps", type=int, default=2000, dest="tail_reps", help="--tail: null replicates (default 2000)")
    ap.add_argument("--tail-seed", type=int, default=1, dest="tail_seed", help="--tail: null seed (default 1)")
    ap.add_argument("--tail-min-total", type=int, default=2, dest="tail_min_total",
                     help="--tail: list signs with at least this many pool occurrences (default 2)")
    a = ap.parse_args()

    if a.tail:
        letters = load_pool(a.file, a.sep, a.strip_clear)
        print_tail(letters, a.tail, a.tail_end, a.tail_reps, a.tail_seed, a.tail_min_total,
                   a.top if a.top != 25 else 0)
        return

    toks = load_tokens(a.file, a.sep, a.strip_clear)

    did_new = False
    if a.contacts:
        print_contacts(toks, a.contacts, a.tag_min, a.tag_threshold)
        if a.vowels:
            print()
            print_vowels(toks, a.contacts)
        did_new = True
    if a.kwic is not None:
        if did_new:
            print()
        print_kwic(toks, a.kwic, a.width, a.sort)
        did_new = True
    if a.repeats:
        if did_new:
            print()
        print_repeats(toks, a.repeats, a.maximal)
        did_new = True
    if a.split_at is not None:
        if did_new:
            print()
        if a.split_at == "auto":
            print_split_auto(toks, a.split_min_gain, a.split_min_side)
        else:
            try:
                n_split = int(a.split_at)
            except ValueError:
                ap.error("--split-at takes an integer or 'auto'")
            print_split(toks, n_split)
        did_new = True
    if a.onepart_dict:
        if did_new:
            print()
        rng = None
        if a.onepart_range:
            lo_s, hi_s = a.onepart_range.split(",")
            rng = (int(lo_s), int(hi_s))
        print_onepart(toks, a.onepart_dict, a.top, rng)
        did_new = True
    if did_new:
        return

    n = len(toks)
    c = Counter(toks)
    print(f"tokens: {n}   distinct: {len(c)}")
    if n > 1:
        ic = index_of_coincidence(toks)
        print(f"index of coincidence: {ic:.4f}   (flat over {len(c)} symbols = {1/len(c):.4f})")
    nums = [int(m.group()) for t in toks for m in [re.match(r"\d+", t)] if m]
    if nums:
        print(f"numeric range: {min(nums)}..{max(nums)}")
        widths = Counter(len(str(x)) for x in nums)
        print("digit widths: " + ", ".join(f"{w}-digit={k}" for w, k in sorted(widths.items())))

    print(f"\ntop {a.top} tokens:")
    for t, k in c.most_common(a.top):
        print(f"  {t:>8}  {k:4d}  {100*k/n:5.1f}%")

    bg = Counter(zip(toks, toks[1:]))
    rep = [(p, k) for p, k in bg.most_common(a.top) if k > 1]
    if rep:
        print(f"\nrepeated bigrams:")
        for (x, y), k in rep:
            print(f"  {x} {y}  x{k}")

    once = sum(1 for v in c.values() if v == 1)
    print(f"\nhapax (seen once): {once} of {len(c)} distinct")


if __name__ == "__main__":
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    main()
