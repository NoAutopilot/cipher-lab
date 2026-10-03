#!/usr/bin/env python3
"""A1B-VILL-M (3 Oct 2026, fr3995/PREREG-VILL-TABLE.md addendum A1B-VILL-M): score the target with fr.3995 no.57's full table
under the combined parse: inside each digit run, three digits reading 100-353 (first not 'o') = one nomenclator code (decodes
to its agreed word from keys/key_f200_no57_nomen.tsv, else to nothing), otherwise no57_score's 1-2-figure rule; certified header
signs as codes. Null: 200 keys with values permuted within class (syllable/double/sign vs nomenclator). Power first: 20 synthetic
French texts (word-tokenised 'fr' corpora; an agreed nomenclator word -> its code, other words greedily into syllable/double/
letter units, absent units -> a dropped sign token) at the target's code count, through the same parse; gate 16/20 rank 1.
PASS = rank 1 of 201 and z >= 3. Rows: Bourdeau (bourdeau/) and A1B-VILL-TX2 pass B.
Also builds keys/key_f200_no57_nomen.tsv from fr3995/vill_m_reader{A,B}.tsv (agreed = same normalised first variant).
Usage: python3 no57_nomen_score.py [--check | --errsweep]   (--check exits 1 if the key or no57_nomen_score.tsv is stale)"""
import sys, random, re, statistics, unicodedata
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import strips_score as ss
import no57_score as ns
DIG = ss.DIG

def norm(w):
    w = unicodedata.normalize("NFKD", w.split(" ou ")[0]).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z]", "", w)

def reads(fn):
    d = {}
    for l in open(HERE / "fr3995" / fn):
        if l.startswith("#") or not l.strip(): continue
        f = l.rstrip("\n").split("\t"); d[f[0]] = f[1]
    return d

def nomen_key_text():
    a, b = reads("vill_m_readerA.tsv"), reads("vill_m_readerB.tsv")
    out = ["# fr.3995 no.57 (Feb 1593), canvas f200, nomenclator entries for the 57 target 3-figure codes (A1B-VILL-M, 3 Oct 2026).",
           "# grade M = both blind Sonnet readers give the same normalised first variant (fr3995/vill_m_readerA.tsv, vill_m_readerB.tsv);",
           "# I = disagreeing, not scored (decodes to nothing). value = normalised first variant.",
           "# code\tvalue\tgrade\treaderA\treaderB"]
    for c in sorted(a, key=int):
        na, nb = norm(a[c]), norm(b.get(c, "?"))
        out.append(f"{c}\t{na if na == nb and na else '?'}\t{'M' if na == nb and na else 'I'}\t{a[c]}\t{b.get(c, '?')}")
    return "\n".join(out) + "\n"

def load_nomen(txt):
    return {l.split("\t")[0]: l.split("\t")[1] for l in txt.splitlines() if l and not l.startswith("#") and l.split("\t")[2] == "M"}

def parse(lines, key, nomen):
    """returns codes; nomenclator codes are 'N'+digits (in nomen or not)."""
    codes = []
    for toks in lines:
        i = 0
        while i < len(toks):
            t = toks[i]
            if t in DIG:
                if i + 2 < len(toks) and t != "o" and toks[i + 1] in DIG and toks[i + 2] in DIG:
                    v = int("".join(toks[i:i + 3]).replace("o", "0"))
                    if 100 <= v <= 353: codes.append("N" + str(v)); i += 3; continue
                if i + 1 < len(toks) and toks[i + 1] in DIG:
                    c = (t + toks[i + 1]).replace("o", "0")
                    if c in key: codes.append(c); i += 2; continue
                c = t.replace("o", "0")
                if c in key: codes.append(c)
            elif t in key: codes.append(t)
            i += 1
    return codes

def ntok(c): return 3 if c[0] == "N" else (len(c) if c.isdigit() else 1)

def decode(codes, key, nomen):
    return "".join(nomen.get(c[1:], "") if c[0] == "N" else (key[c] if key.get(c, "NULL") != "NULL" else "") for c in codes)

def shuf(d, rnd):
    cs = [c for c in d if d[c] != "NULL"]; vs = [d[c] for c in cs]; rnd.shuffle(vs); k = dict(d); k.update(zip(cs, vs)); return k

def rank_z(codes, key, nomen, model, rnd, n=200):
    real = model.score(decode(codes, key, nomen))
    sh = [model.score(decode(codes, shuf(key, rnd), shuf(nomen, rnd))) for _ in range(n)]
    rank = 1 + sum(s >= real for s in sh)
    return real, rank, (real - statistics.mean(sh)) / (statistics.pstdev(sh) or 1e-9)

