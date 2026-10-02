# AUDIT: hessen-1824 (HStAM 9 a Nr. 259 f. 249, HCPortal 513)

Verifier: VERIFY-HESSEN-1824 (account 2), 2 Oct 2026, 04:10-04:3x UTC. Brief: `.claude/briefs/runs/2026-10-02-acct3-verify-hessen1824.md`.
Claim under audit: SOLVERDIFF-BOURDEAU (account 2, 2 Oct 2026, `sources/solver-diffs/2026-10-02-bourdeau.tsv`) says this
leaf was read in full by D. Bourdeau on 28 Sept 2026.

## Verdict

| Item | Class | Key | Text |
|---|---|---|---|
| f. 249, cipher body (6 lines, 169 signs) | **N0** -- plaintext and decipherment of this very item already known | `published` (D. Bourdeau, dbourdeau/cyphersolver, 28 Sept 2026, credited; method from the period decipherer's own Anmerkung on the leaf) | `known` |

Earliest citation located: dbourdeau/cyphersolver commit `8729a43d` (28 Sept 2026 20:05 -0500, i.e. 29 Sept 01:05 UTC),
"Site: write-up for Snell to an unidentified correspondent, 20 Feb 1824 (HStAM 9 a Nr. 259 f. 249, HCPortal 513)":
`targets/hesse1824/` (NOTES.md, ct.txt, decrypt.py, reading.txt), `SOLVED_CATALOGUE.md` #126, and
https://dbourdeau.github.io/cyphersolver/hesse1824.html. His NOTES.md dates the reading session 28 Sept 2026.
Read here at HEAD `34e0fc8` (fresh clone, 2 Oct 2026). Bourdeau's code is MIT, his text CC BY 4.0 (CLAUDE.md rule 8).
The period decipherer (anonymous, Kurhessen, 1824) found the method and worked the first word ("schiket") on the leaf; his
full solution is not on the leaf.

**Safe sentence:** "The 1824 Hessian cipher HStAM 9 a Nr. 259 f. 249 (HCPortal 513) was read in full by D. Bourdeau
(cyphersolver, 28 Sept 2026) using the key rule the period decipherer noted on the leaf; we re-applied his key to our own
independent transcription and it reproduces his reading."
**Unsafe sentence:** anything implying this project read, recovered or contributed the reading of this leaf.

## Same item

- Shelfmark HStAM 9 a Nr. 259 f. 249, HCPortal record 513, date 20 Feb 1824: identical in his NOTES.md and ours.
- Image: both fetched `https://api.hcportal.eu/media/1439/17901677521692.jpg` (ours: `images/manifest.json`,
  sha1 f0048eee...; his `record513.json` names the same `original`).
- His ct.txt and our blind transcription agree on 164 of 170 signs (below): the same text.

## Re-derivation on our transcription (`bourdeau_check/check.py`, `--check` exits non-zero if `result.txt` is stale)

Key and method as he states them (re-implemented, not copied): Vigenere table without j, key `bcdefg` written
continuously over every sign, b..g = +2..+7, cipher columns run on past z into the signs 1 2 3 4; his one key-phase
slip (one sign omitted, `zss[p]kkw`) applied; his eleven letter-level copy-slip corrections NOT applied (text as written).

| Run | Plaintext words exact (of 35) | Letters (of 170) |
|---|---|---|
| his ct.txt, as written | 27 | 159 |
| our transcription, as written | 10 | 85 |
| ours, with the one sign we dropped restored (`erylfe` -> `erlylfe`) | 25 | 156 |

Transcription differences (ours vs his), from `result.txt`:
- sign 7 `r` vs `v` (`ufmoqmv`): his `v` gives "schiket"; ours gives "schikep". His reading is right; our 2 Oct gaps pass had
  already flagged `v` from the image.
- `Jmixl` vs `fmixl`: our `J` is outside the table; his `f` gives "diese".
- `erylfe` vs `erlylfe`: we dropped an `l`, which shifts the key phase for the whole rest of the text -- the cause of the
  10/35 vs 25/35 gap.
- `iuw` vs `1uw`: his digit sign `1` (v under e run-on) gives "von"; our `i` does not. Our 2 Oct gaps pass had flagged `1uw`.
- `ktrogg` vs `ktroqq` (the last two signs): both are copy slips in his reading too (he corrects one q -> g); ours gives
  "folged", his "folgen" after correction.
With these restored, the remaining 6 differing words (einen, fragen, wegen, auff, dieses, plans) are exactly his listed
copy-slip words, read identically by both transcriptions. No disagreement with his reading survives on our side.

Grades (rule 4), for the reading as held here: key `published`; tokens H per Bourdeau's own grading (his NOTES.md:
whole text H except "Lisching" C); the 11 slip-corrected signs I.

## Search log (verifier, 2 Oct 2026)

- dbourdeau/cyphersolver, fresh clone HEAD `34e0fc8`, history deepened to 25 Sept 2026: `targets/hesse1824/` read in full;
  first commit touching the target or catalogue row #126 is `8729a43d` (28 Sept 2026). His own prior-art step names our
  repository (notes folder, no reading) and finds "nothing in print".
- HCPortal record 513 (his `record513.json`, our intake 26 Sept): `solution: "Not solved"`, `note: null` -- the record
  does not carry the reading.
- Web search (one query, 2 Oct 2026): "Lisching" Snell Follen 1824 Chiffre Wetzlar -- Deutsche Biographie (Ludwig Snell),
  Wikisource ADB (Wilhelm Snell), HLS; none prints this text or a decipherment.
- Not searched (not needed for N0, which rests on the located decipherment): canonical editions of the Mainz Central
  Commission files, JSTOR. An earlier print would not change the class.

## Postmortem (one line)

Our ladder (bHCP periodic_vigenere at P6/7 on 26 letters with the digit signs excluded, masc, homophonic, running_key,
crib-drag, periodic_masc) never reached the reading because no step applied the leaf's own Anmerkung -- the period
decipherer's stated key rule and worked first word were the crib, and the design (25-letter table, columns running on
into digit signs, one dropped sign) broke every generic family's assumptions; the 2 Oct finish-or-blocker pass named this
as the highest-value next step, two days after Bourdeau had already read it. Lesson: transcribe and apply a leaf's own
decipherer's note before any blind family.

Over-claims corrected: none found (our files never claimed a reading). NEAR.md and status.json `near` rows retired, NOTES.md
status set to `found-solved` in this commit. No SECOND-OPINIONS-QUEUE row (N0).
