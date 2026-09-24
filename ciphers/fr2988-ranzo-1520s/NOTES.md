open

**LANE N3 orchestrator, 24 Sept 2026 18:03 UTC:** open, but not a separate nomination: same Ranzo corpus as ciphers/fr3022-garbino-1528 (Bourdeau pooled both); the recovery/cryptanalysis lane should treat them as one target.

**Edition check (LANE N3 csED3, 24 Sept 2026 18:xx UTC):** hold lifted -- verdict `open`, but **same key/corpus as
CS2-01 (`ciphers/fr3022-garbino-1528`), already on the board -- do not open a second board slot for this folder.**
Calendar of State Papers Venice vols III (1520-1526) and IV (1527-1533), full text, and Marino Sanudo's *I Diarii*
vol. XLIII (1 Oct 1526 - end Jan 1527, bracketing the one hard date in this volume's contents note), full text, all
read on archive.org; none names Ranzo. DECODE record documents and Aymeloglu's repository checked (below).
Bourdeau's own repository shows he already transcribed this exact letter as part of his combined Ranzo/no.20
corpus. Section 2 below. Brief `.claude/briefs/runs/2026-09-24-lane-n3-csED3.md`.

# Hieronimo Ranzo (Venice) cipher letters, 1520s — BnF fr. 2988 ff.9r-11v

QUEUE row: CS2-15 (`sources/solver-diffs/2026-09-24-cyphersolver-site.tsv`, LANE N3 scout scCS2, 24 September
2026 — catalogue item 170 at dbourdeau.github.io/cyphersolver/catalogue.html), DECODE R1894. Check-solved run
24 September 2026 by LANE N3 csCS2c (session_0113dPptSGXZiBF5uwvtKmtc), brief
`.claude/briefs/runs/2026-09-24-lane-n3-csCS2c.md`.

## What it is

Bourdeau's catalogue: "attempted, open (same initial-letter+number code as CS2-01/Garbino letter; non-alphabetical
numbering; annealer recovers only function words)." Two items headed "Lettre en chiffre de « V° HIERONIMO RANZO »"
appear in the fr.2988 recueil (items 1 and 3 of the volume's contents, per the BnF catalogue note below);
Bourdeau's ff.9-11 citation and DECODE R1894 point at this same pair. Prior scout pass (24 Sept 2026) marked the
image route "likely on Gallica; ark not confirmed" and the row "copy-order (unconfirmed, check Gallica fr.2988)."

## Image route (confirmed copy-free, this pass)

Gallica SRU (`dc.type all "manuscrit"` scoped to "Français 2988") returns two digitisations of the same
shelfmark (one "from the original document," one "from a substitute document," both giving identical catalogue
text) — used the original-document one, ark `btv1b525240150`. IIIF manifest (278 canvases) carries real foliation
labels for this volume (not "NP"): canvas index 24 = "9r", 25 = "9v", 26 = "10r", 27 = "10v", 28 = "11r", 29 =
"11v" (Gallica view numbers f25-f30). info.json for f25: 4298×5845, level2 profile, full resolution. **Image is
online now, full size, folios pinned exactly** (no eye-checked anchor needed — this manifest, unlike fr.15564,
carries genuine per-canvas foliation).

The BnF catalogue's contents note for fr.2988 (read via the same SRU record) lists, among ~56 items: "1 Lettre en
chiffre de « V° HIERONIMO RANZO » ; 2 « Double de lettres escriptes en chiffre par NICOLAS RAINCE,... De Romme,
XVme decembre V.C.XXVI [15 Dec 1526] » ; 3 Lettre en chiffre de « V° HIERONIMO RANZO » ; 4 «Proposition de la
majesté imperiale...1546»..." Items 1 and 3 (Ranzo's own cipher letters) flank item 2, Nicolas Raince's "double"
(copy) of separately-enciphered letters dated Dec 1526 from Rome — **these are catalogued as three distinct
items, not one continuous correspondence**; nothing in the catalogue note states item 2 is a decipherment of
items 1 or 3. No recipient is named for Ranzo's letters (items 1, 3) in this note.

## Same correspondence/key as CS2-01? (brief's question) -- yes, and already merged by Bourdeau himself

Bourdeau's own catalogue entry for CS2-15 states "same initial-letter+number code as CS2-01/Garbino letter"
(CS2-01 = BnF fr. 3022 no. 20, Hieronimo Ranzo(?) to "Garbino," 11 Apr 1528, ff.44r-46v). Checking his working
folder directly (fresh shallow clone of dbourdeau/cyphersolver, 24 Sept 2026, `vasto1527/NOTES.md`) goes further
than "same system": **he already transcribed this exact letter and pooled it into his no.20 corpus**:

> "Ranzo's signed letters, BnF fr. 2988 ff. 2r-v, 9r-10v (ark btv1b9059908w, views 6, 7, 17-20) | ~2,600 [groups] |
> `n20/ranzo_c0*.txt`, transcribed by six subagents. f. 2v is marked "dup.a" (duplicate)."

and, citing the DECODE record directly:

> "DECODE R1894 (catalogue entry 170), 21 Sept 2026. The record 'BNdF AncienFonds invnr.2988 ff9-11' (Ranzo,
> Italian, 4 pp., dated 1520 by BnF's 1520-29 range) is the fr. 2988 Ranzo letter already transcribed above.
> The record has no key, decipherment or transcription. Nothing new was attempted, and the entry is marked
> 'attempted, open' in the same state as no. 20."

So this folder's target (fr.2988 ff.9r-11v, DECODE R1894) **is** one of the two Ranzo cipher items Bourdeau already
folded into the combined ~3,900-group corpus that LANE R4 worker N's control-first cryptanalysis note (ROOM.md,
17:10) already accounts for under `ciphers/fr3022-garbino-1528` ("Bourdeau's best: 46% token / 9% type at ~3,900
pooled groups"). **Recommendation: do not nominate this folder as a separate stage-2 board slot.** Either fold this
folder's content into `ciphers/fr3022-garbino-1528/NOTES.md` as a sibling-source section, or keep it as a
reference folder cross-linked from there, but any future recovery/cryptanalysis pass should work the pooled
corpus once, not attack fr3022 and fr2988 as two unrelated targets and double the cost.

**Ark discrepancy, flagged not resolved (Gallica is not a host this brief grants):** Bourdeau's ark for fr.2988 is
`btv1b9059908w` (views 6, 7 = f.2r-v; 17-20 = f.9r-10v), confirmed by him against real transcribed content. The
prior csCS2c pass in this folder used a **different** ark, `btv1b525240150`, inferred only from IIIF canvas
foliation labels, never checked against page content. Gallica documents "two digitisations of the same shelfmark"
(original vs. substitute); these may be the same two, or one may be wrong. A recovery-lane worker must confirm
which ark actually shows Ranzo's cipher before capturing images -- do not assume csCS2c's ark is correct just
because its foliation labels lined up.

f.2 itself is also its own DECODE record (R2294, "Français 2988, f.2", Non-decrypted, see below) -- so "item 1"
of the BnF contents note (the first "Lettre en chiffre de V HIERONIMO RANZO") is very likely f.2, distinct from
"item 3" (this folder's ff.9-11), consistent with Bourdeau transcribing both as one Ranzo set.

## Date (brief's question: date from the clear parts and Bourdeau's notes)

No exact date is established for ff.9r-11v specifically -- grade I (inferred), not H or C. What is known:

- DECODE's own two records for this item give only decade brackets: R1894 "1520-1529" (BnF's own range per
  Bourdeau's quote above), R2295 "1520-1540".
- The BnF contents note (section "Image route" above) catalogues Ranzo's two letters (items 1, 3) flanking
  Nicolas Raince's "double" of Dec 1526 letters (item 2) -- a shelving/binding order, not proof the Ranzo items
  are contemporary with Dec 1526, but consistent with it (recueils of this kind are often bound in roughly
  chronological blocks).
- WebSearch (this pass) on the Gattinara family: Girolamo/Hieronimo Ranzo appears in Piedmontese archival material
  on the Arborio di Gattinara family (ASVercelli finding aid; aggregated search snippets, not independently
  fetched against a citable primary text this pass -- flag as unverified) as a relative of Chancellor Mercurino
  Gattinara, in his household, presenting accounts as his **chamberlain for 1524-1529**. This is consistent with,
  not proof of, a Ranzo cipher letter from within that decade.

Taken together (grade I): **c.1524-1529, most plausibly nearer 1526** (the Raince flanking date), is the best
available estimate, not an established date. On that basis this pass read the calendars for the full decade
(CSP Venice) and the sub-period bracketing the one hard date in the volume (Sanudo vol. XLIII), rather than a
single month, since no single month can be justified as *the* date.

## Six-source search log (24 September 2026)

1. **Tomokiyo / Cryptiana** (named source for this cipher family). WebSearch located Cryptiana content on
   Ranzo's system: "Document No. 20 from Madrid dated 11 April 1528 is in the initial-letter code of Hieronimo
   Ranzo, Gattinara's kinsman... Tomokiyo published a partial key and left two thirds of the first page unread.
   The key checks against the glosses (Guienne, tres confident, Fumé; adds 87 = e, 22 null, # = Roy de
   Navarre)." A second search confirms the same wording: "No. 20, from Madrid on 11 April 1528, is in the
   initial-letter code of Hieronimo Ranzo, Gattinara's kinsman. However, No. 20 needs Ranzo's table or a clear
   copy to be fully deciphered." **Both quoted passages describe CS2-01 (fr.3022 no.20, the Garbino letter)
   specifically, by date and archival number — neither names fr.2988 or an ff.9-11 item.** No sentence located
   anywhere (WebSearch, not the live cryptiana.web.fc2.com site directly, which was not fetched this pass)
   claims fr.2988 ff.9-11 itself has been read, partially or fully. Per the M9/Morvillier lesson (check-solved.md):
   this is quoted verbatim precisely because it is *not* a claim about this letter, to avoid the same overclaim.
2. **Standard printed edition / calendar (edition check, LANE N3 csED3, 24 Sept 2026).** No French royal/
   diplomatic series calendars an intercepted Venetian dispatch, so the calendar that covers this sender and
   period is the *Calendar of State Papers, Venice* (the standard English-language calendar for exactly this
   place/decade), read in full text on archive.org: vol. III pt.1, 1520-1526 (ed. Rawdon Brown, London 1869,
   archive.org id `calendarofstatep3118brow`, 30,723 lines OCR) and vol. IV, 1527-1533 (ed. Rawdon Brown, London
   1871, id `calendarofstatep4187brow`, 57,933 lines OCR) -- both grepped for "Ranzo" and "Ranz[oc]": **no genuine
   hit in either** (only false positives on the surname "Soranzo"); OCR quality confirmed usable by "Gattinara"
   (80 + 39 hits) and "Venice" (248 + 367 hits) counts, both far above chance. Marino Sanudo's *I Diarii* --
   vol. LIX (`idiariidimarinos59sanu`) is the edition's own 1903 "Indice Generale" (a volume/date map, not a name
   index: "XLIII / 1526, 1 ottobre - 1527, [end] Jan[uary]"), used to locate the volume bracketing the one hard
   date this folder has (Dec 1526, the Raince flanking item): **vol. XLIII** (`idiariidimarinos43sanu`, Oct 1526 -
   end Jan 1527, 66,559 lines OCR), fetched and grepped: **no genuine "Ranzo" hit** (only "Soranzo" false
   positives), OCR usable (373 hits for "venezia/venetia"). The other ~9 volumes covering the wider c.1524-1529
   window (vols XXXVI-XLII, XLIV-LI roughly) were not fetched this pass (58-volume edition, no exact date to
   narrow further, out of this pass's budget) -- flagged for whoever promotes this to a solver stage, though
   given a real hit in vol. XLIII specifically (bracketing the one hard date available) would have been the most
   likely single volume to carry one.
3. **DECODE R1894 documents.** `sources/decode/records-non-decrypted-2026-09-24.tsv` (on disk) confirms status
   "Non-decrypted" for id 1894 but carries no document-attachment column. Cross-checked against a fresh shallow
   clone of aaymeloglu/unsolved-ciphers's `catalogue/decode-records.jsonl` (a public, no-login RecordsView field
   scrape, dated 23 Sept 2026 by that repo's own git log -- confirmed public: `catalogue/fetch_decode.py`'s own
   docstring states "No login is used: the fields, including... 'Available Documents', are public"): id **1894**
   carries `"Available Documents": "Transcription"` (not Key or Decryption -- DECODE's schema distinguishes these,
   confirmed by a different record in the same dataset, id 2988/BL Add MS 4136, "Partially decrypted" with
   `"Available Documents": "Key"`, a stronger category). This is a hard filter per COMMON addition (c) and was
   checked, not skipped: a "Transcription" document is a raw ciphertext transcription, not a decipherment, and is
   fully consistent with Bourdeau's own 21 Sept note (quoted above) that "the record has no key, decipherment" and
   with his own independent transcription of this exact letter around the same date -- most plausibly the same
   transcription, or one like it. DECODE's own Status field ("Non-decrypted") is unchanged between the 24 Sept
   `sources/decode/` snapshot and the 23 Sept Aymeloglu scrape. **Conclusion: hard filter checked and cleared --
   a transcription exists, a decipherment does not.** The neighbouring f.2 item (id 2294, "Français 2988, f.2",
   also Ranzo per Bourdeau's combined-corpus note above) carries the same "Transcription" tag and the same
   reasoning applies. DocumentsList itself (the document's actual content) needs a DECODE login, which this
   brief reserves to the DECODE worker; not fetched.
4. **Solver repositories.** dbourdeau/cyphersolver (fresh shallow clone): covered fully above -- this letter is
   already transcribed and pooled into the no.20/Ranzo corpus, verdict "attempted, open," in the same unsolved
   state as CS2-01. aaymeloglu/unsolved-ciphers (fresh shallow clone, 24 Sept 2026): grepped by shelfmark
   ("2988") and name ("ranzo", "garbino") across the whole repository -- the only hits are the catalogue-harvest
   files already used in item 3 above (`decode-records.jsonl`, `decode-catalog.csv`, `pares-hits.jsonl`,
   `bne-records.jsonl`, none of which is a solve claim), and no target folder (`burgess-1912/`, `ferdinand-1634/`,
   `ferdinand-1635-1640/`, `forster-1644/`, `moray-1568/`, `ottobon-1589/`, `royalist-1646/`, `starhemberg-1758/`,
   `vande-perre-1653/`) touches this shelfmark or sender.
5. **General web / comment threads.** No further hit beyond the Tomokiyo/Cryptiana material in item 1 and the
   Gattinara-household material in the Date section above.

## Verdict: `open` (same key/corpus as CS2-01 -- see above; do not double-book the board)

Image confirmed online (full resolution, folios pinned exactly, ark discrepancy flagged above). CSP Venice
(both volumes covering the full 1520-1533 range) and Sanudo vol. XLIII (bracketing the one hard date available)
read in full text: no hit. DECODE's own hard filter (an attached "Transcription" document) checked and cleared --
it is Bourdeau's own transcription work, not a decipherment. No source read this pass, including both solver
repositories, claims fr.2988 ff.9-11 has been deciphered or its key recovered; the only published work on this
cipher *family* (Tomokiyo's partial initial-letter-code key) is explicitly about a different item (CS2-01/fr.3022
no.20) and is itself incomplete. **This is not a new target: it is unread material Bourdeau already folded into
CS2-01/fr3022-garbino-1528's corpus.** Flag for whoever next works the pooled corpus: try Tomokiyo's partial
Ranzo key (glosses in item 1 above) against this letter's ciphertext before any fresh cryptanalysis.

**Nomination:** posted to ROOM.md, marked explicitly as same-key-as-CS2-01 / no new board slot (see recommendation
above), not as an independent stage-2 candidate.

Rule 10: no novelty claim made. Not decoded, not transcribed (out of scope for check-solved).

Requests this pass (csCS2c, 24 Sept, earlier): gallica.bnf.fr SRU 1, manifest 1, info.json 1 (3-4 total). WebSearch
2. This pass (csED3): archive.org 5 (2 CSP Venice djvu.txt, 1 Sanudo indice djvu.txt, 1 Sanudo vol.43 djvu.txt,
1 advancedsearch), all >=1.5s apart, single fetcher (IA slot). github.com 2 shallow clones (dbourdeau/cyphersolver,
aaymeloglu/unsolved-ciphers, grep only). WebSearch/WebFetch: see the combined report in the Mellon-29 folder's
"Requests" line for the shared background-agent pass (Gattinara-household search, CSP Venice/Sanudo index probes --
that agent's own host counts are internal to its report, not separately billed to a brief host). No DECODE login.
