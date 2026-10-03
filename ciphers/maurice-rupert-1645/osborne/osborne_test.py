#!/usr/bin/env python3
"""FT4d, 3 Oct 2026: Osborne-Rupert sibling key (DECODE 8443, BL Add MS 18982 ff.93-94, 9 Nov 1645) vs Maurice to
Rupert, 7 July 1645 (rule 3). Step 1, per-leaf pair control: consistency of repeated codes' glosses (share of
occurrences agreeing with their code's modal gloss) vs 1000 shuffles of the glosses among occurrences. Step 2, the
key (modal gloss per code) applied to the target cipher numbers, scored with the en16_repo 4-gram model and word
cover vs 200 keys whose values are shuffled among the key rows, plus the judge. Writes osborne_key.tsv,
osborne_reading.txt, osborne_test.tsv; --check exits non-zero if any committed output is stale (rule 7)."""
import csv, json, random, sys, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent; T = HERE.parent; ROOT = T.parents[1]
sys.path.insert(0, str(ROOT / "tools")); import judge_plaintext as jp
occ = [(int(r["code"]), r["gloss"]) for r in csv.DictReader((l for l in open(HERE / "pairs_8443p4.tsv") if not l.startswith("#")), delimiter="\t")]
def consistency(o):
    by = collections.defaultdict(list)
    for c, g in o: by[c].append(g)
    rep = [g for c, gs in by.items() if len(gs) > 1 for g in gs]
    agree = sum(collections.Counter(gs).most_common(1)[0][1] for c, gs in by.items() if len(gs) > 1)
    return (agree / len(rep) if rep else 0.0), len(rep)
real, nrep = consistency(occ); rnd = random.Random(1); glos = [g for _, g in occ]; sh = []
for _ in range(1000):
    g = glos[:]; rnd.shuffle(g); sh.append(consistency(list(zip([c for c, _ in occ], g)))[0])
sh.sort()
by = collections.defaultdict(list)
for c, g in occ: by[c].append(g)
key = {}; krows = []
for c in sorted(by):
    cnt = collections.Counter(by[c]); v, n = cnt.most_common(1)[0]; conflict = len(cnt) > 1
    key[c] = v; krows.append(f"{c}\t{v}\t{n}/{len(by[c])}\t{'M' if conflict or len(by[c])==1 else 'S'}\t{'conflict: '+','.join(cnt) if conflict else ''}")
ct = [l.split("\t")[2] for l in open(T / "ct118.tsv") if not l.startswith(("#", "line"))]
codes = [int(s) for s in ct if s.isdigit()]
hit = [c for c in codes if c in key]
reading = " ".join(key.get(c, f"[{c}]") for c in codes)
def render(k): return "".join(k[c] for c in codes if c in k)
spec = json.load(open(T / "judge_key118.json")); spec["judge"]["corpora"] = [str(ROOT / p) for p in spec["judge"]["corpora"]]
model = jp.NgramModel([jp.read_corpus(pathlib.Path(p)) for p in spec["judge"]["corpora"]])
txt = render(key); sc, cv = model.score(txt), model.cover(txt)
vals = list(key.values()); ks = list(key); r2 = random.Random(1); ctl = []
for _ in range(200):
    v = vals[:]; r2.shuffle(v); t = render(dict(zip(ks, v))); ctl.append((model.score(t), model.cover(t)))
s_sorted = sorted(x[0] for x in ctl); c_sorted = sorted(x[1] for x in ctl)
rank = 1 + sum(1 for x in s_sorted if x > sc); crank = 1 + sum(1 for x in c_sorted if x > cv)
j = jp.judge(spec, txt)["checks"]["language"]
test = ("stat\ttarget\tcontrol_mean\tcontrol_p95\trank\n"
        f"pair_consistency_8443p4\t{real:.3f}\t{sum(sh)/1000:.3f}\t{jp.pct(sh,0.95):.3f}\t{1+sum(1 for x in sh if x>=real)}_of_1001 (repeated-code occurrences {nrep} of {len(occ)})\n"
        f"target_coverage\t{len(hit)}/{len(codes)} tokens keyed\t-\t-\t{len(set(hit))} distinct codes of {len(set(codes))}\n"
        f"4gram\t{sc:.3f}\t{sum(s_sorted)/200:.3f}\t{jp.pct(s_sorted,0.95):.3f}\t{rank}_of_201\n"
        f"word_cover\t{cv:.3f}\t{sum(c_sorted)/200:.3f}\t{jp.pct(c_sorted,0.95):.3f}\t{crank}_of_201\n"
        f"judge\tscore {j['score']}\treal_p05 {j['real_p05']}\tnull_p99 {j['null_p99']}\t{'PASS' if j['pass'] else 'FAIL'} N={j['N']}\n")
outs = {"osborne_key.tsv": "# modal period gloss per code from pairs_8443p4.tsv; grade S = >=2 agreeing occurrences, M = single or conflicting (rule 4: sibling values are S at best, never H for the target)\ncode\tvalue\tagree\tgrade\tnote\n" + "\n".join(krows) + "\n",
        "osborne_reading.txt": "# Osborne key (8443) applied to the target's cipher numbers; [n] = code not in the key. A key test, not a reading.\n" + reading + "\n",
        "osborne_test.tsv": test}
if "--check" in sys.argv:
    bad = [n for n, s in outs.items() if not (HERE / n).exists() or (HERE / n).read_text() != s]
    print("STALE: " + ", ".join(bad) if bad else "osborne outputs up to date"); sys.exit(1 if bad else 0)
for n, s in outs.items(): (HERE / n).write_text(s)
print(test); print(reading)
