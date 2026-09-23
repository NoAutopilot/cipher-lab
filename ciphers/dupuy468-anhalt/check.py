#!/usr/bin/env python3
"""Regenerate the reading of BnF Dupuy 468 f.28r-v from ciphertext.txt and key.tsv (rule 7).

ciphertext.txt: one manuscript line per row, 'line<TAB>tokens<TAB>glosses'. tokens are whitespace
separated: a symbol code, or [PLAIN:word] for a word written in clear by the main hand. glosses are
'word@i-j' items (the interlinear gloss word written over tokens i..j, 1-based positions in that line's
token list), separated by spaces.

key.tsv: 'token<TAB>value<TAB>source<TAB>note'. value is a letter or letter group (a letter sign), '=word'
(a word sign, read as the whole word) or '' (a null or separator). source is 'gloss' (value read from the
interlinear gloss, see key_from_gloss.tsv) or 'search' (value found by the n-gram search, runs.tsv).

exceptions.tsv: 'line<TAB>pos<TAB>token<TAB>key_value<TAB>gloss_value<TAB>reason', one row per (line, pos)
where the gloss word actually written over that token departs from key.tsv's dominant value for the
symbol (a minority vote; NOTES.md "Self-consistency" and the ASSIGNMENTS row 25 brief of 23 Sept 2026).
At these positions gloss_value overrides key.tsv's value for that one occurrence only, and the token is
graded H (read from the gloss, a key source on the document, at that exact spot).

Grades per token (rule 4): H = the token stands under a gloss word that aligns with it letter for letter
(or, for a word sign, a gloss word over it) and the aligned gloss letter equals the key value (read from the
gloss, a key source on the document; votes in key_from_gloss.tsv), or the position has an exceptions.tsv
override; S = not so glossed, read with a value established from the gloss elsewhere (the gloss-derived key
applied, supported by the control in NOTES.md); M = a value from the search only, a key row marked
'uncertain', or a word sign whose own gloss disagrees; unread = no value in the key.

Writes reading.txt (line by line: clear words lower case, deciphered words UPPER CASE, glosses in a
parallel line) and reading_tokens.tsv (one row per cipher token with its value and grade).
  python3 check.py          regenerate both files
  python3 check.py --check  exit 1 if the committed files differ from a fresh regeneration
Written 23 Sept 2026. exceptions.tsv added 23 Sept 2026 (ASSIGNMENTS row 25).
"""
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load_cipher():
    rows = []
    for l in open(os.path.join(HERE, "ciphertext.txt"), encoding="utf-8"):
        if l.startswith("#") or not l.strip():
            continue
        p = l.rstrip("\n").split("\t")
        p += [""] * (3 - len(p))
        toks = p[1].split()
        gl = {}
        for g in p[2].split():
            w, _, span = g.rpartition("@")
            a, _, b = span.partition("-")
            for i in range(int(a), int(b or a) + 1):
                gl[i] = w
        rows.append((p[0], toks, gl, p[2]))
    return rows


def load_key():
    key = {}
    for l in open(os.path.join(HERE, "key.tsv"), encoding="utf-8"):
        if l.startswith("#") or not l.strip() or l.startswith("token\t"):
            continue
        p = l.rstrip("\n").split("\t")
        p += [""] * (4 - len(p))
        key[p[0]] = (p[1], p[2], p[3])
    return key


def same_word(gloss, value):
    """A word-sign gloss agrees with the key value when their first three letters agree ('de' dropped)."""
    a, b = gloss.lstrip("=").lower(), value.lstrip("=").lower()
    a = a[2:] if a.startswith("de") and not b.startswith("de") else a
    return a[:3] == b[:3]


def load_votes():
    v = {}
    for l in open(os.path.join(HERE, "key_from_gloss.tsv"), encoding="utf-8"):
        if l.startswith("#") or l.startswith("line\t") or not l.strip():
            continue
        p = l.rstrip("\n").split("\t")
        v[(p[0], int(p[1]))] = p[3]
    return v


def load_exceptions():
    ex = {}
    for l in open(os.path.join(HERE, "exceptions.tsv"), encoding="utf-8"):
        if l.startswith("#") or l.startswith("line\t") or not l.strip():
            continue
        p = l.rstrip("\n").split("\t")
        ex[(p[0], int(p[1]))] = p[4]
    return ex


def render():
    rows, key, votes, exceptions = load_cipher(), load_key(), load_votes(), load_exceptions()
    out, tok_rows, grades = [], ["line\tpos\ttoken\tvalue\tgrade\tgloss"], Counter()
    for ln, toks, gl, graw in rows:
        words, cur = [], []
        for i, t in enumerate(toks, 1):
            if t.startswith("[PLAIN:"):
                if cur:
                    words.append("".join(cur).upper())
                    cur = []
                words.append(t[7:-1])
                continue
            if (ln, i) in exceptions:
                val, g = exceptions[(ln, i)], "H"
                grades[g] += 1
                tok_rows.append(f"{ln}\t{i}\t{t}\t{val}\t{g}\t{gl.get(i, '')}")
                if val.startswith("="):
                    if cur:
                        words.append("".join(cur).upper())
                        cur = []
                    words.append("<" + val[1:].upper() + ">")
                else:
                    cur.append(val)
                continue
            v, src, note = key.get(t, (None, "", ""))
            if v is None or "?" in (v or ""):
                val, g = "?", "unread"
            else:
                val = v
                vote = votes.get((ln, i))
                if src == "search" or "uncertain" in note:
                    g = "M"
                elif vote is not None and (vote == v or (v.startswith("=") and vote.startswith("=")
                                                         and same_word(vote, v))):
                    g = "H"
                elif v.startswith("=") and i in gl:
                    g = "M"
                else:
                    g = "S"
            grades[g] += 1
            tok_rows.append(f"{ln}\t{i}\t{t}\t{val}\t{g}\t{gl.get(i, '')}")
            if val.startswith("="):
                if cur:
                    words.append("".join(cur).upper())
                    cur = []
                words.append("<" + val[1:].upper() + ">")
            else:
                cur.append(val)
        if cur:
            words.append("".join(cur).upper())
        out.append(f"{ln}  " + " ".join(w for w in words if w))
        if graw:
            out.append(f"{ln}g " + graw)
    head = ["# Reading of BnF Dupuy 468 f.28r-v, regenerated by check.py from ciphertext.txt and key.tsv.",
            "# Clear words lower case; deciphered UPPER CASE (word division of cipher runs is not marked in",
            "# the cipher and is not restored here); <WORD> = word sign; ? = unread; 'g' rows = the gloss.",
            "# Grades: " + ", ".join(f"{k} {v}" for k, v in sorted(grades.items()))]
    return "\n".join(head + out) + "\n", "\n".join(tok_rows) + "\n"


def main():
    txt, toks = render()
    paths = [os.path.join(HERE, "reading.txt"), os.path.join(HERE, "reading_tokens.tsv")]
    if "--check" in sys.argv:
        stale = [p for p, new in zip(paths, (txt, toks))
                 if not os.path.exists(p) or open(p, encoding="utf-8").read() != new]
        if stale:
            print("STALE:", ", ".join(os.path.basename(p) for p in stale))
            sys.exit(1)
        print("reading.txt and reading_tokens.tsv are current")
        return
    for p, new in zip(paths, (txt, toks)):
        open(p, "w", encoding="utf-8").write(new)
    print(txt.splitlines()[3])


if __name__ == "__main__":
    main()
