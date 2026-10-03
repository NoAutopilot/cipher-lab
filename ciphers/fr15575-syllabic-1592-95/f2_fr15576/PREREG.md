# NV05D pre-registration, fr.15576 f.2 (canvas f8 of btv1b9063777v), 3 Oct 2026 15:3x UTC

Committed before any transcription pass. Disclosure: before writing this file the worker looked at one 1400 px overview
of canvas f8 and one native test crop (x 5800-7100, y 1820-2150) to place the crops. What that showed changes the brief's
premise and is stated here before any test is scored:
- the body groups are written as spaced 3-digit numbers (crop: "201 775 114 553 246 [sign] 200 482 199" /
  "661 588 198 733 y 575 163 739 246 20[.]"), not as the spaced 2-digit codes (10-99) of the no.54 syllabary that
  NV05C's control letter fr.3641 f.111r uses;
- the leaf carries a period interlined decipherment in a lighter ink above the cipher lines (crop: "dixe a V.M. en una
  ... de" over line 1; "se quedaua apercibido" over line 2), which NV05B's overview description did not record.

Premise test P1 (gate for the brief's decode step): tokenise as written (a spaced group is one token). Share K of
numeric tokens whose value is a coded row of key_no54.tsv (codes 10-99). If K < 0.50 on the lines read, the no.54
syllabary decode is not applicable to this leaf as written: no decode.json, no judge run and no shuffled-key or
shuffled-order control are run (a decode that is nearly all U cannot be judged, and its controls could not differ from
it -- rule 3, the bCAS/AX-5799 non-test shape). Alternative splittings of a 3-digit group into key codes (2+1, 1+2)
are not tried: nothing in the key sheet or the control letter supports them, and choosing one after seeing the text
would be a rule picked from the target.
If K >= 0.50: decode with key_no54.tsv as the brief states (syllable codes S, header letter signs M, others U), judge
es17a (1590-1625 Spanish state prose, built 3 Oct 2026 -- the nearest era match on disk; es17 is fiction and es17c is
1643-47), value-shuffled key control (200 draws, seed 1) and the shuffled-order target decode through the same judge.

Premise test P2 (one look, no decoding): whether the no.54 key sheet (fr.3995 f.96v-97r, canvas f188 of
btv1b525085665) carries 3-digit codes in its nomenclator in the range the target uses (about 100-800). Reported as
seen / not seen; it does not license a decode in this job either way, since the nomenclator is not transcribed.

Reading scope for P1: the first four body lines (one crop batch, two blind passes + reconciliation per TRANSCRIPTION.md).
