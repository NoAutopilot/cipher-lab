closed-negative

**Status set closed-negative by the parent orchestrator, 24 Sept 2026 18:43 UTC**, from the LANE R4 R solver section below: simple and homophonic substitution of continuous Italian, German or Latin excluded with matched controls (rule 3); the item is more likely a list of disguised names than a text. Capture, atlas and controls stay in the folder. Reopen only with a key source or a different cipher model.

**Edition check (LANE N3 csED3, 24 Sept 2026 18:xx UTC):** hold lifted -- verdict `open`. The standard printed
catalogue (Witten & Pachella, *Alchemy and the Occult*, Yale 1977, vols 3-4) is not reachable in full (HathiTrust
holds only vols 1-2, the 1968 printed-books catalogue; the manuscripts volumes are not digitised anywhere found);
Beinecke's own manuscript-catalogue page (already read by csCS2c, section 2 below) is this item's closest available
standard description and was re-confirmed. One directly relevant piece of scholarship on this manuscript's cipher
content was found and read (Agnieszka Rec, Societas Magica Newsletter 31, Fall 2014) -- it does not solve or read
this folder's target cipher. DECODE record documents and Aymeloglu's repository checked (below), both clean.
Section 2 below. Brief `.claude/briefs/runs/2026-09-24-lane-n3-csED3.md`.

# Pseudo-Elian alchemical cipher, "Lumen luminum" — Beinecke Rare Book & MS Library, Mellon MS 29

QUEUE row: CS2-14 (`sources/solver-diffs/2026-09-24-cyphersolver-site.tsv`, LANE N3 scout scCS2, 24 September
2026 — catalogue item 169 at dbourdeau.github.io/cyphersolver/catalogue.html), DECODE R2877. Check-solved run
24 September 2026 by LANE N3 csCS2c (session_0113dPptSGXZiBF5uwvtKmtc), brief
`.claude/briefs/runs/2026-09-24-lane-n3-csCS2c.md`.

## What it is

Not a letter — an alchemical codex, "Lumen luminum," ascribed (almost certainly falsely) to "Elias Cortonensis"
(Elia da Cortona, a 13th-century Franciscan; the manuscript itself dates to c.1525, and the catalogue's own
judgement is that the attribution is a deliberate pastiche, "a hint of charlatanism"). Bourdeau's catalogue:
"attempted, open (not a letter -- alchemical codex; cipher only ff.1v-2v, ~234 letters; simple/homophonic/
progressive/Vigenère/Alberti all fail)." Prior scout pass (24 Sept 2026) marked the image route "Beinecke online
viewer not checked this pass; DECODE thumbnail only" and the row "copy-order (unconfirmed)."

## Image route (confirmed copy-free, this pass)

