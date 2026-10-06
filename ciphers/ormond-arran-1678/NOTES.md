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

## ZX2-ORM (25 Sept 2026, LANE ZX2)

**Job:** the full Cipher 1 key table (the 15-code placeholder in `keys/cipher1.tsv` replaced with a genuine
reconstruction), re-run of `keys/apply_and_control.py` with the control, and an Ormond/Arran 1677-80 sibling
sweep of HMC Ormonde N.S. vols 4-5 for other cipher-numeral passages.

**Cipher 1 full table.** Fetched Tomokiyo's `charlesii2_Ormond_Longford1.png` from cryptiana.web.fc2.com (1
request; credit Tomokiyo, rule 8) and transcribed all 162 defined code/gloss pairs (from 23 to 1063; one cell,
code 418, has no gloss printed and is omitted) into `keys/cipher1.tsv`. Grading convention (stated plainly since
it is this worker's own choice, not printed on the image): unbracketed glosses grade H (Tomokiyo states them
without a qualifier); any gloss in square brackets, or carrying a "?" or a "->"-marked alternate reading (e.g.
`[k]`, `ie or ca`, `l or le`), grades M. By that rule: 130 H, 32 M.
**Cross-check against the primary source (not just the image):** fetched `calendarofmanusc04greauoft_djvu.txt`
again (archive.org holds vol.4 *and* vol.5 bound in one item, metadata field `volume: 4-5`; 1 request, already
on disk from the earlier YX-ORM pass's neighbour volumes) and located the printed interlinear decipherment at
vol.5 pp.454-461 (Earl of Longford to Earl of Arran, 16 Oct 1680) that is very likely Tomokiyo's own source for
this table. Sample check: the printed line "The great **112 206 134 41**" decodes letter-by-letter under the
image's table to "affair(112) de(206) ba(134) t(41)" = "affair debat[e]", cohering perfectly with "The great
affair debate concerning..." -- strong independent corroboration that the unbracketed entries are correct, not
just internally consistent with Tomokiyo's own page. Per rule 2 (image over transcription) the image, not this
worker's own reading of the messy interlinear OCR, is what went into `cipher1.tsv`; the OCR was used only to
spot-check.

**Control test (`keys/apply_and_control.py`, unchanged script, updated key):**

| Key | Defined codes | Target coverage | Control mean (1000 draws) | Control 99th pctile | P(random >= target) | Verdict |
|---|---|---|---|---|---|---|
| Cipher 1 (full, this pass) | 162 | 6/20 (30.0%) | 3.79 | 8 | 14.8% | **negative** -- at/below the control's 99th pctile |
| Cipher 2 (unchanged) | 328 | 5/20 (25.0%) | 6.38 | 11 | 34.9% | negative (YX-ORM, unchanged) |
| Cipher 3 (unchanged) | 37 | 3/20 (15.0%) | 1.01 | 3 | 7.8% | negative (YX-ORM, unchanged) |

Matched groups (Cipher 1, full table): 33=e/l/s (M), 425=knave (H), 57=l (H), 54=h (H), 32=k (M), 55=i (M). In
context ("...726 91 **33** **425** 93 **57** 384 **54** 700 720 but it seems 732 573 526 **32** 643 214 **55**
440") the matches spell no coherent word or name in sequence (e/l/s-knave-?-l-?-h and k-?-?-i-?): not a reading.
Six of the eight target values above Cipher 1's own printed range (445, 342, 726, 700, 720, 732 all exceed the
key's highest defined code, 1063, is fine, but the *density* of definitions above 700 is much sparser: only
920/1039/1054/1063 are defined above 800, all place-name codes, none matching) is itself weak structural evidence
against this key, independent of the control, as already noted for Cipher 3 in YX-ORM.

**Verdict: still no key fits, now on a real test.** The Cipher 1 test that YX-ORM correctly flagged as "not a
real test -- insufficient key data" (15/~800 codes) is now a genuine one (162 codes spanning the target's full
observed range), and it is a clean negative: coverage does not clear the control's 99th percentile, and the
handful of matches do not cohere. This does not upgrade the target's status (`open`, stage 2, unchanged): a
negative against three named keys is not a claim that no key exists, and Tomokiyo's own unpublished attempt
(already on file, YX-ORM point 4) tried the *complete* table (his own working notes show a partial substitution
attempt, not just a coverage count) and reached the same conclusion by a different method.

