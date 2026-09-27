#!/usr/bin/env python3
"""Token frequency analysis for a ciphertext file.

Usage: python3 tools/freq.py FILE [--sep REGEX] [--top N] [--strip-clear]
       python3 tools/freq.py FILE --contacts K
       python3 tools/freq.py FILE --kwic TOKEN [--width W] [--sort left|right]
       python3 tools/freq.py FILE --repeats N
       python3 tools/freq.py FILE --split-at N

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

--kwic TOKEN --width W --sort left|right: every occurrence of TOKEN with W
tokens of context each side, one row per occurrence, sorted on the left
context (immediate left neighbour first, then outward) or the right context
(immediate right neighbour first).

--repeats N: every token n-gram of length >= N that recurs (two or more
times), for each length starting at N and increasing until a length has no
repeats at all; each row gives the n-gram, its count and its start
positions. When N <= 3, a separate "near-repeats" table follows: every pair
of length-3 windows that differ in exactly one of their three positions
(a Bazeries-style variably-spelled probable phrase), excluding exact
repeats (already in the table above).

--split-at N: the lowest gap in the sorted distinct numeric values is found
by eye/a one-off script (not automated here -- see LESSONS-TOMOKIYO.md C1);
this option takes that N and reports token count, distinct count and index
of coincidence separately for the tokens below N and at-or-above N.
"""
import argparse
import re
import signal
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


def print_contacts(toks, k, tag_min, tag_threshold):
    print("token\tcount\tpct\tself_succession\ttag\tpreceders\tfollowers")
    for r in contacts_table(toks, k, tag_min, tag_threshold):
        pre = ";".join(f"{t}:{ct}" for t, ct in r["preceders"].most_common())
        fol = ";".join(f"{t}:{ct}" for t, ct in r["followers"].most_common())
        print(f"{r['token']}\t{r['count']}\t{r['pct']:.1f}\t{r['self_succession']}\t{r['tag']}\t{pre}\t{fol}")


def print_kwic(toks, token, width, sort):
    print("pos\tleft_context\ttoken\tright_context")
    for r in kwic_rows(toks, token, width, sort):
        print(f"{r['pos']}\t{' '.join(r['left'])}\t{token}\t{' '.join(r['right'])}")


def print_repeats(toks, n_min):
    print("length\tngram\tcount\tpositions")
    length = n_min
    any_found = False
    while True:
        reps = ngram_repeats(toks, length)
        if not reps:
            break
        any_found = True
        for g, pos in sorted(reps.items(), key=lambda kv: (-len(kv[1]), kv[0])):
            print(f"{length}\t{' '.join(g)}\t{len(pos)}\t{','.join(map(str, pos))}")
        length += 1
    if not any_found:
        print(f"(no recurring {n_min}-gram or longer found)")
    if n_min <= 3:
        print("\nnear-repeats (length 3, differ in exactly one position):")
        near = near_repeats_length3(toks)
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--sep", default=r"[;\s]+", help="regex used to split tokens")
    ap.add_argument("--top", type=int, default=25)
    ap.add_argument("--strip-clear", action="store_true")
    ap.add_argument("--contacts", type=int, metavar="K", help="contact table of the K most frequent tokens")
    ap.add_argument("--kwic", metavar="TOKEN", help="KWIC listing of every occurrence of TOKEN")
    ap.add_argument("--width", type=int, default=5, help="KWIC context width, tokens each side (default 5)")
    ap.add_argument("--sort", choices=["left", "right"], default="left", help="KWIC sort key (default left)")
    ap.add_argument("--repeats", type=int, metavar="N", help="recurring token n-grams of length >= N, with positions")
    ap.add_argument("--split-at", type=int, dest="split_at", metavar="N",
                     help="report token/distinct/IC separately for groups < N and >= N")
    ap.add_argument("--tag-min", type=int, default=3, dest="tag_min",
                     help="min count for a --contacts prefix/suffix-like tag (default 3)")
    ap.add_argument("--tag-threshold", type=float, default=0.4, dest="tag_threshold",
                     help="context-concentration threshold for a --contacts tag (default 0.4)")
    a = ap.parse_args()

    toks = load_tokens(a.file, a.sep, a.strip_clear)

    did_new = False
    if a.contacts:
        print_contacts(toks, a.contacts, a.tag_min, a.tag_threshold)
        did_new = True
    if a.kwic is not None:
        if did_new:
            print()
        print_kwic(toks, a.kwic, a.width, a.sort)
        did_new = True
    if a.repeats:
        if did_new:
            print()
        print_repeats(toks, a.repeats)
        did_new = True
    if a.split_at is not None:
        if did_new:
            print()
        print_split(toks, a.split_at)
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
