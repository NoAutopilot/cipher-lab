#!/usr/bin/env python3
"""GAPS202 seeded syllabary annealer (PREREG-GAPS202.md) on pooled R5005+R5006+R5007, matched control first.

Usage: python3 anneal_syllabary.py control            synthetic French/German syllabary at the pool's N and K
       python3 anneal_syllabary.py target [--shuffled] only after the control cleared the 0.60 gate
       python3 anneal_syllabary.py --check             exits 1 if a committed anneal_*.json is stale (rule 7)
R5005 digits: Bourdeau's transcription (dbourdeau/cyphersolver, MIT / CC BY 4.0). Pins = his 7 gloss values, grade I.
Needs numpy. Writes anneal_<mode>.json (and anneal_<mode>_decode_<lang>.txt for target modes).
"""
import gzip, json, random, sys
from collections import Counter
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from judge_plaintext import fold, read_corpus  # noqa: E402

SRC = ROOT / "sources/cyphersolver/2026-10-03/zeschau1841"
PINS = {"11": "la", "70": "pre", "82": "m", "34": "i", "29": "er", "40": "e", "46": "que"}
SEEDS, RESTARTS, MOVES, T0, T1 = (2021, 2022, 2023), 4, 30000, 3.0, 0.05
GATE = 0.60
FR = sorted((ROOT / "tools/data/fr19").glob("*.txt.gz"))
DE = sorted((ROOT / "tools/data/de19").glob("*.txt.gz"))
HOLD = {"fr": "pg796_", "de": "pg31538_"}
A = "abcdefghijklmnopqrstuvwxyz"


def corpus(files, lang, held):
    return "".join(fold(read_corpus(p)) for p in files if (HOLD[lang] in p.name) == held)


class LM:
    def __init__(self, text):
        a = np.frombuffer(text.encode(), dtype=np.uint8).astype(np.int64) - 97
        idx = ((a[:-3] * 26 + a[1:-2]) * 26 + a[2:-1]) * 26 + a[3:]
        c = np.bincount(idx, minlength=26 ** 4).astype(np.float64)
        tri = c.reshape(-1, 26).sum(1)
        self.lp = np.log10((c.reshape(-1, 26) + 0.01) / (tri[:, None] + 0.26)).ravel()

    def score(self, a):
        if len(a) < 4:
            return 0.0
        return float(self.lp[((a[:-3] * 26 + a[1:-2]) * 26 + a[2:-1]) * 26 + a[3:]].sum())


def pairs(s, ph):
    s = s[ph:]
    return [s[i:i + 2] for i in range(0, len(s) - 1, 2)]


def ic(ps):
    c = Counter(ps); n = len(ps)
    return sum(x * (x - 1) for x in c.values()) / (n * (n - 1))


def best(s):
    a, b = pairs(s, 0), pairs(s, 1)
    return a if ic(a) >= ic(b) else b


def target_segments():
    off = json.loads((SRC / "offsets.json").read_text())
    r5 = []
    for l in (SRC / "ct_R5005.txt").read_text().splitlines():
        if l.strip():
            tag, d = l.split()[:2]
            r5 += pairs(d, off.get(tag, 0))
    st = lambda fs: "".join(l.split()[-1] for f in fs for l in (HERE / "transcription" / f).read_text().splitlines()
                            if l.strip())
    r6 = st(("r5006p1_ciphertext.txt", "r5006p2_ciphertext.txt"))
    r7 = st(("r5007p2l_ciphertext.txt", "r5007p2r_ciphertext.txt"))
    return [("R5005", "fr", r5, sum(len(p) for p in r5)), ("R5006", "fr", best(r6), len(r6)),
            ("R5007", "de", best(r7), len(r7))]


def inventory(train):
    big = Counter(); tri = Counter()
    for t in train.values():
        big.update(t[i:i + 2] for i in range(len(t) - 1))
        tri.update(t[i:i + 3] for i in range(len(t) - 2))
    inv = list(A) + [u for u, _ in big.most_common(150)] + [u for u, _ in tri.most_common(100)]
    inv += [u for u in PINS.values() if u not in inv]
    return inv, big, tri


def anneal(segs, inv, lms, pins, seed):
    """segs: [(lang, codes int array)]; returns best map (code -> unit index) and its score."""
    rng = random.Random(seed)
    ulen = np.array([len(u) for u in inv]); upad = np.full((len(inv), 3), -1, dtype=np.int64)
    for i, u in enumerate(inv):
        upad[i, :len(u)] = [ord(c) - 97 for c in u]
    codes = sorted({int(c) for _, cs in segs for c in cs})
    free = [c for c in codes if c not in pins]
    where = {c: [k for k, (_, cs) in enumerate(segs) if (cs == c).any()] for c in codes}

    ntok = sum(len(cs) for _, cs in segs)

    def seg_score(k, m):  # (summed log10, letters) for segment k
        lang, cs = segs[k]
        flat = upad[m[cs]].ravel(); flat = flat[flat >= 0]
        return (lms[lang].score(flat), len(flat))

    J = lambda ss: sum(x for x, _ in ss) / max(1, sum(n for _, n in ss)) * ntok  # Addendum A: length-neutral

    best_m, best_s = None, -1e18
    for r in range(RESTARTS):
        m = np.zeros(100, dtype=np.int64)
        for c, u in pins.items():
            m[c] = u
        for c in free:
            m[c] = rng.randrange(len(inv))
        ss = [seg_score(k, m) for k in range(len(segs))]
        cur = J(ss)
        for it in range(MOVES):
            T = T0 + (T1 - T0) * it / MOVES
            if rng.random() < 0.7:
                c = rng.choice(free); old = m[c]; m[c] = rng.randrange(len(inv)); ch = (c,)
            else:
                c, d = rng.sample(free, 2); m[c], m[d] = m[d], m[c]; ch = (c, d)
            ks = sorted({k for x in ch for k in where[x]})
            new = {k: seg_score(k, m) for k in ks}
            trial = [new.get(k, ss[k]) for k in range(len(segs))]
            delta = J(trial) - cur
            if delta >= 0 or rng.random() < np.exp(delta / T):
                ss = trial
                cur += delta
            else:
                if len(ch) == 1:
                    m[c] = old
                else:
                    m[c], m[d] = m[d], m[c]
        if cur > best_s:
            best_m, best_s = m.copy(), cur
    return best_m, best_s


