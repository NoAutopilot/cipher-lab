# BIR-CCE (account 3 worker) -- 4 Oct 2026 15:0x UTC (account-3 orchestrator; owner approved)
Target: ciphers/nevers-birago-fr3251-1572. Read research/MARY-STUART-METHOD-2026-10-04.md (sections 1 row 15, 3 "Birago") and
LESSONS-LASRY.md section 3 item 8 first. Hypothesis (Lasry et al. 2023, App. B "cross-cipher contamination"): some of the 1572 letters'
off-sheet or conflicting signs are the clerk using a symbol from the EARLIER Ceppo-Nevers key
(ciphers/ceppo-nevers-fr3251-1570s/keys/key_ceppo_nevers.tsv) instead of the 1572 key (keys/key_nevers_birago_1572.tsv). Caveat to state
in every output: same-day use of both keys by one clerk is NOT established here, unlike Mary Stuart's packets.
1. Glyph correspondence first, value-blind: map each 1572 off-sheet/conflict sign shape (harvest/offsheet/subtype_counts.tsv, the X_*
   labels incl. X_CE, the T95/T50 conflict, T42) to a Ceppo-Nevers table cell by SHAPE ONLY, from the two key images (Tomokiyo's
   nevers_add1.png and NeversBirago.png, sources/cryptiana or as the key files' headers say) and the atlas tiles -- one Sonnet vision call
   on a montage, never shown any plaintext or value; write cce/glyph_map.tsv (1572 sign, Ceppo cell or none, confidence) and push it
   BEFORE any value is looked up.
2. PREREG (pushed before scoring): statistic = for each mapped sign occurrence in nos.71/73/77/85/86/90 (committed reading tokens, not
   no.87, which stays the known-answer item), the it16dip/fr16 n-gram gain of substituting the Ceppo value vs leaving it unread (and vs
   the current 1572 value for conflict signs); null = the same with Ceppo values drawn from shuffled glyph-to-cell maps (shuffles of the
   Ceppo cells among mapped signs, 1000 draws) -- a null that CAN differ from the target on this statistic (rule 3, check it in the
   prereg). Known-answer check first: on no.87, where the clerk sheet (key_1572_clerk.tsv) is C, mapped signs with a clerk value must
   show whether the Ceppo value matches the clerk value more often than the shuffled null; if no mapped sign occurs on no.87, say so and
   the test runs without a positive control (report as weaker). Gate: target gain > null p99.
3. Report per sign: occurrences, Ceppo value, gain, null p99, verdict; nothing enters key.tsv or exceptions in this job (a PASS sign is
   graded M with a ROOM line for a later verifier). Write cce/RESULTS.md, a NOTES.md section, HYPOTHESES.md row.
Disk only except at most 2 Gallica/cryptiana fetches if a key image is not on disk. Model Opus 5.5 worker, Sonnet for the one vision
call. Cap USD 4, box 60 min. ROOM claim/done via tools/room.py. Do not touch other targets.
