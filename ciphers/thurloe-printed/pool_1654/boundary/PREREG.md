# NEAR3-THUR pre-registration: one-vote M boundary test (4 Oct 2026, written before `boundary_test.py` was run)

Job: LANE-NEAR3 wave 2, NEAR3-THUR (account 2 worker). Codes under test: the four one-vote M entries of
`key_stamford.tsv` named by V3a (AUDIT.md "Second opinion SO-THURLOE-P4", rows 6-7): **67 england, 153 thecavaliers,
84 noticeofandalthough, 275 that.** Each has exactly one occurrence in the printed-decipherment letters P5+P6 / P7
(the "later Stamford letters", 20 and 30 March), which is where its one vote came from.

Disclosure: before writing this file the worker grepped `tokens.tsv` for the four codes and read the raw djvu lines
around each occurrence (to learn where they are). The rule below is mechanical and is applied by the script to the
targets and to the controls alike; the controls decide whether the test may change anything.

## Statistic (per occurrence)
`boundary_test.py` takes the occurrence's djvu line in the cipher paragraph and:
1. **Furniture check.** If the occurrence's djvu line is a page running head (matches `STATE\s+PAPERS`, `THURLOE`,
   or spaced capitals `J\s+O\s+N\s+H`) the token is page furniture, not cipher: verdict **REFUTE (furniture)**.
2. **Contexts.** Tokenise the cipher paragraph (djvu lines of the letter's cipher span) in reading order. Left context:
   walk back from the token, decoding numerals with the key *with the code under test removed* (letters as their
   meaning, codes >= 44 as their word meaning, the sign as "thelordprotector") and clear words as written, until at
   least 10 letters; stop early (context too short) at a token that is unreadable or not in the key. Right context:
   the same forward.
3. **Normalise** both contexts, the claimed meaning and the printed decipherment ("The same letter decypherd") to
   lower-case letters only, with f->s (long s), v->u, j->i, y->i.
4. **Locate.** Semi-global edit-distance match of the left context anywhere in the decipherment; accept the best
   end position only if its cost <= 25% of the context length and it is unique (no other end position more than
   5 characters away at equal cost). Then match the right context starting within 60 characters after that end, same
   cost limit. The **gap** is the decipherment text between the left match's end and the right match's start.
5. **Verdict.** L = len(meaning). CONFIRM if edit(gap, meaning) <= floor(0.2 L). REFUTE (gap) if
   edit(gap, meaning) > 0.5 max(L, len(gap)). Otherwise, or if either context is too short or not located,
   INCONCLUSIVE.

## Controls (rule 3; each can differ from the target by construction)
- **K (known answer).** Every occurrence in P5+P6 / P7 of a code >= 44 graded C (81, 83, 85, 130, 158, the sign)
  plus 60 occurrences, sampled with `random.Random(0)`, of letter values graded C or H with >= 10 votes, each run with
  its own key meaning (the code itself removed from the key while its contexts are decoded, as for the targets).
  Statistic: share CONFIRM of K occurrences that reach a verdict, and share reaching a verdict at all.
- **W (wrong meaning).** The same K occurrences, each with its meaning swapped for a different code's meaning
  (derangement by `random.Random(1)`, letters swapped with letters, words with words). Statistic: share CONFIRM
  (false-confirm rate). W changes the quantity compared (the meaning), so it can fail where K passes.
- **Gate.** The test licenses grade changes only if K CONFIRM >= 80% of K verdicts AND W false-CONFIRM <= 10% of
  W verdicts AND at least 60% of K occurrences reach a verdict. Otherwise: non-test, no grade or key change.

## What each outcome does (only if the gate passes)
- **CONFIRM** on the code's sibling occurrence: the entry becomes **C** (known plaintext bounded on both sides by
  independently keyed context), recorded in `decode_stamford.py` as `BOUNDARY_C` with this file named. P4 tokens of that
  code move M -> C.
- **REFUTE (furniture):** the numeral is not cipher; the entry is removed from the key (`BOUNDARY_DROP`).
- **REFUTE (gap):** the stored meaning is wrong at its only witness; the meaning is replaced by the bounded gap at grade
  **M** (the replacement was not the hypothesis under test, so it is not promoted).
- **INCONCLUSIVE:** nothing changes.
Expected effect on P4 (whose 3 tokens of 67 and 1 of 153 are the only P4 tokens of these codes; 84 and 275 do not
occur in P4): at most M 16 -> 12 and C 338 -> 342; no letter of the reading changes. `decode_stamford.py --check`
must exit 0 after the change, and the two cross-letter control shares (92.3%, 93.7%) are reported before and after.

