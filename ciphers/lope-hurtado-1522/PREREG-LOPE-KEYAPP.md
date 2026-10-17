# PREREG-LOPE-KEYAPP (17 Oct 2026, written 01:4x UTC by date -u, pushed before any scored run)

Brief: .claude/briefs/runs/2026-10-17-acct4-research-director-3.md, JOB LOPE-KEYAPP. Key under test: Kolosova 2024, Cifrario 7
(`kolosova2024_cifra7.tsv`, our transcription of the printed table, published key, credited). Witness: Bourdeau,
github.com/dbourdeau/cyphersolver `targets/lopehurtado/` (MIT / CC BY 4.0), HEAD 044576987ca9336b06f7c6598aaa89a4b57fa9f4
(2026-10-14), shallow clone, deleted after.

Question: do Kolosova's cifra-7 values agree with the code values Bourdeau fixed from the contemporary clear copies (gate), and,
only if so, how many of the code tokens Bourdeau left unread in R9634 and R9646 does cifra 7 value?

## Notation (fixed now)
Code token = a prefix sign (Bourdeau z / ɣ or y / x / t / ʃ / r) plus 1-3 Latin letters. Bourdeau -> Kolosova: z -> 3, ɣ -> y,
y -> y, ʃ -> s, ɡ -> g, ᵹ -> i (the equation ɣᵹb = yib logged in HYPOTHESES.md before this job). Any other non-Latin sign in the
group (ʒ, ℔, ε, digits) makes it not a code token for this test. Values compared lowercased, accents stripped, ç -> z, j -> g,
parenthetical glosses dropped ('le (+s = les)' -> le, 'Sa (Su Santidad)' -> su santidad, 'otro (+s = otros)' -> otro). A
Kolosova code printed with two words (tef paz/nec, tor, xac, 3uf, xor mo/mu) agrees if either word agrees. Nothing else is
normalised: otro vs otra, por vs razón, de vs (3az) count as they stand.

## Known-answer set (fixed now)
Primary: every code row in Bourdeau's key_codes.tsv whose source is the R9644 cipher (ff.237-239) against its clear copy
(ff.241-242), including the rows sourced on R9648 (the duplicate despatch, read through the same R9644 clear, per his
read_r9644.md), plus every code in read_r9649.md's "New values" and "Re-confirmed" lists (clear copy f.268). Both confirmed and
probable rows; nulls (Ꮒ, ʃta, yω) and spelled words excluded. Strict subset (reported beside it, not gated): R9644 ff.237-239 and
R9649 rows only, without the R9648 rows. Counts: agree / disagree / absent (code not in cifra 7).

## Null control
Shuffle the `word` column of kolosova2024_cifra7.tsv (codes fixed) 200 times, seed 1522, recount agreements on the same set.

## Gate
PASS iff agree / (agree + disagree) >= 0.80 on the primary set AND real agree > shuffle p99. FAIL -> log non-test, stop.

## Application (only after PASS)
Every code token in R9634 (r9634_cipher.txt, read against r9634_reading.tsv's {..} unread spans and ~probable words) and R9646
(read_r9646.md's transcription blocks, unread list) that Bourdeau left unread or probable is looked up in cifra 7 (grade H,
published key). Before/after coverage per record = tokens valued / cipher tokens, using Bourdeau's own totals (R9634 872/1191,
R9646 97/121) plus the cifra-7 gains. A token counts as a gain only when the cifra-7 group matches exactly and the cifra-7 row is
tx H; an M row in our transcription gives an M token. The five HYPOTHESES.md conflict codes stay M at every occurrence, with the
value(s) the context admits reported, none picked. Cifra 10: share of the same records' code tokens found in cifra 10 vs cifra 7;
a record fitting cifra 10 better is flagged, not re-read.

## Decision (pre-registered, brief step 5)
(a) gate PASS and >= 10 new tokens read in R9634: NOTES.md "## LOPE-KEYAPP (17 Oct 2026)" with the gain table, the lines whose sense
changed, per-token grades; next step a fresh rule-7 re-derivation by a verifier; label `key application` (pipeline 7).
(b) gate PASS and < 10 new tokens in R9634: the table adds little at 1522; say so and name what would (the 2024 book's discussion
pages, the BNE siblings).
(c) gate FAIL: non-test; list the disagreements for a re-read of the scan by the parent.
No key.tsv of our own; no reading described outside NOTES.md; status stays partial.
