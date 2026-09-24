# Project one-pager (shared by every application)

Attach or paste this where a programme asks for a project summary or a supporting document. Numbers are from
`status.json` and the targets' `AUDIT.md` files as of 24 Sept 2026, 13:28 UTC; refresh them before sending.

**cipher-lab: reading undeciphered historical cipher letters with AI agents, under a verifier protocol**

Principal investigator: [your name], independent researcher. Repository (public):
https://github.com/NoAutopilot/cipher-lab

**The problem.** European archives hold thousands of diplomatic and military letters written in cipher between
about 1450 and 1870. Many were never deciphered, or were deciphered on a separate sheet that was filed in another
box. Specialist lists such as S. Tomokiyo's Cryptiana and the DECODE database (de-crypt.org) record hundreds of
items still marked unsolved. Two open solver projects (dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers) have
worked through much of that list. What is left needs catalogue work outside DECODE, page images from the holding
archives, and careful checking against printed editions.

**The method.** One person directs a team of AI agent sessions (Claude). Each session does one job: scout,
check-solved, transcription, key recovery, solving, or verification. Readings are reproducible: a script
regenerates each reading from the transcription and the key and fails if the committed reading is stale. Every
decoded token is graded (H from a key source, C from known plaintext, S cryptanalytic with a matched control,
M uncertain, I inferred). No negative result is reported without a synthetic control of the same length, design
and language. A separate verifier session then searches editions, catalogues, full-text libraries and scholarship
to disprove novelty, and assigns a class from N0 (already known) to N5 (confirmed by the holding archive).

**Results so far (about one week of work, 17 to 24 Sept 2026).**

- 15 cipher passages classed N4: no prior decipherment located after a logged search, each after two independent
  audits. They come from seven groups of letters: Gramont to Villandry and to Francis I, Rome 1530 (BnF fr. 2980);
  Danzay to the Cardinal of Lorraine, 1557 (BnF fr. 20140); two Union telegrams to Butler, April 1864 (Huntington
  Eckert papers); Stamford to Thurloe's office, 1655 (Birch 1742); three Blathwayt intelligence items, 1727-29
  (Huntington mssBLA); three letters of Lodewijk van Nassau to William of Orange, 1573-74; three items of the
  Orange and Elector August of Saxony correspondence, 1561-64. One of the fifteen was read cryptanalytically,
  without any key source (WVO 53: 238 of 364 tokens at grade S, 126 uncertain).
- 13 items shown to be already solved or printed before any solver time was spent on them, and 5 catalogue
  corrections (for example, BnF Dupuy 468 f.28: the leaf catalogued as Anhalt 1515/16 is the Latin cipher original
  of a letter printed in French in 1896).
- 3 negative results with matched controls, and 13 datasets and tools handed on (machine-readable keys, a
  printed-cipher detector run over 914 editions, catalogue sweeps of 493 items outside DECODE).
- 33 shared scripts with offline tests; 19 audit files that log every source searched and every one unreachable.

**Why it matters.** The readings restore lost passages of diplomatic correspondence, give archives corrected
catalogue entries, and give the cipher-history community keys and datasets they can check. The project is also a
worked record of how AI agents over-claim and how a verifier protocol catches it: in the first week the verifier
sessions downgraded several claims before they left the repository.

**What support would do.** Model usage is the bottleneck. The project runs on one personal subscription whose
usage window stops all work when it is spent. Credits or a stipend would pay for more solver and verifier sessions,
copy orders from archives (The National Archives, the British Library, German state archives), and database access
(JSTOR, Gale State Papers Online) for the verifier's searches.

**Open access.** Everything is public on GitHub: transcriptions, keys, readings, audit logs and tools.
