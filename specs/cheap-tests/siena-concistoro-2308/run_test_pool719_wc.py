"""R13-SIENAWC (6 Oct 2026): nos. 7 + 19 pooled (agent J, N=481, K=62) under R13-SIENA719's homophonic + nomenclator design
with ONE change, a structural restriction on where a word code may sit: tools/homophonic_anneal.py solve_nomen(word_signs=...)
proposes a vocab word only on signs J tokenised as multi-character units or as drawn non-alphanumeric marks (27 of the
pool's 55 unfixed signs, 110 tokens); every single letter- or digit-shaped sign decodes to a letter only.
Pre-registered in ciphers/siena-concistoro-2308/PREREG-R13-SIENAWC.md (pushed before the scored run). Material, knobs,
corpus, VOCAB/NOMEN and control construction are run_test_pool719_nomen.py / run_test_no07_nomen.py's, imported unchanged.
Matched control, same restriction: the 10 NOMEN signs are eligible (the design assumption under test: a nomenclator's word
codes are drawn signs) plus 17 unfixed letter homophones whose counts are matched greedily to the target's eligible-sign
counts left after each NOMEN sign takes its nearest target count, so the eligible set has the target's size and count shape.

  python3 run_test_pool719_wc.py control --err 0 0.035 0.07 --seeds 1 2 3 4 5   # control first
  python3 run_test_pool719_wc.py target --seeds 1 2 3                            # only if both gates pass
  python3 run_test_pool719_wc.py shuffled --seeds 1 2 3
  python3 run_test_pool719_wc.py --check
"""
import random
import sys
from collections import Counter
from pathlib import Path

import run_test_pool719_nomen as P

R = P.R
H = R.H
R.OUT = Path(__file__).with_name("results_pool719_wc.json")


def eligible(s):
    return len(s) > 1 or not s.isalnum()


def target_eligible():
    seq = [x for r in R.runs() for x in r]
    return {s for s in set(seq) if eligible(s) and s not in R.FIX}, Counter(seq)


def control_word_signs(seq, truth, fixed, tgt_counts):
    cnt = Counter(seq)
    pool = sorted(tgt_counts, reverse=True)
    nomen_signs = [s for s in cnt if len(truth[s]) > 1]
    for s in nomen_signs:
        pool.remove(min(pool, key=lambda n: abs(n - cnt[s])))
    cands = sorted(s for s in cnt if len(truth[s]) == 1 and s not in fixed)
    chosen = set()
    for n in pool:
        free = [s for s in cands if s not in chosen]
        if free:
            chosen.add(min(free, key=lambda s: (abs(cnt[s] - n), s)))
    return set(nomen_signs) | chosen


def control_one(args):
    sd, err = args
    m = R.model()
    seq_t = [x for r in R.runs() for x in r]
    tc = Counter(seq_t)
    el_t, _ = target_eligible()
    units = R.control_units(sd, [len(r) for r in R.runs()])
    seq, truth = R.encipher(units, len(tc), sd)
    fixed = R.pick_fixed(seq, truth, [(R.FIX[s], tc[s]) for s in R.FIX])
    ws = control_word_signs(seq, truth, fixed, [tc[s] for s in el_t])
    if err:
        erng, signs = random.Random(500 + sd), sorted(set(seq))
        seq = [erng.choice([s for s in signs if s != x]) if x not in fixed and erng.random() < err else x for x in seq]
    sc, key = H.solve_nomen(seq, m, R.RESTARTS, R.ITERS, sd, 1.0, R.VOCAB, R.WORD_PROB, fixed, R.WORD_BONUS,
                            word_signs=ws)[0]
    ok = sum(key[x] == u for x, u in zip(seq, units))
    unf = [(x, u) for x, u in zip(seq, units) if x not in fixed]
    wtok = [(x, u) for x, u in zip(seq, units) if u in R.NOMEN]
    return {"seed": sd, "err": err, "N": len(seq), "K": len(set(seq)), "fixed_signs": len(fixed),
            "word_signs": len(ws), "word_sign_tokens": sum(x in ws for x in seq), "nomen_tokens": len(wtok),
            "token_acc": round(ok / len(seq), 3), "token_acc_unfixed": round(sum(key[x] == u for x, u in unf) / len(unf), 3),
            "nomen_recall": round(sum(key[x] == u for x, u in wtok) / max(1, len(wtok)), 3),
            "word_signs_assigned": sorted(v for v in key.values() if len(v) > 1),
            "decoded": "".join(key[x] for x in seq)[:120], "plain": "".join(units)[:120]}


def target_one(args):
    sd, shuffle = args
    m = R.model()
    seq = [x for r in R.runs() for x in r]
    ws, _ = target_eligible()
    if shuffle:
        random.Random(100 + sd).shuffle(seq)
    res = H.solve_nomen(seq, m, R.RESTARTS, R.ITERS, sd, 1.0, R.VOCAB, R.WORD_PROB, dict(R.FIX), R.WORD_BONUS,
                        word_signs=ws)
    sc, key = res[0]
    return {"seed": sd, "score": round(sc, 2), "key": key, "decoded": "".join(key[x] for x in seq),
            "word_signs": {s: v for s, v in key.items() if len(v) > 1}, "restart_scores": [round(r[0], 1) for r in res]}


R.control_one, R.target_one = control_one, target_one

if __name__ == "__main__":
    sys.argv[0] = __file__
    R.main()
