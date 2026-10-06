#!/usr/bin/env python3
"""R12A-ECKV2 (6 Oct 2026, verifier): per-token grade decision for Leghorn, Legend and Leopard in the sent ledgers mssEC 18-19.

Usage: hurlbut_row_grades.py [--write | --check]

Input: ec18/leghorn_uses.tsv, ec18/legend_uses.tsv, ec18/leopard_uses.tsv (R12A-ECKLEG: every use, aligned or not to its
dated OR ser. I print). Output: ec18/hurlbut_row_grades.tsv, one row per use with the grade decided under rule 4.
--check exits 1 if the committed output is stale, or if any of the three words appears in a committed reading
(ec18/readings.md, ec18/s2/readings.md) or alignment table, since those would then need a carried grade.

The rule (AUDIT.md "Carry-over R12A-ECKV2"), the same as lehigh_grades.py's:
- C: the OR print of this very telegram (same date, addressee and surrounding words) prints a word in the slot; the token
  takes that printed meaning (Canby, Butler, the sound "can be", the word "circumstances"). Known plaintext of this use.
- gloss: Leopard 9057, where the ledger writes "Gen Canby" in clear with "leopard" inserted above it; the print reads Canby.
  An operator's pairing beside clear text, not a code-only token, so it is kept out of the C count.
- M: no print reads the slot (not found in OR, or an OCR lacuna). Leghorn/Leopard: the book's H value (mssEC 41 p.17,
  Hurlbut) is contradicted by every print-read use, so H does not carry. Legend: two values read by print in overlapping
  months (Butler 11 Feb - 10 Nov 1864, Canby 27 May 1864 - 19 May 1865), so no witness matches an unread use (rule 4).
The key rows (ciphers/eckert-1864/key.md p.17 l.5-6) stay H as the record of what the book says.
"""
import csv, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORDS = ("leghorn", "legend", "leopard")
OUT = HERE / "hurlbut_row_grades.tsv"
BOOK = "Maj Gen S. A. Hurlbut"
SENSES = (("Canby", "Canby"), ("Butler", "Butler"), ('\'can be\'', "can be"), ("'circumstances'", "circumstances"),
          ("'these circumstances'", "circumstances"))
M_WHY = {
    "leghorn": "no print reads the slot; book H (Hurlbut) contradicted by all 15 print-read uses",
    "leopard": "OR slot lost in OCR; book H (Hurlbut) contradicted by all 10 print-read uses",
    "legend": "no print reads the slot; Legend has two print-read values in overlapping months (Butler, Canby): M",
}


def grade(word, r):
    st, sense = r["status"], r["sense"]
    if st.startswith("aligned"):
        for pre, mean in SENSES:
            if sense.startswith(pre):
                if word == "leopard" and r["pointer"] == "9057":
                    return "gloss", mean, "ledger writes 'Gen Canby' in clear with 'leopard' inserted; print reads Canby"
                return "C", mean, f"print of this telegram reads {mean!r} (OR {r['or_vol']} p.{r['or_page']})"
        raise SystemExit(f"unclassified sense: {sense!r} ({word} {r['pointer']})")
    if st == "not aligned" or st.startswith("date/addressee matched"):
        return "M", "", M_WHY[word]
    raise SystemExit(f"unclassified status: {st!r} ({word} {r['pointer']})")


def committed_hits():
    pat = re.compile(r"\b(" + "|".join(WORDS) + r")", re.I)
    files = [HERE / "readings.md", HERE / "s2" / "readings.md", HERE / "align_tokens.tsv", HERE / "s2" / "align_tokens.tsv"]
    return [f"{f.relative_to(HERE)}:{i}" for f in files if f.exists()
            for i, l in enumerate(f.read_text().splitlines(), 1) if pat.search(l)]


def main(argv):
    out = ["word\tledger\tpointer\tdate_ocr\taddressee_header\tform\tbook_value\tbook_grade\tdecided_meaning\tdecided_grade\treason"]
    tally = []
    for w in WORDS:
        rows = list(csv.DictReader((HERE / f"{w}_uses.tsv").open(), delimiter="\t", quoting=csv.QUOTE_NONE))
        n = {}
        for r in rows:
            g, mean, why = grade(w, r)
            key = f"{g} {mean}".strip()
            n[key] = n.get(key, 0) + 1
            out.append(f"{w}\t{r['ledger']}\t{r['pointer']}\t{r['date_ocr']}\t{r['header']}\t{r['form']}\t{BOOK}\tH\t{mean}\t{g}\t{why}")
        tally.append(f"{w} {len(rows)}: " + ", ".join(f"{k} {v}" for k, v in sorted(n.items())))
    out.append("# counts: " + "; ".join(tally))
    text = "\n".join(out) + "\n"
    hits = committed_hits()
    if hits:
        sys.stderr.write("a Hurlbut-row word is in a committed reading; carry its grade there: " + ", ".join(hits) + "\n")
        return 1
    if "--write" in argv:
        OUT.write_text(text)
    elif "--check" in argv:
        if not OUT.exists() or OUT.read_text() != text:
            sys.stderr.write("stale: hurlbut_row_grades.tsv\n")
            return 1
        print("current")
    print(out[-1])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
