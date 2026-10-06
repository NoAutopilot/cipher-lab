#!/usr/bin/env python3
"""R11-ZESCORP: fill-free pattern-rarity crib score on an era/register-matched control (PREREG-R11-ZESCORP.md).

No objective, no fill: a crib placement is admitted only if the cipher window repeats codes exactly where the crib's
tokenised core repeats units (injective both ways) and agrees with Bourdeau's 7 pins; a crib "qualifies" only if its
pattern is rare under the target's own code frequencies (order-shuffled French code streams, NSHUF shuffles: at most
MAXNULL admitted placements in all of them together). Every admitted placement of a qualifying crib enters the seed;
placements that contradict each other on a shared code or unit are all dropped (cross-crib agreement).

Control = wordseg_syllabary.build_control()'s design unchanged (N 2,666, K 98, 7 pins, 1 pct digit error, greedy
longest-match units, de19 German) with the French plaintext and the unit inventory drawn from tools/data/fr1840
(1835-1850 diplomatic French; held-out file lettresetpapiers08ness feeds the control plaintext), three keys.
Arm B (gated): the attacker tokenises cribs with a unit list built by the same rule from a different corpus (fr1810
training + de19), as on the target, where the true syllabary's units are unknown. Arm A (diagnostic): the generator's
own unit list.
Usage: python3 crib_rarity.py control | target | --check   (--check re-runs the control, exits 1 if the json is stale)
"""
import json, random, re, sys
from collections import Counter
from multiprocessing import Pool
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import anneal_syllabary as G  # noqa: E402
import wordseg_syllabary as W  # noqa: E402
import crib_drag as D  # noqa: E402

FR1840 = sorted((G.ROOT / "tools/data/fr1840").glob("*.txt.gz"))
FR1810 = sorted((G.ROOT / "tools/data/fr1810").glob("*.txt.gz"))
HOLD_FR = "lettresetpapiers08ness"
KEYS = (209, 210, 211)
NSHUF, MAXNULL, SHSEED = 40, 1, 11000
NGRAM_TOP, NGRAM_MIN_LETTERS, NGRAM_MAXN = 40, 12, 5
G0, G1, G2 = 3, 0.90, 10
OUT = HERE / "crib_rarity_control.json"
OUT_T = HERE / "crib_rarity_target.json"


def use_corpus(files, hold):
    W.FR = files; W.HOLD = {"fr": hold, "de": "pg31538_"}


def ngram_cribs(train_words_by_file):
    """Top word n-grams (2..5 words, >= 12 letters) of the fr1840 TRAINING files; fixed before any control text is read."""
    c = Counter()
    for ws in train_words_by_file:
        for n in range(2, NGRAM_MAXN + 1):
            for i in range(len(ws) - n + 1):
                g = "".join(ws[i:i + n])
                if len(g) >= NGRAM_MIN_LETTERS:
                    c[g] += 1
    out = []
    for g, _ in c.most_common():
        if not any(g in h or h in g for h in out):
            out.append(g)
        if len(out) >= NGRAM_TOP:
            break
    return out


def crib_list():
    use_corpus(FR1840, HOLD_FR)
    tr = [W.words_of(W.read_corpus(p)) for p in FR1840 if HOLD_FR not in p.name]
    cr = list(D.CRIBS)
    for g in ngram_cribs(tr):
        if g not in cr:
            cr.append(g)
    return cr


def units_by_rule(train_words, K):
    """build_control's unit rule (letters + multi-letter pins + top bigrams/trigrams until K) on a given training set."""
    inv, big, tri = G.inventory({k: "".join(v) for k, v in train_words.items()})
    units = list(G.A) + [u for u in G.PINS.values() if len(u) > 1]
    for u, _ in (big + tri).most_common():
        if len(units) >= K:
            break
        if u in inv and u not in units:
            units.append(u)
    return units


