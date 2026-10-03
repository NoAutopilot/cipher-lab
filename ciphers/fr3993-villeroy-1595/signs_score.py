#!/usr/bin/env python3
"""VILL-SIGNS (3 Oct 2026, fr3995/PREREG-VILL-SIGNS.md): strips_score.py's method with the f159 table's figures plus the
target signs certified against it (keys/key_f159_full.tsv: L = r, w = m, + = x). Certified sign tokens are kept as codes;
segmentation otherwise as strips_score.segment. Power control first (20 synthetic French texts, rank 1 of 201); below 16/20
the target is not scored. Usage: python3 signs_score.py [--check]  (writes signs_score.tsv; --check exits 1 if stale)"""
import sys, random
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import strips_score as ss
DIG = ss.DIG

def load_key(p):
    k, g = {}, {}
    for l in open(p):
        if l.startswith("#") or not l.strip(): continue
        c, v, gr = l.rstrip("\n").split("\t")[:3]; k[c] = v; g[c] = gr
    return k, g

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
            elif t in key: codes.append(t)
            i += 1
    return codes

def synth(model, key, grade, n_tokens, cover, rnd):
    inv = {}
    for c, v in key.items(): inv.setdefault(v, []).append(c)
    err = sum(1 for c in key if grade[c] == "I") / len(key)
    allc = list(key)
    j = rnd.randrange(0, len(model.raw) - 2 * n_tokens); txt = model.raw[j:j + n_tokens]
    toks = []
    for ch in txt:
        if ch not in inv or rnd.random() > cover: toks.append("S"); continue
        c = rnd.choice(inv[ch])
        if rnd.random() < err: c = rnd.choice(allc)
        toks.extend(["o" if d == "0" else d for d in c] if c.isdigit() else [c])
    return segment([toks], key), err

def main():
    rnd = random.Random(1)
    model = ss.jp.NgramModel([ss.jp.read_corpus(p) for p in ss.jp.LANG_CORPORA["fr"]])
    key, grade = load_key(HERE / "keys/key_f159_full.tsv")
    lines = ss.tokens(); ntok = sum(len(t) for t in lines)
    nkey = sum(1 for t in lines for x in t if x in DIG or x in key); cov = nkey / ntok
    codes = segment(lines, key); L = len(ss.decode(codes, key))
    hdr = "key\tcoverage\treader_err\tpower_rank1_of_20\tpower_verdict\ttarget_letters\ttarget_score\ttarget_rank\ttarget_z\tverdict"
    p, err = 0, 0
    for s in range(20):
        sc, err = synth(model, key, grade, int(L / cov), cov, rnd)
        if ss.rank_z(sc, key, model, rnd)[1] == 1: p += 1
    if cov < 0.5: row = f"f159+signs\t{cov:.3f}\t\t\t\t\t\t\t\tnot testable"
    elif p < 16: row = f"f159+signs\t{cov:.3f}\t{err:.3f}\t{p}\tnon-test\t{L}\t\t\t\tstop (power below 16/20)"
    else:
        real, rank, z = ss.rank_z(codes, key, model, rnd)
        row = f"f159+signs\t{cov:.3f}\t{err:.3f}\t{p}\tpowered\t{L}\t{real:.3f}\t{rank}/201\t{z:.2f}\t" + ("PASS" if rank == 1 and z >= 3 else "FAIL")
    out = hdr + "\n" + row + "\n"
    f = HERE / "signs_score.tsv"
    if "--check" in sys.argv: sys.exit(0 if f.exists() and f.read_text() == out else 1)
    f.write_text(out); print(out); print("decode:", ss.decode(codes, key)[:200])

if __name__ == "__main__":
    main()
