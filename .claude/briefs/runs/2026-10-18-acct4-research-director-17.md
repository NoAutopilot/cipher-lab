# Research director, wave 17 (18 Oct 2026, 09:1x UTC by date -u): rule-7 re-derivation and verifier, sherwood-cossit-1781

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself, `tools/experiment_log.py --check`). This session did not solve and does not protect the solver's conclusions.

## JOB SHERWOOD-VERIFY (account 4; Opus 5.5; cap USD 12; box 90 minutes; hosts: archive.org (11280377bsb page images, at most 40; full-text search), heritage.canadiana.ca (H-1737 frames 15-17 only, if needed), Google Books API (with &country=US and the key), OpenAlex/Semantic Scholar/CrossRef (keys), HathiTrust EF API, web search; JSTOR rows to JSTOR-QUEUE.tsv; Price: vision calls: 5 x USD 0.5 + 1 reconciliation = 3.5)

Target ciphers/sherwood-cossit-1781 (BL Add MS 21838 pp.345-347, the Cossit/Summer cypher to Justus Sherwood, Feb 1783). Claim under audit,
as NOTES.md "## Reading from Entick 1781" states it: the cypher is a page/column-line code into John Entick, *The New Spelling Dictionary*
(1781), and it reads: 216 pair rows graded H 8, C 4, S 147, M 55, I 2, agreeing with Sherwood's own p.84-85 paraphrase for messages 1 and 4.
Part A -- rule 7 re-derivation (do this first, from the spec, the key and the transcription only; do not read the solver's
entries_image.tsv or reading.txt until A2 is written):
A1. Blind re-read of the book cells: for the 167 distinct (P, W) cells the cypher uses, read both columns' W-th printed line yourself
    from the 11280377bsb page images (line crops by `tools/iiif_lines.py --image FILE --region ... --out DIR`, paste the commands; montage
    sheets of crops, never whole pages; 5 sheets), counting wrapped continuation lines as lines (the convention under test). Write
    verify/entries_blind.tsv.
A2. Then diff against book/entries_image.tsv: agreement per cell, and every disagreement settled from the image. Run
    `python3 decode_entick.py --check` and say whether the committed reading changes under your cells; per rule 7 a difference larger than
    the M-graded tokens sends the reading back (say so and stop Part B's class at "pending").
A3. Independently check the gate: does February 138-28 sit on line 28 of col 1 under the line-count rule, and do the other 7 anchors?
Part B -- verifier (CLAUDE.md "Verifier brief (template)", .claude/briefs/verifier.md): try to disprove novelty and over-claim. Search at
least: Brymner's Report 1888 and later Haldimand calendars; Collections of the Vermont Historical Society (vol. II, the Haldimand
negotiations); the Vermont State Papers and Governor and Council records; Mary Beacock Fryer, *Buckskin Pimpernel: the exploits of Justus
Sherwood, Loyalist spy* (1981) and any other Sherwood biography; scholarship on Ranna Cossit (Claremont, NH) and on Loyalist secret
service and dictionary codes (Entick, Bailey; Arnold-André as the comparison); Google Books phrase searches on distinctive decoded phrases
("Thunderclap", "One of the Thirteen Ship", "Colonel Strong" with "Windsor" and "sleighs"); the open indexes; Cryptiana, Cipherbrain,
Klausis; both solver repositories; DECODE. Log every family searched or unreachable. Append JSTOR-QUEUE.tsv rows in both families
(rule 10 (g)(i) and (ii)).
B1. Write AUDIT.md: N-class (rule 10) for the item with key source `ours` (codebook identified) and whether the plaintext is known; depth
    (rule 4a: share of cipher tokens H/C/S, D-level with the check used, and for D2+ one true sentence about the content that you write);
    safe and unsafe sentences; postmortem; correct every over-claiming sentence in the folder (NOTES.md, spec). If N3 or better, append the
    SECOND-OPINIONS-QUEUE.tsv row in this session. Run `tools/depth_check.py` if it applies and paste the output.
Report: A2 agreement and --check result, the gate, N-class, depth, safe sentence, five lines.
