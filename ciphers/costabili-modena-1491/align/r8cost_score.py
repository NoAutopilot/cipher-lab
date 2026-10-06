#!/usr/bin/env python3
"""R8-COST (6 Oct 2026): score the two blind P4 passes per PREREG-R8-COST.md.
usage: r8cost_score.py passA.tsv passB.tsv [--out r8cost_score.tsv]
Joins each line's overlapping segment crops (drops '|' cut signs; drops the longest suffix/prefix repeat of <= 6 tokens
between neighbours), aligns A vs B per line with difflib on sign tokens, and reports err_2reader, C coverage
(against key_n9cos2.tsv) and the decode-gate verdict; writes per-line agreed sequences with C values."""
import csv, difflib, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
PUNCT = {".", ",", ":", ";", "/", "|"}

def key():
    k = {}
    for r in csv.DictReader(open(os.path.join(HERE, "key_n9cos2.tsv")), delimiter="\t"):
        k[r["sign"]] = (r["value"], r["grade"])
    return k

def tokens(signs):
    out = []
    for grp in signs.split():
        if grp.startswith("["):
            out.append(("CLEAR", grp)); continue
        parts = [p for p in grp.split("_") if p]
        for i, p in enumerate(parts):
            if p in PUNCT: continue
            out.append(("SIGN", p))
        if parts: out.append(("SEP", " "))
    return out

def load(path):
    lines = {}
    for r in csv.DictReader(open(path), delimiter="\t"):
        m = re.match(r"(?:p4_)?(L\d)_s(\d+)", r["crop"])
        if not m: continue
        lines.setdefault(m.group(1), []).append((int(m.group(2)), r.get("signs") or "", r.get("gloss") or ""))
    joined = {}
    for ln, segs in lines.items():
        seq = []
        for _, s, _ in sorted(segs):
            t = [x for x in tokens(s)]
            sig = [x for x in t if x[0] == "SIGN"]
            prev = [x for x in seq if x[0] == "SIGN"]
            drop = 0
            for n in range(min(6, len(sig), len(prev)), 0, -1):
                if [x[1] for x in prev[-n:]] == [x[1] for x in sig[:n]]:
                    drop = n; break
            k = 0
            for x in t:
                if x[0] == "SIGN" and k < drop:
                    k += 1; continue
                seq.append(x)
        joined[ln] = seq
    return joined, lines

def main():
    a, la = load(sys.argv[1]); b, lb = load(sys.argv[2])
    out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else None
    K = key()
    tot = eq = cov = 0; rows = []; dis = 0; samelen = 0
    for ln in sorted(set(a) | set(b)):
        sa = [x[1] for x in a.get(ln, []) if x[0] == "SIGN"]
        sb = [x[1] for x in b.get(ln, []) if x[0] == "SIGN"]
        sm = difflib.SequenceMatcher(None, sa, sb, autojunk=False)
        dec = []
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == "equal":
                for s in sa[i1:i2]:
                    tot += 1; eq += 1
                    v, g = K.get(s, ("?", "-"))
                    if g == "C": cov += 1; dec.append(v)
                    else: dec.append("[" + s + "]")
            else:
                n = max(i2 - i1, j2 - j1); tot += n
                if op == "replace" and i2 - i1 == j2 - j1:
                    samelen += i2 - i1; dis += i2 - i1
                dec.append("{" + "".join(sa[i1:i2]) + "/" + "".join(sb[j1:j2]) + "}")
        rows.append((ln, " ".join(sa), " ".join(sb), "".join(dec)))
    agree_pos = eq + samelen
    err = dis / agree_pos if agree_pos else float("nan")
    c = cov / tot if tot else 0.0
    print(f"aligned positions {tot}; A=B {eq}; same-length substitutions {dis}; err_2reader {err:.3f}")
    print(f"C coverage {cov}/{tot} = {c:.3f}; gate >= 0.80: {'PASS (decode)' if c >= 0.80 else 'FAIL (no running decode)'}")
    for r in rows: print("\t".join(r))
    if out:
        with open(out, "w") as f:
            f.write("line\tpassA_signs\tpassB_signs\tagreed_C_decode ([sign]=agreed non-C, {A/B}=split)\n")
            for r in rows: f.write("\t".join(r) + "\n")

if __name__ == "__main__":
    main()
