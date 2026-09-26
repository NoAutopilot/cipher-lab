#!/usr/bin/env python3
"""Local key repair: for each code in a substitution key, in order of frequency in a given
ciphertext, try replacing its value with a single letter, NULL, or a common French bigram/trigram,
and keep whichever choice most improves an order-5 character n-gram model's total log-probability
of the whole decoded stream (clear words kept as fixed context, other codes at their current
working value). Sweeps rounds until nothing changes or --rounds is reached. Deterministic: no
randomness anywhere -- codes are visited most-frequent-first (ties broken by code string), candidate
values are tried in a fixed order (current value first, then letters, NULL, bigrams, trigrams), and
a tie between two candidate scores keeps whichever was tried first (never overwrites a strictly-equal
score), so a re-run on unchanged inputs reproduces the same key byte for byte.

Written 26 Sept 2026 for LANE AX2's AX2-4612S job brief (H-S: a few of key_full.tsv's rare-letter
codes might stand for a two-letter French syllable, or a different letter, instead of the letter
key_full.tsv currently gives them -- lodewijk-van-nassau-1573-74's 4612/5799).

  python3 tools/key_repair.py CIPHERTEXT.tsv --key KEY.tsv --out-key REPAIRED.tsv
      [--out-reading reading.txt] [--out-changes changes.tsv] [--margin 3.0] [--rounds 4]
      [--clear-prefix =] [--nonsign '[blank],[blot],[spot]'] [--bigrams 60] [--trigrams 20]
      [--letters abcdefghijklmnopqrstuvwxyz]

Ciphertext is read with tools/decode_key.py's own format-detecting loaders (pipe/tsv/rows), so any
ciphertext.tsv already used by decode_key.py works unchanged. The key TSV is read with
tools/decode_key.py's load_key (code[/sign/token], value[/letter/word_or_phrase], optional grade,
source, note). A code present in the key but never occurring in this ciphertext is left untouched
(repairing it would have zero effect on this file's score, so it never crosses --margin).

The n-gram model is tools/french16_ngram.py's order-5 Witten-Bell model by default (--ngram-module
to reuse this tool for another language's corpus module built the same way, e.g. german_ngram.py);
its own fold() (accents stripped, uppercase, J->I, U->V, W->VV) is applied to every letter before
scoring, matching tools/word_share_check*.py's convention, so a manuscript's period 'u'/'v' spelling
distinction in the key survives into the repaired key TSV even though the model itself folds them
together for scoring.

Output: a changes table (code, count, old, new, gain) to stdout and --out-changes; the repaired key
TSV (--out-key, same columns as the input key, every changed row's grade set to S and its source/note
naming this tool's gain, unchanged rows byte-identical to the input); the final decoded stream
(--out-reading, one line, the same concatenation the model itself scored -- not a target's own graded
reading.txt/tokens.tsv, which tools/decode_key.py generates separately from the repaired key TSV).
"""
import argparse
import csv
import functools
import os
import sys
import unicodedata
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import decode_key as dk  # noqa: E402

ALPHA26 = "abcdefghijklmnopqrstuvwxyz"


def fold(s):
    """Same convention as tools/french16_ngram.py's fold(): NFD-strip accents, uppercase, J->I,
    U->V, W->VV. Cached: candidate values and clear words repeat heavily across the sweep."""
    s = unicodedata.normalize("NFD", s)
    s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn").upper()
    s = s.replace("J", "I").replace("U", "V").replace("W", "VV")
    return s


fold = functools.lru_cache(maxsize=None)(fold)


def corpus_ngrams(words, n, top):
    """Most frequent n-length substrings of the folded, concatenated corpus text -- the same
    concatenation (no word-boundary marker) the character model itself is trained on. Ties broken
    alphabetically so the result is deterministic across runs and Python hash seeds."""
    text = "".join(fold(w) for w in words)
    counts = Counter(text[i : i + n] for i in range(len(text) - n + 1))
    ranked = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return [g.lower() for g, _ in ranked[:top]]


def load_ciphertext(path, clear_prefix, nonsign):
    job = dict(clear_prefix=clear_prefix, nonsign=nonsign)
    fmt = dk.detect_format(path)
    return dk.LOADERS[fmt](path, job)


def code_counts(recs):
    c = Counter()
    for r in recs:
        if r["kind"] == "sign":
            c[r["sign"]] += 1
    return c


def is_absent(val):
    return not val or val.upper() == "NULL" or val == "?"


def build_template(recs):
    """Fixed folded fragments for clear/dot/line rows, computed once; a ('sign', code) marker for
    every repairable position, resolved against the current working values on every stream build."""
    template = []
    for r in recs:
        if r["kind"] == "clear":
            w = dk.clear_word(r["raw"])
            template.append(("fixed", fold(w)))
        elif r["kind"] == "sign":
            template.append(("sign", r["sign"]))
        # 'dot' and 'line' rows contribute nothing to the decoded stream
    return template


