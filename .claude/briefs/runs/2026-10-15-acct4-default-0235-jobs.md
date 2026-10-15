# LANE DEFAULT-account-4-20261015-0235 jobs (account 4, lane orchestrator session_019RmekEruYMrW91sGQqKSUQ) -- 15 Oct 2026 02:4x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 02:35-12:35 UTC 15 Oct. Gate 0a: no SESSION-SWEEP-account-4 row.
VERIFY-BACKLOG.tsv regenerated 02:40: high rows Birago/ceppo (off limits); low rows birago (off limits), sachsstaatsarchiv N0 (register only),
eckert (googleapis, held by LANE DEFAULT-A2-0209-15 GB-PASS2, 503). Backlog = `next_steps.py --hot-only` runnable rows plus a read-only
scoping pass over 22 hot folders. Excluded: everything LANE DEFAULT-A1-0206-15 and LANE DEFAULT-A2-0209-15 hold (baluze167, fr4712, fr4735,
sforza-duke, pro3055-clinton, mccormick, kaliningrad, erba, clair1161, eckert, thurloe), VIV-KEYSTONE (fr16104/fr16106), BNF-FOCUS holdings
(fr3982, fr3985-3990, no.60), Birago family/ceppo, Armstrong, Debosnys, cipher-lab-private.
Intake gate 02:4x UTC (tools/intake_gate_check.py, exit 0 each): es132-vargas-mexia-1578, fr16142-noailles-constantinople-1571,
fr16045-pisany-rome-1585, lodewijk-van-nassau-1573-74, na-suriname-map-1781 (bl-gualterio-1700 is a key image-check, not deep work).

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-14-acct1-default-1840-jobs.md` (read it in full, and the
files it points to), with these substitutions:
- address every ROOM line "for LANE DEFAULT-A4-0235-15 (account 4)"; export `CIPHERLAB_ACCOUNT=account-4` before any tools/room.py call;
- first actions: `git fetch origin && git checkout -B main origin/main`, `date -u`, read the last 40 ROOM.md lines, post a claim line with
  your box end time; if a live claim (< 6 h, no done) already covers your job, post a flag + done line and stop;
- every claim/halfway/done ROOM line ends "usage: not readable here";
- **images never go into git**: crops, regions and page fetches stay in your session scratchpad; commit only TSV/MD/scripts and, where a
  folder has one, a regen recipe line;
- www.googleapis.com answered 503 at 02:2x-02:3x UTC: no job here uses it;
- openapi.bnf.fr / gallica.bnf.fr are shared with account-1 and VIV workers: ROOM take/release lines, >= 3 s apart, one at a time;
- run `tools/prior_work.py` for your item before the first priced step, and pre-register (PREREG-<job>.md pushed) before any score;
- every other rule there holds unchanged (halfway line, gaps_check on `partial`, decode_key --check where a reading changes, no novelty
  words, no AskUserQuestion, stop at 80% of cap or box, `date -u` before any time, "cost not visible to this session");
- solver jobs: report what was found and where it was not found; do not classify novelty.

## Wave 1 (02:5x UTC 15 Oct)

### ES132-F89 (Opus, cap 4, box 75 min, gallica.bnf.fr or openapi.bnf.fr <= 6 requests): es132-vargas-mexia-1578 two-crop look at the 40 f.89 candidates
Read NOTES.md sections A3V3-ES9396 and ES132-40 (around lines 900-964) and `dup_settled.tsv`. ES132-40 stopped only because no native f.93-95
duplicate image was on disk and its brief excluded Gallica. Refetch the five duplicate regions with the folder's own `./regen_images.sh fetch
f93r` ... `f95r` recipe INTO YOUR SCRATCHPAD (do not commit them), cut both sides with tools/iiif_lines.py exactly as ES132-40's commands do, then
run the look as ES132-40 specified: per candidate, the f.89 crop beside the duplicate crop, with planted decoys (known-settled tokens with a
proposed wrong value) at >= 20% of items; gate pre-registered: decoys rejected >= 80% or the look licenses nothing. Units: about 3 batched Sonnet
vision calls (~13 candidates + decoys each) x 0.6 + 1 reconcile x 0.6 = ~2.4. Apply only candidates the gate licenses, via the folder's existing
settle path; `decode_key.py --check` after. Stop before starting a batch that would cross 80% of cap.

### NOAI-C262 (Opus, cap 5, box 90 min, gallica.bnf.fr or openapi.bnf.fr <= 6; archive.org <= 4): fr16142-noailles-constantinople-1571 c262 lower cipher rows
Remaining gaps items 4 and 8 (NOTES.md ~1714-1732). (a) Cut the c262 cipher rows below c262rc L10 (beside gloss L14-L21) with tools/iiif_lines.py
--follow-slope (region below y 3318, x from ~1380; check the debug overlay before any pass); two blind Sonnet passes against the settled labels
(per-line crops only, never the full canvas), plus one reconcile; extend c262rc_recon.tsv and gloss.tsv only where the two passes agree or the
reconcile settles from the crop; re-run the test0 gate script with --check, reporting the gate number before and after. Units: 2 passes x ~1.2
(rows split into 2 calls each, 0.6/call) + reconcile 0.6 = ~3. If the two passes split on > 10% of signs, stop scoring (TRANSCRIPTION.md), write
focus rows, do not extend the recon. (b) ~1: grep Charrière III (IA full text, be-api or the _djvu.txt already on disk if present) and any IA-held
Lepanto relation for "Relation d'une bataille" / the c231 incipit; log hits and misses.

### PIS-275V (Opus, cap 3, box 60 min, openapi.bnf.fr <= 8): fr16045-pisany-rome-1585 f.275v head L04 end + tile re-cut
NOTES.md Verdict (~line 1090) and ~1089-1112, 1259-1367: the f.275v head L04 step was not run because Gallica 403'd on 9 Oct; openapi.bnf.fr
worked on 13 Oct. Fetch the f.275v head region at native resolution (scratchpad), re-cut the D4-PISA tile instrument at native resolution, and
read L04's end with two blind Sonnet passes on line crops (2 x 0.6) + 1 reconcile (0.6). Apply only agreed/settled signs; decode_key --check.

### LVN-3R (Opus, cap 4, box 75 min, resources.huygens.knaw.nl or the folder's own image host <= 6): lodewijk-van-nassau-1573-74 LVN16-3R per-token read on 4610 p1/p2 and 4611
Verdict gap 3 (NOTES.md ~4509-4561): the LVN16-3R zoomed per-token read with its control has been done on 4616 and 4610 p3 only (raised 4616
C 246 -> 260; FAILed its control on p3, where per-token crops are [retired] -- do NOT repeat p3). Run the same protocol, same control, same gate,
unchanged, on 4610 p1, then p2, then 4611 (stop after any unit whose control fails; report per unit). Units: ~5 Sonnet calls (incl. control)
x 0.6 + 1 reconcile. Apply only tokens the unit's own control licenses (rule 3 per-unit merge paragraph).

### SUR-2061 (Opus, cap 2, box 50 min, service.archief.nl IIIF <= 8): na-suriname-map-1781 VEL2061 clear-text crib hunt
NOTES.md ~3725-3728 and ~4089: den Heijer 2012's 2039 and 2077 pages were read; VEL2061 (NA 2.14.97 inv. 24.2) was planned and cloud-reachable
but not read. Fetch its legend/notes at native resolution (scratchpad), read in clear (one Sonnet call, 0.6 + checker 0.6), and test whether any
clear text matches the unkeyed 2061 tokens' positions or names (pre-registered: a match must hold at >= 2 tokens with no conflicting known
key value). No key edit unless decode_key --try's own control passes for the value class. Report found / not found with the items read.

### GUAL-KEYS (Opus, cap 2, box 50 min, archive.org <= 6): bl-gualterio-1700 image-check of the M key rows
NOTES.md ~259-274: image-check the 122 M rows of the Gualterio key and 33 of the Sicily key against the printed leaves n82, n84, n85, n87
(HMC Stuart Papers vol. 6 on archive.org; keys/build_hmc6_keys.py). One strip pass per leaf on line crops (4 x 0.3 Sonnet), each with >= 5
planted wrong rows as a control; regrade M -> H only where the strip reads the row exactly and the planted rows are caught (>= 80%).
Rebuild the key with the folder's script and its check.

## Wave 2 (refills from 03:0x UTC 15 Oct; intake gate 02:49 UTC exit 0: fr15575-syllabic-1592-95, na-janssens-java-1811, fr5761-election-1519, fr16144-savary-lancosme-1588; antt-linhares-chave status line terminal, gate n/a)

### SYL-CARET (Opus, cap 1.5, box 45 min, disk only): fr15575-syllabic-1592-95 the no.54 legend mark ^ against the f.228 L01-L04 gloss
NOTES.md SYL54-TRY (Suggestion ~line 1146), SYL-1LC, and the last Verdict (~1200). Two --try controls failed (syllable class, single-letter
class). Different instrument: use the leaf's own L01-L04 interlinear gloss (`f228/gloss_v2.tsv`, scored PASS 0.674) as known plaintext at the
`^` positions; pre-register a tally of s vs l (and any other candidate in key_no54_legend.tsv rows 2, 9) at those positions against a
control that tallies the same statistic at gloss positions of H-read single-letter signs shuffled across the leaf (200 seeds). Gate: the
winning value's count beats the control p95 and no conflicting H. A PASS is a C-grade lead for the key row only if the gloss hand is period
(say what NOTES establishes); no decode of L09+ in this job. 0 subagent calls.

### JAV-COLLET (Opus, cap 1.5, box 45 min, disk only): na-janssens-java-1811 Collet 1910 crib values on leaf 188
AUDIT.md ~89-95 "Found, not applied": Collet's two printed sentences give values for 853, 1121, 1173 (l.1) and 381, 125, 1065, 72 (l.10-11).
Test each with `tools/decode_key.py ciphers/na-janssens-java-1811 --try CODE=VALUE` at every occurrence in the pool (and --avalanche where it
helps); pre-register which values you will try before running. A value enters key.tsv as C only where --try's own control passes for that value
class and no occurrence elsewhere contradicts it; otherwise log it M in HYPOTHESES.md, no key edit. Remember Collet paraphrases ("l'état des"
may be the cipher's own text). decode_key --check after any key edit; judge_plaintext per rule 7 if the reading changes.

### ELEC-WALK (Opus, cap 4, box 75 min, gallica.bnf.fr or openapi.bnf.fr <= 20; archive.org <= 2): fr5761-election-1519 name-code plain-copy walk
NOTES.md R9-ELEC and KH2-A sections (from ~597; "Next steps (not run) (1)" at ~621). Walk the fr.5761 ff.54-172 copies whose names are in
cipher at 600 px sheet scale (tools/gallica_folio.py for canvas mapping), list every leaf with a cipher name group, and match its date/letter
against Kluckhohn's printed resolved names (RTA J.R. I, IA bub_gb_0gFoAAAAMAAJ djvu, offsets ~2685183 and ~2827217). Record (group, printed
name, leaf, print page) pairs in a TSV; a value enters key.tsv as C only where >= 2 independent occurrences agree and none conflicts; single
occurrences stay M leads. Census first (<= 12 requests), then at most 8 native line crops for the matched groups (scratchpad only).

### SAV-L14 (Opus, cap 1.5, box 45 min, gallica.bnf.fr or openapi.bnf.fr <= 6): fr16144-savary-lancosme-1588 the c251-252 L14 margin gloss vs Charrière IV
NOTES.md WAIT-PASS-5 (~377-382: "date match only so far"). Read the L14 margin gloss of c251-252 (30 Apr 1586) on native line crops (one Sonnet
read + one checker, 2 x 0.6) and collate it word by word with Charrière IV's printed letter of that date (djvu on disk). Report: is the gloss
a decipherment of a cipher passage that the print gives in clear (then list the cipher span it sits over -- a known-plaintext pair for the
key, no key edit in this job), or unrelated. PX-BRODEC normalisation before any agreement figure.

### LIN-LAB2 (Opus, cap 1, box 40 min, disk first; iiif.archive.org <= 4): antt-linhares-chave second blind labeller on sheet_0255_c3
NOTES.md LIN-CAL section (from ~1751), option (b) at ~1807-1809, PREREG-LINCAL.md and hocr/lincal_score.py. One blind labelling pass by a
different model (Sonnet) under LIN-CAL's pre-registered count rule, then score with lincal_score.py: does 3241315 read "Jus" or "Justa"?
Follow the PREREG's decision rule exactly; one token changes grade only if it says so.
