#!/usr/bin/env python3
"""untersberg-code NEAR step (3b), 26 Sept 2026, LANE B5 worker bUNT6.

Joint alignment of Hs 1's 61 ordered letter-tokens (S. d. d. occo. x. / Satrnrop ... /
P. 6. m. ... / m. 519. ... / ariu. ... / mic r l y. ...) against all four of Herzog
1929 pp.28-29's remaining un-tested witnesses at once -- Hs 13 (mostly plain Latin,
19 tokens), Hs 3 / Hs 3a / Hs 11 (11-letter initial runs each) -- extending bUNT5's
single-witness (Hs 12) line-level test to a token-level, multi-witness test with a
matched shuffle control, per CLAUDE.md rule 3.

Design (stated plainly, not hidden): Hs 12 (bUNT5) gave a clean 1:1 line<->word
correspondence (6 lines, 6 words), so that script aligned by LINE and permuted whole
words. Hs 13/3/3a/11 have no such correspondence to Hs 1's six physical lines (Hs 13
prints across 12 short apparatus lines; Hs 3/3a/11 print a single row of 11 initials
each) -- Herzog's apparatus lineation reflects his own page layout, not Hs 1's. So
this test drops the line boundary and works on Hs 1's flat, ordered 61-token letter
sequence (digits excluded; the two "eth" crossed-d suspension-glyph tokens kept in
their true position but excluded from initial-letter comparison, per bUNT5's own
convention -- rule 2, not a Latin letter). For each witness W (length n_W tokens), it
slides W's token sequence over every valid contiguous window of Hs 1's 61-token
sequence and scores the alignment two ways at each offset:
  (a) initial-letter match count (case-insensitive; ETH/digit positions never match)
  (b) expansion count: a witness token strictly longer than the aligned Hs 1 token
      AND starting with the Hs 1 token's letters (case-insensitive) -- the "Hs 12
      Bellum/Famus" pattern, here checked against Hs 13's spelled-out words too
The best offset per witness is the one maximizing (a); the JOINT target score is the
sum of the four witnesses' best-offset initial-letter counts (out of 19+11+11+11=52
possible). No expansion candidate is graded unless it survives at the best-scoring,
control-beating offset (rule 4: "a token pair counts toward a grade only at C ... or
M; no expansion from the corpus expander" -- this script never uses expand_lib.py).

Control (rule 3): the identical four-witness best-offset joint-scoring procedure is
re-run on 500 random shuffles of Hs 1's flat 61-token order (seed 20260925, same seed
family as bUNT5/test1's controls on this target), reporting the joint-score
distribution and the real joint score's percentile within it -- exhaustive 61! is
infeasible, so this uses "the same shuffle scheme bUNT5 used" clause of the brief
(500 trials, matching test1_abbreviation.py's own N).

Source: specs/cheap-tests/untersberg-code/witnesses.tsv (Herzog 1929 pp.28-29
apparatus, transcribed and image-checked by LANE B4 bUNT5). Credit: Herzog's own
1929 print; this script only re-derives a control statistic from it.

Usage: python3 align_joint.py
"""
import random

# ---------------------------------------------------------------------------
# Hs 1's flat, ordered 61-token letter sequence (witnesses.tsv siglum "1"),
# digits excluded, "eth" (crossed-d suspension glyph) kept in position but
# marked with initial=None (never matches, never an expansion target).
# ---------------------------------------------------------------------------
HS1_TOKENS = [
    # line 1 (5 tokens: S . eth . eth . occo . x .)
    "S", None, None, "occo", "x",
    # line 2 (5 tokens)
    "Satrnrop", "a", "f", "l", "d",
    # line 3 (12 tokens)
    "P", "m", "a", "t", "q", "o", "t", "m", "r", "u", "a", "t",
    # line 4 (12 tokens)
    "m", "r", "l", "v", "e", "p", "a", "tt", "tt", "l", "x", "missm",
    # line 5 (11 tokens)
    "ariu", "a", "o", "u", "st", "g", "c", "x", "l", "alto", "mvraco",
    # line 6 (16 tokens)
    "mic", "r", "l", "y", "pymi", "l", "o", "p", "m", "i", "v", "m", "l", "t", "t", "g",
]
assert len(HS1_TOKENS) == 61, len(HS1_TOKENS)
assert sum(1 for t in HS1_TOKENS if t is None) == 2  # the two eth tokens

