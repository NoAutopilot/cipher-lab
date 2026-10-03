#!/usr/bin/env python3
"""Held-out check of the received-side twin found by GAPS171 (3 Oct 2026): mssEC 02 p.12-13 (object 3588-3589) and
mssEC 03 p.37 (object 2093), Halleck to Stanton, St Louis 7 Mar 1862, printed OR ser. I vol. 8 pp. 831-832.

PAIRS are the code word -> print word slots read by aligning the two volunteer transcriptions with the print (same
order, one code word per print name; both copies agree on every slot). For each slot whose code word already has a
key.md value (from SENT-ledger witnesses, independent of this telegram), the prediction is key.md's value nearest the
date; agreement is counted. Control: key.md's meanings permuted across its words (seeded, 2000 draws), same count.
Usage: received_twin_check.py [--check]   (--check exits 1 unless the real count beats the control p99)
"""
import random, sys, datetime
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import decode as dec  # noqa: E402

DAY = datetime.date(1862, 3, 7)
PAIRS = [("Indus", "Stanton"), ("Koran", "Ohio"), ("Luna", "Missouri"), ("Myrtle", "Cumberland River"),
         ("Alvord", "Buell"), ("wayworn", "army"), ("Lamb", "Kansas"), ("Alden", "Halleck")]


def predict(key, w):
    rows = key.get(w.lower())
    if not rows:
        return None
    m, _ = dec.pick(rows, DAY)
    return m


def agree(key):
    n = hit = 0
    for w, p in PAIRS:
        m = predict(key, w)
        if m is None:
            continue
        n += 1
        hit += p.lower() in m.lower() or m.lower() in p.lower()
    return hit, n


def main(argv):
    key = dec.load_key()
    hit, n = agree(key)
    words, vals = list(key), list(key.values())
    rng = random.Random(171)
    null = []
    for _ in range(2000):
        v = vals[:]
        rng.shuffle(v)
        null.append(agree(dict(zip(words, v)))[0])
    null.sort()
    p99 = null[int(0.99 * (len(null) - 1))]
    print(f"real {hit}/{n} slots agree with key.md (pick nearest 7 Mar 1862); shuffled-key mean "
          f"{sum(null)/len(null):.2f}, p99 {p99}")
    for w, p in PAIRS:
        print(f"  {w:8s} print {p:18s} key.md {predict(key, w)}")
    if "--check" in argv and not hit > p99:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
