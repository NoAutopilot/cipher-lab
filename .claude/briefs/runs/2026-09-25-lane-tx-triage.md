# LANE TX triage: printed-ciphertext detector sections (25 Sept 2026)

Worker: TX-SWEEP (Sonnet, session_01HpooJxJvDWvNMKLdZ4YjTQ), for LANE TX orchestrator session_01UDxtM9Xv2dnPfoo5z9T6wA.
Clock checked: `date -u` = 2026-09-25 06:18:43 UTC.

Method: read the five named QUEUE.md headers in full (grepped for `^## Printed ciphertext`), applied the brief's
exclusions (ciphers/thurloe-printed; anything claimed in ROOM.md in the last six hours; every R5/N4/B/V2/PX/LX/OX
target), then read each remaining row's own check-solved/verifier state from NOTES.md/AUDIT.md/STATUS.md/ROOM.md
before scoring it. Rule 10 wording throughout; no reading is claimed by this worker.

## What is actually in the five sections (not ~38 rows; the true count is 26, reported rather than padded)

| Section | Rows | Outcome |
|---|---|---|
| "Printed ciphertext (detector test of 23 September 2026)" | P1-P24 (24 rows) | P1 found-solved (skip); P2-P24 (23 rows) are `ciphers/thurloe-printed` |
| "Printed ciphertext, round 2 (24 September 2026)" | 0 rows | 0 survivors (180 passages, all judged table/noise with matched controls); nothing to triage |
| "Printed ciphertext (detector round 3, LANE S, 24 September 2026)" | W1 (1 row) | skip: found-solved |
| "Printed ciphertext (detector round 4, LANE S, 24 September 2026)" | 0 rows | 0 survivors (18 passages, all cipher-with-decipherment or table/noise); nothing to triage |
| "Printed ciphertext, HathiTrust detector (LANE N, 24 September 2026)" | HT1 (1 row) | **open, triaged below** |

The brief's "about 38 rows, about 32 never swept, 6 left open" does not match what is on disk today (26 rows
total, 24 of them one target's Thurloe rows). Reported as found, not reconciled against the estimate.

## Skipped (already closed)

