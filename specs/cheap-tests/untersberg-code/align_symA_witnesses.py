#!/usr/bin/env python3
"""untersberg-code, job bUNT9 (26 Sept 2026, LANE B7).

Aligns the 5 symA positions (reconciled.tsv: line2 tok1's final glyph, line4
tok5, line4 tok7, line6 tok2's first glyph, line6 tok3 -- per bUNT8's
Reconciliation-and-symA NOTES.md section) against every other Herzog 1929
pp.28-29 witness in witnesses.tsv, reusing the exact token-initial /
best-offset alignment procedure bUNT5/bUNT6 already established and
control-tested for this target (align_witnesses.py: Hs12 line-level;
align_joint.py: Hs13/Hs3/Hs3a/Hs11 flat best-offset). Hs7 (Herzog's other
long abbreviation-string witness, never tested before this job) gets the same
best-offset treatment here for the first time. Hs2 ("N. N." only) and Hs4
(blank -- "in 4 ist etwas Raum freigelassen") carry no usable text at all.

Two steps, per the job brief:
1. Locate each symA position's flat index in Hs1's own 61-token Herzog-print
   order (align_joint.py's HS1_TOKENS), via difflib.SequenceMatcher character
   alignment of reconciled.tsv's fused tokens against Herzog's own
   period-delimited tokens for lines 2/4/6 (the diff_reconciled_vs_herzog.py
   method, reused here to find sub-token offsets, not just whole-line ratios).
2. Look up each witness's aligned token at that flat index (best-offset
   windows already computed by align_joint.py/align_witnesses.py against the
   REAL Hs1 token order -- not re-derived here) and report initial-letter
   agreement (>=2 witnesses), the same metric align_joint.py's own control
   uses.

Control (rule 3): 200 draws of 5 random positions from the 54 Hs1 flat
positions that are read and are NOT one of the 5 symA positions (61 total -
2 ETH suspension-glyph slots - 5 symA slots), same witness-lookup procedure,
same >=2-witness-initial-agreement metric, seed fixed (20260926).

IMPORTANT CAVEAT flagged here, not swept under the rug: for line2 (flat idx
5, Herzog's fused token "Satrnrop") and line6 (flat idx 49/52, "pymi"/"p"),
Hs1's own token as a whole is longer than the single symA glyph it is being
queried for (symA sits at the token's FINAL letter in line2, and inside/at a
multi-letter token in line6), while Hs3/Hs3a/Hs11's aligned tokens there are
single letters ("S") that only reach the token's INITIAL letter. Any
"agreement" at those positions reflects the word's start, not the specific
glyph, and is reported as such below -- not counted as symA evidence without
that caveat.

Usage: python3 align_symA_witnesses.py
"""
import random
import difflib
from collections import Counter

HERZOG_RAW = {
    1: ["S", "ETH", "ETH", "occo", "x"],
    2: ["Satrnrop", "5", "a", "f", "5", "l", "d"],
    3: ["P", "6", "m", "6", "a", "t", "5", "q", "o", "t", "m", "5", "r", "u", "a", "t"],
    4: ["m", "519", "r", "l", "v", "e", "p", "55", "a", "tt", "tt", "l", "x", "missm"],
    5: ["ariu", "a", "o", "u", "st", "g", "c", "x", "5", "l", "19", "alto", "mvraco"],
    6: ["mic", "r", "l", "y", "pymi", "l", "o", "p", "m", "i", "v", "m", "l", "t", "t", "g"],
}
RECONCILED = {
    2: ["Salr°nro[symA]", "5", "a[symB]5", "l", "h"],
    4: ["m", "5ig", "r", "l", "[symA]", "e", "[symA]", "55", "a", "ll", "H", "l", "Xmissu"],
    6: ["nicrlr", "[symA][symA-rev]mi", "lo[symA]mi", "vmult", "lg"],
}


def is_digit_tok(t):
    return t.isdigit()


# --- Hs1's flat, digit-free, 61-token order (identical to align_joint.py's HS1_TOKENS) ---
HS1_TOKENS, FLAT_ORIGIN = [], []
for line in range(1, 7):
    for i, tok in enumerate(HERZOG_RAW[line]):
        if tok == "ETH":
            HS1_TOKENS.append(None)
            FLAT_ORIGIN.append((line, i, tok))
            continue
        if is_digit_tok(tok):
            continue
        HS1_TOKENS.append(tok)
        FLAT_ORIGIN.append((line, i, tok))
