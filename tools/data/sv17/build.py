#!/usr/bin/env python3
"""Build tools/data/sv17 (Swedish chancery letters of about 1620-1650) from raw archive.org `_djvu.txt`.

GAPS67 (3 Oct 2026, account-4), the de17 / la17 pattern, for ciphers/riksarkivet-r4282-1628 (a 1628 Swedish-court cipher
letter whose homophonic tests into Latin, German and French were control-backed negatives), which had no Swedish judge
corpus at all. The source is Rikskansleren Axel Oxenstiernas skrifter och brefvexling (AOSB, 1888-1897 Google scans),
which prints the chancellor's and his correspondents' letters in their own words and spelling (medh, uthi, thet, migh,
haffuer, effter) but mixes in Latin and German letters and the editors' own 1880s Swedish (headnotes, notes: med, det,
hvad). Reads raw_<identifier>.txt from --raw DIR, then per file:
  1. rejoins words hyphenated across OCR lines; maps long s to s and å to a (judge_plaintext.fold has no å and would
     drop it; ä and ö fold to ae and oe there);
  2. keeps an OCR line only when it has >= 4 word tokens; drops lines with "google";
  3. register filter on chunks of 15 lines (--chunk): Swedish function words (och att som the then det en af på til
     för icke eller jag han wij så är ...) >= 12 pct of tokens (--min-swedish; drops Latin, German, French) AND
     period-spelling markers (medh uthi thet thenne thesse migh sigh tigh effter haffuer hafwer hwad hwilket ähr wore
     ...) >= 3 per chunk (--min-period; drops most editorial prose, which spells med, det, mig, sig, efter, hafva);
  4. stops a file at 450,000 folded letters (no source dominates the model);
  5. writes <identifier>.txt.gz.
Never add the target letter (Riksarkivet R4282, DECODE 4282), its sibling R4284, or a source that prints a decipherment of
either. python3 tools/data/sv17/build.py --raw DIR
"""
import argparse, gzip, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from judge_plaintext import fold  # noqa: E402

WORD = re.compile(r"[^\W\d_]+", re.UNICODE)
FILES = ["rikskanslerenax00akadgoog", "rikskanslerenax00palagoog", "rikskanslerenax00styfgoog",
         "rikskanslerenax01palagoog", "rikskanslerenax02akadgoog", "rikskanslerenax03akadgoog"]
# rikskanslerenax01styfgoog dropped (German letters to the chancellor, 18 'och' in 2 MB); rikskanslerenax01akadgoog: HTTP 500
SWEDISH = set("och ock att at som the then den det thet en ett af aff på paa til till för icke ike eller jag iag han hon "
              "wij vij wi vi så är ähr ar oss os mig migh sig sigh medh med uthi uti i om ok ther där hwad hvad hans "
              "theres eder edher".split())
PERIOD = set("medh uthi uti thet thenne thesse thetta migh sigh tigh effter epter haffuer hafwer haffwer hafuer hwad "
             "hwilket hwilken hwar hwarföre ähr wore wara warit skole skulle kongl doch någhot thermedh therföre "
             "therhos ifrå sampt samptligen förthenskuld eij ey".split())


def share(words, vocab):
    words = [w.lower() for w in words]
    k = sum(w in vocab for w in words)
    return k / max(1, len(words)), k


def clean(text, chunk=15, cap=450000, min_sw=0.12, min_period=3):
    text = re.sub(r"-\s*\n\s*", "", text.replace("ſ", "s").replace("å", "a").replace("Å", "A"))
    lines = [WORD.findall(l) for l in text.splitlines() if "google" not in l.lower()]
    lines = [t for t in lines if len(t) >= 4]
    out, n = [], 0
    for i in range(0, len(lines), chunk):
        if n >= cap:
            break
        block = lines[i:i + chunk]
        words = [w for t in block for w in t]
        g, _ = share(words, SWEDISH)
        _, p = share(words, PERIOD)
        if g >= min_sw and p >= min_period:
            out.extend(" ".join(t) for t in block)
            n += sum(len(fold("".join(t))) for t in block)
    return out, n, len(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--raw", required=True, help="directory holding raw_<identifier>.txt djvu OCR files")
    ap.add_argument("--chunk", type=int, default=15)
    ap.add_argument("--min-swedish", type=float, default=0.12)
    ap.add_argument("--min-period", type=int, default=3)
    a = ap.parse_args()
    for ident in FILES:
        raw = (Path(a.raw) / f"raw_{ident}.txt").read_text(encoding="utf-8", errors="replace")
        out, n, tot = clean(raw, chunk=a.chunk, min_sw=a.min_swedish, min_period=a.min_period)
        with gzip.open(HERE / f"{ident}.txt.gz", "wt", encoding="utf-8") as fh:
            fh.write("\n".join(out) + "\n")
        print(f"{ident}\tlines_kept={len(out)}/{tot}\tfolded_letters={n}")


if __name__ == "__main__":
    main()
