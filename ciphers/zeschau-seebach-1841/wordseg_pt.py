#!/usr/bin/env python3
"""R9-ZESCH2: the R9-ZESCH word-parse objective, unchanged, under a stronger search (PREREG-R9-ZESCH2.md).

Objective: wordseg_syllabary.WordLM.llr over 20-token chunks, injective key, 7 pins fixed -- imported, not copied.
Search, and how it differs from R9-ZESCH's annealer (2 restarts x 50,000 moves, random start, one chain cooling 2.0->0.05):
  1. crib-free frequency-rank initialisation: the non-pin codes, ranked by their count in the ciphertext, are matched to
     the candidate units ranked by their expected frequency (training text tokenised by greedy longest match over a
     unit list built by the same design rule the control generator uses: 26 letters + Bourdeau's multi-letter pin units
     + commonest training bigrams/trigrams up to K). No plaintext of the cipher is used.
  2. parallel tempering: REPLICAS chains at fixed temperatures TEMPS, each started from the frequency-rank key with
     its own few random swaps, adjacent replicas exchanging keys every EXCH moves (Metropolis on the J difference).
  3. a code-code swap move (the frequency-preserving move) half the time, beside R9-ZESCH's code->unit move.
Usage: python3 wordseg_pt.py control | target [--shuffled] | --check
"""
import json, math, random, sys
from collections import Counter
from multiprocessing import Pool
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import anneal_syllabary as G  # noqa: E402
import wordseg_syllabary as W  # noqa: E402

SEEDS = (2191, 2192, 2193)
TEMPS = (0.05, 0.15, 0.4, 1.0, 2.0)
REPLICAS = len(TEMPS)
MOVES = 50000          # per replica (5 replicas -> 250,000 moves per seed; R9-ZESCH: 100,000)
EXCH = 400
PERTURB = 10
GATE = 0.60


def unit_list(inv, K):
    held, lms, inv2, big, tri = SETUP
    units = list(G.A) + [u for u in G.PINS.values() if len(u) > 1]
    for u, _ in (big + tri).most_common():
        if len(units) >= K:
            break
        if u in inv and u not in units:
            units.append(u)
    return units


def unit_freq(units, train, share):
    by_len = sorted(units, key=len, reverse=True)
    f = Counter()
    for lang, txt in train.items():
        c = Counter(); i = 0; n = len(txt)
        while i < n:
            u = next((u for u in by_len if txt.startswith(u, i)), txt[i])
            c[u] += 1; i += len(u)
        tot = sum(c.values())
        for u in units:
            f[u] += share[lang] * c[u] / tot
    return f


def freq_init(segs, inv, pins, train):
    codes = sorted({int(c) for _, cs in segs for c in cs})
    K = len(codes)
    units = unit_list(inv, K)
    ntok = Counter(l for l, cs in segs for _ in cs); tot = sum(ntok.values())
    f = unit_freq(units, train, {l: ntok[l] / tot for l in ("fr", "de")})
    pinned = set(pins.values())
    urank = [inv.index(u) for u in sorted(units, key=lambda u: -f[u]) if inv.index(u) not in pinned]
    cc = Counter(int(c) for _, cs in segs for c in cs)
    crank = [c for c in sorted(codes, key=lambda c: -cc[c]) if c not in pins]
    m = np.zeros(100, dtype=np.int64)
    for c, u in pins.items():
        m[c] = u
    for c, u in zip(crank, urank):
        m[c] = u
    return m


class Chain:
    def __init__(self, m, ch, lms, inv, where):
        self.m = m.copy(); self.ch = ch; self.lms = lms; self.inv = inv; self.where = where
        self.ss = [self.sc(k) for k in range(len(ch))]; self.cur = sum(self.ss)

    def sc(self, k):
        lang, cs = self.ch[k]
        return self.lms[lang].llr("".join(self.inv[self.m[c]] for c in cs))

    def owner(self):
        return {int(self.m[c]): c for c in self.where}


def search(segs, inv, lms, pins, seed, train):
    rng = random.Random(seed)
    ch = W.chunks_of(segs)
    codes = sorted({int(c) for _, cs in segs for c in cs})
    free = [c for c in codes if c not in pins]
    where = {c: [k for k, (_, cs) in enumerate(ch) if (cs == c).any()] for c in codes}
    pool_units = [u for u in range(len(inv)) if u not in set(pins.values())]
    m0 = freq_init(segs, inv, pins, train)
    chains = []
    for r in range(REPLICAS):
        m = m0.copy()
        for _ in range(PERTURB):
            a, b = rng.sample(free, 2); m[a], m[b] = m[b], m[a]
        chains.append(Chain(m, ch, lms, inv, where))
    owners = [c.owner() for c in chains]
    best_m, best_s = chains[0].m.copy(), max(c.cur for c in chains)
    init_J = chains[0].cur
    for it in range(MOVES):
        for r, (c, T) in enumerate(zip(chains, TEMPS)):
            own = owners[r]
            a = rng.choice(free)
            old = int(c.m[a])
            if rng.random() < 0.5:
                d = rng.choice(free)
                if d == a:
                    continue
                u = int(c.m[d])
            else:
                u = rng.choice(pool_units)
                if u == old:
                    continue
                d = own.get(u)
            c.m[a] = u
            if d is not None:
                c.m[d] = old
            ks = sorted(set(where[a]) | (set(where[d]) if d is not None else set()))
            new = {k: c.sc(k) for k in ks}
            delta = sum(new[k] - c.ss[k] for k in ks)
            if delta >= 0 or rng.random() < math.exp(delta / T):
                for k in ks:
                    c.ss[k] = new[k]
                c.cur += delta
                own.pop(old, None); own[u] = a
                if d is not None:
                    own[old] = d
                if c.cur > best_s:
                    best_s, best_m = c.cur, c.m.copy()
            else:
                c.m[a] = old
                if d is not None:
                    c.m[d] = u
        if it % EXCH == EXCH - 1:
            for r in range(REPLICAS - 1):
                a, b = chains[r], chains[r + 1]
                x = (a.cur - b.cur) * (1 / TEMPS[r + 1] - 1 / TEMPS[r])
                if x >= 0 or rng.random() < math.exp(x):
                    chains[r], chains[r + 1] = b, a
                    owners[r], owners[r + 1] = owners[r + 1], owners[r]
    return best_m, best_s, init_J


