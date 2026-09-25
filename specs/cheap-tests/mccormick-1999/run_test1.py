#!/usr/bin/env python3
"""Cheap test 1 for specs/mccormick-1999.json: catalogue repeated tokens (2+ chars) across both
notes, and compute three numbers -- vowel share, share of text covered by repeated n-grams
(n=3..6), and index of coincidence -- for the notes and for three matched controls at the same N
(letters-only): real English prose, the same English with vowels dropped, and English letters
shuffled. No decipherment attempted (rule 10 / brief scope). tools/data/pg1661_holmes.txt only,
no network. Written 25 Sept 2026, LANE B2 worker bMCC.
"""
import json
import random
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
SPEC = json.loads((ROOT / "specs/mccormick-1999.json").read_text())

VOWELS = set("AEIOU")


def letters_only(s):
    return "".join(ch for ch in s.upper() if ch.isalpha())


def tokens_of(lines):
    """Split each line on any non-letter character; keep tokens of length >= 2."""
    out = []
    for line in lines:
        for tok in re.split(r"[^A-Za-z]+", line):
            if len(tok) >= 2:
                out.append(tok.upper())
    return out


def vowel_share(letters):
    if not letters:
        return 0.0
    return sum(1 for c in letters if c in VOWELS) / len(letters)


def ngram_coverage(letters, n):
    """Fraction of letter positions covered by an n-gram that occurs >=2 times in `letters`."""
    L = len(letters)
    if L < n:
        return 0.0
    counts = Counter(letters[i:i + n] for i in range(L - n + 1))
    covered = [False] * L
    for i in range(L - n + 1):
        if counts[letters[i:i + n]] >= 2:
            for j in range(i, i + n):
                covered[j] = True
    return sum(covered) / L


def index_of_coincidence(letters):
    L = len(letters)
    if L < 2:
        return 0.0
    counts = Counter(letters)
    num = sum(c * (c - 1) for c in counts.values())
    den = L * (L - 1)
    return num / den


def three_numbers(letters):
    return {
        "vowel_share": round(vowel_share(letters), 4),
        "ngram_coverage_n3": round(ngram_coverage(letters, 3), 4),
        "ngram_coverage_n4": round(ngram_coverage(letters, 4), 4),
        "ngram_coverage_n5": round(ngram_coverage(letters, 5), 4),
        "ngram_coverage_n6": round(ngram_coverage(letters, 6), 4),
        "ic": round(index_of_coincidence(letters), 5),
        "n_letters": len(letters),
    }


