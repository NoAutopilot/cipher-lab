# La Luzerne to Destouches, 16 and 31 January 1781 — Huntington mssDE 68 / mssDE 108(A)

Status: open

## Description

Two ciphered letters from Anne-César, Chevalier de la Luzerne (French minister to the United States) to
Charles-René-Dominique Sochet Destouches (commander, French naval squadron, Expédition particulière), in the
Charles-René-Dominique Sochet Destouches papers, 1754-1804 (bulk 1780-1781), Huntington Library, mssDE 1-120.
Per the Huntington CONTENTdm item records (found by the LANE S scout, 24 Sept 2026, QUEUE.md row U1):
- mssDE 68 (16 Jan 1781, 4pp): "numerical cipher" on pp.1-3 (5+9+4 lines), p.4 not checked by the scout.
- mssDE 108(A) (31 Jan 1781, 8pp): "numerical cipher", 11+ lines on p.1 of 8.
Two siblings in the same small collection are catalogued as already deciphered in a contemporary hand: mssDE 37
(26 Feb 1781, "decoded by Destouches") and mssDE 55 (3 Mar 1781, "translated in another hand") — a possible
in-collection key (LESSONS.md's "the key was in the archive beside the letter" pattern), not confirmed this pass.

## Check-solved sweep, 24 September 2026

**Editions first.**
- *Doniol, Histoire de la participation de la France à l'établissement des États-Unis d'Amérique* (1886), vol.
  5 (archive.org `histoiredelapart05doniuoft`, covers 1781): full-text search via the Internet Archive be-api
  fts endpoint. `"16 janvier 1781"` — 0 hits. `"31 janvier 1781" Destouches` — 0 hits. `Destouches chiffre` — 1
  hit, page 920, a letter headed "LE CHEVALIER DESTOUCHES, DU 2 MAI 1781" that mentions "le chiffre de M. le
  comte de Vergennes" and a "mémoire chiffré" enclosure — a different letter (2 May 1781), about Vergennes's
  cipher, not La Luzerne's, and not the 16/31 Jan items. No sign in this volume of the two dated letters under
  review, by phrase search only; the volume was not read page by page.
- *Stevens's Facsimiles of Manuscripts in European Archives Relating to America*: not searched directly (no
  full-text copy located this pass; its index is by document, not full-text-searchable online without a
  library subscription) — logged as not checked, not as negative.
- Rochambeau/Destouches correspondence in print: the OAC finding aid for the Destouches papers
  (oac.cdlib.org/findaid/ark:/13030/c8d79jq3/) confirms the collection and its span (mssDE 1-120) but its web
  rendering gives only the collection-level scope note, not item-level entries for mssDE 68/108(A)/37/55 —
  read via WebFetch, item detail not present in the fetched page.
- Founders Online: searched for La Luzerne↔Destouches items near these dates. La Luzerne to Washington, 27
  March 1781 (founders.archives.gov/documents/Washington/03-31-02-0137, fetched via `tools/browser_fetch.js`
  after a bare curl returned an empty 202) encloses a copy of a *different* Destouches letter (to La Luzerne,
  concerning the Battle of Cape Henry, referenced via Destouches to GW, 19 March) — not the 16/31 Jan items.
  No Founders Online document found enclosing or quoting the 16 or 31 Jan 1781 letters.

**Directly relevant lead, not a match on this shelfmark.** Cryptiana's blog (local snapshot,
`sources/cryptiana/blog/2021_09_decoded-but-not-identified-code-of.html`, linked from `web/unsolved.htm`)
carries Tomokiyo's post "Decoded but not Identified Code of Luzerne, French Minister to the United States"
(23 Sept 2021): a ciphered passage in a *different* La Luzerne letter, dated **8 January 1781**, at the
Rochambeau Papers, Beinecke Library, Yale (brbl-dl.library.yale.edu/vufind/Record/4528532) — nine days before
mssDE 68. Tomokiyo's own words: "I found a passage in code of a letter dated 8 January 1781 of Chevalier de la
Luzerne, minister to the United States... This is not an undecoded ciphertext, but I could not identify the
assignment of figures when I examined this many years ago." The figures run as high as 1199, and Daniel
Bourdeau's own notes (`cyphersolver/destaing/NOTES.md` line 13, in the shallow clone) independently record "The
Luzerne 1781 code on cryptiana's blog runs to 1199 → a different, larger code" (i.e. different from the
~600-element code Bourdeau was checking for a 1779 d'Estaing letter). This is a different item (different
shelfmark, different holding library, 8 days earlier) from mssDE 68/108(A), so it does not identify *this*
letter and this verdict is not "solved" — but it establishes that La Luzerne was using a large (~1200-element)
numerical code in exactly this window (Jan 1781) for correspondence to French commanders in America, that a
decoded plaintext of a sibling letter already exists (from the Yale item's own accompanying decoded copy, not
from cryptanalysis), and that its key/figure-assignment was not identified by Tomokiyo. Combined with mssDE
37/55 being catalogued as already deciphered in the same small Huntington collection, this is a strong
key-recovery lead for a future worker, not evidence that mssDE 68/108(A) themselves have been read.