def build(key_seed):
    """wordseg_syllabary.build_control() with fr1840 French and the key drawn from rng(key_seed); returns string units."""
    use_corpus(FR1840, HOLD_FR)
    held, lms, inv, big, tri = W.setup()
    tsegs = G.target_segments()
    K = len({p for _, _, ps, _ in tsegs for p in ps})
    rng = random.Random(key_seed)
    units = list(G.A) + [u for u in G.PINS.values() if len(u) > 1]
    for u, _ in (big + tri).most_common():
        if len(units) >= K:
            break
        if u in inv and u not in units:
            units.append(u)
    codes = rng.sample(range(100), K)
    u2c = dict(zip(units, codes))
    pins = {u2c[u]: u for u in G.PINS.values()}
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
        segs.append((lang, [int(p) for p in G.pairs("".join(digs), 0)]))
        truth.append(toks)
    c2u = {c: u for u, c in u2c.items()}
    return segs, truth, pins, c2u, units, K


def tok(s, by_len):
    out, i = [], 0
    while i < len(s):
        u = next((u for u in by_len if s.startswith(u, i)), s[i]); out.append(u); i += len(u)
    return out


def consistent(win, core, pins, pin_of_unit):
    u2c, c2u = {}, {}
    for c, u in zip(win, core):
        if c in pins and pins[c] != u:
            return None
        if u in pin_of_unit and pin_of_unit[u] != c:
            return None
        if u2c.setdefault(u, c) != c or c2u.setdefault(c, u) != u:
            return None
    return {c: u for c, u in c2u.items() if c not in pins}


def admits(streams, core, pins, pin_of_unit):
    L = len(core); out = []
    for si, cs in streams:
        for p in range(len(cs) - L + 1):
            mp = consistent(cs[p:p + L], core, pins, pin_of_unit)
            if mp is not None:
                out.append((si, p, mp))
    return out


def run(segs, pins, att_units, cribs, truth=None, c2u_true=None):
    by_len = sorted(att_units, key=len, reverse=True)
    pin_of_unit = {u: c for c, u in pins.items()}
    fr = [(si, cs) for si, (l, cs) in enumerate(segs) if l == "fr"]
    rng = random.Random(SHSEED)
    shuf = []
    for _ in range(NSHUF):
        s = []
        for si, cs in fr:
            x = list(cs); rng.shuffle(x); s.append((si, x))
        shuf.append(s)
    rows, acc = [], []
    for crib in cribs:
        core = tok(crib, by_len)[1:-1]
        if len(core) < 2:
            rows.append({"crib": crib, "core": core, "qualifies": False, "why": "core < 2 units"}); continue
        null = sum(len(admits(s, core, pins, pin_of_unit)) for s in shuf)
        q = null <= MAXNULL
        hits = admits(fr, core, pins, pin_of_unit) if q else []
        r = {"crib": crib, "core": core, "repeats": len(core) - len(set(core)),
             "pin_units": sum(u in pin_of_unit for u in core), "null_admits": null, "E_null": round(null / NSHUF, 3),
             "qualifies": q, "admitted": len(hits)}
        if truth is not None:
            r["true_instances"] = sum(truth[si][p:p + len(core)] == core for si, _ in fr
                                      for p in range(len(truth[si]) - len(core) + 1))
            r["letter_occurrences"] = sum("".join(truth[si]).count(crib) for si, _ in fr)
            r["admitted_true"] = sum(all(c2u_true.get(c) == u for c, u in mp.items()) for _, _, mp in hits)
        rows.append(r)
        acc += [(crib, si, p, mp) for si, p, mp in hits]
    # cross-crib agreement: drop every placement that contradicts any other on a shared code or unit
    bad = set()
    for i, (_, _, _, a) in enumerate(acc):
        ia = {u: c for c, u in a.items()}
        for j in range(i + 1, len(acc)):
            b = acc[j][3]
            if any(c in a and a[c] != u for c, u in b.items()) or any(u in ia and ia[u] != c for c, u in b.items()):
                bad.update((i, j))
    seed = {}
    for i, (_, _, _, mp) in enumerate(acc):
        if i not in bad:
            seed.update(mp)
    shared = Counter(c for i, (_, _, _, mp) in enumerate(acc) if i not in bad for c in mp)
    res = {"cribs": len(cribs), "qualifying": sum(r.get("qualifies", False) for r in rows), "admitted": len(acc),
           "dropped_conflict": len(bad), "seed_codes": len(seed),
           "seed_codes_corroborated": sum(1 for c in seed if shared[c] > 1),
           "seed": {str(c): u for c, u in sorted(seed.items())}, "rows": rows}
    if c2u_true is not None:
        ok = sum(c2u_true.get(c) == u for c, u in seed.items())
        res.update(seed_correct=ok, seed_precision=round(ok / len(seed), 3) if seed else None,
                   letter_occurrences_qualifying=sum(r.get("letter_occurrences", 0) for r in rows if r.get("qualifies")),
                   letter_occurrences_all=sum(r.get("letter_occurrences", 0) for r in rows))
    return res