SETUP = None


def init_setup():
    global SETUP, TRAIN
    SETUP = W.setup()
    TRAIN = {"fr": "".join(W.corpus_words(W.FR, "fr", False)), "de": "".join(W.corpus_words(G.DE, "de", False))}


def acc(m, segs, truth, pins, inv):
    ok = tot = 0
    for (lang, obs), toks in zip(segs, truth):
        for c, u in zip(obs, toks):
            if int(c) in pins:
                continue
            tot += 1; ok += inv[m[c]] == u
    return round(ok / tot, 4)


def _ctl(sd):
    init_setup()
    held, lms, inv, segs, truth, pins, tm, units, K = W.build_control()
    m, s, j0 = search(segs, inv, lms, pins, sd, TRAIN)
    m0 = freq_init(segs, inv, pins, TRAIN)
    return {"seed": sd, "J": round(s, 1), "init_J": round(j0, 1), "init_token_acc": acc(m0, segs, truth, pins, inv),
            "token_acc": acc(m, segs, truth, pins, inv)}


def control(out):
    init_setup()
    held, lms, inv, segs, truth, pins, tm, units, K = W.build_control()
    true_J = round(sum(lms[l].llr("".join(inv[tm[c]] for c in cs)) for l, cs in W.chunks_of(segs)), 1)
    with Pool(len(SEEDS)) as p:
        rows = p.map(_ctl, SEEDS)
    for r in rows:
        print(r, flush=True)
    mean = round(sum(r["token_acc"] for r in rows) / len(rows), 4)
    res = {"mode": "control", "objective": "R9-ZESCH word-parse LLR (wordseg_syllabary.py, unchanged)",
           "search": "freq-rank init + parallel tempering", "temps": TEMPS, "moves_per_replica": MOVES, "exch": EXCH,
           "K": K, "N_tokens": sum(len(t) for t in truth), "true_key_J": true_J, "seeds": rows,
           "mean_token_acc": mean, "gate": GATE,
           "verdict": "CONTROL PASSES GATE" if mean >= GATE else "CONTROL BELOW GATE"}
    out.write_text(json.dumps(res, indent=1) + "\n")
    print(res["verdict"], mean, "true_J", true_J)


def _tgt(args):
    sd, shuffled = args
    init_setup()
    held, lms, inv, *_ = SETUP
    rng = random.Random(2020)
    segs = []
    for name, lang, ps, _ in G.target_segments():
        ps = list(ps)
        if shuffled:
            d = list("".join(ps)); rng.shuffle(d); ps = G.pairs("".join(d), 0)
        segs.append((lang, np.array([int(p) for p in ps], dtype=np.int64)))
    pins = {int(c): inv.index(u) for c, u in G.PINS.items()}
    m, s, j0 = search(segs, inv, lms, pins, sd, TRAIN)
    return sd, s, m, segs, inv


def target(out, shuffled):
    if json.loads((HERE / "wordseg_pt_control.json").read_text())["verdict"] != "CONTROL PASSES GATE":
        sys.exit("CONTROL BELOW GATE: target not run (PREREG-R9-ZESCH2)")
    with Pool(len(SEEDS)) as p:
        rows = p.map(_tgt, [(sd, shuffled) for sd in SEEDS])
    sd, s, m, segs, inv = max(rows, key=lambda r: r[1])
    dec = {"fr": "", "de": ""}
    for lang, cs in segs:
        dec[lang] += "".join(inv[m[c]] for c in cs)
    for lang, t in dec.items():
        (HERE / f"{out.stem}_decode_{lang}.txt").write_text(t + "\n")
    res = {"mode": out.stem, "seed_J": {r[0]: round(r[1], 1) for r in rows}, "best_seed": sd, "J": round(s, 1),
           "key": {f"{c:02d}": inv[m[c]] for c in sorted({int(x) for _, cs in segs for x in cs})}}
    out.write_text(json.dumps(res, indent=1) + "\n")
    print(res["seed_J"])


if __name__ == "__main__":
    if "--time" in sys.argv:
        import time
        MOVES = int(sys.argv[sys.argv.index("--time") + 1])
        t = time.time(); r = _ctl(2191)  # timing only: accuracy is not printed before the prereg is pushed
        print("moves/replica", MOVES, "s", round(time.time() - t, 1))
        sys.exit(0)
    if "--check" in sys.argv:
        import tempfile
        tmp = Path(tempfile.mkdtemp()) / "wordseg_pt_control.json"
        control(tmp)
        sys.exit(0 if tmp.read_text() == (HERE / "wordseg_pt_control.json").read_text() else 1)
    if sys.argv[1] == "control":
        control(HERE / "wordseg_pt_control.json")
    else:
        sh = "--shuffled" in sys.argv
        target(HERE / ("wordseg_pt_target_shuffled.json" if sh else "wordseg_pt_target.json"), sh)