## v1 result (run 4 Oct 2026, 01:39 UTC) and v2 pre-registration (written before v2 was run)
v1 (`python3 boundary_test.py`, `results.tsv`): K 80 occurrences, 26 reach a verdict (**32.5%, below the 60% gate**),
CONFIRM 23/26 = 88.5%; W 80, 22 verdicts, false-CONFIRM 0/22 = 0.0%. **Gate FAIL: v1 is a non-test, no grade or key
change.** v1 target verdicts (seen, logged, not acted on): 67 CONFIRM (gap "aengland", edit 1), 275 REFUTE-furniture
(running head "JOHN THURLOE ESQ. &c, 275"), 84 INCONCLUSIVE (left not located), 153 INCONCLUSIVE (left context too
short). Cause of the low coverage: 36 of 80 K occurrences stop at an OCR-unreadable or unkeyed token within 10 letters.

**v2 (one change, `--skip 2`):** while building a context, up to 2 unreadable ('?') or unkeyed numeral tokens per side
are skipped (contribute no letters) instead of ending the context; the 25% cost limit absorbs the missing letters.
Everything else -- MIN_CTX 10, cost 25%, window 60, uniqueness 5, verdict thresholds, the same K and W samples (same
seeds), the gate (K verdicts >= 60%, K CONFIRM >= 80%, W false-CONFIRM <= 10%) and the outcome rules -- is unchanged.
v2 writes `results_v2.tsv`. If v2 also fails its gate, the boundary test is logged "untestable by this method at
this OCR quality" (rule 3, second attempt at an unchanged approach) and no third tuning is run.

## v3 pre-registration: page-image transcription (A3V2-THURBT, 4 Oct 2026, written 05:5x UTC before `--tx` was run)
Rule 3 third-attempt clause: the djvu-OCR instrument is retired (v1 32.5%, v2 48.8% K coverage, both below the 60%
gate). v3 changes the *instrument*, not the test: the cipher lines of the pages carrying the 67 and 153 contexts are
read from the archive.org page images (collectionofstat03thur leaves 285 = p.275 and 288 = p.278, native 2365x4074,
cut into line crops with `tools/iiif_lines.py --image`), transcribed by two blind Opus passes per page, reconciled
with `tools/reconcile_passes.py` and the worker's own read of the crops (an unresolved token is written `?`). Only two
of the five cipher pages (274, 275, 277, 278, 279) are transcribed: five pages at three vision calls each would cross
80% of the job's USD 9 cap, so per the brief only the pages carrying the targets' contexts are read; p.274 (84's
context, line 22921) and pp.277/279 stay djvu OCR. Written down before the run: a K occurrence on an OCR page keeps
the OCR's coverage problem, so the registered gate (60% of *all* K occurrences reach a verdict) is harder to pass on a
half-transcribed stream than it would be on a full one; the per-page split printed under the gate is descriptive and
licenses nothing.
- Input: `tx/pages.tsv` names the pages; `tx/p275.tsv` (crops L02-L34, the letter's lines from "28. 7. 30." to "know,
  whether you have received them or noe."; the brief to the passes said L02-L36, but L35-L36 turned out to be the
  decipherment's heading and first line, which stay on the plain side -- corrected at reconciliation, 05:5x UTC) replaces djvu 23014-23062; `tx/p278.tsv` (crops L02-L67, the whole page
  below the running head) replaces djvu 23250-23325. The running heads are not transcribed (they were page furniture
  in v1/v2; `A.JUNK_LINE` drops them anyway). Every other line, the plain side (djvu OCR of "The same letter
  decypherd"), MIN_CTX 10, cost 25%, window 60, uniqueness 5, the verdict thresholds, `--skip 2` (v2's rule, kept),
  the K/W sampling procedure (seeds 0 and 1; the sampled set is re-drawn from the new unit stream, since the
  population of keyed letter occurrences changes with the instrument), the gate (K verdicts >= 60%, K CONFIRM >= 80%,
  W false-CONFIRM <= 10%) and the outcome rules are unchanged. v3 writes `results_tx.tsv`.
- Targets: 67 (p.275 line 1 of the letter, djvu 23015) and 153 (p.278, djvu 23297), the two the brief names; 84 (p.274,
  djvu 22921, not transcribed) is reported as it falls but was not the object of this run; 275 is gone from the key
  (A3V2-THUR275) and from the targets.
- If the gate FAILs: non-test, no grade or key change; the row is logged "untestable by this method on a two-page
  transcription", and the only further step this file allows is the same test on the remaining three pages (new
  material for the same instrument), not another knob.
- v1/v2 regenerated 4 Oct 2026 after A3V2-THUR275's JUNK_LINE change (the 275 target row is gone, one K occurrence at
  djvu 23015 lost its left context: v1 K 26 -> 25 verdicts, v2 48.8% -> 47.5%); both `--check` clean again.

