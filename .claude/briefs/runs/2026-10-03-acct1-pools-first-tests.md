# LANE-POOLS first cheap tests (account 1), 3 Oct 2026 22:3x UTC -- four pools, one worker each

Why: LANE-POOLS's check-solved pass (`.claude/briefs/runs/2026-10-03-acct1-pools-cs.md`) left four pools `partial` with the
intake gate passing and a named cheapest next step. CLAUDE.md Pipeline 3a: each gets a spec and ONE first cheap test with a
matched control, both numbers into the spec's `cheap_test_done`; the orchestrator promotes. Two pools were not sent on:
fr16104-vivonne-spain-1572 (>= 26 letters already carry a clerk decipherment, < 600 open signs flagged: below the pool bar) and
baluze167-davaux-1637 (5 undeciphered passages reported, the rest interlinear: likely below the bar).

Templates: `.claude/briefs/breadth.md` + the common tail in `.claude/briefs/README.md`; `TRANSCRIPTION.md` for the transcription
step. Model Opus 5.5 (you); subagents Sonnet, at most 3. **Cap USD 8, box 60 minutes** from your own `date -u`; per-unit pricing
(Usage 6): the unit is ONE page/leaf, at most 2 blind transcription passes + 1 reconciliation (3 subagent calls, ~USD 1.5 each)
plus the fixed ~USD 3 of reading and pushing. Stop before starting a unit that would cross 80% of cap or box. Crop step is
mandatory and pasted before the first subagent call: `tools/iiif_lines.py --ark <ark> --canvas <N> --out ciphers/<t>/images
--debug` (Gallica) or `tools/iiif_lines.py --image <file> --out ...` (a DECODE image); check the debug overlay; subagents get
only crop paths, never a full page.

Every job:
1. `python3 tools/intake_gate_check.py <slug>`; paste output in NOTES.md (exit 0 required; it was 0 at 22:2x).
2. `python3 tools/tool_shelf.py "<the step in words>"` once; name the tool used or why none fits.
3. Write `specs/<slug>.json` in the shape of `specs/fr4715-vieuville-pool.json` (slug, name, date, language_candidates,
   ciphertext (as transcribed, with source and date), ciphertext_source, alphabet, constraints, cheap_tests_in_order,
   matched_control, cheap_test_done, judge, value, written) and `ciphers/<slug>/` files: `ciphertext.tsv` (as transcribed, never
   silently repaired), the key file you used (`key.tsv` with its source), the script that regenerates your numbers.
