#!/usr/bin/env python3
"""Build tools/data/es18 (1690-1725 Spanish letters, gazette and diplomatic prose) from raw archive.org `_djvu.txt`.

GAPS5-na-schonenberg-1678-1716 (2 Oct 2026, account-4), the V6-PTCORP pattern (tools/data/pt18) for a 1702-1716
Spanish letter whose nearest corpus on disk (es17c7, 1634-1648) is 55-80 years off. Reads the raw OCR files named in
MANIFEST.tsv from --raw DIR, then per file:
  1. rejoins words hyphenated across OCR lines;
  2. long-s repair for the 1690-1710 original printings, which OCR long s as `f` ("defpues", "eftado"): every word
     holding an `f` is replaced by its best variant (each f kept or read as s, at most 4 f's) when that variant is at
     least 3x as frequent as the word itself in a long-s-free reference vocabulary, or when the f-form is unattested
     there and the s-form is attested -- tools/data/es17c7 (19th-c.
     printings) plus the two 1792-print San Felipe volumes of this corpus (the same rule as tools/data/it16dip/build.py);
  3. keeps an OCR line only when it has >= 4 word tokens and at least half of its tokens of 3+ letters are in the
     reference vocabulary (drops library stamps, column-garbled gazette lines, Latin marginalia, title-page scatter);
  4. writes the kept lines, gzipped, as <identifier>.txt.gz (judge_plaintext folds letters itself).
  python3 tools/data/es18/build.py --raw DIR
"""
import argparse, collections, gzip, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from judge_plaintext import fold, read_corpus  # noqa: E402

WORD = re.compile(r"[A-Za-zÀ-ÿſ]+")


def ref_vocab(raw, clean_ids):
    c = collections.Counter()
    for p in sorted((HERE.parent / "es17c7").glob("*.txt.gz")):
        c.update(re.findall(r"[a-z]+", fold_words(read_corpus(p))))
    for ident in clean_ids:
        c.update(re.findall(r"[a-z]+", fold_words((Path(raw) / f"{ident}.txt").read_text(encoding="utf-8", errors="replace"))))
    return c


def fold_words(t):
    """fold() per word, keeping spaces (fold() itself strips everything but letters)."""
    return " ".join(fold(w) for w in WORD.findall(t))


def _variants(lw):
    out = [""]
    for ch in lw:
        out = [o + x for o in out for x in (("f", "s") if ch == "f" else (ch,))]
    return out


def longs(word, voc):
    lw = word.lower()
    if "f" not in lw or lw.count("f") > 4:
        return word
    base = voc.get(fold(lw), 0)
    best, bc = None, 0
    for v in _variants(lw):
        n = voc.get(fold(v), 0)
        if v != lw and n > bc:
            best, bc = v, n
    # accept the s-reading when it is 3x as frequent as the f-reading, or when the f-reading is unattested in the
    # clean vocabulary at all and the s-reading is attested (a form unseen in 7M+ letters of clean Spanish is OCR)
    if best is None or bc < (3 * base if base else 1):
        return word
    return best.capitalize() if word[:1].isupper() else best


def clean(text, voc, repair):
    text = re.sub(r"-\s*\n\s*", "", text)
    if repair:
        text = WORD.sub(lambda m: longs(m.group(0).replace("ſ", "s"), voc), text)
    kept, tot, out = 0, 0, []
    for line in text.splitlines():
        toks = WORD.findall(line)
        if len(toks) < 4:
            continue
        tot += 1
        long_toks = [fold(t) for t in toks if len(t) >= 3]
        if long_toks and sum(1 for t in long_toks if t in voc) / len(long_toks) >= 0.5:
            out.append(" ".join(toks)); kept += 1
    return out, kept, tot


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--raw", required=True, help="directory holding <identifier>.txt raw djvu OCR files")
    a = ap.parse_args()
    rows = [l.rstrip("\n").split("\t") for l in (HERE / "MANIFEST.tsv").open(encoding="utf-8")]
    hdr, rows = rows[0], rows[1:]
    ids = [r[hdr.index("identifier")] for r in rows]
    repair_col = hdr.index("longs_repair")
    clean_ids = [r[hdr.index("identifier")] for r in rows if r[repair_col] != "yes"]
    voc = ref_vocab(a.raw, clean_ids)
    for r in rows:
        ident = r[hdr.index("identifier")]
        text = (Path(a.raw) / f"{ident}.txt").read_text(encoding="utf-8", errors="replace")
        out, kept, tot = clean(text, voc, r[repair_col] == "yes")
        with gzip.open(HERE / f"{ident}.txt.gz", "wt", encoding="utf-8") as g:
            g.write("\n".join(out) + "\n")
        print(f"{ident}\tkept_lines {kept}/{tot}\tfolded_letters {len(fold(' '.join(out)))}")


if __name__ == "__main__":
    main()
