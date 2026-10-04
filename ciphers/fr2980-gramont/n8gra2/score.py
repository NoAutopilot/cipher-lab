#!/usr/bin/env python3
"""N8-GRA2 scorer (PREREG-N8-GRA2.md): share of keyed cipher tokens of fr.3040 f.18r whose key.tsv value agrees with
the aligned Le Grand III p.454-455 print, beside N1 (shuffled print) and N2 (shuffled key) p99 nulls and the planted
positive control P (print enciphered with key.tsv, 13% token error, same N, 20 seeds).

  python3 score.py --control            # control and its own nulls only (run first)
  python3 score.py --target recon.tsv   # target (rows f18r_L01..L10 per the PREREG), its nulls, per-code alignments
"""
import argparse, json, random, re, sys, unicodedata
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
KEY = HERE.parent / "key.tsv"
PRINT = HERE / "print_span.txt"
MATCH, MISM, GAP = 2, -1, -2
ERR = 0.13  # registered; --err overrides for the post-hoc bracket only
ROWS = {f"f18r_L{i:02d}" for i in range(1, 11)}


def norm(s):
    s = s.replace("ſ", "s")
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).upper()
    s = s.replace("J", "I").replace("Y", "I").replace("U", "V").replace("W", "VV")
    return re.sub(r"[^A-Z]", "", s)


def load_key():
    key = {}
    for ln in KEY.read_text().splitlines()[1:]:
        f = ln.split("\t")
        if len(f) >= 2:
            key[f[0]] = f[1]
    return key


def keyed(v):
    return v not in ("NULL", "?", "") and v.isalpha()


def load_print():
    return norm(" ".join(l for l in PRINT.read_text().splitlines() if not l.startswith("#")))


def decode(tokens, key):
    """tokens -> list of (token, letters or None for wildcard or '' for null)."""
    out = []
    for t in tokens:
        if t in ("/", ".") or not t:
            continue
        if "?" in t or "|" in t or t.startswith("NEW:") or t not in key:
            out.append((t, None))
            continue
        v = key[t]
        if v == "NULL":
            continue
        out.append((t, norm(v) if keyed(v) else None))
    return out


def align_agree(dec, pr):
    """semi-global NW; returns (agree, keyed_n, per-token aligned print string or None)."""
    letters, owner = [], []
    for k, (t, v) in enumerate(dec):
        for c in (v if v else "*"):
            letters.append(c); owner.append(k)
    n, m = len(letters), len(pr)
    P = np.frombuffer(pr.encode(), dtype=np.uint8)
    H = np.zeros((n + 1, m + 1))
    ar = np.arange(m + 1) * (-GAP)
    for i in range(1, n + 1):
        c = letters[i - 1]
        if c == "*":
            s = np.zeros(m)
        else:
            s = np.where(P == ord(c), MATCH, MISM).astype(float)
        A = np.empty(m + 1)
        A[0] = H[i - 1, 0] + GAP
        A[1:] = np.maximum(H[i - 1, :-1] + s, H[i - 1, 1:] + GAP)
        H[i] = np.maximum.accumulate(A + ar) - ar
    j = int(np.argmax(H[n])); i = n
    got = [[] for _ in dec]
    while i > 0:
        c = letters[i - 1]
        if j > 0:
            s = 0 if c == "*" else (MATCH if pr[j - 1] == c else MISM)
            if np.isclose(H[i, j], H[i - 1, j - 1] + s):
                got[owner[i - 1]].append(pr[j - 1]); i -= 1; j -= 1; continue
        if np.isclose(H[i, j], H[i - 1, j] + GAP):
            got[owner[i - 1]].append("-"); i -= 1; continue
        j -= 1
    al = ["".join(reversed(g)) for g in got]
    kn = sum(1 for (t, v) in dec if v)
    ag = sum(1 for (t, v), a in zip(dec, al) if v and a == v)
    return ag / kn if kn else 0.0, kn, al


def nulls(tokens, key, pr, rng, reps=200):
    n1, n2 = [], []
    dec = decode(tokens, key)
    for _ in range(reps):
        l = list(pr); rng.shuffle(l)
        n1.append(align_agree(dec, "".join(l))[0])
        codes = [c for c, v in key.items() if keyed(v)]
        vals = [key[c] for c in codes]; rng.shuffle(vals)
        k2 = dict(key); k2.update(zip(codes, vals))
        n2.append(align_agree(decode(tokens, k2), pr)[0])
    return float(np.percentile(n1, 99)), float(np.percentile(n2, 99))


def plant(key, pr, n, rng):
    by = {}
    for c, v in key.items():
        if keyed(v) and len(norm(v)) == 1:
            by.setdefault(norm(v), []).append(c)
    allc = [c for c, v in key.items() if keyed(v)]
    toks = [rng.choice(by[ch]) for ch in pr if ch in by][:n]
    return [rng.choice([c for c in allc if c != t]) if rng.random() < ERR else t for t in toks]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--control", action="store_true")
    ap.add_argument("--target")
    ap.add_argument("--n", type=int, default=0, help="control length (default: target keyed length or 200)")
    ap.add_argument("--seeds", type=int, default=20)
    ap.add_argument("--err", type=float, default=None, help="post-hoc bracket only; the registered control is 0.13")
    ap.add_argument("--reps", type=int, default=200)
    a = ap.parse_args()
    global ERR
    if a.err is not None:
        ERR = a.err
    key, pr = load_key(), load_print()
    res = {}
    if a.control:
        n = a.n or 200
        sc, n1s, n2s = [], [], []
        for s in range(a.seeds):
            rng = random.Random(s)
            t = plant(key, pr, n, rng)
            sc.append(align_agree(decode(t, key), pr)[0])
            if s < 3:
                p1, p2 = nulls(t, key, pr, rng, a.reps)
                n1s.append(p1); n2s.append(p2)
        res["control"] = dict(n=n, err=ERR, mean=float(np.mean(sc)), min=float(min(sc)), N1_p99=max(n1s), N2_p99=max(n2s),
                              gate=max(max(n1s), max(n2s)) + 0.15)
        res["control"]["pass"] = res["control"]["mean"] >= res["control"]["gate"]
    if a.target:
        toks = []
        for ln in Path(a.target).read_text().splitlines():
            f = ln.split("\t")
            if len(f) == 2 and f[0][:9] in ROWS:
                toks += f[1].split()
        dec = decode(toks, key)
        ag, kn, al = align_agree(dec, pr)
        p1, p2 = nulls(toks, key, pr, random.Random(99), a.reps)
        res["target"] = dict(tokens=len(dec), keyed=kn, agree=ag, N1_p99=p1, N2_p99=p2,
                             pass_=bool(ag >= 0.50 and ag > max(p1, p2)))
        per = {}
        for (t, v), x in zip(dec, al):
            per.setdefault(t, []).append((v or "", x))
        res["per_code"] = {t: [f"{v}->{x}" for v, x in L] for t, L in sorted(per.items())}
    print(json.dumps(res, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
