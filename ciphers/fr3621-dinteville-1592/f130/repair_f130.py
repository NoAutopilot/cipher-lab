#!/usr/bin/env python3
"""f.130r key repair (pre-registered in NOTES.md, A2-DIN3, 3 Oct 2026, before scoring).

  python3 ciphers/fr3621-dinteville-1592/f130/repair_f130.py           write f130/repair/* outputs
  python3 ciphers/fr3621-dinteville-1592/f130/repair_f130.py --check   exit 1 if the committed outputs are stale

Free rows (v', 0', the two NEW signs, and key_syl rows with agree < 3) are hill-climbed (coordinate ascent over the 26
letters, max 8 sweeps) on the fr16 4-gram statistic of score_f130.py, over f.130 + the f.128 cipher signs. Held-out
check: a free row's repaired value must be one of the letters f128/align_syl.tsv aligns to that sign (where it aligns
any), else it reverts to its key_syl value. Control: the same climb + rejection from 1000 shuffled seed keys
(seed 20261003). Stability: 20 random-start climbs of the real key (seed 20261004).
"""
import csv, json, math, random, sys
from collections import Counter, defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
TGT = HERE.parent
ROOT = HERE.parents[2]
OUT = HERE / "repair"
sys.path.insert(0, str(ROOT / "tools"))
from judge_plaintext import NgramModel, read_corpus  # noqa: E402

SEED, NSHUF, SEED_STAB, NSTAB, MAXSWEEP = 20261003, 1000, 20261004, 20, 8
FREE = ["v'", "0'", "NEW:e-hook", "NEW:N-like", "zh", "D", "o", "1", "c", "9", "r", "plus", "div", "T", "h", "B", "n"]
AZ = "abcdefghijklmnopqrstuvwxyz"


def load_key():
    key = {}
    for r in csv.DictReader(open(TGT / "f128" / "key_syl.tsv"), delimiter="\t"):
        n, a = int(r["n"]), int(r["agree"])
        key[r["sign"]] = (r["meaning"], a, n)
    return key


def gloss_letters():
    g = defaultdict(Counter)
    for r in csv.DictReader(open(TGT / "f128" / "align_syl.tsv"), delimiter="\t"):
        for ch in r["plain_chunk"]:
            if ch in AZ:
                g[r["sign"]][ch] += 1
    return g


def texts():
    ct = list(csv.DictReader(open(HERE / "ciphertext.tsv"), delimiter="\t"))
    f128 = []
    for r in csv.DictReader(open(TGT / "f128" / "gloss_pairs.tsv"), delimiter="\t"):
        if r["signs"].strip():
            f128.append([s for s in r["signs"].split()])
    return ct, f128


def build_windows(ct, f128, keyed, sid):
    seqs, cur = [], []
    def brk():
        if cur:
            seqs.append(cur[:])
        cur.clear()
    for r in ct:
        s = r["sign"]
        if s.startswith("CLEAR:") or s not in keyed:
            brk()
        else:
            cur.append(sid[s])
    brk()
    for seg in f128:
        for s in seg:
            if s not in keyed:
                brk()
            else:
                cur.append(sid[s])
        brk()
    return [tuple(seq[i:i + 4]) for seq in seqs for i in range(len(seq) - 3)]


def table(model):
    """flat list: index a*17576 + b*676 + c*26 + d -> log10 P(d | abc), add-k as NgramModel.score."""
    k = model.k; T = []
    for a in AZ:
        for b in AZ:
            for c in AZ:
                ctx = model.ctx.get(a + b + c, 0); den = math.log10(ctx + 26 * k)
                for d in AZ:
                    T.append(math.log10(model.c.get(a + b + c + d, 0) + k) - den)
    return T


def wscore(T, w, val):
    return T[val[w[0]] * 17576 + val[w[1]] * 676 + val[w[2]] * 26 + val[w[3]]]


def score(T, W, val):
    return sum(wscore(T, w, val) for w in W) / len(W)


def climb(T, W, val, free_ids, touch):
    """coordinate ascent; only the windows touching the changed sign are rescored (sum is exact, not approximate)."""
    val = list(val); tot = sum(wscore(T, w, val) for w in W)
    for _ in range(MAXSWEEP):
        changed = False
        for f in free_ids:
            ws = touch[f]
            if not ws:
                continue
            old = val[f]; cur = sum(wscore(T, w, val) for w in ws); bl, bd = old, 0.0
            for x in range(26):
                if x == old:
                    continue
                val[f] = x; d = sum(wscore(T, w, val) for w in ws) - cur
                if d > bd + 1e-12:
                    bl, bd = x, d
            val[f] = bl
            if bl != old:
                changed = True; tot += bd
        if not changed:
            break
    return val, score(T, W, val)


def reject(val, base, free_ids, signs, gl):
    val = list(val); rej = []
    for f in free_ids:
        s = signs[f]
        if gl.get(s) and AZ[val[f]] not in gl[s]:
            rej.append((s, AZ[val[f]], sum(gl[s].values())))
            val[f] = base[f]
    return val, rej


