"""R8-THUR25: build key_<name>_img.tsv from img_pairs_P2x.tsv (Birch 1742 printed gloss read from the page image) and
print the cross-letter agreement on shared codes. Grade C, or M for an out-of-range code or a code printed with two glosses."""
import csv
from collections import defaultdict,Counter
def norm(s): return s.lower().replace("ſ","s").replace(".","").replace(",","").replace(":","").replace("'","").replace(" ","").replace("f","s")
K={}
for L,name in [("P25","lockhart"),("P26","burton"),("P27","johnson1"),("P28","johnson2")]:
    d=defaultdict(Counter)
    for r in csv.DictReader(open(f"img_pairs_{L}.tsv"),delimiter="\t"): d[r["code"]][r["gloss"]]+=1
    K[L]=d
    with open(f"key_{name}_img.tsv","w") as f:
        f.write("code\tmeaning\tcount\tgrade\tsource\n")
        for c in sorted(d,key=int):
            for g,n in d[c].most_common():
                f.write(f"{c}\t{g}\t{n}\t{'M' if c in ('2372','3031') or len({norm(x) for x in d[c]})>1 else 'C'}\tBirch 1742 printed gloss, page image (R8-THUR25 img_pairs_{L}.tsv)\n")
for x,y in [("P27","P28"),("P26","P27"),("P26","P28"),("P25","P27"),("P25","P28"),("P25","P26")]:
    s=[c for c in K[x] if c in K[y]]; g=[c for c in s if {norm(z) for z in K[x][c]}&{norm(z) for z in K[y][c]}]
    print(f"{x}/{y}: shared {len(s)}, same meaning {len(g)}; differ: {[(c,dict(K[x][c]),dict(K[y][c])) for c in s if c not in g][:8]}")
