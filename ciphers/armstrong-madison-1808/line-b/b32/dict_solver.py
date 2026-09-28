"""Line B step B32 -- dictionary-constrained sign-to-letter substitution over the 54 words B30 found (type 20 = space).
Score of a map: sum over segments of log(1 + freq(word)) if the decoded string is an en18 dictionary word, else a
small letter-bigram log-probability term (tiebreak / partial credit). Search: simulated annealing over maps from the
34 signs to 26 letters (homophones allowed), 24 restarts x 25,000 proposals (reassign one sign, or swap two signs).
Controls first (rule 3): 3 synthetic runs -- 54 consecutive en18 words (held-out volume, Jefferson IX), letters ->
34 signs with 8 extra homophones on the commonest letters, spaces = sign 20 -- gate = >= 60 percent of words right on
3 of 3; then a shuffled-target floor (sign identities permuted within segments) beside the target if the gate is met.
Run: python3 dict_solver.py [--restarts 24 --steps 25000]"""
import argparse, gzip, math, random, re, sys
from collections import Counter
from pathlib import Path
HERE = Path(__file__).resolve().parent; REPO = HERE.parents[3]
ALPHA = "abcdefghijklmnopqrstuvwxyz"
frags = [l.strip().split(';') for l in open(REPO / "ciphers/armstrong-madison-1808/codex-2026-09-27b/glyphs.txt") if l.strip()]
def segments(fr):
    out = []
    for f in fr:
        cur = []
        for g in f:
            if g == '20':
                if cur: out.append(cur); cur = []
            else: cur.append(g)
        if cur: out.append(cur)
    return out
TARGET = segments(frags); SIGNS = sorted(set(g for s in TARGET for g in s))
# corpus
paths = sorted((REPO / "tools/data/en18").glob("*.txt.gz"))
train = [p for p in paths if "jeff" not in p.name]; held = [p for p in paths if "jeff" in p.name]
def words_of(p):
    t = gzip.open(p, "rt", encoding="utf-8", errors="replace").read().lower(); n = len(t)
    return re.findall(r"[a-z]+", t[int(n*0.1):int(n*0.9)])
train_words = [w for p in train for w in words_of(p)]
FREQ = Counter(train_words); DICT = {w: math.log1p(n) for w, n in FREQ.items() if n >= 2}
BG = Counter(); UNI = Counter()
for w in train_words[:600000]:
    s = " " + w + " "
    for a, b in zip(s, s[1:]): BG[(a, b)] += 1; UNI[a] += 1
def bg_lp(word):
    s = " " + word + " "; lp = 0.0
    for a, b in zip(s, s[1:]): lp += math.log((BG[(a, b)] + 0.5) / (UNI[a] + 14))
    return lp
def score(segs, m):
    tot = 0.0
    for s in segs:
        w = "".join(m[g] for g in s)
        if w in DICT: tot += 3.0 + DICT[w]
        else: tot += 0.15 * bg_lp(w)
    return tot
CAP = 2   # at most two signs per letter (the controls' own homophone design)
def solve(segs, signs, rng, restarts, steps):
    best = (-1e18, None)
    for r in range(restarts):
        while True:
            m = {g: rng.choice(ALPHA) for g in signs}
            if max(Counter(m.values()).values()) <= CAP: break
        cur = score(segs, m); T0, T1 = 3.0, 0.05; use = Counter(m.values())
        for i in range(steps):
            T = T0 * (T1 / T0) ** (i / steps); g = rng.choice(signs); old = m[g]
            if rng.random() < 0.7:
                c = rng.choice(ALPHA)
                if use[c] >= CAP or c == old: continue
                m[g] = c; use[old] -= 1; use[c] += 1; undo = [(g, old)]
            else:
                h = rng.choice(signs)
                if h == g: continue
                m[g], m[h] = m[h], m[g]; undo = [(g, old), (h, m[g])]
            new = score(segs, m)
            if new >= cur or rng.random() < math.exp((new - cur) / T): cur = new
            else:
                for k, v in undo: m[k] = v
                use = Counter(m.values())
        if cur > best[0]: best = (cur, dict(m))
    return best
def synth(rng):
    ws = words_of(rng.choice(held)); start = rng.randint(0, len(ws) - 200); words = ws[start:start + 54]
    letters = Counter(c for w in words for c in w); common = [c for c, _ in letters.most_common(8)]
    signs = SIGNS[:]; rng.shuffle(signs); key = {}
    for c, g in zip(ALPHA, signs[:26]): key[c] = [g]
    for c, g in zip(common, signs[26:34]): key[c].append(g)
    segs = []
    for w in words:
        segs.append([rng.choice(key[c]) for c in w])
    return words, segs
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--restarts", type=int, default=24); ap.add_argument("--steps", type=int, default=25000)
    ap.add_argument("--skip-controls", action="store_true"); a = ap.parse_args()
    rng = random.Random(17); ok = 0
    if not a.skip_controls:
        for k in range(3):
            words, segs = synth(random.Random(100 + k)); sc, m = solve(segs, SIGNS, rng, a.restarts, a.steps)
            dec = ["".join(m[g] for g in s) for s in segs]; right = sum(1 for d, w in zip(dec, words) if d == w)
            print(f"control {k}: score {sc:.1f}, words right {right}/54 = {100*right/54:.0f}%  e.g. {' '.join(dec[:8])} | truth {' '.join(words[:8])}", flush=True)
            ok += right / 54 >= 0.6
        print("GATE (>= 60% on 3 of 3):", "MET" if ok == 3 else "NOT MET", flush=True)
    sc, m = solve(TARGET, SIGNS, rng, a.restarts, a.steps)
    dec = ["".join(m[g] for g in s) for s in TARGET]; inD = sum(1 for d in dec if d in DICT)
    print(f"TARGET: score {sc:.1f}, dictionary words {inD}/54; map {sorted(m.items())}")
    print("TARGET decode:", " ".join(dec))
    # shuffled-target floor: sign identities permuted within the whole sequence, segment lengths kept
    floors = []
    for k in range(3):
        r2 = random.Random(900 + k); flat = [g for s in TARGET for g in s]; r2.shuffle(flat); it = iter(flat)
        sh = [[next(it) for _ in s] for s in TARGET]; s2, m2 = solve(sh, SIGNS, rng, a.restarts, a.steps)
        d2 = ["".join(m2[g] for g in s) for s in sh]; floors.append((s2, sum(1 for d in d2 if d in DICT)))
        print(f"shuffled floor {k}: score {s2:.1f}, dictionary words {floors[-1][1]}/54  e.g. {' '.join(d2[:10])}", flush=True)
if __name__ == "__main__":
    main()
