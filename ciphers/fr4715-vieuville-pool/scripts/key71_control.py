#!/usr/bin/env python3
"""Known-answer gate for key no.71 (BnF fr.3995 f.133r) on the Vieuville-Nevers pool, as pre-registered in
witness/key71/PREREG.md (GAPS-fr4715-vieuville-pool-14, 3 Oct 2026).

  python3 scripts/key71_control.py [--key witness/key71/key71_reconciled.tsv] [--any-layer] [--seed 71]

A: our five C-graded glosses (7 Roy, 71 montolon, 93 Mr, 14 Card de bourbon, 22 Soissons) vs the key's entry for the
   same number in the layer the mark selects (MARK_LAYER; --any-layer: any word-code layer). Controls: all 120 gloss
   permutations (exact) and 10,000 uniform random codes 1-100 per gloss, same match rule.
B: the key's letter header vs key_vieuville_nevers.tsv's numeric letter rows; control 10,000 letter-label permutations.
Exit 0 = PASS, 3 = FAIL (the gate in PREREG.md). Also prints the M-graded pairs as data (never gating).
"""
import argparse, csv, itertools, random, re, sys, unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
KNOWN_C = [("7", "bar", "Roy"), ("71", "bar", "montolon"), ("93", "two dots", "Mr"),
           ("14", "bar", "Card de bourbon"), ("22", "bar", "Soissons")]
KNOWN_M = [("13", "bar", "Narre"), ("27", "bar", "nauarre?"), ("27", "bar", "Neuers"), ("52", "two dots", "Normandie"),
           ("44", "bar", "Roy"), ("99", "bar", "bours"), ("49", "two dots", "Champagne")]
MARK_LAYER = {"bar": "persons", "two dots": "places", "dot": "mots"}
ALIAS = {"mr": "monsieur", "mre": "monsieur", "mons": "monsieur", "card": "cardinal", "cal": "cardinal", "c": "cardinal",
         "narre": "nauarre", "d": "duc", "mme": "madame"}
STOP = {"de", "d", "le", "la", "l", "du", "des"}


def norm_tokens(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = s.replace("v", "u").replace("y", "i").replace("h", "").replace("'", " ")
    toks = [t for t in re.split(r"[^a-z]+", s) if t]
    out = set()
    for t in toks:
        t = ALIAS.get(t, t)
        t = ALIAS.get(t.replace("i", "y"), t)
        if t not in STOP:
            out.add(t)
    return out


def matches(gloss, entry):
    g, e = norm_tokens(gloss.rstrip("?")), norm_tokens(entry)
    return bool(g) and g <= e


def load_key(path):
    rows = [r for r in csv.DictReader((l for l in open(path, encoding="utf-8") if not l.startswith("#")), delimiter="\t")]
    word = {}
    letters = {}
    for r in rows:
        if r["layer"] == "letter":
            for n in r["number"].split("/"):
                if n.strip().isdigit():
                    letters[n.strip()] = r["entry"].strip().lower()
        else:
            for n in r["number"].split("/"):
                n = n.strip()
                if n.isdigit():
                    word.setdefault((r["layer"], str(int(n))), []).append(r["entry"])
    return word, letters


def a_score(word, pairs, any_layer):
    hits = []
    for code, mark, gloss in pairs:
        layers = {l for (l, c) in word} if any_layer else {MARK_LAYER[mark]}
        ok = any(matches(gloss, e) for l in layers for e in word.get((l, code), []))
        hits.append(ok)
    return hits


def p95(xs):
    xs = sorted(xs)
    return xs[int(0.95 * (len(xs) - 1))]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--key", default=str(HERE / "witness/key71/key71_reconciled.tsv"))
    ap.add_argument("--any-layer", action="store_true")
    ap.add_argument("--seed", type=int, default=71)
    a = ap.parse_args()
    rng = random.Random(a.seed)
    word, letters = load_key(a.key)

    hits = a_score(word, KNOWN_C, a.any_layer)
    real_a = sum(hits)
    print("A known answer (C):", " ".join(f"{c}{'=' if h else '!='}{g}" for (c, _, g), h in zip(KNOWN_C, hits)))
    perm = []
    glosses = [g for _, _, g in KNOWN_C]
    for p in itertools.permutations(range(5)):
        pairs = [(KNOWN_C[i][0], KNOWN_C[i][1], glosses[p[i]]) for i in range(5)]
        perm.append(sum(a_score(word, pairs, a.any_layer)))
    rnd = []
    for _ in range(10000):
        pairs = [(str(rng.randint(1, 100)), m, g) for _, m, g in KNOWN_C]
        rnd.append(sum(a_score(word, pairs, a.any_layer)))
    pa, pr = p95(perm), p95(rnd)
    print(f"A REAL {real_a}/5 | permutation (120, exact) mean {sum(perm)/len(perm):.3f} p95 {pa} max {max(perm)}"
          f" | random-code (10000) mean {sum(rnd)/len(rnd):.3f} p95 {pr} max {max(rnd)} | layer rule: "
          f"{'any word layer' if a.any_layer else 'mark-selected'}")

    tom = {}
    for r in csv.DictReader((l for l in open(HERE.parent / "fr4715-montholon-1589/keys/key_vieuville_nevers.tsv",
                                             encoding="utf-8") if not l.startswith("#")), delimiter="\t"):
        if r["sign"].strip().isdigit():
            tom[r["sign"].strip()] = r["value"].strip().lower()
    agree = sum(1 for s, v in tom.items() if letters.get(s) == v)
    real_b = agree / len(tom)
    codes = list(letters)
    vals = [letters[c] for c in codes]
    ctrl = []
    for _ in range(10000):
        rng.shuffle(vals)
        m = dict(zip(codes, vals))
        ctrl.append(sum(1 for s, v in tom.items() if m.get(s) == v) / len(tom))
    pb = p95(ctrl)
    dis = [f"{s}:{v}/{letters.get(s, '-')}" for s, v in sorted(tom.items(), key=lambda x: int(x[0])) if letters.get(s) != v]
    print(f"B REAL {agree}/{len(tom)} = {real_b:.3f} | label permutation (10000) mean {sum(ctrl)/len(ctrl):.3f} p95 {pb:.3f}"
          f" | disagreements (Tomokiyo/key71): {' '.join(dis) or 'none'}")

    mh = a_score(word, KNOWN_M, a.any_layer)
    print("M pairs (data, not gating):", " ".join(f"{c}{'=' if h else '!='}{g}" for (c, _, g), h in zip(KNOWN_M, mh)))
    ok = real_a >= 4 and real_a > pa and real_a > pr and real_b >= 0.80 and real_b > pb
    print("GATE", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 3)


if __name__ == "__main__":
    main()
