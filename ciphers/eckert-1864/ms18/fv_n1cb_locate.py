#!/usr/bin/env python3
"""FV-N1C-b (LANE LEDGER-12, 10 Oct 2026): place each printed entry in the cached IA djvu text (sources/ia-fulltext/print-check),
print the running heads around it and the printed passage (text layer). Disk only; the page image check is fv_n1cb_ia.py."""
import gzip, re, os
R = os.path.join(os.path.dirname(__file__), "../../../sources/ia-fulltext/print-check")
W = [("N2-JA", "warofrebellion322unit", "no law authorizing an inspector"),
     ("N2-JB", "warofrebellion013404rootrich", "Thirteenth Corps has been temporarily"),
     ("N2-JC", "warofrebellion013403rootrich", "return yourself immediately to New Orleans"),
     ("N2-JD", "warofrebellion372unit", "replied to none of my telegrams"),
     ("N2-JE", "warofrebellion372unit", "commenced crossing at McCoy"),
     ("N2-JF", "warofrebellion013403rootrich", "claims that Special Orders"),
     ("N2-JJ", "warofrebellion371unit", "too perilous to be undertaken"),
     ("N2-KD", "warofrebellion372unit", "another regiment of heavy artillery"),
     ("N2-KE", "officialrecordso0010unse", "Onondaga and Atlanta will be")]
def norm(s): return re.sub(r"[^a-z]", "", s.lower())
for e, ia, ph in W:
    t = gzip.open(os.path.join(R, ia + "_djvu.txt.gz"), "rt", errors="ignore").read()
    # map letters-only index back to raw index
    idx = [i for i, c in enumerate(t) if c.isalpha()]; letters = "".join(t[i].lower() for i in idx)
    hits = [m.start() for m in re.finditer(norm(ph), letters)]
    print("=====", e, ia, repr(ph), "hits", len(hits))
    for h in hits[:3]:
        p = idx[h]
        HD = r"(?m)^.*(?:UNION|CONFEDERATE|SQUADRON|CHAP\.|OPERATIONS|CORRESPONDENCE).*$"
        nums = lambda seg: [n for l in re.findall(HD, seg) for n in re.findall(r"\b(\d{1,4})\b", l)]
        print(" heads before:", nums(t[max(0, p-9000):p])[-2:], " after:", nums(t[p:p+9000])[:2])
        print(" " + re.sub(r"\s+", " ", t[max(0, p-900):p+1300]))
