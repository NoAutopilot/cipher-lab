# es17c7: all seven Cartas tomes (1634-1648), widening es17c from three folds to seven

Built 27 Sept 2026 (parent worker MERCY-JUDGE2, `.claude/briefs/runs/2026-09-27-parent-ytbiz-mercy-judge2.md`),
a validation-only job on `ciphers/espagnol142-mercy-1648`. `tools/data/es17c` (25 Sept 2026, LANE R6 worker MJ)
already register-matched the target -- 1643-1647 Spanish court-newsletter prose from three of the seven **tomos**
of *"Cartas de algunos PP. de la Compañía de Jesús sobre los sucesos de la Monarquía entre los años de 1634 y
1648"** -- but its own leave-one-file-out check blends 23.5% from only three folds that disagree 4x (10.0/21.0/
39.5%), which CLAUDE.md rule 3's MJ/es17c paragraph flags as "a FAIL/PASS of unknown reliability", the same way a
control below its own gate cannot license a target reading. This job fetches the other four tomes so the same
check runs on seven folds instead of three, and re-scores the reading, the letter's own clear words and 20
shuffled nulls under the pre-registered conditions the brief states.

## Source

Internet Archive `_djvu.txt` OCR of all seven tomes of *Memorial histórico español* (Madrid, Real Academia de la
Historia) that together make up the whole *Cartas* series, University of Toronto scans (the same `realuoft`
series es17c already used for tomos V-VII):

| identifier | MHE tomo | Cartas tomo | date range | folded letters |
|---|---|---|---|---|
| memorialhistri13realuoft | XIII | I | 1634 - 1636 | 751,121 |
| memorialhistri14realuoft | XIV | II | Jan 1637 - 17 Aug 1638 | 709,927 |
| memorialhistri15realuoft | XV | III | 17 Aug 1638 - 22 Sep 1640 | 688,302 |
| memorialhistri16realuoft | XVI | IV | 22 Sep 1640 - early 1643 | 674,595 |
| memorialhistri17realuoft | XVII | V | Feb 1643 - end 1644 | 717,113 |
| memorialhistri18realuoft | XVIII | VI | c.1645-1647 | 719,360 |
| memorialhistri19realuoft | XIX | VII (last) | 17 Feb 1645 - 4 Jun 1647 | 662,800 |

