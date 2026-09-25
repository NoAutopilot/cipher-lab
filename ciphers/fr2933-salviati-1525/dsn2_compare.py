#!/usr/bin/env python3
"""LANE R8 DSN2 (25 Sept 2026): compare the DSN2 syllabary target decodes across seeds and against chance, as
dsn_compare.py does for DSN, but on the per-param decode files family_run.py now writes
(families/syllabary-<seed>-<params>.txt). Cross-seed letter agreement, hits of common Italian words of five letters
or more against three shuffles, score per symbol and the mark map from each file's header.
  python3 ciphers/fr2933-salviati-1525/dsn2_compare.py "err=0.05,marks=mixed" [seeds...]   (default 1 2 3)"""
import os, random, re, sys
D = os.path.dirname(os.path.abspath(__file__))
params = sys.argv[1]
seeds = [int(s) for s in sys.argv[2:]] or [1, 2, 3]
WORDS = ("della delle dello questo questa quello quella essere hanno havere sopra molto tutto tutti anche perche quando "
         "prima dopo senza contro verso ancora signore signor maesta papa cesare imperatore denari lettere").split()


def load(seed):
    path = f"{D}/families/syllabary-{seed}-{params}.txt"
    if not os.path.exists(path):
        return None
    lines = open(path, encoding="utf-8").read().splitlines()
    head = [l for l in lines if l.startswith("#")]
    body = [l for l in lines if not l.startswith("#")]
    info = {}
    if len(head) > 1:
        for k in ("score_per_symbol", "symbols", "letters"):
            m = re.search(rf'"{k}": (-?[0-9.]+)', head[1]); info[k] = float(m.group(1)) if m else None
        info["key"] = dict(re.findall(r'"(M[^"]+)": "([a-z])"', head[1]))
    m = re.search(r"control mean ([0-9.]+)", head[0]); info["control"] = float(m.group(1)) if m else None
    return body, info


def hits(text, rng=None):
    if rng:
        t = list(text); rng.shuffle(t); text = "".join(t)
    return sum(text.count(w) for w in WORDS)


decs = {s: load(s) for s in seeds}
decs = {s: v for s, v in decs.items() if v}
for s, (body, info) in decs.items():
    text = "".join(body)
    sh = [hits(text, random.Random(k)) for k in (1, 2, 3)]
    key = info.get("key") or {}
    marks = {k[1:]: v for k, v in key.items() if k in ("M~", "M1", "M5", "M7", "M#", "M+", "Mdot", "Mo", "Mot")}
    print(f"seed {s}: control {info.get('control')} per symbol {info.get('score_per_symbol')} symbols {info.get('symbols')} "
          f"letters {len(text)}; word hits {hits(text)} vs shuffles {sh}; marks {marks}; first 80: {text[:80]}")
ss = sorted(decs)
for i in range(len(ss)):
    for j in range(i + 1, len(ss)):
        a, b = "".join(decs[ss[i]][0]), "".join(decs[ss[j]][0])
        n = min(len(a), len(b))
        print(f"letter agreement seeds {ss[i]}/{ss[j]}: {sum(x == y for x, y in zip(a, b)) / max(1, n):.3f} (over {n} letters)")
