#!/usr/bin/env python3
"""R9-ZESCH word-segmentation objective (PREREG-R9-ZESCH.md) on pooled R5005+R5006+R5007, matched control first.

Different instrument from GAPS202's retired letter-4-gram annealer: the decode is scored by its best parse into
dictionary WORDS (Viterbi over a word-unigram model, an unparsed letter costs a fixed penalty), as a log-likelihood
ratio against a letter-unigram background, and the key is kept one-code-per-unit (injective), as the control's design is.

Usage: python3 wordseg_syllabary.py control            synthetic syllabary at the pool's N, K, pins, 1 pct error
       python3 wordseg_syllabary.py target [--shuffled] only after the control cleared the gate
       python3 wordseg_syllabary.py --check             re-runs the control; exits 1 if wordseg_control.json is stale (rule 7)
French word model: tools/data/fr1810 (1800-1811 official correspondence; held-out file lettresindites01napo feeds the
control plaintext). German: tools/data/de19 (held-out pg31538, as GAPS202). R5005 digits: Bourdeau's transcription
(dbourdeau/cyphersolver, MIT / CC BY 4.0). Pins = his 7 gloss values, grade I. Reuses anneal_syllabary.py's pool parse,
inventory and control construction.
"""
import json, math, random, re, sys
from collections import Counter
from multiprocessing import Pool
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import anneal_syllabary as G  # noqa: E402
from judge_plaintext import read_corpus, FOLD  # noqa: E402  (tools/ on path via anneal_syllabary)

SEEDS, RESTARTS, MOVES, T0, T1 = (2091, 2092, 2093), 2, 50000, 2.0, 0.05
CHUNK, MAXW, MINC, OOV = 20, 14, 2, -2.0
GATE = 0.60
FR = sorted((G.ROOT / "tools/data/fr1810").glob("*.txt.gz"))
HOLD = {"fr": "lettresindites01napo", "de": "pg31538_"}


def words_of(text):
    return re.findall(r"[a-z]+", text.lower().translate(FOLD))


def corpus_words(files, lang, held):
    w = []
    for p in files:
        if (HOLD[lang] in p.name) == held:
            w += words_of(read_corpus(p))
    return w


class WordLM:
    def __init__(self, words):
        c = Counter(x for x in words if len(x) <= MAXW)
        n = sum(c.values())
        self.lp = {w: math.log10(k / n) for w, k in c.items() if k >= MINC}
        lc = Counter("".join(words)); ln = sum(lc.values())
        self.bg = {ch: math.log10(lc.get(ch, 0.5) / ln) for ch in G.A}

    def llr(self, x):
        """Best word parse of x minus letter-unigram background (log10)."""
        n = len(x); best = [0.0] + [-1e18] * n; lp = self.lp; bg = self.bg
        for i in range(n):
            b = best[i]
            if b <= -1e17:
                continue
            v = b + bg[x[i]] + OOV
            if v > best[i + 1]:
                best[i + 1] = v
            for j in range(i + 1, min(n, i + MAXW) + 1):
                w = lp.get(x[i:j])
                if w is not None and b + w > best[j]:
                    best[j] = b + w
        return best[n] - sum(bg[ch] for ch in x)


def chunks_of(segs):
    """[(lang, codes array)] -> list of (lang, codes slice) chunks of CHUNK tokens."""
    out = []
    for lang, cs in segs:
        for i in range(0, len(cs), CHUNK):
            out.append((lang, cs[i:i + CHUNK]))
    return out


def anneal(segs, inv, lms, pins, seed):
    rng = random.Random(seed)
    ch = chunks_of(segs)
    codes = sorted({int(c) for _, cs in segs for c in cs})
    free = [c for c in codes if c not in pins]
    where = {c: [k for k, (_, cs) in enumerate(ch) if (cs == c).any()] for c in codes}
    pinned_units = set(pins.values())
    pool_units = [u for u in range(len(inv)) if u not in pinned_units]

    def sc(k, m):
        lang, cs = ch[k]
        return lms[lang].llr("".join(inv[m[c]] for c in cs))

    best_m, best_s = None, -1e18
    for r in range(RESTARTS):
        m = np.zeros(100, dtype=np.int64)
        for c, u in pins.items():
            m[c] = u
        start = rng.sample(pool_units, len(free))
        owner = {}
        for c, u in zip(free, start):
            m[c] = u; owner[u] = c
        ss = [sc(k, m) for k in range(len(ch))]
        cur = sum(ss)
        for it in range(MOVES):
            T = T0 + (T1 - T0) * it / MOVES
            c = rng.choice(free); u = rng.choice(pool_units); old = int(m[c])
            if u == old:
                continue
            d = owner.get(u)  # injective: take u from its owner by swapping
            m[c] = u
            if d is not None:
                m[d] = old
            ks = sorted(set(where[c]) | (set(where[d]) if d is not None else set()))
            new = {k: sc(k, m) for k in ks}
            delta = sum(new[k] - ss[k] for k in ks)
            if delta >= 0 or rng.random() < math.exp(delta / T):
                for k in ks:
                    ss[k] = new[k]
                cur += delta
                owner.pop(old, None); owner[u] = c
                if d is not None:
                    owner[old] = d
            else:
                m[c] = old
                if d is not None:
                    m[d] = u
        if cur > best_s:
            best_m, best_s = m.copy(), cur
    return best_m, best_s


