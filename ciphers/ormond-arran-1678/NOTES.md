open
HMC *Calendar of the Manuscripts of the Marquess of Ormonde, N.S.*, vol.4 (archive.org `calendarofmanusc04greauoft`)
pp.92-108 read in full by this worker (the letter itself, its index entry, and every neighbouring cipher item in
the same run of pages), a full-text search run across all of archive.org for the letter's own "trial whether you
are skilful in deciphering" sentence, and Tomokiyo's cryptiana page (`charlesii2.htm`, on disk) read in full,
including an unpublished HTML-comment note showing he already tried the nearest candidate key and rejected it —
none finds a decipherment.

## Check-solved (LANE CX, 25 Sept 2026)

1. **The edition itself, read in full at the page.** Fetched `calendarofmanusc04greauoft_djvu.txt` (1 request) and
   read pp.92-108 directly (not just the index). The target letter (Ormond to Earl of Arran, dated in the
   calendar "1677-8, January 24") begins on p.92 and its ciphertext falls on **p.93**, exactly as transcribed in
   `ciphertext.txt`: "If what he says of 445 and 342, be true 726 91 33 425 93 57 384 54 700 720 but it seems 732
   573 526 32 643 214 55 440. This is a trial whether you are skilful in deciphering, else it might have been
   written in plain letters." (one apparent OCR slip in this worker's own archive.org fetch, "58" for the ninth
   group, resolved against Tomokiyo's independently-keyed transcription of the same passage below, which agrees
   with our file's "57" — not changed here, flagged for the image check). No decipherment, gloss, or footnote
   accompanies this passage in the calendar.
2. **The neighbouring pages, read for contrast.** The same run of pages contains three *other* cipher passages in
   the Ormond circle's 1677-8 correspondence that the calendar's editors evidently *could* gloss when a period key
   or interpolation survived: p.94 area, Feb letters mention "this cipher... betwixt us"; pp.105-106 (Arran to
   Ormond, 9 Feb 1677-8) uses a two-letter name/place code with the plaintext interpolated in brackets ("hm [D.
   Bucks]", "dk [Court]", "4o [King]", "cf [change]"); p.107 footnote states explicitly "The equivalents for the
   words in cipher in the original are interpolated in Ormond's [own] handwriting" (i.e. a contemporary
   decipherment survives in the manuscript itself for *that* letter, which the calendar's editors then printed).
   **No such interpolation exists for the p.93 passage** — the calendar's own practice of printing a period gloss
   when one survived in the manuscript, demonstrated on both sides of it, makes its absence here informative: no
   contemporary key for this specific passage is recorded to have survived.
   The volume's own index confirms only two cipher passages total: `"Cipher, letters partly written in, 93,
   105-6."` — nothing else in this volume.
3. **Full-text search, archive.org-wide, with a control.** `be-api.us.archive.org/fts/v1/search` for the exact
   phrase "trial whether you are skilful in deciphering" (1 request): 3 hits total, all three the *same* HMC
   volume under three different digitisations/reprints (`calendarofmanusc04greauoft` itself; `cu31924091754063`,
   Cornell's own scan of the identical calendar; `reports-from-commissioners_1906_62`, the same report reprinted
   in the Parliamentary sessional papers series). No independent discussion, reprint, or decipherment of this
   passage exists anywhere in the Internet Archive's full-text index outside the calendar's own three copies. This
   is the control: the search engine returns real hits (the source volume, under all its digitisations), so a
   miss elsewhere is a genuine negative, not a broken query.
4. **Tomokiyo, cryptiana `charlesii2.htm` — the specific letter is directly discussed, quoted verbatim per
   LESSONS.md's rule.** The page's "Marquis of Ormond's Correspondence" section covers several reconstructed
   Ormond-circle nomenclators (Ormond-Anglesey 1663-4; the Arran-to-Ormond two-letter code of 9 Feb 1678, p.105,
   reconstructed from the manuscript's own interpolations noted above; three "Ormond-Longford" ciphers of 1680-83).
   Under the heading **"An Unidentified Cipher?"**, Tomokiyo writes, quoted verbatim: *"The cipher in undeciphered
   segments in a letter from Ormond to Arran, 24 January 1678 (vol.4, p.93), looks similar to this [the
   Ormond-Longford Cipher 1 just described], but seems different."* He then quotes the identical ciphertext this
   target already has on file. Rendered on the live page this stops there (matching the prior sweep's summary,
   "look similar... but seems different"); the underlying HTML file on disk carries an **unpublished working note
   in an HTML comment** (not shown on the rendered page) recording that Tomokiyo actually tried the Ormond-Longford
   Cipher 1 key against this passage. Decoded from Shift-JIS and translated: *"Even applying the above [key], it
   does not read. Also, since the frequently-occurring symbols do not overlap [with the key's high-frequency
   assignments], it seems to be different [a different cipher]."* His draft partial substitution (445→lo/London
   area, 342→hi/Halifax, a few single letters guessed, several positions left as bare placeholders) does not cohere
   into readable text. **This worker did not run or repeat this test — it is Tomokiyo's own prior, unpublished
   attempt, read from the on-disk snapshot, not fresh cryptanalysis by this worker**, and it directly explains
   Bourdeau's parallel note below.
