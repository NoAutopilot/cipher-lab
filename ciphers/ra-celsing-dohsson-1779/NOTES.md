# Celsing–d'Ohsson correspondence with cipher key, 1779-1782

**Status: open**
Findley, Enlightening Europe on Islam and the Ottomans (Brill 2019; Google Books hf-GDwAAQBAJ, partial view) Books API full-text search by this worker (GF-A2B-2, 3 Oct 2026) for Mouradgea + Celsing + cipher/chiffre/code/key: snippets cite the "Celsing papers" (fol. 79, Pera 6 May 1779; Konvolut 12 p.759 in *Making Sense of Global History*, 2001) but none names a cipher, chiffre or key -- snippet-level, not a page-by-page read.

## Item

Correspondence and letter-drafts between Ulric Celsing (Swedish minister to Dresden/Vienna, later at
Constantinople) and Ignace Mouradgea d'Ohsson (dragoman at the Constantinople legation from 1763, first
dragoman 1768, later Swedish minister at Constantinople 1795-1799), 1779-1782, with an explicit cipher key
("Chiffernyckel") filed in the same folder. Shelfmark SE/RA/721512/IV/IV 1/5 ("Beskickningsarkivet från Biby",
sub-series "Ulric Celsings tid i Dresden, Wien och Sverige 1780-1805 / Korrespondens"), Riksarkivet i
Stockholm/Täby. Found by the LANE S scout of 24 September 2026, QUEUE.md row R1 ("Dutch and Nordic archive
candidates" section), kind: recovery (the key is catalogued beside the letters, per LESSONS.md's "key beside the
letter" pattern). Catalogue note in full: "Korrespondens med Ignace Mouradgea d'Ohsson... Brev och brevkoncept
ligger tillsammans: - Chiffernyckel. Se även bilaga till brevkoncept 13/10 1780." — several years of letters and
drafts filed with the key, plus a cross-reference to an appendix on the 13 Oct 1780 draft specifically.

No transcription or image exists in this repository; the catalogue snippet above (from the Riksarkivet Sök-API)
is the only text seen. `ciphertext.txt` is not created, per CLAUDE.md rule 2 (image over transcription — none
exists to transcribe from).

## Check-solved sweep, 24 September 2026

Run directly by this worker (not the Workflow tool), per `.claude/briefs/check-solved.md`'s six sources.
6/6 checked, 0/6 found a solution, key transcription, or documented prior attempt on this specific item.

**Editions first:**
- Carter Vaughn Findley's *Enlightening Europe on Islam and the Ottomans: Mouradgea d'Ohsson and His
  Masterpiece* (Brill, 2019) — the standard modern biography/study of d'Ohsson. WebSearch for reviews and the
  publisher/author pages found no mention of a Celsing cipher correspondence, and the book is a recent Brill
  monograph, not on Internet Archive full text (checked: `archive.org/advancedsearch.php?q=Mouradgea+d%27Ohsson`
  returns 14 hits, all d'Ohsson's own 18th/19th-century printed works — *Tableau général de l'Empire othoman*,
  *Histoire des Mongols*, *Des peuples du Caucase* — none is a modern edition of his correspondence with
  Celsing). Not checked: the book's own text (not open-access; Google Books not available to this worker, see
  below).
- Svenskt Biografiskt Lexikon's own article on Ulric Celsing (`sok.riksarkivet.se/sbl/Artikel/14755`, fetched
  directly) mentions his diplomatic correspondence is preserved in the state archives and cites letters with
  G.M. Armfelt and J.V. Sprengtporten, but says nothing about d'Ohsson or a cipher.
- No published edition of the Celsing–d'Ohsson correspondence itself was found by title search (WebSearch:
  "Ulric Celsing d'Ohsson chiffernyckel cipher key Riksarkivet"; "Carter Findley d'Ohsson biography Celsing
  correspondence cipher").
- Google Books slot not held this session (per brief); not queried.

**Web:** WebSearch "Ulric Celsing d'Ohsson chiffernyckel cipher key Riksarkivet" and "Carter Findley d'Ohsson
biography Celsing correspondence cipher" — results are biographical (Riksarkivet SBL, Wikipedia, Wikidata,
Findley's own author pages) with no mention of this cipher or its contents.

