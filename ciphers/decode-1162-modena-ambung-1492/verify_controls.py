#!/usr/bin/env python3
"""VERIFY-MOD1162 (account 3, 3 Oct 2026): re-run of score_g.py G against variant controls and gloss readings.
Run from this folder: python3 verify_controls.py. Output pasted in AUDIT.md. Descriptive, not a new gate."""
import sys, random, statistics
sys.path.insert(0,'.')
import score_g as s
key, groups, gloss = s.load()
vals = {k:v for k,(v,g) in key.items()}
bands = {b: sorted(k for k,(v,g) in key.items() if g==b) for b in "CM"}
def ctrl(gl, seeds):
    out=[]
    for seed in seeds:
        r=random.Random(seed); d={}
        for b,ss in bands.items():
            vs=[vals[x] for x in ss]; r.shuffle(vs); d.update(zip(ss,vs))
        out.append(s.G(d,groups,gl)[0])
    out.sort(); return out
def rep(name, gl, seeds):
    g=s.G(vals,groups,gl)[0]; c=ctrl(gl,seeds)
    print(f"{name}: G={g:.4f} ctrl mean={statistics.mean(c):.4f} p99={c[int(.99*(len(c)-1))]:.4f} max={c[-1]:.4f} n>=G={sum(x>=g for x in c)}/{len(c)}")
rep("orig gloss, seeds 0-999", gloss, range(1000))
rep("orig gloss, seeds 50000-54999", gloss, range(50000,55000))
# DECODE doc 3593 (transcriber RP, 2020) gloss readings, independent of pass A
dg = dict(gloss)
dg["p1L01_1"]=("il goino d l noseoato d strugonio","letters")
dg["p1L05_1"]=("pocha esima","letters"); dg["p1L05_2"]=("pocha esima","letters")
dg["p1L06_1"]=("Le semipiano di lo acivescovo","letters")
dg["p1L06_3"]=("mi prorepitio","letters")
dg["p1L08_1"]=("famiglia dl arcivescovo","letters")
dg["p1L08_3"]=("ne comprino","letters")
rep("DECODE-3593 gloss, seeds 50000-54999", dg, range(50000,55000))
# tight gloss: only the words directly over each letter group (drop spill-over words)
tg = dict(gloss)
tg["p1L01_1"]=("il gouerno","letters"); tg["p1L05_1"]=("pocha","letters"); tg["p1L05_2"]=("estima","letters")
tg["p1L06_1"]=("lo Seruipiana","letters"); tg["p1L08_1"]=("famiglia","letters")
rep("tight gloss, seeds 50000-54999", tg, range(50000,55000))
# frequency null: each sign gets an independent Italian-frequency letter
freq="eeeeeeeeeeeaaaaaaaaaaaiiiiiiiiiiooooooooonnnnnnnlllllllrrrrrrrtttttttsssssscccccdddddpppuuuummmgvzbfh"
for name,gl in (("orig",gloss),("tight",tg)):
    g=s.G(vals,groups,gl)[0]; out=[]
    for seed in range(5000):
        r=random.Random(seed+90000); d={k:r.choice(freq) for k in vals}
        out.append(s.G(d,groups,gl)[0])
    out.sort(); print(f"freq-null {name}: G={g:.4f} mean={statistics.mean(out):.4f} p99={out[int(.99*4999)]:.4f} max={out[-1]:.4f} n>=G={sum(x>=g for x in out)}")
