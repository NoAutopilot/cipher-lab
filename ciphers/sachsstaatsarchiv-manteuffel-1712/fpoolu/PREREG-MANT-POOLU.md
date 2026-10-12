# PREREG-MANT-POOLU (12 Oct 2026, 18:3x UTC by date -u; LANE DEFAULT-A2-1810 account 2; pushed in its own commit BEFORE any crop pass, decode or score)

Job: .claude/briefs/runs/2026-10-12-ytbiz-default-1810-jobs.md "MANT-POOLU". Never-read code-bearing leaves of HStA Dresden 10026 Loc. 694/08
(MANT-CEN5 census_unglossed.tsv), pooled to a length the gate can test. Key: key.tsv at origin/main as of this commit, unchanged by this job.

## Pool (fixed now; six frames, the brief's maximum)
Frames fetched once each 12 Oct 2026 18:29 UTC (frames.tsv URLs, HTTP 200; images in scratch, folder over 30 MB):
| frame | film label | date / stamp | sha256 prefix | code lines seen at 1450 px (worker's eye, before any pass) |
|---|---|---|---|---|
| 0088 | 0089 | Berl. 31 May 1712, No 35, stamp 65 (right page) | 66b01d938e909baa | ~6 runs + singles (13 several times, 171, 1.44), ~35-40 tokens; small writing above some runs |
| 0247 | 0248 | Berl. 6 Aout 1712, No 63, stamp 191 (right page) | 06962d6f84a1da6f | 57.28.35.59, 272, 57.28 -- ~7 tokens; no writing above seen |
| 0426 | 0427 | left page = end of a Manteuffel report (para 7), stamp 335/6 area | da42dc86ecf6d3da | one ~10-code run with a small word above; right page Flemming to Manteuffel, Greifswald 23 Oct 1712, single 46 x2 |
| 0442 | 0443 | stamp 349 (right page) | e0ae6101db898692 | 217, 35.30.51.66.21.120, 187 -- ~8 tokens; no writing above seen |
| 0483 | 0484 | Berl. 11 Nov 1712, page 386 (right page) | 370618475942c6a4 | para 3 run ~6.21.2.28.6.35.5.10 (insertion above), last line 103.34.26 -- ~11 tokens |
| 0489 | 0490 | Berl. 15 Nov 1712, stamp 391 (right page) | a7a5c13298f4b1cc | run 44.66.63.50.39.60.35.51.15.26.10.2.35 with small writing above; 150 with a word above -- ~14 tokens |
Dropped / skipped (one line each): **0146** (Berl. 25 juin 1712, No 48) dropped -- Acta Borussica BO I pp.212-213 quotes a Manteuffel report of
25 June 1712 (mant0608/abbo_check.py PRINTED; MANT-0136B: it names Ilgen in clear, leaf "film ~0145-0146"); whether the quote covers 0146's runs
cannot be settled from disk (BO I djvu not on disk; archive.org reserved for THUR-94 this wave), so it is treated as printed. **0435** skipped --
already transcribed and decoded by MANT-R8 (8 Oct 2026; not never-read). 0088 kept: BO I paraphrases the 31 May dispatch (MANT-0089) by the
names of 0089's runs (Creutz, Krautt, Blaspil); no quotation of 31 May was found, and 0088's runs are other runs. Disclosed.
Disclosure: the worker has seen key.tsv and these six frames at sheet scale (1450 px) before this file; no crop, pass, decode or score exists yet.
Estimated pool from the sheets: ~85-95 code tokens, of which the unglossed letter-class part is not known until the passes (several runs carry
writing above, which leaves the gate stream by the rule below). If the gate stream is short, the power rule decides (too-short), not this file.

## Inputs
- Crops: `tools/iiif_lines.py --image <frame>.jpg --out fpoolu/crops ...` strip crops of the code-bearing lines only, each strip tall enough to
  include the band above the code line (where any interlinear writing sits); committed with manifest.json.
- Two blind Sonnet passes (A crop order, B reversed), one subagent call per frame per pass; short frames (0247, 0442, 0483) may share one call
  per pass, crops labelled per frame. Passes see no key value; they read the code digits AND any writing above a group, verbatim (V-BRANDT).
- Worker reconciliation of code DIGITS only, from native zooms, where the passes disagree -> fpoolu/ciphertext.tsv (line ids prefixed by frame,
  e.g. 0088R03). Disclosure: key.tsv seen; digits settled from the image; doubtful digits conf low. Writing above is never settled by the worker:
  each pass's text is kept as that pass wrote it (fpoolu/gloss_A.tsv, gloss_B.tsv; a span = the token ids it sits over).

## Gate (b), the pooled gate (decides; per-leaf numbers reported only)
- Stream = every code token of the pool, frame order 0088, 0247, 0426, 0442, 0483, 0489 and reading order within a frame, that (i) is in key.tsv
  with a 1-3 letter value, (ii) is NOT under writing above in EITHER blind pass (union of gloss_A/gloss_B spans), (iii) is not in a
  NAME-ABBREVIATION group (a maximal run of exactly 2-3 codes whose sequence occurs as a whole run >= 3 times in the pool). Whole-name codes
  (150, 171, 187, 217, 257, 272, ... any value of 4+ letters or a name) and codes not in key.tsv leave the stream.
- Judge: fr18 4-gram (tools/judge_plaintext.py LANG_CORPORA["fr18"]), as MANT-0454 / MANT-0181.
- (i) key-permuted control: letter values permuted among key.tsv's letter-valued codes, 1000 permuted keys per scored unit, p95 / p99.
- Block rule (MANT-0177/0181 design, because the positive-control windows exist only up to 52 letters: 11 windows at 52, 3 at 60, 0 at 70 --
  power "at the pool's N" cannot be measured above 52; disclosed deviation from the brief's wording): pooled letters L <= 52 -> scored whole
  (seed 4400), power at L; L > 52 -> consecutive non-overlapping 52-letter blocks from the start (seed 4400+k), power at 52; tail < 52 reported.
- Power: windows from 694/09 0085 r9+r10 and 0136 unglossed (as f0181_08/judge_gate.py), 200 permuted (seed 7) per window, pass if real > 190th
  of 200; a TEST only if power >= 0.80, else "too-short" (no S grade, not a negative).
- (ii) SHUFFLED-TARGET control (MANT-0181; CLAUDE.md rule 3, ARM-C1): the stream's token ORDER shuffled 100 times (seed 4410+k), each decoded
  under the REAL key and scored on the same letter span. VOID test: if more than 5 of 100 shuffled-target decodes score above the (i) p95 of that
  block, the judge is VOID for this pool ("judge cannot decide"); order test: block PASS also needs real > 95 of the 100 shuffled orders.
- Block verdict: PASS (TEST, not VOID, real > (i) p95 AND > shuffled 95th), FAIL, VOID, too-short. **Pool verdict: VOID if any block is VOID;
  else too-short if power < 0.80; else PASS if every block PASSes; MIXED if some; FAIL if none.** A tail is never gated.
- Reported only, never a gate: the whole pool scored against (i) and (ii) at its full length (no power behind it above 52); each frame's own
  stream against (i) (seed 4420+frame index); each run's decode and score.
- Expected risk, stated before any number: at N >= 52 the shuffled-target decode keeps the real key's letter frequencies, which the permuted-key
  control destroys, so VOID is a likely outcome (MANT-0181 voided at 51). A VOID is reported as "judge cannot decide", not as a negative.

## Known answers (reported only, not a gate)
For each span with writing above: each blind pass's text beside the key.tsv decode of the codes under it, with a letter-position match count
(fpoolu/known_answer.tsv). No threshold; never settled by the worker; N is too small for a gate unless >= 5 spans of >= 3 letters exist, in
which case it is still reported only (no gate is pre-registered for it).

## Grades (rule 4; fpoolu/grade.py)
H only where key.tsv's row grade is H (none). S only for a stream letter token, conf high/med, in a PASS block of a TEST pool that is not VOID.
Name / whole-word codes M; name-abbreviation groups M; low-conf digits M; tokens under writing above M (C is not claimed: the writing is not
settled by a gate here); codes not in key.tsv U; repaired I.

## Decode and checks
Decode with tools/decode_key.py fpoolu (decode.json in fpoolu/, the folder's existing per-leaf layout; no private decoder), `--check` exit 0.
Check 5: decoded phrases with clear context through tools/print_check.py (no IA host this wave; HTRC/OpenAlex/crossref only, Google Books
skipped: googleapis answered 503 to the lane at 18:1x UTC) before any "not located" sentence. Fixed before any score; any deviation is disclosed
in NOTES.md as a deviation.
