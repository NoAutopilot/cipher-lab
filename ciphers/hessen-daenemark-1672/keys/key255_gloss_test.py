#!/usr/bin/env python3
"""A2-HDK, 2 Oct 2026: does HCPortal key 255's letter table (HStAM 4 d Nr. 1234 ff.13-16, endorsed
'Clavis ... mit Secretario Lincker 1666') read the two 2-digit runs on f.4 (image 0004) of this letter
the way the letter's own interlinear/marginal gloss does?  Statistic: matches over pre-stated
(token, gloss-letter) pairs.  Control (rule 3): the same table with its 24 letter labels randomly
permuted across the columns (homophone groups and the doubled-letter row move together), which
changes every decoded letter, so the control CAN differ from the target.  Token readings are M
(one eye, native crop); key table read from the 1400-px image of key255_0013 (M)."""
import random, sys
L = "ABCDEFGHIKLMNOPQRSTUWXYZ"
NUM = {"A":[20,30,40,50,60],"B":[22,32,42,52,62],"C":[24,34,44,54,64],"D":[26,36,46,56,66],
 "E":[28,38,48,58,68],"F":[21,31,41,51,61],"G":[23,33,43,53,63],"H":[25,35,45,55,65],
 "I":[27,37,47,57,67],"K":[29,39,49,59,69],"L":[70,80,90,100,110],"M":[72,82,92,102,112],
 "N":[74,84,94,104,114],"O":[76,86,96,106,116],"P":[78,88,98,108,118],"Q":[71,81,91,101,111],
 "R":[73,83,93,103,113],"S":[75,85,95,105,115],"T":[77,87,97,107,117],"U":[79,89,99,109,119],
 "W":[120,130,140,150,160],"X":[122,132,142,152,162],"Y":[124,134,144,154,164],"Z":[126,136,146,156,166]}
DBL = dict(zip(L, "CC DD EE FF GG HH II KK LL MM NN OO PP QQ RR SS TT UU WW XX YY ZZ AA BB".split()))
# pre-stated pairs: token as read on the native crop -> gloss letter written over/beside it
RUN1 = [("FF","D"),("67","I"),("85","S"),("33","G"),("XX","U"),          # gloss 'disgu-'
        ("119","U"),("74","N"),("26","D"),                              # 'und'
        ("28","E"),("83","R"),("117","T"),("20","A"),("37","I"),("104","N")]  # 'erta(n)in'
RUN2 = [("63","G"),("38","E"),("22","B"),("FF","D"),("20","A"),("75","S"),  # 'geb' 'das'
        ("YY","W"),("96","O"),("30","A"),("32","B"),("110","L"),("XX","U")]   # 'wo' 'ab l.u'
def table(perm):
    t = {}
    for col, lab in zip(L, perm):
        for n in NUM[col]: t[str(n)] = lab
        t[DBL[col]] = lab
    return t
def score(t, pairs): return sum(t.get(tok) == g for tok, g in pairs)
pairs = RUN1 + RUN2
if "--alt22" in sys.argv: pairs = [(("21" if tok == "22" else tok), g) for tok, g in pairs]
if "--notes" in sys.argv:  # tokens exactly as NOTES.md's Remaining gaps read them on 1 Oct 2026, before key 255 was seen
    sub = {"67":"69","28":"24","22":"21","YY":"WO","32":"31"}
    pairs = [(sub.get(tok, tok), g) for tok, g in pairs]
real = score(table(L), pairs)
random.seed(255); n = 20000; ge = 0; tot = 0; mx = 0
for _ in range(n):
    p = list(L); random.shuffle(p); s = score(table(p), pairs); tot += s; mx = max(mx, s); ge += s >= real
print(f"pairs {len(pairs)}  key255 matches {real}  control mean {tot/n:.2f}  control max {mx}  "
      f"p(control>=real) {(ge+1)/(n+1):.5f}")
if "--quiet" not in sys.argv: print("decode:", " ".join(f"{tok}={table(L).get(tok,'?')}" for tok, _ in pairs))
