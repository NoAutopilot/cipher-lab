#!/usr/bin/env python3
"""R11-SIENA4750: no. 7 (agent J, 363 tokens) against key R4750's nomenclator (agent G transcription, Bourdeau, CC BY 4.0).

Pre-registration: ciphers/siena-concistoro-2308/PREREG-R11-SIENA4750.md (pushed in e34b0fc45 before this script ran).
T1 numeral codes as adjacent digit pairs (order-shuffle and code-set-shuffle controls, planted-code power);
T2 written code words among J's clear words (it16dip random word-list control);
T3 low-count signs with their per-token bigram cost under R9-SIENA7's seed-1 fit (descriptive).
`--check` re-runs and exits 1 if results_r4750.json differs.
"""
import argparse, gzip, json, math, random, re, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
TOK = ROOT / "ciphers/siena-concistoro-2308/transcripts/no07.tok"
R9 = HERE / "results_no07.json"
DATA = ROOT / "tools/data/it16dip"
OUT = HERE / "results_r4750.json"

CODES = ["97", "19", "88", "23", "72", "15"]
# R4750 written code words (agent G, keys/R4750.txt), uncertain alternatives included per the PREREG.
CODE_WORDS = ["gallus", "cocna", "corno", "pesce", "fecon", "falcone", "volpe", "fede", "spredo", "ficaus", "ficus",
              "venenum", "penne", "villa", "aqua", "forte", "fuoco", "storps", "storpsi", "virtus", "tedio", "fallo",
              "sangue", "cani", "catena", "ventura", "ducum", "calamitas", "senecitas", "senectus", "dubio", "leo",
              "agata", "luna", "equus", "potens", "remedio", "fucoe", "furore", "glans", "morcellino", "moncellino"]
N_WRITTEN = 36  # written code words on the sheet (alternatives are readings of these)
# Agent J's clear words in L02-L12 (transcripts/no07.txt @ adbf9a1), extracted per the PREREG rule (>= 4 letters).
CLEAR = ['ordinare', 'prima', 'omzo', 'lungo', 'forse', 'bisino', 'mezo', 'certando', 'parendo', 'torbe', 'andare',
         'lesercito', 'altro', 'segno', 'ofese', 'ordinassimo', 'altro', 'come', 'ordine', 'rimo', 'parte', 'omnibu',
         'longo', 'ordinando', 'diverse', 'mostra', 'continuo', 'gentilmente', 'questo', 'modo', 'volendo', 'mandare',
         'grande', 'sapendo', 'bravi', 'come', 'potra', 'similmente', 'omgi', 'permanersi', 'altro', 'domandando',
         'denari', 'fuorusciti', 'apoli', 'potremo', 'fare', 'tale', 'altrui', 'ordine', 'sopra', 'tutti', 'dispensare']
DIG = set("123456789")


def runs():
    return [l.split() for l in TOK.read_text().splitlines() if l.strip() and not l.startswith("#")]


def m_count(rs, codes):
    cs = set(codes)
    return sum(1 for r in rs for a, b in zip(r, r[1:]) if a in DIG and b in DIG and a + b in cs)


def shuffle_runs(rs, rng):
    out = []
    for r in rs:
        r = r[:]
        rng.shuffle(r)
        out.append(r)
    return out


def rand_codeset(rng):
    d = rng.choice("123456789")
    s = {d + d}
    while len(s) < 6:
        a, b = rng.sample("123456789", 2)
        s.add(a + b)
    return sorted(s)


def t1_gate(rs, rng, na, nb):
    real = m_count(rs, CODES)
    ca = sum(1 for _ in range(na) if m_count(shuffle_runs(rs, rng), CODES) >= real)
    cb = sum(1 for _ in range(nb) if m_count(rs, rand_codeset(rng)) >= real)
    pa, pb = (ca + 1) / (na + 1), (cb + 1) / (nb + 1)
    return real, pa, pb, (pa <= 0.05 and pb <= 0.05)


def plant(rs, rng, k=4):
    rs = shuffle_runs(rs, rng)
    slots = [(i, j) for i, r in enumerate(rs) for j in range(len(r) - 1)]
    used = set()
    n = 0
    while n < k:
        i, j = rng.choice(slots)
        if (i, j) in used or (i, j - 1) in used or (i, j + 1) in used:
            continue
        used.add((i, j))
        c = rng.choice(CODES)
        rs[i][j], rs[i][j + 1] = c[0], c[1]
        n += 1
    return rs