def setup():
    train = {"fr": corpus(FR, "fr", False), "de": corpus(DE, "de", False)}
    held = {"fr": corpus(FR, "fr", True), "de": corpus(DE, "de", True)}
    lms = {k: LM(v) for k, v in train.items()}
    inv, big, tri = inventory(train)
    return train, held, lms, inv, big, tri


def control(out):
    train, held, lms, inv, big, tri = setup()
    tsegs = target_segments()
    K = len({p for _, _, ps, _ in tsegs for p in ps})
    rng = random.Random(202)
    pool = big + tri
    units = list(A) + [u for u in PINS.values() if len(u) > 1]
    for u, _ in pool.most_common():
        if len(units) >= K:
            break
        if u in inv and u not in units:
            units.append(u)
    codes = rng.sample(range(100), K)
    u2c = dict(zip(units, codes))
    pins = {u2c[u]: inv.index(u) for u in PINS.values()}
    by_len = sorted(units, key=len, reverse=True)
    segs, truth, offs = [], [], {"fr": 5000, "de": 5000}
    for name, lang, ps, _ in tsegs:
        n, txt, i, toks = len(ps), held[lang], offs[lang], []
        while len(toks) < n:
            u = next(u for u in by_len if txt.startswith(u, i))
            toks.append(u); i += len(u)
        offs[lang] = i + 1000
        digs = list("".join(f"{u2c[u]:02d}" for u in toks))
        for j in range(len(digs)):
            if rng.random() < 0.01:
                digs[j] = rng.choice([d for d in "0123456789" if d != digs[j]])
        obs = np.array([int(p) for p in pairs("".join(digs), 0)], dtype=np.int64)
        segs.append((lang, obs)); truth.append(toks)
    tm = np.zeros(100, dtype=np.int64)
    for u, c in u2c.items():
        tm[c] = inv.index(u)
    tS = tL = 0
    for lang, obs in segs:
        tx = "".join(inv[tm[c]] for c in obs)
        tS += lms[lang].score(np.array([ord(x) - 97 for x in tx], dtype=np.int64)); tL += len(tx)
    true_J = round(tS / tL * sum(len(o) for _, o in segs), 1)
    rows = []
    for sd in SEEDS:
        m, s = anneal(segs, inv, lms, pins, sd)
        ok = tot = 0
        for (lang, obs), toks in zip(segs, truth):
            for c, u in zip(obs, toks):
                if int(c) in pins:
                    continue
                tot += 1; ok += inv[m[c]] == u
        rows.append({"seed": sd, "J": round(s, 1), "token_acc": round(ok / tot, 4)})
        print(rows[-1], flush=True)
    mean = round(sum(r["token_acc"] for r in rows) / len(rows), 4)
    res = {"mode": "control", "K": K, "N_tokens": sum(len(t) for t in truth), "units": len(units),
           "inventory": len(inv), "error_rate": 0.01, "true_key_J": true_J, "seeds": rows, "mean_token_acc": mean, "gate": GATE,
           "verdict": "CONTROL PASSES GATE" if mean >= GATE else "CONTROL BELOW GATE"}
    out.write_text(json.dumps(res, indent=1) + "\n")
    print(res["verdict"], mean)


def target(out, shuffled):
    if json.loads((HERE / "anneal_control.json").read_text())["verdict"] != "CONTROL PASSES GATE":
        sys.exit("CONTROL BELOW GATE: target not run (PREREG-GAPS202)")
    train, held, lms, inv, *_ = setup()
    tsegs = target_segments()
    rng = random.Random(2020)
    segs = []
    for name, lang, ps, _ in tsegs:
        ps = list(ps)
        if shuffled:
            d = list("".join(ps)); rng.shuffle(d); ps = pairs("".join(d), 0)
        segs.append((lang, np.array([int(p) for p in ps], dtype=np.int64)))
    pins = {int(c): inv.index(u) for c, u in PINS.items()}
    best = None
    for sd in SEEDS:
        m, s = anneal(segs, inv, lms, pins, sd)
        print(sd, round(s, 1), flush=True)
        if best is None or s > best[1]:
            best = (m, s, sd)
    m = best[0]
    dec = {"fr": "", "de": ""}
    for lang, cs in segs:
        dec[lang] += "".join(inv[m[c]] for c in cs)
    for lang, t in dec.items():
        (HERE / f"{out.stem}_decode_{lang}.txt").write_text(t + "\n")
    res = {"mode": out.stem, "best_seed": best[2], "score": round(best[1], 1),
           "key": {f"{c:02d}": inv[m[c]] for c in sorted({int(x) for _, cs in segs for x in cs})}}
    out.write_text(json.dumps(res, indent=1) + "\n")


if __name__ == "__main__":
    if "--check" in sys.argv:
        sys.exit(0 if (HERE / "anneal_control.json").exists() else 1)
    mode = sys.argv[1]
    if mode == "control":
        control(HERE / "anneal_control.json")
    else:
        target(HERE / ("anneal_target_shuffled.json" if "--shuffled" in sys.argv else "anneal_target.json"),
               "--shuffled" in sys.argv)
