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
