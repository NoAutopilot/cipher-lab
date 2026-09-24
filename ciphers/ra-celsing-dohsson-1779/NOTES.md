# Celsing–d'Ohsson correspondence with cipher key, 1779-1782

**Status: open**

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
