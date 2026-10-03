#!/usr/bin/env python3
"""mlh-1976 cheap test 2: cross-reference the catalogued sign shapes against period character sets.

GAPS131-mlh-1976 (account-4), 3 Oct 2026.

Inputs (all in this file, nothing fetched):
  SIGNS     -- each catalogued sign of NOTES.md's sign table (S1..S20, the letter-shaped D/O and the
               literal connector), with a short list of candidate glyphs (Unicode) its blind shape
               description could plausibly be.  The candidate lists were written from the NOTES.md
               descriptions alone, before any set membership was computed, but by a writer who knows
               the APL/ALGOL sets -- see CAVEAT below.
  SETS      -- printable repertoires from public documentation:
               ASCII-1967 (USAS X3.4-1967, 95 printable), EBCDIC as printed on System/360 (letters,
               digits, the 1964 special characters), APL\\360 on the IBM 2741 APL typeball (base keys
               plus the standard overstrikes of APL\\360 / APLSV, 1966-1975; later APL2 glyphs such as
               the epsilon-underbar, quad-arrows and up-shoe-stile are excluded), ALGOL 68 reference
               language (Revised Report 1975 representation symbols).
Statistic:  per set, the number of non-literal signs with at least one candidate in the set; and the
            "programming-specific" count: signs with a candidate in APL or ALGOL 68 but no candidate in
            ASCII or EBCDIC.
Control:    the same statistic over TRIALS random catalogues of the same size: each sign's candidate
            list replaced by a random sample of the same length from POOL (every assigned code point in
            the Unicode blocks the candidates are drawn from).  The control varies on the statistic's
            own axis (which glyphs are candidates), so it can fail differently from the target (rule 3).
CAVEAT:     the null is lenient toward the target: real candidates are common shapes (triangle,
            circle, caret, arrow, plus) that any symbol repertoire carries, while random pool glyphs are
            mostly exotic.  A target excess over this null therefore shows "the shapes are generic
            symbols", not "the sender used APL"; the programming-specific count is the discriminating figure.

Usage: python3 charset_xref.py [--check]   (writes charset_xref.tsv and charset_xref_summary.json;
       --check exits 1 if the committed outputs differ from a fresh run)
"""
import json, random, sys, unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
TRIALS = 2000
SEED = 1976

SIGNS = [  # (code, short description, candidates, literal?)
    ("S1", "dash + integral/S curl", "∫ʃ§~∽", False),
    ("S2", "stem, filled dot near top, macron above", "¡⫯⍿", False),
    ("S3", "open P on stem", "Pρ⍴Þ", False),
    ("S4", "small filled dot (reused label)", ".·∘", False),
    ("S5", "outline triangle apex up", "△∆Δ", False),
    ("D", "letter-shaped D", "D▷", False),
    ("O", "plain open circle", "O○0", False),
    ("S8", "caret / chevron without base", "^∧Λ", False),
    ("S9", "n-shape with descending tail", "nηŋ∩", False),
    ("S10", "stem topped by arch with two dots", "⊤↑☂⍦", False),
    ("S11", "triangle with zigzag tail", "∆⍙↯", False),
    ("S12", "zigzag / lightning, blocky 5 or S", "5SZ↯ϟ⌁", False),
    ("S13", "e-loop on underline curling into arrow", "e℮∊↪", False),
    ("S14", "single-stroke right arrow", "→", False),
    ("S15", "circle with central dot", "⊙☉◉⍟", False),
    ("S16", "stem crossed by two bars", "F‡ǂ∓±", False),
    ("S17", "D/6 loop with inner curl", "D6∂δð", False),
    ("S18", "P with dot in bowl", "P⍴℗ṗ", False),
    ("S19", "asymmetric cross", "+×x†", False),
    ("S20", "oval with arrowhead inside", "⍈⍄⊳⊲", False),
    ("⇒", "double-stroke right arrow (literal connector)", "⇒", True),
    ("/", "slash (literal)", "/", True),
    ("|", "vertical stroke (literal)", "|1l", True),
]

