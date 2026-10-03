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
