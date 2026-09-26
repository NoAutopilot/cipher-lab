#!/usr/bin/env python3
"""AX-NAMES: align each Groen-printed sibling letter's cipher token stream to Groen's clear print and
record what every code above 120 absorbs (name, word, syllable or nothing).

Model (semi-global DP per manuscript page, plaintext = the whole printed letter, free start/end):
  * a numeral 1-120 emits its key.tsv block letter (cost 0 on a match, u=v, i=j=y cheap; else 1);
  * ii / iii emit p / l; a clear =word emits its letters (same match costs);
  * every code above 120 is FREE here (key.tsv's own values for them are not assumed): it emits
    0..MAXL printed letters at cost BASE + PER*len, so it absorbs a stretch only where the numeral
    and clear-word stream leaves one unexplained;
  * skip a token (cost 1), skip a printed letter (cost 1).
Per occurrence of a code >120 it writes the absorbed string and the number of exactly matched
letters on each side in a +-6 window (the anchors), to axnames/occ_<letter>.tsv.

Usage: python3 axnames/align_names.py [LETTER ...]   (default: all pairs in PAIRS)
"""
import csv, os, re, sys, unicodedata
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
JAN = os.path.join(os.path.dirname(T), "jan-van-nassau-1572-75")
MAXL, BASE, PER = 22, 0.6, 0.15


def letters(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if c.isalpha() and c.isascii())
    return s.replace("j", "i").replace("v", "u").replace("w", "uu")


def keymap():
    k = {}
    with open(os.path.join(T, "key.tsv")) as f:
        for r in csv.DictReader(f, delimiter="\t"):
            k[r["code"]] = r["value"]
    return k


def groen_body(fname, start, end):
    txt = open(os.path.join(T, fname if "/" in fname or fname.startswith("plaintext") else os.path.join("groen", fname))).read()
    txt = re.sub(r"\[pagina \d+\]|\[p\. \d+\]|Ga naar (margenoot|voetnoot)\S*\s*\[#\d+\]", " ", txt)
    txt = re.sub(r"\[struck:[^\]]*\]", " ", txt)
    i = txt.index(start)
    j = txt.index(end, i) + len(end)
    return txt[i:j]


# letter id -> (ciphertext tsv, [(groen file, start phrase, end phrase)])
PAIRS = {
    "5810": ("ciphertext_5810.tsv", [("groen_IV_CDLXVIII.txt", "Messieurs mes frères, par la lettre", "Vlessingue, ce 6e janvier")]),
    "5811": ("ciphertext_5811.tsv", [("groen_IV_CDLXXXIII.txt", "Messieurs mes frères. Depuis", "Nicolas Brunynck")]),
    # known-answer control only (key.tsv's own source pair; excluded from names.tsv by build_names.py)
    "sib": ("ciphertext_sib.tsv", [("plaintext_4613.txt", "Monseigneur depuis", "25 de Mars"), ("plaintext_4615.txt", "Monsieur, depuis", "l'an 1574")]),
    "4503": ("ciphertext_4503.tsv", [("groen_IV_CDLXXXIV.txt", "Monsieur mon frère. Retournant", "ensemble ce que faict l'ennemy")]),
}


def clean_pt(s):
    return letters(s)


def tokens(path):
    out = []
    with open(os.path.join(T, path)) as f:
        for r in csv.DictReader(f, delimiter="\t"):
            s = (r.get("sign") or r.get("token") or "").strip()
            if s.startswith("w:"):
                s = "=" + s[2:]
            if not s or s.startswith("["):
                continue
            out.append((r["line"], r.get("position") or r.get("idx"), s))
    return out


def emit(sign, key):
    """-> ('fix', letters) or ('free', code)."""
    if sign.startswith("="):
        return ("fix", letters(sign[1:]))
    if sign == "ii":
        return ("fix", "p")
    if sign == "iii":
        return ("fix", "l")
    if "/" in sign:  # unsettled split: take the first reading
        sign = sign.split("/")[0]
    if sign.isdigit():
        n = int(sign)
        if 1 <= n <= 120:
            return ("fix", letters(key.get(sign, "")) or "?")
        return ("free", str(n))
    return ("fix", letters(sign))


EQ = {("u", "v"), ("i", "y")}


def mcost(a, b):
    if a == b:
        return 0.0
    if (a, b) in EQ or (b, a) in EQ:
        return 0.2
    return 1.0


