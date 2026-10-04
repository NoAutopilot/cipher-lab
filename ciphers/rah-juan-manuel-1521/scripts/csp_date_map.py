#!/usr/bin/env python3
"""Map CSP Spain vol. II (Bergenroth 1866) Juan Manuel entries to the 28 DECODE records R9499-R9529.

RUN3-RJM, 4 Oct 2026. Source: British History Online, cal-state-papers/spain/vol2, pages pp381-386 .. pp463-481
(fetched once to --cache, >= 1.6 s apart, descriptive UA). Match rule: Salazar volume A.23/A.24 = BRAH 9/23, 9/24,
and the CSP folio range ends on (or spans) the folio Tomokiyo gives for the record's decipherment page; the closing
date line ("Rome, the Nth of <Month> 1522") must agree with Tomokiyo's date. Writes csp_date_map.tsv.
A CSP abstract is an English editorial summary, not printed plaintext: a match is a print-check result for the log.
Usage: csp_date_map.py --cache DIR [--out csp_date_map.tsv]
"""
import argparse, html, os, re, subprocess, sys, time, urllib.request

PAGES = ["pp381-386", "pp386-400", "pp401-405", "pp405-412", "pp412-419", "pp419-426", "pp426-434",
         "pp434-447", "pp448-462", "pp463-481"]
BASE = "https://www.british-history.ac.uk/cal-state-papers/spain/vol2/"
UA = "cipher-lab research script (contact via repository)"
# Tomokiyo, AlonsoSanchez.htm (sources/cryptiana/web), list of Juan Manuel letters: record, date, BRAH vol, decipher folio
RECORDS = [
    ("R9499", "1522-03-01", 23, 5), ("R9500", "1522-03-03", 23, 19), ("R9501", "1522-03-07", 23, None),
    ("R9502", "1522-03-08", 23, 42), ("R9503", "1522-03-12", 23, 54), ("R9504", "1522-03-15", 23, 66),
    ("R9506", "1522-03-18", 23, 90), ("R9507", "1522-03-21", 23, 98), ("R9508", "1522-03-22", 23, 102),
    ("R9510", "1522-04-01", 23, 125), ("R9511", "1522-04-12", 23, 176), ("R9512", "1522-04-14", 23, 192),
    ("R9513", "1522-04-15", 23, 204), ("R9514", "1522-04-21", 23, 223), ("R9515", "1522-04-24", 23, None),
    ("R9516", "1522-04-25", 23, 224), ("R9517", "1522-04-27", 23, 254), ("R9518", "1522-04-29", 23, 275),
    ("R9519", "1522-05-06", 24, 32), ("R9520", "1522-05-16", 24, 75), ("R9521", "1522-05-19", 24, 94),
    ("R9523", "1522-05-26", 24, 116), ("R9524", "1522-05-31?", 24, 125), ("R9525", "1522-06-05", 24, 145),
    ("R9526", "1522-06-06", 24, 150), ("R9527", "1522-06-11", 24, 164), ("R9528", "1522-06-18", 24, 197),
    ("R9529", "1522-06-19", 24, 201),
]
MONTHS = {m: i for i, m in enumerate(["january", "february", "march", "april", "may", "june", "july", "august",
                                      "september", "october", "november", "december"], 1)}
HEAD = re.compile(r"^\s*(M\. Re\. Ac\..*?)(?:\t|\s{2,})\s*(\d{3})\.\s+(.*)$")
DATE = re.compile(r"the (\d{1,2})(?:st|nd|rd|th|d)? (?:of )?([A-Z][a-z]+),? (15\d\d)")


def fetch(cache):
    os.makedirs(cache, exist_ok=True)
    for p in PAGES:
        f = os.path.join(cache, p + ".html")
        if not os.path.exists(f):
            req = urllib.request.Request(BASE + p, headers={"User-Agent": UA})
            open(f, "wb").write(urllib.request.urlopen(req, timeout=60).read())
            time.sleep(1.6)


