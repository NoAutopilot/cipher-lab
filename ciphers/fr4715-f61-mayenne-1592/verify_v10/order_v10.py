#!/usr/bin/env python3
"""VERIFY-F61-V10 (29 Sept 2026, verifier session_01BBihDVXNJZJwuUvhLshzw4): an independent re-implementation of runner 13's within-run order
statistic (H342/H344/H346/H350/H351/H349), written and committed BEFORE any run. Shares no scoring code with family/h3xx_*.py or
tools/partial_key_test.py: its own letter model, its own exact decoder, its own seeds. Inputs taken as committed: the reconciled sign drafts
family/passes/<leaf>/ciphertext_draft.tsv and key v7 through build_key_v7.load_key_v7 (the key's own loader; EBR_A form A, EBR_B form B).

Statistic (the runner's definition, re-coded):
  runs  = maximal stretches of consecutive keyed signs within one draft line, length >= 4 (any unkeyed / PLAIN / DASH / OTHER sign breaks a run).
  S(K, runs) = sum over runs of the best letter path through the run's cells (exact Viterbi over last-3-letter states), scored by MY
          interpolated letter 4-gram model of tools/data/fr16 (folded j->i, v->u, y->i; lambdas .55/.25/.12/.06/.02 over 4/3/2/1-gram and
          uniform; every letter of a run scored, first letters by the lower orders), divided by the letters scored.
  gain(K) = S(K, real runs) - mean over 10 within-run shuffles (each run's signs permuted in place; seed 10010, the same shuffles for every key).
  null keys = 100 keys with v7's cells permuted within bins of 3 keyed classes adjacent in the leaf's own token rank (seed 10020).
  'order signal' on a leaf iff gain(v7) > the 95th percentile (index 94 of 100 sorted) of the null keys' gains.

Controls and gates (fixed here, before running):
  (a) in-sample positive control: f.101r and f.188r (leaves key v7 was built from) must both show 'order signal', else every held-leaf line is
      'not tested'.
  (b) shuffled-order null that CAN differ on this statistic: 10 targets per leaf with the keyed signs permuted across ALL keyed positions of the
      leaf (run cuts and sign frequencies fixed, order destroyed; seed 10030), 40 null keys each. The design is valid on a leaf iff at most 2/10
      shuffled targets show 'order signal' (5% expected); a leaf failing this is VOID whatever its real result.
  (c) the frequency-bin permuted keys are the null in the statistic itself (above); also reported: bins of 2 (tighter frequency match, seed
      10040, 100 keys) on the held leaves, same 95% rule.
  (d) power (ARM3-ADJ): 20 random subsets of runs (without replacement, seed 10050) of each in-sample leaf, sized to each held leaf's own run
      count where the in-sample leaf is long enough, 40 null keys per subset; power = share with 'order signal'. Plus the held leaves f.124r and
      f.97r subsampled to 51 runs (f.106r's count), the runner's H351 question. A held-leaf miss is a negative only if in-sample power at its N
      >= 0.80 AND held-leaf power at its N >= 0.80; else 'untestable at this N'.
  (e) contamination check (found in reading the notes, before running): VBAR_A's g/t was chosen over v4's s/t partly by a sequence-gain test
      on a pool that included f.97r and f.124r (H146/H151, 28 Sept). So f.124r / f.97r are not fully held for VBAR_A. Re-run the held-leaf test
      with VBAR_A = s/t (v4's cell): if the signal survives, the contamination does not carry it.
  (f) per class, size-matched (H349/H355): for HASH4, C43, H24, ZBAR on f.124r, f.97r and in-sample f.101r, f.188r: v7's cell vs 40 random
      cells of the same size (letters drawn by fr16 frequency without replacement, v7's own cell excluded; seed 10060), everything else v7;
      share of alternatives v7 beats (strictly). 'supported' iff >= 0.95. Misses read as information only where both in-sample leaves pass.
Rule 10 / rule 4: set-level evidence about key v7's cells; no letter on f.61 is read or graded here; no cell is changed.
  python3 order_v10.py [--part a|b|d|e|f|all] [--check]   (results in order_v10_<part>_result.txt)"""