**Combined: 4,923,218 folded letters** (well over es17c's 2,099,273). The four new tomes (I-IV, MHE XIII-XVI)
were confirmed by their own printed front matter ("CARTAS DE ALGUNOS PP. DE LA COMPAÑÍA DE JESÚS ... TOMO
[I-IV]", each stating the date range it covers) before fetching in full. See MANIFEST.tsv for URLs, byte counts
and sha1; tomos XVII-XIX are byte-identical copies of the files already committed at `tools/data/es17c/`.

## Hold-out check

Grepped all four new raw volumes for "Mercy"/"Mercij", "Barneton", "Sumiller" and "Brandenburg" before cleaning
(the same terms es17c's own README checked). **Zero hits for Mercy/Mercij or Barneton in any of the four; one
generic "sumiller de Corps" reference (memorialhistri13realuoft, a different court office held by someone else,
not the target's addressee or his office) — the same non-hit shape es17c's own three volumes already showed.**
These four tomes (1634-1643) predate the target's own 6 June 1648 letter by 5-14 years and predate even Leopold
Wilhelm's 1647 arrival as governor-general (the sender inferred by V6-MERCY's postmortem), so no hit was
expected. Not flagged in ROOM.md (nothing found that needed flagging).

## Cleaning

Same convention as es17c: each raw `_djvu.txt` was cut to the letter text only, front matter (title page,
"LIBRARY / UNIVERSITY OF TORONTO" ownership stamp, OCR garbage from an illustrated/blank leaf) removed before
the volume's own first `CARTAS` section heading (raw line 73 of tomo XIII, 65 of XIV, 77 of XV, 84 of XVI in
each volume's own raw djvu text). Unlike tomo XIX (which needed its own cumulative seven-tomo name index cut
from the end), none of tomos XIII-XVI carries a comparable back-matter index -- each simply ends
"FIN DEL TOMO [I-IV]" followed by a few lines of University of Toronto library-pocket boilerplate, left in
place (the same "scattered low-volume OCR noise ... not worth further stripping" judgment es17c's own README
made).

## Wired into `tools/judge_plaintext.py`

Added as a new, separate key `LANG_CORPORA["es17c7"]`, alongside `"es17c"` (unchanged, not edited in place per
this job's brief) and `"es"` (the spec default, also unchanged). A spec opts in with
`"judge": {"language": "es17c7", ...}`. `python3 tools/judge_plaintext.py --selftest` passes after the edit
(selftest is corpus-agnostic).

## Held-out real-prose false-negative rate, es17c vs es17c7 (rule 3, both numbers)

`holdout_check.py` (leave-one-file-out, N=519 matching the target's own code-only reading length, 200 samples
per held-out file), run on both corpora this pass:

```
es17c (3 folds, unchanged from 25 Sept 2026):
held_out=memorialhistri17realuoft.txt.gz N=519 samples=200 real_p05=-0.847 false_negatives=79/200 (39.5%)
held_out=memorialhistri18realuoft.txt.gz N=519 samples=200 real_p05=-0.866 false_negatives=42/200 (21.0%)
held_out=memorialhistri19realuoft.txt.gz N=519 samples=200 real_p05=-0.892 false_negatives=20/200 (10.0%)
TOTAL false-negative rate: 141/600 (23.5%)

es17c7 (7 folds, this job):
held_out=memorialhistri13realuoft.txt.gz N=519 samples=200 real_p05=-0.878 false_negatives=21/200 (10.5%)
held_out=memorialhistri14realuoft.txt.gz N=519 samples=200 real_p05=-0.866 false_negatives=21/200 (10.5%)
held_out=memorialhistri15realuoft.txt.gz N=519 samples=200 real_p05=-0.882 false_negatives=15/200 (7.5%)
held_out=memorialhistri16realuoft.txt.gz N=519 samples=200 real_p05=-0.902 false_negatives=4/200 (2.0%)
held_out=memorialhistri17realuoft.txt.gz N=519 samples=200 real_p05=-0.867 false_negatives=46/200 (23.0%)
held_out=memorialhistri18realuoft.txt.gz N=519 samples=200 real_p05=-0.869 false_negatives=29/200 (14.5%)
held_out=memorialhistri19realuoft.txt.gz N=519 samples=200 real_p05=-0.872 false_negatives=20/200 (10.0%)
TOTAL false-negative rate: 156/1400 (11.1%)
per-fold spread: 2.0-23.0% (11.5x)
```

**Blended rate roughly halved (23.5% -> 11.1%) but per-fold spread widened, not narrowed** (3.95x on es17c's
three folds -- 39.5/10.0 -- versus 11.5x on es17c7's seven -- 23.0/2.0). Four more, more homogeneous-looking
folds (2.0-14.5%) pulled the blend down, but tomo XVII's own fold is *worse* alone against the wider six-file
training set than it was against the narrower two-file training set inside es17c (23.0% vs 39.5% -- actually
better here, but still the single highest fold) while tomo XVI's fold is now very low (2.0%). This is the same
shape CLAUDE.md rule 3's es17c/MJ paragraph and the EN-FOLDS paragraph both warn about: adding sources does not
automatically tighten a blended fold rate, and a wide per-fold spread says the blended number is not trustworthy
on its own, whichever direction it moved. Per this job's pre-registered gate (11.1% blended is over the 10%
line, and 11.5x per-fold spread is far over the 2x line), **es17c7 does not clear the gate either** -- widening
the corpus did not turn the judge into a usable gate for this target's own N.

## Judge output, clear words and the reading, against es17c7 (rule 7, pasted)

Spec variant `{"judge": {"language": "es17c7", "letters_min": 200, "control_samples": 200}}` (not committed as
a separate `specs/` file, matching es17c's own convention -- see
`ciphers/espagnol142-mercy-1648/NOTES.md`'s MERCY-JUDGE2 section for the exact commands and full pasted output,
including the 20 shuffled-null scores).

```
$ python3 tools/judge_plaintext.py <es17c7 spec variant> --file ciphers/espagnol142-mercy-1648/reading.txt
ok   length: got=1342, min=200, max=1000000000
FAIL language: score=-1.027, null_p99=-1.961, real_p05=-0.858, real_median=-0.789, mode=both, N=1342
$ python3 tools/judge_plaintext.py <es17c7 spec variant> --file ciphers/espagnol142-mercy-1648/m2/clear_words_only.txt
ok   length: got=782, min=200, max=1000000000
FAIL language: score=-0.889, null_p99=-1.937, real_p05=-0.87, real_median=-0.795, mode=both, N=782
```

**The letter's own clear words still FAIL** (-0.889 vs real_p05 -0.870, a 0.019 gap) -- narrower than es17's
0.004-wide near-miss but still on the wrong side, and essentially the same borderline shape es17c already
showed (-0.891 vs -0.867, a 0.024 gap). Per this job's own pre-registered condition (blended rate under 10% AND
per-fold spread under 2x AND clear words PASS, or the verdict is "judge cannot decide" regardless of the
reading's own score), **neither corpus-quality leg of the gate is met, so the verdict is "judge cannot decide"
-- the reading's own FAIL is not read as a negative.**

## 20 shuffled-null decodes

Reported for the record (the brief's own pre-registration means these do not change the verdict, since the
corpus-quality gate already failed before this step): the reading's own folded letters (N=1342, comment lines
stripped the same way the CLI strips them), shuffled with 20 different seeds (order destroyed, letter multiset
unchanged), scored through the same es17c7 model. **All 20 shuffled nulls FAIL** (scores -2.103 to -1.996, all
below `null_p99` -1.961 -- the judge's own corpus-derived shuffle threshold at this N -- and far below `real_p05`
-0.858), so the judge does at least separate the reading's own order from a scramble of the same letters at this
N; that is a necessary condition for the judge to be informative, not a sufficient one given the corpus-quality
gate above.

## Excluded / not attempted this pass

CODOIN and the "Sor María de Ágreda y Felipe IV" correspondence, both already excluded by es17c's own README for
the reasons stated there -- not revisited. A homogeneity split (by correspondent or date range within a tomo,
rather than by whole tomo) is the next cheap step named by es17c's own README and remains untried; the seven-fold
result above suggests it may matter more than tomo count alone (tomo XVI's very low 2.0% beside tomo XVII's
23.0%, both now trained on six other tomes, still differ by over 10x).

Requests this pass: archive.org 4 `advancedsearch.php`/`metadata` lookups (confirming tomos XIII-XVI exist and
reading their own titles), 4 `_djvu.txt` downloads, all >=1.6s apart, descriptive UA (well under the brief's
30-request/IA-only allowance; no other host touched).
