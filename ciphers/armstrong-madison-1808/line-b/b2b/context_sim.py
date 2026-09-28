"""Line B step B2b -- operator digit vs sparse-grid slot, by context similarity within a row.

Parse every group as (row, form): 2-digit xy -> row xy, bare head; xyz -> row xy, form (0, z); 1xyz -> row xy, form
(1, z); single digits -> their own class. Each token's context = class of the previous and of the next symbol in the
letter (H bare head, T3 3-digit, T4 4-digit, D single digit, S shorthand run, E line edge / illegible). Each distinct
value gets a 12-cell context histogram. Statistic: the mean over rows with >= 2 distinct forms of the mean pairwise
similarity (1 - Jensen-Shannon divergence, base 2) between the row's forms, each pair weighted by min(count) so that
singleton forms do not dominate. Null (rule 3): permute row labels among distinct values within the same tier and
count bin (1, 2, 3-4, 5+), keeping every value's own context histogram (2,000 draws).
Positive control: en18 windows encoded with a real inflection grammar (crude stemmer: words sharing a stem share a row,
the class digit is the suffix), 3 seeds; negative control: B2's Bf layout (different words per row), 3 seeds.
Gate: positive control above its null p95 on 3 of 3 seeds, negative control not, before the target is read.
Run: python3 context_sim.py  (offline, about 30 s)."""
import math, random, sys
from collections import Counter, defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent; TDIR = HERE.parents[1]
sys.path.insert(0, str(HERE.parent / "b1")); sys.path.insert(0, str(HERE.parent / "b2"))
from padding_test import en18_words
import designs

CLASSES = ["H", "T3", "T4", "D", "S", "E"]
def cls(t):
    if t is None: return "E"
    if isinstance(t, str): return "S" if t.startswith("*") else "E"
    if t < 10: return "D"
    if t < 100: return "H"
    if t < 1000: return "T3"
    return "T4"
def row_of(v):
    if v < 10: return None
    if v < 100: return v
    if v < 1000: return v // 10
    return (v - 1000) // 10

def target_seq():
    seq = []
    for line in open(TDIR / "ciphertext.txt", encoding="utf-8"):
        if line.startswith("#"): continue
        seq.append(None)   # line edge
        for t in line.split():
            seq.append(int(t) if t.isdigit() else t)
    seq.append(None)
    return seq

def histograms(seq):
    """value -> 12-cell context histogram (prev classes, next classes) and count."""
    H = defaultdict(lambda: [0.0] * 12); C = Counter()
    for i, t in enumerate(seq):
        if isinstance(t, int) and t >= 10:
            p = cls(seq[i-1] if i > 0 else None); n = cls(seq[i+1] if i+1 < len(seq) else None)
            H[t][CLASSES.index(p)] += 1; H[t][6 + CLASSES.index(n)] += 1; C[t] += 1
    return H, C

def jsd(a, b):
    def norm(x):
        s = sum(x); return [v / s for v in x] if s else x
    a = norm(a); b = norm(b); m = [(x + y) / 2 for x, y in zip(a, b)]
    def kl(p, q): return sum(x * math.log2(x / y) for x, y in zip(p, q) if x > 0)
    return (kl(a, m) + kl(b, m)) / 2

def statistic(H, C, rowmap):
    rows = defaultdict(list)
    for v in H:
        r = rowmap[v]
        if r is not None: rows[r].append(v)
    vals = []; ws = []
    for r, vs in rows.items():
        if len(vs) < 2: continue
        sims = []; w = []
        for i in range(len(vs)):
            for j in range(i + 1, len(vs)):
                sims.append(1 - jsd(H[vs[i]], H[vs[j]])); w.append(min(C[vs[i]], C[vs[j]]))
        vals.append(sum(s * x for s, x in zip(sims, w)) / sum(w)); ws.append(sum(w))
    return sum(v * x for v, x in zip(vals, ws)) / sum(ws), len(vals)

def bins(c): return 0 if c == 1 else 1 if c == 2 else 2 if c <= 4 else 3
def run(label, seq, rng, draws=2000):
    H, C = histograms(seq)
    rowmap = {v: row_of(v) for v in H}
    s, nrows = statistic(H, C, rowmap)
    # null: permute row labels within (tier, count bin)
    groups = defaultdict(list)
    for v in H: groups[(cls(v), bins(C[v]))].append(v)
    null = []
    for _ in range(draws):
        rm = {}
        for g, vs in groups.items():
            labels = [rowmap[v] for v in vs]; rng.shuffle(labels)
            for v, l in zip(vs, labels): rm[v] = l
        null.append(statistic(H, C, rm)[0])
    null.sort(); p95 = null[int(.95 * len(null))]; p99 = null[int(.99 * len(null))]
    pct = 100 * sum(1 for x in null if x < s) / len(null)
    print(f"{label:48s} rows>=2 forms {nrows:3d}  stat {s:.3f}  null mean {sum(null)/len(null):.3f} p95 {p95:.3f} p99 {p99:.3f}  pct {pct:5.1f}")
    return s, p95, pct

def synth_seq(words, code, rng, n=369):
    """like designs.simulate but keeps OOV words as shorthand-run markers and inserts line edges every ~24 tokens."""
    ws = rng.choice(words); start = rng.randint(0, len(ws) - 3000); out = [None]; k = 0
    for w in ws[start:]:
        if w in code:
            out.append(code[w]); k += 1
            if k % 24 == 0: out.append(None)
            if k == n: break
        elif not (isinstance(out[-1], str)): out.append("*")
    out.append(None); return out

def main():
    rng = random.Random(21)
    words = en18_words()
    print("=== POSITIVE CONTROL: stem + class-digit grammar (design A of B2; forms of one stem share a row) ===")
    codeA = designs.build(words, "A", random.Random(7))
    pos = [run(f"A stem grammar seed {i}", synth_seq(words, codeA, random.Random(500 + i)), rng) for i in range(3)]
    print("=== NEGATIVE CONTROL: Bf alphabetical buckets, frequency-ordered members (different words per row) ===")
    codeB = designs.build(words, "Bf", random.Random(7))
    neg = [run(f"Bf buckets seed {i}", synth_seq(words, codeB, random.Random(700 + i)), rng) for i in range(3)]
    gate = all(p[2] >= 95 for p in pos) and sum(1 for n in neg if n[2] >= 95) <= 1
    print(f"\nGATE (positive 3/3 above p95, negative <=1/3): {'MET' if gate else 'NOT MET'} -- positives {[round(p[2],1) for p in pos]}, negatives {[round(n[2],1) for n in neg]}")
    print("\n=== TARGET ===")
    run("TARGET armstrong-madison-1808", target_seq(), rng)

if __name__ == "__main__":
    main()
