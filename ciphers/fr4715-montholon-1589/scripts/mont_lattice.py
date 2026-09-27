#!/usr/bin/env python3
"""MONT-LATTICE (27 Sept 2026): a per-position digit lattice for the four f.81r calibration lines, decoded with the
key's code inventory, a French letter bigram and a dotted word-code prior; scored by mont4715c.py digscore unchanged.

    python3 scripts/mont_lattice.py tune       # grid on the tuned pair (L03, L08) only; writes witness/lattice/tune.tsv
    python3 scripts/mont_lattice.py run        # chosen setting -> witness/lattice/lattice.tsv (+ shuffled-weight
                                               # streams shuffle_{1..5}.tsv, neighbour log neighbours.tsv)
    python3 scripts/mont4715c.py digscore witness/lattice/lattice.tsv L13,L15   # the held-out gate (NOTES.md)

Pre-registration, held-out rule and controls: NOTES.md "MONT-LATTICE". Script only, no network, no reading call.
Voters are the streams already on disk; the decoder may choose only a digit some voter proposed or a MONT-CAL
confusion neighbour of one (logged), never a digit at a column no voter read.
"""
import csv
import gzip
import glob
import json
import math
import os
import random
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mont4715c as M  # noqa: E402

LINES = ["L03", "L08", "L13", "L15"]
TUNED, HELD = ["L03", "L08"], ["L13", "L15"]
RD = "witness/read_digits/"
OUT = "witness/lattice/"
# MONT-CAL U1's ten most frequent confusions, true -> read: 3->5 3->7 3->0 5->3 8->0 5->0 2->3 8->1 8->5 1->5.
# A read digit r therefore proposes every true t with t->r in that list.
CONF = [("3", "5"), ("3", "7"), ("3", "0"), ("5", "3"), ("8", "0"), ("5", "0"), ("2", "3"), ("8", "1"), ("8", "5"),
        ("1", "5")]
NEIGH = {}
for t, r in CONF:
    NEIGH.setdefault(r, set()).add(t)
VOTERS = ["C", "A", "B", "PA", "PB", "V2"]
DOT_BLIND = {"B"}  # call B returned no dot marks at all (MONT-RECROP); it abstains on dots


# ---------------------------------------------------------------- voter streams
def voter_streams():
    out = {}
    for v, f in (("C", "call_C.tsv"), ("A", "call_A.tsv"), ("B", "call_B.tsv"), ("V2", "ref_v2.tsv")):
        rec = M.read_stream_tsv(RD + f)
        out[v] = {}
        for ln in LINES:
            st = M.stream_of(rec.get(ln, ""))
            if v == "A":  # call A's '???' tail marks where its truncated sheet lost the line: no coverage
                while st and st[-1][0] == "?":
                    st.pop()
            out[v][ln] = st
    for v, f in (("PA", "witness/pass_a.tsv"), ("PB", "witness/pass_b.tsv")):
        out[v] = {ln: [] for ln in LINES}
        for r in csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"):
            ln = r["line"].strip()
            if ln not in out[v]:
                continue
            s = r["sign"].strip()
            if re.fullmatch(r"'?\d+", s):
                out[v][ln] += M.stream_of(s)
            else:
                out[v][ln].append(("?", False))
    return out


