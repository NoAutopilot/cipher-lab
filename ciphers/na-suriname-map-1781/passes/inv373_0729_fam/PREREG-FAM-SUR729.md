# PREREG-FAM-SUR729 (LANE FAMILY, account 2), written 8 Oct 2026 ~17:30 UTC, pushed before any crib is transcribed or scored

Source: NA 1.05.03 inv. 373 scan 0729 (No 552c "Petitie", Nieuw Amsterdam batch, Oct 1781), native 4799x3976 from service.archief.nl
IIIF. Its ruled table has row labels in cipher with plain glosses "Voor het Fortres Nieuw Amsterdam", "Voor het Fort Zeelandia",
"Voor het Fort Leyden", "Voor de Schans Purmerent", "Voor de vlot Batterijen"; the running text above names the same four sites
(glossed). Question: do 0729's cipher spellings of the site names match, sign for sign, the site name in the map title cartouches
already transcribed in this folder (4.VEL 2046 "redout Purmerent": ciphertext_2046_legend.tsv lines 2046_title1/2046_title2;
4.VEL 2077 "fortress Zelandia": ciphertext_2077_legend.tsv lines 2077_L01-L03)?

Cribs. The cipher word(s) under the gloss "Purmerent" and under "Zeelandia" (word boundaries as written; "Fort"/"Schans" excluded),
transcribed by this worker from native crops into the folder's sign names (glyphs.md / ciphertext tsv conventions), at every
occurrence on 0729 (row label and running text). If two occurrences of one name differ, both are scored and the lower is reported as
the headline. Leyden vs 2061 and Nieuw Amsterdam vs 2039 are NOT scored: no title-cartouche transcription of either is on file.

Statistic S(crib, lines) = max over every ungapped window of the crib's length inside one line (no wrap across lines) of the number of
positions whose sign label is identical. Reported as k/len.

Hit (per crib), all three required:
 (1) S on its own site's title lines >= 0.5 x len;
 (2) cross-site/other-text null: S on its own title lines is strictly greater than S over every window of every OTHER transcribed map
     line in the folder (ciphertext_2039_legend.tsv, ciphertext_2039_remarque.tsv, ciphertext_2061_battery.tsv, ciphertext.tsv, the
     other site's legend file, and the non-title lines of its own sheet);
 (3) shuffled-crib null: S on its own title lines > the 99th percentile of S for 1000 random permutations of the crib's own signs
     (seed 729) against the same title lines.
Both nulls change which signs fall at which window positions, so each can differ from the target on S (rule 3: not a non-test by
construction).

Use of a hit. Grade C only for a value the 0729 gloss fixes: a 0729 cipher sign whose plain letter is fixed by letter-count alignment
of the crib to its glossed word (equal length, or one unambiguous homophone/null position). On the map, a cartouche token identical to
an aligned crib sign takes that value at C only where it is currently U or M and the aligned value is fixed; where it is already H and
agrees, it is noted as corroboration (no grade change); where it disagrees, it is logged to conflicts.tsv and stays as it is (M at most).
Everything else M. A miss changes no token. A descriptive value-level comparison (both sides decoded under key_period_codes_nieuw.tsv)
may be reported but is not part of the gate.
