"""READ2-SIENA (3 Oct 2026): known-key transfer of Bourdeau's keys nos. 25/14/4 onto the two pooled open systems
(nos. 6+24, 20+23) -- the one key/piece pairing the folder had not tested (bSIE tested the seven short pieces; bSIE2 ran
ciphertext-only homophonic on the pools). Same by-name sign matching as run_test.py (keys.py).
Statistic: it-corpus 4-gram per-letter score (judge_plaintext NgramModel.score) of the decoded letter stream, in order.
Controls (rule 3, each can differ from the target for this order-sensitive statistic):
  (a) 200 value-shuffled keys (same sign names, values permuted) applied in real order -> rank of the real key;
  (b) 20 order-shuffled cipher streams decoded with the real key (coverage identical by construction, asserted).
Positive control (power at the covered count): a real it-corpus passage of the pool's token length, letters kept at
random positions at the key's coverage rate, scored with its correct values vs the same stream under 200 value-
shuffled letter maps; reports the fraction of 20 passages where the correct map ranks above all 200 (power).
Degenerate optimum: a key mapping every sign to one frequent letter, or one with tiny coverage, can score oddly; the
value-shuffled control keeps the key's own value multiset and coverage fixed, so it cannot win on either.
Run: python3 specs/cheap-tests/siena-concistoro-2308/run_test_pools.py  (deterministic, seeds fixed)
"""
import sys, os, random, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "../../.."))
sys.path.insert(0, os.path.join(ROOT, "tools")); sys.path.insert(0, HERE)
import judge_plaintext as jp
from keys import KEYS

model = jp.NgramModel([jp.read_corpus(p) for p in jp.LANG_CORPORA["it"]])
corpus = "".join(c for c in jp.read_corpus(jp.LANG_CORPORA["it"][0]).lower() if c.isalpha())

def toks(name):
    p = os.path.join(ROOT, "ciphers/siena-concistoro-2308/transcripts", name + ".tok")
    return " ".join(l for l in open(p) if not l.startswith("#")).split()

def norm(key):
    return {k.lower(): v for k, v in key.items() if v and v.isalpha() and len(v) == 1}

def decode(tokens, key):
    return "".join(key[t.lower()] for t in tokens if t.lower() in key)

def shuffled_key(key, rnd):
    ks = list(key); vs = [key[k] for k in ks]; rnd.shuffle(vs); return dict(zip(ks, vs))

out = []
for pool in ("no06_24all", "no20_23all"):
    T = toks(pool)
    for kname, raw in KEYS.items():
        key = norm(raw)
        real = decode(T, key); n = len(real); cov = n / len(T)
        rs = model.score(real)
        rnd = random.Random(1)
        vs = [model.score(decode(T, shuffled_key(key, rnd))) for _ in range(200)]
        rank = sum(v >= rs for v in vs)  # how many shuffled keys score >= real
        os_ = []
        for s in range(20):
            sh = list(T); random.Random(100 + s).shuffle(sh)
            d = decode(sh, key); assert len(d) == n
            os_.append(model.score(d))
        # positive control at this coverage and length
        prnd = random.Random(7); wins = 0
        for i in range(20):
            st = prnd.randrange(0, len(corpus) - len(T)); passage = corpus[st:st + len(T)]
            kept = "".join(c for c in passage if prnd.random() < cov)
            ok = model.score(kept)
            letters = sorted(set(kept))
            beat = 0
            for _ in range(200):
                perm = letters[:]; prnd.shuffle(perm); m = dict(zip(letters, perm))
                beat += model.score("".join(m[c] for c in kept)) >= ok
            wins += beat == 0
        row = dict(pool=pool, key=kname, tokens=len(T), covered=n, coverage=round(cov, 3), real_score=round(rs, 3),
                   valshuf_mean=round(sum(vs) / 200, 3), valshuf_max=round(max(vs), 3), valshuf_ge_real=rank,
                   ordshuf_mean=round(sum(os_) / 20, 3), ordshuf_max=round(max(os_), 3),
                   poscontrol_power=wins / 20, text=real[:80])
        out.append(row); print(json.dumps(row))
json.dump(out, open(os.path.join(HERE, "results_pools.json"), "w"), indent=1)
