#!/usr/bin/env python3
"""N9-MANT (5 Oct 2026): n-gram duplicate search of the Loc. 694/08 pool against f.409r / f.409v / f.410 (PREREG-N9-MANT.md).

Disk only. Usage: python3 n9mant/pool_ngrams.py [--check]   (run from the target folder or anywhere; paths are relative to this file)
Writes n9mant/hits.tsv, n9mant/spans.tsv, n9mant/control.tsv; --check exits 1 if the committed outputs differ from a fresh run.
"""
import csv, random, re, sys, io, os
from pathlib import Path

T = Path(__file__).resolve().parent.parent
OUT = T / "n9mant"
NUM = re.compile(r"^\d+$")

def norm(g):
    g = g.strip().strip("[]{}()?").lower()
    if g == "bir":
        return "612"            # RUN4-MANT cross-witness (I)
    return g if NUM.match(g) else None   # anything not a plain group = break

def segs_from_codes(seq_of_strings):
    """list of code strings (space- or dot-separated) -> list of segments (lists), unreadable groups break a segment"""
    out = []
    for s in seq_of_strings:
        cur = []
        for g in re.split(r"[\s.]+", s.strip()):
            if not g:
                continue
            n = norm(g)
            if n is None:
                if cur: out.append(cur); cur = []
            else:
                cur.append(n)
        if cur: out.append(cur)
    return out

def rows(path, skip_hash=True):
    with open(path, newline="") as f:
        lines = [l for l in f if not (skip_hash and l.startswith("#"))]
    return list(csv.DictReader(io.StringIO("".join(lines)), delimiter="\t"))

def query_streams():
    ct = rows(T / "ciphertext.tsv")
    by = {}
    for r in ct:
        by.setdefault(r["line"], []).append((int(r["pos"]), r["sign"]))
    def leaf(prefixes):
        segs = []
        for line in sorted(by):
            if any(line.startswith(p) for p in prefixes):
                segs += segs_from_codes([" ".join(s for _, s in sorted(by[line]))])
        return segs
    f409r = segs_from_codes([r["orig_codes"] for r in rows(T / "f0500_0502/witness_matched_runs_mant3.tsv") if r["orig_leaf_line"].startswith("f409r")])
    f409r += segs_from_codes([r["f409r_or_f409v"][len("f409r "):] for r in rows(T / "f0501/witness_matched_runs_mant2.tsv") if r["f409r_or_f409v"].startswith("f409r ")])
    f409r += leaf(["694-08_0510"])
    return {"f409r": f409r, "f409v": leaf(["694-08_0511_f409v"]), "f410": leaf(["694-08_0511_f410"])}

def pool_streams():
    P = {}
    P["0500"] = segs_from_codes([r["codes"] for r in rows(T / "f0500_0502/reconciled_mant4.tsv") if r["frame"] == "0500"])
    P["0502"] = segs_from_codes([r["codes"] for r in rows(T / "f0500_0502/reconciled_mant4.tsv") if r["frame"] == "0502"])
    P["0501"] = segs_from_codes([r["codes"] for r in rows(T / "f0501/reconciled.tsv")])
    P["0528"] = segs_from_codes([r["codes"] for r in rows(T / "f423_0528/reconciled.tsv")])
    P["0527"] = segs_from_codes([r["codes"] for r in rows(T / "f422v_0527/reconciled.tsv")])   # D2B-MANT27, 5 Oct 2026
    P["0579_f467"] = segs_from_codes([r["code_groups"] for r in rows(T / "f467/passA.tsv") if r.get("code_groups")])
    f468 = [l.rstrip("\n").split("\t") for l in open(T / "f468/passes.tsv") if not l.startswith("#")]
    P["0580_f468"] = segs_from_codes([" ".join(r[4] for r in f468 if len(r) > 4)])
    for r in rows(T / "frame_rank_gaps189.tsv"):
        if r["frame"] != "0528":
            P[r["frame"] + "_eyeM"] = segs_from_codes(r["codes_seen_eye_M"].split(";"))
    for r in rows(T / "frame_classify_gaps207.tsv"):
        if r["frame"] not in ("0501", "0528"):
            P[r["frame"] + "_eyeM"] = segs_from_codes(re.findall(r"\d+(?:\.\d+)+", r["code_range"]))
    return P

