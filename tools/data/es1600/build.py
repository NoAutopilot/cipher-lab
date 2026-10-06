#!/usr/bin/env python3
"""Build tools/data/es1600 (1598-1621 Spanish state letters, CODOIN 19th-century printing) from raw archive.org `_djvu.txt`.

R12-OLDCORP (6 Oct 2026, LANE-RUN12-account-2) for na-oldenbarnevelt-2442-1605 (a 23 Dec 1605 Spanish letter), step (d')
of its NOTES.md section 12: es17a (1590-1625) mixes two 19th-century printings with three long-s originals, and its
leave-one-file-out spread (22.5-97%) reflects that. This corpus takes one register and one printing kind instead: the
*Coleccion de documentos ineditos para la historia de Espana* (CODOIN, 1842-95), archive.org `coleccindedocuNNmadruoft`.
Rules fixed in ciphers/na-oldenbarnevelt-2442-1605/transcription/PREREG_R12-OLDCORP.md before the build:
  --survey : per volume, the share of four-digit years 1500-1700 that fall in 1598-1621 (candidate when >= 0.40).
  build    : within each MANIFEST.tsv volume keep text from a line naming a year in 1598-1621 up to the next line naming a
             1500-1700 year outside it; drop footnote lines ("(1) ..."), lines with >= 2 Latin/Italian/French function
             words, and hold-out names (Senisteros, Cisneros, Juan de la Pena); then tools/data/es18/build.py's clean()
             unchanged (no long-s repair; reference vocabulary es17c7 + es17a); cap 650k folded letters per file.
  python3 tools/data/es1600/build.py --raw DIR --survey     # writes nothing
  python3 tools/data/es1600/build.py --raw DIR              # writes <id>.txt.gz for the MANIFEST.tsv rows
"""
import argparse, collections, gzip, importlib.util, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from judge_plaintext import fold, read_corpus  # noqa: E402

_spec = importlib.util.spec_from_file_location("es18_build", HERE.parent / "es18" / "build.py")
es18 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(es18)

YEAR = re.compile(r"(?<!\d)(1[5-6]\d\d|1700)(?!\d)")
LO, HI = 1598, 1621
FOREIGN = {"che", "il", "gli", "della", "delle", "nella", "questo", "sono", "perche", "et", "est", "ad", "quod", "cum",
           "sunt", "nobis", "vobis", "le", "les", "du", "des", "aux", "avec", "nous", "vous", "qui", "dans", "ont", "sont"}
HOLDOUT = re.compile(r"seniste|cisneros|juan de la pe[nñ]a", re.I)
FOOTNOTE = re.compile(r"^\s*\(\s*\d\s*\)")


def share(text):
    ys = [int(y) for y in YEAR.findall(text)]
    inw = sum(1 for y in ys if LO <= y <= HI)
    return inw, len(ys)


def window(text):
    """Keep lines from an in-window year line to the next out-of-window (1500-1700) year line."""
    keep, on = [], False
    for line in text.splitlines():
        ys = [int(y) for y in YEAR.findall(line)]
        if ys:
            if any(LO <= y <= HI for y in ys):
                on = True
            elif all(not (LO <= y <= HI) for y in ys):
                on = False
        if on:
            keep.append(line)
    return "\n".join(keep)


def ref_vocab():
    c = collections.Counter()
    for d in ("es17c7", "es17a"):
        for p in sorted((HERE.parent / d).glob("*.txt.gz")):
            c.update(re.findall(r"[a-z]+", es18.fold_words(read_corpus(p))))
    return c


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--raw", required=True, help="directory holding <identifier>.txt raw djvu OCR files")
    ap.add_argument("--survey", action="store_true", help="print each volume's in-window year share; write nothing")
    ap.add_argument("--cap", type=int, default=650000)
    ap.add_argument("--min-letters", type=int, default=100000)
    a = ap.parse_args()
    if a.survey:
        for p in sorted(Path(a.raw).glob("*.txt")):
            t = p.read_text(encoding="utf-8", errors="replace"); inw, n = share(t)
            print(f"{p.stem}\tyears {n}\tin_window {inw}\tshare {inw / n if n else 0:.3f}\twindow_letters {len(fold(window(t)))}")
        return
    rows = [l.rstrip("\n").split("\t") for l in (HERE / "MANIFEST.tsv").open(encoding="utf-8")][1:]
    voc = ref_vocab()
    for r in rows:
        ident = r[0]
        t = window((Path(a.raw) / f"{ident}.txt").read_text(encoding="utf-8", errors="replace"))
        pre = []
        for line in t.splitlines():
            if FOOTNOTE.match(line) or HOLDOUT.search(line):
                continue
            if sum(1 for w in re.findall(r"[a-zà-ÿ]+", line.lower()) if w in FOREIGN) >= 2:
                continue
            pre.append(line)
        out, kept, tot = es18.clean("\n".join(pre), voc, False)
        lines, n = [], 0
        for line in out:
            lines.append(line); n += len(fold(line))
            if n >= a.cap:
                break
        if n < a.min_letters:
            print(f"{ident}\tDROPPED folded_letters {n} < {a.min_letters}"); continue
        with gzip.open(HERE / f"{ident}.txt.gz", "wt", encoding="utf-8") as g:
            g.write("\n".join(lines) + "\n")
        print(f"{ident}\tkept_lines {kept}/{tot}\twritten_lines {len(lines)}\tfolded_letters {n}")


if __name__ == "__main__":
    main()
