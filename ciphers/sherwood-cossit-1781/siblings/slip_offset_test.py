#!/usr/bin/env python3
"""Page-slip test for M rows that Sherwood's sketch (B.178 pp.84-85) names a word for.

Hypothesis (from Sherwood, 1 Mar 1783, B.178 p.105: "frequent mistakes made in numbering the pages"): some M groups
are page P+-1 of the intended entry, line W unchanged. Statistic: for each offset d in -6..+6 (d=0 included), the number
of listed groups whose OCR line (P+d, either column, W) begins with the first four letters of the sketch word
(long s normalised). Control: offsets |d| = 2..6 are the matched null for d = +-1 (same groups, same OCR, same rule).
The expected words were fixed in EXPECTED below before any neighbouring page was looked at; they are our reading of
Sherwood's paraphrase, so a hit is a lead graded M/I at most, never a reading. OCR misses are not negatives.
Usage: slip_offset_test.py [--check]   (--check exits 1 if siblings/slip_offset_test.out is stale)
"""
import csv, os, re, sys
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
EXPECTED = [("176-26", "house"), ("4-31", "accounts"), ("84-25", "council"), ("32-12", "below"),
            ("156-23", "french"), ("143-38", "fleet"), ("16-2", "and"), ("188-7", "indies"),
            ("366-32", "thunder"), ("226-30", "marched"), ("131-22", "from"), ("382-23", "vermont"),
            ("146-16", "force"), ("315-2", "saturday")]
ocr = {}
for r in csv.DictReader(open(os.path.join(root, "book/entick_lines.tsv")), delimiter="\t"):
    ocr[(int(r["page"]), int(r["col"]), int(r["line"]))] = r["ocr"]
def norm(s):
    s = s.lower().replace("ſ", "s")
    s = re.sub(r"[^a-z]", "", s)
    return s.replace("f", "s")  # long s read as f by the OCR; applied to both sides
lines = []
hits = {}
for d in range(-6, 7):
    n = 0; who = []
    for g, word in EXPECTED:
        p, w = map(int, g.split("-"))
        key = norm(word)[:4] if len(word) > 3 else norm(word)
        for c in (1, 2):
            t = norm(ocr.get((p + d, c, w), ""))
            if t.startswith(key):
                n += 1; who.append("%s->p%d c%d [%s]" % (g, p + d, c, ocr[(p + d, c, w)][:28])); break
    hits[d] = n
    lines.append("d=%+d\thits=%d/%d\t%s" % (d, n, len(EXPECTED), ", ".join(who)))
null = [hits[d] for d in range(-6, 7) if abs(d) >= 2]
lines.append("d=+-1 total %d; control |d|=2..6 per-offset mean %.2f, max %d (10 offsets); d=0 %d"
             % (hits[-1] + hits[1], sum(null) / len(null), max(null), hits[0]))
txt = "\n".join(lines) + "\n"
outp = os.path.join(here, "slip_offset_test.out")
if "--check" in sys.argv:
    ok = os.path.exists(outp) and open(outp).read() == txt
    print("slip_offset_test current" if ok else "STALE"); sys.exit(0 if ok else 1)
open(outp, "w").write(txt); print(txt, end="")
