#!/usr/bin/env python3
"""R12A-ECKV (6 Oct 2026, verifier): per-token grade decision for the code word Lehigh in the sent ledgers mssEC 18-19.

Usage: lehigh_grades.py [--write | --check]

Input: ec18/lehigh_uses.tsv (D1-ECK62S: 13 uses, each aligned or not to its dated OR ser. I print) and the two committed
alignment tables ec18/align_tokens.tsv, ec18/s2/align_tokens.tsv (the two uses that fall in committed readings).
Output: ec18/lehigh_grades.tsv, one row per use with the grade decided under rule 4. --check exits 1 if the committed
output is stale or if a committed-reading token is missing from either alignment table.

The rule (AUDIT.md "Carry-over R12A-ECKV"):
- C: the OR print of this very telegram (same date, addressee and surrounding words) prints a word in the Lehigh slot;
  the token takes that printed meaning ("Canby" person, or the sound "can be"). Known plaintext of this use, not a key
  value carried from elsewhere.
- M: the use is dated, but no print reads the slot (OCR margin lacuna) or no print exists (Sept 1865). The key book's H
  value (mssEC 41 p.17 l.6, Hurlbut) is contradicted by every print-read use of 24 Oct 1864 - 24 May 1865, so H does
  not carry to an unread use in or after that window (rule 4: conflicting support -> M where no witness reads it).
- clear: not a code token (a clear place/product word).
The key row itself (ciphers/eckert-1864/key.md p.17 l.6) stays H as the record of what the book says.
"""
import csv, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
USES, OUT = HERE / "lehigh_uses.tsv", HERE / "lehigh_grades.tsv"
COMMITTED = {"9947": "9947.505", "10020": "10020.609"}  # uses that are tokens of committed readings (readings.md, s2/readings.md)


def grade(r):
    st, sense = r["status"], r["sense"]
    if st.startswith("aligned") and sense.startswith("Canby"):
        return "C", "Canby", "print of this telegram reads Canby"
    if st.startswith("aligned") and sense.startswith('"can be"'):
        return "C", "can be", "print of this telegram reads 'can be'"
    if st.startswith("date/addressee matched"):
        return "M", "", "dated, OR slot lost in OCR; book H (Hurlbut) contradicted by all 8 print-read uses"
    if st == "not aligned":
        return "M", "", "Sept 1865, not in OR ser. I; book H (Hurlbut) contradicted by all 8 print-read uses"
    if st == "not a code use":
        return "clear", "", "clear word (Lehigh Iron)"
    raise SystemExit(f"unclassified status: {st!r} ({r['pointer']})")


def main(argv):
    rows = list(csv.DictReader(USES.open(), delimiter="\t", quoting=csv.QUOTE_NONE))
    tok = {}
    for f in (HERE / "align_tokens.tsv", HERE / "s2" / "align_tokens.tsv"):
        for l in f.read_text().splitlines():
            c = l.split("\t")
            if len(c) > 6 and c[6].lower() == "lehigh":
                tok.setdefault(c[0], []).append((f.parent.name, c[5], c[8], c[10]))
    out = ["ledger\tpointer\tdate\tentry_in_committed_readings\tbook_value\tbook_grade\tdecided_meaning\tdecided_grade\treason"]
    n = {"C": 0, "M": 0, "clear": 0}
    for r in rows:
        g, mean, why = grade(r)
        n[g] += 1
        ent = COMMITTED.get(r["pointer"], "")
        if ent:
            seen = tok.get(ent, [])
            if len(seen) != 2 or any(s[2] != "H" or s[3] != "CONFLICT" for s in seen):
                sys.stderr.write(f"{ent}: expected an H CONFLICT Lehigh row in both align_tokens tables, got {seen}\n")
                return 1
        out.append(f"{r['ledger']}\t{r['pointer']}\t{r['date']}\t{ent}\tMaj Gen S. A. Hurlbut\tH\t{mean}\t{g}\t{why}")
    out.append(f"# counts: C {n['C']}, M {n['M']}, clear {n['clear']} (of {len(rows)} uses)")
    text = "\n".join(out) + "\n"
    if "--write" in argv:
        OUT.write_text(text)
    elif "--check" in argv:
        if not OUT.exists() or OUT.read_text() != text:
            sys.stderr.write("stale: lehigh_grades.tsv\n")
            return 1
        print("current")
    print(out[-1])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
