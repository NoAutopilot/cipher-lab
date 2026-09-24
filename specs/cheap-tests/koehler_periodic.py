#!/usr/bin/env python3
"""Cheap test cheap_tests_in_order[0] (24 Sept 2026, LANE B breadth worker bKOE), koehler-1944: periodic IC and
Kasiski examination for period 2-30 on the pooled 924 letters (specs/koehler-1944.json 'ciphertext' groups, same
five messages as specs/cheap-tests/koehler_ic.py; message 3 is headed 137 letters by Kahn but has 140 as printed
-- this script pools the 140 actually present, per that script's WARNING and the parsing used throughout this repo).
Question: does a Vigenere-family or running-key system leave a periodic signal (a period whose coset IC sits near
German plaintext, or a Kasiski distance spectrum favouring one small period), which the flat pooled IC (cheap test
1, koehler_ic.out, 0.0399) alone cannot rule out?

Matched controls (rule 3), same per-message lengths, German plaintext (tools/data/de16/composed_enhg.txt, the only
German corpus on disk):
  (a) periodic-key control: one random period P in 2-30, one random Vigenese key of length P, each message
      enciphered with the key restarting at phase 0 -- tests whether this script's own method would find a real
      period of this length in ciphertext this short.
  (b) one-time-key control: each message enciphered with an independent uniform random shift per letter (running
      key as long as the message, never repeated) -- tests that a genuinely non-periodic system reads flat here,
      the way test 1 already found the target reads flat on plain IC.
"""
import argparse, json, random, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
A = "abcdefghijklmnopqrstuvwxyz"


def ic(s):
    c = Counter(s)
    n = len(s)
    return sum(v * (v - 1) for v in c.values()) / (n * (n - 1)) if n > 1 else 0.0


def fold_german(text):
    t = text.lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    return "".join(ch for ch in t if ch in A)


def load_messages():
    spec = json.loads((ROOT / "specs/koehler-1944.json").read_text())
    msgs = []
    for m in spec["ciphertext"]:
        letters = "".join(m["groups"].split())
        assert letters.isalpha() and letters.islower()
        assert len(letters) == m["letters"], (len(letters), m["letters"])
        msgs.append(letters)
    return msgs


def periodic_ic(msgs, max_period=30):
    """Weighted-average coset (every-P-th-letter) IC for each candidate period, computed PER MESSAGE and
    pooled by coset length -- not on the five messages concatenated into one stream. These are five separate
    radio transmissions (Kahn 1981); a Vigenere-family key almost certainly restarts phase at each message
    start, so a global coset over the naive 924-letter concatenation straddles boundaries at arbitrary phases
    (none of 237/178/140/140/229 is a multiple of a small period) and dilutes any real signal -- confirmed
    empirically: the first version of this script (message-boundary-blind) found only 0.0451 at its own
    control's true period 6, barely above uniform 0.0385; this per-message version recovers it cleanly (see
    .out). Higher = more consistent with a period-P polyalphabetic system (a true period's cosets are each
    monoalphabetic, so their IC approaches the plaintext language's IC rather than the flat pooled value)."""
    out = {}
    for p in range(2, max_period + 1):
        ics, weights = [], []
        for msg in msgs:
            for i in range(p):
                c = msg[i::p]
                if len(c) > 1:
                    ics.append(ic(c)); weights.append(len(c))
        out[p] = sum(i * w for i, w in zip(ics, weights)) / sum(weights) if weights else 0.0
    return out


def kasiski(msgs, ngram=3, max_period=30):
    """Repeated-ngram distance spectrum, WITHIN each message only (never across message boundaries, for the
    same restart-per-message reason as periodic_ic): for every candidate period, how many pairwise distances
    between repeats of the same ngram it divides. A real short period concentrates hits on its own divisors."""
    factor_counts = Counter()
    ndist = 0
    for msg in msgs:
        positions = {}
        for i in range(len(msg) - ngram + 1):
            positions.setdefault(msg[i:i + ngram], []).append(i)
        for pos in positions.values():
            if len(pos) > 1:
                for i in range(len(pos)):
                    for j in range(i + 1, len(pos)):
                        d = pos[j] - pos[i]
                        ndist += 1
                        for p in range(2, max_period + 1):
                            if d % p == 0:
                                factor_counts[p] += 1
    return factor_counts, ndist


