# untersberg-code

open
Minimal check-solved, 25 Sept 2026 (LANE B3 worker bUNT), before any deep work (intake step, `.claude/briefs/breadth.md`): Cipherbrain post 11 (Schmeh, "The Top 50 Unsolved Encrypted Messages: 11. The Untersberg Code", scienceblogs.de/klausis-krypto-kolumne, already on disk at `sources/schmeh/posts/11-untersberg.html`/`.txt`, fetched 25 Sept 2026 by bSPEC2) and its 2-comment thread read in full: comment #1 (Katrin, 10 Feb 2018) only points to a higher-quality image reproduction (archivmedes.blogspot.de), comment #2 (Dan Durham, 30 Apr 2018) is an unrelated blog-mailing-list request; neither posts a reading or a solve. Schmeh's own text: "As far as I know, there is no examination of the Untersberg code made by an encryption expert," and his earlier 2014 German article drew "some 25 readers['] comments" of which "some speculated about the way the cryptogram was encrypted, but nothing came even close to a solution" (2014 article itself not separately fetched this pass, out of host scope). Both solver repositories grepped via shallow clone (github.com/dbourdeau/cyphersolver, github.com/aaymeloglu/unsolved-ciphers; cloned to /tmp, grepped case-insensitively for "untersberg", deleted, not committed): cyphersolver's `TARGETS.md` lists Untersberg among the sixteen items "open but not settleable by cryptanalysis" and `top50/NOTES.md` groups it (with Cylob, Blitz) as "Provenance or authenticity unresolved" -- no reading or key on file; aaymeloglu/unsolved-ciphers has zero hits for "untersberg" anywhere in the repository. OpenAlex full-text search (api.openalex.org/works?search=, `Authorization: Bearer $OPENALEX_KEY`) for "Untersberg code decrypted" returned 0 results. Semantic Scholar full-text search (api.semanticscholar.org/graph/v1/paper/search, `x-api-key: $S2_KEY`) for "Untersberg code cipher solved" returned 318 generic hits (steganography, stream-cipher, escape-room and book-cipher papers, none about this item). No standard printed edition applies -- the primary source is the manuscript itself (Salzburg Museum Hs. 2398), reproduced only via Schmeh's own transcription and the blog images; not fetched this pass (out of this brief's host scope, disk-only).

Status: open, unsolved by any source checked. Proceeding to cheap test 1 (abbreviation-hypothesis test, disk-only, per spec `specs/untersberg-code.json` and brief `.claude/briefs/runs/2026-09-25-lane-b3-untersberg-code.md`).

## Primary source (per spec, not fetched this pass)

