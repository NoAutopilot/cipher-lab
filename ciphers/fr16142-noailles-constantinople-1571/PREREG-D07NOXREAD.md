# PREREG D07-NOXREAD -- c510 L05-L14 reader-transcription decode with Tomokiyo's key, scored against Dupuy 521 221R ff.

Written 7 Oct 2026 01:3x UTC (date -u), committed and pushed before either reader pass is run and before any decode statistic exists.
Brief: `.claude/briefs/runs/2026-10-07-account1-default-0042-jobs.md` D07-NOXREAD. Method = RUN6-NOXREAD's reader route
(reader signs named in Tomokiyo's table terms, key = the letter part of each id, test0's exact-LCS statistic); the retired
atlas-tile/bridge instrument is not used.

## Material
- c510 native canvas (Gallica btv1b9060927q f510, sha1 3a81f5c8..., = run2/nxatl/source_manifest.json), lines L05-L14 cut with
  `tools/iiif_lines.py --region 1050,250,3780,5450 --centres <run2/nxatl/line_centres.json c510> --follow-slope 300 --slope-margin 15
  --max-width 1400 --overlap 100 --prefix c510r` (30 crops, 3 per line; crops kept in the worker scratchpad, regenerable).
  L05 opens in clear ("Jours au paravant La reception d'icelle que"); readers transcribe only the cipher after the clear words.
- Reader references: Tomokiyo's table image (CharlesIX_Acqs2.png, not committed) and an exemplar sheet of c262 tiles per label of
  `witness/c262rc_recon.tsv` (tiles of the label's majority atlas cluster only; built from committed crops; not committed), plus the
  NX-RECUT glyph rulings (n1, t2, W:le, e3, s2, d1).
- Reference text: Dupuy 521 221R-226R as `run2/nxaln/nxaln.py dupuy_stream()` (after "la reception d icelle que"), letters only
  (test0 norm). Window = the first ceil(1.2 x n) letters, n = letters in the decode being scored.

## Passes and the stop rule
Two Sonnet subagent passes, one call each, blind to each other, to every earlier reading and to Dupuy; given crop paths + the two
reference images only. Output one TSV row per line: `L05<TAB>tokens`. `tools/reconcile_passes.py` aligns them;
**if err_2reader (disagreement columns / aligned columns) > 0.10, the job stops after reconciliation** (TRANSCRIPTION.md / brief):
the reconciled text is written but no decode statistic is computed or reported. Reconciliation is this worker's, from the crops,
before any decode is printed, Dupuy not consulted.

## Statistic, controls, gate (only if err_2reader <= 0.10)
Scored text = the reconciled transcription; '#' (o1/e2) resolved as e (primary), o reported beside it.
Statistic R = exact LCS ratio 2*LCS/(|a|+|b|) (test0 `--stat lcs`) between the decode and the Dupuy window.
Controls (each can change R):
- (k) shuffled key: letter values permuted among the letter glyph ids present, 1000 seeds (seed 16142). Gate: R > p99.
- (o) decode letter-order shuffled, 1000. Gate: R > p99.
- (c) Dupuy window word-order shuffled, 10 seeds. Gate: R > max.
- (w) wrong window: same-length Dupuy windows starting at letter offsets 1500, 2500, ... (every 1000) to the end. Gate: R > max.
PASS = all four gates. Reported, not gated: each blind pass decoded alone, and the 'o' resolution.
Grades (rule 4): no per-token alignment is run here, so every decoded token is M whether or not the block passes (as RUN6-NOXREAD);
S 0, H 0, C 0. A PASS licenses only "the reader transcription of c510 L05-L14 under Tomokiyo's key reads toward Dupuy's copy beyond
four nulls", a candidate for a verifier, not a reading.
