#!/usr/bin/env python3
"""HEID-1623A: token/unit tables for the 1623 block (NA 1.01.02 inv. 6022 scans 166, 171), the 166-vs-171 witness control, the
marginal-note table, the alignment pairs for tools/interlinear_align.py, and the unit-grammar comparison with 1621.

usage: python3 build.py [--check]     (inputs recon_166.txt, recon_171.txt, note_recon.txt; ../heid1621g/units.tsv)
Rules: PREREG-HEID1623A.md. Token = numeral or single letter ([clear]/[sym] dropped). Witness control = difflib matched tokens /
max(len). S = control PASS and both readers agree (no '|' split) and the token aligns to an identical token in the other witness;
else M. No value is read; nothing here decodes. --check exits 1 if a committed output differs."""
import sys, os, difflib, io, csv, re, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, "..", "heid1621g"))
from units import read_recon, units_from_tokens, is_num, is_let  # heid1621g grammar, reused unchanged

def toks(name):
    return [t for t in read_recon_here(name) if is_num(t[2]) or is_let(t[2])]

def read_recon_here(name):  # read_recon reads from heid1621g's folder; same parser, this folder
    import units; old = units.H; units.H = H
    try: return read_recon(name)
    finally: units.H = old

def build():
    out = {}
    a, b = toks("recon_166.txt"), toks("recon_171.txt")
    sa, sb = [t[2] for t in a], [t[2] for t in b]
    sm = difflib.SequenceMatcher(None, sa, sb, autojunk=False)
    matched = sum(bl.size for bl in sm.get_matching_blocks()); agree = matched / max(len(sa), len(sb))
    PASS = agree >= 0.90
    ia = {}; ib = {}
    for bl in sm.get_matching_blocks():
        for k in range(bl.size): ia[bl.a + k] = bl.b + k; ib[bl.b + k] = bl.a + k
    def rows(T, other, peer):
        r = []
        for i, (line, pos, tok, alt) in enumerate(T):
            ok = PASS and not alt and i in other and not peer[other[i]][3]
            why = []
            if not PASS: why.append("witness control below gate")
            if alt: why.append(f"split {tok}|{alt}")
            if i not in other: why.append("no identical token in the other witness")
            elif peer[other[i]][3]: why.append("other witness split")
            r.append(dict(line=line, pos=pos, kind="num" if is_num(tok) else "let", token=tok, alt=alt,
                          confidence="S" if ok else "M", why="; ".join(why) or "readers agree; witnesses agree; control PASS"))
        return r
    cols = ["line", "pos", "kind", "token", "alt", "confidence", "why"]
    hdr = ("# NL-HaNA 1.01.02 inv. 6022 scan %s, Brederode, Straatsburg 12 Aug 1623 (Resolutien NR 6 p.260 res. 1721a). HEID-1623A, 16 Oct 2026:"
           " two blind Sonnet readers + reconciliation on native line crops. S = sign as transcribed (no value read); M = otherwise.\n")
    for scan, T, oth, peer in (("166", a, ia, b), ("171", b, ib, a)):
        s = io.StringIO(); s.write(hdr % scan); w = csv.DictWriter(s, cols, delimiter="\t", lineterminator="\n"); w.writeheader()
        for r in rows(T, oth, peer): w.writerow(r)
        out[f"ciphertext_6022_{scan}.tsv"] = s.getvalue()
    # witness diff table
    s = io.StringIO(); s.write("op\t166\t171\n")
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal": s.write(f"{op}\t{' '.join(sa[i1:i2])}\t{' '.join(sb[j1:j2])}\n")
    s.write(f"# matched {matched} / max({len(sa)}, {len(sb)}) = {agree:.3f}; gate 0.90: {'PASS' if PASS else 'FAIL'}\n")
    out["witness_166_171.tsv"] = s.getvalue()
    # note table
    s = io.StringIO(); s.write("# Marginal note beside the 171 block, HEID-1623A: two readers + reconciliation; every word grade M.\nline\tpos\tword\talt\tgrade\n")
    for ln in open(os.path.join(H, "note_recon.txt"), encoding="utf-8"):
        if ln.startswith("#") or not ln.strip(): continue
        L, rest = ln.rstrip("\n").split("\t", 1)
        for p, wd in enumerate(rest.split(), 1):
            w0, alt = (wd.split("|", 1) + [""])[:2]
            s.write(f"{L}\t{p}\t{w0}\t{alt}\tM\n")
    out["note_6022_171.tsv"] = s.getvalue()
    # unit grammar (heid1621g grammar) and coincidences with 1621
    u = {sc: units_from_tokens(read_recon_here(f"recon_{sc}.txt")) for sc in ("166", "171")}
    u21 = list(csv.DictReader((l for l in open(os.path.join(H, "..", "heid1621g", "units.tsv"), encoding="utf-8") if not l.startswith("#")), delimiter="\t"))
    ids21 = {r["unit"] for r in u21}
    s = io.StringIO(); s.write("scan\tunits\tP(pair+letter)\tS1(number+letter)\tR(run>2+letter)\tL(bare letter)\tN(numbers, no letter)\tcoinciding_1621_units\n")
    for sc, U in u.items():
        f = lambda k: sum(1 for x in U if x["form"].startswith(k))
        co = sorted({x["unit"] for x in U if x["unit"] in ids21})
        s.write(f"{sc}\t{len(U)}\t{f('P')}\t{f('S1')}\t{f('R')}\t{f('L')}\t{f('N')}\t{' '.join(co)}\n")
    nums23 = {t for t in sb + sa if is_num(t)}; nums21 = set()
    for r in u21:
        nums21 |= {x for x in r["numbers"].split(".") if x}
    s.write(f"# numerals 1623 (both witnesses): {len(nums23)}; also in 1621 units: {len(nums23 & nums21)} ({' '.join(sorted(nums23 & nums21, key=int))})\n")
    s.write(f"# 1621 units file: ../heid1621g/units.tsv ({len(u21)} rows)\n")
    out["grammar_1623_vs_1621.tsv"] = s.getvalue()
    return out, agree, PASS

if __name__ == "__main__":
    out, agree, PASS = build()
    bad = 0
    for fn, txt in out.items():
        p = os.path.join(H, fn)
        if "--check" in sys.argv:
            if not os.path.exists(p) or open(p, encoding="utf-8").read() != txt: print("STALE", fn); bad = 1
        else: open(p, "w", encoding="utf-8").write(txt)
    print(f"witness control 166 vs 171: {agree:.3f} ({'PASS' if PASS else 'FAIL'} at 0.90)")
    sys.exit(bad)
