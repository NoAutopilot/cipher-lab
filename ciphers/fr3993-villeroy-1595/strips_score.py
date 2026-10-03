#!/usr/bin/env python3
"""VILL-STRIPS (3 Oct 2026; VILL-7280 added the canvas f159 table, keys/key_f159_letters.tsv, same rules, fr3995/PREREG-VILL-7280.md): decode the target's figure tokens with the fr.3995 f.74v / f.104v letter strips
(keys/key_f74r_letters.tsv, keys/key_f104r_letters.tsv), score with the fr16 4-gram model of tools/judge_plaintext.py,
rank against 200 value-shuffled keys, and run the PREREG-VILL-STRIPS power control (20 synthetic French texts at the
target's own length and coverage, at the strip's measured reader error) first.
Segmentation: within the token stream, a figure followed by a figure is read as a two-figure code when that code is in
the key, otherwise as a one-figure code; 'o' is 0; non-figure signs are dropped (no identical sign certified, rule 2).
Usage: python3 strips_score.py [--seed 1]   (writes strips_score.tsv; --check exits 1 if the committed TSV is stale)"""
import sys, random, statistics, importlib.util
from pathlib import Path
HERE = Path(__file__).resolve().parent; ROOT = HERE.parents[1]
spec = importlib.util.spec_from_file_location("jp", ROOT / "tools/judge_plaintext.py"); jp = importlib.util.module_from_spec(spec); spec.loader.exec_module(jp)
DIG = set("123456789o")

def load_key(p):
    k, g = {}, {}
    for l in open(p):
        if l.startswith("#") or not l.strip(): continue
        c, v, gr = l.rstrip("\n").split("\t"); k[c] = v; g[c] = gr
    return k, g

def tokens():
    out = []
    for fn in ["bourdeau/ct_f148r.txt", "bourdeau/ct_f148v_149r.txt"]:
        for line in open(HERE / fn):
            if line.startswith("#") or not line.strip(): continue
            out.append(line.split())
    return out

def segment(lines, key):
    codes = []
    for toks in lines:
        i = 0
        while i < len(toks):
            t = toks[i]
            if t in DIG:
                if i + 1 < len(toks) and toks[i + 1] in DIG:
                    c = (t + toks[i + 1]).replace("o", "0")
                    if c in key: codes.append(c); i += 2; continue
                codes.append(t.replace("o", "0"))
            i += 1
    return codes

def decode(codes, key):
    return "".join(key[c] for c in codes if c in key and key[c] != "NULL")

def shuffled(key, rnd):
    cs = [c for c in key if key[c] != "NULL"]; vs = [key[c] for c in cs]; rnd.shuffle(vs)
    k = dict(key); k.update(zip(cs, vs)); return k

def rank_z(codes, key, model, rnd, n=200):
    real = model.score(decode(codes, key))
    sh = [model.score(decode(codes, shuffled(key, rnd))) for _ in range(n)]
    rank = 1 + sum(s >= real for s in sh)
    z = (real - statistics.mean(sh)) / (statistics.pstdev(sh) or 1e-9)
    return real, rank, z

def synth(model, key, grade, n_tokens, cover, rnd):
    """French window of the target's figure-token count, enciphered with the key; tokens at the target's non-figure share
    become a sign token; the token stream goes through the same segmentation as the target; codes on I-graded cells are corrupted to a random code at the strip's reader error."""
    inv = {}
    for c, v in key.items():
        if v != "NULL" and c.isdigit(): inv.setdefault(v, []).append(c)
    err = sum(1 for c in key if grade[c] == "I") / len(key)
    allc = [c for c in key if c.isdigit()]
    j = rnd.randrange(0, len(model.raw) - 2 * n_tokens); txt = model.raw[j:j + n_tokens]
    toks = []
    for ch in txt:
        if ch not in inv or rnd.random() > cover: toks.append("S"); continue
        c = rnd.choice(inv[ch])
        if rnd.random() < err: c = rnd.choice(allc)
        toks.extend("o" if d == "0" else d for d in c)
    return segment([toks], key), err

def main():
    rnd = random.Random(1)
    model = jp.NgramModel([jp.read_corpus(p) for p in jp.LANG_CORPORA["fr"]])
    lines = tokens(); ntok = sum(len(t) for t in lines); nfig = sum(1 for t in lines for x in t if x in DIG)
    rows = ["strip\tcoverage\treader_err\tpower_rank1_of_20\tpower_verdict\ttarget_letters\ttarget_score\ttarget_rank\ttarget_z\tverdict"]
    for name, kp in [("f74v(no.40)", "keys/key_f74r_letters.tsv"), ("f104v(no.58)", "keys/key_f104r_letters.tsv"), ("f159(no.43?)", "keys/key_f159_letters.tsv")]:
        key, grade = load_key(HERE / kp)
        cov = nfig / ntok
        if cov < 0.5:
            rows.append(f"{name}\t{cov:.3f}\t\t\t\t\t\t\t\tnot testable"); continue
        codes = segment(lines, key); L = len(decode(codes, key))
        p, err = 0, 0
        for s in range(20):
            sc, err = synth(model, key, grade, int(L / cov), cov, rnd)
            if rank_z(sc, key, model, rnd)[1] == 1: p += 1
        if p < 16:
            rows.append(f"{name}\t{cov:.3f}\t{err:.3f}\t{p}\tnon-test\t{L}\t\t\t\tstop (power below 16/20)"); continue
        real, rank, z = rank_z(codes, key, model, rnd)
        v = "PASS" if rank == 1 and z >= 3 else "FAIL"
        rows.append(f"{name}\t{cov:.3f}\t{err:.3f}\t{p}\tpowered\t{L}\t{real:.3f}\t{rank}/201\t{z:.2f}\t{v}")
    out = "\n".join(rows) + "\n"
    f = HERE / "strips_score.tsv"
    if "--check" in sys.argv:
        sys.exit(0 if f.exists() and f.read_text() == out else 1)
    f.write_text(out); print(out)
    for name, kp in [("f74v", "keys/key_f74r_letters.tsv"), ("f104v", "keys/key_f104r_letters.tsv"), ("f159", "keys/key_f159_letters.tsv")]:
        key, _ = load_key(HERE / kp); print(name, decode(segment(lines, key), key)[:160])

if __name__ == "__main__":
    main()
