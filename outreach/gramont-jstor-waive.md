status: ready
subject: Seven readings are at N4; run or waive their JSTOR rows so the outreach can go out (Gramont x2, Danzay, Thurloe P4, Lodewijk van Nassau x3)
to: you (no email; JSTOR-QUEUE.tsv or the local JSTOR runner)

Both Gramont readings (BnF fr. 2980 f.29r to Villandry and f.30 to Francis I, 20 May 1530) reached N4 at 07:03 UTC 24 Sept 2026: "no prior decipherment located" after the final-families audit (AUDIT.md 'N4 decision (final families)'; Camusat 1619 read page by page, DECODE searched, Champollion-Figeac, Sanuto, the open indexes). The one outreach gate still open is gate 2's JSTOR rows: 11 queued Gramont rows in JSTOR-QUEUE.tsv (lines 2-7, 27-29, 33-34).

Either (a) run them with the local runner on your PC (tools/jstor_runner_brief.md; the runner writes the hits column and sets status), or (b) waive them: set each row's status to `waived <date>` in JSTOR-QUEUE.tsv. Then the verification lane drafts the outreach notes (Tomokiyo and Lasry by email; an issue on the two solver repositories) for you to send. ASKS.md row 32.

Update 09:55 UTC: Danzay f.35r-36r (07:53), Thurloe P4 Stamford 1655 (09:25) and Lodewijk van Nassau 4610/4611/4616 (09:41) are N4 as well. Their JSTOR rows are in JSTOR-QUEUE.tsv under their folder names; the same choice applies to each: run with the local runner, or set the row's status to `waived <date>`. Waiving is reasonable: the open-index scholarship pass (OpenAlex, Semantic Scholar, CrossRef) found nothing for any of them, and the JSTOR rows are the same queries on a paywalled index.

Update 11:03 UTC: Blathwayt papers addenda, Huntington mssBLA 186 (cipher lines), 191(a) and 184 (ciphers/huntington-blathwayt-madrid-1728) are N4 as well (AUDIT.md 'N4 set (LANE W2 worker B1)'). Their six JSTOR rows are at JSTOR-QUEUE.tsv file lines 45-47 and 57-59; the same choice applies (run, or `waived <date>`). OpenAlex has not answered for this target (429 twice), so its open-index pass also needs a run or a waiver (ASKS row 40). BLA 186's clear text is printed (Rose, *Marchmont Papers* 1831, ii 414-15), which any note must state.
