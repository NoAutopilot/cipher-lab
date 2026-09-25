#!/usr/bin/env python3
"""yogtze-1984 cheap test 1: acrostic/initialism feasibility search.

Target: the 6 letters Y-O-G-T-Z-E (the word Stoll wrote, per Cipherbrain post 21) read as the
initials of a six-word phrase he might have blurted out ("Jetzt geht mir ein Licht auf!").

At N=6 (below any unicity, spec's own constraints.unicity_note) there is no statistical
cryptanalysis to run. This is a lexical feasibility check: for each of the six required initial
letters, how many candidate words does a real-language wordlist actually offer? A letter with
zero or very few candidate words makes an acrostic in that language implausible on its face,
independent of whether any particular phrase is "found" -- no phrase produced here is a reading
(brief instruction).

Per the LANE B3 brief (2026-09-25-lane-b3-yogtze-1984.md): the control is the same statistic
computed for 20 random 6-letter strings drawn from the same language's word-initial-letter
frequency distribution, using the same wordlist and the same search. Two languages are run
(German -- Stoll's own language and the language of his utterance; English -- the spec's named
control comparison), each against its own random-string control, never cross-language.

Wordlists: built from the same corpora tools/judge_plaintext.py's LANG_CORPORA already vets as
real, unrelated prose (never a target's own reading) -- tools/data/de20 (1880-1940 German,
closer in period to 1984 than the wired de16 Early New High German default) and
tools/data/pg1661_holmes.txt + pg2701_mobydick.txt (19th-c. English). A word list is the set of
distinct alphabetic tokens (lowercased) with length >= 2, so single-letter tokens and punctuation
do not inflate counts.
"""
import argparse
import collections
import gzip
import json
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TARGET = "YOGTZE"

WORD_RE_DE = re.compile(r"[a-zA-ZäöüÄÖÜß]+")
WORD_RE_EN = re.compile(r"[a-zA-Z]+")


def load_de20_text():
    de20 = ROOT / "tools" / "data" / "de20"
    chunks = []
    for gz in sorted(de20.glob("*.txt.gz")):
        with gzip.open(gz, "rt", encoding="utf-8", errors="replace") as fh:
            chunks.append(fh.read())
    return "\n".join(chunks)


def load_en_text():
    chunks = []
    for name in ("pg1661_holmes.txt", "pg2701_mobydick.txt"):
        chunks.append((ROOT / "tools" / "data" / name).read_text(encoding="utf-8", errors="replace"))
    return "\n".join(chunks)


def normalize_de(word):
    w = word.lower()
    w = w.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    return w


def build_wordlist(text, word_re, normalize=None):
    tokens = word_re.findall(text)
    words = set()
    counts = collections.Counter()
    for t in tokens:
        w = normalize(t) if normalize else t.lower()
        if len(w) < 2:
            continue
        words.add(w)
        counts[w[0]] += 1
    return words, counts


def initial_letter_freq(counts):
    total = sum(counts.values())
    letters = sorted(counts)
    freqs = [counts[l] / total for l in letters]
    return letters, freqs


def match_stat(letters6, words):
    """For a 6-letter string, per-position candidate-word counts and the bottleneck (min)."""
    per_position = []
    for ch in letters6:
        n = sum(1 for w in words if w[0] == ch.lower())
        per_position.append(n)
    return per_position


def run_language(lang, text, word_re, normalize, target, n_controls, seed):
    words, counts = build_wordlist(text, word_re, normalize)
    letters, freqs = initial_letter_freq(counts)

    target_pos = match_stat(target.lower(), words)
    target_min = min(target_pos)
    target_zero_positions = [target[i] for i, c in enumerate(target_pos) if c == 0]

    rng = random.Random(seed)
    control_mins = []
    control_rows = []
    for _ in range(n_controls):
        draw = "".join(rng.choices(letters, weights=freqs, k=len(target)))
        pos = match_stat(draw, words)
        control_rows.append({"string": draw.upper(), "per_position": pos, "min": min(pos)})
        control_mins.append(min(pos))

    control_mins_sorted = sorted(control_mins)
    n = len(control_mins_sorted)
    rank = sum(1 for m in control_mins_sorted if m <= target_min)  # how many controls <= target
    pct = 100.0 * rank / n

    example_words = {}
    for ch in target:
        cl = ch.lower()
        matches = sorted(w for w in words if w[0] == cl)
        example_words[ch] = matches[:5]

    return {
        "language": lang,
        "wordlist_size": len(words),
        "target_string": target,
        "target_per_position_counts": dict(zip(list(target), target_pos)),
        "target_min_count": target_min,
        "target_zero_count_positions": target_zero_positions,
        "example_words_per_letter": example_words,
        "control_n": n_controls,
        "control_seed": seed,
        "control_min_counts": control_mins_sorted,
        "control_min_mean": sum(control_mins) / n,
        "control_min_range": [min(control_mins), max(control_mins)],
        "target_min_percentile_vs_control": pct,
        "control_rows": control_rows,
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--controls", type=int, default=20)
    ap.add_argument("--seed", type=int, default=25092026)
    ap.add_argument("--out", default=None)
    args = ap.parse_args(argv)

    de_text = load_de20_text()
    en_text = load_en_text()

    de_result = run_language("de", de_text, WORD_RE_DE, normalize_de, TARGET, args.controls, args.seed)
    en_result = run_language("en", en_text, WORD_RE_EN, None, TARGET, args.controls, args.seed + 1)

    out = {"target": TARGET, "de": de_result, "en": en_result}
    text = json.dumps(out, indent=2, ensure_ascii=False)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
