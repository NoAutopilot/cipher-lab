# PREREG -- BAL103-200, f.200r cipher vs its period decipherment (written and pushed before any alignment or score)

Worker BAL103-200 (account 2, LANE DEFAULT-A2-0710), 13 Oct 2026, written 07:48 UTC by `date -u`. Same design as
`b189/PREREG-BAL103-189.md` (read in full; every rule there not changed below holds unchanged). Key source under test: published
(Tomokiyo, louisxiv0.htm 1644 table) as this folder names its signs (`key_decode.tsv`, carrying R7C-BAL103K's c = p).

**Material.** BnF Baluze 103 (btv1b9001389d), DECODE R2745. openapi.bnf.fr canvas 424 = f.200r (foliated 200 by eye), cipher with a few clear words, headed "Du cinquiesme Octobre 1644 a Fontainebleau", 20 lines; the cipher continues on c426 (f.201r), c428 (f.202r), c430 (f.203r); c432 (f.204r) blank; c434 = f.205r, period decipherment headed "[Le]ttre de Monsieur Le Tellier du cinquiesme Oct.bre 1644 a Fontainebleau" (DECODE R2745 = ff.200-206). Only f.200r is transcribed in this job (one native region c424 1100,1950,3200,4300; crops `b200/images/f200r_L01-20_s1/s2.jpg` by `tools/iiif_lines.py --image b200/images/src_c424_1100_1950_3200_4300.jpg --prefix f200r --follow-slope 400 --debug`, overlay checked, 20 bands on 20 lines). Decipherment region c434 1500,1150,3100,4800 (native), read once after the reconciliation. Decipherment span P: from its start to the word that ends f.200r line 20 (that end is located by reading, since f.200r carries no clear word at its foot; if it cannot be located the whole f.205r page is used -- the DP has a free end gap), struck words omitted, interlinear insertions taken in, + 200 letters slack.
**Disclosure:** the canvases were viewed once at 800 px to identify the cipher leaf and its decipherment; at that size the decipherment's opening lines ("On a trouve beaucoup a redire de ce que on a sollicite le principat ... la ville de Barcelone d'envoyer icy des Ambassadeurs ...") were legible, and the clear words "pour empescher" on f.200r line 15 and "pour empescher que on ne" in the decipherment's line 18 were noticed. The passes are blind regardless (they never see either).
The decipherment is NOT transcribed or read closely until this file is pushed and both blind passes and the reconciliation are
committed. The blind passes are Sonnet subagents given only the f.200r line crops, `tx/PASS_INSTRUCTIONS.md` and the key sheet,
never the decipherment, never told the content.

**Units.** Two blind passes (A, B; B reads the lines in reverse order), one Sonnet call each; one reconciliation by this worker
(`tools/reconcile_passes.py --keep-plain`, disagreements settled from the crops, M grade throughout) -> `b200/f200r_rec.tsv`,
committed before the decipherment is read.

**Decode, statistic A, control, gate, per-sign classes, licensed edits:** exactly as PREREG-BAL103-189.md (script `b200/score200.py`
= `b189/score189.py` with file names changed only): A = matched cipher-derived letters / cipher-derived letters after semi-global
unit-cost DP against the decipherment span (from its start to the word ending the last transcribed cipher line, + 200 letters slack);
control 200 permutations of the single-letter cell values (seed 1644; it changes the decoded letters, so it can differ from the target
on A); gate A >= 0.60 AND A > perm p99 on BOTH blind passes. Per-sign confirmed/contradicted/undecided as there. Licensed key.tsv
edits: a sign contradicted in the reconciliation AND with the same aligned letter on >= 2 occurrences in each blind pass separately;
never the 9 (i|r|s) and never the f.50 sorter-bound confusable pairs (owner's pass). A sign contradicted on f.200r is additionally
reported against f.171r and f.189r (sign_table.tsv there): an edit is licensed only if it is not confirmed on either earlier sibling.

**The 9 counts and the pooled decision rule (stated in advance).** Standalone 9 tokens in the reconciliation, aligned letter,
strict-known per r10/PREREG.md addendum (aligned letter in {i, r, s} AND two letters each side match contiguously); k_i / k_r / k_s
strict and loose. Pool strict-known 9s: f.171r 6 (all s, r10/nines.tsv), f.189r 3 (all s, b189/nines.tsv), + f.200r.
- **What makes the split test a real test.** The registered test (G vs S shape -> {i} vs {r|s}, best-map accuracy vs exact
  label-permutation null p95) can PASS only when the pooled strict N and its minority-class count k sit on a `perfect_can_pass = yes`
  row of r10/power9.tsv: N >= 7 and k_i >= 2 (and N - k_i >= 2). Below that the read is a NON-TEST whatever it would show, and is
  not run.
- If the pool reaches that bar: the shape read runs as registered in r10/PREREG.md (one blind Sonnet call on a crop around each
  pooled strict 9, no values; PASS licenses only applying the split to the owner's f.50 9 piles later, no exceptions.tsv edit) --
  if this job's cap and box cannot cover the call, the counts are reported and the read is the named next step.
- If k_i stays < 2: NON-TEST logged. f.230 (DECODE R2746) is then run in this job only if f.200r finishes under 80% of cap (USD 4)
  and box (08:52 UTC); else named as next step.
- Descriptive only (licenses nothing; flagged by BAL103-189): the same counts for r vs s (k_r strict), with the same power9 bar
  stated for a later r-vs-s registration.