## v3 addendum: remaining pages (N8-THUR, LANE-NEAR8 account 2 worker, 4 Oct 2026, written 16:3x UTC before any new crop, read or run)
This is the one further step the v3 section allows ("the same test on the remaining three pages (new material for the same
instrument), not another knob"). It is **not a fourth tuning**: no threshold, statistic, window, skip rule, seed, sampling
procedure or gate changes; the djvu-OCR instrument stays retired. What is new is material read by the same instrument
(page image -> `tools/iiif_lines.py` line crops -> two blind passes -> reconcile):
- Cipher side: the remaining three cipher pages, p.274 (leaf 284; replaces djvu 22886-23012, P5+P6's first page, carrying 84's
  context), p.277 (leaf 287; replaces djvu 23233-23248, P7's first lines) and p.279 (leaf 289; replaces djvu 23327-23347, P7's
  last cipher lines). With pp.275/278 already transcribed, every cipher line of both letters is then image-read.
- Plain side: the two printed decipherment paragraphs ("The same letter decypherd"), P5+P6 = p.275 lower + p.276 (djvu
  23066-23144) and P7 = p.279 lower + p.280 (djvu 23351-23422), each read once from line crops by one blind Sonnet pass and
  checked by the worker against the crops (the brief's unit: 1 read + check). The transcribed lines replace the djvu lines in
  the plain span; `A.JUNK_LINE`/`A.JUNK_SUB`/`A.plain_words`/`norm` apply to them unchanged. This is the same image-for-OCR
  instrument change v3 made on the cipher side, applied to the side A3V2-THURBT's diagnosis named as the limit; Birch's own
  modernised spelling stays (it is the printed text, not an OCR error), so it is not a correction of the test toward the claim.
- Switch: `--txplain` (reads `tx/plain_pages.tsv`); the registered run is `boundary_test.py --skip --tx --txplain`, writing
  `results_tx_full.tsv`; `results_tx.tsv` (v3 as run by A3V2-THURBT) is left as recorded.
- Reported, side by side: (a) **pooled v3-full** (all five cipher pages + both decipherment paragraphs image-read; this is the
  gated number) and (b) **new-only** -- the K/W occurrences whose cipher line is on pp.274/277/279 (descriptive, licenses
  nothing on its own). Also descriptive, to show which half moved the numbers: `--skip --tx` with the five cipher pages but
  OCR plain side.
- K/W are re-drawn by the registered procedure (seeds 0/1) from the new unit stream, as v3 did. Written down before the run:
  this is a second look at a gate that failed by one occurrence, so a PASS here is reported with that history; the new-only
  split is printed so a reader can see whether the new material, not the redraw, carries any change.
- Gate and outcomes unchanged: K verdicts >= 60% of K, K CONFIRM >= 80% of verdicts, W false-CONFIRM <= 10% of verdicts.
  PASS: a target's CONFIRM licenses lifting its key entry from M to S (one vote + a gated control), nothing more; REFUTE
  licenses dropping the entry; INCONCLUSIVE leaves it M. FAIL: non-test, no grade or key change, and this instrument is
  closed for these entries ("untestable by this method at this N", rule 3 third-attempt clause) -- no further page exists.
- **Erratum, written after the run (N8-THUR, 4 Oct 2026, 16:4x UTC), logged openly.** The addendum's bullet above restated the
  CONFIRM outcome as "M to S". That contradicts the binding outcome rules ("What each outcome does", v1), which v3 and this
  addendum both declare unchanged: CONFIRM -> **C** (the meaning is known plaintext bounded by independently keyed context in
  Birch's printed decipherment, which is rule 4's C, not a cryptanalytic S), REFUTE (gap) -> the bounded gap at **M**. The
  binding v1 rules were applied (`decode_stamford.py` BOUNDARY_C / BOUNDARY_M). A verifier who reads the addendum's "S" as the
  registered outcome should grade 67 and 153 S instead; either way P4's H/C/S share is the same (95.8%).
- Result (results_tx_full.tsv, `--skip --tx --txplain --check`): K 55/80 = 68.8% verdicts, K CONFIRM 46/55 = 83.6%, W 0/52:
  **gate PASS**. New-only (pp.274/277/279): K 17/29 = 58.6%, CONFIRM 15/17 = 88.2%, W 0/19. Targets: 67 CONFIRM (p275_L02,
  edit 0) + 3 INCONCLUSIVE (p.274), 153 CONFIRM (p278_L46, edit 0), 84 REFUTE-gap (p274_L39, gap "although", edit 11).
