#!/usr/bin/env python3
"""Build tools/data/nl16 (Dutch prose of 1569-1589 in its own spelling) from raw DBNL plain-text downloads.

NL16-11106 (8 Oct 2026, LANE FAMILY, account 2), the de1600 (CORP-DE16) pattern, for ciphers/wvo-11106-bergh-1572 (a 19 Sept
[1572] cipher letter from Willem van den Bergh to Willem van Oranje), whose homophonic family had no era-matched Dutch corpus:
nl18 is 1770-1799, nl20 1880-1940, nl_dev a modern Bible, nl_repo targets' own readings. The sources are DBNL
(dbnl.org/nieuws/text.php?id=ID) diplomatic or near-diplomatic editions of Marnix, Coornhert and Spieghel; each file also
carries the editors' 1858-2007 introductions and notes, so a filter keeps only chunks that read as period text. Reads
raw_<id>.txt from --raw DIR, then per file:
  1. drops DBNL page markers ({==12==} {>>pagina-aanduiding<<}) and the TEI header (everything before "Verantwoording");
  2. splits the text into chunks of --chunk word tokens (default 80);
  3. keeps a chunk when Dutch function words are >= 15 pct of its tokens (--min-dutch; drops Latin, French and mangled lines)
     AND it has >= 3 period-spelling markers (--min-period: ende, ofte, wt, ick, welck, oock, sulcx, vande, inden, totten, gh-
     prefixed words ...; the 1858-2007 editors never write them)
     AND it has < 3 modern-only words (hij, zij, wij, ook, uitgave, werd, zijne ...: the editors' own Dutch);
  4. stops a file at 450,000 folded letters (no source dominates the model);
  5. writes <id>.txt.gz.
Never add the target (KHA A 11/XIV, WVO 11106), its neighbours, or a source that prints a decipherment of it.
python3 tools/data/nl16/build.py --raw DIR
"""
import argparse, gzip, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from judge_plaintext import fold  # noqa: E402

WORD = re.compile(r"[^\W\d_]+", re.UNICODE)
# kept out as the offline test's held-out source: cice001offi01 (Coornhert, Officia Ciceronis, 1561)
FILES = ["marn001bien01", "marn001trou01", "coor001zede01", "spie001twes01", "coor001boev01"]
DUTCH = set("ende en de het een van in te dat die is niet met hy hi sy zy wy ghy op als so soo zo voor aen aan maer maar door "
            "oock ook al tot uyt wt hem haer hun sijn zyn syn was wert wordt worden heeft hebben dan ofte of wel ick ik dit deze dese "
            "welck welcke daer daar wat noch nochtans".split())
PERIOD = set("ende ofte oft wt vut ick welck welcke welcken elck elcken oock ooc sulcx sulcke sulcken sulck dese desen int "
             "vande vanden inde inden opt totten metten tselve alsoo mits naer gheen gheene ghy hy sy zy wy oyt nyet niemant "
             "sijnder haerder daerom daeromme waerom daer waer maer gaen staen aen haer seer seyde gelijck ghelijck "
             "zulcks zulck dinck wesen weesen".split())
# modern-only words (the editors' Dutch; the 1569-1589 texts write hy/hi, zy/sy, wy, oock/óóck, wert): a chunk with >= 3 is dropped
MODERN = set("hij zij wij ook uitgave werd zijne zijner zich blz bladzijde druk editie herdruk tekst eeuw schrijver".split())
# not markers (the 1858-1942 editors also write them): eenen, zoo, menschen, dingen, hoe, vry


def share(words, vocab):
    words = [w.lower() for w in words]
    hits = sum(w in vocab or (vocab is PERIOD and w.startswith("gh") and len(w) > 3) for w in words)
    return hits / max(1, len(words)), hits


def clean(text, chunk=80, cap=450000, min_dutch=0.15, min_period=3):
    k = text.find("Verantwoording")
    text = text[k:] if k >= 0 else text
    text = re.sub(r"\{==[^}]*==\}|\{>>[^}]*<<\}", " ", text)
    text = re.sub(r"-\s*\n\s*", "", text.replace("ſ", "s"))
    words = WORD.findall(text)
    out, n = [], 0
    for i in range(0, len(words), chunk):
        if n >= cap:
            break
        block = words[i:i + chunk]
        d, _ = share(block, DUTCH)
        _, p = share(block, PERIOD)
        _, m = share(block, MODERN)
        if d >= min_dutch and p >= min_period and m < 3:
            out.append(" ".join(block))
            n += len(fold("".join(block)))
    return out, n, (len(words) + chunk - 1) // chunk


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--raw", required=True, help="directory holding raw_<id>.txt DBNL text downloads")
    ap.add_argument("--chunk", type=int, default=80)
    ap.add_argument("--min-dutch", type=float, default=0.15)
    ap.add_argument("--min-period", type=int, default=3)
    a = ap.parse_args()
    for ident in FILES:
        raw = (Path(a.raw) / f"raw_{ident}.txt").read_text(encoding="utf-8", errors="replace")
        out, n, tot = clean(raw, chunk=a.chunk, min_dutch=a.min_dutch, min_period=a.min_period)
        with gzip.open(HERE / f"{ident}.txt.gz", "wt", encoding="utf-8") as fh:
            fh.write("\n".join(out) + "\n")
        print(f"{ident}\tchunks_kept={len(out)}/{tot}\tfolded_letters={n}")


if __name__ == "__main__":
    main()