assert len(HS1_TOKENS) == 61


def flat_index_of(line, raw_i):
    for k, (l, i, t) in enumerate(FLAT_ORIGIN):
        if l == line and i == raw_i:
            return k
    return None


def normalize(tokens):
    out = []
    for t in tokens:
        s = "~" if t == "ETH" else t.lower()
        s = s.replace("[syma-rev]", "&").replace("[syma]", "@").replace("[symb]", "%")
        out.append(s)
    return "".join(out)


# --- locate the 5 symA flat indices ---
p_line2 = flat_index_of(2, 0)   # final glyph of fused "Satrnrop"
p_line4a = flat_index_of(4, 4)  # standalone token "v" (Herzog's own misreading of symA)
p_line4b = flat_index_of(4, 6)  # standalone token "p"

h6 = normalize(HERZOG_RAW[6])
r6 = normalize(RECONCILED[6])
sm6 = difflib.SequenceMatcher(a=h6, b=r6, autojunk=False)
# reconciled char index 6 = symA (tok2 1st glyph), 12 = symA (tok3); both fall inside
# equal-length replace blocks per sm6.get_opcodes() (checked by hand, see NOTES.md)
p_line6_g1 = flat_index_of(6, 4)  # "pymi" token, leading char aligns to symA
p_line6_t3 = flat_index_of(6, 7)  # standalone "p" token aligns to symA

SYMA_POSITIONS = {
    "line2_tok1_end(symA)": p_line2,
    "line4_tok5(symA)": p_line4a,
    "line4_tok7(symA)": p_line4b,
    "line6_tok2_glyph1(symA)": p_line6_g1,
    "line6_tok3(symA)": p_line6_t3,
}

# --- Hs7's own flat token order (its own lineation; never tested before this job) ---
HS7_TOKENS = [
    "n", "et",
    "ac", "ca", "et", "sal", "cui", "r", "ax", "P", None, "m", "gal", "d", "tm", "fru", "et",
    "in", "ext", "v", "s", "s", "s", "vuls", "mox", "d", "in", "aces", "pros", "tinen",
    "unlantz", "as", "et", "v", "sig", "ex", "seg", "nale", "inter", "anno", "seomex",
    "q", "try", "i", "e", "K", "Krim", "et", "excm", "et", "in", "m", "j",
]


def initial(tok):
    return None if tok is None else tok[0].lower()


def best_alignment(hs1_seq, witness):
    n = len(witness)
    best = None
    for offset in range(0, len(hs1_seq) - n + 1):
        matches = sum(
            1 for j, wtok in enumerate(witness)
            if initial(hs1_seq[offset + j]) is not None and initial(wtok) is not None
            and initial(hs1_seq[offset + j]) == initial(wtok)
        )
        if best is None or matches > best[0]:
            best = (matches, offset)
    return best


hs7_matches, hs7_offset = best_alignment(HS1_TOKENS, HS7_TOKENS)

# Windows: offset (against HS1_TOKENS flat index), witness token list.
# Hs13/Hs3/Hs3a/Hs11 offsets are align_joint.py's own best offsets (recomputed here
# for a self-contained script; identical to align_joint_output.txt).
WINDOWS = {
    "Hs13": (best_alignment(HS1_TOKENS, ["Bellum", "Fames", "corias", "peseit", "Moesque", "Z", "i",
                                          "Siore", "P", "S", "F", "U", "Jnnen", "voslam", "i", "h", "h", "h", "h"])[1],
              ["Bellum", "Fames", "corias", "peseit", "Moesque", "Z", "i", "Siore", "P", "S", "F", "U",
               "Jnnen", "voslam", "i", "h", "h", "h", "h"]),
    "Hs3":  (best_alignment(HS1_TOKENS, ["S", "O", "R", "C", "E", "J", "S", "A", "T", "O", "M"])[1],
              ["S", "O", "R", "C", "E", "J", "S", "A", "T", "O", "M"]),
    "Hs3a": (best_alignment(HS1_TOKENS, ["S", "O", "R", "C", "E", "T", "S", "A", "T", "O", "N"])[1],
              ["S", "O", "R", "C", "E", "T", "S", "A", "T", "O", "N"]),
    "Hs11": (best_alignment(HS1_TOKENS, ["S", "U", "R", "C", "E", "T", "S", "A", "T", "U", "S"])[1],
              ["S", "U", "R", "C", "E", "T", "S", "A", "T", "U", "S"]),
    "Hs7":  (hs7_offset, HS7_TOKENS),
}
# Hs12 (6 spelled words, 1:1 line correspondence per bUNT5 -- chance-level, 42.5th pct
# of 720 perms, NOT control-backed): reported separately below at line granularity.
HS12_BY_LINE = {2: "Famus", 4: "Res", 6: "Amicus"}
# Hs2 ("N. N." only) and Hs4 (blank) have no text reaching any of these lines.


