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
