#!/usr/bin/env python3
"""Build tools/data/nl18/*.txt.gz from Internet Archive _djvu.txt OCR of 1770-1799 Dutch prose (NL18-CORPUS, 3 Oct 2026).

Usage: python3 tools/data/nl18/build_nl18.py RAW_DIR   (RAW_DIR holds <identifier>.txt as downloaded from
       https://archive.org/download/<id>/<id>_djvu.txt; see MANIFEST.tsv). Writes <identifier>.txt.gz beside this script.

Two normalizations, both recorded in README.md:
 1. drop OCR lines that are English (Google Books boilerplate, the odd English quotation): a line with >= 2 of
    the, this, google, that, which, is, with, you, are, book, books.
 2. long-s repair: the 18th-c. prints set the long s, which the OCR reads as 'f' ("Amfterdam", "eerft", "fchip"), while
    the target legends are decoded to a round 's'. Leaving it would make every real 'st'/'sch' look improbable to the
    model and bias the gate toward FAIL. For each word containing 'f', every variant replacing a subset (<= 3 f's) of
    them with 's' is looked up in tools/data/nl20 (1880-1940 Dutch, where no long s exists; y queried also as ij); the
    most frequent variant wins, the original included (so 'heeft', 'of', 'oft' stay). Unattested words get one
    mechanical rule, 'f' before c/t/p/k/m/n/w -> 's' ('Baft' -> 'Bast', 'doorfplyten' -> 'doorsplyten'). It is a heuristic: it errs toward leaving 'f'.
"""
import gzip, itertools, re, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from judge_plaintext import read_corpus  # noqa: E402

FILES = ["beschryvingvangu01hart", "beschryvingvangu02hart", "bub_gb_mGdCAAAAcAAJ", "bataviaindeszelf02amst",
         "beschryvingvanh00esch", "reizennaaceilon00roosgoog", "verzamelingvanst01vand"]
EN = {"the", "this", "google", "that", "which", "is", "with", "you", "are", "book", "books"}


def nl20_lexicon():
    c = Counter()
    for p in sorted((HERE.parent / "nl20").glob("*.txt.gz")):
        c.update(re.findall(r"[a-z]+", read_corpus(p).lower()))
    return c


def best(word, lex, cache):
    lw = word.lower()
    if "f" not in lw:
        return word
    if lw in cache:
        out = cache[lw]
    else:
        pos = [i for i, ch in enumerate(lw) if ch == "f"][:3]
        cands = []
        for r in range(len(pos) + 1):
            for sub in itertools.combinations(pos, r):
                v = "".join("s" if i in sub else ch for i, ch in enumerate(lw))
                n = lex.get(v, 0) + lex.get(v.replace("y", "ij"), 0)
                cands.append((n, -r, v))
        n, _, v = max(cands)
        out = v if n > 0 else re.sub(r"f(?=[ctpkmnw])", "s", lw)
        cache[lw] = out
    return out if word.islower() else (out.capitalize() if word[:1].isupper() else out)


def main():
    raw = Path(sys.argv[1])
    lex = nl20_lexicon(); cache = {}
    for fid in FILES:
        t = (raw / f"{fid}.txt").read_text(encoding="utf-8", errors="replace")
        keep = []
        for ln in t.splitlines():
            if len(EN & set(re.findall(r"[a-z]+", ln.lower()))) >= 2:
                continue
            keep.append(re.sub(r"[A-Za-z]+", lambda m: best(m.group(0), lex, cache), ln))
        out = "\n".join(keep) + "\n"
        with gzip.open(HERE / f"{fid}.txt.gz", "wt", encoding="utf-8") as fh:
            fh.write(out)
        print(fid, len(out))


if __name__ == "__main__":
    main()
