"""periodic_vigenere: Vigenere / Beaufort / variant-Beaufort with a short repeating key (no shared tool existed,
so this family carries its own short solver; 25 Sept 2026).

Design: 26-letter alphabet (judge_plaintext.fold), tabula vig (c = p + k), beau (c = k - p) or varbeau (c = p - k).
Period: params period=P, else the spec's constraints.period, else a coset-IC scan over 2..period_max (default 30)
taking the smallest period whose mean coset IC is within 90% of the best. Solver: per coset the shift that
maximises unigram log-likelihood, then coordinate ascent over the key under an add-k trigram model, `restarts`
random-start repeats, best trigram score wins. Control: a corpus window of the target's length (held out of the
model) under a random key of the same period and tabula.
params: tabula (vig), period (scan), period_max (30), order (3), continuous (1: the key runs on across lines,
the default for one text given as lines; 0: the key phase restarts at every message, the default for a spec
whose ciphertext is a list of {groups} messages such as koehler-1944). The control key's period is the given one, else
the period the scan finds on the target (the runner passes the target tokens as params["target_msgs"])."""
import math, random, re
from collections import Counter
import judge_plaintext as jp
from families import draw_window

DESCRIPTION = "periodic Vigenere/Beaufort/variant-Beaufort, random key of the given or scanned period (own solver)"
A = "abcdefghijklmnopqrstuvwxyz"
IDX = {c: i for i, c in enumerate(A)}


def encipher(tab, p, k):
    return {"vig": (p + k) % 26, "beau": (k - p) % 26, "varbeau": (p - k) % 26}[tab]


def decipher(tab, c, k):
    return {"vig": (c - k) % 26, "beau": (k - c) % 26, "varbeau": (c + k) % 26}[tab]


class Model:
    def __init__(self, texts, order=3, k=0.5):
        s = "".join(jp.fold(t) for t in texts)
        self.o = order
        self.n = Counter(s[i:i + order] for i in range(len(s) - order + 1))
        self.c = Counter(s[i:i + order - 1] for i in range(len(s) - order + 2))
        uni = Counter(s)
        tot = sum(uni.values())
        self.lu = {a: math.log((uni[a] + 0.5) / (tot + 13)) for a in A}
        self.k, self.cache = k, {}

    def logp(self, g):
        v = self.cache.get(g)
        if v is None:
            v = math.log((self.n[g] + self.k) / (self.c[g[:-1]] + self.k * 26))
            self.cache[g] = v
        return v

    def score(self, s):
        return sum(self.logp(s[i:i + self.o]) for i in range(len(s) - self.o + 1))


def coset_ic(msgs, P):
    tot, cnt = 0.0, 0
    for j in range(P):
        col = [c for m in msgs for c in m[j::P]]
        n = len(col)
        if n < 2:
            continue
        f = Counter(col)
        tot += sum(v * (v - 1) for v in f.values()) / (n * (n - 1))
        cnt += 1
    return tot / max(1, cnt)


def find_period(msgs, pmax):
    ics = {P: coset_ic(msgs, P) for P in range(2, pmax + 1)}
    best = max(ics.values())
    for P in range(2, pmax + 1):
        if ics[P] >= 0.9 * best:
            return P, ics
    return 2, ics


def _decode(msgs, key, tab):
    P = len(key)
    return ["".join(A[decipher(tab, IDX[c], key[i % P])] for i, c in enumerate(m)) for m in msgs]


def _solve_period(msgs, P, tab, model, rng, restarts):
    best = (-1e18, None)
    for r in range(restarts):
        if r == 0:  # unigram start per coset
            key = []
            for j in range(P):
                col = [c for m in msgs for c in m[j::P]]
                key.append(max(range(26), key=lambda k: sum(model.lu[A[decipher(tab, IDX[c], k)]] for c in col)))
        else:
            key = [rng.randrange(26) for _ in range(P)]
        cur = sum(model.score(d) for d in _decode(msgs, key, tab))
        improved = True
        while improved:
            improved = False
            for j in rng.sample(range(P), P):
                old = key[j]
                for k in range(26):
                    if k == old:
                        continue
                    key[j] = k
                    sc = sum(model.score(d) for d in _decode(msgs, key, tab))
                    if sc > cur:
                        cur, old, improved = sc, k, True
                key[j] = old
        if cur > best[0]:
            best = (cur, list(key))
    return best


def make_control(spec, seed, corpora, params):
    tab = params.get("tabula", "vig")
    P = int(params.get("period", 0)) or int((spec.get("constraints") or {}).get("period", 0) or 0)
    text = jp.fold("\n".join(corpora))
    lengths = params.get("lengths") or [params["N"]]
    rng = random.Random(seed + 1000)
    if not P and params.get("target_msgs"):
        # the brief's design: a random key of the period FOUND on the target (a coset-IC statistic, not a solve)
        P, _ = find_period(["".join(m) for m in params["target_msgs"]], int(params.get("period_max", 30)))
    if not P:
        P = rng.randrange(3, int(params.get("period_max", 30)) + 1)
    key = [rng.randrange(26) for _ in range(P)]
    plain, rest = draw_window(text, sum(lengths), seed)
    cont = _continuous(params)
    msgs, pos = [], 0
    for n in lengths:
        p = plain[pos:pos + n]
        off = pos if cont else 0
        pos += n
        msgs.append([A[encipher(tab, IDX[a], key[(off + i) % P])] for i, a in enumerate(p)])
    params["control_key"] = "".join(A[k] for k in key)
    return msgs, plain, [rest]


def _continuous(params):
    """Key runs on across message boundaries (one text written over several lines) unless the spec gives
    separate messages ({groups} entries, key phase restarting at each) or --param continuous=0/1 says so."""
    if "continuous" in params:
        return bool(int(params["continuous"]))
    return not params.get("messages_independent", False)


def solve(cipher_msgs, spec, seed, restarts, corpora, params):
    tab = params.get("tabula", "vig")
    msgs = ["".join(m) for m in cipher_msgs]
    if _continuous(params):
        msgs = ["".join(msgs)]
    for m in msgs:
        if re.search(r"[^a-z]", m):
            raise SystemExit("periodic_vigenere needs a-z ciphertext signs")
    model = Model(corpora, int(params.get("order", 3)))
    rng = random.Random(seed)
    P = int(params.get("period", 0)) or int((spec.get("constraints") or {}).get("period", 0) or 0)
    ics = None
    if not P:
        P, ics = find_period(msgs, int(params.get("period_max", 30)))
    sc, key = _solve_period(msgs, P, tab, model, rng, max(1, restarts))
    dec = _decode(msgs, key, tab)
    n = sum(len(m) for m in msgs)
    info = {"period": P, "tabula": tab, "continuous_key": _continuous(params), "key": "".join(A[k] for k in key), "score_per_letter": round(sc / max(1, n), 4)}
    if ics:
        info["coset_ic_top"] = sorted(((round(v, 4), p) for p, v in ics.items()), reverse=True)[:5]
    return "".join(dec), sc / max(1, n), info


def score_recovery(plain, truth):
    n = max(1, len(truth))
    return sum(1 for a, b in zip(plain, truth) if a == b) / n