WITNESSES = {
    "Hs13": ["Bellum", "Fames", "corias", "peseit", "Moesque", "Z", "i", "Siore", "P",
             "S", "F", "U", "Jnnen", "voslam", "i", "h", "h", "h", "h"],
    "Hs3":  ["S", "O", "R", "C", "E", "J", "S", "A", "T", "O", "M"],
    "Hs3a": ["S", "O", "R", "C", "E", "T", "S", "A", "T", "O", "N"],
    "Hs11": ["S", "U", "R", "C", "E", "T", "S", "A", "T", "U", "S"],
}


def initial(tok):
    return None if tok is None else tok[0].lower()


def score_offset(hs1_seq, witness, offset):
    """Score aligning witness[j] with hs1_seq[offset+j] for all j. Returns
    (initial_matches, expansions) where expansions counts witness tokens that
    strictly extend the aligned Hs1 token (case-insensitive prefix)."""
    matches = 0
    expansions = []
    for j, wtok in enumerate(witness):
        htok = hs1_seq[offset + j]
        hi, wi = initial(htok), initial(wtok)
        if hi is not None and wi is not None and hi == wi:
            matches += 1
        if htok is not None and len(wtok) > len(htok) and wtok.lower().startswith(htok.lower()):
            expansions.append((j, htok, wtok))
    return matches, expansions


def best_alignment(hs1_seq, witness):
    n = len(witness)
    best = None  # (matches, offset, expansions)
    for offset in range(0, len(hs1_seq) - n + 1):
        matches, expansions = score_offset(hs1_seq, witness, offset)
        if best is None or matches > best[0]:
            best = (matches, offset, expansions)
    return best  # first (lowest-offset) max is kept, matching bUNT5's determinism


def joint_score(hs1_seq):
    total = 0
    detail = {}
    for name, wtoks in WITNESSES.items():
        matches, offset, expansions = best_alignment(hs1_seq, wtoks)
        total += matches
        detail[name] = (matches, offset, expansions, len(wtoks))
    return total, detail


def main():
    total_possible = sum(len(w) for w in WITNESSES.values())

    real_total, real_detail = joint_score(HS1_TOKENS)
    print(f"Hs1 flat sequence: {len(HS1_TOKENS)} tokens (2 eth-glyph positions excluded from matching)")
    print(f"Witnesses: {', '.join(f'{k} (n={len(v)})' for k, v in WITNESSES.items())}")
    print(f"Total possible joint matches: {total_possible}\n")

    print("=== REAL Hs1 order ===")
    for name, (matches, offset, expansions, n) in real_detail.items():
        print(f"  {name}: best offset={offset}, initial matches={matches}/{n}")
        if expansions:
            for j, htok, wtok in expansions:
                print(f"    expansion candidate: Hs1[{offset+j}]={htok!r} <- {name}[{j}]={wtok!r}")
        else:
            print(f"    no expansion candidates at this offset")
    print(f"  JOINT real score: {real_total}/{total_possible} = {real_total/total_possible:.3f}\n")

    rng = random.Random(20260925)
    n_trials = 500
    shuffle_scores = []
    for _ in range(n_trials):
        shuffled = HS1_TOKENS[:]
        rng.shuffle(shuffled)
        s, _ = joint_score(shuffled)
        shuffle_scores.append(s)

    mean = sum(shuffle_scores) / len(shuffle_scores)
    lo, hi = min(shuffle_scores), max(shuffle_scores)
    percentile = 100.0 * sum(1 for s in shuffle_scores if s <= real_total) / len(shuffle_scores)
    ge = sum(1 for s in shuffle_scores if s >= real_total)

    print(f"=== CONTROL: {n_trials} random shuffles of Hs1's 61-token order (seed 20260925) ===")
    print(f"  control mean: {mean:.3f}/{total_possible} ({mean/total_possible:.3f})")
    print(f"  control range: [{lo}, {hi}]")
    print(f"  real ({real_total}) percentile in control distribution: {percentile:.1f}")
    print(f"  {ge}/{n_trials} shuffles ({100*ge/n_trials:.1f}%) tie or beat the real joint score")
    verdict = "ABOVE" if real_total > mean else ("AT" if real_total == mean else "BELOW")
    print(f"  real vs control mean: {verdict}")


if __name__ == "__main__":
    main()
