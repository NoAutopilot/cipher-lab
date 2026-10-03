#!/usr/bin/env python3
"""FT4e, 3 Oct 2026: the Osborne key extended with the unread cipher lines of DECODE 8443 P2 and 8444 P2 (8443 P1 is
all clear text, no cipher), then the FT4d target test re-run unchanged. Step 1, per-page gate (rule 3, per unit,
before merging): each new page's glosses must agree with the P4 key (pairs_8443p4.tsv, read by FT4d) on the codes
they share more often than the same page's glosses shuffled among its own occurrences (1000 shuffles; gate: real >
shuffle p95). Within-page repeat consistency vs shuffle is reported too. Step 2, the merged key (modal gloss per code
over P4 plus every page that cleared) applied to the target, en16_repo 4-gram and word cover vs 200 keys with values
shuffled among the key rows (seed 1), plus the judge -- the same statistics as osborne_test.py. Writes
osborne_key2.tsv, osborne_reading2.txt, osborne_test2.tsv; --check exits non-zero if any committed output is stale."""
import csv, json, random, sys, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent; T = HERE.parent; ROOT = T.parents[1]
sys.path.insert(0, str(ROOT / "tools")); import judge_plaintext as jp
def load(fn): return [(int(r["code"]), r["gloss"]) for r in csv.DictReader((l for l in open(HERE / fn) if not l.startswith("#")), delimiter="\t")]
def modal(o):
    by = collections.defaultdict(list)
    for c, g in o: by[c].append(g)
    return {c: collections.Counter(gs).most_common(1)[0][0] for c, gs in by.items()}, by
def consistency(o):
    _, by = modal(o); rep = [g for gs in by.values() if len(gs) > 1 for g in gs]
    agree = sum(collections.Counter(gs).most_common(1)[0][1] for gs in by.values() if len(gs) > 1)
    return (agree / len(rep) if rep else 0.0), len(rep)
def agreement(o, ref):
    sh = [(c, g) for c, g in o if c in ref]
    return (sum(1 for c, g in sh if ref[c] == g) / len(sh) if sh else 0.0), len(sh)
p4 = load("pairs_8443p4.tsv"); p4key, _ = modal(p4)
pages = {"8443p2": load("pairs_8443p2.tsv"), "8444p2": load("pairs_8444p2.tsv")}
lines = ["stat\ttarget\tcontrol_mean\tcontrol_p95\trank_or_gate"]
merged = list(p4); cleared = []
for name, o in pages.items():
    ra, na = agreement(o, p4key); rc, nc = consistency(o); rnd = random.Random(1); sa, sc_ = [], []
    codes = [c for c, _ in o]; gl = [g for _, g in o]
    for _ in range(1000):
        g = gl[:]; rnd.shuffle(g); oo = list(zip(codes, g)); sa.append(agreement(oo, p4key)[0]); sc_.append(consistency(oo)[0])
    sa.sort(); sc_.sort(); ok = ra > jp.pct(sa, 0.95)
    lines.append(f"{name}_agree_with_P4key\t{ra:.3f} ({na} shared occ of {len(o)})\t{sum(sa)/1000:.3f}\t{jp.pct(sa,0.95):.3f}\t{'CLEARS' if ok else 'HELD'} (rank {1+sum(1 for x in sa if x>=ra)} of 1001)")
    lines.append(f"{name}_repeat_consistency\t{rc:.3f} ({nc} repeated occ)\t{sum(sc_)/1000:.3f}\t{jp.pct(sc_,0.95):.3f}\trank {1+sum(1 for x in sc_ if x>=rc)} of 1001")
    if ok: merged += o; cleared.append(name)
key, by = modal(merged); krows = []
for c in sorted(by):
    cnt = collections.Counter(by[c]); v, n = cnt.most_common(1)[0]; conflict = len(cnt) > 1
    new = "" if c in p4key else "new"
    krows.append(f"{c}\t{v}\t{n}/{len(by[c])}\t{'M' if conflict or len(by[c])==1 else 'S'}\t{('conflict: '+','.join(cnt)) if conflict else ''}{(' ' if conflict and new else '')+new}")
ct = [l.split("\t")[2] for l in open(T / "ct118.tsv") if not l.startswith(("#", "line"))]
codes = [int(s) for s in ct if s.isdigit()]; hit = [c for c in codes if c in key]
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
lines += [f"merged_key\t{len(key)} codes from P4 + {','.join(cleared) or 'none'} ({len(merged)} occurrences)\t-\t-\t{len(key)-len(p4key)} codes new over P4",
          f"target_coverage\t{len(hit)}/{len(codes)} tokens keyed\t-\t-\t{len(set(hit))} distinct codes of {len(set(codes))}",
          f"4gram\t{sc:.3f}\t{sum(s_sorted)/200:.3f}\t{jp.pct(s_sorted,0.95):.3f}\t{rank}_of_201",
          f"word_cover\t{cv:.3f}\t{sum(c_sorted)/200:.3f}\t{jp.pct(c_sorted,0.95):.3f}\t{crank}_of_201",
          f"judge\tscore {j['score']}\treal_p05 {j['real_p05']}\tnull_p99 {j['null_p99']}\t{'PASS' if j['pass'] else 'FAIL'} N={j['N']}"]
test = "\n".join(lines) + "\n"
outs = {"osborne_key2.tsv": "# modal period gloss per code over pairs_8443p4.tsv plus every new page that cleared its per-page gate (osborne_test2.tsv); S = >=2 agreeing occurrences, M = single or conflicting; 'new' = code not in the P4 key (rule 4: sibling values are S at best, never H for the target)\ncode\tvalue\tagree\tgrade\tnote\n" + "\n".join(krows) + "\n",
        "osborne_reading2.txt": "# extended Osborne key (8443 P4 + P2, 8444 P2) applied to the target's cipher numbers; [n] = code not in the key. A key test, not a reading.\n" + reading + "\n",
        "osborne_test2.tsv": test}
if "--check" in sys.argv:
    bad = [n for n, s in outs.items() if not (HERE / n).exists() or (HERE / n).read_text() != s]
    print("STALE: " + ", ".join(bad) if bad else "osborne2 outputs up to date"); sys.exit(1 if bad else 0)
for n, s in outs.items(): (HERE / n).write_text(s)
print(test); print(reading)
