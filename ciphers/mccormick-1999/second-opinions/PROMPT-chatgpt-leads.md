LEADS REQUEST, label SO-MCCORMICK-LEADS

We are an AI-assisted open cipher-research repository (github.com/NoAutopilot/cipher-lab; a person plus AI
agents). We are NOT asking you to verify a reading -- we want leads, because our own cryptanalysis has run
every family we can license with a matched control and come up empty on this famous, already widely-attempted
target.

THE ITEM
- Ricky McCormick's encrypted notes: two handwritten notes (about 30 and 33 lines, 746 letters total) found
  in his pocket after his body was found in a field near St. Louis, Missouri, in June 1999. FBI's own
  codebreaking unit (CRRU) and the American Cryptogram Association have both failed to solve it (per Klaus
  Schmeh's account, "The Top 50 unsolved encrypted messages", entry 10).
- Our files: notes and full search/test log https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/mccormick-1999/NOTES.md,
  the four solver families we ran with their controls https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/mccormick-1999/HYPOTHESES.md.
  There is no separate ciphertext.txt: the working text is the transcription embedded in the family test files
  under `ciphers/mccormick-1999/families/`, since the notes are handwritten symbol/letter groups, not a single
  clean alphabet.
- Tests already run, each against a matched control before the target:
  1. IC/n-gram test: language-like structure (not random), vowel share below normal prose but above zero.
  2. Simple substitution (masc), N=746: English control 0.994 (0.989-0.999) vs target FAIL (-1.48 vs real
     p05 -0.864). Excluded.
  3. Homophonic substitution K=24, N=746: English control 0.998 vs target FAIL (-1.48); a false-positive
     floor check (the target's OWN letters shuffled three ways) scored the same FAIL band as the real target
     (-1.81 to -1.90) -- so this anneal cannot tell the real text from its own shuffle at this length; letter-
     substitution families say nothing about this cipher either way at N=746.
  4. Token/nomenclator anneal over the 132 distinct groups: the control (same scheme, 3 seeds) recovered only
     0.8% against a 0.5% gate -- CONTROL BELOW GATE, not a real test of the code-word hypothesis.
- Net: every letter-substitution family we can run is excluded with a passing control; the code-word/shorthand
  family is untested because we cannot build a control that reads anything at only 132 tokens.

WHAT WE HAVE ALREADY CHECKED (do not just repeat these)
- Cipherbrain (Schmeh) post 10 and its full 6-comment thread, including the taringa.net "solution" claim,
  which is a homophone-guessing exercise ("8=eight=ai=a") already rejected by that thread's own commenters, not
  a real decipherment.
- Both solver repositories (dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers): no hit.

WHAT WOULD ACTUALLY HELP (leads, not a verdict)
1. Known keys, codebooks or personal shorthand systems documented for this case specifically (has anyone
   published a claimed key, a partial code table, or a description of McCormick's own habits -- e.g. a
   Gregg-shorthand or homemade-abbreviation background -- from a source we might not have seen)?
2. Any printed source (a book, a documentary transcript, a court record, a forensic report) that quotes or
   discusses the notes' content beyond what Cipherbrain already covers.
3. A cryptologist, forensic linguist or amateur solver who has written specifically and seriously about this
   case (a name, an article, a forum thread, a video) -- even one whose claim we should go verify ourselves.
4. Given that letter-substitution is excluded with passing controls and the code-word family's own control
   cannot yet read anything at 132 tokens, what would you try first: a longer synthetic control to find the
   token count where a code-word anneal starts to work, a specific abbreviation-lexicon-constrained search
   (e.g. Gregg shorthand, a period slang/street-code list), or something else entirely?

HOW TO REPORT
- Write your answer as one Markdown file at `ciphers/mccormick-1999/second-opinions/chatgpt-leads-2026-09-26.md`
  in github.com/NoAutopilot/cipher-lab. Do not touch any other file. Create branch
  `second-opinion/SO-MCCORMICK-LEADS` and open a pull request titled exactly
  `[SO-MCCORMICK-LEADS] leads: Ricky McCormick's encrypted notes, 1999`.
- Header: `label: SO-MCCORMICK-LEADS`, `model: <your model name and version>`, `date: <UTC date>`,
  `prompt: PROMPT-chatgpt-leads.md in this folder`, then leads under headings matching items 1-4 above.
- Every citation needs author, title, year, and a URL, or mark it "unverified". Never invent a page number.
- We are not asking for a verdict on whether this has ever been solved -- only a separate verifier on our side
  makes that call. Leads only.
