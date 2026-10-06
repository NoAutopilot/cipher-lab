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
a key for the Haersolte system. The other 1432 "Haersolte" hits across the edition were paged through on 3 Oct 2026 (A2P4-HAER section below).
(d) Recipient's side: Heinsius is the recipient, and his edition is the one read. The other side of the cover note
(the enclosed letter "à mons.r le grephier", i.e. Griffier Fagel / States-General, NA 1.01.02 Lias Polen) was **not
searched** this pass. No US/Canadian-type state series applies. Unreachable here: the NA originals, which are
undigitised.
Requests: resources.huygens.knaw.nl 7 (pages.json 1, p.130, p.397, p.398, 3 search queries), github.com 2 shallow
clones (shared with the other three targets of GF-A2-8), WebSearch 7.

## Haersolte paging across the Heinsius edition (A2P4-HAER, 3 Oct 2026, 18:33-18:50 UTC)

Intake gate (`python3 tools/intake_gate_check.py heinsius-vanhaersolte-1703`): "open (line 1) -- edition/page or full-text-search
citation found within 6 lines", exit 0. Reading step only; no transcription, key application or cryptanalysis was done.

Step run (the folder's named step): `retroboeken/heinsius/search_in_text/index_html?search_term:ustring:utf-8=Haersolte&batch_start=N`,
N = 1, 21, ... 1421, 2.2 s apart, descriptive UA. Result: 72 result pages, 1431 of the 1432 reported hits parsed (one snippet line not
parsed), all HTTP 200, kept in `haersolte_hits.tsv` (volume, printed page, snippet). Hits per volume (Deel 1-19): 33, 85, 106, 105,
88, 93, 85, 84, 57, 80, 102, 81, 55, 96, 111, 103, 64, 0 (Deel 18), 3. The search returns one snippet per page, not per mention,
and it matches the name, so it lists pages, not ciphered letters.
Positive control: the 30 Mar 1703 page (Deel 2 p.130, letter 341) is in the hit list and the OCR page reproduces the known
footnote 341.1 and the codes 178 and 198 (same on re-fetch of the page). The control can differ: a page not holding the name would not appear.

Cipher-word filter on the 1431 snippets (sleutel, cijfer, geheim, niet gevonden, niet aangetroffen): 5 snippets.
- **Deel 3 p.208, letter 588, Van Haersolte, 1 July 1704, H.A. 918** (OCR page read). Footnote 588.1: "De brief is gericht aan d'Alonne en niet
  ondertekend; de gespatieerd afgedrukte passages zijn door Haersolte in cijfer geschreven en door d'Alonne opgelost." So the edition
  prints a contemporary decipherment (by d'Alonne) of Haersolte's cipher passages in a 1704 letter. The OCR text does not mark which words
  were spaced; the page image is the only witness (not fetched: 1 crop allowed, not needed for this step). It is 1704, a year after
  letters 341 and 1017, and no code numbers appear in the printed text, so whether it is the same system is **not known**. Graded: no
  reading made by us (0 H/C/S/M/I tokens); the printed deciphered passages are period decipherment text, not ours.
- Deel 12 p.528 (letter 892, 26 Nov 1711) and Deel 16 p.4 (1714): "niet aangetroffen"/"niet gevonden" refer to an advice and a copy of a letter, not a key.
- Deel 5 p.680 (1706), Deel 6 p.344 (1707): the word "geheim" in the sense of secret; no cipher.

Deel 2 (1703) read page by page: 70 OCR pages (printed pp.81-600, the pages the search listed) via
`retroapp/service_heinsius/02_163/html/heinsius_02_GS163_<p>.html`. Grepped for sleutel, cijfer, geheimschrift, opgelost and for numeric
codes 140-199: the only cipher footnote is 341.1 (control). One further page shows a code in the running text, **Deel 2 p.362, letter 929, Van
Haersolte, 24 July 1703, Warschau, H.A. 841**: "... de republic[k] ... ris 142 , als de coning van Sweden op dat point soude blijven staen"
(code 142, in the 140-180 name-code range the 178 and 143/144/180 codes of letters 341 and 1017 sit in). There is no cipher footnote
(929.1 is only "Aanwezig in H.A. 841"), and the OCR may have dropped the rest of a spaced-type passage. Counted as one candidate sibling token
(grade M at best, a single number in OCR); the page image would settle it. Letter 1017 (pp.397-398) was not among the 70 pages and was
not re-read (read in GF-A2-8).

Where it was not found: no printed key or decipherment of the 1703 system (codes 178, 198) in any of the hits or the 70 pages read. The
edition's coverage of Deel 1 and Deels 3-19 for Haersolte letters in cipher was only filtered through snippets, not read page by page (Deel 3's
Haersolte letters run 1704, a different year); that is a snippet filter, not a negative for those volumes.

Requests: resources.huygens.knaw.nl about 150 (1 root, 72 search pages, 1 first-page repeat, 2 redirect probes, 2 pages.json, 2 Deel 3 OCR
pages, 70 Deel 2 OCR pages). That is **over the brief's 120 cap**: the Deel 2 page batch was sized from the hit list after the paging was
done (70 pages, not the ~35 estimated) and ran in the background, so the cap was passed before the count was checked. All requests were at
least 2.2 s apart, descriptive UA, no 429/403. WebSearch 0, vision 0, subagents 0.

## Verdict (A2P4-HAER, 3 Oct 2026)

**Status: open (unchanged).** Paging all 1432 Haersolte hits and reading 70 Deel 2 pages found no key or decipherment of the 1703 system. Two
leads for more material: letter 929 (24 July 1703, Deel 2 p.362, code 142 in the OCR text, same H.A. 841) and letter 588 (1 July 1704, Deel 3
p.208, passages in cipher printed deciphered by d'Alonne, different year).

## Page images of letters 929 and 588 (R11A-HEIN, 6 Oct 2026, 14:26-14:29 UTC)

Route: `retroboeken/heinsius/pages.json?source=2` and `?source=3` (one each) for the `image_url`/`html_url`, then the page JPEGs
(native size as served, about 864x1376) `images/heinsius_02_GS163_361.jpg`, `_362.jpg`, `images/heinsius_03_GS169_208.jpg` and the three
OCR pages. Crops: `python3 tools/iiif_lines.py --image images/heinsius_02_GS163_362.jpg --out images/crops362 --prefix p362 --region
0,380,872,330 --lines-per-crop 4 --distance 15` (4 crops), the same with `--out images/crops362fn --region 0,1100,872,279 --lines-per-crop 8
--distance 10` for the footnotes (1 crop), and `--image images/heinsius_03_GS169_208.jpg --out images/crops208 --prefix p208 --region
0,60,864,640 --lines-per-crop 6` (5 crops). One read of the crops by this worker (no subagent).

**Step 1, letter 929 (Van Haersolte, Warsaw, 24 July 1703, H.A. 841, Deel 2 pp.361-362).** Crop `crops362/p362_L02.jpg` prints, in roman
(not spaced) type: "dat de republicq soude konnen vervallen in die gedagten om hunne wapenen te voegen tegens 142², als de coning van Sweden
op dat point soude blijven staen" (the OCR's "ris" is "tegens"). Footnote 929.2 (crop `crops362fn/p362fn_L01.jpg`, and the OCR page):
"Er stond eerst ,,de Russen", maar dat woord is uitgekrabd en vervangen door het cijfer; het oorspronkelijke woord is echter leesbaar
gebleven." So in the original Haersolte wrote "de Russen", scratched it out and wrote the code over it, and the editors could still read
the word: **142 = "de Russen"** (the Russians), on the editors' reading of the original. It is the only code in the letter; nothing else on
pp.361-362 is spaced or numeric. Grade for that one token: C (the writer's own clear word under his code, reported by the edition; image of
the print only, rule 2 -- conditional on the editors' reading of H.A. 841). Counts: C 1, H/S/M/I 0.
What it does and does not give this folder: 142 does not occur in the target letter 341 (codes 178, 198) or in letter 1017 (143, 144,
178, 180, and the small numbers), so **no token of the target is read by it**. It is one more data point that the 140-180 range is a
name/nation list in the same correspondent's 1703 system (same H.A. 841 bundle), and 142 = de Russen beside 143/144 is a weak hint that
neighbouring codes are other powers or nations -- an inference (I), not a reading. No key file exists in this folder and none was made
(brief: no key change without a pre-registered test).

**Step 2, letter 588 (Van Haersolte to d'Alonne, 1 July 1704, H.A. 918, Deel 3 p.208).** The crops show the spaced (letter-spaced)
passages footnote 588.1 says Haersolte wrote in cipher and d'Alonne deciphered. Read once at this resolution (grade M for the boundaries):
"coning van Sweden" (l.6), "electie" (l.9), "den koning van Sweden" (l.10), "coning van Polen" and "Fransche parthije" (last two lines);
other names on the page (cardinael, palatin van Posen, prins Alexander, Bugh, Weisel) look roman, not spaced, but the scan is too coarse to
be sure. The middle of the letter is an editorial summary in italics (Haersolte's refusal to state a preference, his letter to Jessen), not
the letter's text. **Not usable as a crib for this folder now:** the edition prints only the clear text of the ciphered passages, never the
cipher numbers, so there is no cipher/clear pair on the page; the letter is to d'Alonne, not Heinsius, and a year later (1704), so even the
same system is not established. What it does give: a list of clear words the 1704 cipher carried (koning van Sweden, koning van Polen,
electie, Fransche parthije), which become a crib list if H.A. 918 (with d'Alonne's interlinear decipherment, if he wrote one) is ever seen
beside H.A. 841.

Requests: resources.huygens.knaw.nl 8 (2 pages.json, 3 JPEG, 3 OCR html), all >= 2.2 s apart, descriptive UA, all HTTP 200. Gallica 0,
WebSearch 0, subagents 0.

## Verdict (R11A-HEIN, 6 Oct 2026)

**Status: open (unchanged).** Code 142 in sibling letter 929 is glossed by the edition (the scratched-out original word "de Russen" is
legible under it), grade C, one token; it reads nothing in the target letter. Letter 588's spaced passages are period decipherments without
their cipher numbers, so not a crib on the print alone. The 1703 system's key is still not located.

## Van Haersolte letter list, Deel 2 (and Deel 3 page list) (R11A-HEIN2, 6 Oct 2026, 15:15-15:22 UTC)

Brief: list every Van Haersolte letter in Deel 2 not among the 70 pages A2P4-HAER read, and say for each whether the print shows cipher
numbers, spaced-type deciphered passages, or a number-to-word pair stated by the edition.

Route. The `toc1` chronological-letter accessor that works for `retroboeken/willemiii` does **not exist** for this book:
`retroboeken/heinsius/toc1/index_html?correspondent:ustring:utf-8=Haersolte` answers HTTP 404 (Huygens error page), and the book's root
page links only the 19 volumes. The Deel 2 person index (pp.634-635, OCR) lists pages where Haersolte is *mentioned* ((I), 11, 15, 44,
146, 154, 158, 227, 271, 287, 292, 318, 436, 480, 481, 522, 531, 548; "reis naar Polen" 50, 60, 63, 81, 99); it does not list his own letters
(pp.130, 362, 397 are absent), so it is not a letter list. Used instead: every 1703 Haersolte letter is filed "H.A. 841", so a full-text search
for `841` (`search_in_text`, 7 result pages, 130 hits parsed, 83 in Deel 2) lists his letter pages. Positive control: pp.130 (letter 341) and 362
(929) are in the 841 hit list. 23 Deel 2 hit pages were not among the 70 read (or 361-362, 397-398); p.615 is an index page and p.326 a false hit
(letter *number* 841, l'Hermitage), so 21 pages were fetched (OCR html), plus p.595 for the end of letter 1499.

Result, Deel 2: **21 Van Haersolte letters not previously read** (`deel2_letters_r11a.tsv`: nos. 16, 38, 41, 72, 88, 119, 130, 155, 166, 181,
203, 286, 296, 426, 481, 511, 843, 1197, 1333, 1483, 1499; 4 Jan - 29 Dec 1703; Riga, Frauenburg, Memel, Warsaw). Fifteen are printed only as a
title ("Nouvelles uit Riga") or an editor's Dutch summary, which would not reproduce cipher; six print some full text (41, 155, 426, 1197, 1499,
and 286's summary runs to p.107). **None** of the 21 shows a cipher number, a spaced-type passage or a cipher footnote on the pages fetched;
grep for sleutel/cijfer/geheim/ontcijfer/opgelost/uitgekrabd/gespatieerd/chiffre and for 2-3 digit numbers in running text found nothing
cipher-related (the "geheim" hits are "geheimraad"/"geheime dienst"). **No number-to-word pair is stated anywhere in them; no key change.**
Graded tokens read by us: 0.

Cross-check: a whole-edition search for `gespatieerd` (the editors' word for passages printed letter-spaced because they were in cipher; 5
result pages, 96 hits) gives **no hit in Deel 1 or 2** and one in Deel 3 (p.208, letter 588, already known). On the OCR index, then, the 1703
volume never uses the spaced-deciphered convention: the edition prints the 1703 Haersolte codes (341, 929, 1017) as bare numbers, with a
decipherment only where the writer's erased word survived (929.2). A search for `uitgekrabd` returned **0** hits although footnote 929.2 contains
the word (R11A-HEIN read it on the page image), so the OCR index misses that word: the zero is a failed positive control, not a negative.

Deel 3 (1704, H.A. 918): the same search for `918` (7 result pages, 138 hits) gives **103 Deel 3 pages** (`hits_HA918_r11a.tsv`), too many to read
under this brief's 60-request cap; not read. Only p.208 (letter 588) intersects the `gespatieerd` hits.

Where it was not found: no printed key, no spaced deciphered passage, no number-to-word pair for the 1703 system in the 21 Deel 2 letters above,
nor any `gespatieerd` footnote in Deels 1-2. Not covered: Haersolte letters whose OCR mangles both the name and "841" (none known; the 841 search
and the 1432-hit name paging overlap well but are both OCR); the small-number sequences of the 1017 type on the 70 pages A2P4 read were grepped
only for codes 140-199 (A2P4 section); Deel 3's 103 letter pages.

Requests: resources.huygens.knaw.nl 49 (toc1 1 [404], book root 1, pages.json 1, index pp.634-635 and 659-660 4, `841` search 7, `918` search 7,
`gespatieerd` search 5, `uitgekrabd` search 1, letter pages 22), all >= 2.2 s apart, descriptive UA, all HTTP 200 except the toc1 404. WebSearch
0, vision 0, subagents 0.

## Verdict (R11A-HEIN2, 6 Oct 2026)

**Status: open (unchanged).** 21 more Deel 2 Haersolte letters listed and read: none carries cipher, and the edition never prints a spaced
decipherment in Deel 2. The 1703 system's cipher extent is unchanged (letters 341, 929, 1017); the only glossed code is still 142 = de Russen
(C, 1 token, letter 929). The key is still not located in print.

## Deel 3 (1704, H.A. 918) page read (R11A-HEIN3, 6 Oct 2026, 15:37-15:46 UTC)

Brief: for each of the 103 Deel 3 pages in `hits_HA918_r11a.tsv`, say whether the print shows cipher numbers, spaced (deciphered) passages or a
number-to-word pair stated by the edition, and check them against the target letter's codes (341: 178, 198; with 1017's 143, 144, 180 and 929's 142).

Route: OCR html `retroapp/service_heinsius/03_169/html/heinsius_03_GS169_<page>.html`, 2.2 s apart, descriptive UA. Pages below 100 are
zero-padded (`_012.html`, read from `pages.json?source=3`); the first pass used unpadded names and got HTTP 500 (BookServicePageNotFoundError) on
22 pages. Inside the 110-request cap, 6 of those 22 were re-fetched (pp.33, 40, 46, 51, 67, 71: the autograph or full-text ones by their
snippets); **16 were not read** (pp.12, 13, 16, 20, 23, 25, 31, 43, 48, 52, 59, 63, 74, 77, 81, 86: all "Ondert. orig." letters whose snippet opens
with the editor's Dutch summary, a form that does not reproduce cipher; a summary not read is still not a negative). Per page: `deel3_pages_r11a.tsv`.

Result on the 87 pages read: 80 Van Haersolte letter headings (nos. 87 to 1327, 1 Feb - 31 Dec 1704; 23 "Eigenh. orig.", 15 with 600+ characters
of text). Script checks, per page:
- cipher keywords (cijfer, ontcijfer, gespatieerd, opgelost, chiffre, sleutel, uitgekrabd): **only p.208** (letter 588, footnote 588.1, known).
- code numbers in running text (a 2-3 digit number after an article or preposition, dates, quantities, page and letter cross-references
  excluded): **none**. Positive control (string level, the printed sentences on disk in this file): the same pattern catches "le 178 que 198"
  (letter 341) and "tegens 142" (letter 929); it would miss an OCR-mangled context like the "ris 142" A2P4 met on p.362.
- the target codes 142/143/144/178/180/198: present only as printed page numbers (pp.142, 178, 180, 198) and in the index on p.494 -- **no code
  token**.
- letter-spaced runs in the OCR: present, but they are OCR spacing of words with m/o glyphs ("h o m m e", "c o m m e", "d o e n", "m o e t"),
  not editorial spacing; and the method fails its own positive control -- letter 588's five spaced cipher passages come through the OCR mostly
  closed up (only "c o n ." and "H o . Mo." survive). So the OCR cannot show spaced-type passages; only the editors' footnote (588.1) can, and the
  keyword check above covers that.

Where it was not found: no printed key, no code number, no number-to-word pair, and no cipher footnote other than 588.1 in the 87 Deel 3 pages
read. Not covered: the 16 unread pages above; spaced passages the editors may have printed without a footnote (the OCR cannot show them; only the
page images would); Haersolte letters whose heading OCR misses the name (the block split matched HAERSOLTE/HAKRSOLTE/HALRSOLTE). Graded tokens
read by us: 0. No key change.

Requests: resources.huygens.knaw.nl 110 (1 test page, 102 pages of which 22 were HTTP 500 [wrong file names, my error], 1 pages.json, 6 re-fetched
pages), all >= 2.2 s apart, descriptive UA, no 429/403. WebSearch 0, vision 0, subagents 0.

## Verdict (R11A-HEIN3, 6 Oct 2026)

**Status: open (unchanged).** Deel 3's H.A. 918 pages show cipher in one letter only (588, d'Alonne's deciphered passages, no numbers); none of
the target's codes (178, 198) or the 1703 name codes appears as a code in 1704 print. The 1703 system's key is still not located in print.

## Next step (cheap, depends on no one)
1. Re-grep the 70 Deel 2 pages A2P4 read for the small-number runs of letter 1017's kind (1-70 inside text), which A2P4's 140-199 grep could not
   catch: about 70 requests to resources.huygens.knaw.nl (one session, >= 2 s apart), ~USD 1, script only.
2. Deel 3 (1704): R11A-HEIN3 read 87 of the 103 H.A. 918 pages (no cipher beyond letter 588). Left: the 16 unread pages listed in its section
   (zero-padded names `_012.html` etc., 16 requests, ~USD 0.3, script only).
3. Ask the NA (REQUEST.md) to include H.A. 918 beside H.A. 841, so d'Alonne's decipherment of the 1704 letter can be compared with its cipher.

## While waiting
The NA original (H.A. 841) is undigitised; REQUEST.md stands. Independent of that: next steps 1-2 above.
