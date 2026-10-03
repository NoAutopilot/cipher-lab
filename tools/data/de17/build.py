#!/usr/bin/env python3
"""Build tools/data/de17 (German chancery and diplomatic prose of about 1630-1660) from raw archive.org `_djvu.txt`.

GAPS62 (3 Oct 2026, account-4), the la17 / TOOL-FR17 pattern, for ciphers/riksarkivet-r4282-1628 (a 1628 Swedish-court
cipher letter; the Swedish chancery wrote German as well as Latin), whose German judge would otherwise fall back to de16 (an
8.5 KB model-composed text) or de19/de20 (19th-20th c.). The sources are 19th-century source editions that print the
period letters and acts in their own words (u/v and i/j regularised by the editors, otherwise period spelling: seind, dero,
umb, derowegen, nit). The editions also carry the editors' own 1860s-1880s German (introductions, headnotes, regests), so
the filter keeps only chunks that read as period text. Reads raw_<identifier>.txt from --raw DIR, then per file:
  1. rejoins words hyphenated across OCR lines; maps long s to s (judge_plaintext.fold drops it otherwise);
  2. keeps an OCR line only when it has >= 4 word tokens; drops lines with "google";
  3. register filter on chunks of 15 lines (--chunk): German function words (und der die das zu in den von mit ...)
     >= 12 pct of tokens (--min-german; drops Latin, French, Italian and mangled OCR) AND period-spelling markers
     (seind seyn dero deroselben derowegen umb darumb nit uff auff alß sambt itzo jetzo anitzo gnedig ...) >= 2 per
     chunk (--min-period; drops most editorial 19th-century prose, which never uses them);
  4. stops a file at 450,000 folded letters (no source dominates the model);
  5. writes <identifier>.txt.gz.
Never add the target letter (Riksarkivet R4282, DECODE 4282), its sibling R4284, or a source that prints a decipherment of
either. python3 tools/data/de17/build.py --raw DIR
"""
import argparse, gzip, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from judge_plaintext import fold  # noqa: E402

WORD = re.compile(r"[^\W\d_]+", re.UNICODE)
FILES = ["dieverhandlungen01irme", "dieverhandlungen02irme", "dieverhandlungen03irme",
         "urkundenundacten1601berluoft", "urkundenundacte32kommgoog"]  # bub_gb_PggKAAAAIAAJ dropped (README)
GERMAN = set("und der die das zu in den von mit sich nicht ist auf auch als es dem des ein eine so daß dass dasz wir sie "
             "er ich ihr wie sein zu an aus bei nach wird werden haben hat sollen soll wollen wol wohl solches".split())
PERIOD = set("seind seyn sein dero deroselben derowegen dahero umb darumb warumb nit uff auff uf alß alss sambt sammt "
             "itzo jetzo anitzo anietzo gnedig gnedigst gnädigst unterthänigst underthänig hiemit hierbei allhier "
             "solchergestalt dergestalt negst nechst jedoch zuvorderst zumahl wan dan denen thun thut thäte gethan".split())


def share(words, vocab):
    words = [w.lower() for w in words]
    return sum(w in vocab for w in words) / max(1, len(words)), sum(w in vocab for w in words)


def clean(text, chunk=15, cap=450000, min_german=0.12, min_period=2):
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
    ap.add_argument("--chunk", type=int, default=15)
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
