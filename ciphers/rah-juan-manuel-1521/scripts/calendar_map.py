#!/usr/bin/env python3
"""D1A-RJM, 8 Oct 2026. Extends csp_date_map.py: for every record, the CSP Spain II entry (if any), a match
confidence, and whether the calendar text mentions cipher / deciphering passages. Also scans ALL entries (any title)
whose closing date or text could match the 12 records csp_date_map.py left empty, so a missing Juan Manuel heading
does not hide an entry filed under another title. Needs the BHO page cache of csp_date_map.py (--cache DIR).
Writes calendar_map.tsv. A CSP abstract is an English editorial summary, not printed plaintext (print-check result)."""
import argparse, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import csp_date_map as m

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--cache", required=True)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "calendar_map.tsv"))
    a = ap.parse_args()
    ents = m.entries(a.cache)
    allr = [e for e in ents if 385 <= e["no"] <= 435]
    rows = []
    for rec, date, vol, dfol in m.RECORDS:
        d = date.rstrip("?")
        hit = None
        for e in allr:
            v, f1, f2 = m.folios(e["source"]); cd = m.closing_date(e["body"])
            fol = v == vol and dfol is not None and f1 <= dfol <= f2
            dat = cd == d
            if fol or dat:
                hit = (e, v, f1, f2, cd, fol, dat); break
        if not hit:
            # loose: any entry of any title whose body names the day/month
            y, mo, dy = d.split("-"); mon = [k for k, n in m.MONTHS.items() if n == int(mo)][0]
            pat = re.compile(r"\b%d(st|nd|rd|th|d)? (of )?%s\b" % (int(dy), mon.capitalize()))
            loose = [e["no"] for e in allr if pat.search(" ".join(e["body"][-6:]))]
            rows.append([rec, date, "", "", "", "", "none", "", "", "", "loose-date-hits:" + (",".join(map(str, loose)) or "-")])
            continue
        e, v, f1, f2, cd, fol, dat = hit
        body = " ".join(e["body"])
        conf = "high (folio+date)" if fol and dat else "medium (date only)" if dat else "medium (folio only)"
        if not (e["title"].startswith("Juan Manuel")): conf += "; title=" + e["title"][:30]
        # form segments: each "Spanish ... pp. N" run is one document of the entry (letter + enclosures)
        segs = re.findall(r"Spanish\b[^|]*?\bpp?\.? ?\d+", body)
        segs = [x[-160:] if len(x) > 160 else x for x in segs]
        rest = body
        for x in re.findall(r"Spanish\.?[^.]*\.(?: [A-Z][^.]*deciph[^.]*\.)?", body): rest = rest.replace(x, " ")
        other = [x.strip()[:140] for x in re.findall(r"[^.]*\b(?:cipher|deciph|cypher)[^.]*\.", rest)]
        form = "in cipher" if re.search(r"in cipher", body) else ""
        dec = "contemporary deciphering" if re.search(r"[Cc]ontemporary deciph", body) else ""
        rows.append([rec, date, e["no"], e["page"], e["source"], cd, conf, form, dec,
                     str(len(segs)), " || ".join(other) if other else "-"])
    with open(a.out, "w") as fh:
        fh.write("record\ttomokiyo_date\tcsp_no\tcsp_page\tcsp_source\tcsp_closing_date\tmatch_confidence\tsays_in_cipher\tsays_contemporary_deciphering\tn_document_form_lines\tother_cipher_sentences\n")
        for r in rows: fh.write("\t".join(map(str, r)) + "\n")
    print("matched %d of %d" % (sum(1 for r in rows if r[6] != "none"), len(rows)))
if __name__ == "__main__": main()
