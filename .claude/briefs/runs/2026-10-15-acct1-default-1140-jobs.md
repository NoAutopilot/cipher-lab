# LANE DEFAULT-account-1-20261015-1140 jobs (account 1, lane orchestrator session_013wJZeHsieHfTMbqKn1r5zR) -- 15 Oct 2026 11:5x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 11:40-21:40 UTC 15 Oct. Gate 0a: SESSION-SWEEP-account-1 stale-claimed since 5 Oct
22:40, proceeded. VERIFY-BACKLOG.tsv (11:14 15 Oct): high rows Birago/ceppo (off limits), rest audit2 on N0/N1 items (known text; not run).
Backlog = `next_steps.py --hot-only` runnable rows + the A1-0740 handoff next list + gap-list steps a survey found runnable without a person.
Excluded: folders held by live DEFAULT-A4-1035-15 (lodewijk-van-nassau-1573-74, clair1161-avis-flandre-1688, baluze167-davaux-1637,
fr4735-monluc-lansac-poland-1573, fr5761-election-1519, fr2980-gramont, matignon-mayenne-1586, oldenbarnevelt-brederode-1605) and
DEFAULT-A2-1109-15 (oldenbarnevelt, harley-287-1587, na-suriname-map-1781, fr3975-vieuville-1587, colbert26-lathuillerie-1644,
thurloe-printed); Birago family, Armstrong, Debosnys, VIV-KEYSTONE (fr16104/fr16105/fr16106), cipher-lab-private. Steps behind an open owner
sort (fr3985/fr3987 no.60 copyist forms, fr7129, fr16142 c262, wvo-hessen) are not briefed.
Intake gate 11:5x UTC (tools/intake_gate_check.py, exit 0 each): mccormick-1999, naf14913-rousseau-venice-1743, na-janssens-java-1811,
sachsstaatsarchiv-manteuffel-1712, pro3055-clinton-1779, es132-vargas-mexia-1578.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-15-acct1-default-0740-jobs.md` (read it in full, and the
files it points to), with these substitutions:
- address every ROOM line "for LANE DEFAULT-A1-1140-15 (account 1)"; export `CIPHERLAB_ACCOUNT=account-1` before any tools/room.py call;
- no www.googleapis.com in this wave; no gallica.bnf.fr (openapi.bnf.fr only, if a job names it);
- each job edits only its own folder (plus a tools/ option and its offline test where the job says so); never key.tsv beyond what a
  passed, pre-registered gate licenses, never status.json, STATUS.md or the owner's published pages.

## Wave 1 (11:5x UTC 15 Oct)

### MCC-CMU (Opus, cap 6, box 90 min, raw.githubusercontent.com or the CMU svn host <= 3 requests, else disk): mccormick-1999 phonetic skeleton
Verdict: "phonetic-skeleton variant of the suffix-mark model from CMUdict with its matched control and the three nulls, ~$6". Read MCC-SUFX,
MCC-JUDGE and MCC-GREGG first and reuse `tools/token_anneal.py --sufx --lexicon --target-nulls` (add a `--phonetic` lexicon option there with an
offline test if needed; no private copy). Fetch CMUdict once (BSD-licensed; keep only a manifest + regen command if it is large, no copy over
5 MB in git). PRE-REGISTER in NOTES before any score: the skeleton mapping, the matched control (synthetic note of the target's 132 tokens built
from the same model) and its read gate, the three nulls (type, type-mark, NCBE-fixed), and the margin rule. Control first: if it does not read,
stop and log "non-test". This is the third lexicon of the same suffix-mark model: if the target does not beat all three nulls on the registered
rule, log the suffix-mark family [retired] under rule 3's third-attempt clause (untested-by-this-tool, not refuted). No vision calls.
NOTES "## MCC-CMU", gaps + Verdict, gaps_check.

### NAF-SPLIT (Opus, cap 3, box 60 min, disk only): naf14913-rousseau-venice-1743 anchored split on f.249/f.250
Gap step: "the same anchored split on f.249/f.250 (501 or another count-matched f.206 C anchor, pins, 722 ti vs i on its segment, own (s)/(g)
controls), pre-registered, script only, ~$2". Read the anchored-split section(s) it copies (the f.206 run and its PREREG) first; pre-register
with a commit before scoring; run the existing script with the new pair (an option, not a copy). A result moves a code grade only as the
registered rule says (count-level C at most, M otherwise). NOTES "## NAF-SPLIT", gaps + Verdict, gaps_check.

### JAV-198 (Opus, cap 3.5, box 60 min, disk first, IIIF host of the folder's manifest <= 6): na-janssens-java-1811 leaf 198 digit cross-check
Gap step: "leaf 198 (raw No.3) against 199-200 (glossed No.3) as a further digit cross-check, ~$2". Read SPLIT-na-janssens-java-1811 (the
leaf-188 method) first. `tools/iiif_lines.py` crops (command pasted before the first subagent call), two blind passes + one reconciliation
(3 units x ~0.7), compare the reconciled digits with the 199-200 copy; any disagreement goes to corrections.tsv only when the image settles it.
No key change. NOTES "## JAV-198", gaps + Verdict, gaps_check.

### MANT-YSHAPE (Opus, cap 2.5, box 45 min, disk only): sachsstaatsarchiv-manteuffel-1712 y-glyph shape-measure
Suggestion in the y-slot section: "a shape-measure (glyph_atlas match of the y-slots against known-4/known-9 exemplars from y49/known.tsv, ~$1
CPU)". Use `tools/glyph_atlas.py match` (with `--shuffle` for its null); pre-register the decision rule (margin over the label-shuffled null,
per slot) before running; a slot is relabelled only if it clears the rule, at M. No vision calls. NOTES "## MANT-YSHAPE", gaps + Verdict,
gaps_check.

### CLIN-3004C (Opus, cap 7, box 90 min, image-uab.canadiana.ca <= 12): pro3055-clinton-1779 3004 pp.232-233
A1-0740 next 4: "B.147 pp.232-233 for 3004" (Images 876-877). Exactly CLIN-3004B's method (read CLIN-3004 and CLIN-3004B and their PREREGs):
B2 gate and permuted-key control registered before decoding, crops command pasted, one blind pass + reconciliation per page. Text-known item
(lane guardrail share): no reading changes. NOTES "## CLIN-3004C", Remaining gaps retry line + Verdict, gaps_check.

### ES132-PLANT (Opus, cap 2.5, box 45 min, disk only): es132-vargas-mexia-1578 planted-tile audit on f.51v/f.52r
AUD2-MANT3's suggestion: "a planted-tile control (`lookalike_pass.py audit --plant`) on these pages would say whether the re-read's A preference
is reading or echo (~$1.5)". Pre-register the plant count and the pass rule; run it; report agreement on planted vs real tiles. Not a fourth
vision pass on f.89. No key or grade change unless the registered rule licenses it. NOTES "## ES132-PLANT", gaps + Verdict, gaps_check.

Wave 1 sessions (11:52 UTC): MCC-CMU session_015gGQAjAqatuChWV8To1faG; NAF-SPLIT session_01UYRnd6TejcfNpkmpDQ8hiK; JAV-198
session_011AnLTbKX7QzvBALUi6hcEm; MANT-YSHAPE session_017vGV8HrZnXWuyvZCeL1aD8; CLIN-3004C session_01Mhfbz8mapFgBBZpzvJXFtJ;
ES132-PLANT session_01917Hod65WgksnoxjsE5rqK.
