# cylob-c1995

open
Minimal check-solved, 25 Sept 2026 (LANE B3 worker bCYL), before any transcription (intake step, `.claude/briefs/breadth.md`): Cipherbrain post 50 (Schmeh, 8 Feb 2017, scienceblogs.de/klausis-krypto-kolumne, this pass fetched to `sources/schmeh/posts/50-cylob.html`/`.txt` and the combined `?all=1` two-page render to `sources/schmeh/posts/50-cylob-all.html`/`.txt`) and its 7-comment thread read in full: no solution or reading posted by any commenter, only speculative hypotheses (piano/mixer-channel notation, computer print-statement guess, Maya glyphs, Pokemon room-design resemblance); Schmeh's own text says "So far, I haven't heard from anybody who has concrete knowledge about this cryptogram" and his favourite hypothesis is that it "is simply a piece of modern art without a real purpose." Both solver repositories grepped via shallow clone (github.com/dbourdeau/cyphersolver, github.com/aaymeloglu/unsolved-ciphers; cloned to /tmp, grepped, deleted, not committed): cyphersolver's `TARGETS.md` lists Cylob among items "open but not settleable by cryptanalysis" and `top50/NOTES.md` groups it with Blitz/Untersberg as "provenance or authenticity unresolved", no reading or key on file; aaymeloglu/unsolved-ciphers `SHORTLIST.md` lists Cylob under "No solve claims found ... on Schmeh's current unsolved page", status open. OpenAlex full-text search (api.openalex.org/works?search=, `Authorization: Bearer $OPENALEX_KEY`) for "Cylob cryptogram solved" returned 0 results. Semantic Scholar full-text search (api.semanticscholar.org/graph/v1/paper/search, `x-api-key: $S2_KEY`) for "Cylob cryptogram" returned 929 generic hits, none about this item (top results: a Nabokov literary-studies book, a phishing-detection CNN paper, an unrelated medical dose-finding study literally named CYLOB, an Adorno/Kafka essay, an optical-security paper). No standard printed edition applies (the booklet was picked up free in a London bookshop c.1995-96 and has no publisher, ISBN or library holding found or searched this pass; the primary sources are Cylob's own blog post and Schmeh's two Cipherbrain articles, both read this pass).

Status: open, unsolved by any source checked. Proceeding to cheap test 1 (fetch primary source, update spec) per brief `.claude/briefs/runs/2026-09-25-lane-b3-cylob-c1995.md`.

## Cheap test 1: fetch Cipherbrain post 50, update spec (25 Sept 2026, LANE B3 worker bCYL)

Fetched the post (`sources/schmeh/posts/50-cylob.html`, the default 2-page render) and, to get the full
article and all 7 comments in one extra request, its `?all=1` combined render
(`sources/schmeh/posts/50-cylob-all.html`; both converted to `.txt` with `tools/html2text.py`; sources/ are
unmodified snapshots per CLAUDE.md, not edited after saving). 2 requests to scienceblogs.de, >=1.5 s apart,
browser User-Agent, both HTTP 200.

Corrections to the spec from the primary source (`UNSOLVED-SURVEY.md` row 15 and the prior spec were built
from the survey's own summary, not this post):

- **Form, confirmed from the post's own text** (not the survey's paraphrase): "the Cylob cryptogram mainly
  consists of a sequence of rectangles containing geometrical patterns. The booklet doesn't contain any
  letters or numbers." This is not confirmed as a discrete fixed-size symbol alphabet the way the survey's
  "24 symbols" framing implies -- it reads as patterned rectangles, closer to the gold-bar/pictogram family
  Bourdeau already judged "not settleable" than to a classical substitution cipher. Cheap test 3 in the
  spec (grid-vs-cipher structural check) is upgraded from a proposal to the load-bearing next test.
- **"24 symbols (reader Torsten)"**: not found anywhere in this post or its comment thread (no comment
  signed "Torsten"; no symbol count given by Schmeh). This claim is not sourced to this post -- it likely
  comes from Schmeh's separate "List of Encrypted Books" page (linked in this post as item 00056, not
  fetched this pass, out of the brief's scope) or from UNSOLVED-SURVEY.md's own prior research. Left
  unconfirmed in the spec; do not treat it as established until traced to a primary source.
- **Provenance, confirmed**: British musician Cylob (Chris Jeffs) found a pile of free booklets in "Dillon's
  Arts" bookshop (later a Waterstone's), central London, c.1995-96. Cylob is not the author, only the
  finder; no second copy of the booklet is known to Schmeh.