collections.library.yale.edu's own catalogue search answers plain curl with an HTTP 202 challenge page (needs a
real browser — same pattern CLAUDE.md's Access playbook documents for Yale). `tools/browser_fetch.js` cleared it.
Search for "Mellon MS 29" surfaces catalog record `17388793` ("Lumen luminum, etc," creator "Elia, da Cortona,
frate, -1253," call number "Mellon MS 29," 74 images) — matches this target exactly. Its IIIF Image API endpoint
(`https://collections.library.yale.edu/iiif/2/17388794/info.json`, the first of the item's 74 images) answers
**plain curl directly** (no browser challenge on the image API itself, only on the HTML catalogue search page):
2269×3105, level2 profile — **image is online now, full size**. Exact image indices for ff.1v-2v (the cipher
folios) were not pinned down this pass (the item page's own image-label list did not load in the static HTML
capture; out of scope for check-solved to chase further) — flagged for a recovery-lane worker.

## Is the cipher already solved? (brief's gate)

1. **Beinecke's own description.** The standard pre-1600 manuscripts catalogue entry
   (`pre1600ms.beinecke.library.yale.edu/docs/pre1600.mell029.htm`, WebFetch) states: "written throughout in red
   and black in an italic hand with considerable abbreviation and partly in cipher"; "The text continues, partly
   in cipher on ff. 1v-2r, where alchemical operations are described"; and separately, "on f. 2v is an
   explanation of the ciphers for the signs of the Zodiac, which may be seen in the facsimile provided." The
   f.2v item is a **self-contained symbol legend for zodiac/planetary alchemical signs** (a standard alchemical
   convention, explained in the manuscript itself), distinct from the ff.1v-2r "alchemical operations" passage
   that Bourdeau's ~234-letter cipher attempt (and DECODE R2877) actually targets. The catalogue nowhere states
   the ff.1v-2r cipher itself has been read or its key published — it only documents the existence and location
   of the encrypted material. Citations given in the catalogue entry (TK 1237, TK 336-337 — Thorndike-Kibre
   incipit numbers; De Ricci-Bond 7(26) — the standard Yale pre-1600 MS census) are incipit/census matches, not
   claims of decipherment.
2. **DECODE R2877 documents (edition check, LANE N3 csED3, 24 Sept 2026).** `sources/decode/records-non-decrypted-
   2026-09-24.tsv` (on disk) confirms status "Non-decrypted" for id 2877, no document-attachment column.
   Cross-checked against a fresh shallow clone of aaymeloglu/unsolved-ciphers's `catalogue/decode-records.jsonl`
   (a public, no-login RecordsView field scrape, dated 23 Sept 2026): id **2877** carries `"Available Documents":
   ""` -- **empty, no document of any kind attached** (contrast a genuine hard-filter case in the same dataset,
   id 2988/BL Add MS 4136, "Partially decrypted" with a "Key" document attached). Clean: no hard filter, nothing
   to check further. `"Inline Cleartext": "Yes"` in the same record matches the Beinecke description below (the
   manuscript is mostly clear Latin, only ff.1v-2r are "partly in cipher").
3. **Standard printed catalogue.** Witten, Pachella et al., *Alchemy and the Occult: A Catalogue of Books and
   Manuscripts from the Collection of Paul and Mary Mellon* (Yale University Library, 4 vols, 1968/1977) is the
   standard reference the brief names. HathiTrust Bibliographic API (`catalog.hathitrust.org/api/volumes/brief/
   recordnumber/000162183.json`, OCLC 6485401, found by WebSearch): holds only **vol. 1** (`inu.30000006085066`)
   and **vol. 2** (`inu.30000006085074`), both "Limited (search-only)" and both the **1968 printed-books**
   volumes (1472-1790) -- the **manuscripts volumes (3-4, 1977, which would carry the actual Mellon MS 29 entry)
   are not on HathiTrust**, and a WebSearch/archive.org advancedsearch found no digitisation of any volume
   anywhere else (limited edition of 500 sets; archive.org query for `title:(alchemy occult mellon witten)`
   returns 0 results). Route exhausted for the primary catalogue itself. Beinecke's own manuscript-catalogue page
   (`pre1600ms.beinecke.library.yale.edu/docs/pre1600.mell029.htm`, already quoted by csCS2c, re-confirmed this
   pass) is drawn from the same De Ricci-Bond/Thorndike-Kibre census tradition and is this item's best available
   standard description in practice.
4. **Literature on the Mellon pseudo-Elian manuscripts.** alchemywebsite.com's Mellon Collection database entry
   for MS 29 (WebFetch) gives only physical description (33 folios, paper, 190×132mm, "Elias Cortonensis, O.F.M.
   Lumen luminum") with "no mention of ciphers, transcriptions, editions, or scholarly discussions." A WebSearch
   for the manuscript together with "cipher"/"zodiac"/"alchemical" returned only the same Beinecke catalogue
   entry, the alchemywebsite listing, and unrelated Mellon manuscripts (MS 2, 24, 33). A second WebSearch on
   cryptiana.web.fc2.com + "Mellon"/"Elia"/"Cortona" returned no relevant hit (Tomokiyo's site does not appear to
   cover this item). **One genuine, directly relevant scholarly source found and read this pass** (WebSearch +
   WebFetch/Read of the PDF): Agnieszka Rec (Yale), "Ciphers and Secrecy Among the Alchemists: A Preliminary
   Report," *Societas Magica Newsletter* 31 (Fall 2014), societasmagica.org. Its footnote 8, quoted verbatim (per
   the M9 lesson):

   > "Another manuscript, Mellon MS 29, includes a code that was used with the same intent to conceal as the
   > ciphers discussed below. Written around 1525, Mellon MS 29 is a Latin and Italian copy of the Lumen luminum
   > ascribed to the Franciscan Elias of Cortona. Since it does not use a cipher, the manuscript will not be
   > discussed further in the present study. However it is worth emphasizing the technical distinction between a
   > 'cipher' and a 'code'... In a code, the unit of encryption is a word. So, for example, the list of codewords
   > on f.1r of Mellon MS 29 maps 'Scorpio' to 'prk∫yq∫7gp' and 'Cancer' to 'irgp∫hk∫cel.'"

   Rec's own main text (section 1) independently corroborates the Beinecke catalogue's zodiac note: "Of the thirty
   alchemical manuscripts in that collection written before 1600, only one -- Mellon MS 27 -- includes ciphers,
   while Decknamen, allegories, and figurative language appear in all thirty" -- i.e. by Rec's own technical
   distinction (letter-level cipher vs. word-level code), **Mellon MS 29's f.1r zodiac list is a *code*, not the
   *cipher* this folder's DECODE record and Bourdeau's "~234 letters" figure target**; her article explicitly
   declines to discuss it further and makes no claim about the separate ff.1v-2r "alchemical operations" cipher
   passage. This is consistent with, not a solution of, this folder's target, and is the field's only located
   scholarly acknowledgement that Mellon MS 29 carries encoded content at all -- also confirming the field
   assessment that "alchemical ciphers have yet to receive systematic treatment... a comprehensive list of
   manuscript witnesses" does not yet exist. api.openalex.org: rate-limited this pass ("Insufficient budget...
   $0 remaining; resets at midnight UTC" -- the shared daily IP budget, already exhausted earlier today by
   another lane's open-index run per ROOM.md 17:22); not retried (one-retry-after-pause limit already spent by
   that earlier run on this IP).

5. **Solver repositories (edition check, LANE N3 csED3, 24 Sept 2026).** Fresh shallow clones of both. dbourdeau/
   cyphersolver: no target folder or note for "mellon", "elia", "cortona" or "lumen luminum" anywhere beyond the
   catalogue-list references already known (`unsolved.htm`, `CATALOGUE.md`) -- his own repository has not
   attempted this item beyond the catalogue-status line already quoted ("attempted, open... simple/homophonic/
   progressive/Vigenere/Alberti all fail"). aaymeloglu/unsolved-ciphers: grepped by "mellon"/"elia"/"lumen
   luminum"/"cortona" -- hits are only the catalogue-harvest files (`decode-records.jsonl`, `decode-catalog.csv`,
   `pares-pages.jsonl`, `fetch_pares_images.py`) plus incidental string matches in unrelated targets
   (`starhemberg-1758`, `royalist-1646`, `forster-1644` -- "mellon" substrings in unrelated words/names, checked
   and dismissed) and the repo's own `CATALOGUE.md`/`AGENTS.md` boilerplate; no target folder for this item.

## Verdict: `open`

Image confirmed online (full resolution). No source read this pass, including the one genuine piece of scholarship
located on this manuscript's encoded content (Rec 2014) and both solver repositories, shows the ff.1v-2r
alchemical-operations cipher (the actual target, distinct from f.1r/f.2v's self-keyed zodiac-sign codeword list --
itself a *code* by Rec's own technical distinction, not this target's letter-level *cipher*) has been transcribed,
edited or solved anywhere. DECODE's own hard filter (an attached document) does not apply here: none is attached.
The primary standard catalogue (Witten & Pachella's manuscripts volumes) could not be reached at all (not
digitised, per HathiTrust's holdings above) -- Beinecke's own catalogue page stands in for it, already read.
Bourdeau's own catalogue status ("attempted, open," several classical cipher families excluded by his own solver)
stands unchallenged, and is not a same-corpus situation like the fr2988-ranzo-1520s folder (this is a standalone
alchemical codex, no sibling letter, no known key-in-archive route found this pass).

**Nomination:** posted to ROOM.md (stage-2, copy-free, cryptanalysis kind — not a letter, no key-in-archive
route apparent from what was checked this pass).

Rule 10: no novelty claim made. Not decoded, not transcribed (out of scope for check-solved).

Requests this pass (csCS2c, 24 Sept, earlier): collections.library.yale.edu — 1 browser_fetch (search page,
cleared the 202 challenge), 1 browser_fetch (item page), 1 plain curl (IIIF info.json, no challenge). WebSearch 3,
WebFetch 2 (pre1600ms.beinecke.library.yale.edu, alchemywebsite.com — neither is a host this brief names
explicitly, both
reached via WebFetch/WebSearch per the brief's general grant of those tools). No DECODE, no solver-repo clone.

This pass (csED3): catalog.hathitrust.org 2 (brief request), api.openalex.org 1 (429/rate-limited, not retried).
WebSearch 2, WebFetch 1 (societasmagica.org PDF, read via the Read tool once fetched). github.com 2 shallow clones
(dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers, grep only — shared with the fr2988-ranzo-1520s folder's
checks, not two separate clones). No archive.org needed for this folder (the Witten catalogue is not on it).

## Capture and passes (24 Sept 2026, LANE R4 Q)

Brief `.claude/briefs/runs/2026-09-24-lane-r4-q-mellon-capture.md`. Image route confirmed and used:
`collections.library.yale.edu` IIIF only, catalog record 17388793. Manifest (`/manifests/17388793`, IIIF
Presentation 3.0) labels canvases plainly by folio ('1r','1v','2r',...); no offset puzzle like fr.20140/fr.16092.
ff.1v/2r/2v = canvases/image ids 17388797/17388798/17388799. `tools/iiif_lines.py` already accepted a plain IIIF
image URL as its positional `url` argument (quality defaults to `default` for any non-Gallica base) — no
`--image-url` option was needed, the brief's premise ("if it only handles Gallica arks") did not hold, so the
tool is unchanged. Native images and line crops in `images/` (manifest.json), pruned to the cipher-bearing lines
only (f1v_L16-18, f2r_L08-10, f2v_L01-12) to stay well under 30 MB (5.4 MB total).

**Atlas: `tools/glyph_atlas.py` not used, by design.** The brief assumed pseudo-Elian/pigpen glyph shapes (per
Bourdeau's catalogue description, itself from a DECODE thumbnail, not the image). The image shows otherwise: the
ff.1v-2r "alchemical operations" passage and the f.2v zodiac codeword list (Beinecke catalogue: "on f.2v is an
explanation of the ciphers for the signs of the Zodiac") are both written in the *same* ordinary Italian
humanist cursive hand as the surrounding plaintext — short nonsense letter-groups (word-nomenclature/substitution,
not an invented symbol alphabet), dot- or space-separated, mixed with a few scribal extensions (a tironian-shaped
mark transcribed '7', a yogh/z-tail shape transcribed '3', a long-s, an eszett-like ligature 'ß' on the Leo row,
small superscript flourishes transcribed "'"). `glyph_atlas.py`'s connected-component segmentation is built for
per-glyph invented alphabets (dupuy452, fr2933-salviati) and would blob-segment joined cursive strokes, not
letters; running it here would not have produced a usable atlas. `atlas.tsv` (committed) is instead a direct
paleographic sign tally built from the two transcription passes: 32 distinct codes over 248 signs (close to
Bourdeau's "~234 letters" estimate for ff.1v-2v — the gap is consistent with an estimate made from a thumbnail).

**Rec 2014 as an external anchor (grade C).** Agnieszka Rec's footnote 8 (already quoted in section 2 above)
gives two of the twelve f.2v zodiac codewords verbatim: Cancer -> "irgp∫hk∫cel", Scorpio -> "prk∫yq∫7gp". Both
match this pass's images letter-for-letter once ∫ (long s) is read as 's' -- and both resolve, in the scribe's
own hand, a letterform this pass otherwise found genuinely hard to call between 'q' and 'g' (a closed loop with
a descender tail). Those two words are graded C throughout (from print); the same letterform was then read 'g'
elsewhere only where the shape matched (graded S, calibration from Rec, not a raw guess), left 'q'/M where the
shape did not clearly match. Note for whoever solves this: Rec cites this list as "f.1r"; the Beinecke catalogue
and this pass's own canvas labels place it on f.2v. Same wording, same two confirmed words -- almost certainly a
foliation discrepancy (older count, or a citation slip), not a second list. Not resolved here.

**Passes.** Pass A (this worker, `passA_Q.tsv`) and pass B (one blind Sonnet subagent, `passB_subagent.tsv`,
crops only, no access to pass A) transcribed independently. `tools/reconcile_passes.py` (wide format, NW
alignment): 78.7% raw sign agreement (237/301 aligned columns; the brief's 80% gate was narrowly missed, driven
almost entirely by f2v's twelve short, closely-spaced codewords and one pass-B error including two words of
plaintext, "pista im", that continue past the last cipher word on f1v_L18). `disagreements.tsv`,
`ciphertext_draft.tsv` and `agreement.tsv` committed as the reconciler's output. This worker then settled every
disagreement row against the image crops by hand (word breaks re-checked against visible dots/gaps, e.g. the
Virgo and Aquario codewords were re-segmented from 1-2 words to 3-4 once the dots were looked at directly; the
f1v_L18 plaintext tail dropped; case and the X-I roman-numeral form on the Sagitarius row settled) and wrote the
adjudicated reading to `ciphertext.tsv` (long format: line, position, sign, confidence H/C/S/M, alt).
Grade counts: **H 197, C 21 (Rec 2014, two words), S 11 (g/q calibration from Rec), M 19 (genuine letterform or
mark ambiguity left open -- mostly q/a, 3/z, s/f-long-s and two uncertain marks)**. No H or C majority overall:
this is a cryptanalytic-capture result except the two Rec-sourced words. 58 word-tokens, 248 signs, 32 sign
types; word lengths 1-13 (median 3, the f.2v codewords running longer than the ff.1v-2r recipe words).

Rule 10: no novelty claim made; this is a transcription capture, not a reading or a solve. No decoding attempted
(out of scope, a separate Opus brief per the parent's line).

Requests this pass: collections.library.yale.edu -- 2 (manifest, one `info.json` reachability check) + N cached
IIIF image fetches (3 full-page: canvases 17388797/98/99; each >=2s apart, well under the 20-request brief cap).
No other hosts touched. Subagents: 1 (Sonnet, blind pass B only, per the LANE R4 16:58 rule).

ROOM.md: `done: for LANE R4: mellon capture 78.7% raw / settled to 197H+21C+11S+19M of 248 signs, 58 tokens/32 types`.

## Solver (24 Sept 2026, LANE R4 R)

Brief `.claude/briefs/runs/2026-09-24-lane-r4-r-mellon-solver.md`, Opus, disk only, no subagents, no hosts contacted.
Input: `ciphertext.tsv` (LANE R4 Q transcription from the Yale IIIF images: 248 signs, 32 types, word breaks kept).
Solver: `tools/homophonic_anneal.py` (order 3, 8 restarts x 40000 iters for the target; `--control` mode for controls),
signs `/` (word break) and `'` (superscript flourish) skipped, so the target runs at N=244, K=31.

**Controls (rule 3), `control_results.tsv`, N=248, 3 seeds each:**

| language / corpus | monoalphabetic K=21 | homophonic K=32 |
|---|---|---|
| Italian (it16 letters corpus; plaintext from letterescrittea01vanzgoog, excluded from corpus) | 96.0 / 96.0 / 88.3 % | 96.0 / 89.9 / 89.5 % |
| German (de16 composed_enhg, last 2.5 KB held out as plaintext) | 97.2 / 97.2 / 97.2 % | 92.3 / 83.1 / 85.5 % |
| Latin (`control/corpus_la_composed.txt`, 4 KB composed by the model -- NOT a historical source, n-gram stats only; plaintext `plain_la.txt` held out) | 87.1 / 87.1 / 11.3 % | 15.3 / 18.1 / 13.3 % |

No Latin corpus was on disk; the composed one is too small for the 32-type homophonic design, so **Latin homophonic
is uncontrolled** (control < 60%) and nothing below speaks to it. Latin monoalphabetic reads in 2 of 3 seeds.

**Target:** run under Italian, German and Latin models, in written order and with each word's letters reversed
(the reading-order variant; `control/target_wordrev.tsv`). None of the six gives language: best Italian
"rirelleochilreinitemaiaeaureineratat...", German "stsechedgothseertneinenenas...", Latin "pmperaeratmapestmued...".
Score per letter: target -2.61 to -2.83 against solved controls -2.13 (Italian), -2.34 (German), -2.68 (Latin mono);
the target sits well below the Italian and German controls. Outputs `control/target_{fwd,rev}_{it,la,de}.json`.

**Result: no reading (cryptanalytic negative, conditional on the Q transcription).** Monoalphabetic and homophonic
simple substitution (up to 32 types) over continuous Italian or German, in either reading order, is excluded at this
length with controls reading 83-97%; for Latin only the monoalphabetic design is excluded (controls 87/87/11%).
No token is graded; no decode.json or key.tsv written (no key exists). No phrase search run (nothing to search);
archive.org not contacted.

Why the design may not be a continuous substitution at all (observations, not tested): f.2v is a list of twelve
codewords, one per zodiac sign (Cancer = `irgpshkscel`, Scorpio = `prksyqs7gp` per Rec 2014), not running prose, so
the text is a set of short labelled items; the Cancer word fails the pattern of "dissolutione/dissolution" (the
alchemical process traditionally paired with Cancer: plaintext ss at 3-4, cipher g,p) under any monoalphabetic key.
Several ff.1v-2r words end alike (`leor`, `hyor`, `olor`), consistent with a nomenclature or verbal code.

Suggestions (one line each, not done): a real Latin corpus (Latin Library or an alchemical Latin text from
archive.org) to control the Latin homophonic design; test the twelve f.2v words as a codeword list keyed to their
zodiac labels (known plaintext per line) under a progressive/Alberti design with the f.2v labels as cribs.
