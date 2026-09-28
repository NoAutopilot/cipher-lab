"""Line B step B1 -- trailing-zero padding as a homophone device (28 Sept 2026).

Hypothesis: the key permits zeros appended on the right without changing the meaning (the rule the frame-127
compact Livingston key states, ChatGPT PR 50 / campaign H7), so a frequent 1-99 value v is also written 10v.
Statistic S_w: share of particle TOKENS (values 1-99) whose x10 form (100-990) is present in the letter;
S_u: the same over distinct particle values; S3: share of 3-digit tokens whose x10 form (1000-1990) is present.
Null (rule 3, can differ): keep the particle set fixed, redraw the set of distinct x0 book values among the
multiples of 10 in [100, 1900], (a) uniformly, (b) weighted by the target's own hundreds-block token profile
(so the 800-1099 trough is respected). Negative control: the four real THE=972 letters (no padding rule).
Positive control: en18 letters encoded with a 99-word particle list (values 1-99) and a book (100-1899),
particles padded with probability p, book units flat or 0-heavy (target's 0.39), same N; 3 seeds each.
Gate (pre-registered before any target number was printed): the positive control at p=0.3 clears its null p95 on
3 of 3 seeds AND the negative control does not clear p95 on 3 of 4 letters; only then is the target's own
percentile read as evidence either way.
Run: python3 padding_test.py [--draws 2000]  (offline, ~20 s)
"""
import argparse, gzip, importlib.util, random, re, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
TDIR = HERE.parents[1]                      # ciphers/armstrong-madison-1808
REPO = TDIR.parents[1]
US = REPO / "tools" / "data" / "uscodes-1800"
EN18 = REPO / "tools" / "data" / "en18"


def target_tokens():
    toks = []
    for line in open(TDIR / "ciphertext.txt", encoding="utf-8"):
        if line.startswith("#"):
            continue
        toks += [int(t) for t in line.split() if t.isdigit()]
    return toks


def usage_instances():
    spec = importlib.util.spec_from_file_location("ustats", US / "stats.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return {k: [int(x) for x in v.split()] for k, v in m.THE972_USAGE.items()}


def stat(toks):
    c = Counter(toks)
    present = set(c)
    part = [v for v in toks if v < 100]
    three = [v for v in toks if 100 <= v < 1000]
    sw = sum(1 for v in part if 10 * v in present) / max(1, len(part))
    dp = sorted(set(part))
    su = sum(1 for v in dp if 10 * v in present) / max(1, len(dp))
    s3 = sum(1 for v in three if 10 * v in present) / max(1, len(three))
    return sw, su, s3


def null_draws(toks, rng, draws, weighted, vmax=1900):
    """Redraw the distinct x0 book values (>=100, %10==0) among multiples of 10 in [100, vmax]."""
    c = Counter(toks)
    x0 = sorted(v for v in c if v >= 100 and v % 10 == 0)
    others = [v for v in toks if not (v >= 100 and v % 10 == 0)]
    pool = list(range(100, vmax + 1, 10))
    if weighted:
        hb = Counter(v // 100 for v in toks if v >= 100)
        w = [hb.get(p // 100, 0) + 0.25 for p in pool]   # +0.25: no hundred has zero weight
    else:
        w = [1.0] * len(pool)
    # multiplicity of each x0 value is kept, the value is redrawn
    mult = [c[v] for v in x0]
    out = []
    for _ in range(draws):
        chosen = []
        avail = pool[:]; aw = w[:]
        for _ in x0:
            i = rng.choices(range(len(avail)), weights=aw)[0]
            chosen.append(avail.pop(i)); aw.pop(i)
        t = others[:]
        for v, m in zip(chosen, mult):
            t += [v] * m
        out.append(stat(t))
    return out


def pct(x, arr):
    return 100.0 * sum(1 for a in arr if a < x) / len(arr)


def summarize(label, toks, rng, draws):
    s = stat(toks)
    res = {}
    for wname, weighted in (("uniform", False), ("hundreds-weighted", True)):
        nd = null_draws(toks, rng, draws, weighted, vmax=max(1900, max(toks)))
        for k, name in enumerate(("S_w", "S_u", "S3")):
            arr = [d[k] for d in nd]
            arr_s = sorted(arr)
            p95 = arr_s[int(0.95 * len(arr_s))]
            res[(wname, name)] = (s[k], sum(arr) / len(arr), p95, pct(s[k], arr))
    n = len(toks); npart = sum(1 for v in toks if v < 100)
    print(f"\n{label}: N={n}, particle tokens={npart}, distinct particles={len(set(v for v in toks if v < 100))}, "
          f"distinct x0 book values={len(set(v for v in toks if v>=100 and v%10==0))}")
    print("null            stat   target  null_mean  null_p95  percentile")
    for (wname, name), (v, m, p95, pc) in res.items():
        print(f"{wname:17s} {name:5s} {v:7.3f} {m:9.3f} {p95:9.3f} {pc:9.1f}")
    return res


# ---------------- positive control ----------------
def en18_words():
    words = []
    for p in sorted(EN18.glob("*.txt.gz")):
        t = gzip.open(p, "rt", encoding="utf-8", errors="replace").read().lower()
        ws = re.findall(r"[a-z]+", t)
        n = len(ws)
        words.append(ws[int(n * 0.1):int(n * 0.9)])
    return words


def synth(words, rng, n_tokens, p_pad, zero_heavy):
    """Encode a random 369-token window: 99 commonest words -> values 1-99 (random order), other words -> a
    book value in 100-1899 (a random hundreds block, a random decade, units 0 with prob zero_heavy else
    uniform 1-9); particles padded (v -> 10 v) with probability p_pad."""
    freq = Counter(w for ws in words for w in ws)
    top99 = [w for w, _ in freq.most_common(99)]
    pv = dict(zip(top99, rng.sample(range(1, 100), 99)))
    book = {}
    def bookval(w):
        if w not in book:
            while True:
                h = rng.randint(1, 18); d = rng.randint(0, 9)
                u = 0 if rng.random() < zero_heavy else rng.randint(1, 9)
                v = 100 * h + 10 * d + u
                if v not in book.values():
                    book[w] = v; break
        return book[w]
    ws = rng.choice(words)
    start = rng.randint(0, len(ws) - n_tokens - 1)
    toks = []
    for w in ws[start:start + n_tokens]:
        if w in pv:
            v = pv[w]
            if rng.random() < p_pad:
                v *= 10
            toks.append(v)
        else:
            toks.append(bookval(w))
    return toks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--draws", type=int, default=2000)
    ap.add_argument("--seeds", type=int, default=3)
    a = ap.parse_args()
    rng = random.Random(11)
    print("=== NEGATIVE CONTROL: real THE=972 letters (no padding rule) ===")
    for k, v in usage_instances().items():
        summarize(f"THE972 {k}", v, rng, a.draws)
    print("\n=== POSITIVE CONTROL: en18 synthetic, 369 tokens ===")
    words = en18_words()
    for zero_heavy in (0.10, 0.39):
        for p_pad in (0.0, 0.3, 0.5):
            for seed in range(a.seeds):
                r = random.Random(100 * seed + int(1000 * p_pad) + int(zero_heavy * 10))
                toks = synth(words, r, 369, p_pad, zero_heavy)
                summarize(f"SYNTH zero_heavy={zero_heavy} p_pad={p_pad} seed={seed}", toks, rng, a.draws)
    print("\n=== TARGET (read only after the gate above) ===")
    summarize("TARGET armstrong-madison-1808 ciphertext.txt", target_tokens(), rng, a.draws)


if __name__ == "__main__":
    main()
