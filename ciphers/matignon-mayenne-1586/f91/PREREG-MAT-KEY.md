# PREREG MAT-KEY (15 Oct 2026, account-2 worker, LANE DEFAULT-A2-0810-15)

Written 09:4x UTC 15 Oct 2026 by `date -u`, before any judge score is computed. Brief: `.claude/briefs/runs/2026-10-15-ytbiz-default-0810-jobs.md`
job MAT-KEY. Prior work: `tools/prior_work.py matignon-mayenne-1586 --item-spec 'shelfmark=BnF fr.15572;folio=110-124v,177;sender=Mayenne'
--step-type key --offline` exit 4: plaintext KNOWN (Bourdeau's key and the f.91 period margin decipherment, Tomokiyo l.640, both already used as
sources); the LEAD rows are this lane's own claims and Bourdeau's snapshot (his key.json carries no value for U, T, D2, BOX2: GAPS2 diff, 2 Oct).

## Image check (done first, eye, 3 openapi.bnf.fr requests)
A label is applied only if the same shape carries it in (a) the f.91 reader passes (f.91v block D line 1, reconciled H tokens
`7 T c U t .v. o D2 A B t q 8 h 1 w- t BOX2 ...`), (b) the f.78v reference chart those readers used (Bourdeau's own f.78v labels) and (c) a target
leaf in Bourdeau's transcription (f.124v, canvas 131, lines 1, 2 and 12: `... o g U .v. m ...`, `h d B he M T d E ...`, `... g m BOX2 .v. z .v. o U
... E D2 .v. Ze ...`).

## Key edit (only for labels that pass the image check)
key.tsv rows U=e, T=r, D2=a, BOX2=u, grade S, source "MAT-KA block-held-out gloss test (a948d56a8) + MAT-KEY image check". + (= m) is not
applied (too-short in MAT-KA; the target carries no `+` token). Readings regenerated with `tools/decode_key.py ciphers/matignon-mayenne-1586`;
`--check` must exit 0 after.

## Judge (report, not a gate on the key edit)
`judge_leaves.py --shuffles 20` (fr16 spec judge, per leaf, within-line shuffle control, real_p05/null_p99 at the leaf's N) run on the committed
key (before, output to scratch) and on the edited key (after, committed `openings/leaf_judge.tsv`). Reported per leaf: real score before/after,
shuffle mean before/after, and the margin (real - shuffle mean) before/after. Expected direction if the four values are right: the margin rises
on the leaves carrying most of the 418 changed tokens (f110, f123r, f123v, f124r, f124v, fr15571-f177). A margin that falls on those leaves is
reported as evidence against, not hidden. Note: judge_leaves.py reads M values at their first alternative and drops U, as before; the edit
only adds letters. The judge says "worth a verifier", never "right" (rule 7).
