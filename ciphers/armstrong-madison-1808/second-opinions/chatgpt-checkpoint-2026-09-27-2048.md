# Armstrong continuation: audit of Annet rule and sign readings

Status: open. No defensible Armstrong plaintext or target key assignment.
Recorded UTC: 2026-09-27 20:48:42.
Batch: completed source audit. Running jobs: none. Active lease: none.

## Parent, objective, and retained work

Parent: [PR #46](https://github.com/NoAutopilot/cipher-lab/pull/46), immutable head `ca2607b130bcb4cf65c3c5b29b9c68a501c83ef8`, path `ciphers/armstrong-madison-1808/checkpoints/20260927T202603Z.md`.
Follow its parent [#45](https://github.com/NoAutopilot/cipher-lab/pull/45), head `533dd43553c0befac9276bc29921a4f1e1ccc536`, then bootstrap [#44](https://github.com/NoAutopilot/cipher-lab/pull/44), head `58df6cf8c070c780df86faeec30900729f9229ba`.

Read the narrative chain before this bounded audit. The all-state REST PR collection was checked at bootstrap and before this checkpoint; #46 remained the latest preceding checkpoint and had no active lease. Closed without merging remains the expected landing workflow. No searches or saved winners were rerun. The 144 decimal-order results in #44 and 24 mixed-piece winners in #46 remain intact with their original limitations.

Objective: audit the exercise-2 primitive recognition against the source alphabet and rules before target transfer. This is a further answer-aware inspection by one agent, not an independent observer or blind recognition trial.

## Completed source corrections

Source: [Annet scan catalogued as 1770](https://www.dropbox.com/scl/fi/e0nih2zcsrhl5tfq2d8wy/Annets-Shorthand-1770.pdf?dl=1&rlkey=rn4g1tw3iwvnkv0wasqory24m), SHA-256 `243dfc316e7b7d2fb7cd282dcb503ce50aac3d44334bf93fa03e419bb017df3c`. Downloaded successfully and hash matched. [Stenophile catalogue](https://www.stenophile.com/historical) still supplies this link. The exact imprint date remains qualified as in #45; the hash identifies the witness.

Inspected PDF pp3, 10-17 and enlarged relevant crops. PDF page numbers are 1-based; rectangles below and in the capsule use PDF points from the upper-left corner.

| Prior entry | Direct source observation | Consequence |
|---|---|---|
| #45 rule table and #46 code: comma for or/ed | PDF p14, printed p10, rule 8 says the endings **ing or ed** can be replaced by a small comma when they take the outline too low | This does not license whole-word OR. Correct the suffix metadata to ing/ed and withdraw the unsupported OR candidate |
| #46 `THEN_THERE: [then, there]` and #45 item-20 label | PDF p3 labels the hooked sign **their, there** | Correct the label to THEIR_THERE. Item-20 THERE remains among the supported sign values; THEN is not supplied by this entry |
| Exercise 2 position 15 labelled COMMA | Enlarged p17 outline is a descending diagonal stroke, resembling the marks aligned to AND at positions 6 and 9 | Preserve as DIAGONAL_UNRESOLVED. Do not relabel it as a proven whole-word OR sign |

The alphabet's diagonal a entry on p3 carries AN; the p11 tittle rule supplies A/AN before a word. Neither establishes an AND or OR alias for the diagonal by itself. PDF p15 separately gives larger n for THAN/THEN, reinforcing why the p3 hooked-sign entry must not be labelled THEN_THERE.

The p17 exercise-4 crop also has five similarly directed strokes at the locations aligned, with the answer visible, to its five conjunctions AND. This is corroborating visual context only, not an independent transcription or a certified new sign value. Rule 10 on p14 allows slanting dashes as stops, and rule 9 allows omitted words with blanks. Separator-plus-omission is therefore a possible explanation to investigate alongside a context-dependent sign or a plate/text discrepancy. None is selected as established.

### Effect on the saved development fixture

The parent candidate set at exercise-2 position 15 was `[or, ed]`. It was founded on the incorrect rule reading and is withdrawn in this audit. All other parent candidate rows are retained for traceability, not certified.

The strictly audited inherited fixture now covers **12/16** printed words, down from 13/16. This is a mechanical removal of an unsupported candidate, **not** a fresh recognition score or a decoder failure rate. It still misses DUTIFUL and both ANDs, and now leaves OR unresolved. The missing DUTIFUL remains a lexical-coverage issue. No replacement alias was learned from the printed answer, and no annealing or corpus search was run.

The full-word expansions and exercise outline assignments remain M-grade. The source labels/rule corrections are directly readable printed evidence, but this does not upgrade any Armstrong token. Target H/C/S/M/I plaintext assignments produced in this batch: **zero**.

## Exact inputs and recovery

| Input | SHA-256 |
|---|---|
| Source PDF | 243dfc316e7b7d2fb7cd282dcb503ce50aac3d44334bf93fa03e419bb017df3c |
| Parent #46 checkpoint text saved with trailing LF | e0ed828811ecebc276578e58fe16dc08eca9242a6424e23c4d99127d65d9bfc0 |
| Extracted parent Python capsule | 79ce28007848174b74e3813c1eb569195c8a8669c3032c293825d69a2047d201 |
| Audit recovery code below | ec13527cb03d77b642ea9508f8e2acf5023330c921e869eb785d2e0b6f0f1edb |

The parent program was parsed using Python AST and literal values; it was not executed. Its saved EXPECTED_ANNET rows supplied the inherited candidate lists. The capsule below embeds the audited rows and source corrections, so replay needs only the exact PDF, Python, and PyMuPDF. It requires no corpus, repository, solver, network, or previous scratch directory.

Extract the sole Python fence to `recover.py`, then run:

`python recover.py /absolute/path/to/Annet.pdf /absolute/fresh/output`

It verifies the PDF hash, refuses output under a detected Git worktree or into a nonempty directory, writes nine source crops, audit.json, crop-spec.json, and a SHA-256 manifest. Replay completed successfully in a fresh /tmp directory: coverage 12/16, target assignments 0, crops 9. The three narrow conjunction-mark crops and printed-answer crop were visually checked. No image-recognition accuracy is claimed by these integrity checks.

## Source failures and limits

No new source-access failure occurred. A local attempt to import requests failed because that package was absent in the default interpreter; curl then obtained the PDF successfully. The bundled runtime supplied PyMuPDF. This is not a blocker. No LOC/Rotunda endpoint was retried and no Livingston/Brant key was obtained; their existing access gaps remain in #44. No outreach, login, or access-control bypass occurred.

The corrected literal Annet instrument remains incomplete. The association between Annet and Armstrong is still unestablished. The old solver results are unchanged; these corrections concern the known-answer shorthand fixture, not a target decipherment or a design-family exclusion.

## One concrete next action

Using this exact same PDF, align the conjunction region of **exercise 11** against p16's printed words (AND, ARE, OR, OUGHT) and transcribe only its local stroke alternatives with crop coordinates. Check whether AND/OR are explicit signs, separators with omitted words, or unresolved plate/text discrepancies. Keep the exercise answer-aware and retain alternatives. Do not introduce general AND/OR aliases until the source rule or repeated contrasting examples supports them. Exercises 2, 4, 20, and the exercise-11 row viewed here are not held-out material.

Do not rerun mixed-piece or decimal-order searches. No target application is licensed by 12/16 development coverage.

## Continuation state and write boundary

```json
{
  "schema_version": 1,
  "checkpoint_id": "20260927T204842Z",
  "parent_pr": 46,
  "parent_head": "ca2607b130bcb4cf65c3c5b29b9c68a501c83ef8",
  "research_state": "open",
  "batch_state": "source-audit-complete",
  "active_lease": null,
  "running_jobs": [],
  "source_corrections": 3,
  "development_coverage": [
    12,
    16
  ],
  "target_assignments": 0,
  "next_action_id": "annet-exercise11-connective-alignment",
  "base_main_sha": "146365137bf6483c814880bd7cb3119e2dc90ad4"
}
```

Branch created from current remote main `146365137bf6483c814880bd7cb3119e2dc90ad4`. Exactly one new checkpoint file is intended. Never write/push main, merge, edit existing repository files, or touch ROOM.md, STATUS.md, status.json, or TSV queues. Each later checkpoint must use a fresh UTC-stamped branch from remote main and a one-added-file PR. The landing worker copies and closes without merging. Discover newer all-state PRs and leases before resuming. Do not send outreach or change the separate queue automation.

## Recovery capsule

```python
"""Replay the source audit without a corpus, solver, network, or repository write.
Usage: python recover.py /absolute/Annet.pdf /absolute/fresh/output
Requires PyMuPDF. Output must be outside any detected Git worktree.
"""
from pathlib import Path
import hashlib,json,sys
import fitz
DATA={'source_pdf_sha256': '243dfc316e7b7d2fb7cd282dcb503ce50aac3d44334bf93fa03e419bb017df3c', 'protocol': 'Answer-aware source audit; no blind recognition, no target application.', 'coverage': 12, 'total': 16, 'rows': [{'index': 1, 'components': 'DOT', 'grade': 'M', 'expected': 'a', 'candidates': ['a', 'you', 'an'], 'candidate_count': 3, 'expected_in_candidates': True, 'expected_in_corpus': True, 'expected_rank': 1}, {'index': 2, 'components': 'd+u+t+FULL', 'grade': 'M', 'expected': 'dutiful', 'candidates': [], 'candidate_count': 0, 'expected_in_candidates': False, 'expected_in_corpus': False, 'expected_rank': None}, {'index': 3, 'components': 'ch+l+d', 'grade': 'M', 'expected': 'child', 'candidates': ['child'], 'candidate_count': 1, 'expected_in_candidates': True, 'expected_in_corpus': True, 'expected_rank': 1}, {'index': 4, 'components': 'l+v+s', 'grade': 'M', 'expected': 'loves', 'candidates': ['leaves', 'lives', 'levies', 'levees', 'olives', 'loves'], 'candidate_count': 6, 'expected_in_candidates': True, 'expected_in_corpus': True, 'expected_rank': 6}, {'index': 5, 'components': 'f+r', 'grade': 'M', 'expected': 'father', 'candidates': ['father', 'for', 'far', 'free', 'fear', 'four', 'offer', 'fair', 'fore', 'affair', 'faire', 'fire', 'fur', 'fer', 'offre', 'fre', 'fare', 'fere', 'foroe', 'fri', 'affr', 'ferior', 'fr', 'freer', 'ofier', 'afiair', 'afore', 'fairer', 'ferr', 'foffre', 'fra', 'affaire', 'afiaire', 'afiier', 'efore', 'fiour', 'fir', 'offirir', 'offrir', 'ofifer', 'oifer'], 'candidate_count': 41, 'expected_in_candidates': True, 'expected_in_corpus': True, 'expected_rank': 1}, {'index': 6, 'components': 'a', 'grade': 'M', 'expected': 'and', 'candidates': ['an'], 'candidate_count': 1, 'expected_in_candidates': False, 'expected_in_corpus': True, 'expected_rank': None}, {'index': 7, 'components': 'm+th+r', 'grade': 'M', 'expected': 'mother', 'candidates': ['mother'], 'candidate_count': 1, 'expected_in_candidates': True, 'expected_in_corpus': True, 'expected_rank': 1}, {'index': 8, 'components': 's+t+r', 'grade': 'M', 'expected': 'sister', 'candidates': ['austria', 'astor', 'sister', 'ister', 'store', 'str', 'ster', 'aster', 'satur', 'stature', 'steer', 'stir', 'siter', 'situar', 'statuere', 'stouter', 'stru'], 'candidate_count': 17, 'expected_in_candidates': True, 'expected_in_corpus': True, 'expected_rank': 3}, {'index': 9, 'components': 'a', 'grade': 'M', 'expected': 'and', 'candidates': ['an'], 'candidate_count': 1, 'expected_in_candidates': False, 'expected_in_corpus': True, 'expected_rank': None}, {'index': 10, 'components': 'b+r', 'grade': 'M', 'expected': 'brother', 'candidates': ['brother', 'burr', 'bear', 'bar', 'bearer', 'ber', 'barrere', 'barrier', 'bor', 'bore', 'bare', 'br', 'bri', 'barr', 'beer', 'bur', 'bureau', 'aberra', 'abore', 'bier', 'boor', 'broi', 'iber'], 'candidate_count': 23, 'expected_in_candidates': True, 'expected_in_corpus': True, 'expected_rank': 1}, {'index': 11, 'components': 'l+k', 'grade': 'M', 'expected': 'likewise', 'candidates': ['likewise', 'like', 'lake', 'look', 'alike', 'leak'], 'candidate_count': 6, 'expected_in_candidates': True, 'expected_in_corpus': True, 'expected_rank': 1}, {'index': 12, 'components': 'DOT', 'grade': 'M', 'expected': 'a', 'candidates': ['a', 'you', 'an'], 'candidate_count': 3, 'expected_in_candidates': True, 'expected_in_corpus': True, 'expected_rank': 1}, {'index': 13, 'components': 'k+n+d', 'grade': 'M', 'expected': 'kind', 'candidates': ['kind'], 'candidate_count': 1, 'expected_in_candidates': True, 'expected_in_corpus': True, 'expected_rank': 1}, {'index': 14, 'components': 'm+r', 'grade': 'M', 'expected': 'master', 'candidates': ['master', 'mr', 'more', 'mere', 'mar', 'mer', 'amer', 'ameri', 'memoir', 'mare', 'mari', 'moreau', 'morier', 'emer', 'moore', 'mur', 'emere', 'imre', 'maimer', 'memoire', 'memor', 'meroe', 'miaire', 'mirror', 'moira', 'mor', 'morei', 'mre', 'oommeroe'], 'candidate_count': 29, 'expected_in_candidates': True, 'expected_in_corpus': True, 'expected_rank': 1}, {'index': 15, 'components': 'DIAGONAL_UNRESOLVED', 'grade': 'M', 'expected': 'or', 'candidates': [], 'candidate_count': 0, 'expected_in_candidates': False, 'expected_in_corpus': True, 'expected_rank': None, 'audit_note': 'Previously COMMA with or/ed candidates. The image is a diagonal; p14 rule 8 supplies ing/ed suffixes, not whole-word or.'}, {'index': 16, 'components': 'm+s', 'grade': 'M', 'expected': 'mistress', 'candidates': ['miss', 'mistress', 'mss', 'mass', 'meas', 'mis', 'amiss', 'mais', 'mies', 'ms', 'missis', 'massa', 'mes', 'amuse', 'mess', 'ames', 'mois', 'masses', 'moose', 'mous', 'mus', 'aims', 'mas', 'masse', 'meuse', 'mise', 'amis', 'ems', 'ims', 'miamis', 'mims', 'mos', 'ums'], 'candidate_count': 33, 'expected_in_candidates': True, 'expected_in_corpus': False, 'expected_rank': 2}], 'corrections': [{'id': 'comma-suffix', 'source_page': 14, 'printed_page': 10, 'rule': 8, 'old': ['or', 'ed'], 'corrected_suffixes': ['ing', 'ed'], 'whole_word_or_supported': False}, {'id': 'their-there', 'source_page': 3, 'old': ['then', 'there'], 'corrected': ['their', 'there'], 'scope': 'Explicit sign label, not exercise-2 coverage'}, {'id': 'outline15', 'source_page': 17, 'exercise': 2, 'index': 15, 'expected': 'or', 'old': 'COMMA', 'corrected': 'DIAGONAL_UNRESOLVED', 'grade': 'M'}], 'caveats': ['The other 15 rows retain parent candidates without certifying their component readings.', 'The two ANDs still lack an implemented direct value.', 'Dutiful remains absent from the parent corpus lexicon.', '12/16 is audited development coverage, not recognition accuracy.', 'No independent reader has examined these assignments.']}
BOXES={'alphabet-a': (3, [70, 110, 185, 172]), 'their-there': (3, [320, 460, 460, 510]), 'comma-rule': (14, [85, 265, 415, 320]), 'exercise2': (17, [90, 140, 440, 177]), 'e2-06': (17, [188, 146, 203, 164]), 'e2-09': (17, [254, 147, 268, 164]), 'e2-15': (17, [363, 147, 380, 164]), 'exercise4': (17, [90, 197, 444, 232]), 'answer2': (16, [90, 135, 422, 167])}

pdf=Path(sys.argv[1]).resolve()
out=Path(sys.argv[2]).resolve()
if not Path(sys.argv[2]).is_absolute(): raise SystemExit('Absolute output path required.')
if any((x/'.git').exists() for x in [out,*out.parents]): raise SystemExit('Output inside Git worktree refused.')
if out.exists() and (not out.is_dir() or any(out.iterdir())): raise SystemExit('Fresh empty output required.')
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==DATA['source_pdf_sha256']
assert sum(r['expected_in_candidates'] for r in DATA['rows'])==12
assert DATA['rows'][14]['candidates']==[]
out.mkdir(parents=True,exist_ok=True)
d=fitz.open(pdf)
for name,(page,rect) in BOXES.items():
    d[page-1].get_pixmap(matrix=fitz.Matrix(4,4),clip=fitz.Rect(rect)).save(out/(name+'.png'))
(out/'audit.json').write_text(json.dumps(DATA,indent=2)+'\n')
(out/'crop-spec.json').write_text(json.dumps(BOXES,indent=2)+'\n')
manifest={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(out.iterdir()) if f.is_file()}
(out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(dict(coverage=DATA['coverage'],total=DATA['total'],target_assignments=0,crops=len(BOXES))))
```
