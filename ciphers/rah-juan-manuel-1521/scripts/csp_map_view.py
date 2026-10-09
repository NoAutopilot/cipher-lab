#!/usr/bin/env python3
"""Offline view of calendar_map.tsv + csp_date_map.tsv in the J3 JMAN-CSP column layout -> csp_map.tsv.
--check exits 1 if the committed csp_map.tsv is stale. No network."""
import csv, sys, os
d = os.path.dirname(os.path.abspath(__file__)) + "/.."
cal = {r["record"]: r for r in csv.DictReader(open(d + "/calendar_map.tsv"), delimiter="\t", quoting=csv.QUOTE_NONE)}
dm = {r["record"]: r for r in csv.DictReader(open(d + "/csp_date_map.tsv"), delimiter="\t", quoting=csv.QUOTE_NONE)}
rows = []
for rec in cal:
    c, m = cal[rec], dm.get(rec, {})
    has = bool(c["csp_no"])
    prints = "English editorial abstract of the letter; no cipher groups, no verbatim plaintext" if has else "no CSP entry found"
    rows.append([rec, c["tomokiyo_date"], c["csp_no"], c["csp_page"], prints, m.get("csp_form", ""),
                 "yes" if c["says_in_cipher"] else "no", "yes" if c["says_contemporary_deciphering"] else "no",
                 c["match_confidence"]])
out = "record\tdate\tcsp_entry_no\tbho_page\twhat_csp_prints\tcsp_form_line\tsays_in_cipher\tsays_deciphered\tmatch\n" + \
      "\n".join("\t".join(r) for r in rows) + "\n"
p = d + "/csp_map.tsv"
if "--check" in sys.argv:
    sys.exit(0 if os.path.exists(p) and open(p).read() == out else 1)
open(p, "w").write(out)