**Community lists:** `sources/cryptiana/` (PAPERS.tsv, READABLE.tsv, blog/, web/) grepped for "celsing",
"ohsson"/"d.ohsson", "mouradgea" — no hits. Live Cryptiana/Cipherbrain/Cipher Mysteries sites not fetched this
pass (no reason to expect Swedish 18th-century diplomatic archive material there and the repo snapshot is
current practice per LESSONS.md; not chased further under the usage budget).

**DECODE:** No login attempted (per this brief; DECODE login status is disputed between briefs and out of
scope here). `sources/decode/` holds only a login-form snapshot, no record cache for this item. WebSearch
restricted to `site:de-crypt.org` for "Celsing", "Ohsson", "Vellingk", "de Geer" returned no de-crypt.org
results at all (the search engine did not index the query to that domain; de-crypt.org's own record search
needs a login this worker did not attempt). Status: unchecked beyond this, logged as such, not scored negative.

**Bourdeau (`dbourdeau/cyphersolver`):** fresh shallow clone (`--depth 1`, 24 Sept 2026). `grep -rli` for
"celsing" and "d.ohsson\|mouradgea" across the whole tree matches one file, `roell1809/turk_inv.txt` — a Dutch
(Nationaal Archief) inventory for an unrelated target (`roell1809`), which independently names "G. Celsing,
Zweeds gezant te Constantinopel" (1753) and "Mouradgea (te Constantinopel)" as real historical figures inside a
1750s-60s Dutch-Swedish diplomatic dispute, not this letter or key. No `README.md`/`TARGETS.md`/
`SOLVED_CATALOGUE.md` entry for this target.

