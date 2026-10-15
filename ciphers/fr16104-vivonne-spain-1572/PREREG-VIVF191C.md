# PREREG-VIVF191C -- f.191r (ink 63) L22-L36, third fresh blind pass E with a per-line drift check (15 Oct 2026, 02:2x UTC by date -u)

Job VIV-F191C (run on account 1 for LANE VIV-KEYSTONE, account 4; brief .claude/briefs/runs/2026-10-15-acct4-for-acct1-jobs.md, JOB VIV-F191C).
Written and pushed BEFORE any crop, reader call or statistic of this job. Report only: tx/viv63_f191/f191.py's reconciliation
(3-of-4 rule, PREREG-VIVF191 s.3), rec.tsv, decode.tsv, key.tsv, reading_piece63.tsv and status.json are not changed. A 5-pass rule, if
any, is the parent's separate PREREG.

## 1. Lines and crops
- Lines: f.191r L22-L36 (15 lines; the lines where VIV-F191B found pass D drifted across line ids).
- Crops: PREREG-VIVF191 s.1 command, verbatim (openapi.bnf.fr, one request, take/release ROOM lines, >= 3 s apart, at most 2 requests
  in this job); acceptance: every box identical to images/p63/manifest_vivf191.json for L22-L36 (s1 and s2), and the debug overlay
  checked by eye on those lines. Crops stay in the scratchpad; no image file into git.

## 2. Reader protocol (pass E)
- Sonnet subagents, blind: prompt = tx/SIGNS.md + "segments s1/s2 of a line overlap ~150 px: write the overlapping signs once" (as
  PREREG-VIVF191 s.2). Readers see no key value, no decode, no earlier pass (A, B, C, D) and no other reader's output.
- One call per two lines (four crops: Lnn_s1, Lnn_s2, Lmm_s1, Lmm_s2), L22+L23, ..., L34+L35, L36 alone: 8 calls. Each call is told the
  line id of each crop and returns one `Lnn<TAB>codes` row per line, text only. The worker saves the rows unedited (except joining the
  eight replies) as tx/viv63_f191/f191r_passE.tsv (`row<TAB>codes`, pass A/B/C/D format).
- Cleaning: f191.py's clean() (tx/viv63_clean.py rules).

## 3. Drift check (per line, gate for using pass E)
- For each line Lnn in L22-L36: same = NW agreement fraction of E[Lnn] with A[Lnn]; nb = max(agreement of E[Lnn] with A[Lnn-1], A[Lnn+1])
  (agreement = matched pairs / alignment length, f191.py nw_agree / mapping()). The line passes when same > nb (strict).
- Gate: E is used (sections 4-5 reported as results) only if >= 13 of 15 lines pass. Otherwise E is logged with its numbers and not used;
  sections 4-5 are then reported as diagnostics only, labelled "not used".
- Instrument controls, reported beside E (they can fail differently from E, since each pass's own rows enter the statistic): the same
  check on pass C (expected to pass, VIV-F191B 36/36) and on pass D (expected to fail on many of L22-L36, VIV-F191B's diagnostic
  A-D 0.745). If C fails >= 3 of 15 or D passes all 15, the drift check is reported as non-discriminating here and E's gate is "not a test".

## 4. Agreement (reported)
- Per line on L22-L36 and pooled: err_2reader = 1 - (sum matched)/(sum alignment length), NW (f191.py stats (a)), for E-A, E-B, E-C; and,
  for reference, A-B, A-C, B-C on the same lines.

## 5. What a fourth vote would settle (reported, no rule changed)
- Columns: f191.py cols() generalised to five passes A, B, C, D, E (star on A, insertions paired by order within each pass); columns
  where A-D are all '-' are dropped, so the A-D columns and decide() reproduce rec.tsv's flags (checked: flagged count on L22-L36 equals
  rec.tsv's, before the oo merge).
- For every rec.tsv-flagged column on L22-L36: plurality = decide(A, B, C, D)'s sign; E is counted as agrees-plurality, agrees-minority
  (E equals another non-'-' sign in A-D), other sign, or '-'.
- Also: with E in D's place (A, B, C, E), how many of those columns reach >= 3 of 4 (settled), and how many of those settle on the old
  plurality sign vs a different sign. Counts only; no reconciliation file is written.

## 6. Stop rule
Cap USD 8 (cost not visible to this session: stop at 80% of the box), box 90 minutes (02:10-03:40 UTC 15 Oct, 80% at 03:22); do not
start a reader call after 03:22. openapi.bnf.fr <= 2 requests.
