# tools/data/uscodes-1800 -- published early-US diplomatic codes, value->word tables

Built 26 Sept 2026, LANE ARM worker ARM-CODES, for `ciphers/armstrong-madison-1808` (the 20 Feb 1808
Armstrong-to-Madison letter, in a code neither the State Department nor any sibling table matches directly).
Every later family (direct-transfer sweep, one-part/two-part design test, nomenclator solver) reads from
this directory. This job does not decode the target; that is ARM-A2 (next job).

## What is here

| File | Code | Correspondents | Entries | Grades | Source |
|---|---|---|---|---|---|
| `WE028.tsv` | WE028 (THE=1385) | James Monroe <-> James Madison, sent to Paris to assist Livingston | 1600 | H (Tomokiyo's own transcription of a printed source) | `cryptiana.web.fc2.com/code/WE028.txt`, fetched 26 Sept 2026. Served Shift-JIS (a Japanese host), not UTF-8 -- `raw/WE028.txt` kept as fetched; `build_tables.py` decodes it correctly. A handful of entries (1261-1267, punctuation; 375, a bracketed Japanese gloss) are non-ASCII. |
| `THE972_bourdeau.tsv` | THE=972 | John Armstrong <-> James Madison (all letters *except* the 20 Feb 1808 target) | 580 | H/C/M/I, Bourdeau's own grades, kept as published | `github.com/dbourdeau/cyphersolver`, `armstrong/key972.js`, commit `fc0c9e865d0fae67ca92d19750d2b09ab11972e0`, cloned and grepped 26 Sept 2026, then deleted (repo not committed here). MIT licence (code) -- cited, kept as a derived TSV under this repository's own tooling, not a verbatim copy of `key972.js`'s JS syntax. |
| `THE972_tomokiyo_partial.tsv` | THE=972 | same | 227 | C or M (M where the source's own string carries a `?`/`...` uncertainty marker or a bracketed alternative reading; see `build_tables.py`'s own docstring for the rule) | Tomokiyo's raw harvest, `code972_partial.json`, fetched via the same Bourdeau clone (it is also on cryptiana's own site under a different, cleaner rendering -- see next row). No stated licence for Tomokiyo's own text; cited, not verbatim-copied beyond the plain value/word pairs a TSV needs. |
| `THE972_tomokiyo_clean.tsv` | THE=972 | same | 95 | C (Tomokiyo's own convention: reconstructed from a single known-plaintext letter, the 4 May 1806 one) | `cryptiana.web.fc2.com/code/madison_THE_972.txt`, fetched 26 Sept 2026. This is Tomokiyo's own cleaned current version (no `?`/`...` markers) -- a strict subset relationship with `THE972_tomokiyo_partial.tsv` was not checked value-by-value this pass; both are kept since they are different published renderings. |

`raw/` holds every file exactly as fetched (or cloned then copied out), so `source_line` in each TSV points
at a real, re-fetchable line. `raw/madison_AFIO_key.txt` is also kept for provenance (the already-adjudicated,
rejected AFIO key -- see `ciphers/armstrong-madison-1808/NOTES.md`'s "AFIO claimed solution" section); it is
**not** treated as a sibling code table anywhere in `stats.py`, since it is a disproven guess at the target's
own key, not an independently attested codebook.

`decodes/` holds Bourdeau's own decodes of Armstrong's other 1808 letters in THE=972 (his own idiolect,
same months as the target), rendered fresh this pass with his `decode972.py` (cloned, run, deleted):
- `armstrong_1808-08-30_ps.txt` -- postscript of 30 Aug 1808 (48 of 49 groups read; see Bourdeau's own
  `armstrong/NOTES.md` for the one doubtful group).
- `armstrong_1808-02-22.txt`
- `armstrong_1808-02-15.txt` (Founders 99-01-02-2703, the letter Bourdeau's paired check reads at 72% in
  THE=972 -- see `ciphers/armstrong-madison-1808/NOTES.md`).
- `armstrong_1808-09-07_frag3414.txt` (a short fragment).
No separate decode exists for the 4 May 1806 letter as a standalone file in Bourdeau's repository: that
letter's known plaintext *is* the source Tomokiyo built `code972_partial.json`/`madison_THE_972.txt` from in
the first place (both already captured above as tables, not as a third decode file).

## Not reachable / not published as tables

- **WE027** (Robert R. Livingston <-> Madison, ~1700 elements): named descriptively by both Tomokiyo and
  Bourdeau (cited to Weber 1979 pp.154, 188), but no `.txt`/`.json` transcription exists anywhere found --
  not on cryptiana.web.fc2.com/code/ (checked directly: `WE027.txt` 302-redirects to fc2's generic 404,
  the same signal every other untried `WEnnn.txt` guess gave except `WE028.txt`, which is a genuine `200`)
  and not in either solver repository.
- **Every other WE-numbered code Tomokiyo names** (Jefferson/Short's WE062 -- a *transposition* cipher, not
  a word/syllable code, so out of scope for a value->word table regardless; Livingston/Jay's WE007/WE008/
  WE033/WE031; Franklin/Dumas's WE003/WE004/WE041; the Virginia Delegates' Code THE=6/WE015; CUPID/WE050):
  Tomokiyo's site (`code/index.htm` "Decoding Revolutionary Correspondence", plus `livingst.htm`,
  `jeffersn.htm`, `state.htm`, `frankli2.htm`, `jayscode.htm`, `washingt.htm`, `franklin.htm`, all fetched
  and grepped this pass) publishes worked *decoded-letter specimens* under these WE numbers (individual
  code groups shown inline, next to their plaintext, in his prose), never a downloadable full table file.
  Extracting a table from inline HTML specimens is a different, much larger job than this one (per-page
  scraping and manual alignment) and out of this brief's cap; flagged for a future job if a specific one of
  these codes turns out to matter (none besides THE=972 and WE028 has been suggested by Tomokiyo or Bourdeau
  as plausibly related to the 20 Feb 1808 target).
- **Weber 1979** (*United States Diplomatic Codes and Ciphers, 1775-1938*) itself, the print survey both
  Tomokiyo and Bourdeau cite the WE numbers to: found on Internet Archive, identifier
  `unitedstatesdipl0000webe` (one `advancedsearch.php` query, 26 Sept 2026), but `access-restricted-item:
  true` and its only collection tag besides `internetarchivebooks` is `printdisabled` -- per CLAUDE.md's
  Access playbook (IA-BORROW job, 25 Sept 2026), a `printdisabled`-only item cannot be borrowed by this
  account regardless of retries, so not chased further. HathiTrust's bibliographic API
  (`catalog.hathitrust.org/api/volumes/brief/oclc/4592801.json`, OCLC number from an Open Library search,
  Chrome User-Agent per the playbook) returned `{"records": {}, "items": []}` -- no HathiTrust volume at
  all. Weber himself is not reachable as a full-view text by this worker.

## Stats

`python3 stats.py` (offline, reads only the TSVs here and `ciphers/armstrong-madison-1808/ciphertext.txt`)
writes `stats.tsv`. It reports, per sibling table, per THE=972 real-usage instance (the four decodes above,
individually and pooled), and for the target (all 369 tokens, and the 216 distinct values): entry/token
count, value range, last-digit distribution, a per-hundred-block value count (the "gap pattern"), and, for
the four value->word tables only (a usage instance or the target's own ciphertext has no known plaintext to
rank alphabetically), the Spearman rank correlation between value order and alphabetical order of the
plaintext, a count of alphabetical run-blocks, and the ten commonest plaintext words by homophone count
(how many distinct code values map to the same word).

### Headline results (see `stats.tsv` for the full table)

- **No sibling shows the target's last-digit skew.** The target's 369 tokens run digit-0 93x (25%),
  digit-1 66x (18%), digits 2/3/5/9 7-17x each -- confirmed by this script (`93,66,17,10,41,12,32,46,45,7`
  for digits 0-9). None of the four value->word tables' own defined-value sets is anywhere near this flat-
  vs-skewed shape (WE028 is exactly flat by construction, 160 per digit, since it is one un-gapped run
  1-1600; the three THE=972 tables run 53-65 per digit, not skewed). Real *usage* of THE=972 (the four
  decodes, pooled, 474 tokens) is closer to flat-with-noise than to the target's shape too (highest digit is
  2 at 70, not digit-0 at 44) -- so the target's own digit-0/digit-1 dominance is not a generic feature of
  this code family's construction or of how it gets used in real letters; it is specific to the target.
