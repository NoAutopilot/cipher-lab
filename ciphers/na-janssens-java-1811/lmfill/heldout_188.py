#!/usr/bin/env python3
"""Held-out fill test of the GAPS17 LM-context instrument on leaf 188 (R11-JANSLM, 6 Oct 2026). Gates
pre-registered in lmfill/PREREG-R11-JANSLM.md (commit 2a454d193) before this script scored anything.

Usage: python3 lmfill/heldout_188.py   (from the target folder; writes lmfill/heldout_188.tsv, and
lmfill/unkeyed_candidates.tsv only if every gate passes)
"""
import csv, random, sys
from collections import Counter
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE / "lmfill"))
from lmfill import LM, jp, rows  # noqa: E402

WIN, MASKS, CSEEDS, FRAC, MARGIN = 3, 10, 20, 0.20, 1.0
A_MIN, P_MIN, P_N = 0.30, 0.80, 10


def main():
    key = {r["code"].strip(): r["value"].strip() for r in rows("key.tsv")}
    toks = rows("reading_tokens.tsv")
    vals = [jp.fold(t["value"]) if t["grade"] in "CM" and t["value"] not in ("", "?") else None for t in toks]
    raw = [t["value"] for t in toks]
    vocab = sorted({jp.fold(v) for v in key.values() if jp.fold(v)})
    items = [i for i, t in enumerate(toks) if t["grade"] == "C" and vals[i]]
    lm = LM("".join(jp.fold(jp.read_corpus(p)) for p in jp.LANG_CORPORA["fr1810"]))

    @lru_cache(maxsize=None)
    def sc(s):
        return lm.score(s)

    def ctx(i, masked):
        def side(rng_):
            out = []
            for j in rng_:
                if j in masked or vals[j] is None:
                    if vals[j] is None and raw[j] not in ("", "?") and toks[j]["grade"] in "CM":
                        continue  # punctuation-only neighbour: transparent
                    break
                out.append(vals[j])
                if len(out) == WIN:
                    break
            return out
        L = side(range(i - 1, -1, -1))
        R = side(range(i + 1, len(toks)))
        return "".join(reversed(L)), "".join(R)

    def fill(l, r):
        s = sorted(((sc(l + v + r), v) for v in vocab), reverse=True)
        return s[0][1], s[0][0] - s[1][0]

    prior = max(vocab, key=lambda v: sc(v))
    major = Counter(vals[i] for i in items).most_common(1)[0][0]
    real, ctrl = [], [[] for _ in range(CSEEDS)]
    n_mask = round(FRAC * len(items))
    for m in range(1, MASKS + 1):
        rng = random.Random(m)
        masked = set(rng.sample(items, n_mask))
        allpos = [j for j in range(len(toks)) if j not in masked]
        for i in sorted(masked):
            l, r = ctx(i, masked)
            w, mg = fill(l, r)
            real.append((m, i, toks[i]["sign"], vals[i], l, r, w, round(mg, 3), w == vals[i]))
        for c in range(CSEEDS):
            crng = random.Random(m * 1000 + c)
            for i in sorted(masked):
                j = crng.choice([p for p in allpos if p != i])
                w, mg = fill(*ctx(j, masked))
                ctrl[c].append((w == vals[i], mg))

    A = sum(x[-1] for x in real) / len(real)
    cacc = [sum(ok for ok, _ in cs) / len(cs) for cs in ctrl]
    conf = [x for x in real if x[7] >= MARGIN]
    pc = sum(x[-1] for x in conf) / len(conf) if conf else 0.0
    cconf = [ok for cs in ctrl for ok, mg in cs if mg >= MARGIN]
    cpc = sum(cconf) / len(cconf) if cconf else 0.0
    cls = Counter(x[3] for x in conf if x[-1])
    dominated = bool(cls) and cls.most_common(1)[0][1] > sum(cls.values()) / 2
    base_prior = sum(vals[x[1]] == prior for x in real) / len(real)
    base_major = sum(vals[x[1]] == major for x in real) / len(real)
    g1, g2 = A >= A_MIN, A > max(cacc)
    g3 = len(conf) >= P_N and pc >= P_MIN and pc > cpc and not dominated
    with open(HERE / "lmfill/heldout_188.tsv", "w", encoding="utf-8") as f:
        f.write("mask_seed\tidx\tcode\ttrue\tleft\tright\twinner\tmargin\tcorrect\n")
        for x in real:
            f.write("\t".join(map(str, x)) + "\n")
    print(f"items {len(items)} (C, foldable); masked per seed {n_mask}; trials {len(real)}; vocab {len(vocab)}")
    print(f"gate1 top-1 accuracy {A:.3f} (>= {A_MIN}) {'PASS' if g1 else 'FAIL'}")
    print(f"gate2 shuffled-context pooled acc: mean {sum(cacc)/len(cacc):.3f}, max {max(cacc):.3f} -> "
          f"{'PASS' if g2 else 'FAIL'}")
    print(f"gate3 confident fills (margin>={MARGIN}): {len(conf)}, precision {pc:.3f}; control confident "
          f"{len(cconf)}, precision {cpc:.3f}; correct-confident by value {dict(cls)} dominated={dominated} -> "
          f"{'PASS' if g3 else 'FAIL'}")
    print(f"baselines (not gated): context-free prior '{prior}' {base_prior:.3f}; majority '{major}' {base_major:.3f}")
    print("ALL GATES", "PASS" if (g1 and g2 and g3) else "FAIL")
    return 0 if (g1 and g2 and g3) else 1


if __name__ == "__main__":
    sys.exit(main())
