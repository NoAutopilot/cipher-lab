# AVS53 pre-registration (3 Oct 2026, 14:2x UTC, worker AVS53 for LANE-A2PUSH3, account 2) -- committed before any score

Question: do key_53's decodes support moving any of letter 53's 126 M tokens (transcription-doubt flags on f.266r-v)
to S, under a dictionary-word test that a shuffled key must be able to fail?

Premise found on disk first: key_53 was already applied to f.266v by F1 (24 Sept 2026; ciphertext_53.tsv rows
53p2_L01-L03, reading_53.txt). This job therefore does not re-decode f.266v; it runs the regrade test below over the
whole letter (p1 + p2), using decode_key.py's existing output.

Eligible tokens: every row of reading_tokens_53.tsv graded M whose sign is in key_53.tsv (124 tokens). Not eligible:
the two sign-9 tokens (not in key_53, value f by context in exceptions_53.tsv) and the DOT/COL separators (segmentation
doubt, not a letter).

Unit: the DOT-delimited word containing the token, decoded with key_53 (exceptions applied), lowercased and folded
(uu->w, v->u, j->i, y->i, umlauts to base vowel, double letters kept).

Dictionary (genuine period German only; tools/data/de16/composed_enhg.txt is excluded because it is model-composed and
topic-overlapping, a circularity risk): word types from tools/data/de17 (five archive.org OCR files, count >= 2) plus the
genuine sibling decipherment texts on disk in this folder (align_74.txt plaintext units, plaintext_74.txt,
plaintext_98.txt, align_124.txt plaintext units; count >= 1), all folded the same way.
A unit is "in dictionary" if it is a dictionary type, or it splits into two dictionary types each of length >= 3.

Control (rule 3; it can differ, because permuting values changes the decoded letters and so the word membership being
counted): key_53 with its values permuted within frequency bands (signs sorted by n in key_53.tsv, four bands of five),
G1/G7 homophones permuted as independent signs, exceptions held fixed, 1000 draws, seed 53.

Gates:
1. Aggregate gate first: the share of DOT-units of 53 that are in dictionary under key_53 must exceed the control's 99th
   percentile. If it does not, stop: no token moves, log "non-test at this dictionary".
2. Per token (only if gate 1 passes), the token moves M -> S iff (a) its unit is in dictionary under key_53, AND
   (b) the same unit is in dictionary in at most 5% of the control draws (so a short common word reached by chance
   does not count), AND (c) for a 'differ' row, the other pass's sign (recon53/ciphertext_draft.tsv alt column),
   substituted at that position, does not also give an in-dictionary unit.
Every other eligible token stays M. The move is recorded as an exception row (grade S, reason "AVS53 rule") with
"exception_grade_overrides_conf": true for job 53 only; ciphertext_53.tsv (the transcription) is not edited, and the
doubt flag stays visible there.

Known limit, stated now: key_53 was annealed from this same transcription, so a dictionary unit is partly a consequence
of the fit; the control measures chance agreement, not fitting. An S here means "the key reads this sign into a period
word beyond chance", not that the image was re-read. A native-resolution image re-read remains the stronger test.