def grams(segs, n):
    out = []
    for si, s in enumerate(segs):
        for i in range(len(s) - n + 1):
            out.append((tuple(s[i:i + n]), si, i))
    return out

def shared(q, p, n):
    pset = {}
    for g, si, i in grams(p, n):
        pset.setdefault(g, []).append((si, i))
    return [(g, qsi, qi, pset[g]) for g, qsi, qi in grams(q, n) if g in pset]

def count(q, p):
    return len({h[0] for h in shared(q, p, 4)}), len({h[0] for h in shared(q, p, 6)})

def spans(q, p, n=4):
    """maximal common contiguous runs >= n, as (q seg, q start, p seg, p start, length)"""
    res = []
    for qsi, qs in enumerate(q):
        for psi, ps in enumerate(p):
            for i in range(len(qs)):
                for j in range(len(ps)):
                    if (i and j and qs[i - 1] == ps[j - 1]):
                        continue
                    L = 0
                    while i + L < len(qs) and j + L < len(ps) and qs[i + L] == ps[j + L]:
                        L += 1
                    if L >= n:
                        res.append((qsi, i, psi, j, L, " ".join(qs[i:i + L])))
    return res

def main():
    Q, P = query_streams(), pool_streams()
    # internal: query leaves against each other
    allP = dict(P)
    for k in ("f409v", "f410"):
        allP["Q_" + k] = Q[k]
    hits, span_rows, ctrl = [], [], []
    rng = random.Random(9409)
    for qn, q in Q.items():
        flat = [g for s in q for g in s]
        draws = []
        for _ in range(200):
            sh = flat[:]; rng.shuffle(sh)
            draws.append([sh])
        for pn, p in allP.items():
            if pn == "Q_" + qn:
                continue
            c4, c6 = count(q, p)
            sp = spans(q, p)
            in_order = sum(1 for s in sp if s[4] >= 6)
            cs = [count(d, p) for d in draws]
            m4 = sum(c[0] for c in cs) / 200; x4 = max(c[0] for c in cs)
            m6 = sum(c[1] for c in cs) / 200; x6 = max(c[1] for c in cs)
            dup = "DUPLICATE" if (c6 >= 2 and c6 > x6) else ("4-gram only" if c4 > x4 else "-")
            hits.append([qn, pn, sum(map(len, q)), sum(map(len, p)), c4, c6, len(sp), max([s[4] for s in sp], default=0), dup])
            ctrl.append([qn, pn, f"{m4:.3f}", x4, f"{m6:.3f}", x6])
            for s in sp:
                span_rows.append([qn, pn, s[0], s[1], s[2], s[3], s[4], s[5]])
    outs = {}
    def w(name, head, data):
        f = io.StringIO()
        wr = csv.writer(f, delimiter="\t", lineterminator="\n"); wr.writerow(head); wr.writerows(data)
        outs[name] = f.getvalue()
    w("hits.tsv", ["query", "pool_leaf", "q_groups", "p_groups", "shared_4grams", "shared_6grams", "spans_ge4", "longest_span", "verdict"], hits)
    w("spans.tsv", ["query", "pool_leaf", "q_seg", "q_start", "p_seg", "p_start", "length", "codes"], span_rows)
    w("control.tsv", ["query", "pool_leaf", "shuf_mean_4", "shuf_max_4", "shuf_mean_6", "shuf_max_6"], ctrl)
    if "--check" in sys.argv:
        stale = [n for n, v in outs.items() if not (OUT / n).exists() or (OUT / n).read_text() != v]
        print("STALE: " + " ".join(stale) if stale else "OK: n9mant outputs reproduce")
        sys.exit(1 if stale else 0)
    for n, v in outs.items():
        (OUT / n).write_text(v)
    for h in hits:
        print("\t".join(map(str, h)))

if __name__ == "__main__":
    main()
