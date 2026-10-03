# AUDIT: malsburg-hessen-1636 (HStAM 4 h Nr. 1411 ff. 3-33, HCPortal 496, 497, 502-509)

Verifier: VERIFY-MALSBURG-BOURDEAU (spawned by LANE-A2PUSH, account 2, for the account-3 orchestrator), 3 Oct 2026,
01:59-02:3x UTC. Brief: `.claude/briefs/runs/2026-10-03-acct3-verify-malsburg-bourdeau.md`.
Claim under audit: SOLVERDIFF-BOURDEAU (`sources/solver-diffs/2026-10-03-bourdeau.tsv` row 7) says D. Bourdeau read
the same ten HCPortal records in part on 28 Sept 2026 (numerical key from the ciphertext alone, 95.9% of 9,736 cipher
tokens), and that NEAR.md's description of our own work ("ff.3 and 12 read twice blind, f.3 89.7%, f.12 96.2%") might
be a competing reading.

## What "our reading" is (correction first)

There is no reading of ours to compare. The NEAR.md figures 89.7% / 96.2% are **pass-to-pass transcription agreement**
of two blind sign passes (bMAL3, `tools/reconcile_passes.py`, 26 Sept 2026), not plaintext. Our own NOTES.md "Remaining
gaps" (1 Oct 2026) states it: "Read so far: 0 cipher signs read as plaintext ... no key and no family PASS". Every
family run on the pool (masc, homophonic, block homophonic w3-5, letter+syllable) is logged in HYPOTHESES.md as a FAIL or
a CONTROL BELOW GATE. What this project holds is a transcription: 5,757 signs, of which ff.3/12/23 (1,828 signs) are
reconciled in `pool/pooled.tsv`.

## Verdict

| Item | Class | Key | Text |
|---|---|---|---|
| Numerical cipher of ff. 3-33 (all ten records), ours = transcription only, no reading | **N0** -- plaintext and decipherment of this very item already known | `published` (D. Bourdeau, dbourdeau/cyphersolver `targets/malsburg1637`, 28 Sept 2026, credited) | `known` (in part: 95.9% of his 9,736 cipher tokens; codes mostly open) |
| f. 12 ten-line alphabetic block (repeating shifts 4,5,3,6,2 over a 24-letter alphabet) | **N0** for this project -- we never transcribed or read it | `published` (Larry Beck with ChatGPT, integrated into Bourdeau's repository 2 Oct 2026, `targets/malsburg1637/alphabetic/`) | `known` (substantial, with stated uncertainties) |

Status: **found-solved**. His reading covers everything ours covers (ours covers no plaintext at all), and more: all ten
records including leaves we never transcribed (ff.14, 18, 25, 29, 31 and the first blocks of ff.3 and 12).

Dates and evidence. Our intake (26 Sept 2026, NOTES.md line 2) read his CATALOGUE.md #338 at HEAD `fc0c9e86` as "no
reading found" -- true on that date. His key file header reads "annealer result of 28 Sept ... polished over all pages,
28 Sept"; the solver diff dates the posting to commit `46f0a711`, 28 Sept 2026, and PR 17 / the alphabetic block to
2 Oct 2026. Read here at HEAD `a4292cb1` (fresh shallow sparse clone, 3 Oct 2026, committed 2 Oct 2026 20:26 -0500).
One GitHub API call to list the path's commit history returned an error object (not retried); the 28 Sept date rests
on his own key.txt header and the 3 Oct solver-diff row, not on a commit listing read here. Our transcription work
(26 Sept) predates his posting but contains no reading, so nothing of ours predates and differs materially. Bourdeau's
code is MIT, his text CC BY 4.0 (CLAUDE.md rule 8); nothing of his is copied into this folder, his files are read from
a scratch clone by `bourdeau_align/align.py`.

**Safe sentence:** "Otto von der Malsburg's 1637 cipher letters (HStAM 4 h Nr. 1411, HCPortal 496-509) were read in
part by D. Bourdeau (cyphersolver, 28 Sept 2026; 95.9% of the numerical cipher, codes mostly open), with the f. 12
alphabetic block added by Larry Beck with ChatGPT (2 Oct 2026). Our independent blind transcription of ff. 3, 12 and 23
matches his on 86-96% of tokens and reads as German under his key."
**Unsafe sentence:** anything implying this project read, recovered, or contributed any part of the reading, or that
our ff. 3/12 figures (89.7%, 96.2%) were reading rates.

## Same item

- Shelfmark HStAM 4 h Nr. 1411, ff. 3-33; HCPortal ids 496, 497, 502-509: identical in his NOTES.md and ours.
- His `fNNN.txt` files are named by HCPortal digital image number, as ours (`hstam_4_h_1411_00NN`) are.

## Token alignment (`bourdeau_align/align.py`, outputs `align_summary.tsv`, `disagreements_ff3_12.tsv`,
`decode_ours_under_his_key.txt`)

