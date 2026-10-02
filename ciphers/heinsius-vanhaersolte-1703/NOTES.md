open
Briefwisseling van Anthonie Heinsius 1702-1720, Deel 2 (GS 163) p.130, letter no. 341, read by this worker (GF-A2-8, 2 Oct 2026) from the Huygens retroboeken OCR page, with p.397-398 (letter no. 1017) and a full-text search of all 19 volumes for "geheimschrift" and of Deel 2 for "178"; the editor's footnote states the key is not known.

# Johan van Haersolte (Warsaw) to Anthonie Heinsius, two-name numeric code, 30 March 1703

QUEUE row: HU9 (`QUEUE.md`, "Huygens and Nationaal Archief correspondence editions", LANE N2 round-2 sub-heading;
`sources/huygens/cipher-letters-round2-2026-09-24.tsv`). Brief `.claude/briefs/runs/2026-09-24-lane-n2-csHU3.md`
(LANE N2, follow-up to scHU2's round-2 harvest). Models: `ciphers/heinsius-hermitage-1704` and
`ciphers/heinsius-dopff-1702` (csHU2).

## Source

Anthonie Heinsius correspondence archive, Nationaal Archief 3.01.19 ("H.A." in the edition), inv.nr. 841.
Printed in J.G. Smit / A.J. Veenendaal (ed.), *Briefwisseling van Anthonie Heinsius 1702-1720*, Deel 2 (GS163),
p.130, letter no. 341, via the Huygens `retroboeken/heinsius` viewer (no login, `resources.huygens.knaw.nl`).
Image `images/heinsius_02_GS163_130.jpg` (the printed edition's own page scan; rule 2 applies -- this remains
conditional on the print until the NA original at inv.nr. 841 is seen).

## Check-solved sweep, 24 September 2026

1. **Edition read directly this pass**, fetched via `retroboeken/heinsius/pages.json?source=2` (mapping printed
   page 130 to `page_index=137`) rather than the search pane, since the exact page and letter number were
   already known from the round-2 harvest TSV. Full letter, quoted verbatim:
   > "341. van VAN HAERSOLTE, 30 maart 1703. Eigenh. orig. H.A. 841.
   > Monsieur, Je prens la liberté de vous envoyer la lettre à mons.r le grephier soubs cachet volant, afin que
   > vous en fassiés un tel usage comme vous le trouvères à propos, car il importe beaucoup qu'on ne sçache
   > point icy les dispositions y comprises pour ne pas gâter point l'affaire dont tout paroit dépendre; car je
   > vois visiblement qu'il n'y a personne plus capable de ramener le 178 que 198, à quoy tout le succès de la
   > negotiation en dépendra. Je suis -- v. Haersolte. Warschau, den 30 maert 1703."
   Only **two** numeric codes in the whole letter (178, 198), both standing for people ("le 178", "198"), in an
   otherwise fully legible French letter -- a very short cipher extent, structurally like HU1 (Dopff, ten codes)
   but shorter still. Footnote, quoted verbatim: **"341. 1. Niet aangetroffen; de sleutel tot het gebruikte
   geheimschrift is niet bekend."** (Not encountered; the key to the cipher used is not known.)
2. **Neighbouring letters checked** (same page, printed pp.129-131, letters 338-343 read in full): no. 339
   (Portland, printed elsewhere per Japikse), no. 340 (Goudet, political/military summary), no. 342 (l'Hermitage,
   "Nouvelles uit Londen", plain), no. 343 (Tilly, plain, own footnote "Niet aangetroffen" but no cipher mention).
   None mentions a key or a decipherment for letter 341.
3. **Volume introduction / later volumes for a found key.** Not separately re-read this pass (budget); the
   round-2 harvest's own broad "cijferschrift"/"onopgelost"/"gecijferd" sweep already ran across the whole
   19-volume edition (all `source_id`s) and surfaced only this single Van Haersolte instance -- if a later
   volume had recorded the key being found, the editors' own cross-referencing convention (seen in HU10 below,
   and in HU1/HU2's footnotes citing "zie hiervóór nr. X") makes it very likely the harvest's full-text sweep
   would have caught a "sleutel gevonden" style note under those same search terms. This is inference from the
   harvest's coverage, not a direct re-check of every volume's own front matter.
4. **Post-edition literature search.** `WebSearch "Van Haersolte Heinsius cijferschrift sleutel geheimschrift
   Warschau 1703"`: results confirm Johan van Haersolte was the States-General's extraordinary envoy at the
   Polish/Saxon court, remaining until June 1703 (Dutch Wikipedia, `stadvollenhove.nl`), consistent with the
   letter's Warsaw dateline, but no article or note reporting a solved cipher for this correspondence. This is a
   search result, not proof of absence (rule 10) -- no direct BMGN/TvG/Nederlands Archievenblad index search was
   run for the Deel 2 volume specifically (its own five-post-publication-years window was not established this
   pass; Deel 1 was reviewed in BMGN c.1977 per HU1's NOTES.md, and Deel 2 likely followed within a few years of
   that, but this was not confirmed).
5. **Community lists.** `sources/cryptiana/web/dutch.htm` and `sources/cryptiana/web/unsolved.htm` grepped for
   "Haersolte"/"Hermitage"/"Sauniere": no hit in either.
6. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv`, `records-decrypted-2026-09-24.tsv`,
   `records-non-decrypted-2026-09-24-diff.tsv` grepped for "haersolte", "841", "warschau"/"warsaw": zero hits.
7. **Solver repositories.** Fresh shallow clones this pass (`dbourdeau/cyphersolver`, `aaymeloglu/unsolved-
   ciphers`), grepped word-bounded for "haersolte" and "breda": no target folder, README, or catalogue row
   names this letter or sender in either repository (the loose substring "breda" hit only unrelated corpus/
   wordlist files, not a target).

## Verdict

**Status: open.** The printed edition carries the actual ciphertext (two numeric name-codes, "178" and "198")
with the editor's own explicit statement that the key was never found ("niet aangetroffen... niet bekend"), not
merely omitted or left untranslated. No later print, community list, DECODE record, or solver repository names a
solution. Only two ciphertext tokens total -- almost certainly below unicity distance alone (LESSONS.md's "below
unicity distance" blocker class), unless a sibling letter in the same system turns up; none has yet.

**Copy status: NOT copy-free.** `www.nationaalarchief.nl/onderzoeken/archief/3.01.19/invnr/841`: the page's
embedded JSON (`viewer.response`) gives `"unittitle":"Haersolte, Johan van-, heer van Cranenburg-, uit Riga,
Frauenburg, Memel, Koningsbergen, Lublin en Warschau.","availability":"PHYSICAL","scans":[]` -- confirmed
matching sender, not digitised. Same accessor and positive control as csHU2's work (see `ciphers/heinsius-
dopff-1702/NOTES.md`). `REQUEST.md` written.

**Kind: cryptanalysis.** No known key, no solved sibling, and only two repeating-nothing numeric codes (each
appears once) in an otherwise plain letter -- the shortest and hardest of the three items in this brief; a
future worker's best lever is the same candidate key search that HU2 used (NA 3.01.19's "Cijferschrift"
subsection, invnrs 2315-2317), though 2317 is described as "probably for correspondence with England"
(Sauniere/l'Hermitage), not Poland, so it is not an obvious fit for a Warsaw-based envoy's cipher; invnr 2315
("Stukken betreffende cijfers en sleutels van cijferschrift", a general miscellany) is the more plausible lead
for this specific letter and was not individually examined this pass.

Search log (rule 10): reported above, per source. Not classified for novelty (verifier's job, rule 10).
Requests this pass (shared across HU9/HU10/HU11, see `ciphers/breda-statengeneraal-1624-25/NOTES.md` for the
full accounting): `resources.huygens.knaw.nl` 4 for this item specifically (pages.json source=2, pp.129/130/131),
`www.nationaalarchief.nl` 1 (invnr 841). WebSearch 1. No subagents.

## Web and blog check (GF-A2-8, 2 Oct 2026)

Plain web searches (WebSearch, standard):
1. `Van Haersolte Heinsius 30 maart 1703 Warschau` (sender + recipient + date): Wikipedia (Heinsius), BMGN review
   downloads, the NA 3.01.19 finding-aid PDF, lensonleeuwenhoek pages, a DBNL Huygens volume. None mentions letter 341
   or a key; nothing to open beyond the edition already read.
2. `"Heinsius" "841" Haersolte cijfer geheimschrift` (shelfmark + cipher word): only biographies of other Heinsiuses,
   catalogue pages. No hit.
3. `"plus capable de ramener le 178"` (the letter's most distinctive clear-text phrase, quoted): only boat listings and
   dictionary pages. The phrase is not on the open web outside the Huygens viewer.
4. `Johan van Haersolte envoy Poland 1703 cipher letter Heinsius` (descriptive title): Heinsius Wikipedia (mentions his
   cabinet noir), Huygens edition page (huygens.knaw.nl/?p=11458), a BL catalogue record for Haersolte letters from
   Danzig 1705-06, a Dominic Winter lot (Hedges cipher table, English, unrelated). No decipherment of letter 341.
Blog site searches:
5. Cipherbrain, `site:scienceblogs.de` "Heinsius Haersolte cipher": ten unrelated Klausis posts (Henry II device, WW2,
   Blitz ciphers). None about Heinsius or a Dutch 1703 letter; no comment thread to read.
6. Cryptiana, `site:cryptiana.blogspot.com` + `cryptiana.web.fc2.com` "Heinsius cipher Haersolte": no results.
7. Cipher Mysteries, `site:ciphermysteries.com` "Heinsius cipher Dutch 1703": van Heeck manuscript, d'Agapeyeff,
   Zodiac and similar. Nothing on this letter.
No plausible hit, so no comment thread applied. No decipherment or plaintext of the item was found on the open web.

## Premise check (GF-A2-8, 2 Oct 2026)

(a) Decipherments the folder mentions: **none found.** NOTES.md and REQUEST.md mention no decipherment, gloss or clear
copy. The one cipher statement is the editor's footnote 341.1 ("Niet aangetroffen; de sleutel tot het gebruikte
geheimschrift is niet bekend"), re-read on the p.130 OCR page this pass.
(b) Other solvers' working files: **not found.** Fresh shallow clones of dbourdeau/cyphersolver and
aaymeloglu/unsolved-ciphers (2 Oct 2026), grepped case-insensitively for haersolte|heinsius. Bourdeau has three hits,
all in other targets' keys (rakoczi1707 `393 - Heinsius Pensionaire`; windischgraetz1720 key5018 `Heinsius 112`;
bay1706 copy of the same Rakoczi document). These are Habsburg/Hungarian nomenclators naming Heinsius as a person,
not this letter or its 178/198 codes. Aymeloglu: one hit, a word-frequency list (forster-1644/lex_old.txt). Cited,
not copied.
(c) Physical neighbours: **a sibling ciphertext found, but no decipherment.** The NA original (H.A. 841) is not
digitised (`availability: PHYSICAL`, 24 Sept pass), so the edition's neighbours stand in for the leaves. Letters
338-343 (pp.129-131) were re-read with no key note. The full-text search of Deel 2 for "178" (23 hits, mostly index
pages) found **letter no. 1017, Van Haersolte to Heinsius, 11 Aug 1703, "Uit Warschau", Eigenh. orig. H.A. 841**
(pp.397-398), which prints a ciphered passage in what reads as the same system: name-codes in the 140-180 range
(`178`, `143`, `180 144`) mixed with small numbers 1-70 (`32 30 1 7 15 14`, `29 1 18 1 7 39 26 39 36 5 1 70`) inside
Dutch clear text. Its footnote 1017.1 reads "De sleutel van dit cijferschrift is niet gevonden" (the key to this
cipher was not found). So 178 occurs in both letters, and the earlier verdict's "none has yet" about a sibling no
longer holds: the cipher extent is two letters, 24 code tokens (22 in no. 1017 as printed, 2 in no. 341), not two. The whole-edition search for
"geheimschrift" (4 hits) adds only Buys 1714 (Deel 16 pp.299, 347) and a Deel 19 bibliography line. Nothing prints
a key for the Haersolte system. The other 1432 "Haersolte" hits across the edition were not paged through; that is
the next step for more siblings.
(d) Recipient's side: Heinsius is the recipient, and his edition is the one read. The other side of the cover note
(the enclosed letter "à mons.r le grephier", i.e. Griffier Fagel / States-General, NA 1.01.02 Lias Polen) was **not
searched** this pass. No US/Canadian-type state series applies. Unreachable here: the NA originals, which are
undigitised.
Requests: resources.huygens.knaw.nl 7 (pages.json 1, p.130, p.397, p.398, 3 search queries), github.com 2 shallow
clones (shared with the other three targets of GF-A2-8), WebSearch 7.
