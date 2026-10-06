"""R8-SIENA19 (6 Oct 2026): no. 19's signs against the no. 13/16 alignment (Bourdeau) as a known-key fit.
Pre-registered in ciphers/siena-concistoro-2308/PREREG-R8-SIENA19.md (pushed before this ran).
S1 order-free count fit (sum log10 binomial upper tail); S2 mean it16 bigram log10 prob over adjacent covered pairs.
Controls: (a) 2000 value-shuffled keys from the key's own ten letters (S1, S2); (b) 200 order-shuffled streams (S2 only:
order cannot change S1). Positive control: 100 it16 passages of N letters, H1a (every matched-letter occurrence is the
matched sign) and H1b (half of them), power = share reaching the gate (p <= 0.05 vs 500 value shuffles).
POST HOC (not in the PREREG, reported as such): posthoc_S1_true_key_le_real = share of H1 passages whose TRUE-key S1 is
as low as no. 19's real S1 (how often H1 itself produces the observed count misfit).
Run: python3 specs/cheap-tests/siena-concistoro-2308/run_test_no19.py [--check]   (deterministic; --check compares
results_no19.json and exits 1 if stale)
"""
import sys, os, json, math, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "../../.."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import judge_plaintext as jp

LETTERS = list("abcdgilnor")
VARIANTS = {"P": {"TRI": "b", "3": "l", "CT": "r"},
            "V2": {"TRI": "b", "3": "l", "CT": "r", "0": "a", "TT": "r"}}

text = "".join(c for p in jp.LANG_CORPORA["it"] for c in jp.read_corpus(p).lower() if "a" <= c <= "z")
uni = Counter(text); tot = sum(uni.values()); P = {c: uni[c] / tot for c in uni}
bi = Counter(text[i:i + 2] for i in range(len(text) - 1))
def lbig(a, b): return math.log10((bi[a + b] + 1) / (uni[a] + 26))

def load():
    p = os.path.join(ROOT, "ciphers/siena-concistoro-2308/transcripts/no19.tok")
    return " ".join(l for l in open(p) if not l.startswith("#")).split()

def tail(n, k, p):  # P(X >= k), X ~ Bin(n, p)
    return sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k, n + 1))

def s1(counts, key, n):
    return sum(math.log10(max(tail(n, counts[s], P[v]), 1e-300)) for s, v in key.items() if counts.get(s, 0))

def pairs(stream, key):
    out = []
    for a, b in zip(stream, stream[1:]):
        if a in key and b in key: out.append((key[a], key[b]))
    return out

def s2(stream, key):
    pr = pairs(stream, key)
    return (sum(lbig(a, b) for a, b in pr) / len(pr)) if pr else None

def shuf_key(key, rnd):  # distinct values per distinct... each sign a value from the ten letters, distinct across signs
    signs = list(key); vals = rnd.sample(LETTERS, len(signs)); return dict(zip(signs, vals))

def rank_p(real, ctrl):
    c = [x for x in ctrl if x is not None]
    return (sum(1 for x in c if x >= real) + 1) / (len(c) + 1), len(c)

def run():
    T = load(); stream = T  # "|" kept as a breaker for S2
    toks = [t for t in T if t != "|"]; n = len(toks); counts = Counter(toks)
    res = {"N": n, "variants": {}}
    for vname, key in VARIANTS.items():
        rnd = random.Random(19)
        r = {"covered": sum(counts[s] for s in key), "counts": {s: counts[s] for s in key},
             "expected_counts": {s: round(n * P[v], 2) for s, v in key.items()}}
        R1 = s1(counts, key, n); R2 = s2(stream, key)
        ks = [shuf_key(key, rnd) for _ in range(2000)]
        C1 = [s1(counts, k, n) for k in ks]; C2 = [s2(stream, k) for k in ks]
        O2 = []
        for _ in range(200):
            t = toks[:]; rnd.shuffle(t); O2.append(s2(t, key))
        p1, _ = rank_p(R1, C1); p2, m2 = rank_p(R2, C2) if R2 is not None else (None, 0)
        o2 = [x for x in O2 if x is not None]
        r.update({"S1_real": round(R1, 3), "S1_valshuf_mean": round(sum(C1) / len(C1), 3),
                  "S1_valshuf_p95": round(sorted(C1)[int(0.95 * len(C1))], 3), "S1_p": round(p1, 4),
                  "S2_pairs": [a + b for a, b in pairs(stream, key)],
                  "S2_real": None if R2 is None else round(R2, 3),
                  "S2_valshuf_mean": round(sum(x for x in C2 if x is not None) / max(1, m2), 3),
                  "S2_p": None if p2 is None else round(p2, 4),
                  "S2_ordershuf_mean": round(sum(o2) / len(o2), 3) if o2 else None,
                  "S2_ordershuf_n_with_pairs": len(o2),
                  "S2_ordershuf_ge_real": sum(1 for x in o2 if R2 is not None and x >= R2)})
        # positive control
        pw = {}
        for h, keep in (("H1a", 1.0), ("H1b", 0.5)):
            prnd = random.Random(1913); hit1 = hit2 = n2 = 0; low1 = 0
            for _ in range(100):
                o = prnd.randrange(len(text) - n); pas = text[o:o + n]
                letters = sorted(set(key.values())); signs_for = {}
                for s, v in key.items(): signs_for.setdefault(v, []).append(s)
                st = []
                for ch in pas:
                    if ch in signs_for and prnd.random() < keep: st.append(prnd.choice(signs_for[ch]))
                    else: st.append("x" + ch)  # uncovered token
                cnt = Counter(st); a1 = s1(cnt, key, n); a2 = s2(st, key)
                if a1 <= R1: low1 += 1
                kk = [shuf_key(key, prnd) for _ in range(500)]
                if s1(cnt, key, n) is not None and rank_p(a1, [s1(cnt, k, n) for k in kk])[0] <= 0.05: hit1 += 1
                if a2 is not None:
                    n2 += 1
                    if rank_p(a2, [s2(st, k) for k in kk])[0] <= 0.05: hit2 += 1
            pw[h] = {"posthoc_S1_true_key_le_real": low1 / 100, "S1_power": hit1 / 100, "S2_power": hit2 / 100, "S2_passages_with_pairs": n2}
        r["positive_control"] = pw
        res["variants"][vname] = r
    return res

if __name__ == "__main__":
    res = run(); outp = os.path.join(HERE, "results_no19.json"); s = json.dumps(res, indent=1, ensure_ascii=False)
    if "--check" in sys.argv:
        ok = open(outp).read().strip() == s.strip(); print("check:", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(outp, "w").write(s + "\n"); print(s)