def build():
    key = load_key(); gl = gloss_letters(); ct, f128 = texts()
    signs = sorted(set(key) | set(FREE))
    sid = {s: i for i, s in enumerate(signs)}
    keyed = set(signs)
    W = build_windows(ct, f128, keyed, sid)
    model = NgramModel([read_corpus(p) for p in sorted((ROOT / "tools" / "data" / "fr16").glob("*.txt.gz"))])
    T = table(model)
    free_ids = [sid[s] for s in FREE]
    base = [AZ.index(key[s][0]) if s in key else AZ.index("e") for s in signs]
    touch = {f: [w for w in W if f in w] for f in free_ids}
    seed_score = score(T, W, base)
    rv, rs_raw = climb(T, W, base, free_ids, touch)
    rv2, rej = reject(rv, base, free_ids, signs, gl)
    real = score(T, W, rv2)
    # stability
    rnd = random.Random(SEED_STAB); stab = Counter()
    for _ in range(NSTAB):
        v0 = list(base)
        for f in free_ids:
            v0[f] = rnd.randrange(26)
        sv, _ = climb(T, W, v0, free_ids, touch)
        sv, _ = reject(sv, base, free_ids, signs, gl)
        for f in free_ids:
            stab[(signs[f], AZ[sv[f]])] += 1
    # control: same shuffle as score_f130.py (letter values permuted among key_syl's keyed signs)
    rnd = random.Random(SEED); ks = sorted(key); letters = [key[s][0] for s in ks]
    ctrl = []
    for _ in range(NSHUF):
        p = letters[:]; rnd.shuffle(p)
        v0 = list(base)
        for s, l in zip(ks, p):
            v0[sid[s]] = AZ.index(l)
        pre = score(T, W, v0)
        cv, _ = climb(T, W, v0, free_ids, touch)
        cv, _ = reject(cv, v0, free_ids, signs, gl)
        ctrl.append((pre, score(T, W, cv)))
    sc = sorted(c[1] for c in ctrl)
    p95 = sc[int(0.95 * (len(sc) - 1))]
    gate = real > p95
    res = {"stat": "fr16 4-gram mean log10 P/letter, f.130 + f.128 cipher runs, all free rows keyed", "windows": int(len(W)),
           "seed_key_score": round(seed_score, 4), "repaired_before_rejection": round(rs_raw, 4),
           "repaired_real": round(real, 4), "rejected": [list(r) for r in rej],
           "shuf_seed_mean": round(sum(c[0] for c in ctrl) / NSHUF, 4),
           "shuf_repaired_mean": round(sum(sc) / NSHUF, 4), "shuf_repaired_p95": round(p95, 4),
           "shuf_repaired_max": round(sc[-1], 4), "shuffles_ge_real": sum(1 for c in sc if c >= real),
           "n_shuffles": NSHUF, "gate_pass": gate}
    # final key and grades
    krows = ["sign\tvalue\tgrade\tsource\tstability\tgloss_letters"]; kgrade = {}
    for s in signs:
        v = AZ[rv2[sid[s]]]; glc = gl.get(s, Counter())
        if s not in FREE:
            a, n = key[s][1], key[s][2]
            g = "C" if a >= 3 and a / n >= 0.5 else "M"; src = f"key_syl {a}/{n} (held)"
        else:
            st = stab[(s, v)]
            changed = s not in key or key[s][0] != v
            src = ("repair" if changed else "key_syl kept by repair") + (f" (key_syl {key[s][0]} {key[s][1]}/{key[s][2]})" if s in key else " (unkeyed in key_syl)")
            if any(r[0] == s for r in rej):
                src = f"key_syl {key[s][1]}/{key[s][2]} (repair value rejected by f.128 gloss)"
            if glc.get(v, 0) >= 2:
                g = "C"
            elif gate and st >= 14 and not any(r[0] == s for r in rej):
                g = "S"
            else:
                g = "M"
        kgrade[s] = g
        gls = ",".join(f"{a}:{b}" for a, b in glc.most_common())
        krows.append(f"{'hash' if s == '#' else s}\t{v}\t{g}\t{src}\t{stab[(s, v)] if s in FREE else ''}\t{gls}")
    tok = ["line\tpos\tsign\tconf\tvalue\tgrade"]; gc = Counter(); lines = {}
    for r in ct:
        s = r["sign"]
        if s.startswith("CLEAR:"):
            lines.setdefault(r["line"], []).append("[" + s[6:] + "]"); continue
        v = AZ[rv2[sid[s]]]; g = kgrade[s] if r["conf"] == "H" else "M"
        gc[g] += 1
        tok.append(f"{r['line']}\t{r['pos']}\t{s}\t{r['conf']}\t{v}\t{g}")
        lines.setdefault(r["line"], []).append(v.upper() if g == "M" else v)
    res["grades"] = {g: gc[g] for g in "CSMU"}
    reading = ["# f.130r decoded with the repaired key (repair_f130.py, A2-DIN3). lower = C or S, UPPER = M, [..] = clear.",
               "# grades: " + " ".join(f"{g} {gc[g]}" for g in "CSMU")]
    reading += [f"{ln}\t{' '.join(v)}" for ln, v in lines.items()]
    ctl = ["i\tseed_stat\trepaired_stat"] + [f"{i}\t{a:.4f}\t{b:.4f}" for i, (a, b) in enumerate(ctrl)]
    st = ["sign\tvalue\tcount_of_20"] + [f"{s}\t{v}\t{c}" for (s, v), c in sorted(stab.items())]
    return {"result.json": json.dumps(res, indent=1) + "\n", "key_repaired.tsv": "\n".join(krows) + "\n",
            "tokens.tsv": "\n".join(tok) + "\n", "reading.txt": "\n".join(reading) + "\n",
            "control.tsv": "\n".join(ctl) + "\n", "stability.tsv": "\n".join(st) + "\n"}


def main():
    out = build()
    if "--check" in sys.argv:
        bad = [f for f, t in out.items() if not (OUT / f).exists() or (OUT / f).read_text() != t]
        print("check: committed outputs match" if not bad else f"check: STALE {bad}")
        sys.exit(1 if bad else 0)
    OUT.mkdir(exist_ok=True)
    for f, t in out.items():
        (OUT / f).write_text(t)
    print(out["result.json"])


if __name__ == "__main__":
    main()
