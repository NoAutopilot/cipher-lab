# PREREG-SUP-PISANY (20 Oct 2026, written 02:2x UTC by date -u, pushed in its own commit before any reader call)

Job: SUP-PISANY, brief .claude/briefs/runs/2026-10-20-acct4-research-director-28.md (account 2). The folder's own named next step
(NOTES.md "## Escalation", RUN6-PIS verdict line): "the f.244r overlap double reads (L06 p27-p30, L08 p25-p26) as a geometry-judged
transcription fix". A transcription question (delete tokens a double read put in tx86), never a key edit: key86.tsv unchanged.

## Why a different instrument (rule 3, third-attempt clause)
PISA-MERGE (12 Oct) gated these two deletions on nw_score against the Colbert copy: G-OV6 FAIL G4 (share 0.075), G-OV8 FAIL G3a, and noted
G3a "fails this shape by design" for a repeat. A score against a copy with err 0.284 is a poor instrument for whether a sign was read twice.
This job does not re-run that score as a gate; it decides from geometry and blind sight. The score is not re-run at all.

## Geometry (measured before this PREREG, no reader)
images/f244r_L0N_s1.jpg and _s2.jpg (tools/iiif_lines.py outputs of earlier jobs; e.g. L06 s2 from
https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060906j/f500/600,2680,2960,1460/full/0/native.jpg, box [1960,3497,3560,3714]) are 1600 px
strips; normalised correlation of s1[:, off:1600] with s2[:, 0:1600-off] over off 1300-1445 peaks at off 1360 with r = 1.0000 on all
nine lines: the band s1 x 1360-1600 is the same pixels as s2 x 0-240. Any sign in that band is visible in both strips, so a strip-by-strip
transcription can read it twice. Crops for the readers: PIL sub-crops of those committed line crops (sup_pisany/make_crops in NOTES),
no network: s1 x 1240-1600, s2 x 0-360, and a seamless stitched window x 1000-1960 (s1 to 1360, then s2) in which nothing can repeat.

## Readers (4 blind Opus calls; 2 per span; plan sup_pisany/plan.json, seeds 20261020+r)
Each call sees only: three labelled pairs (left = end of a strip, right = start of a strip) in shuffled order -- the target pair, a
same-line control pair (another f.244r line, truth by the geometry above: a shared run exists) and a decoy pair (s1 end of one line with
s2 start of a different line, truth: nothing shared) -- and the target's stitched window. No key, no labels, no transcription, no hint of
which pair is which or what is expected. Per pair the reader answers: does the right image begin with signs that are the same physical
ink as the end of the left image (yes/no), and if yes, the shared run as shape descriptions. For the window: transcribe the signs left to
right as shape descriptions, and say whether any group of 2+ signs occurs twice in a row.
R1, R2: L06 (window x 1000-1960). R3, R4: L08.

## GATE per span (L06 = G-OV6, L08 = G-OV8)
- GK: in BOTH calls for the span, the same-line control answered yes and the decoy answered no (2/2 per call). A miss in either call
  makes the span a non-test (logged, nothing deleted).
- GT: in BOTH calls, the target pair answered yes, and the shared run named includes the group in question (L06: a q-like sign, a round o,
  a crossed p, a d-like sign = tx86 p22-p26 / p27-p30; L08: an a and a lambda = p23-p24 / p25-p26), judged by this worker in the
  reconciliation against the two readings of tx86 before deletion.
- GW: in BOTH calls the stitched window shows that group once (no repeat reported, and the transcribed window contains it once).
PASS = GK and GT and GW. On PASS the second copy is deleted (L06 p27-p30 T14 T30 T45 T18; L08 p25-p26 T26 T37 -- the same deletions
PISA-MERGE named, the first copy kept because it carries the finer reads: ?[qcross] T30 T19 ?[tcross] T18, and RS244's committed T19), by
sup_pisany/apply_sup.py from a byte-identical copy tx86/ciphertext_f244r_preSUP.tsv, asserting each label; then decode_key.py re-decode,
t31_grades.py --grade --page f244r, judge_plaintext (descriptive), every apply_* --check. FAIL or non-test: nothing changes.
Positions: 1-based counting '/', as tx86, pisa_244/locate.tsv and PISA-MERGE.

## Decision rule (pushed 8d22753ee)
PASS on a span -> commit that deletion, regenerate the f.244r reading and grades, flag for a verifier (AUDIT.md not edited).
FAIL -> the overlap double read stays in tx86, logged; the step is [retired] for this instrument too and the next is a person's look.
Non-test (GK miss) -> logged, nothing deleted; the same next.
Cost: vision calls: 4 x USD 0.5 + 1 reconciliation (this worker) = 2.5.

## Decision
(Belief and Would-change restate the gate pushed in 8d22753ee before any reader call; the five-line form is added after the run, the gate unchanged.)
Belief: tx86 f.244r L06 p27-p30 and L08 p25-p26 are second reads of signs in the s1/s2 overlap band, and blind sight plus geometry can show it.
Would change it: GK 2/2 in both calls per span, the target pair shared with a run including the q-o-p-d (L06) / a-lambda (L08) group, and the stitched window showing the group once, in both calls.
Observed: geometry r = 1.0000 at offset 1360 on 9/9 lines; GK 2/2 in all 4 calls (8/8 control answers right); target shared 4/4; window group once 4/4 (L06 "/ q o p d h s t o d lambda u", L08 "tau varpi v a lambda q y"); but the shared run is "o, crossed p, d, h" (R1, R2) and "tau, varpi, v, a" (R3, R4): the q and the lambda lie just outside the 240 px band (worker's look agrees) -> GT FAIL both spans.
Decision: stop -- FAIL as registered; nothing deleted; tx86, key86, readings and grades unchanged; not re-gated after seeing the reads.
Lesson: the GT clause assumed the whole duplicated group sits in the overlap band; a double read can straddle the band edge (the transcriber re-reads a sign cut at the strip edge), so a gate on 'which signs are shared' must use the band's measured contents, not the transcription's duplicated tokens; the window reading (GW) is the instrument that bears on the deletion.
