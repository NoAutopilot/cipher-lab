# D1-F16142A pre-registration: per-token masked alignment with denser anchors (account 1, 6 Oct 2026, committed before any statistic)

Brief: `.claude/briefs/runs/2026-10-06-account1-default-1240-jobs.md` job D1-F16142A (LANE DEFAULT-account-1-20261006-1240).
Script: `aln/noxalign_dense.py` (imports noxalign.py unchanged). Disk only, 0 requests, 0 subagents. key.tsv unchanged.
Inputs identical to RUN6-NOXALIGN (PREREG-NOXALIGN.md): stream `witness/c262rc_recon.tsv`, label -> pile map, basin consensus key cL,
gloss = decode262.gold() as now committed (leaf-corrected L01-L13; gloss_below_L13.tsv NOT used, no cipher under it).

## Why "hybrid" is redefined
The named step was "Tomokiyo letters on the agreeing labels, basin elsewhere". On an agreeing label the two letters are equal, so that
hybrid is the basin decode itself (no new anchors). The only published-key anchors the basin decode lacks are the five W: word signs
(W:le x19, W:que x5, W:par x2, W:ont, W:qui), which the basin key reads as single letters. Densified decode ("dense"): W: signs spell
their published word (le, que, par, ont, qui), every other mapped sign keeps its basin letter. No letter label takes a Tomokiyo value.

## Procedure (one primary run)
noxalign.recover / settle unchanged except the gap: a masked sign is recovered iff it falls in a difflib 'replace' opcode with
i2-i1 == j2-j1 <= 5 (was 3). Masked labels = the 36 non-W labels (34 letter labels + D1 + N5); W: signs are never masked.

## Statistic
S = number of the 36 masked labels settled to their own basin letter.

## Nulls (each can move S: changes which positions are recovered and/or which letter lands there)
(g) gloss letter order shuffled, 200 draws, random.Random(16142), same procedure;
(k) basin key values permuted across piles (W: signs keep their words), 200 draws, same rng continuing, same procedure.
**PASS iff S > (g) p99 AND S > (k) p99** (strict). Otherwise FAIL, all numbers reported.
Headroom: RUN6-NOXALIGN's nulls sat at p99 0, max 0-1, so the control is not at ceiling; with gap 5 the nulls may rise, and are
recomputed here, not borrowed.

## Reported, not gated (no threshold shopping: these never change the verdict)
- the same three numbers at gap 3 with dense anchors, and at gap 5 with basin-only anchors (which ingredient moved S);
- per disagreeing label (basin != Tomokiyo letter): recovered n, settled letter, gloss_says basin/tomokiyo/neither/none;
- count of letter labels settled to their Tomokiyo letter under dense anchors.

## Grades
FAIL: all tokens stay M. PASS: a sign may move to S (cryptanalytic, with control) only if its label is settled to its basin letter AND
that sign's own recovered gloss letter equals it; every other sign stays M. The gloss is a period interlinear, but the mapping of a
reader label to a pile is ours, so S not C. Conditional on one reconciler's labels, RUN2-NXATL's unchecked alignment and the owner's merges.
