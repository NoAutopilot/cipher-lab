#!/usr/bin/env python3
"""A1B-VILL-L (3 Oct 2026, fr3995/PREREG-VILL-TABLE.md addendum A1B-VILL-L): score the target with fr.3995 no.57's table
(canvas f200): Sillabes/Lettres doubles grid cells read alike by two blind readers (keys/key_f200_no57_syll.tsv, use=yes)
plus the 9 certified header signs (keys/key_f200_no57_signs.tsv). Segmentation as signs_score.py (two-figure code when in
the key, else one-figure; 'o' = 0; certified signs as codes; everything else dropped). fr 4-gram model of
tools/judge_plaintext.py; rank vs 200 value-shuffled keys; power control first (20 synthetic French texts at the target's
code count, plaintext parsed greedily into the key's units, longest first; gate 16/20 rank 1). PASS = rank 1 of 201 and
z >= 3. Rows: Bourdeau's transcription (bourdeau/) and A1B-VILL-TX2 pass B (tx2/passB.tsv; '?' stripped).
Unregistered secondary (disclosed): --errsweep re-runs the power control with 10/17/25 pct of codes replaced at random
(rule 3 error bracket: TX2 measured 16.8 pct pass-to-pass sign disagreement), seed 7, prints only.
Usage: python3 no57_score.py [--check | --errsweep]   (writes no57_score.tsv; --check exits 1 if stale)"""
import sys, random
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import strips_score as ss
DIG = ss.DIG

def load_key():
    k = {}
    for l in open(HERE / "keys/key_f200_no57_syll.tsv"):
        if l.startswith("#") or not l.strip(): continue
        c, v, g, use = l.rstrip("\n").split("\t")[:4]
        if use == "yes": k[c] = v
    for l in open(HERE / "keys/key_f200_no57_signs.tsv"):
        if l.startswith("#") or not l.strip(): continue
        c, v = l.split("\t")[:2]; k[c] = v
    return k

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
                c = t.replace("o", "0")
                if c in key: codes.append(c)
            elif t in key: codes.append(t)
            i += 1
    return codes

def passb_tokens():
    out = []
    for l in open(HERE / "tx2/passB.tsv"):
        f = l.rstrip("\n").split("\t")
        if len(f) < 2 or f[0] == "row": continue
        out.append([t.rstrip("?") for t in f[1].split() if t.rstrip("?")])
    return out

def synth(model, key, n_codes, rnd):
    inv = {}
    for c, v in key.items(): inv.setdefault(v, []).append(c)
    units = sorted(inv, key=len, reverse=True)
    j = rnd.randrange(0, len(model.raw) - 20 * n_codes); txt = model.raw[j:]
    toks, n, i = [], 0, 0
    while n < n_codes:
        for u in units:
            if txt.startswith(u, i):
                c = rnd.choice(inv[u]); toks.extend(["o" if d == "0" else d for d in c] if c.isdigit() else [c])
                i += len(u); n += 1; break
        else:
            toks.append("S"); i += 1
    return segment([toks], key)

def errsweep():
    rnd = random.Random(7)
    model = ss.jp.NgramModel([ss.jp.read_corpus(p) for p in ss.jp.LANG_CORPORA["fr"]]); key = load_key(); allc = list(key)
    print("err\tpower_rank1_of_20\tmean_z\tmin_z")
    for err in (0.10, 0.17, 0.25):
        p, zs = 0, []
        for s in range(20):
            codes = [rnd.choice(allc) if rnd.random() < err else c for c in synth(model, key, 319, rnd)]
            r = ss.rank_z(codes, key, model, rnd); p += r[1] == 1; zs.append(r[2])
        print(f"{err:.2f}\t{p}\t{sum(zs)/20:.2f}\t{min(zs):.2f}")

def main():
    if "--errsweep" in sys.argv: return errsweep()
    rnd = random.Random(1)
    model = ss.jp.NgramModel([ss.jp.read_corpus(p) for p in ss.jp.LANG_CORPORA["fr"]])
    key = load_key()
    hdr = "transcription\tkey_codes\ttokens\tcovered_tokens\tcoverage\tcodes\tpower_rank1_of_20\tpower_verdict\ttarget_letters\ttarget_score\ttarget_rank\ttarget_z\tverdict"
    rows = [hdr]; decs = []
    for name, lines in [("bourdeau", ss.tokens()), ("tx2_passB", passb_tokens())]:
        ntok = sum(len(t) for t in lines)
        codes = segment(lines, key)
        covered = sum(2 if c.isdigit() and len(c) == 2 else 1 for c in codes)
        cov = covered / ntok
        base = f"{name}\t{len(key)}\t{ntok}\t{covered}\t{cov:.3f}\t{len(codes)}"
        if cov < 0.5: rows.append(base + "\t\t\t\t\t\t\tnot testable"); continue
        p = sum(1 for s in range(20) if ss.rank_z(synth(model, key, len(codes), rnd), key, model, rnd)[1] == 1)
        dec = ss.decode(codes, key); decs.append((name, dec))
        if p < 16: rows.append(base + f"\t{p}\tnon-test\t{len(dec)}\t\t\t\tstop (power below 16/20)"); continue
        real, rank, z = ss.rank_z(codes, key, model, rnd)
        rows.append(base + f"\t{p}\tpowered\t{len(dec)}\t{real:.3f}\t{rank}/201\t{z:.2f}\t" + ("PASS" if rank == 1 and z >= 3 else "FAIL"))
    out = "\n".join(rows) + "\n"
    f = HERE / "no57_score.tsv"
    if "--check" in sys.argv: sys.exit(0 if f.exists() and f.read_text() == out else 1)
    f.write_text(out); print(out)
    for n, d in decs: print(n, "decode:", d[:240])

if __name__ == "__main__":
    main()
