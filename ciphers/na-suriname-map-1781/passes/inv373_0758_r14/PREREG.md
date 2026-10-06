# PREREG R14-SUR758 (6 Oct 2026, 15:5x UTC by date -u; committed and pushed BEFORE the blind pass is run or score.py exists)
Material: NA 1.05.03 inv. 373 scan 0758 (IIIF fb805061-...ba36.jp2, native 4834x3988), right page (folio stamp 681): a plain
letter with two enciphered passages, each cipher line with a lighter plain Dutch line ABOVE it. Upper passage 6 pairs (crops L01-L06;
L01's cipher line opens with the plain words "nige eclaircissementen door vraagen" and its gloss "noopens den Staat" sits over the
cipher part only; L06 is the gloss "winnen" over a short cipher group). Lower passage 5 pairs (L11-L15; L15 is a short gloss over a
short group at the foot). L07-L10 are plain letter lines, cut only so band edges fall between the passages; not given to the reader
and not scored. 15 crops cut by tools/iiif_lines.py (crops/manifest.tsv). Crops not committed (folder over 30 MB).
Question: does 0758's cipher use the same sign system as the map key / the 0692-0693, 0702 and 0730 letters?
Method: R13-SUR702's PREREG and score.py unchanged in every rule (passes/inv373_0702_r13/PREREG.md), with R13-SUR730's parser fix
('\&' = one sign '&'), except:
- Reader: ONE blind Sonnet pass on the 11 pair crops (crop paths only; the same reader-code vocabulary as 0702/0730/0746; NO values,
  NO key) -> passA_sonnet_blind.tsv. NEW (R14-SUR746 lesson): the reader is told to write ' | ' at EVERY visible blank space between
  sign groups in the cipher line (the writer's own gaps), and to write single spaces only between signs inside one group. The word
  pairing then splits on '|' only. Plain words written in a cipher row (L01's opening) are to be written as one token
  [plain: ...]; the scorer drops [plain...] tokens. The worker reconciles the GLOSS only -> gloss_reconciled.tsv; no blind cipher
  token is altered for S1/S2.
- S2 = agreement with the POOLED 0693+0702+0730 sign table (as R14-SUR746). S2 descriptive.
- Control: gloss letters permuted across all used positions, 1,000 permutations, seed 758 (can vary on S1 and S2).
Gate (unchanged): SAME SYSTEM if S1 (key_period_codes_nieuw.tsv) >= 0.60 AND S1 > control p99. Otherwise 'not shown'.
Power floor (R14-SUR746 lesson, set now): if fewer than 30 keyed positions align, the result is logged 'non-test: underpowered'
whatever the numbers, not a pass and not a negative.
Per-code table descriptive; conflicts with an H/C value seen >= 2 times -> conflicts.tsv rule-4 data row (no key edit);
[y-fam] m|n vs d counts added to the y row of conflicts.tsv as a further glossed witness.
Descriptive, no gate: blind sign count vs gloss letter count per pair (as R14-SUR746 signcount.tsv).
No key.tsv / key_period_codes_nieuw.tsv edit; candidate values -> candidates_0758.tsv for a verifier.
Also listed (not tested): gloss words naming a map sheet, a legend letter or a fortress work, as crib candidates for 4.VEL 2039.