def align_page(toks, pt, key):
    """Semi-global DP over expanded units (one unit per emitted letter for fixed tokens)."""
    units = []  # (tok_index, kind, letter-or-code)
    for ti, (_, _, s) in enumerate(toks):
        kind, v = emit(s, key)
        if kind == "fix":
            for c in v:
                units.append((ti, "L", c))
        else:
            units.append((ti, "F", v))
    P = len(pt)
    parr = np.array([ord(c) for c in pt])
    INF = 1e9
    n = len(units)
    D = np.empty((n + 1, P + 1), dtype=np.float32)
    D[0] = 0.0  # free start in plaintext
    ar = np.arange(P + 1, dtype=np.float32)
    for i, (_, kind, v) in enumerate(units, 1):
        prev = D[i - 1]
        cur = prev + 1.0  # skip this unit
        if kind == "L":
            c = ord(v)
            mc = np.where(parr == c, 0.0, 1.0).astype(np.float32)
            if v in "uv":
                mc = np.where((parr == ord("u")) | (parr == ord("v")), 0.0, mc)
            if v in "iy":
                mc = np.where((parr == ord("i")) | (parr == ord("y")), np.minimum(mc, 0.2), mc)
            cur[1:] = np.minimum(cur[1:], prev[:-1] + mc)
        else:
            best = prev + BASE
            for k in range(1, MAXL + 1):
                cand = np.full(P + 1, INF, dtype=np.float32)
                cand[k:] = prev[:-k] + BASE + PER * k
                best = np.minimum(best, cand)
            cur = np.minimum(cur, best)
        # skip printed letters: cur[j] = min_k cur[k] + (j-k)
        cur = np.minimum.accumulate(cur - ar) + ar
        D[i] = cur
    # backtrace from best end (free end)
    j = int(np.argmin(D[n]))
    score = float(D[n][j])
    i = n
    path = []  # (unit index, pt start, pt end)
    while i > 0:
        _, kind, v = units[i - 1]
        val = D[i][j]
        prev = D[i - 1]
        if j > 0 and abs(D[i][j - 1] + 1.0 - val) < 1e-3 and not _unit_explains(units[i - 1], prev, j, val, pt):
            j -= 1
            continue
        if kind == "L":
            if j > 0 and abs(prev[j - 1] + mcost(v, pt[j - 1]) - val) < 1e-3:
                path.append((i - 1, j - 1, j)); i -= 1; j -= 1; continue
            if abs(prev[j] + 1.0 - val) < 1e-3:
                path.append((i - 1, j, j)); i -= 1; continue
            # u/v i/y equivalence tolerance
            if j > 0 and abs(prev[j - 1] + 0.2 - val) < 1e-3:
                path.append((i - 1, j - 1, j)); i -= 1; j -= 1; continue
        else:
            done = False
            for k in range(0, min(MAXL, j) + 1):
                if abs(prev[j - k] + BASE + PER * k - val) < 1e-3:
                    path.append((i - 1, j - k, j)); i -= 1; j -= k; done = True; break
            if done:
                continue
            if abs(prev[j] + 1.0 - val) < 1e-3:
                path.append((i - 1, j, j)); i -= 1; continue
        if j > 0:
            j -= 1
            continue
        path.append((i - 1, j, j)); i -= 1
    path.reverse()
    return units, path, score


def _unit_explains(unit, prev, j, val, pt):
    _, kind, v = unit
    if kind == "L":
        return (j > 0 and abs(prev[j - 1] + mcost(v, pt[j - 1]) - val) < 1e-3) or abs(prev[j] + 1.0 - val) < 1e-3
    for k in range(0, min(MAXL, j) + 1):
        if abs(prev[j - k] + BASE + PER * k - val) < 1e-3:
            return True
    return abs(prev[j] + 1.0 - val) < 1e-3


def run(letter, toks, pt, key, pagekey=lambda t: t[0].split("_")[1] if "_" in t[0] else t[0]):
    pages = {}
    for t in toks:
        pages.setdefault(pagekey(t), []).append(t)
    rows = []
    for pg, ptoks in pages.items():
        units, path, score = align_page(ptoks, pt, key)
        # per-unit exact-match flags for anchor counting
        match = []
        for (ui, s, e) in path:
            _, kind, v = units[ui]
            match.append(kind == "L" and e - s == 1 and mcost(v, pt[s]) < 0.5)
        for pi, (ui, s, e) in enumerate(path):
            ti, kind, v = units[ui]
            if kind != "F":
                continue
            left = sum(match[max(0, pi - 6):pi])
            right = sum(match[pi + 1:pi + 7])
            line, pos, sign = ptoks[ti]
            ctx_l = pt[max(0, s - 12):s]
            ctx_r = pt[e:e + 12]
            rows.append([letter, pg, pi, line, pos, v, pt[s:e], left, right, ctx_l, ctx_r])
        n_l = sum(1 for u in units if u[1] == "L")
        n_m = sum(match)
        print(f"{letter} {pg}: units {len(units)}, letter units {n_l}, exact matches {n_m} ({100*n_m/max(1,n_l):.0f}%), score {score:.0f}", file=sys.stderr)
    return rows


HDR = ["letter", "page", "unit", "line", "pos", "code", "absorbed", "left_anchor", "right_anchor", "ctx_left", "ctx_right"]


def main():
    key = keymap()
    which = sys.argv[1:] or list(PAIRS)
    for letter in which:
        ct, spans = PAIRS[letter]
        pt = "".join(letters(groen_body(*sp)) for sp in spans)
        pk = (lambda t: t[0].split("_")[0]) if letter == "sib" else (lambda t: t[0].split("_")[1] if "_" in t[0] else t[0])
        rows = run(letter, tokens(ct), pt, key, pk)
        with open(os.path.join(HERE, f"occ_{letter}.tsv"), "w") as f:
            w = csv.writer(f, delimiter="\t", lineterminator="\n")
            w.writerow(HDR)
            w.writerows(rows)


if __name__ == "__main__":
    main()