**Sibling sweep (`siblings.tsv`).** Grepped the combined vol.4-5 djvu text for lines carrying 4+ short (2-4
digit) numeral tokens, across the whole item (100,100 lines). Real cipher-numeral passages cluster only in
pp.454-498 (the rest of the >2,000 matches past that range are the volume's own back-of-book page-number index,
not ciphertext -- checked and excluded). Found, beyond the target and the already-known p.498 worked example:
Longford to Arran 16 Oct 1680 (pp.454-461, ~230 groups by OCR count, unverified/approximate -- this passage is
almost certainly Tomokiyo's own source for the Cipher 1 table, since the editor prints an interlinear
decipherment above the numbers throughout); Arran to Ormond 30 Oct 1680 (pp.469-470, 57 groups, also printed
with an interlinear gloss -- and, per the author's own next letter of 20 Nov, transmitted with copying errors:
"I conclude the cipher is not well copied"); Arran to Ormond 13 Nov 1680 (pp.486-487, 16 groups, footnoted "The
equivalents of this cipher are in Ormond's hand, but scarcely legible" -- a *period* decipherment, not
Tomokiyo's reconstruction); and one short, genuinely print-undeciphered snippet, Arran to Ormond 20 Nov 1680
(pp.493-494, 6 groups: 267 379 734 34 71 59), which the letter itself offers as a legibility test case and which
scores 5/6 against `cipher1.tsv` (267=Essex H, 379=is H, 734=the H, 34=[m] M, 59=n H) -- too short (N=6) for a
meaningful control, not gated, reported as a curiosity only.
**None of this pools with the target.** All four sibling passages found already carry their own printed (or
manuscript-interpolated) decipherment; they are the *source material* the Cipher 1 key was built from, not
additional undeciphered ciphertext in the same system that could be pooled with the target's 20 groups for a
bigger-N cryptanalytic attempt. The target (Jan 1677/8) also predates the whole Cipher 1 cluster (Oct-Nov 1680)
by close to three years, consistent with Tomokiyo's own "looks similar... but seems different" framing and with
this pass's negative coverage result. No sibling in the target's *own* system was found.

**Novelty:** not classified by this worker (rule 10); a verifier session assigns the N-class. Not new, not
first, not previously untried -- Tomokiyo already tried the full Cipher 1 key by his own method (YX-ORM point 4,
unpublished HTML-comment note) and reached the same negative; this worker adds an independent, control-backed
coverage test of the same key, also negative, plus the sibling-letter search.

Requests this pass: `archive.org`-family 5 (`advancedsearch.php` 1, `metadata` 1, `be-api.us.archive.org/fts/v1/search`
2, `_djvu.txt` download 1 -- the two `be-api` calls were made back-to-back without the full 1.5s gap the
good-citizen rule asks for; no error resulted, flagged here rather than silently corrected after the fact);
`cryptiana.web.fc2.com` 1 (the key-table PNG). No logins, no credentials, no subagents (the transcription was
done directly from the image by this worker, not delegated, per the fan-out/subagent-sizing note in
RETRO-2026-09-25k proposal 1 -- a 162-cell single-image table read in one pass is well under the sign-count
scale that flagged GOLD-4D).

## Web and blog check (WEBCHECK-ormond-arran-1678, 2 Oct 2026)

The open-web and blog comment-thread step that `.claude/briefs/check-solved.md` requires (CHECK-SOLVED-WEB, 28 Sept
2026), run 2 Oct 2026 01:05-01:20 UTC by a WEBCHECK worker (account-4), brief
`.claude/briefs/runs/2026-10-01-account4-webcheck.md`. Nothing else was done: no transcription, no key test, no
decoding.

**Result: no decipherment or plaintext of this item located by these queries on 2 Oct 2026** (a search result, never
a novelty verdict, rule 10). The status word on line 1 stays `open`.

### (a) Plain web searches (WebSearch, 10 queries)

| # | Query | Result |
|---|---|---|
| 1 | `Ormond Arran "24 January 1678" cipher letter` (sender + recipient + date) | Wikipedia pages on the Butler earls of Arran and TNA Discovery catalogue rows (1667 Ormond correspondence). Nothing on this letter. |
| 2 | `"HMC Ormonde" OR "Marquess of Ormonde" vol. 4 p. 93 cipher 1678 Arran` (shelfmark + cipher) | Catalogue records of the calendar itself (Google Books `cmtnAAAAMAAJ`, NLI `vtls000131145`, HathiTrust `000274578`, an AbeBooks listing, TannerRitchie). No page content, no discussion of p.93. |
| 3 | `"trial whether you are skilful in deciphering"` (most distinctive clear-text phrase, quoted) | No result carries the phrase (dictionary and essay pages on "decipher" only). Consistent with the archive-wide be-api result in Check-solved point 3 above, where the only full-text hits are the calendar's own three digitisations. |
| 4 | `"Ormond to Arran" 1678 undeciphered cipher` (the folder's own descriptive title) | Wikipedia; `dbourdeau.github.io/cyphersolver/index.html` (opened, below); two forks of Bourdeau's repo, `github.com/arya1515/cyphersolver` and `github.com/setsunaatto/cyphersolver` (opened, below); a calligraphy page on undeciphered scripts. |
| 5 | `"Ormond" "Arran" 1678 "cypher" OR "cipher" Kilkenny Longford nomenclator deciphered` | Bourdeau's index again (Maltravers-Ormonde 1634-35 only); Wikipedia "1677 in Ireland"; two Cryptologia articles on cipher-key instructions and papal ciphers, neither about this letter. |
| 6 | `Ormond Arran 1678 cipher solves Claude OR GPT` (model-solve announcements, check-solved.md) | Only the Vals AI / Urquhart "Cyphral Distich" coverage (31 Aug 2026, a different cipher), the Kryptos K4 ChatGPT debunk gist, this repository's own GitHub page (`github.com/NoAutopilot/cipher-lab`, already flagged in Check-solved point 8), and `github.com/AlexFitzgerald47/cracking-problems-hub/pull/7` (opened, below). No announcement that any model read this letter. |
| 7 | `site:scienceblogs.de/klausis-krypto-kolumne Ormond Arran` | Nine Cipherbrain posts returned, none mentioning Ormond or Arran (Cointet pigpen, Top-25 list, RAF ciphers, Kryptos documentary, Henry II device, Cold War radio, a Caribbean telegram). |
| 8 | `site:cryptiana.blogspot.com Ormond Arran 1678` | The engine returned no page from that domain at all (Wikipedia only); the blog's own search was run directly instead (b, below). |
| 9 | `site:ciphermysteries.com Ormond Arran cipher` | Ten Cipher Mysteries posts returned (d'Agapeyeff, Somerton Man, Weldon, pigeon cipher, Cincinnati fence runes, ...), none mentioning Ormond or Arran. |
| 10 | `site:cipherbrain.de Ormond OR Ormonde OR Arran cipher` (Schmeh's current domain, in addition to the scienceblogs.de archive the brief names) | No page from that domain returned. |

### (b) Site searches of the three blogs by name

- **Cipherbrain** (`scienceblogs.de/klausis-krypto-kolumne/?s=Ormond`, 1 request): the blog's own search answers
  "Wir konnten leider keine Beiträge finden, die zu Ihrer Anfrage passen" (no posts match). The newer domain
  `cipherbrain.de/?s=Ormond` was also tried: HTTP 503 on the first request, then on the single permitted retry after
  a pause a TLS "internal error" alert (curl exit 35, status 000) -- unreachable from this container, not retried
  further (good-citizen rule). The on-disk Schmeh snapshot (`sources/schmeh/posts/`, `top50-scienceblogs.txt`) was
  grepped with zero requests: the only "arran" matches are substrings in unrelated words on the Roosevelt, Dorabella,
  Ferdinand III and Rayburn posts; no Ormond.
- **Cryptiana blog** (`cryptiana.blogspot.com/search?q=Ormond`, 1 request): exactly one post, "Duke of Ormond's
  Ciphers during the 1660s", 17 Mar 2024, `cryptiana.blogspot.com/2024/03/duke-of-ormonds-ciphers-during-1660s.html`.
  Opened (1 request) and its comment thread read: **0 comments** ("No comments:"). The post's full text is a notice
  that the "Marquis of Ormond's Correspondence" section was added to `charlesii2.htm` and that the 1663-64
  Ormond-Anglesey cipher follows the DECODE R433 template; it does not mention Arran 1678 or this passage.
  Tomokiyo's own pages: the on-disk snapshot `sources/cryptiana/` (downloaded 19 Sept 2026, additions 24 Sept) was
  grepped first with zero requests -- the only files naming this letter are `web/unsolved.htm`,
  `web/unsolved-2026-09-24.htm` and `web/charlesii2.htm` (all already read in full in Check-solved point 4 above; the
  Cryptiana blog HTML files on disk match "ormond"/"arran" only inside Blogger widget JavaScript, not in any post or
  comment body). The two live pages were then re-read once each (2 requests to `cryptiana.web.fc2.com`) to catch any
  update since the snapshot: `code/unsolved.htm` ("Last modified on 27 September 2026") still lists "An Unidentified
  Ormond-Arran Cipher (1678)" with the same twenty groups and no solution note; `code/charlesii2.htm` ("Last modified
  on 17 March 2024") still reads, under "An Unidentified Cipher?", verbatim: "The cipher in undeciphered segments in a
  letter from Ormond to Arran, 24 January 1678 (vol.4, p.93), looks similar to this, but seems different." No
  decipherment on either page.
- **Cipher Mysteries** (`ciphermysteries.com/?s=Ormond`, 1 request): five posts returned, every hit the steamship
  "SS Ormonde" in the Somerton Man passenger-list posts (11 Jan 2020, 9 Nov 2019, 2 Nov 2019, 1 Nov 2019,
  11 Dec 2014). None concerns the Duke of Ormond, Arran or any 17th-century cipher; no comment thread opened since no
  post is plausibly about this letter.

### (c) Every plausible hit opened and its thread read

- `github.com/AlexFitzgerald47/cracking-problems-hub/pull/7` ("Discover Irish-connected historical ciphers; flag
  solved Maltravers case", 16-17 Sept 2026, single author AlexFitzgerald47, no reviewer comments): the one sentence
  about this item, verbatim, "A separate Ormond–Arran 1678 passage remains a possible future candidate pending its
  own source and solution audit." A candidate list, not a reading; no decipherment claimed.
- `dbourdeau.github.io/cyphersolver/index.html` ("updated 1 October 2026"): the only Ormonde entry is the solved
  Maltravers to Ormonde 1634-35 item; no Arran 1678 reading. Consistent with `TARGETS.md` row 7 ("too short; not
  attempted", Check-solved point 5) and with today's solver diff `sources/solver-diffs/2026-10-02-bourdeau.tsv`, which
  carries this target as class (c) "listed only".
- `github.com/arya1515/cyphersolver` and `github.com/setsunaatto/cyphersolver`: both are forks of
  dbourdeau/cyphersolver; their README and file lists mention Ormonde only for the 1634-35 Maltravers item (the
  setsunaatto fork's one "Arran" is "19 = Arran" in the 1585 Wotton-Walsingham key, a different Arran). No Ormond-Arran
  1678 work in either.

### Requests per host

WebSearch 10 queries; `github.com` 3; `dbourdeau.github.io` 1; `cryptiana.blogspot.com` 2; `cryptiana.web.fc2.com` 2;
`ciphermysteries.com` 1; `scienceblogs.de` 1; `cipherbrain.de` 2 (503, then TLS failure on the one retry). All one at a
time per host. No logins, no credentials, no subagents.

### Intake gate re-run

```
$ python3 tools/intake_gate_check.py ormond-arran-1678
ormond-arran-1678: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit code: 0
```

## Premise check (GF4-BATCH1, account-4, 2 Oct 2026)

**Result: not found solved.** No decipherment, plaintext or applied key for the p.93 passage was found under (a)-(d).
Status stays `open`. This is the adversarial pass of `.claude/briefs/check-solved.md` "Premise check", run 2 Oct 2026
23:53 to 3 Oct 00:00 UTC (`date -u`). No test or reading was run. One transcription flag (the ninth group, below) goes to the
image check and is not repaired here.

**(a) Decipherments the folder mentions, opened. Not found.**
- Tomokiyo's HTML-comment note in `sources/cryptiana/web/charlesii2.htm` (on disk, read in the check-solved pass above).
  It records a *failed* application of the Ormond-Longford Cipher 1 to this passage, not a reading.
- The calendar's two printed glosses near this letter, opened in vol.4's djvu text (fetched fresh this pass). One is
  p.105-6, Arran to Ormond, 9 Feb 1677-8: a two-letter code with bracketed equivalents. The other is the p.107 footnote
  ("The equivalents for the words in cipher in the original are interpolated in Ormond's handwriting"). Both are
  different systems from the 3-digit groups on p.93, and neither glosses p.93. The volume index lists only 93 and
  105-6 as cipher passages.
- Cipher 1-3 keys and the sibling passages of 1680 (`keys/`, `siblings.tsv`): these carry their own printed
  decipherments, are a different system (YX-ORM, ZX2-ORM negatives), and none covers this passage.

**(b) Other solvers' working files. Not found.**
- **Bourdeau**: fresh shallow clone, HEAD 2341682 (2 Oct 2026 15:12 -0500). `TARGETS.md:190` still reads "too short;
  not attempted". `targets/ormonde/` (analyze.py, cipher_runs.txt, knowler_excerpts.txt, NOTES.md) is the 1634-35
  Maltravers item only. Its `445`-like hits are index page numbers in his harvested text, not this passage.
- **Aymeloglu**: fresh shallow clone, HEAD d2800bb (27 Sept 2026). No `ormond` or `arran` file, folder or row.

**(c) Physical neighbours (the letters on either side in the same Kilkenny series, HMC vol.4 pp.90-110). Not found, but a
reply bears on it.**
- **Arran's reply, 5 Feb 1677-8 (London, vol.4 pp.101-102):** "three packets were sent me ... with yours of the 24th,
  26th and 29th of last month ... Since you tell me what you wrote in cipher is not of great importance, I will not
  venture the post's going away by endeavouring to decipher it to-night, but you may depend upon me so far as this
  cipher goes which is betwixt us, if the copies are true." So the recipient had not deciphered it on 5 Feb. A full
  grep of vol.4 for cipher/decipher (about 30 hits) found no later letter in which Arran reports the decipherment.
  The nearest later cipher in the run is Arran's 9 Feb two-letter code, a different system.
- Ormond to Arran, 29 Jan 1677-8 (pp.99-100), in clear, on the same subject (Douglas, "a notorious cheat", Maunsell,
  Granard). It is context for the passage's topic, not a decipherment. No crib test was run (out of brief).
- The originals: the preface (vol.4 pp.v-vi) says the 1677-85 Kilkenny correspondence survives largely intact, and
  that Bodleian Carte MSS 38-40, 45, 47, 50, 52-54, 216-217 hold "duplicate drafts or contemporary office copies" of
  it. A Carte copy of this letter, with or without a gloss, was not checked: the Bodleian catalogue and images were
  not reached this pass. **Unreachable**; a cheap next step is the Bodleian online Carte calendar for Ormond to Arran,
  24 Jan 1677/8.

**(d) Recipient's side and other prints. Not found.**
- **HMC Sixth Report, Appendix (1877), pp.720-721** (Gilbert's report on the Kilkenny Ormonde MSS, 1665-79;
  archive.org `sixthreportroyal00manu`, full text grepped). This is a second, earlier print of the same letter in the
  original spelling ("This is a tryall whether you are skilfull in decyphering, els it might have been written in
  plaine letters"). The cipher groups are printed undeciphered. There is no gloss or footnote, the same as in 1906. The
  same text is reprinted in `reportofroyalcom06grea` and `reportsfromcommi0047unse_47` (Parliamentary Papers).
- Interior-phrase searches. IA full text (be-api): "too nice a modesty" (10 hits), "still a greater mystery to me"
  (7), "what he says of 445" (4). Google Books (country=US, keyed): "445 and 342" (7), "too nice a modesty can be of no
  use" (8), "skilfull in decyphering" (118, all unrelated). Every hit is one of the HMC prints or one of two modern
  books that quote the clear opening ("sloth and too nice a modesty", on Arran's court duties): *After the Civil
  Wars* (2014) and *Lord Churchill's Coup* (Webb). Neither prints the cipher groups or a reading of them.
- Arran's own papers: no separate edition was found. Carte's *Life of Ormond* book VIII was not searched this pass
  (the HMC preface says it gives this period little space).

**Transcription flag (not repaired, rule 2/ciphertext as transcribed).** `ciphertext.txt` gives the ninth group as
**57**. Both independent editorial transcriptions of the manuscript give **58**: the 1877 Sixth Report (Gilbert), and
the 1906 calendar, where Google Books' separate OCR also shows 58. The check-solved note at point 1 above took 58 for
an OCR slip and 57 from Tomokiyo's typed transcription. Two editors against one later typed copy favours 58. The file
stays as transcribed until the manuscript (NLI Ormond papers or a Carte copy) or a page image of the 1877/1906 print
is checked. The earlier key-coverage tests are unaffected in substance: 57 and 58 are both single groups among 20.

Requests this pass: archive.org 3 (vol.4 djvu, Sixth Report djvu, plus 4+5 be-api fts calls, >=2 s apart),
googleapis.com 3 (keyed, country=US), github.com 2 (shallow clones, shared with this batch). No logins.

## FT4-ormond-arran-1678 (3 Oct 2026, account-4): Carte calendar route

Run 3 Oct 2026 02:21-02:29 UTC (`date -u`). No cryptanalysis, no reading, no test.

**Route that worked.** The Bodleian's own online Carte Calendar pages (`bodley.ox.ac.uk/dept/scwmss/projects/carte/carte54.html`)
now 301 to `archives.bodleian.ox.ac.uk/...`, which serves an Anubis "Making sure you're not a bot!" page to curl (1 request);
`https://www.bodley...` resets the connection; the Wayback Machine answered "Temporarily Offline"; one headless-Chromium attempt
timed out (killed, not retried). The same calendar text (Edwards's MS. Carte Calendar vols 30-61, keyed by the Bodleian in 2004)
is platformed by the Virtual Record Treasury of Ireland (virtualtreasury.ie, VRTI, 2024). Its public search endpoint
(`POST https://by2022-prod.adaptcentre.ie/IR_REST_V2/webapi/doc_search`, JSON body with `indexDBName: "beyond_2022"`,
`kwList`, `kwOperList: ["ALL"]`, `kwSearchFieldList`: `all` or `referenceCode`) answers plain curl with no key; the per-item
REST endpoint answers 401 and was not used.

**Finding 1 -- the key sheet (premise evidence, not a reading).** `Bodleian MS. Carte Calendar 54/46`:
"Cypher [used in the correspondence of the Duke of Ormond] with the Earl of Arran: January 1678" -- "Calendar of MS. Carte 50,
fol(s). 439-440 (276)". The calendar gives the title only, no abstract and no table. A second, later key exists:
`MS. Carte Calendar 58/76`, "Cypher [used in the Correspondence of the Duke of Ormond with his son] the Earl of Arran:
25 April 1682", MS. Carte 50, fols. 435-436 (274). The January 1678 sheet is dated the month of our letter (24 Jan 1677/8) and
names the same correspondents, so it is very likely the key of this passage; that it *is* that key is inferred, not checked, until
someone reads fols. 439-440. It is not one of the three keys already tested here (`keys/cipher1-3`: Ormond-Longford, HMC vols 5-7).
Whether the HMC or anyone has printed MS. Carte 50 fols. 439-440 was not searched this pass.

**Finding 2 -- no Carte copy of the letter in the calendar.** Retrieved MS. Carte Calendar vol.54 items 25-60 (19 Jan - c.5 Feb
1678, contiguous) by reference-code search: none is Ormond to Arran of 24 Jan 1678 (nearest Ormond out-letters are to Henry
Coventry, 19 and 22 Jan, MS. Carte 146; 54/32 is Ormond to Coventry with William Douglas's narrative, MS. Carte 146 fols. 63-67,
context for the passage's subject). A full-text query "Ormond to Arran January 1678" over the whole index returned no such item
either. So the calendar records no second copy of the letter; the Kilkenny original (NLI) printed in HMC remains the only witness
found. The calendar prints no summary or clear text of the p.93 passage: **the item's plaintext is not in print in this source.**

**Holding-catalogue availability flag: not read.** The archives.bodleian.ox.ac.uk record for MS. Carte 50 is behind the same
Anubis challenge from this container; filed as LOCAL-QUEUE row L39 for the owner's desk runner (catalogue flag, and if a viewer
exists, fols. 439-440 imaged).

Requests: bodley.ox.ac.uk 3 (one 301, two resets), archives.bodleian.ox.ac.uk 1 curl + 1 browser attempt (timed out),
web.archive.org 1 (offline page), virtualtreasury.ie 3 (SPA shell and its JS bundle), by2022-prod.adaptcentre.ie 1 (401) +
13 search POSTs, all >=1.6 s apart, one at a time. WebSearch 2 queries. No logins, no vision calls.

## FT4b-ormond-arran-1678 (3 Oct 2026, account-4): prior print of the Carte 50 key; Digital Bodleian

Run 3 Oct 2026 02:38-02:45 UTC (`date -u`). No cryptanalysis, no reading, no test; no vision calls.

**Prior print of MS. Carte 50 fols. 439-440: none found.** Searched by interior string and shelfmark, not title only.
- HMC *Ormonde* N.S. vols IV and V (archive.org `calendarofmanusc04greauoft`, one OCR file carrying both volumes, vol. V
  from OCR line 52222): all 36 "cipher/cypher" lines read in context. They are letters partly in cipher, two
  editors' notes that Ormond interlined the equivalents (vol. IV p.107 and a vol. V letter) and three vol. V index
  entries ("Cypher, employed in correspondence, 454, 469, ..."). No key table and no Carte 50 item is printed; the
  vol. IV preface names Carte 50 only as one of the Oxford volumes for 1677-85 and points to Russell and Prendergast's
  report for its contents.
- Internet Archive full text (be-api fts, 15 queries): exact `"Carte 50, f. 439"`, `"Carte 50, fol. 439"`,
  `"Carte MS. 50, f. 439"`, `"Carte 50, ff. 439"`, `"Carte 50, f. 440"`, `"cypher with the Earl of Arran"`,
  `"cipher with the Earl of Arran"`: 0 hits each. The broader queries hit secondary works that cite other Carte 50
  folios (f.58, f.86, f.103, f.194, f.349). One of them cites **another cipher key in the same volume**: J.P. Kenyon,
  *Robert Spencer, Earl of Sunderland* (1958), reads Bodl. Carte MS. 232 f.49 (1679) with "[cipher key Carte MS. 50,
  f. 472]" (IA `robertspencerear0000keny`; Google Books `JlY0AAAAIAAJ` snippet agrees). So at least one 20th-century
  historian used a Carte 50 key to read Ormond-circle cipher. That key is f.472, not ff.439-440, and its table is not
  printed in the snippet. Charles Middleton studies cite a different key, "Carte MS 256".
- Google Books API (key, `country=US`, 6 queries): `"Carte 50" cipher Arran` returns Russell and Prendergast, *The
  Carte Manuscripts in the Bodleian Library* (1871; also in the DKPR 32nd Report), whose snippet describes vols 48-51
  only at title level ("drafts or copies ... of Ormonde's letters ... in cipher"). `"Carte MS. 50" "cipher key"`
  returns only Kenyon (above). The `"f. 439"`/`"fol. 439"` queries return only noise (338/332 unrelated items).
- OpenAlex (3 searches): 0 / 7 / 6 results, none about an Ormond-Arran key. The 7 and 6 overlap; nearest is
  "Breaking the Code. John Wallis and the Politics of Concealment" (2016), general.
Result: no transcription of the Carte 50 ff.439-440 table was found in these sources. This is a search result,
not a novelty verdict (rule 10). Not searched: JSTOR (cloud-blocked), Kenyon's full text at f.472 (lending-only),
and the 1871 Russell-Prendergast report's full entry for vol. 50.

**Digital Bodleian: no images of MS. Carte 50.** Queried with the Data API's JSON search
(`GET digital.bodleian.ox.ac.uk/search/` with `Accept: application/ld+json`). `shelfmark:"MS. Carte 50"` returned 0,
`"Carte 50"` returned 0 and `shelfmark:Carte` returned 3: MS. Carte 3, 55 and 91. Positive control: the same API
lists those three Carte volumes, so the 0 means the search found nothing, not that the search is broken. This is
the image portal's result, not the holding record's flag. The holding-catalogue flag (archives.bodleian.ox.ac.uk,
Anubis-challenged to the cloud, FT4) is already queued as LOCAL-QUEUE **L39**, so no new row was filed. Nothing was
fetched: no images are online to fetch.

Requests: archive.org 10 (1 OCR file, 1 advancedsearch, 8 metadata); be-api.us.archive.org 15; googleapis.com 6;
api.openalex.org 3; digital.bodleian.ox.ac.uk 7 (2 HTML search/developer pages, 1 data-API doc, 4 JSON searches).
Every request ran one at a time, at least 1.6 s apart.

## FT4c-ormond-arran-1678 (3 Oct 2026, account-4): ninth group 57/58 on the 1906 page image

Run 3 Oct 2026 02:56-03:05 UTC (`date -u`). No cryptanalysis, no reading.

**Page image.** IA `calendarofmanusc04greauoft_page_numbers.json` maps printed p.93 of vol. IV to leaf 123 (leafNum,
confidence 99; the vol. V half of the item has its own p.93 at leaf 875, not used). Fetched the page image once:
`https://archive.org/download/calendarofmanusc04greauoft/page/n122.jpg` (0-based index n122 = leaf 123; 2592x4374,
HTTP 200 image/jpeg), kept as `images/hmc4_p93_n122.jpg` (1.2 MB). The page carries the running number "93" and the
Ormond-to-Arran letter of 24 Jan 1677/8; the item's own OCR (`_djvu.txt`, line 6632) reads the passage on this page.

**Crop (command run).**
`python3 tools/iiif_lines.py --image ciphers/ormond-arran-1678/images/hmc4_p93_n122.jpg --region 0,3160,2400,220 --lines-per-crop 4 --max-width 2400 --out ciphers/ormond-arran-1678/images/crops_p93 --prefix p93`
-> 3 lines, 1 crop, `images/crops_p93/p93_L01.jpg` (manifest beside it). A first cut at `--region 200,3350,2300,380`
fell one line too low (it showed "..., 54, 700, 720 but it seems ..." onward) and was discarded. **2 vision calls**
(brief named one; the extra one was the mis-placed crop, read by the worker itself, no subagent).

**What the print shows.** The crop's third line reads, clearly: "what he says of 445 and 342, be true 726, 91, 33,
425, 93, 58," -- the ninth group is printed **58**. The final digit's closed upper and lower bowls are those of an 8,
unlike the open-left 3s of "33" in the same line. So the 1906 page image agrees with its own OCR and with the 1877 Sixth
Report and Google Books' OCR (GF4-BATCH1 Premise check): all print witnesses read 58; only Tomokiyo's typed
transcription, from which `ciphertext.txt` was taken, has 57.

**ciphertext.txt not changed** (CLAUDE.md layout rule: as transcribed, never silently repaired). Finding logged here: the
ninth group should be taken as **58** on the print evidence (the 1906 image, plus two independent editorial texts); the
file keeps Tomokiyo's 57 as its transcription source. The NLI original has not been checked (needs physical access or
an NLI reproduction); the key-coverage tests are unaffected in substance (YX-ORM/ZX2-ORM: a single group among 20,
neither 57 nor 58 recurs in the passage).

Requests: archive.org 5 (page_numbers.json x2, one a 500 retried once after a pause; files metadata 1; page image 1;
`_djvu.txt` 1), all one at a time, >=2 s apart. No logins.

## R8-ORM (6 Oct 2026, account 2, LANE-RUN8): the 1871 Russell-Prendergast report's entry for MS. Carte 50

Run 6 Oct 2026 03:37-03:41 UTC (`date -u`). Lookup only: no reading, no test, no vision calls.

**Where the text was found.** Not on archive.org: `advancedsearch` for the title, the authors and the DKPR report
(4 queries) found no scan of the 1871 report (the one "thirty-second report" hit is the *Irish* Deputy Keeper's,
`op1254077-1001`, a different series). Google Books API (key, `country=US`, 1 query `"Carte Manuscripts in the
Bodleian"`) gives **`Qv8UAAAAQAAJ`**, *The Carte manuscripts in the Bodleian library, Oxford. A report, by C.W. Russell
and J.P. Prendergast* (1871), full view (ALL_PAGES, 252 pp.); also full view `DN-bhb-8AcYC` (1888 issue, not used).
The page-text view is captcha-blocked from the cloud (host table), so the volume was read through Google's
search-within-volume JSON (`tools/gbooks_search_within.py` endpoint, `jscmd=SearchWithinVolume2`), and the vol. 50
entry rebuilt from overlapping snippets, each joined on a shared run of at least five words.

**The entry, p.43 (Part II, "Notices of Carte's MSS."), as rebuilt:**
"Vol. 50, formerly marked "WW 2," folio. Copies and original drafts of the Duke of Ormonde's letters, from 1669 to
1687, to the following persons: -Captain G. Mathews, Lord Clanricarde, the Lord Chancellor of Ireland, the Constable
of Castile (Governor of the Low Countries), Sir J. Temple (Solicitor General), Lord Ossory, Lord Kingston, Lord Arran,
Lord Aungier, Lord Derby, Lord Strafford, the Prince of Orange, Sir G. Lane, Sir W. Temple, the King, Lord Arlington,
Lord and Lady Burlington, Colonel Fitzpatrick, Sir Robert Southwell, Sir W. Coventry, the Archbishop of Canterbury,
the Lord Primate of Ireland, Lord Sunderland, Lord Coventry, the Earl of Rochester, the Earl of Longford, and others.
There are also some miscellaneous papers, among which are the following: -Instrument of the University of Oxford,
making Lord Clarendon High Steward. The Duke of Ormonde's Speech in the Cause between Hyde and Emerton. Letter to the
King after Major Warren was sent over in 1642, with a memorandum about transporting the Forces to England (Feb.
1643). A prayer of Ormonde's. Patent of Precedence of Lord Ossory's children. Settlement proposed on the Marriage of
James Earl of Ossory and Lady Hyde. Account of Ormonde's Debts, &c. **At the end of the volume is a collection of
ciphers of the following persons: -Sir H. de Vic, the Lord Chancellor of Ireland, the Lord Chancellor of England,
Lord Arlington, Sir E. Nicholas, the Earl of Orrery, Sir W. Coventry, Lords Anglesea, Ossory, Carlingford, Kingston,
Conway, Longford, and Arran, Sir T. Clarges, Sir G. Carteret, Captain Barrington, Colonel W. Legg, Sir Robert
Southwell, Sir G. Lane, J. Walsh, Dr. Gorges, Sir Robert Booth, and P. Alden. They are dated from 1662 to 1682.**"
(Snippet OCR artefacts "Governor vernor" and "Sir J. Tem Temple" normalised; nothing else changed.)

And p.72 (the report's summary of the Ormonde papers): "The four volumes 48-51 contain drafts or copies, very many
autograph, of Ormonde's own letters, and in volume 50 is a collection of the various ciphers (with their respective
keys) employed by Ormonde and his several correspondents."

**What it adds and what it does not.**
- It confirms, from an 1871 description independent of the Bodleian online record (L39), that the cipher collection
  in vol. 50 includes a cipher **of Lord Arran**, and one of **Lord Longford** (the 1680 sibling correspondent tested in
  YX-ORM/ZX2-ORM), inside an overall date range 1662-1682 that covers Jan 1678, and that the report counts the keys as
  present ("with their respective keys").
- It gives **no folio numbers** and no dates per cipher: within-volume searches for "439", "440" and "472" hit only
  other volumes' references and the index (pp.39, 92-93, 213, 234, 236). So it neither confirms nor contradicts that
  fols. 439-440 are the Ormond-Arran key, says nothing of the f.472 key Kenyon cited, and does not say whether vol. 50
  holds one Arran cipher or several (e.g. one for 1678 and one for his 1682-84 Deputyship).
- It prints **no key table** (searches for "key"/"keys" return only p.27 De Boderie, p.46 vol. 74's "keys to ciphers
  before and during the Rebellion", p.72 above and unrelated pp.74-143). A search result for this volume, not a
  novelty verdict (rule 10).

Requests: archive.org 4 (advancedsearch); www.googleapis.com 1; books.google.com 37 (SearchWithinVolume2 JSON,
one at a time, 2 s apart, all HTTP 200, no challenge). No logins.

## Remaining gaps (FT4c-ormond-arran-1678, 3 Oct 2026)
Read so far: 0 of 20 groups read (no key has fitted: YX-ORM, ZX2-ORM; status open, not partial)
- key sheet MS. Carte 50 fols. 439-440 (Ormond-Arran cypher, Jan 1678) - blocker: waiting-on LOCAL-QUEUE L39; the catalogue flag is unreachable from the cloud (archives.bodleian.ox.ac.uk Anubis challenge, FT4), Digital Bodleian has no Carte 50 images (FT4b, positive control returned Carte 3/55/91), and no printed transcription was found (FT4b section above), so the leaves need a reproduction order or a person's reading
- ninth group 57 vs 58 - resolved for the print 3 Oct 2026 (FT4c): the 1906 page image reads 58, like the 1877 print; ciphertext.txt keeps Tomokiyo's 57 as transcribed; only the NLI original is unchecked - blocker: needs-physical-access; the Kilkenny original is in the NLI Ormond papers, no online image located, and every print witness already agrees on 58

## Escalation (3 Oct 2026, FT4c)
- [x] siblings: 1680 Ormond-Longford sibling passages and keys tested (YX-ORM, ZX2-ORM), no fit
- [x] clear-pages: Arran's reply of 5 Feb and Ormond's clear letter of 29 Jan read (Premise check c)
- [ ] known-keys: MS. Carte 50 fols. 439-440 key sheet located 3 Oct 2026; read it once L39 or a reproduction order returns images
- [x] print: no printed Carte 50 fols. 439-440 table found in HMC Ormonde N.S. IV-V, IA full text, Google Books or OpenAlex (FT4b, 3 Oct 2026); the 1871 Russell-Prendergast report (p.43) lists a cipher "of ... Arran" among vol. 50's keys, 1662-1682, but prints no table and no folios (R8-ORM, 6 Oct 2026)
- [n/a] key-rebuild: twenty groups are far too short for cryptanalytic key rebuilding
- [x] image-check: ninth group read as 58 on the IA page image of the 1906 print, vol. IV p.93 (FT4c, 3 Oct 2026)
- [n/a] retry: no earlier route failed that a retry would change
Verdict: keep going: 0 internal gaps; cheapest next: read the MS. Carte 50 fols. 439-440 key sheet and apply it to the 20 groups once LOCAL-QUEUE L39 returns images or a reproduction is ordered (blocked on LOCAL-QUEUE L39), ~$1

## While waiting

- While L39 is pending, read the 1871 Russell and Prendergast report (*The Carte Manuscripts in the Bodleian Library*,
also DKPR 32nd Report) entry for MS. Carte 50 in a public-domain scan, for any description of fols. 439-440 or the
f.472 key Kenyon used. This depends on nobody. Done 6 Oct 2026 (R8-ORM, section above): vol. 50 entry read, Arran cipher listed, no folios, no table. The 57/58 image check was done on 3 Oct 2026 (FT4c): the print reads 58.
- 5 Oct 2026 (PR-LAND-67): LOCAL-QUEUE L39 answer landed, local-runner/L39-2026-10-05.md -- MS. Carte 50 (ark:29072/x08c97kq77qq) "NOT AVAILABLE ONLINE", "a large collection of ciphers in use from 1662-82" from fol. 405; no item-level record for fols. 439-440.
