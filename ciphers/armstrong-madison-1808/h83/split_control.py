"""H83: freq.py --split-at auto (split_auto) on the target, matched control first.
Control: ARM-DESIGN's seq_pblock design (design/design_stats.py: particle block 1-99 + 1,800 content forms numbered
100-1899 in random order, en18 plaintext), N=369, seeds 1000..1004 (the row's pre-registered 5), known edge 100.
Gate (row H83, pre-registered 9 Oct 00:2x UTC in CAMPAIGN.md): best single split within |err|<=3 of 100 on the
control; the target's proposed edge is logged only if the control passes. A value-redraw null on the target
(TT-FREQ C1's null: each numeric token redrawn uniformly over the file's [min,max], 20 seeds) is reported beside it."""
import sys, random, re
from collections import Counter
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "design")); sys.path.insert(0, str(HERE.parents[2] / "tools"))
import design_stats as D, freq
corp = D.en18_words(); allw = Counter(w for f in corp for w in f)
particles = [w for w, _ in allw.most_common(400)][:99]; stopset = set(particles)
content = [w for w, _ in allw.most_common(3000) if w not in stopset][:1800]
def seq_pblock(r):
    vv = list(range(100, 1900)); r.shuffle(vv)
    t = {i + 1: p for i, p in enumerate(particles[:99])}; t.update(dict(zip(vv, content)))
    c = D.TableCode(t); c.drops = 0; c.enc_only = True; return c
def sample_words(r, k):
    f = r.choice(corp); i = r.randrange(0, len(f) - k); return f[i:i + k]
def show(res):
    s = res["singles"][0] if res["singles"] else (0.0, None)
    b = res["band"]
    return s, b
N = 369; errs = []
print("CONTROL seq_pblock, known edge 100")
for sd in range(1000, 1005):
    r = random.Random(sd); code = seq_pblock(r); t = []
    while len(t) < N:
        code.drops = 0; t = code.encode(sample_words(r, N * 2), r)[:N]
    toks = [str(x) for x in t]
    (g, n), band = show(freq.split_auto(toks))
    low = sum(1 for x in t if x < 100)
    err = None if n is None else n - 100; errs.append(err)
    print(f"seed {sd}: low<100 {low}/{N}  best single N={n} gain={g:.1f} err={err}  band={band}")
ok = sum(1 for e in errs if e is not None and abs(e) <= 3)
print(f"control seeds within |err|<=3: {ok}/5")
gate = ok >= 4
print("CONTROL", "PASS" if gate else "BELOW GATE")
tgt = [t for l in open(HERE.parent / "ciphertext.txt") if not l.startswith('#') for t in l.split() if re.fullmatch(r"\d+", t)]
if gate:
    (g, n), band = show(freq.split_auto(tgt))
    print(f"TARGET: best single N={n} gain={g:.1f} band={band} singles={freq.split_auto(tgt)['singles']}")
    vals = [int(x) for x in tgt]; lo, hi = min(vals), max(vals); nn = []
    for sd in range(20):
        rr = random.Random(sd); z = [str(rr.randint(lo, hi)) for _ in vals]
        s2 = freq.split_auto(z)["singles"]; nn.append(s2[0][1] if s2 and s2[0][0] >= 10 else None)
    print("value-redraw null best N (gain>=10 else None):", nn)
else:
    print("TARGET not run (control below gate)")
