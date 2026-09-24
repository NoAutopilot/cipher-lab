"""Matched control for f.54r (rule 3): Italian plaintext enciphered with a random homophonic key of 36 signs
(tools/homophonic_anneal.make_control), laid out on the target's own row pattern: every sign row of
ciphertext_f54r.tsv takes one plaintext letter, every plain box ('_') consumes --per-box letters that stay out
of the cipher stream (as the plain Italian words do). Writes control/interleaved_sSEED.tsv (sign column,
plain rows as '_') and control/interleaved_sSEED_truth.json.  Usage: make_interleaved.py PLAIN.txt SEED [--per-box 2]
Score a solve with: make_interleaved.py --score OUT.json SEED"""
import csv, json, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "tools"))
import homophonic_anneal as ha
D = os.path.dirname(os.path.abspath(__file__))
if sys.argv[1] == "--score":
    out, seed = json.load(open(sys.argv[2])), sys.argv[3]
    t = json.load(open(f"{D}/interleaved_s{seed}_truth.json"))
    ok = sum(a == b for a, b in zip(out["decoded"], t["plain"]))
    print(f"interleaved control seed {seed}: {ok}/{len(t['plain'])} = {ok/len(t['plain']):.1%}")
    sys.exit(0)
plain, seed = open(sys.argv[1], encoding="utf-8").read(), int(sys.argv[2])
per = int(sys.argv[sys.argv.index("--per-box") + 1]) if "--per-box" in sys.argv else 2
rows = list(csv.DictReader(open(f"{D}/../ciphertext_f54r.tsv"), delimiter="\t"))
n_sign = sum(r["code"] != "_" for r in rows); n_box = len(rows) - n_sign
seq, p, truth = ha.make_control(plain, 36, n_sign + per * n_box, None, seed)
out, kept, i = [], [], 0
for r in rows:
    if r["code"] == "_":
        out.append((r["line"], "_")); i += per
    else:
        out.append((r["line"], seq[i])); kept.append(p[i]); i += 1
with open(f"{D}/interleaved_s{seed}.tsv", "w") as f:
    f.write("line\tsign\n"); f.writelines(f"{a}\t{b}\n" for a, b in out)
json.dump({"plain": "".join(kept), "K": len({s for _, s in out if s != '_'}), "truth": truth},
          open(f"{D}/interleaved_s{seed}_truth.json", "w"))
print(f"seed {seed}: {len(kept)} cipher letters, K={len({s for _, s in out if s != '_'})}, {n_box} plain boxes x {per}")
