"""build_lexicon.py -- MCC-GREGG (LANE DEFAULT-A1-0740-15, 15 Oct 2026): the Gregg-lexicon word list.

Source: John Robert Gregg, Gregg Shorthand Dictionary, new and revised edition (New York: Gregg Publishing, 1916; preface
dated 17 June 1916; public domain), Internet Archive item greggshorthanddi0000john_c6j8, OCR text
https://archive.org/download/greggshorthanddi0000john_c6j8/greggshorthanddi0000john_c6j8_djvu.txt (fetched 15 Oct 2026).
The OCR text itself is not committed (re-fetch it from that URL); this script turns it into gregg1916_headwords.txt.

Rule (fixed before any score): from the dictionary body (after the line 'GREGG SHORTHAND' that follows the preface),
every capitalised word [A-Z][a-z]+ on a line is a headword candidate; a candidate ending in '-' is joined with the first
lower-case word at the start of the next non-empty line (Abandon- / ment). The shorthand outlines OCR as noise (short
capitalised strings like 'Le', 'Pe'); the list is therefore kept only where it meets an English word list (the LM
corpus vocabulary is applied later, in token_anneal.lexicon_pool). Lower-cased, sorted, unique.
Usage: python3 build_lexicon.py DICT_DJVU_TXT manual1916_par61_ocr.txt (see __main__)
"""
import re, sys


def headwords(text):
    i = text.find("GREGG SHORTHAND", text.find("PREFACE"))
    lines = [l.strip() for l in text[i:].splitlines()]
    out = set()
    for n, l in enumerate(lines):
        for m in re.finditer(r"\b([A-Z][a-z]+)(-?)(?=\s|$)", l):
            w = m.group(1)
            if m.group(2):
                nxt = next((x for x in lines[n + 1:n + 4] if x), "")
                k = re.match(r"([a-z]+)", nxt)
                if not k:
                    continue
                w += k.group(1)
            out.add(w.lower())
    return sorted(out)




# ---- brief forms (word-signs): Gregg Shorthand Manual (1916; public domain), IA greggshorthanda00greggoog, OCR text
# https://archive.org/download/greggshorthanda00greggoog/greggshorthanda00greggoog_djvu.txt (fetched 15 Oct 2026),
# paragraph 61 "Key to review exercise on word-signs" items 1-12, saved verbatim as manual1916_par61_ocr.txt.
# Split on commas; a hyphenated entry gives each part as a word, except that a part which is a suffix (ent, ence, y, ly,
# n) is added to the first part (differ-ent-ence -> differ, different, difference). OCR repairs, fixed before any score:
OCR_FIX = {"mi- more": "am-more", "befgre-": "before-", "tehalf": "behalf", "fuU-y": "full-y", "gOrgood": "go-good",
           "market-Mr.": "market-mr", "Messrs.": "messrs", "to-morrow": "to-tomorrow"}
SUFFIX_PARTS = {"ent", "ence", "y", "ly", "n"}


def brief_forms(par61):
    t = par61
    for a, b in OCR_FIX.items():
        t = t.replace(a, b)
    t = re.sub(r"-\s*\n\s*", "-", t)            # entries broken across lines
    t = re.sub(r"\b\d+\.\s", " ", t)            # item numbers
    out = set()
    for e in t.replace("\n", " ").split(","):
        parts = [p for p in re.findall(r"[A-Za-z]+", e)]
        if not parts:
            continue
        base = parts[0].lower()
        out.add(base)
        for p in parts[1:]:
            p = p.lower()
            out.add(base + p if p in SUFFIX_PARTS else p)
    return sorted(out)


if __name__ == "__main__":
    # python3 build_lexicon.py DICT_DJVU_TXT manual1916_par61_ocr.txt -> writes gregg1916_headwords.txt,
    # gregg1916_briefforms.txt and gregg1916_lexicon.txt (their union, the MCC-GREGG lexicon) beside this script
    from pathlib import Path
    here = Path(__file__).resolve().parent
    hw = headwords(open(sys.argv[1], encoding="utf-8", errors="replace").read())
    bf = brief_forms(open(sys.argv[2], encoding="utf-8").read())
    (here / "gregg1916_headwords.txt").write_text("\n".join(hw) + "\n")
    (here / "gregg1916_briefforms.txt").write_text("\n".join(bf) + "\n")
    (here / "gregg1916_lexicon.txt").write_text("\n".join(sorted(set(hw) | set(bf))) + "\n")
    print(len(hw), len(bf), len(set(hw) | set(bf)))
