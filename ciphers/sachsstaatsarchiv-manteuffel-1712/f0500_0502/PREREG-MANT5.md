# PREREG-MANT5 (RUN5-MANT5, 4 Oct 2026, written 13:06 UTC by date -u, account 1), before any normalised score

Why: RUN5-MANT4 found code 864 counted *inconsistent* on 0502 only because its two glosses are written "Roy de Prusse" and
"R. de Prusse"; PREREG-MANT4 registered no gloss normalisation (CLAUDE.md rule 3, PX-BRODEC paragraph). This file registers one,
written from the gloss strings in pairs_0500.tsv, pairs_0502.tsv and ../f0501/pairs.tsv, before any normalised alignment or score.

Normalisation (applied to every gloss string, real pairing and every shuffle draw alike, before alignment):
1. Abbreviations: whole whitespace-delimited tokens, after lowercasing and stripping the punctuation `.,;:'"`, are expanded by
   gloss_norm.tsv (r -> roy, pr -> prince, pol -> pologne). This is every abbreviation present in the three leaves' gloss strings.
   Nothing else is expanded; truncated or uncertain name glosses ("stein", "lexander") are left as written.
2. Case: one case (lower). Already done inside tools/interlinear_align.py plain_letters() (seg.lower()); restated, no change.
3. Punctuation: one set -- apostrophes and stops become token breaks, then all non-letters are dropped by plain_letters()
   (re.sub [^a-z]); 0501's "qu'un" -> "qu un", matching 0500/0502's existing transcription convention.
4. NOT normalised (registered so it cannot be added later): period spelling variants (celuy, feldt/feld, honnete), accents
   (none present), word division, s/f and u/v (the tool's own fold() applies as before).
Everything else is PREREG-MANT4 unchanged: same aligner options (--floor 0 --max-chunk 14 --seg-bonus 1.0 --len-prior 0.5, no
--prior), same S / S_multi definitions, 200 pairing-shuffle draws, seeds 500 (0500), 502 (0502), 501 (0501), gate N_rec >= 3 AND
S_real > p95(S_shuffle) strictly; tie or miss = leaf HELD, nothing into key.tsv. Grades as PREREG-MANT4.
0501 is re-run only as a check that nothing else moved (its prior result: S 0.400 vs p95 0.200 PASS, S_multi tie 0.250); its key.tsv
entries (770 C, 865 M) are not re-graded by this run unless the normalised gate *loses* the PASS, which would be reported as a flag.
Expected effect stated in advance: only 864 (0502) and the "pr" runs of 0501 change input; 0500 has no abbreviation, so its result
must reproduce RUN5-MANT4's exactly (a reproduction check on the script). Script: shuffle_control_norm.py PAIRS SEED OUT.
