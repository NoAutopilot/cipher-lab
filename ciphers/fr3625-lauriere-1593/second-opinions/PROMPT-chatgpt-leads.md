LEADS REQUEST, label SO-LAURIERE-LEADS

We are an AI-assisted open cipher-research repository (github.com/NoAutopilot/cipher-lab; a person plus AI
agents). We are NOT asking you to verify a reading -- we want leads. We have a partial match on a candidate
key sheet and cannot get further without more material.

THE ITEM
- A letter from Lauriere to the duc de Nevers, Chalons, 9 July 1593, Bibliothèque nationale de France, ms.
  français 3625, no.55. 86 cipher groups; 19 of them already read by Daniel Bourdeau
  (github.com/dbourdeau/cyphersolver).
- Our files: full search/test log https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/fr3625-lauriere-1593/NOTES.md.
- What we found: a candidate period key, BnF fr.3995 no.57 (identified via Tomokiyo's catalogue as
  "Laveriere to Nevers, Feb-Aug 1593", fol.103 fold-out -- the same correspondent pair and exact date range),
  tested against 12 code-value anchors taken from a glossed sibling letter (fr.3625 no.10): 4 of 12 match
  exactly (code 335 = pape, 59 = du, 346 = volonté, 25 = que) against a 1000-shuffle control mean of 0.072
  (p99 = 1, max = 2) -- a real, control-backed margin, but short of the 6/12 gate we pre-registered before
  running it. The misses look structured, not random: no.57's code 335 = soit and 141 = catholique, while
  fr.3625's own key has 141 = soit and 288 = Catholique -- consistent with a RENUMBERED word bank from the
  same chancery rather than an unrelated sheet, but not proven.
- We also checked whether any other nearby fr.3995 key sheet (nos. 58, 66, 61, 45, all 1592-94) could host
  the same 12 anchors: none can, on structural grounds alone (no.58's numeral word-bank caps at 99, too small
  for several of our codes; nos. 66/61 have no numeral word-bank at all, coding by single symbols or spelled-
  out letters instead; no.45 alphabetises its word list differently and disagrees with fr.3625 on the one
  comparable anchor) -- so no.57 remains the single best partial match on file, not one of several candidates.

WHAT WOULD ACTUALLY HELP (leads, not a verdict)
1. Is BnF fr.3632 no.8, a second glossed Lauriere letter we have identified but not yet obtained (it is not
   digitised; a physical/digitisation request would be needed), likely to carry more of the same code values
   as fr.3625 no.10? Anything you can find about fr.3632's contents or a finding-aid description would help
   us decide whether to pursue that request.
2. Any published edition or calendar of Lauriere's, or the Nevers chancery's, 1593 correspondence (League-
   period Nevers papers, a regional-history bulletin for Champagne/Chalons, a study of French royal or League
   ciphers of the 1590s) that might independently corroborate or extend the renumbered-word-bank hypothesis.
3. A scholar who has written on Tomokiyo's or Bourdeau's identified 1590s French chancery key families, or on
   BnF fr.3995 specifically (it appears to be a compiled key-book covering many correspondents of this
   period).
4. Given a real but sub-gate margin (4/12 exact vs a 0.072 shuffle mean, needed 6/12), and no other candidate
   sheet even structurally able to host these anchors, is a full transcription of no.57's entire word bank
   (not just the 12 anchors) checked group-by-group against no.55 worth doing, or should we wait for the
   fr.3632 request first?

HOW TO REPORT
- Write your answer as one Markdown file at `ciphers/fr3625-lauriere-1593/second-opinions/chatgpt-leads-2026-09-26.md`
  in github.com/NoAutopilot/cipher-lab. Do not touch any other file. Create branch
  `second-opinion/SO-LAURIERE-LEADS` and open a pull request titled exactly
  `[SO-LAURIERE-LEADS] leads: Lauriere to Nevers cipher, BnF fr.3625 no.55, 1593`.
- Header: `label: SO-LAURIERE-LEADS`, `model: <your model name and version>`, `date: <UTC date>`,
  `prompt: PROMPT-chatgpt-leads.md in this folder`, then leads under headings matching items 1-4 above.
- Every citation needs author, title, year, page, and a URL, or mark it "unverified". Never invent a page
  number.
- We are not asking for a verdict on novelty -- only a separate verifier on our side makes that call. Leads
  only.
