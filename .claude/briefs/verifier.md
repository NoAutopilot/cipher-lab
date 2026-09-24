# Verifier (Fable, cap $30)
Read CLAUDE.md (rule 10, Workers). Target: <folder>; claim under audit: <sentence>. You are adversarial: try
to disprove novelty. Extract exact date, parties, plaintext, ciphertext, identifiers. Search by metadata and
by quoted plaintext phrases across: canonical editions (all series and indexes), sender- and
recipient-specific correspondence editions, the holding archive's catalogue and blog, the transcription
project's pages, Google Books, HathiTrust, Internet Archive, GitHub cipher projects, scholarship through the open
indexes (OpenAlex, Semantic Scholar, Persée, HAL, CrossRef); JSTOR queries go as rows into JSTOR-QUEUE.tsv and never
block a class on their own. Log every
family searched and every one unreachable. Write AUDIT.md: verdict table with N-class per item, per-item
sections, evidence table, "did we first-decipher?", confidence, postmortem, and correct every over-claiming
sentence in the folder. + common tail.
If you re-date or re-attribute the item from the plaintext, the edition search widens to every volume of the series
within two years of every plausible date and under every candidate sender; it never narrows. Read the volume's
Regesten by date and source note, not by phrase. Lesson of Dupuy 468, 23 Sept 2026.
Search the holding archive's full text across the whole collection (e.g. CONTENTdm dmQuery on the collection), not only the
item's own record: duplicates and letter-book copies live elsewhere. Lesson of Eckert 1864 second audit, 24 Sept 2026.

## Second opinions from outside models

The owner pastes the board's second-opinion prompts into ChatGPT or another model and files the answers at
`ciphers/<target>/second-opinions/<model>-<date>.md`, verbatim, one file per answer. A verifier treats such a file as a
list of leads, never as a verdict: every citation in it is checked against the source itself (an edition page, a
catalogue record, a DOI), confirmed leads go into AUDIT.md's search log with the source, invented or unverifiable
citations are listed in AUDIT.md under "Second-opinion claims not confirmed" so nobody chases them twice. The class
moves only on a confirmed source. A ROOM.md line `for LANE V: <target> second opinion filed` announces each file.
