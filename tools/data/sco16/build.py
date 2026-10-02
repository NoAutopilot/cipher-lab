#!/usr/bin/env python3
"""Build tools/data/sco16 (1550-1600 Middle Scots prose) from raw archive.org `_djvu.txt`.

GAPS6-moray-wood-1568 (2 Oct 2026, account-4), the V6-PTCORP pattern (tools/data/pt18, es18/build.py) for a 13 July
1568 Scots cipher postscript (ciphers/moray-wood-1568) whose nearest corpus on disk (tools/data/en16_repo, ~104k letters
of 1650s English Thurloe readings, no README) is ~90 years off and a different language variety. Reads the raw OCR files
named in MANIFEST.tsv from --raw DIR (raw_<identifier>.txt), then per file:
  1. rejoins words hyphenated across OCR lines;
  2. long-s repair (es18/build.py's rule, imported) for files marked longs_repair=yes (the 1833 Bannatyne Club Diurnal,
     printed with long s: "caftell", "faid"), against a reference vocabulary built from the other, long-s-free files;
  3. keeps an OCR line only when it has >= 4 word tokens and at least half of its 3+-letter tokens are in that vocabulary;
  4. register filter: kept lines are grouped in chunks of 15; a chunk is kept only when its Scots spelling markers
     (thair, thame, quhilk, quhen, quha, sall, efter, nocht, ...) are at least as many as its modern-English markers
     (their, them, which, when, who, shall, after, not, ...) -- drops the 19th-c. editors' introductions and notes;
  5. stops a file at 700,000 folded letters (no source dominates the model, the es18 San Felipe lesson);
  6. writes <identifier>.txt.gz (judge_plaintext folds letters itself).
Never add ciphers/moray-wood-1568 material, Aymeloglu's or Bourdeau's Scots corpora, or any Moray-to-Wood letter here.
  python3 tools/data/sco16/build.py --raw DIR
"""
import argparse, collections, gzip, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1])); sys.path.insert(0, str(HERE.parent / "es18"))
from judge_plaintext import fold  # noqa: E402
from build import WORD, fold_words, longs  # noqa: E402  (tools/data/es18/build.py)

SCOTS = set("thair thame quhilk quhilkis quhen quha quhair quhat quhome quhais quhill ane sall suld sould efter nocht fra "
            "aganis sic maist haill thairof thairfoir thairin heirof wes thay thai thir gif quhy".split())
MODERN = set("their them which when who whom where what shall should after not from against such most whole therefore "
             "they these whose while its been has would".split())


def clean(text, voc, repair, chunk=15, cap=700000):
    text = re.sub(r"-\s*\n\s*", "", text)
    if repair:
        text = WORD.sub(lambda m: longs(m.group(0).replace("ſ", "s"), voc), text)
    lines, tot = [], 0
    for line in text.splitlines():
        toks = WORD.findall(line)
        if len(toks) < 4:
            continue
        tot += 1
        lt = [fold(t) for t in toks if len(t) >= 3]
        if lt and sum(1 for t in lt if t in voc) / len(lt) >= 0.5:
            lines.append(toks)
    out, n = [], 0
    for i in range(0, len(lines), chunk):
        if n >= cap:
            break
        ws = [fold(t) for toks in lines[i:i + chunk] for t in toks]
        s, m = sum(w in SCOTS for w in ws), sum(w in MODERN for w in ws)
        if s >= m and s > 0:
            out.extend(" ".join(t) for t in lines[i:i + chunk]); n += len(fold("".join(ws)))
    return out, len(lines), tot


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--raw", required=True, help="directory holding raw_<identifier>.txt djvu OCR files")
    a = ap.parse_args()
    rows = [l.rstrip("\n").split("\t") for l in (HERE / "MANIFEST.tsv").open(encoding="utf-8")]
    hdr, rows = rows[0], rows[1:]
    rc = hdr.index("longs_repair")
    voc = collections.Counter()
    for r in rows:
        if r[rc] != "yes":
            voc.update(fold_words((Path(a.raw) / f"raw_{r[0]}.txt").read_text(encoding="utf-8", errors="replace")).split())
    for r in rows:
        text = (Path(a.raw) / f"raw_{r[0]}.txt").read_text(encoding="utf-8", errors="replace")
        out, kept, tot = clean(text, voc, r[rc] == "yes")
        with gzip.open(HERE / f"{r[0]}.txt.gz", "wt", encoding="utf-8") as g:
            g.write("\n".join(out) + "\n")
        print(f"{r[0]}\tvocab_lines {kept}/{tot}\tscots_lines {len(out)}\tfolded_letters {len(fold(' '.join(out)))}")


if __name__ == "__main__":
    main()