5. **Bourdeau's `TARGETS.md` (dbourdeau/cyphersolver), fresh shallow clone, grepped.** Row 7: `"Ormond → Arran, 24
   Jan 1678 (HMC Ormonde iv. 93) | 1678 | 20 groups of a nomenclator | Only if the Ormond–Longford design applies |
   too short; not attempted."` Same shelfmark, date, page and group count as this target; the "Only if the
   Ormond-Longford design applies" caveat matches Tomokiyo's own framing above almost exactly, and Bourdeau states
   plainly he has not attempted it (unlike Tomokiyo, whose comment shows he did try and reject that same design).
   His `ormonde/` solved-target folder is a *different* item (Ormonde-Maltravers, 1634-35) with no reference to
   Arran or 1678.
6. **Aymeloglu (aaymeloglu/unsolved-ciphers), fresh shallow clone, grepped.** No whole-word hit for "ormond" or
   "arran" anywhere in the repository, including `CATALOGUE.md` and `SHORTLIST.md` — not listed at all.
7. **DECODE.** `sources/decode/*.tsv` (the cached record listings on disk) grepped for "ormond"/"arran": no hit.
8. **Community lists / general web.** Two WebSearch queries (`"Ormond" "Arran" cipher 1678 "HMC" OR "Kilkenny
   Castle" deciphered`; `Ormond Arran 1678 cipher "20 groups" OR nomenclator solved Cipherbrain OR Cryptiana`) and
   one Cipherbrain-specific query (`Klaus Schmeh Cipherbrain "Ormond" cipher Kilkenny Restoration`): no independent
   discussion or claimed solve found anywhere. **Flag:** the second query's own results surfaced this repository
   (`github.com/NoAutopilot/cipher-lab`) as a public, search-indexed hit describing this very target — noted for
   the orchestrator, not acted on by this worker (out of scope: no repo-visibility changes named in this brief).

**Verdict: open, stage 2 verified unsolved.** The standard edition is read at the page by this worker (not
quoted from a summary), a controlled archive-wide full-text search is run and returns only the edition's own
copies, and the one named specialist source that discusses this exact letter (Tomokiyo) is quoted verbatim and
shown to have already tried the nearest candidate key without success. Not "new"; not "unpublished" (rule 10) —
Bourdeau's catalogue already lists this item, unattempted; Tomokiyo already tried and rejected one key. Below
unicity distance (about 20 code groups) remains the operative constraint per the prior assessment; no sibling
letter in the *same* key has been found (the two nearby cipher letters at pp.102-107 and 105-6 are confirmed
different systems). **Next, for a future cryptanalysis worker (not this one):** the two other Ormond-Longford
reconstructed keys on `charlesii2.htm` (Cipher 2, vol.6 p.xix; Cipher 3, vol.7 p.xx) are not recorded as tried by
Tomokiyo against this passage and are the cheapest untried step, followed by an image check of the "57"/"58"
digit discrepancy noted in point 1.

Requests this pass: `archive.org`-family 2 (the calendar's own `_djvu.txt`; `be-api.us.archive.org/fts/v1/search`),
`github.com` 2 (fresh shallow clones of both solver repos, shared with this batch's other targets), WebSearch 3
queries. No subagents, no images, no logins, no key testing.

# Ormond to Arran (24 January 1678)

- **Source:** Calendar of the manuscripts of the Marquess of Ormonde, vol.4, p.93. Short undeciphered segments in a letter from the Duke of Ormond to the Earl of Arran.
- **Status:** Open. Note that the calendar text itself says "This is a trial whether you are skilful in deciphering, else it might have been written in plain letters."
- **Transcription:** `ciphertext.txt`. Numbers up to 732 embedded in cleartext.
- **Background page:** `sources/cryptiana/web/charlesii2.htm` (other Ormond and Arran ciphers, which look similar but seem different).
- **Ideas:** Only about 20 code groups, too few for statistical attack. Best route is to compare against the known Ormond-Arran keys in charlesii2.htm and test partial matches. Also check Daniel Bourdeau's site (dbourdeau.github.io/cyphersolver), who solved the 1634-35 Ormonde-Maltravers cipher in September 2026.
- **Solver status (19 Sept 2026):** Not attempted by either project beyond noting it is about 20 groups written as a test. Below unicity. Needs another letter in the same cipher.
