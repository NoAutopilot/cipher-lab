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

**Date correction, 24 Sept 2026 (LANE R worker R1, from `dmGetItemInfo` on both items' own compound-object
pointers, not the search-endpoint snippet the scout read):** the two dates above are swapped. mssDE 68 (4pp) is
dated "1781 January 31" ("A Philadelphie, le 16 Janvier 1781" is mssDE 108(A)'s own dateline, not 68's — see
below); mssDE 108(A) (8pp) is dated "1781 January 16". Page counts (68=4pp, 108(A)=8pp) match the scout's row;
only the two dates were transposed. Also, and more consequentially: mssDE 68 is **not** an undeciphered item —
its own catalogue note (full text below) says the numerical code is "translated into French in another hand",
and direct examination confirms an interlinear contemporary French decipherment runs beside the cipher on all
three of its written pages (p1-p3). Of the two "undeciphered" items in this row, only mssDE 108(A) (Jan 16, 8pp,
entirely in code except three lines of French conclusion on p6) in fact lacks any decipherment in the archive.

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
px (all lines viewed and compared by eye, not re-read digit by digit in a blind pass; one crop at native resolution); one difference seen, group 155 is **1170** on the page (Tomokiyo 470).
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
## Image capture and inventory, 24 September 2026 (LANE R worker R1)

Same CONTENTdm access route as `ciphers/huntington-blathwayt-madrid-1728/NOTES.md` (see that file for the exact
working `dmQuery`/`dmGetItemInfo`/IIIF parameter forms). Fetched all pages of mssDE 68 (4pp), mssDE 108(A) (8pp),
mssDE 37 (2pp) and mssDE 55 (2pp) — 16 images total, ~2.6 MB — to `images/`, with `images/manifest.json` (item,
page, pointer, url, file, bytes, sha1, date, catalogue_note verbatim) and `images/inventory.tsv`. `dmGetItemInfo`
on each item's own `cpd` pointer gave the full catalogue `notes` field verbatim (quoted in full below); the date
correction above comes from this field, not from re-reading the page images (the images were then checked against
it and agree).

**Full catalogue notes (verbatim, `dmGetItemInfo`, 24 Sept 2026):**
- mssDE 68 (dateh "January 31, 1781", box "mssDE Box 1"): "Autograph letter, signed, describing French naval
  operations. Approximately half of the letter is written in numerical code, paragraphs of which are interspersed
  between lines of manuscript text. In the opening paragraph La Luzerne mentions Benedict Arnold's activities in
  the Chesapeake Bay. The letter is dated at the head of the first page, and is signed by La Luzerne at the bottom
  of the third page. The numberical [sic] code has been translated into French in another hand. The fourth page
  is blank. Title supplied by cataloger."
- mssDE 108(A) (dateh "January 16, 1781", box "mssDE Box 1"): "Autograph letter, signed, describing French naval
  operations and activities of British forces. The letter is written in numerical code. Three lines of conclusion,
  in French, and La Luzerne's signature, are on the sixth page. The seventh and eighth pages are blank. The letter
  is dated 'A Philadelphie, le 16 Janvier 1781' at the top of the first page, and is addressed to Destouches on
  the bottom of the first page. Title supplied by cataloger."
- mssDE 37 (dateh "February 26, 1781", box "mssDE Box 1"): "Autograph letter, signed, describing French and
  British naval operations. Fourteen lines of the letter are written in a numerical cipher, and have been decoded
  by Destouches. A portion of the cipher discusses British activities in the war. The letter is dated Philadelphia,
  26 February, 1781 at the top of the first page, and is signed by La Luzerne at the end of the second page. Title
  supplied by cataloger."
- mssDE 55 (dateh "March 3, 1781", box "mssDE Box 2"): "Autograph letter, signed, describing French naval
  operations. La Luzerne begins the letter with congratulating Destouches on his capture of the British ship HMS
  Romulus in the Chesapeake Bay. Much of the letter is written in a numerical cipher, and is translated in another
  hand, in French. Title supplied by cataloger."

**Direct examination confirms all four notes.** mssDE 68: cipher on p1-p3 interspersed with clear French, each
cipher line followed immediately by its own interlinear French decipherment on the same page (a different hand
from mssDE 55's decipherment); p4 blank. mssDE 108(A): pure numeric cipher on p1-p6 (p3-p5 not individually
re-opened this pass, inferred from the uniform pattern on p1/p2/p6 and the catalogue note — flagged so the next
worker treats this as inferred, not directly checked, per rule 4/grade I), three lines of French conclusion plus
signature at the top of p6, p7-p8 blank; genuinely undeciphered in the archive. mssDE 37: cipher on p1-p2 with
interlinear decipherment in an amber/orange ink, closing signed "Le Ch[evalie]r de la Luzerne". mssDE 55: cipher
on p1-p2 with interlinear decipherment in pencil (visibly a different decipherer's hand from mssDE 37's), same
closing signature. Approximate token counts and per-page detail in `images/inventory.tsv`.

**Net effect on this item's status:** three of the four Huntington items in this small correspondence (mssDE 68,
37, 55) already carry a contemporary French decipherment on the page; only mssDE 108(A) (8pp, ~570 numeric tokens
by rough count) is undeciphered in the archive itself. Combined with the Tomokiyo/Cryptiana lead already in this
file (a sibling ~1200-element code at Yale, same window, key not identified there either), mssDE 108(A) is now a
much better-defined key-recovery target: three in-collection decipherments (68, 37, 55) from the same clerk's
network, all close in date (Jan-Mar 1781), are strong candidates for reconstructing the figure table that
mssDE 108(A) itself needs. Not attempted this pass (out of this worker's brief; handed to LANE R worker R2, key
recovery, per ROOM.md).

