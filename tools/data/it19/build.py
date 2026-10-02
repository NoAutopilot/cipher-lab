#!/usr/bin/env python3
"""Build it19 (A2-CAS7, LANE-A2PUSH, 2 Oct 2026): Italian political, historical and epistolary prose of about
1800-1830, for castelcicala-1816 (Neapolitan despatches London/Paris 1816-23), which it16 and it16dip (16th c.)
do not era-match. Same method as tools/data/pt18 (V6-PTCORP): archive.org `_djvu.txt` OCR, one file per source.

Reads the raw files named in MANIFEST.tsv from --raw DIR, then per file:
  1. drops Google Books boilerplate lines, rejoins words hyphenated across OCR lines;
  2. merges OCR paragraphs to chunks of >= 60 words and keeps a chunk only when it reads as Italian prose:
     Italian function words >= 22% of tokens, French function words <= 2%, Latin endings <= 3%, junk tokens
     (no two letters in a row) <= 20%, fewer than 2 ']' (drops indexes, tables and French/Latin apparatus);
  3. caps each file at CAP folded letters (no source dominates; rule 3 fold-count paragraph);
  4. writes one kept chunk per line, folded words space-separated, gzipped as <identifier>.txt.gz.
  python3 tools/data/it19/build.py --raw DIR
"""
import argparse, gzip, re, unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent


def fold(s):
    """Same as tools/italian_ngram.py fold() (kept local: that module needs numpy)."""
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


def paragraphs(text):
    buf = []
    for line in text.splitlines():
        if line.strip():
            buf.append(line.strip())
        elif buf:
            yield " ".join(buf); buf = []
    if buf:
        yield " ".join(buf)

CAP = 650_000
IT = set("di che e la il non per del in a si da le al della un una con ma se lo mi gli io è era sua suo i ed come "
         "più quando dei alla delle nel sono anche già poi ne ci essere ha aveva fu re così questo quella quello "
         "loro egli o tra fra sopra dopo dal dalle degli ai".split())
FR = {"les", "des", "du", "au", "aux", "est", "une", "sur", "mais", "ont", "leur", "cette", "qui", "dans", "pour"}
BOILER = re.compile(r"Google|digitized|Digitized|public domain|books\.google|This is a digital copy|"
                    r"Usage guidelines|automated query", re.I)


def keep(par):
    w = re.findall(r"[a-z]+", fold(par))
    n = len(w)
    if n < 30:
        return False
    it = sum(1 for x in w if x in IT)
    fr = sum(1 for x in w if x in FR)
    la = sum(1 for x in w if len(x) > 3 and re.search(r"(orum|arum|ibus|unt|que)$", x))
    junk = sum(1 for x in re.findall(r"\S+", par) if not re.search(r"[A-Za-zÀ-ÿ]{2}", x))
    return it >= 0.22 * n and fr <= 0.02 * n and la <= 0.03 * n and junk <= 0.20 * n and par.count("]") < 2


def chunks(text, minw=60):
    buf = []
    for par in paragraphs(text):
        buf.append(par)
        if sum(len(x.split()) for x in buf) >= minw:
            yield " ".join(buf); buf = []
    if buf:
        yield " ".join(buf)


def build_one(text, cap=CAP):
    text = "\n".join(l for l in text.splitlines() if not BOILER.search(l))
    text = re.sub(r"-\s*\n\s*", "", text)
    kept = tot = letters = 0
    out = []
    for par in chunks(text):
        tot += 1
        if letters < cap and keep(par):
            ws = [x for x in re.split(r"[^a-z]+", fold(par)) if x]
            out.append(" ".join(ws)); kept += 1
            letters += sum(len(x) for x in ws)
    return out, kept, tot, letters


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--raw", required=True)
    a = ap.parse_args()
    ids = [l.split("\t")[0] for l in (HERE / "MANIFEST.tsv").read_text().splitlines()[1:] if l.strip()]
    for ident in ids:
        text = (Path(a.raw) / f"{ident}.txt").read_text(encoding="utf-8", errors="replace")
        out, kept, tot, letters = build_one(text)
        with gzip.open(HERE / f"{ident}.txt.gz", "wt", encoding="utf-8") as g:
            g.write("\n".join(out) + "\n")
        print(f"{ident}\tkept {kept}/{tot} chunks\tletters {letters}")


if __name__ == "__main__":
    main()
