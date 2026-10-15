# PREREG-OBRED552 (15 Oct 2026, 08:3x UTC by date -u; addendum to PREREG-OBRED556, written before scans 552-554 are fetched or any number computed)

Job: NL-HaNA 1.01.02 inv. 6019 scans 552-554 (the start of the Oggersheim letter of 14 Oct 1619 whose numeral blocks are on 555-556,
OBRED-556) and a second blind pass of scan 555 line L15 ("30 265 434 530 320", one transcription only in OBRED-556).

1. Placement, by eye, before any transcription: for each of 552, 553, 554 record hand, address/dateline/signature, and whether the text
   runs on into 555 (555 left page begins "de Catholijcken ..."). A scan that holds no part of this letter is recorded as what it is and
   not transcribed.
2. Transcription protocol exactly as OBRED-556: crops by `tools/iiif_lines.py --image ... --debug` (overlay checked), two blind Sonnet
   passes (not told any value, no. 92 or the 556 transcription), reconciled by this worker on the crops; grade H-read where both passes
   agree with high confidence, M otherwise. Glosses read once by this worker on taller crops, checked once blind (Sonnet); C where both
   agree on one letter/name over one group, M otherwise. Output rows appended to `ciphertext_556.tsv` with the same columns (scan column
   carries 552-554).
3. 555 L15: one new crop that holds the whole line; two blind Sonnet passes (a separate crop call each). If both new passes agree with the
   OBRED-556 single read on a group, that group is H-read; otherwise M with all readings in the note.
4. Scoring: none gated. If new numeral groups are found, `obred187/overlap556.py` is NOT re-run with a changed input (its gate stays as
   frozen); this job reports only a descriptive count of new distinct values and how many are in R = V92 | V187, labelled "descriptive,
   not gated". No --try, no key.tsv edit (OBRED-TRY's step).
Requests: service.archief.nl <= 8 (METS + 3 scans at 5000 px + at most 4 re-fetches); NA take/release ROOM lines; images not committed.
