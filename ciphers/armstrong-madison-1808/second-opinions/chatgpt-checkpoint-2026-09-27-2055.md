# Armstrong continuation: contrasting connective outlines in Annet

Recorded UTC: 2026-09-27 20:55:29 UTC.
Status: open. Completed batch: exercise-11 local source alignment.
Parent: [PR #47](https://github.com/NoAutopilot/cipher-lab/pull/47), immutable head `62b13ad253057b15bfffa1ac6766b2e6d1ca2e41`, file `ciphers/armstrong-madison-1808/checkpoints/20260927T204842Z.md`. Follow its parent chain to #46, #45, #44; their saved experiments must not be rerun.

## User steering and active continuation

The user explicitly requested continuing work instead of returning routine inconclusive status reports. Save such batches to GitHub without another status notification. This communication preference was also added to the existing Armstrong continuation task; its enablement and schedule are unchanged, and the separate queue task was not modified.

Active lease: `armstrong-glyph-source-comparison`, owned by the foreground continuation that created this checkpoint, expires **2026-09-27T22:00:00Z**. The lease covers comparison of the source-grounded Annet primitives with the long Armstrong graphic passages, including boundary uncertainty; another run should skip that batch while the lease is valid. This is a coordination note for work active at checkpoint creation, not a claim that a detached worker was launched. No solver process is running. Other source/key investigations are unleased.

## Completed result

Inspected the exact parent Annet PDF, SHA-256 `243dfc316e7b7d2fb7cd282dcb503ce50aac3d44334bf93fa03e419bb017df3c`, obtainable from [the catalogue's scan](https://www.dropbox.com/scl/fi/e0nih2zcsrhl5tfq2d8wy/Annets-Shorthand-1770.pdf?dl=1&rlkey=rn4g1tw3iwvnkv0wasqory24m). Exact imprint date remains qualified in #45.

PDF p16, printed p12, exercise 11 prints the sequence "and therefore sovereigns are or ought". On the matching p17 engraving:
- AND aligns to a descending diagonal, like the AND-aligned marks in exercises 2 and 4.
- ARE aligns to the small right-facing curve consistent with alphabet r.
- OR aligns to a loop attached to a right-facing curve, provisionally o+r.
- OUGHT aligns to the forked part-sign labelled aught/ought on p3.

All four alignments are **M, answer-aware, one reader**. The ARE/OR contrast is directly inspectable in adjacent marks; it is not a recognition-accuracy test. This makes it unsafe to generalize exercise 2's diagonal at the printed OR position into a general OR sign. Exercise 2 may contain a plate/text discrepancy, an abbreviation, or omitted-word punctuation; the reason remains unresolved. No new direct OR alias or AND alias was installed in the inherited candidate engine. The parent 12/16 audited development coverage is unchanged.

The full exercise was not decoded blindly. Only the four local marks were transcribed; the surrounding printed answer was used to locate them. Target plaintext assignments: zero. The earlier correction of comma suffixes to ing/ed and of the p3 sign to THEIR_THERE stands.

## Reproduction

The sole code block below requires Python and PyMuPDF. It checks the PDF hash, refuses output in a detected Git worktree or nonempty directory, and writes four crops plus the full row, answer region, and alignment data. Coordinates are PDF points, upper-left origin; pages are 1-based. These exact crops were rendered and visually inspected during the batch. Run `python recover.py /absolute/Annet.pdf /absolute/fresh/output`. No network, corpus, annealing, or repository write is involved.

## Continuing work and input provenance

The foreground continuation has retrieved and hash-checked the following target evidence for the leased comparison:
- [Tomokiyo inventory](https://cryptiana.web.fc2.com/code/madison_armstrong_graphic.png): `870a28315e330f94e257da0a9f4d0ea17b642bc1e0693457a8fb1c4cc9c00586`.
- [Passage sheet 1](https://cryptiana.web.fc2.com/code/madison_armstrong_graphic1.png): `6b11d02b39ee0c21fcf5ce436defbcdd5a2584b7bb63bb1aa9e92a6b54711710`.
- [Passage sheet 2](https://cryptiana.web.fc2.com/code/madison_armstrong_graphic2.png): `e85d535c31d2ee181b0e2c527ebfc07311d6c2763c8d8a847b235971206d19f5`.
- Repository manuscript `images/M34-014-0030.jpg`: `bd0b6c7c74d36794efab28b302a8ea3810028feb60313836c8abef7a801c0681`.
- Repository manuscript `images/M34-014-0031.jpg`: `d4989c726ca22bce53800b2d091d650f7f8040a808d50979c1569ff3c3b12ac0`.

The target files live under `ciphers/armstrong-madison-1808/`; repository images were retrieved read-only. No target inference is recorded yet. A search-engine-1 query was noisy and gave irrelevant results; search-engine-2 located the current Madison project page, existing solver claims, and the known Monroe catalogue lead. No new key was obtained, and no previously blocked endpoint was retried. The established cautions about unverified online decipherment claims remain.

Next concrete action: inspect native target page-1 long passages and page-3 tail against the source primitives, preserving joined-stroke, dot and length alternatives; determine whether a literal match can be made without inventing glyph values. Record the result and release the lease in a fresh checkpoint. If the literal instrument cannot discriminate, move to primary-key recovery rather than tuning a flat-letter surrogate.

## Immutable boundary

Base: current remote main `2e201087af44dfb3282890fdc8cc51eb4e0e0878`. One ADDED checkpoint file on a fresh `second-opinion/armstrong-checkpoint-20260927T205529Z` branch and one PR to main. Never write/push main, merge, edit an existing file, or touch ROOM.md, STATUS.md, status.json or TSV queues. No outreach. Landing worker copies and closes without merging.

```python
from pathlib import Path
import hashlib,json,sys
import fitz
SOURCE_SHA='243dfc316e7b7d2fb7cd282dcb503ce50aac3d44334bf93fa03e419bb017df3c'
DATA=[
 {'word':'and','primitive':'descending diagonal; no licensed general alias','rect':[252,410,263,423],'grade':'M'},
 {'word':'are','primitive':'r, right-facing curved stroke','rect':[294,409,305,423],'grade':'M'},
 {'word':'or','primitive':'o+r candidate, loop joined to right-facing curve','rect':[305,408,318,425],'grade':'M'},
 {'word':'ought','primitive':'AUGHT_OUGHT candidate','rect':[319,407,332,426],'grade':'M'}]
p=Path(sys.argv[1]).resolve();out=Path(sys.argv[2]).resolve()
assert hashlib.sha256(p.read_bytes()).hexdigest()==SOURCE_SHA
if any((x/'.git').exists() for x in [out,*out.parents]):raise SystemExit('Outside Git worktrees only')
if out.exists() and any(out.iterdir()):raise SystemExit('Fresh output required')
out.mkdir(parents=True,exist_ok=True);d=fitz.open(p)
for x in DATA:d[16].get_pixmap(matrix=fitz.Matrix(8,8),clip=fitz.Rect(x['rect'])).save(out/(x['word']+'.png'))
d[16].get_pixmap(matrix=fitz.Matrix(5,5),clip=fitz.Rect(87,394,445,444)).save(out/'row.png')
d[15].get_pixmap(matrix=fitz.Matrix(5,5),clip=fitz.Rect(88,414,431,479)).save(out/'answer.png')
(out/'alignment.json').write_text(json.dumps(DATA,indent=2)+'\n')
print('four M-grade answer-aware alignments; zero target assignments')
```