- **Images, not fetched this pass** (the brief's cheap test 1 does not ask for the 20 grid-page scans; a
  later test): the post embeds 11 of the claimed 20 pages at `scienceblogs.de/klausis-krypto-kolumne/files/
  2015/05/Cylob-NN-614.png` for NN = 01..11 (reused from Schmeh's May 2015 German-language article on the
  same item, not refetched or re-hosted for this 2017 post), plus a small cover-bar thumbnail
  (`.../files/2017/02/Cylob-50-bar.png`). The remaining 9 of the 20 pages the post's text claims ("the book
  has 20 pages") are not embedded in either the paginated or the `?all=1` render of this post -- either a
  second, un-fetched source has the rest, or the post's embedded set is genuinely partial. Not resolved this
  pass.
- **New lead, not in the survey or the prior spec**: the post links "a partial transcription of the Cylob
  cryptogram" hosted at `https://cloud.rotering-net.de/public.php?service=files&t=4d7d9aaa54244fba485ad528a82fb050`
  (Schmeh's own Nextcloud share, not scienceblogs.de). Not fetched this pass -- the brief names
  scienceblogs.de only. This is the natural next cheap test: it may already give a transcription without
  needing to transcribe the 20 grid pages from scratch.
- **Date**: "about 1995 or 1996" per Cylob's own account, confirmed from the post (not independently
  narrowed further).

No control applies to a fetch; this step is not a cryptanalytic test and has no numbers to report.

## Web and blog check (GF-A2-11, 3 Oct 2026)

Run for LANE-A2PUSH (account 2), 3 Oct 2026, 00:30-00:38 UTC. WebSearch (plain web); hits opened with WebFetch.

(a) Plain web searches, four:
1. `Cylob cryptogram solved` -- hits: Cipherbrain post 50 (2017, both renders), Cipherbrain "revisited the cylob
   cryptogram" (18 Aug 2020), Cipherbrain "a booklet similar to the cylob cryptogram" (24 Nov 2020), the Top-50 list
   page, Futility Closet "The Cylob Cryptogram" (3 Apr 2026), Mathew Ingram's newsletter (16 Apr 2026).
2. `Cylob Chris Jeffs booklet Dillons bookshop strange symbols book` -- Boing Boing (?p=1109788), Cipherbrain 2020
   revisit, Futility Closet; the rest unrelated (symbol dictionaries, an alchemy forum).
3. `"Cylob-Manuskript" OR "Cylob manuscript" Rätsel` -- the Cipherbrain posts above plus the Orwell-1984 colour-cipher
   post (2016, a different item) and Boing Boing.
4. `"Cylob" cryptogram Futility Closet rectangles geometrical patterns booklet` -- the same set; nothing else.
No page found claims a solution, decipherment, author or meaning; every summary repeats "the meaning of all this has
never been discovered".

(b) Blog site searches:
- Cipherbrain: covered by searches 1-4 (all six Cylob posts/pages it has surfaced); the 2017 post 50 thread (7 comments)
  was read in full by bCYL, 25 Sept 2026, above.
- Cryptiana: `site:cryptiana.blogspot.com Cylob` -- no cryptiana page returned (only Cipherbrain and unrelated pages).
- Cipher Mysteries: `site:ciphermysteries.com Cylob` -- no ciphermysteries page returned; the site's own search for the
  related artist (`ciphermysteries.com/?s=Cointet`) finds one post, "Guy de Cointet's 'A Captain From Portugal'
  (1972)" (26 Apr 2022), opened below.