def align(back, oth):
    """Semi-global alignment of a voter stream to the backbone (free end gaps); '?' matches anything at 0.
    Returns ops: ('m', i, j) aligned, ('d', i) backbone i with voter gap, ('i', i, j) voter j inserted after i."""
    n, m = len(back), len(oth)
    NEG = -10 ** 9
    S = [[0] * (m + 1) for _ in range(n + 1)]
    T = [[None] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        T[i][0] = "u"
    for j in range(1, m + 1):
        T[0][j] = "l"
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            a, b = back[i - 1][0], oth[j - 1][0]
            s = 0 if "?" in (a, b) else (2 if a == b else -1)
            best, t = S[i - 1][j - 1] + s, "d"
            gu = 0 if j == m else -2
            gl = 0 if i == n else -2
            if S[i - 1][j] + gu > best:
                best, t = S[i - 1][j] + gu, "u"
            if S[i][j - 1] + gl > best:
                best, t = S[i][j - 1] + gl, "l"
            S[i][j], T[i][j] = best, t
    ops, i, j = [], n, m
    while i > 0 or j > 0:
        t = T[i][j]
        if t == "d":
            ops.append(("m", i - 1, j - 1)); i -= 1; j -= 1
        elif t == "u":
            ops.append(("d", i - 1)); i -= 1
        else:
            ops.append(("i", i - 1, j - 1)); j -= 1
    ops.reverse()
    # coverage: backbone positions between the voter's first and last aligned position
    mi = [o[1] for o in ops if o[0] == "m"]
    lo, hi = (min(mi), max(mi)) if mi else (1, 0)
    return ops, lo, hi


def build_columns(streams, ln, w):
    """Columns keyed (i, k): k=0 backbone position i of call C; k>=1 the k-th digit a voter inserted after i.
    Each column: votes {digit|'none': weight}, dot weight, dot-capable cover weight, proposers {digit: [voters]}."""
    back = streams["C"][ln]
    cols = {}

    def col(key):
        return cols.setdefault(key, {"v": {}, "dot": 0.0, "dcov": 0.0, "who": {}})

    def vote(key, v, sym, dotted):
        if w.get(v, 0) <= 0:
            return
        c = col(key)
        if sym == "?":
            return
        c["v"][sym] = c["v"].get(sym, 0) + w[v]
        if sym != "none":
            c["who"].setdefault(sym, []).append(v)
            if v not in DOT_BLIND:
                c["dcov"] += w[v]
                if dotted:
                    c["dot"] += w[v]

    for i, (d, dt) in enumerate(back):
        col((i, 0))
        vote((i, 0), "C", d, dt)
    for v in VOTERS:
        if v == "C" or w.get(v, 0) <= 0:
            continue
        oth = streams[v][ln]
        ops, lo, hi = align(back, oth)
        ins = {}
        for o in ops:
            if o[0] == "m":
                vote((o[1], 0), v, oth[o[2]][0], oth[o[2]][1])
            elif o[0] == "d" and lo <= o[1] <= hi:
                vote((o[1], 0), v, "none", False)
            elif o[0] == "i" and lo <= o[1] < hi:
                k = ins[o[1]] = ins.get(o[1], 0) + 1
                vote((o[1], k), v, oth[o[2]][0], oth[o[2]][1])
    # the voters (and C) covering an insertion slot without inserting there vote 'none'
    for key in [k for k in cols if k[1] > 0]:
        c = cols[key]
        c["v"]["none"] = c["v"].get("none", 0) + w["C"]
    return [cols[k] for k in sorted(cols)]


def column_options(c, nb):
    """-> list of (sym, logp, dot_opts, neighbour_only, weight); dot_opts [(dotted, logp)]."""
    tot = sum(c["v"].values())
    if tot <= 0:
        return [("?", 0.0, [(False, 0.0)], False, 0.0)]
    mass = dict(c["v"])
    nbm = {}
    for d, m in c["v"].items():
        for t in NEIGH.get(d, ()):
            nbm[t] = nbm.get(t, 0) + nb * m
    for t, m in nbm.items():
        mass[t] = mass.get(t, 0) + m
    Z = sum(mass.values())
    if c["dot"] > 0 and c["dcov"] > 0:
        pd = min(0.95, max(0.05, c["dot"] / c["dcov"]))
        dopts = [(True, math.log(pd)), (False, math.log(1 - pd))]
    else:
        dopts = [(False, 0.0)]
    out = []
    for s, m in mass.items():
        if m <= 0:
            continue
        nbonly = s != "none" and s not in c["v"]
        out.append((s, math.log(m / Z), dopts if s != "none" else [(False, 0.0)], nbonly, m / Z))
    return out


# ---------------------------------------------------------------- language and key model
def bigram():
    cnt, uni = {}, {}
    for p in glob.glob("../../tools/data/fr16/*.txt.gz"):
        txt = gzip.open(p, "rt", encoding="utf-8", errors="ignore").read().lower()
        for w_ in re.findall(r"[a-zà-ÿ]+", txt):
            w_ = "#" + re.sub(r"[^a-z]", "", M.norm(w_)) + "#"
            for a, b in zip(w_, w_[1:]):
                cnt[(a, b)] = cnt.get((a, b), 0) + 1
                uni[b] = uni.get(b, 0) + 1
    A = "#abcdefghilmnopqrstuxyz"
    lp, lu = {}, {}
    U = sum(uni.get(b, 0) + 1 for b in A)
    for b in A:
        lu[b] = math.log((uni.get(b, 0) + 1) / U)
    for a in A:
        row = sum(cnt.get((a, b), 0) + 0.5 for b in A)
        for b in A:
            lp[(a, b)] = math.log((cnt.get((a, b), 0) + 0.5) / row)
    return lp, lu


def dotted_prior():
    """Dotted word-code counts from aligned_dump.txt's glosses, excluding every dump group inside any calibration
    line's window (v2-anchored span +- 8), so no calibration line's answer enters the model."""
    toks = []
    for ln in open("aligned_dump.txt", encoding="utf-8"):
        if ln.startswith("#"):
            continue
        toks += ln.split()
    codes = [re.sub(r"\(.*$", "", t) for t in toks if t != "...."]  # the page's trailing ellipsis is not a group
    dump, spans = M.dump_spans()
    assert codes == dump, "aligned_dump.txt codes do not match aligned_dump_codes.txt"
    excl = set()
    for ln in LINES:
        js = spans[ln]
        excl |= set(range(max(0, js[0] - 8), min(len(dump), js[-1] + 9)))
    cnt = {}
    for j, c in enumerate(codes):
        if j not in excl and c.startswith("'") and c[1:].isdigit():
            cnt[c[1:]] = cnt.get(c[1:], 0) + 1
    return cnt, len(excl)


class Model:
    def __init__(self):
        key = M.load_key()
        freq = {"e": 14.7, "a": 8.1, "s": 7.9, "i": 7.2, "t": 7.2, "n": 7.1, "r": 6.5, "u": 6.3, "l": 5.5, "o": 5.3,
                "d": 3.7, "c": 3.3, "p": 3.0, "m": 2.9, "q": 1.4, "f": 1.1, "b": 0.9, "g": 0.9, "h": 0.7, "x": 0.4,
                "y": 0.3, "z": 0.1}
        by = {}
        for r in key:
            if r["sign"].isdigit():
                by.setdefault(r["value"].strip().lower(), []).append(r["sign"])
        self.code = {}
        for val, sg in by.items():
            for s in sg:
                self.code[s] = (M.norm(val), math.log(freq.get(val[:1], 0.5) / 100 / len(sg)))
        self.lp, self.lu = bigram()
        self.dcnt, self.nexcl = dotted_prior()
        self.dN = sum(self.dcnt.values())

    def group(self, piece, dotted, last, lam, mu):
        """score and new 'last' letter for one parsed group."""
        if dotted:
            if len(piece) != 2:
                return math.log(1e-6), "#"
            sc = math.log(0.01)
            if mu:
                p = (self.dcnt.get(piece, 0) + 0.5) / (self.dN + 50)
                sc += mu * math.log(p * 100)
            if lam:
                sc += lam * (self.lp[(last, "#")] - self.lu["#"])
            return sc, "#"
        if piece in self.code:
            val, sc = self.code[piece]
            if lam and val:
                sc += lam * (self.lp[(last, val[0])] - self.lu[val[0]])
            return sc, (val[-1] if val else "#")
        return (math.log(0.0005) if len(piece) == 2 else math.log(1e-6)), "#"


def decode(cols, P, lam, mu):
    """Viterbi over columns. State (pending first digit or None, last letter). Returns [(sym, dotted, nbonly, wt)]."""
    NEGINF = -1e18
    states = {(None, "#"): (0.0, None)}
    hist = []
    for c in cols:
        opts = column_options(c, P["nb"])
        new = {}

        def put(k, sc, bp):
            if sc > new.get(k, (NEGINF,))[0]:
                new[k] = (sc, bp)
        for (pend, last), (s, _) in states.items():
            for sym, lp_, dopts, nbo, wt in opts:
                if sym == "none":
                    put((pend, last), s + lp_, ((pend, last), None))
                    continue
                if sym == "?":
                    s2, l2 = s, last
                    if pend:
                        g, l2 = P["model"].group(pend[0], pend[1], last, lam, mu)
                        s2 += g
                    put((None, "#"), s2 + lp_, ((pend, last), ("?", False, False, 0.0)))
                    continue
                for dotted, ld in dopts:
                    em = (sym, dotted, nbo, wt)
                    base = s + lp_ + ld
                    if pend is None:
                        g, l2 = P["model"].group(sym, dotted, last, lam, mu)
                        put((None, l2), base + g, ((pend, last), em))
                        put(((sym, dotted), last), base, ((pend, last), em))
                    else:
                        if dotted:
                            continue  # a dot on the second digit of a pair is not a group form
                        g, l2 = P["model"].group(pend[0] + sym, pend[1], last, lam, mu)
                        put((None, l2), base + g, ((pend, last), em))
        hist.append(new)
        states = new
    best, bk = NEGINF, None
    for (pend, last), (s, _) in states.items():
        if pend:
            s += P["model"].group(pend[0], pend[1], last, lam, mu)[0]
        if s > best:
            best, bk = s, (pend, last)
    out = []
    for new in reversed(hist):
        sc, (pk, em) = new[bk]
        if em:
            out.append(em)
        bk = pk
    return out[::-1]


def to_text(path):
    return "".join(("'" if d and s != "?" else "") + s for s, d, _, _ in path)


def fast_score(texts, lines, margin=8):
    """digscore's statistic without its controls (for the tuning grid only; gates are read from digscore itself)."""
    viterbi = M.key_parser()
    dump, spans = M.dump_spans()
    tot = {"dig": 0, "bare": 0, "dotted": 0}
    hit = dict.fromkeys(tot, 0)
    for ln in lines:
        st = M.stream_of(texts[ln])
        dig = [None if c == "?" else c for c, _ in st]
        js, best = spans[ln], None
        for s in range(max(0, js[0] - margin), js[0] + margin + 1):
            for e in range(js[-1] - margin, min(len(dump) - 1, js[-1] + margin) + 1):
                if e <= s:
                    continue
                ref = dump[s:e + 1]
                rd = list(M.groups_stream(ref).replace("'", ""))
                v = M.lcs_len(dig, rd)
                k = (2 * v - len(rd), -abs(s - js[0]) - abs(e - js[-1]))
                if best is None or k > best[0]:
                    best = (k, ref, rd, v)
        _, ref, rd, v = best
        groups, _ = M.parse_stream(st, viterbi)
        h, t = M.summarize(M.lcs_pairs(groups, ref), ref)
        hit["dig"] += v
        tot["dig"] += len(rd)
        for k in ("bare", "dotted"):
            hit[k] += h[k]
            tot[k] += t[k]
    return {k: hit[k] / tot[k] for k in tot}, hit, tot


def run_setting(streams, model, S, lines, shuffle_rng=None):
    texts, logs = {}, []
    for ln in lines:
        cols = build_columns(streams, ln, S["w"])
        if shuffle_rng is not None:
            cols = shuffle_cols(cols, shuffle_rng)
        path = decode(cols, {"nb": S["nb"], "model": model}, S["lam"], S["mu"])
        texts[ln] = to_text(path)
        for k, (s, d, nbo, wt) in enumerate(path):
            if nbo:
                logs.append((ln, k + 1, s, round(wt, 4)))
    return texts, logs


def shuffle_cols(cols, rng):
    """Control (i): each column's vote vector is replaced by a random column's (same line), its values assigned to
    this column's own candidates in random order; candidate sets, coverage and dot marks stay where they were."""
    vecs = [sorted(c["v"].values(), reverse=True) for c in cols if c["v"]]
    out = []
    for c in cols:
        if not c["v"]:
            out.append(c)
            continue
        vec = rng.choice(vecs)
        keys = list(c["v"])
        rng.shuffle(keys)
        vals = (vec + [min(vec)] * len(keys))[:len(keys)]
        c2 = dict(c)
        c2["v"] = dict(zip(keys, vals))
        out.append(c2)
    return out


def write_tsv(path, texts):
    with open(path, "w", encoding="utf-8") as f:
        f.write("line\tdigits_with_marks\tconfidence\n")
        for ln in LINES:
            if ln in texts:
                f.write(f"{ln}\t{texts[ln]}\tlattice\n")


def grid():
    for wA in (0, 0.5, 1.0):
        for wB in (0, 0.3, 0.6):
            for wP in (0, 0.15, 0.3):
                yield {"w": {"C": 1.0, "A": wA, "B": wB, "PA": wP, "PB": wP, "V2": wP}, "nb": 0.1, "lam": 0.5,
                       "mu": 1.0}


def tune():
    os.makedirs(OUT, exist_ok=True)
    streams, model = voter_streams(), Model()
    rows = []

    def ev(S):
        texts, logs = run_setting(streams, model, S, TUNED)
        r, _, _ = fast_score(texts, TUNED)
        rows.append((json.dumps(S, sort_keys=True), r["dig"], r["bare"], r["dotted"], len(logs)))
        print(f"{r['dig']:.3f} {r['bare']:.3f} {r['dotted']:.3f} nb-chosen {len(logs)}  {json.dumps(S, sort_keys=True)}",
              flush=True)
        return r["dig"] + r["bare"] + r["dotted"]

    best = max(grid(), key=ev)  # stage 1: voter weights at nb 0.1, lambda 0.5, mu 1
    stage2 = []
    for nb in (0.0, 0.1, 0.3):
        for lam in (0.0, 0.5, 1.0):
            for mu in (0.0, 1.0):
                stage2.append({**best, "nb": nb, "lam": lam, "mu": mu})
    best = max(stage2, key=ev)  # ties keep the first (smallest nb, lambda, mu)
    with open(OUT + "tune.tsv", "w") as f:
        f.write("setting\tG0\tG1\tG2\tneighbour_chosen\n")
        for r in rows:
            f.write("\t".join(str(x) if not isinstance(x, float) else f"{x:.4f}" for x in r) + "\n")
    json.dump(best, open(OUT + "chosen.json", "w"), sort_keys=True, indent=1)
    print("CHOSEN", json.dumps(best, sort_keys=True))


def run():
    streams, model = voter_streams(), Model()
    S = json.load(open(OUT + "chosen.json"))
    texts, logs = run_setting(streams, model, S, LINES)
    write_tsv(OUT + "lattice.tsv", texts)
    with open(OUT + "neighbours.tsv", "w") as f:
        f.write("line\tlattice_pos\tdigit\tweight_share\n")
        for r in logs:
            f.write("\t".join(map(str, r)) + "\n")
    rng = random.Random(1)
    for i in range(1, 6):
        t2, _ = run_setting(streams, model, S, LINES, shuffle_rng=rng)
        write_tsv(OUT + f"shuffle_{i}.tsv", t2)
    print(f"dotted prior: {model.dN} dotted groups, {len(model.dcnt)} codes, {model.nexcl} dump groups excluded")
    print(f"neighbour-chosen positions: {len(logs)}")
    for ln in LINES:
        print(ln, texts[ln])


if __name__ == "__main__":
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    {"tune": tune, "run": run}[sys.argv[1]]()
