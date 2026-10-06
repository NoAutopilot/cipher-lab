# PREREG R8-HEL (6 Oct 2026, written 04:07 UTC by date -u, pushed before any image is fetched or read)

Question: in R1953 (BL Add MS 32275, Hellen, 1752; DECODE record 1953), does any token in R4369's keyed range 801-1796 carry the
wrong one of 0/8 (this hand writes 8 as a loop with a slanted bar, close to its 0; R7A-HEL53)?

Candidates: `zero_eight/candidates.py` -> `candidates.tsv`: 138 tokens of the R7A-HEL53 "all" stream whose code is in 801-1796 and
which have a 0<->8 twin (any subset of their 0/8 digits swapped) that R4369 keys with a different value (39 H, 87 S, 8 M, 4 U).
Of these, 17 were already looked at on the image by R7A-HEL53's reconciler (6 corrected, 6 'differ' upheld, 5 unreached lines
read): they are carried as settled and not re-read. The remaining 121 had two independent readers agree (DECODE's transcriber and a
blind Sonnet read) but no targeted 0/8 look.

Method: the R7A-HEL53 page images are re-fetched (one DECODE browser login; the R7A crops lived in a scratchpad and are gone), line
crops cut with tools/iiif_lines.py. One Sonnet call per page reads only the masked digits: each candidate is shown as its group with
every 0/8 digit replaced by '?', plus its left and right neighbour groups (unmasked) to locate it; the reader answers 0, 8 or
'unclear' per '?'. The key and the meanings are never shown to the reader. This worker then looks at every token where the reader's
answer differs from DECODE or is 'unclear' (reconciliation, one unit).

Decision rule (fixed now):
1. The image decides; key context never does. A digit is changed only if (a) the Sonnet reader gives the other digit AND (b) the
   reconciler, looking at the crop, sees the other digit's form (8 = closed upper loop or crossing stroke; 0 = single open oval
   with no crossing). Both must agree -> corrections.tsv row, confidence high.
2. Reader gives the other digit, reconciler sees DECODE's digit or cannot tell -> no change; row with confidence 'ambiguous',
   not applied; the token is reported as 0/8-ambiguous.
3. Reader agrees with DECODE, or says 'unclear' and the reconciler sees DECODE's digit -> no change, no row.
4. Key context (whether the twin's meaning reads better in the sentence) is recorded in a `context` column for every row, for
   information only. It licenses nothing: a correction that only makes the sentence read better is not made, and a correction the
   image forces is made even if the sentence reads worse.
5. ciphertext_R1953.txt is never modified (rule 2); corrections go to zero_eight/corrections.tsv and are applied on top of
   image_check_r1953's "all" stream in a separate pipe file, re-decoded with the R4369 key unchanged, with --check.

Report: candidates read, changes (high), ambiguous, and H/S/M/U before (image_check_r1953 "all": H 153, S 306, M 16, U 372 of 847)
and after.

Stop rule: cap 3.5, box 04:04-04:49 UTC (80% = 04:40). If the login fails or full-size images are not served, stop and report
"untested at this session", no third attempt.
