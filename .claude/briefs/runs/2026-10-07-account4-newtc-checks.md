# NEWT-C check-solved jobs (LANE NEWT-C-account-4, written 7 Oct 2026 00:0x UTC by date -u)

Parent: LANE NEWT-C-account-4 (session_01XXcLqsU7GkbYZoN7rPaBzx), brief .claude/briefs/runs/2026-10-06-acct3-newtargets.md PART C.
Steps copied from LANE NEWT-B-account-2's jobs brief (.claude/briefs/runs/2026-10-06-account2-newtb-checks.md) so both parts check the
same way. One worker per job below. Model Sonnet. Cap USD 7 per job (check-solved 5 + premise check 2), box 70 min; stop at 80% of either.
No transcription, no key application, no cryptanalysis, no paid orders, no DECODE login.

## Selection (why these six)

Source: QUEUE.md "NEWT-C scout, 6-7 Oct 2026 (account 4)" (17 kept rows from sources/newt-scout/2026-10-06/S1-S4). Top six by EV,
pools first, BnF tie-breaker. Held: rijks-margaretha-parma-key-1567 (EV 0.9 but one ~330-sign sample printed on a key sheet: not a
pool, and the sample's text is likely the key's own illustration). Each scout row's full columns are in its S<n>.tsv; read your row
first. Your job's own question is the duplicate-effort and already-in-print risk named below; answer it before anything else.

## Jobs