def text(cache, p):
    here = os.path.dirname(os.path.abspath(__file__))
    tool = os.path.join(here, "..", "..", "..", "tools", "html2text.py")
    return subprocess.run([sys.executable, tool, os.path.join(cache, p + ".html")], capture_output=True,
                          text=True, check=True).stdout


def entries(cache):
    out, cur, page = [], None, None
    for p in PAGES:
        page = int(p[2:].split("-")[0])
        for line in text(cache, p).splitlines():
            m = re.search(r"\[Page (\d+)\]", line)
            if m:
                page = int(m.group(1))
                continue
            h = HEAD.match(line)
            if h:
                cur = {"no": int(h.group(2)), "source": h.group(1).strip(), "title": h.group(3).strip(),
                       "page": page, "body": []}
                out.append(cur)
            elif cur is not None:
                cur["body"].append(line.strip())
    return out


def folios(source):
    v = re.search(r"A\.\s*(\d+)", source)
    f = re.search(r"ff?\.\s*(\d+)(?:\s*-\s*(\d+))?", source[v.end():] if v else source)
    if not v or not f:
        return None, None, None
    a = int(f.group(1)); b = int(f.group(2) or a)
    return int(v.group(1)), a, b


def closing_date(body):
    for line in reversed(body):
        if re.search(r"Rome|Indorsed", line):
            m = DATE.search(line)
            if m and m.group(2).lower() in MONTHS:
                return "%s-%02d-%02d" % (m.group(3), MONTHS[m.group(2).lower()], int(m.group(1)))
            m = re.search(r"last day of ([A-Z][a-z]+),? (15\d\d)", line)  # "postrero", R9524
            if m and m.group(1).lower() in MONTHS:
                import calendar
                mo = MONTHS[m.group(1).lower()]
                return "%s-%02d-%02d" % (m.group(2), mo, calendar.monthrange(int(m.group(2)), mo)[1])
    return ""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cache", required=True)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "csp_date_map.tsv"))
    a = ap.parse_args()
    fetch(a.cache)
    jm = [e for e in entries(a.cache) if "Juan Manuel" in e["title"] and e["title"].startswith("Juan Manuel")]
    rows, used = [], set()
    for rec, date, vol, dfol in RECORDS:
        hit = None
        for e in jm:
            v, f1, f2 = folios(e["source"])
            cd = closing_date(e["body"])
            fol_ok = v == vol and dfol is not None and f1 <= dfol <= f2
            date_ok = cd == date.rstrip("?")
            if fol_ok or (date_ok and v == vol):
                hit = (e, v, f1, f2, cd, "folio+date" if fol_ok and date_ok else ("folio" if fol_ok else "date"))
                break
        if hit:
            e, v, f1, f2, cd, how = hit
            used.add(e["no"])
            enc = " ".join(e["body"])
            form = re.search(r"(Spanish\.[^.]*\.(?:[^.]*deciph[^.]*\.)?)", enc)
            rows.append([rec, date, "9/%d" % vol, dfol or "", e["no"], e["page"], e["source"], cd, how,
                         form.group(1).strip() if form else ""])
        else:
            rows.append([rec, date, "9/%d" % vol, dfol or "", "", "", "", "", "none", ""])
    unmatched = [e for e in jm if e["no"] not in used and e["no"] >= 392 and e["no"] <= 430]
    for e in unmatched:
        v, f1, f2 = folios(e["source"])
        rows.append(["-", "", "", "", e["no"], e["page"], e["source"], closing_date(e["body"]), "csp-only", ""])
    with open(a.out, "w") as fh:
        fh.write("record\ttomokiyo_date\tbrah_vol\tdecipher_folio\tcsp_no\tcsp_page\tcsp_source\tcsp_closing_date\tmatch\tcsp_form\n")
        for r in rows:
            fh.write("\t".join(str(x) for x in r) + "\n")
    n = sum(1 for r in rows if r[0] != "-" and r[8] != "none")
    print("records with a CSP entry: %d of %d; CSP-only Juan Manuel entries Mar-Jun range: %d" % (n, len(RECORDS), len(unmatched)))


if __name__ == "__main__":
    main()
