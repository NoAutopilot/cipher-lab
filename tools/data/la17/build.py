#!/usr/bin/env python3
"""Build tools/data/la17 (Latin letters of scholar-diplomats and the Swedish crown's agents, about 1590-1649) from raw archive.org `_djvu.txt`.

GAPS57 (3 Oct 2026, account-4), the TOOL-FR17 / V6-PTCORP pattern, for ciphers/riksarkivet-r4282-1628 (a 1628
Swedish-court cipher letter, clear word "expensas"), whose judge fell back to la18 (Zaluski, 1709-11 Polish chancery).
Every source prints the period letters in their own Latin (OCR keeps the long s as f, exactly as la18's Zaluski scans do,
so the two corpora carry the same noise). Reads raw_<identifier>.txt from --raw DIR, then per file:
  1. rejoins words hyphenated across OCR lines;
  2. keeps an OCR line only when it has >= 4 word tokens;
  3. register filter: kept lines in chunks of 15 (--chunk); a chunk is kept only when Latin function words
     (et in ad non cum ut quod qui quae sed ...) make up >= 12 pct of its tokens (--min-latin) -- drops French, Dutch,
     German and Greek letters, editors' vernacular prefaces, indexes, and runs of mangled OCR; and only when its e count is
     >= 1.5 x its c count (real Latin about 2.3x): some scans read e as c ("ct", "cxfpcctationc"). The 1687 Grotius
     Epistolae (bub_gb_7cDeih1PbMkC, e 2.7 pct / c 11.4 pct after filtering) and L. Camerarius 1625 (10514355bsb, 2.7k
     letters survive) were fetched and dropped for OCR (README);
  4. stops a file at 650,000 folded letters (no source dominates the model);
  5. writes <identifier>.txt.gz (judge_plaintext folds letters itself).
Never add the target letter (Riksarkivet R4282, DECODE 4282), its sibling R4284, or a source that prints a decipherment of
either. python3 tools/data/la17/build.py --raw DIR
"""
import argparse, gzip, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from judge_plaintext import fold  # noqa: E402

WORD = re.compile(r"[^\W\d_]+", re.UNICODE)
FILES = ["hugonisgrotiiepi00grot", "hugonisgrotiiad00oxengoog", "bub_gb_WTkBFjX6G_UC", "bub_gb_FK3cWikzFwsC",
         "bub_gb_mBpUAAAAcAAJ", "epistolaecelebe00grotgoog"]
LATIN = set("et in ad non cum ut quod qui quae quam sed est esse eft effe atque ac nec neque si de ex per a ab pro "
            "me te se nos vos nobis vobis tibi mihi ille illi hoc haec hic ita enim etiam vel aut tamen jam iam".split())


def latin_share(words):
    words = [w.lower() for w in words]
    return sum(w in LATIN for w in words) / max(1, len(words))


def clean(text, chunk=15, cap=650000, min_latin=0.12):
    text = re.sub(r"-\s*\n\s*", "", text)
    lines = [WORD.findall(l) for l in text.splitlines() if "google" not in l.lower()]
    lines = [t for t in lines if len(t) >= 4]
    out, n = [], 0
    for i in range(0, len(lines), chunk):
        if n >= cap:
            break
        block = lines[i:i + chunk]
        letters = fold("".join(w for t in block for w in t))
        if latin_share(w for t in block for w in t) >= min_latin and letters.count("e") >= 1.5 * letters.count("c"):
            out.extend(" ".join(t) for t in block)
            n += sum(len(fold("".join(t))) for t in block)
    return out, n, len(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--raw", required=True, help="directory holding raw_<identifier>.txt djvu OCR files")
    ap.add_argument("--chunk", type=int, default=15)
    ap.add_argument("--min-latin", type=float, default=0.12)
    a = ap.parse_args()
    for ident in FILES:
        raw = (Path(a.raw) / f"raw_{ident}.txt").read_text(encoding="utf-8", errors="replace")
        out, n, tot = clean(raw, chunk=a.chunk, min_latin=a.min_latin)
        with gzip.open(HERE / f"{ident}.txt.gz", "wt", encoding="utf-8") as fh:
            fh.write("\n".join(out) + "\n")
        print(f"{ident}\tlines_kept={len(out)}/{tot}\tfolded_letters={n}")


if __name__ == "__main__":
    main()
