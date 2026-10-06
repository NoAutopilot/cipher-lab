"""R9-SIENA15 (6 Oct 2026): no. 15 (R4803) against key R4764 through the shape concordance
ciphers/siena-concistoro-2308/concordance_R4764_no15.tsv. Pre-registered in PREREG-R9-SIENA15.md (pushed in cc19de4a4 first).
S2 = mean it16 bigram log10 prob over adjacent letter pairs inside maximal valued stretches (nulls dropped; '|' and
unvalued signs break). Controls: (a) 2000 value-shuffled keys; (b) 200 order-shuffled streams. Gate: p_a <= 0.05 and
real > p95(b). Positive control: 100 it16 passages enciphered under H1 (see PREREG); power >= 0.8 or the miss is a non-test.
Run: python3 specs/cheap-tests/siena-concistoro-2308/run_test_no15.py [--check]  (deterministic; --check exits 1 if
results_no15.json is stale)
"""
import sys, os, json, math, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "../../.."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import judge_plaintext as jp
FOLD = os.path.join(ROOT, "ciphers/siena-concistoro-2308")

text = "".join(c for p in jp.LANG_CORPORA["it"] for c in jp.read_corpus(p).lower() if "a" <= c <= "z")
uni = Counter(text); bi = Counter(text[i:i + 2] for i in range(len(text) - 1))
LB = {}
def lbig(a, b):
    k = a + b
    if k not in LB: LB[k] = math.log10((bi[k] + 1) / (uni[a] + 26))
    return LB[k]

def load_tokens():
    out = []
    for l in open(os.path.join(FOLD, "transcripts/no15.tok")):
        if l.startswith("#") or not l.strip(): continue
        out += l.split()[1:]
    return out

def load_conc():
    P, V = {}, {}
    for l in open(os.path.join(FOLD, "concordance_R4764_no15.tsv")):
        if l.startswith("# ") or l.startswith("no15_sign"): continue  # the sign "#" starts a data row
        f = l.rstrip("\n").split("\t")
        (P if f[1] == "P" else V)[f[0]] = f[2]
    Vf = dict(P); Vf.update(V)
    return {"P": P, "V": Vf}

def norm(v): return "et" if v == "&" else v

def s2(stream, key):
    tot = n = 0; prev = None
    for t in stream:
        v = key.get(t)
        if v == "NULL": continue
        if t == "|" or v is None: prev = None; continue
        s = norm(v)
        if prev is not None: tot += lbig(prev, s[0]); n += 1
        for a, b in zip(s, s[1:]): tot += lbig(a, b); n += 1
        prev = s[-1]
    return tot / n if n else None

def shuf_key(key, rnd):
    vs = [s for s, v in key.items() if v != "NULL"]; vals = [key[s] for s in vs]; rnd.shuffle(vals)
    k = dict(key); k.update(zip(vs, vals)); return k

def shuf_order(stream, rnd):
    pos = [i for i, t in enumerate(stream) if t != "|"]; vals = [stream[i] for i in pos]; rnd.shuffle(vals)
    s = list(stream)
    for i, v in zip(pos, vals): s[i] = v
    return s

def p95(xs): xs = sorted(x for x in xs if x is not None); return xs[int(0.95 * (len(xs) - 1))]

def gate(stream, key, rnd, na, nb):
    real = s2(stream, key)
    a = [s2(stream, shuf_key(key, rnd)) for _ in range(na)]
    b = [s2(shuf_order(stream, rnd), key) for _ in range(nb)]
    pa = (sum(1 for x in a if x is not None and x >= real) + 1) / (len([x for x in a if x is not None]) + 1)
    return real, pa, a, b, (pa <= 0.05 and real > p95(b))

def encipher(passage, key, q, r, breaks, rnd):
    by_val = {}
    for s, v in key.items():
        if v != "NULL": by_val.setdefault(norm(v), []).append(s)
    nulls = [s for s, v in key.items() if v == "NULL"]
    out = []; i = 0
    while i < len(passage) and len(out) < breaks[-1] + 50:
        c = passage[i]
        if i + 1 < len(passage) and passage[i + 1] == c and c + c in by_val and rnd.random() < q:
            out.append(rnd.choice(by_val[c + c])); i += 2
        elif passage[i:i + 2] == "et" and "et" in by_val and rnd.random() < q:
            out.append(rnd.choice(by_val["et"])); i += 2
        elif c in by_val and rnd.random() < q:
            out.append(rnd.choice(by_val[c])); i += 1
        else:
            out.append("_" + c); i += 1
        if nulls and rnd.random() < R_NULL: out.append(rnd.choice(nulls))
    return out

def place_breaks(toks, real_stream):
    s = []; it = iter(toks)
    for t in real_stream: s.append("|" if t == "|" else next(it))
    return s

R_NULL = 27 / (232 - 27)

def run():
    T = load_tokens(); conc = load_conc()
    nreal = sum(1 for t in T if t != "|")
    breaks = [nreal]
    res = {"N": nreal, "variants": {}}
    for vn, key in conc.items():
        rnd = random.Random(15)
        valued = sum(1 for t in T if key.get(t) not in (None, "NULL"))
        nulls = sum(1 for t in T if key.get(t) == "NULL")
        real, pa, a, b, ok = gate(T, key, rnd, 2000, 200)
        # tune q so mean valued count of an enciphered N-token stream matches the target
        prng = random.Random(1515); starts = [prng.randrange(0, len(text) - 2000) for _ in range(100)]
        def mean_valued(q):
            rr = random.Random(7); tot = 0
            for st in starts[:30]:
                e = encipher(text[st:st + 2000], key, q, R_NULL, breaks, rr)[:nreal]
                tot += sum(1 for t in e if key.get(t) not in (None, "NULL"))
            return tot / 30
        lo, hi = 0.0, 1.0
        for _ in range(14):
            mid = (lo + hi) / 2
            if mean_valued(mid) < valued: lo = mid
            else: hi = mid
        q = round((lo + hi) / 2, 4); reach = mean_valued(1.0)
        pr = random.Random(151); hits = 0; pos_valued = []
        for st in starts:
            e = encipher(text[st:st + 2000], key, q, R_NULL, breaks, pr)[:nreal]
            pos_valued.append(sum(1 for t in e if key.get(t) not in (None, "NULL")))
            s = place_breaks(e, T)
            hits += gate(s, key, pr, 500, 100)[4]
        res["variants"][vn] = {"valued_tokens": valued, "null_tokens": nulls, "S2_real": round(real, 4),
            "valshuf_mean": round(sum(x for x in a if x is not None) / len([x for x in a if x is not None]), 4),
            "valshuf_p95": round(p95(a), 4), "p_a": round(pa, 4),
            "ordshuf_mean": round(sum(x for x in b if x is not None) / len([x for x in b if x is not None]), 4),
            "ordshuf_p95": round(p95(b), 4), "gate_pass": bool(ok), "q": q,
            "valued_reach_at_q1": round(reach, 1), "poscontrol_mean_valued": round(sum(pos_valued) / len(pos_valued), 1),
            "power": hits / len(starts)}
    return res

if __name__ == "__main__":
    out = os.path.join(HERE, "results_no15.json")
    r = run(); js = json.dumps(r, indent=1, sort_keys=True)
    if "--check" in sys.argv:
        ok = os.path.exists(out) and open(out).read() == js + "\n"
        print("results_no15.json", "current" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(out, "w").write(js + "\n"); print(js)