LET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIG = "0123456789"
SETS = {
    "ASCII-1967": "".join(chr(c) for c in range(33, 127)),
    "EBCDIC-S360": LET + LET.lower() + DIG + "¢.<(+|&!$*);¬-/,%_>?:#@'=\"",
    "APL360-2741": LET + DIG + "¨¯<≤=≥>≠∨∧×÷?⍵∊⍴~↑↓⍳○*←→⍺⌈⌊_∇∆∘'⎕|⊥⊤:;,./\\+-()[]∪∩⊂⊃"
                   + "⍋⍒⌽⊖⍉⍟⌹!⍎⍕⍝⍞⍱⍲⌿⍀⍫⍙",
    "ALGOL68-RR": LET + LET.lower() + DIG + "+-×÷/*=<>≤≥≠¬∧∨↑↓⌈⌊⊥⏨¢#|:;,.()[]@'\"∘",
}
PROG = ("APL360-2741", "ALGOL68-RR")
GEN = ("ASCII-1967", "EBCDIC-S360")

BLOCKS = [(0x21, 0x7E), (0xA1, 0xFF), (0x0180, 0x024F), (0x0391, 0x03C9), (0x2100, 0x214F),
          (0x2190, 0x21FF), (0x2200, 0x22FF), (0x2300, 0x23FF), (0x25A0, 0x25FF), (0x2600, 0x26FF),
          (0x2A00, 0x2AFF)]


def pool():
    out = []
    for a, b in BLOCKS:
        for c in range(a, b + 1):
            ch = chr(c)
            if unicodedata.name(ch, None) and unicodedata.category(ch)[0] in "LSPN":
                out.append(ch)
    return out


def score(cands):
    """cands: list of candidate strings (non-literal signs). Returns per-set hit counts and prog-specific."""
    hits = {s: 0 for s in SETS}
    spec = 0
    for c in cands:
        ins = {s: any(g in SETS[s] for g in c) for s in SETS}
        for s in SETS:
            hits[s] += ins[s]
        spec += (any(ins[s] for s in PROG) and not any(ins[s] for s in GEN))
    hits["prog_specific"] = spec
    return hits


def run():
    rows = ["code\tdescription\tcandidates\tliteral\t" + "\t".join(SETS) + "\tmatched_glyphs"]
    for code, desc, cands, lit in SIGNS:
        cols, matched = [], []
        for s, rep in SETS.items():
            m = [g for g in cands if g in rep]
            cols.append("Y" if m else "-")
            if m:
                matched.append(f"{s}:{''.join(m)}")
        rows.append(f"{code}\t{desc}\t{cands}\t{'yes' if lit else 'no'}\t" + "\t".join(cols) + "\t" + "; ".join(matched))
    real = [c for _, _, c, lit in SIGNS if not lit]
    target = score(real)
    P = pool()
    rng = random.Random(SEED)
    keys = list(target)
    samples = {k: [] for k in keys}
    for _ in range(TRIALS):
        h = score(["".join(rng.sample(P, len(c))) for c in real])
        for k in keys:
            samples[k].append(h[k])
    ctrl = {}
    for k in keys:
        v = sorted(samples[k])
        ge = sum(1 for x in v if x >= target[k])
        ctrl[k] = {"mean": round(sum(v) / len(v), 3), "p95": v[int(0.95 * len(v)) - 1], "max": v[-1],
                   "p_ge_target": round((ge + 1) / (len(v) + 1), 4)}
    summary = {"n_signs": len(real), "pool_size": len(P), "trials": TRIALS, "seed": SEED,
               "set_sizes": {s: len(set(r)) for s, r in SETS.items()},
               "target": target, "control": ctrl}
    return "\n".join(rows) + "\n", json.dumps(summary, ensure_ascii=False, indent=1) + "\n"


def main():
    tsv, js = run()
    t, j = HERE / "charset_xref.tsv", HERE / "charset_xref_summary.json"
    if "--check" in sys.argv:
        ok = t.exists() and j.exists() and t.read_text() == tsv and j.read_text() == js
        print("charset_xref: committed outputs current" if ok else "charset_xref: STALE")
        sys.exit(0 if ok else 1)
    t.write_text(tsv)
    j.write_text(js)
    print(tsv + js)


if __name__ == "__main__":
    main()
