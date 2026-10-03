#!/usr/bin/env python3
"""spot1 gate (A2P4-LVN97, 3 Oct 2026): align the decoded 5797 spot1 run to Groen IV p.222 in order.

Implements spot1/prereg.md exactly (committed 7d636fe2 before any pass or alignment):
  python3 align_spot1.py            -> prints A, B for the target and controls (s) and (d), the gate, and per-unit
                                       decodes; writes spot1/gate.tsv and spot1/units.tsv
Inputs: spot1/ciphertext_spot1.tsv (reconciled, long format line/pos/sign/conf; clear words 'w:x', attached
fragments 'w:~x'), ../key_full.tsv, ../groen/groen_IV_CDXLIV.txt.
"""
import csv, random, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
T = HERE.parent

def norm(s):
    s = s.lower()
    for a, b in (("ä", "a"), ("ö", "o"), ("ü", "u"), ("ß", "ss"), ("v", "u"), ("w", "u"), ("j", "i"), ("y", "i"),
                 ("ck", "k")):
        s = s.replace(a, b)
    s = re.sub(r"[^a-z?]", "", s)
    return re.sub(r"([a-z])\1+", r"\1", s)

def lev(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cost = 0 if (ca == cb and ca != "?") else 1
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost))
        prev = cur
    return prev[-1]

def sim(a, b):
    return 1 - lev(a, b) / max(len(a), len(b), 1)

def load_key():
    key = {}
    for r in csv.DictReader(open(T / "key_full.tsv"), delimiter="\t"):
        key[r["code"].strip()] = r["value"].strip()
    return key

def units(path, key):
    """Decoded units in order: (kind, raw, decoded) with kind 'clear' or 'cipher'."""
    rows = list(csv.DictReader(open(path), delimiter="\t"))
    out, cur = [], None
    def flush():
        nonlocal cur
        if cur:
            out.append(("cipher", ".".join(cur[0]), "".join(cur[1]), cur[2]))
        cur = None
    for r in rows:
        s = r["sign"].strip()
        if s.startswith("w:") and not s.startswith("w:~"):
            flush(); out.append(("clear", s[2:], s[2:], 0)); continue
        if cur is None:
            cur = [[], [], 0]
        if s.startswith("w:~"):
            cur[0].append(s[3:]); cur[1].append(s[3:])
        else:
            v = key.get(s, "?")
            cur[0].append(s)
            if v == "NULL":
                continue
            if v in ("", "?") or not re.fullmatch(r"[a-z]+", v):
                cur[1].append("?" if v in ("", "?") or not v.isalpha() else v)
            else:
                cur[1].append(v); cur[2] += 1
    flush()
    return out

def groen_words(text):
    text = re.sub(r"Ga naar (margenoot\+|voetnoot\(?\d\)?) \[#\d+\]", "", text)
    return [w for w in (norm(x) for x in text.split()) if w]

def dp(cw, ref, thr=0.75, exact=False):
    """Monotone alignment; returns (matched cipher words, set of consumed ref indices)."""
    n, m = len(cw), len(ref)
    best = [[(0, 0, None)] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 and j == 0:
                continue
            cands = []
            if i: cands.append((best[i - 1][j][0], best[i - 1][j][1], ("skipc", i - 1, j)))
            if j: cands.append((best[i][j - 1][0], best[i][j - 1][1], ("skipr", i, j - 1)))
            if i:
                for k in ((1,) if exact else (1, 2, 3)):
                    if j - k < 0: break
                    r = "".join(ref[j - k:j])
                    ok = (cw[i - 1] == r) if exact else (sim(cw[i - 1], r) >= thr)
                    if ok:
                        p = best[i - 1][j - k]
                        cands.append((p[0] + 1, p[1] + k, ("match", i - 1, j - k, k)))
            best[i][j] = max(cands, key=lambda c: (c[0], c[1]))
    i, j, used = n, m, set()
    while (i or j) and best[i][j][2]:
        st = best[i][j][2]
        if st[0] == "match":
            used.update(range(st[2], st[2] + st[3])); i, j = st[1], st[2]
        elif st[0] == "skipc": i, j = st[1], st[2]
        else: i, j = st[1], st[2]
    return best[n][m][0], used

def stats(us, ref):
    clear = [norm(u[2]) for u in us if u[0] == "clear" and norm(u[2])]
    _, clear_used = dp(clear, ref, exact=True)
    F = set(range(len(ref))) - clear_used
    elig = [norm(u[2]) for u in us if u[0] == "cipher" and len(norm(u[2]).replace("?", "")) >= 3]
    nm, used = dp(elig, ref)
    A = len(used & F) / max(len(F), 1)
    B = nm / max(len(elig), 1)
    return A, B, len(F), len(elig), nm

def main():
    key = load_key()
    us = units(HERE / "ciphertext_spot1.tsv", key)
    g = (T / "groen" / "groen_IV_CDXLIV.txt").read_text().splitlines()
    para = [l for l in g if l.strip()]
    tgt_txt = next(l for l in para if "werden E.G. nhumehr von der bekannten" in l) + " " + \
        next(l for l in para if l.startswith("Wir seint resolvirt alsbalt"))
    ref = groen_words(tgt_txt)
    N = len(ref)
    def window(starts):
        i = next(k for k, l in enumerate(para) if l.lstrip().startswith(starts) or starts in l[:60])
        ws = []
        for l in para[i:]:
            ws += groen_words(l)
            if len(ws) >= N: break
        return ws[:N]
    d = {"d1": window("Die schwere last"), "d2": window("Ga naar margenoot+ [#496]Von zeittungen"),
         "d3": window("Es lest sich, Gott lob")}
    out = [("target", *stats(us, ref))]
    Bs = []
    for seed in range(1, 201):
        r = ref[:]; random.Random(seed).shuffle(r)
        s = stats(us, r); Bs.append(s[1]); out.append((f"s{seed}", *s))
    for k, v in d.items():
        out.append((k, *stats(us, v)))
    with open(HERE / "gate.tsv", "w") as f:
        f.write("ref\tA\tB\tF\teligible\tmatched\n")
        for row in out:
            f.write("\t".join(str(round(x, 4)) if isinstance(x, float) else str(x) for x in row) + "\n")
    with open(HERE / "units.tsv", "w") as f:
        f.write("n\tkind\traw\tdecoded\tletters\n")
        for i, u in enumerate(us, 1):
            f.write(f"{i}\t{u[0]}\t{u[1]}\t{u[2]}\t{u[3]}\n")
    A, B = out[0][1], out[0][2]
    p95 = sorted(Bs)[int(0.95 * len(Bs)) - 1]
    dmax = max(o[2] for o in out if o[0] in d)
    g1, g2, g3 = A >= 0.50, B >= p95 + 0.15, B >= dmax + 0.15
    print(f"target N={N} words: A={A:.3f} (F={out[0][3]}) B={B:.3f} ({out[0][5]}/{out[0][4]})")
    print(f"shuffle (s) n=200: B mean {sum(Bs)/len(Bs):.3f} p95 {p95:.3f} max {max(Bs):.3f}; A mean "
          f"{sum(o[1] for o in out if o[0].startswith('s'))/200:.3f}")
    for o in out:
        if o[0] in d:
            print(f"{o[0]}: A={o[1]:.3f} B={o[2]:.3f} ({o[5]}/{o[4]})")
    print(f"gate: A>=0.50 {g1}; B>=p95+0.15 {g2}; B>=dmax+0.15 {g3} -> {'PASS' if g1 and g2 and g3 else 'FAIL'}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
