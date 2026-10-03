#!/usr/bin/env python3
"""GAPS69 (3 Oct 2026): is a period-P design (P alphabets in rotation) plausible for the R4282 stream?
design_prior.py's statistics are unigram and label-free, so they cannot see periodicity. Two label-free coset
statistics, each against 2000 random permutations of the same stream (a permutation destroys position-phase
structure but keeps the counts, so the control CAN differ from the target on this axis, rule 3):
  dIC  = mean index of coincidence over the P cosets minus the whole-stream IC (polyalphabetic: > 0, inflated)
  TVD  = mean pairwise total-variation distance between coset distributions (different alphabets: large)
Positional phase runs continuously over the stream (the periodic_masc default, continuous=1).
Writes period_test.tsv; --check re-computes and exits 1 if the committed file is stale."""
import csv, random, sys, os
from collections import Counter
from itertools import combinations
H = os.path.dirname(os.path.abspath(__file__))
seq = open(os.path.join(H, "stream_tokens.txt")).read().split()

def ic(s):
    c = Counter(s); n = len(s)
    return sum(v*(v-1) for v in c.values())/(n*(n-1))

def stats(s, P):
    cos = [s[i::P] for i in range(P)]
    dic = sum(ic(c) for c in cos)/P - ic(s)
    tv = []
    for a, b in combinations(cos, 2):
        ca, cb = Counter(a), Counter(b)
        keys = sorted(set(ca) | set(cb))
        tv.append(0.5*sum(abs(ca[k]/len(a) - cb[k]/len(b)) for k in keys))
    return dic, sum(tv)/len(tv)

def positive(P, w):
    """Positive control (power): a la17 window of the target's N enciphered under P independent random keys
    over a K-sign inventory, then a share 0.034 of tokens redrawn (the measured two-reader error)."""
    sys.path.insert(0, os.path.join(H, "..", "..", "..", "tools"))
    import judge_plaintext as jp
    text = jp.fold("".join(jp.read_corpus(p) for p in jp.LANG_CORPORA["la17"]))
    r = random.Random(1000 + w)
    st = r.randrange(len(text)//20, len(text)*19//20 - len(seq))
    plain = text[st:st + len(seq)]
    letters = sorted(set(plain))
    keys = []
    for c in range(P):
        sg = list(range(34)); r.shuffle(sg); keys.append(dict(zip(letters, sg)))
    ct = [keys[i % P][a] for i, a in enumerate(plain)]
    return [r.choice(ct) if r.random() < 0.034 else x for x in ct]

rows = []
rng = random.Random(69)
streams = [("target", seq)] + [(f"posctl{w}", None) for w in range(1, 4)]
for name, base in streams:
  for P in range(2, 9) if name == "target" else (2,):
    s0 = base if base is not None else positive(P, int(name[-1]))
    d0, t0 = stats(s0, P)
    nd = nt = 0; dl = []; tl = []
    for _ in range(2000):
        s = s0[:]; rng.shuffle(s)
        d, t = stats(s, P); dl.append(d); tl.append(t)
        nd += d >= d0; nt += t >= t0
    dl.sort(); tl.sort()
    rows.append([name, P, f"{d0:.5f}", f"{dl[1899]:.5f}", f"{(nd+1)/2001:.4f}", f"{t0:.4f}", f"{tl[1899]:.4f}", f"{(nt+1)/2001:.4f}"])
# line-reset phase variant (key restarts at every line of the reconciled TSV), P=2, target only
import csv as _csv
_rows = [r for r in _csv.DictReader(open(os.path.join(H, "..", "tx2", "ciphertext_reconciled.tsv")), delimiter="\t")
         if r["sign"] not in ("DOT", "COL")]
assert [r["sign"] for r in _rows] == seq
_ph, _prev, _i = [], None, 0
for r in _rows:
    if r["line"] != _prev:
        _i, _prev = 0, r["line"]
    _ph.append(_i % 2); _i += 1

def _tv_phase(s):
    a = [x for x, p in zip(s, _ph) if p == 0]; b = [x for x, p in zip(s, _ph) if p == 1]
    ca, cb = Counter(a), Counter(b)
    return 0.5*sum(abs(ca[k]/len(a) - cb[k]/len(b)) for k in sorted(set(ca) | set(cb)))
t0 = _tv_phase(seq); tl = []; nt = 0
for _ in range(2000):
    s = seq[:]; rng.shuffle(s); t = _tv_phase(s); tl.append(t); nt += t >= t0
tl.sort()
rows.append(["target_line_reset", 2, "-", "-", "-", f"{t0:.4f}", f"{tl[1899]:.4f}", f"{(nt+1)/2001:.4f}"])
hdr = ["stream", "period", "dIC_target", "dIC_perm_p95", "dIC_p", "TVD_target", "TVD_perm_p95", "TVD_p"]
out = os.path.join(H, "period_test.tsv")
txt = "\t".join(hdr) + "\n" + "".join("\t".join(map(str, r)) + "\n" for r in rows)
if "--check" in sys.argv:
    sys.exit(0 if open(out).read() == txt else 1)
open(out, "w").write(txt); print(txt)
