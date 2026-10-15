# PREREG ELEC-VERSO (worker ELEC-VERSO, LANE DEFAULT-A4-1236-15, account 4, 15 Oct 2026, 13:1x UTC by date -u)

Written and pushed before any image is fetched or compared. No numeric score is computed in this job; the rules below fix what
counts as a finding.

Step (1) verso census, fr.5761 (btv1b52510561g), openapi.bnf.fr IIIF v3 at full/1000,:
- Units: the versos of ff.160-165 not yet read: f.160v c324, f.161v c326, f.162v c328, f.163v c330. (f.164v c332 was read by ELEC-383
  and f.165v c334 by ELEC-KLU, both at 1000 px, names in letters; they are not re-fetched.)
- Per canvas the reader records: heading/dateline if any, names written in letters, and every isolated non-letter sign standing in a
  word slot (not an ordinary abbreviation mark: tilde, p-bar, 9-like con/us, 7-like par/et). A canvas with such a sign gets one native
  crop (<= 1 further request) before it is logged.
- A logged sign is a lead, grade M; it is paired with a printed name only if Kluckhohn's text for that letter is identified, and no
  pairing is graded above M in this job.

Step (2) image-to-image, the four nr. 383 signs (oXo, Phi, Hbar, Lfo) against the fr.5761 f.51r-53r keys on disk
(images/canvas105_folio51r.jpg ... canvas109_folio53r.jpg, 1500 px): exactly ELEC-POOL's five-feature rule (stroke count, closed loops,
crossings, dominant orientation, detached marks; "match" = 5/5, "partial" = 4/5, else no match), features of the target sign recorded
before the key rows are viewed. Rows compared: each leaf's rows for roy catholicque / Catholicque(r), Brandebourg, Treves, Palatin, and every
other name row on the leaf as distractors. A target matching a row other than its printed name's is a conflict. Outcome M whatever it says;
no key.tsv edit, no grade change in elecpair383/. Target crops re-fetched from c335/c336 (<= 2 requests, scratch only).

Step (3) fr.3897 Joachim items 36-38: only if >= 30% of cap is left after (1)-(2); census rule as step (1).
