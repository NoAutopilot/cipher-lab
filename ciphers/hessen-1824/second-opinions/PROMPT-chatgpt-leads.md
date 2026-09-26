LEADS REQUEST, label SO-HESSEN1824-LEADS

We are an AI-assisted open cipher-research repository (github.com/NoAutopilot/cipher-lab; a person plus AI
agents). We are NOT asking you to verify a reading -- we want leads. Every solver family we can run has either
failed a passing control or failed to build a working control at all at this text's length.

THE ITEM
- A Hessian polyalphabetic message, dated 20 Feb 1824, held at Hessisches Staatsarchiv Marburg, 9 a Nr. 259
  f.249 (catalogued via HCPortal, item 513). N=164 letters, one blind transcription on file (no second pass
  yet).
- Our files: full test log https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/hessen-1824/NOTES.md,
  our solver runs with controls https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/hessen-1824/HYPOTHESES.md.
  There is no separate ciphertext.txt; the transcription is embedded in the family test files under
  `ciphers/hessen-1824/families/`.
- Tests run, each against a matched control, first on a German corpus built from 1880-1940 sources (an era
  gap against this 1824 letter), then on a purpose-built 1810s-20s corpus (Goethe's Italienische Reise,
  Chamisso's Peter Schlemihl):
  1. Periodic Vigenere, periods 6/7/16: control 1.000, target FAIL. Excluded.
  2. Simple substitution (masc): control 0.823, target FAIL. Excluded.
  3. Homophonic substitution (same decode as masc): control 0.878, target FAIL. Excluded.
  4. Running-key cipher, on the era-mismatched 1880-1940 corpus: control itself only reached 0.372 against a
     0.6 gate -- CONTROL BELOW GATE, non-test.
  5. Running-key cipher, on our own purpose-built 1810s-20s corpus (tools/data/de19, ~1.04M letters; its own
     held-out false-negative rate is a noisy 39.3% blended over only 3 folds, so it is of admittedly unknown
     reliability): control-only mean 0.331 (0.213-0.457) at beam width 6000, and byte-identical results at
     beam width 15000 (so not simply beam-limited) -- still CONTROL BELOW GATE. The target itself was never
     even run, since its own control never cleared the bar.
- Net: every letter-substitution family is excluded with a passing control; running-key is untestable at
  N=164 with our solver on either corpus we tried.

WHAT WOULD ACTUALLY HELP (leads, not a verdict)
1. Is there more ciphertext from the SAME system -- other letters in HStAM 9 a Nr. 259, or a sibling series,
   that we could pool to get past N=164 (running-key ciphers typically need much more text than substitution
   ciphers to solve, which may be exactly why our control itself cannot clear the gate at this length)?
2. Any published catalogue description, finding aid, or archival-history article (Hessisches Staatsarchiv
   Marburg's own publications, a Hessian regional-history journal) that names the correspondents, the context,
   or even a candidate key/running-key source text for 1824 Hessian diplomatic or administrative ciphers.
3. A scholar of early-19th-century German diplomatic cryptography, or of Hessian state-archive holdings from
   this period, who might know this item or this cipher system.
4. Given that our running-key solver's OWN control cannot clear its gate at N=164 even with an era-matched
   corpus, would you recommend a different solver/method for short running-key ciphers, or is more ciphertext
   really the only lever here?

HOW TO REPORT
- Write your answer as one Markdown file at `ciphers/hessen-1824/second-opinions/chatgpt-leads-2026-09-26.md`
  in github.com/NoAutopilot/cipher-lab. Do not touch any other file. Create branch
  `second-opinion/SO-HESSEN1824-LEADS` and open a pull request titled exactly
  `[SO-HESSEN1824-LEADS] leads: Hessian polyalphabetic message, HStAM 9 a Nr. 259, 1824`.
- Header: `label: SO-HESSEN1824-LEADS`, `model: <your model name and version>`, `date: <UTC date>`,
  `prompt: PROMPT-chatgpt-leads.md in this folder`, then leads under headings matching items 1-4 above.
- Every citation needs author, title, year, and a URL, or mark it "unverified". Never invent a page number.
- We are not asking for a verdict on novelty -- only a separate verifier on our side makes that call. Leads
  only.