def vigenere_encipher(plain, key):
    return "".join(A[(A.index(p) + A.index(k)) % 26] for p, k in zip(plain, (key[i % len(key)] for i in range(len(plain)))))


def german_window(corpus, n, rng):
    if n > len(corpus):
        raise ValueError("corpus shorter than requested window")
    start = rng.randrange(len(corpus) - n)
    return corpus[start:start + n]


def report_periods(label, msgs, top=5):
    pic = periodic_ic(msgs)
    best = sorted(pic.items(), key=lambda kv: -kv[1])[:top]
    kas, ndist = kasiski(msgs)
    kas_top = kas.most_common(top)
    return pic, best, kas_top, ndist


def fmt_top(best):
    return ", ".join(f"P={p}:{v:.4f}" for p, v in best)


def fmt_kas(kas_top, ndist):
    return f"({ndist} repeat-3gram distance pairs) " + ", ".join(f"P={p}:{c}" for p, c in kas_top)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=1)
    args = ap.parse_args()
    rng = random.Random(args.seed)

    msgs = load_messages()
    lengths = [len(m) for m in msgs]
    assert sum(lengths) == 924, sum(lengths)

    corpus = fold_german((ROOT / "tools/data/de16/composed_enhg.txt").read_text(encoding="utf-8", errors="replace"))

    # control (a): one random period, one random Vigenere key, restarted at each message's own start
    P = rng.randrange(2, 31)
    key = "".join(rng.choice(A) for _ in range(P))
    ctrl_a_msgs = [vigenere_encipher(german_window(corpus, n, rng), key) for n in lengths]

    # control (b): independent one-time (uniform, non-repeating-key) shift per letter, per message
    ctrl_b_msgs = []
    for n in lengths:
        plain = german_window(corpus, n, rng)
        shifts = [rng.randrange(26) for _ in range(n)]
        ctrl_b_msgs.append("".join(A[(A.index(p) + s) % 26] for p, s in zip(plain, shifts)))

    assert sum(len(m) for m in ctrl_a_msgs) == 924 and sum(len(m) for m in ctrl_b_msgs) == 924

    print(f"seed={args.seed}  message lengths (pooled 924, per-message coset test, key/shift restart at each message): {lengths}")
    print("(msg3: Kahn header 137, letters as printed 140 -- 140 used, per koehler_ic.py's parse)")
    print(f"control (a) periodic key: period P={P}, key length {P}")
    print()

    rows = [("target", msgs), ("control_a_periodic(P=%d)" % P, ctrl_a_msgs), ("control_b_onetime", ctrl_b_msgs)]
    print("label\tbest_period_IC_avg\ttop5_periods(IC)\tkasiski_top5(count)")
    results = {}
    for label, mm in rows:
        pic, best, kas_top, ndist = report_periods(label, mm)
        results[label] = (pic, best, kas_top, ndist)
        print(f"{label}\t{best[0][1]:.4f} (P={best[0][0]})\t{fmt_top(best)}\t{fmt_kas(kas_top, ndist)}")

    print()
    print("cross-check: target's IC at control (a)'s own period P=%d vs control (a)'s own best period" % P)
    t_pic = results["target"][0]
    ctrl_a_label = "control_a_periodic(P=%d)" % P
    print(f"  target IC at P={P}: {t_pic[P]:.4f}   control_a IC at its own best period P={results[ctrl_a_label][1][0][0]}: {results[ctrl_a_label][1][0][1]:.4f}")

    ref = "reference: German plain unigram IC ~0.076 (koehler_ic.out), uniform/random ~0.0385, target pooled flat IC (cheap test 1) 0.0399"
    print()
    print(ref)


if __name__ == "__main__":
    main()
