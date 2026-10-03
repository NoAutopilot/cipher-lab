#!/usr/bin/env python3
"""Build tools/data/de1600 (German princely letters and chancery acts of about 1567-1611) from raw archive.org `_djvu.txt`.

CORP-DE16 (3 Oct 2026, account-4), the de17 (GAPS62) pattern, for ciphers/decode-1411-hhsta-vienna-1600 (a c.1575-1600
Habsburg court/chancery cipher letter in German), whose judge under de17 (1630-1660) could not recognise even the leaf's own
period gloss. The sources are 19th-century source editions that print the letters and acts in their own spelling (vnd/unnd,
dz, seind, wöllen, gnedig, uff, nit), beside the editors' own 1870s-1900s German (introductions, headnotes, regests), so a
filter keeps only chunks that read as period text. Reads raw_<identifier>.txt from --raw DIR, then per file:
  1. rejoins words hyphenated across OCR lines; maps long s to s;
  2. keeps an OCR line only when it has >= 4 word tokens; drops lines with "google";
  3. register filter on chunks of 8 lines (--chunk): German function words >= 12 pct of tokens (--min-german; drops
     Latin, French, Italian and mangled OCR) AND >= 2 period-spelling markers per chunk (--min-period; the 1880s editors
     never write vnd, dz, seind, wöllen, gnedig, uff, nit, sambt ...);
  4. stops a file at 450,000 folded letters (no source dominates the model);
  5. writes <identifier>.txt.gz.
Never add the target (DECODE R1411, HHStA Staatskanzlei Interiora Chiffrenschluessel Kt. 14 Fasc. 20), its sibling leaves,
or a source that prints a decipherment of any of them. python3 tools/data/de1600/build.py --raw DIR
"""
import argparse, gzip, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from judge_plaintext import fold  # noqa: E402

WORD = re.compile(r"[^\W\d_]+", re.UNICODE)
FILES = ["briefedespfalzgr01joha", "briefedespfalzgr02joha", "bub_gb_zc4FAAAAQAAJ",
         "bub_gb_6M4FAAAAQAAJ", "briefeundactenz01mayrgoog", "bub_gb__s4FAAAAQAAJ"]
# dropped (README): fuggerzeitungenu00klaruoft (Klarwill 1923 modernises the spelling), bub_gb_3U8VAAAAYAAJ (Kluckhohn,
# Briefe Friedrich des Frommen: Fraktur OCR unreadable, "feine brin gefatyr guroegent")
GERMAN = set("und vnd unnd der die das zu in den von mit sich nicht nit ist auf auch als es dem des ein eine so daß dass dz "
             "wir sie er ich ir ihr wie sein an aus bei bey nach wird werden haben hat sollen soll wollen wöllen wol solches".split())
PERIOD = set("vnd unnd vnnd dz seind seyen seie dero derowegen dahero umb darumb warumb nit uff auff uf alß sambt itzo "
             "jetzo itzt iezo jezo gnedig gnedigen gnedigst gnediger gnedigsten underthenig unterthenig underthenigst "
             "wöllen wöllten wölle het hett ime imme inen ine irer iren irem khay kay mt durchleuchtig vns vnser vnsere "
             "wirdt wurdt vleis vleissig bevelch befelch bevelhen allain maist maistes vil dise dises disem disen diser "
             "gwalt thuen dieweil sonderlich gleichwol sovil wievil derselbig dasselbig selbig ewer ewr eur zwai zway "
             "khunden khonnen khumen gelt solt ward warde hievor hernach bericht bey sey seye".split())


def share(words, vocab):
    words = [w.lower() for w in words]
    hits = sum(w in vocab for w in words)
    return hits / max(1, len(words)), hits


def clean(text, chunk=8, cap=450000, min_german=0.12, min_period=2):
    text = re.sub(r"-\s*\n\s*", "", text.replace("ſ", "s"))
    lines = [WORD.findall(l) for l in text.splitlines() if "google" not in l.lower()]
    lines = [t for t in lines if len(t) >= 4]
    out, n = [], 0
    for i in range(0, len(lines), chunk):
        if n >= cap:
            break
        block = lines[i:i + chunk]
        words = [w for t in block for w in t]
        g, _ = share(words, GERMAN)
        _, p = share(words, PERIOD)
        if g >= min_german and p >= min_period:
            out.extend(" ".join(t) for t in block)
            n += sum(len(fold("".join(t))) for t in block)
    return out, n, len(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--raw", required=True, help="directory holding raw_<identifier>.txt djvu OCR files")
    ap.add_argument("--chunk", type=int, default=8)
    ap.add_argument("--min-german", type=float, default=0.12)
    ap.add_argument("--min-period", type=int, default=2)
    a = ap.parse_args()
    for ident in FILES:
        raw = (Path(a.raw) / f"raw_{ident}.txt").read_text(encoding="utf-8", errors="replace")
        out, n, tot = clean(raw, chunk=a.chunk, min_german=a.min_german, min_period=a.min_period)
        with gzip.open(HERE / f"{ident}.txt.gz", "wt", encoding="utf-8") as fh:
            fh.write("\n".join(out) + "\n")
        print(f"{ident}\tlines_kept={len(out)}/{tot}\tfolded_letters={n}")


if __name__ == "__main__":
    main()