- **The target's value gap at 900-1099 is real and specific.** 3 tokens land in 900-999 and 1 in 1000-1099
  (4 total, matching the brief's own count) against double-digit counts in every neighbouring hundred-block
  for the target's own distinct-value list. No sibling table or usage instance shows a comparably deep
  trough at exactly that block (WE028 and the THE=972 tables all carry 25-47 entries in 900-999 and
  1000-1099 alike; the pooled usage instances show 53 and 37 respectively) -- the trough is not inherited
  from a shared codebook design, consistent with the target being built on a still-unidentified table rather
  than a rare region of a code we already have.
- **Blockwise-alphabetical, all four tables, not one-part or arbitrary two-part.** Spearman rho between
  value-order and plaintext-alphabetical-order is near zero for every table (-0.09 to -0.25, not the +1.0 a
  single fully-alphabetical one-part code would show, nor scattered near zero *with* one block each, which a
  wholly random two-part code's per-block alphabetisation would not produce either); alphabetical block
  counts are 98 (WE028, ~16 entries/block), 99/48/18 for the three THE=972 tables (~5-6 entries/block on the
  denser ones) -- many short ascending runs, confirming the construction NOTES.md already describes
  qualitatively ("blockwise alphabetical... syllables restart the alphabet every few dozen groups") with a
  number: on the order of 5-16 entries per alphabetical block across all four published tables, a shared
  construction convention across Livingston's, Monroe's and Armstrong's codes alike.
- **Homophone counts are modest and syllable-concentrated.** WE028 (a near-1:1 word code, 1600 values for
  1600 mostly-distinct entries) has almost no homophones (its commonest repeated forms occur only twice).
  THE=972's tables show real homophony concentrated on short common syllables/words (`re` x6, `tion` x4,
  `be` x4 in the denser Bourdeau table) -- consistent with a syllable-and-word code needing several values
  for its most frequent short units, the same shape a nomenclator/nomenclator-solver family (family C in
  `HYPOTHESES.md`'s ladder) will need to model.

## Licences (CLAUDE.md rule 8)

Bourdeau's `cyphersolver` repository: code MIT, text CC BY 4.0 -- cited above per file, the JS/JSON tables
re-expressed as TSV rows by this repository's own `build_tables.py`, not copied verbatim as code.
Aymeloglu's `unsolved-ciphers` repository has no licence and was not used as a source for this job (grepped
in the target's own intake pass, `NOTES.md`, no hit for this target). Tomokiyo (cryptiana.web.fc2.com): no
stated licence on his own pages; cited by URL and fetch date throughout, his tables kept as raw fetches
under `raw/` and re-expressed as TSVs, never claimed as this project's own work.

## Requests this session

cryptiana.web.fc2.com: 41 total, >=1.5s apart, descriptive User-Agent, no 429/403/challenge seen -- 2
(`code/`, an index/demo page, not a real code-list index, fetched once as a status check and once for
content) + 3 (`livingst.htm`, `jeffersn.htm`, `state.htm`) + 4 (`frankli2.htm`, `jayscode.htm`,
`washingt.htm`, `franklin.htm`) + 27 (`WEnnn.txt` guesses for n in 001-020,027,031,033,041,050,062,094, all
but WE028 came back a 302 to fc2's generic 404 page) + 2 (status-only redirect checks on `WE028.txt` and
`WE003.txt`, to confirm the 200-vs-302 signal before trusting the loop) + 3 (`WE028.txt` real content,
`madison_THE_972.txt`, `madison_AFIO.txt`).
github.com: 1 shallow clone (`dbourdeau/cyphersolver`, deleted after copying the MIT/CC-BY-4.0 files cited
above). archive.org: 2 (`advancedsearch.php` for Weber 1979, then `metadata/unitedstatesdipl0000webe` to
check its access-restriction and collection tags). openlibrary.org: 1 (OCLC lookup for Weber 1979).
catalog.hathitrust.org: 2 (first attempt 403'd with a descriptive UA -- Cloudflare-challenged, per the
Access playbook's own note that this endpoint needs a full Chrome UA string; the one permitted retry with a
Chrome UA succeeded, 200, empty result). No logins, no credentials touched.