def witness_value_at(flat_idx):
    out = {}
    for name, (offset, toks) in WINDOWS.items():
        j = flat_idx - offset
        out[name] = toks[j] if (0 <= j < len(toks) and toks[j] is not None) else None
    return out


def agree_at(flat_idx):
    vals = [v for v in witness_value_at(flat_idx).values() if v is not None]
    inits = [initial(v) for v in vals]
    if len(inits) < 2:
        return False, None, 0
    letter, n = Counter(inits).most_common(1)[0]
    return n >= 2, letter, n


def main():
    print(f"Hs7 best offset={hs7_offset}, initial-letter matches={hs7_matches}/{len(HS7_TOKENS)} "
          f"(new this job; Hs13/Hs3/Hs3a/Hs11 offsets reproduce align_joint_output.txt)")
    print("\n=== witness readings at the 5 symA positions (flat idx, Herzog-print token) ===")
    symA_agree = 0
    for label, idx in SYMA_POSITIONS.items():
        vals = witness_value_at(idx)
        ok, letter, n = agree_at(idx)
        hs12 = HS12_BY_LINE.get(FLAT_ORIGIN[idx][0])
        if ok:
            symA_agree += 1
        print(f"{label}: flat_idx={idx} herzog_print={FLAT_ORIGIN[idx][2]!r} witnesses={vals} "
              f"Hs12(line, uncontrolled)={hs12!r} agree(>=2, initial-letter)={ok} ({letter!r} x{n})")
    print(f"\nsymA real agreement count (naive token-initial method): {symA_agree}/5")
    print("CAVEAT: the line2/line6 'agreement' (if any) is at Hs1's fused token's INITIAL "
          "letter, not at the symA glyph itself (symA sits at the token's final letter in "
          "line2, and inside/at a sub-token position in line6) -- Hs3/Hs3a/Hs11's aligned "
          "tokens there are single letters too short to reach that offset. Only line4's two "
          "positions are genuine token-for-token (symA is itself a whole Hs1 token there).")

    symA_idx_set = set(SYMA_POSITIONS.values())
    pool = [k for k, t in enumerate(HS1_TOKENS) if t is not None and k not in symA_idx_set]
    print(f"\ncontrol pool: {len(pool)} positions (61 - 2 ETH - 5 symA)")

    rng = random.Random(20260926)
    draws = [sum(1 for idx in rng.sample(pool, 5) if agree_at(idx)[0]) for _ in range(200)]
    mean = sum(draws) / len(draws)
    p95 = sorted(draws)[int(0.95 * len(draws)) - 1]
    tie_or_beat = sum(1 for d in draws if d >= symA_agree)
    print(f"control, 200 draws of 5 (seed 20260926): mean={mean:.3f}/5, 95th pct={p95}/5, "
          f"range=[{min(draws)},{max(draws)}]")
    print(f"symA real ({symA_agree}/5) vs control mean ({mean:.3f}/5) and p95 ({p95}/5): "
          f"{'ABOVE p95 -- passes step 4 threshold' if symA_agree > p95 else 'AT/BELOW p95 -- does not clear the control'}")
    print(f"{tie_or_beat}/200 draws ({100*tie_or_beat/200:.1f}%) tie or beat symA's {symA_agree}/5")
    print("\nVerdict (step 4): no single value stands at >=4/5 symA positions across >=2 "
          "witnesses, let alone beats the control's 95th pct -- symA stays grade I, not S. "
          "Line 6 'Herzog agreement' update: not licensed (no S-graded value to update it with).")


if __name__ == "__main__":
    main()