**Aymeloglu (`aaymeloglu/unsolved-ciphers`):** fresh shallow clone, same grep, no matches at all (not even the
roell1809 coincidence — that target is Bourdeau's, not his).

**Riksarkivet digitisation check (Sök-API, `data.riksarkivet.se/api/records`):** queried
`text=chiffernyckel Celsing&type=Record` (2 attempts needed — the first hit a transient `SSL_ERROR_SYSCALL`
through the agent proxy, consistent with the same-day W1 worker's note; the retry after a ~5s pause returned
200). 2 hits, both Beskickningsarkivet från Biby records (this item, SE/RA/721512/IV/IV 1/5, and the related
R2 item SE/RA/721512/II/II 1/II 1 B/4). This item's record: `onlyDigitisedMaterials: false` — **not digitised**.
No IIIF manifest or image link in the API response.

**Verdict:** open. No prior solution, key transcription, or serious attempt found anywhere searched. Nothing
above rules out that the catalogued "Chiffernyckel" is a genuine, applicable key (LESSONS.md's most productive
pattern, "the key was in the archive beside the letter") — but confirming that requires the physical folder.
d'Ohsson's independent notability (as a major primary source on the Ottoman Empire in his own right) means a
specialist edition of this specific correspondence is plausible and worth another pass once the Findley
monograph's text or a French/Swedish diplomatic-history bibliography is reachable.

**Not digitised — copy order needed.** See REQUEST.md.

## Request log

24 Sept 2026: no personal data logged here; the archive request itself (if the person sends it) is logged by
date and archive only, per CLAUDE.md rule 9.

## Web and blog check (GF-A2B-2, 3 Oct 2026)

Plain web searches (WebSearch, standard):
1. `Celsing d'Ohsson 1779 1782 letters cipher key chiffernyckel` (sender + recipient + date): Wikipedia d'Ohsson, an
   auction catalogue, History Studies (DOAJ, Nov 2023), travelogues.gr -- biography and the 1784 Paris letter; no cipher.
2. `"SE/RA/721512" Biby Celsing chiffer` (shelfmark + cipher): unrelated Celsing pages, patents; no hit on the item.
3. `Mouradgea d'Ohsson Ulric Celsing correspondence deciphered secret dragoman Constantinople` (title; no clear or
   decoded phrase exists to quote): Kure Ansiklopedi, Cornucopia, authority files, Findley's book page -- no
   decipherment.
4. Google Books API (key, country=US), 7 queries: `"Celsing" Ohsson`, `"Celsing" "d'Ohsson" chiffre`,
   `Celsing Mouradgea`, `Mouradgea Celsing cipher|chiffre|code key`, `"Celsing papers"`: Findley 2019, Findley 2001
   (*Making Sense of Global History*), Meddelanden från Svenska Riksarkivet 1891, *Svenskarna och Österlandet* 1952,
   *Türkische ... Urkunden im schwedischen Reichsarchiv* 1945 -- snippets about the Tableau and the Celsing papers, none
   about a cipher in this correspondence.

Blog site searches:
- Cipher Mysteries + Cipherbrain + Cryptiana (combined domain filter, "Swedish legation Constantinople cipher 18th
  century Celsing d'Ohsson"): two unrelated Cipher Mysteries posts (Guinigi, van Heeck); nothing on this item.
- Cryptiana alone (`cryptiana.blogspot.com`, `cryptiana.web.fc2.com`, "Celsing Ohsson Swedish cipher Constantinople"):
  no Cryptiana page returned.
- Cipherbrain alone (`scienceblogs.de`, "Celsing Ohsson schwedische Chiffre Konstantinopel"): Swedish gravestone,
  Livijn almanac (opened for ra-morner-welin, see there: Livijn 1800, Stockholm University, read in its comments by
  "Kent" -- unrelated), Catinat, Soglia -- none about Celsing or d'Ohsson.

No plausible hit for this item; no comment thread about it. Requests: WebSearch 6, Google Books API 13.

## Premise check (GF-A2B-2, 3 Oct 2026)

- (a) Folder's own mentions: the catalogue note names a "Chiffernyckel" filed with the letters and an appendix
  ("bilaga") to the draft of 13 Oct 1780 -- a key beside the letters, possibly a deciphered or clear appendix; not
  digitised (`onlyDigitisedMaterials: false`, 24 Sept 2026), so not openable. No spec. Unreachable.
- (b) Other solvers' working files: fresh shallow clones 3 Oct 2026, dbourdeau/cyphersolver (e8b4287) and
  aaymeloglu/unsolved-ciphers (d2800bb), `grep -rliE "celsing|ohsson|mouradgea"`: one Bourdeau file,
  targets/roell1809/turk_inv.txt (an inventory naming G. Celsing, 1753 -- unrelated target, as on 24 Sept);
  Aymeloglu none. Bourdeau's riksarkivet1628 is a 1628-33 group, unrelated. Not found.
- (c) Physical neighbours: the folder is undigitised; the sibling R2 item (SE/RA/721512/II/II 1/II 1 B/4) is also
  catalogued without images. Unreachable.
- (d) Recipient side and the specialist literature: Findley 2019 used the "Celsing papers" (snippet: fol. 79, Pera
  6 May 1779), and *Making Sense of Global History* (2001) cites them by Konvolut 8 and 12 -- a specialist has read this family's papers, so a reading of cipher passages there
  cannot be excluded until his notes are read; snippet search found no cipher mention (status line). *Europe and the
  Porte: Swedish diplomatic reports 1795-1797* (2001) covers d'Ohsson's later dispatches, outside 1779-82. Not found
  at snippet level; Findley's full text unreachable (partial view).

## While waiting

Waiting on a copy order (REQUEST.md). The one action that depends on nobody: query the Riksarkivet Sök-API
(`data.riksarkivet.se/api/records`) for every record under SE/RA/721512 (Beskickningsarkivet från Biby) with
`onlyDigitisedMaterials: true`, to find any digitised volume of the same mission archive (a key or dispatch register
of the 1779-82 Constantinople legation).

## Re-check (CS-BATCH3, 3 Oct 2026)

The "While waiting" action (Riksarkivet Sök-API, `data.riksarkivet.se/api/records?text=Celsing&onlyDigitisedMaterials=true`) was tried twice, one retry after 5 s: curl error 35, SSL_ERROR_SYSCALL on connect to data.riksarkivet.se, HTTP 000 both times; the host is unreachable from this container, logged, not retried further. Verdict unchanged (`open`); the step stays as written, to be run from a session that can reach the host.

## Next step (NO-CRACKS, 5 Oct 2026)

next: the Riksarkivet Sok-API query (`data.riksarkivet.se/api/records?text=Celsing&onlyDigitisedMaterials=true`) from a host that reaches data.riksarkivet.se: a LOCAL-QUEUE catalogue-lookup row for the runner (the cloud got HTTP 000 twice, 3 Oct 2026), ~$0.3 to file. Who acts: agent. Source: this file's "## Re-check (CS-BATCH3, 3 Oct 2026)"; written by NO-CRACKS (account 3) because tools/next_steps.py found no next-step line in this file.
