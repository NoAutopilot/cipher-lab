# PREREG_slic.md -- pre-registered S licence for the unprinted paragraphs (ES132-SLIC, 8 Oct 2026)

Written and pushed 8 Oct 2026 before any score below was computed (brief: .claude/briefs/runs/2026-10-08-acct3-scout-jobs.md
"## ES132-SLIC"). Script: `slic.py` (written after this file; `--check` exits 1 if its outputs are stale). Precedent shape:
BIR-APPLY / D2-B117KAPC (ciphers/birago-fr3252-1571-72/NOTES.md). Nothing here sets depth or the N-class.

## Material (all on disk, no fetch)
- Known-answer paragraph P19: f.90v L10-L26 (19 Sept 1578), blind passes `passes/f90v_passA/B.tsv` (test 1 loader: load_lines +
  passnorm.norm_line), print `teulet_19sep1578.txt`.
- Known-answer paragraph P15: f.119v lower L07-L13 (`passes/passA/B.tsv`, test 1 loader) + f.120r L01-L04 (`passes/f120r_passA/B.tsv`,
  test2.load_pass), print `teulet_15oct1578.txt` (15 Oct 1578).
  Only the blind passes are used on the known-answer side (the reconciled f.119v/f.90v printed lines were touched by a reconciler
  who had read Teulet).
- Unprinted target: 19 Sept letter f.89r, f.89v, f.90r, f.91r (test2.load_pass), f.90v L01-L09 + L27 (test 1 loader);
  15 Oct letter f.119r L01-L20 (test 1 loader), f.119v upper (`f119vU`, load_pass), f.119v lower L02-L06 (`ciphertext.tsv` /
  `passes/passA/B.tsv`), f.120r L05-L29 (load_pass). Reconciled text = the committed `ciphertext_*.tsv` (clear spans cut by
  test2.strip_clear exactly as test2 does).

## Definitions
- Token components ("key cells"): its base symbol with underline (a key.tsv row, e.g. `24`, `35_`, `y`), its vowel indicator
  (`+ . σ ρ ⊣`, if present) and each above-mark (`@l @m @n @r @s`, if present). `@2` and dropped marks carry no letter and are
  not cells.
- Agreed token: in a line, difflib alignment of pass A vs pass B (tokens with trailing '?' stripped, as test2.err2); a token is
  agreed iff it lies in an `equal` block and neither pass marks it '?'. On the target side a reconciled token is agreed iff it is
  equal (no '?') to the aligned token of pass A AND of pass B (difflib of R vs A and R vs B, each per line).
- Correct token (known-answer side): decode all agreed key-decodable tokens of the paragraph with key.tsv in order, normalise
  with test0.norm per token, join, difflib-align to the normalised print (test0.known_agreement's procedure); a token is correct
  iff every letter of its segment lies in a matching block.
- Confirmed cell: a cell that occurs in at least **k = 2** correct agreed tokens of the derivation paragraph(s). k is fixed here;
  k = 1 and k = 3 are reported as sensitivity only and gate nothing.
- **Rule (S licence):** a token becomes S iff (i) it is agreed by both blind passes, (ii) it is key-decodable (not a code, not
  `{word}`, not a number >= 38 absent from key.tsv, not '#'), and (iii) every one of its cells is confirmed. Every other
  key-decodable token stays M. Code tokens (Cp.30 nomenclature, numbers >= 38 and `{words}`, no key on disk) stay U, are
  counted separately and never enter gate (a).

## Gates (all must pass; if any fails, stop, log in HYPOTHESES.md with both numbers, M stays M)
- (a) Held-out accuracy, both directions: derive confirmed cells from P19, apply the rule to P15's agreed tokens, accuracy =
  correct S tokens / S tokens; then derive from P15 and apply to P19. Require accuracy >= **0.90** in both directions, and at
  least 20 S tokens licensed in each direction (fewer = no test, counts as FAIL).
- (b) Control that can differ: the same two directions under 200 value-shuffled Cp.30 keys (test0.shuffled, seed 1578: the
  letter values permuted among numeric bases, which changes both which cells are confirmed and which tokens are correct).
  Report per direction the shuffled licensed-token count (mean, p95) and accuracy (mean, p95; undefined = 0). Pass iff, in both
  directions, shuffled p95 licensed count <= 0.25 x the true-key count AND shuffled p95 accuracy < 0.90.
- (c) Power at the measured error: r = pooled token disagreement of passes A and B (test2.err2) over all unprinted target lines
  above, computed by the script before injection. Into both known-answer paragraphs inject substitutions independently into
  pass A and pass B at rate r/2 each (a substituted token is drawn uniformly from the pooled known-answer token inventory),
  and in addition mirror 25% of the injected substitutions into the other pass at the same position (correlated misreads that
  agreement cannot catch). This is on top of the real passes' own disagreement, so harsher than measured. 20 seeds (1..20).
  Pass iff gate (a) (both directions, >= 0.90, >= 20 S tokens) holds on >= 16 of 20 seeds.

## If all gates pass (unit 3)
- Final confirmed cells: those occurring in >= k = 2 correct agreed tokens of P19 and P15 pooled.
- Regrade every unprinted target token with the rule; recount H/C/S/M/U per letter; list the longest contiguous S stretch per
  letter, in decoded letters, in reading order across lines and pages of one letter (any non-S key token or any code token
  breaks the stretch; '/' and clear-span cuts do not count as letters but a clear span breaks it) beside the design AD.
- AD for Cp.30, computed and written before the stretch is measured: H(K) = log2 of the Cp.30 letter table's key space
  (N = the numeric base symbols in key.tsv, counted by the script, each over 20 letter values: N x log2(20), the unfitted table, per tonight's depth
  bar -- a period key that was not fitted does not shrink H(K) to the liberties) plus every liberty (one bit per M token and
  per '?' inside the stretch: none inside an S stretch by construction; each settled-from-duplicate token inside it counts one
  liberty); R = 3.2 bits/letter (Spanish, per-letter redundancy); unicity U = H(K)/R; AD = 1.5 x U. The verifier, not this
  session, rules depth.
- Judge (unit 4): tools/judge_plaintext.py with the folder's es16 corpus on the S-only text and on a shuffled-target decode;
  per-fold spread reported (rule 3).