import csv, gzip, glob, math, os, random, sys
from collections import Counter
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.abspath(f"{HERE}/.."); F = f"{T}/family"; ROOT = os.path.abspath(f"{T}/../..")
sys.path.insert(0, F)
FOLD = str.maketrans("jvy", "iui"); ALPHA = "abcdefghiklmnopqrstuwxz"
IN_SAMPLE = ("recf101r", "recf188r")
HELD = ("recf124r", "recf97r", "rec108v", "recf108vg", "recf108vagree", "recf106rall18")
# ---- letter model -----------------------------------------------------------------------------------------------------------------------
def build_lm():
    txt = []
    for f in sorted(glob.glob(f"{ROOT}/tools/data/fr16/*.txt.gz")):
        import unicodedata
        t = gzip.open(f, "rt", errors="ignore").read()
        t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower().translate(FOLD)
        txt.append("".join(ch for ch in t if ch in ALPHA))
    s = "".join(txt); C = [Counter() for _ in range(5)]
    for n in range(1, 5):
        for i in range(len(s) - n + 1): C[n][s[i:i + n]] += 1
    return C, len(s)
C, NTOT = build_lm(); LAM = (0.55, 0.25, 0.12, 0.06, 0.02); _cache = {}
def lp(h, ch):
    """log10 P(ch | h), h up to 3 letters, interpolated."""
    k = h + ch
    if k in _cache: return _cache[k]
    p = LAM[4] / len(ALPHA) + LAM[3] * C[1][ch] / NTOT
    ws = LAM[:3][::-1]   # weights for 2-,3-,4-gram: .12,.25,.55
    for n, w in zip((1, 2, 3), ws):
        if len(h) >= n:
            ctx = h[-n:]; d = C[n][ctx]
            if d: p += w * C[n + 1][ctx + ch] / d
    v = math.log10(p); _cache[k] = v; return v
for a in ALPHA:   # warm the unigram/short-context cache
    lp("", a)
# ---- decoder ----------------------------------------------------------------------------------------------------------------------------
def viterbi(sets):
    st = {"": 0.0}
    for S in sets:
        nb = {}
        for h, v in st.items():
            for ch in S:
                w = v + lp(h, ch); t = (h + ch)[-3:]
                if w > nb.get(t, -1e18): nb[t] = w
        st = nb
    return max(st.values())
def S(key, runs):
    tot = n = 0
    for r in runs:
        tot += viterbi([key[c] for c in r]); n += len(r)
    return tot / n
# ---- data -------------------------------------------------------------------------------------------------------------------------------
import build_key_v7 as bk
KB, KA = bk.load_key_v7(ebr="B"), bk.load_key_v7(ebr="A")
def v7cell(c):
    v = KA["EBR"] if c == "EBR_A" else KB["EBR"] if c == "EBR_B" else KB.get(c, ())
    return tuple(sorted({x.translate(FOLD) for x in v}))
def leafdata(prefix):
    rows = list(csv.DictReader((l for l in open(f"{F}/passes/{prefix}/ciphertext_draft.tsv") if not l.startswith("#")), delimiter="\t"))
    keyed = lambda s: bool(v7cell(s))
    runs, cur, last = [], [], None
    for r in rows:
        if r["line"] != last or not keyed(r["sign"]):
            if len(cur) >= 4: runs.append(cur)
            cur = []
        if keyed(r["sign"]): cur.append(r["sign"])
        last = r["line"]
    if len(cur) >= 4: runs.append(cur)
    cnt = Counter(s for r in runs for s in r)
    classes = sorted(cnt, key=lambda c: (-cnt[c], c))
    return runs, classes
