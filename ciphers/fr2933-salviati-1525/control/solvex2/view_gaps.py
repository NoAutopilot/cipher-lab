"""solvEX2 reader view: round R's decode with the target's plain-box positions shown as '..' (each box withholds 2
letters; the box positions are public on the leaf, so the reader may see them). Lines of up to 60 signs; under each
letter its stream position mod 10, so a crib is named by position.   python3 view_gaps.py DIR R"""
import json, os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, ".."))
import codemark_curve as cc
d, r = sys.argv[1], int(sys.argv[2])
rj = json.load(open(os.path.join(d, f"round{r}.json")))
dec, conf, cr = rj["decoded"], rj["conf"], rj["cribs"]
seq = [l.rstrip("\n").split("\t")[1] for l in open(os.path.join(d, "cipher.tsv"))][1:]
pat = cc.pattern(len(seq))
i, L, C, P = 0, "", "", ""
out = []
for is_sign in pat:
    if is_sign:
        s = seq[i]
        L += dec[i]; C += "*" if s in cr else str(min(9, int(conf[s] * 9 + 1e-9))); P += str(i % 10); i += 1
        if i % 60 == 0:
            out.append(f"{i - 60:4d} {L}\n     {C}\n"); L = C = P = ""
    else:
        L += ".."; C += "  "
if L.strip("."):
    out.append(f"{i - len(L.replace('..', '')):4d} {L}\n     {C}\n")
print("\n".join(out))
