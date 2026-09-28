"""Line B step B2 -- which hierarchical layout reproduces B1's decade-family statistics?

Designs simulated on en18 text (60 windows of 369 coded tokens each; words outside the design's vocabulary are
dropped as shorthand-run wildcards, the target's own device for OOV words):
  A   stem + class slots, two stem series: the 90 most frequent stems -> heads 10-99 (bare head = base form),
      inflected forms 10h+c with a FIXED class->digit map (s/es 0, ed 1, est 2, ion 3, ing 4, ment 5, ly 6, er 7,
      ness/ity 8, other 9); stems ranked 91-180 -> series 1: base 1h0, classes 1h+c (c>=1, same map, 'other' folded to 9).
  A2  stem + class slots, ONE series: heads 10-99 = 90 stems, 10h+c = inflection classes, 1000+10h+c = a second
      class dimension on the same stem (e.g. the class forms of a derived word), 90 stems only, rest wildcard.
  B   alphabetical buckets: the 1990 most frequent words sorted alphabetically into 90 buckets; the bucket's most
      frequent word is the 2-digit head, its next members in ALPHABETICAL order fill 10h+0..9 then 1h0..1h9.
  Bf  as B but members ordered by FREQUENCY within the bucket (z = 0 the commonest after the head).
  C   three separately alphabetical tiers: the 90 most frequent words -> 10-99 alphabetically; the next 1900 words
      sorted alphabetically and dealt alternately to 100-999 and 1000-1999 (both tiers span the alphabet).
  C2  as C but tier 2 = words ranked 91-990, tier 3 = words ranked 991-1990 (a frequency split), each alphabetical.
Statistics (B1, family_test.py): r_fam, r_1xyz, r_34, r_row, S_w, z0 share and {2,3,5,9} share per tier.
Run: python3 designs.py [--sims 60] (offline, about 1 minute)."""
import argparse, gzip, random, re, sys
from collections import Counter, defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent; TDIR = HERE.parents[1]; REPO = TDIR.parents[1]
sys.path.insert(0, str(HERE.parent / "b1"))
from padding_test import target_tokens, en18_words

V = list(range(10, 100))
def corr(xs, ys):
    mx = sum(xs)/len(xs); my = sum(ys)/len(ys)
    sxy = sum((x-mx)*(y-my) for x, y in zip(xs, ys)); sxx = sum((x-mx)**2 for x in xs); syy = sum((y-my)**2 for y in ys)
    return sxy / (sxx*syy) ** 0.5 if sxx and syy else 0.0
def stats(t):
    cc = Counter(t); heads = [cc[v] for v in V]
    f3 = [sum(cc[10*v+u] for u in range(10)) for v in V]; f4 = [sum(cc[1000+10*v+u] for u in range(10)) for v in V]
    rows = [sum(cc[100*h+v] for h in range(1, 19)) for v in V]
    part = [v for v in t if v < 100]
    sw = sum(1 for v in part if 10*v in cc) / max(1, len(part))
    t3 = [v for v in t if 100 <= v < 1000]; t4 = [v for v in t if v >= 1000]
    z0_3 = sum(1 for v in t3 if v % 10 == 0) / max(1, len(t3)); z0_4 = sum(1 for v in t4 if v % 10 == 0) / max(1, len(t4))
    rare3 = sum(1 for v in t3 if v % 10 in (2, 3, 5, 9)) / max(1, len(t3)); rare4 = sum(1 for v in t4 if v % 10 in (2, 3, 5, 9)) / max(1, len(t4))
    return dict(r_fam=corr(heads, f3), r_1xyz=corr(heads, f4), r_34=corr(f3, f4), r_row=corr(heads, rows), S_w=sw,
                z0_3=z0_3, z0_4=z0_4, rare3=rare3, rare4=rare4, part_share=len(part)/len(t), n3=len(t3), n4=len(t4),
                distinct=len(cc), singletons=sum(1 for n in cc.values() if n == 1))
KEYS = ["r_fam", "r_1xyz", "r_34", "r_row", "S_w", "z0_3", "z0_4", "rare3", "rare4", "part_share", "distinct", "singletons"]