Requests this pass: hdl.huntington.org — see the combined count in this worker's ROOM.md `done` line (shared
budget with the Blathwayt target above; both fetched in one session, well under the 250-request cap).

## R6 progress, 24 Sep 2026 07:15 UTC (LANE R worker R6, stopped over cap by the lane orchestrator)

Status unchanged: open. Nothing below classifies novelty.

**Done (pushed).**
- `images/crops/`: three overlapping 2x bands per cipher page (68 p1-3, 37 p1-2, 55 p1-2, 108(A) p1-6), cut from the images already on disk; no Huntington request this session.
- mssDE 108(A): two blind Sonnet passes (`passA.tsv` 707 groups, `passB.tsv` 719), reconciled with tools/reconcile_passes.py (`recon108/`): 95.1% agreement after renumbering pass A's p5 (it skipped p5 L08, 387 ... 1113, confirmed on the image). **`ciphertext.tsv`: 719 groups, 685 H / 34 M**, every disagreement settled on the image (almost all were pass A dropping a leading 7 drawn as '>').
- mssDE 68/37/55 groups: two blind passes (`passA_decipher.tsv` 533, `passB_decipher.tsv` 531), reconciled (`recon_decipher/`, 94.6%, 29 disagreement columns). Settlements read on the image but **not yet applied** (the tool call was stopped): 68 p1 L01/3 1066; 68 p1 L02/9 391, /12 49 (M); 68 p2 L01/3 346, /8 391; L02/5 341, /7 391; L03/1 80; L05/9 1125, /11 30 (M); L06/5 534; L09/4 341, /6 391, /10 391 (pass B missed it); 37 p1 L04/7 832; L06/5 931, /8 1103 (M); 37 p2 L01/2 341; L03/4 381; L04/8 339, /9 832; L07/9 1137 (M); 55 p1 L06/8 12; L08/8 444; L09/3 713 (M); 55 p2 L01/5 40, /9 953 (M); L03/10 336 (M); L11/9 1187. The hand's 3 (a flat-topped 'ʒ') is what the passes split between 2, 3 and 9.
- `build_pairs.py`: pairs groups with the interlinear glosses, builds key.tsv (H from ink glosses, M from pencil), key_conflicts.tsv and key_yale_crosscheck.tsv, with --check. Not yet run (needs ciphertext_decipher.tsv).

**Half-done.** `interlinear_readings_draft.txt`: the interlinear decipherment read from the image by R6 for every cipher line of 68, 37 and 55, one unit per group in order ('?' doubtful, '[x:..]' struck, 'P:' pencil, '_' nothing written). To become `interlinear_readings.tsv` (columns line, hand, units) once each line's unit count is checked against the settled groups.

**Findings from the image (observed, not yet in a committed table).**
- **mssDE 68's own decipherment is complete:** every one of its 177 groups (p1 5 lines, p2 9, p3 4) has an ink gloss under it, nulls marked "nul" (1187, 394, 848). So mssDE 68 is read by its own contemporary decipherment (a transcription of it, not a solve). mssDE 37 is also fully glossed in ink (amber/brown). **mssDE 55 is not:** ink glosses stop at p1 L08 pos 7 ("Mr de la Fayette"); the rest of p1 and all of p2 carry only sparse pencil glosses in another, undated hand.
- mssDE 108(A) itself carries a few **pencil glosses** in what looks like the same hand as 55's pencil: margin "835" at p1 L01 (the group that opens 68, 37 and 55 but is absent from 108(A)), "e" under 80, "de" under 10 (x3), "ri" under 480/991 region, "les" under 947 on p3 (x4). A partial later decoding attempt on the leaf; hand and date not established.
- The Huntington code is **not** the Yale 8 Jan 1781 (Rochambeau) code as aligned by Tomokiyo/R2: vous = 32 here (Yale 32 = de la), et = 96 (Yale 96 = se), tes = 391 (Yale la), de la = 337/531 (Yale 337 = et), bons = 45 (Yale general), en = 713 (Yale un/une), de = 10. The Yale C pairs should not be applied to 108(A) at grade C; build_pairs.py writes the shared-figure agreement to key_yale_crosscheck.tsv and does not merge them.
- Consistent Huntington values seen across letters (ink): 10 de, 202 a, 125 a, 6 que, 32 vous, 941 ne, 947 les, 725 les, 331 a, 341 fre, 981 ga, 391 tes, 599 sur, 610 etre, 880 pres, 626 r, 628 sont, 940 '.', 976 '.', 1181 se, 480 ri, 832 vi, 991 ere, 1193 ti, 444 te, 1151 de, 1086 de, 1131 cent, 863 hommes, 1070 ser, 1187 nul.

**Left.** Apply the settlements above -> `ciphertext_decipher.tsv`; finish `interlinear_readings.tsv` and run `build_pairs.py` (pairs_contemporary.tsv, key.tsv, conflicts, Yale cross-check); decode.json + tools/decode_key.py on 108(A) with --check; per-token grades; matched control before any S grade; NOTES search log (Stevens's Facsimiles, Founders Online not re-run). ROOM 'for LANE W' line only when the reading is ready.
