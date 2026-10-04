#!/usr/bin/env python3
"""potocka_trial.py: does Bourdeau's Potocka key (key-potocka.json) read R7524? A trial decode with a matched control
(A3V3-SANGP, 4 Oct 2026; CLAUDE.md rule 3).

Key: D. Bourdeau, cyphersolver targets/potocka1714/key-potocka.json (text CC BY 4.0), fetched 4 Oct 2026, used as data.
Statistic: mean log10 P(letter | 3 previous) of the decoded text, over every 4-gram lying wholly inside a run of
key-covered positions (uncovered tokens are gaps; [PLAIN] words are dropped, as in the 232-token stream). Model: add-k
4-gram (tools/judge_plaintext.NgramModel) on tools/data/pl18 minus the held-out file (HELD), from which the control
plaintexts are drawn.
  target      R7524's 232 tokens decoded with the key.
  control A   (key right) S windows of 232 held-out letters enciphered WITH the Potocka key at the target's own covered
              positions (letters the key lacks, j/v, become gaps) and with 45 out-of-range homophones elsewhere; decoded
              with the key. Same N, same coverage mask, same run structure as the target.
  control B   (key wrong) the same windows enciphered with a random reassignment of the key's letter values to its signs,
              decoded with the true key: the control's own failure mode, so A can fail differently from B.
  null        the target's tokens shuffled (order), decoded with the key, S draws.
Verdict: the key reads R7524 only if the target scores inside control A's distribution (above A's 5th percentile) AND
above the null's 95th percentile. Prints the numbers; writes trial_results.json and target_decode.txt.
  python3 potocka_trial.py [--S 200] [--seed 1] [--check]
"""
import argparse, gzip, json, random, re, statistics, sys
from math import log10
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import judge_plaintext as J  # noqa: E402

PL18 = ROOT / "tools" / "data" / "pl18"
HELD = "bc.wbp.lodz.pl.Pamietniki_do_panowania_Augusta_II_91967.txt.gz"


def stat(model, letters):
    """letters: list of a-z or None (gap). Mean log10 4-gram prob inside covered runs; also count of 4-grams."""
    tot, n, run = 0.0, 0, ""
    for ch in letters + [None]:
        if ch is None:
            for i in range(3, len(run)):
                g = run[i - 3:i + 1]
                tot += log10((model.c.get(g, 0) + model.k) / (model.ctx.get(g[:-1], 0) + model.V * model.k)); n += 1
            run = ""
        else:
            run += ch
    return (tot / n if n else float("nan")), n


def pct(xs, q):
    xs = sorted(xs); return xs[min(len(xs) - 1, max(0, int(q * len(xs))))]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--S", type=int, default=200); ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--check", action="store_true"); a = ap.parse_args()
    key = json.loads((HERE / "key-potocka.json").read_text())
    toks = (HERE / "r7524_tokens.txt").read_text().split()
    assert len(toks) == 232
    mask = [t in key for t in toks]
    files = sorted(PL18.glob("*.txt.gz"))
    model = J.NgramModel([J.read_corpus(f) for f in files if f.name != HELD])
    held = J.fold(J.read_corpus(PL18 / HELD))
    rnd = random.Random(a.seed)
    dec = [key.get(t) for t in toks]
    t_score, t_n = stat(model, dec)
    inv = {}
    for s, v in key.items():
        inv.setdefault(v, []).append(s)
    oor = [str(x) for x in range(79, 160)][:45]  # 45 out-of-range signs for uncovered positions
    A, B, NUL, KA = [], [], [], []
    for _ in range(a.S):
        j = rnd.randrange(0, len(held) - 232); pt = held[j:j + 232]
        # control A: key right at the target's covered positions
        homo = {}
        ct = []
        for i, ch in enumerate(pt):
            if mask[i] and ch in inv:
                ct.append(rnd.choice(inv[ch]))
            else:
                if ch not in homo:
                    homo[ch] = rnd.sample(oor, 4)
                ct.append(rnd.choice(homo[ch]))
        KA.append(len(set(ct)))
        A.append(stat(model, [key.get(s) for s in ct])[0])
        # control B: same plaintext, key values permuted across signs (a wrong key of the same shape)
        vals = list(key.values()); rnd.shuffle(vals); wrong = dict(zip(key.keys(), vals))
        winv = {}
        for s, v in wrong.items():
            winv.setdefault(v, []).append(s)
        ctb = [rnd.choice(winv[ch]) if (mask[i] and ch in winv) else rnd.choice(homo.get(ch, oor[:1]))
               for i, ch in enumerate(pt)]
        B.append(stat(model, [key.get(s) for s in ctb])[0])
        sh = toks[:]; rnd.shuffle(sh)
        NUL.append(stat(model, [key.get(t) for t in sh])[0])
    res = {"N": 232, "covered": sum(mask), "covered_signs": len({t for t in toks if t in key}), "signs": len(set(toks)),
           "target_score": round(t_score, 4), "target_4grams": t_n,
           "controlA_key_right": {"mean": round(statistics.mean(A), 4), "p05": round(pct(A, .05), 4), "min": round(min(A), 4),
                                  "signs_mean": round(statistics.mean(KA), 1)},
           "controlB_key_wrong": {"mean": round(statistics.mean(B), 4), "p95": round(pct(B, .95), 4)},
           "null_shuffled_target": {"mean": round(statistics.mean(NUL), 4), "p95": round(pct(NUL, .95), 4)},
           "S": a.S, "seed": a.seed, "held_out": HELD}
    res["A_beats_B_share"] = round(sum(x > pct(B, .95) for x in A) / len(A), 3)
    res["verdict"] = ("key reads R7524" if t_score > res["controlA_key_right"]["p05"] and t_score > res["null_shuffled_target"]["p95"]
                      else "key does not read R7524 (control-backed)" if res["A_beats_B_share"] >= 0.9
                      else "non-test: control A does not separate from control B")
    decode = " ".join(d if d else "·" for d in dec)
    out = json.dumps(res, indent=1)
    if a.check:
        old = (HERE / "trial_results.json").read_text()
        if old.strip() != out.strip() or (HERE / "target_decode.txt").read_text().strip() != decode:
            print("STALE: committed trial_results.json / target_decode.txt differ"); sys.exit(1)
        print("OK: committed results reproduce"); return
    (HERE / "trial_results.json").write_text(out + "\n"); (HERE / "target_decode.txt").write_text(decode + "\n")
    print(out); print("decode:", decode)


if __name__ == "__main__":
    main()
