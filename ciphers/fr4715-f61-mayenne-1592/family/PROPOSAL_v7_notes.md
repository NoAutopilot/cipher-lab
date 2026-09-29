# Proposal: key-note and row changes for a v7 build (CAMPAIGN.md H275, runner 10, 29 Sept 2026)

Written by campaign runner session_0148wt8Aokh6aZEdJsXzYiZX for the build worker the orchestrator queues (F61-FAMILY-11 or later). Nothing here is
applied: `family/key_period_v6.tsv` is unchanged. Each line is tagged **endorsed** (a verifier's AUDIT.md verdict) or **pending** (a runner result
still to be audited, VERIFY-F61-V9). A build worker applies only the endorsed lines unless the orchestrator's brief says otherwise; the pending lines
are listed so the brief can name them.

| # | row(s) in key_period_v6.tsv | change | source | status |
|---|---|---|---|---|
| 1 | ZHOOK i 28 / x 3 (CELL i/x, f.176r) | note: replace "no glyph link" with "the 2# sign = H24 cell, glyph link VERIFY-F61-V8 (setF/setG 10/10 vs 0/27 distractors); grade S on f.61" -- value unchanged | AUDIT.md VERIFY-F61-V8 verdict (1) | **endorsed** (V8) |
| 2 | 4PI rows (f.101r d 5 / n 3 / q 2 / a 1 / c m p s 1; f.188r d 9 / a 5 / ...) | split by sign: keep 4PI = the 4-head hash, CELL d/q pooled (f.101r, f.108r overlay d 4 / p 1, f.188r's d/q rows); move f.188r's a/n 4PI rows (a 5, n 1 and the e/h/r strays) to a separate row `4RTAIL` (a 4 with an r-tail, V8's third form; V8 suggests they may be C43 miscoded -- one test before pooling) | V8 verdict (2), "finding for the key" | **endorsed** (the split); the 4RTAIL destination is V8's suggestion, pending a test |
| 3 | new class `4OVERPI` (f.61 only: L01 12, L11 9) | a separate row, never pooled with 4PI: L11 9 = a/n at grade M from Tomokiyo's S5 letter alone (V8); L01 12 unread | V8 verdict (2) | **endorsed** (V8) |
| 3b | `4OVERPI` L11 9 | alternative witness: the lexicon reads S5 only as "me l'entendoit", i.e. L11 9 = d (grade I), against the published n (H268/H269; HYPOTHESES.md row "campaign H268") | runner 10 | **pending** (V9 decides between the witnesses; a build worker records both letters in the note, applies neither as a cell without the verdict) |
| 4 | C6 e 2 (f.101r) / e 1 (f.188r) | add an F61READ row `C6 - 0 fr.4715 f.61r` (unread on f.61): Tomokiyo's dash at all 5 in-span C6, no glyph link (H237), the pooled cell keeps its leaves | H261; HYPOTHESES.md row "campaign H261" | **pending** (V9) |
| 5 | CA (no row; a null in the skeleton) | note in KEY.md's f.61 section: "CA = a null drawn as the letter a (letterform two blind sorts 10/10, cipher hand H63, no letter in the markup H259)" -- no row, no count change | H256/H259/H260; family/f61_null_band.tsv | **pending** (V9 wording) |
| 6 | HASHLOOP (UNREAD) | unchanged; the one route to a value is a person's read of f.106r's gloss (H243 pack, family/images/person_pack_106r) | H241/H243 | -- |
| 7 | 4STEM F61READ a/n (L11) | unchanged; note that Tomokiyo's own letter there is a dash (H261) and the lexicon witness gives n (H268), inside the cell | H261/H268 | **pending** (note only) |
| 8 | CH e 3 (f.101r) / m 3 (f.188r) (pooled e/m; two leaves' letters, HYPOTHESES.md H289) | add an F61READ row `CH - 0 fr.4715 f.61r` (unread or null on f.61, beside the C6 one, item 4): Tomokiyo's dash at its one token (L05 2, H281) in "les choses sont a [LOOPSTEM1] [CH] trop avancees", complete French without it (Correction, H295); letterform of the clear h in one blind sort, 1/1 with the 3 text h's, PHI/C43 0/4, n = 1 flagged (H298); a blind positional reader listed it as the clear letter h (H297); the pooled cell keeps its leaves. Meter if applied: two-way 59 -> 58, unread-or-null 26 -> 27 | H298; family/f61_null_band.tsv note row; family/f61_nulls_as_letters.tsv | **pending** (not in V9's brief; for the next verifier; n = 1) |

Reproduction after any build: `python3 family/build_key_v6.py --check` must still pass for v6, and the v7 script must reproduce f.61 53/55 (published
markup) and f.108r 74/84 with 2000 permuted keys, as v6 does (`family/build_key_v6_result.txt`); with S5 as the entendoit witness, H269's numbers
(54/56 under d or under the pooled cell) are the reference. Grades: every f.61 letter above stays S or M except the lexicon lead, which is I.

## Status of the items (H301, runner 11 session_01RNzUvRTqBTAw7BukhKyKBU, 29 Sept 2026, 11:2x UTC)

Items 1-3 are in key v7 (F61-FAMILY-11, 10:17 UTC: ZHOOK note, the 4PI d/q split with 4PIR held, 4PIPI L11 9 a/n grade M and L01 12 unread; KEY.md
"key v7"). Item 5 (CA) was endorsed in part by VERIFY-F61-V9 and written by F61-FAMILY-12 (11:15 UTC) as a KEY.md section and the null-band class
note, no key row. Item 4 (C6): V9 endorsed the conflict with a sharper statement (C6 = e excluded on f.61 at 4 of 5 in-span words); F61-FAMILY-12
carried that into HYPOTHESES.md's row, and no F61READ key row was written (the f.61 decode file has no class-note column; the null band is the one
class-note file). Item 3b (L11 9 = d) and item 7 remain pending; item 8 added by H301, pending.