def main():
    note1_lines = SPEC["ciphertext"]["note_1"]
    note2_lines = SPEC["ciphertext"]["note_2"]
    all_lines = note1_lines + note2_lines

    # --- token catalogue (rule: 2+ character tokens, split on any non-letter) ---
    toks = tokens_of(all_lines)
    tok_counts = Counter(toks)
    top20 = tok_counts.most_common(20)

    # positions: for each of the top-20 tokens, which note/line indices it appears in
    positions = {}
    for tok, _ in top20:
        hits = []
        for note_idx, lines in ((1, note1_lines), (2, note2_lines)):
            for line_idx, line in enumerate(lines):
                line_toks = [t.upper() for t in re.split(r"[^A-Za-z]+", line) if len(t) >= 2]
                cnt = line_toks.count(tok)
                if cnt:
                    hits.append({"note": note_idx, "line": line_idx, "count": cnt})
        positions[tok] = hits

    # substring occurrence count: how often each top-20 token appears anywhere in the concatenated
    # letters-only text (including embedded inside longer undelimited runs, e.g. NCBE inside
    # "OPREHLDULDNCBE"), distinct from the delimiter-isolated `count` column above
    all_letters_concat = letters_only("".join(all_lines))

    def substring_count(hay, needle):
        n, start, c = len(needle), 0, 0
        while True:
            i = hay.find(needle, start)
            if i == -1:
                return c
            c += 1
            start = i + 1

    with (OUT / "top20_tokens.tsv").open("w") as f:
        f.write("rank\ttoken\tdelimited_count\tsubstring_count\tlength\tlines(note:line:count)\n")
        for i, (tok, cnt) in enumerate(top20, 1):
            loc = ";".join(f"{h['note']}:{h['line']}:{h['count']}" for h in positions[tok])
            subc = substring_count(all_letters_concat, tok)
            f.write(f"{i}\t{tok}\t{cnt}\t{subc}\t{len(tok)}\t{loc}\n")

    # --- letters-only text, combined across both notes (matches spec judge N=700-800) ---
    combined_letters = letters_only("".join(all_lines))
    note1_letters = letters_only("".join(note1_lines))
    note2_letters = letters_only("".join(note2_lines))
    N = len(combined_letters)

    target_numbers = three_numbers(combined_letters)
    target_numbers["note1_only"] = three_numbers(note1_letters)
    target_numbers["note2_only"] = three_numbers(note2_letters)

    # --- matched controls at the same combined N, tools/data only, no fetch ---
    holmes_raw = (ROOT / "tools/data/pg1661_holmes.txt").read_text(encoding="utf-8", errors="replace")
    holmes_letters_full = letters_only(holmes_raw)

    def cut(letters_full, n, seed):
        rng = random.Random(seed)
        start = rng.randrange(0, max(1, len(letters_full) - n))
        return letters_full[start:start + n]

    SEEDS = [1, 2, 3]

    def avg_numbers(list_of_dicts):
        keys = [k for k in list_of_dicts[0] if not isinstance(list_of_dicts[0][k], dict)]
        return {k: round(sum(d[k] for d in list_of_dicts) / len(list_of_dicts), 4) for k in keys}

    # control A: real English prose, cut to N letters
    ctrl_prose_runs = [three_numbers(cut(holmes_letters_full, N, s)) for s in SEEDS]
    ctrl_prose = avg_numbers(ctrl_prose_runs)

    # control B: same English with vowels dropped, then cut to N letters (post-drop)
    holmes_novowel_full = "".join(c for c in holmes_letters_full if c not in VOWELS)
    ctrl_novowel_runs = [three_numbers(cut(holmes_novowel_full, N, s)) for s in SEEDS]
    ctrl_novowel = avg_numbers(ctrl_novowel_runs)

    # control C: English letters shuffled (same overall letter distribution as the prose sample, shuffled)
    def shuffled(letters_full, n, seed):
        rng = random.Random(seed + 100)
        sample = list(cut(letters_full, n, seed))
        rng.shuffle(sample)
        return "".join(sample)

    ctrl_shuf_runs = [three_numbers(shuffled(holmes_letters_full, N, s)) for s in SEEDS]
    ctrl_shuf = avg_numbers(ctrl_shuf_runs)

    out = {
        "spec": "specs/mccormick-1999.json",
        "test": "cheap_tests_in_order[0] (brief-specified measurable version)",
        "date": "25 Sept 2026",
        "N_combined_letters": N,
        "top20_repeated_tokens_file": "top20_tokens.tsv",
        "notes_target": target_numbers,
        "control_A_english_prose_n3seeds": ctrl_prose,
        "control_B_english_vowels_dropped_n3seeds": ctrl_novowel,
        "control_C_english_letters_shuffled_n3seeds": ctrl_shuf,
        "control_source": "tools/data/pg1661_holmes.txt (Sherlock Holmes, Project Gutenberg #1661), 3 random-offset cuts (seeds 1,2,3), no network fetch",
        "note_on_tokens": "tokens are maximal runs of letters split on any non-letter char (space, hyphen, paren, digit, punctuation); distinct from the three-numbers letters-only fold used for vowel/ngram/IC, which strips all non-letters and concatenates within each note",
    }
    (OUT / "test1_result.json").write_text(json.dumps(out, indent=1))

    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