4. Run test 0 below and its matched control. The control is a key-known-answer (decoded vs a period/printed decipherment of the
   same passage, token agreement) **and** a null (the same scoring with 200 shuffled keys -- a shuffle that CAN change the
   statistic, rule 3's orthogonality paragraph). Report both numbers side by side, the shuffle p95, and N. If the known-answer
   half fails its own gate, stop: "non-test at this transcription error" (rule 3 calibration paragraph), do not score the target.
5. Grade per token (rule 4: C where a period/printed decipherment gives the value, S cryptanalytic with control, M, I). Any
   candidate plaintext goes through `tools/judge_plaintext.py specs/<slug>.json --file <reading>` and the output is pasted
   (rule 7); state the corpus era match (no 16th-c. Spanish corpus exists: es17 is Cervantes-era -- say so, never treat its
   FAIL/PASS as decisive).
6. NOTES.md: append the result, update "## Remaining gaps"/"## Escalation"/Verdict, `python3 tools/gaps_check.py <slug>` OK line
   pasted. Do not touch QUEUE.md, POOLS.tsv, status.json. Do not run test 2.

Targets (your prompt names one):

A. **rah-juan-manuel-1521** (DECODE R9499-R9529, Juan Manuel to Charles V, 1521-22). Key: Tomokiyo 2025, on disk
   `sources/cryptiana/keys/AlonsoSanchez_2.tsv` ("mainly from the first page of the contemporary decipherment attached to DECODE
   record R9528"). Images: one DECODE browser login (`tools/decode_browser_login.js`; CLAUDE.md DECODE row; images NOT committed
   -- DECODE material is not public domain: keep them in your scratchpad, commit only crops' manifest and the transcription).
   Test 0: known-answer = the key on R9528 page 1 lines that carry the period interlinear decipherment (token agreement with the
   gloss -- note this is in-sample for Tomokiyo's table, so it calibrates transcription, not the key); target = a page of a
   different record with NO gloss (from the 2 with none, R9501/R9515, or an unglossed later page), Spanish word-cover of the
   decode vs 200 shuffled tables, N stated. Watch for the key being a sibling (Sanchez) table, not Juan Manuel's own: if
   CS-3's NOTES say otherwise, follow them and log it.
B. **es132-vargas-mexia-1578** (BnF Espagnol 132, Gallica btv1b10032556x). Third party: github.com/el-descifrador/cabinet-noir
   published 30 readings of this pool on 2 Oct 2026 -- re-check its git log first and pick only letters it has not read; credit it.
   Key: Cp.30 (Alcocer 1921, Devos 1950; Tomokiyo spanish3D.htm) -- where is it on disk? (`sources/cryptiana/keys/`, else
   cabinet-noir's `cle/` files are CC BY 4.0: cite and copy with attribution). Test 0: Teulet 1862 vol.5 prints the official
   Simancas decipherment ("Déchiffr. officiel") of Philip II to Vargas 19 Sept 1578 and 15 Oct 1578 -- the dates of f.89 and
   f.119 (CS-1: "Tomokiyo says contents differ, unchecked"). Transcribe one page of f.89 (or f.119), decode with Cp.30;
   known-answer = token agreement with Teulet's text where they overlap (if Teulet is a different letter, say so: that itself
   is the result, and score the decode by Spanish word-cover vs 200 shuffled keys instead).
C. **fr16144-savary-lancosme-1588** (BnF fr.16144, Gallica btv1b9060974c, ff.75-206). Step 0 (disk-only, ~10 min): finish the
   count CS-2 left -- Charrière IV whole-volume grep (already on disk or IA ngociationsdel04charuoft) for every Lancosme letter
   printed, matched to the folios; list which cipher letters have neither print nor a leaf decipherment. If fewer than ~2,000
   open signs remain, stop there and say so (pool fails the bar). Else test 0: the margin-decipherment page (canvas 380) through
   `tools/interlinear_align.py` (or a direct sign->letter table if the margin glosses sign by sign) to recover the Savary table
   (grade C); held-out known-answer = that table on a second glossed leaf (c324 or c340 clerk decipherment) scored against its
   gloss, vs 200 shuffled tables. Tomokiyo's table (henryiii.htm) is a second witness: compare.
D. **fr16142-noailles-constantinople-1571** (BnF fr.16142, Gallica btv1b9060927q, ff.109-275). CS-4 found NO cipher leaf in 3
   canvases and could not confirm the scout's canvas-160 claim. Step 0: survey -- `tools/gallica_folio.py` to map folio->canvas,
   then low-res (`full/600,/0/default.jpg`) one look per canvas across ff.109-275 in batches of 20 (contact sheets, one vision
   call per sheet): count cipher pages, glossed pages, clear pages. Read Charrière III footnote pages pp.522-524 (CS-4's named
   cheapest step). If fewer than ~2,000 open cipher signs, stop (pool fails the bar). Else test 0: align one glossed page to its
   gloss (or a Dupuy 521 clear extract matched to a cipher letter) to recover the table, held-out known-answer on a second
   glossed page vs 200 shuffled tables.

Good-citizen rule: one request at a time per host, >= 1.5 s apart (Gallica 2 s, browser UA); stop a host on 429/403/challenge;
one DECODE login per session. Never print credentials. Report request counts per host.

Done line (tools/room.py, role "LANE-POOLS FT-<A-D> (account-1 worker)"): `done (<start>-<end> UTC, brief met|box|cap):
commit <sha>. <slug>: test 0 <what>: target <number> vs control <number> (shuffle p95 <x>, N <n>); known-answer <x>; judge
<PASS/FAIL/n.a.>; gaps_check OK; requests ...; cost: see the lane ledger`. A result worth the owner's attention (a key opening
an unglossed letter above its control): one extra ROOM `flag` to LANE-POOLS with a one-line English gist marked as
interpretation. Report what was found and where it was not found; do not classify novelty.
