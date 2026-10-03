# GAPS23 pre-registration: 2077 legend decode vs the plain Nota of 4.VEL 2078 (3 Oct 2026, account-4)

Written 3 Oct 2026 04:48 UTC (clock read), committed and pushed before the 2078 Nota is transcribed and before any score.
Job: VERIFY-SURINAME-2077 (AUDIT.md item 4) named this step: 4.VEL 2078 (Wollant, July 1782, plain plan of the same fort,
"Nota") lists the same buildings in plain Dutch. 2078 is a *parallel* text (different wording and order), not the 2077
plaintext, so the test asks: do the 2077 decoded letters agree with the partner 2078 entry more than with a non-partner
2078 entry, and more than a wrong key's letters agree with the right partner?

## Inputs (fixed now)

- 2077 side: `ciphertext_2077_legend.tsv` + `reading_2077_legend_nieuw_tokens.tsv` as committed (decode_key --check exit 0,
  658 tokens H 500 M 106 U 52). An entry is the run of cipher tokens from an entry-label plain word (`w:a` ... `w:z`,
  `w:α.` etc.) to the next label, across lines; plain words inside the entry are dropped (they are not under test).
- 2078 side: the left-hand Nota ("Pl. Ie E", present state) of NA 4.VEL 2078, transcribed from the archive's own scan
  (service.archief.nl IIIF, 8046x6210) with tools/iiif_lines.py crops, two blind Opus reads + at most one reconciliation.
  Readers see only the crops and are told it is 18th-century Dutch handwriting; they never see the 2077 decode.
  The book facsimile (den Heijer 2012 p. 329) is the fallback only if the IIIF fetch fails.

## Gating pairs (chosen by the verifier in AUDIT.md item 4 before this job; not re-chosen)

2077 q <-> 2078 b ("Artillerie Casserne en Monteerings Kamer"); 2077 u <-> 2078 d ("Laboratorium van d'Artillerie");
2077 r <-> 2078 k ("Adjudant Wooning & Garnisoen Schryvery"); 2077 t <-> 2078 n ("Bakkery, defect");
2077 p <-> 2078 c ("Casserne, oud en defect"). The 2078 text used is the reconciled transcription of that entry letter,
not the verifier's paraphrase. Any further pairing found after transcription is SECONDARY: reported, never gating.

## Normalisation (both sides; the PX-BRODEC lesson)

Lower case; long s -> s; ÿ and ij -> y; & -> "en"; every character not a-z dropped. A multi-letter 2077 value (a code
group) expands to its letters, each with the token's grade. Nothing else (no c/k, ae/a, d/t merging).

## Statistic

Per pair, a Needleman-Wunsch alignment of the 2077 entry's tokens (global on the 2077 side) against the 2078 entry's
letters (free end gaps on the 2078 side): +2 when the 2078 letter is in the token's value set (an M token `g|l` has two;
a U token `?` has none), -1 mismatch, -1 gap. Statistic A = (H tokens aligned to the identical 2078 letter) / (H tokens
in the entry). Pooled A = sum of matches / sum of H over the five pairs. Script: `passes/nota2078_gaps23/score.py`,
committed with this file.

## Controls (each can differ from the target on A)

- N1, label shuffle: each 2077 gating entry is aligned to a 2078 Nota entry drawn uniformly from all transcribed 2078 Nota
  entries other than its own partner; 2000 draws of the pooled A. (Changes the partner text, so A can move.)
- N2, value-shuffled key: a uniformly random permutation of the 26 letters is applied to every 2077 token value (the
  same as a value-shuffled one-to-one key), aligned to the true partners; 2000 draws. (Changes the letters, so A can move.)
- Seed 20261003.

## Gate

PASS if pooled A (real) > p99 of N1 AND > p99 of N2. Otherwise FAIL (logged as a FAIL with both control numbers;
the target stays `partial`, rule 5). Per-pair A and per-pair N1 p99 are reported, non-gating. A letter confusion table
(H value vs aligned 2078 letter) is reported, non-gating, descriptive only.

## Regrade rule (applied only on PASS)

Within a gating pair, or a secondary pair whose own A exceeds its own N1 p99 (pair-level, same 2000-draw method), a 2077
token graded M or U that the optimal alignment places on a 2078 letter L (not a gap) is regraded C with value L when
(i) for M, L is one of its listed values (a 2078 letter outside the M set changes nothing and is logged), and (ii) the
nearest three H tokens on each side inside the entry (fewer if the entry boundary is closer, at least two in all) are
each aligned to an identical 2078 letter. Written to `exceptions_nieuw_image.tsv` (grade C, reason names the 2078 entry),
then `tools/decode_key.py ciphers/na-suriname-map-1781` and `--check` must exit 0. New H/C/M/U counts and M+U rate
reported. The verifier's AUDIT.md class is not touched.
