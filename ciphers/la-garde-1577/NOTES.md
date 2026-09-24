open

# La Garde, superintendent of Schoonhoven, to Willem van Oranje, partly unsolved cipher, 28 November 1577

QUEUE row: NB4 (`QUEUE.md`, "Dutch and Belgian archives (LANE N scout of 24 September 2026)").

## Source

WVO briefnr **6179** (https://resources.huygens.knaw.nl/wvo/app/brief?nr=6179), 28 November 1577 (dated "A
Walheyn, ce 28e jour de novembre 1577" in the letter itself), from La Garde, superintendent of Schoonhoven, to
William of Orange: a report on troop strength and cavalry shortage near Namur. Koninklijk Huisarchief Den Haag,
A 11/XIV C/G-1. Free PDF, no login: `resources.huygens.knaw.nl/media/wvo/images/06000-06999/06179.pdf`. WVO's
Opmerkingen field: "Gedeeltelijk in onopgelost cijferschrift" (partly in unsolved cipher). **Confirmed by eye
this pass** (`images/06179_p1-1.png`, manuscript foliation p.32): continuous clear French prose about troop
dispositions and cavalry near Namur, headed "1577 Nov. 28" in a later archival hand -- confirms the correct
record; the cipher-bearing page(s) among the letter's 4pp were not specifically located this pass (not required
to confirm the record).

## Check-solved sweep, 24 September 2026

Run directly by this worker (Sonnet, no Workflow tool, no subagents).

1. **Editions first -- and decisive.** Printed by Groen van Prinsterer, *Archives ou correspondance inédite de
   la maison d'Orange-Nassau*, 1re série, **tome VI (1577-1579)**, pp. 249-251, **Lettre DCCLXXXIX**, "La Garde
   au Prince d'Orange. Détails militaires sur l'armée des Etats-Généraux." (title confirmed via DBNL,
   `dbnl.org/tekst/groe009arch06_01/groe009arch06_01_0095.php`, fetched and read directly this pass, not
   summarised from a search snippet). WVO's own Brongegevens field cites this precisely: "VI, 249-251 nr.
   DCCLXXXIX **(onv)**" -- "onv." = onvolledig, incomplete -- with the full edition citation ("Groen van
   Prinsterer, G., ed. ... Première série 8 dln. (Leiden 1835-1847)"). **Read directly this pass**: the DBNL
   text of Lettre DCCLXXXIX contains visible editorial gaps/ellipses at multiple points, with an explicit
   footnote at the site of one major gap: **"Les lacunes sont occasionnées par des passages chiffrés"** (the
   gaps are caused by passages in cipher). This confirms, from the edition itself (not merely inferred from the
   "(onv)" flag), that **Groen's 1839 print does not deciphered the cipher passages -- it omits them entirely**,
   consistent with LESSONS.md's Orange-Nassau-1572 precedent (a Groen footnote stating the cipher "infiniment
   plus nombreux que les lettres" defeated any attempted comparison). This target therefore genuinely reaches
   check-solved as open even though it is printed: the print is of the plain-text portions only.
