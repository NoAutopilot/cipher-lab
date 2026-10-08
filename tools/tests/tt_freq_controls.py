#!/usr/bin/env python3
"""TT-FREQ known-answer controls for tools/freq.py --split-at auto (C1), --contacts --vowels (C4) and
--repeats with gaps (C5); pass lines pre-registered in tools/tests/PREREG-TT-FREQ.md (pushed first).

Cases: Ormonde (Clanricarde to Ormonde, 1643/4), ciphertext and decipherment as printed by S. Tomokiyo,
Cryptiana, sources/cryptiana/web/ormonde.htm ("Cipher in Question", "Deciphered Text"; his own two-digit
reduction, "Reduction of the Problem"); and Lodewijk van Nassau 1574 siblings 4613/4615
(ciphers/lodewijk-van-nassau-1573-74/ciphertext_sib.tsv, key.tsv C-graded from the period decipherment).
Writes tools/tests/TT-FREQ-controls.tsv. Run: python3 tools/tests/tt_freq_controls.py"""
import csv
import os
import random
import re
import statistics
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import freq  # noqa: E402

VOWELS = set("aeiouy")
SEEDS = range(20)
OUT = os.path.join(ROOT, "tools", "tests", "TT-FREQ-controls.tsv")


def ormonde():
    txt = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "html2text.py"),
                          os.path.join(ROOT, "sources", "cryptiana", "web", "ormonde.htm")],
                         capture_output=True, text=True).stdout.splitlines()
    a = next(i for i, l in enumerate(txt) if "The fragment in cipher is as follows" in l)
    b = next(i for i, l in enumerate(txt) if l.startswith("### Reduction"))
    groups = [g for l in txt[a + 1:b] for g in l.split()]
    toks, word_of = [], []
    for w, g in enumerate(groups):
        i = 0
        while i < len(g):
            n = 3 if g[i] == "1" else 2
            toks.append(g[i:i + n])
            word_of.append(w)
            i += n
    c = next(i for i, l in enumerate(txt) if l.startswith("### Deciphered Text"))
    key = {}
    for code, val in re.findall(r"(\d+) < ([^>]+?) >", "\n".join(txt[c:])):
        v = val.split("->")[0].strip()
        key[code] = v if re.fullmatch(r"[a-z]", v) else ("NULL" if v == "-" else v.upper())
    return toks, word_of, key


def lodewijk():
    d = os.path.join(ROOT, "ciphers", "lodewijk-van-nassau-1573-74")
    toks = [r["token"] for r in csv.DictReader(open(os.path.join(d, "ciphertext_sib.tsv"), encoding="utf-8"),
                                                delimiter="\t") if r["token"].isdigit()]
    key = {}
    for r in csv.reader(open(os.path.join(d, "key.tsv"), encoding="utf-8"), delimiter="\t"):
        if r and r[0].isdigit() and len(r) > 1:
            key[r[0]] = r[1]
    return toks, key


def value_null(toks, seed):
    r = random.Random(seed)
    vals = [int(t) for t in toks]
    lo, hi = min(vals), max(vals)
    return [str(r.randint(lo, hi)) for _ in vals]


def order_null(toks, seed):
    t = list(toks)
    random.Random(seed).shuffle(t)
    return t


def best_split(toks):
    r = freq.split_auto(toks)
    single = r["singles"][0] if r["singles"] else (0.0, None)
    band = r["band"]
    return single, band


def vowel_acc(toks, key, n_letters=20):
    c = freq.Counter(toks)
    order = [t for t, _ in c.most_common()]
    letters = [t for t in order if re.fullmatch(r"[a-z]", key.get(t, ""))][:n_letters]
    k = max(order.index(t) for t in letters) + 1
    cls = {t: cl for t, cl, _ in freq.sukhotin_classes(toks, k)}
    ok = sum((cls[t] == "V") == (key[t] in VOWELS) for t in letters)
    return ok / len(letters), cls, letters


def maximal_repeats(toks, n_min):
    allr = freq.ngram_repeats_all(toks, n_min)
    out = []
    for L, reps in allr.items():
        longer = allr.get(L + 1, {})
        right_ext = {tuple(p) for p in longer.values()}
        for g, pos in reps.items():
            if tuple(pos) in right_ext:
                continue  # extends right with identical positions
            prev = {toks[p - 1] if p > 0 else None for p in pos}
            if len(prev) == 1 and None not in prev:
                continue  # extends left
            out.append((L, g, pos))
    return out


