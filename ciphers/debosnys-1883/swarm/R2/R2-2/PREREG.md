# R2-2 T-LOW pre-registration (DEB-SWARM2-R2-2, written 29 Sept 2026 08:3x UTC, before any crop is cut or read)

Brief: `.claude/briefs/runs/2026-09-29-deb-swarm2-R2-2.md`; entry R2-2 of `../../DIGEST-1.md` "Round-2 prompts".
Public copies only. Nothing here is a reading of the cipher (grade S/M; 0 H, 0 C).

## Order of work (the known-answer control gates everything after it)

1. Public-resolution search (web search for a larger public copy than the Schmeh/Cipherbrain PNGs; logged).
2. Written sign-or-mark rule for BAR-SOLID, BAR-THIN, BLOB, DASH-V, DASH-H, HOOK-L (RULE.md), from the images.
3. Declared folds: PCT+PCT-SLASH, X+X-DOT, X+X-CURL. Every error figure is reported unfolded and folded.
4. **Known-answer control** (below). If it fails, stop: steps 5-6 are not run.
5. Two fresh value-blind readers on the 156 disputed c1+c2 boxes and a 90-box audit sample (60 of the 291
   majority-settled, 30 of the 464 A-B agreed, seed 20260929), one line of crops per call.
6. Adjudication and noise estimate.

## Known-answer control (step 4)

- Synthetic page: 12 lines x 8 target boxes = 96 targets, each line padded with neighbours so every target has two
  neighbours each side. Pixels: real box crops from the public PNGs (the source boxes of `glyphs/bitmaps.npz`, i.e.
  `glyphs/signs.tsv` rows, native pixels, no resampling) pasted onto blank paper cut from the same scans. Deviation from
  the digest's wording, stated: bitmaps.npz holds 48x48 size-normalised copies of these same boxes; re-rendering those
  at box size would resample the ink, so the boxes' own pixels are used instead, which is exactly the public resolution.
- Truth: an instance is eligible only if passes A and B agreed on it (`agree-AB` in the settled drafts, c1-c4) and it is
  not an exemplar tile of `glyphs/inventory.tsv` (the readers' reference sheet). Target ids are drawn from the pooled
  A/B/C candidate ids of the 156 disputed boxes (matched class mix), restricted to ids with an eligible instance;
  neighbours from the settled c1+c2 id distribution. Seed 20260929. Stated limitation: the truth labels are two-reader
  agreements, which H51 bounds at up to ~17 pct hidden error on c2 -- so the control's error is an upper bound on the
  protocol's, and the control cannot test segmentation (no `_` boxes are planted).
- Readers: R1 a Sonnet subagent, R2 an Opus subagent, each fresh, never shown truth, pass files or this file's rule
  section; the H2 reader prompt (`scripts/PROMPTS_c1.md`) plus the RULE.md sign-or-mark instruction; the 160-id
  inventory sheet as tiles; one line (8 targets) per call; each target crop = the box plus two neighbours each side,
  target outlined in red, upscaled 4x Lanczos.
- Protocol output per target: settled = R1's id if R1 == R2, else unsettled.
- **Control error** = (settled and != truth) + unsettled, over 96, at the declared folds. Also reported: unfolded, and
  each reader's single error.
- **Kill (control): control error > 5 pct (more than 4 of 96) -> stop and report: the public images are the limit.**

## Real run (only if the control passes)

- Votes per disputed box: A, B, C, R1, R2. Settled if R1 == R2, else an id with >= 3 of 5 votes, else unsettled.
- Audit: fresh R1 == R2 agreeing on an id different from the settled id counts as a measured majority/agreement error;
  R1 != R2 counts half. Rates scaled to the strata (291, 464).
- Noise estimate over the 914 c1+c2 boxes = (unsettled disputed + est. wrong majority + est. wrong agreed) / 914,
  folded and unfolded.
- **Kill (real): estimate >= 5 pct (folded) -> the protocol does not bring c1+c2 under 5 pct on public images.**
