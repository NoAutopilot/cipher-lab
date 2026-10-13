#!/usr/bin/env python3
"""SALV-CRIB (13 Oct 2026, LANE DEFAULT-A4-2135): isomorph crib scan from f57v's plain passage, as pre-registered in
PREREG-SALV-CRIB.md (pushed before any score). Disk only.

Cipher: the eight leaves' ciphertext_<leaf>.tsv rows read exactly as build_spec.py reads them (same f57r 17.15+ drop, same
hapax ids); a sign run is a maximal stretch of sign boxes, broken only by a plain box (a line end does not break it).
Views: F = full sign string (base^marks), B = base code only. Statistic H(w) = number of length-L windows inside runs
whose equality pattern is exactly w's letter-equality pattern. Nulls: 1,000 permutations of w's letters; 1,000 random
same-length folded words from the it16 corpus. Gate: p <= 0.005 against both, and H >= 1.
Planted control: synthetic cipher on the target's run lengths, it16 plain, the crib planted once, design matched to the
view (F: the target's code+mark types as homophones; B: its 36 base codes), CM_ERR measured-error mix at 0.064 and 0.146.

  python3 crib_scan.py            run everything, write crib_scan_results.tsv and crib_scan_control.tsv, print summary
  python3 crib_scan.py --check    rerun and exit 1 if the committed TSVs differ (rule 7; deterministic seeds)
"""
import csv, os, random, re, sys
from collections import Counter

D = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(D))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import homophonic_anneal as ha  # fold()

LEAVES = ("f54r", "f54v", "f55r", "f55v", "f56r", "f56v", "f57r", "f57v")
GATED = ["pagare", "contentato", "diligentia", "beueraggio", "suggellata"]
VARIANTS = ["bisognera", "prometto", "salviati", "octobre"]
NNULL, ALPHA, SEEDS, ERRS = 1000, 0.005, 20, (0.064, 0.146)
MIX = (0.465, 0.331, 0.204)  # del : ins : code, codemark_curve.py CM_MIX default
PARTNER = {"#": "+", "+": "#", "g": "y", "y": "g", "bh": "g", "Z": "#", "f": "y", "phi": "bh"}
CORPUS = ["alcuneletteredip00ferr.txt", "delleletterefam02seghgoog.txt", "lettereinedited00tassgoog.txt",
          "lettereinedited01cibrgoog.txt", "lettereineditedi01carouoft.txt"]
RES = os.path.join(D, "crib_scan_results.tsv")
CTL = os.path.join(D, "crib_scan_control.tsv")


def runs():
    """[(tokens, locs)]: tokens 'base^marks', locs 'leaf.line.pos'."""
    out, cur, loc = [], [], []
    for lf in LEAVES:
        for x in csv.DictReader(open(os.path.join(D, f"ciphertext_{lf}.tsv")), delimiter="\t"):
            if lf == "f57r" and x["line"] == "17" and float(x["pos"]) >= 15:
                continue
            if x["code"] == "_":
                if cur:
                    out.append((cur, loc)); cur, loc = [], []
                continue
            code = f"?{lf}.{x['line']}.{x['pos']}" if x["code"] == "?" else x["code"]
            cur.append(f"{code}^{x['marks']}"); loc.append(f"{lf}.{x['line']}.{x['pos']}")
    if cur:
        out.append((cur, loc))
    return out


def base(t):
    return t.split("^", 1)[0]


def pat(seq):
    first = {}
    return tuple(first.setdefault(s, len(first)) for s in seq)


def windows(rs, L):
    for ri, r in enumerate(rs):
        for i in range(len(r) - L + 1):
            yield ri, i, r[i:i + L]


def pattern_counts(rs, L):
    return Counter(pat(w) for _, _, w in windows(rs, L))


def corpus_text():
    return "".join(open(os.path.join(ROOT, "tools", "data", "it16", f), encoding="utf-8", errors="ignore").read()
                   for f in CORPUS)


def corpus_words(txt):
    ws = set()
    for w in re.split(r"[^a-zA-Zàèéìòùáíóú]+", txt.lower()):
        f = ha.fold(w)
        if f:
            ws.add(f)
    by = {}
    for w in sorted(ws):
        by.setdefault(len(w), []).append(w)
    return by


def nulls(w, by_len, rng):
    perms = []
    for _ in range(NNULL):
        l = list(w); rng.shuffle(l); perms.append("".join(l))
    pool = [x for x in by_len.get(len(w), []) if x != w]
    words = [rng.choice(pool) for _ in range(NNULL)]
    return perms, words


def pval(h, cnt, sample):
    return (1 + sum(1 for s in sample if cnt.get(pat(s), 0) >= h)) / (NNULL + 1)


def score(w, cnt, by_len, rng):
    perms, words = nulls(w, by_len, rng)
    h = cnt.get(pat(w), 0)
    p1, p2 = pval(h, cnt, perms), pval(h, cnt, words)
    differ = sum(1 for s in perms if pat(s) != pat(w)) / NNULL
    return h, p1, p2, differ, (h >= 1 and p1 <= ALPHA and p2 <= ALPHA)


# ---------- planted control ----------
def alloc(units, freqs):
    """codemark_curve.py's alloc: highest-frequency unit to the letter with the largest remaining deficit."""
    tot_u, tot_f = sum(w for _, w in units), sum(freqs.values())
    deficit = {a: f / tot_f for a, f in freqs.items()}
    homs = {a: [] for a in freqs}
    for name, w in units:
        empty = [a for a in homs if not homs[a]]
        a = max(empty, key=lambda a: freqs[a]) if empty else max(deficit, key=deficit.get)
        homs[a].append((name, w)); deficit[a] -= w / tot_u
    return homs