| job | slug (new folder) | scout row | item | the question to settle |
|---|---|---|---|---|
| NC-CROI | colbert-croissy-london-1668-74 | S4-02 | Colbert de Croissy (ambassador, London) <-> Louis XIV / Lionne, 1668-74, BnF Mélanges de Colbert 149-167 (Tomokiyo names e.g. Colbert 149 f.109, 159 f.203, 164 f.105); key already on disk: ciphers/colbert155-beziers-1670/keys/key_colbert_croissy_1668.tsv | github.com/el-descifrador/cabinet-noir has ~27 files naming Croissy and Bourdeau targets/colbert/NOTES.md names the Croissy key: list which Croissy London letters either repo already read (quote), and the DECODE status of each Colbert 149-167 record. Also whether the dispatches are printed in clear (Mignet, Négociations relatives à la succession d'Espagne; Recueil des instructions Angleterre). Open only the letters neither repo nor print covers |
| NC-SANC | fr16147-sancy-constantinople-1611-18 | S4-01 | Achille de Harlay de Sancy (ambassador, Constantinople) -> Louis XIII, 1611-18, BnF fr.16145-16149 (interlined decipherments on most letters; Tomokiyo Sancy Cipher-2) | Bourdeau's cyphersolver CATALOGUE.md lists Sancy fr.16148 ff.200,206 (item 311) "readable with a key in hand": is it his stated next step (score down per scout.md)? Count letters with NO interlinear decipherment (sample canvases via the manifest; Gallica probe first) -- the pool is only the unglossed residue |
| NC-BETH | fr3669-bethune-rome-1625 | S2-01 | Philippe de Béthune (ambassador, Rome) <-> Herbault / Louis XIII, 1624-25, BnF fr.3669 (also fr.3484, fr.3675); contemporary decipherment under/beside the cipher on ff.12-13 | are the Béthune Rome dispatches printed in clear anywhere (the 1667 Ambassade extraordinaire de MM. ... Béthune? Avenel's Richelieu Lettres for the replies)? How many letters carry no decipherment on the leaf? |
| NC-MONL | fr4735-monluc-lansac-poland-1573 | S2-02 | Jean de Monluc, bishop of Valence, and Guy de Lansac (Polish election embassy) -> Charles IX / Catherine, 1572-73, BnF fr.4735; Tomokiyo henryiii.htm "Ciphers of Monluc and Lansac, Sent to Poland (1573)" | Noailles, Henri de Valois et la Pologne en 1572 (1867, 3 vols, IA) prints much of this embassy's correspondence: which fr.4735 cipher letters are printed in clear there, and which have a déchiffrement on the leaf? Residue = letters neither |
| NC-ENGA | fr15972-england-ambassadors-1595-1608 | S4-03 | French ambassadors in England (La Fontaine, Boissise, Dujardin, La Boderie) -> Henri IV / Villeroy, 1595-1608, BnF fr.15972; Tomokiyo reconstructs one key per ambassador | Ambassades de M. de La Boderie en Angleterre (1750, 5 vols) prints Boderie's 1606-11 dispatches in clear: which fr.15972 cipher letters are in it? Check also Laffleur de Kermaingant (L'ambassade de France en Angleterre sous Henri IV, Boissise/Harlay). Residue = letters neither printed nor glossed |
| NC-BAUG | clair369-baugy-castille-maurier-1616 | S4-05 | Nicolas de Baugy (agent, The Hague) and others -> Mangot / Louis XIII, 1616-17, BnF Clairambault 369 (Tomokiyo: Baugy f.2 and f.59 "undeciphered") | Bourdeau's CATALOGUE.md lists Baugy Clair 369 ff.2,59 (item 309) as readable with a key in hand: his stated next step? Is Baugy's Hague correspondence printed (Ouvré, Lettres de Baugy 1616-17? check) and are ff.2/59 in it? |

For every job: read the scout row and S<n>.md, then check-solved as below. A verdict of `found-solved` or `blocked` is a full answer.
Slug may be adjusted to house style; say so.

## Steps (each worker, its own job only)

0. First action `python3 tools/room.py --start` (if it fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`).
   `date -u`. ROOM claim via tools/room.py with your job id, slug, cap 7, box end time, "for LANE NEWT-C-account-4".
1. Read .claude/briefs/check-solved.md in full and run it for your item: six sources (web incl. the model-solve family; print:
   the standard edition/calendar opened by you, with pages; community lists and the "## Web and blog check" section with the
   four plain searches and the three blog site searches, comment threads opened; DECODE login-free listing via
   `tools/decode_list.py` and the record page; Bourdeau and Aymeloglu -- fresh shallow clones in your scratchpad, grep by
   shelfmark, DECODE id, sender, date, read the hit files, quote any sentence about this very letter verbatim; and the
   solver's own planning text for it). Editor's-note phrase sweep and HTRC fallback as that brief says.
2. Premise check (a)-(d) as in the same brief, written as "## Premise check (<job>, <date>)".
3. Create ciphers/<slug>/NOTES.md: line 1 the bare status word (open, partial, found-solved, blocked, ...), line 2 the one
   sentence naming the edition/calendar you read and the pages, then sources, the verdict reasoning, the two sections above,
   and "## While waiting" if blocked or waiting. No ciphertext.txt unless a transcription already exists in print or on
   DECODE as an attached document (then copy it as transcribed, with source and date).
4. Run `python3 tools/intake_gate_check.py <slug>` and paste its output into NOTES.md. Fix the citation until it exits 0 when the
   verdict is open/partial; a blocked/found-solved verdict may stay nonzero -- say so.
5. Only if the verdict is open or partial and the gate exits 0: write specs/<slug>.json (follow specs/README.md and an
   existing spec such as specs/rayburn-2004.json: slug, name, date, language_candidates, ciphertext_pending or ciphertext with
   source, alphabet, constraints, cheap_tests_in_order with test 1 = the table's named test made concrete, matched_control,
   cheap_test_done [] , judge block, value, model, written). Do NOT run the test.
6. If found-solved: say who read it and where (README F0/F1/F2), and what correction or key it leaves to hand on.
7. Leave shared registers (CATALOG.md, QUEUE.md, status.json, WORK-QUEUE.tsv) to the lane. Commit only your folder and spec by explicit path,
   `git fetch origin main && git rebase FETCH_HEAD && git push origin HEAD:main`.
8. ROOM done line via tools/room.py: verdict, gate exit code, spec written or not, request counts per host, "for LANE NEWT-C-account-4".
   Report in five lines; stop.

Good-citizen rule and the CLAUDE.md host table for every request (DECODE 1.5-2 s apart; BL IIIF is dead; TNA Discovery API ok;
Google Books with country=US and the key; OpenAlex/S2 with keys). At most two Sonnet subagents. Report what was found and where it
was not found; do not classify novelty; never the words new, first, novel, solved, cracked for anything this project did. Never
print or commit credentials. Never call AskUserQuestion. Never name the owner.
