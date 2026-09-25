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

## YX-ORM (25 Sept 2026)

**Job:** recovery test -- apply Tomokiyo's three reconstructed Ormond-Longford keys (charlesii2.htm) to the target's
20 code groups, each against a matched control (rule 3). Keys and script: `keys/cipher{1,2,3}.tsv`,
`keys/apply_and_control.py` (also checks the tsv's 20 groups against `ciphertext.txt` and exits 1 if stale).

**Key provenance, corrected from Tomokiyo's page.** Cipher 2 and Cipher 3 are *not* Tomokiyo's own reconstructions
as his prose might suggest -- they are the **printed key tables in the HMC volumes themselves** ("Key to the
Cipher used in the Letters of the Earl of Longford to the Duke of Ormond", HMC Ormonde n.s. vol.6 p.xix-xxii and
vol.7 p.xx), supplied to the editor by a Mrs. Lomas who deciphered Longford's letters, and transcribed here in
full from `archive.org/download/cu31924091754089/cu31924091754089_djvu.txt` (vol.6, lines ~1188-2140) and
`.../cu31924091754097/cu31924091754097_djvu.txt` (vol.7, lines ~1291-1330) -- grade H throughout (read from a key
source per rule 4), a few OCR-ambiguous entries (e.g. vol.6 "268 kn", "357 wa" for "she"? left as printed) marked
M. This is a **published key** (Mrs. Lomas's, via the HMC editor), not ours -- key source = `published` if this
ever reaches an AUDIT.md. Cipher 1 (vol.5 p.454ff, 1680) has no printed table in either volume fetched this pass;
only Tomokiyo's own PNG image (not in this repo's `sources/` snapshot) shows the full reconstruction. `keys/cipher1.tsv`
holds only the 15 codes independently confirmed by the HMC editor's own worked example on vol.5 p.498 ("579[our]
446[letter] 64[s] 725[to] 566[Ormond] 86[ar] 27[e] 552[o] 582[pe] 59[n] 240[ed] 551[on] 736[that] 681[si] 206[de]",
quoted on charlesii2.htm) -- not a usable fraction of what is presumably an ~800-entry table, so the Cipher 1 row
below is not a real test of that key, only a placeholder showing why: those 15 confirmed codes happen to share no
value with the target's 20 groups. **Tomokiyo's own unpublished attempt to apply the *full* Cipher 1 key to this
exact target (HTML comment in charlesii2.htm, already logged above under Check-solved point 4) remains the only
real Cipher 1 test on record; not repeated by this worker.**

**Control (rule 3):** for each key, 1,000 random draws of 20 integers uniform in [32,732] (the target's own
observed min/max), scored for coverage against that key's defined codes, seed 1. This tests whether the target's
raw hit count is better than picking 20 numbers blind in the same range would do against that key's code density
-- not a null-cipher control (there is no ciphertext-design match for a ~20-group nomenclator fragment to
control against), but the rule-3 control the brief names for a coverage gate.

| Key | Source | Defined codes | Target coverage | Control mean (1000 draws) | Control 99th pctile | P(random >= target coverage) | Verdict |
|---|---|---|---|---|---|---|---|
| Cipher 1 (1680, vol.5) | Tomokiyo PNG, not on disk; only 15 confirmed codes here | 15 | 0/20 (0%) | 0.38 | 2 | not meaningful (see above) | not a real test -- insufficient key data |
| Cipher 2 (Longford, vol.6 p.xix, published/Lomas) | HMC vol.6 OCR, this pass | 328 | 5/20 (25%) | 6.38 | 11 | 34.9% | **negative** -- below the control mean |
| Cipher 3 (Longford, vol.7 p.xx, published/Lomas) | HMC vol.7 OCR, this pass | 37 | 3/20 (15%) | 1.01 | 3 | 7.8% | **negative** -- common by chance, not above the 99th pctile |

**Matched groups (for the record, not a reading -- coverage did not clear the control gate for either key):**
Cipher 2: 445=re, 33=i, 93=bring, 384=of, 32=h. Cipher 3: 445=um, 425=the, 440=Tyrconnel (the last plausible as a
name in this circle, but one hit in 20 with the other two matches contributing no coherent sense, and 8 of the
20 target groups -- 726, 700, 720, 732, 573, 526, 643, and borderline 342 -- exceed Cipher 3's own printed range
entirely, cap 445, which is itself close to a structural argument against this key independent of the control).

**Verdict: no key fits.** Neither Cipher 2 nor Cipher 3 clears "coverage above the control's 99th percentile and
the covered words read sensibly in context" (brief's gate); Cipher 1 cannot be tested with the data on disk, and
Tomokiyo's own full-key attempt (already on file) was rejected on a frequency-mismatch basis. This does not
change the target's status (`open`, stage 2 verified unsolved, unchanged from Check-solved above): a negative
against three named keys, one incompletely tested, is not a claim that no key exists. Not new, not first, not
previously untried in full (rule 10) -- Tomokiyo tried Cipher 1 himself; this worker adds a first documented test
of Cipher 2 and Cipher 3 against this specific passage, both negative.

**Next, for a future worker:** fetch `charlesii2_Ormond_Longford1.png` from the live cryptiana site
(cryptiana.web.fc2.com, not yet tried this pass, not in the good-citizen host table) to get Cipher 1's full table
and run a genuine coverage test for it; or treat this target as archived at "below unicity, three named keys
tried, no sibling letter found" until one turns up.

Requests this pass: `archive.org` 2 (`cu31924091754089_djvu.txt`, `cu31924091754097_djvu.txt`, one retry needed
on each for a 302 redirect, `curl -L`, >=1.5s apart, both >200KB text fetched once to disk and read from disk
after). No other hosts, no subagents, no logins, no credentials.
