# OpenAI, "On the Navier-Stokes Millennium Prize Problem" (8 Sept 2026)

Fetched 25 Sept 2026, 16:40-16:50 UTC, by parent 7c at the owner's request ("take how they broke this as
inspiration, add to our gold target approaches").

- `https://openai.com/index/navier-stokes-solution/`: HTTP 403 to curl with a browser UA (one request), 403 to the
  fetch tool, a "Just a moment..." Cloudflare page to headless Chromium (one request), and the Wayback CDX index reset
  the connection (one request). Not retried further (good-citizen rule). The page text is therefore known here only
  through the coverage below.
- `navier-stokes.pdf` (2.96 MB, HTTP 200 from cdn.openai.com): the paper, "Finite time blowup for Navier-Stokes",
  kept as the primary source. No PDF text extractor is installed in this container (pypdf's cryptography binding is
  broken, no pdftotext); the next worker that needs the acknowledgements or methods paragraph should install one.
- Coverage read (25 Sept 2026): unite.ai, "OpenAI says internal AI system resolved the Navier-Stokes problem";
  search-result summaries of Neowin (403 to the fetch tool), The Tufts Daily, miraflow.ai, ecuacionganadora.com;
  arXiv 2609.17642 (a follow-up paper, title only).

## What the coverage says about the method (quoted where the source quoted OpenAI)

- Claim: an analytical proof plus a Lean formalization that the three-dimensional Navier-Stokes equations with a
  smooth, compactly supported force develop a singularity in finite time (the forced case; the unforced Euler
  regularity problem was resolved by about 100 agents first, in about 50 hours). Released 8 Sept 2026. The Clay
  Mathematics Institute's evaluation is "deliberately unhurried"; OpenAI "does not intend to claim the Millennium
  Prize". A priority dispute on the forced Euler case (Alpöge and Buckmaster, Lean-verified 22 Aug 2026) was
  acknowledged by OpenAI.
- System: "a system of coordinating agents powered by the internal model, with access to a cached version of the
  internet and the ability to run code, subdivided into groups that could communicate within each group"; "on the
  order of 10,000 concurrent agents".
- Timeline: launched 1 Sept 2026; resolution "about 88 hours after the first agents were launched" (5 Sept); a
  further 17 hours for the Lean formalization and verification.
- Volume: across all attempted problems "4.9 million messages and about 300 billion output tokens"; the
  Navier-Stokes work "2.7 million messages and approximately 130 billion output tokens".
- Iteration: agents were first pointed at the easier sibling problem (unforced Euler), then "shifted to
  Navier-Stokes, prompted with the Euler resolution, updated to a further-trained version of the model mid-effort",
  and a separate tool (Codex) was "used to consolidate the most useful insights" for the next round.
- Verification: the Lean check is what confirmed validity; the human evaluation is separate and ongoing.

The lessons drawn for this repository are in UNSOLVED-SURVEY.md ("What the Navier-Stokes result adds") and
PROCESS-2026-09-24.md (proposal 6, the standing gold lane).