**Community lists.** Cryptiana's own unsolved-ciphers list (`sources/cryptiana/web/unsolved.htm`) mentions the
Luzerne 8 Jan 1781 item (see above) but nothing under Destouches or mssDE. Live-web search
("Destouches Luzerne cipher 1781 Cipherbrain", "cipher mysteries", "reddit codes") returned no discussion of
this item on Cipherbrain, Cipher Mysteries, MysteryTwister or r/codes.

**DECODE.** Login is known broken (ASKS.md row 1); not attempted. The DECODE catalogue snapshot inside
Aymeloglu's repository (`unsolved-ciphers/catalogue/decode-catalog.csv`) has four "Luzerne" rows, all British
Library Add MS 32263 (Luzerne↔Vergennes correspondence, 1779-83) — a different collection, not Huntington
mssDE, and not Destouches. No DECODE row found for Huntington mssDE material.

**Bourdeau (dbourdeau/cyphersolver).** Shallow clone, 24 Sept 2026. `grep -rliE "luzerne|destouches"
--include=*.md` hits: `catinat1691/NOTES.md` (false positive — "vallées de Luzerne", a Piedmont valley, unrelated)
and `destaing/NOTES.md` (the Luzerne-1781-code note above, about the Yale item, not mssDE). No folder for this
target, no mssDE mention anywhere in the repo.

**Aymeloglu (aaymeloglu/unsolved-ciphers).** Shallow clone, 24 Sept 2026. `grep -rliE "luzerne|destouches"` hits
only the DECODE catalogue CSV rows described above (BL Add MS 32263). No folder, no README/TARGETS/SHORTLIST
mention, no mssDE mention.

## Verdict

**open.** No solution, key, plaintext or documented attempt on mssDE 68 or mssDE 108(A) specifically was found
in any of the six sources swept (editions checked by phrase search, not read cover to cover; web, community
lists, DECODE cache, Bourdeau, Aymeloglu). Doniol vol. 5 and Founders Online were checked and do not print these
two letters by phrase search. Stevens's Facsimiles and the Rochambeau printed correspondence proper were not
reachable this pass and are logged as unchecked, not negative. The Tomokiyo/Cryptiana lead above (a sibling
~1200-element code, decoded elsewhere, key not identified) is reported as a lead for a future solver, not as a
match on this item; report what was found and where it was not found, no novelty classification made here.