(c) Opened, comment threads read (WebFetch):
- Cipherbrain, "Cylob-Manuskript: ein ungelöstes Rätsel" (1 May 2015, German): 11 scans shown (Cylob-01..11), text
  says 22 pages; 15 comments, no pagination (Joe, Richard SantaColoma x3, emma, Klaus Schmeh x4, Dave, Gert Brantner,
  Thorsten, Philipp Bisson, Wolfgang Anschlag x2; 1 May 2015 - 31 Aug 2017). Hypotheses only (musicians' stage plan,
  factory floor plan, 1990s game copy-protection sheet, IQ test); "Thorsten" (2 May 2015) announces the transcription
  update; Wolfgang Anschlag (28-30 Aug 2017) proposes a symbol-to-letter substitution ("16 Symbole, das häufigste kommt
  17 Mal vor") and Schmeh answers "Diesen Ansatz müsste man weiterverfolgen" -- a proposal, no reading posted.
- Cipherbrain, "revisited the cylob cryptogram" (18 Aug 2020): three hypotheses (cipher, modern art, game accessory,
  with Elonka Dunin); 2 comments (TWO, 20 Aug 2020, "Spy IQ test"; David Oranchak, 13 Sept 2020, repeating elements
  between two pages). No solution.
- Cipherbrain, "a booklet similar to the cylob cryptogram" (24 Nov 2020): Guy de Cointet's "A Captain from Portugal"
  (1972) as a similar artist's booklet; 11 comments (Richard Bean, Armin x3, Klaus Schmeh x2, ShadowWolf x2, Matthew
  Brown, jan, a Cipher Mysteries pingback; 24 Nov 2020 - 26 Apr 2022). The decipherments posted there ("A CAPT AIN FR
  OM POR TUGAL", "like bands of pigmentation in the zebra ...") are of **de Cointet's** booklet, not the Cylob booklet;
  no comment attributes the Cylob booklet to de Cointet or anyone.
- Cipher Mysteries, de Cointet post (26 Apr 2022): mentions Cylob only through Schmeh's post title; 2 comments
  (Rossignol, nickpelling, 28 Apr 2022), neither about Cylob.
- Futility Closet (3 Apr 2026): no comments shown; "The meaning of all this has never been discovered."
- Mathew Ingram newsletter (16 Apr 2026): no comments shown; no solution claimed.
- Boing Boing (?p=1109788): HTTP 403 to WebFetch, not retried -- unreachable this pass.

Result: no decipherment, plaintext, identified author or meaning of the Cylob booklet found on the open web or in the
blog threads read.

## Premise check (GF-A2-11, 3 Oct 2026)

- **(a) Decipherments or transcriptions the folder mentions: transcription found, no decipherment.** The "partial
  transcription" link in post 50 (`cloud.rotering-net.de/public.php?service=files&t=4d7d...`, not fetched by bCYL) was
  opened this pass: an ownCloud share whose download is `Cylob-Manuskript.pdf` (application/pdf, 602,402 bytes, 12
  pages, sha256 0f9deae8ef6b313a2087cc3be944bfeea964afc80c334943a5d94bd351232082, PDF author "Thorsten Rotering", created 2 May 2015 -- the "Thorsten" of the 2015 thread). Page
  1 is a "Transkriptionstabelle" of 24 sign labels A-X with frequencies; its notes say the "Standardalphabet" has 16
  signs, the frequencies ignore sign doublings on pp. 1 and 3, and page 20 shows new signs read as simplified versions
  of standard ones (shown in brackets, e.g. C (N), D (Q)); the remaining pages give page images with the letter
  labels under them. This is the source of the "24 symbols (Torsten)" figure bCYL could not trace. It is a
  transcription only, no reading. Not committed (third-party file, licence unknown); URL, size and hash recorded here
  for a later transcription job. No other decipherment, gloss or clear copy is mentioned in this folder or its spec.
- **(b) Other solvers' working files: not found.** dbourdeau/cyphersolver HEAD 2341682 (2 Oct 2026): hits only in
  `TARGETS.md` (open, "not settleable by cryptanalysis"), `research/top50/` (NOTES.md, top50.txt/json/htm; provenance
  or authenticity unresolved), `research/catalogue_harvest/hcportal/index.json` and `targets/urquhart/src/list.json`
  (list entries) -- no target folder, transcription, output or solver run. aaymeloglu/unsolved-ciphers HEAD d2800bb
  (27 Sept 2026): `SHORTLIST.md` only (open, no solve claims), no working files.
- **(c) Physical neighbours: not found.** The item is a printed booklet with no known second copy (Schmeh, post 50). The
  "neighbours" are the booklet's other pages: the 2015 post shows 11 scans (01-11) while the texts say 20 or 22 pages;
  Rotering's PDF shows the pages he transcribed (pp. 1-20 by its own page labels). No clear text, key or note appears in
  any description of the booklet ("no letters or numbers, not even page numbers"). The nearest analogue, Guy de
  Cointet's 1972 booklet, was read in 2020 by Cipherbrain commenters; nobody links its author to the Cylob booklet.
- **(d) Recipient's side: not applicable / not found.** There is no addressee; the finder's side is Cylob's own account
  (read by bCYL via Schmeh's posts, 25 Sept 2026). No edition or archive applies.

Verdict of this pass: no decipherment or plaintext found; status stays `open`. Next-step note (not run): Rotering's
2015 transcription is on line and may serve as the second pass for any transcription job (rule 2: the scans decide).
Requests: WebSearch 6; scienceblogs.de 3 (WebFetch); futilitycloset.com 1; newsletter.mathewingram.com 1;
ciphermysteries.com 2 (site search, post); boingboing.net 1 (403); cloud.rotering-net.de 2 (share page, download).

`python3 tools/intake_gate_check.py cylob-c1995` after both sections (3 Oct 2026, GF-A2-11): `cylob-c1995: open (line 3) -- edition/page or full-text-search citation found within 6 lines`, exit 0 (exit 1 before).

## Next step (NO-CRACKS, 5 Oct 2026)

next: fetch Rotering's 2015 partial transcription PDF again (the cloud.rotering-net.de share named above), turn it into ciphertext.tsv and check one grid page against the scan before any solve (rule 2), ~$2. Who acts: agent. Source: this file's "Next-step note (not run): Rotering's 2015 transcription"; written by NO-CRACKS (account 3) because tools/next_steps.py found no next-step line in this file.

## Rotering 2015 transcription -> ciphertext.tsv; one page checked against a scan (R12D-CYLOB, 6 Oct 2026)

Run for LANE-RUN12-account-4, 6 Oct 2026, 15:45-15:50 UTC. No solve attempted.

- **Fetch.** `Cylob-Manuskript.pdf` from the cloud.rotering-net.de share above (the old `public.php?...&download` URL now
  307-redirects to `index.php/s/4d7d9aaa54244fba485ad528a82fb050/download`): HTTP 200, 602,402 bytes, sha256
  0f9deae8...2082 -- identical to the file GF-A2-11 recorded on 3 Oct. Not committed (third-party, licence unknown).
- **ciphertext.tsv** (190 rows: page, row, col, kind, sign) built by `rotering_to_tsv.py` from `pdftotext -bbox` word
  boxes (`--check` regenerates and exits 1 if stale). Transcription by Thorsten Rotering (2 May 2015), credited in the
  file header; conventions recorded there: labels A-X, 16-sign standard alphabet, C D E G H I K L only on p.20 (his
  "simplified variants": C~N D~Q E~O G~P H~S I~V K~T L~M); only dark-printed tiles transcribed, faded ghost tiles and
  picture panels not (picture rows kept as `-`); each page has one header sign above a 3-wide grid (6-wide on p.20,
  plus one sign under it, kind=trailer, column approximate); pp.2 and 4 blank; pp.1 and 3 carry only two signs each
  (A, P, the same on both); p.17 and p.19 have no transcribed sign, p.18 one picture only. 167 signs on pp.1-20.
  The PDF covers booklet pp.1-20 (Schmeh's texts say 20 or 22 pages).
- **Internal check against Rotering's own frequency table: exact match** (all 24 labels, total 157) when one of the
  duplicate pp.1/3 is counted once and p.20's standard-alphabet signs (A x3, B x2, F x2, J x1) are left out -- his
  note says the counts ignore the doublings on pp.1 and 3; the p.20 exclusion is inferred from the arithmetic, not
  stated by him.
- **Image check (rule 2), one page.** Scan: Schmeh's 2015 post image `scienceblogs.de/klausis-krypto-kolumne/files/
  2015/05/Cylob-07-614.png` (614x446, one spread; not committed, re-fetchable). `tools/iiif_lines.py --image` cut 14
  row bands that split the tall tiles in half, so the vision unit used the right half-page crop instead (one page, one
  call). Its layout (header + 5 rows of 3) matches only Rotering's p.13 among the five candidate pages (7, 10, 12, 13,
  15): T / Q J S / V Q F / J M N / R A A / U P X. Sign identity agrees on all 16 tiles: the repeated labels fall on
  identical shapes (Q at r1c1 and r2c2, the mirrored double-block; J at r1c2 and r3c1, the ringed dot; A at r4c2 and
  r4c3, the comb-top), and the other 10 labels fall on 10 mutually distinct shapes; all 15 grid tiles on that page are
  dark-printed, so nothing was skipped. This checks the transcription's partition into signs on one page, not the label
  names (arbitrary). Mapping noted: Cylob-07 right half = booklet p.13 (left half presumably p.12, not checked).
- **Not done / next.** The other 10 pages of the 2015 post (Cylob-01..11) have not been checked against the TSV; pp.21-22
  (if they exist) and the faded ghost tiles are untranscribed. Next cheap test on this TSV: spec cheap test 3
  (grid-vs-cipher structural check) with a matched control, ~$2.

Requests: cloud.rotering-net.de 2 (first without -L, 307; one follow-up); scienceblogs.de 1. All HTTP 200/307, no blocks.

## Spec cheap test 3: fixed discrete alphabet structural check, with matched control (R12D-CYL3, 6 Oct 2026)

Run for LANE-RUN12-account-4, 6 Oct 2026, 16:05-16:12 UTC (date -u). Disk only, no requests. Pre-registered in
`PREREG-test3.md` (pushed 0b48ed25e before the scored run); script `structural_test3.py` (seed 20261006, `--check` exits 1 if
`test3_results.json` is stale). Conditional on Rotering's 2015 partition into signs (rule 2; one page eye-checked by R12D-CYLOB).

Scored sequence: p.1 (once) + pp.5-16, header then grid rows: **N=140, K=16** (A B F J M N O P Q R S T U V W X). p.20 kept apart.

| statistic | target | English, fixed 26->16 map (300 seeds) mean [p05-p95] | uniform K=16 null p95 | order-shuffle null p95 | p (target vs null) |
|---|---|---|---|---|---|
| S1 index of coincidence | 0.0696 | 0.1008 [0.0804-0.1277] | 0.0667 | (invariant) | 0.0065 vs uniform |
| S2 repeated within-page trigram tokens | 21 | 24.7 [12-43] | 8 | 10 | <0.0005 vs shuffle |
| S3 repeated 3-sign grid rows | 4 | 3.9 [0-9] | 2 | 2 | 0.028 vs shuffle |
| bigram-repeat tokens (descriptive) | 70 | 86.1 [73-98] | 60 | 67 | 0.018 vs shuffle |
| new types in 2nd half (descriptive) | 1 | 1.0 [0-3] | 1 | -- | -- |

Gates (as pre-registered): **G0 power** S1 1.00 (pass), S2 0.677 (**fail**, below 0.80: at N=140 the English control beats its
own shuffle p95 on S2 only 68% of the time). **G1** alphabet skew: PASS (0.0696 > 0.0667). **G2** sequential structure: the
target's S2 (21) is far above the shuffle p95 (10) and S3 (4) above its p95 (2), but because G0 failed for S2 the pre-registered
rule makes G2 a non-test for licensing the verdict -- reported, not used. Neither S2 nor S3 is above the English p99.

Reading (cryptanalytic, no H/C tokens; nothing read):
- The inventory saturates: all 16 standard signs appear in the first half, 1 new type in the second -- a fixed discrete
  alphabet under Rotering's partition, not continuously varying patterns.
- It is skewed above a flat draw (G1), but **flatter than every one of the 300 English seeds** through a fixed 16-sign map
  (target IC 0.0696 below the English p05 0.0804; 100% of seeds >= target), and its bigram repetition (70) sits below the
  English p05 (73) while its trigram and whole-row repetition (21, 4) sit at the English median. Shape: little bigram texture,
  but whole units recurring (e.g. rows `TAP FJN` on pp.6 and 16) -- more like repeated blocks over a near-flat alphabet than
  like English letters through a simple many-to-one table. Not a refutation of a language cipher (a homophonic or
  nomenclator design, or another language, would be flatter); English through a fixed 16-sign map is disfavoured at this N.
- p.20 (descriptive): 25 tokens, 12 types, `LECKAI DJIEDG FEHGFB AEDCBA` + trailer G; its last row runs A E D C B A and the
  rows share runs (E D, F E/F B, D C B A), table-like rather than text-like. Not scored.

Spec verdict word: G1 pass, G2 non-test (G0 failed) -> "skewed fixed alphabet; order structure beyond shuffle observed but
not licensed at this N". Test 4 (English IC/frequency against this alphabet) is **not** licensed by this test's own gate, and
S1 already places the target below the English-through-16-signs control. One-line suggestion (not run): a design test on the
repeat structure itself -- positional placement of repeated rows/headers across pages and the p.20 table against a matched
synthetic grid -- before any language test, ~$2.
