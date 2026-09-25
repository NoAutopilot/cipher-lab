#!/usr/bin/env python3
"""LANE R8 DSN (25 Sept 2026): compare the syllabary target decodes (families/syllabary-<seed>.txt) across seeds and
against chance: cross-seed agreement per token and per letter, hits of common Italian words of five letters or more
against three shuffles of each decode, and each run's score per symbol from the file header.
  python3 ciphers/fr2933-salviati-1525/dsn_compare.py [--prefix irregular] [seeds...]   (default 1 2 3)"""
import json, os, random, re, sys
D = os.path.dirname(os.path.abspath(__file__))
PREFIX = "syllabary" + (sys.argv.pop(sys.argv.index("--prefix") + 1).join(["-", ""]) if "--prefix" in sys.argv else "")
if "--prefix" in sys.argv: sys.argv.remove("--prefix")
seeds = [int(s) for s in sys.argv[1:]] or [1, 2, 3]
WORDS = ("della delle dello questo questa quello quella essere hanno havere sopra molto tutto tutti anche perche quando "
         "prima dopo senza contro verso ancora signore signor maesta papa cesare imperatore denari lettere").split()


def load(seed):
    lines = open(f"{D}/families/{PREFIX}-{seed}.txt", encoding="utf-8").read().splitlines()
    head = [l for l in lines if l.startswith("#")]
    body = [l for l in lines if not l.startswith("#")]
    info = {}  # the info line is cut at 2000 chars by family_run.py, so pull the fields by regex
    if len(head) > 1:
        for k in ("score_per_symbol", "score_per_letter", "symbols", "letters"):
            m = re.search(rf'"{k}": (-?[0-9.]+)', head[1]); info[k] = float(m.group(1)) if m else None
        info["key"] = dict(re.findall(r'"(M[^"]+)": "([a-z])"', head[1]))
    m = re.search(r"score (-?[0-9.]+)", head[0])
    return body, info, float(m.group(1)) if m else None


def hits(text, rng=None):
    if rng:
        t = list(text); rng.shuffle(t); text = "".join(t)
    return sum(text.count(w) for w in WORDS)


decs = {s: load(s) for s in seeds}
for s, (body, info, sc) in decs.items():
    text = "".join(body)
    sh = [hits(text, random.Random(k)) for k in (1, 2, 3)]
    print(f"seed {s}: score {sc} per symbol {info.get('score_per_symbol')} per letter {info.get('score_per_letter')} "
          f"symbols {info.get('symbols')} letters {len(text)}; word hits {hits(text)} vs shuffles {sh}; first 80: {text[:80]}")
    vow = {k: v for k, v in (info.get("key") or {}).items() if k.startswith("M")}
    print("   mark -> vowel:", " ".join(f"{k[1:]}={v}" for k, v in sorted(vow.items(), key=lambda kv: kv[0])[:14]))
for i, a in enumerate(seeds):
    for b in seeds[i + 1:]:
        ba, bb = decs[a][0], decs[b][0]
        tok = let = n_tok = n_let = 0
        for la, lb in zip(ba, bb):
            n_let += max(len(la), len(lb)); let += sum(x == y for x, y in zip(la, lb))
        print(f"seeds {a}/{b}: letter agreement {let / max(1, n_let):.1%} over {n_let} letters")
