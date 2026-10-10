#!/usr/bin/env python3
"""FV-N1C-b (LANE LEDGER-12, 10 Oct 2026): print body (IA djvu text layer, after the page image was read) against the decoded body,
using step0_ordered.py's words()/body()/lcs(). Reports LCS / print content words and / decoded content words, and the words on each side
missing from the other. Disk only."""
import gzip, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(HERE, "../../../sources/ia-fulltext/print-check")
src = open(os.path.join(HERE, "step0_ordered.py")).read(); g = {"__file__": os.path.join(HERE, "step0_ordered.py")}
exec(src[:src.index("EXTRA = ")], g)
W = [("N2-JA", "warofrebellion322unit", "I know of no law", "want on it"),
     ("N2-JB", "warofrebellion013404rootrich", "can be assigned as you may desire", "made available"),
     ("N2-JC", "warofrebellion013403rootrich", "Lieutenant-General Grant directs that, on the receipt", "early as possible"),
     ("N2-JD", "warofrebellion372unit", "General Sigel reports that Early", "attack the line in force"),
     ("N2-JE", "warofrebellion372unit", "General Averell informs me that the enemy commenced", "moving in three columns"),
     ("N2-JF", "warofrebellion013403rootrich", "As some time may elapse", "his home in Illinois"),
     ("N2-JJ", "warofrebellion371unit", "As stated in my former dispatch", "up the Shenandoah Val"),
     ("N2-KD", "warofrebellion372unit", "I am of the opinion that another regiment", "written to-day at length"),
     ("N2-KE", "officialrecordso0010unse", "The Onondaga and the Atlanta will", "Convoy will be sent from the north. Answer")]
def L(s): return re.sub(r"[^a-z]", "", s.lower())
for e, ia, a, b in W:
    t = gzip.open(os.path.join(R, ia + "_djvu.txt.gz"), "rt", errors="ignore").read()
    idx = [i for i, c in enumerate(t) if c.isalpha()]; letters = "".join(t[i].lower() for i in idx)
    i = letters.find(L(a)); j = letters.find(L(b), i); assert i >= 0 and j > i, (e, i, j)
    pr = t[idx[i]: idx[j + len(L(b)) - 1] + 1]
    pr = re.sub(r"(?m)^.*(?:UNION|CHAP\.|SQUADRON|OPERATIONS IN).*$", " ", pr)        # running heads out
    pr = re.sub(r"-\s*\n\s*", "", pr)                                                 # hyphen breaks joined
    pw = g["words"](pr); dw, _ = g["body"](g["ents"][e][1])
    n = g["lcs"](dw, pw)
    print(f"{e}\tLCS {n}\tprint {len(pw)} ({n/len(pw):.2f})\tdecoded {len(dw)} ({n/len(dw):.2f})")
    print("   print-only:", " ".join(w for w in pw if w not in set(dw)))
    print("   decoded-only:", " ".join(w for w in dw if w not in set(pw)))