def synth(view, crib, err, seed, lens, plain, units, base_freq):
    rng = random.Random(seed * 1000 + len(crib) * 7 + int(err * 1000) + (0 if view == "F" else 500000))
    start = rng.randrange(0, len(plain) - sum(lens) - 10)
    p = plain[start:start + sum(lens)]
    letters, k = [], 0
    for n in lens:
        letters.append(list(p[k:k + n])); k += n
    cand = [i for i, n in enumerate(lens) if n >= len(crib)]
    ri = rng.choice(cand); off = rng.randrange(0, lens[ri] - len(crib) + 1)
    letters[ri][off:off + len(crib)] = list(crib)
    homs = alloc(units, Counter(c for r in letters for c in r))
    bun, bw = zip(*base_freq.most_common())
    un, uw = zip(*units)
    out, planted = [], None
    for j, r in enumerate(letters):
        seq, clean = [], []
        for i, c in enumerate(r):
            names, ws = zip(*homs[c])
            s = rng.choices(names, ws)[0]
            hit = rng.random() < err
            if not hit:
                seq.append(s); clean.append(True); continue
            u = rng.random()
            if u < MIX[0]:
                clean.append(False)  # deleted
                if seq: pass
                continue
            if u < MIX[0] + MIX[1]:
                seq.append(s); clean.append(True)
                seq.append(rng.choices(un, uw)[0]); clean.append(False)  # inserted after
                continue
            b = base(s) if view == "F" else s
            nb = PARTNER.get(b) or rng.choices(bun, bw)[0]
            seq.append(nb + s[len(b):] if view == "F" else nb); clean.append(False)
        out.append(seq)
        if j == ri:
            planted = (ri, off, err)
    return out, ri, off, letters


def planted_found(view, rs, ri, off, crib):
    """Is the planted crib still an exact isomorph window somewhere in its run near its slot (within 2 positions)?"""
    r = rs[ri]; L = len(crib); pw = pat(crib)
    return any(0 <= i <= len(r) - L and pat(r[i:i + L]) == pw for i in range(off - 2, off + 3))


def main():
    rs = runs()
    toks = [t for r, _ in rs for t in r]
    views = {"F": [r for r, _ in rs], "B": [[base(t) for t in r] for r, _ in rs]}
    locs = [l for _, l in rs]
    txt = corpus_text()
    by_len = corpus_words(txt)
    plain = ha.fold(txt)
    lines = [f"runs {len(rs)} tokens {len(toks)} F-types {len(set(toks))} B-types {len(set(base(t) for t in toks))}"]
    res = [["crib", "gated", "view", "L", "H", "p_shuffle", "p_words", "perm_pattern_differs", "hit", "windows"]]
    rng = random.Random(20261013)
    for w in GATED + VARIANTS:
        for v in ("F", "B"):
            cnt = pattern_counts(views[v], len(w))
            h, p1, p2, differ, hit = score(w, cnt, by_len, rng)
            where = [locs[ri][i] for ri, i, s in windows(views[v], len(w)) if pat(s) == pat(w)]
            res.append([w, "yes" if w in GATED else "no", v, len(w), h, f"{p1:.4f}", f"{p2:.4f}", f"{differ:.3f}",
                        "HIT" if hit else "-", ",".join(where[:40]) + (",..." if len(where) > 40 else "")])
    # planted control
    lens = [len(r) for r, _ in rs]
    unitsF = Counter(toks).most_common()
    unitsB = Counter(base(t) for t in toks).most_common()
    bfreq = Counter(base(t) for t in toks)
    ctl = [["crib", "view", "err", "seeds", "power_gate", "planted_window_survives", "mean_H_planted"]]
    for w in GATED:
        for v, units in (("F", unitsF), ("B", unitsB)):
            for e in ERRS:
                passed = found = 0; hs = []
                for sd in range(1, SEEDS + 1):
                    syn, ri, off, _ = synth(v, w, e, sd, lens, plain, units, bfreq)
                    cnt = pattern_counts(syn, len(w))
                    h, p1, p2, _, hit = score(w, cnt, by_len, random.Random(sd))
                    passed += hit; found += planted_found(v, syn, ri, off, w); hs.append(h)
                ctl.append([w, v, e, SEEDS, f"{passed / SEEDS:.2f}", f"{found / SEEDS:.2f}", f"{sum(hs) / len(hs):.2f}"])
    # '#' descriptive
    hb = [t for t in toks if base(t) == "#"]
    rep = [f"{locs[ri][i]}" for ri, (r, _) in enumerate(rs) for i in range(len(r) - 1) if base(r[i]) == base(r[i + 1]) == "#"]
    lines.append(f"base # tokens {len(hb)}; marks {dict(Counter(t.split('^', 1)[1] for t in hb).most_common())}; "
                 f"## adjacent at {rep}")
    return res, ctl, lines


def dump(rows):
    return "".join("\t".join(str(c) for c in r) + "\n" for r in rows)


if __name__ == "__main__":
    res, ctl, lines = main()
    a, b = dump(res), dump(ctl)
    if "--check" in sys.argv:
        ok = open(RES).read() == a and open(CTL).read() == b
        print("ok" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(RES, "w").write(a); open(CTL, "w").write(b)
    print("\n".join(lines)); print(a); print(b)
