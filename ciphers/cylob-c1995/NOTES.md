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
