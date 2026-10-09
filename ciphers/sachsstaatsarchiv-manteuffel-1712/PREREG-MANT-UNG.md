# PREREG-MANT-UNG (9 Oct 2026, 16:5x UTC by date -u; written before any transcription pass was run and before any score; LANE FAMILY-A2j account 2)

Leaves: HStA Dresden 10026 Loc. 694/08 frames 0290 (fullsize 0290.jpg, 4346x3860, sha256 prefix de41885c327bbdd8 = inv08f.tsv; film card
"Aufnahme Einheit 0291"; right page, stamp 224, 'ce 17 Sept. 1712') and 0383 (0383.jpg, 4345x3860, sha256 prefix 75f47e96783e0745 = inv08f.tsv;
card 0384; two pages, stamp 307 on the right page). One GET each, 9 Oct 2026 16:4x UTC. Key: key.tsv at origin/main as of this commit, unchanged.

## Premise (found before this file, at preview scale)
- 0290 is NOT unglossed (inv08f said "no clear gloss words"): small interlinear notes stand over most code groups ('mant' over 160, a phrase
  over the line-2/3 runs, a name over the line-4 single code, 'flem' over 155, 'Roy de Prusse' over 257, 'le Roy' over 150, 'Manteuffel'
  over 160). So 0290 is a glossed key test (MANT-0136B protocol), not a reading of unglossed material. Codes above 401 stand under the notes.
- 0383 is unglossed and continues the P.S. of 0382 (stamp 306): Acta Borussica, Behoerdenorganisation I (1894), IA diebehrdenorgan01posngoog
  _djvu.txt, pp.257-258 (Nr. 72), prints Manteuffel's report of 4 Oct 1712 ending "... Grumbkow est si bien en cour, grace a son patron Ilgen,
  qu a moins que Kameke et d'autres n'y mettent empeche, il sera dans peu tres puissant. Kameke se souvint avant hier que je lui avais predit
  ... par complaisance pour Ilgen, avec lequel il aurait a souhaiter de vivre en amitie parceque c'est un homme dont la cour ne saurait
  absolument se passer ...." and then (no new date) "Kameke ne se sentant pas encore assez fort pour hazarder une bataille decisive contre
  Ilgen, cherche sous main a se rapatrier avec lui ... tous les ministres aux cours etrangeres lui envoient les memes relations qu'a Ilgen, ce
  qu'il m'a dit dernierement en grande confidence ....": the clear text of 0383's left lines 5-12 and right lines 15-27 at preview scale, with
  the code names in clear. So 0383's text is in print (known text); its code tokens are mostly single-code name initials.
- No BO I print found for a Manteuffel report of 17 Sept 1712 (OCR-tolerant grep of 'September 1712'/'17. Sept'): 0290 not found in BO I by
  this method. Berner 1901 djvu: HTTP 500 (stopped, unchecked).

## Inputs
- Codes: two blind Sonnet passes per leaf over the committed line crops (f0290_08/crops: 13 two-line bands of the right page; f0383_08/crops:
  14 bands left page + 14 right page, both pages in one call per pass to stay within the cap -- disclosed deviation from "one page per call");
  pass B in reverse order. Each 0290 pass ALSO reads the interlinear notes (V-BRANDT: gloss read blind, two passes, scored per pass); passes
  see no key value. Worker reconciliation of code digits from the image where the passes disagree -> ciphertext.tsv, before any span is
  attached and any score is computed. Disclosure: this worker has seen key.tsv, the notes at preview scale and the BO I print; digits are
  settled from the image only; doubtful ones low. Gloss text is NEVER settled by this worker: each blind pass's gloss is scored as written.
- 0290 spans: one row per gloss note, assigned by position to the code sub-run under it, per pass (gloss_spans_A.tsv, gloss_spans_B.tsv).
- 0383 print spans (gate c): one row per code sub-run that the BO I pp.257-258 quotation covers, the printed word at that place as text
  (expected from the print before any pass: 7.60 Grumbkow, 9 Ilgen, 11 Kameke, 11 Kameke, 7.60 Grumbkow, 9 Ilgen on the left page;
  11 Kameke, the code before 'cher-che' Ilgen, the code after "qu'a" Ilgen on the right page). Elided runs ('....') are not spans.

## Statistics and gates (fixed now)
- Gate (a) 0290: f0136_08/gloss_gate.py statistic unchanged (copied to f0290_08/gloss_gate.py, seed 290, control: key values permuted over
  codes, 1000 draws), scored per blind pass; PASS if S > p99 AND S >= 0.5 x keyed tokens in the spans; < 10 keyed tokens = too short.
  Deciding row: the LOWER of the two passes. Whole-word name codes (150, 155, 160, 257) match only when the note spells the key value (a
  lower bound, as 0474/0136B). Codes outside key.tsv score as misses; a code > 230 under a note is listed in f0290_08/candidates.tsv as a
  witness (held, never entered in key.tsv; C at most if the deciding row PASSes).
- Gate (b) 0290 and 0383: exactly f0176_08/judge_gate.py (fr18 4-gram, letter values permuted, 1000 keys, power from the 0085 r9+r10 and 0136
  windows, TEST only if power >= 0.80, else too-short), seeds 290 and 383, on code tokens NOT covered by a gloss span (0290) / all code
  tokens (0383). Name-abbreviation rule as PREREG-MANT-0176.
- Gate (c) 0383: gloss_gate.py --print statistic on print_spans.tsv, seed 383; same PASS rule. Caveat: the 1894 editor may have read a
  Dresden decipherment, so (c) is a known-answer row, not independent corroboration.
- Grades (rule 4): a 0290 code matched under a PASSing deciding row = C; a 0383 code matched under a PASSing (c) = C; else S only under a
  PASSing (b) TEST; otherwise M. Unkeyed = U.
