open
Groen van Prinsterer, Archives ou correspondance inédite de la Maison d'Orange-Nassau, 1e série, tome VI (1839), pp. 249-251, Lettre DCCLXXXIX, read directly by this worker (DBNL) with an explicit footnote confirming the cipher passages are omitted from print, not deciphered.

# La Garde, superintendent of Schoonhoven, to Willem van Oranje, partly unsolved cipher, 28 November 1577

QUEUE row: NB4 (`QUEUE.md`, "Dutch and Belgian archives (LANE N scout of 24 September 2026)").

## Check-solved (LANE CX, 25 Sept 2026)

Formal six-source re-run per `.claude/briefs/check-solved.md`, on top of the 24 Sept check-solved sweep already
below (not repeated where its own log already answers a source). GSME and LMSAC (6467's own editions) were read
by OX-LAG (25 Sept, 03:25 UTC per that section's own dating) and are not re-read here per this worker's brief.

1. **Web search** (this worker, 25 Sept 2026): `"La Garde" "Willem van Oranje" OR "Prince d'Orange" 1577 cijfer
   solved cipherbrain` surfaced only the DBNL Groen VI page itself (already read directly, see below), Gachard's
   edition home page, and general Dutch-Revolt biography. A separate model-solve-announcement check (this repo's
   Vals AI / Schneier / itdoeswhatnow source family, run once for all four of this worker's targets) found the
   Urquhart 1653 and Cyphral Distich stories, unrelated to this letter. No hit naming this letter, this cipher, or
   a solution.
2. **Standard edition/calendar.** Groen VI 249-251: already read directly and quoted (footnote above; see the 24
   Sept section below) — stands as line 2's citation. **Gachard's *Correspondance de Guillaume le Taciturne,
   prince d'Orange*** (this worker's brief specifically named it, not covered by the 24 Sept sweep): its retroboeken
   host is reachable (`resources.huygens.knaw.nl/retroboeken/gachard`, HTTP 200, 6 volumes listed) but this
   worker's attempt at the documented `<accessor>/index_html?search_term:...` full-text-search route
   (`gachard/1/search_in_text/index_html?search_term:ustring:utf-8=Orange&batch_start=1`) returned HTTP 500
   ("Pagina niet gevonden of Fout") — the accessor id shown in volume 1's page markup (`search_in_text`) is not
   the right path segment for this book's search URL, unlike the `toc1`/search patterns CLAUDE.md documents for
   the other retroboeken titles; one retry not attempted further per the good-citizen one-retry rule. Fell back to
   WVO's own Brongegevens field for 6179, which is a comprehensive per-letter bibliography (confirmed comprehensive
   by cross-check: 6467's own Brongegevens lists three editions, Groen + GSME + LMSAC, in the same field format) —
   for 6179 it lists **only** Groen van Prinsterer VI 249-251 (onv.), not Gachard. This is "not cited by WVO's own
   bibliography," a weaker claim than "searched and absent," logged as such; the Gachard full-text search itself
   is an open item for whoever next has time to find the right accessor path.
3. **Community lists.** `sources/cryptiana/web/dutch.htm` already read in full by the 24 Sept sweep below (no
   mention). No Cipherbrain/Schmeh-specific page was found in `sources/`; the web search above (query 1) is this
   worker's Cipherbrain-equivalent check and found nothing.
4. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` already grepped by the 24 Sept sweep below,
   zero hits for "la garde"/nassau/oranje; re-checked, same file, same result.
5. **Bourdeau** (`github.com/dbourdeau/cyphersolver`, fresh depth-1 clone by this worker, 25 Sept 2026, not the
   24 Sept sweep's clone): `grep -ril "la garde\|6179\|willem.*oranje\|van oranje"` — zero hits anywhere in the
   repository.
6. **Aymeloglu** (`github.com/aaymeloglu/unsolved-ciphers`, fresh depth-1 clone by this worker, 25 Sept 2026):
   same grep — zero hits.

**Verdict: open, unchanged.** Nothing in this pass's six sources locates a decipherment, key, or prior reading of
this letter's cipher passages. Line 2's citation (Groen VI, read directly, cipher passages explicitly noted as
omitted) is the gate-passing sentence. Novelty not classified (rule 10; not this brief's job).

Requests this pass: resources.huygens.knaw.nl 3 (correspondanceguillaumetaciturn landing page, retroboeken/gachard
landing + volume 1 page, retroboeken/gachard search attempt, wvo/app/brief?nr=6179 re-fetch), all ≥1.5s apart, one
500 (search route, not a block, one retry not spent further). github.com 2 (fresh shallow clones, dbourdeau +
aaymeloglu, deleted after grep). WebSearch 4 queries. No subagents, no logins, no credentials.

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

## OX-LAG: print check of 6467's cited editions (25 September 2026, LANE OX worker, Sonnet, $4 cap, no subagents)

**Job:** check whether the two printed editions WVO cites for **6467** (Marnix to Willem van Oranje, 2 Nov 1577 --
the letter with the WVO-noted "oplossing in de marge", margin solution, beside its first cipher run) print a key,
a decipherment, or a plaintext crib for 6179's or 6467's own cipher passages, and re-confirm Groen VI 249-251 for
6179.

**Fetched** (`editions/manifest.json`, both PDFs + PyMuPDF text extracts saved to `editions/`):
- **GSME**: Gerlo, Aloïs, en Rudolf De Smet, eds., *Marnixi Epistulae* (Brussel 1990-1996), II, 133-135, nr. 97.
  `resources.huygens.knaw.nl/media/wvo/images/edities/GSME/06467_ed.pdf` (3pp, OCR'd scan).
- **LMSAC**: Marnix de Sainte Aldegonde, Ph., *Correspondance et mélanges*, ed. Lacroix (Paris-Bruxelles-Genève
  1860), pp. 241-242. `resources.huygens.knaw.nl/media/wvo/images/edities/LMSAC/06467_ed.pdf` (2pp, OCR'd scan).
- Also confirmed in the 6467 record itself: a third citation, Groen van Prinsterer, *Archives d'Orange-Nassau*
  VI, 219-221 nr. DCCLXXVIII -- **this is 6467's own Groen citation, a different page range from 6179's** (VI,
  249-251, Lettre DCCLXXXIX, already read directly by the 24 Sept check-solved sweep above). Not re-fetched
  this pass (no PDF link offered on the 6467 record page for this edition; GSME/LMSAC already answer the
  question for 6467, and DBNL/Groen VI for 6179 was already read directly and quoted with its own footnote by
  that sweep -- re-fetching would duplicate a already-settled, directly-quoted finding on a host another
  lane (LANE V2) has used for this same volume).

**What each prints for 6467's cipher passages.** Both editions print the letter's clear French text
continuously around the cipher; **neither deciphers either passage**:
- **GSME reproduces the raw cipher digit-groups in running text**, unlike a decipherment: `"Si on pouvoit
  justifier le faict de Gand, 7.8.2.11.10.14.14.12.9.3. $.4.14.4.8.15.2.4.$. 11.4.3.9.2.17.5.11 ce seroit un
  grand poinct, car j'entends que ce que V[ostre] E[xcellence] a veu n'est pas autentique et que 10.8.2.10.
  5.7.9.$.4.10.8.9.$*.4.7.1.3.12."` (`editions/6467_GSME.txt`). Its footnote apparatus glosses the surrounding
  *history*, not the cipher: `"17 Ie faict de Gand] De arrestatie van Aarschot en zijn aanhang."` (the arrest of
  the Duke of Aarschot and his following) -- a content note, not a key. No footnote anywhere in the 3pp
  addresses the numerals themselves, and none reproduces or mentions a marginal annotation.
- **LMSAC gives clear text only, and treats the two cipher runs inconsistently**: the *first* run is dropped
  silently with no mark at all -- its text reads straight through, `"...ny contentement. Si on pouvoit
  justifier le faict de Gand, ce seroit un grand poinct, car j'entends que ce que V. Exc. a veu n'est pas
  autenticque et que"` -- while the *second* run is marked with an ellipsis and an editorial footnote:
  `"....... ..(l)."` ... `"(1) Ce passage est en chiffres"` (this passage is in cipher) (`editions/6467_LMSAC.txt`).
  Same pattern as Groen VI on 6179 (cipher passages omitted from print), but LMSAC does not even flag the first
  omission as a lacuna.

**Correction to this file's own margin-note reading.** R15's section above transcribed a note beside 6467 run 1
as *"Justiffier le faict du grand"* and treated it as a short marginal gloss. Both print editions independently
agree the letter's own **running main-text clause** immediately before run 1 reads **"justifier le faict de
Gand"** (the Ghent/Aarschot affair, per GSME's footnote), not "du grand" -- R15's read of "du grand" is very
likely that same main-text clause read with two letters confused ("de Gand" / "du grand" look similar
abbreviated), not a distinct annotation. This does **not** resolve WVO's own claim of a genuine marginal
solution (Opmerkingen: *"waarvan de eerste met oplossing in de marge"*, of which the first passage has a
solution in the margin) -- neither edition reproduces or mentions any marginal annotation at all, so if one
exists it is manuscript-only, still unconfirmed by any worker on this target, and remains the one live lead
here (see "left for whoever picks this up" below).

**Transcription cross-check (a side-value of this print check, not itself a decode).** GSME's digit sequence
lines up almost exactly, position for position, against this file's own reconciled `ciphertext_6467_v2.tsv`,
once GSME's `$`/`$*` placeholder (used where GSME's typesetter had no glyph) is read against this file's `07`/
`[mark]` notation for the same recurring flourish:
- **Run 1** (27 signs): GSME `7 8 2 11 10 [14] 14 12 9 3 $ 4 14 4 8 [15] 2 4 $ 11 4 3 9 2 17 5 11` vs v2's base
  digits (p2L6+p2L7+p2L8) `7 8 2 11 10 [19] 14 12 9 3 07 4 14 4 8 [11] 2 4 07 11 4 3 9 2 17 5 11` -- 25 of 27
  agree exactly, including both `$`=`07` positions. Two new mismatches, **not previously flagged as disputed**
  (both currently graded H in v2): position 6 (v2 `19`/p2L6 pos6 vs GSME `14`) and position 16 (v2 `11`/p2L7
  pos7 vs GSME `15`). One existing internal dispute is resolved toward the file's own current reading: p2L7
  pos12 (`4`, alt `B:24`) -- GSME agrees `4`.
- **Run 2** (18 signs, dropping the free-standing `[mark]` row p2L11 pos8 which has no numeral counterpart):
  GSME `10 8 2 10 5 7 9 $ 4 10 8 9 $* 4 7 1 3 12` vs v2 (p2L10+p2L11) `10 8 2 10 5 7 9 07 4 10 8 9 07[mark] 4 7 1
  5 12` -- **every position agrees**, including the asterisked `$*`/`07`+`[mark]` position (13th), which both
  witnesses independently flag as unusual. One existing internal dispute is resolved **away from** the file's
  current primary reading: p2L11 pos12 currently reads `5^` (alt `B:3^`) -- GSME agrees with the alternate,
  `3^`, not the committed `5^`.
- Not acted on in `ciphertext_6467_v2.tsv` itself (out of this print-check brief's scope -- a transcription
  reconciliation call, not a print check): the file is left as L4 wrote it. A future transcription pass should
  weigh GSME as a third independent witness at these four positions (two now-resolved disputes, two new
  mismatches) before any further solver rerun; GSME's own text is an OCR'd scan of a 1990s scholarly edition,
  not itself infallible, so this is evidence to weigh, not an automatic overwrite.

**Groen VI 249-251 (6179, re-confirmed, not re-fetched).** Stands as the check-solved sweep above already
found and quoted: the printed edition's gaps are explicitly captioned *"Les lacunes sont occasionnées par des
passages chiffrés"* -- 6179's own cipher passages are omitted from print, not deciphered.

**Verdict (per the brief's three options): (c) neither.** No key or decipherment of this cipher family is
printed in GSME, LMSAC, or Groen VI; no plaintext crib for either passage's own enciphered words exists in any
of the three. All three print or gloss the clear text *around* the cipher, never through it. This is a
negative for the print-check route on 6467 and reconfirms the existing negative on 6179's own edition.

**Left for whoever picks this up:** (1) the manuscript margin beside 6467 run 1 (`images/06467_p2.png`) is the
one remaining lead in this record -- WVO's own field says a solution sits there, and no worker has yet
confirmed by eye whether it is a real word-for-word decipherment (as opposed to R15's likely misreading of the
adjacent main-text clause, corrected above); a focused native-resolution crop of just that margin, not the
full page, is the cheap next test. (2) Weigh the four GSME cross-check positions above into
`ciphertext_6467_v2.tsv` on the next reconciliation pass. Novelty not classified (not this brief's job).

Requests: resources.huygens.knaw.nl 3 (1 record page `brief?nr=6467`, 2 PDF fetches, all ≥1.5s apart). No other
hosts touched (archive.org and www.googleapis.com, listed as possible hosts in the brief, were not needed once
GSME/LMSAC answered the question directly). No subagents. Cost well under $4 cap.

## Y1: the 6467 margin (25 Sept 2026, LANE R6)

**Job:** confirm by eye, at the best available resolution, what WVO's Opmerkingen field calls a "solution in the
margin" (`oplossing in de marge`) beside 6467 run 1, and align it to `ciphertext_6467_v2.tsv` if it is one.

**Resolution check (before cropping).** Re-fetched `06467.pdf` (request 1) and extracted its page-2 image
natively (`fitz.Pixmap` on the embedded XObject, offline after the fetch): 831×1244 grayscale, *lower*
resolution than the already-saved `images/06467_p2.png` (1241×1754), which is an upscaled render of the same
source. Also read the WVO record page (request 2, `brief?nr=6467`): it links only the same PDF plus a small
thumbnail, no IIIF or larger scan. **`06467_p2.png` already on disk is the best resolution this host offers**;
no re-fetch of a sharper image was possible. Crops below are native-resolution 3x/4x LANCZOS enlargements of
that file, saved to `images/` and logged in `images/manifest.json` under `margin_crops_25_sept_2026`.

**What the margin carries.** The whole left-margin column beside both cipher runs
(`images/margin_6467_leftcolumn_3x.png`) holds exactly two annotations, nothing else:

- Beside run 1 (`images/margin_6467_run1_4x.png`): two lines, **"Justifier le faict du grand"** — confirms
  R15's original read exactly, now at a sharper crop. Clearly a separate hand/ink from the body text, written
  in the margin proper (not interlinear).
- Beside run 2 (`images/margin_6467_run2_4x.png`): a short abbreviation, read **"N.[c?].f."** (three
  letter-groups separated by points) — this is at the image's native-resolution ceiling; further magnification
  (tried at 8x) only blurs, it does not resolve the middle letter further.

**Neither is a word-for-word decipherment key, and no `key_6467_margin.tsv` is written.** Run 1's note is 5-6
words against a 27-sign cipher run; run 2's is 3 letter-groups against an 18-sign run. L4's solver rerun already
tried this exact text as a crib against the ciphertext ("Test C") and found no consistent many-to-one
sign-to-letter map in 27 signs at up to 6 nulls — that negative stands; this pass adds no new crib attempt
(brief: no cryptanalysis beyond the gloss alignment).

**New finding: the margin's wording appears, unmarked, in both print editions' running text — but not on the
manuscript's own main-text line.** OX-LAG quoted GSME's edited text as "Si on pouvoit justifier le faict de
Gand, [27 digits] ce seroit un grand poinct" and read this as GSME merely reproducing raw cipher digits, "not a
decipherment." Rendering GSME's own PDF page as an image (`editions/6467_GSME.pdf`, offline, already on disk,
no new fetch) and reading it directly confirms the phrase "justifier le faict de Gand" is typeset as ordinary
prose with no brackets, italics or apparatus mark distinguishing it from the surrounding text; its only
footnote ("17 le faict de Gand] De arrestatie van Aarschot en zijn aanhang") glosses its historical content, not
its textual status. LMSAC (1860) independently gives the same phrase at the same point and, per OX-LAG, drops
the cipher digits after it entirely. **But this exact phrase is not on the manuscript's own main-text line**: a
sharp crop of that line (`images/margin_6467_run1_4x.png`'s companion region, main text at y≈340-430 on
`06467_p2.png`) shows the hand write straight through "...ny contentement. Si on pourra
7.8.2.11.10.19.14.12.9." with no intervening clear words between "pourra" and the cipher digits — confirmed by
direct inspection at 3x, not by OCR. The only place on the page carrying that wording is the margin note beside
it. So two independent editions (1860 and 1990s) both silently absorbed the margin's words into their running
transcription at this point, with no apparatus note saying why.

That is evidence about what kind of note this is, not evidence that it decodes the cipher: read this way, the
manuscript's clear-text sentence is "Si on pouvoit [margin: justifier le faict de Gand], [27 still-undeciphered
cipher signs] ce seroit un grand poinct" -- i.e. even crediting the margin as the sentence's own omitted clear
words (an insertion/correction mark, the ordinary early-modern use of a margin, not a cipher solution), a
separate ~27-sign clause between "Gand" and "ce seroit" remains completely unread. That reading is more
consistent with L4's crib-test negative and the length mismatch than treating the note as a solution of the
numerals themselves. WVO's own "oplossing in de marge" tag is not shown wrong by this -- a cataloguer glancing
at a margin note beside a cipher passage and a manuscript that once had "opgelost" written somewhere on it could
reasonably describe it that way -- but it is not confirmed as a numeral-by-numeral solution by anything found
this pass, and the two print editions' silent, unmarked adoption of the same words is the most likely source of
WVO's characterization, not independent confirmation of it.

**Left for whoever picks this up:** (1) whether "justifier le faict de Gand" belongs in
`ciphertext_6467_v2.tsv`/a plaintext file as a C-grade (known-plaintext) clear-text insertion at this point in
the letter, sourced from two print editions plus the manuscript's own margin, is a transcription-reconciliation
call, not a decode -- out of this brief's scope. (2) The 27-sign clause after "Gand," and the 18-sign clause
after "que," remain fully unread; no new crib is proposed here. (3) run 2's margin abbreviation ("N.[c?].f.")
is unidentified; it is too short to be this letter's own passage content and reads more like an archival/filing
mark, but that is speculation outside this brief's scope.

Requests: resources.huygens.knaw.nl 2 (1 record page `brief?nr=6467`, 1 PDF fetch, ≥1.5s apart). No other hosts.
No subagents. Cost well under $5 cap.

## ZX2-LAG: pool (25 Sept 2026, LANE ZX2)

**Job:** widen the pool -- search WVO for every letter by or to La Garde and every 1576-1579 Orange-circle
letter whose notes mention cipher, and check any with cipher whether it uses the same dot-separated 1-24
numeral system as 6179/6467.

**Intake gate:** `python3 tools/intake_gate_check.py la-garde-1577` -> `la-garde-1577: open (line 1) -- edition/page
or full-text-search citation found within 6 lines` (exit 0).

**Source, not re-queried.** LANE N's 24 Sept 2026 harvest (`sources/wvo/NOTES.md`, `sources/wvo/cipher-letters-2026-09-24.tsv`)
already enumerated every WVO record whose Opmerkingen field mentions cijfer/chiffre/onopgelost/oplossing --
92 genuine cipher-related records, fetch-once per "fetch once, keep a manifest" (CLAUDE.md Usage item 4). This
pass filters that TSV to 1576-1579 instead of re-hitting `wvo/app/brieven?opmerkingen=...`: 13 records besides
the 3 already on file (6179, 6467, 5564). La Garde's own correspondent index (11 letters, only 6179 carries
cipher) was already confirmed by R9 24 Sept ("Searched WVO for other La Garde letters... a combined
correspondent+opmerkingen query confirms only 6179 itself carries 'cijferschrift'") -- not re-run.

**Fetched and checked by eye** (contact-sheet render of every page, plus close crops where a cipher passage was
visible; `siblings.tsv` has the full table, `images/manifest.json`'s `zx2_lag_sibling_sweep_25_sept_2026` block
lists the files): 424, 6136, 6178, 6221, 6238, 5227, 10700 -- 7 records, all their pages rendered (4+13+3+5+2+6+3 = 36 pages).

**Result: 0 same-system siblings.** Of the 7 fetched:
- **424** (Aerschot, 2 May 1579, German, KHAG): WVO's "solved on leaf" tag refers to a separate Simancas copy
  ("contemporaine kopie...is ontcijferd en uit het Frans in het Spaans vertaald", per `sources/wvo/NOTES.md`
  item 4), not this leaf -- checked both text pages at 1600px, continuous clear German prose throughout, no
  digit groups anywhere.
- **6178** (Lumbres, 26 Apr 1576, French) and **6221** (Guillaume David/La Huguerye, 19 May 1576, French):
  continuous clear prose on every leaf, no cipher visible. 6221's PDF also carries a bound-in printed excerpt
  page (a Kervyn/Groen-style edition scan of the same letter), confirming it is printed elsewhere -- consistent
  with the "solved elsewhere" status already in the TSV.
- **10700** (to the Reich deputies, 13 Jul 1579): the fetched leaf is itself a Simancas copy headed "Copia de
  carta del Principe de Orange... desciffrada" -- already-deciphered Spanish plaintext, not raw cipher.
- **6136** (Reinier Cant, Bremen, 14 Feb 1576): **cipher present and extensive** -- 8 of 13 rendered pages are
  entirely numeral cipher, dense dot-separated groups. But the value range runs to 150+ (e.g. "137", "144",
  "109", "127") with occasional symbol nulls (dagger/cross marks), against La Garde/Marnix's cap of 24 -- a
  materially larger alphabet, i.e. a different (and apparently much bigger) cipher system, not a pooling match.
  **This looks like a substantial unsolved cipher letter in its own right** (see "flag" below); not pursued
  further here, out of this brief's scope (pooling for La Garde only).
- **6238** (Junius de jonge, 26 Jan 1576, German): a short passage of invented cipher *symbols* (typeset-regular
  glyphs, not numerals) at the foot of p1 -- a substitution-table design, not the numeral system.
- **5227** (Willem van Oranje to Jan van Nassau, 4 Feb 1576): a short numeral passage at the foot of p4,
  dot-separated but mixed with lowercase roman letters as nulls/homophones (e.g. "79.12.6.L.94.p.7...83.m.62...",
  values to ~94) -- matches the already-established Jan-van-Nassau house-cipher description from 5564
  ("numeral groups with roman-letter labels mixed in"), confirming that design as a real multi-letter pattern
  for Jan van Nassau's own correspondence, not La Garde/Marnix's.

**Not fetched, inferred by cluster** (per `siblings.tsv`, flagged as such, not verified): 5228, 5561 (same
Jan-van-Nassau/KHAG cluster as 5227/5564); 10725, 12630, 12631 (same 1579 Reich-deputies/Gachard-cited cluster
as 10700). None of these clusters, on the one representative checked, carries the La Garde/Marnix design, so
checking the remaining cluster members was not expected to change the answer and was skipped to stay in budget
-- a genuine gap if a future worker wants full coverage, not a claim that they were checked.

**Pooled sign count: unchanged.** 0 same-system siblings found among the letters checked -> the pool stays
6179 (v2: 113+80 = 193 rows) + 6467 (v2: 27+19 = 46 rows) = **239 tokens, same as L4's 25 Sept count**. This does
not change the unicity picture for the homophonic family: L4's negative (target never beats its own 8%-noise
control, both with and without overlines as distinct signs) was already run at N=189-199, above the 150-sign
threshold this brief's pooling step exists to reach -- there was no shortfall to fill, and finding 0 matching
siblings confirms the ceiling on this route rather than opening a new one. The lever named in this job's line 2
("length") is not available from this circle's other correspondents; whatever narrows the homophonic/periodic
negative further has to come from a different family (family_run.py's masc/running_key) or a genuine key/crib
source, not more pooled ciphertext.

**Flag for the parent/orchestrator (not acted on, out of this brief's scope and files):** WVO 6136 (Reinier
Cant to Willem van Oranje, Bremen, 14 Feb 1576, KHAG shelfmark, `resources.huygens.knaw.nl/wvo/app/brief?nr=6136`)
is an entirely-enciphered, apparently unsolved multi-page letter (8+ of 13 pages of dense numeral cipher, values
into the 100s) with no existing target folder or QUEUE.md row found (`grep -rn "6136\|Reinier Cant"` across
QUEUE.md, STATUS.md, ciphers/*/NOTES.md: no hits outside an unrelated numeral run in na-raad-azie-1800). Worth
a scout/QUEUE row of its own -- this worker does not touch QUEUE.md per scope.

Requests: resources.huygens.knaw.nl 7 (PDF fetches for 424, 6136, 6178, 6221, 6238, 5227, 10700; all ≥2.1s
apart). No other hosts. No subagents (all rendering/cropping done locally with pymupdf + Pillow, installed from
PyPI, offline after fetch). Novelty not classified (not this brief's job).

## ZX2-LAG2: finish the WVO sibling sweep (25 Sept 2026, LANE ZX2)

**Job:** the predecessor's 5 (brief said 6; recount below) remaining unchecked 1576-1579 candidates, then a
live WVO query for La Garde/Schoonhoven correspondent + opmerkingen cipher terms, since the harvest on disk
may predate or miss hits.

**Intake gate:** `python3 tools/intake_gate_check.py la-garde-1577` -> `la-garde-1577: open (line 1) -- edition/page
or full-text-search citation found within 6 lines` (exit 0, re-checked at claim time).

**Recount.** Re-grepping `sources/wvo/cipher-letters-2026-09-24.tsv` for 1576-1579 gives 15 rows, not the
brief's "13": 424, 5227, **5228**, **5561**, 5564, 6136, 6178, 6179, 6221, 6238, 6467, 10700, **10725**,
**12630**, **12631**. Minus the 3 already on file (6179, 6467, 5564) = 12 candidates, minus ZX2-LAG's 7 fetched
(424, 6136, 6178, 6221, 6238, 5227, 10700) = **5** remaining, not 6 -- all 5 are now fetched and checked below;
none were left unaccounted for.

### Step 1: the 5 remaining candidates, same method (fetch PDF, render contact sheet, eye-check, delete PDF)

- **5228** (Willem van Oranje to Jan van Nassau, 4 Apr 1576): **cipher present**, p2 -- dot-separated numeral
  groups mixed with roman letters and symbol nulls, e.g. "69.p.4. 61.94.61.z.[symbol].20.62. 77.84.55.88...123.
  51.72.d.52. 64.E.l.U.d.q.n. faict grand bien 83.k.55.W...3.2." (full crop `images/siblings/5228_p2_full.jpg`),
  values running into the 120s. This matches the Jan-van-Nassau house-cipher design already established from
  5227/5564 (numeral groups with roman-letter/symbol nulls, values well above 24), not the La Garde/Marnix
  design -- **not a pooling match**. p6 also carries a clear-text numbered list ("1. le dic de saxe...", 10
  items) that looks like a policy/resolution summary, unrelated to this cipher passage; not pursued (out of
  scope).
- **5561** (Jan van Nassau to Willem van Oranje, 9 May 1576): continuous clear German prose throughout all 3
  pages, address leaf with seal, no digit groups anywhere -- **no cipher on this leaf**.
- **10725** (Willem van Oranje to Jan van der Linden, 20 Jun 1579): headed "Copia de carta del Principe de
  Orange...descifrada" -- an already-deciphered Simancas Spanish copy, same pattern as 10700, continuous clear
  prose, **no raw cipher digits**.
- **12630** (gedeputeerden van Duitse Rijk to Willem van Oranje, 25 Jun 1579): "Copia de carta...confirmada",
  continuous clear Spanish prose, **no cipher digits**.
- **12631** (Willem van Oranje to Heinrich-Otto von Schwartzemberg, 29 Apr 1579): headed "descifrada",
  continuous clear Spanish prose, **no cipher digits**.

Confirms by eye, not just inference, the cluster read the predecessor had flagged as unverified for 5228/5561
(Jan van Nassau cluster) and 10725/12630/12631 (1579 Gachard-cited "gedeputeerden" cluster): every member
checked reads the same way as its cluster's already-checked representative. **Result: 0 of 5 same-system,
1 with cipher present but wrong design (5228).**

### Step 2: live WVO query

`resources.huygens.knaw.nl/wvo/app/zoek_geavanceerd` gives the real advanced-search field names (`brieven?geavanceerd=1`
alone only re-lists the default 25 rows regardless of query params -- confirmed by sending a nonsense
correspondent name and getting the identical "25 resultaten"; do not trust that route). The working route is
`brieven?af_naam_vol=<name>&af_naam_volBool=AND&geavanceerd=1&batch_size=100` for correspondent (br_rich
direction defaults to "beide", both to/from) and `brieven?opmerkingen=<term>&opmerkingenBool=AND&jaar=1576&
eindjaar=1579&datumBool=AND&geavanceerd=1&batch_size=100` for a date-scoped remarks search.

- **Correspondent, "La Garde"**: 11 hits (1809, 1878, 1977, 2004, 2365, 3103, 3109, 3112, 6179, 6277, 8428) --
  exactly matches R9's 24 Sept count ("11 found via the correspondent index"), confirming no new La Garde
  letters since. Only 6179 (the target) carries cipher, per R9's already-run combined query (not re-run here,
  per this worker's brief).
- **Correspondent, "de la Garde"**: same 11 hits (the site's field does substring/fuzzy match, "La Garde"
  already covers it).
- **Correspondent, "Lagarde"** (no space): 0 hits.
- **"The Schoonhoven office"**: tried two readings. `af_naam_vol=Schoonhoven` (surname match) returns 26 hits,
  almost all "van Schoonhoven" as a personal surname, not La Garde's office -- too broad to be the intended
  lead and not pursued further (out of this brief's time box). `plaats=Schoonhoven` (place of origin) returns
  3 hits, one in range: **10761** (Hugo van Groenhoven, 6 Sept 1577, from Schoonhoven) -- opmerkingen field
  read directly, no cipher mention ("Gericht aan Gilbert van Est..."), not a cipher letter. The other two
  (4751, 1575; 5820, 1566) fall outside 1576-1579.
- **Opmerkingen date-scoped re-run, 1576-1579, term "cijfer"**: live query returns exactly the same 15
  briefnrs as the on-disk `cipher-letters-2026-09-24.tsv` for this range (424, 5227, 5228, 5561, 5564, 6136,
  6178, 6179, 6221, 6238, 6467, 10700, 10725, 12630, 12631) -- **the harvest is current, no staleness found**.
- **Opmerkingen date-scoped re-run, 1576-1579, term "chiffre"**: 0 hits (matches the 24 Sept harvest's finding
  that chiffre's one hit, 6131, falls outside this range).
- `gecijferd` and `cijferschrift` not separately re-run live: both are substrings of `cijfer`, already proven
  a complete superset by the 24 Sept harvest (sources/wvo/NOTES.md item 3) and re-confirmed current by the
  `cijfer` date-scoped re-run above returning the identical 15-row set the disk TSV has.

**Minimum met:** every La Garde letter in WVO is listed in `siblings.tsv` with cipher yes/no (11 correspondent
hits, only 6179 carries cipher, per R9 + this pass's live re-confirmation).

### Step 3: same-system hit with an image

None. All 5 fetched candidates plus the live query turned up 0 new same-system hits. **Pooled count unchanged:
239 signs (6179 193 + 6467 46), same as ZX2-LAG and L4.** Nothing crossed the 150-sign pooling threshold from
new material because there was no new material of the right design to pool.

**Conclusion.** The WVO sibling pool for the La Garde/Marnix dot-separated 1-24 numeral system is now fully
enumerated at 2 letters (6179, 6467), 239 pooled tokens. Every 1576-1579 Orange-circle cipher record in WVO has
been checked by eye (12 of 12 non-target candidates: 7 by ZX2-LAG, 5 by this worker) or is a plaintext-copy
duplicate already excluded by design (5228/5561/10725/12630/12631 confirm rather than merely infer the two
clusters ZX2-LAG had flagged). This route is exhausted; any further pooling needs a different lead (a
non-WVO archive, a different correspondent circle, or a period key/crib), not more WVO querying.

Requests: resources.huygens.knaw.nl 17, all ≥2.1s apart, descriptive User-Agent: 5 PDF fetches
(5228/5561/10725/12630/12631); 4 route-discovery fetches (`brieven?correspondent=...&geavanceerd=1` with a
real name and with a nonsense name, confirming that param is silently ignored -- both return the identical
"25 resultaten" default listing; `brieven?geavanceerd=1` and `zoek_geavanceerd` read to find the real field
name, `af_naam_vol`); 7 working search queries (`af_naam_vol`: La Garde, Lagarde, de la Garde, Schoonhoven;
`plaats`: Schoonhoven; `opmerkingen` date-scoped 1576-1579: cijfer, chiffre); 1 detail-page fetch (10761). No
other hosts. No subagents. Novelty not classified (not this worker's job).

## WC-LAGARDE (26 Sept 2026, LANE WC worker)

**Job:** settle L4's 9 fully-unresolved cells from the already-fetched images, then rerun `solve_l2.py` with its
matched controls plus a noisy control at an injected-error level bracketing the transcription's own measured
pass-to-pass disagreement (CLAUDE.md rule 3, SALV-DIAG lesson).

**Step 0 (intake gate):** `python3 tools/intake_gate_check.py la-garde-1577` -> `la-garde-1577: open (line 1) --
edition/page or full-text-search citation found within 6 lines` (exit 0).

**Step 1: the 9 cells.** Installed numpy+Pillow from PyPI (offline after fetch, `tools/iiif_lines.py` needs
numpy). No new network fetch -- all crops cut from the already-fetched full-page PNGs on disk
(`images/06179_p2.png`, `06179_p3.png`, `06467_p2.png`) with local PIL crop/zoom (2x-10x LANCZOS) into
`images/crops_wc/` (not all intermediate crops are individually referenced below; the ones cited are the
clearest read for each cell). Two independent blind reads per hard cell: this worker's own direct crop read,
plus one Sonnet subagent (general-purpose Agent) given only the two hardest zoomed crops with no candidate
values shown, asked to describe the glyph shape (not to guess a "sensible" cipher value). The subagent's
independent read matched this worker's own for both cells it was asked about (6179 p2L28 pos12: "18^", a
1-stroke feeding one closed loop under one continuous overline, not the committed "12" nor alt "8^"; 6179 p3L6
pos8: a loop-with-crossbar flourish mark riding on a plain "1" downstroke, not the committed "9" nor a bare
"1" without the mark) -- two-witness agreement on the two hardest calls.

All 9 cells settled, 0 remain unresolved. `ciphers/la-garde-1577/build_v2.py`'s `CONFIRMED` mechanism was
extended (previously only cleared a `note`'s "unresolved" tag for one 25 Sept cell; now also overrides
`group`/`conf` so a reconciliation rerun reproduces these readings per rule 7) and wired into all four
reconcile_page calls (previously only 6467 run2 used it, so a plain rerun of `build_v2.py` would have silently
reverted the 6179 p2/p3 and 6467 run1 fixes back to "unresolved"). `python3 build_v2.py`'s output after this
change matches the hand-settled files byte-for-byte except for note wording (verified with `diff`); regenerating
is now the reproducible path, not the hand edit.

| Cell | Was (A/alt) | Settled | Evidence |
|---|---|---|---|
| 6179 p2L28 pos12 | 12 / B:8^ / C:18 | **18^** | crop: 1-stroke + one closed loop under one overline; independent blind subagent read agrees exactly |
| 6179 p3L6 pos7 | 18^ / B:[mark] | **18^** (confirmed) | crop: clear 1+8 digits under one overline, not a free mark |
| 6179 p3L6 pos8 | 9 / B:1 | **1~** | crop: loop-crossbar flourish over a plain 1-downstroke, not this scribe's ordinary rounded 9-loop (compared directly against p3L6 pos3's own 9); independent blind subagent read agrees |
| 6179 p3L6 pos16 | 12 / B:2 | **2** | crop: bare small loop-tail digit right after the free-standing pos15 mark, no leading 1-stroke |
| 6179 p3L7 pos5 | 6 / B:8 | **6** (confirmed) | crop: clear overlined 6-shape |
| 6179 p3L7 pos6 | 18 / B:10 | **18** (confirmed) | crop: 1-stroke + 8-loop, not a closed-oval 10 |
| 6179 p3L7 pos17 | 18 / B:10 | **18** (confirmed) | crop: 1-stroke + 8-loop before the overlined 12 and free mark that precede "de vre Sgre" |
| 6467 p2L7 pos12 (run1) | 4 / B:24 | **24** | crop: clear two-digit 24; agrees with OX-LAG's 25 Sept GSME print-edition cross-check, which already flagged GSME reading 24 here |
| 6467 p2L11 pos12 (run2) | 5^ / B:3^ | **3^** | crop: overlined 3 (downward-opening loop, unlike 5's upper hook); agrees with OX-LAG's GSME cross-check |

Two of the nine (6467 run1/run2 pos12) had already been flagged by OX-LAG's independent GSME print-edition
cross-check (25 Sept 2026) as likely needing this exact correction; this pass's own blind image read reaches
the same value from the manuscript image directly, an independent confirmation via a different method.

**Counts after settling:** 239 rows total (unchanged), H 187 (was 178), M 52 (was 61), 0 unresolved (was 9).
Measured pass-to-pass disagreement (rows carrying a witness `alt`, i.e. two blind passes disagreed on the
literal sign): **48/239 = 20.1%** now (was 57/239 = 23.8% before this pass); M-grade rate (includes
majority-resolved marks): **52/239 = 21.8%** now (was 61/239 = 25.5%).

**Step 2: `solve_l2.py` rerun with error-bracketed noisy control.** Added a `--noise-rate` flag (default 0.08,
the original L2/L4 value, preserved) so the noisy control's injected-error level is no longer hardcoded --
CLAUDE.md rule 3's SALV-DIAG lesson requires this bracket the transcription's own measured disagreement rather
than stay fixed at whatever level the first worker happened to pick. Corpus: `tools/data/fr16` both
Catherine de Médicis volumes, gunzipped to a scratch file (155,320 lines combined); control-plain: lines
1006-1030 of `lettresindites00marg_djvu.txt` (Marguerite de Valois, 1580 letter to the Queen Mother), same as
L2/L4, disjoint from the training corpus and from the target's own clear text. Bracket tested: 8% (historical
baseline), then a scan from 20% to 28% to find exactly where each mode's noisy control stops beating the
target, against a measured rate of 20.1-25.5% depending on which of the two rates above is used.

| Mode | Control clean | Control 8% noise | Control 20-26% noise | Control 28% noise | Target 6179 score/tok |
|---|---|---|---|---|---|
| base-digit (default, N=189, K=25) | 73.5%, -2.157 | 48.7%, -2.329 | 28.6% at 22%, -2.413 | 15.9%, -2.449 | **-2.484** (worse than every noisy control tried, 8-28%) |
| overlined/marked as distinct signs (`--mark-signs`, N=199, K=42) | 68.8%, -2.076 | 16.1%, -2.196 | 21.6% at 20% (-2.264) / 16.1% at 24-25% (-2.217) / 9.5% at 26% (-2.259) | 7.0%, **-2.353** | **-2.281** (worse than control at every level 8-26%; control collapses below target only at 28%) |

Test B (periodic Vigenère/Beaufort, periods 1-14): control still reads 100% at period 5 a24; target's best score
moved slightly with the corrected transcription (base-digit -3.496 at a23/period14, mark-signs -3.320 at the
same) but is unchanged in kind -- gibberish, no period/alphabet combination reads. Test C (the 6467 run-1 margin
note as a crib, both spellings, <=6 nulls): still no consistent many-to-one sign-to-letter map on the corrected
run-1 sequence (positions shifted by the pos12=24 correction, but the crib fit function still returns no match).

**Result: negative for both designs, still control-backed, now against a control whose injected error brackets
the transcription's own measured disagreement rate.** Base-digit mode's negative is robust throughout the
entire tested range (8-28%): the target never beats even a control degraded by simulated error nearly 4x the
transcription's own current M-rate (21.8%). Mark-signs mode's negative holds at every noise level from 8% up
through 26% -- comfortably past both the current (21.8%) and legacy (25.5%) measured-disagreement figures --
and only flips (control score drops below target's) at 28%, a level with no support in this transcription's own
measured error. Per rule 3's SALV-DIAG test ("if the control collapses at or below the measured error, the
negative is not a test at this transcription error"): the collapse point here (between 26% and 28%) sits above
every measured-disagreement figure computed for this transcription, so the existing negative is *not*
undermined the way Salviati's was -- this is a genuine, if narrower-margin than it first looked, confirmation
that the negative survives realistic transcription noise, not a non-test.

**Status: stays `open`** (rule 5) -- this pass strengthens L4's existing control-backed negative for the
monoalphabetic/homophonic and periodic-polyalphabetic families rather than showing it was a non-test, so there
is no basis to move to `partial`/NEAR.md. Not `closed-negative`: only two of the possible design families
(masc/homophonic-substitution and periodic-polyalphabetic, both via this target's own hand-rolled `solve_l2.py`
rather than `tools/family_run.py`) have a matched, now error-bracketed control; `masc`/`running_key` via
`tools/family_run.py` have not been tried on this target. Recommendation for the orchestrator, not set here: if
a `family_run.py` pass on `masc`/`running_key` also returns a control-backed negative, this target's ladder
would be exhausted and `closed-negative` becomes a legitimate call at that point -- but that is the next
worker's job, not this one's.

Requests: none (all crops cut locally from images already on disk; no network fetch this pass). One Sonnet
subagent (general-purpose Agent, blind read of two crops, no candidates shown). Cost: see the lane ledger.

## WC-LAGARDE2 (26 Sept 2026, LANE WC worker)

**Job:** the owner's stuck-rule try -- the materially different family the sign system itself suggests (numerals
1-24 carrying overlines and loop marks: base code = letter and the mark = a following vowel (syllabary), or
signs standing for whole words (wordcode)) -- run via `tools/family_run.py` rather than this target's own
hand-rolled `solve_l2.py`, since neither `syllabary` nor `wordcode` had been tried on this target before.

**Step 0 (intake gate):** `python3 tools/intake_gate_check.py la-garde-1577` -> `la-garde-1577: open (line 1) --
edition/page or full-text-search citation found within 6 lines` (exit 0).

**Step 1: spec.** `specs/la-garde-1577.json` written by the new `ciphers/la-garde-1577/build_spec.py`, pooling both
letters' 239 primary-reading tokens (the same count WC-LAGARDE's own settling pass reported; excludes the 6
trailing witness-only insertion rows in `ciphertext_6179_v2.tsv` that L4 already flagged "not counted in the
totals") into code^mark tokens: a bare numeral is `N^`, an overlined one `N^ol`, one carrying the loop-crossbar
flourish `N^lp`, and a free-standing flourish with no attached digit (11 of the 239, WC-LAGARDE's settling did not
change this) its own base code `MARK^` -- the same choice `solve_l2.py --mark-signs` already makes for these rows.
27 distinct base codes (numerals 1-24 plus '07' and '29', which do not fit that range at the current transcription,
plus MARK), 48 code+mark types, marks 195 bare / 39 overline / 5 loop-crossbar (18.4% marked share). `row_pattern`
is one manuscript-line run of S's per pooled `ciphertext` line with a single plain-box gap between runs -- this
transcription recorded only the cipher tokens, not the interleaving plain French words, so there is no finer
honest pattern to write than the one `family_run.py`'s own no-pattern default already builds from the same message
lengths; it is written out explicitly anyway so the run/gap structure is visible in the spec file. `judge` block:
language fr, corpora both `tools/data/fr16` volumes (matching L2/L4/WC-LAGARDE's own corpus choice), letters
200-380.

**Step 2: syllabary.** `python3 tools/family_run.py specs/la-garde-1577.json --family syllabary --seeds 3
--measured-error 0.23 --param err=0.23 --gate 0.6 --label "WC-LAGARDE2 stuck-rule try"` (0.23 = mid of WC-LAGARDE's
measured 20.1-25.5% pass disagreement; `--param err=0.23` was accepted alongside `--measured-error 0.23` with no
argument conflict). Control (N=228-233, K=48-49, base code = letter, an overline/loop mark = the following vowel,
5% error bracket widened to 23% to match this transcription's own measured disagreement): **recovery 0.159 / 0.393
/ 0.603, mean 0.385** -- **CONTROL BELOW GATE** (0.6). Target not run; row appended to HYPOTHESES.md by the tool
itself.

**Step 3: wordcode** (time remained well under the 80% box line). `python3 tools/family_run.py
specs/la-garde-1577.json --family wordcode --seeds 3 --measured-error 0.23 --param codes=marked --param err=0.23
--gate 0.6 --label "WC-LAGARDE2 stuck-rule try"` (`--param` is `action="append"` in this tool -- two separate
`--param` flags, not one string, the one adjustment needed beyond the brief's literal command line). Control
(N=227-233, K=39-46, marked numerals as whole-word/name codes; per-class breakdown printed by the tool: letters
class recovery 0.119-0.722, codes class 0.000-0.073 with 80-87% of code tokens landing in the control's own word
list): **recovery 0.280 / 0.586 / 0.096, mean 0.321** -- **CONTROL BELOW GATE** (0.6). Target not run.

**Result: both families untestable at 239 tokens and this error level, not a negative for either (rule 3).** A
control this far below its own gate (0.32-0.39 against 0.6) at N=239 means neither family's own solver can read a
control cipher of the same length, sign count and design under this transcription's measured error, so a target
run would prove nothing about the target either way -- per rule 3 and the brief's own step 4, this is recorded as
"not a test at this N and error," not as a control-backed negative the way the monoalphabetic/homophonic and
periodic families were in L4/WC-LAGARDE. This is consistent with `specs/README.md`'s general observation that
`family_run.py`'s families need roughly N>=150-200 for the control itself to have power, and both new families
here add a second axis of freedom (the mark/vowel assignment, or the code/word split) on top of the same short
pooled length that already strained the periodic-Vigenere control in L4's own solve_l2.py runs (test B's control
still read 100% there only because a period-5 short key is a much smaller search than an open mark-to-vowel or
letter-to-word assignment).

**Status: stays `open`** (rule 5). Not `closed-negative`: the ladder is not exhausted -- `masc`/`running_key` via
`tools/family_run.py` have still not been tried on this target (WC-LAGARDE's own recommendation), and syllabary/
wordcode themselves are untested-by-this-tool at this N and error (not refuted), per CLAUDE.md's "second attempt"
paragraph: a further tuning of the same knob (a lower --gate, a different --param) is not the next test; a
genuinely different instrument or new material is. Concretely: (1) pooling more of the same numeral-cipher family
would raise N past the point where these controls have power (ZX2-LAG's sibling sweep found no same-system
sibling among the 1576-1579 Orange-circle letters checked so far, but did flag 6136, Reinier Cant 14 Feb 1576, as a
different, much larger unsolved numeral cipher, K>=150+ -- not a pooling match for this target); (2) a lower --gate
would not fix a control this far below 0.6, since the gate reflects whether the family's own solver has power at
this N at all, not a threshold tuned to this target. Spec's `cheap_test_done` filled with both rows' numbers.

Requests: none (no network this pass). No subagents. Cost: see the lane ledger.

## Web and blog check (GF-A2-4, 2 Oct 2026)

Queries (WebSearch, 2 Oct 2026 22:4x UTC), each with what came back:
1. sender + recipient + date: `La Garde Schoonhoven Prince d'Orange 28 novembre 1577 Walhain lettre chiffre` -- Wikipedia
   "Siege of Schoonhoven (1575)", DBNL Groen V (groe009arch05_01_0095 and colofon), DBNL biography "[de la Garde]",
   WVO edition PDF KLRP 10320 (another letter). Opened groe009arch05_01_0095: Lettre DLXXVII, Orange to Jan van Nassau,
   29 Sept 1575 -- no La Garde letter, no cipher. Nothing names 28 Nov 1577 or the cipher.
2. shelfmark + cipher: `"A 11/XIV C/G-1" OR "Walheyn" 1577 cijferschrift La Garde` -- unrelated manuscript catalogues
   (Louis Morel de La Garde calligraphy, Manuscripta juridica); no hit on the shelfmark.
3. distinctive phrase: `"Lettre DCCLXXXIX" Groen van Prinsterer La Garde passages chiffrés` -- DBNL calendarium days,
   Groen VI colofon, WVO PDF 07304 (another letter); the edition page itself (already read, line 2) is the only match.
4. folder title: `La Garde superintendent Schoonhoven to William of Orange partly unsolved cipher 1577` -- Schoonhoven
   1575 pages, WVO project page, Bauer *Unsolved!* listings, HistoCrypt articles on other ciphers; none names this letter.
5. Cipherbrain: `site:scienceblogs.de klausis-krypto-kolumne Oranien 1577 verschlüsselt Brief` -- archive/index pages
   and unrelated posts (German conquistador cryptogram, a 15th-century encryption); nothing on Orange or 1577.
6. Cryptiana blog: `site:cryptiana.blogspot.com William of Orange Dutch Revolt cipher` -- no cryptiana.blogspot.com result.
7. Cipher Mysteries: `site:ciphermysteries.com Dutch Revolt 1577 cipher letter` -- no ciphermysteries.com result (HistoCrypt
   Portuguese-cipher articles instead).
No blog post about this letter, so no comment thread to read. No decipherment or plaintext found on the open web.

## Premise check (GF-A2-4, 2 Oct 2026)

(a) Decipherments the folder already mentions: the only one is WVO's "oplossing in de marge" for sibling 6467 (Marnix,
2 Nov 1577) -- opened by eye by R15 and Y1 (25 Sept, crops `images/margin_6467_*`): the margin reads "Justifier le faict
du grand/de Gand" (a clear-text insertion both print editions absorb) and "N.[c?].f.", not a decipherment of the 27- and
18-sign runs; L4's Test C found no consistent map using it as a crib. 5564's "opgelost" (Jan van Nassau, a different
design) has no decipherment sheet in its 3pp file. For 6179 itself nothing in NOTES.md, the spec or HYPOTHESES.md
mentions a decipherment, gloss or clear copy. Not found.
(b) Other solvers' working files: shallow clones of dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers (2 Oct 2026),
grep `la garde|schoonhoven|walheyn|walhain|6179|6467` -- every hit is the French common noun "la garde" (Nevers,
Matignon, Selve, Catinat files) or a coincidental number; Bourdeau's README line 193 is "the French galleys under the guns
of La Garde" (Marseille, 1530s). No working file for this letter. Aymeloglu cited, not copied. Not found.
(c) Physical neighbours: the whole WVO PDF 06179 is on disk (`images/06179_p1-p4.png`, inventory.tsv): p1 clear prose,
p2-p3 cipher in clear prose, p4 the address leaf -- no decipherment, slip or clear copy on any of the four pages; the
KHA folder's leaves beyond this letter are not imaged (unreachable). Not found within the letter's own leaves.
(d) Recipient's side: Groen van Prinsterer VI pp.249-251 (the Orange-side edition, line 2) prints the letter with the
cipher passages omitted per its own footnote; Gachard's Correspondance de Guillaume le Taciturne not searched (search
route returned 500 on 25 Sept, LANE CX) -- unreachable. Not found in print.
Result: nothing found that reads 6179's cipher passages.

## A2-LAG: the 6467 margin words placed as a C-grade clear-text insertion (2 Oct 2026, account 2, LANE-A2PUSH)

**Job:** Y1's follow-up (1) only -- place "justifier le faict de Gand" where it belongs as a C-grade clear-text
insertion, with a reproducible check (rule 7). No cryptanalysis, no network.

**Intake gate:** `python3 tools/intake_gate_check.py la-garde-1577` -> `la-garde-1577: open (line 1) --
edition/page or full-text-search citation found within 6 lines` (exit 0).

**Image read (rule 2, this worker's own direct read of two crops already on disk, no subagent):**
- `images/margin_6467_run1_4x.png`: the left-margin note reads **"Justifier le faict de / Gand"** on two lines.
  The second line is "Gand" (G-a-n-d, no r), and "de" stands as its own word ending a flourished e at the end of
  line 1. This agrees with both print editions (GSME II 133-135 nr 97; LMSAC 241-242) and does **not** support
  R15's and Y1's "du grand". Y1's correction stands in reverse: the margin and the editions agree word for word.
- `images/crops_wc/6467p2_run1_overview.png`: the main-text words before run 1 read **"on pouvoit"**, as both
  editions print them, not Y1's "pourra". ("Si" is at the end of the line above, outside this crop; it rests on
  the editions here.) The margin note sits level with that line, to the left of "on pouvoit 7.8.2...". No caret
  or insertion mark shows in this crop.

**Placement:** `cleartext_6467.tsv` holds three C-grade rows anchored to `ciphertext_6467_v2.tsv` (that file is
not touched; `build_v2.py` still regenerates it unchanged): main text "Si on pouvoit" before p2L6 pos1; the margin
insertion "justifier le faict de Gand" in the same slot, after "pouvoit" and before run-1 sign 1; main text "ce
seroit un grand poinct" after p2L8 pos4. `build_clear_6467.py [--check]` checks every anchor against v2 and
regenerates `reading_6467_run1.txt`:

    Si on pouvoit [justifier le faict de Gand] <7> <8> <2^> <11> <10> <19> <14> <12> <9~> <3> <07> <4> <14~> <4^> <8> <11> <2^> <4> <07> <11> <24> <3> <9~> <2^> <17^> <5> <11> ce seroit un grand poinct

Grades: clear words C 13 (manuscript image plus two editions), H 0, S 0, M 0, I 0. The 27 cipher signs are
still unread, with no key and nothing decoded. This is a placement of clear text, not a reading of the cipher, so
there is no judge or spec run and no control (rule 3 does not apply: no solver, gate or alignment was run).
`--check` exit 0.

**What this settles and what it does not:** Y1's follow-up (1) is done: the margin words are placed, graded C,
and the transcription conflict between the margin and the editions is closed in favour of "de Gand". The margin
note is the sentence's own clear words written beside the line. It is not a solution of the numerals. Y1's
follow-ups (2) (the 27-sign and 18-sign clauses, unread) and (3) (run 2's margin "N.[c?].f.") are untouched and
still open.

**Next cheapest step:** ~~follow-up (3): one cropped image read of run 2's margin abbreviation to say whether it
is a filing mark or part of the text, using a 4x crop already on disk (`images/margin_6467_run2_4x.png`), about
$0.5.~~ Done 2 Oct 2026 by A2-LAG2 (section below): same hand and ink as the run-1 margin note, level with run 2's
second cipher line, not a filing mark; meaning unidentified. The unread cipher clauses still have no key material. WC-LAGARDE2's family controls fell below their gates
at this N, so a further family run needs new material (more same-system ciphertext), not a new setting (rule 3,
third-attempt clause).

Requests: none (no network). Vision: 2 direct image reads by this worker, 0 subagent calls.

## A2-LAG2: run 2's margin abbreviation read from the image (2 Oct 2026, account 2, LANE-A2PUSH)

**Job:** Y1's follow-up (3) only -- one cropped image read of the margin note beside 6467 run 2, to say whether it is a
filing mark or part of the letter. No cryptanalysis, no network.

**Intake gate:** `python3 tools/intake_gate_check.py la-garde-1577` -> `la-garde-1577: open (line 1) -- edition/page or
full-text-search citation found within 6 lines` (exit 0).

**Image read (rule 2; this worker's own direct reads, no subagent).** Three images, all from `images/06467_p2.png`
(1241x1754, the best this host serves, per Y1):
- `images/margin_6467_run2_4x.png` (Y1's crop, x40-260 y640-720): three letter-groups with points, **"N. c. f."**
  The third letter is a long f with a crossbar, the firmest of the three. The second is an open c. The first is a
  capital N whose last stroke ends in a small loop; it may carry a superscript letter (Nr, Nb), which this resolution
  does not settle. A stray dot sits to the left at the baseline.
- `images/crops_wc/6467p2_run2_margin_context_2x.png` (new, x0-1000 y590-770, 2x, made with ImageMagick from the page
  on disk): the note sits **level with the second line of run 2** (p2L11, "9.07.4.10.8.9.07*.4.7..."), not with
  the line where run 2 starts ("...pas autentique et que 10.8.2.1[0]..."). It is in the margin proper, left of the
  ruled edge. p2L11 carries the asterisk-like mark after the second `07` (v2 pos 8, GSME's `$*`), the only such mark
  on the page. The note carries no matching asterisk, so the link between the two is not shown, only possible.
- `images/margin_6467_run1_4x.png` (for comparison of hands only): the run-1 note's crossed f ("justifier",
  "faict") and its c ("faict") have the same form as the run-2 note's f and c, in the same light ink, at the same
  slant and size. **Both margin notes look like one hand.**

**Answer to follow-up (3):** not a filing mark. A filing or archive mark normally sits at the head, foot or dorse
and is in a later hand. This note is in the text margin, level with a cipher line, in what looks like the same hand
and ink as the run-1 note, which A2-LAG showed is the sentence's own clear words written beside the line. So it
belongs with the letter's own margin apparatus (the writer's, or a contemporary reader's beside the cipher). What
"N. c. f." stands for is unidentified. Neither print edition prints it: GSME (`editions/6467_GSME.txt` l.57-58) gives
"et que 10.8.2.10. 5.7.9.$.4.10.8.9.$*.4.7.1.3.12." with no margin text, and LMSAC (`editions/6467_LMSAC.txt`
l.35-36) gives "que ....... ..(l)." with the digits dropped.

**What this does not do.** Three initials against an 18-sign run with no word divisions are not a usable crib, and
none was tried. They are not a key either. Unlike run 1's note, they cannot be the clause's own clear words written
out in full. Grades: this is a transcription of a margin note, not a reading of cipher. Cipher tokens read: 0 (H 0,
C 0, S 0, M 0, I 0). Margin letters: f firm, c likely, N likely, any superscript on N unresolved. No judge or spec run
and no control (rule 3 does not apply: no solver, gate or alignment was run).

**Where Y1's follow-ups stand:** (1) done (A2-LAG); (3) done here, read as far as this image allows. (2) The 27-sign
and 18-sign clauses of 6467 and all of 6179's cipher are still unread, with no key material.

**Next cheapest step:** ~~the untried family for this numeral system that WC-LAGARDE2 names: `masc` through
`tools/family_run.py` on the pooled 6179+6467 ciphertext (N=239), matched control first (rule 3), about $3. This is a
different instrument from the syllabary/wordcode families that fell below their gates, so it is not a third pass
at the same knob. Expect the control to be weak at N=239 under the measured transcription error: if it falls below
its gate, the step is "not a test at this N" and the target waits for new material (a same-system sibling, or
Gachard's Correspondance de Guillaume le Taciturne, unreachable on 25 Sept). Another route: a higher-resolution
image of KHA A 11/XIV C/M-12 f.2 from the Koninklijk Huisarchief (owner-side copy request) would settle the N's
superscript; it is low value on its own.~~ Done 3 Oct 2026 by A2-LAG3 (section below): the clean control passes, but at the measured error it falls below its gate, so this is not a test at this N and error.

Requests: none (no network). Vision: 3 direct image reads by this worker, 0 subagent calls. New file:
`images/crops_wc/6467p2_run2_margin_context_2x.png` (176 KB).

## A2-LAG3: `masc` through `tools/family_run.py`, matched control first (3 Oct 2026, account 2, LANE-A2PUSH)

**Job:** the Verdict's next cheapest step only: `masc` on the pooled 6179+6467 ciphertext, control first (rule 3). No
network, no image reads.

**Intake gate:** `python3 tools/intake_gate_check.py la-garde-1577` -> `la-garde-1577: open (line 1) -- edition/page or
full-text-search citation found within 6 lines` (exit 0).

**Design check before running.** The spec's own tokens are code+mark types (N=239, K=48). A one-sign-per-letter control
cannot have 48 distinct letters: `homophonic_anneal.fold` gives a 24-letter alphabet (j->i, v->u), so `family_run.py`
would have built a control far below the target's K (dry run shows K=48; the control's window accept test can never
pass). So the run uses the base codes: `build_basecode.py` (new, `--check` exits 0) strips the mark suffix and drops
the free-standing `MARK^` flourishes, the same choice as `solve_l2.py`'s base-digit mode, and writes
`families/basecode_cipher.txt`: **N=229, K=26** (1-24 plus `07` and `29`, kept as transcribed). Even this K is two
above the 24-letter alphabet, so a strict simple substitution cannot fit the transcription as it stands unless `07`
and `29` are variants of other signs; each control drew K=19-21 (the most a 229-letter French window gives). The
controls are therefore at the target's N and design, but below its K -- they are easier than the target, not harder.

**Tool change.** `tools/families/masc.py` had no way to inject transcription error into its control, so a masc FAIL
could never bracket this target's measured 20.1-25.5% pass disagreement (rule 3, SALV-DIAG paragraph). Added
`--param noise=p`, the same redraw recipe as `homophonic.py`'s `noise=p` (its `_inject_noise`), default 0 unchanged;
offline test `tools/tests/test_masc_family.py` (ok, changed share 0.207 at noise 0.25); `tools/tests/test_family_run.py`
still passes.

**Runs** (`python3 tools/family_run.py specs/la-garde-1577.json --family masc --cipher
ciphers/la-garde-1577/families/basecode_cipher.txt --tokens space --seeds 3 --gate 0.6 [--measured-error 0.23 --param
noise=p] [--control-only]`; corpus the spec's two fr16 volumes; rows in HYPOTHESES.md):

| Control noise | Control recovery, seeds 1-3 | Mean | Gate 0.6 | Target |
|---|---|---|---|---|
| 0 (clean) | 0.948 / 0.978 / 0.983 | 0.969 | met | run: best score -572.867; judge **FAIL** (below) |
| 0.20 (below measured; tool warns non-test) | 0.777 / 0.332 / 0.585 | 0.565 | not met | not run (control-only) |
| 0.23 (= `--measured-error`) | 0.563 / 0.507 / 0.031 | 0.367 | not met | not run (CONTROL BELOW GATE, exit 3) |
| 0.26 | 0.310 / 0.297 / 0.406 | 0.338 | not met | not run (control-only) |

Judge on the clean-gated target decode (`families/masc-1-a2lag3masconbase.txt`), as `family_run.py` printed it:
`FAIL language: score=-1.208, null_p99=-1.601, real_p05=-0.96, real_median=-0.806, mode=both, N=229`. The decode is
gibberish ("osleeetereeenetornoute..."); the anneal's key gives five signs to `e`. The target's anneal score
(-572.9) sits inside the range of the noise-0.23 controls' own scores (-564.2 to -597.6), so it does not separate from
a correctly-keyed noisy control either. The control CAN differ from the target on the statistic (recovery and anneal
score both depend on the key and the token values the noise redraws), so this is a real control, not a non-test by
construction.

**Result: masc is untestable at N=229 and this transcription's measured error -- not a negative.** The clean control
reads 97%, so a clean masc at this N would be read; but at the measured error band (0.20-0.26) the control falls to
0.34-0.57, below its gate, and the target's FAIL is drawn from a clean control only. Grades: 0 cipher tokens read
(H 0, C 0, S 0, M 0, I 0). Note for the orchestrator, not acted on: WC-LAGARDE's `solve_l2.py` "control-backed
negative" for the same design rests on the target scoring below the noisy control, not on a noisy control meeting a
recovery gate (its own base-digit control read 28.6% at 22% noise); on `family_run.py`'s gate standard that earlier
negative would also read "not a test at this error". Status line unchanged (`open`).

**Where the ladder stands.** masc/homophonic and periodic via `solve_l2.py`: score-based negatives (see note above);
syllabary, wordcode, masc via `family_run.py`: controls below gate at the measured error. `running_key` is the one
family neither instrument has tried; `family_run.py` needs three corpus texts for it and the fr16 folder has two, and
its control will face the same N=229 and 20-25% error. The step that changes the picture is lower transcription
error (a better image, KHA A 11/XIV C/M-12, owner-side request) or more same-system ciphertext (Gachard, Correspondance
de Guillaume le Taciturne, unreachable 25 Sept).

**Next cheapest step:** ~~`running_key` through `tools/family_run.py` on `families/basecode_cipher.txt` with
`--measured-error 0.23` and a third 1570s French corpus text added to `tools/data/fr16`, control first, about $3;
expect the control to fall below its gate at this N and error, in which case the target waits for new material
(a better image to lower the error, or same-system siblings).~~ Superseded 3 Oct 2026 by GAPS145 (section below): `tools/data/fr16` already has three texts, but `running_key` cannot take this cipher (it joins numeric tokens into one digit string), so GAPS145 ran a design statistic instead.

Requests: none (no network). Vision: 0 reads, 0 subagent calls. New files: `build_basecode.py`,
`families/basecode_cipher.txt`, `families/masc-1-a2lag3masconbase.txt`, `tools/tests/test_masc_family.py`.

## GAPS145: index of coincidence against matched design controls (3 Oct 2026, account-4)

**Job:** the cheapest open follow-up after Y1 (1). Y1's (2), the unread clauses, has no key material. A2-LAG3 named
`running_key` through `tools/family_run.py` as the next step. A design check came first. `tools/families/running_key.py`
`solve()` joins each message's tokens with `"".join(m)`, so the base codes `15 16 22 ...` would become the digit string
`151622...`. It is a 26-letter Vigenere decoder, and it needs letter tokens in a known alphabet order. Feeding it this
cipher would test a guessed number-to-letter map, not the family. Instead this step asks a cheaper question that no
earlier pass asked: is the ciphertext's unigram profile the peaked profile of a one-sign-per-letter substitution, or a
flat one? The question is scripts only, uses no network and no vision, and does not depend on the solver's power.

**Intake gate:** `python3 tools/intake_gate_check.py la-garde-1577` -> `la-garde-1577: open (line 1) -- edition/page or
full-text-search citation found within 6 lines` (exit 0).

**Method** (`families/ic_design_check.py`, output `families/ic_design_check.tsv`, `--check` exits 0, seeded). The
target is `families/basecode_cipher.txt` (N=229, K=26; marks stripped). The controls are at the same N and in French
from `tools/data/fr16`, all three books:
(a) masc, 300 windows. IC does not change under substitution, so this is the window's own IC.
(b) running key (Vigenere, a plain window plus a key window from a different book), 300 windows.
(c) `tools/families/homophonic.py`'s own `make_control` at K=26, 40 seeds, clean.
(a) and (b) are each also run at the measured error 0.23, under two noise models. `profile` redraws from the
sequence's own unigram profile, the `homophonic.py` recipe. `uniform` replaces with a random other type, which is the
worst case for this statistic because it flattens toward 1/K.
The control can differ from the target on this statistic, because the designs separate. Under every noise model the
masc p05 lies above the running-key p95: the lowest masc p05 is 0.0565 and the highest running-key p95 is 0.0467. Only
the extreme tails touch (masc uniform min 0.0507, running-key profile max 0.0556). No shuffled-target control was run, because IC ignores token order and a shuffle would match by
construction.

| Design | Noise 0.23 | Mean IC | p05-p95 | Target IC 0.0420: share of controls below it |
|---|---|---|---|---|
| masc | clean | 0.0779 | 0.0689-0.0881 | 0.000 (min 0.0639) |
| masc | profile | 0.0795 | 0.0691-0.0929 | 0.000 |
| masc | uniform (worst case) | 0.0643 | 0.0565-0.0746 | 0.000 (min 0.0507) |
| running key | clean | 0.0409 | 0.0382-0.0445 | 0.740 |
| running key | profile | 0.0425 | 0.0390-0.0467 | 0.447 |
| running key | uniform | 0.0399 | 0.0376-0.0429 | 0.900 |
| homophonic K=26 | clean | 0.0464 | 0.0412-0.0518 | 0.075 |

**Result.** The target's base-code profile is flat. Its IC is 0.0420, below all 300 masc controls, including the
worst-case uniform-noise ones (lowest 0.0507). Stripping the marks merges signs, and merging can only raise IC, so the
true marked-sign profile is flatter still. **On this statistic a one-sign-per-letter substitution of French on the base
codes is excluded at this N and the measured error.** This is a design exclusion by a statistic that does not depend on
solver power, with its matched control beside it. It is not a solver negative. It also explains A2-LAG3's result: the
masc anneal gave five signs to `e` because a flat profile forces that. The profile fits running key (target at the
45-90th percentile) and is at the low edge of homophonic K=26 (7.5th percentile). It does not separate those two, and
it says nothing for or against a nomenclator or syllabary, whose IC depends on the code list. 0 tokens read
(H 0, C 0, S 0, M 0, I 0). The status line is unchanged (`open`).

**What this changes in the ladder.** masc on base codes moves from "untestable at this error (A2-LAG3)" to "excluded by
IC, control-backed". A better image no longer needs to re-test masc. Families still live: homophonic (only score-based
negatives so far, at `solve_l2.py`), running key or another polyalphabetic, nomenclator, and syllabary/wordcode (controls
below gate, WC-LAGARDE2). A running key in a 1577 Orange-party field letter would be unusual for the period. The numeric
sign set 1-24 looks like letter positions, but this is not tested here.

**Next cheapest step:** a periodicity test (IC by period 1-12 and the Kasiski / Friedman statistic on the base codes,
with running-key, periodic-Vigenere and homophonic K=26 controls at N=229 and error 0.23), scripts only, about USD 1.
It separates a periodic polyalphabetic from homophonic or running key. If nothing separates, the target waits for new
material: a sharper image of KHA A 11/XIV C/M-12 to lower the 20-25 % error, or more same-system ciphertext such as
Gachard, Correspondance de Guillaume le Taciturne.

Requests: none (no network). Vision: 0 reads, 0 subagent calls. New files: `families/ic_design_check.py`,
`families/ic_design_check.tsv`.


## GAPS149: periodicity test on the base codes (3 Oct 2026, account-4)

**Job:** GAPS145's named next step. Is the flat base-code profile (IC 0.0420) a periodic polyalphabetic, or an
aperiodic design such as running key or homophonic? The work is scripts only: no network, no vision, no subagents.
Intake gate exit 0 (same line as GAPS145).

**Pre-registration.** The decision rule was committed before any run: `families/periodicity_prereg.md`, commit
e33a96cd. For p = 1..20 the script takes IC_p, the mean unbiased column IC with token i in column i mod p, and the
excess E_p = IC_p - IC_1. Each E_p is z-scored against a pooled aperiodic null: masc, running key and homophonic K=26,
40 seeds each. The family-wise statistic is Z = max z_p over p = 2..20. The target counts as "periodic at p0" only
if three things hold:
1. Z is above the null's p95.
2. At least half of the multiples of p0 up to 20 have z > 2.
3. The periodic-Vigenere control at p0 detects its own period in at least 50% of seeds.

A miss excludes Vigenere only at periods whose own control detects at least 80% of the time. Script:
`families/periodicity_check.py`, output `families/periodicity_check.tsv`, seeded, `--check`.

**Controls.** All controls use fr16 at N=229, K=26 and noise 0.23. The aperiodic null uses the `homophonic.py`
profile-redraw noise recipe. Periodic Vigenere runs with a random key at p = 2..12, under both profile and uniform
noise. This statistic depends on token order, and a periodic control can differ from an aperiodic one on it, so this
is a real test (rule 3).

| | Target | Aperiodic null (120) | Vigenere controls (40 per period) |
|---|---|---|---|
| Max z, p = 2..20 | **1.93** (at p=7) | p95 3.13, max 4.68 | mean 3.9-8.4; target's percentile in them 0.000-0.050 |
| Friedman L_F | **10.6** | masc median 0.97; running key 9.0 (p05-p95 3.8-301); homophonic 4.8 (2.9-13.2) | 2.0-19.7 (median, by period and noise) |

Per-design rank of the target's Z: masc 0.43, running key 0.80, homophonic 0.63. The target's largest per-period z
are p7 +1.93, p18 +1.40, p9 +1.23 and p16 +1.22. None reaches 2, so the multiples rule never fires.

Vigenere detection rate by period (profile / uniform noise): p2 0.70/0.78; p3 0.93/0.88; p4 0.83/0.70; p5 0.98/0.95;
p6 0.58/0.43; p7 0.80/0.88; p8 0.73/0.70; p9 0.40/0.60; p10 0.70/0.68; p11 0.80/0.70; p12 0.60/0.43.

**Result.** Under the pre-registered rule there is no periodic signal (rule 1 fails: 1.93 < 3.13). A periodic
Vigenere on the base codes is **excluded, control-backed, at periods 3, 5 and 7**, where the control detects at least
80% of the time under both noise models. Periods 4 and 11 are excluded under profile noise only. Periods 2, 6, 8-10
and 12, and 13-20, are **untested** at this N and error, because their power is below 80%. Descriptively, the
target's Z falls below the 5th percentile of every Vigenere control at every period from 2 to 12.

Friedman L_F 10.6 does not discriminate. It sits at the running-key median and in the upper tail of homophonic (92nd
percentile), and it reflects the flat IC that GAPS145 already found. Caveat (pre-registered): the 11 dropped MARK^
flourishes, and any sign dropped or doubled in transcription, shift column phase. The controls model substitution
error only, so the exclusion holds conditional on no phase slips. 0 tokens read (H 0, C 0, S 0, M 0, I 0). Status
unchanged (`open`).

**Ladder now.** masc is excluded by IC (GAPS145). Periodic Vigenere is excluded at p3, p5 and p7, and untested at the
other periods. The surviving aperiodic designs, homophonic and running key, are not separated by IC, IC-by-period or
Friedman. Nomenclator and syllabary/wordcode stay open (controls below gate, WC-LAGARDE2).

**Next cheapest step.** None of the remaining statistics can separate homophonic from running key at N=229 and 23%
error. The next step needs new material:
- a sharper image of KHA A 11/XIV C/M-12, to lower the error and raise power at the untested periods; or
- more same-system ciphertext, for example Gachard, *Correspondance de Guillaume le Taciturne*, which would pool N.

A cheap scripted option is a contact/digram test (homophonic spreads a letter's bigram partners across signs; running
key gives near-independent bigrams), with matched controls at N=229, about USD 1. Its power at this N is unknown and
must be checked on the control first.

Requests: none. Vision: 0 calls. New files: `families/periodicity_prereg.md`, `families/periodicity_check.py`,
`families/periodicity_check.tsv`.

## R15-LAGDIG: contact/digram test, homophonic vs running key, power on the control first (6 Oct 2026, account 2, LANE-RUN15-account-2)

**Job:** GAPS149's cheap scripted option. Can a contact/digram statistic separate homophonic from running key at
N=229 and the measured error? Scripts only: no network, no vision, no subagents. Intake gate (lane orchestrator,
17:1x UTC): `la-garde-1577: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.

**Pre-registration:** `families/digram_prereg.md`, commit 5ecf5fd21, pushed before any run. The primary statistic is
Z_R, the repeated-bigram count (sum of C(n_b, 2) over adjacent bigrams) z-scored against 200 shuffles of the same
sequence. Shuffles keep the unigram profile, so Z_R measures order only. Adjacent mutual information (Z_MI) was
registered as descriptive and decides nothing. Controls, 40 seeds each:
- homophonic: `homophonic.py make_control`, K=26, fr16, `profile=target`;
- running key with a fr16 key from a different book (RK-fr);
- running key with a 17th-c. Dutch key from `tools/data/nl_repo` (RK-nl).

Noise was a profile redraw at 0, 0.10, 0.23 and 0.30. The gate: power passes only if AUC(Z_R) >= 0.80 against both
running-key variants at e=0.23. If power failed, the target would not be scored. Z_R depends on token order, so the
designs can differ on it (rule 3 check).

**Result (step 1, power, controls only):** `families/digram_check.py` (seeded, `--check` ok),
`families/digram_check.tsv`.

| error | AUC Z_R homo vs RK-fr | vs RK-nl | AUC Z_MI vs RK-fr (descriptive) | vs RK-nl |
|---|---|---|---|---|
| 0.00 | 0.977 | 0.949 | 0.996 | 0.983 |
| 0.10 | 0.934 | 0.906 | 0.981 | 0.962 |
| **0.23** | **0.759** | **0.710** | 0.885 | 0.843 |
| 0.30 | 0.679 | 0.710 | 0.759 | 0.774 |

Mean Z_R at e=0.23 is 1.19 for homophonic (p05-p95 -0.74 to 3.81) and 0.01 / 0.18 for the two running-key variants
(p95 1.35 / 2.06). **Power FAIL** (min AUC 0.710 < 0.80). The pre-registered primary statistic cannot separate
homophonic from running key at N=229 and 23% error. The target was **not scored**, and its Z_R was not computed. Up to
10% error the statistic separates the designs well (AUC >= 0.90), so this is another place where the transcription
error, not the method, is the limit. 0 tokens read (H 0, C 0, S 0, M 0, I 0). Status unchanged (`open`).

**Observation (not a result).** The descriptive Z_MI clears 0.80 against both running-key variants at e=0.23 (0.885 /
0.843), but not at 0.30. That was seen after the run, so under rule 3 it cannot be promoted to the gate here.

**Next cheapest step:** a fresh pre-registration with Z_MI as the primary statistic and new control seeds, about
USD 1, CPU only. It is a different instrument, not a re-tune of Z_R. Its power at the error ceiling is marginal: it
fails at 0.30, so the measured error band (20-25%) sits near its edge. If its power holds on fresh seeds, score the
target. Otherwise, as GAPS149 said, the target waits for new material: a sharper image of KHA A 11/XIV C/M-12, or
pooled same-system ciphertext.

Requests: none. Vision: 0 calls. New files: `families/digram_prereg.md`, `families/digram_check.py`,
`families/digram_check.tsv`.
