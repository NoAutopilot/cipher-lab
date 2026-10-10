#!/usr/bin/env python3
"""FV-N2g (LANE LEDGER-12, 10 Oct 2026): print check of N2-KA, N2-KB on the cached OR djvu texts (disk only; the same files and the same
letters-only phrases N2R-6's n2r6_printcheck.py already hit -- its .out lists the volumes, the reader's NOTES said 'not located').
Prints the OCR window around each hit and the nearest page header before/after. Writes ms18/fv_n2g_print.out (N2-KC's Grant Papers
snippets were fetched from the Google Books API on 10 Oct 2026 and are appended to the .out by hand, see AUDIT (FV-N2g) s.1)."""
import gzip, os, re
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
CASES = [("N2-KA", "warofrebellion013403rootrich", "Your last instructions in regard to"),
         ("N2-KB", "warofrebellion33unit", "General Burnside left unexpectedly last night")]
out = []
for e, v, ph in CASES:
    t = re.sub(r"\s+", " ", gzip.open(os.path.join(D, v + "_djvu.txt.gz"), "rt", errors="ignore").read())
    i = t.find(ph)
    w = t[i-160: i+620]
    heads = re.findall(r"(?:UNION\. (\d{3})|\b(\d{3}) OPERATIONS)", t[i-2500: i+1400])
    out.append(f"{e} | {v} | offset {i} | page heads near: {heads}\n  {w}")
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fv_n2g_print.out"), "w").write("\n".join(out) + "\n"); print("\n".join(out))
