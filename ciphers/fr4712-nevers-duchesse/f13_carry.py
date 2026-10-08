#!/usr/bin/env python3
"""DUCH-F13: carry fr.4712 f.13r glossed codes to f.10r per PREREG_duchf13.md.
python3 f13_carry.py [--check]   writes f13_carry.tsv (per-token carry) and f13_carry_stats.tsv; --check exits 1 if stale.
Reads f13_code_gloss.tsv, ciphertext_f10_digits.tsv (S2/S3 via score_key1.segs), keys/key_no1.tsv, and the
same-hand condition HAND_SAME below (recorded in NOTES.md before this script was first run)."""
import csv, random, sys
from pathlib import Path
H = Path(__file__).resolve().parent
sys.path.insert(0, str(H))
import score_key1 as sk

# prereg (c): True / False / None (undecided) -- set from the NOTES.md hand comparison.
# 3 Oct 2026 DUCH-F13: None (not shown, leaning different: f.10r open 8 vs f.13r looped 8).
# 8 Oct 2026 D2-F4712: True, applying the owner's eye check (ASKS 113, 5 Oct 2026, "I think the same") under ASKS 113's
# pre-registered rule; the conflicting 8-form evidence and R11A-F4712's NON-TEST (6 Oct) are recorded beside it in NOTES.md.
HAND_SAME = True

def load_pairs():
    rows = [l for l in open(H / "f13_code_gloss.tsv") if not l.startswith("#")]
    return list(csv.DictReader(rows, delimiter="\t"))

def gloss_table(pairs):
    """code -> (gloss, grade) using H pairs only; a code with two different H glosses is M ('conflict')."""
    hs = {}
    for p in pairs:
        if p["grade"] == "H" and p["gloss"] != "-":
            hs.setdefault(p["code"], set()).add(p["gloss"])
    return {c: (sorted(g)[0], "H") if len(g) == 1 else (" / ".join(sorted(g)), "conflict") for c, g in hs.items()}

def norm(t):
    return str(int(t)) if t.isdigit() else t

def carry(tokens, table):
    out = []
    for t in tokens:
        g = table.get(norm(t))
        if g is None:
            out.append((t, "", ""))
        elif g[1] == "conflict" or HAND_SAME is not True:
            out.append((t, g[0], "M"))
        else:
            out.append((t, g[0], "C"))
    return out

def coverage(tokens, codes):
    return sum(norm(t) in codes for t in tokens)

def main():
    pairs = load_pairs()
    table = gloss_table(pairs)
    key = {c: v for c, (v, k) in sk.load_key().items()}
    segs = sk.segs(sk.load_lines())
    rows, stats = [], []
    rng = random.Random(13)
    for name, lines in segs.items():
        toks = [t for l in lines for t in l]
        car = carry(toks, table)
        for i, (t, g, gr) in enumerate(car):
            rows.append((name, i + 1, t, g, gr))
        cov = coverage(toks, set(table))
        nC = sum(gr == "C" for _, _, gr in car)
        # stat 2: random code sets of the same size from 1-99
        k = len(table)
        ge = sum(coverage(toks, {str(x) for x in rng.sample(range(1, 100), k)}) >= cov for _ in range(1000))
        stats.append((name, len(toks), cov, nC, k, round(ge / 1000, 3)))
    # stat 3: agreement of f.13r H glosses with key no.1 (exact, case-insensitive substring either way)
    def agree(tab):
        n = 0
        for c, (g, gr) in tab.items():
            v = key.get(c, "")
            if v and v not in "-" and len(v) > 1 and (g.lower().rstrip(".") in v.lower() or v.lower() in g.lower()):
                n += 1
        return n
    obs = agree(table)
    codes, gl = list(table), [table[c] for c in table]
    ge3 = 0
    for _ in range(1000):
        rng.shuffle(gl)
        ge3 += agree(dict(zip(codes, gl))) >= obs
    out1 = "segmentation\tidx\ttoken\tf13_gloss\tgrade\n" + "".join("\t".join(map(str, r)) + "\n" for r in rows)
    out2 = ("segmentation\tn_tokens\tcoverage\tn_C\tn_glossed_codes\tp_random_codeset\n"
            + "".join("\t".join(map(str, r)) + "\n" for r in stats)
            + f"# stat 3 key-family: f.13r H codes agreeing with key no.1 = {obs}/{len(table)}, rotation p = {ge3/1000:.3f}\n"
            + "# rotated-gloss control on coverage: identical by construction (coverage ignores which gloss), non-test\n")
    if "--check" in sys.argv:
        ok = (H / "f13_carry.tsv").read_text() == out1 and (H / "f13_carry_stats.tsv").read_text() == out2
        print("OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    (H / "f13_carry.tsv").write_text(out1); (H / "f13_carry_stats.tsv").write_text(out2)
    print(out2)

if __name__ == "__main__":
    main()
