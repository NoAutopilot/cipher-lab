#!/usr/bin/env python3
"""translit_ru.py: transliterate lower-cased Russian (Cyrillic) text on disk into one of four Latin
transliteration schemes for the kaliningrad-2015 Russian-substitution hypothesis (GOLD-KAL2, 26 Sept 2026).

  python3 tools/translit_ru.py --scheme s1|s1s|s3p|s3 IN_DIR OUT_FILE

IN_DIR: a directory of .txt.gz (or .txt) files, Cyrillic lower-case verse/prose text with optional
"== CHAPTER N ==" marker lines (tools/data/ru19's own format) -- marker lines are dropped, everything else
is split into words on runs of Cyrillic letters (punctuation, brackets, digits, Latin chapter-marker text
all fall away as word separators). OUT_FILE: a single .txt(.gz) file, one line per input line, words space
separated, in the chosen scheme's Latin letters.

Conventions shared by all four schemes (project convention, not a scholarly transliteration standard):
ё is folded to е's letter EXCEPT where a scheme's own rule names ё explicitly (S3'/S3's paired-consonant
rule); ъ is always dropped; й and ы both become y. Every scheme keeps a plaintext alphabet inside
homophonic_anneal.fold()'s ALPHA = "abcdefghiklmnopqrstuwxyz" (24 letters, a-z minus j and v) --
never use j or v.

Schemes (see the job brief `.claude/briefs/runs/2026-09-26-lane-gold-c5-kaliningrad-russian.md` for the
letter-by-letter table this implements verbatim):
  s1   scientific with digraphs (23 Latin letters; q is the soft sign ь, about 1.5 pct of letters)
  s1s  s1 with q (the soft sign) removed entirely (22 letters; softness lost)
  s3p  phonemic partial: s1, except a paired consonant (б в г д з к л м н п р с т ф х) followed by
       я, ю, ё or ь writes the consonant, then q, then the vowel as a, u, o (nothing for ь);
       я ю ё elsewhere stay ya yu e. q is then about 2.9 pct of letters.
  s3   phonemic full: s3p, and also q before е and и after a paired consonant (vowel then e, i).
       q is then about 12.6 pct of letters.

Test: python3 tools/tests/test_translit_ru.py
"""
import argparse
import gzip
import re
import sys
from pathlib import Path

PAIRED = set("бвгдзклмнпрстфх")
CHAPTER_MARKER = re.compile(r"^==.*==$")
CYRILLIC_WORD = re.compile(r"[а-яё]+")

# S1 base map: every scheme starts here, then s1s/s3p/s3 override selected letters/contexts.
S1_MAP = {
    "а": "a", "б": "b", "в": "w", "г": "g", "д": "d", "е": "e", "ё": "e", "ж": "zh", "з": "z",
    "и": "i", "й": "y", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r",
    "с": "s", "т": "t", "у": "u", "ф": "f", "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh",
    "щ": "shch", "ъ": "", "ы": "y", "ь": "q", "э": "e", "ю": "yu", "я": "ya",
}

# vowel forms written after a paired-consonant + q under s3p/s3
_SOFT_VOWEL = {"я": "a", "ю": "u", "ё": "o", "ь": "", "е": "e", "и": "i"}
_TRIGGERS_S3P = {"я", "ю", "ё", "ь"}
_TRIGGERS_S3 = _TRIGGERS_S3P | {"е", "и"}

SCHEMES = ("s1", "s1s", "s3p", "s3")


def extract_words(text):
    """Yield (line words) for each non-marker line: runs of Cyrillic letters, everything else dropped."""
    for line in text.splitlines():
        line = line.strip()
        if not line or CHAPTER_MARKER.match(line):
            continue
        yield CYRILLIC_WORD.findall(line.lower())


def _translit_word_s1(word, drop_soft_sign=False):
    out = []
    for c in word:
        if drop_soft_sign and c == "ь":
            continue
        out.append(S1_MAP.get(c, ""))
    return "".join(out)


def _translit_word_soft(word, triggers):
    out = []
    n = len(word)
    i = 0
    while i < n:
        c = word[i]
        nxt = word[i + 1] if i + 1 < n else None
        if c in PAIRED and nxt in triggers:
            out.append(S1_MAP.get(c, ""))
            out.append("q")
            out.append(_SOFT_VOWEL[nxt])
            i += 2
        else:
            out.append(S1_MAP.get(c, ""))
            i += 1
    return "".join(out)


def transliterate_word(word, scheme):
    if scheme == "s1":
        return _translit_word_s1(word)
    if scheme == "s1s":
        return _translit_word_s1(word, drop_soft_sign=True)
    if scheme == "s3p":
        return _translit_word_soft(word, _TRIGGERS_S3P)
    if scheme == "s3":
        return _translit_word_soft(word, _TRIGGERS_S3)
    raise ValueError(f"unknown scheme {scheme!r}")


def transliterate_text(text, scheme):
    lines = []
    for words in extract_words(text):
        lat_words = [transliterate_word(w, scheme) for w in words]
        lat_words = [w for w in lat_words if w]
        if lat_words:
            lines.append(" ".join(lat_words))
    return "\n".join(lines)


def read_text_file(path):
    if str(path).endswith(".gz"):
        with gzip.open(path, "rt", encoding="utf-8") as f:
            return f.read()
    return Path(path).read_text(encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--scheme", required=True, choices=SCHEMES)
    ap.add_argument("in_dir")
    ap.add_argument("out_file")
    args = ap.parse_args()

    in_dir = Path(args.in_dir)
    files = sorted(p for p in in_dir.iterdir() if p.suffix == ".gz" or p.suffix == ".txt")
    if not files:
        sys.exit(f"no .txt/.txt.gz files found in {in_dir}")

    out_lines = []
    for f in files:
        text = read_text_file(f)
        out_lines.append(transliterate_text(text, args.scheme))
    out_text = "\n".join(l for l in out_lines if l)

    letters = re.sub(r"[^a-z]", "", out_text)
    for bad in ("j", "v"):
        if bad in letters:
            sys.exit(f"BUG: scheme {args.scheme} produced forbidden letter {bad!r}")

    out_path = Path(args.out_file)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if str(out_path).endswith(".gz"):
        with gzip.open(out_path, "wt", encoding="utf-8") as f:
            f.write(out_text)
    else:
        out_path.write_text(out_text, encoding="utf-8")

    print(f"wrote {out_path} ({len(files)} source files, {len(letters)} letters, scheme={args.scheme})")


if __name__ == "__main__":
    main()
