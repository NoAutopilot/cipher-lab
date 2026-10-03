#!/usr/bin/env python3
"""FT4b, 3 Oct 2026: test Digby key no. 118 (BL Add MS 72438 ff.59-60) on Maurice to Rupert, 7 July 1645 (rule 3).
Scores the cipher-only decode (clear words, nulls and blank slots dropped) with the en16_repo 4-gram model and word
cover, against 200 decodes under keys whose values are shuffled among the key rows (seed 1), plus the judge's own
real-text / shuffled-text controls. Exits non-zero if the committed key118_test.tsv is stale (--check)."""
import csv, json, random, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "tools")); import judge_plaintext as jp
rows = [r for r in csv.DictReader((l for l in open(HERE / "key118.tsv") if not l.startswith("#")), delimiter="\t")]
key = {int(r["code"]): r["value"] for r in rows}
ct = [l.split("\t")[2] for l in open(HERE / "ct118.tsv") if not l.startswith(("#", "line"))]
codes = [int(s) for s in ct if s.isdigit()]
def render(k): return "".join(k[c].replace("_", "") for c in codes if c in k and k[c] != "[null]")
spec = json.load(open(HERE / "judge_key118.json")); spec["judge"]["corpora"] = [str(ROOT / p) for p in spec["judge"]["corpora"]]
model = jp.NgramModel([jp.read_corpus(pathlib.Path(p)) for p in spec["judge"]["corpora"]])
txt = render(key); sc, cv = model.score(txt), model.cover(txt)
vals = [r["value"] for r in rows]; codes_k = [int(r["code"]) for r in rows]; rnd = random.Random(1); ctl = []
for _ in range(200):
    v = vals[:]; rnd.shuffle(v); t = render(dict(zip(codes_k, v))); ctl.append((model.score(t), model.cover(t)))
s_sorted = sorted(x[0] for x in ctl); c_sorted = sorted(x[1] for x in ctl)
rank = 1 + sum(1 for x in s_sorted if x > sc); crank = 1 + sum(1 for x in c_sorted if x > cv)
j = jp.judge(spec, txt)["checks"]["language"]
out = ("stat\ttarget\tshuffled_key_mean\tshuffled_key_p95\trank_of_201\n"
       f"4gram\t{sc:.3f}\t{sum(s_sorted)/200:.3f}\t{jp.pct(s_sorted,0.95):.3f}\t{rank}\n"
       f"word_cover\t{cv:.3f}\t{sum(c_sorted)/200:.3f}\t{jp.pct(c_sorted,0.95):.3f}\t{crank}\n"
       f"judge\tscore {j['score']}\treal_p05 {j['real_p05']}\tnull_p99 {j['null_p99']}\t{'PASS' if j['pass'] else 'FAIL'} N={j['N']}\n")
f = HERE / "key118_test.tsv"
if "--check" in sys.argv:
    ok = f.exists() and f.read_text() == out; print("key118_test.tsv up to date" if ok else "STALE"); sys.exit(0 if ok else 1)
f.write_text(out); print(out)
