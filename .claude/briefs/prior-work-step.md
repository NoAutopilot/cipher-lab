# Prior-work step (every brief that transcribes, keys, decodes, aligns, crops, looks up or audits an item)

Owner, 8 Oct 2026: "Can we improve our chances of not solving already solved work?" and "must be applicable to other work, not
just Eckert". Evidence: workflow wf_e1b87449-ccc mined all 68 AUDIT.md files and the room log (scratchpad copy in the account-3
orchestrator's session; summary in STATUS.md "Prior-work leak study, 8 Oct 2026"): 310 records of work spent on items already read,
180 of them outside Eckert, across 80 targets; about USD 1,600 avoidable. Kinds: plaintext already in print 143, a period
decipherment or clear copy on the same leaf or a sibling leaf 72 (the largest non-Eckert source), our own earlier work 49, the
holder's own public transcription 19, a modern decipherment 14. 216 were caught only by the solver or the first audit; about two
thirds were catchable in seconds by a script before reading.

**If `tools/prior_work.py` exists, run it** (`python3 tools/prior_work.py <slug> --item <id> --offline`, then `--network` for a
single letter at intake, then `--reading <file>` after decode) and obey its exit code: 3 DONE (stop, ROOM flag), 2 KNOWN with no
named consumer (stop, or proceed only as a named known-answer/key check), 4 LOOK/LEAD/UNCHECKED owed (do that one look or read
first; it blocks this item only, never the lane), 0 proceed on the CLEAR / KNOWN-PART residue it lists. **Until it exists, run the
checklist below by hand** and paste one line per check (route, query, result) into the worker's NOTES section before the first
priced step. A check that did not run is "unchecked", never "clear".

1. **Our own work (always, offline, seconds).** `git fetch` first. Grep the item's identifiers (volume + folio + canvas, never
   folio alone; DECODE R-id; WVO nr; ledger pointer; inv./scan) in the target's NOTES.md, AUDIT.md, ITERATE.md, HYPOTHESES.md,
   PROGRESS.tsv, status.json, WORK-QUEUE.tsv and the last ~1,500 ROOM.md lines. A done/[x]/[already run]/[retired] marker or an
   artefact the step would produce = DONE. A ROOM claim < 6 h old with no done line = someone else's live work: take another item.
   Registers (NEXT-STEPS.tsv, SIBLINGS-*.tsv, LOOSE-ENDS-*.md, specs) are leads, not facts: every row is re-checked here before a
   brief is written from it (SIBS-READ, 8 Oct: 6 of 6 rows were already done, glossed or printed).
2. **The leaf and its neighbours (first priced step of any transcription).** From images already on disk where possible: the
   cipher page, its facing page, two canvases before, the next 2-4 after the last leaf, and every image of a unit of 8 or fewer.
   Ask: is there an interlinear or marginal decipherment, a clear copy, a "dechiffré"/"descifrado"/"ontcijferd" heading, a clerk's
   copy? One Sonnet call per crop, two on any doubt. A gloss on the leaf or a sibling makes the text KNOWN (N0): use it as a key
   source or known answer, not as a target. A gloss on a DIFFERENT letter is not this letter's.
3. **Holder, portal and solver repositories (cached, 0-3 requests).** The holder's catalogue note / scopeContent / public
   transcription for this item (Huntington transcription field, TNA Discovery, WVO Inhoud and its print codes, BnF analysis, RAH
   "copia ... descifrada", DECODE record page count and documents -- DECODE's "Non-decrypted" flag is not evidence); Tomokiyo's
   cached pages under sources/cryptiana ("deciphered"/"attached" = KNOWN for that folio); the two solver repositories' reading
   files for this shelfmark (a directory or catalogue line is only a duplicate-effort risk).
4. **Edition and calendar identity (before reading).** The standard printed correspondence and calendars for the SENDER and the
   RECIPIENT and their office in that period (the check-solved verdict names them; KEY-OFFICES.tsv seeds them): search by date
   (+-1 day, with the period's calendar style), both correspondents, and place, with full-text where the edition is on IA/HathiTrust
   EF/Google Books (country=US). A calendar abstract that prints only the clear part makes the cipher spans the residue, not the
   whole letter. Run a positive control per edition (a letter you know is in it); a missed control = unchecked.
5. **After decode, before any class, SO row or "not located" sentence (G3).** Re-search with the decoded phrases
   (`tools/print_check.py`), including same-day replies and antecedents, other correspondents' versions of the same news, and the
   press of the day; anything sharing two rare entities or numbers within +-3 days is SUBSTANCE: the verifier diffs it before any
   N3. (Five of eight first-audit N3 Eckert entries fell this way on 8 Oct.)

Family adapters (extra routes on top of 1-5): **civil-war telegrams** -- the Huntington's own transcription of the same pointer,
OR ser. I, II and III and ORN by date + both correspondents, same-leaf siblings in other codes, and the newspaper of the day;
**printed pairs** (Thurloe/Birch type) -- the decipherment printed beside the cipher in the same edition; **Dutch** -- WVO print
codes (GPA, Groen, Japikse) opened at the cited page; **Spanish/Flemish** -- Gachard, CSP Spain, the Salazar index; **French
embassies** -- the Négociations/Correspondance volumes and Tomokiyo's per-volume pages; **German** -- Acta Borussica, RTA,
Politische Correspondenz; **US early republic** -- Founders Online and the Madison/Monroe papers.
