# Research director, wave 14 (18 Oct 2026, 06:1x UTC by date -u): program A, key-application test for sherwood-cossit-1781

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself, `tools/experiment_log.py --check`). The job ends its NOTES section with the six research-director questions in one
line each. Report what was found and where it was not found; no novelty class (rule 10).

## JOB SHERWOOD-PAGES (account 4; Opus 5.5; cap USD 6; box 60 minutes; hosts: recherche-collection-search.bac-lac.gc.ca / LAC finding aids (at most 10 requests), heritage.canadiana.ca (at most 25 requests, 1.5 s apart), loyalist.lib.unb.ca (at most 5); Price: vision calls: 8 x USD 0.5 + 1 reconciliation = 4.5)

CHECK-SHERWOOD (ciphers/sherwood-cossit-1781/NOTES.md) found the item unsolved: Brymner 1888 calendars "Sherwood gives a sketch of what he
understands by the cypher message of Cossit and Summer" (Add MS 21837 = B.177-2 p.84) and "Cypher messages brought in by Summer 345 to
347" (Add MS 21838 = B.178). Its premise check names a strong lead: the Haldimand service's book cipher keyed to the title page of *A List
of the General and Field Officers* (1778), which this repository already holds transcribed and reconciled:
ciphers/pro3055-clinton-1779/passes/title1778_reading.txt (30 lines) and passes/tomokiyo_key_pairs.tsv (Tomokiyo's line/letter cells;
credit Tomokiyo, Cryptiana haldimand.htm; Knepper via Friedman 1965; Leighton and Matyas 1985). Question: is the Cossit/Summer cipher
written in that system, and if so what does it read?
1. Locate: map Add MS 21837 and 21838 to a heritage.canadiana.ca reel (CHECK-SHERWOOD showed H-1649..H-1655 = Add MS 21804-21834, h1656
   absent, h1657 another fonds; use LAC's finding aid for MIKAN 105513 or the reel list, and the UNB Loyalist Collection's table). If not
   located within the request caps, stop, write what was tried, and name the route (an ASKS candidate line, not a row).
2. Fetch B.177-2 p.84 and B.178 pp.345-347 (find the page by the volume's own pagination; a few neighbouring images to find it are
   allowed inside the cap). Save to ciphers/sherwood-cossit-1781/images/ with images/manifest.json, under 30 MB. Cut line crops with
   `tools/iiif_lines.py --image <file> --out <dir>` (paste the command) and send only crops to vision calls, never a full image.
3. Describe the cipher's form (figure pairs? dots/slashes? words?) and Sherwood's sketch (written out, or only cited). Transcribe the
   cipher tokens as written (rule 2) with two blind passes if numeric, reconciled (`tools/reconcile_passes.py`).
4. If the tokens are figure pairs, apply the 1778 title-page key (line, letter-in-line) to every pair with a small script in the folder that
   regenerates the reading (rule 7; reuse pro3055's conventions, including its -1/-2 count-error note) and grade per token (rule 4). Matched
   control (rule 3): the same script on the same tokens with the key's line order shuffled (20 shuffles), reporting the share of English
   words for both, so a reading is distinguished from chance. If not figure pairs, say what system it looks like and stop.
5. NOTES.md "## Pages and key-application test (SHERWOOD-PAGES, 18 Oct 2026)": the reel and image ids, the form, the tokens, the reading
   (or why none) with grades and the control's numbers, a comparison with Sherwood's sketch if it is written out, and the next step.
Report: reel located or not, cipher form, reading share vs shuffled control, the next step, five lines.
