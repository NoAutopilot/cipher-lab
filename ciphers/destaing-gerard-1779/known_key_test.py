#!/usr/bin/env python3
"""FT4 (3 Oct 2026): known-key test of the La Luzerne-Destouches 1781 key on d'Estaing's 30 April 1779 code.

Pre-registered in NOTES.md "FT4-destaing-gerard-1779". Statistic: fr18 4-gram mean log10 score (and word cover) of the
decoded text over runs of >=2 consecutive keyed tokens. Control: 1000 value-shuffled keys (coverage fixed). Gate: target
above control p99. Positive control: the key on its own ciphertext, 5 windows of the target's N, masked to the target's
coverage. Exits 0 always; prints both numbers. No network.
"""
import csv, random, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import judge_plaintext as jp

KEYF = ROOT / "ciphers/huntington-luzerne-destouches-1781/key.tsv"
key = {}
for r in csv.DictReader(open(KEYF), delimiter="\t"):
    v = r["value"].strip()
    if v and r["code"].strip().isdigit():
        key[int(r["code"])] = v
codes = sorted(key)
model = jp.NgramModel([jp.read_corpus(p) for p in jp.LANG_CORPORA["fr18"]])


def runs_text(toks, k, mask=None):
    out, cur = [], []
    for i, t in enumerate(toks):
        if t in k and (mask is None or mask[i]):
            cur.append(k[t])
        else:
            if len(cur) >= 2:
                out.append("".join(cur))
            cur = []
    if len(cur) >= 2:
        out.append("".join(cur))
    return out


def stat(toks, k, mask=None):
    segs = runs_text(toks, k, mask)
    txt = "".join(segs)
    if len(jp.fold(txt)) < 8:
        return None, None, 0
    # letter-weighted mean of per-run scores (runs are not contiguous text)
    tot = n = 0
    for s_ in segs:
        L = len(jp.fold(s_))
        if L >= model.n:
            tot += model.score(s_) * (L - model.n + 1); n += L - model.n + 1
    return (tot / n if n else None), model.cover(txt), len(jp.fold(txt))


def shuffled(rnd):
    vals = [key[c] for c in codes]; rnd.shuffle(vals)
    return dict(zip(codes, vals))


def trial(toks, mask, rnd, draws=1000):
    t, tc, L = stat(toks, key, mask)
    ctrl = []
    for _ in range(draws):
        s_, _, _ = stat(toks, shuffled(rnd), mask)
        if s_ is not None:
            ctrl.append(s_)
    ctrl.sort()
    return t, tc, L, ctrl


def main():
    rnd = random.Random(1)
    tgt = [int(r["token"]) for r in csv.DictReader(open(HERE / "ciphertext.tsv"), delimiter="\t") if r["kind"] == "CODE"]
    covered = sum(t in key for t in tgt)
    cov = covered / len(tgt)
    print(f"key: {len(key)} valued codes, range {codes[0]}-{codes[-1]}")
    print(f"TARGET coverage: {covered}/{len(tgt)} tokens = {cov:.3f}; distinct keyed {len({t for t in tgt if t in key})}/{len(set(tgt))}")
    t, tc, L, ctrl = trial(tgt, None, rnd)
    p99 = jp.pct(ctrl, 0.99); p95 = jp.pct(ctrl, 0.95)
    print(f"TARGET run-text letters {L}: score {t:.3f} cover {tc:.3f} | CONTROL (value-shuffled, n={len(ctrl)}) "
          f"mean {sum(ctrl)/len(ctrl):.3f} p95 {p95:.3f} p99 {p99:.3f} | GATE {'PASS' if t > p99 else 'FAIL'}")
    print("TARGET runs:", " | ".join(runs_text(tgt, key)))
    # positive control
    own = [int(r["group"]) for r in csv.DictReader(open(KEYF.parent / "ciphertext.tsv"), delimiter="\t")
           if r["group"].strip().isdigit()]
    passes = 0
    for w in range(5):
        j = rnd.randrange(0, len(own) - len(tgt))
        win = own[j:j + len(tgt)]
        keyed = [i for i, x in enumerate(win) if x in key]
        keep = set(rnd.sample(keyed, min(len(keyed), covered)))
        mask = [i in keep for i in range(len(win))]
        pt, pc, pL, pctrl = trial(win, mask, rnd)
        ok = pt is not None and pt > jp.pct(pctrl, 0.99)
        passes += ok
        print(f"POSITIVE window {w} (start {j}, own coverage {len(keyed)}/{len(win)} masked to {len(keep)}): letters {pL} "
              f"score {pt:.3f} cover {pc:.3f} | control mean {sum(pctrl)/len(pctrl):.3f} p99 {jp.pct(pctrl,0.99):.3f} | {'PASS' if ok else 'FAIL'}")
    print(f"POSITIVE CONTROL: {passes}/5 windows clear p99 -> test is {'a test' if passes >= 4 else 'a NON-TEST at this coverage'}")


if __name__ == "__main__":
    main()
