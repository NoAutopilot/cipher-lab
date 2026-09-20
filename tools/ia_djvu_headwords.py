#!/usr/bin/env python3
"""Locate headwords in an Internet Archive book by scan index and running head.

Downloads <id>_djvu.xml (per-page OCR), and for each word reports the first scan whose
text has the word at the start of a line (optionally preceded by "To "), with the first
two OCR lines of that scan, which normally carry the printed page number and the
running head (e.g. "268 MOR"). Long s is tolerated (s matches s or f). Running heads
are OCR and must be checked by eye where they matter.

Usage: ia_djvu_headwords.py IA_IDENTIFIER [Word ...]   (default word list is for the
Wellington-Maitland 1812 dictionary code). Written 19 Sept 2026.
"""
import html, os, re, subprocess, sys

WORDS = ["Alphabet", "And", "At", "Be", "Can", "Cipher", "Cypher", "Day", "Early", "Head", "Morrow",
         "Occupy", "Period", "Provision", "Quarter", "Sea", "South", "Supply", "Theft", "Use",
         "Westward", "Which", "Will", "You"]


def fetch(iid):
    fn = f"{iid}_djvu.xml"
    if not os.path.exists(fn) or os.path.getsize(fn) < 1000:
        subprocess.run(["curl", "-sS", "-L", "-A", "Mozilla/5.0", "-o", fn,
                        f"https://archive.org/download/{iid}/{iid}_djvu.xml"], check=False)
    return open(fn, encoding="utf-8", errors="ignore").read()


def pages(xml):
    out = []
    for obj in re.findall(r"<OBJECT.*?</OBJECT>", xml, re.S):
        lines = []
        for ln in re.findall(r"<LINE>(.*?)</LINE>", obj, re.S):
            lines.append(html.unescape(" ".join(re.findall(r"<WORD[^>]*>(.*?)</WORD>", ln))))
        out.append(lines)
    return out


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    iid = sys.argv[1]
    words = sys.argv[2:] or WORDS
    pg = pages(fetch(iid))
    print("==", iid, len(pg), "scans")
    found = {}
    for i, lines in enumerate(pg):
        txt = "\n".join(lines)
        for w in words:
            if w in found:
                continue
            pat = w.replace("s", "[sf]")
            if re.search(r"(^|\n)\s*(To\s+)?" + pat + r"[,.'’]\s", txt):
                found[w] = (i, " | ".join(lines[:2])[:60])
    for w in words:
        print(f"  {w:10s}", found.get(w))


if __name__ == "__main__":
    main()
