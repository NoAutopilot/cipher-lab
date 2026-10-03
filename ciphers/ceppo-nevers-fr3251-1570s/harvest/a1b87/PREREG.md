# A1B-CEPPO-87 pre-registration (3 Oct 2026, written 18:05 UTC, pushed before any blind read)

Brief `.claude/briefs/runs/2026-10-03-acct1-a1b-ceppo-87.md`. Two units, both judged by rules fixed here.

## Readers
Two independent blind Sonnet subagent passes (A, B), one call each, tiles only (no page, no sign sheet values, no
candidate value, no prior read). Each pass gets every tile of both units in one batch. Questions are shape questions
(unit 1) and "what letter is written above sign k" (unit 2). This worker cut the tiles and looked at them only to
check that the target sign is inside the tile; it is the reconciler and does not cast a third vote.

## Unit 1: f.87 passC L04.39 (S65 plain 8 in passC, H; blind reconciler D read S80 "8 with bar through waist")
Located by passC neighbours L04.37-L04.45 (S17 S31 [S65] S49 S88 S76 S52 S74 S75 = "...ℒ 8 ∴ ≠ ꝯij 3 6 +" at the right end
of cipher line 4). Rule R-8 from `../../../birago-fr3252-1571-72/harvest/witness_pairs/PREREG.md` (e1760f2e): a bar through the
waist running out past both sides -> S80 (a); no bar -> S65 (et).
- Both readers see the bar -> proposed S80 (a). It becomes S only if gates (ii) key control at f.87's two-reader error 0.28
  ranks 1/201 with power >= 18/20 on 3 seeds and (iii) the judge does not get worse (VERIFY-CEPPO-WP's gate (iii)); else
  recorded at M with the shape reading noted.
- Both readers see no bar -> S65 stays; D's read is outvoted, recorded.
- Split or "cannot tell" -> S65 stays, token downgraded H -> M in the reading grades (contested), UNDECIDED logged.

## Unit 2: glossed S31 / S76 on fr.3252 f.36r / f.37r (never f.117r / f.144r / f.168)
Located by script from the committed transcriptions (birago `harvest/f36r/ciphertext_f36_v2.tsv`, `harvest/f36/recon.tsv`):
S31 at r36n_L11 pos 3 and r36n_L13 pos 30 (f.36r); S76 at r37_L01 pos 14 (f.37r; pass B read S58?). Tiles of ~5-7 signs
with the gloss band above. Each reader lists the signs left to right with a short shape description and the letter
written above each (or ? / none). The target sign is identified by its neighbours in the transcription.
- A gloss counts only if both readers give the same letter above the identified sign.
- What it changes on f.87: a gloss confirming the printed value (S31 m, S76 z) adds a witness count to that sign's value
  but gives NO shape rule separating S31/S32/S76, so f.87's S31/S32/S76 tokens (e.g. L04.38, L04.42) stay at their
  current grades. A shape rule needs >= 2 agreeing glossed instances per member with a deciding feature both readers
  name; this job cannot reach that for S32 (no f.36r/f.37r S32 instance is targeted), so no f.87 regrade from unit 2 is
  possible by construction unless a gloss CONTRADICTS the printed value. A contradiction is logged as a data conflict
  (rule 4) in HYPOTHESES.md with the witness, and f.87 tokens of that sign are set to M, not re-valued.
- A gloss over an upright/slanted hash at a line end seen incidentally is recorded, not acted on.
