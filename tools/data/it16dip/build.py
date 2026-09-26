#!/usr/bin/env python3
"""Build it16dip (SALV-CTX, LANE SALV, 26 Sept 2026): 16th-c. Italian diplomatic letters for fr2933-salviati-1525.

Reads the raw archive.org `_djvu.txt` files named in MANIFEST.tsv from --raw DIR, then per file:
  1. rejoins words hyphenated across OCR lines;
  2. long-s repair: the 1564 and 1769-71 prints read long s as `f` ("quefto", "gratiffimo"); every word holding an
     `f` is replaced by its best variant (each f kept or read as s, `fl` also read as the st ligature, at most 4) when the variant is at least 3x as
     frequent as the word itself in a long-s-free reference vocabulary (tools/data/it16, 19th-c. printings);
  3. merges OCR paragraphs shorter than 60 words (the 1564 print has a blank line after every line), keeps a chunk only when tools/italian16_corpus.py's keep() accepts it, or -- for the 18th/19th-c. editions
     that print "e/ed" for "et", and for noisy OCR -- a relaxed test: no `et` requirement, `ed` not counted modern,
     period markers >= 15% (not 25%), junk tokens <= 25%, FOREIGN <= 3% and French function words <= 2% (drops
     Desjardins' French apparatus and Latin);
  4. writes one kept paragraph per line, words space-separated (judge_plaintext folds letters; wordcode splits on
     spaces), gzipped as <identifier>.txt.gz.
  python3 tools/data/it16dip/build.py --raw DIR
"""
import argparse, collections, gzip, itertools, os, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
import italian16_corpus as ic  # noqa: E402
from italian_ngram import fold, paragraphs  # noqa: E402



def ref_vocab():
    c = collections.Counter()
    for p in sorted((HERE.parent / "it16").glob("*.txt")):
        c.update(re.findall(r"[a-z]+", fold(p.read_text(encoding="utf-8", errors="replace"))))
    return c


def _variants(lw):
    """Every reading of lw with each `f` kept, read as long s, or (before `l`) `fl` read as the st ligature."""
    out = [""]
    i = 0
    while i < len(lw):
        ch = lw[i]
        if ch == "f" and i + 1 < len(lw) and lw[i + 1] == "l":
            out = [o + x for o in out for x in ("fl", "sl", "st")]; i += 2; continue
        if ch == "f":
            out = [o + x for o in out for x in ("f", "s")]
        else:
            out = [o + ch for o in out]
        i += 1
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
    if best is None or bc < 3 * max(base, 1):
        return word
    return best.capitalize() if word[:1].isupper() else best


def chunks(text, minw=60):
    """OCR paragraphs, short ones (one printed line between blank lines, as in the 1564 print) merged until minw words."""
    buf = []
    for par in paragraphs(text):
        buf.append(par)
        if sum(len(x.split()) for x in buf) >= minw:
            yield " ".join(buf); buf = []
    if buf:
        yield " ".join(buf)


def keep_relaxed(par):
    w = re.findall(r"[a-z]+", fold(par))
    n = len(w)
    if n < 15:
        return False
    p = sum(1 for x in w if x in ic.PERIOD)
    m = sum(1 for x in w if x in ic.MODERN and x != "ed")
    f = sum(1 for x in w if x in ic.FOREIGN)
    f += sum(1 for x in w if len(x) > 3 and re.search(r"(orum|arum|ibus|unt)$", x))
    fr = sum(1 for x in w if x in {"les", "des", "du", "au", "aux", "est", "que", "qu", "une", "sur", "mais", "ont", "leur", "cette"})
    junk = sum(1 for x in re.findall(r"\S+", par) if not re.search(r"[A-Za-zÀ-ÿ]{2}", x))
    return (p >= 0.15 * n and m <= max(1, 0.03 * n) and f <= 0.03 * n and fr <= 0.02 * n and junk <= 0.25 * n
            and par.count("]") < 2)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--raw", required=True)
    a = ap.parse_args()
    voc = ref_vocab()
    ids = [l.split("\t")[0] for l in (HERE / "MANIFEST.tsv").read_text().splitlines()[1:] if l.strip()]
    for ident in ids:
        text = (Path(a.raw) / f"{ident}.txt").read_text(encoding="utf-8", errors="replace")
        text = re.sub(r"-\s*\n\s*", "", text)
        text = re.sub(r"[A-Za-zÀ-ÿſ]+", lambda m: longs(m.group(0).replace("ſ", "s"), voc), text)
        kept, tot, out = 0, 0, []
        for par in chunks(text):
            tot += 1
            if ic.keep(par) or keep_relaxed(par):
                ws = [x for x in re.split(r"[^a-z]+", fold(par)) if x]
                out.append(" ".join(ws)); kept += 1
        body = "\n".join(out) + "\n"
        with gzip.open(HERE / f"{ident}.txt.gz", "wt", encoding="utf-8") as g:
            g.write(body)
        print(f"{ident}\tkept {kept}/{tot}\tletters {sum(len(re.sub('[^a-z]', '', x)) for x in out)}")


if __name__ == "__main__":
    main()
