#!/usr/bin/env python3
"""spot1 gate 2 (A2P4-LVN98, 3 Oct 2026): Groen-normalised (N2) cipher-unit score of 5797 spot 1.

Implements spot1/prereg2.md exactly (committed d1c8541e before any score). Reuses align_spot1.py's units(), sim/DP and
paragraph selection; only the normalisation (N2, both sides) and the metric (B2, cipher units only) differ.
  python3 align_spot1_v2.py  -> prints B2 for target, (s) and (d), the gate; writes spot1/gate2.tsv and spot1/units2.tsv
"""
import random, re, sys
import align_spot1 as v1

ABBR = [(r"\bE\.\s*[fF]\.\s*G\.", " euer gnaden "), (r"\bE\.\s*G\.", " euer gnaden "), (r"\bS\.\s*G\.", " seine gnaden "),
        (r"\bI\.\s*G\.", " ihre gnaden "), (r"(?<![A-Za-z.])H\.(?=\s)", " herr ")]
VAR = [("dt", "t"), ("th", "t"), ("tz", "z"), ("ph", "f"), ("ck", "k"), ("c", "k"), ("qu", "ku"), ("v", "u"), ("w", "u"),
       ("j", "i"), ("y", "i"), ("ie", "i"), ("ae", "a"), ("oe", "o"), ("ue", "u")]

def n2(s):
    s = s.lower()
    for a, b in (("ä", "a"), ("ö", "o"), ("ü", "u"), ("ß", "ss")):
        s = s.replace(a, b)
    for a, b in VAR:
        s = s.replace(a, b)
    s = re.sub(r"(?<=[aeiou])h(?![aeiou])", "", s)
    s = re.sub(r"e$", "", s)
    s = re.sub(r"[^a-z?]", "", s)
    return re.sub(r"([a-z])\1+", r"\1", s)

def ref_words(text):
    text = re.sub(r"Ga naar (margenoot\+|voetnoot\(?\d\)?) \[#\d+\]", "", text)
    for p, r in ABBR:
        text = re.sub(p, r, text)
    return [w for w in (n2(x) for x in text.split()) if w]

def b2(elig, ref):
    nm, _ = v1.dp(elig, ref)
    return nm / max(len(elig), 1), nm

def main():
    key = v1.load_key()
    us = v1.units(v1.HERE / "ciphertext_spot1.tsv", key)
    elig_units = [u for u in us if u[0] == "cipher" and len(n2(u[2]).replace("?", "")) >= 3]
    elig = [n2(u[2]) for u in elig_units]
    para = [l for l in (v1.T / "groen" / "groen_IV_CDXLIV.txt").read_text().splitlines() if l.strip()]
    tgt = next(l for l in para if "werden E.G. nhumehr von der bekannten" in l) + " " + \
        next(l for l in para if l.startswith("Wir seint resolvirt alsbalt"))
    ref = ref_words(tgt); N = len(ref)
    def window(starts):
        i = next(k for k, l in enumerate(para) if l.lstrip().startswith(starts) or starts in l[:60])
        ws = []
        for l in para[i:]:
            ws += ref_words(l)
            if len(ws) >= N: break
        return ws[:N]
    d = {"d1": window("Die schwere last"), "d2": window("Ga naar margenoot+ [#496]Von zeittungen"),
         "d3": window("Es lest sich, Gott lob")}
    out = [("target", *b2(elig, ref))]
    Bs = []
    for seed in range(1, 201):
        r = ref[:]; random.Random(seed).shuffle(r)
        s = b2(elig, r); Bs.append(s[0]); out.append((f"s{seed}", *s))
    for k, v in d.items():
        out.append((k, *b2(elig, v)))
    with open(v1.HERE / "gate2.tsv", "w") as f:
        f.write("ref\tB2\tmatched\teligible\n")
        for o in out:
            f.write(f"{o[0]}\t{o[1]:.4f}\t{o[2]}\t{len(elig)}\n")
    # per-unit: which reference words each eligible unit matched in the target alignment
    nm, used = v1.dp(elig, ref)
    with open(v1.HERE / "units2.tsv", "w") as f:
        f.write("raw\tdecoded\tn2\tbest_ref_sim\n")
        for u, e in zip(elig_units, elig):
            best = max(((v1.sim(e, "".join(ref[j:j + k])), " ".join(ref[j:j + k])) for k in (1, 2, 3)
                        for j in range(N - k + 1)), key=lambda x: x[0])
            f.write(f"{u[1]}\t{u[2]}\t{e}\t{best[0]:.2f} {best[1]}\n")
    B = out[0][1]
    p95 = sorted(Bs)[int(0.95 * len(Bs)) - 1]
    dmax = max(o[1] for o in out if o[0] in d)
    g1, g2, g3 = B >= 0.50, B >= p95 + 0.15, B >= dmax + 0.15
    print(f"target N={N} words (N2): B2={B:.3f} ({out[0][2]}/{len(elig)})")
    print(f"shuffle (s) n=200: B2 mean {sum(Bs)/len(Bs):.3f} p95 {p95:.3f} max {max(Bs):.3f}")
    for o in out:
        if o[0] in d:
            print(f"{o[0]}: B2={o[1]:.3f} ({o[2]}/{len(elig)})")
    print(f"gate: B2>=0.50 {g1}; B2>=p95+0.15 {g2}; B2>=dmax+0.15 {g3} -> {'PASS' if g1 and g2 and g3 else 'FAIL'}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
