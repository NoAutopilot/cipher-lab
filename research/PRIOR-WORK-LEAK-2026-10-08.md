# Prior-work leak study, 8 Oct 2026 (workflow wf_e1b87449-ccc, account-3 orchestrator)

Owner question: "Can we improve our chances of not solving already solved work?" -- and "must be applicable to other work not just Eckert".
Method: 14 readers over all 68 AUDIT.md files, one over ROOM/LEDGER/registers for internal duplicates, one inventory of existing gates; a design pass; four adversarial critics (coverage, false-block, generality, practicality); a revision. Records: research/PRIOR-WORK-LEAK-2026-10-08.tsv (307 rows; 3 withheld because they touch restricted material). Must-not-block cases: research/PRIOR-WORK-SURVIVORS-2026-10-08.tsv (72 rows).
All catch figures below are in-sample (fitted to the records that motivated the design); a leave-one-target-out replay must replace them before they are called predictive.

## Waste summary (final design pass)

**Counting**
There are 310 records as filed. Removing 3 duplicates and 5 survivors leaves 302: 124 Eckert and 178 non-Eckert.
- The duplicates are gramont A (a sub-span of gramont B), the second N2-L, and the pro3055 2894 Brymner credit correction.
- The survivors are 4992.3, 4982.1, E78, O9-BA and O9-BB.

The unit is still the record, not the item. E1-E20 is one record covering 16 entries, and internal sweeps cover 3 to 41 rows each. Percentages therefore depend on the unit, and the replay job below recounts in items.

By kind:
- prior print of the plaintext: 143
- period gloss or clear copy: 72
- duplicate of our own work: 49
- holder public transcription: 19
- prior decipherment: 14
- other: 5

Where caught (as recorded):
- premise: about 63
- solver: about 138
- first audit: about 77
- second audit: about 20
- later: 10
- unclear: 1

About 105 (35%) surfaced only after a reading existed and had been audited or reported. 13 second-opinion (SO) rows were withdrawn, and E6 and E12 reached the owner as 'never printed'.

**What the revised gate does with them (in-sample)**
295 of the 302 surface before reading.
- **282 blocked or routed.** These exit 3 (DONE), 2 (KNOWN) or 4 (owed one look, read or diff), or exit 0 with the work restricted to a listed residue. Roughly 130 of them are held only until one owed LOOK, LEAD or WEB answer is recorded; that is the gate's running cost.
- **13 flagged.** These are SUBSTANCE or KEY-SOURCE: decoding proceeds, but N3+ classes, SO rows and 'not located' sentences wait for the verifier's diff. This is exactly the withdrawn-SO shape: E26, E28, E29, N2-BL, O9-AK, O9-BC, E83, E84, E49, E54, E72, E73 and E70.

The remaining 7:
- 2 HOLD, which is the right answer (R9501, na-suriname 2039);
- 2 races caught only for the spend that followed (malsburg, hessen-1824);
- 1 missed (N2-BG, a memoir paraphrase);
- 1 out of scope (DEB-PRIV1, private repository);
- 1 correctly CLEAR (bowes D4).

The first design's 306/310 was wrong in two ways. It counted CONTEXT as caught, although CONTEXT never blocks. It also mixed 'blocked' with 'decided'.

**Generality**
- The family-independent checks (own-work, LOOK, holder/portal/solver repo, network, printed-cipher, consumer rule) surface 145 of the 178 non-Eckert records.
- The office-keyed edition scan adds 27, for 172 of 178. Those 27 rest on edition lists seeded with the very sources the records found late. The generality critique estimates that a surname title search would have found about 7 of them.
- The civil-war adapter carries 109 of the 124 Eckert records.

None of these is measured recall. Until the leave-one-target-out replay is run and published, the edition-scan numbers are fitted, not predictive.

**Dollars**
The records give about USD 1,600 avoidable, some of it estimated: clair349 174, spinelli 173, na-suriname 155, schonenberg about 107, eckert-1864 about 100, fr16142 about 90, pro3055 about 87, paget about 86, dupuy452 about 70, luzerne 64, dupuy468 60, hessen-daenemark 45, wvo-hessen 35, costabili 30, szembek 30, and dozens of USD 10-30 items.

Revised in-sample expectation, by what stops it:
- about USD 450 of post-catch grading: the consumer rule alone, with no new tool;
- about USD 480: network and WEB rows (spinelli, the na-suriname de Leeuw hit, dupuy452, dupuy468, morillo);
- about USD 300-400: LOOK (paget, schonenberg, wvo-hessen, szembek, luzerne, fr5160, part of clair349);
- about USD 40 spent plus three USD 60 lanes at risk: own-work;
- about USD 100 Eckert plus about USD 250 non-Eckert: the edition scan, in-sample.
Races cost about USD 160, and that stays unavoidable.

New running cost, which is an estimate until ledgered:
- LOOK: about USD 0.4-2 per manuscript item;
- LEAD reads: about USD 0.05-0.3 each;
- network: USD 0 in fees, but rate-capped;
- the OR/ORN index: a one-time build of about 60 volumes, each verified by title page and date profile, priced in its own brief.

**Build order (dollars avoided per build cost)**
1. The consumer rule.
2. The work_queue check in room.py --push. Absent today: tools/room.py never calls work_queue.
3. Done-marker and parallel-column fixes in next_steps.py and next_steps_fresh.py, plus the own-work core.
4. LOOK as the first priced step of transcription.
5. The holder, portal and solver-repository scan.
6. Tiered network and WEB rows.
7. Office-keyed edition sets, validated by replay.
8. The printed-cipher router.
9. The OR/ORN index, last.

**What stays unfixable**
(1) **Races.** No check before reading can see a reading that does not exist yet (malsburg, hessen-1824). Re-diffing before every brief only cuts the spend that follows.
(2) **Sources no index reaches.** Memoir paraphrases (N2-BG), and scholarship behind paywalls or cloud blocks (Kolosova, de Leeuw, JSTOR, HathiTrust full text, academia.edu, the msstate Grant Papers, books.google page view). HOLD and UNCHECKED-NET route these to the owner's runners. The gate cannot be complete from the cloud.
(3) **Edition recall on new targets.** It stays unmeasured until the replay runs. The replay itself needs full git history, and this checkout is shallow (checked 8 Oct 2026). The office-keyed sets and full-text derive queries should beat a surname search by an amount nobody has measured.
(4) **The model look.** The same visual question failed four times in the records (paget, wvo-hessen, clair349, clair1108). The per-line question, Opus escalation and 'a flag cannot be cleared by no-gloss' lower the risk; they cannot guarantee a letter-spaced or phrase-over-run gloss is seen.
(5) **Lending-only and in-copyright editions** (PUSG 10-12, Basler, Haynes, Bolivar 2021, de Leeuw). They give snippets only, so no date-line scan is possible and their verdict ceiling is LEAD.
(6) **Catalogue errors.** Where the catalogue's sender, recipient or date is wrong and the alternative queries (date+place, old cote, subscription) also miss, the result is still a silent CLEAR.
(7) **Private-repository duplicates.** These sit outside the public gate under rule 9a; the private session must run the gate itself.
(8) **Whole-ledger network search.** It cannot run under the good-citizen rule: eckert-1864's 893 segments x 12 requests is about 4,800. For ledgers, pre-read network catches move to G3, before the verifier. That saves the audit and SO cost, not the decode cost.
(9) **Wrong negatives already logged** in about 320 folders before positive controls existed (erving, bowes, the Lossen negative for lodewijk 172, janssens Opkomst). They are not re-validated unless the gate is re-run on those folders.
(10) **Unheaded decipherment sheets** near an item (nevers no.86 / no.87). They can only be attributed after transcription.
(11) **Clock and history skew across four accounts.** The gate reads origin/main and fails to UNCHECKED rather than guessing. It cannot make another account's unpushed work visible.

## Ranked checks

1. **Known-item routing with a named consumer** -- A rule in the gate's exit logic and in the brief templates.

- Exit 2 (KNOWN) becomes exit 0 only when --known-answer names a consumer: an unread item_id the key or grading will be applied to, or a gate named in a brief (gate:<name>).
- Grade refinement, corpus building or re-decoding on the KNOWN item itself has no consumer, so it stays at exit 2.
- A witness or cell-check purpose must first diff against any print already on disk.
- The rule applies per item and per scope, never as a target status. A target with an unglossed residue stays partial under rule 5, and that residue is its only workable scope (costabili P4 and the ~5,060-sign pool; hessen-daenemark codes 625, 602, 634 and 68).

The first design accepted any stated purpose. That would have admitted every post-catch job, since each had one ('C-grade the key', 'witness check'). When: brief-writing, and at every exit-2 result. Level: item and scope. Mechanism: script. Records caught (in-sample): 0. Cost: Seconds, USD 0, and no new tool beyond the flag.

It adds no catches: its roughly 12 records are counted under the checks that first find them. It does carry the largest single dollar line, about USD 450 of post-catch spend:
- schonenberg: about 87
- fr16142: about 90
- hessen-daenemark: 45
- paget
- costabili: about 30
- pro3055: six 2380/3868 cell jobs, about 28, run before anyone read the VHS print on disk
- birago no.24: F36-GLOSS, 18.33, scored X
- colbert26: DA1-COL, about 14.7
- fr15575
- the suriname 2061 re-decode. False-block risk: Low. Each of the roughly 55 deliberate known-answer records had a consumer:
- gramont f.18 graded the key.tsv that read f.29 and f.30;
- eckert-1862 T1-T10 fed the residue entries;
- fr3641 was a named control;
- es132's printed paragraphs were gate (a);
- vanbeuningen's print was a crib;
- N2-L checked the ledger key.
Remaining risk: a calibration whose consumer is a family control rather than an item. The gate:<name> form covers that case.

2. **Own-work and register gate (with fixes made where the registers are written)** -- **State.** The gate starts with git fetch and reads every file from origin/main, not the working tree. If the clone is shallow (this one is) and a needed line blames to a boundary commit, it runs --deepen for those paths; if that fails, the check is UNCHECKED. It prefers dated headings and ROOM tags over blame.

**DONE (exit 3)** needs typed evidence for the same volume + folio + canvas or unit range, one of:
- the artefact the step type itself produces, read from a per-folder ARTEFACTS.tsv that the shared tools write (current file conventions until it exists);
- a WORK-QUEUE done or bounced row;
- a '[done', '[x]', '[already run' or '[retired]' marker on that very bullet;
- a 'Job:'/'Brief:' line inside a done section.

**LEAD (exit 4)** comes from weaker evidence:
- Prose overlap with a later dated section or ROOM done line gives LEAD 'done-candidate' with file:line. This is the next_steps_fresh test, applied to both the next_step and the parallel column.
- A ROOM claim under six hours old with no done line, on the same slug and identifier, gives LEAD 'live claim'.