def setup():
    train = {"fr": corpus_words(FR, "fr", False), "de": corpus_words(G.DE, "de", False)}
    held = {"fr": "".join(corpus_words(FR, "fr", True)), "de": "".join(corpus_words(G.DE, "de", True))}
    lms = {k: WordLM(v) for k, v in train.items()}
    inv, big, tri = G.inventory({k: "".join(v) for k, v in train.items()})
    return held, lms, inv, big, tri


def build_control():
    """GAPS202's control construction, verbatim in design (same K, units, pins, 1 pct error), fr1810 held-out text."""
    held, lms, inv, big, tri = setup()
    tsegs = G.target_segments()
    K = len({p for _, _, ps, _ in tsegs for p in ps})
    rng = random.Random(209)
    units = list(G.A) + [u for u in G.PINS.values() if len(u) > 1]
    for u, _ in (big + tri).most_common():
        if len(units) >= K:
            break
        if u in inv and u not in units:
            units.append(u)
    codes = rng.sample(range(100), K)
    u2c = dict(zip(units, codes))
    pins = {u2c[u]: inv.index(u) for u in G.PINS.values()}
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
        segs.append((lang, np.array([int(p) for p in G.pairs("".join(digs), 0)], dtype=np.int64)))
        truth.append(toks)
    tm = np.zeros(100, dtype=np.int64)
    for u, c in u2c.items():
        tm[c] = inv.index(u)
    return held, lms, inv, segs, truth, pins, tm, units, K


def _ctl(sd):
    held, lms, inv, segs, truth, pins, tm, units, K = build_control()
    m, s = anneal(segs, inv, lms, pins, sd)
    ok = tot = 0
    for (lang, obs), toks in zip(segs, truth):
        for c, u in zip(obs, toks):
            if int(c) in pins:
                continue
            tot += 1; ok += inv[m[c]] == u
    return {"seed": sd, "J": round(s, 1), "token_acc": round(ok / tot, 4)}


def control(out):
    held, lms, inv, segs, truth, pins, tm, units, K = build_control()
    true_J = round(sum(lms[l].llr("".join(inv[tm[c]] for c in cs)) for l, cs in chunks_of(segs)), 1)
    with Pool(len(SEEDS)) as p:
        rows = p.map(_ctl, SEEDS)
    for r in rows:
        print(r, flush=True)
    mean = round(sum(r["token_acc"] for r in rows) / len(rows), 4)
    res = {"mode": "control", "objective": "word-parse LLR vs letter unigram, injective key", "K": K,
           "N_tokens": sum(len(t) for t in truth), "units": len(units), "inventory": len(inv), "error_rate": 0.01,
           "chunk": CHUNK, "moves": MOVES, "restarts": RESTARTS, "true_key_J": true_J, "seeds": rows,
           "mean_token_acc": mean, "gate": GATE,
           "verdict": "CONTROL PASSES GATE" if mean >= GATE else "CONTROL BELOW GATE"}
    out.write_text(json.dumps(res, indent=1) + "\n")
    print(res["verdict"], mean, "true_J", true_J)


def target(out, shuffled):
    if json.loads((HERE / "wordseg_control.json").read_text())["verdict"] != "CONTROL PASSES GATE":
        sys.exit("CONTROL BELOW GATE: target not run (PREREG-R9-ZESCH)")
    held, lms, inv, *_ = setup()
    rng = random.Random(2020)
    segs = []
    for name, lang, ps, _ in G.target_segments():
        ps = list(ps)
        if shuffled:
            d = list("".join(ps)); rng.shuffle(d); ps = G.pairs("".join(d), 0)
        segs.append((lang, np.array([int(p) for p in ps], dtype=np.int64)))
    pins = {int(c): inv.index(u) for c, u in G.PINS.items()}
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
    res = {"mode": out.stem, "best_seed": best[2], "J": round(best[1], 1),
           "key": {f"{c:02d}": inv[m[c]] for c in sorted({int(x) for _, cs in segs for x in cs})}}
    out.write_text(json.dumps(res, indent=1) + "\n")


if __name__ == "__main__":
    if "--check" in sys.argv:
        import tempfile
        tmp = Path(tempfile.mkdtemp()) / "wordseg_control.json"
        control(tmp)
        sys.exit(0 if tmp.read_text() == (HERE / "wordseg_control.json").read_text() else 1)
    if "--time" in sys.argv:  # timing only: objective speed on a random key, no accuracy computed
        import time
        held, lms, inv, segs, truth, pins, tm, units, K = build_control()
        ch = chunks_of(segs); rng = np.random.default_rng(0); m = rng.integers(0, len(inv), 100)
        t = time.time(); [lms[l].llr("".join(inv[m[c]] for c in cs)) for l, cs in ch]
        print(len(ch), "chunks, full eval s", round(time.time() - t, 3), "words fr", len(lms["fr"].lp), "de", len(lms["de"].lp))
        sys.exit(0)
    mode = sys.argv[1]
    if mode == "control":
        control(HERE / "wordseg_control.json")
    else:
        target(HERE / ("wordseg_target_shuffled.json" if "--shuffled" in sys.argv else "wordseg_target.json"),
               "--shuffled" in sys.argv)
