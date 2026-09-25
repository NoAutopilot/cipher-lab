#!/usr/bin/env python3
"""Cheap test 1 for pollaky-1865-1875: N, distinct K, IC per ad, plus matched controls
(English text of the same N, uniform-random string of the same K) for the three letter-based
ads (1, 3, 4). Ad 2 is a digit/number code, not letters, so no letter-corpus control is run for it
(brief: "for letter ads"). No fetch; reads tools/data/pg1661_holmes.txt already on disk.

Usage: python3 stats.py
"""
import random
import re
import string
from collections import Counter

random.seed(20260925)

HOLMES = "tools/data/pg1661_holmes.txt"


def ic(seq):
    n = len(seq)
    if n < 2:
        return 0.0
    counts = Counter(seq)
    num = sum(c * (c - 1) for c in counts.values())
    return num / (n * (n - 1))


def report(label, tokens):
    n = len(tokens)
    counts = Counter(tokens)
    k = len(counts)
    val = ic(tokens)
    print(f"{label}: N={n} K={k} IC={val:.4f}")
    return n, k, val


def english_letters(path, n_target, seeds=3):
    with open(path, encoding="utf-8", errors="ignore") as f:
        text = f.read()
    letters = [c.upper() for c in text if c.isalpha()]
    results = []
    for seed in range(seeds):
        rng = random.Random(1000 + seed)
        start = rng.randrange(0, max(1, len(letters) - n_target))
        window = letters[start:start + n_target]
        results.append(ic(window))
    return results


def uniform_random(k_target, n_target, seeds=3):
    alphabet = list(string.ascii_uppercase)[:max(k_target, 2)]
    results = []
    for seed in range(seeds):
        rng = random.Random(2000 + seed)
        seq = [rng.choice(alphabet) for _ in range(n_target)]
        results.append(ic(seq))
    return results


print("=== Ad 1 (secret script, invented signs) ===")
ad1_run = ["SIGN-01", "SIGN-02", "SIGN-03", "SIGN-04", "SIGN-05",
           "SIGN-01", "SIGN-07", "SIGN-08", "SIGN-09", "SIGN-10"]
n1, k1, ic1 = report("ad1 cipher run", ad1_run)
eng1 = english_letters(HOLMES, n1)
rnd1 = uniform_random(k1, n1)
print(f"  control: English text, same N={n1}, 3 seeds: IC = {['%.4f' % v for v in eng1]}")
print(f"  control: uniform random string, same K={k1}, N={n1}, 3 seeds: IC = {['%.4f' % v for v in rnd1]}")

print()
print("=== Ad 2 (number code, 1871) ===")
ad2_groups = ["56", "717", "9362", "81720", "19736", "14", "618", "9", "77314",
              "390", "400", "272", "20", "211", "59", "91", "881", "460", "80",
              "401", "70", "447", "415", "91", "437", "801", "10031", "874", "92",
              "871", "2391", "941", "72050", "67321", "438921", "150"]
report("ad2 number groups", ad2_groups)
print("  (digit/number code, not letters -- no English-corpus control run per brief)")

print()
print("=== Ad 3 (1875-05-08, letter pseudo-words) ===")
ad3_text = ("StrCatokwacopaOlcabrokorlestedCoomemegaSesipyyocashostikrRepItedconlecmistrl"
            "HrsclamcaselcluchozametMoprediscoContoladsemotIadfilisatQftCagapBalmnopsemsov"
            "ApHodsamIopotonrogfimsecharsenrTolshrItedjolecmistrlDingDeclonEreflodbr")
ad3_letters = [c.upper() for c in ad3_text if c.isalpha()]
n3, k3, ic3 = report("ad3 letters", ad3_letters)
eng3 = english_letters(HOLMES, n3)
rnd3 = uniform_random(k3, n3)
print(f"  control: English text, same N={n3}, 3 seeds: IC = {['%.4f' % v for v in eng3]}")
print(f"  control: uniform random string, same K={k3}, N={n3}, 3 seeds: IC = {['%.4f' % v for v in rnd3]}")

print()
print("=== Ad 4 (1875-05-20, letter pseudo-words; plaintext tail excluded) ===")
ad4_text = ("UmemPoayatlgertyDpeatcnrftinNvtinrdnDmlurpinrtrcamnrEtdAtndngtnsurs"
            "OtenpuEtfdorshpxnNdtsfindseseoCotegrTsvlysdinlgeNgtndusdendoEdrstneirs"
            "UiNdtedIolapstedttocAPYxnWtubtrfftrstendinhofsvmnrDilyAtdwtsursOatvpu"
            "YAratiRileohmae")
ad4_letters = [c.upper() for c in ad4_text if c.isalpha()]
n4, k4, ic4 = report("ad4 letters (cipher portion only)", ad4_letters)
eng4 = english_letters(HOLMES, n4)
rnd4 = uniform_random(k4, n4)
print(f"  control: English text, same N={n4}, 3 seeds: IC = {['%.4f' % v for v in eng4]}")
print(f"  control: uniform random string, same K={k4}, N={n4}, 3 seeds: IC = {['%.4f' % v for v in rnd4]}")
