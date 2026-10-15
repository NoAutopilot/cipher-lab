# PREREG ELEC-R2 (addendum to elecverso/PREREG-ELEC-VERSO.md; worker ELEC-R2, LANE DEFAULT-A4-1236-15, account 4, 15 Oct 2026, 13:3x UTC by date -u)

Written and pushed before the target crops are fetched and before the reader call. One blind second reader (one Sonnet subagent
call), given crop paths only: no sign names, no ELEC-VERSO matches, no Kluckhohn print, no hint which crops are real.

Targets (6, shuffled, labelled T1-T6 by a fixed shuffle, seed 20261015):
- 4 real: the nr. 383 signs oXo (f.166v l.1, c336 native x 650-950 y 180-320), Phi and Hbar (f.166r l.20, c335 native
  x 860-1260 y 2780-2950, cut into two crops), Lfo (f.166v l.12, c336 native x 1850-2150 y 1560-1760); openapi.bnf.fr <= 3 requests.
- 2 decoys, cut from images/canvas109_folio53r.jpg (f.53r, a key not in the panels): the Colonien sign (circle-stroke-circle,
  the nearest look-alike of oXo) and the palatinus sign (same name as Lfo, different shape).
Panels (from disk): A = f.51r lower part (canvas105 x 0-1500 y 1250-2050: the "la Vernade devers Treves" block and its side note);
B = f.51v whole leaf (canvas106; carries the Cleves and Saxe rows that conflicted under ELEC-VERSO's rule).
Reader task: for each target, the single best-matching sign row in A or B (give panel + the name written beside it, as read), or
"none"; a confidence 1-3; then transcribe the side note in A (the block of text to the right of the lower rows), first word first.

Registered rule (decided now):
- PASS (second reader confirms) iff >= 3 of the 4 real targets are assigned to their own name's row in panel A (oXo -> Roy
  catholicque, Phi -> Brandebourg, Hbar -> Treves, Lfo -> Palatin; name reading tolerant of spelling) AND 0 of the 2 decoys are
  assigned to any panel-A row. Decoy assigned to a panel-A row = control FAIL: the reader's matching is not discriminating and the
  real-target result licenses nothing.
- The control varies on the matching axis: a decoy can land on a panel-A row exactly as a real target can.
- Outcome grade stays M whatever the result (two readers, one key image; no second ciphertext occurrence). key.tsv unchanged
  unless decode_key --try at every occurrence accepts (not run in this job: no f.51r rows in key.tsv yet).
- Note's first word: reported as read; "semblable" counted confirmed only if the reader gives it (or "sem-blable" variant) unprompted.