_WORDS = None
def words():
    global _WORDS
    if _WORDS is None:
        t = " ".join(ss.jp.read_corpus(p) for p in ss.jp.LANG_CORPORA["fr"])
        t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
        _WORDS = re.findall(r"[a-z]+", t)
    return _WORDS

def synth(key, nomen, n_codes, rnd):
    inv = {}
    for c, v in key.items():
        if v != "NULL": inv.setdefault(v, []).append(c)
    units = sorted(inv, key=len, reverse=True); wn = {v: c for c, v in nomen.items()}
    W = words(); j = rnd.randrange(0, len(W) - 40 * n_codes); toks = []
    def emit(c): toks.extend(["o" if d == "0" else d for d in c] if c.isdigit() else [c])
    while True:
        w = W[j]; j += 1
        if w in wn: emit(wn[w])
        else:
            i = 0
            while i < len(w):
                for u in units:
                    if w.startswith(u, i): emit(rnd.choice(inv[u])); i += len(u); break
                else: toks.append("S"); i += 1
        if len(toks) > 4 * n_codes:
            cs = parse([toks], key, nomen)
            if len(cs) >= n_codes: return cs[:n_codes]

def main():
    ktxt = nomen_key_text(); kp = HERE / "keys/key_f200_no57_nomen.tsv"
    nomen = load_nomen(ktxt); key = ns.load_key()
    rnd = random.Random(1); model = ss.jp.NgramModel([ss.jp.read_corpus(p) for p in ss.jp.LANG_CORPORA["fr"]])
    if "--errsweep" in sys.argv:
        r2 = random.Random(7); allc = list(key) + ["N" + c for c in nomen]
        print("err\tpower_rank1_of_20\tmean_z\tmin_z")
        for err in (0.10, 0.17, 0.25):
            p, zs = 0, []
            for s in range(20):
                cs = [r2.choice(allc) if r2.random() < err else c for c in synth(key, nomen, 300, r2)]
                r = rank_z(cs, key, nomen, model, r2); p += r[1] == 1; zs.append(r[2])
            print(f"{err:.2f}\t{p}\t{sum(zs)/20:.2f}\t{min(zs):.2f}")
        return
    hdr = "transcription\tkey_codes\tnomen_agreed\ttokens\tcovered_tokens\tcoverage\tcodes\tnomen_codes\tnomen_decoded\tpower_rank1_of_20\tpower_verdict\ttarget_letters\ttarget_score\ttarget_rank\ttarget_z\tverdict"
    rows = [hdr]; decs = []
    for name, lines in [("bourdeau", ss.tokens()), ("tx2_passB", ns.passb_tokens())]:
        n = sum(len(t) for t in lines); codes = parse(lines, key, nomen)
        live = [c for c in codes if (c[0] == "N" and c[1:] in nomen) or (c[0] != "N" and key.get(c, "NULL") != "NULL")]
        cov = sum(ntok(c) for c in live) / n; nn = sum(c[0] == "N" for c in codes); nd = sum(c[0] == "N" and c[1:] in nomen for c in codes)
        base = f"{name}\t{len(key)}\t{len(nomen)}\t{n}\t{sum(ntok(c) for c in live)}\t{cov:.3f}\t{len(codes)}\t{nn}\t{nd}"
        if cov < 0.5: rows.append(base + "\t\t\t\t\t\t\tnot testable"); continue
        p = sum(1 for s in range(20) if rank_z(synth(key, nomen, len(codes), rnd), key, nomen, model, rnd)[1] == 1)
        dec = decode(codes, key, nomen); decs.append((name, dec))
        if p < 16: rows.append(base + f"\t{p}\tnon-test\t{len(dec)}\t\t\t\tstop (power below 16/20)"); continue
        real, rank, z = rank_z(codes, key, nomen, model, rnd)
        rows.append(base + f"\t{p}\tpowered\t{len(dec)}\t{real:.3f}\t{rank}/201\t{z:.2f}\t" + ("PASS" if rank == 1 and z >= 3 else "FAIL"))
    out = "\n".join(rows) + "\n"; f = HERE / "no57_nomen_score.tsv"
    if "--check" in sys.argv:
        sys.exit(0 if f.exists() and f.read_text() == out and kp.exists() and kp.read_text() == ktxt else 1)
    kp.write_text(ktxt); f.write_text(out); print(out)
    for nm, d in decs: print(nm, "decode:", d[:300])

if __name__ == "__main__":
    main()
