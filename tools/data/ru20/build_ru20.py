#!/usr/bin/env python3
"""build_ru20.py: clean Internet Archive _djvu.txt OCR of Soviet-era Russian prose into tools/data/ru20 (KAL-RUCORP, 15 Oct 2026).

  python3 tools/data/ru20/build_ru20.py RAW_DIR          (RAW_DIR holds the six _djvu.txt files named in MANIFEST.tsv)

Writes tools/data/ru20/<name>.txt.gz (lower-case Cyrillic, one line per OCR paragraph) and, through tools/translit_ru.py,
tools/data/ru20_lat/s1s/<name>.txt.gz (one file per source, so judge_plaintext.py --holdout has one fold per source).
Cleaning: end-of-line hyphenation joined; Latin look-alike letters inside an otherwise Cyrillic word mapped to Cyrillic;
lines with no Cyrillic word of 2+ letters (page numbers, running heads of digits) dropped. Nothing else is repaired:
OCR misreads stay (one more reason the fold check, not the in-model p05, is the gate).
"""
import gzip, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
LOOK = str.maketrans("aeopcxykmthbABEKMHOPCTXY", "аеорсхукмтнвавекмнорстху")
CYR = re.compile(r"[а-яё]")

def clean(raw):
    raw = re.sub(r"[-­]\s*\n\s*", "", raw)            # join hyphenated line breaks
    out = []
    for line in raw.splitlines():
        words = []
        for w in re.findall(r"[A-Za-zА-Яа-яЁё]+", line):
            if CYR.search(w.lower()):
                w = w.translate(LOOK)
            words.append(w.lower())
        cyr = [w for w in words if re.fullmatch(r"[а-яё]+", w)]
        if any(len(w) >= 2 for w in cyr):
            out.append(" ".join(cyr))
    return "\n".join(out) + "\n"

def main():
    raw_dir = sys.argv[1]
    rows = [l.rstrip("\n").split("\t") for l in open(os.path.join(HERE, "MANIFEST.tsv"), encoding="utf-8")][1:]
    os.makedirs(os.path.join(HERE, "..", "ru20_lat", "s1s"), exist_ok=True)
    for r in rows:
        name, raw = r[0], r[1]
        text = clean(open(os.path.join(raw_dir, raw), encoding="utf-8", errors="replace").read())
        dst = os.path.join(HERE, name + ".txt.gz")
        with gzip.open(dst, "wt", encoding="utf-8") as f:
            f.write(text)
        with tempfile.TemporaryDirectory() as td:
            os.symlink(dst, os.path.join(td, name + ".txt.gz"))
            subprocess.run([sys.executable, os.path.join(ROOT, "tools", "translit_ru.py"), "--scheme", "s1s", td,
                            os.path.join(HERE, "..", "ru20_lat", "s1s", name + ".txt.gz")], check=True)
        print(name, sum(len(re.findall(r"[а-яё]", l)) for l in text.splitlines()), "Cyrillic letters")

if __name__ == "__main__":
    main()