SUFFIXES = [("ness", 8), ("ity", 8), ("ment", 5), ("tion", 3), ("sion", 3), ("ing", 4), ("est", 2), ("ly", 6),
            ("er", 7), ("or", 7), ("ed", 1), ("es", 0), ("s", 0)]
def stem_class(w):
    for suf, c in SUFFIXES:
        if len(w) > len(suf) + 2 and w.endswith(suf):
            return w[:-len(suf)], c
    return w, None   # base form

def build(words, design, rng):
    freq = Counter(w for ws in words for w in ws)
    code = {}
    if design in ("A", "A2"):
        stemfreq = Counter(); forms = defaultdict(Counter)
        for w, n in freq.items():
            s, c = stem_class(w); stemfreq[s] += n; forms[s][w] += n
        ranked = [s for s, _ in stemfreq.most_common(180)]
        for i, s in enumerate(ranked):
            if i < 90:
                h = 10 + i
                for w in forms[s]:
                    _, c = stem_class(w)
                    code[w] = h if c is None else 10*h + c
            elif design == "A":
                h = 10 + i - 90
                for w in forms[s]:
                    _, c = stem_class(w)
                    code[w] = 1000 + 10*h + (0 if c is None else max(1, c))
        if design == "A2":   # second dimension: the 90 stems' forms that collide (same class twice) go to 1000+
            seen = Counter()
            for w in list(code):
                v = code[w]
                if v >= 100:
                    seen[v] += 1
                    if seen[v] > 1: code[w] = 1000 + v
    elif design in ("B", "Bf"):
        top = [w for w, _ in freq.most_common(1990)]
        top.sort()
        size = len(top) / 90.0
        for b in range(90):
            bucket = top[int(b*size):int((b+1)*size)]
            bucket_f = sorted(bucket, key=lambda w: -freq[w])
            head = bucket_f[0]; code[head] = 10 + b
            rest = bucket_f[1:] if design == "Bf" else sorted(bucket_f[1:])
            for j, w in enumerate(rest[:20]):
                code[w] = (10*(10+b) + j) if j < 10 else (1000 + 10*(10+b) + j - 10)
    elif design in ("C", "C2"):
        ranked = [w for w, _ in freq.most_common(1990)]
        t1 = sorted(ranked[:90])
        for i, w in enumerate(t1): code[w] = 10 + i
        if design == "C":
            rest = sorted(ranked[90:]); t2 = rest[0::2][:900]; t3 = rest[1::2][:1000]
        else:
            t2 = sorted(ranked[90:990]); t3 = sorted(ranked[990:1990])
        for i, w in enumerate(t2): code[w] = 100 + i
        for i, w in enumerate(t3): code[w] = 1000 + i
    return code

def simulate(words, code, rng, n=369):
    ws = rng.choice(words); start = rng.randint(0, len(ws) - 3000)
    out = []
    for w in ws[start:]:
        if w in code: out.append(code[w])
        if len(out) == n: break
    return out

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--sims", type=int, default=60); a = ap.parse_args()
    words = en18_words()
    tgt = stats(target_tokens())
    print("TARGET: " + "  ".join(f"{k}={tgt[k]:.3f}" if isinstance(tgt[k], float) else f"{k}={tgt[k]}" for k in KEYS))
    print(f"\n{'design':7s}{'stat':11s}{'mean':>8s}{'sd':>7s}{'p05':>8s}{'p95':>8s}{'target':>8s}{'pct':>7s}")
    for design in ("A", "A2", "B", "Bf", "C", "C2"):
        rng = random.Random(7)
        code = build(words, design, rng)
        rows = [stats(simulate(words, code, random.Random(1000 + i))) for i in range(a.sims)]
        for k in KEYS:
            arr = sorted(r[k] for r in rows); m = sum(arr)/len(arr); sd = (sum((x-m)**2 for x in arr)/len(arr))**0.5
            pct = 100*sum(1 for x in arr if x < tgt[k])/len(arr)
            print(f"{design:7s}{k:11s}{m:8.3f}{sd:7.3f}{arr[int(.05*len(arr))]:8.3f}{arr[int(.95*len(arr))]:8.3f}{tgt[k]:8.3f}{pct:7.1f}")
        print()

if __name__ == "__main__":
    main()
