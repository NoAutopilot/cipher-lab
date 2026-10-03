#!/usr/bin/env python3
"""List the residue entries that read end to end with no M-graded key token, for a later verifier. GAPS167, 3 Oct 2026.

Usage: residue_candidates.py PAGES_DIR [--write | --check]
  PAGES_DIR: the same <pointer>.json page texts print/residue_decode.py reads (manifest: residue/pages_manifest.tsv).
  --write rewrites print/residue/candidates.tsv; --check exits 1 if it is stale.

An entry is a candidate when it carries >= 1 key.md token and none graded M (decode.py's dated rule, same per-entry
loop and date carry-over as residue_decode.py). Columns: grades C/I, oov (tokens in no English corpus word list: names,
misspellings or unread code), and `page_in_print`, the print source print/residue_print.tsv gives for the PAGE (a page
match is not proof this entry is the printed one; N1 shape where printed). Candidate is a sorting label, not a reading
claim and not a novelty verdict (rule 10): the source text is the volunteer transcription, not reconciled to the image.
"""
import csv, glob, io, json, os, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import residue_decode as rdc  # noqa: E402  (loads decode.py and the dated key)

dec = rdc.dec
OUT = HERE / "residue" / "candidates.tsv"


def run(pages_dir):
    key = dec.load_key()
    voc = rdc.vocab()
    skip = rdc.matched()
    printed = {}
    for r in csv.DictReader(open(HERE / "residue_print.tsv"), delimiter="\t"):
        if r["pointer"].isdigit():
            printed.setdefault(int(r["pointer"]), set()).add(r["print_source"])
    rows, last = [], None
    for f in sorted(glob.glob(os.path.join(pages_dir, "*.json")), key=lambda x: int(os.path.basename(x)[:-5])):
        ptr = int(os.path.basename(f)[:-5])
        try:
            d = json.load(open(f))
        except Exception:
            continue
        text = (d.get("text") or "").strip()
        if ptr in skip or not text or ptr < 4956:
            continue
        for i, e in enumerate(rdc.entries(text), 1):
            day = dec.parse_day(re.sub(r"\bApl\b", "Apr", e.splitlines()[0])) or last
            last = day or last
            r, c = dec.decode_entry(dec.entry_text(e.splitlines()), key, day)
            n = sum(c.values())
            if n == 0 or c.get("M", 0):
                continue
            oov = sum(1 for w in re.findall(r"[A-Za-z]+", re.sub(r"\[[^\]]*\]|\{[^}]*\}", " ", r)) if w.lower() not in voc and len(w) > 1)
            rows.append({"pointer": ptr, "entry": i, "date": day.strftime("%d %b 1862") if day else "",
                         "C": c.get("C", 0), "I": c.get("I", 0), "oov": oov,
                         "page_in_print": "; ".join(sorted(printed.get(ptr, ()))),
                         "reading": re.sub(r"\s+", " ", r).strip()})
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=["pointer", "entry", "date", "C", "I", "oov", "page_in_print", "reading"],
                       delimiter="\t", lineterminator="\n")
    w.writeheader(); w.writerows(rows)
    return rows, buf.getvalue()


def main(argv):
    if len(argv) < 2 or argv[1].startswith("-"):
        print(__doc__); return 2
    rows, tsv = run(argv[1])
    if "--write" in argv:
        OUT.write_text(tsv); print(f"written {len(rows)} candidate entries"); return 0
    if "--check" in argv:
        if not OUT.exists() or OUT.read_text() != tsv:
            print("candidates.tsv is stale"); return 1
        print("candidates.tsv is current"); return 0
    sys.stdout.write(tsv); return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
