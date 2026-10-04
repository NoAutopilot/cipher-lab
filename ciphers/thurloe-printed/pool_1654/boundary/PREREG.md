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
