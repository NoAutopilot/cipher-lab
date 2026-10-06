# PREREG -- R12-RJM147, rah-juan-manuel-1521: both letter alphabets held out on R9526 (6 Jun 1522) against the CODOIN XXVI print
Written 6 Oct 2026, clock 12:2x UTC (`date -u` 12:23 at the start of writing); committed and pushed BEFORE `python3 scripts/test147.py`
is run for the first time. At this point the worker has NOT seen the token contents of passes/f147_A.tsv or passes/f147_B.tsv (the two
blind Sonnet passes are still running) and no alignment exists.

Material. DECODE R9526 (one browser login, 6 Oct 2026): record page "BRAH Signatura 9/24, f. 147-150", 4 images. P1 right = f.147
(cipher), P3 = f.147v (left) + f.148 (right) (cipher), P2 right = f.150 (the secretaría's decipherment, first page only, "De don Juan
manuel de Roma a vj de Junio 1522"), P4 left = a slip with clear lines over cipher (not used). So A-24 ff.147-148 = R9526 (folio match,
not date only). Plaintext = CODOIN XXVI núm. 36 pp.49-50 ("Capítulo de carta original ... descifrada a continuación por la
secretaría", print opens "....." i.e. a chapter from mid-letter), read from the IA page images and written to
passes/gloss_codoin26_p49.tsv. The print is the grade-C source. Normalisation fixed now: "2,000" -> "dos mil" (the f.150 clerk writes
"dos mil ducados" and f.147v carries a clear "dos"); "V. M." kept as printed; accents folded by the aligner as in test 1.

Span (located before any pass was read, by eye on the images): the f.150 decipherment's "// Los de genova dizen rehusan ..." starts
6 lines from the foot of f.150; f.147v crop line 1 ends in clear "gastaran en ello", line 5 carries clear "puede venir", line 11-12
clear "no creo q hara falta y es muy suficiente ombre para / ello y el lo hara de buena voluntad ... y terna causa para ello", and
f.147v line 16 opens with the B sign that also brackets a clear passage on f.147. Rey de Francia (3x in the print's tail) fits the
repeated "X ges .. ott" groups on f.147v lines 13-14. Crop lines handed to the passes (tools/iiif_lines.py crops):
line 1 = f.147 crop L07, 2-3 = f.147 L08-L09 (the last two lines of f.147), 4-18 = f.147v L01-L15.
- PRIMARY span (gated): lines 2-18.
- SENSITIVITY span (reported only): line 1's tokens after its last B-sign token + lines 2-18.

Method (scripts/test147.py): R12-RJM42's scripts/test42.py functions reused by import (score(), keys()), test 1's reconcile/to_pair,
tools/interlinear_align.py run_align with the identical settings (code prefix @, --code-chunk 2, word codes %, null cost -1.0, max chunk
10, clear-consumes, prior-free). No line is dropped for being in clear: the print carries the clear passages, so bracketed clear words stay in and consume print letters (clear-consumes); this differs from test42, whose clerk wrote "Claro" instead of the clear text. ?n normalisation: filled in an addendum to
this file from each pass's own notes column only, before the first scored run; anything not mapped there stays unscored.

Gate 0, calibration (first): share of nomenclator code tokens whose aligned chunk equals their own table word >= 0.50 (unchanged from
PREREG_f42). Below it, neither key is scored ("non-test at this alignment").

Statistic per key (unchanged): S = share of scored symbol tokens whose aligned chunk equals the key's value (null = empty chunk); keys
alphabet.tsv and key_tomokiyo_alpha.tsv (firm rows with our_label); control = 200 keys with the same values permuted among the same
labels, seeds 1..200 (alignment fixed, values move, so the control can differ from the target on S). Gate per key: PASS iff
S > control max AND S >= 0.24. No incipit exclusion: Tomokiyo's printed line is the letter's first line (f.147 line 1), outside the span.
Scored set = every symbol token in the primary span.

A PASS licenses no key, grade or reading change in this job (brief: report both numbers; no key/grade change); it goes to a verifier.
A FAIL with gate 0 passed is a held-out FAIL for that key at this transcription error (err_2reader reported beside it). Rule 3 note:
this is a different letter and a printed (not clerk-read) plaintext, not a re-run of f.40 or f.199.

## Addendum (12:2x UTC, after both passes reported their row counts and ?n notes, before any token content was read or any scoring)
1. Clear lines: the first draft of this file (never pushed) said all-bracketed lines would be dropped as in test42. Both passes report
   lines 13-14 as mostly clear Spanish; the print contains that text, so dropping them would remove letters the gloss still has.
   Fixed above (no clear-line drop) before the first scored run; the script does not drop them.
2. ?n normalisation from the passes' own notes: pass A used no ?n. Pass B: ?1 "a 7-like numeral or long flourish stroke" -> 7
   (test42's A ?1 precedent); ?2-?8 (tall looped stroke, dagger-like sign, F with a hook, hooked h-like sign, o-like sign with a raised
   stroke, long-tailed flourish, looped flourish at the right edge) stay unmapped (unscored).
