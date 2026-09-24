open

# August van Saksen (Sachsen) and Willem van Oranje, three cipher letters/postscripts, 1561-1564

QUEUE row: NB2 (`QUEUE.md`, "Dutch and Belgian archives (LANE N scout of 24 September 2026)").

## Source

Three letters/postscripts in the correspondence between Elector August of Saxony and William of Orange (Anna
of Saxony, August's niece, married William in 1561 -- the marriage this correspondence surrounds), "in
cijferschrift", no solution recorded in the WVO database:

| briefnr | date | direction | place | WVO record |
|---|---|---|---|---|
| 53 | 24 Oct 1561 | Willem -> August | Breda | https://resources.huygens.knaw.nl/wvo/app/brief?nr=53 |
| 57 | 18 Nov 1561 | August -> Willem | Torgau | https://resources.huygens.knaw.nl/wvo/app/brief?nr=57 |
| 126 | 16 Sep 1564 | Willem -> August | Brussel | https://resources.huygens.knaw.nl/wvo/app/brief?nr=126 |

Primary sources: Sächsisches Hauptstaatsarchiv Dresden, Geheimer Rat (Geheimes Archiv), Locat 9941/3 (53, 57)
and Locat 8510/5 (126); Koninklijk Huisarchief Den Haag holds copies/excerpts of some. Free PDF scans, no
login: `resources.huygens.knaw.nl/media/wvo/images/00000-00999/000{53,57,126}.pdf`.

**Confirmed by eye this pass** (`images/00053_p1-1.png`): 00053 is a German secretary-hand plaintext letter
(courtesy/family news, dogs and ferrets sent as gifts, per WVO's Inhoud field) with a cipher postscript at the
foot of the page in an **arbitrary-symbol cipher** (glyphs including X, V, Λ, ϖ, Δ, combined with digits) --
visibly a different design from the Lodewijk van Nassau numeral cipher of NB1, consistent with WVO's own note
"Een gedeelte van de brief is in cijferschrift" (part of the letter is in cipher). 00057 and 00126 not fetched
as images this pass (budget; both confirmed reachable by the scout, HTTP 200).

Four other letters from the same correspondence circle and years (briefnrs 74, 98, 153, 175) **do** carry a
contemporary solution or decipherment, per the scout's control sweep (QUEUE.md) -- not re-verified by this
worker, cited as background only.

## Check-solved sweep, 24 September 2026

Run directly by this worker (Sonnet, no Workflow tool, no subagents).

1. **Editions first / printed excerpt found for 57.** Briefnr 57's Brongegevens field (fetched and read this
   pass) cites: **"Demandt, Nassau-oranische Korrespondenzen, I, 78 nr. 113 -- excerpt"**. This is Karl E.
   Demandt's *Nassau-oranische Korrespondenzen 1553-1570*, published as **Regesten** (calendar-style summaries,
   not full transcriptions) in *Hessisches Jahrbuch für Landesgeschichte* 38 (1988), p. 49ff, and 39 (1989),
   p. 87ff, itself based on 18th-century Dillenburg archivists' own summaries of the originals (per WebSearch
   snippets of the work's own subtitle: "...in Gestalt der von den Dillenburger Archivaren Johannes von Arnoldi
   und Heinrich Westerburg Ende des 18. [Jahrhunderts]..."). **This worker could not locate or read Demandt's
   text itself this pass** -- *Hessisches Jahrbuch für Landesgeschichte* is a specialist regional journal, not
   found on Internet Archive, HathiTrust or Google Books by WebSearch, and not fetched. Given it is described
   as a Regest (a calendar entry summarising a letter's contents and archival location, in the same genre as an
   English "calendar of state papers" entry, not a diplomatic edition printing full text), a full cipher
   decipherment inside it would be unusual but is not ruled out by this worker's search. **Flagged as an open
   gap, not resolved**: WVO's own field labels the Demandt reference "excerpt" (not "editie", the label used for
   Groen van Prinsterer's full edition -- see NB4/`ciphers/la-garde-1577/NOTES.md`), which is weak positive
   evidence it is a summary, not a full/deciphered text, but this is inferred from the database's own citation
   genre labels, not from reading Demandt directly. 53 and 126 have no printed-edition citation in Brongegevens
   at all (manuscript only).
   No other candidate edition was located and read for this specific correspondence (Kluckhohn's "Briefe",
   named in CLAUDE.md's editions-first list for August of Saxony, was searched by WebSearch and found to concern
   a different Kluckhohn edition -- the WebSearch surfaced only August von Kluckhohn's biographical details, no
   locatable "Briefe" volume matching this correspondence; not pursued further, flagged as a second gap).
2. **WVO curatorial field.** As with NB1, the Opmerkingen field for 53, 57 and 126 carries no "oplossing" /
   "ontcijferd" / "ontcijfering" marker (contrast the four already-excluded siblings 74/98/153/175 in the same
   correspondence circle, confirmed by the scout to carry such markers).
3. **Community lists.** `sources/cryptiana/web/dutch.htm` read in full (see NB1 notes): no mention of this
   correspondence. WebSearch (`Kluckhohn Briefe August von Sachsen Wilhelm von Oranien 1561 1564 Chiffre`)
   found nothing relevant beyond genealogical pages confirming the 1561 marriage date.
4. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` grepped for the same terms as NB1: zero
   hits.
5. **Solver repositories.** Same fresh clones as NB1 (24 Sept 2026), grepped the same way: no hits relevant to
   this correspondence circle in either repository.
6. **General web search.** As item 3; also `Demandt "Nassau-oranische Korrespondenzen" Wiesbaden 1955 Band 1
   review` and `Demandt "Nassau-oranische Korrespondenzen" August von Sachsen Wilhelm von Oranien 1561 Chiffre`
   -- surfaced only the HessJb 38/39 (1988/1989) citation above and unrelated genealogy/biography pages; no
   solution claim found for any of the three letters.

## Verdict

**Status: open** (53, 126 firmly; 57 open but with an unread printed excerpt citation flagged as a genuine gap
-- see item 1). No solution, key or full deciphered plaintext found in six sources for any of the three.

**Copy status: copy-free.** Free PDF scans confirmed reachable; 53 viewed by eye, cipher confirmed present
(symbol design). 57 and 126 confirmed reachable (HTTP 200) but not opened this pass. No REQUEST.md needed for
the manuscripts; **a REQUEST.md-style follow-up worth naming for the next worker: access to Hessisches Jahrbuch
für Landesgeschichte 38 (1988) and 39 (1989) to read Demandt's regest of letter 57 directly**, not chased this
pass (not a personal-data request, so not written up as a formal REQUEST.md row this pass -- flagged here
instead as it needs a library/journal-access route, not a manuscript copy order).

**Kind: cryptanalysis** (no sibling decipherment identified for this specific trio this pass, unlike NB1;
the four already-solved circle-mates 74/98/153/175 are a possible future alignment lead, not chased here).

## Image capture, 24 September 2026 (LANE R worker R9)

Targets 57 (4pp) and 126 (5pp) fetched in full. All four siblings named in the brief -- 74, 98, 153, 175 --
opened as WVO records first (all "Willem -> August", same correspondence run and direction as 53/126, each
already flagged with an explicit cipher+solution note in Opmerkingen before fetching) then fetched in full (7,
6, 9 and 10 pages respectively) and rendered to PNG at 100dpi (lower than NB1/NB4's 150dpi, to fit 44 pages
under the 30MB folder cap -- re-fetch pdf_url at higher resolution for a solver pass). `images/manifest.json`
and `images/inventory.tsv` (per-page content, cipher type, approx tokens, decipherment location) written.

**Kind should be revisited: this is now also a recovery target, at least for a subset.** Confirmed by eye:
- **74**: cipher (f.18-18v) AND its contemporary decipherment (f.19-20, clear German, headed with the
  cipher's evident subject) are both imaged -- exactly the sibling pattern WVO's Opmerkingen promised.
- **98**: cipher (f.66) and a probable decipherment (f.68-69, headed "Zeittunge auss Franckreich") imaged;
  not confirmed word-for-word against the cipher's length, flagged for the solver.
- **153**: cipher (f.4) AND **two independent** contemporary decipherments (f.5, f.6 -- near-duplicate but not
  identical opening sentences) imaged. WVO's "waarvan 2 oplossingen" note is confirmed literally.
- **175**: cipher is not block-form but interlinear, run inline within clear German prose at several points in
  the letter, several with small marginal glosses in a different hand/ink directly above -- consistent with
  WVO's "(opgelost)" note but not confirmed as a full decipherment by this worker (flagged for a solver pass;
  see inventory.tsv per-page notes).

**Six distinct cipher designs observed across this one correspondence circle** (53/57: letters + arbitrary
symbols incl. Λ, Δ; 74/126: different arbitrary-symbol repertoires from 53/57 and from each other; 98: numerals
+ a few symbols; 153: pure overlined numerals, no symbols; 175: interlinear). **A solver should not assume one
key covers 53/57/126 just because 74/98/153 share a recoverable key with their own decipherments** -- the
designs differ letter to letter even within "Willem -> August" in this eight-year window. The alignment lead
is strongest for 153 (cipher + 2 decipherments) and 74 (cipher + 1 decipherment); 53/57/126 (the actual
targets) do not yet have a confirmed matching design to any deciphered sibling -- this needs eye comparison of
glyph repertoires once a solver pass runs, not assumed from correspondence direction alone.

Host: resources.huygens.knaw.nl, 10 requests this pass (4 WVO record pages + 6 PDF fetches, >=2s apart).
Folder kept at 24MB under the 30MB cap.

## R14: atlas and passes (24 September 2026, stopped over cap)

Done and pushed: `glyphs/atlas.md` (glyph codebook built from 74 p3-p4, 98 p2, 126 p4 by eye, no
pixel-crop segmentation available in this container -- see atlas.md's method note; 53/57 share G1/G3/G4
with 74/126 but also show G2 and G13 not confirmed elsewhere, so repertoire overlap is partial, not
identical, matching R9's "six distinct cipher designs" note above); `plaintext_74.txt` (ff.19-20,
briefnr 74's decipherment leaf) and `plaintext_98.txt` (ff.68-69, briefnr 98's decipherment leaf),
both best-effort palaeography, German as written, [?] on uncertain words, not aligned or decoded.

Left undone: the two blind passes (passA.tsv, passB.tsv) over 126 p4, 74 p3-p4, 98 p2, 53 p1 postscript,
57 p3 block (both blocks -- 57 p3 has two separately-signed cipher blocks, not one, noted to the pass
workers). Two Sonnet subagents were launched to do these blind from the atlas and had not written their
output files when this worker was stopped at cap ($10.70 against a $7 cap); neither passA.tsv nor
passB.tsv exists on disk. Their agent sessions may still be running in the orchestrator's environment
and could still land results; if so, whoever picks this target up next should check for them before
re-running the passes, then `tools/reconcile_passes.py passA.tsv passB.tsv` (header `line pos sign
briefnr page lineno`, matching the tool's "long" format) into `recon/`. No sign count or agreement
percentage is available -- the passes never completed. No H/C/S/M/I grades apply here (no decoding
attempted this pass).