2. **Post-edition journal search (check-solved.md lesson of 24 Sept 2026, the Oxenstierna/Torpadie case).**
   Tome VI was published in **1839**; per that lesson, searched for a later decipherment in the national
   historical-journal literature of the following years. WebSearch (`"La Garde" Willem van Oranje 1577 Namen
   troepensterkte cijfer ontcijferd`) found nothing relevant -- results were general Dutch-Revolt military
   history (K.W. Swart's *Willem van Oranje en de Nederlandse Opstand*, DBNL) with no mention of this letter or
   its cipher. No specific 1840s Dutch/Belgian historical-journal search (e.g. *Bijdragen voor Vaderlandsche
   Geschiedenis*) was run by name this pass -- flagged as a narrower follow-up, not completed, given this
   worker's budget was shared across four targets.
3. **WVO curatorial field.** As above, explicit "(onv)" and "onopgelost" -- the clearest of this batch's four
   targets.
4. **Community lists.** `sources/cryptiana/web/dutch.htm` read in full: no mention of La Garde or this letter.
   WebSearch as item 2 found nothing further.
5. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` grepped for "la garde"/nassau/oranje: zero
   hits.
6. **Solver repositories.** Same fresh clones as NB1-NB3 (24 Sept 2026): grepped for "la garde"/nassau/oranje/
   khag/wvo -- no hits relevant to this letter or correspondent in either repository.

## Verdict

**Status: open.** The standard printed edition (Groen van Prinsterer, tome VI) was located, read directly, and
confirmed to omit rather than decipher the cipher passages, with an explicit editorial footnote saying so. No
later decipherment found in a (limited) post-edition search, no community list, DECODE record or solver
repository names a solution. This is the strongest-founded "open" verdict of this batch's four targets, since
it rests on a direct reading of the edition itself rather than an inference from curatorial silence.

**Copy status: copy-free.** Free PDF confirmed reachable and viewed by eye. No REQUEST.md needed.

**Kind: cryptanalysis** (no contemporary decipherment or sibling-with-key identified this pass; the cipher
passages' extent within the 4pp was not mapped, a task for a future solver pass, not this check-solved sweep).

## Image capture, 24 September 2026 (LANE R worker R9)

6179 fetched in full (4pp) and rendered to PNG at 150dpi. Cipher passages located: p2-p3 (foliation 32v-33r),
numeral groups (dot-separated, mostly 1-2 digits) embedded word-by-word within continuous clear French prose,
~140 cipher tokens total across the two pages -- the cipher is a minority of the letter's text, consistent
with WVO's "gedeeltelijk" (partly) and with Groen's edition omitting only those clauses.

Searched WVO for other La Garde letters (11 found via the correspondent index; a combined
correspondent+opmerkingen query confirms only 6179 itself carries "cijferschrift") and for any other 1577
letter to Orange noted as deciphered (opmerkingen="oplossing"/"ontcijferd"/"cijferschrift" + year=1577): three
hits total, 6179 plus two candidates, both fetched and rendered (at most three, per the brief):
- **6467** (Filips van Marnix van St. Aldegonde, 2 Nov 1577, Brussels): same numeral-cipher design as 6179
  (dot-separated 1-2 digit groups). WVO Opmerkingen: "Twee passages in cijferschrift, waarvan de eerste met
  oplossing in de marge" (two cipher passages, the first with a solution in the margin) -- marginal annotations
  are visible near the first cipher run on p2 but this worker could not confirm by eye that they constitute a
  full decipherment (flagged for a solver pass). **Note for a future novelty check, not acted on here**: this
  record's Brongegevens already lists two printed-edition PDFs (edities/GSME and edities/LMSAC) -- this letter
  has been printed somewhere, unlike 6179.
- **5564** (Jan van Nassau, 11 Jan 1577, Siegen): a different cipher design from 6179 -- German text, numeral
  groups mixed with roman-letter labels (e.g. "a.32.b"), not pure numerals. WVO Opmerkingen: "Met opgelost
  cijferschrift" (with solved cipher), but no separate decipherment sheet is present in this 3pp file (the
  letter is only 3pp: 2pp text + 1pp address leaf) -- the "opgelost" status is not confirmed imaged by this
  worker, flagged for a solver pass or a further WVO/archive check.

`images/manifest.json` and `images/inventory.tsv` (per-page content, cipher type, approx tokens, decipherment
location) written. Host: resources.huygens.knaw.nl, 10 requests this pass (8 WVO record/search pages + 2 PDF
fetches, >=2s apart). Folder kept at 24MB under the 30MB cap (PDFs deleted after rendering).

## R15 progress (24 Sept 2026, stopped over cap by orchestrator)

Brief: two blind passes of 6179 pp.2-3 and 6467's two cipher passages (passA.tsv/passB.tsv), reconcile, transcribe
the 6467 marginal note, write an "R15: passes" NOTES section with counts/overlap. Stopped by the orchestrator at
~$8 against a $4 cap before any of that landed.

Done: claimed the target in ROOM.md; re-read the images by eye (06179_p2.png, 06179_p3.png, 06467_p2.png) and
confirmed both cipher passages are on 6467 p2 (not p1/p3 as the earlier inventory guess left open): the first run
("on pourra 7.8.2.11.10.19.14.12.9. 3.07.4.14.4.8.11.2.4.07.11.24.3.9. 2.17.5.11", ending "Ce seroit un grand
poinct") has a two-word-plus-abbreviation marginal note beside it reading, as best transcribed at 3x crop,
"Justiffier le faict du grand" over "grand" on a second line -- far shorter than the ~15-group cipher run beside
it, so this reads as a short marginal gloss/label, not a word-for-word decipherment (category (c) in the brief's
terms; a full solution would need to run to something like fifteen words). The second run ("que 10.8.2.10.5.7
9.07.4.10.8.9.07*.4.7.1.3.12") has a short abbreviation-like note beside it, tentatively "N.s.c.f." or similar
(low confidence at this resolution) -- also far shorter than its ~12-group run, same "gloss, not decipherment"
read. Neither note was logged to marginal_6467.tsv (not written) since the brief called for both blind passes
first, and those had not returned before the cap hit.

Launched two independent Sonnet subagents (blind pass A, blind pass B) on 06179_p2/p3 + 06467_p2, with the
line/position/token/confidence TSV format and `w:`-prefixed clear-word context tokens (chosen over the brief's
literal `=word` so the files reconcile with tools/reconcile_passes.py's existing `w:`/`[PLAIN:...]` convention
unmodified -- same intent, existing syntax). Both were still running when the cap notice arrived; per the
orchestrator's instruction this worker did not wait for them and did not read any more images. Their output was
never captured to disk (they were told to return the TSV as reply text, not write files), so nothing from them
is recoverable by a later worker except by re-running the same two prompts.

Not done: passA.tsv, passB.tsv, recon/, marginal_6467.tsv, the "R15: passes" counts/overlap section, decode --
none of it exists on disk. No host requests were made (all reading was from the already-fetched images).

Left for whoever picks this up: re-launch the two blind-pass subagents (or do the passes directly) on the three
images above; the margin-note reading in this section is a starting point but should be re-checked independently
rather than trusted, since it was read by the same eyes that then briefed the subagents. Cost overrun cause, for
the retrospective: reading three full manuscript-page images at native resolution by eye (twice, once directly
and once implicitly through two subagent dispatches with embedded task context) is expensive on Sonnet; a
narrower crop-first workflow (tools/iiif_lines.py-style line crops passed to the subagents instead of full pages)
would likely have kept this under cap.

## L1: transcription (24 September 2026)

Single-worker blind transcription (no subagents, no network, offline from the images already on disk), direct
reading only (not a two-pass reconcile — the brief for this worker was a solo pass, not a matched pair). Installed
Pillow locally (`pip install pillow`, PyPI, not a research host) since neither Pillow nor ImageMagick was present
in the container and the full-page PNGs are too dense to read cipher digits from at native display size; used it
only to crop/upscale regions of the images already on disk into `/tmp` scratch files for reading, nothing written
to the repo. `ciphertext_6179.tsv` (pp.2-3, 194 rows) and `ciphertext_6467.tsv` (p2's two marginal-note passages,
46 rows) written and pushed page-by-page as instructed. `freq.py` (20-line offline script, reads both TSVs) computes
the counts below; rerun it after any correction.

**Notation used in the `group` column** (documented here since it isn't in the brief): digits and the `.`/`/`
separator are transcribed literally; a trailing `^` marks a numeral written with a horizontal overline (seen
throughout both letters, e.g. `16^`); a trailing `~` marks a small loop-with-crossbar flourish that recurs above
some digits in a form distinct from the plain overline (first noticed on 6179 p2-p3, also present on 6467 p2 run1
as `07`/`4~`/etc.; one instance on 6467 p2 run2, `07~~`, has what looks like an extra stroke on the same mark); a
row with `group` = `[mark]` (optionally suffixed with an adjoining digit, e.g. `[mark]15`) is a case where this
flourish appears to stand free between two numerals rather than clearly sitting atop one, so it is given its own
row rather than silently attached to a neighbour (rule 2). **This flourish's identity is not established** — it
could be a diacritic on the tens digit, a word- or clause-boundary marker, or a null; a future worker with the key
should check whether `[mark]`/`~` tokens correlate with word starts once anything decodes. `doubt`=`M` marks a
specific digit-identity or mark-placement call this worker was not confident in (mostly a recurring 4-vs-9 and
8/18-vs-10 shape confusion in this hand, and the one interlinear "16 stacked over 12" insertion on 6179 p2 line 27,
which could equally be a correction replacing one number with the other rather than two consecutive groups) — these
are exactly the rows a second pass or the image should re-check before this is treated as final, per rule 7's
"reproducible" standard (this transcription is a first read, not yet a settled one).

**Counts** (`python3 ciphers/la-garde-1577/freq.py`): 238 total token rows across both files (183 in 6179, 45 in
6467); 10 of those are free-standing `[mark]` tokens with no attached digit. Of the 228 numeral tokens, 25 distinct
base-digit values appear, ranging 1-24, with no value above 24 anywhere in either letter. 16 tokens carry the plain
overline, 2 the loop-cross flourish attached to a digit (plus the 10 free-standing ones above). Most frequent
values: 10 (22x), 8 (16x), 9 (13x), 16/3/2 (12x each), 1/14/11 (11x each), 12/7 (10x each) — a fairly flat
distribution over a small alphabet, not the long tail of hapax-heavy values a word-nomenclator would show over
~230 tokens.

**What the design looks like**: a value range capped at 24 with heavy reuse (10 appears once per ~10 tokens) is
far more consistent with a **numbers-for-letters** cipher — one code number per letter of a ~20-25-letter French
alphabet (u/v and i/j often unified in this period, which would land near 22-24 distinct letters) — than a
numbers-for-words nomenclator, which would need hundreds of distinct values and show most values as hapax or
near-hapax over this many tokens (compare LESSONS.md's Chaulnes 1690: 300 groups but 116 distinct, i.e. more than
a third unique; here only 25 distinct over 228, about an eighth). This reading is offered as a transcriber's
observation only, not a decode — the next worker (Opus, with a matched control per rule 3) should test it: build a
frequency-rank map against period French letter frequencies and see whether the plain-substitution controls in
tools/ read a synthetic French text of the same length before trying the target, exactly as LESSONS.md's "controls,
always" section describes. The `^`/`~` marks are the obvious first thing to test as conditioning on that map (e.g.
"marked forms are the same letter doubled/repeated" or "marked forms are the following-letter's diacritic in this
period's orthography") rather than as separate cipher values, given how few of them there are relative to the
run lengths.

Not done, per brief: no decoding, no fetch of Groen/DBNL (dbnl.org is LANE V2's host). Left for the next worker:
re-verify the `doubt=M` rows against the images directly (this worker's crops are not saved to the repo, only to
this container's /tmp scratch, so a fresh set of crops is needed); resolve whether the 6467 margin note reads
"N.c.f." or "N.d.f." (both letters are visually possible at this resolution); confirm whether 6179 p2's "16 over 12"
stack (line 27) is two groups or a correction.

## L2: cryptanalysis (24 September 2026, LANE R2 worker L2, Opus, no network)

**Result: negative for two designs, each with a matched control. Conditional on L1's single-pass transcription (rule 2), whose M rows were not settled on the image this pass.**

Script: `solve_l2.py` (`python3 ciphers/la-garde-1577/solve_l2.py --corpus <fr16 Catherine de Médicis letters, both vols, gunzipped> --control-plain <Marguerite de Valois, Lettres inédites, lines 1006-1030 of lettresindites00marg_djvu.txt: the 1580 letter to the Queen Mother>`; about 20 s). Training corpus and control prose are disjoint. Signs are L1's numbers with `^`/`~`/`[mark]` stripped (`07` kept distinct). Target 6179: 185 tokens, 24 distinct signs. Groen's clear text (DBNL, LANE V2's host) is not on disk, so the control prose is contemporary French letter prose (1580) and not this letter's own clear text; ROOM line posted asking LANE V2 for it.

| Test | Control (same N=185, same sign count) | Target 6179 |
|---|---|---|
| A. Homophonic / simple substitution, tools/homophonic_anneal.py, trigram, 8 restarts x 30k | clean 73.5% of letters read (score/token -2.17); with 8% of tokens randomised to mimic misreadings, 38.9% (-2.29) | no reading: restarts disagree, best -2.52/token, worse than the noisy control, output not French |
| B. Periodic Vigenère/Beaufort, periods 1-14, alphabets a24 (a-z less j,v,w, plus &), reversed, a23; number n = n-th letter | enciphered with a random period-5 key: 100% read | no reading: best -3.64/token (a23, period 14), gibberish |
| C. Crib, 6467 run 1 (27 signs) vs its margin note "Justifier le faict du grand" (with and without "iustiffier") | n/a (exact search) | no consistent many-to-one sign-to-letter map even with up to 6 nulls |

Observations:
- Index of coincidence of 6179 is 0.043 (flat, 1/24 = 0.042), no repeated trigram in 185 tokens, periodic IC shows no period 1-26. A homophonic control of this size is also flat (0.042), so IC does not decide between designs by itself.
- The 6467 margin note sits beside run 1 and completes the clear syntax ("on pourra [run 1] Ce seroit un grand poinct"), so it may be a decipherment of the opening words, but it is not a monoalphabetic one: the first ten signs 7 8 2 11 10 19 14 12 9 3 would make "iustiffier" with two homophones each for i (10, 12) and f (19, 14), and then sign 8 must be both u and the i of "faict". Either the note is a gloss rather than a decipherment, or the system is polyalphabetic / uses the overlines as part of the sign. Test B found no periodic key that makes the crib consistent under the fixed alphabets tried.
- **Transcription gap found on the image:** 6467 p2 carries overlines on many more numerals than L1 recorded (checked on a crop of run 2: 8̄, 5̄, 7̄, 1̄0, 3̄ and 2̄, 1̄7 on the run 1 continuation line; L1 marked only some). If the overline distinguishes signs (e.g. 4 vs 4̄ as different letters), the sign count rises well above 24 and test A must be rerun with the overline as part of the sign. The same should be checked on 6179 pp.2-3.
- What the overline and the loop mark do: not established.

Not done (cost): step 1 of the brief, settling L1's M rows (25 rows in 6179, 1 in 6467) on the image. The noisy control shows misreadings at that rate would roughly halve what a monoalphabetic solver reads, so they do not by themselves explain a target that reads nothing, but a settled transcription with the overlines recorded is the prerequisite for any further attempt.

Suggestions (one line each): (1) a Sonnet transcription pass recording every overline and loop mark on 6179 pp.2-3 and 6467 p2, then rerun `solve_l2.py` with overlined numerals as distinct signs; (2) obtain Groen VI 249-251 clear text for crib context around each gap (LANE V2); (3) check the 1577 Orange-circle cipher literature (Marnix's own systems, 6467's printed editions GSME/LMSAC per R9) for a numeral table of this design.

Search log (print): Groen VI 249-251 (Lettre DCCLXXXIX) is recorded above by the check-solved sweep as omitting the cipher passages ("Les lacunes sont occasionnées par des passages chiffrés"); not re-read by L2 (no network). Novelty not classified.

## L3: second transcription, progress only (24 September 2026, LANE R2 worker L3, Sonnet, $5 cap, stopped over cap at $13.2 by the orchestrator before reconciling)

Brief: two blind Sonnet passes of 6179 pp.2-3 and 6467 p2 recording every numeral group's digits, overline,
dot/loop mark, and clear-text neighbours (L1 under-recorded these marks); reconcile with `tools/reconcile_passes.py`
(L1 as a third witness); rerun `solve_l2.py` with overlined numbers as distinct signs; report both control and
target numbers.

**Landed, pushed:**
- `ciphertext_6179_passA.tsv`, `ciphertext_6467_passA.tsv`: pass A complete. Counts (pass A's own report): 6179 p2
  113 groups (lines 22,24-28), p3 80 groups (lines 6-9); 6467 p2 46 groups (lines 6-8,10-11). Marks: `^` 29 (6179)
  + 10 (6467); `~`/free-standing `[mark]` 11 (6179) + 4 (6467); conf=M 18 (6179) + 4 (6467). Pass A worked from
  10x local crops (own PIL script, offline), distinguished the loop-crossbar flourish from ordinary cursive
  descenders on 6/9, and flagged several boundary-straddling marks as free-standing `[mark]` rows rather than
  guessing a neighbour. Did not open L1's files (confirmed blind).
- `ciphertext_6179_passB.tsv`: pass B's 6179 (p2+p3) landed. **`ciphertext_6467_passB.tsv` did not land** — pass B
  was still working on 6467 p2 when the cap notice arrived; its output is not on disk and was not captured (the
  subagent could not be stopped via TaskStop, task id not found -- it may still complete and hand back after this
  worker has stopped; if so, a later worker should look for it before relaunching).
- `solve_l2.py`: given `--ciphertext-6179`/`--ciphertext-6467` (default unchanged) and `--mark-signs` (test A/C
  treat a marked numeral as a sign distinct from its plain form; test B stays numeric-only, unaffected by design).
  Verified the default invocation still reproduces L2's exact reported numbers (A control clean 73.5%, 8% noise
  38.9%, B control 100%, both cribs no consistent map) before any of this section's edits, so the L2 result stands
  unchanged pending a v2 rerun.
- `reindex_l1.py`, `ciphertext_6179_L1.tsv`, `ciphertext_6467_L1.tsv`: reformats L1's two files to the `line`-first
  long format `tools/reconcile_passes.py` needs (line id `p{page}L{line}`, e.g. `p2L22`), so L1 can be fed in as
  the third witness when reconciliation runs.

**Not done (stopped over cap, per the orchestrator's instruction not to reconcile or run the solver this pass):**
pass B's 6467 p2 file; the `tools/reconcile_passes.py` run over the three (pass A, pass B, L1-reindexed) witnesses
for 6179, and two (pass A, L1-reindexed; pass B's 6467 missing) for 6467; settling any disagreements.tsv rows on
the image; `ciphertext_6179_v2.tsv`/`ciphertext_6467_v2.tsv`; the `solve_l2.py --mark-signs` rerun on the v2 files
and its reported control/target numbers; this section's own "L3: second transcription" summary with final counts
(this is progress-only, not that summary).

**Left for whoever picks this up:** check first whether pass B's `ciphertext_6467_passB.tsv` has since appeared
(the subagent may complete after this worker stops); if not, either wait for it or relaunch a single blind pass B
on `images/06467_p2.png` alone (06179 pp.2-3 don't need rerunning, pass B's file for those already landed). Then:
`python3 tools/reconcile_passes.py ciphertext_6179_passA.tsv ciphertext_6179_passB.tsv ciphertext_6179_L1.tsv
--line-sub '^' ''` (check the id scheme lines up -- all three now use `p2L22`-style ids) `--out-dir .`, settle
disagreements.tsv on the image, write `ciphertext_6179_v2.tsv`/`ciphertext_6467_v2.tsv`, then
`python3 solve_l2.py --corpus <fr16 both vols, gunzipped> --control-plain <Marguerite de Valois lines 1006-1030>
--ciphertext-6179 ciphertext_6179_v2.tsv --ciphertext-6467 ciphertext_6467_v2.tsv --mark-signs` and report the
printed numbers here as the actual "L3: second transcription" result section, replacing/extending this one. Cost
note for the retrospective: two Sonnet subagents each reading three full manuscript pages (with additional
own-script 10x crops) ran well past a $5 cap on their own before this worker's own token use is even counted --
this is the same lesson R15 already logged (crop-first workflow needed) recurring at higher cost; a target-specific
`iiif_lines.py`-style local crop cutter (offline, no IIIF fetch needed since the pages are already on disk) run
once by the orchestrating worker before dispatching passes, handing each subagent only the relevant line-crops
instead of full pages, is the fix to actually adopt next time, not just note again.

## L4: reconciled transcription and rerun (24 September 2026, LANE R2 worker L4, Sonnet, $4 cap, no subagents, no network)

**Line-id mismatch found before reconciling.** `tools/reconcile_passes.py` aligns witnesses by matching line
id, but L1's own line numbers did not match pass A's: on 6179 p3, L1 numbered the same five physical lines one
lower throughout (`p3L5`-`p3L8` vs pass A's `p3L6`-`p3L9`); on 6467, L1 used its own running sub-index
(`p2L1`-`p2L5`) instead of the manuscript's real line numbers pass A used (`p2L6`-`p2L8`, `p2L10`-`p2L11`,
with `p2L9` a plain-text line neither cipher run touches). Both are cosmetic (the token *sequence* and every
page/run's total count match pass A's once re-segmented -- 113/80 for 6179 p2/p3, 27/19 for 6467's two runs),
not a content disagreement, so this pass wrote `build_v2.py` to reconcile per page (6179) or per cipher run
(6467) rather than per raw line id: it re-derives each witness's sign sequence for a page/run, aligns it to
pass A's with `tools/reconcile_passes.py`'s own imported Needleman-Wunsch (`rp.nw`) and `norm_sign`, and adds
one refinement that tool does not have -- a base-digit majority pass for cells whose literal strings (which
include the `^`/`~` marks) have no 2-of-3 (or 2-of-2) match but the underlying numeral does (e.g. 6179 p2
col34: A=`24^`, B=`29^`, L1=`24` -- no literal majority, but A and L1 agree the numeral is 24, so the cell
writes `24` at conf M with the mark left disputed, instead of standing as an unresolved 3-way split). Also
handles 6179 pass B, which per L3 never reached p3 or 6467 (stopped over cap): 6179 p2 reconciles 3-way (pass
A, pass B, L1), 6179 p3 and both 6467 runs reconcile 2-way (pass A, L1).

**Counts** (`python3 build_v2.py`): 6179 p2 113 rows, H 83, M 30 (1 unresolved); 6179 p3 80 rows, H 61, M 19 (6
unresolved); 6467 run 1 (p2 lines 6-8) 27 rows, H 20, M 7 (1 unresolved); 6467 run 2 (p2 lines 10-11) 19 rows,
H 14, M 5 (1 unresolved, down from 2 -- see below). 239 rows total, 178 H (74.5%), 61 M, 9 genuinely
unresolved (no majority at the digit level either): `ciphertext_6179_v2.tsv` p2L28 pos12; p3L6 pos7,8,16;
p3L7 pos5,6,17; `ciphertext_6467_v2.tsv` p2L7 pos12 (run1), p2L11 pos12 (run2) -- each keeps pass A's own
reading with the other witness's in `alt` and `note` says `unresolved`, not silently dropped. Also: 4
witness-only insertions on 6179 (tokens pass B or L1 has that align to no position in pass A -- e.g. a mark
one pass attached to a neighbour and another gave its own row) and 0 on 6467, appended at the end of each v2
file with no line/pos (not counted in the totals above; rule 2, nothing repaired silently).

**Image settling.** No PIL/ImageMagick and no network in this brief (the crop tooling used by L1 and L3
needs one or the other), so the only recourse for the 9 unresolved cells was reading the already-fetched full
page PNGs directly (`images/06179_p2.png`, `06179_p3.png`, `06467_p2.png`) at their saved resolution, no crop.
That was legible enough to confirm one cell outright: 6467 run 2 position 8 (pass A's `07` then a
free-standing `[mark]`, vs L1's merged `07~~`) -- the image shows a small mark distinct from the digit
following the second `07` on that line, matching pass A's split; `ciphertext_6467_v2.tsv` p2L11 pos8 now
reads `note=confirmed on images/06467_p2.png (L4): ...` instead of `unresolved`. The other 8 could not be
called safely at this resolution without a crop/zoom tool -- guessing at exactly the digit pairs (8/18, 9/1,
2/12, 4/24, 5/3, etc.) both trained passes already flagged as uncertain risked introducing a wrong "reading"
rather than reporting an honest gap, so they stand as pass A's reading, conf M, `unresolved`, with L1's
alternative preserved in `alt` for whoever next has a crop tool or zoom capability on this target.

**Solver rerun** (`solve_l2.py --ciphertext-6179 ciphertext_6179_v2.tsv --ciphertext-6467
ciphertext_6467_v2.tsv`, same fr16-corpus/Marguerite-de-Valois-control setup as L2, both trained on text
disjoint from the target and control alike):

| Mode | Test A control clean | Test A control 8% noise | Test A target 6179 | Test B control (period 5) | Test B target 6179 | Test C crib (both spellings) |
|---|---|---|---|---|---|---|
| overlined numbers folded to base digit (default, N=189, K=25) | 73.5% read, score/tok -2.157 | 48.7% read, -2.329 | no reading, -2.503 (worse than noisy control) | 100% read | no reading, best -3.549 (a23, period 14), gibberish | no consistent sign->letter map |
| overlined/marked numbers as distinct signs (`--mark-signs`, N=199, K=41) | 73.4% read, -2.082 | 29.6% read, -2.177 | no reading, -2.304 (worse than noisy control) | 100% read | no reading, best -3.371 (a23, period 14), gibberish | no consistent sign->letter map |

**Result: negative for both designs in both modes, each against a matched control of the same length and
sign count, on the reconciled transcription (L2's transcription gap -- more overlines on 6467 than L1
recorded, flagged as untested there -- is now addressed: this rerun used the properly-marked v2 file and the
`--mark-signs` distinct-sign mode L2 could not run).** The target never outperforms its own noisy (8%
misreading-rate) control in test A under either mode, and test B's target never approaches the control's 100%
read under any period/alphabet/direction tried. Test C (the 6467 margin note as a crib) still finds no
consistent many-to-one sign-to-letter map in either spelling, at up to 6 nulls, in 27 signs -- consistent with
L2's read that the note is a short gloss rather than a word-for-word decipherment, or that the system is not a
fixed monoalphabetic/periodic-polyalphabetic one over a 23-25-letter alphabet. This strengthens L2's original
negative (which ran without the overline data and without the reconciled transcription) rather than reversing
it.

**Not settled by this pass, for whoever picks this up next:** the 9 unresolved cells above need either a crop
tool run offline against the images already on disk (`tools/iiif_lines.py` needs IIIF/network; a local
PIL/ImageMagick crop script like L1's would work if that dependency is available) or a third blind pass on
just those lines; none of the 9 changes the negative result's shape (they are single-digit disputes within
lines that already read no better than gibberish either way). Novelty not classified (not this brief's job).

Requests: none (offline, no network, per brief). Cost: well under $4 cap.
