# PREREG-R13-SIENAJ (6 Oct 2026, written 17:45 UTC by date -u, pushed before any scored run)

Job R13-SIENAJ (LANE LANE-RUN13-account-4). Question: does R11-SIENAPOOL's sign-stock overlap of no. 7 with nos. 19 and 9
(pJ 0.001 and 0.003, gate 0.0033) survive when the three letters' signs are labelled by a reader other than Bourdeau's agent J?

**Blind labelling.** The worker labels sign shapes of the cipher passages of no. 7 (DECODE R4796 P1), no. 19 (R4807) and no. 9
(R4798, if the box allows) from line crops (`tools/iiif_lines.py --image ...`), without opening agent J's transcripts (this folder's
`transcripts/no07.tok`, `no19.tok`, Bourdeau's `no09.txt`) or any concordance built on them until the blind inventories are committed.
Exposure already present and disclosed: R11-SIENAPOOL's NOTES table names six of J's shared labels (no. 9: `6~`, `P_`, `DEL`;
no. 19: `S`, `V`, `k`). Per letter the worker writes `r13sienaj/inv_noNN.tsv`: one row per distinct sign shape (shape id, description,
count estimate, a crop/line where seen). Convention: a shape that is a plain Latin letter or Arabic digit is labelled as that letter or
digit (as every agent in R11's matrix did); any other drawn sign gets an id `X<n>`. The concordance between letters (`r13sienaj/
concordance.tsv`) is decided from the crops: same shape -> same id; when in doubt -> different ids (the conservative direction for this
test, since merging inflates overlap). Doubtful merges are listed with a flag; the scored run uses the conservative (unmerged) set.

**Statistic and null (unchanged from PREREG-R11-SIENAPOOL).** J = Jaccard of sign-type inventories, sibling vs no. 7. Null: 2000
curveball swaps (seed 11) of the 16-piece x sign incidence matrix in which the rows for nos. 7, 19 and 9 are replaced by the blind
inventories and all other rows stay as R11 parsed them. Gate unchanged: pJ <= 0.05/15 = 0.0033. B (bigrams) is not computed (only
inventories are read, not sequences). Script: `specs/cheap-tests/siena-concistoro-2308/sign_overlap_pool.py --blind DIR`, output
`results_pool_blind.json`. If no. 9 is not labelled in the box, its row stays agent J's and only no. 19 is scored as blind.

**Reader-bias control (can vary on J).** A single reader can also impose one convention on three letters. As a control the worker also
labels, blind and in the same session, one fasc. 2 piece of a different system that sat below its null in R11 (no. 11, R4800, if on
disk / fetchable in the same login; otherwise none, disclosed). Its row is replaced likewise; it must NOT clear (expected pJ well above
the gate). If it clears, the worker's labelling is merge-biased and the no. 7/19/9 result is void (logged "non-test: reader bias").

**Interpretation.** No. 19 (and 9) clears on blind labels -> overlap survives the agent-J confound; name the pooled nomenclator run
(nos. 7+19+9, R10-SIENA7N family) as next with cost. Does not clear -> the confound is the logged explanation of R11's signal (rule 3:
a "not clearing" on a reader's inventory at this N is conditional on that reader; logged, not a refutation of a shared system).
Secondary (descriptive, after scoring): agreement of the blind no. 7 inventory with agent J's (types matched by shape).
Nothing is read; status stays open.