**Copy status.** Copy-free: both items are digitised, viewer pages load without a login wall at
`hdl.huntington.org/digital/collection/p15150coll7/id/<pointer>` (per the LANE S scout's 24 Sept 2026 check).
No REQUEST.md needed for U1.

## Access notes

Huntington CONTENTdm: item-info calls only this pass (`dmGetItemInfo`), not the search endpoint (already run by
the scout); request count below.

## Searched, 24 September 2026 (for CLAUDE.md rule 1)

Cipher's name/shelfmark in a search engine (web); sender's printed correspondence (Doniol); calendars/state-paper
series (n/a, US domestic collection, no CSP series); community list comment threads (Cryptiana local + live
search); DECODE (cache only, login broken); both solver repositories (shallow clone, grep).

## Key recovery, step 1-2: the Beinecke 8 Jan 1781 code passage (LANE R worker R2, 24 Sept 2026)

Status unchanged: open. This section is about the sibling letter at Yale, not yet about mssDE 68/108(A).

**Item.** La Luzerne to Rochambeau, Philadelphia, 8 Jan 1781, Beinecke GEN MSS 146 (Rochambeau Papers) box 2 folder
137, Yale OID 16490985 (the brbl-dl VuFind 4528532 link now redirects to collections.library.yale.edu/catalog/16490985,
which answers curl with a 202 challenge; the IIIF manifest and image API serve curl directly). Catalogue: "Letter
signed. 10 1/2 pages ... Partly in code, with accompanying decode on a separate page". All 9 openings fetched at 1800 px
to `images/yale/` with `manifest.json` (sha1 per file): code 240 groups on c6-c7 (Tomokiyo's pp.6-8), a separate
contemporary decode sheet on c8-c9, rest clear French. Route: access playbook 1 (IIIF, curl).

**Alignment.** `alignment_yale_8jan1781.tsv` (one row per group: figure, unit aligned, grade),
`key_tomokiyo.tsv` (per figure), both regenerated and checked by `build_key_tomokiyo.py [--check]` against the
Cryptiana snapshot plus the image correction list. Figures: Tomokiyo's transcription checked against the image at 1800
px (all lines viewed; one crop at native resolution); one difference, group 155 is **1170** on the page (Tomokiyo 470).
Plaintext: Tomokiyo's print checked against the decode sheet; the sheet reads "le **reste** de l'armée", "quitta",
"je l'assurai promptement du **zèle** (interlined over a struck word) avec lequel votre **armée**", "le **soin** de ces
mesures", "laissé **aux** général Washington", and after "les ameriquains" a struck-out phrase (the last 8 groups,
814 532 362 305 511 372 148 334, left U).
Grades per token (240): **C 127, M 106, U 7** (no H: there is no key sheet; the decode sheet is known plaintext).
Per distinct figure: C 73, M 99, U 6 (178 figures seen).

**What the pairs show about the code.**
- It is a **two-part (randomised) code**: on the 72 C single-meaning pairs, Spearman rho between figure order and
  alphabetical order is -0.13, shuffle p = 0.26 (10,000 shuffles, seed 1781). So no interpolation between known
  figures is possible (grade S by interpolation is ruled out for this code).
- It is **syllabic with homophones**, not a word code: dan 1173 serves dans/danger/dangereuse (4x), de-fec-ti-on
  664 575 812|278 959 (twice, two homophones for "ti"), re-elle-ment 424 864 860, mo-ment 595 860. Homophones seen:
  de 664/921/(842?), que 416/872, ce 892/903, la 769/391, un(e) 1096/713, et 894/337/181, vous 573/799/1185,
  se 389/96. A code group for "de la" (32, 3x). 532 and 350 fall at sentence ends (stop or null, M).
- Range 4-1199 in 240 groups, consistent with Bourdeau's note (destaing/NOTES.md l.13) that it runs to ~1200.
- Bourdeau (github.com/dbourdeau/cyphersolver, shallow clone 24 Sept 2026, grep "Luzerne"): note only
  (destaing/NOTES.md l.13, destaing/profile.json), no figure/plaintext pairs; nothing copied.

**Consequence for mssDE 68/108(A).** If the Huntington letters (16 and 31 Jan 1781, eight and twenty-three days
later, same sender) use this code, 73 C figures (the commonest function words and syllables) give partial coverage at
best; the M rows need a second alignment pass before use. Steps 3 onward (mssDE 37/55 contemporary decipherments,
blind passes of mssDE 68/108(A), decode_key.py, matched control) wait on LANE R worker R1's Huntington images, not
pushed at 05:18 UTC; not started.

**Search log for LANE V (prior decipherment of mssDE 68/108(A)), 24 Sept 2026.** Checked this session: Tomokiyo's
Cryptiana post (local snapshot) and the Yale item (a different letter, to Rochambeau; its decode sheet does not
mention Destouches); Bourdeau's repository by grep for "Luzerne" (no mssDE, no Destouches). Not found in either.
Earlier sweep (same day, section above): Doniol vol.5 phrase search, Founders Online, OAC finding aid, Cryptiana list,
DECODE cache in Aymeloglu's repo (BL Add MS 32263 rows only), Aymeloglu grep; not found. Not checked: Stevens's
Facsimiles, the Huntington's own catalogue notes for mssDE 68/108(A) beyond the scout's, DECODE live search (LANE N's
host), Google Books (LANE V's). No novelty classification made.

Requests this session: collections.library.yale.edu 12 (1 record page 202, 1 manifest, 9 images, 1 crop), all >=1.5 s
apart, descriptive UA; github.com 1 shallow clone (Bourdeau). No Huntington, Gallica, Google Books or DECODE requests.

Suggestion (not done): a second, independent alignment pass over the 106 M rows by a separate session, working from
images/yale/c6-c9 only, to promote or correct them before the key is applied to mssDE 68/108(A).