- **P1** (`Archives ou correspondance inédite... Orange-Nassau t.III`, Lettre CCCLXXXV): row itself says
  `**found-solved, 23 Sept 2026**` — see `ciphers/orange-nassau-1572/NOTES.md`. Skipped per brief ("Skip rows
  already closed... found-solved").
- **W1** (`rikskanslerenax00styfgoog`, Gustav II Adolf to Oxenstierna, 23 Jul 1632): the QUEUE.md row text itself
  still reads "open, stage 2 verified unsolved (conditional)" as last edited, but ROOM.md 2026-09-24 06:26 UTC
  (LANE W worker C, VERIFIER) and STATUS.md line 516 both record the target moved to **found-solved / class N0**
  the same day: R. Torpadie, "Några ord om chifferskrift", *Historisk tidskrift* 8 (1888) pp. 376-383 (IA
  `historisktidskriftsv8`, page/382) prints the full plaintext and key table for this exact letter; the repo's own
  reading (control 98.0%) is an independent re-decipherment of an already-published solution, not a new one.
  Skipped as closed; QUEUE.md's own row text for W1 is stale and a one-line correction is worth a future editor's
  pass (not this brief's scope — ROOM.md/STATUS.md already carry the current status).

## Excluded

- **P2-P24** (23 rows, all of Thurloe State Papers vols. 2/3/5/7): `ciphers/thurloe-printed`, explicitly named as
  LANE T's in the brief's exclusion list (includes P3, P10 and the Stamford P4 the brief names by name). Not
  triaged beyond this line.

## Triaged: HT1

**The passage.** *Recueil des instructions données aux ambassadeurs et ministres de France depuis les traités de
Westphalie jusqu'à la Révolution française: Suède*, vol. 2, Commission des archives diplomatiques, printed 1884-85.
Two independent HathiTrust library scans agree: `njp.32101076191640` (scan seq 24) and `hvd.hl237b` (scan seq 26).
The signal is a **table-of-contents entry** ("TABLE DES CHAPITRES" header, body token "Chiffre" x2, capitalised) —
not itself a passage of ciphertext. Extent and cipher type are both **unknown**: the HTRC Extracted Features API
gives bag-of-words token counts with no word order, so it can confirm the word "Chiffre" appears near the front
matter but cannot say how long the chapter is, what page it starts on, or whether its content is raw ciphertext,
a decoded/keyed nomenclator table, or a narrative mention.

**Decipherment in print: not established either way — this is the open question.** What was read this pass: (1)
the HTRC EF counts already on file from the LANE N detector round (`sources/htrc/NOTES.md`); (2) a new check this
pass — Google Books now hosts a matching **full-view, public-domain scan** of this exact volume: `aFl0UpDNkusC`
("...Suède", 1885, `viewability: ALL_PAGES`, `pageCount: 638`, PDF downloadable) — this is a route the HT1 row
text doesn't mention (it says the TOC page image is "out of this brief's hosts", naming only babel.hathitrust.org
or a library copy). The book has no OCR text layer (`readingModes.text: false`, image-only), so it cannot be
grepped the way `_djvu.txt` can; the "search inside" HTML endpoint (`books.google.com/books?id=...&q=Chiffre`)
302-redirected rather than returning snippets from a plain curl (needs a real browser session or a different
entry point — not chased further, this is a locate-the-page step, not a solve). The chapter itself was not read.

**Key route:** none confirmed. If the "Chiffre" chapter turns out to be this genre's usual appendix — a printed
cipher/nomenclator table for the Sweden embassy, rather than raw undeciphered correspondence — it would be a
*published key*, useful for any unread Sweden-embassy cipher letter of the same period (e.g. AE Correspondance
politique Suède, not yet searched for a matching undeciphered passage). This is **inferred** from the genre
pattern (LESSONS.md: continental editions mostly print cipher as decoded plaintext or a key table, not blind
digits) and from precedent within this same series (Rikskansleren/Oxenstierna volumes print "the figures are:"
footnotes with the editor's own key), not confirmed for this specific chapter.

**EV:** 5/10. The first cheap test (find the TOC's actual page number, read that one page image, see whether the
chapter is a key table, a raw cipher passage, or neither) costs one page-image fetch and resolves nearly all the
present uncertainty; a Google Books full-view scan being available this session lowers that cost further than the
row currently states. Value is moderate either way it resolves (a usable key is a recovery lead; an unread cipher
passage is a fresh cryptanalysis/recovery candidate; a false positive costs nothing further). Not scored higher
because nothing here yet confirms the passage is cipher at all — the TOC entry could equally name a chapter that
only *discusses* the embassy's use of cipher in prose.

**Named first step:** per the intake gate, check-solved is the standing first step for any row going forward — but
check-solved presumes a located passage to search for, which HT1 does not yet have. The step before that (not
itself deep work): locate the "Chiffre" chapter's printed page number from the TOC (via the Google Books
full-view scan `aFl0UpDNkusC`, or a library reading-room copy of vol. 2 of this Recueil series) and read that one
page. Once the chapter's content is known, run check-solved on whatever it turns out to be before any further
work.

## Ranked table

| Rank | Row id | Passage | Key route | EV | First step |
|---|---|---|---|---|---|
| 1 | HT1 | Recueil des instructions...Suède vol.2, "Chiffre" TOC entry | none confirmed; inferred possible published key | 5/10 | locate TOC page via Google Books `aFl0UpDNkusC`, read it; then check-solved |

**TOP FOUR:** only HT1 survives exclusion/skip filtering this sweep — there is no second, third or fourth
candidate row among the ~38 the brief expected. P1 and W1 are closed (found-solved); P2-P24 are excluded
(thurloe-printed, LANE T's); rounds 2 and 4 returned 0 survivors each with matched controls.

**Counts:** 26 rows read across the five sections; 1 triaged open (HT1); 2 skipped as already closed (P1, W1); 23
excluded (P2-P24, thurloe-printed); 0 rows with a confirmed key route (HT1's is inferred, not confirmed). Vein
rated low to moderate, per the brief — this sweep's own contribution is a short negative-shaped result (24 of 26
rows are dead ends for this lane) plus one located, previously-unlocated-by-this-lane access route (Google Books
full view of the Suède volume) for the one open row.

**Hosts:** archive.org 2 requests (`advancedsearch.php`, >=1.5s apart, no `_djvu.txt` fetched — no new candidate
passage needed it); www.googleapis.com 2 requests (`books/v1/volumes` search + volume detail, >=1.5s apart, key
sent, `&country=US` set, never printed); books.google.com 1 request (search-inside HTML, 302, dead end, not
retried). No archive.org djvu fetch, no be-api, no data.htrc.illinois.edu call this pass (the HT1 EF counts were
already on file from the LANE N detector round; re-fetching them would have added nothing this triage needed).
No subagents used (triage was a single read-and-score pass, well under the 2-subagent cap). No logins, no other
credentials touched.
