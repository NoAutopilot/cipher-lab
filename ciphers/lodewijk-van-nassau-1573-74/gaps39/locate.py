"""GAPS39 step 1: candidate print locations for GAPS33's dropped occurrences (gaps33/dropped.tsv) plus the fresh-control
pool, for hand location. Restricted Smith-Waterman: the right anchor is searched only within 60 print letters after the
left anchor's end (and vice versa), so a far spurious match cannot win. Prints, per occurrence, the cipher window and
both anchors' scores/positions; the hand decision goes in gaps39/hand_locate.tsv before any reading."""
import os, sys, re, csv
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, os.path.join(T, "gaps33")); sys.path.insert(0, os.path.join(T, "axnames"))
import build as B, align_names as A

def occs():
    out = {}
    for letter in ("5810", "5811"):
        ct, spans = A.PAIRS[letter]
        raw = re.sub(r"\s+", " ", " ".join(A.groen_body(*sp) for sp in spans))
        pt, idx = B.printmap(raw)
        toks = A.tokens(ct); dec = [B.val(s) for (_, _, s) in toks]
        for i, (line, pos, s) in enumerate(toks):
            out[(letter, line, str(pos))] = dict(letter=letter, line=line, pos=str(pos), code=s, i=i, dec=dec, pt=pt, idx=idx, raw=raw)
    return out

def window(x):
    i, dec = x["i"], x["dec"]
    return " ".join(d for d in dec[max(0, i - 15):i] if d != "") + " [?] " + " ".join(d for d in dec[i + 1:i + 16] if d != "")

def locate(x):
    i, dec, pt = x["i"], x["dec"], x["pt"]
    Lq = "".join(dec[max(0, i - 40):i]).replace("_", "")[-24:]; Rq = "".join(dec[i + 1:i + 41]).replace("_", "")[:24]
    sl, stl, el = B.sw(Lq, pt)
    lo = el; hi = min(len(pt), el + 60)
    sr, srt, er = B.sw(Rq, pt[lo:hi]); srt += lo
    # also right-first
    sr2, srt2, _ = B.sw(Rq, pt)
    sl2, _, el2 = B.sw(Lq, pt[max(0, srt2 - 60):srt2]); el2 += max(0, srt2 - 60)
    return dict(Lq=Lq, Rq=Rq, left=(sl, el, sr, srt), right=(sl2, el2, sr2, srt2))

if __name__ == "__main__":
    O = occs()
    for r in csv.DictReader(open(os.path.join(T, "gaps33", "dropped.tsv")), delimiter="\t"):
        x = O[(r["letter"], r["line"], r["pos"])]; l = locate(x)
        print(f"== {r['letter']} {r['line']}:{r['pos']} {r['kind']}")
        print("  WIN:", window(x))
        for nm in ("left", "right"):
            sl, el, sr, srt = l[nm]
            print(f"  {nm}-first sl={sl} sr={sr} gap={srt-el} el={el} | ...{x['pt'][max(0,el-24):el]} | {x['pt'][el:srt]} | {x['pt'][srt:srt+24]}...")
