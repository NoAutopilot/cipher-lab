# GAPS21-na-suriname-map-1781 (account-4), 3 Oct 2026 -- pre-registration (committed before any vision call or re-judge)

Target: 4.VEL 2077 legend only (ciphertext_2077_legend.tsv, 658 cipher tokens; GAPS20 decode H 456 / M 150 / U 52,
M+U rate 0.307).

M/U classes on 2077 by frequency (reading_2077_legend_nieuw_tokens.tsv): g (g|l) 46, [u-dots] 17, t 17, [sigma] U 14,
[f-loop] 13, [d-loop] 12, s 12, [dot] U 10, [kappa] U 9, b (k|i) 8, [d-hook] U 5, [amp] U 5, [x-dots] U 4, then <=3 each.

Classes to settle (this job): g (g|l, per token), b (k|i, per token), t, [u-dots], [f-loop], [d-loop], s -- 125 M tokens
on 15 lines. The U classes are not settled here (no key-sheet value to compare against beyond the GAPS15 reference set).

Instrument: blind shape comparison exactly as GAPS16 (passes/signcmp_gaps16/brief.md): the existing line crops
images/crops_2077_leg/leg77_<L>_s1/_s2.jpg (cut by tools/iiif_lines.py, command in NOTES.md GAPS19) are given as query
lines, renamed; references = GAPS15's value-blind sheet passes/signcmp_gaps15/blind_refs.jpg (R1-R29, mapping in
passes/signcmp_gaps15/blind_key.json). The call is told only "handwritten signs", no letters, values, decode or repo files;
it reports EVERY sign in the line with its best and second reference tile and confidences, so look-alikes are mixed in
by construction. At most 2 calls; call 1 = lines L05 L11 L15 L12 L14 L18 (74 target tokens), call 2 (only if the cap
allows) = L06 L08 L02 L03 L09 L10 L19 L20 L16.

Mapping back: the call's ordinal index is mapped to a token only where the reported sign count of the line equals the
transcription's (cipher + plain) sign count or, failing that, where the reported neighbour shapes agree with the
transcription's neighbours; otherwise the line's tokens stay as they are.

Settle rule (same as GAPS15/16): a token's value is set from the image only when best conf >= 0.6 and the runner-up
carries a different value; then it is written to exceptions_nieuw_image.tsv at grade H "by exception" with the call row
cited (two-valued tokens settle to one value). Otherwise it stays M. A shape-name class (t, [u-dots], [f-loop], [d-loop],
s) moves from M to H at code level in key_period_codes_nieuw.tsv only if >= 2/3 of its mapped instances meet the settle
rule on the key value already given; else per-token exceptions only.

Judge rule: re-decode with --check exit 0; new M+U token rate reported. The nl18 judge (NL18-CORPUS) is re-run beside
200 letter shuffles and judge_nl18_sweep.py's power curve; a FAIL or PASS counts as a test ONLY if the new M+U token rate
is below 0.05 (the judge's measured power threshold, ~5% letter error). At or above 0.05 the result is logged as a
non-test, with the reading's score placed on the corrupted-prose curve. A PASS that counts AND beats all 200 shuffles ->
"reading ready" ROOM line for a separate verifier; no status change.
