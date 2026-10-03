# Pre-registration: GAPS2-matignon-mayenne-1586 (3 Oct 2026, account-4), written and pushed before any scoring

Step (Verdict line, gap 1): score the per-leaf M-only beam's M choices (`mu_leaf_beam.py`, unchanged: U held as TOK,
exact per-line Viterbi, LM catheri01) against Bourdeau's per-leaf readings instead of the shared-corpus judge.

**Reference.** Bourdeau's per-line decoder output in dbourdeau/cyphersolver HEAD 4d32ec9 (cloned to scratch 3 Oct
2026, MIT, credited per rule 8; not copied into this repository): `targets/matignon1586/reading_f143.txt` (f143r,
21 lines), `reading_f143v.txt` (33), `reading_f154.txt` (28), `reading_f173.txt` (33) -- line counts equal to
`ciphertext.txt`'s for those leaves. His LM is built from Berger de Xivrey's Lettres missives de Henri IV
(`mklm.py`), disjoint from catheri01. ff.150, 196, 201 have only prose summaries with ellipses (`*_reading.md`), which
cannot be aligned per line or per token; they are out of scope for this step (a deviation from the Verdict line's
file list, stated here before scoring). Bourdeau's readings are not ground truth: agreement is agreement with another
modern LM-assisted reading, not accuracy (rule 3 caveat a).

**Normalisation (caveat b).** Both sides: NFD accents stripped, lower case, v->u, j->i, w->u, k->c, then every
non a-z character dropped (spaces, '+', '*', punctuation); his '+'/'*' unknowns thus become alignment gaps. Our
rendering: as `mu_leaf_beam.render` (H value, chosen M alternative, U and '*' dropped), same mapping.

**Statistic.** Per line, a Levenshtein alignment (unit costs) of our rendering against his normalised line; an M
token *agrees* iff every letter of its chosen alternative is aligned to an identical letter. A(arm) = agreeing M
tokens / all M tokens on the leaf. Arms: beam (Viterbi choices), first (first alternative, as `reading_letters.txt`),
null (20 within-line token shuffles, seeds 1..20: the beam is run on the shuffled line, each M token's choice is
mapped back to its original position, and the line is rendered in its ORIGINAL order -- so only the context the
choice saw changes). Caveat (c): the null changes the choices, hence can differ on A; the number of M choices that
differ between beam and each null draw is reported.

**Power check (control, run first).** `mb.build_control` at each leaf's structure, held-out catheri02, seeds 1,2,3,
with the TRUE plaintext alternative as the reference: m_acc(beam) vs m_acc of the same 20-shuffle null. A leaf is
testable iff beam > null max on >= 2 of 3 seeds. Ceiling: if the control's first-candidate baseline >= 0.95 the leaf
is a non-test.

**Gate (target).** Leaf PASS iff A(beam) > max A(null) AND A(beam) >= A(first) + 0.02. Overall "agreement signal"
iff at least 3 of the testable leaves PASS and at least 3 leaves are testable; fewer than 3 testable leaves =
"non-test at this N". No value is committed to key.tsv/exceptions.tsv by this step either way.