Our reconciled pool (`pool/pooled.tsv`, cipher signs only) against his transcription of the same image, `difflib`
alignment after notation normalisation (dot/doubt/underline marks stripped; our `z1` = his `Z`):

| Image | Our tokens | His tokens on the image | His span aligned to ours | Matched | Share of ours | Replaced | His only | Ours only |
|---|---|---|---|---|---|---|---|---|
| 0003 (f.3 postscript) | 191 | 455 | 193 | 179 | 0.937 | 13 | 1 | 0 |
| 0012 (f.12 L44-L49) | 159 | 712 | 159 | 153 | 0.962 | 6 | 0 | 0 |
| 0023 (f.23, held at M 0.144) | 1,439 | 1,443 | 1,443 | 1,235 | 0.858 | 199 | 16 | 10 |

Our transcription was made blind of his (26 Sept, two days before his posting). Decoded under his `key.txt` and
`codes.txt`, ours reads as German on all three images, e.g. f.3 L26 "angebewedenderfridenutractaten", f.12 L48
"CH[137]apartzu[Hamburg]oderlubecktractenen" -- an independent confirmation that his key reads this ciphertext.

The 19 disagreement sites on our two H-graded leaves (ff.3, 12; `disagreements_ff3_12.tsv`): 4 are notation only (his
Z/j where we wrote 7; his G where we wrote Y, both = ei); at about 13 his token gives the German word and ours does not
(f.3 "bewegen" 29 vs our 27, "fridenstractaten" 68 vs 58, "tractiren" 94 30 vs our M-graded blot token 930, f.12
"geschriben" 10 18 vs 20 28, "nunmer" 65 vs 85); 2 are undecided. Our transcription therefore offers no correction to
his on these leaves; on f.23 (our leaf held at M) the 199 replacements are dominated by our own known reader error.

## Where each covers what the other lacks

- His, not ours: the reading itself; the first blocks of ff.3 and 12 (our passes covered only the postscripts and
  f.12 L44-L49); ff.4, 13, 14, 15, 17, 18, 24, 25, 29-33 transcribed and read; the f.12 alphabetic block; five codes
  inferred (128 Cöln, 130 Hamburg, 188 die Staaten, 253 Regiment, 273 Compagnien, grade I in his own file).
- Ours, not his: nothing that fills a gap he leaves open. His open items are the code referents (about 40 of about 45
  three-digit codes, and the signs V, K, Q, f, m, 4#, +, XX) and the f.12 block's 43/45/LL labels. Our record-509 code
  cribs (`cribs.tsv`, 222 rows) tied their shuffle control (class consistency 0.812 vs shuffle p95 0.836, HYPOTHESES.md)
  and narrowed no code, so they carry no evidence to offer. No outreach line is drafted (brief item 4 applies only if
  our work fills something his leaves open; it does not).

## Search log (this verifier)

- dbourdeau/cyphersolver `targets/malsburg1637/` read: NOTES.md (head 150 lines), key.txt, codes.txt, dec.py,
  f003.txt, f012.txt, f023.txt headers; 3 Oct 2026. Host github.com: 1 clone; api.github.com: 1 request (error object).
- Our folder: NOTES.md (status, intake, bMAL2/bMAL3, NEXT-MAL, Remaining gaps, Escalation), pool/pooled.tsv,
  ciphertext.txt, HYPOTHESES.md by reference.
- No further print or scholarship search: an N0 needs only the prior decipherment of this very item, which is in hand.

## Postmortem

NEAR.md row 22 and the brief described our ff.3/12 pass agreement (89.7%, 96.2%) as if it were a reading ("Our own
reading ... f.3 89.7%, f.12 96.2%"). It was never a reading; corrected here and in NEAR.md's closed row. The intake's
"no reading found" for Bourdeau was correct on 26 Sept and went stale on 28 Sept; the 2 Oct solver diff missed the
target and the 3 Oct one caught it (the solver-diff row says so). The target leaves the board as found-solved; the code
referents stay open in his reading, which is a matter for his repository, not a gap held open here.