def main():
    rows = []
    # ---------- Ormonde
    toks, word_of, key = ormonde()
    letters = sorted(int(k) for k, v in key.items() if re.fullmatch(r"[a-z]", v))
    nulls = sorted(int(k) for k, v in key.items() if v == "NULL")
    words = sorted(int(k) for k, v in key.items() if len(v) > 1 and v != "NULL")
    print(f"ormonde: {len(toks)} tokens, letters {letters[0]}-{letters[-1]}, nulls {nulls[0]}-{nulls[-1]}, "
          f"word codes {words[0]}-{words[-1]}; unkeyed tokens {sorted(set(t for t in toks if t not in key))}")
    edge = 90
    (g, n), band = best_split(toks)
    errs = [abs(n - edge) if n else 999, abs(band[2] - edge) if band else 999]
    null_hits = 0
    null_ns = []
    for s in SEEDS:
        (gn, nn), bn = best_split(value_null(toks, s))
        prop = [nn if gn >= 10 else None, bn[2] if bn and bn[0] >= 10 else None]
        null_ns.append(nn if gn >= 10 else "none")
        if any(p is not None and abs(p - edge) <= 3 for p in prop):
            null_hits += 1
    c1o = min(errs) <= 3 and null_hits <= 2
    rows.append(["C1", "ormonde", f"single N={n} gain={g:.1f}; band=[{band[1]},{band[2]}) gain={band[0]:.1f}",
                 f"|err| single={errs[0]} band={errs[1]} (true edge {edge})",
                 f"value-null: {null_hits}/20 seeds land within 3 of {edge}; null N: {null_ns}",
                 "PASS" if c1o else "FAIL"])
    # C4
    acc, cls, lets = vowel_acc(toks, key)
    nulls_acc = [vowel_acc(order_null(toks, s), key)[0] for s in SEEDS]
    c4o = acc >= 0.75 and cls.get("78") == "V" and acc - statistics.mean(nulls_acc) >= 0.15
    rows.append(["C4", "ormonde", f"sukhotin accuracy {acc:.3f} on 20 top letter tokens; 78 -> {cls.get('78')}",
                 "V-classed: " + ",".join(f"{t}={key[t]}" for t in lets if cls[t] == "V"),
                 f"order-null mean {statistics.mean(nulls_acc):.3f} (min {min(nulls_acc):.3f}, max {max(nulls_acc):.3f})",
                 "PASS" if c4o else "FAIL"])
    # C5
    nrep = sum(len(v) for v in freq.ngram_repeats_all(toks, 3).values())
    null_rep = sorted(sum(len(v) for v in freq.ngram_repeats_all(order_null(toks, s), 3).values()) for s in SEEDS)
    p95 = null_rep[int(0.95 * (len(null_rep) - 1) + 0.5)]
    mx = maximal_repeats(toks, 3)
    plain = ["".join(key.get(t, "?") if re.fullmatch(r"[a-z]", key.get(t, "")) else "[" + key.get(t, "?") + "]"
                     for t, w in zip(toks, word_of) if w == wi) for wi in range(max(word_of) + 1)]
    good = 0
    detail = []
    for L, gram, pos in mx:
        ok = True
        for p in pos:
            ws = word_of[p:p + L]
            within = len(set(ws)) == 1
            starts = p == 0 or word_of[p - 1] != word_of[p]
            ends = p + L == len(toks) or word_of[p + L] != word_of[p + L - 1]
            if not (within or (starts and ends)):
                ok = False
        if ok and len(set(word_of[pos[0]:pos[0] + L])) == 1:
            ok = len({plain[word_of[p]] for p in pos}) == 1
        good += ok
        detail.append(f"{' '.join(gram)}={''.join(plain[w] for w in sorted(set(word_of[pos[0]:pos[0]+L])))}"
                      f"x{len(pos)}gaps{freq.position_gaps(pos)}{'' if ok else '(off-word)'}")
    share = good / len(mx) if mx else 0.0
    c5o = nrep > p95 and share >= 0.6
    rows.append(["C5", "ormonde", f"repeated n-grams >=3: {nrep}; maximal {len(mx)}, on a repeated word {good} ({share:.2f})",
                 "; ".join(detail), f"order-null counts {null_rep} (p95 {p95})", "PASS" if c5o else "FAIL"])
    # ---------- Lodewijk
    ltoks, lkey = lodewijk()
    edge = 121
    (g, n), band = best_split(ltoks)
    err = abs(n - edge) if n else 999
    null_hits, null_ns = 0, []
    for s in SEEDS:
        (gn, nn), bn = best_split(value_null(ltoks, s))
        null_ns.append(nn if gn >= 10 else "none")
        if gn >= 10 and abs(nn - edge) <= 5:
            null_hits += 1
    c1l = err <= 5 and null_hits <= 2
    rows.append(["C1", "lodewijk-sib", f"{len(ltoks)} numeric tokens; single N={n} gain={g:.1f}; band=[{band[1]},{band[2]}) gain={band[0]:.1f}",
                 f"|err| single={err} (true edge {edge})",
                 f"value-null: {null_hits}/20 seeds within 5; null N: {null_ns}", "PASS" if c1l else "FAIL"])
    acc, cls, lets = vowel_acc(ltoks, lkey)
    nulls_acc = [vowel_acc(order_null(ltoks, s), lkey)[0] for s in SEEDS]
    rows.append(["C4", "lodewijk-sib", f"sukhotin accuracy {acc:.3f} on 20 top letter tokens",
                 "V-classed: " + ",".join(f"{t}={lkey[t]}" for t in lets if cls[t] == "V"),
                 f"order-null mean {statistics.mean(nulls_acc):.3f} (min {min(nulls_acc):.3f}, max {max(nulls_acc):.3f})",
                 "PASS" if (acc >= 0.75 and acc - statistics.mean(nulls_acc) >= 0.15) else "FAIL"])
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("# TT-FREQ controls, tools/tests/tt_freq_controls.py; pass lines tools/tests/PREREG-TT-FREQ.md\n")
        f.write("check\tcase\tresult\tdetail\tnull\tverdict\n")
        for r in rows:
            f.write("\t".join(r) + "\n")
    for r in rows:
        print("\t".join(x if len(x) < 400 else x[:400] + "..." for x in r))


if __name__ == "__main__":
    main()
