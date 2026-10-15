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

## Wave 2 (12:3x UTC 15 Oct)
Wave 1 results: NAF-SPLIT 2.14 N (722 undecided), JAV-198 3.10 D (168/171), MANT-YSHAPE 2.12 Q (NON-TEST: no digit boxes -- the brief's
error), CLIN-3004C 4.03 D (p.232 PASS, p.233 non-test), ES132-PLANT 3.17 D- (PASS 26/27; 1.27x: cap 2.5 was under the Opus floor + one call).
Intake gate 12:3x UTC (exit 0 each): fr16045-pisany-rome-1585, fr16144-savary-lancosme-1588 (es132, manteuffel passed at 11:5x).
Cap sizing: an Opus worker's floor is ~2 before any look; no cap below 3 in this wave.

### ES132-P52 (Opus, cap 3.5, box 45 min, disk only): es132-vargas-mexia-1578 planted-tile audit on f.52r
ES132-PLANT's next: "same PREREG on f.52r, ~2.5". Read ES132-PLANT and PREREG faac3f749; register the f.52r addendum (plant count, gate) by
commit before the call; one call; score by the registered rule. No key, grade or reading change unless licensed. NOTES "## ES132-P52",
gaps + Verdict, gaps_check.

### SAV-GLOSS (Opus, cap 4, box 60 min, openapi.bnf.fr <= 6): fr16144-savary-lancosme-1588 c251-252 margin gloss, two blind passes
SAV-L14's suggestion: "a two-pass blind transcription of the c251-252 margin gloss on wider native crops (left edge at pct x=0), ~2 Sonnet
passes + 1 reconcile, ~$2, then add it beside c380's gloss as alignment input for the table recovery gap". Crops command pasted before the first
subagent call; the gloss is clear French (no sign values involved); 2 Sonnet passes + 1 reconciliation = 3 units. Write the gloss TSV beside
c380's gloss; do NOT run the alignment (it waits on the owner's sort of c370-375/c380 labels). NOTES "## SAV-GLOSS", gaps + Verdict,
gaps_check. openapi.bnf.fr take/release lines.

### PIS-FA (Opus, cap 3, box 45 min, archivesetmanuscrits.bnf.fr <= 15, openapi.bnf.fr <= 4): fr16045-pisany-rome-1585 two catalogue lookups
Gap steps: "18 June 1588 letters (fr.16046 ff.165, 179) ... next: Brienne 354-356 for June 1588, catalogue lookup first, ~$1" and "Originals of
the Dec 1586-Feb 1587 and Apr-Dec 1587 dispatches ... next: BnF finding aid search for other Pisany volumes (fr. or Cinq Cents de Colbert),
~$1". Catalogue only: find the records, quote shelfmark, folio range, date and digitised flag/ark; at most 4 thumbnail looks to confirm a hit
holds Pisany cipher. No transcription, no decode. NOTES "## PIS-FA", gaps + Verdict, gaps_check.

### MANT-V66 (verifier, Opus, cap 3, box 40 min, disk only): sachsstaatsarchiv-manteuffel-1712 66 = Alefeld on 0151
NOTES: "Next: verifier look at 66 = Alefeld on 0151 vs key.tsv 66 (~$0.5, disk)". You are a verifier, not the solver: read the section that
proposed it, check the 0151 crop(s) and key.tsv row 66 and every other occurrence of 66 with `tools/decode_key.py <t> --try 66=...` (its
control), rule agree / disagree / undecided with the evidence; a key change only if the rule licenses it, graded as decode_key says. Write the
ruling in AUDIT.md (a dated "MANT-V66" section) and a one-line pointer in NOTES. No novelty class change.

### MANT-CUT (Opus, cap 4, box 60 min, disk only): sachsstaatsarchiv-manteuffel-1712 digit cutter, then the MANT-YSHAPE rule
MANT-YSHAPE was a NON-TEST: the y-slot crops carry whole groups and glyph_atlas's segmenter located the 4|9 digit in <= 8/69 clean slots. Add a
digit-cutter option to `tools/glyph_atlas.py` (group crop + digit index -> digit box by column ink profile; offline test in tools/tests/) --
no private copy. Validate it first on the known-4/known-9 exemplars of y49/known.tsv (it must locate >= 80% of them, by your eye on a contact
sheet, else stop and log the cutter as failing). Then run MANT-YSHAPE's pre-registered rule unchanged on the 8 conflict slots. No vision
subagent beyond one contact-sheet check. NOTES "## MANT-CUT", gaps + Verdict, gaps_check; SYSTEM.md line for the option
(tools/system_map_check.py passes).

Wave 2 sessions (12:27 UTC): ES132-P52 session_01VmuqNnHHNZGbHx1FE5eotd; SAV-GLOSS session_01PDDCRgPMF6ae1cQKfL3rCp; PIS-FA
session_017yochWwdis2b16tH7JUPP3; MANT-V66 session_01QSAS2S78gaxX3Zjb8eHh3D; MANT-CUT session_01Wwrz39JiiXHYLBkuQy4MKQ. MCC-CMU (wave 1) still live.