def _ctl(key_seed):
    cribs = crib_list()
    segs, truth, pins, c2u, gen_units, K = build(key_seed)
    use_corpus(FR1810, "lettresindites01napo")
    trB = {"fr": W.corpus_words(FR1810, "fr", False), "de": W.corpus_words(G.DE, "de", False)}
    attB = units_by_rule(trB, K)
    out = {"key_seed": key_seed, "unit_overlap_B": len(set(attB) & set(gen_units))}
    out["A"] = run(segs, pins, gen_units, cribs, truth, c2u)
    out["B"] = run(segs, pins, attB, cribs, truth, c2u)
    return out


def control():
    with Pool(3) as p:
        per = p.map(_ctl, KEYS)
    B = [r["B"] for r in per]
    occ = sum(b["letter_occurrences_qualifying"] for b in B) / len(B)
    prec = [b["seed_precision"] for b in B]
    mprec = round(sum(x or 0 for x in prec) / len(prec), 3)
    mok = round(sum(b["seed_correct"] for b in B) / len(B), 2)
    g = {"G0": occ >= G0, "G1": mprec >= G1, "G2": mok >= G2}
    return {"cribs": crib_list(), "keys": KEYS, "B_mean_qualifying_occurrences": round(occ, 2),
            "B_mean_seed_precision": mprec, "B_mean_seed_correct": mok,
            "A_mean_seed_precision": round(sum(r["A"]["seed_precision"] or 0 for r in per) / len(per), 3),
            "A_mean_seed_correct": round(sum(r["A"]["seed_correct"] for r in per) / len(per), 2),
            "gates": g, "verdict": "CONTROL PASSES GATE" if all(g.values()) else "CONTROL BELOW GATE", "per_key": per}


def summary(res):
    print({k: v for k, v in res.items() if k not in ("per_key", "cribs")})
    for r in res["per_key"]:
        for arm in "AB":
            a = r[arm]
            print(r["key_seed"], arm, "qual", a["qualifying"], "adm", a["admitted"], "drop", a["dropped_conflict"],
                  "seed", a["seed_codes"], "ok", a["seed_correct"], "prec", a["seed_precision"],
                  "occ_q", a["letter_occurrences_qualifying"], "occ_all", a["letter_occurrences_all"])


if __name__ == "__main__":
    a = sys.argv[1:]
    if a == ["--check"]:
        sys.exit(0 if json.dumps(control(), indent=1) + "\n" == OUT.read_text() else 1)
    if a == ["control"]:
        res = control(); OUT.write_text(json.dumps(res, indent=1) + "\n"); summary(res)
    elif a == ["cribs"]:
        print(crib_list())
    elif a == ["target"]:
        if json.loads(OUT.read_text())["verdict"] != "CONTROL PASSES GATE":
            sys.exit("CONTROL BELOW GATE: target not run (PREREG-R11-ZESCORP)")
        sys.exit("target mode: implement only after a passed control (PREREG-R11-ZESCORP.md)")