def lev(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def w_count(words, codes):
    return sum(1 for w in words if any(lev(w, c) <= 1 for c in codes))


def corpus_text():
    files = sorted(p for p in DATA.glob("*.txt.gz"))
    return "\n".join(gzip.open(p, "rt", encoding="utf-8").read().lower() for p in files)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    rng = random.Random(4750)
    rs = runs()
    toks = [t for r in rs for t in r]
    assert len(toks) == 363, len(toks)
    res = {"n_tokens": len(toks), "codes": CODES}

    # T1
    real, pa, pb, ok = t1_gate(rs, rng, 2000, 2000)
    hits = [(i, j, r[j] + r[j + 1]) for i, r in enumerate(rs) for j in range(len(r) - 1)
            if r[j] in DIG and r[j + 1] in DIG and r[j] + r[j + 1] in CODES]
    # all digit pairs, for the record
    dp = Counter(r[j] + r[j + 1] for r in rs for j in range(len(r) - 1) if r[j] in DIG and r[j + 1] in DIG)
    pw = [t1_gate(plant(rs, rng), rng, 500, 500)[3] for _ in range(200)]
    res["T1"] = {"M_real": real, "hits_run_pos_code": hits, "p_order": round(pa, 4), "p_codeset": round(pb, 4),
                 "pass": ok, "power_k4": sum(pw) / len(pw), "digit_pairs": dict(sorted(dp.items()))}

    # T2
    txt = corpus_text()
    types = sorted({w for w in re.findall(r"[a-z]+", txt) if len(w) >= 3})
    bylen = {}
    for w in types:
        bylen.setdefault(len(w), []).append(w)
    lens = [len(w) for w in CODE_WORDS]  # one length-matched random word per code string (36 words + alternatives)
    wreal = w_count(CLEAR, CODE_WORDS)
    whits = [(w, c) for w in CLEAR for c in CODE_WORDS if lev(w, c) <= 1]
    cnt = 0
    for _ in range(2000):
        lst = [rng.choice(bylen[L]) for L in lens]
        if w_count(CLEAR, lst) >= wreal:
            cnt += 1
    pw2 = (cnt + 1) / 2001
    res["T2"] = {"n_clear": len(CLEAR), "n_code_strings": len(CODE_WORDS),
                 "W_real": wreal, "hits": whits, "p": round(pw2, 4), "pass": wreal >= 1 and pw2 <= 0.05}

    # T3: per-token bigram cost under R9-SIENA7 seed-1 key
    key = json.loads(R9.read_text())["target"][0]["key"]
    letters = re.sub(r"[^a-z]", "", txt)
    big = Counter(zip(letters, letters[1:]))
    uni = Counter(letters)
    V = 26

    def cost(p, c):
        return -math.log10((big[(p, c)] + 1) / (uni[p] + V))
    costs = []
    for r in rs:
        dec = [key.get(t, "?") for t in r]
        for j, t in enumerate(r):
            costs.append((t, cost(dec[j - 1], dec[j]) if j > 0 and dec[j] != "?" and dec[j - 1] != "?" else None))
    vals = sorted(c for _, c in costs if c is not None)
    med = vals[len(vals) // 2]
    cnts = Counter(toks)
    low = {}
    for s, n in sorted(cnts.items(), key=lambda x: (x[1], x[0])):
        if n <= 3:
            cs = [c for t, c in costs if t == s and c is not None]
            mc = sum(cs) / len(cs) if cs else None
            low[s] = {"n": n, "fit_letter": key.get(s), "mean_cost": None if mc is None else round(mc, 3),
                      "high_cost": None if mc is None else mc > med}
    res["T3"] = {"median_cost": round(med, 3), "low_count_signs": low}

    js = json.dumps(res, indent=1, sort_keys=True) + "\n"
    if a.check:
        if not OUT.exists() or OUT.read_text() != js:
            print("STALE: results_r4750.json differs")
            sys.exit(1)
        print("check ok")
        return
    OUT.write_text(js)
    print(js)


if __name__ == "__main__":
    main()
