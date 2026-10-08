#!/usr/bin/env python3
"""MS18-R1 step: diff each reader row against every mssEC19 entry (sources/mssEC19), the Fort Monroe ledger (sources of mssEC25 under fortmonroe/entries-fm.tsv is metadata only; page text in sources/mssEC25 if present) and every filed ### header in ciphertext*.txt. Prints top token-overlap neighbours (>=3 shared non-function tokens of length>=4)."""
import re, sys, glob
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); import decode, entries_mssEC19 as E
FUNC=set("the and for that this with from have been will were your they their there then than which would should could upon into over under about after before what when where have also only very more most such".split())
def tk(s): return {w for w in re.findall(r"[a-z]+", s.lower()) if len(w)>=4 and w not in FUNC}
mine = [(h, tk(decode.entry_text(l)), decode.entry_text(l)) for h,l in decode.load_ciphertext(HERE/"ms18"/"ms18_r1_entries.txt")]
pools = {}
for name, d, base in [("mssEC19","sources/mssEC19",8892),("mssEC18","sources/mssEC18",9660)]:
    pools[name] = E.segment(E.load_pages(d), base=base)
import os
if os.path.isdir(HERE/"sources/mssEC25"):
    pools["mssEC25"] = E.segment(E.load_pages("sources/mssEC25"), base=0, titled=True)
filed = []
for f in glob.glob(str(HERE/"ciphertext*.txt")):
    for h,l in decode.load_ciphertext(Path(f)): filed.append((Path(f).name,h,tk(decode.entry_text(l))))
for h,t,txt in mine:
    print("==", h.split("|")[0].strip(), h.split("|")[2].strip(), len(t),"toks")
    res=[]
    for name,ents in pools.items():
        for e in ents:
            if name=="mssEC18" and any(str(e["pointer"])==h.split("|")[2].strip() and False for _ in [0]): pass
            s = t & tk(" ".join(e["lines"]))
            if len(s)>=3 and not (name=="mssEC18" and str(e["pointer"])==h.split("|")[2].strip() and False):
                res.append((len(s),name,e["pointer"],e["entry_on_page"],e["header"][:50],sorted(s)[:6]))
    for fn,fh,ft in filed:
        s=t&ft
        if len(s)>=4: res.append((len(s),fn,fh.split("|")[0].strip(),"", "",sorted(s)[:6]))
    for r in sorted(res,reverse=True)[:6]: print("  ",r)
