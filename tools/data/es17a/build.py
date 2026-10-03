#!/usr/bin/env python3
"""Build tools/data/es17a (1590-1625 Spanish state, diplomatic and court prose) from raw archive.org `_djvu.txt`.

OLD-ES17A (3 Oct 2026, LANE-A1, account 1) for na-oldenbarnevelt-2442-1605 (a 23 Dec 1605 Spanish letter), which the
nearest Spanish corpora on disk miss by register (es17: Cervantes/Quevedo fiction) or by 40 years (es17c: 1643-47).
Same cleaning as tools/data/es18/build.py, whose clean() and long-s repair are imported unchanged; only the reference
vocabulary differs: es17c7 plus the two 19th-century printings of this corpus (Cabrera 1857, San Clemente 1892).
Each file is capped at --cap folded letters (default 650k, the la17 convention) so Cabrera's 2.3 MB does not
dominate the model. MANIFEST.tsv names the files and which get the long-s repair (the 1592/1624/1625 originals).
  python3 tools/data/es17a/build.py --raw DIR
"""
import argparse, collections, gzip, importlib.util, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from judge_plaintext import fold, read_corpus  # noqa: E402

_spec = importlib.util.spec_from_file_location("es18_build", HERE.parent / "es18" / "build.py")
es18 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(es18)


ITALIAN = {"che", "il", "gli", "della", "delle", "dello", "nella", "questo", "questa", "sono", "chi", "piu", "perche", "non", "ho", "hai"}


def ref_vocab(raw, clean_ids):
    c = collections.Counter()
    for p in sorted((HERE.parent / "es17c7").glob("*.txt.gz")):
        c.update(re.findall(r"[a-z]+", es18.fold_words(read_corpus(p))))
    for ident in clean_ids:
        c.update(re.findall(r"[a-z]+", es18.fold_words((Path(raw) / f"{ident}.txt").read_text(encoding="utf-8", errors="replace"))))
    return c


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--raw", required=True, help="directory holding <identifier>.txt raw djvu OCR files")
    ap.add_argument("--cap", type=int, default=650000, help="max folded letters kept per file")
    a = ap.parse_args()
    rows = [l.rstrip("\n").split("\t") for l in (HERE / "MANIFEST.tsv").open(encoding="utf-8")]
    hdr, rows = rows[0], rows[1:]
    rc = hdr.index("longs_repair")
    voc = ref_vocab(a.raw, [r[0] for r in rows if r[rc] != "yes"])
    for r in rows:
        ident = r[0]
        text = (Path(a.raw) / f"{ident}.txt").read_text(encoding="utf-8", errors="replace")
        # drop the Google Books boilerplate preamble (English/Spanish) before cleaning
        text = re.sub(r"(?s)^.{0,6000}?(at http://books\.google\.com/|books\.google\.com/)\s*", "", text, count=1)
        out, kept, tot = es18.clean(text, voc, r[rc] == "yes")
        lines, n = [], 0
        for line in out:
            if sum(1 for t in line.lower().split() if t in ITALIAN) >= 2:  # Perez prints Italian passages
                continue
            lines.append(line); n += len(fold(line))
            if n >= a.cap:
                break
        with gzip.open(HERE / f"{ident}.txt.gz", "wt", encoding="utf-8") as g:
            g.write("\n".join(lines) + "\n")
        print(f"{ident}\tkept_lines {kept}/{tot}\twritten_lines {len(lines)}\tfolded_letters {len(fold(' '.join(lines)))}")


if __name__ == "__main__":
    main()
