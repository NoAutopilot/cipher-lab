# PREREG CLIN-F49 (16 Oct 2026, 13:5x UTC by date -u; written before Image 1125 is fetched, before any pass and before any score)

Job CLIN-F49 (account 4, brief .claude/briefs/runs/2026-10-16-acct4-research-steps-2.md). Item: **B.148 f.49** (H-1649 Image 1125,
IIIF c0sn0105nb0k), Carleton to Haldimand, 22 July 1782 (Tomokiyo, sources/cryptiana/web/haldimand.htm: "A deciphered letter from the
same date is at p.50-51 but does not seem to match"; Tomokiyo prints an extract of about 80 groups with his own reading of it).
No period decipherment of this page is recorded in this folder. Images 1126-1127 (pp.50-51) are not fetched in this job.

**Belief before the test:** high (~0.9) that the x-marked letter cells read under the 1778 title-page key: Tomokiyo's extract spells
"indications", "hostile", "pointing", "new", "disposed", "think", "bearer" from x-marked groups whose line-position pairs fit
title1778_reading.txt (spot check of x23-5 = i, x23-8 = n done from the printed extract, not from the page). The open question is
whether the whole page does, beyond the extract, and what the rest of the letter-spelled text is.

**Design (CLIN-3502B/check_p300.py's B2 unchanged except the hit test, because there is no known answer):**
- Key: passes/title1778_reading.txt as printed (variant a) GATED; variant (b) (line 1 "BY PERMISION of the RIGHT HONORABLE")
  reported, not gated.
- Cell classes, rule R0 (PREREG-UNA-CLIN): x/+ L-P or -P = letter; full pair without x/+ = word code (the 1782 code list; not decoded
  by this job; Tomokiyo's glosses for word codes are not used in any score).
- A run = >= 3 consecutive all-H letter cells in one column, ended by an underline or a non-letter cell.
- **Hit (replaces the known-answer substring test):** the run's decoded string, letters only, is a word of the era lexicon, or splits
  into exactly two lexicon words of >= 3 letters each. Lexicon = every word (a-z only, lower case) occurring >= 3 times in the en18
  corpus (tools/data/en18/*.txt.gz, American official correspondence 1788-1819; nearest era-matched English corpus on disk; no 1782
  British corpus exists in tools/data). Fixed now: no other lexicon, no prefix/suffix credit, no edit-distance credit. A real word
  misspelled by the encipherer counts as a miss (bias against PASS, accepted).
- Control: page-permuted key (title page letters shuffled, line lengths kept), 1000 seeds, seed 123, same hit test.
- Prechecks (printed before hits are looked at): can_differ >= 0.99 and runs_ge3 >= 10, else NON-TEST.
- **Gate: B2 share >= 0.60 AND hits > control max.** Not re-tuned after scoring.
- Reported, not gated: per-run agreement of our decode with Tomokiyo's printed extract (his letters vs ours on the same groups).

**Method:** Image 1125 fetched once at full/max (scratchpad), 1600 px copy committed; columns cut by tools/iiif_lines.py; two blind
Opus reads (one subagent each, crops only, no key, no reading, not told the question); worker reconciliation on the crops only,
before any decode or score; a cell still open is M and breaks a run. No cell changed after the scorer is first run.
Scorer passes/check_p49.py (check_p300.py with names, input and hit test changed; --check exits 1 when stale).

**What would change the belief:** FAIL (share < 0.60 or hits <= control max) = the 1778 key is not shown to read the page beyond its
extract (could be transcription error, a different key for part of the page, or 1782 code groups mis-classed as letters). NON-TEST =
too few runs. A PASS says only that the 1778 key reads these runs as English words beyond the permuted-key control; it is not a reading
of the word-code groups and not a novelty claim (rule 10).

## Decision
- PASS: decode; letters S inside gate-passing runs, M elsewhere; reading_p49.txt with grade counts; print_check on decoded phrases;
  compare with Tomokiyo's extract and the Brymner B.148 calendar entry for 22 July 1782 (disk only); ROOM "reading ready" for a verifier.
- FAIL or NON-TEST: write the numbers in NOTES.md and stop (f.93 is not this job).
