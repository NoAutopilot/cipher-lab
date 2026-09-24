"""solvEX2 (24 Sept 2026): build worker P's code+mark (cm) control at N sign tokens on the target's own sign/box row
pattern, exactly as control/codemark_curve.py build('cm', N, seed) (126 code+mark types allotted by frequency deficit,
each plain box withholding 2 letters, Vanzolini chars 200,050 on, held out of the corpus), and write it for
tools/crib_rounds.py --cipher-tsv/--plain. Sign names (code^marks, which contain '#' and '|') become ids u000..u125 by
the target's pooled frequency rank. Prints N and K only; the plaintext and key go to src/hidden_sSEED.json, which the
reader never opens.   python3 make_cm.py SEED [N=720]"""
import json, os, sys
from collections import Counter
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, ".."))
import codemark_curve as cc

seed = int(sys.argv[1]); n = int(sys.argv[2]) if len(sys.argv) > 2 else 720
seq, toks, info = cc.build("cm", n, seed)
sg = [x for x in cc.rows() if x["code"] != "_"]
units = [u for u, _ in Counter(f"{x['code']}^{x['marks']}" for x in sg).most_common()]
ids = {u: f"u{i:03d}" for i, u in enumerate(units)}
# truth key: rebuild the allotment as build() does (deterministic), sign -> letter
homs = cc.alloc(Counter(f"{x['code']}^{x['marks']}" for x in sg).most_common(), Counter("".join(toks)))
truth = {ids[name]: a for a, hs in homs.items() for name, _ in hs if ids[name] in {ids[s] for s in seq}}
os.makedirs(f"{D}/src", exist_ok=True)
with open(f"{D}/src/cipher_s{seed}.tsv", "w") as fh:
    fh.write("pos\tsign\n" + "".join(f"{i}\t{ids[s]}\n" for i, s in enumerate(seq)))
json.dump({"plain": "".join(toks), "truth": truth, "design": "cm", "N": n, "seed": seed},
          open(f"{D}/src/hidden_s{seed}.json", "w"))
print(f"cm seed {seed}: N={len(seq)} K={len(set(seq))}")
