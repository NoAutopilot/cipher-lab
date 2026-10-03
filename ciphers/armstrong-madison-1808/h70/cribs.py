#!/usr/bin/env python3
"""H70: count crib phrases and closing/opening formulas across Armstrong's own letters to Madison on file
(letters.txt from Founders Early Access; the target 99-01-02-2728 excluded from every count). Offline.
Writes crib_counts.tsv and formulas.tsv. No scoring of the target, no decoding."""
import re, sys
TARGET = "99-01-02-2728"
LO, HI = sys.argv[1] if len(sys.argv) > 1 else "1807-11-01", sys.argv[2] if len(sys.argv) > 2 else "1808-06-30"
letters = []
for blk in open("letters.txt").read().split("=== ")[1:]:
    head, rest = blk.split("\n", 1)
    date, did, title = [x.strip() for x in head.split("|")]
    if "from John Armstrong" not in title or TARGET in did or not (LO <= date <= HI): continue
    g = lambda k: (re.search(rf"^{k}: (.*)$", rest, re.M) or [None, ""])[1]
    letters.append(dict(date=date, id=did, to=("Jefferson" if "Thomas Jefferson" in title else "Madison"), opener=g("OPENER"), body=g("BODY"), closer=g("CLOSER")))
def clear(t):  # drop numeral groups and editorial brackets; keep clear words only
    return re.sub(r"\s+", " ", re.sub(r"⟨[^⟩]*⟩|\b\d+\s*\.?\s*s?\b(?=\s|$)", " ", t))
CRIBS = [  # (phrase regex, label)
 (r"\bEmperor", "Emperor"), (r"\bHis Majesty|H\. ?M\.?", "His Majesty / H. M."), (r"\bNapoleon", "Napoleon"),
 (r"\bChampagny", "Champagny"), (r"Prince of Benevent|Benevento|Talleyrand|T_+d", "Prince of Benevento / Talleyrand"),
 (r"Minister of Marine", "Minister of Marine"), (r"Minister of (Exterior|Foreign) Relations", "Minister of Exterior/Foreign Relations"),
 (r"\bdecrees?\b", "decree(s)"), (r"Nov(ember|\.)? ?(21\.? )?1806", "November 1806 (decree)"), (r"Dec(ember|emb|r)?\.? ?(17\.? )?1807", "December 1807 (decree)"),
 (r"\bsequest", "sequester/sequestration"), (r"\bconfiscat", "confiscate"), (r"\bcaptur", "capture"),
 (r"\bembargo", "embargo"), (r"\bneutral", "neutral"), (r"\bcommerce", "commerce"),
 (r"\bEngland|Great Britain|British", "England / Great Britain / British"), (r"\bSpain|Spanish", "Spain"), (r"\bPortug", "Portugal"),
 (r"\bFlorida", "Florida(s)"), (r"\bRussia", "Russia"), (r"\bDenmark|Danes|Danish", "Denmark"), (r"\bSweden", "Sweden"), (r"\bHolland", "Holland"),
 (r"\bAustria", "Austria"), (r"\bHamburg", "Hamburg"), (r"\bPinkney", "Pinkney"), (r"\bErving|Irving", "Erving"), (r"\bSkipwith", "Skipwith"),
 (r"\ballies|\ballied|alliance", "ally/alliance"), (r"\benem(y|ies)", "enemy"), (r"\bwar\b", "war"),
 (r"\bour (business|affairs)", "our business/affairs"), (r"\bthis Government", "this Government"), (r"\bUnited States|\bU\. ?S\.", "United States / U. S."),
 (r"\bI have the honor to be", "I have the honor to be"), (r"\bwith (very )?high (respect|consideration)", "with (very) high respect/consideration"),
 (r"most obedient", "most obedient"), (r"humble [Ss]ervant", "humble servant"), (r"\bthe (\d+)(th|st|d|nd|rd)?\.? (inst|instant|ultimo|ult)", "the Nth instant/ultimo"),
 (r"\bmy (last )?letter of the", "my (last) letter of the"), (r"\benclosed|inclosed|subjoin", "enclosed/inclosed/subjoin"), (r"\bconveyance", "conveyance"),
 (r"\bmessenger", "messenger"), (r"\bI have (this moment )?received", "I have (this moment) received"), (r"\bdispatch|despatch", "dispatch"),
]
with open("crib_counts.tsv", "w") as f:
    f.write("label\tregex\tletters_with\tletters_total\ttotal_hits\tletter_dates\n")
    for rx, lab in CRIBS:
        hits = [(L["date"], len(re.findall(rx, clear(L["body"]), re.I))) for L in letters]
        w = [d for d, n in hits if n]
        f.write(f"{lab}\t{rx}\t{len(w)}\t{len(letters)}\t{sum(n for _, n in hits)}\t{','.join(w)}\n")
CLOSE = re.compile(r"((?:and )?(?:I have the honor to be|I am,? (?:Sir,? )?with|I am very high|With (?:very |the )?high(?:est)? (?:respect|consideration)|(?:and )?am,? Sir,? (?:with|your))[^.]{0,160}?(?:Serv\w*\.?|Servt\.?))", re.I)
with open("formulas.tsv", "w") as f:
    f.write("date\tid\tto\topener\tfirst_words\tclosing_formula\twords_before_formula\tps_after_formula\tsigned\n")
    for L in letters:
        b = re.sub(r"\s+", " ", re.sub(r"⟨[^⟩]*⟩", " ", L["body"])).strip(); w = b.split()
        m = None
        for m in CLOSE.finditer(b): break
        form = m.group(1) if m else ""
        before = " ".join(b[:m.start()].split()[-12:]) if m else ""
        after = "yes" if m and len(b[m.end():].split()) > 3 else "no"
        f.write(f"{L['date']}\t{L['id']}\t{L['to']}\t{L['opener']}\t{' '.join(w[:10])}\t{form}\t{before}\t{after}\t{L['closer']}\n")
print(len(letters), "Armstrong letters", LO, HI)
