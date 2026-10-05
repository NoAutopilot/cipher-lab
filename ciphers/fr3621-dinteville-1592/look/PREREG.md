# DIN-3623 unit 1 pre-registration (account-1 worker, 3 Oct 2026, written ~09:55 UTC before any image is viewed)

Brief `.claude/briefs/runs/2026-10-03-acct1-din-3623.md` step (1). Question: on f.128 (Gallica btv1b52524472n f265) are
the 7 occurrences of `0` that align to a non-e print letter (`firm/conflicts.tsv` rows 6-12: L03.1:13 c, L03.1:45 p,
L04.1:2 s, L05.1:4 s, L05.1:7 p, L05.1:28 s, L05.1:55 s) one sign with the e-reading `0`s, or a second sign merged
under the label `0` (a variant such as f.130's `0'`, the zero with a stroke or accent over it)?
Disclosure: I have seen the sign sequences and the conflict table, and f.130/tokens.tsv's list of 0' positions; no image.

Instrument: ONE vision look (this worker reading a composite) at the existing f.128 line crops
`images/f128_L03_s1/s2`, `L04_s1/s2`, `L05_s1/s2` (made by tools/iiif_lines.py in A2-DIN) stacked over f.130's
`images/zoom/f130_L02_s1_z.jpg` (holds f.130 L02 pos 13 and 18, both 0' read H). For each `0` on f.128 that can be
located, record: plain round zero / zero with a mark above or through it / other shape, and whether it is the
conflicting (non-e) or an e-reading occurrence.

Decision rule:
- **merged (two signs)**: >= 5 of the 7 conflicting occurrences are located and >= 4 of those carry the same visible
  mark (stroke/accent over or through the zero) that f.130's 0' carries, AND <= 1 of the located e-reading `0`s carries
  it. Then the conflicts are re-classed `transcription` (the sign is 0', not 0) in firm/conflicts.tsv; this counts as
  explained for the strict rule (firm_grades.py extended to accept the class, recorded here before running), f.128's
  0' occurrences are noted as the support for f.130's 0' (values c/p/s: still several letters, so 0' stays M/U, no
  value promoted), and decode_key.py --check + firm_grades.py --check are re-run (rule 7).
- **one sign**: the located conflicting occurrences look like the e-reading ones (no consistent mark; <= 1 of them
  marked). Row 0 stays M; the polyphone/scribal-error reading stands; nothing changes.
- **undecided**: anything else (fewer than 5 located, or a mark on 2-3 of them, or marks on e-readings too). Nothing
  changes; logged as image-undecided at this crop resolution.

## Unit 2-3 rule: fr.3623 f.23r sign set (written ~09:50 UTC, after the 808 px overview, before any line crop is read)

Overview (look/../f3623/f23rv_overview.jpg): f.23r carries a pasted slip, about 9 cipher lines with an interlinear
Italian decipherment in another hand, a signature and a dated line ("del angres il 2 ottobre"); f.23v carries only an
endorsement/address strip. One vision call (Sonnet subagent, 16 line crops from tools/iiif_lines.py) lists the cipher
signs with the f.128/f.130 labels (f128/pass_instructions.md + f128/README.md extras + v', 0') or NEW:<description>,
with counts, no values. Rule:
- **same family**: >= 85% of f.23r's cipher tokens take an existing f.128/f.130 label AND >= 70% of f.130's 20 most
  frequent sign types occur on f.23r. Then, if v', 0' or a NEW f.130 sign occurs on f.23r under an interlinear gloss,
  an alignment job is written as the next step with its price (not run now).
- **different**: < 60% of tokens take an existing label. Then f.23r is not a key source for v'/0'/NEW.
- **undecided**: anything between.

## Unit 1 re-look at native resolution (D2-DIN0, account 1, 5 Oct 2026, written 18:50 UTC before any new crop is viewed)

Brief `.claude/briefs/runs/2026-10-05-acct1-d2-din0.md` (a). Same question and **the same decision rule as unit 1 above,
unchanged** (merged: >= 5 of 7 conflicting located AND >= 4 of them carry f.130's 0' mark AND <= 1 located e-reading `0`
carries it; one sign: <= 1 of the located conflicting marked, rest like the e-readings; undecided: anything else).
Only the instrument changes: DIN-3623 viewed a 2400 px composite that the viewer downscales (~0.65x); this look uses
native-resolution sub-crops cut from the cached native region with
`python3 tools/iiif_lines.py --image ciphers/fr3621-dinteville-1592/images/src_ark_12148_btv1b52524472n_f265_200_1800_3700_560.jpg --out ciphers/fr3621-dinteville-1592/look/din0 --prefix f128n --centres 263,367,471 --lines-per-crop 1 --max-width 700 --overlap 120 --mask-neighbours --debug`
(no network), laid out two segments per row with ImageMagick, no rescaling, one sheet per line (L03, L04, L05 of f.128 =
din0 L01, L02, L03), viewed once by this worker in one pass. Each of the 7 conflicting positions is located by its
neighbouring signs from firm/conflicts.tsv; each e-reading `0` seen on the same sheets is recorded too.
Pre-declared tie-break, so that the call is mechanical: a zero counts as "marked" only if a stroke rises from the zero
and curls over or crosses above it (f.130's 0'); a plain round zero, a zero with a ligature tail joining the next sign
at mid-height, or an ink blot counts as plain; an occurrence that cannot be told apart from its neighbours counts as not
located. Disclosure: I have read DIN-3623's per-occurrence result (3 stemmed: L05.1:7, :28, :55; 4 plain).
If (a) gives merged (>= 5 of 7 settled as one class with the rule met), step (b) re-runs the per-occurrence check for
rows 0, sq, m with the conflicts re-classed `transcription`; otherwise (b) and (c) are not run.
