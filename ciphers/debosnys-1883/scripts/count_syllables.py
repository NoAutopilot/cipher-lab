#!/usr/bin/env python3
"""French syllable/letter counter for the GOLD-4B form test.

Heuristic, not a full prosody engine: groups consecutive vowels into one
syllable nucleus each (standard French diphthong behaviour), and treats a
word-final unaccented "e" as mute -- not counted -- unless it is the line's
last word AND the word has no other vowel group (so a monosyllable like "je"
still counts as 1, never 0). A line-final word's trailing mute e is dropped
per the classical "feminine ending" convention (counted syllables = the
alexandrine's 12, not the extra written e). Elisions before a vowel-initial
word are assumed already marked in the transcription by an apostrophe
(m'ecoute, j'ai, qu'une, l'avenir, ...), which French orthography does for us.

Usage: import count_syllables(word), line_syllables(line, is_last_word_line_final=True)
"""
import re
import sys

VOWELS = "aàâeéèêëiîïoôuûùyœæAÀÂEÉÈÊËIÎÏOÔUÛÙYŒÆ"


def vowel_groups(word):
    groups = []
    cur = ""
    for ch in word:
        if ch in VOWELS:
            cur += ch
        else:
            if cur:
                groups.append(cur)
                cur = ""
    if cur:
        groups.append(cur)
    return groups


def count_word_syllables(word, line_final=False):
    w = word.lower()
    groups = vowel_groups(w)
    if not groups:
        return 0
    n = len(groups)
    last = groups[-1]
    # mute e: last vowel group is a lone, unaccented "e"
    if last == "e" and w.endswith("e"):
        if n > 1:
            # word has other vowels: this trailing e is mute unless kept
            # (it is always dropped here; elision-before-vowel is already
            # marked by an apostrophe in the transcription, and a
            # not-line-final e before a consonant is the one case classical
            # scansion keeps -- handled by the caller for non-final words)
            if not line_final:
                return n  # keep it: e before a consonant, mid-line, counts
            return n - 1
        else:
            # monosyllable made only of "e" (le, de, je, ne, se, ce...):
            # never drops to 0
            return 1
    return n


def line_syllables(text):
    words = re.findall(r"[A-Za-zÀ-ÿœŒ']+", text)
    # split on apostrophes: "m'ecoute" -> "m'" handled as elided already,
    # so just strip the leading elided fragment (single letter + ') and
    # count the remainder word; the elided fragment contributes 0 syllables
    # (its vowel was dropped, replaced by the apostrophe)
    total = 0
    n_words = len(words)
    for i, w in enumerate(words):
        if "'" in w:
            # e.g. "m'ecoute", "j'ai", "qu'une", "l'avenir", "c'est", "d'humanite"
            frag_after = w.split("'")[-1]
            total += count_word_syllables(frag_after, line_final=(i == n_words - 1))
        else:
            total += count_word_syllables(w, line_final=(i == n_words - 1))
    return total


def line_letters(text):
    return len(re.findall(r"[A-Za-zÀ-ÿœŒ]", text))


if __name__ == "__main__":
    for line in sys.stdin:
        line = line.rstrip("\n")
        if not line:
            continue
        print(f"{line_syllables(line)}\t{line_letters(line)}\t{line}")