def build_stream(template, values):
    parts = []
    for kind, data in template:
        if kind == "fixed":
            parts.append(data)
        else:
            val = values.get(data)
            if is_absent(val):
                continue
            parts.append(fold(val))
    return "".join(parts)


def candidate_values(letters, bigrams, trigrams):
    seen, out = set(), []
    for v in list(letters) + ["NULL"] + list(bigrams) + list(trigrams):
        if v not in seen:
            seen.add(v)
            out.append(v)
    return out


def repair(template, key, model, margin, rounds, cand_values):
    """Greedy per-code local search. Returns (final values dict, changes list of
    (code, count, old, new, gain), rounds actually run)."""
    counts = Counter(data for kind, data in template if kind == "sign")
    codes_by_freq = sorted((c for c in counts if c in key), key=lambda c: (-counts[c], c))
    values = {c: key[c]["value"] for c in key}
    changes = []
    rounds_run = 0
    for _ in range(rounds):
        rounds_run += 1
        any_change = False
        for code in codes_by_freq:
            cur = values[code]
            base_score = model.logp(build_stream(template, values))
            best_val, best_score = cur, base_score
            for cand in cand_values:
                if cand == cur:
                    continue
                values[code] = cand
                s = model.logp(build_stream(template, values))
                values[code] = cur
                if s > best_score:
                    best_score, best_val = s, cand
            gain = best_score - base_score
            if best_val != cur and gain > margin:
                values[code] = best_val
                changes.append((code, counts[code], cur, best_val, gain))
                any_change = True
        if not any_change:
            break
    return values, changes, rounds_run


def write_key(path, key, values, changes, tool_note_prefix="key_repair.py"):
    changed = {code: (old, new, gain) for code, count, old, new, gain in changes}
    codes = list(key)
    fieldnames = ["code", "value", "grade", "source", "note"]
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(fieldnames)
        for code in codes:
            row = key[code]
            value = values.get(code, row["value"])
            if code in changed:
                old, new, gain = changed[code]
                w.writerow([code, value, "S", tool_note_prefix,
                            f"{old!r} -> {new!r}, gain {gain:.2f}"])
            else:
                w.writerow([code, value, row.get("grade") or "", row.get("source") or "",
                            row.get("note") or ""])


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ciphertext")
    ap.add_argument("--key", required=True)
    ap.add_argument("--out-key", required=True)
    ap.add_argument("--out-reading")
    ap.add_argument("--out-changes")
    ap.add_argument("--margin", type=float, default=3.0, help="minimum score gain to accept a change (default 3.0)")
    ap.add_argument("--rounds", type=int, default=4)
    ap.add_argument("--clear-prefix", default="=")
    ap.add_argument("--nonsign", default="[blank],[blot],[spot]")
    ap.add_argument("--letters", default=ALPHA26)
    ap.add_argument("--bigrams", type=int, default=60)
    ap.add_argument("--trigrams", type=int, default=20)
    ap.add_argument("--ngram-module", default="french16_ngram")
    a = ap.parse_args(argv)

    nonsign = [x for x in a.nonsign.split(",") if x]
    recs = load_ciphertext(a.ciphertext, a.clear_prefix, nonsign)
    template = build_template(recs)
    key = dk.load_key(a.key)

    ngram = __import__(a.ngram_module)
    model = ngram.load()
    corpus_words = list(ngram.corpus_words()) if hasattr(ngram, "corpus_words") else list(model.words.elements())
    bigrams = corpus_ngrams(corpus_words, 2, a.bigrams)
    trigrams = corpus_ngrams(corpus_words, 3, a.trigrams)
    cand_values = candidate_values(a.letters, bigrams, trigrams)

    values, changes, rounds_run = repair(template, key, model, a.margin, a.rounds, cand_values)

    print(f"{len(changes)} change(s) over {rounds_run} round(s) (margin {a.margin}, "
          f"{len(cand_values)} candidate values: {len(a.letters)} letters + NULL + "
          f"{len(bigrams)} bigrams + {len(trigrams)} trigrams)")
    print("code\tcount\told\tnew\tgain")
    for code, count, old, new, gain in changes:
        print(f"{code}\t{count}\t{old}\t{new}\t{gain:.3f}")

    if a.out_changes:
        with open(a.out_changes, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, delimiter="\t", lineterminator="\n")
            w.writerow(["code", "count", "old", "new", "gain"])
            for code, count, old, new, gain in changes:
                w.writerow([code, count, old, new, f"{gain:.3f}"])

    write_key(a.out_key, key, values, changes)

    if a.out_reading:
        with open(a.out_reading, "w", encoding="utf-8") as f:
            f.write(build_stream(template, values) + "\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