**Registers read:** NEXT-STEPS, SIBLINGS, LOOSE-ENDS, ZOOM-ASKS.tsv, specs/*.json, KEY-CROSSMATCH.tsv, WORK-QUEUE, ASKS, HUMAN-TX-ASKS, HYPOTHESES, ITERATE, NEAR, status.json, AUDIT.md, PROGRESS.tsv, and other folders naming the same shelfmark + folio or record id.

**Step types:** read, transcribe, decode, crop, lookup, audit, upgrade-audit, new-family-audit, propagate-revision, instrument, sweep, settle, handoff, index, queue, spec, lead.

**Fixes at origin:**
- next_steps.py treats done markers and back-references ('the Follow-up line above') as done.
- next_steps_fresh.py checks the parallel column.
- room.py --push and the dispatcher run work_queue.check().
- A worker that stops on DONE or KNOWN rewrites its source register line in the same commit. When: brief-writing; lane opening over NEXT-STEPS, SIBLINGS, LOOSE-ENDS, ZOOM-ASKS and the specs backlog; every WORK-QUEUE write. Level: item and step (volume + folio + canvas, or unit range). Mechanism: script. Records caught (in-sample): 53. Cost: 1-3 s offline after one git fetch (plus --deepen for the paths read when the clone is shallow), USD 0. A LEAD done-candidate costs the brief writer one read of the cited file:line.

It covers the 48 public internal duplicates, plus N2-AO and N2-BA (already mapped in AUDIT.md), pro3055 DIGBY and the 2380 conflicts (the VHS print was on disk), and malsburg f.12 (worked after found-solved).

Dollars: about USD 40 spent, plus three USD 60 lanes put at risk by one re-queued WORK-QUEUE row.. False-block risk: Low-medium, now that DONE needs typed evidence keyed on volume + folio + canvas. Prose overlap only ever gives a LEAD. Cases where it would otherwise misfire:
- R13-SURSWP4's new offset;
- D1A-B167's fifth passage, which became an N3 D2 item;
- DEB-PRIV1 part (d);
- baluze f.229, whose identifiers recur across D1-BAL170, D1A-B167, D4-B167 and AUD1;
- fr16104 vs fr16105 crops, and fr3252 vs fr4702 ff.36-37.
next_steps_fresh's 0.29 vs 0.30 margin on fr3789 shows how fragile its threshold is, which is why it never blocks alone.

propagate-revision, upgrade-audit and new-family-audit are never DONE (the E4/E5 routes to N4; birago no.77; nevers no.73/85).

Out of scope: the private repository.

3. **Leaf-and-neighbour LOOK as the first priced step of transcription** -- Answered first from images already listed in images/manifest.json.

**Tier 1:** the cipher page and its facing page, as 1200-1600 px native crops.

**Tier 2** runs when the volume's convention, a catalogue, Tomokiyo or DECODE hint, or tier 1 calls for it:
- 2 canvases before the item;
- the next 2-4, counted from the item's last leaf, plus one further piece;
- +-1 canvas around any folio that had to be resolved;
- every image of a unit of 8 or fewer (Arcinsys, DECODE);
- any catalogue-paired sibling;
- for maps, plans and lists, any item with the same subject and maker in the catalogue range.

**Neighbours** come from a per-holder adapter: Gallica canvases, Huntington ptr +-n, NA scan +-n, the WVO PDF page list, DECODE record images, Arcinsys aufn_*, RAH didl refs. For non-IIIF holders, the copy-order template asks for the neighbours along with the target.

**The question is asked per clear line next to a numeral run:**
- Does its letter or syllable count fit the run?
- Does the prose read on without it?
- Are the words letter-spaced?
- Whose heading or date does the sheet carry?
- What fraction is covered?

**Escalation.** Two Sonnet calls run per crop. Any disagreement, catalogue or scout flag, Tomokiyo hint, or 'Partially decrypted/solved' status escalates to one Opus call. A 'no gloss' answer never clears another source's flag.

**Attribution.** An unheaded sheet nearby is KEY-SOURCE nearby-sheet. A same-date docket alone never pairs a sheet with an item.

**Feedback.** --record writes gloss phrases into clear_words and reruns the edition and network checks. When: per manuscript item, as the first priced step of its transcription brief; at check-solved only for a single-letter target. Level: item (leaf and neighbours). Mechanism: script+model. Records caught (in-sample): 31. Cost: Tier 1 is 2 crops x 2 Sonnet calls, about USD 0.4-1.0, at an estimated USD 0.1-0.25 per call; ledger rows replace these figures once they exist. An Opus escalation adds about USD 0.5-1. Tier 2 runs only on a hint. Gallica region requests: 4-7 per item, 1.5 s apart.

It covers all 31 non-Eckert gloss and sibling records listed for the look, including the 2 nla records by looking back and fr16104 ink 50 by counting from the last leaf. Thurloe P14 has moved to the printed-cipher router.

Dollars: about USD 300-400 (paget 86, schonenberg about 107, wvo-hessen 35, szembek 30, luzerne 64, fr5160, part of clair349).. False-block risk: Low-medium.
- Show-through: nevers no.90 f.185r L15.
- Stray letters that contradict the key: WVO 126 'e e r e'.
- Partial glosses give KNOWN-PART with the covered fraction: fr16104 ink 54 has about 60 letters over about 1,950 tokens.
- A sheet whose heading names another item is a KEY-SOURCE, not KNOWN (no.86 vs no.87's sheet; fr16104 ink 51 docket vs ink 53).
- The civil-war adapter ignores later pencil over route, blind and check words (E47, N2-R, N2-AZ).

Residual risk: a model can still miss a gloss shape it missed before. This is not fully fixable.

4. **Holder, portal and solver-repository leads** -- Each sentence is classified, not each field, with a negation and partial lexicon (sans, not, un-, niet, gedeeltelijk, partly, en partie, 'no deciphering appended', 'key not found'). Only entries anchored to the item count: shelfmark, item number and folio on one parsed entry. A note written for a whole volume is CONTEXT.

Shelfmarks match fuzzily ('5232' for 3252), and folios match within +-2 across the finding-aid, ink and Tomokiyo foliations. A fuzzy match is LEAD, never KNOWN.

Per source:
- **Print codes in a holder record** (WVO GPA, GPAS, GSME, LMSAC, DNOK, JC, 'Japikse ... nr.', Groen, Fruin) are pointers: LOOK edition-page, never KNOWN by themselves. 'Collectie Japikse' and other unseen copies are CONTEXT unseen-witness.
- **RAH:** 'Copia del ... cifrado' or 'Es copia conforme' gives LEAD, settled by one text-leaf check. 'Copia, en cifra' gives CONTEXT.
- **DECODE:** the listing's status and page count are LEADs to LOOK. 'Cleartext Publication' and 'Transcription' documents with a <PLAINTEXT> tag are LEADs to fetch, batched through one browser login per session. 'Partially decrypted' (and HCPortal 'Partially solved') gives KNOWN-PART, with the residue taken from the documents and the image.
- **Tomokiyo mirror (cp932):** 'deciphered' or 'attached' gives KNOWN for that folio. 'can be read with' gives KEY-SOURCE published. 'not deciphered' or 'undeciphered' is no evidence.
- **Solver repositories:** KNOWN only from a reading file for this shelfmark and folio, dated before our reading and not citing cipher-lab, our issues or our folders. A directory name or a catalogue or planning line is CONTEXT duplicate-effort-risk. The repositories are re-diffed before every brief.

**Freshness:** solver clones after 48 h, and the Tomokiyo page, DECODE row and HCPortal record after 7 days, are UNCHECKED offline and refreshed in network mode. When: intake, and before every brief (the solver-repository re-diff). Level: item. Mechanism: script. Records caught (in-sample): 35. Cost: Seconds. 0-3 requests (cached mirror and clones, plus one catalogue or CONTENTdm record), USD 0. DECODE document fetches are a separately priced step: one browser login per session.

It covers:
- WVO print codes, via the opened page: lodewijk 5811/4503/5810/5797 and jvn 5200/5218/5222;
- Discovery scopeContent;
- the printed BnF catalogue's 'avec chiffre et dechiffrement' (birago no.24);
- DECODE/HCPortal: decode-1162, costabili, hessen-daenemark x2;
- the Tomokiyo mirror: gramont, R9502, nevers no.87, pro3055 3050/3077, fr4715, fr3641, fr4712, fr16142 A;
- catalogue notes: luzerne x2, antt-fcc, xiquena, pisany x3;
- solver repositories: royalist, plus the post-race spend on hessen-1824 and malsburg.
33 non-Eckert, 2 Eckert. The Huntington clear-share test has moved to the civil-war adapter.. False-block risk: Medium-low once sentences are classed, entries are anchored and print codes are only pointers.

Status words mislead in both directions:
- DECODE R2761 'Decrypted' is a key only;
- R9502 'Non-decrypted' has a decipherment page;
- R361 'Non-decrypted' carries a Cleartext Publication document.

Catalogue scope:
- fr3416 f.35 is 'avec chiffre', while f.38 is 'avec chiffre et dechiffrement';
- the fr5160 notice is written for the whole volume.

Solver repositories: Bourdeau's gramont1529 folder reads fr.3091 and fr.3071, not f.29/f.30. His espagnol 144 f.22 page copies our issue 16 and is excluded.

5. **Network identity search and WEB rows (tiered)** -- **Tiering.** Runs at check-solved for single items. For pools and ledgers it runs only on the CLEAR residue of the next batch about to be read, at most about 25 items per session. The rest of a ledger runs at G3, before the verifier.

**Transport.** print_check is used as a library through its own Net subclass and writes only to prior-work.tsv:
- a per-item 403 on archive.org/download (a lending-only djvu) falls back to be-api and does not block the host;
- a 5xx or a reset gets one retry after a pause, then UNCHECKED-NET;
- a true host block stops that host for the run.
Limits: at most 12 requests per item, 1.5 s per host.

**Queries:**
- shelfmark strings and old cotes;
- sender + recipient + year + the cipher word in the item's language, in full text (be-api; Google Books with key and country=US; gbooks_search_within);
- clear-word phrases and code-value pairs;
- OpenAlex and CrossRef;
- loc.gov search JSON and the item country's press APIs, with coverage read from the API and a cap of about 30 per session;
- portal databases: Aerztebriefe, EMLO bibo_Note, the HCPortal API.

**Verdicts.** A hit with the date and both correspondents, a shelfmark string, or the cipher word with the sender is LEAD. The item's own content is KNOWN. Anything else is CONTEXT. Every family row carries a positive-control query against the same host and edition. A missed control gives UNCHECKED-NET, never CLEAR, and 'unreachable' must quote the catalogue_ladders route that was tried.

**WEB rows** (Cipherbrain, Cipher Mysteries, Cryptiana, Reddit r/codes, Wikipedia talk) are LOOK kind=web, exit 4 until recorded. Each has a same-blog positive control, and our own repository and outreach text are excluded. A blog claim is CONTEXT claim until both plaintext and method are published and reproducible.

**Sharing.** Rows are committed with a 14-day valid_until, so the other accounts reuse them. When: check-solved for single items; the next batch's CLEAR residue for pools and ledgers; G3 for the rest of a ledger. Level: item. Mechanism: script+model. Records caught (in-sample): 19. Cost: 6-12 requests, 30-60 s, USD 0 in API fees. A WEB row costs about USD 0.05-0.2. Before this is wired into check-solved, the Google Books project quota is recorded in KEYS.md.

It covers:
- non-Eckert: spinelli (WEB), the na-suriname de Leeuw shelfmark hit (LEAD), dupuy452 x2, dupuy468, morillo item 3 (after LOOK feedback), janssens 188, oxenstierna (editor's-note row), trew 1618, digby (Wheatstone), erving (with a positive control), bowes D1 (code-value pairs), lodewijk 172 (KNOWN-PART, blank scope);
- Eckert: E36, E65, plus E26, O9-BC and E29 as SUBSTANCE.

Dollars: about USD 480.. False-block risk: Medium. Name collisions: Senisteros, 'capitano Scipione', 'Advis de flandres', 'Captain Feilner' with 93 hits, 'dem printzen zu hispanien' with 300 hits.

Citations without text are CONTEXT, or KNOWN-PART when they concern the same letter's clear part: Delavaud fr.20140 fos 16-56, Pascal fol.21, Glawischnig on JvN 5551, Gerard on fr.3416 fol.35, d'Ars on fr16104 ink 63.

A transient 429 or 503 gives UNCHECKED-NET, never HOLD (baluze170 f.229).

6. **Office-keyed edition and calendar identity scan at three gate points** -- **Composition.** Edition sets are keyed by office/post, date span and language, not by holder. They are seeded from KEY-OFFICES.tsv (70 rows with office, correspondents, years and language) and from each family's existing NOTES.md. An item gets every set that matches.

Each edition-volume row carries:
- identifiers verified by title page and date profile;
- date span and language;
- access tier (djvu, be-api-only, snippet, htrc-ef, none);
- segmenter (calendar-number, groen-lettre, footnote, or-dateline, birch-heading);
- a positive-control letter; a missed control voids the row.

**Matching.** Dates are generated per language and era: Roman-numeral days, feast days, o.s./n.s. by country and year, regnal years, the Republican calendar. Names go through an office/title alias table.

**Routes:**
- (a) Date +-1 day, the same sender and the same recipient in the same direction, and content cover of the clear words or holder surrogate above a pair-local control: KNOWN.
- (c) Content only, with no date or correspondent: LEAD.
- A translation: LEAD.
- A numbered calendar entry without a surrogate: LEAD 'read entry N before transcribing'.
- A same-letter print of the clear part only: KNOWN-PART, with the cipher spans as the residue.
- A reply or antecedent: CONTEXT.
- A print within +-3 days that names a correspondent and shares 2 or more rare entities: SUBSTANCE.
- An undated item: LEAD, not CLEAR.
- Snippet tier: capped at LEAD.
- A catalogue-only sender or recipient adds date+place, old-cote and subscription queries. When: G1 before transcription (identity plus holder surrogate); G2 after the clear frame is transcribed and before keying; G3 after decode (--reading). Level: item. Mechanism: script. Records caught (in-sample): 27. Cost: For the cached-text tier, 1-5 s offline against a committed compact index per family, USD 0. Fts-only and snippet sources are priced as network rows.

One-time cost per edition volume: verify identity by title page and date profile, and run its positive control. Building the volume lists was error-prone even for Eckert (431unit vs _0; ser. III vol. 4 missing).

It covers 27 non-Eckert records, in-sample:
- jan-van-nassau 5213/5221/5207; pro3055 2894 body/3868/2380/3853;
- vanbeuningen; thurloe P10 L10 (Powell); blathwayt 186 (LEAD); bowes A/B/D2/D3;
- janssens No.4/No.5; fr3621; morillo 1; clair349;
- es132 x2; rah-salazar 1/3/5; digby; fr16142 B; gunther.

Dollars: about USD 250, in-sample.. False-block risk: Medium, and lower than in the first design:
- direction-matched correspondents keep the antecedents and replies of E5, E47, E62, N2-T and N2-BM out of KNOWN;
- content-only and misdated matches are LEAD, never KNOWN;
- same-letter clear-part calendars (fr3621 f.130, WVO 57) give KNOWN-PART, not KNOWN.
Same sender, recipient and month, different letter: CONTEXT unless overlap beats the pair-local control (gramont f.30 vs ASI: longest run 18 vs controls 9-11; manteuffel f.410; espagnol142 Lonchay no.183).

Recall on new targets is unmeasured: the replay is required.

7. **Printed-cipher span router (Birch-type editions; separate spaced-type and silent-roman detectors)** -- Cut heading-to-heading spans and read the sender from the heading above the cluster, never from the preceding signature.

**KNOWN** when either:
- the span has at least one exact-length neighbour line and its per-group letter votes beat a within-span shuffled-line null (check_interlinear.py --votes, scored against that null); or
- the negation-aware decipher-word regex fires inside the span.

**LOOK page-image (one call)** when numerals are present and neither test fires.

**KNOWN-PART** when numerals are printed undeciphered, blanks are left, or '(Cypher.)' is printed: those spans are the residue.

**Editor's note.** A note saying 'not deciphered / key not found' adds a required row searching the national historical journal and reviews of the edition, from the edition's year to +10, before CLEAR.

**Other print conventions** have their own detectors: Japikse's spaced type, and Groen's silent roman stretches. When: before extraction or decode of a printed-pair item. Level: item (letter span). Mechanism: script. Records caught (in-sample): 23. Cost: Seconds on the cached djvu, USD 0, plus one page-image LOOK call (about USD 0.2-0.5) for each span with numerals where neither test fires.

Measured 8 Oct 2026, exact-length neighbour lines: P4 0/10, P8 1, P16 2, P17 13, P21 2, P22 4, P23 3, P24 6; P3, P6, P7 and P10-P15 have 0. The raw vote majority share does not separate on its own (P17 0.33 over 290 votes; P5 0.94 over 17), so the null is required.

It covers all 23 Thurloe items. 16 of them had been misattributed by the nearest-heading trap.. False-block risk: Low. P4 has no exact-length line, so it cannot be KNOWN. One LOOK call returns it CLEAR, even though P5-P7 in the same volume are KNOWN.

Veenendaal no.92, the Groen blanks in 5797 and the jan-van-nassau 5549 body all give KNOWN-PART with their spans as the residue, never KNOWN.

The within-span null has not yet been computed. Until it is, the share threshold is not set, and the test reports the null rate beside the share.

8. **US Civil War telegram adapter (OR/ORN compact index, telegram identity, clear-share with classed key)** -- **Index.** One committed index is built from about 60 OR, ORN, PUSG and related volumes, each verified by title page and date profile. It holds date lines with hour, from, to, page and offset, plus rare 3-gram postings, so neither the full texts nor a regex over 60 volumes is needed per item.

**Routes:**
- (b) Telegram identity: one entry with the same date, hour within 30 minutes, the same sender and the same recipient gives KNOWN. Two or more candidates, or a one-day offset, gives LEAD, resolved first by a scripted diff of the clear words and by the model only when that is ambiguous.
- Full and content-only routes as in check 6.
- SUBSTANCE for other-officer or other-addressee prints that share 2 or more rare entities.

**Clear-share test** (moved here from the core). Each key-book row carries a class: person, place, title, number, date/time, signature, vessel, blind or content.
- Plaintext scope: KNOWN when the residue holds no content-class token.
- Code-value scope: KNOWN only when each residue value is itself in print (the DCW list); otherwise KNOWN-PART with the residue listed.
- A key without classes makes the test UNCHECKED.

**Normalisation.** Telegraph normalisations (number words, the clerk's '=' and phonetic splits) live only here.

**Tiers.** PUSG 10-12 and Basler are lending-only: be-api presence only, ceiling LEAD. For ledgers the network pass moves to G3. When: G1 for ledger entries with a volunteer transcription or other clear words on disk; G2/G3 for the rest. Level: item (ledger entry). Mechanism: script. Records caught (in-sample): 109. Cost: Building the index is a one-time job, priced in its own brief, including the identity verification that LS-PRE did by hand (the 431unit, 502unit and 522unit errors; OR ser. III vol. 4 and ORN 11/26 were missing). After that: 1-5 s per entry offline, USD 0.

It covers 92 records by the index:
- 74 eckert-1864 and 18 eckert-1862;
- about 12 of them LEAD and 9 SUBSTANCE (E72, N2-BL, E83, E84, E49, E54, E73, O9-AK, E28).
It covers 17 more by the clear-share test: 16 Huntington transcriptions and 1 DCW row. E81, E82, E76 and N2-BQ are routed to residue-only work.

Dollars: about USD 100, mostly in avoided verifier passes and the 13 withdrawn SO rows.. False-block risk: Medium.
- Halleck often sent Grant several telegrams on the same day, so the hour is required and more than one candidate gives LEAD.
- Ledger and print hours differ (E25: 12.30 vs 12.20; 4999.2 is printed a day earlier).
- Replies and antecedents (E5, E47, E62, N2-T, N2-BM) are CONTEXT or SUBSTANCE, never KNOWN.
- LS-PRE's false hit on N2-M (warofrebellion392unit, cov15) is LEAD, never KNOWN.
- 4992.3 is KNOWN-PART for 'Sermon', never KNOWN.

## Gate specification (tools/prior_work.py)

**Purpose.** A per-item, per-scope prior-work gate for any item: a letter, a leaf, a ledger entry, a DECODE record, a printed-pair span, a code value, a blank, or a step taken from a register.

Before a job transcribes, keys, decodes, aligns, crops, looks up or audits an item, and again after decode before any novelty wording, the gate answers whether that item or step has already been read, and by whom:
- by us;
- by its period clerk (a gloss or clear copy on the leaf or a sibling);
- by its holder (a transcription or catalogue note);
- by an edition or calendar of the correspondents' office and period;
- by the press;
- by a scholar;
- by a solver repository or portal.

It is general by composition, not selection. Every item gets the core, plus every matching holder route, portal route and office-keyed edition set. Eckert is one adapter among many: the civil-war adapter, which holds the telegram-specific machinery.

Every verdict carries evidence. A check that did not actually run is reported as UNCHECKED, never as CLEAR. Known items are routed to residue-only or consumer-named known-answer work, not refused. The gate says 'worth a read' or 'already read'; it never assigns novelty, which stays the verifier's under rule 10.

Its in-sample catch figures are fitted to the records that motivated it. A leave-one-target-out replay must replace them before it is described as predictive.

**Inputs.** **Items.** ciphers/<slug>/items.tsv, written by check-solved in the same commit as its verdict. Columns:
- item_id, shelfmark, volume, folio/leaf/canvas;
- record ids: DECODE R-id, HCPortal, WVO nr, ptr, inv./scan;
- the date as written and normalised (calendar noted);
- sender, recipient, office/post, place, language;
- item kind: correspondence, ledger entry, printed pair, map/plan/list, diary, anonymous, or modern/press;
- the holder record URL;
- an optional clear_words file;
- a verified-from-leaf flag for every field.

--derive exists only to backfill existing folders. It proposes rows into items.pending.tsv, marks every field catalogue-only, and one model review accepts them. Step mode instead takes --brief FILE or --register FILE --columns ..., and parses item keys with tools/shelfmark.py.

**Registries.**
- catalogue_ladders.tsv, with the new prefix column. Holders it lacks today: Simancas, ASMo, HHStA, Riksarkivet, Kornik, NRS, Lambeth, NLA, KHA, the Italian archives, BL Add/Cotton/Harley.
- prior_portals.tsv: DECODE, HCPortal, WVO, the DCW blog, Zooniverse, the Tomokiyo mirror, the solver repositories.
- prior_editions.tsv, one row per edition volume: office/post, date span, language, verified ids, access tier, segmenter, and a positive-control item.

Initial sets are seeded from KEY-OFFICES.tsv and from a grep of each family's NOTES.md. They include:
- the civil-war adapter;
- bnf-French-embassies;
- spanish-flemish;
- tna-16c and tna-18c (SP 104/107, BL Newcastle Add MS, Coxe, Hardwicke, HMC);
- haldimand-canada;
- wvo-orange;
- nl-colonial (4.VEL, 1.04, 1.05, 2.01: AMH, Opkomst, den Heijer via NA 2.14.97 IIIF, de Leeuw, Colenbrander);
- rah (Rodriguez Villa, CSP Spain, the Salazar Indice);
- pt (ANTT, the Linhares editions);
- de (Acta Borussica, RTA, Politische Correspondenz, Aerztebriefe, HCPortal, Arcinsys);
- printed-cipher (Birch-type);
- sweden (Riksarkivet, Historisk tidskrift, Handlingar);
- italy-poland-swiss (Sanuto, Nuntiaturberichte, Acta Tomiciana);
- us-early-republic (Founders Online, the Madison and Monroe papers, Weber);
- wwii (TNA HW, NARA RG 457);
- unattributed;
- modern/press.

**Local state.** Read from origin/main:
- AUDIT.md, status.json, PROGRESS.tsv, NEAR.md, NOTES.md, ROOM.md;
- WORK-QUEUE.tsv, ASKS.md, HUMAN-TX-ASKS.tsv, ZOOM-ASKS.tsv, KEY-CROSSMATCH.tsv, specs/*.json;
- HYPOTHESES.md, ITERATE.md, NEXT-STEPS.tsv, SIBLINGS-*.tsv, LOOSE-ENDS-*.md;
- images/manifest.json, ARTEFACTS.tsv, passes/;
- sources/cryptiana/web, the solver-repository clones (with HEAD date) and the committed per-family indexes.

**Flags.**
- --offline: the default at brief-writing; it reads cached network rows still inside valid_until.
- --network
- --strict: makes UNCHECKED-NET blocking.
- --point {intake,brief,clear-frame,post-decode}
- --reading FILE: gate point G3.
- --known-answer CONSUMER
- --step-type, with the extended list in step 3.
- --record ROWID ANSWER: answers LOOK, LEAD and WEB rows.
- --learn
- --derive

**Outputs.** **ciphers/<slug>/prior-work.tsv**, append-only and checked by file_shrink_guard. Each row holds:
- item_id, scope, check, family, route, query;
- the positive-control result and the hits;
- evidence of 200 characters or fewer with file:line or URL, keeping the content rather than eliding it;
- the verdict and the requests per host;
- valid_until, the UTC date, and the origin/main commit that was read.

**Verdicts per scope.** Scopes are plaintext, clear-part, cipher-spans, code-values, blank-spans, key/mapping and step.
- **DONE**: typed evidence that the step is already done.
- **KNOWN**
- **LOOK**: kind image, web or edition-page.
- **LEAD**: one read or diff is owed. Sub-types: done-candidate, live-claim, telegram-ambiguous, content-only, translation, calendar-entry, shelfmark-hit, fuzzy-match, snippet-tier, copia.
- **UNCHECKED**: a required pre-read family produced no usable row. Causes: not run, uncached, 5xx, stale clone or mirror, shallow blame, no holder route, a key without classes, or a missed positive control.
- **UNCHECKED-NET**: a network family did not run. It warns at brief time and blocks under --strict and at G3.
- **HOLD**: only for a printed or scholarship source with a positive pointer and a queued route. It names one parallel action and lapses to a logged gap after 14 days.
- **KNOWN-PART**: with the residue listed.
- **SUBSTANCE**
- **KEY-SOURCE**: published, or a nearby sheet.
- **CONTEXT**: tagged as reply, antecedent, event, citation, regest, unseen-witness, claim, duplicate-effort-risk or volume-note.
- **CLEAR**

**Item exit code.**
- 3: the step is DONE.
- 2: every scope the brief would work is KNOWN and no valid consumer is named.
- 4: any scope that would be worked is LOOK, LEAD, UNCHECKED or HOLD.
- 0: otherwise, with the work restricted to the CLEAR and KNOWN-PART scopes and their listed residue.

**Other output.**
- A predicted N-class, written for the plaintext scope only and never passed to the verifier.
- A paste block, which is informational and not gate evidence.
- A --json form for status.json and verify_backlog.
- look.tsv listing the crops owed.
- On a block, one ROOM line through room.py.

**Steps.**

- **0. Read current state.**
- Run git fetch and read every file from origin/main (git show, or a scratch worktree). The user's checkout is never modified.
- If the clone is shallow and a needed line blames to a boundary commit, run git fetch --deepen for those paths. If it still does, that check is UNCHECKED.
- Prefer dated headings, ROOM tags and WORK-QUEUE ids over blame.
- Report the age of each solver clone (HEAD date), of the Tomokiyo page that names the shelfmark, of the DECODE listing snapshot and of the HCPortal record. Past 48 h for clones, or 7 days for the others, the row is UNCHECKED offline and refreshed by one If-Modified-Since request in --network mode.
- **1. Resolve items.**
- Read items.tsv. For existing folders without one, --derive proposes rows into items.pending.tsv, marked catalogue-only, for one model review.
- In step mode, parse keys with tools/shelfmark.py. Leaves are keyed on volume + folio + canvas, never folio alone, because one folder can hold fr.16104 and fr.16105, or fr3252 and fr4702 ff.36-37.
- The normaliser covers:
  - BnF fonds and old cotes (Anc. 8565 = Bethune 8565 = fr.3040);
  - BL, TNA SP/PRO, RAH 9/, AGS, ASV, BNE;
  - WVO nr, NA 1.xx/2.xx/3.xx/4.VEL inv./scan, KHA, HStAM, SHStA Loc.;
  - Huntington ptr/mss, Birch P/vol/page;
  - ANTT PT/TT, Riksarkivet, Kornik BK;
  - HCPortal ids and DECODE R-ids.
- **2. Compose the item's sources.**
- Every item gets the core, plus every matching holder route (catalogue_ladders prefix), portal route and edition set (matched on office/post, date span and language).
- A DECODE id adds the portal; it never replaces the holder.
- An unmapped holder prefix is UNCHECKED 'no holder route'.
- A correspondence item with no matching edition set is a 'core only' warning, counted at every lane opening. check-solved clears it by recording either the editions it read or 'no sender-side or recipient-side edition exists (families searched: ...)'.
- Anonymous, diary and modern items go to the unattributed or modern/press families, matched by shelfmark and content only.
- **3. Own work (offline, always).**
- DONE comes only from typed evidence for the same unit:
  - the artefact the step type produces, from ARTEFACTS.tsv (written by the shared tools: unit, step, file, date), or from the current file conventions until it exists;
  - a WORK-QUEUE done or bounced row with the same id;
  - a '[done', '[x]', '[already run' or '[retired]' marker on that bullet;
  - a 'Job:'/'Brief:' line inside a done section.
- Prose overlap alone gives LEAD done-candidate with file:line. That covers a later dated NOTES section or ROOM done line sharing the step's identifiers, on either the next_step or the parallel column.
- A ROOM claim under 6 h old with no done line, on the same slug and identifier, gives LEAD live-claim.
- Step types: read, transcribe, decode, crop, lookup, audit, upgrade-audit, new-family-audit, propagate-revision, instrument, sweep, settle, handoff, index, queue, spec, lead.
- propagate-revision, upgrade-audit and new-family-audit are never DONE. A re-audit is refused only when it repeats the families an existing audit already searched.
- Private-repository work is out of scope: the private session runs this tool in its own checkout.
- **4. Holder, portal and solver-repository leads (cached, or 0-3 requests).**

General rules:
- Classify each sentence with the negation and partial lexicon.
- Accept only entries anchored to the item. A note written for a whole volume is CONTEXT volume-note.
- Shelfmarks match fuzzily, and folios within +-2 across foliation systems, with the system recorded. A fuzzy match is LEAD.

Per source:
- **Print codes in a holder record** (WVO GPA, GPAS, GSME, LMSAC, DNOK, JC; 'Japikse ... nr.'; Groen; Fruin) give LOOK edition-page: open the cited pages and run step 6. They never give KNOWN by themselves. Unknown codes are resolved through WVO's abbreviation list or flagged. 'Collectie Japikse' and other unseen copies are CONTEXT unseen-witness.
- **RAH:** 'Copia del ... cifrado' or 'Es copia conforme' gives LEAD copia (one text-leaf check). 'Copia, en cifra' or 'Copia ... cifrada' gives CONTEXT.
- **DECODE:** the listing's status and page count give LEAD to LOOK. 'Cleartext Publication', a 'Transcription' with a <PLAINTEXT> tag, or a published paleography study gives LEAD to fetch, batched through one browser login per session as a separately priced step. 'Partially decrypted' and HCPortal 'Partially solved' give KNOWN-PART, with the residue from the documents and the image.
- **Tomokiyo:** 'deciphered' or 'attached' gives KNOWN for that folio. 'can be read with' gives KEY-SOURCE published. 'undeciphered' is no evidence.
- **Solver repositories:** KNOWN only from a reading file for this shelfmark and folio, dated before our reading and not citing cipher-lab, our issue numbers or our folders. Directory names, catalogue lines and planning lines are CONTEXT duplicate-effort-risk.
- **Holder public transcription:** the clear-share test runs only in adapters that supply a classed key (civil-war). Everywhere else, the DECODE <PLAINTEXT> tag or a scopeContent clause gives KNOWN-PART for that span.
- **5. Edition and calendar identity scan** (offline over the committed per-family index; at G1, G2 and G3).

Inputs:
- Dates come from a generator per language and era (Roman-numeral days, feast days, o.s./n.s. by country and year, regnal years, the Republican calendar).
- Names go through the office/title alias table seeded from KEY-OFFICES ('Madame' = Louise de Savoie; 'Evesque de Tarbe' = Gramont).
- Before reading, content is the holder surrogate: Discovery scopeContent, WVO Inhoud, a BnF analysis, a DECODE description, or a CSP or Brymner abstract. At G2 it is the clear frame or subscription. At G3 it is the decoded reading.

Routes:
- (a) Date +-1 day, the entry's sender equal to the item's sender and its recipient equal to the item's recipient, and content cover above a control built from that pair's adjacent entries in the same volume: KNOWN.
- (b) Telegram identity (adapters with hour lines): see check 8.
- (c) Content only, with no date or correspondent: LEAD content-only, settled by a scripted diff, and by the model only when the script is ambiguous.
- A translation: LEAD.
- A numbered calendar entry matching date, place and correspondents but without a surrogate: LEAD calendar-entry.
- A same-letter calendar, regest, footnote or catalogue entry that prints only the clear part: KNOWN-PART, scope clear-part, with every cipher span as the residue. It becomes KNOWN for the cipher spans only with a decipherment sentence, or with text at the cipher's position checked against the leaf's run layout.
- Reversed direction, another addressee, or a reply or antecedent: CONTEXT. SUBSTANCE when the print is within +-3 days, names at least one correspondent, and shares at least two rare entities or numbers with the item's words.
- Undated items: correspondents plus place plus surrogate inside the volume's span gives LEAD.
- Snippet-tier editions cap at LEAD.
- A catalogue-only sender or recipient adds date+place, old-cote, subscription and single-correspondent queries. A hit is LEAD.

Each family runs its positive control in the same run. A missed control makes that family UNCHECKED, never CLEAR.
- **6. Printed-cipher spans** (Birch-type only; separate detectors for Japikse's spaced type and Groen's silent roman stretches).
- Cut heading-to-heading spans, with the sender taken from the heading above, never from the preceding signature.
- KNOWN when the span has at least one exact-length neighbour line and its per-group votes beat a within-span shuffled-line null, or when the negation-aware decipher-word regex fires inside the span.
- Numerals present and neither test fires: LOOK page-image.
- Undeciphered numerals, blanks or '(Cypher.)': KNOWN-PART, with those spans as the residue.
- An editor's 'not deciphered / key not found' note: a required row searching the national historical journal and reviews of the edition, from the edition's year to +10, before CLEAR.
- **7. Network and WEB** (--network, tiered).

When it runs:
- at check-solved for single items;
- for pools and ledgers, only on the CLEAR residue of the next batch, at most about 25 items per session;
- for the rest of a ledger, at G3.

Transport:
- A Net subclass of print_check, used as a library, writing only to prior-work.tsv.
- A per-item 403 on archive.org/download falls back to be-api.
- A 5xx or a reset gets one retry after a pause, then UNCHECKED-NET.
- A true host block stops that host for the run.
- Limits: 12 or fewer requests per item, 1.5 s per host.

Queries and verdicts:
- Queries are as in check 5.
- A positive control runs per host and edition. A missed control gives UNCHECKED-NET, and 'unreachable' quotes the catalogue_ladders route tried.
- A hit with date and both correspondents, a shelfmark string, or the cipher word with the sender is LEAD. The item's own content is KNOWN. Anything else is CONTEXT.

WEB rows:
- They are LOOK kind=web, with a same-blog positive control, and exclude our own repository and outreach text.
- For single-letter targets they are the existing '## Web and blog check' section.
- Modern and press items: claims are CONTEXT claim until both plaintext and method are published and reproducible. Press puzzles also search the same publication from +1 to +8 weeks.

Rows carry a 14-day valid_until.
- **8. LOOK**, the first priced step of the transcription brief.
- Answer from manifest images first.
- Tier 1: the cipher page and its facing page.
- Tier 2, on a convention, hint or tier-1 answer:
  - 2 canvases before the item;
  - the next 2-4 counted from the last leaf, plus one further piece;
  - +-1 canvas around any folio that had to be resolved;
  - every image of a unit of 8 or fewer;
  - catalogue-paired siblings;
  - for maps, plans and lists, the same subject and maker.
- Neighbours come from the per-holder neighbour adapter. For holders without free images, the copy-order template requests them.
- Ask per clear line next to a numeral run: count fit, whether the prose reads on without it, letter spacing, heading or date, fraction covered.
- Two Sonnet calls per crop. Any disagreement, external flag or 'Partially' status escalates to Opus. 'No gloss' never clears another source's flag.
- An unheaded sheet nearby is KEY-SOURCE nearby-sheet. A same-date docket alone never pairs.
- The civil-war adapter ignores later pencil over route, blind and check words.
- --record stores the answer, writes any gloss phrases into clear_words, and reruns steps 5 and 7.
- **9. Scopes and aggregation.**
- A code value or blank obtained by collating two prints, or an event print that supplies the blank's missing fact, gives KNOWN-PART with N2 predicted. This is applied uniformly: bowes D2 and D3, and lodewijk 172. bowes D4, with no print, stays CLEAR.
- A names-only residue is KNOWN only when each name code's value is itself in print. Otherwise it is KNOWN-PART code-values (4992.3 'Sermon').
- Before a line-end token counts as residue, check it against the adjacent line's gloss (szembek B). Match clear text elsewhere on the leaf against the unglossed lines (schonenberg C).
- Within a scope, finer anchored evidence beats coarser evidence: an opened page beats a print code.
- Item exit codes are as in the outputs.
- --known-answer CONSUMER lowers exit 2 to 0 only for an unread item_id or a named gate. Witness and cell checks first diff against any print on disk.
- HOLD needs a positive pointer and a queued route (ASKS, LOCAL-QUEUE or JSTOR row) and names a parallel action. It blocks only this item's transcription and lapses to a logged gap after 14 days.
- A transient error, an unseen archival witness or a cloud-blocked host never makes HOLD.
- **10. Output and learning.**
- Append the prior-work.tsv rows, print the verdicts, and exit with the code. On a block, add one ROOM line through room.py.
- G3 (--reading) reruns steps 5 and 7 with the decoded phrases. An SO row, an N3+ class or a 'not located' sentence requires G3 rows for that item, with every SUBSTANCE row diffed.
- --learn appends to prior_editions.tsv only with office/post, date span, language, verified ids, access tier, segmenter and the positive-control item that taught it. Rows without them are rejected. Each later scan reports the edition's hit rate, so a noisy entry is retired.
- --derive proposals wait in a pending file until the scripted title-page and date-profile check passes.

**Catches.**

- **Own work: 53 records (46 non-Eckert, 7 Eckert).**
All 48 public internal duplicates, which are register lag, SIBLINGS 6 of 6, re-audits, re-queued WORK-QUEUE rows and nightly re-posted leads. Plus N2-AO and N2-BA (already mapped in AUDIT.md), the suriname 2061 re-decode after N0, pro3055 DIGBY and the 2380 conflicts (VHS print on disk), and malsburg f.12 (worked after found-solved).
Register lag comes back as a LEAD done-candidate with file:line unless the artefact or a marker proves DONE.
- **Leaf-and-neighbour LOOK: 31 non-Eckert.**
- nevers-birago no.77 and no.82 (+-1 around the resolved folio);
- fr16104 ink 50 (next piece counted from the last leaf);
- fr5160 f.86, f.88 and f.67;
- manteuffel x2; paget x2; wvo-hessen 1109; rah-canada; schonenberg x3; clair1108 x2; colbert26 x2; clair1067; trew 1614;
- nla x2 (looking back one image);
- fr15575 x3; fr3993; szembek x2;
- suriname 2077 (same subject and maker);
- jan-van-nassau 5549's roman stretch.
E70 surfaces as KEY-SOURCE (flagged).
- **Holder, portal and solver-repository leads: 35 (33 non-Eckert, 2 Eckert).**
- WVO print codes, resolved by opening the cited page;
- Discovery scopeContent;
- the BnF printed catalogue (birago no.24);
- DECODE/HCPortal (decode-1162, costabili, hessen-daenemark x2);
- the Tomokiyo mirror (gramont, R9502, nevers no.87, pro3055 3050/3077, fr4715, fr3641, fr4712, fr16142 A);
- catalogue notes (luzerne x2, antt-fcc, xiquena, pisany x3);
- royalist;
- the post-race spend on hessen-1824 and malsburg, the only part of those two races any gate can catch.
- **Network identity and WEB rows: 19 (14 non-Eckert, 5 Eckert).**
- spinelli (WEB, exit 4);
- na-suriname de Leeuw (shelfmark LEAD);
- dupuy452 x2; dupuy468; morillo item 3 (after LOOK feedback); janssens 188 (LEAD);
- oxenstierna (editor's-note row); trew 1618; digby; erving (now with a positive control);
- bowes D1; lodewijk 172 (KNOWN-PART blank scope);
- E36 and E65.
E26, O9-BC and E29 are flagged SUBSTANCE.
- **Office-keyed edition scan: 27 non-Eckert, in-sample.**
As listed under check 6. About half need a route the first design had no adapter for (Opkomst, Rodriguez Villa, Powell, CSP Scotland via BL Cotton, AMH). Their recall on a new target is unmeasured until the replay runs.
- **Printed-cipher router: 23 Thurloe items.**
About 12 come from exact-length votes against the null and some from the regex. The rest, P14 among them, come from one page-image LOOK each. All 16 misattributions caused by the nearest-heading trap are corrected by reading the sender from the heading above.
- **Civil-war telegram adapter: 109 Eckert.**
- 92 by the OR/ORN index. Of these, about 12 are LEAD (short code-heavy telegrams with ambiguous candidates, 4995.1, T7, PUSG and Basler at snippet tier) and 9 are SUBSTANCE.
- 17 by the classed clear-share test: E74 and 4999.1 KNOWN; E81, E82, E76 and N2-BQ restricted to their residue.
- **Consumer rule: no new records, about USD 450.**
Post-catch grading on schonenberg, fr16142, hessen-daenemark, paget, costabili, the pro3055 cells, birago no.24, fr15575 and colbert26 would have needed an unread consumer item or a named gate.
- **Totals, in-sample, out of 302:**
- 295 surface before reading: 282 blocked or routed, and 13 flagged (decode allowed; N3+, SO rows and 'not located' wait for the verifier's diff).
- 2 HOLD with a positive pointer (R9501, na-suriname 2039).
- 2 races caught only for the spend that followed.
- 1 missed (N2-BG).
- 1 out of scope (DEB-PRIV1).
- 1 correctly CLEAR (bowes D4).
Roughly 130 of the 282 are held only until one owed look, read or diff.

**Must not block.**

- **Clear words public, code words unread.** eckert-1864 E4 (53 of 63 words clear), E5, E37, E51, N2-M, E66. These give KNOWN-PART with the residue listed and exit 0, with the work restricted to the residue, unless every residue token is a non-content class whose value is in print.
- **Printed reply or antecedent.** E5's antecedent (Butler to Meigs, Butler Corr. IV p.112); E47 and E62 against Biggs's reply (OR I/33 p.814); N2-T against Dana's reply of 7 June; N2-BM against Ingalls's reply; N2-M's 17 June sequel; E66 Van Vliet; lodewijk 4610, 4611 and 4616 against Orange's replies and WVO 'Antwoord op' links. These give CONTEXT, or SUBSTANCE at most; never KNOWN, because direction is required.
- **Same letter, clear part calendared or cited.** fr3621 f.130 (Revue de Champagne XII p.341, 'En chiffres'); WVO 57 (Demandt nr.113 regest); jvn 5551 (Glawischnig footnote); fr16104 ink 63 (d'Ars 1884); ceppo f.21v (Pascal 1960 fn.6); gramont f.29 (Catalogue des actes IX [412]). These give KNOWN-PART scope clear-part with every cipher span as residue, or CONTEXT citation. Never KNOWN.
- **Print code over numerals or blanks.** jvn 5549 (GPAS, body printed as raw numerals); WVO 5797 (GPA, blanks 153 and 161); Veenendaal no.92. The code is LOOK edition-page; the body or blanks then come out CLEAR or KNOWN-PART.
- **Unseen archival witnesses.** WVO 53, 57 and 126 (KHA minute, Dresden minute, Collectie Japikse copy); the Marburg copy of jvn 5551; gramont f.30's Simancas or Vienna decipherment; hellen's GStA PK file. These give CONTEXT unseen-witness for the verifier's N4 log, never HOLD.
- **Transient errors and cloud-blocked hosts.** baluze170 f.229 (a Semantic Scholar 429 and three Google Books 503s); HTRC EF 500 'Mongo no primary'; HathiTrust and JSTOR. These give UNCHECKED-NET or a retry row, or HOLD only with a positive pointer and a queued route. Never a permanent block.
- **Anonymous items and items with no edition.** clair1161 ('Advis de flandres'); mssBLA 191 enclosure (a) and 184; na-oldenbarnevelt-2442 (Senisteros to Pena). The check-solved record 'no edition exists (families searched)' clears them, and identity is checked by shelfmark and content only.
- **Modern claims.** kaliningrad-2015 (two self-reported claims); scorpion-1991 (three claimed plaintexts); mccormick-1999; rubin-1953 (Pelling 2018). These give CONTEXT claim until both plaintext and method are published and reproducible.
- **Narrow artefacts over a public plaintext.** 4992.3 ('Sermon = Bowling Green' printed nowhere); vanbeuningen item 2 key; the bowes C sign table; the antt-linhares dictionary identification; WVO 5797 codes 153 and 161. Each is its own scope, CLEAR or KNOWN-PART, so the item exits 0.
- **Negated or partial status wording.** Gachard 'En partie chiffree, sans le dechiffrement'; Tomokiyo 'These undeciphered letters can be read ...'; NA 3.01.14 'Gedeeltelijk gedecodeerd'; Veenendaal 'de sleutel erop heb ik [niet gevonden]'; DECODE R2761 and R1980 'Decrypted' (key only); Bourdeau's 'read in part / no published reading'. These are no evidence, KNOWN-PART, KEY-SOURCE or CONTEXT, as the sentence says.
- **Ciphered copies.** The 48 Salazar index rows pairing 'copia' with 'cifra' ('Copia, en cifra.', 'Copia manuscrita, en cifra') give CONTEXT. Only 'Copia del ... cifrado' or 'Es copia conforme', with no ciphertext on the leaf, gives KNOWN.
- **Nearby decipherments that cannot be attributed before reading.** nevers no.86 vs no.87's unheaded laid-in sheet (canvas 182); fr16104 ink 51's '5 Septemb 1572' docket vs ink 53; birago fr3252 no.30 vs no.24; WVO 53/126 vs 74/98/124; manteuffel f.410 vs f.467/468; fr4702 vs fr3252 'ff.36-37'. These give KEY-SOURCE, settled after transcription.
- **Later pencil in telegraph ledgers.** E47's header words, N2-R's 'doing, did, get, man, change', N2-AZ's 'flor, weida'. The civil-war adapter ignores them.
- **Solver-repository planning lines and copies of our work.** Bourdeau's CATALOGUE line and the excluded.json entry for gramont1529 (that folder reads fr.3091 and fr.3071 only); espagnol 144 f.22, his page that copies our issue 16. These give CONTEXT or are excluded.
- **Audits that raise or deepen a class.** E4 and E5 to N4 after a second audit; birago no.77 raised by AUDIT 3; nevers no.73 and no.85; O9-BB's possible third audit. These run as upgrade-audit or new-family-audit; only a repeat of the same families is refused.
- **A later step on the same leaf.** baluze 170 f.229 across D1-BAL170, D1A-B167, D4-B167 and AUD1; fr16104/fr16105 crops; R13-SURSWP4's new offset; D1A-B167's fifth passage. DONE is typed and keyed on volume + folio + canvas; prose overlap gives LEAD only.
- **Unglossed residue under a 'Partially decrypted' status.** costabili R1166 P4 and its pool; hessen-daenemark codes 625, 602, 634 and 68. These give KNOWN-PART with the residue as the only workable scope; the target stays partial.
- **Volume-wide catalogue notes and two-column OCR.** fr5160 cc58150z 'souvent accompagnees du dechiffrement'; fr3416 f.35 'avec chiffre' vs f.38 'avec chiffre et dechiffrement'; pro3055's Brymner reflow. Only item-anchored entries count.
- **Same sender, recipient and month, but a different letter.** gramont f.30 vs ASI Apr 1530 (run 18 vs controls 9-11); manteuffel f.410 vs Acta Borussica Nr.82; espagnol142 Lonchay no.183. These give CONTEXT unless overlap beats the pair-local control.
- **Name and term collisions.** Senisteros, 'capitano Scipione', 'Advis de flandres', Birague in the Memoires de Nevers, 'Captain Feilner' (93 hits), 'dem printzen zu hispanien' (300 hits). These give CONTEXT unless one entry carries the date, both correspondents and the content.
- **Thurloe P4.** It has no exact-length neighbour line, so it is never KNOWN; one LOOK returns it CLEAR, although P5-P7 in the same volume are KNOWN.
- **Declared known-answer work with a consumer.** gramont fr.3040 f.18 grading key.tsv for f.29/f.30; eckert-1862 T1-T10; fr3641 as a control; es132's printed paragraphs as gate (a); vanbeuningen's print as a crib; N2-L as a key check.
- **Revision propagation and rule-7 re-derivations.** nevers no.86's code-85 fix carried to AUDIT, SO and status.json. propagate-revision is never DONE.

**Offline tests.**

- **test_state_and_freshness**
- a shallow temp repo whose needed line blames to the boundary gives UNCHECKED, never fresh;
- a stub that is behind origin reads origin/main;
- a solver clone with HEAD older than 48 h, and a Tomokiyo page older than 7 days, give UNCHECKED offline;
- a live ROOM claim under 6 h with no done line gives LEAD live-claim.
- **test_own_work_register**
- sp78-france (a While-waiting bullet plus a later dated section naming SP 78/113/56 and /58) gives LEAD done-candidate with file:line;
- the salvago '[already run 3 and 6 Oct' bullet gives DONE;
- the taurello 'Job: R8-TAUR' line gives DONE;
- the fr3789 back-reference gives LEAD;
- the suriname '[retired]' context-tile gives DONE for that instrument;
- a parallel-column step is checked;
- ZOOM-ASKS.tsv (A4-RFHDK), specs/*.json (NEWT-A) and KEY-CROSSMATCH.tsv rows are read.
- **test_own_work_typed**
- baluze: manifest lists 4 of 5 passages, giving DONE for those 4 and CLEAR for 170 f.229r-v;
- fr16104 vs fr16105 crops named c105_f102r_* do not cross-match;
- frames.tsv seen=y for 0503-0592 gives DONE only inside that range;
- nevers no.86 with two audits gives DONE for a same-families reaudit, and CLEAR for propagate-revision, upgrade-audit and new-family-audit;
- room.py --push refuses a re-queued WORK-QUEUE id that already has a done row.
- **test_sentence_classes**
- Gachard 'sans le dechiffrement' gives no evidence;
- 'Gedeeltelijk gedecodeerd' gives KNOWN-PART;
- Veenendaal's 'sleutel ... niet gevonden' gives no evidence plus the editor's-note row;
- Tomokiyo 'undeciphered ... can be read' gives KEY-SOURCE;
- 'f.18 (no.6) ... both deciphered' gives KNOWN;
- RAH 'Copia del telegrama cifrado' gives LEAD copia;
- 'Copia, en cifra.' gives CONTEXT.
- **test_catalogue_anchoring**
- fr3416 f.35 'avec chiffre' gives CLEAR and f.38 'avec chiffre et dechiffrement' gives KNOWN;
- the fr5160 volume note gives CONTEXT volume-note;
- the 1874 OCR '5232' for 3252 gives LEAD fuzzy-match with the system recorded;
- nevers no.82 matches across Fol.162, ink 160 and Tomokiyo f.160.
- **test_print_code_pointer**
- WVO 5811 'GPA IV, 364-366' gives LOOK edition-page;
- 5549 GPAS: the opened page gives body CLEAR and stretch KNOWN;
- 5797: letter KNOWN-PART, blanks 153 and 161 CLEAR;
- WVO 53 'Collectie Japikse' gives CONTEXT unseen-witness;
- WVO 4610 'Antwoord op' gives CONTEXT;
- GSME and LMSAC are resolved through the abbreviation list, and an unknown code is flagged.
- **test_decode_portal**
- R1162 'Partially decrypted' with a PLAINTEXT document gives KNOWN-PART with the residue;
- R2761 'Decrypted' with no inline plaintext gives KEY-SOURCE;
- R9502 'Non-decrypted' with 3 images gives LOOK;
- R361 'Cleartext Publication' gives LEAD fetch;
- HCPortal 494 'Partially solved' gives KNOWN-PART pending LOOK.
- **test_solver_repo**
- the Aymeloglu royalist README 'renders' line plus '72438', dated before ours, gives KNOWN;
- Bourdeau's gramont1529 folder against fr.2980 f.29/f.30 gives CONTEXT;
- his espagnol 144 page citing our issue 16 is excluded;
- the 'no published reading ... read in part' line gives CONTEXT duplicate-effort-risk.
- **test_edition_routes**
- E6 (OR I/32 pt 3 p.498 with double spaces and the OCR 'can he mounted'), by full or telegram identity, gives KNOWN;
- E5, E47 and N2-T against their antecedents and replies give CONTEXT;
- E62 gives SUBSTANCE at most;
- the VHS II 2380 misdated paraphrase gives LEAD content-only;
- 4995.1 (7 vs 17 Feb) gives LEAD;
- blathwayt 186 in Rose's English gives LEAD translation;
- the LS-PRE false hit on N2-M gives LEAD, not KNOWN;
- fr3621 f.130 and WVO 57 give KNOWN-PART clear-part with the cipher spans as the residue;
- an undated fixture inside a volume span gives LEAD;
- an edition row whose positive control misses gives UNCHECKED.
- **test_telegram_identity**
- two Halleck-to-Grant telegrams on the same day with hours 2 h apart give KNOWN for the matching hour;
- E25 (12.30 vs 12.20) gives KNOWN within 30 minutes;
- 4999.2 printed a day earlier gives LEAD;
- a short code-heavy entry (N2-Z) with a unique match gives KNOWN without content cover.
- **test_clear_share_classes**
- E74 (only the signature coded) gives KNOWN;
- 4999.1 (names only, values in print) gives KNOWN;
- E81 (Quartermaster, '4', 'steamers') gives KNOWN-PART restricted to its residue, or KNOWN if all classes are non-content;
- E82, E76 and O9-BA follow the same rule;
- 4992.3 ('Sermon' value unprinted) gives KNOWN-PART code-values;
- a key file without class tags gives UNCHECKED.
- **test_printed_cipher** (on the real ciphers/thurloe-printed extraction files)
- P4 gives 0 exact-length lines, then LOOK, then CLEAR;
- P17 (13 exact) gives KNOWN against the shuffled null;
- the P22 cluster under a 'George Monck.' signature takes its sender from the 'Lord Fauconberg to H. Cromwell' heading;
- a P14 italic fixture gives LOOK page-image;
- Japikse no.316 spaced type gives LOOK edition-page;
- Veenendaal no.92 gives KNOWN-PART plus the editor's-note row;
- the null rate is reported beside the share.
- **test_scope_rules**
- bowes D2 and D3 give KNOWN-PART code-values with N2 predicted, and D4 CLEAR;
- lodewijk 172 plus the event print gives KNOWN-PART blank-span;
- es132 f.89 gives KNOWN for the f.90v L10-L26 paragraph and CLEAR for the rest;
- a szembek B line-end half token is matched to the adjacent gloss line;
- a finer CLEAR beats a coarser print-code KNOWN.
- **test_look_geometry_and_rules**
- nla Nr.548 (letter aufn_0003, sheet aufn_0002) puts the earlier image in look.tsv;
- fr16104 ink 50 puts ink 51 (f.162r) in, via the last-leaf rule;
- nevers no.82 puts canvas 164 in via +-1;
- suriname 2077 lists 4.VEL 2078 by subject and maker;
- an unheaded sheet two leaves on gives KEY-SOURCE nearby-sheet;
- a same-date docket alone does not pair;
- a recorded 'no gloss' does not clear a catalogue flag;
- --record with gloss phrases reruns steps 5 and 7 (fr16142 A 'farce se jouera').
- **test_network_net**
- with Net stubbed: a 502, then a retry 502, gives UNCHECKED-NET;
- a lending-only 403 on archive.org/download falls back to be-api, and the host stays usable for the next volume;
- a host 429 stops that host for the run;
- an erving fixture whose positive control misses gives UNCHECKED-NET, not CLEAR;
- a WEB row exits 4 until recorded;
- github.com/<owner>/cipher-lab hits are excluded;
- print-check.tsv is byte-identical after a gate run.
- **test_hold_rules**
- R9501 (Kolosova annex of 78 cipher letters, with a queued row) gives HOLD naming the parallel action, and it lapses to a logged gap after 14 days;
- baluze170 f.229 with a 429 gives UNCHECKED-NET, not HOLD;
- WVO 126's unseen KHA minute gives CONTEXT;
- clair1161 with a 'no edition exists' record clears;
- kaliningrad-2015 thread claims give CONTEXT claim.
- **test_exit_and_consumer**
- KNOWN with no --known-answer exits 2;
- --known-answer 'grade key.tsv' with no item or gate exits 2;
- --known-answer item:fr.2980-f.29 exits 0 and writes the consumer into the paste block;
- DONE exits 3;
- LOOK, LEAD and UNCHECKED exit 4;
- KNOWN-PART exits 0 and lists the residue;
- SUBSTANCE exits 0 and blocks G3 sign-off until it is diffed.
- **test_composition_heldout**: one fixture per family the records do not cover, each asserting either the right composition or an explicit core-only warning, and never a silent CLEAR or a false HOLD:
- ra-celsing-sillen-1755 (sweden);
- siena-concistoro-2308 (italy);
- sp87-newcastle-1743 (tna-18c);
- decode-1411-hhsta-vienna-1600 (DECODE portal plus the HHStA holder);
- kaliningrad-2015 (modern);
- armstrong-madison-1808 (us-early-republic);
- dupuy468 (BnF holder plus the RTA office set, not bnf only);
- rah-salazar (RAH holder plus the 'Spanish envoys in England' CSP set).
- **test_learn_and_derive**
- --learn without office, date span, language, access tier or a control item is rejected;
- an accepted row appends and passes file_shrink_guard;
- --derive writes only to items.pending.tsv and the pending editions file, and marks fields catalogue-only;
- the sources.tsv variants in beinecke-manchester and the 5 other non-standard folders parse or report UNCHECKED.
- **test_replay_harness**: harness only, on a two-folder fixture repo.
- It checks out a folder at its brief commit, removes the catching source from prior_editions.tsv, runs --derive and the offline core, and reports recall per check.
- The full replay over the records is a separate priced job, needing full history.
- **test_no_network**: every test runs under --offline against fixtures in tools/tests/fixtures/prior_work/, with Net stubbed and a guard asserting that no socket is opened. The test file is tools/tests/test_prior_work.py.

**Wiring.** **Rule and system map.**
- CLAUDE.md Usage 8a gains one line naming tools/prior_work.py as the per-item prior-work gate, with its must-catch and must-not-block kinds in its docstring and offline tests in tools/tests/test_prior_work.py.
- SYSTEM.md lists the tool, tools/shelfmark.py and the three registries, as system_map_check requires.

**(1) Rollout.**
- Warn-only on new deep-work briefs first.
- Enforce on new briefs once the replay recall is published and the false-block rate on the SURVIVORS list has been measured from a real run.
- The 158 open and partial targets that pass intake_gate_check today are not failed on the day: a backfill job is priced per folder (--derive plus one review), and enforcement follows.

**(2) check-solved (.claude/briefs/check-solved.md and .claude/workflows/check-solved.js).**
- It writes the structured items.tsv row in the same commit as its verdict.
- Its Premise check starts with `tools/prior_work.py <slug> --point intake --network`.
- The session answers the LOOK and WEB rows. For single-letter targets, the WEB rows are the existing '## Web and blog check' section.
- For pools, it runs on each new item as the item is added.

**(3) tools/intake_gate_check.py.**
- It reads prior-work.tsv, not a pasted block. Every items.tsv row must have rows from every required family, newer than the newest items.tsv row and inside valid_until, with no UNCHECKED in a required pre-read family.
- The verdict is per item.
- The pasted '## Prior-work gate' block is informational only.

**(4) Common brief tail (.claude/briefs/README.md).**
- Every brief that transcribes, keys, decodes, aligns, crops, looks up or verifies an item states the item verdict, its scopes and residue, and any consumer.
- The worker's first action is `python3 tools/prior_work.py <slug> --brief <brief> --offline`.
- It stops with a ROOM flag on exit 3, on exit 2 without a valid consumer, or on exit 4 for an item it would transcribe. Exit 4 blocks only that item, never the rest of the lane.

**(5) transcription.md.**
- The LOOK is the first priced step, with one call per crop and the per-call price stated (Usage 6), plus a stop rule.
- check-solved does not run a separate LOOK pass over whole pools.

**(6) Lane opening (default-lane.md steps 2/2b; parent.md duties 0b/0c).**
- Run `tools/prior_work.py --register NEXT-STEPS.tsv --columns next_step,parallel --offline` before choosing job 1.
- SIBLINGS-*.tsv, LOOSE-ENDS-*.md, ZOOM-ASKS.tsv, specs/*.json and key_crossmatch output pass through --register before any brief is written from them.
- room.py --start prints the count of stale prior-work rows and the share of open targets that are core-only.

**(7) Solver and verifier (solver.md, campaign.md, breadth.md, verifier.md).**
- After decode, the solver runs --reading (G3).
- An SO row, an N3+ class or a 'not located' sentence needs G3 rows, with every SUBSTANCE row diffed. verify_backlog checks this mechanically.
- The verifier receives the prior-work family log (what was searched and hit), never the predicted class, and runs its own families.
- Each N0-N2 it finds is fed back with --learn in the same commit.
- A re-audit is typed upgrade-audit or new-family-audit, or it is refused.

**(8) Room and queue.**
- room.py --push runs work_queue.check() on WORK-QUEUE.tsv and file_shrink_guard on the registries.
- The dispatcher runs the same check before writing a row.

**(9) Private repository.** The private session runs prior_work.py in its own checkout. Nothing crosses into this repository (rule 9a).

**Reuses.**

- **tools/premise_check.py**
- reuses near_rows(), find_file() and manifest_lists_leaf();
- leaf_of() and normalise_leaf() are replaced by tools/shelfmark.py, which keys volume + folio + canvas;
- premise_check gains check (e), which calls prior_work's offline core, so the parent's pre-spawn LIKELY/SPLIT checks inherit it.
- **tools/next_steps_fresh.py**: keywords(), overlap(), is_stale(), blame_times(), anchor_line(), later_paragraphs(), room_done_lines(). Fixed at origin to check the parallel column, and used only for LEAD done-candidate, never DONE.
- **tools/next_steps.py**: fixed at origin to treat '[done', '[already run', '[x]', 'Job:'/'Brief:' lines inside done sections, and back-references as done. An undated While-waiting section is superseded by a later dated section that names its identifiers.
- **tools/work_queue.py check()**: its duplicate job_id test is called from room.py --push and from the dispatcher. tools/room.py has no work_queue call today (checked 8 Oct 2026).
- **tools/print_check.py**, imported as a library:
- functions: Net, norm(), dehyphen(), search_text(), find_cached_djvu(), read_text(), check_ia(), check_ia_global(), check_gbooks(), check_openalex(), check_crossref(), resolve_htids(), check_htrc();
- a new identity entry point that needs no phrases.txt;
- main() is never called, so print-check.tsv in the 37 folders that hold one is untouched.
- **tools/gbooks_search_within.py and tools/htrc_ef_headwords.py**: the access ladder for snippet-tier and Cloudflare-blocked editions (bowes CSP Scotland vi was reached this way).
- **tools/solver_repo_diff.py and tools/decode_neighbours_exclude.py**: build_ours_index(), folio_tokens(), build_bourdeau_index() and build_aymeloglu_lines(). Their keys() and volume_keys() move into tools/shelfmark.py and gain the missing grammars.
- **tools/loose_ends.py**: material_keys() and is_tracked(), for register parsing in step mode.
- **ciphers/eckert-1864/entries_mssEC19.py**: orcheck(), plain_runs() and known_blocks(), plus ls3_r18b_printcheck.py's letters-only scan. These are promoted into the civil-war adapter, not the core, together with the telegraph normalisations.
- **ciphers/thurloe-printed/check_interlinear.py**: --votes, scored against a new within-span shuffled null; plus tools/thurloe_extract.py's heading logic, tools/ia_numeral_runs.py and tools/htrc_numeral_pages.py for detecting editions that print numerals.
- **Holder routes**: tools/bnf_findingaid.py, tools/discovery_items.py --notes, tools/huntington_transc.py (plus a new CISOSEARCHALL collection-search option), tools/digitarq_fetch.py, tools/decode_list.py, tools/decode_browser_login.js (one login per session), tools/browser_fetch.js (RAH OAI didl, Arcinsys), and tools/data/catalogue_ladders.tsv with a new prefix column.
- **KEY-OFFICES.tsv** (70 rows with office, correspondents, years and language) seeds the office-keyed edition sets and the title/office alias table. KEY-DESIGN.tsv tells the clear-share step which keys have classable rows.
- **LOOK crops**: tools/gallica_folio.py and tools/iiif_lines.py, used through the per-holder neighbour adapter. **Registry writes**: tools/file_shrink_guard.py on every append-only TSV.

## Process changes

- **Route known items through a named consumer, at no tool cost, before anything else is built.**
- A KNOWN item or scope is worked only when --known-answer names an unread item_id the key or grading will be applied to, or a gate named in a brief.
- Grade refinement, corpus building or re-decoding on the KNOWN item itself stays refused.
- Witness and cell checks diff against any print on disk first.
- This is applied per item and per scope, never as a target status: a target with an unglossed residue stays partial under rule 5, and the residue is its only workable scope.

This stops about USD 450 of post-catch spend: schonenberg, fr16142, hessen-daenemark, paget, costabili, the pro3055 cells, birago no.24 (F36-GLOSS scored X), fr15575, colbert26, and the suriname 2061 re-decode.
- **Fix the registers where they are written, not only in a parallel parser.**
- next_steps.py treats done markers, done-section 'Job:'/'Brief:' lines and back-references as done.
- next_steps_fresh.py checks the parallel column.
- room.py --push and the dispatcher call work_queue.check(); today room.py does not.
- A worker that stops on DONE or KNOWN rewrites its source register line in the same commit.

Cases: sp78-france, salvago, taurello, fr3789, fr15575, fr16142 D1A-DUP521, decode-2754, and the three USD 60 lanes re-queued on 6 Oct.
- **Read current state, or say so.**
- Every gate run fetches and reads origin/main.
- On a shallow clone it deepens the paths it reads, or reports UNCHECKED.
- It prefers dated headings and ROOM tags over blame.
- A ROOM claim under six hours old is a LEAD, not a free target.

Same-day duplicates such as R9-SRCH/R10-SRCH2 and D12-E62H's live verifier are invisible otherwise.
- **Look before transcribing, as the first priced step of the transcription brief.**
- Use native 1200-1600 px crops, with the per-line question.
- Run two calls per crop, escalating to Opus on disagreement or on any outside flag.
- 'No gloss' can never clear a flag raised by another source.
- A thumbnail or contact sheet can never record 'no gloss'.
- For holders without free images, the copy order asks for the facing page, two leaves before, two to four after, and the paired sibling.
- **Status fields and print codes are leads, never verdicts.**
- Each sentence is classified with negation and partial wording.
- Only entries anchored to the item count.
- A print code opens the cited page before anything is KNOWN.

Contradictions on file: R9502 and gramont 4227 'Non-decrypted' with decipherments; R361 'Non-decrypted' with a Cleartext Publication; fr16104 ink 50 'sans' with ink 51 'dechiffre de la precedente'; R2761 'Decrypted' as a key only; jvn 5549 GPAS over raw numerals.
- **Every search row carries a positive control from the same run.**
- A family whose control missed is UNCHECKED, never CLEAR.
- 'Unreachable' quotes the catalogue_ladders route tried, after the access ladder: djvu, then be-api, then gbooks search-within, then HTRC EF.

Wrong negatives on file: erving 'no result', later 7 hits; bowes CSP Scotland vi 'unreachable'; den Heijer 'unreachable'; Lossen 'not on IA'; janssens Opkomst read at the wrong volume.
- **Edition sets are keyed by office, period and language, not by who holds the leaf.**
- They are seeded from KEY-OFFICES.tsv and each family's own NOTES.md.
- Every edition-volume row carries an access tier, a segmenter and a positive-control letter.
- Before rollout, a minimum set is added for each family the records did not cover: Sweden, Italy/Poland/Switzerland, the US early republic, 18th-century SP and BL Newcastle, WWII, modern/press.
- The share of open targets that are core-only is reported at every lane opening.
- **check-solved writes the item's identity as data, not prose.**
The row covers item_id, shelfmark, volume, folio/canvas, ids, date, sender, recipient, office, place, language, kind and holder URL, each field flagged as verified from the leaf or taken from the catalogue. It is written in the same commit as the verdict. When the catalogue's correspondents are unverified, the gate adds date+place, old-cote and subscription queries, and their hits are LEAD.
- **Run the gate at three points, not one.**
- G1 before transcription: identity, holder surrogate, own work, LOOK.
- G2 after the clear frame is transcribed and before keying: the clear-frame screen ('Cerbes Joachin').
- G3 after decode: the solver's phrase search becomes a gate rerun.
An SO row, an N3+ class or any 'never printed / not located / no prior decipherment' sentence requires G3 rows with every SUBSTANCE row diffed. E6 and E12 went to the owner as 'never printed', and 13 SO rows were withdrawn.
- **SUBSTANCE is the verdict for the withdrawn-SO class.**
A print within +-3 days that names a correspondent and shares two rare entities or numbers with the item lets decoding proceed. The N-class and the SO row wait for the verifier's diff. This covers E26, E28, E29, N2-BL, O9-AK, O9-BC, E72, E73, E83, E84, E49 and E54, which the first design would have let through as CONTEXT.
- **Network search is tiered and shared, not per item across whole ledgers.**
- Check-solved runs it for single items, and on the next batch's CLEAR residue for pools: at most about 25 items per session, at most 12 requests per item.
- The rest of a ledger runs at G3.
- Rows are committed with a 14-day validity, so the four accounts reuse them.
- Chronicling America's API is retired (404, 8 Oct 2026). Use loc.gov search JSON under a hard cap, plus the item country's press APIs.
- The Google Books project quota goes into KEYS.md before this is wired.
- **HOLD is narrow.**
It needs a printed or scholarship source with a positive pointer that it edits or deciphers this item or its pool, and a queued ASKS, LOCAL-QUEUE or JSTOR row. It names one parallel action, blocks only that item's transcription, and lapses to a logged gap after 14 days. Unseen archival witnesses go to the verifier's N4 log as CONTEXT. Transient errors and cloud-blocked hosts are UNCHECKED-NET.
- **Re-diff solver repositories and refresh portal records before every brief, not only at intake.**
- KNOWN from a solver repository needs a reading file for the shelfmark and folio, dated before ours and not built on our issues.
- A target harvested from another solver's open list is flagged as a collision risk.

Cases: malsburg about USD 149, hessen-1824 about USD 13, royalist about USD 23, R13-MALS after found-solved; Bourdeau's 1 Oct espagnol 144 page copied our issue 16.
- **Printed-pair extraction reads the sender from the heading above the cluster, never from the preceding signature.**
The interlinear test is exact-length votes against a within-span shuffled null, not a share of chance length matches. Measured 8 Oct 2026: P4 has 0 exact-length lines while P17 has 13, and the raw vote share alone does not separate (P17 0.33, P5 0.94).
- **Verifier catches feed the edition sets with scope.**
- --learn appends an edition row only with office/post, date span, language, verified ids, access tier, segmenter and the positive-control item that taught it.
- The registry is append-only TSV under file_shrink_guard, never a shared JSON.
- Each later scan reports the edition's hit rate, so a noisy entry is retired.

Seed rows from the records: Chronicling America and loc.gov, PUSG, the Welles diary, Plum, Rose, Aerztebriefe, OR ser. III vol. 4, ORN 11 and 26, the OR I/43 pt 1 identifier fix, OR ser. I vol. 52 pt 1, Opkomst XIII, Rodriguez Villa, Powell NRS.
- **Measure before claiming.**
- Before the gate is called predictive, a priced job checks out every catching record's folder at its brief commit (full history; this clone is shallow), removes the catching source from the registry, runs --derive and the offline core, and publishes recall per check, counted in items rather than records.
- The same job runs the gate on the SURVIVORS list and publishes the false-block rate.
- The misses choose the --derive query templates: full text on sender + recipient + year + cipher word, not a surname title search.
- **Stated limits (unfixable by this gate).**
- races with other solvers before their reading exists;
- unindexed paraphrases and sources reachable only from the owner's desk;
- edition recall on new targets, until the replay runs;
- residual model-look error on gloss shapes it has missed before;
- snippet-only editions, whose verdict ceiling is LEAD;
- wrong catalogue metadata that every alternative query also misses;
- private-repository duplicates;
- whole-ledger network search under the rate rules;
- wrong negatives logged before positive controls existed;
- attribution of unheaded nearby decipherment sheets before transcription;
- another account's unpushed work.
Each is reported, as UNCHECKED, HOLD, LEAD or a logged gap, rather than hidden as CLEAR.

## Critiques (issues the final pass addressed)

### coverage -- needs-changes
- [high] Records that get CONTEXT are counted as caught, but CONTEXT never blocks (exit 0). This hides the class that produced most of the withdrawn second-opinion rows. -- fix: Add a verdict SUBSTANCE (predicts N2). It fires when a print within ±3 days names at least one correspondent and shares at least 2 rare entities or numbers with the clear words (vessel names, '16,000', Johnson's Island, Holabird, Hilton Head). It returns exit 0 for decoding, but blocks any N3+ class, any SO row and any 'not located' sentence until the verifier has diffed the hit. Report blocked (exit ≠ 0) and flagged (CONTEXT, SUBSTANCE, KNOWN-PART) as separate counts.
- [high] The KNOWN rule in step 4 requires date, correspondents and content all at once. That rule misses misdated, mis-attributed and OCR-garbled prints, and the design's own tests contradict it. -- fix: Allow two independent routes to KNOWN:
(a) content only: rare-3-gram or phrase cover above a shuffled control inside one entry, with no date or correspondent required (catches 2380, 4995.1, dupuy468 'Cerbes Joachin');
(b) for telegrams: date ±1, hour and both correspondents, with no content-cover requirement.
A translation (Rose) gets KNOWN-candidate from correspondents + place + named entity (Ripperda), plus a LOOK diff. Move the misdated fixtures into the step-4 tests so the rule and the tests agree.
- [high] The coverage figures are circular. The adapter lists were seeded by hand with exactly the sources the records found late, so 122 (check 1) and '28 need a family list' are not measured recall. -- fix: Add a replay test. For each record, check out the folder at its brief commit (git worktree), remove the catching source from prior_adapters.json, run --derive plus --network, and report recall per check. Publish that number in place of 306, and use the misses to choose the --derive query templates (for example sender + recipient + year + the cipher word in full text, rather than title search).
- [high] No check guards against a negative search with no positive control, although that is the commonest root cause in the records. Only 403, 429 or a challenge page mark a host as blocked. -- fix: Every family row carries a positive control from the same run: one known-hit query against the same host and edition, such as a phrase from the volume's own title page or a known letter in it. A family whose control did not hit is HOLD, never CLEAR. 'Unreachable' must quote the catalogue_ladders route that was tried.
- [high] The LOOK geometry and scope leave out several records the design counts under check 6. -- fix: - Look at 2 canvases before the item, and at every image of a unit of 8 or fewer (Arcinsys, DECODE).
- Count 'next filed piece' from the item's last leaf, and look one piece further.
- Look ±1 canvas around any folio that was resolved.
- Give a page-image LOOK to any printed-cipher span where check 4 finds numerals but neither the interlinear test nor the regex fires. P4 stays CLEAR.
- For maps, plans and lists, a sibling is any item with the same subject and maker in the catalogue range, compared by content.
- [high] The model look repeats failures the records already show. Higher resolution and one Sonnet call do not address how those failures happened. -- fix: Ask the LOOK question per clear line above a numeral run:
- Does the line's syllable or letter count fit the run?
- Does the surrounding prose read on without it (paget's test)?
- Are the words letter-spaced?
Run on Opus, or as two Sonnet calls where any disagreement, catalogue flag, scout flag or 'Partially decrypted/solved' status escalates to Opus. A 'no gloss' answer cannot clear a flag raised by another source.
- [high] Routing KNOWN items as known-answer jobs (exit 2 plus a purpose) would not have stopped the ~USD 450 of post-catch spend. Each of those jobs had a purpose the flag would accept. -- fix: --known-answer must name a consumer: an unread item_id the key will be applied to, or a gate named in a brief. Grade refinement on the KNOWN item itself has no consumer and stays at exit 2. For witness or cell-check purposes, require the diff against any print already on disk as the first step.
- [medium] The own-work check, as specified, misses several of the 48 internal duplicates it claims. -- fix: - First action: git fetch, then read origin/main, and fail if behind.
- A ROOM claim under 6 h old, with no done line, on the same slug and identifier gives HOLD 'live claim'.
- Add ZOOM-ASKS.tsv, specs/*.json, KEY-CROSSMATCH.tsv and HUMAN-TX-ASKS to --register and local state.
- The private-repo session writes a done-ids digest (ids only, no content) into the public repo.
- Run the work_queue uniqueness check in the dispatcher or a pre-push step, not only in room.py.
- [medium] Under the design's own scope rules some claimed catches come out CLEAR, and scope is treated inconsistently between similar cases. -- fix: Make the rules scope-aware. For code-value or blank-span scope, a value obtained by collating two prints, or an event print that supplies the blank's missing fact, gives KNOWN-PART-N2, not CLEAR. Apply this uniformly to D2, D3, D4 and 172. Before counting a line-end token as residue, check it against the adjacent line's gloss. Match any clear text elsewhere on the leaf against the unglossed lines.
- [medium] The clear-share test never defines a 'content code word', so several Huntington N1 records would come out KNOWN-PART with exit 0 and be decoded anyway. -- fix: Tag each key-book row with a class: person, place, title, number, date/time, signature, vessel, other. KNOWN means the residue contains only person, place, title, signature and date/time tokens, or at most 2 tokens. Add E81, E82 and E76 as fixtures.
- [medium] The adapter prefix map has holes, so some claimed catches have no route. -- fix: Add an nl-colonial adapter for 4.VEL, 1.04, 1.05 and 2.01: AMH, Opkomst, den Heijer via NA 2.14.97, de Leeuw, Colenbrander. Add explicit rah and pt entries. An unmapped prefix gives HOLD 'no adapter', not core only.
- [medium] A print code (GPA) gives KNOWN with no test of the cited span, and the Japikse spaced-type convention has no test. -- fix: Treat a print code as a pointer: fetch the cited pages and run check 4 (numerals, blanks, roman text, spaced type) before KNOWN. Extend the regex to 'Groen', 'Japikse' and 'Fruin'. Add a Japikse no.316 fixture, or a LOOK at the page image.
- [medium] Tally audit: the arithmetic is internally consistent, but the unit of counting is inconsistent, which inflates the headline percentages. -- fix: Count items, not records. Remove the duplicates and the survivors. Report blocked and flagged separately. On these records, the gate as specified blocks or routes about 277 of 305 for certain, not 306/310. A further ~20 depend on thresholds the design does not state: the short telegrams, E81/E82/E76/N2-BQ, the adapter-mapping holes, nla, fr16104, clair349, gunther, P10 L10 (Powell is in no adapter) and E70/fr5160 f.67 (sibling rule).
- [medium] The WEB row that spinelli depends on has no exit code. Spinelli is the second-costliest record. -- fix: Make WEB a LOOK-class row with exit 4 until it is recorded. Its first query is a positive control on the same blog.
- [low] Only the solver clones are refreshed. The other prior-work sources go stale. -- fix: Apply the same 48 h refresh (or an If-Modified-Since check per brief) to the Tomokiyo page that names the shelfmark, to the item's HCPortal API record and to its DECODE listing row.
- [low] LOOK results are not fed back into the text searches, and an editor's 'key not found' note is treated as CLEAR. -- fix: --record-look writes the gloss phrases into clear_words and re-runs checks 1 and 5. An editor's 'not deciphered / key not found' note emits a required row searching the national historical journal register and reviews of the edition, for the edition's year to +10, before CLEAR.
- [low] Shelfmark and folio matching is exact, but catalogue OCR and foliation systems vary. -- fix: Match shelfmarks fuzzily (digit transpositions, OCR digit confusions) and folios within ±2 across the finding-aid, ink and Tomokiyo systems. Record the system each match used.

### false-block -- needs-changes
- [high] A citation, regest or calendar of the same letter that prints only its clear part is treated as KNOWN. The network rule says a hit is 'CONTEXT unless the snippet carries the date and both correspondents, or the item's own content'. Before reading, the only 'own content' anyone can match is the clear frame. So every same-letter calendar or citation of the clear part becomes KNOWN. The must_not_block list hides this by filing two of these cases as 'same sender, recipient and month, different letter', when they are the very letter. -- fix: A calendar, regest, footnote or catalogue hit gives KNOWN only if it shows that the cipher span itself is in print. That means a positive decipherment sentence, or printed text at the cipher's position checked against the leaf's cipher-run layout. A same-letter print of the clear part should give a new verdict, KNOWN-CLEAR (exit 0), whose residue is every cipher span. Move WVO 57 and fr3621 f.130 into a must-not-block class 'same letter, clear part calendared' and add an offline fixture for each, plus fixtures for the Glawischnig and d'Ars footnotes.
- [high] The edition identity scan's KNOWN test ignores direction. It allows a date window of +/-1 day and accepts 'both correspondents inside one entry span'. A printed reply or antecedent carries both names and the same topic words, so its content cover will beat a global shuffled control. The design also opens a second route to KNOWN with no date at all: the 2380 test says 'KNOWN ... through Brymner-paraphrase phrases, not the date'. That route also turns the known false clear-word hits into KNOWN. -- fix: Require the entry's sender to equal the item's sender and its recipient to equal the item's recipient. Require header time and date to be consistent. Measure cover on the item's distinctive n-grams against a control built from that correspondent pair's adjacent entries in the same volume, not against a global shuffle. The misdated-paraphrase route (VHS 2380) should give LOOK, settled by one model comparison, and never KNOWN on its own. Add fixtures for E5, E47 and N2-T, each of which must return CONTEXT.
- [high] A holder-record print code gives KNOWN for the whole item, and the rule that a verdict's strength decides the item (DONE > KNOWN > KNOWN-PART) lets that coarse KNOWN override the edition scan's finer KNOWN-PART or CLEAR. The 'Japikse' code also matches a record that names an unpublished copy. -- fix: A holder print code should give LOOK-EDITION: open the cited page and run the scope tests. It should never give KNOWN by itself. Aggregate per scope (plaintext, cipher spans, blanks, code values), so that a finer KNOWN-PART or CLEAR beats a letter-level KNOWN. Match 'Japikse' only as a published citation ('Japikse ... nr.'), never 'Collectie Japikse'. Add fixtures for 5549 (body CLEAR, stretch KNOWN) and WVO 53 (CLEAR).
- [high] HOLD fires far too often and blocks transcription (exit 4). As specified, any 'named source unread or route blocked' gives HOLD, and so does any 403, 429 or challenge. Almost every true N3/N4 names some unread source; that is exactly why it is not N5. Some of these sources can never be read from the cloud, so the block would be permanent. -- fix: Give HOLD only when there is a positive pointer that the unread source edits or deciphers this item or its pool, as Kolosova's annex of 78 cipher letters does for R9501 and de Leeuw's treatment of 2039 does. A transient 429 or 503 should give a 'retry' row, never HOLD. HOLD should gate novelty wording and N-class claims, not transcription. Give it a time-box after which it drops to a logged gap.
- [high] Step 0 gives 'HOLD no edition named until check-solved names one'. This permanently blocks anonymous items, and items whose senders have no printed papers. The identity scan's 'both correspondents' test cannot run on them either. -- fix: Let check-solved record 'no sender-side or recipient-side edition exists (families searched: ...)'. That record clears the HOLD. Anonymous items get an identity check by shelfmark and content only.
- [high] The printed-gloss interlinear test, as specified (a neighbour within +/-3 lines whose letter count is within +/-3 of the group count, judged by a share threshold), cannot tell the N4 item P4 from the N0 items. It measures chance length matches. -- fix: Require consistent votes (the check_interlinear --votes test): exact-length pairs must give a one-system group-to-letter map. Or compare against a per-span shuffled-line null. Add a P4 fixture built from the real file that must return CLEAR, and report the null rate beside the share.
- [medium] The clear-share rule 'residue is names or a signature gives KNOWN' closes items whose only contribution is the value of a name code. The design also collapses per-scope classes into one item verdict, and KNOWN dominates. So the scopes it promises to keep separate (code-words, key/mapping) still exit 2, and the 'predicts N0 or N1' text is then fed to the verifier, which anchors it. -- fix: Count a names-only residue as KNOWN only when each name code's value is itself in print (the DCW blog list, or a published key). Otherwise give KNOWN-PART with scope code-words. The item's exit code should be 0 whenever any scope is CLEAR or KNOWN-PART. Write a predicted N-class only for the plaintext scope. Add a 4992.3 fixture.
- [medium] The decipherment regexes and status words ignore negation and partial wording. /d[ei]c[iy]ph|dechiffr|.../, 'gedecodeerd' and 'sleutel' all match sentences that say the opposite, or only part. -- fix: Classify at sentence level with a negation and partial lexicon: sans, not, un-, 'no deciphering appended', niet, gedeeltelijk, partly, 'en partie'. A partial match gives KNOWN-PART, a negated one gives no evidence. Add offline fixtures for each phrase above.
- [medium] The RAH title rule ('Copia'/'Es copia' gives KNOWN) would block ciphered copies, which are common in the Spanish pools. -- fix: Give KNOWN only for 'Copia del ... cifrado' or 'Es copia conforme' after one text-leaf check shows no ciphertext (the xiquena case). 'Copia, en cifra' and 'Copia ... cifrada' give CLEAR. Add both fixtures.
- [medium] The leaf-and-neighbour look cannot attribute an unheaded or merely same-date decipherment before anything is read, and it will mistake later pencil marks in telegraph ledgers for glosses. The rule 'heading names another item gives KEY SOURCE' covers neither case. -- fix: An unheaded sheet nearby gives KEY-SOURCE-CANDIDATE (exit 0), settled after transcription by an alignment test of run lengths and order. A same-date docket alone never pairs a sheet with an item. The us-civil-war-telegrams adapter should exclude pencil over route, blind or check words. Add fixtures for no.86 and ink 53.
- [medium] The solver-repo rules give KNOWN on a directory or a planning line, and on pages that copy our own reading. They ignore the source's date and where its reading came from. -- fix: KNOWN from a solver repository needs a reading file for this shelfmark and folio, dated before our reading and not citing cipher-lab, our issue numbers or our folders. Directory names and catalogue or planning lines give CONTEXT. Exclude github.com/<owner>/cipher-lab and our outreach text from the web and blog rows.
- [medium] Refusing a re-audit of any two-audit item blocks the repository's normal routes to N4, and the routes to an honest downgrade. -- fix: Add step types for an upgrade audit (closes a named gap family) and for a new-family audit (a family neither audit searched). Refuse only a re-audit that repeats the same families.
- [medium] Own-work DONE is keyed on folio or keyword overlap without the volume or the step type, so a later step on the same leaf (crop, then transcribe, then decode, then audit) matches the earlier one. -- fix: Key leaves on volume + folio + canvas. Mark DONE only from typed evidence, meaning the artefact the step itself produces exists: crops for crop, passes/*.tsv for transcribe, reading_*.txt for decode, an AUDIT section with a class for audit. Never mark DONE from prose overlap alone.
- [medium] A 'Partially decrypted' or 'Partially solved' status, and the 'N0 on arrival' process change, close the unglossed residues, which are the only parts that could become N3. -- fix: Give KNOWN-PART, with the residue taken from the record documents and the image. Apply N0-on-arrival per item and per scope, never as a target status.
- [low] Catalogue notes written for a whole volume, and OCR from two-column catalogues, can attach 'avec chiffre et déchiffrement' to the wrong item. -- fix: Accept only entries anchored to an item, with shelfmark, item number and folio verified on the same parsed entry. Ignore notes written for a whole volume. Add fixtures for fr3416 f.35 and f.38.

### generality -- needs-changes
- [high] The adapter is picked on the wrong axis. Step 0 chooses ONE family from the holder's shelfmark prefix, but which editions print a letter depends on the correspondents' office, the date and the language, not on who holds the leaf. A holder-keyed adapter gets the catalogue route right and the edition list wrong. It also routes a DECODE R-id to a 'decode route' only, which hides the underlying holder and its editions. -- fix: Compose three registries instead of choosing one family. (1) Holder routes: tools/data/catalogue_ladders.tsv plus a new shelfmark-prefix column. (2) Portal routes: DECODE, HCPortal, WVO, the DCW blog, Zooniverse. (3) Edition sets keyed by office/post, date span and language. Seed (3) from KEY-OFFICES.tsv, which already has office, correspondents, years and language columns (71 rows), for example 'French embassy in Spain 1560-80', 'Spanish envoys in England', 'Imperial diet'. An item gets core, then every holder, portal and office entry that matches. A DECODE id adds the portal and never replaces the holder.
- [high] The non-Eckert edition lists are fitted to the 310 records after the fact, so the claimed recall (177 of 180 non-Eckert, 28 of them by edition scan) is measured in-sample. The --derive route that would have to find editions for a new target is a surname search over IA titles and subjects. That finds family-paper editions but not the calendars, state-paper series and journals behind most non-Eckert misses. Several claimed catches are not even backed by the adapter lists as written. -- fix: Before the tool is wired into the brief tail, run a leave-one-target-out validation. For each non-Eckert edition catch, remove the edition that record contributed, rebuild the adapter with --derive from NOTES.md as it stood before the catch (git show), and report how many are still caught. Publish that number in place of 177/180. Separately, credit the generalizable win: editions that check-solved named but misread (bowes Surtees, clair349 Guise read at the wrong pages, fr16142 Charriere grepped only for metadata, janssens Opkomst read at the wrong volume) are caught by re-scanning by date, and that win does not need hindsight lists.
- [high] HOLD over-fires outside Eckert and would false-block items, including counted N4 survivors. (a) 'No sender-side or recipient-side edition named' HOLDs every anonymous item, diary or modern cryptogram forever. (b) 'A named source is unread or its route is blocked' fires on the unseen archival witnesses that holder records list as a matter of course. (c) A per-host 403, 429 or challenge becomes a HOLD even when another route to the same edition works. Exit 4 blocks transcription in all three cases. -- fix: Split HOLD into three cases. HOLD-PRINT applies only when a printed or scholarship source with a queued route (ASKS/LOCAL-QUEUE row) is unread, as with R9501 Kolosova and suriname de Leeuw. An unseen archival witness becomes CONTEXT tagged 'unseen-witness', passed to the verifier's N4 log, and never blocks. Missing-edition HOLD applies only to correspondence-type items; anonymous, diary and modern items go to a 'modern' or 'unattributed' family instead. Before any host failure becomes a HOLD, an edition must run its access ladder: djvu, then be-api fts, then gbooks search-within (country=US), then HTRC EF per-page tokens. Add must_not_block fixtures for WVO 126, 57 and 53 and for kaliningrad-2015.
- [high] A new target cannot get its adapter automatically from its check-solved verdict and NOTES source lines. Every input --derive relies on is missing, unstructured, written after the reading, or not yet built. -- fix: Make check-solved emit a structured items row: item_id, shelfmark, folio/canvas, date, sender, recipient, office, place, language, holder URL, and a flag for whether each field was verified from the leaf or taken from the catalogue. Write it in the same commit as the verdict, and have intake_gate_check require it. Add the prefix column to catalogue_ladders.tsv and fill the missing holders. Have --derive emit a proposed prior-adapter.json that a model reviews once at intake, and say so; do not claim no hand-coding. Until then, an item with no derivable family should report 'core only' as a warning, not pass silently.
- [high] Pre-read, the edition identity scan can block almost only Eckert items. KNOWN requires date, both correspondents AND content cover in one entry, and content cover needs clear words on disk before decoding. Huntington volunteer transcriptions give the Eckert ledger those clear words. An all-cipher or untranscribed manuscript letter has none, so every edition hit for it can only be CONTEXT, which never blocks. The tally counts these as catches anyway. -- fix: Run the gate at three points: pre-transcription (identity by date, place and correspondents scored against a holder content surrogate), post-clear-text transcription and pre-keying (the clear-word screen on the letter's own clear frame or subscription, the dupuy468 'Cerbes Joachin' shape), and post-decode (--reading, which turns the solver's phrase search into a gate rerun). Allow KNOWN on date, place and correspondents in a numbered calendar entry when the holder surrogate overlaps above a control. Without a surrogate, emit a 'LIKELY-KNOWN: read entry N before transcribing' that blocks until one model look at that entry.
- [medium] The 'family-independent' core contains Eckert-only machinery, and its date and name handling is English and Gregorian. -- fix: Move the clear-share test and the clerk-split normalisation into the us-civil-war adapter. Give the core a date-expression generator per language and era, and a title/office alias table seeded from KEY-OFFICES.tsv correspondents. State the fallback for undated items explicitly: correspondents plus place plus content surrogate inside the edition volume's date span, which yields LIKELY-KNOWN/LOOK, never CLEAR by default.
- [medium] KNOWN depends on catalogue sender and recipient, which are wrong for a noticeable share of non-Eckert items. When the catalogue is wrong, the strict both-correspondents rule fails silently and returns CLEAR. -- fix: Carry a per-field 'verified-from-leaf' flag in items.tsv. When sender or recipient is catalogue-only, also run date+place, old cote, clear subscription and single-correspondent queries, and when those hit, return LIKELY-KNOWN rather than CLEAR. Add an item alias table (old cotes such as Anc. 8565 = Bethune 8565 = fr.3040; ink, folio and canvas; duplicate witnesses in other archives).
- [medium] The script half of LOOK works on Gallica/IIIF only. 'Next 2-4 canvases' has no neighbour enumeration for most holders, and for targets with purchased images the neighbouring folios are never ordered. -- fix: Add a per-holder neighbour adapter (Gallica manifest canvases; Huntington ptr +-n; NA scan +-n; WVO PDF page list; DECODE images in the record; Arcinsys aufn_*; RAH didl refs). For non-IIIF holders, make the REQUEST.md and copy-order template ask for the facing page, the next 2-4 leaves and any catalogue-paired sibling along with the target, so LOOK can run when the images arrive.
- [medium] The offline, USD 0 identity scan assumes public-domain IA djvu with per-volume date maps and entry segmenters. That holds for the Official Records, not for most non-Eckert editions. Building the volume lists was error-prone even for Eckert. -- fix: Give each edition-volume entry: identifiers, date span, language, access tier (djvu / be-api-only / snippet / HTRC-EF / none), segmenter type, and a positive-control row (a known letter the scan must find). Fail the adapter build if the control is missed. At snippet tiers, downgrade the verdict ceiling to LIKELY-KNOWN. Mark the printed-cipher adapter as Birch-type only, with separate detectors for spaced type and silent roman type.
- [medium] Modern, newspaper and puzzle targets have no family, and the verdict set lacks CLAIMED-UNVERIFIED. If the Spinelli rule ('a blog comment thread holds the reading, so KNOWN') is applied literally, it would block targets whose threads carry contradictory, unaccepted claims. -- fix: Add a 'modern/press' family: Cipherbrain, Cipher Mysteries, Reddit r/codes and Wikipedia talk as required WEB rows; the same publication's later issues (+1 to +8 weeks) for press puzzles; non-US newspaper APIs; coverage dates read from the API, not hard-coded. Add a verdict CLAIMED (evidence: plaintext published? method published? independently reproduced?) that never blocks and is promoted to KNOWN only when a method plus plaintext is published and reproducible.
- [medium] Whole families have no adapter, and the 'tna' list is 16th-century-centric. Roughly 60-90 of about 320 folders (20-28%) would get core only, and for them the identity scan does nothing. -- fix: Before rollout, add a minimum office-and-date adapter for each uncovered family, seeded by grepping that family's existing NOTES.md for edition names and IA identifiers. Add an 18th-century 'tna-ghq' entry (SP 104 entry books, SP 107 decyphers, BL Newcastle Add MS, Coxe, Hardwicke, HMC private-paper reports). Report the share of folders that get core only at every lane opening.
- [medium] Own-work matching and the step taxonomy are built around the reading pipeline. About a third of the 48 internal duplicates are other kinds of step, and item keys do not normalise the shelfmark systems of half the holders. -- fix: Extend --step-type with instrument, sweep, settle, handoff, index, queue, spec and lead. Key 'DONE' to the instrument name plus a unit range, and to '[retired]' markers. Add the missing shelfmark grammars to one shared normaliser used by premise_check, solver_repo_diff and prior_work. Have the shared tools write a per-folder ARTEFACTS.tsv (unit, step, file, date) instead of guessing from file names. State that private-repository duplicates are out of scope and need a check run inside the private session.
- [medium] --learn adds sources to a family with no scope, so family lists grow without bound. The next item in that family then runs date-line scans over irrelevant editions, and name-collision CONTEXT noise rises. -- fix: Make --learn require office/post, date span, language, volume identifiers, access tier and the positive-control item that taught it, and reject an entry without them. Scan only editions whose date span covers the item. Have the next scan report the added edition's hit rate, so a noisy entry is retired.
- [low] Parsing of WVO edition codes and DECODE document types uses a closed list. The real fields carry more codes and types than GPA, GPAS, Japikse and 'Partially decrypted'. -- fix: Treat any edition code in the Brongegevens field as a KNOWN-candidate lead, resolved through WVO's own abbreviation list, with unknown codes flagged rather than ignored. Add the DECODE document types 'Cleartext Publication', 'Transcription' with a <PLAINTEXT> tag, and 'paleography study [pub]' to the test fixtures.
- [low] The offline tests are almost all in-sample fixtures from the same 310 records. Nothing tests how the gate behaves on target kinds it was not built around. -- fix: Add one held-out fixture per uncovered family, built from a real folder not among the records (for example ra-celsing-sillen-1755, siena-concistoro-2308, sp87-newcastle-1743, decode-1411-hhsta-vienna-1600, kaliningrad-2015, armstrong-madison-1808). Each must assert either the right adapter composition or an explicit 'core-only' warning, and that the default is never a silent CLEAR or a false HOLD.

### practicality -- needs-changes
- [high] When a check does not actually run, the gate silently returns CLEAR. The verdict set has no NOT-RUN or INCOMPLETE state; only 403, 429 and challenge pages become HOLD. A check skipped under the --offline default, a 5xx, a reset or timeout, 'max-requests reached', a volume not yet cached, or a non-JSON reply all fall through to CLEAR. Separately, print_check.Net marks a whole host blocked after a single 403, so the first lending-only djvu poisons archive.org for the rest of a multi-item run. -- fix: Add an UNCHECKED verdict (exit 4, or a loud warning outside --strict). It is set per item for every check family the adapter requires that produced no row, a 'not searched' row, an uncached text, or a 5xx/timeout. Call print_check as a library with its own Net subclass. That subclass treats a per-item 403 on archive.org/download (lending-only) as 'fall back to be-api' and not as a host block. It also allows the playbook's one retry after a pause for 5xx and resets, and stops network mode for the run, not per item, when a host really blocks. Add an offline test in which a stubbed 502 and a stubbed lending-only 403 both yield UNCHECKED, never CLEAR.
- [high] The rank-1 edition and calendar scan is billed as offline, 1-5 s and USD 0 once cached. For a material part of its claimed 122 catches no cacheable text exists, and caching the rest has an unpriced storage or refetch cost. Cleanly scanning 60+ volumes per item also needs a prebuilt index, which the design does not specify. -- fix: Split each adapter's sources into cached-text and fts-only. Price fts-only sources as network rows with a per-item request count; they are not offline. For the cached-text families, commit one compact per-family index built once from each volume. Each volume is verified by title page and date profile, as LS-PRE did by hand. The index holds date lines with hour, from, to, page and offset, the headings, and rare 3-gram postings, so neither the full texts nor a per-item regex over 60 volumes is needed. State the one-time cost per family, including that verification step, in the build brief.
- [high] The network identity pass at the claimed 12 or fewer requests per item cannot run over 'several hundred ledger entries' within the good-citizen rule. Several of its named routes are currently dead or throttled. Wiring (3), which runs `--all-items --network` at check-solved, would issue thousands of requests per ledger folder, while catching only 5 of 130 Eckert records. -- fix: Tier it. Run the offline core on every item. Run the network pass only on the CLEAR residue of the next batch about to be read, at most about 25 items per session, and for ledger families move it to the pre-report or verifier step. Implement check_chronam as loc.gov search JSON with a hard per-session cap of about 30 and a date window, falling back to HOLD on 429. Commit prior-work.tsv network rows with a validity window (for example 14 days, reset when --learn adds a family to the adapter) so that sessions on four accounts reuse each other's results. Record the Google Books project quota in KEYS.md before wiring the pass into check-solved.
- [high] The own-work check (54 claimed catches) and the paste block's freshness rule both depend on git-blame times. Cloud sessions are shallow clones, where blame attributes every older line to the boundary commit. 'Later than the anchor' then becomes meaningless, and the result is silent false 'fresh' or 'CLEAR'. -- fix: Before using blame, require `git fetch --deepen` (or --unshallow) for the paths read. If a needed line still blames to a boundary commit, return UNCHECKED for that item, not fresh or CLEAR. Prefer machine-readable anchors: dated '## ... (<date>, TAG)' headings and the ROOM tag of the brief. Add an offline test on a shallow temp repo.
- [medium] The KNOWN precision rules contradict the catch counts. Under the design's own must-not-block rules, many of the claimed catches come out as CONTEXT, which never blocks. The 306/310 figure is fitted with hindsight, and the offline tests are built from the same records. -- fix: Add a non-terminal LEAD verdict (exit 4, like LOOK) for strong but unconfirmed hits. Examples are an exact date, hour and both correspondents in an index entry, a shelfmark-string hit, or a hit on the cipher word plus the sender. One cheap read or diff resolves it to KNOWN or CONTEXT. Calibrate the thresholds on a held-out split, not on the catch records. Report the false-block rate on the SURVIVORS list from an actual run, beside the catch rate.
- [medium] The LOOK step is priced per item at intake and depends on Gallica. Across pool folders that comes to roughly USD 100-500 and stalls whenever Gallica blocks. The design also contradicts itself on how many vision calls a look takes. -- fix: Answer a LOOK from images already listed in images/manifest.json before fetching. Make the look the first priced step of the transcription brief, with a stop rule, instead of a separate intake pass over whole pools. Use two tiers: first the cipher page and its facing page at 1200-1600 px, then the next canvases or the sibling only when the volume's convention (decipherment filed after the cipher) or a catalogue or Tomokiyo hint says so. State one call per crop and the per-call price in the brief.
- [medium] The design overlaps with gates that already exist and stacks a third prose requirement on intake_gate_check. That requirement can be gamed by pasting, and it lands as a flag day: no folder has items.tsv, while 158 open or partial targets pass the gate today. -- fix: Have intake_gate_check read prior-work.tsv, the machine file, for item coverage and run dates, and drop the pasted-block requirement. Make prior-work.tsv the Premise check's evidence, not a parallel artefact. Roll out warn-only for new deep-work briefs first, and price an --derive backfill per folder before enforcing. Reuse the existing Web and blog check section instead of emitting a second WEB row for single-letter targets.
- [medium] Reusing print_check as written would overwrite existing evidence and does not fit identity mode. -- fix: Import check_ia, check_gbooks and the other check functions and write only to prior-work.tsv. Add --identity as a library entry point that needs no phrases. Never call main() from the gate. Add a test that print-check.tsv is byte-identical after a gate run.
- [medium] The DECODE and holder 'status register' checks are described as 0-3 requests taking seconds. DECODE documents need a browser login, and the clear-share test needs a name-vs-content label on code words, which only some keys have. -- fix: Use the listing status and page count as a LEAD that sends the item to LOOK. Batch DECODE document fetches once per session, in a separate priced step. Require each key table used for the clear-share test to carry a per-row class (name, place, signature, blind, content), and return UNCHECKED where a key has none.
- [medium] The checks are ranked by records caught, not by dollars avoided. As a result the costliest piece to build (the Eckert edition adapters) comes first, while the cheapest high-value pieces are spread through the wiring. -- fix: Build in dollar order. (1) The N0-on-arrival known-answer rule in the briefs, at no tool cost. (2) Call work_queue check() from room.py --push. (3) The done-marker, parallel-column and back-reference fixes in next_steps.py and next_steps_fresh.py, where the register lag originates, instead of a parallel parser in prior_work. (4) Look as the first transcription step. (5) Solver-repo grep plus CISOSEARCHALL, WVO Brongegevens and BnF 'déchiffrement' flags. (6) The Eckert edition index last.
- [low] tools/data/prior_adapters.json is a shared JSON written by --learn from verifiers on four accounts, which invites merge conflicts and silent overwrites. --derive's candidate editions from an IA surname search need an acceptance and identity check, which is not budgeted. -- fix: Use an append-only TSV (family, source, ia_id or route, verified_by, date) checked by file_shrink_guard. Have --derive write proposals to a separate pending file, accepted only after a scripted title-page and date-profile check.
- [low] Freshness of offline sources is handled for solver clones (48 h) but not for the Tomokiyo mirror. 'Refetch if older than 48 h' also contradicts the --offline default, and sources/cyphersolver holds per-target snapshots, not a clone. -- fix: In --offline mode, report the HEAD age of each solver clone and mirror, and return UNCHECKED past the limit instead of fetching. Add a weekly If-Modified-Since refresh of the Tomokiyo pages the adapters cite, done politely, one request at a time.
- [low] HOLD (exit 4) for unread sources behind cloud-blocked hosts can pile up into owner-desk stalls, with no parallel action. -- fix: A HOLD row must name its LOCAL-QUEUE or JSTOR row and one parallel action, as next_steps --wait-only already expects. HOLD blocks only the transcription of that item, never the rest of the lane.
