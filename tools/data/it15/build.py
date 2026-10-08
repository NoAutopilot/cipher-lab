#!/usr/bin/env python3
"""Build tools/data/it15: 15th-c. Lombard chancery Italian (SFZ-NEXT, 8 Oct 2026) for the Sforza 1446-47 slips
(ciphers/sforza-pusterla-1447-f13 et al.), which it16dip (16th-c. diplomatic letters) does not era-match (rule 3).

Sources (fetched once, raw OCR kept out of the repo; MANIFEST.tsv):
  osio2  Osio, Documenti diplomatici tratti dagli archivj milanesi II (1869), IA bub_gb_XkUAjq5V07wC _djvu.txt
  osio3  the same, III (1872, Visconti documents to 1447), IA bub_gb_88IStucIdgAC _djvu.txt
  asl    Mazzatinti, Archivio storico lombardo X (1883), OCR asl1883.txt from dbourdeau/cyphersolver
         targets/it1583/ (text CC BY 4.0, credited; the 19th-c. editorial prose is dropped by the filter)
Filter: tools/italian_ngram.py's paragraphs() + archaic_ratio() with its own corpus rule (n >= 12, archaic >= 3,
archaic >= 1.0 x (modern + 1), foreign/Latin <= 12%), i.e. its `corpus --min-ratio 1.0` (the sforza-maino-1446 recipe).
Leak guard: a paragraph sharing any 30-letter shingle with a Pusterla clear text used as a key unit (--exclude files:
ciphers/sforza-italien1584-1447/pusterla/clear_*.txt) is dropped, so Osio's print of the f.71 letter is not in the model.
Folds: six files. Osio II keeps only 67 Italian paragraphs (its documents are mostly Latin), so it is one file; Osio III
is cut in four quarters by paragraph order (osio3a-d, roughly chronological); asl is one file. Quarters of one volume are
NOT independent sources -- read the per-fold spread in README.md with that in mind.
Output: one paragraph per line, folded lower-case words (accents stripped, j->i kept as is), gzipped.
  python3 tools/data/it15/build.py --raw DIR [--exclude FILE ...]
"""
import argparse, gzip, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from italian_ngram import paragraphs, archaic_ratio, fold  # noqa: E402

SRC = [("osio2", "bub_gb_XkUAjq5V07wC_djvu.txt", 1), ("osio3", "bub_gb_88IStucIdgAC_djvu.txt", 4), ("asl", "asl1883.txt", 1)]


def letters(s):
    return re.sub(r"[^a-z]", "", fold(s))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--raw", required=True)
    ap.add_argument("--exclude", nargs="*", default=[])
    a = ap.parse_args()
    shingles = set()
    for f in a.exclude:
        t = letters(" ".join(l for l in open(f, encoding="utf-8") if not l.startswith("#")))
        shingles |= {t[i:i + 30] for i in range(0, max(0, len(t) - 29))}
    rows = []
    for name, fn, parts in SRC:
        text = open(Path(a.raw) / fn, "rb").read().decode("utf-8", errors="replace")
        text = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", text)  # rejoin hyphenated line breaks
        kept, total, leak = [], 0, 0
        for par in paragraphs(text):
            total += 1
            A, M, F, n = archaic_ratio(par)
            if n < 12 or A < 3 or A < 1.0 * (M + 1) or F > 0.12 * n or par.count("]") >= 2:
                continue
            t = letters(par)
            if shingles and any(t[i:i + 30] in shingles for i in range(0, max(0, len(t) - 29), 5)):
                leak += 1; continue
            kept.append(" ".join(re.findall(r"[a-z]+", fold(par))))
        cuts = [round(k * len(kept) / parts) for k in range(parts + 1)]
        for k in range(parts):
            suf, part = ("" if parts == 1 else "abcd"[k]), kept[cuts[k]:cuts[k + 1]]
            out = HERE / f"{name}{suf}.txt.gz"
            with gzip.open(out, "wt", encoding="utf-8") as g:
                g.write("\n".join(part) + "\n")
            nl = sum(len(letters(p)) for p in part)
            rows.append(f"{name}{suf}\t{fn}\t{len(part)}\t{nl}")
        print(f"{name}: kept {len(kept)}/{total} paragraphs, {leak} dropped by the leak guard", file=sys.stderr)
    (HERE / "MANIFEST.tsv").write_text("file\tsource\tparagraphs\tletters\n" + "\n".join(rows) + "\n")
    print("\n".join(rows))


if __name__ == "__main__":
    main()