def shuffles(runs, seed, k=10):
    rng = random.Random(seed); out = []
    for _ in range(k):
        s = []
        for r in runs: r2 = r[:]; rng.shuffle(r2); s.append(r2)
        out.append(s)
    return out
def gain(key, runs, shuf):
    return S(key, runs) - sum(S(key, s) for s in shuf) / len(shuf)
def binned_keys(base, classes, n, seed, width=3):
    rng = random.Random(seed); bins = [classes[i:i + width] for i in range(0, len(classes), width)]; out = []
    for _ in range(n):
        mp = dict(base)
        for bn in bins:
            cs = [base[c] for c in bn]; rng.shuffle(cs); mp.update(zip(bn, cs))
        out.append(mp)
    return out
def test(args):
    """one (key, runs) evaluation: returns gain(v7-like base) and the null gains"""
    base, runs, classes, nnull, seed, width, shufseed = args
    sh = shuffles(runs, shufseed)
    gv = gain(base, runs, sh)
    null = sorted(gain(k, runs, sh) for k in binned_keys(base, classes, nnull, seed, width))
    p95 = null[int(round(0.95 * nnull)) - 1] if nnull >= 20 else max(null)
    return gv, p95, sum(x >= gv for x in null), sum(null) / len(null)
def basekey(classes, override=None):
    k = {c: v7cell(c) for c in classes}
    if override: k.update(override)
    return k
def fmt(tag, runs, r, n):
    gv, p95, ge, mean = r
    return f"{tag}: runs {len(runs)}, signs {sum(map(len, runs))}; gain(v7) {gv:.4f}; null mean {mean:.4f} p95 {p95:.4f}, >= v7 {ge}/{n} -> {'order signal' if gv > p95 else 'no order signal'}"
# ---- parts ------------------------------------------------------------------------------------------------------------------------------
def part_a(pool):
    out = ["(a)+(c) real drafts, bins of 3, 100 null keys (seed 10020), 10 within-run shuffles (seed 10010)"]
    jobs, tags = [], []
    for p in IN_SAMPLE + HELD:
        runs, cl = leafdata(p); jobs.append((basekey(cl), runs, cl, 100, 10020, 3, 10010)); tags.append((p, runs))
    for p in HELD[:2] + HELD[5:]:
        runs, cl = leafdata(p); jobs.append((basekey(cl), runs, cl, 100, 10040, 2, 10010)); tags.append((p + " [bins of 2]", runs))
    res = pool.map(test, jobs); sig = {}
    for (t, runs), r in zip(tags, res):
        out.append(fmt(t, runs, r, 100)); sig[t] = r[0] > r[1]
    ctl = sig["recf101r"] and sig["recf188r"]
    out.append("(a) positive control in-sample f.101r and f.188r: " + ("PASS" if ctl else "FAIL -- held-leaf lines 'not tested'"))
    return out
def part_b(pool):
    out = ["(b) shuffled-order targets: keyed signs permuted across all keyed positions of the leaf (seed 10030), 10 targets, 40 null keys each"]
    for p in IN_SAMPLE + HELD:
        runs, cl = leafdata(p); rng = random.Random(10030); jobs = []
        for t in range(10):
            flat = [s for r in runs for s in r]; rng.shuffle(flat); it = iter(flat); sr = [[next(it) for _ in r] for r in runs]
            jobs.append((basekey(cl), sr, cl, 40, 10020 + t, 3, 10010))
        res = pool.map(test, jobs); fp = sum(r[0] > r[1] for r in res)
        out.append(f"{p}: shuffled targets with 'order signal' {fp}/10 (gains {' '.join(f'{r[0]:.3f}' for r in res)}) -> "
                   + ("design valid on this leaf" if fp <= 2 else "VOID on this leaf"))
    return out
