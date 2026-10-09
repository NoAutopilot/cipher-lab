# PREREG-BRO178 (9 Oct 2026, BRO-178 worker, account 2; for LANE FAMILY-A2j)

Written and pushed before any score on the target was computed. The only run before this commit was
`scripts/27_bro178_align.py dryrun --perms 200` on a stand-in (first 40 tokens of appendix Carta 13, not the target):
S 35/40 = 0.875 vs permuted mean 0.239, p99 0.350 -- so the statistic can separate at about this N.

**Premise correction (eye check, 15:2x UTC).** m0178 carries ONE code run, lines 1-4, ending
`vai 4.19.26 Caminho 55.24.12.57.3.y.8.21.15.12 14.19`; BRO-SWEEP's "second run ... mid-page" is that same run's tail
(clear prose follows, then the close "Londres 25 de Abril de 1713"). The run is the tail of Carta 79 (begins on m0177),
whose cipher copy and Deciffrada the appendix gives (plaintext_appendix.tsv row m0287 / Carta 79). So this is a known-text
key test and a body-vs-appendix copy diff, not a reading.

**Material.** Target stream `body178_ciphertext.tsv` (m0178 lines 1-4), from two blind Sonnet passes over
`images/crops_m0178_b178/` (bro178/passA.tsv, passB.tsv; crop paths only, appendix never shown), reconciled with
`tools/reconcile_passes.py --keep-plain` and settled by the worker from the crops (each settlement listed in NOTES.md).
Known text: Carta 79's Deciffrada, folded to a-z.

**Alignment, statistic, control.** Exactly PREREG-BRO123's (scripts/24_bro123_align.py functions, imported unchanged):
semi-global DP, S = share of keyed cipher tokens aligned to a letter equal to their key.tsv value; 1,000 permutations of
key.tsv's value column (seed 178), DP re-run per permutation (S depends on the code->value assignment, so the control can
differ from the target). Gate: S_real > p99. If FAIL at this N (about 50 tokens): logged as too short / not separated, no
attestation. key.tsv is not edited in either case.

**Copy diff (descriptive, no gate).** `scripts/27_bro178_align.py diff`: token-level difflib between the body run and the
appendix Carta 79 cipher line, written to bro178_diff.tsv.

**Clear prose m0253-m0254 (part b).** One blind Sonnet read of crops m0253_L10, m0253_L11, m0254_L04
(bro178/clear_m0253_m0254.txt): text only, a crib/context source, graded nothing.
