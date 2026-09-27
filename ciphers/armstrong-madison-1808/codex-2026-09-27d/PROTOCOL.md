# Local transcription alternatives

Recorded before control results. This experiment allows changes only at
the ten manuscript positions listed in `alternatives.tsv`; all other
glyph identities remain fixed. Each listed position has two possible
labels, hence 1,024 transcriptions before considering the alphabet. The
alternatives were chosen by image inspection, without a plaintext proposal.
They are provisional judgments by the same reader, not independent
reconciliation or a corrected authoritative transcription.

Search a 24-letter alphabet with at most two glyphs per letter, jointly
with these binary choices. A departure from the original transcription
costs 0.3 log10 score units. Fix that value before target search. Retain
the existing historical English four-gram model and reset boundaries.
This tests a noisy alphabetic transcription, not a historical shorthand
system.

Two fresh held-out Jefferson controls have 257 tokens and 36 types with
the same fragment lengths. Give them ten binary ambiguities at the same
sequence positions and deliberately place five incorrect first choices
in each. Their symbol counts and glyph-confusion relationships do not
match the unknown target design. No control plaintext is used as a crib.

Run hard-label then joint-label searches with 1,000 restarts of 90,000
iterations. In the joint search, half the restarts begin from perturbed
hard-search keys; the rest begin randomly. The controls must each recover
at least 95% of letters AND restore at least four of the five deliberately
wrong labels before running the target. This checks the new operation of
correcting transcription errors, not just general language recovery.

If they pass, run the joint search on the target using the previous fixed
transcription's retained candidate pool as the warm start. A readable
candidate must be checked against the images, numerical context and
repeated signs. Failure does not exclude the target's use of an alphabet:
the visual alternative list may be incomplete, and the language model and
glyph segmentation may be wrong. A score improvement alone is not a
decipherment or proof that a proposed transcription change is correct.

No new target run with these alternatives has been made when this protocol
was recorded. All old transcriptions and results are preserved.
