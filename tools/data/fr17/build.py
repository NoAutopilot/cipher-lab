#!/usr/bin/env python3
"""Build tools/data/fr17 (French diplomatic/administrative/epistolary prose, about 1617-1644) from raw archive.org `_djvu.txt`.

TOOL-FR17 (3 Oct 2026, account-4), the V6-PTCORP / sco16 pattern, for 1630s-1650s French targets (first:
ciphers/decode-2754-bnf-baluze156-1636, whose spec fell back to fr16, c.1560-1615). Every source is a 19th-c. critical
edition (Documents inedits / Tamizey de Larroque) that prints the 17th-c. letters in their own spelling (estoit, nostre,
faict) beside the editor's modern-French notes and introductions. Reads raw_<identifier>.txt from --raw DIR, then per file:
  1. rejoins words hyphenated across OCR lines;
  2. keeps an OCR line only when it has >= 4 word tokens (--debris also drops a line whose tokens are more than a third
     1-2 letters; tried 3 Oct 2026 with --chunk 6, it shrank the corpus 29 pct and did not lower the fold rates -- README);
  3. register filter: kept lines are grouped in chunks; a chunk is kept only when its period-spelling markers
     (estoit, avoit, nostre, mesme, estre, faict, -oit/-oient imperfects ...) outnumber-or-equal its modern-spelling markers
     (etait, avait, notre, meme, etre, -ait/-aient ...) and there is at least one; chunks of 15 lines (--chunk) -- drops the editors' notes,
     introductions, indexes and Google/IA boilerplate, which are 19th-c. French;
  4. stops a file at 650,000 folded letters (no source dominates the model, the es18 San Felipe lesson);
  5. writes <identifier>.txt.gz (judge_plaintext folds letters itself).
Never add the target letters themselves (Baluze 155/156 Sabran-circle letters, Lasry's keys' plaintexts) or a source that
prints them. python3 tools/data/fr17/build.py --raw DIR
"""
import argparse, gzip, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from judge_plaintext import fold  # noqa: E402

WORD = re.compile(r"[^\W\d_]+", re.UNICODE)
FILES = ["bub_gb_OIQItRIybmIC", "bub_gb_wBJLsV8B_BgC", "lettresdepeiresc01peiruoft", "lettresdepeiresc02peiruoft",
         "lettresdejeancha01chap", "lettresducardina01maza"]
PERIOD = set("estoit estoient avoit avoient seroit seroient pourroit devoit faisoit vouloit nostre vostre nostres vostres "
             "mesme mesmes estre esté estés estant faict faicte faicts sçavoir sçay sçait aussy ceste cest icy cognoistre "
             "connoistre cognoissance connoissance recognoistre paroistre aultre aultres eust feust fust desja apres "
             "monsr mondict ledict ladicte dict escrit escrire escript".split())
MODERN = set("était étaient avait avaient serait seraient pourrait devait faisait voulait notre votre nôtre vôtre même "
             "mêmes être étant fait faite savoir sais sait aussi cette ici connaître connaissance reconnaître paraître "
             "autre autres eût fût déjà après écrit écrire".split())
NOT_IMPF = set("soit voit doit droit froit croit fait sait plait mais jamais".split())


def markers(words):
    p = m = 0
    for w in words:
        w = w.lower()
        if w in PERIOD:
            p += 1
        elif w in MODERN:
            m += 1
        elif len(w) > 4 and w not in NOT_IMPF and (w.endswith("oit") or w.endswith("oient")):
            p += 1
        elif len(w) > 4 and w not in NOT_IMPF and (w.endswith("ait") or w.endswith("aient")):
            m += 1
    return p, m


def clean(text, chunk=15, cap=650000, debris=False):
    text = re.sub(r"-\s*\n\s*", "", text)
    lines = [WORD.findall(l) for l in text.splitlines()]
    lines = [t for t in lines if len(t) >= 4 and not (debris and sum(len(w) <= 2 for w in t) * 3 > len(t))]
    out, n = [], 0
    for i in range(0, len(lines), chunk):
        if n >= cap:
            break
        block = lines[i:i + chunk]
        p, m = markers(w for t in block for w in t)
        if p >= m and p > 0:
            out.extend(" ".join(t) for t in block)
            n += sum(len(fold("".join(t))) for t in block)
    return out, n, len(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--raw", required=True, help="directory holding raw_<identifier>.txt djvu OCR files")
    ap.add_argument("--chunk", type=int, default=15, help="lines per register-filter chunk (default 15, the committed build)")
    ap.add_argument("--debris", action="store_true", help="also drop OCR-debris lines (not used for the committed build)")
    a = ap.parse_args()
    for ident in FILES:
        raw = (Path(a.raw) / f"raw_{ident}.txt").read_text(encoding="utf-8", errors="replace")
        out, n, tot = clean(raw, chunk=a.chunk, debris=a.debris)
        with gzip.open(HERE / f"{ident}.txt.gz", "wt", encoding="utf-8") as fh:
            fh.write("\n".join(out) + "\n")
        print(f"{ident}\tlines_kept={len(out)}/{tot}\tletters_after_fold={n}")


if __name__ == "__main__":
    main()
