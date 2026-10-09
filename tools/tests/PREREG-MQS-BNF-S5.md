# PREREG MQS-BNF-S5 (LANE MQS next, account 4) -- written before any scoring

Date: 9 Oct 2026, 09:42 UTC by date -u. Worker MQS-BNF-S5 (session_01F36TpH2jpGzNjQ6WkNjunG), for orchestrator (account-4).
Brief: .claude/briefs/runs/2026-10-09-ytbiz-mqs-next-bnf-s5.md (S5 of MQS-BNFPILE's "Later sessions"). Disk only; no host
contacted; no Gallica (403 to cloud since 8 Oct). No reading, no decoding, no status/key/AUDIT change.

## What S5 can and cannot do from the cloud today

The S5 list is: sign inventory on line crops, shape match against keys on file, a small sample read, a language trial,
the recipient's and sender's papers, the intercepting power's key depots (M45). The first three need page images; every
S2A/S2B pile is on Gallica (fr.3029 digitised yes), and Gallica answers 403 to cloud sessions. They are **not attempted**
and stay with S4/S5 for the next session in which Gallica answers. What can be done from the saved notices is the
catalogue side of attribution, built as one option:

`tools/bnf_findingaid.py --attribute NOTICE.html [...]` -- one row per bare (and named-but-unattributed) cipher item:
- **neighbour lead**: the nearest preceding and following attributed letters in the notice's own item order (sender,
  recipient, place/date text, folio distance), and whether the two agree; graded as a LEAD (M), never an attribution;
- **papers to search**: the candidate sender's and recipient's names (the "recipient's and sender's papers" step,
  as names to look up -- no lookup is done);
- **keys on file**: KEY-OFFICES.tsv rows whose `correspondents` or `office` name a candidate (a name lookup on the
  register, not a shape match -- the shape match needs images);
- **interceptor depots (M45)**: a fixed table of powers -> archive series where keys and decipherers' copies sit,
  for each power the candidate names imply (lead only; to be logged as a searched family when searched);
- **language trial set**: always the full trial list for `family_run.py --langs`; a neighbour's language (an
  "en italien"/"en latin" neighbour) is printed as `neighbour:<lang>` and is never the default (S5 brief, M41);
- volume-level leads (title, Présentation) for a notice with no item list (the 26 S2B image-triage notices).

## Corpus

Every saved notice under sources/bnf-findingaids/2026-10-07/ and 2026-10-09/, one per ark (filename). Attributed letters
are items whose text starts "Lettre de/d'" (optionally "Copie d'une", "originale") with a parsable sender (the first
upper-case word of 4+ letters in the sender clause, e.g. BONNYVET, TREMOILLE). Count before scoring (2026-10-09 only):
1,752 attributed letters in 52 volumes, of which 30 are cipher-flagged ("chiffr" in the item text).

## K1 known answer (design-matched: masked cipher letters)

Mask each attributed **cipher-flagged** letter (its sender hidden), predict its sender from the notice alone: top-1 =
the sender of the nearest preceding attributed letter in item order (the following one if there is none). Statistic
A_c = share of masked cipher letters whose predicted sender equals the true sender. This is the same design as the
intended use (a cipher item in a BnF notice whose sender the notice does not give), the same catalogue language
(French notices) and the same unit (one item). Expected: A_c about 0.5 (cipher items are sometimes filed apart from
their sender's run). Secondary, reported but not gated: A_all over all attributed letters (expected about 0.65), and the
"agree" precision (prev and next senders agree) for both sets.

## N1 within-volume random-position null (the gate's null)

Predict each masked letter's sender from a uniformly random *other* attributed letter of the **same volume** (200
draws, seed 20261009); report mean and p95 of the accuracy. Why it can differ from K1 for this statistic: K1 uses
adjacency in item order; N1 keeps the volume's sender mix and destroys order. A volume ordered by sender runs gives
K1 >> N1; a volume whose cipher items are filed apart gives K1 ~ N1 (rule 3, a control that can vary). Ceiling check:
if N1's mean is >= 0.95 the volume mix alone answers and there is no headroom -- the result is then "non-test".

## N2 across-volume null (floor)

Same, the random letter drawn from a **different** volume. Reported only.

## Gate

PASS iff (a) N_c >= 20 masked cipher letters, (b) N1_c mean < 0.95, (c) A_c >= N1_c p95 + 0.10. PASS ships
`--attribute` neighbour lead at shelf grade `controlled-only` (a lead generator, never an attribution: its output is M).
FAIL ships it at `weak` with both numbers and is not re-briefed. The keys-on-file, depot and language parts are plumbing
with offline catch / must-not-block tests and no control of their own: their grade follows the row (they are not claimed
to find anything). Nothing is run on a target from this option beyond listing leads for fr.3029 and the 26 image-triage
notices.

## Results (filled after scoring at 09:44 UTC by date -u; numbers above are not edited)

Corpus as run: 140 notices with >= 1 attributed letter (2026-10-07 + 2026-10-09, one per ark filename); the "52 volumes,
30 cipher letters" pre-count above covered 2026-10-09 only and a narrower letter pattern.
`python3 tools/bnf_findingaid.py --attribute-control sources/bnf-findingaids/2026-10-0[79]/*.html [--all-letters]`

| Set | N | volumes | A (top-1) | agree n / prec | N1 within-volume mean / p95 | N2 across-volume mean |
|---|---|---|---|---|---|---|
| cipher letters (gated) | 59 | 21 | 0.322 | 12 / 0.500 | 0.333 / 0.407 | 0.005 |
| all letters (reported) | 6,070 | 140 | 0.253 | 1,362 / 0.652 | 0.179 / 0.184 | 0.011 |

Gate: (a) N_c 59 >= 20 yes; (b) N1_c mean 0.333 < 0.95 yes (headroom); (c) A_c 0.322 >= 0.407 + 0.10 **no -> FAIL**.
A_c sits at the within-volume null's mean: for cipher letters, adjacency in the notice adds nothing over the volume's
sender mix. Over all letters adjacency beats N1 p95 by 0.069 (under the +0.10 a gate would ask; not gated), and the
agree case reads 0.652 -- the lead carries some signal for clear letters, none shown for cipher ones. Both nulls can and
did differ from K1 (N2 0.005 vs N1 0.333 shows the volume mix is most of the signal). Expected values were A_c ~0.5 and
A_all ~0.65; both came in lower (sender keys are imperfect: first-name-only signatures such as HENRY / CATERINE and
title-only senders read as separate keys, which lowers K1 and N1 alike).

Shelf: `--attribute` **weak** (FAIL above, not re-briefed); `--attribute-control` weak (the instrument that produced it).
Read a lead as "who writes in this volume", never as "who wrote this item".

Leads listed (no target changed): fr.3029 -- 7 rows (nos 34 f.67, 49, 59 f.134, 66, 68, 70 f.182, 72); no.34 is the
only agree=yes (TREMOILLE before and after, 2 folios each side; recipients ROBERTET / ROI); nos 49, 66, 68 sit between
TREMOILLE and BONNYVET; 70 and 72 follow BONNYVET; KEY-OFFICES.tsv names none of them; powers France only; no year in
the notice, so the generic trial set; no.59's neighbour is Latin (neighbour:la, not promoted). The 26 S2B image-triage
notices each give one volume-level row (powers from title/Présentation text: e.g. Dupuy 155 France Spain Papacy Empire
Florence Savoy; Clair. 460 Spain). Not built (need page images, Gallica 403 to cloud): sign inventory on line crops,
shape match against keys on file, the sample read -- they stay with S4/S5 when Gallica answers.
