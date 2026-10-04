# PREREG N8-GRA2: fr.3040 f.18r no.6 cipher block vs Le Grand III p.454-455 as known plaintext (4 Oct 2026, written 16:4x UTC, before any read or score)

Brief: `.claude/briefs/runs/2026-10-04-ytbiz-near8-wave2.md`, job N8-GRA2 (account 2, for LANE-NEAR8). Pushed before any
transcription pass and before the statistic is computed on the target.

## Pair (established before this file, by image and OCR only)
- Cipher: BnF fr.3040 no.6, Gramont to the grand maître, "A Boulongne, le XXVIIIme jour de mars" (finding aid cc49499h,
  d0e150). Gallica `ark:/12148/btv1b9059870w` (every canvas label 'NP'): canvas 32 = f.18r (folio number "18" visible),
  canvas 33 = f.18v, canvas 34 = f.19r (folio "19", end of the letter in clear, signed "G de Gramont E. de Tarbe").
  The letter is mixed: clear passages and cipher blocks, with marginal notes beside the cipher blocks.
- Print: Le Grand, *Histoire du divorce* III, *Preuves* pp.454-457 (MDZ bsb10280117 scans 460-463), "Lettre de Mr. de
  Gramont Evesque de Tarbe à Mr. de Montmorency. De Boulongne le 23. Mars", subscribed "A Boulongne ce 28. jour de Mars";
  Béthune vol. 8565. The clear passages of f.18r-19r read, by eye at sheet scale, as the same words as the print
  ("vous m'escripvistes a vostre partement de la court que je feisse ce que me seroit possible pour entretenir Mons. de
  Rochefort", "Monseigneur je presuppose que messeigneurs seront en France", the Corfou postscript). The print runs on
  continuously where the leaf has cipher, so it gives the plaintext of the cipher blocks.
- Le Grand III **p.399** (the page the Verdict named) is *not* this letter: it is inside "Dechiffrement des Lettres de
  Monsieur de Tarbe" (pp.394-40x, Béthune vol. 866 pag. 68, to the king, "Sire", Bologna, after the emperor's departure).

## Scope (unit-priced, Usage 6)
Only the first 10 cipher lines of the f.18r block (the block that starts after the clear "& a la replique que ledict de
Rochefort pensa faire"). Units: 2 blind Sonnet passes on line crops + 1 reconciliation = 3 units. The rest of f.18r-19r is
not read in this job.

## Statistic (registered)
`agree` = share of keyed cipher tokens (tokens whose code has a letter value in key.tsv at this commit, NULL and '?'
excluded) whose value matches the print letters they are aligned to.
- Decode: each reconciled token -> key.tsv value (multi-letter values such as SS, ET, LL expand); unkeyed and uncertain
  tokens become a one-character wildcard that never scores.
- Print: Le Grand p.454 from "il luy dit qu'il laissast la parole aux autres" through the end of p.455, as OCR'd by MDZ,
  hand-checked only for OCR slips in that span.
- Normalisation, both sides identical (rule 3 PX-BRODEC): upper case; long s -> S; accents stripped; J, Y -> I; U -> V;
  W -> VV; everything not A-Z dropped.
- Alignment: letter-level Needleman-Wunsch, match +2, mismatch -1, gap -2, free end gaps on the print side (the block's end
  point in the print is not fixed in advance). A token agrees only if all its letters are aligned to equal letters.

## Nulls and control (each can differ from the target on this statistic)
- N1 shuffled plaintext: the same decode aligned to the print span with its letters shuffled, 200 shuffles, p99.
- N2 shuffled key: key.tsv letter values permuted among the keyed codes, the same tokens re-decoded and aligned to the true
  print, 200 permutations, p99.
- Positive control P (planted at the measured reader error): the print span enciphered with key.tsv (each letter -> a
  random keyed code with that value; letters with no code skipped), then 13% of tokens replaced by a random other code
  (err_2reader on f.30 = 1 - 0.873 raw agreement, NOTES "agreement gives 1735/1987"), same length as the reconciled target,
  20 seeds, mean. Control gate: mean(P) >= max(N1 p99, N2 p99) + 0.15 on the control's own nulls. If the control misses
  its gate, stop: non-test, no target verdict.

## Gate (registered)
PASS iff the control passed AND target `agree` >= 0.50 AND target `agree` > max(N1 p99, N2 p99).
FAIL iff the control passed and either target condition misses. A FAIL is conditional on the transcription (rule 2) and
is not a key-family negative on its own.

## What a PASS licenses
Open codes (key.tsv value '?' or not in key.tsv, NEW: shapes) that occur in the aligned span: a code aligned to the same
print letter in >= 2 occurrences gets a key.tsv row at grade C, source "fr.3040 f.18r vs Le Grand III p.454 (N8-GRA2)";
a code seen once is listed in NOTES, not keyed. Keyed codes whose aligned letter disagrees in >= 2 occurrences are listed
as conflicts (rule 4), not changed. Then `decode.py --check`; VERIFIER WANTED flagged in ROOM.md.