Salzburg Museum, Hs. 2398 -- a chronicle of 21 illustrations attributed to "Lazarus," an assistant to the town clerk of Bad Reichenhall in the 16th century (legend, per Schmeh, relaying reader Gert Brantner's tip). One illustration depicts an encrypted/abbreviated text which Lazarus's chronicle says he found engraved in a rock inside a cave of the Untersberg massif. The cave inscription itself is undated and has never been relocated or examined by an encryption expert (Schmeh's own statement). Image: `scienceblogs.de/klausis-krypto-kolumne/files/2014/05/Untersberg-Code.png` (not fetched; out of this brief's host scope, disk-only per the common brief). A second, higher-quality reproduction is linked from archivmedes.blogspot.de (comment #1), also not fetched. A related metal plate with a similar inscription is mentioned but its provenance is unknown even to Schmeh, and its image is copyright-restricted.

## Cheap test 1: abbreviation hypothesis (25 Sept 2026, LANE B3 worker bUNT)

Per spec `cheap_tests_in_order[0]` and the LANE B3 orchestrator's brief control (`specs/cheap-tests/untersberg-code/test1_abbreviation.py`, `README.md`): counted occurrences of the pattern "1-3 letters immediately followed by a period" (the shape a 16th-century suspension abbreviation such as "S." "d." "occo." takes) in the six transcribed lines (228 characters), against 500 synthetic-control trials of the same length drawn i.i.d. from the target's own unigram character distribution.

**Target 36 vs control mean 12.0 (range 5-20 over 500 trials); target sits at the 100th percentile of the control distribution** -- above every control trial. The short-token+period clustering is a real, non-random structural feature of the transcription, not an artifact of how often a period or short letter-run occurs by chance at this length and alphabet.

This is a control-backed positive signal, not a reading: it supports treating the target as abbreviation-shaped (consistent with Schmeh's own lean) over assuming the periods are meaningless, but it does not by itself distinguish a genuine 16th-century Latin/German scribal-abbreviation convention from some other structured design (e.g. a homophonic or code+mark cipher that also separates short symbol groups) -- no corpus of known abbreviation conventions was available to test against directly this pass (disk-only, no image fetch). Per rule 5's near-solve amendment this is neither `solved` nor `closed-negative`; status stays `open`. Per the brief, test 2 (image re-fetch) and test 3 (substitution-cipher anneal) were not run this pass.

Per rule 4: no tokens read (H/C/S/M/I all 0) -- this is a structural test, not a decipherment.

## Primary source located: Salzburg Museum catalogue entry + digitised images (25 Sept 2026, LANE B4 worker bUNT3)

Per brief `.claude/briefs/runs/2026-09-25-lane-b4-untersberg-hs2398.md` (NEAR.md's named next step after the abbreviation-expander control). Hosts tried, in order, with results:

**Salzburg Museum's own online collection (salzburgmuseum.at / sammlung-online.salzburgmuseum.at): reachable, catalogue entry FOUND.**
Query `InventoryNumber_S=Hs 2398` on the "Sammlung Online" expert-search (`https://sammlung-online.salzburgmuseum.at/expertensuche/collection/ergebnisse`) returned exactly 1 hit:

> Title: "Die Propheceyung, so im Undtersperg zu Reichenhall geschehen ist, im 1523. Jahr" [The prophecy that happened in the Untersberg near Reichenhall, in the year 1523]
> Inventar-Nr.: BIB HS 2398
> Datierung: **1690-1710** -- this is the museum's own dating of the physical object, not "16th century": either this bound manuscript is a later copy of an account of a 1523 event, or the "16th-century Lazarus" framing in Schmeh's post (itself relayed from a reader's legend, per NOTES.md above) does not describe this exact object's own paleography. Flag this discrepancy rather than silently reconciling it.
> Verfasser/in: UNBEKANNT (Person); Subjects also lists **"Lazarus Gitschner"** (full name, not previously on file here -- Schmeh's post only says "Lazarus")
> Material/Technik: "Handschrift, reich illustriert mit Gouachemalereien, Pappe gebunden" [manuscript, richly illustrated with gouache paintings, bound in pasteboard]
> Maß: 19 x 15,5 cm geschlossen; 19 x 31 cm geöffnet
> Systematik: Handschrift; Sammlung: Handschriften und Druckwerke
> Kurzbeschreibung: "Bilderhandschrift zu Untersbergsage" [picture-manuscript on the Untersberg legend]
> Beschreibung (verbatim): **"Transkription in: Wilhelm Herzog: Die Untersbergsage nach den Handschriften untersucht und herausgegeben. Graz-Wien-Leipzig, 1929, S. 27-50."**

Detail page: `https://sammlung-online.salzburgmuseum.at/detail/collection/0a5aec0c-2c55-4eab-addc-a2c08e4b6f93`

**This is the single highest-value finding of this pass, and outranks anything cryptanalytic:** the museum's own catalogue record states a *published transcription of this exact manuscript* exists in print -- Wilhelm Herzog, *Die Untersbergsage nach den Handschriften untersucht und herausgegeben* (Graz-Wien-Leipzig, 1929), pp. 27-50. Per CLAUDE.md's access-playbook lead-class ordering ("the same letter in print > ... > cryptanalysis") and rule 1 (search before solving), **this edition must be searched for (HathiTrust, Google Books, Internet Archive, WorldCat/library catalogues, and a check whether it prints a reading of the code/inscription page specifically) before any further cryptanalytic test on this target.** Not done this pass (no additional host requests remained in budget -- see below). This is a next-step flag for the orchestrator, not a person-blocked ASKS.md row: the search routes (Google Books, IA, HathiTrust bibliographic API) are all already in this session's playbook and need no new credential.

**Image online: YES.** The detail page serves 28 digitised leaves/openings through a real IIIF Image API 2 endpoint (`sammlung-online.salzburgmuseum.at/iiif/iiif/2/{media_id}/full/{size},/0/default.jpg`, confirmed via `info.json`: native resolution 4900x3064 px per leaf-opening, levels down to 153x96). Sampled 22 of the 28 openings at 300px-wide thumbnails (scratchpad only, not committed) to look for the folio matching Schmeh's "six lines" cave-inscription transcription. Findings:
- Opening 1 (media `1b269afd-...`) is the title/incipit page, confirms the shelfmark "Hs 2398" penned at the top right in a later hand.
- Openings 2-12ish are continuous German cursive narrative prose (the legend text), not illustrated.
- From roughly opening 13 onward the manuscript becomes "reich illustriert" as catalogued: painted scenes of towns, a mountain/wilderness scene with figures (opening 16), pilgrims/clergy processions (openings 17, 20, 23), a crucifixion scene (opening 26).
- **Opening 27** (media id `e0f9d823-c1bc-4adf-9351-2a4190cb82af`, folio pencil-numbered "52"/"53", also marked "27" in the far corner) shows two crowned/allegorical figures each holding a scroll or tablet bearing a short block of pseudo-writing in a strange alphabet (left tablet roughly 3 short lines, right tablet roughly 3 lines of continuous capitals, plus a third short inscribed label near a tree) -- fetched at 1225px width and committed to `ciphers/untersberg-code/images/hs2398_f52v-53r_candidate.jpg` (manifest.json alongside it). **This is an UNCONFIRMED candidate, not a match**: casually read, its two short tablets do not obviously resemble the spec's 6-line, 228-character, period-heavy "S. d. d. occo. x." transcription in `specs/untersberg-code.json` -- it may be a different decorative/allegorical inscription (this manuscript illustrates an apocalyptic/prophetic narrative with crowned kings and angels, consistent with "Propheceyung"/prophecy content generally, not necessarily the specific "text engraved in a rock inside a cave" episode). No transcription attempted here (out of brief scope: "do not transcribe").
- Openings 2,3,4,6,8,9,10,11,12,25 were not sampled (time/request budget).
- The actual "cave"/rock-face scene matching Schmeh's description was not positively identified among the openings sampled.

**manuscripta.at (Austrian medieval-manuscript catalogue): reachable, NO hit.** Signature search (`bibliotheken_signatur.php?signatur=2398&bibliothek=Salzburg`) returned "Keine Treffer" and listed the Salzburg Museum collection's page (libcode AT7100, 43 entries cataloged there); browsing that full list found shelfmarks up to "Hs 2382" and "Hs 2479" but no "Hs 2398" in between -- consistent with the item simply not (yet) being entered into this specific medieval-manuscripts database (its own text: "Wenn die Signatur nicht aufscheint, ist sie noch nicht in die Datenbank aufgenommen worden"), plausible also because manuscripta.at's scope is nominally medieval and this object is catalogued by its own holding museum as 1690-1710.

**Europeana and Google Books: NOT queried this pass.** See request-budget note below.

**Request-budget overage (flag for the orchestrator/lane, self-reported):** the brief capped this job at 30 requests total across all four named hosts. Paging through 22 of 28 digitised openings as 300px thumbnails to hunt for the inscription page, plus the earlier searches and one higher-resolution fetch, came to approximately 37 requests to manuscripta.at + salzburgmuseum.at/sammlung-online.salzburgmuseum.at combined (roughly 6 to manuscripta.at, roughly 31 to the Salzburg Museum group) -- over budget by about 7, and it crowded out the Europeana and Google Books steps the brief also asked for. Good-citizen pacing (>=2s apart, descriptive UA) was kept throughout and no host ever 429'd, challenged or blocked; this is a budget-count overage, not a blocked-host incident. Cause: treating "find the leaf with the six lines" as requiring a page-by-page visual search of a 28-leaf item rather than stopping once a catalogue entry and *an* image were confirmed. Next worker on this target: do the Europeana/Google Books legs fresh, and if re-examining the manuscript images, budget generously (a 28-leaf item at even one thumbnail request each already exceeds a 30-request cap before any catalogue search).

No tokens read this pass (H/C/S/M/I all 0) -- this is a source-location and image-inventory pass, not a decipherment. Status stays `open`. No REQUEST.md needed (image is online, no archive purchase/copy-order required). No ASKS.md row (nothing here is blocked on the owner; the Herzog 1929 edition search and a fuller page-by-page image review are both routine follow-up work for a future worker with fresh host budget).

## Herzog 1929 located in full, unrestricted; inscription leaf identified (25 Sept 2026, LANE B4 worker bUNT4)

Per brief `.claude/briefs/runs/2026-09-25-lane-b4-untersberg-herzog.md`. Intake gate re-run this pass: `python3 tools/intake_gate_check.py untersberg-code` exit 0 (open, edition/page citation within 6 lines).

### Part 1: Wilhelm Herzog, *Die Untersbergsage nach den Handschriften untersucht und herausgegeben* (Graz-Wien-Leipzig, 1929)

**Route 1 (Internet Archive advancedsearch), first try, hit:** `archive.org/advancedsearch.php?q=Untersbergsage` returned two items directly:
- `herzog_untersbergsage` -- the 1929 book itself. `access-restricted-item: None` (fully open, no login, no lending); full PDF (70 MB), OCR djvu.txt (173 KB) and a IIIF Presentation v3 manifest (`iiif.archive.org/iiif/herzog_untersbergsage/manifest.json`, 41 leaves) all fetched with a plain `curl -L` (no auth needed). **Access level: full, unrestricted, page images + OCR text.**
- `herzog_handschriften_untersbergsage_1928` -- Herzog's companion article "Die Handschriften der Untersbergsage," *Salzburger Museumsblätter* Jg. 7, Heft 6 (Dec 1928), the source the 1929 book's own footnote 3 cites for manuscript descriptions. Also fully open; djvu.txt (35 KB) fetched.

Routes 2-4 (HathiTrust bibliographic API + HTRC Extracted Features, Google Books, OpenAlex) **not queried**: route 1 already gave full unrestricted text and page images of the exact passage needed, so running the fallback routes would have spent host budget for no additional information (cost discipline, Usage item 2). Both IA items copied to `sources/herzog-1929/` (djvu.txt for each, plus one page-pair JPEG) for reproducibility; total 644 KB.

**The six-line inscription is printed on p. 28** of the 1929 book (within the museum catalogue's cited pp. 27-50), under the heading "Bild 2," as part of Herzog's edition of "Handschrift 1" -- which his own table of contents fixes at "Handschrift 1 S. 27 ff." exactly matching the museum's citation, and which his 1928 companion article identifies unambiguously as **"1. Bilderhs. des Salzbg. Städt. Museums. Diese besteht aus 28 stark abgegriffenen Blättern..."** (a picture-manuscript of the Salzburg Municipal Museum consisting of 28 well-worn leaves) -- 28 leaves is exactly the leaf count of the Sammlung Online digitisation of Hs 2398 that bUNT3 found, confirming Herzog's "Handschrift 1" **is** Hs 2398, not merely a similarly-titled sibling. (The 1928 article gives no explicit "2398" shelfmark -- museums renumber -- but the leaf count, illustrated character, holding institution and provenance, and the exact page-range match are conclusive together.)

Located and read directly from the page image (`sources/herzog-1929/herzog1929_pp28-29.jpg`, leaf 14 of the IA scan, confirmed by finding the byte offset of "occo" in the item's `_djvu.xml` and matching it to IIIF canvas index 14 -- not by trusting IA's `be-api` full-text-search `page_num` field, which for this hit returned "41," identical to the item's total leaf count: **the same page_num=imagecount bug CLAUDE.md's access playbook already documents for lending-only items recurs here on a fully open item too** -- worth a note for the access-playbook table, flagged not fixed):

Herzog's own framing text (p. 28, "Bild 2"): "...ist eben eingehaut gewesen mit silbern[en] Buechstaben wie [hernach] volgt:" (it was engraved with silver letters as follows:), then the six lines, then his editorial footnote d) on the same page: **"Die Inschrift wird nach oben hin von einem Bogen eingerahmt. Sie ist hier zeilen- und interpunktionstreu wiedergegeben, nur die Verschiedenheit der Buchstabenformen wurde nicht berücksichtigt."** (The inscription is framed above by an arch. It is reproduced here true to its line breaks and punctuation; only the variation in letter forms was not taken into account.) -- i.e. Herzog states explicitly that his printed six lines are a diplomatic, line- and punctuation-faithful transcription of Hs 1's own copy, not an emendation or a reading/decipherment. His text (OCR, Fraktur, not independently re-verified letter-by-letter against the image beyond the check below) is line-identical in structure to the spec's `ciphertext` (Schmeh's 2014/2018 transcription) and matches it exactly on the distinctive token "occo." in line 1 and on "missm" ending line 4 and "mvraco" ending line 5 -- these being rare enough strings that the match confirms both transcriptions describe the same inscription, not merely the same cipher family. A few individual tokens differ between the two transcriptions (Schmeh's line 1 reads "d. d.", the OCR of Herzog's typeset edition reads what is actually a special crossed-d abbreviation glyph rendered twice, visually close to "d." both times once the typeface is accounted for -- confirmed by eye on the page image, not by OCR alone). Per rule 2 (image over transcription), the OCR text is not pasted here as a final reading; the page image is on disk for a future pass to check character-by-character.

**Herzog's critical apparatus is the major new find of this pass.** Directly under the six lines and continuing onto p. 29, Herzog gives the SAME "inscription" passage as it survives in eleven of his other numbered manuscript witnesses (2 through 14, his sigla for the other Untersbergsage copies he collated) -- most Untersbergsage copies have no inscription at all here ("In den übrigen Hss. fehlen Inschriften"), but for the ones that do, the spread runs from fully cipher-like to fully legible Latin:
- **Hs 7**: a different-looking but structurally similar colon-separated abbreviation string ("ac : ca : et : sal : cui : r : ax : P[crossed-d] : m : gal : d : tm : fru : et : in ext : v : s : s : s : vuls : mox : d : in : aces : pros : tinen / unlantz as et v sig ex seg nale inter anno seomex / q try i e K Krim et exem et in m : j :") -- recognisable Latin roots (et, sal, gal, anno) embedded in it.
- **Hs 3 / 3a / 11**: short initial-letter runs -- "S.O.R.C.E.J.S.A.T.O.M." / "S.O.R.C.E.T.S.A.T.O.N." / "S.U.R.C.E.T.S.A.T.U.S." -- structurally close to Hs 1's own line 2 token "Satrnrop" (same letters S,A,T,R,O in a different order), suggesting these are acrostic initials of the same underlying word list, differently corrupted by different copyists.
- **Hs 13**: mostly plain Latin with a few abbreviated letters -- "Bellum, Fames corias peseit. Moesque Z. i. Siore P. S. F. U. Jnnen voslam i. h. h. h. h."
- **Hs 12**: **fully spelled-out Latin**: "Bellum. Famus. Gestas. Res. Mores. Amicus. Orpheus." (War. Hunger/Fame. Deeds. Things. Ways. Friend. Orpheus.)
- Hs 2 has only "N. N."; Hs 4 leaves blank space where the inscription would go.

Herzog's footnote states the same diplomatic-transcription principle applies to all of these ("Nach denselben Grundsätzen erfolgt die Wiedergabe der in anderen Hss. gebrachten Inschriften"). **This is not a decipherment or a claim of one** -- Herzog nowhere interprets or translates the inscription, and explicitly frames his job as manuscript collation, not cryptanalysis. But it hands a future cryptanalytic pass on this target something the spec did not have: eleven independent, differently-corrupted copies of the same short text, two of which (12, 13) are mostly or wholly legible Latin. A stemmatic/comparative pass aligning Hs 1's six lines token-by-token against Hs 12's seven Latin words and Hs 3/3a/11's initial-letter runs is the obvious next cheap test on this target and is a stronger lead than anything in the spec's current `cheap_tests_in_order` -- **not attempted here, out of this brief's scope (locate and report, not solve).**

Herzog's footnote apparatus also flags a second inscription elsewhere in Hs 1 itself: "Vgl. fol. 27[a]" (compare fol. 27a) -- Hs 1's own folio 27 (near the end of its illustrated cycle, fol. 9'-27 per the 1928 article) apparently carries a comparable inscription of its own, not transcribed in the excerpt read this pass (would be near the end of the pp. 27-50 range, not reached this pass). This may be relevant to the RULED-OUT opening-27 candidate image bUNT3 flagged (`hs2398_f52v-53r_candidate.jpg`, two allegorical figures with tablets) -- not checked this pass; a future pass reading Herzog pp. 45-50 against that image would resolve it.

### Part 2: leaf identified in the Salzburg Museum's own digitisation

bUNT3's earlier candidate (opening 27, `hs2398_f52v-53r_candidate.jpg`) is **ruled out**: it shows two crowned/allegorical figures each holding a tablet, which does not match Herzog's Bild 2 (a single figure, a small chapel, pine trees, a rock face with a cave/arch) or the arch-framed rock-tablet layout of the inscription itself.

Extracted all 28 media ids in display order from the detail page's embedded HTML (`sammlung-online.salzburgmuseum.at/detail/collection/0a5aec0c-2c55-4eab-addc-a2c08e4b6f93`), confirming opening 1 = media `1b269afd...` (title page, matches bUNT3) and opening 27 = media `e0f9d823...` (matches bUNT3's candidate, now ruled out). Per Herzog's own foliation (Bild 2 at fol. 10, right after the illustrated cycle begins at fol. 9'), sampled the five openings bUNT3 had NOT sampled that fall in that early range (openings 8-12, 600px thumbnails):
- Opening 8, 9: plain narrative text, no illustration.
- **Opening 10** (media `56503bb8-1dd3-4aa7-84ed-cf300e4e0612`): left page = title + Bild 1 (five standing figures, matching Herzog's "mein Herr der Stattschreiber, Herr Martin... der Herr Pfleger und sonst auch ein Burger"); right page = **Bild 2** (single figure, small red-roofed chapel, pine trees, rock face with a dark cave/arch entrance) -- this is Herzog's fol. 10 recto, the page immediately before the inscription. Not committed (not the inscription leaf itself; easily refetchable, see manifest.json).
- **Opening 11** (media `dc46a099-dee5-42d5-857c-bd97c80315ab`): **CONFIRMED MATCH.** Left page: the six-line inscription painted as text inside an arch-topped frame on a red rock tablet -- visually matching Herzog's footnote ("the inscription is framed above by an arch") -- with a standing figure copying it and a seated armed figure watching. Right page: narrative prose that reads almost word-for-word against Herzog's printed fol. 11 text ("Und wie ich solang geschaut und abgeschriben hab, in dem ist es Abend worden..."). Pencil pagination visible: "20" (left/verso) and "21" (right/recto) -- consistent with Herzog's own "fol. 10'" (verso, page 20) / "fol. 11" (recto, page 21) foliation of this exact leaf (page = 2x folio for verso, 2x+1 for recto).

Fetched at native resolution (4884x3052, IIIF `info.json` max) to `ciphers/untersberg-code/images/hs2398_opening11_inscription_leaf.jpg` (2.97 MB); manifest.json updated with both the confirmed leaf and the ruled-out candidate, plus a note on the three unsampled-but-relevant openings. Folder now 3.1 MB, well under the 30 MB cap. **Not transcribed** (per brief: "do not transcribe -- a later blind pass will"); the hand-painted inscription visibly differs in some letters from both Schmeh's and Herzog's typeset transcriptions (expected -- three independent renderings of the same abbreviation-heavy original), which is exactly the kind of disagreement a dedicated transcription pass should settle from the image, not from a worker's aside.

### Requests per host, this pass

archive.org (advancedsearch, metadata x2, download djvu.txt x2, djvu.xml x1) -- 6, >=1.6s apart, all HTTP 200 (one earlier IIIF region-crop attempt at `iiif.archive.org` timed out twice at HTTP 504 and was abandoned per the one-retry rule, not counted as a host block, no data lost since the full-page fetch below succeeded).
iiif.archive.org (manifest.json, info.json, one full-page fetch at cached size 1755px after the region-crop 504s) -- 3, >=2s apart, HTTP 200 (plus the 2 timed-out 504 attempts noted above).
sammlung-online.salzburgmuseum.at (detail-page HTML refetch x1, info.json x1, 5 opening thumbnails at 600px, 1 native-resolution leaf fetch) -- 8, >=2s apart, all HTTP 200.
No other hosts touched this pass (HathiTrust, Google Books, OpenAlex, manuscripta.at, Europeana not queried -- see Part 1 note on why routes 2-4 were skipped).

### Status

No tokens read (H/C/S/M/I all 0) -- this remains a source-location, not a decipherment; status stays `open`. This is control-backed-positive-signal-plus-primary-source territory, still `partial`/`open` per rule 5's near-solve amendment, not `solved`. Per rule 10, nothing here is called new, unpublished, unread, first or previously unknown -- Herzog's own 1929 print already reproduces the inscription and Schmeh's 2018 blog post already reproduces a transcription of it; this pass only locates and cross-checks sources that already existed in print, and surfaces Herzog's comparative-witness apparatus as unexploited material. No REQUEST.md/ASKS.md row: nothing here is blocked on the owner (both hosts answered a plain curl with no login).

**Flag for the orchestrator / next worker:** the strongest next cheap test on this target is now a comparative alignment of Hs 1's six-line inscription against Herzog's apparatus for Hs 3/3a/11 (initial-letter runs) and Hs 12/13 (mostly-plain Latin) -- this is philology/collation, not cryptanalysis proper, and might resolve the target (or substantially narrow it) without a substitution anneal at all. Also worth a look: Herzog's "Vgl. fol. 27" cross-reference to a second inscription later in Hs 1 itself (near pp. 45-50, not read this pass), which may be the RULED-OUT opening-27 candidate image already on disk.

## Philological collation against Herzog's other witnesses, with a shuffle control (25 Sept 2026, LANE B4 worker bUNT5)

Per brief `.claude/briefs/runs/2026-09-25-lane-b4-untersberg-collate.md` and NEAR.md's named next step after bUNT4. Intake gate re-run: `python3 tools/intake_gate_check.py untersberg-code` exit 0 (`open`, edition/page citation within 6 lines). This is collation of Herzog's own 1929 printed apparatus (his material, credited below), not an anneal; per rule 10 nothing here is new, unpublished or first.

### 1. Witnesses transcribed and cross-checked against the page image

`specs/cheap-tests/untersberg-code/witnesses.tsv` transcribes Herzog pp.28-29's apparatus for Hs 1 (the target) and all eleven collated witnesses (Hs 2, 3, 3a, 4, 7, 11, 12, 13; the remaining Hss. print no inscription at all, "In den übrigen Hss. fehlen Inschriften"). Source: `sources/herzog-1929/herzog1929_full_djvu.txt` (OCR), each token checked by eye against `sources/herzog-1929/herzog1929_pp28-29.jpg` (rule 2, image over transcription -- did not trust the OCR alone). Six OCR errors were caught and corrected this way: Hs1 line 1 OCR "fr. fr." is actually a crossed-d suspension glyph printed twice (Herzog's own footnote calls this a letter-form variant his diplomatic transcription does not normalise); Hs1 line 2 OCR "5. 1. d." should read "5. l. d." (digit-1/letter-l confusion); Hs7 OCR "eni"/"fra"/"nnlantz"/"exem" should read "cui"/"fru"/"unlantz"/"excm"; Hs13 OCR "Farnes" should read "Fames". Also newly noted: Hs1 line 6's final letter "g" carries Herzog's own footnote marker "d)" as a superscript (the same footnote that states his transcription is diplomatic and notes the arch frame) -- this is an apparatus reference, not a 12th ciphertext letter, and is flagged as such in the TSV rather than silently folded into the token.

Tokenization follows LANE B4 bUNT2's existing convention for this target (period- and space-delimited elementary tokens): 71 tokens total, 61 letter-tokens plus 10 digit-tokens, matching bUNT2's count exactly (cross-check that the two passes are reading the same material the same way).

### 2. Alignment: Hs 1's six lines against Hs 12's six spelled-out words, with a shuffle control

Hs 12 gives the inscription fully spelled out as six words -- "Bellum. Famus. Gestas. Res. Mores. Amicus." -- plus a seventh, "Orpheus.", printed on its own centered sub-line below the list (read as a coda or name, not a 7th line of the six-line set; excluded from the aligned six). Six words against Hs 1's six lines is a plausible 1:1 line correspondence, so `specs/cheap-tests/untersberg-code/align_witnesses.py` tests it directly: for each line i (1-6) and each candidate word order, does ANY of line i's letter-tokens (digits and the two footnote-flagged "eth" abbreviation-glyph tokens excluded, per rule 2 -- not a Latin letter) share its initial letter with the word placed at position i?

**Real order (Bellum, Famus, Gestas, Res, Mores, Amicus): 3/6 lines match** (Famus/f matches line 2's token "f"; Res/r matches line 4's token "r"; Mores/m matches line 5's token "mvraco"). Lines 1 (Bellum/B), 3 (Gestas/G) and 6 (Amicus/A) have no token of the matching initial.

**Control, per rule 3: the identical procedure run on 10 random shuffles of the same six words (seed 20260925): mean 2.10/6, range [1, 3] -- 3 of the 10 shuffles also reach 3/6, tying the real order.** A bonus exact check (not asked for by the brief, cheap to add: all 6! = 720 permutations of the six words) puts the real order's 3/6 at the **42.5th percentile** of the full permutation distribution (306/720 permutations tie or beat it; exact mean 2.333/6, range [0, 5]).

**Verdict: this specific alignment test does not clear its own control.** 3/6 is only slightly above the 10-shuffle sample mean and is tied or beaten by close to half of all possible word orders -- indistinguishable from chance under an exact permutation test. Per rule 3 (a match means nothing without a control showing it beats chance), this alignment method does not license treating any of the three apparent matches (Famus/line 2, Res/line 4, Mores/line 5) as more than coincidence. It is a negative result for this particular method, not a positive one, and it is reported as such rather than as a partial win: rule 3's own header paragraph applies (a control below its own gate cannot license a reading), even though here the "control" is a permutation test rather than a synthetic-text draw.

### 3. Proposed expansion, grade by grade (rule 4)

Given part 2's result, **0 tokens are graded C** -- no aligned position between Hs 1 and a spelled-out sibling witness is licensed with the confidence rule 4's C grade requires ("from known plaintext of a sibling witness"), because the control shows the alignment supporting any such claim is not distinguishable from chance. No tokens are graded M either, for the same reason (M implies a real but weak signal; this alignment method produced no signal beyond noise). The six-word literal sequence from Hs 12, in its own printed order, is recorded as a single **grade-I** (inferred, weak, explicitly not control-backed) line-level hypothesis only -- `specs/cheap-tests/untersberg-code/proposed_expansion.txt` -- offered as a hypothesis for a future pass to test differently (e.g. folding in token length/count, or aligning against Hs 13 and the Hs 3/3a/11 initial-letter runs together instead of Hs 12 alone), not as a reading.

Counts: **C: 0, M: 0, I: 1 (line-level, all six lines, not control-backed), H: 0** (unchanged from every prior pass on this target).

`python3 tools/judge_plaintext.py specs/untersberg-code.json --file specs/cheap-tests/untersberg-code/proposed_expansion.txt`:
```
FAIL length: got=31, min=90, max=130
FAIL language: score=-1.59, null_p99=-1.495, real_p05=-0.539, real_median=-0.438, mode=both, N=31
FAIL - untersberg-code (a PASS is a gate for a verifier, not a reading; rule 10)
```
Both FAILs are expected and not meaningful: the judge's wired language is `de` (German; the spec's own note already flags that `la`/Latin has no corpus in `tools/judge_plaintext.py`) and the candidate is a 6-word Latin string, far short of the spec's letter-count window sized for the full six-line inscription. This FAIL is reported per rule 7 as instructed, not as a finding.

### Status

No tokens read at grade H, C, S or M (rule 4: I: 1 line-level hypothesis only, not control-backed). Status stays `open`/`partial` (rule 5's near-solve amendment; NEAR.md is the orchestrator's file and is not touched by this worker). Per rule 10, nothing here is new, unpublished, first or previously unknown -- this collates Herzog's own 1929 printed apparatus, credited above and in `specs/cheap-tests/untersberg-code/witnesses.tsv`'s header.

**Flag for the orchestrator / next worker:** the initial-letter-only, Hs12-alone alignment tested here does not beat its own permutation control (42.5th percentile of 720). Two untried variants that might do better, if this line is pursued further: (a) fold in token length and count (the brief's other stated cues), not just initial letters; (b) align against Hs 13 (mostly-legible Latin, more words to anchor on) and the Hs 3/3a/11 initial-letter runs together with Hs 12, rather than Hs 12 alone, since Herzog's apparatus frames all of them as copies of the same underlying text and a joint alignment has more constraints per line than any single witness does alone. Neither attempted this pass (brief scope: one alignment, one control).

### Files this pass

`specs/cheap-tests/untersberg-code/witnesses.tsv` (all 12 witnesses' tokens, OCR-vs-image corrections noted), `align_witnesses.py` + `align_output.txt` (the alignment and its control), `proposed_expansion.txt` (the grade-I hypothesis). No new host requests (disk-only, per brief).

## Joint alignment against Hs 13/3/3a/11, with shuffle control (26 Sept 2026, LANE B5 worker bUNT6)

Per job brief `.claude/briefs/runs/2026-09-26-lane-b5-untersberg-joint.md`, NEAR step (3b) named after bUNT5. Intake gate re-run: `python3 tools/intake_gate_check.py untersberg-code` exit 0 (`open`, edition/page citation within 6 lines).

bUNT5 tested Hs 1's six lines against Hs 12's six spelled-out words at line granularity (a clean 1:1 correspondence) and found the alignment indistinguishable from chance (42.5th percentile of 720 permutations). This step extends the test to the four remaining witnesses Herzog's apparatus gives (Hs 13 -- mostly plain Latin, 19 tokens; Hs 3, Hs 3a, Hs 11 -- 11-letter initial runs each), which have no such line correspondence to Hs 1 (Herzog's apparatus lineation reflects his own page layout for each witness, not Hs 1's six physical lines), so `specs/cheap-tests/untersberg-code/align_joint.py` drops the line boundary and works on Hs 1's flat, ordered 61-token letter sequence instead: for each witness, a sliding best-offset search scores initial-letter matches (case-insensitive; the two "eth" suspension-glyph tokens excluded from matching, per bUNT5's own convention) and flags any witness token that strictly extends (case-insensitive prefix of) its aligned Hs 1 token as a candidate expansion (the Hs 12 "Bellum/Famus" pattern, now checked against Hs 13's spelled words too). The joint target score is the sum of the four witnesses' best-offset match counts, out of 19+11+11+11=52 possible.

**Target: 11/52 joint matches** (Hs13 2/19 at offset 7; Hs3 3/11, Hs3a 3/11, Hs11 3/11, all at offset 5) = 0.212.

**Control, per rule 3: the identical four-witness best-offset joint procedure re-run on 500 random shuffles of Hs 1's 61-token order (seed 20260925): mean 10.868/52 (0.209), range [8, 17].** The real score sits at the **70th percentile**, and 59.6% of shuffles (298/500) tie or beat it.

**Verdict: this joint alignment also does not clear its own control** -- 11/52 is barely above the shuffle mean and well within the bulk of the control distribution, indistinguishable from chance, confirming bUNT5's single-witness result now across all four remaining witnesses at once. Two expansion candidates turned up at Hs 13's best-scoring offset (Hs1 token "P" could be extended by Hs13's "peseit"; Hs1 token "m" by Hs13's "Moesque"), but that offset (2/19 matches) is itself below even the joint control mean, so per rule 4 ("a token pair counts toward a grade only at C ... or M") neither is graded -- **0 tokens graded C or M from this test**, matching bUNT5. This closes the philological-collation line opened by bUNT4/bUNT5 for this target: none of Herzog's collated witnesses -- singly (Hs 12) or jointly (Hs 13/3/3a/11) -- align with Hs 1 above chance under an initial-letter test. Status stays `open`/`partial` (NEAR.md is the orchestrator's file, not edited here).

Counts (rule 4, unchanged from bUNT5): C: 0, M: 0, I: 1 (bUNT5's line-level hypothesis, not control-backed), H: 0.

### Files this pass (3b)

`specs/cheap-tests/untersberg-code/align_joint.py`, `align_joint_output.txt`. No new host requests (disk-only, per brief). Credit: Herzog 1929's own printed apparatus (as transcribed by bUNT5 into `witnesses.tsv`), this script only re-derives a control statistic from it.

## Blind transcription of the confirmed leaf vs Herzog's print (26 Sept 2026, LANE B5 worker bUNT6)

Per job brief `.claude/briefs/runs/2026-09-26-lane-b5-untersberg-joint.md`, NEAR step (2b), run since (3b) used well under 40% of its $1.5/45-min share. The leaf image was already on disk (`ciphers/untersberg-code/images/hs2398_opening11_inscription_leaf.jpg`, fetched by bUNT4, confirmed match to Herzog's Bild 2), so no new host fetch was needed.

**Blindness**: the orchestrating worker (this session) has already read Herzog's transcription, `witnesses.tsv` and this NOTES.md in full, so it cannot itself do a blind pass. A fresh Sonnet subagent was spawned with only the image path and instructions to transcribe the six-line boxed inscription (upper-left of the left page); it had no access to this file, the spec, or any other prior transcription of the target -- true blindness, preserved by giving it a clean context. Its raw output is `specs/cheap-tests/untersberg-code/blind_pass.tsv`.

**Diff, per rule 3 (PX-BRODEC lesson, 25 Sept 2026):** the blind pass tokenizes differently from Herzog's period-delimited print -- it often fuses letter-groups Herzog's print separates with a period (e.g. blind line 2 reads "ak5" where Herzog's print gives three separate tokens "a. f. 5."), since periods were not always clearly legible to it as segmentation marks in the handwriting. Comparing token-position to token-position under these two different conventions would measure notation, not agreement, so `specs/cheap-tests/untersberg-code/diff_blind_pass.py` normalizes both sides to one convention per line first -- a single lowercase, period/space-stripped character string -- then diffs with `difflib`'s character-level `SequenceMatcher`.

**Result: 75/109 matched characters across the six lines = 0.688 overall** (per line: L1 0.750, L2 0.786, L3 0.562, L4 0.622, L5 0.808, L6 0.651; `diff_blind_pass_output.txt`).

**Distinctive-token cross-check: 4/4 agree.** Four rare, hard-to-confuse strings were independently read the same way by both passes: line 1's "occo" (both), the line 4/5 boundary word "missm"/"missu" (both give the same m-i-s-s-*-boundary reading), line 5's "mvraco"/"vraco" (both), and line 6's "pymi"/"prmi" (both). This is strong evidence the blind pass is reading the same inscription and largely the same letters as Herzog's 1929 print, not a different or garbled source -- a useful sanity check given three independent renderings of this inscription now exist (Schmeh's, Herzog's, and this pass's).

**Reading this result**: 68.8% character agreement on a hand-painted, heavily abbreviated 17th/18th-century inscription against a 1929 typeset diplomatic edition is consistent with genuine paleographic difficulty, not a failed transcription. The subagent itself flagged several concretely ambiguous glyphs worth a future close look: a repeated loop-glyph at line 1 tokens 2-3 it read as "g" (Herzog's own print independently marks an unusual crossed-d suspension form -- "eth" in witnesses.tsv -- at exactly those two positions, i.e. both passes independently flag the same spot as anomalous, even though they read it differently); an "H"-like two-stroke-plus-crossbar glyph recurring twice in line 4 (tokens 5 and 11); and a figure-8-shaped final character in line 2. The weakest line (L3, 0.562) is dominated by short single-letter tokens where segmentation disagreement, not necessarily misreading, drives most of the character mismatch.

**Not graded.** No tokens are graded H, C or S (rule 4: no key, no known plaintext for this target -- this is a transcription QA pass, not a decipherment). Two notable candidate readings the blind pass gave with its own stated confidence -- line 6's "loqui" and "vult" (ordinary Latin, "to speak" and "wills/wants"), where Herzog's print gives less legible single letters at the corresponding positions -- are **not** graded M here: rule 4's M grade still wants some real, ideally corroborated signal, and a single blind pass reading two words that happen to be plausible Latin, with no control and no second independent pass, is not that. Flagged as a lead: a future pass should look specifically at that spot on the image (line 6, roughly a third of the way in) to check whether "loqui"/"vult" hold up, ideally with a second independent blind pass to reconcile against (per the common brief's reconciliation convention) before any grade is assigned.

Counts (rule 4, unchanged): C: 0, M: 0, I: 1 (bUNT5's line-level hypothesis, not control-backed), H: 0.

### Status

Both (3b) and (2b) are now run. The philological-collation line (bUNT4's flagged next step) is closed: none of Herzog's five collated witnesses -- singly (Hs 12, bUNT5) or jointly (Hs 13/3/3a/11, this pass's 3b) -- align with Hs 1 above chance. The transcription cross-check (2b) confirms the target is being read consistently across three independent renderings (Schmeh, Herzog, this pass) but adds no reading. Status stays `open`/`partial` (rule 5's near-solve amendment; NEAR.md is the orchestrator's file, not edited here).

**NEAR-ready sentence for the orchestrator:** untersberg-code remains `partial` -- the abbreviation-shaped structure is control-backed (test 1, 100th percentile) and the source/leaf/comparanda are now fully identified and cross-checked, but no alignment against Herzog's collated witnesses (single or joint) beats chance, and no expander or blind-transcription pass has produced a control-backed reading. The next named step is either (a) a second independent blind pass of the same leaf reconciled against this one (to settle the line 6 "loqui"/"vult" candidate and the other low-confidence glyphs before grading anything), or (b) building a real period Latin/German abbreviation-convention corpus (Cappelli/Grun word list) to replace the weak de16 stand-in the NEAR-step-1 expander used -- neither attempted this pass (out of budget/scope).

### Files this pass (2b)

`specs/cheap-tests/untersberg-code/blind_pass.tsv` (subagent's raw output), `diff_blind_pass.py`, `diff_blind_pass_output.txt`. No new host requests (image already on disk). One Sonnet subagent (image transcription only).

## Reconciliation and symA (26 Sept 2026, LANE B6 worker bUNT8)

Per job brief `.claude/briefs/runs/2026-09-26-lane-b6-unt8.md`, step (4b), reconciling bUNT7's second blind pass (`pass_b7.tsv`) with bUNT6's `blind_pass.tsv`. Intake gate re-run: `python3 tools/intake_gate_check.py untersberg-code` exit 0 (`open`, edition/page citation within 6 lines).

**Reconciliation.** `reformat_for_reconcile.py` renamed both TSVs' headers to the `line/pos/sign/conf/note` schema `tools/reconcile_passes.py` requires, then `tools/reconcile_passes.py blind_pass_reformat.tsv pass_b7_reformat.tsv --out-dir ciphers/untersberg-code` aligned the two passes per line (Needleman-Wunsch): 6 lines, 49 signs (bUNT6) vs 48 (bUNT7), 32/49 aligned columns agree (65.3%), 17 disagreement columns -> `disagreements.tsv`.

**Settling on the image.** All 17 rows were checked against native-resolution crops of `images/hs2398_opening11_inscription_leaf.jpg` (Pillow installed this session; none was on disk, none pre-existing). 13 of 17 settled with reasonable confidence; 4 stayed genuinely uncertain (M grade, both candidates kept in `disagreements.tsv`'s `settled` column with an `alt`). Corrections went both ways -- bUNT7 was right more often, but bUNT6 was right on two real tokens bUNT7's tokenizer had dropped or misread (line3's "g" between "5" and "o", which bUNT7's alignment had silently skipped, and line4's "ll", which bUNT7 read as a rounded "u"). Full per-row basis in `disagreements.tsv`; `reconciled.tsv` is the full settled 6-line text (pass_b7's tokenization as the base, with these corrections applied).

**symA.** The recurring ligature bUNT7 flagged (hook at top-left, a vertical stroke with a top serif, a small loop where the two join, and a long descender tail below the baseline) is confirmed by direct image comparison at all 5 of the positions bUNT7 named: line2 token1's final glyph, line4 tokens 5 and 7, and line6 token2's first glyph and token3's glyph (`line2_symA.jpg`, `line4_glyph7.jpg`, `line6_w2.jpg`, `line6_w3.jpg`, and the three-way comparison `compare_glyphs2.jpg` that checks line4 token5 against both line4 token7's confirmed symA and line4 token11's confirmed plain "H" -- token5 matches symA's construction, not H's crossed double-stroke, differing from token7 only in a shorter descender). A sixth, mirrored instance ("symA-rev", the same construction flipped left-right) sits immediately next to a plain symA at line6 token2. Two of bUNT6's blind-pass readings at symA positions were very likely content-biased misreadings: line6 token3's "loqui" (plausible Latin "to speak") reads the symA ligature as "q"; line2 token1's "...rop" reads it as a plain "p". Neither "q" nor "p" is graded here (rule 4 -- no key, no known plaintext); symA stays an unidentified recurring mark.

**Cappelli check (candidates qu/que/-rum/-us/-orum/con).** `be-api.us.archive.org/fts/v1/search` full-text search inside `lexiconabbreviat29capp` (Cappelli, *Lexicon abbreviaturarum*, 1929 ed., archive.org identifier `lexiconabbreviat29capp`) against its own general-signs section (p.634, "Segni abbreviativi generali"): the printed descriptions there are (1) a comma/"9"-shaped sign, from the Tironian notes, meaning *con* or *cum*; (2) a sign over certain consonants meaning *er*; (3) a sign at word-end meaning *ur* or *fur*; (4) "gamba tagliato in gamba da una linea trasversale" (a downstroke leg cut by a transversal line) meaning *rum*, e.g. "ypothec[abbr] = ypotecarum". None of these matches symA's actual construction: symA has a hook-loop top and a curved bottom join, not a plain comma, and its descender is a plain curving stroke with no crossbar (ruling out the *-rum* mark specifically, which is defined by the crossbar). No description matching *que*, *-us* or *-orum* turned up in this section. **This check does not confirm any of the five candidates** -- symA remains visually closer to an unidentified or scribe-specific mark than to a standard Cappelli-catalogued Latin suspension. 6 requests to archive.org's be-api host (advancedsearch.php x1, fts/v1/search x5), well under the 15-request cap, >=1.5s apart, descriptive User-Agent.

**Line 6, what the image and the table support.** The image supports: symA appears twice on this line (token2's first glyph, token3), the second glyph at token2 is the same shape mirrored, and neither position is a plain letter (not "p", "r" or "q"). The Cappelli check does not support reading symA as *que* or any other tested Latin suspension there or elsewhere -- so "loqui" is not restored under a different theory; it is simply not what token3 reads. Token1 ("nicrlr"/"ueicrlr") and token4 ("vmult"/"vult") stay M-graded, unresolved by either the image at this resolution or the abbreviation check (neither involves symA).

**Reconciled-vs-Herzog agreement.** Only after `reconciled.tsv` was written and committed (this section's git history) did this worker open `diff_blind_pass.py`, which embeds Herzog's own 1929 print (`HERZOG_LINES`, from `witnesses.tsv`), to build the comparison script -- a bookkeeping slip against the brief's "do not read Herzog's print until the reconciled text is committed" (the reconciliation and every settlement above were completed and decided from the image alone beforehand; nothing in `reconciled.tsv` was revised after this read). `specs/cheap-tests/untersberg-code/diff_reconciled_vs_herzog.py` reruns bUNT6's exact method (lowercase, period-stripped, character-level `difflib.SequenceMatcher` per line; symA/symA-rev/symB collapse to one placeholder character each, the same treatment Herzog's ETH glyph already gets) on `reconciled.tsv` against the same `HERZOG_LINES`.

**Result: 76/110 matched characters = 0.691 overall** (per line: L1 0.750, L2 0.690, L3 0.625, L4 0.622, L5 0.808, L6 0.698; `diff_reconciled_vs_herzog_output.txt`), **beside bUNT6's unreconciled 75/109 = 0.688.** Reconciliation and image-settlement moved the figure by +0.3 points -- essentially flat, not a meaningful gain. This is not a control-backed statistic (no shuffle-null run against it; rule 3 would want one before treating either number as more than descriptive), and it is not evidence the reconciled text is more "correct" than the raw blind pass -- both are transcriptions of the same six lines checked against the same 1929 print, and disagreement can reflect either side's error, abbreviation-convention mismatch (the same PX-BRODEC risk bUNT6 already flagged, unaddressed here since Herzog's print was read only at the very end), or genuine paleographic difficulty.

Counts (rule 4, unchanged): C: 0, M: 4 (line2 tok5 d/h, line6 tok1 n/u-initial, line6 tok4 vult/vmult minim count, plus symB left unresolved), H: 0 (no key, no known plaintext -- nothing here is cryptanalytic or key-sourced), I: 1 (bUNT5's line-level hypothesis, unchanged, not control-backed). Status stays `open`/`partial` (rule 5's near-solve amendment; NEAR.md is the orchestrator's file, not edited here).

### Files this pass (4b)

`reconciled.tsv`, `disagreements.tsv` (reconcile_passes.py output plus a `settled`/`grade`/`basis` column this worker added), `ciphertext_draft.tsv`, `agreement.tsv` (reconcile_passes.py outputs); `specs/cheap-tests/untersberg-code/{blind_pass_reformat.tsv,pass_b7_reformat.tsv,diff_reconciled_vs_herzog.py,diff_reconciled_vs_herzog_output.txt}`. Crops used to settle disagreements were written to this session's scratchpad, not committed (not named in the brief's output list; the basis column in `disagreements.tsv` records what each crop showed). Hosts: archive.org be-api 6 requests (Cappelli check only). No subagents.

## symA against the witnesses (26 Sept 2026, LANE B7 worker bUNT9)

Per job brief `.claude/briefs/runs/2026-09-26-lane-b7-unt9.md`. Intake gate re-run: `python3 tools/intake_gate_check.py untersberg-code` exit 0 (`open`). This aligns the 5 confirmed symA positions (bUNT8's list: line2 tok1's final glyph, line4 tok5, line4 tok7, line6 tok2's first glyph, line6 tok3) against every witness in `witnesses.tsv`, reusing bUNT5/bUNT6's own token-initial / best-offset alignment machinery (`align_witnesses.py`'s Hs12 line mapping, `align_joint.py`'s Hs13/Hs3/Hs3a/Hs11 best offsets, recomputed identically here) rather than inventing a new method. Hs7 (Herzog's other long abbreviation witness, never tested against Hs1 before this job) gets the same best-offset treatment for the first time: best offset=4, 6/53 initial-letter matches, no better than the joint line's chance-level results. Hs2 ("N. N." only) and Hs4 (blank, "in 4 ist etwas Raum freigelassen") have no text reaching any of the 6 lines.

**Locating the flat index.** Line4's two symA tokens are themselves whole, standalone Hs1 tokens in Herzog's own print (index 25 = his "v", index 27 = his "p" -- i.e. Herzog silently normalized both symA occurrences to ordinary letters), so alignment there is genuine token-for-token. Line2 and line6 are messier: reconciled.tsv fuses several of Herzog's period-delimited tokens into one word, so symA sits at a sub-token offset (the *final* letter of Herzog's fused "Satrnrop" in line2; inside/at "pymi" and the standalone "p" in line6) -- found by running `diff_reconciled_vs_herzog.py`'s own character-level `SequenceMatcher` on lines 2/4/6 and reading which Herzog raw token each symA placeholder character's aligned block falls into (confirmed line4's two positions land exactly on symA's own opcode boundaries, cross-checking the by-hand derivation).

**Table (witness -> reading at the symA flat index; `None` = position falls outside that witness's aligned window, i.e. no anchor):**

| position | Herzog's own print | Hs13 | Hs3 | Hs3a | Hs11 | Hs7 | Hs12 (line, uncontrolled) |
|---|---|---|---|---|---|---|---|
| line2 tok1 final glyph | "Satrnrop" (symA read as final "p") | no anchor (window starts at idx7) | "S" | "S" | "S" | "et" | "Famus" |
| line4 tok5 | "v" | "h" | no anchor | no anchor | no anchor | "s" | "Res" |
| line4 tok7 | "p" | no anchor (window ends at idx25) | no anchor | no anchor | no anchor | "vuls" | "Res" |
| line6 tok2 glyph1 | "pymi" (leading p) | no anchor | no anchor | no anchor | no anchor | "K" | "Amicus" |
| line6 tok3 | "p" (standalone) | no anchor | no anchor | no anchor | no anchor | "excm" | "Amicus" |

Hs3/Hs3a/Hs11's "S" at line2 is a granularity artefact, flagged rather than counted at face value: their aligned token there is the single letter "S", which only reaches Herzog's fused token's *first* letter (matching the already-known "Sal..." opening), not its *last* letter where symA actually sits -- a control that cannot vary on the axis being measured licenses nothing (rule 3's bCAS/AX-5799 lesson, same shape here: the witness word is too short to say anything about the position asked). Every other cell is a single witness or no witness at all -- never two witnesses independently agreeing on the same value at the same symA position.

**Control, per rule 3 and the brief's step 3:** 200 draws of 5 random positions (seed 20260926) from the 54 Hs1 flat positions that are read and are not one of the 5 symA slots (61 total - 2 ETH suspension-glyph slots - 5 symA), same witness-lookup and >=2-witness-initial-letter-agreement procedure. Control: mean 1.070/5, 95th pct 3/5, range [0,5]. symA's own count under the identical (uncaveated) method: **1/5** (only the granularity-artefact line2 "S" match) -- at/below the control mean, 144/200 draws (72.0%) tie or beat it, nowhere near the 95th-pct gate. With the granularity caveat applied (excluding the artefact), symA's real count is **0/5**.

**Verdict (brief step 4):** no value stands at even 1 of 5 symA positions across >=2 witnesses on a fair reading, let alone >=4/5, and the naive count does not beat the control's 95th pct either way -- **symA stays grade I** (inferred, unidentified), not S. No update to the line 6 Herzog-agreement figure (nothing here licenses one). This closes the "align symA against the witnesses" step of NEAR.md's named next step for this target with a control-backed negative, consistent with bUNT5/bUNT7's prior finding that no Herzog witness (singly or jointly) aligns with Hs1 above chance -- now confirmed at the specific symA positions too, including Hs7 which had not been tested before.

Counts (rule 4, unchanged from bUNT8): C: 0, M: 4, H: 0, I: 1 (bUNT5's line-level hypothesis; symA remains ungraded, not I -- corrected: symA is reported here as "no signal", not assigned a grade, since rule 4's I still implies some inference and none is licensed). Status stays `open`/`partial` (rule 5's near-solve amendment; NEAR.md is the orchestrator's file, not edited here).

### Files this pass (bUNT9)

`specs/cheap-tests/untersberg-code/align_symA_witnesses.py`, `specs/cheap-tests/untersberg-code/align_symA_witnesses_output.txt`. No new host requests (disk-only, all witness data already in `witnesses.tsv`). No subagents.

SO lead prompt, 26 Sept 2026, QUEUE-FILL.

## UNT-LANG (27 Sept 2026)

Per job brief `.claude/briefs/runs/2026-09-27-parent-ytbiz-unt-lang.md`: read the second-opinion lead item [6] (`second-opinions/chatgpt-leads-2026-09-27.md`, PR-LAND-12) -- Johannes Lang, "Das Erbe der 'Lazarusgeschichte'. Zur Entstehung und Instrumentalisierung der Untersbergsage," *Mitteilungen der Gesellschaft für Salzburger Landeskunde* 150 (2010), pp. 125-178, PDF at `https://www.zobodat.at/pdf/MGSL_150_0125-0178.pdf`.

**Fetch attempt, blocked.** Reachability test (`curl -sS -o /dev/null -w "%{http_code}"`) on the plain URL returned a proxy-side connection reset (`ws_closed_mid_exchange`) on the first try. One retry, per the good-citizen rule, with a browser User-Agent (`Mozilla/5.0`): HTTP 200, but `Content-Type: text/html`, not a PDF, with `Set-Cookie: techaro.lol-anubis-auth=...` / `techaro.lol-anubis-cookie-verification=...` and body title "Making sure you're not a bot!" -- this is the same Anubis JS proof-of-work bot-challenge the access playbook already documents for `bibliotecadigital.rah.es` (CLAUDE.md, Access playbook item 1), now confirmed for zobodat.at too. Per this job's brief ("on a 403 or challenge stop and say so") and the good-citizen rule (one retry after a pause is the limit), stopped here rather than trying the headless-Chromium fallback the playbook documents for that same challenge (`tools/browser_fetch.js --binary`), which this brief's USD 3 cap and 30-minute box were not sized for. Requests to zobodat.at: 2 (one proxy-reset, one 200-with-challenge), >=3s apart.

**Both of the brief's questions are therefore unanswered, not "no":** whether Lang's appendix names a Reichenhall manuscript outside Herzog's twelve, and whether Lang prints, cites or discusses the six-line HS 2398 text, are untested (not a search result under rule 10 -- the source was never read). If a future pass wants this PDF, the next route to try is `tools/browser_fetch.js --binary` against the same URL (the rah.es precedent shows Anubis clears intermittently for a real headless browser, not for curl), or the Wayback Machine CDX API for a cached copy, neither attempted here (out of this brief's scope and cap).

No decode, no other host touched, no credentials, no AskUserQuestion, no solved/new/first/unpublished wording.

## Second-opinion leads (SO-UNTERSBERG-LEADS, 27 Sept 2026)

Landed from PR 34 (`second-opinions/chatgpt-leads-2026-09-27.md`, OpenAI GPT-5/Codex, PR-LAND-12). Leads, not verdicts; every citation below is a claim to verify, never a fact -- unchecked.

- reference-dictionary; Cappelli, _Lexicon abbreviaturarum_ (2nd German ed., 1928), pp. V-VIII, 1-6, archive.org/details/LexiconAbbreviaturarum; unchecked.
- reference-dictionary; Walther, _Lexicon diplomaticum_ (Ulm, 1756), relevant plate/column unverified, books.google.com/books?id=ZItMzqEqxPAC; unchecked.
- reference-dictionary; Grun, _Schlüssel zu alten und neuen Abkürzungen_ (1966), bibliographic lead only, edition/page unverified; unchecked.
- scholarship; Weber-Fleischer, "Die Überlieferung von den Herrschern im Berg," in _Sagenhafter Untersberg_ (Salzburg, 1992), pp. 17-170, a manuscript census/stemma that may hold an HS 2398 edition and sigla absent from Herzog; unchecked.
- scholarship; Kammerhofer-Aggermann, "Ikonologische Marginalien," same volume (1992), pp. 219-266 esp. p. 222, on "Handschrift 1" imagery/codicology; unchecked.
- scholarship; Lang, "Das Erbe der 'Lazarusgeschichte'," _MGSL_ 150 (2010), pp. 125-178, zobodat.at/pdf/MGSL_150_0125-0178.pdf, a later source-critical account with an appendix; unchecked.
- scholarship; Dorninger, "Mythische Endzeitvorstellungen" (year unverified), pp. 3-4, plus.ac.at/wp-content/uploads/2021/02/1157260.pdf, reports a 1623 print of the Lazarus narrative; unchecked.
- witness-print; Schöppner, _Sagenbuch der Bayerischen Lande_ vol. 1 (Munich, 1852), pp. 5-8, prints a shorter initials tradition "S.O.R.C.E.J.S.A.T.O.M."; unchecked.
- prior-claim; untersberg-news.at page prints the six-line HS 2398 text plus a separate initials sequence "S.V.R.C.E.T.S.A.T.V.S." expanded "Surget Satum," and says that phrase is not in the six-line text itself (author/date/pagination unverified) -- a lead for a sibling initials tradition, not symA; unchecked.
- prior-claim; Schmeh 2014 (scienceblogs.de) discusses a 1623 initials form "S.O.R.C.E.I.S.A.T.O.M.," article unpaginated, cited print not inspected; unchecked.
- prior-claim; untersberg.org/untersbergcode.html claims Yve Kupka "resolved" the code in 2015, no method, glyph table or page-level source found; unchecked.
- manuscript-witness; Lang reports a manuscript, apparently 18th-century, offered for sale to the City of Bad Reichenhall around 1990 (appendix cited, present location/accession status unverified); unchecked.
- contact; Weber-Fleischer, Kammerhofer-Aggermann, Lang and Dorninger named as scholars to approach on transmission, codicology, source history and prophecy-literature context respectively (current affiliation/contact details unverified); unchecked.
- methodology; build a same-scribe abbreviation concordance across all 28 IIIF leaves (ductus clustering, full-word contexts) before comparing symA against Cappelli/Walther again; unchecked.
- methodology; give an Early Modern German paleographer a blind crop packet of every symA occurrence (and visually similar marks) with no "loqui vult" hypothesis primed, sign classification before expansion; unchecked.

## UNT-LANG2 (27 Sept 2026)

Per job brief `.claude/briefs/runs/2026-09-27-parent-ytbiz-unt-lang2.md`, the named next step after UNT-LANG's block. Intake gate re-run: `python3 tools/intake_gate_check.py untersberg-code` -- open, edition/page citation within 6 lines.

**Route 1, real browser (up to 3 attempts): still blocked.** `NODE_PATH=$(npm root -g) node tools/browser_fetch.js "https://www.zobodat.at/pdf/MGSL_150_0125-0178.pdf" ... --binary` ran its own internal 3-attempt retry loop (the tool's own `--binary` flag); all 3 navigations returned `content-type=text/html; charset=utf-8, status=200` -- the same Anubis challenge page UNT-LANG found with curl, now confirmed for a real headless browser too, unlike the `bibliotecadigital.rah.es` precedent CLAUDE.md documents (where a real browser clears Anubis intermittently). zobodat.at requests this pass: 3 (the tool's internal retries), all within one `browser_fetch.js --binary` invocation.

**Route 2, Wayback CDX: also failed, transport-level, not a site refusal.** `https://web.archive.org/cdx/search/cdx?url=zobodat.at/pdf/MGSL_150_0125-0178.pdf&output=json` via plain curl failed twice (`ws_closed_mid_exchange`, a proxy-side connection reset, confirmed via `/__agentproxy/status`'s `recentRelayFailures` -- the same failure kind hit an unrelated host, `mtalk.google.com`, in the same window, so this is proxy/transport noise, not web.archive.org blocking us) -- one retry after a 3s pause per the good-citizen rule, same result both times. Tried a second route to the same CDX call through `tools/browser_fetch.js` (no `--binary`, plain page fetch): returned HTTP 200 but body `upstream request failed` (the stub CLAUDE.md's access playbook already documents for Wayback page fetches lacking the `if_` suffix -- "a bare fetch without it can return a stub 'upstream request failed'; retry once before concluding the capture is unreachable") -- retried once after a pause, same stub both times. Four attempts total across two tools/methods, all transport failures, no HTTP error or challenge page ever reached from web.archive.org's own server. web.archive.org requests this pass: 2 curl (both `ws_closed_mid_exchange`) + 2 browser_fetch.js (both `upstream request failed`), >=3s apart.

**Per the brief ("if both fail, stop and file a LOCAL-QUEUE.tsv row"): stopped and filed `LOCAL-QUEUE.tsv` row L26** for the owner's desk runner, naming both prior blockers, the two questions verbatim from UNT-LANG's brief, and "no" as a valid answer for either (rule 10).

**Both of UNT-LANG's questions remain unanswered, not "no":** whether Lang's appendix names a Reichenhall manuscript outside Herzog's twelve, and whether Lang prints, cites or discusses the six-line HS 2398 text, are still untested (not a search result under rule 10 -- the source has never been read by any route tried so far, cloud or otherwise). Sigla TSV: not built (source unread, 0 rows).

No decode, no other host touched, no credentials, no AskUserQuestion, no solved/new/first/unpublished wording. Status stays `open`/`partial` (rule 5's near-solve amendment; nothing here changes the target's evidentiary state, only its access-route exhaustion).

## While waiting (27 Sept 2026, WAIT-PASS-B)

Waits on: LOCAL-QUEUE.tsv row L26 (the owner's desk runner reading Lang 2010's zobodat.at PDF, Anubis-blocked
from the cloud by both curl and headless Chromium), filed 27 Sept 2026.

- S: check Cappelli's Lexicon abbreviaturarum (archive.org) and Walther's Lexicon diplomaticum (Google Books) against symA's shape -- SO-UNTERSBERG-LEADS reference-dictionary items. Done: Cappelli p.634 no match (bUNT8); Walther Tab. CCXX does not match (A2P4-UNT, 3 Oct 2026); Walther leaves 254 and 256-258 (Tab. CCXIX, CCXXI-CCXXIII) do not match either (D2B-UNT, 6 Oct 2026), so Walther's general-sign plates CCXIX-CCXXIII are covered.
- S: fetch Schöppner's Sagenbuch der Bayerischen Lande vol. 1 (1852) for its shorter initials tradition 'S.O.R.C.E.J.S.A.T.O.M.' to compare against symA -- witness-print lead. Done (A2P4-UNT, 3 Oct 2026): identical to Herzog Hs 3, no symA position reached.
- M: build the same-scribe abbreviation concordance across all 28 IIIF leaves (already on disk) before any further Cappelli/Walther comparison -- methodology lead, unchecked.

## Web and blog check (GF4-BATCH21 (account-4), 3 Oct 2026)

Plain web searches (WebSearch, 3 Oct 2026):
(1) `Untersberg Inschrift Geheimschrift Code Lazarus` -- hits: untersberg-news.at "Die Felsinschrift-Untersbergcode?", kollektiv.org "Der Untersberg Code - entschlüsselt?" and "Der Untersberg-Code & die Inschrift am Goldenen Dachl", untersberg.org/untersbergcode.html, untersberg.org/lazarus-gitschner.html, de.metapedia.org, pravda-tv.com and anti-matrix.com reposts "Zeitportal in die Anderswelt: Der Untersberg-Code", a spam mirror (precipitate.voitl-events.de, not opened). The search summary names two claimed decipherers, Yve Kupka (2015) and the Styrian historian Dr. Peter Kneissl -- both opened or chased below.
(2) `"Satrnrop"` (the inscription's most distinctive token, line 2) -- no hit on this item (all results are "SATRN", a music track and an ASU research network).
(3) `"Untersberg-Code" entschlüsselt Kupka OR Kneissl Übersetzung` -- same pages as (1) plus Schmeh's 2014 German Cipherbrain post, a YouTube video "Der Untersberg Code - entschlüsselt?" (not opened, video), a Google Books record for Rainer Limpöck, *Der Untersbergcode: Das Geheimnis des Bergspiegels* (a book; not read, bibliographic lead only).
(4) `"Untersberg code" solved OR deciphered Claude OR GPT OR ChatGPT` -- no hit on this item; results are the Sept 2026 GPT-6 Astra / Opus 5 Enigma, WWI and Napoleon announcements (other items).
(5) `Peter Kneissl Untersberg Code "heiligste Siegel" OR Symbolschrift Deutung` -- kollektiv.org pages, mystikum.at author page for Kneissl. The search engine's summary of the kollektiv.org page quotes "Das Heilige Siegel bewahrt alles Occulte aus heutiger Zeit" as an interpretation of the inscription's first line ("S. d. d. occo. x."); the page itself could not be read (kollektiv.org answered HTTP 503 twice, see below), so neither the full extent of Kneissl's interpretation nor its date is verified.
(6) `mystikum.at Kneissl Untersberg-Code Lazarus Gitschner Inschrift` -- same pages, plus sn.at "Untersberg: Wie der Mythos einst entstanden ist" and zaronews.world repost; nothing new on a reading.

Pages opened:
- untersberg.org/untersbergcode.html (no author or date on the page): "Seit 2015 gilt der Untersbergcode aus der Lazarus-Gitschner-Sage als entschlüsselt - von _Yve Kupka_." The reading given is the initials tradition "S. V. R. G. E. T. S. A. T. U. M." / "S. 0. R. G. E. I, S. A. T. 0. M." = *Surget satum*, "Aufgehen wird, was gesäet worden", with the code said to point to the Nonnberg convent. The page prints the six-line Hs 2398 text too, and its own author says of it: "Wie man aus jenem seltsamen Code die oben geläufigen lateinischen Worte und damit die Übersetzung entziffert, ist mir schleierhaft." So Kupka's claim is a reading of the sibling initials tradition (Herzog's Hs 3/3a/11 shape, already in this folder), not a token-level reading of the six-line text.
- untersberg-news.at/mystischer-untersberg/die-felsinschrift-untersbergcode/: prints the six lines and SURGET SATUM; its own verdict: "Es bleibt nach wie vor ein Rätsel das noch nicht entschlüsselt ist, obwohl es einige behaupten."
- anti-matrix.com/2022/05/23/... (repost of the pravda-tv 2016 article): calls Surgetsatum a "later Christian reinterpretation" and says "Der echte Untersberg-Code wartet nach wie vor auf seine Enthüllung."
- kollektiv.org (both pages): HTTP 503 Service Unavailable on each, stopped (good-citizen rule); the Wayback route was refused by the fetch tool. **Unreachable**: Kneissl's interpretation is known only from a search-engine summary.

Blog site searches, in the brief's order:
- Cryptiana: on-disk `sources/cryptiana/` grepped for "untersberg" first, zero hits (zero requests); live cryptiana.blogspot.com `search?q=Untersberg`: "No posts matching the query: Untersberg."
- Cipher Mysteries `?s=Untersberg`: "no results were found".
- Cipherbrain `?s=Untersberg`: 3 posts -- 2018-02-09 "The Top 50 unsolved encrypted messages: 11. The Untersberg code"; 2014-05-15 "Der Untersberg-Code: Ein ungelöstes Rätsel aus den nördlichen Alpen"; 2018-11-16 "An encrypted diary written by an Austrian servant and soldier" (a different item, not opened).
  - Post 11 LIVE thread re-checked against the 25 Sept 2026 disk copy: still 2 comments (Katrin 10 Feb 2018, image link; Dan Durham 30 Apr 2018, unrelated); nothing added since 25 Sept 2026.
  - 2014 German post, read with its full thread (27 comments, latest 25 Oct 2020) -- not previously read in this folder. Partial suggestions only, none a decipherment: Peter (16 May 2014) "P. 6. m. 6. a. t." as a biblical reference, plus Surget satum; cimddwc (16 May 2014) "sede deo" for the opening and doubts some digits; Peter (17 May 2014) 6 = G, 5 = S; Gert Brantner (19 May 2014) cites Massmann's variant initials "S. O. R. C. E. I. S. A. T. O. M." / "S. V. R: C. E. T. S. A. T. V. S."; Yehoshua (30 Sept-1 Oct 2016) "Gold und wer es erhält"; Astrid (25 Oct 2020) points to Johannes Lang's article (MGSL 150, 2010; already LOCAL-QUEUE L26). Schmeh's own post asks "Schafft es jemand, den Untersberg-Code zu dechiffrieren?" and announces no solution; no comment mentions Kupka or Kneissl.
- klausschmeh.net `?s=Untersberg`: "Nothing Found"; "Solved cryptogram" category: 4 posts (ADFGVX 21 Sept, WWII Enigma 25 Sept, Copenhagen 27 Sept, Koehler 1 Oct 2026), none about this item.

New-publication check: apeiron.re front page -- a minimal landing page, no listing of solved items, nothing on this item. Cabinet Noir (github.com/el-descifrador/cabinet-noir, shallow clone at /tmp/claude-0/cabinet-noir made by a sibling agent, HEAD 47b6db9, 2 Oct 2026) grepped for untersberg / lazarus / occo / satrnrop: one false positive ("soccorso" in ridolfi-1646/README.md), nothing on this item.

Result: no decipherment or plaintext of this item located by these queries on 3 Oct 2026 (a search result, not a novelty verdict, rule 10). Two claimed solutions exist on the open web and are logged here for any later verifier: Kupka 2015 (a reading of the sibling initials tradition as *Surget satum*, which the same page's author says he cannot derive from the six-line text) and Kneissl (an "interpretation" of at least line 1, "Das Heilige Siegel bewahrt alles Occulte aus heutiger Zeit", known only from a search summary; kollektiv.org unreachable, 503). Neither is a token-level reading of the six lines on what could be read, and Schmeh 2018 and untersberg-news.at both still describe the inscription as undeciphered "obwohl es einige behaupten". Status word unchanged. **Flag:** a later reading of line 1 must be compared against Kneissl's before any rule-10 class is given; the kollektiv.org page is the next fetch (a retry from another session, or the owner's desk), and Limpöck's book *Der Untersbergcode* is an unread bibliographic lead.
Requests: WebSearch 6; untersberg.org 2; untersberg-news.at 1; anti-matrix.com 1; kollektiv.org 2 (both 503, stopped); web.archive.org 0 (tool refused); scienceblogs.de 3; cryptiana.blogspot.com 1; ciphermysteries.com 1; klausschmeh.net 2; apeiron.re 1; github.com 0 (clone shared with a sibling agent). One request at a time per host, sequential.

## Premise check (GF4-BATCH21 (account-4), 3 Oct 2026)

(a) Folder's own mentions: **found, none a full reading.** Herzog 1929 pp. 28-29 prints the six lines with his apparatus of other witnesses; Hs 12 is fully spelled-out Latin ("Bellum. Famus. Gestas. Res. Mores. Amicus. Orpheus.") and Hs 13 mostly plain Latin, but Herzog offers no interpretation, and bUNT5/bUNT6's alignments of Hs 1 against Hs 12 and against Hs 13/3/3a/11 both fail their shuffle controls, so neither witness is a clear copy of this text. The SO-UNTERSBERG-LEADS section already lists the untersberg-news "Surget Satum" and untersberg.org Kupka claims as unchecked prior-claim leads; this pass checked both (section above): they read the initials tradition, not the six lines. The blind pass's "loqui"/"vult" (line 6) are our own candidate glosses, ungraded, not a prior reading.
(b) Other solvers' working files: **not found.** On-disk snapshots: `sources/solver-diffs/2026-10-02-bourdeau.tsv` and `-10-03-bourdeau.tsv` list untersberg-code only in Bourdeau's README skip list ("named in the skip list only", unchanged through his HEAD 2341682); the 25 Sept 2026 shallow clones (first section) found cyphersolver's TARGETS.md grouping it as "open but not settleable by cryptanalysis" and zero hits in aaymeloglu/unsolved-ciphers. No rendering, key or apply script for this text in either. Cabinet Noir: no hit.
(c) Physical neighbours: **checked, not found.** The inscription sits on opening 11 (pencil pp. 20/21) of Hs 2398; its facing page (p. 21) is narrative prose matching Herzog's printed fol. 11 text, not a gloss or clear copy (bUNT4, native resolution). Opening 10 is Bild 1/Bild 2 (no text block). Herzog's "Vgl. fol. 27" points to a second inscription later in Hs 1 (opening 27, two figures with tablets of pseudo-writing, bUNT3/bUNT4) -- a sibling inscription, not a decipherment of this one. No slip or laid-in leaf is recorded in the museum's 28-media sequence. (No image viewed this pass, per brief; this is from the folder's own logs.)
(d) Recipient's side: **not applicable** -- a legend-chronicle illustration with no addressee or receiving office; the closest equivalent, the other Untersbergsage witnesses and later prints (Schöppner 1852, Massmann via Brantner, Lang 2010, Weber-Fleischer 1992), carry the initials tradition or are unread (Lang: LOCAL-QUEUE L26).
Verdict: the premise holds as far as can be checked -- no prior decipherment or plaintext of the six-line Hs 2398 text was found in the folder, the solver files, the neighbouring leaves or the web; one claimed partial interpretation (Kneissl, line 1) is unreachable and must be read before any reading of ours is classed. The item stays `open`.

Gate after this pass (3 Oct 2026, GF4-BATCH21):
```
untersberg-code: open (line 3) -- edition/page or full-text-search citation found within 6 lines
exit 0
```

## Kneissl's interpretation read (GAPS77-untersberg-code (account-4), 3 Oct 2026, 10:13-10:2x UTC)

The next fetch GF4-BATCH21 named above has been run. Live site: `http://www.kollektiv.org/` answered 301 to https, and the https host served an **expired TLS certificate** (curl error 60). That was the one retry allowed, and verification was not bypassed. Wayback CDX (`web.archive.org/cdx/search/cdx?url=kollektiv.org&matchType=domain&filter=original:.*ntersberg.*`) returned HTTP 200 and listed both pages. Both were fetched with `id_`:
- `web.archive.org/web/20171016014654/http://kollektiv.org/der-untersberg-code-entschluesselt/` ("Der Untersberg – Code – entschlüsselt?", 14 Sept 2017). This is a video post: a three-sentence teaser and an embedded YouTube talk (`_dIoL-J3w7g`, not watched, no vision/audio). The teaser itself calls Kneissl's result "eine erstaunliche und auch nachvollziehbare **Interpretation** dieser antiken Symbolschrift".
- `web.archive.org/web/20190818071500/https://kollektiv.org/der-untersberg-code-die-inschrift-am-goldenen-dachl-zwei-oder-doch-eins/` ("Der Untersberg-Code & die Inschrift am Goldenen Dachl – Zwei oder doch Eins?", 15 Nov 2018, "Ein Artikel von Dr. Peter Kneissl"). This is the source of the search-summary quote. It gives:
  - a first "Übersetzung" that only glosses four symbols, for example a sign "aus den Rechnungsbüchern der Salzburger Erzbischöfe" meaning a third payment reminder;
  - a second "Übersetzung", a free German paraphrase of all six lines. Line 1 reads "… das Heilige Siegel bewahrt alles Occulte aus heutiger Zeit"; line 6 reads "Erinnere Dich nicht zu lesen sondern triff Vorsorge in Dir selbst zu lesen …". There is no token-to-word mapping;
  - a third "Interpretation", which he calls "am stimmigsten" (the most coherent): single letters are glossed ad hoc from mixed languages, for example x = the Indian name "Xenia", y = Ymir, mic = Hebrew "who is like God", 519 = the death year of Maximilian I. His conclusion is a prophecy of Maximilian I and Mary of Burgundy returning. This reading contradicts the second one line by line. The page also reports a 2016 "Vision" of the content and dates the manuscript to "um 1630"; the museum dates it 1690-1710 (bUNT3).
  - His own closing sentence: "Wer von mir eine vollständige Übersetzung erwartet ist freilich herb enttäuscht!"

Finding: an **interpretation, not a decipherment**. There are three mutually inconsistent readings, none states a method that maps the text token by token, and none can be applied to the text and checked. It is not a published plaintext of this item, so it gives no ground for `found-solved` (rule 5). Status stays `open`. The comparison flag in the Web check above ("a later reading of line 1 must be compared against Kneissl's") is met: the line-1 text is now on file as quoted.

Print copies (search only, not read): OpenAlex `search=Kneissl Untersberg` returned 0 works. Google Books (`q=Kneissl Untersberg`, keyed, `country=US`) returned 43 hits. Three books by or including Kneissl may reprint these interpretations: Peter Kneissl, *Mein Untersberg* (2017-08-28); Peter Kneissl, *Was mir der Untersberg mitzuteilen hatte* (2018-03-07); and Betz, Wolf, Habeck, Kneissl et al., *Der Untersberg ruft* (2018-09-10). None was opened. Given the web text, a printed copy is a bibliographic lead for a verifier, not a step that could change the status.

Requests: kollektiv.org 2 (301, then expired-certificate refusal; stopped); web.archive.org 3 (CDX 1, captures 2); api.openalex.org 1; www.googleapis.com 1. Spaced at least 3 s per host. No vision. NEAR.md is unchanged, because its named next step (symA / Cappelli, Lang via L26) does not depend on this fetch.

## Schöppner 1852 and Walther 1756 against symA (A2P4-UNT (account-2), 3 Oct 2026, 17:36-17:4x UTC)

Brief `.claude/briefs/runs/2026-10-03-acct2-a2p4-unt.md`. Intake gate: `python3 tools/intake_gate_check.py untersberg-code`
-> "untersberg-code: open (line 3) -- edition/page or full-text-search citation found within 6 lines", exit 0.
Match criterion for item 2 committed before any plate was viewed: `specs/cheap-tests/untersberg-code/PREREG-A2P4-UNT.md` (4ea7ca25).

**Item 1, Schöppner, *Sagenbuch der Bayerischen Lande* vol. 1 (München 1852), no. 5 "Ein Wanderer in den Untersberg": located.**
The Wikimedia Commons PDF answered HTTP 429 (not retried). Internet Archive has two Google scans of vol. 1:
`bub_gb_ortBAAAAcAAJ` and `bub_gb_qD7aAAAAMAAJ`. A grep of both `_djvu.txt` files found the line in each. In the
first it reads "ab: S. O. R. C. E. J. S. A. T. O. M. Ueber dem Aufschauen". In the second the OCR reads
"S. O. R. CE. E. J. ...", where "CE." is an OCR fault. `_djvu.xml` puts the line on leaf 25 of `bub_gb_ortBAAAAcAAJ`.
Rule 2 (print image over OCR) was applied with a crop:
`python3 tools/iiif_lines.py --image leaf25.jpg --out crops --region 300,1250,1600,110 --prefix sch_init`
(leaf image from `archive.org/download/bub_gb_ortBAAAAcAAJ/page/n25_w2500.jpg`). The Fraktur on the crop reads
**S. O. R. C. E. J. S. A. T. O. M.** (11 initials, each followed by a full stop). The printed page number was not
read: the header crop caught only the frame rule, and the OCR has no page numbers. The second-opinion lead cites pp. 5-8. Story
no. 5 begins on leaf 24, so the line stands one leaf into the story. The text names Lazarus Aigner (or Gitschner), servant of the
Reichenhall town clerk, in 1529, and the inscription "mit uralten Buchstaben in die Wand gehauen". Its sources are Bechstein's
*Volkssagen ... Oesterreichs* I, 75 f. and Maßmann.
Comparison with `specs/cheap-tests/untersberg-code/witnesses.tsv` (descriptive, a print witness, not the manuscript):
Schöppner's line is **identical letter for letter to Herzog 1929's Hs 3** (S.O.R.C.E.J.S.A.T.O.M). It differs from
Hs 3a (S.O.R.C.E.T.S.A.T.O.N) at positions 6 (J/T) and 11 (M/N), and from Hs 11 (S.U.R.C.E.T.S.A.T.U.S) at 2, 6, 10 and 11. So
Schöppner prints the Hs 3 tradition and adds no witness reading beyond it. It has no sign at any symA position: it is a run
of capital initials, and every symA instance sits inside Hs 1's longer six-line text. This gives no shape or value
for symA (bUNT9 already showed that the initials witnesses reach symA only by a granularity artefact).

**Item 2, Walther, *Lexicon diplomaticum* (Ulm 1756), general-sign plates: does not match (on the one plate viewed).**
Full-view copy: Internet Archive `gri_33125011161557` (Getty, 362 images). The preface says the alphabetical series is
followed by the "signa ... e. g. particulas con, com, contra, esse, est, et, etcetera, etiam". `_djvu.xml` places
those plates on leaves 254-258. Leaf 255 is **Tab. CCXX**, columns 442-444, signs for con, conceditur, conceptus,
continens, contra, cum, de, enim, esse, est and et, with 81 entries viewed. Crop command (a plate is not a text line, so
`tools/iiif_lines.py` found one line only; four explicit bands were cut instead):
`python3 -c "from PIL import Image; im=Image.open('w255.jpg'); [im.crop((0,y,1887,min(3000,y+800))).save('w255_band%d.jpg'%(i+1)) for i,y in enumerate((0,740,1480,2220))]"`
(leaf image `archive.org/download/gri_33125011161557/page/n255_w1887.jpg`). Pre-registered criterion: F1 hook top-left, F2 vertical
stem with top serif, F3 loop at the join, F4 long descender with no crossbar. The nearest signs are the "9"-shaped *con*
forms (col. 442, e.g. 1408 and 1447). They have a top loop (F3, arguably F1) and a tail below the baseline without a crossbar (F4), but no
vertical stem with a top serif (F2). That is 2-3 of 4: partial at best, **not a match**. The *est* signs (small 3/z
shapes), the *esse* bars, the *enim* cross, the *cum* "9" and the *et* ligatures (compound forms with crossing strokes) all
reach fewer features. The comparison was made by eye against bUNT8's written description of symA, not side by side with the symA crop.
Leaves 254 and 256-258 (Tab. CCXXI and after: et cetera, punctum, interrogation and division signs) were **not viewed**.
The vision budget was spent (2 of 2), so the negative covers Tab. CCXX only. This agrees with bUNT8's Cappelli check (p. 634, no match):
symA is not, so far, a catalogued general Latin sign.

Counts (rule 4): H 0, C 0, S 0. No token is graded from either source. Neither is a key for this hand (Hs 2398, c.1690-1710).
Rule 3: neither item is a statistic, so there is no control figure. Item 2 is a pre-registered by-eye shape match with a stated criterion.
Requests: upload.wikimedia.org 1 (429); archive.org 9 (advancedsearch 2, djvu.txt 3, djvu.xml 2, page jpg 2, page_numbers 1), spaced at least 2 s apart.
Vision: 2 calls (Schöppner line plus a blank header crop; Walther Tab. CCXX in 4 bands).

Next step for symA (one line; run by D2B-UNT, 6 Oct 2026, see below): view Walther leaves 254 and 256-258 (Tab. CCXIX tail, CCXXI ff.), 1 vision call
per leaf in bands, about USD 0.5. Better still, build the same-scribe concordance across the 28 leaves first (WAIT-PASS-B item 3).

## Walther leaves 254 and 256-258 against symA (D2B-UNT (account-2), 6 Oct 2026, 00:15-00:2x UTC)

Brief: `.claude/briefs/runs/2026-10-05-account2-default-2217-jobs.md` job D2B-UNT. Intake gate (6 Oct 2026, 00:16 UTC):
`untersberg-code: open (line 3) -- edition/page or full-text-search citation found within 6 lines`. This step was still undone:
the NOTES.md line ending A2P4-UNT's section names it as not run. The criterion is A2P4-UNT's own, committed before any plate was viewed
(`specs/cheap-tests/untersberg-code/PREREG-A2P4-UNT.md`, 4ea7ca25), and was not changed here. A match needs one sign with F1 (hook
at top-left), F2 (vertical stem with a top serif), F3 (loop at the join) and F4 (long descender, plain, NO crossbar). 3 of 4 is
partial. No sign reaching 3 of 4 means "does not match".

**Source and crop step.** The copy is Internet Archive `gri_33125011161557`, page images `page/n{254,256,257,258}_w1887.jpg`
(each 1846-1887 x 3000). Crop step, run and pasted: `python3 tools/iiif_lines.py --image w<N>.jpg --out crops<N> --prefix w<N>`
found 3/2/3/4 "lines" on leaves 254/256/257/258. A plate is a table of signs, not text lines, so the same happened as on leaf 255.
Explicit column-band crops were cut with PIL (`im.crop((150,350,1700,1500))` and `im.crop((150,1450,1700,2650))` per leaf,
reduced to about 1240 px wide). Native-size zooms went to the candidate signs only. For a side-by-side check, a reference crop of
symA was cut from `images/hs2398_opening11_inscription_leaf.jpg` (lines 4-6, box 200,1050,2300,1560, plus a zoom of line 6
"ꝑꝑmi", box 700,1380,1000,1560). A2P4-UNT compared only against bUNT8's written description, so this side-by-side check is an addition.
The crops stayed in the session scratchpad and were not committed (the commands above regenerate them).

**What the leaves are.**

| leaf | plate | cols | content |
|---|---|---|---|
| 254 | Tab. CCXIX | 437-441 | alphabetical YMO-ZZ (ym° imago ... zz zinziber); then *communi*, *completorium*, *componitur* and 27 *con* signs (col. 439-441) |
| 256 | Tab. CCXXI | 445-447 | about 60 *et* signs and ligatures (1155-S.XIV), 21 *et cetera* forms, *et dicitur* |
| 257 | Tab. CCXXII | 448-450 | *etenim*, about 25 *etiam* signs, *ex*, *id est*, *-nt*; *pupilla*, *-rum*, *secundum naturam*, *sed*, *subscripsi* monograms, *VT*; Isidore's critical notae (Accentus, Aduersae, Alogi, Anchorae, Antigraphi, Antisigmatis, Apostrophes, Aspirationis; Ceraunii, Choenix, Circumflexi, Coniunctionis, Coronidis x2, Crismi, Cryphiae, Diastoles, Diples x5, Dragma, Grauis, Libra, Limnisci, Obeli, Obolus, Oxiae, Phietronis, Positurae, Psyches, Rectae et Auersae obelatae, Semiuncia, Uncia) |
| 258 | Tab. CCXXIII | 451-453 | calendar signs (Capitis Draconis, planets); characters before a document's first line (S.VIII-1085, large monogram and chrismon flourishes); puncta 1143-1379; *Punctorum vicarii in fine Diplomatis* (S.VIII) |

**Nearest signs per leaf, against F1-F4.**
- 254: the "9"-shaped *con* and *communi* forms have a top loop and sometimes a tail, but no stem with a serif: 2 of 4. This is the same
  shape class A2P4-UNT found on Tab. CCXX. In the alphabetical half, the *per* p of "yꝑdlia hiperdulia" (S.XIV m) has a stem, a bowl and
  a lead-in, but its descender is **crossed**, which fails F4 by the PREREG's own wording: 2-3 of 4 at best, with the missing feature F4.
- 256: the *et* forms are e+t ligatures (loop plus crossed t ascender). The flourished 1155 forms have a loop and a tail but no
  vertical serifed stem: 2 of 4.
- 257: the nearest is *Coronidis nota* (second form, a ρ-shape: bowl top-right, plain diagonal descender to the lower left). It has F4 and
  arguably F3, but no hook at top-left and no serifed vertical stem: 2 of 4. *sed* 1448 (long-s ligature) has a stem and descender with
  its hook at top-**right** and no loop: 2 of 4. *Phietronis nota* (φ with a ring through the stem) fails F4.
- 258: the "pp" *punctum* (S.VIII, Punctorum vicarii) has two p-shapes with long plain descenders and bowls (F3, F4) but no hook at
  top-left and no top serif: 2 of 4. Puncta 1311/1357/1379 (hooks and s-curves) and the calendar signs reach 2 or fewer.

**Result: does not match (leaves 254, 256, 257, 258).** No sign on any of the four leaves reaches 3 of 4 features. With A2P4-UNT's
Tab. CCXX (leaf 255), all five of Walther's general-sign plates CCXIX-CCXXIII are now viewed against the PREREG with no match. This is a
reference-dictionary search result, not a reading. symA stays ungraded (bUNT9's correction: "no signal", not I). No token is graded from
Walther. It is a reference dictionary, not a key for this hand (rule 4: H 0, C 0, S 0). Rule 3: this is not a statistic and there is
no control figure; it is a pre-registered by-eye shape match. Counts unchanged from bUNT8/bUNT9 (C 0, M 4, H 0, I 1).

**Observation for the next step (not acted on).** In the side-by-side zoom of line 6 "ꝑꝑmi", the first symA instance seems to carry a
short leftward mark on the stem at about baseline height. At this crop (about 1:1 of the 4884 px leaf) the mark cannot be told apart
from the descender's own curl. If it is a crossbar, symA is closer to the ordinary *per/par/por* p (Cappelli's crossed-descender p;
Walther's "yꝑdlia" above) than bUNT8's F4 "no crossbar" allows. That would make F4, and so the PREREG criterion itself, the thing to
re-check. This is not graded and does not change any token. It belongs with the same-scribe concordance (WAIT-PASS-B item 3): compare
all five symA instances with every crossed-descender p across the 28 leaves.

Requests: archive.org 4 (page jpg x4, 2 s apart, descriptive User-Agent), all HTTP 200. No other host. Vision: the four leaves' band
crops and zooms (about 4 leaf-units) plus 2 reference crops of Hs 2398. No subagents.

Next step for symA (one line, not run): the same-scribe concordance across the 28 IIIF leaves on disk, with every crossed-descender p
and every symA-like sign, to settle F4 (crossbar or curl) before any further reference-dictionary comparison. About USD 2-3 (WAIT-PASS-B item 3).

## symA same-scribe concordance, F4 crossbar or curl (R8-UNTB (account-4), 6 Oct 2026, 03:44-03:5x UTC)

Brief: `.claude/briefs/runs/2026-10-06-account4-run8-jobs.md` job R8-UNTB. Intake gate (as pasted in the brief): `untersberg-code: open
(line 3) -- edition/page or full-text-search citation found within 6 lines`. The step was still undone (D2B-UNT's closing line says "not run").
Decision rule pre-registered and pushed before any concordance crop was viewed: `specs/cheap-tests/untersberg-code/PREREG-R8-UNTB.md`
(4e338bf0). Its control: the crops must show a crossbar on at least 3 crossed-descender p's ("ꝑ") of this hand before any symA call counts.

**Correction to the step's premise.** "The 28 IIIF leaves on disk" was not true: only opening 11 (native) and opening 27 (1225 px) were on
disk. The 28 media ids were re-read from the detail page (1 request) and are now listed here in display order, openings 1-28:
1b269afd 4b5c42d3 / c77a3260 / 73ccf971 / 36d9b7c4 / ec0eefb6 / 2472faca / 85829ccf / ee3545c6 / c11153a3 / 56503bb8 / dc46a099 / ac4867cb /
2a58d4c3 / 47c0cffb / 089cd7fc / b31bf664 / 326b6a91 / dfad071c / 43c1056a / d8f70845 / 3440046a / 23f8f47d / 8b15ec2f / 2e0e5eb7 / f29d99d8 /
6c3da5b8 / e0f9d823 / 000a8f4e (first 8 hex digits; full UUIDs in the detail page, `.../iiif/iiif/2/{uuid}/full/{w},/0/default.jpg`).
bUNT3's "openings 2-12ish are prose" is also off: opening 2 is a full-spread painting with no text.

**Leaves viewed (units) and crop step.** Openings 1, 2, 3, 4, 5 fetched at 2450 px wide (half native) to the session scratchpad (not
committed), plus opening 11 at native from disk. Crop step run and pasted, per page:
`python3 tools/iiif_lines.py --image o{3,4,5}.jpg --out crops{N}{L,R} --columns 40:1225 | 1225:2420 --lines-per-crop 7 --max-width 1300`
(3-4 band crops per page, viewed as stacked bands), `python3 tools/iiif_lines.py --image o1.jpg --out crops1 --region 330,640,1900,1300
--lines-per-crop 1` (11 crops), and PIL zooms of the symA instances from `images/hs2398_opening11_inscription_leaf.jpg` (boxes
880,680,1100,960 / 1060,1040,1280,1320 / 700,1380,920,1660 / 1280,1380,1500,1660; the L4 tok5 box was mis-placed twice and is not read).
No subagents; the worker viewed the crops itself (8 band/zoom views of prose, 4 of symA).

**Reference class R (crossed-descender p in this hand): 0 found.**
| opening | pages | script | crossed-descender p | other p forms seen |
|---|---|---|---|---|
| 1 | title + text | Kurrent with Latin-script words (Sicillia, "Spirallamundi" [Speculum mundi], "Forhiria") | 0 | 1 plain Latin-script p in "Sp-": lead-in rising from baseline-left into the bowl, descender curling left at the foot, no bar |
| 2 | painting | none | 0 | -- |
| 3 | 2 prose | Kurrent | 0 | Kurrent p in "Cuper" (R page), plain descender |
| 4 | 2 prose | Kurrent | 0 | none identified |
| 5 | 2 prose | Kurrent | 0 | capital P in "Pallast", "Perlein"; no bar |
| 11 | prose (R) + inscription (L) | Kurrent / painted Latin-style | 0 | inscription capital P (L3 tok1); no other p |
The prose hand is German Kurrent and never needs the Latin *per/par/pro* abbreviation on these pages.

**symA instances (S), recorded under the PREREG's X/C/U.**
- L2 tok1 final glyph: U. A stroke runs from a heavy dot at baseline-left up through the stem into the top-right bowl; nothing crosses the
  descender below the bowl, and the descender itself is plain and straight. Whether that rising stroke is a *per* bar or the letter's own
  lead-in (as on the plain p of opening 1's "Sp-") cannot be told without the reference class.
- L4 tok7: U, same construction as L2.
- L6 tok2 first glyph: U, same construction (this is the mark D2B-UNT saw as "a short leftward mark on the stem at about baseline height":
  it is the heavy dot at the start of the rising stroke).
- L4 tok5: U, not adequately cropped this pass.
- L6 tok3: C. The descender sweeps left into a large open hook (a z/ꝗ-like tail), with no stroke crossing it.
- symA-rev (L6 tok2 second glyph): no descender at all; reported, not counted.

**Result: F4 UNSETTLED (non-test).** The PREREG's resolution control failed: 0 R instances against the 3 required, because the scribe's
prose hand on openings 1-5 and 11 never writes a crossed-descender p. So the crops cannot show what this hand's crossbar looks like, and
no symA tally counts. Rule 3: the control could have passed (any Latin *per* in the prose would have counted) and did not, so this is a
recorded non-test, not a negative. Rule 4: no token graded (H 0, C 0, S 0); counts unchanged from bUNT8/bUNT9 (C 0, M 4, H 0, I 1).

**Observations, not graded.** (1) L6 tok3's tail curls into a large left hook while L2/L4 tok7/L6 tok2 have a straight plain descender
with a rising stroke from a baseline dot: on these crops "symA" may be two different signs, which bUNT8 grouped as one (it noted only
"a longer or shorter descender"). Any later sign-classification pass should keep L6 tok3 apart until settled. (2) The rising stroke from a
baseline dot on the three straight-descender instances has the same direction as the lead-in of the scribe's plain Latin-script p
on opening 1. If this is the same stroke, then the "crossbar" D2B-UNT saw is how this scribe builds p, not a *per* bar. One example cannot
settle that.

Requests: sammlung-online.salzburgmuseum.at 6 (detail page 1; IIIF full/2450 for openings 1-5, 5), at least 2 s apart, descriptive
User-Agent, all HTTP 200. No other host.

Next step for symA (one line, not run): find the reference class elsewhere, using Latin-script words and painted captions on the
illustrated openings 12-28 (opening 27's tablets first, 1225 px on disk, then native). Screen with 400 px thumbnails first, then crop only
the leaves that have Latin script. If no crossed-descender p turns up in the whole manuscript, F4 is untestable within this manuscript and
goes to the paleographer crop packet (SO-UNTERSBERG-LEADS methodology item 2). About USD 2-3.

## symA reference class from the illustrated openings, F4 (R9-UNTB2 (account-4), 6 Oct 2026, 06:01-06:11 UTC by date -u)

Brief: `.claude/briefs/runs/2026-10-06-account4-run9-jobs.md` job R9-UNTB2. Intake gate (pasted): `untersberg-code: open (line 3) --
edition/page or full-text-search citation found within 6 lines`. The step was still undone (R8-UNTB's closing line: "not run").
PREREG: `specs/cheap-tests/untersberg-code/PREREG-R9-UNTB2.md` (3dfacf6e), pushed before any opening 12-28 was viewed. It reuses
PREREG-R8-UNTB unchanged and only widens the units.

**Leaves and crop step.** All 17 openings 12-28 were screened at 400 px (one contact sheet). Opening 27 was fetched at native size,
4900x3064. Then all prose and caption openings were fetched at 2450 px: 12-16 and 19-26, plus openings 6-10, which no pass had read at
reading size (bUNT4 had sampled 8-10 only as 600 px thumbnails). Openings 17 and 18 are paintings with no text, and 28 is the back cover
with the library stamp. Images were saved to the session scratchpad and not committed. Crop step run and pasted:
`python3 tools/iiif_lines.py --image o27.jpg --out c27top --region 2500,0,2400,560 --lines-per-crop 1 --max-width 1300` (inscription
lines 1-2), `--out c27ins3 --region 2560,380,2100,260` (line 3), `--out c27L --region 1640,1120,280,540`, `--out c27L2 --region
1820,1100,200,580` (left tablet), `--out c27R --region 2700,960,680,700` (right scroll); `--image m16.jpg --out c16 --region
1270,490,1080,140`, `--image m12.jpg --out c12 --region 700,30,500,110`, `--image m21.jpg --out c21 --region 1450,1240,300,110`,
`--image m25.jpg --out c25 --region 1340,80,380,110`, `--image m9.jpg --out c9 --region 60,560,330,120`, `--image m10.jpg --out c10
--region 50,50,1100,110`. On single words the tool trims to one ink band (c9 came out 49 px high, the c21 crop missed its word), so
those two were read from PIL zooms of the same 2450 px file instead (m9 box 40,440,560,560 at 2x). No subagents were used. The worker
viewed the images itself: 1 contact sheet, 9 page or page-pair overviews, 7 crops or zooms.

**Reference class R (crossed-descender p in this hand): 0 found, now across all 28 openings.**
| opening | Latin-script words / painted text seen | p forms | R |
|---|---|---|---|
| 6, 7, 8 | none (Kurrent prose) | Kurrent only | 0 |
| 9 | "Speculmundi" [Speculum mundi], L page | 1 Latin-script minuscule p in "Spe-": the descender ends in a leftward curl or loop at the foot, with no bar on either side. Same build as R8-UNTB's opening-1 "Sp-" | 0 |
| 10 | title "Die Prophezeyung so im Undtersperg ..." (Kurrent display hand) | Kurrent p, plain | 0 |
| 12 | "Prelat"-type word (Latin-style capital P), L line 1 | capital P with a loop, plain stem | 0 |
| 13 | captions in Kurrent | -- | 0 |
| 14 | "Instrument", "Musical-", "Coricanten" | none | 0 |
| 15 | "Figuriren", "Musicalische Instrument", "Refent" | none | 0 |
| 16 | "Refent", "Liberey", "Cardinal", "Bischoff", "Prälaten", "Probst", "Prior" | capital P (x2) plain; Kurrent p in "Probst", plain descender | 0 |
| 19 | "Musicalischen Instrumenten", "Figuriren" | none | 0 |
| 20, 22, 23, 24 | "Nation" (23) | none | 0 |
| 21 | "Prälat" (not cropped adequately) | -- | 0 |
| 25 | "Practi(c)ena" [Practiken], R line 2 | Latin-script capital P with an open loop and a plain stem | 0 |
| 26 | INRI titulus (painted) | -- | 0 |
| 27 | 3-line painted inscription (R page) + left tablet of symbol columns + right scroll | inscription "...ONP·..." has a plain capital P; the tablet and scroll have no p-shaped sign with a crossed descender | 0 |
Carried forward from R8-UNTB: openings 1-5 and 11 had 0. Total R = 0 against the 3 required.

**Result: F4 untestable within this manuscript (non-test).** The PREREG resolution control fails for the second time, now with every
text-bearing opening of Hs 2398 viewed at 2450 px or native. This scribe never writes a crossed-descender p. The control could have
passed: any Latin *per/par/pro* abbreviation in the Latin-script words would have counted. It did not, so no symA tally was run. Rule 4:
no token graded (H 0, C 0, S 0). Counts are unchanged from bUNT8/bUNT9 (C 0, M 4, H 0, I 1). By the PREREG this is "untestable here",
not a negative on F4.

**Observation, not graded.** The two Latin-script minuscule p's this scribe writes (opening 1 "Sp-", opening 9 "Spe-") both end the
descender in a leftward foot-curl, with no crossing stroke. That fits R8-UNTB observation 2, that a stroke near the descender may be how
this hand builds p. Two examples do not settle it, and symA is in the painted inscription hand, not the prose hand.

**Observation, not graded (opening 27).** The R page carries a 3-line painted inscription in the same alphabet family as the opening-11
six-liner. Read by eye, unverified: "ISYRLEDETREUTEEIHS / SYREKSTERYTONP·DXYZ / ELTUAAXdÿGHES". The left figure's tablet carries two to
three columns of symbols (3, 9, c, +, 8, ε, a, r, x, e, s ...). The right figure's scroll reads roughly "de Naleesge.. / zotaasdes / ahFa·
Nea:". Line 342 above calls opening 27 "tablets of pseudo-writing". The tablets may be, but the top inscription is a full painted text
and is Herzog's "Vgl. fol. 27" sibling inscription. Not transcribed blind, and not checked against Herzog pp. 45-50 this pass.

**Paleographer crop packet (SO-UNTERSBERG-LEADS methodology item 2): add F4.** "Does symA (L2 tok1 final, L4 tok5, L4 tok7, L6 tok2
first glyph; L6 tok3 kept apart) carry a *per*-bar or this hand's own p lead-in/foot-curl? No crossed-descender p occurs anywhere in Hs
2398 (R8-UNTB + R9-UNTB2, all 28 openings), so the question needs an outside reference hand. Include as comparanda the two plain
Latin-script p's (opening 1 'Sp-', opening 9 m9 2450 px box 40,440,560,560) and the opening-27 inscription's 'P'."

Requests: sammlung-online.salzburgmuseum.at 37 (detail page 1, 400 px thumbnails 17, native opening 27 1, 2450 px 18), at least 2 s
apart, descriptive User-Agent, all HTTP 200. No other host.

Next step for symA (one line, not run): F4 can only move through the paleographer packet (outside reference hand). The cheapest
in-folder step instead is a blind 2-pass transcription of the opening-27 inscription (3 lines, native crops above), collated against
Herzog's "Vgl. fol. 27" apparatus. It is a sibling text in the same alphabet and may show symA-like signs in a second context. About
USD 3-5. It is a machine transcription of a symbol inscription, so check the TRANSCRIPTION.md sorter rule before briefing it.
