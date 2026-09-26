LEADS REQUEST, label SO-BULLET-LEADS

We are an AI-assisted open cipher-research repository (github.com/NoAutopilot/cipher-lab; a person plus AI
agents). We are NOT asking you to verify a reading -- we want leads. Our cryptanalysis is parked: every family
we can license with a matched control has failed its control at this text length, and only new material (not a
different key or a different run of the same method) will move it.

THE ITEM
- A WW2-era message hidden inside a bullet, found near Villa Rossi, Tuscany, dated 13 August 1944 (Klaus
  Schmeh, Cipherbrain, "The Top 50 unsolved encrypted messages: 44. A WW2 encryption hidden in a bullet",
  4 March 2017). 44 letters, plus an indicator group "QM" and a footer "605YZ/FF".
- Our files: full search/test log https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/bullet-tuscany-1944/NOTES.md.
  There is no separate ciphertext.txt (44 letters, quoted in full in NOTES.md).
- Tests already run, each with a matched control:
  1. A forum "solution" reported by SPLOID (Jan 2015) is mechanically excluded (Schmeh himself already
     rejects it for lacking a method; we independently confirmed the mismatch).
  2. Caesar cipher: control 1.000, target FAIL. Excluded.
  3. 93 candidate keys drawn from the indicator groups QM, MQ, 605YZ/FF: control (true key) ranked 1st in
     3/3 trials; target scored 0/93 PASS, cribs at random-chance ceiling (1/12). Excluded.
  4. Periodic Vigenere/Beaufort/variant, periods 2-8: the control itself only recovered 5.3-6.1% against a
     0.6 (60%) gate -- CONTROL BELOW GATE, so no periodic key of period 2-8 has actually been tested at
     N=44; this is a non-test, not a negative.
  5. Indicator-format lookup against known WW2 systems: best structural fit is the US Army M-209 (matches
     the length and slash placement of a real M-209 manual example), but the digits in "605" break the
     letters-only rule that system requires, and the manual's own example runs indicator groups together
     rather than in a clean header/footer split; FM 24-5 message-heading forms and the one located Slidex
     source (Kruh, Cryptologia 8:2, 1984, p.162) give no fit at all; no M-94/M-138 indicator convention
     found either. A checklist control (two known real headers, correctly classified 2/2) backs the method,
     but the fit itself licenses no further test (the one thing it would license, footer YZFF as a key, is
     already excluded above).
- Net: this text is too short (N=44) for any periodic-key family's control to clear its own gate, so the
  target is parked, not closed.

WHAT WE HAVE ALREADY CHECKED (do not just repeat these)
- Cipherbrain post 44 and its full 9-comment thread.
- Both solver repositories (dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers): no hit.
- One OpenAlex and one Semantic Scholar query for "bullet cryptogram Tuscany 1944": zero results each.

WHAT WOULD ACTUALLY HELP (leads, not a verdict)
1. Any published account, museum record, war-diary excerpt, or unit history that identifies the actual
   cipher/code system in use by whichever unit (partisan, German, Allied?) this message belongs to, beyond
   Cipherbrain's summary.
2. Is there a second message from the same find (a second bullet, a companion document) anywhere in print or
   in a museum/collector's record? Our own next step, if this cipher is ever to move, is exactly that: more
   ciphertext from the same system, since 44 letters is too short for any periodic-key control to pass.
3. A cryptologist, WW2 signals historian, or collector who has written specifically about this item (a name,
   an article, a forum post, an auction listing) -- even one we should go verify ourselves.
4. Given the QM/605YZ/FF indicator groups and 44-letter body, does the format resemble any specific national
   system (Italian, German, Allied partisan) you recognise, that we have not already checked (M-209, M-94,
   M-138, Slidex, FM 24-5)?

HOW TO REPORT
- Write your answer as one Markdown file at `ciphers/bullet-tuscany-1944/second-opinions/chatgpt-leads-2026-09-26.md`
  in github.com/NoAutopilot/cipher-lab. Do not touch any other file. Create branch
  `second-opinion/SO-BULLET-LEADS` and open a pull request titled exactly
  `[SO-BULLET-LEADS] leads: WW2 bullet cryptogram, Tuscany 1944`.
- Header: `label: SO-BULLET-LEADS`, `model: <your model name and version>`, `date: <UTC date>`,
  `prompt: PROMPT-chatgpt-leads.md in this folder`, then leads under headings matching items 1-4 above.
- Every citation needs author, title, year, and a URL, or mark it "unverified". Never invent a page number.
- We are not asking for a verdict on whether this has ever been solved -- only a separate verifier on our side
  makes that call. Leads only.