def part_d(pool):
    out = ["(d) power: 20 random run subsets (seed 10050), 40 null keys each; power = share with 'order signal'"]
    sizes = {"recf124r": 227, "recf97r": 203, "recf106rall18": 51, "rec108v": 19, "recf108vg": 8, "recf108vagree": 8}
    for p in IN_SAMPLE + ("recf124r", "recf97r"):
        runs, cl = leafdata(p)
        for tgt, n in sizes.items():
            if p in ("recf124r", "recf97r") and n != 51: continue
            if n >= len(runs): continue
            rng = random.Random(10050 + n); jobs = []
            for i in range(20):
                sub = rng.sample(runs, n); jobs.append((basekey(cl), sub, cl, 40, 10500 + i, 3, 10010))
            res = pool.map(test, jobs); pw = sum(r[0] > r[1] for r in res) / 20
            out.append(f"{p} subsampled to {n} runs ({tgt}'s count): power {pw:.2f}")
    return out
def part_e(pool):
    out = ["(e) VBAR_A contamination check: VBAR_A = s/t (v4's cell) instead of v7's g/t, bins of 3, 100 null keys (the null permutes this key)"]
    jobs, tags = [], []
    for p in ("recf124r", "recf97r") + IN_SAMPLE:
        runs, cl = leafdata(p); jobs.append((basekey(cl, {"VBAR_A": ("s", "t")}), runs, cl, 100, 10020, 3, 10010)); tags.append((p, runs))
    for (t, runs), r in zip(tags, pool.map(test, jobs)): out.append(fmt(t + " VBAR_A=s/t", runs, r, 100))
    return out
LF = None
def alt_cells(cell, n, seed):
    global LF
    if LF is None: LF = {a: C[1][a] for a in ALPHA}
    rng = random.Random(seed); out = set(); tries = 0
    while len(out) < n and tries < 5000:
        tries += 1; pool = dict(LF); s = []
        for _ in range(len(cell)):
            tot = sum(pool.values()); x = rng.random() * tot
            for a, w in pool.items():
                x -= w
                if x <= 0: break
            s.append(a); del pool[a]
        t = tuple(sorted(s))
        if t != tuple(cell): out.add(t)
    return sorted(out)
def perclass(args):
    p, cls, seed = args
    runs, cl = leafdata(p); sh = shuffles(runs, 10010)
    if cls not in cl: return p, cls, None, 0
    base = basekey(cl); gv = gain(base, runs, sh); alts = alt_cells(base[cls], 40, seed)
    ga = [gain(dict(base, **{cls: a}), runs, sh) for a in alts]
    return p, cls, sum(gv > g for g in ga) / len(ga), sum(map(lambda r: r.count(cls), runs))
def part_f(pool):
    out = ["(f) per class, size-matched: v7's cell vs 40 fr16-frequency-drawn cells of the same size (seed 10060); share beaten; supported iff >= 0.95"]
    jobs = [(p, c, 10060 + i) for p in ("recf124r", "recf97r") + IN_SAMPLE for i, c in enumerate(("HASH4", "C43", "H24", "ZBAR"))]
    for p, c, sh, n in pool.map(perclass, jobs):
        out.append(f"{p} {c} ({n} signs in runs): " + ("absent" if sh is None else f"share beaten {sh:.2f} -> {'supported' if sh >= 0.95 else 'not supported'}"))
    return out
PARTS = {"a": part_a, "b": part_b, "d": part_d, "e": part_e, "f": part_f}
if __name__ == "__main__":
    args = sys.argv[1:]; part = args[args.index("--part") + 1] if "--part" in args else "all"
    todo = list(PARTS) if part == "all" else [part]
    with Pool(4) as pool:
        for k in todo:
            txt = "\n".join(PARTS[k](pool)) + "\n"; rs = f"{HERE}/order_v10_{k}_result.txt"
            if "--check" in args:
                ok = os.path.exists(rs) and open(rs).read() == txt; print(k, "check", "OK" if ok else "STALE")
                if not ok: sys.exit(1)
                continue
            open(rs, "w").write(txt); print(txt, end="", flush=True)
