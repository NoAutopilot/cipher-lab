#!/usr/bin/env python3
"""DEC4450-INIT: does fr.2988 f.4 (Raince's clear French) track the base letters of f.2 (Ranzo's initial-letter code)?

Pre-registered in ../PREREG-DEC4450-INIT.md before any f.4 initials were scored.

Inputs
  f2 groups : ../../fr2988-ranzo-1520s/bourdeau/ranzo_c006.txt + ranzo_c007.txt (Bourdeau's transcription, f.2r-v)
  f4 initials: initials.tsv (segment, pos, initial) -- the reconciled initials of the opening and closing lines of
               Raince's f.4-6 letter (two blind passes, reconciled).
Statistic
  S = SW(open_f4, first WIN groups of f.2) + SW(close_f4, last WIN groups of f.2), Smith-Waterman local alignment of
  letter strings (lower-cased; match +2, mismatch -1, gap -2).
Null (shuffled pairing)
  the f.2 letter sequence permuted (composition kept), N_NULL times, same S; p = (1 + #null >= S) / (1 + N_NULL).
Positive control
  synthetic f.2: the same f.4 initials placed at the opening/closing of an f.2-length French initial stream from the
  fr16 corpus, with substitution error at the measured pass disagreement rate and 10% word insertion/deletion; the
  control passes if >= 90% of N_CTRL replicates reach p < 0.01 against the same null.
Usage: score_f2f4.py [--check]   (--check: recompute and compare with result.json, exit 1 if stale)
"""
import gzip, json, random, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
WIN = 150
N_NULL = 2000
N_CTRL = 100
SEED = 4450
INDEL = 0.10


def f2_letters():
    toks = []
    for n in ("ranzo_c006.txt", "ranzo_c007.txt"):
        for line in (ROOT / "ciphers/fr2988-ranzo-1520s/bourdeau" / n).read_text().splitlines():
            if line.startswith("#"):
                continue
            toks += line.split()
    out = []
    for t in toks:
        m = re.match(r"[A-Za-z]", t)
        out.append(fold(m.group(0)) if m else "?")
    return out


def fold(c):
    c = c.lower()
    return {"v": "u", "j": "i"}.get(c, c)


def f4_initials():
    seg = {"open": [], "close": []}
    for line in (HERE / "initials.tsv").read_text().splitlines()[1:]:
        if not line.strip():
            continue
        s, _pos, ini = line.split("\t")[:3]
        seg[s].append(fold(ini.strip()) if ini.strip() else "?")
    return seg["open"], seg["close"]


def sw(a, b, match=2, mis=-1, gap=-2):
    best = 0
    prev = [0] * (len(b) + 1)
    for i in range(1, len(a) + 1):
        cur = [0] * (len(b) + 1)
        ai = a[i - 1]
        for j in range(1, len(b) + 1):
            d = prev[j - 1] + (match if ai == b[j - 1] and ai != "?" else mis)
            v = max(0, d, prev[j] + gap, cur[j - 1] + gap)
            cur[j] = v
            if v > best:
                best = v
        prev = cur
    return best


def stat(op, cl, f2):
    return sw(op, f2[:WIN]) + sw(cl, f2[-WIN:])


def pval(op, cl, f2, rng, n=N_NULL):
    s = stat(op, cl, f2)
    ge = 0
    perm = list(f2)
    for _ in range(n):
        rng.shuffle(perm)
        if stat(op, cl, perm) >= s:
            ge += 1
    return s, (1 + ge) / (1 + n)


_WORDS = []


def corpus_initials(rng, n):
    words = _WORDS
    if not words:
      for p in sorted((ROOT / "tools/data/fr16").glob("*_djvu.txt.gz")):
        txt = gzip.open(p, "rt", errors="ignore").read().lower()
        words += re.findall(r"[a-zàâçéèêëîïôûùüÿ]+", txt)
    start = rng.randrange(0, len(words) - n - 1)
    return [fold(w[0]) for w in words[start:start + n]]


def noisy(seq, err, rng):
    out = []
    for c in seq:
        r = rng.random()
        if r < INDEL / 2:
            continue  # deletion
        if r < INDEL:
            out.append(rng.choice("abcdefghilmnopqrstu"))  # insertion
        out.append(rng.choice("abcdefghilmnopqrstu") if rng.random() < err else c)
    return out


def control(op, cl, n_f2, err, rng):
    hits = 0
    for _ in range(N_CTRL):
        mid = corpus_initials(rng, n_f2)
        syn = noisy(op, err, rng) + mid[len(op):n_f2 - len(cl)] + noisy(cl, err, rng)
        _s, p = pval(op, cl, syn, rng, n=200)
        hits += p < 0.01
    return hits / N_CTRL


def main():
    rng = random.Random(SEED)
    f2 = f2_letters()
    op, cl = f4_initials()
    err = json.loads((HERE / "measured_error.json").read_text())["initial_error"]
    s, p = pval(op, cl, f2, rng)
    ctrl = control(op, cl, len(f2), err, rng)
    res = {"f2_groups": len(f2), "open_len": len(op), "close_len": len(cl), "win": WIN, "S": s, "p": round(p, 4),
           "n_null": N_NULL, "ctrl_power": ctrl, "ctrl_err": err, "indel": INDEL,
           "diag_best_open_all": sw(op, f2), "diag_best_close_all": sw(cl, f2),
           "verdict": ("CONTROL BELOW GATE (non-test)" if ctrl < 0.9 else ("PASS" if p < 0.01 else "FAIL"))}
    out = json.dumps(res, indent=1, sort_keys=True) + "\n"
    if "--check" in sys.argv:
        old = (HERE / "result.json").read_text()
        if old != out:
            print("STALE result.json"); print(out); sys.exit(1)
        print("result.json current"); return
    (HERE / "result.json").write_text(out)
    print(out)


if __name__ == "__main__":
    main()
