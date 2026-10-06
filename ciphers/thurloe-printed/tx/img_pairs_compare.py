"""R8-THUR25: compare page-image gloss pairs (tx/img_pairs_P2x.tsv) with the OCR-line alignment (align_P2x.tsv).
Prints per letter: tokens, C/M before (OCR align) and after (image), how many old C tokens the image confirms,
and within-letter code->gloss consistency for repeated codes vs a gloss-shuffle control (200 shuffles, seed 0).
--check exits 1 if the committed img_pairs_summary.tsv is stale."""
import csv,random,sys,os
from collections import defaultdict
D=os.path.dirname(os.path.abspath(__file__)); F=os.path.dirname(D)
def norm(s): return s.lower().replace("ſ","s").replace(".","").replace(":","").replace(",","").replace("'","").replace(" ","").replace("f","s")
OK={"single","single-segment","agrees"}
out=["letter\ttokens_ocr\tC_ocr\tM_ocr\ttokens_img\tC_img\tM_img\told_C_confirmed\told_C_contradicted\trepeat_codes\trepeat_agree\tshuffle_mean\tshuffle_p95"]
for L in ["P25","P26","P27","P28"]:
    old=[r for r in csv.DictReader(open(f"{F}/align_{L}.tsv"),delimiter="\t") if r["kind"]!="clear"]
    Cold=[r for r in old if r["status"] in OK]
    img=list(csv.DictReader(open(f"{D}/img_pairs_{L}.tsv"),delimiter="\t"))
    Mimg=sum(1 for r in img if "M" in r["read"].split(",")[-1].split() or r["read"].endswith(", M"))
    gl=defaultdict(set)
    for r in img: gl[r["code"]].add(norm(r["gloss"]))
    conf=sum(1 for r in Cold if norm(r["plain_chunk"]) in gl.get(r["value"],set()))
    contra=sum(1 for r in Cold if r["value"] in gl and norm(r["plain_chunk"]) not in gl[r["value"]])
    def cons(pairs):
        d=defaultdict(list)
        for c,g in pairs: d[c].append(g)
        rep=[v for v in d.values() if len(v)>1]
        return len(rep), sum(1 for v in rep if len(set(v))==1)
    pairs=[(r["code"],norm(r["gloss"])) for r in img]
    n,a=cons(pairs); rnd=random.Random(0); sh=[]
    for _ in range(200):
        g=[p[1] for p in pairs]; rnd.shuffle(g); sh.append(cons(list(zip([p[0] for p in pairs],g)))[1])
    sh.sort()
    out.append(f"{L}\t{len(old)}\t{len(Cold)}\t{len(old)-len(Cold)}\t{len(img)}\t{len(img)-Mimg}\t{Mimg}\t{conf}\t{contra}\t{n}\t{a}\t{sum(sh)/len(sh):.2f}\t{sh[int(0.95*len(sh))]}")
txt="\n".join(out)+"\n"
p=f"{D}/img_pairs_summary.tsv"
if "--check" in sys.argv:
    if open(p).read()!=txt: print("STALE"); sys.exit(1)
    print("ok"); sys.exit(0)
open(p,"w").write(txt); print(txt)
