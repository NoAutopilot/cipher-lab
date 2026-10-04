# NEAR3-VHEL -- VERIFIER for hellen-frederick-1752 (4 Oct 2026, written by LANE-NEAR3, account 2 / ytbiz)

Model: Opus. Cap USD 8; box 60 min, whichever first. You are a verifier, a session separate from every solver of this target; do not
protect the solvers' conclusions. Common rules: the "Common to every job below" section of `.claude/briefs/runs/2026-10-04-ytbiz-near3-wave1.md`
(room.py start/claim/push, no dollar figures, no AskUserQuestion). Claim: `python3 tools/room.py "NEAR3-VHEL (account 2 verifier, for LANE-NEAR3)" 'claim: hellen-frederick-1752 verifier (AUDIT.md); box ends <HH:MM> UTC'`.

VERIFIER: ciphers/hellen-frederick-1752. Claim under audit: the R1953 (Hellen, The Hague, to Frederick II, 4 Jan 1752) partial reading under
DECODE R4369 (BL Add MS 32276 f.44, the English Deciphering Branch's key "Hellen avec le Roy de Prusse", codes 801-1796), as NOTES.md
"READ2-HEL" and NEAR.md state it: H 152 S 304 M 16 U 374 of 846 tokens; attribution LR100 beats value-shuffle and order-shuffle controls
(p 0/200, power 1.00); judge FAIL near gate; rule-7 re-derivation 845/846 (READ2-HELRD; the one difference a `~` convention now in
key_r4369/README.md). R4370 (READ2-HEL2) and R4372 (NEAR3-HEL4) were tested as the codes 1-800 half and FAIL.
1. Extract from the repo, per item: date, sender, recipient, place, plaintext as read (`key_r4369/reading_R1953.txt`), ciphertext,
   distinctive phrases (5-10 runs of H/S words), archive identifiers (DECODE R1953, R4369; BL Add MS 32276; any GStA PK / NA shelfmark in
   NOTES), and exactly what the solvers searched (check-solved sections, Politische Correspondenz vols 9-10/13/23, web/blog check,
   solver-repo check, premise check), with dates.
2. Search independently (CLAUDE.md "Verifier brief" families a-g): (a) Politische Correspondenz (Frederick's side) by date 1752 and
   Hellen; (b) Hellen's own reports -- any edition or study of the Prussian legation at The Hague 1750s, Acta Borussica, GStA PK Rep. 96
   finding aids; the English side: BL Add MS 32276 descriptions, any study of the Deciphering Branch's Prussian work (e.g. Ellis, Willes,
   the Bodleian/BL Willes papers; Kenyon/Ellis studies of the Deciphering Branch); (c) documentary editions for the period (e.g. Recueil
   des instructions, Dutch Stadhouder correspondence); (d) DECODE's own record pages R1953/R4369 (login-free listing in sources/decode;
   do NOT log in -- this job reads only what is on disk or login-free); (e) full-text: archive.org be-api and advancedsearch, Google Books
   API with `&country=US&key=$GOOGLE_BOOKS_KEY`, HathiTrust via HTRC EF only; (f) Bourdeau's and Aymeloglu's repositories (grep for Hellen,
   R1953, 4369), Cipherbrain/Cryptiana; (g) OpenAlex (header `Authorization: Bearer $OPENALEX_KEY`), Semantic Scholar (`x-api-key: $S2_KEY`,
   1.1 s), CrossRef, HAL; and append JSTOR-QUEUE.tsv rows in BOTH families (i) sender/recipient/date + cipher keyword and (ii) a bare quoted
   phrase from the decoded text with no cipher keyword. Phrase-search the decoded text (`tools/print_check.py ciphers/hellen-frederick-1752`
   if phrases.txt can be built from the reading; read its --help). Log each family as searched or unreachable, with what was searched.
3. Classify the item N0-N5 (rule 10) with: prior plaintext (yes/no, where, earliest citation), prior decipherment (yes/no), evidence
   quality, confidence, key source (`period`: R4369 is a period key sheet rebuilt by us), one safe sentence, one unsafe sentence. A partial,
   cryptanalytically supported reading (no H for codes 1-800) is classified as what it is; say what fraction it covers.
4. Postmortem: name over-claiming sentences in the folder's files, NEAR.md row and STATUS.md "LANE READ2 handoff" and correct them.
5. Write `ciphers/hellen-frederick-1752/AUDIT.md`; if N3 or better, append the SECOND-OPINIONS-QUEUE.tsv row in the same push (CLAUDE.md
   Operating model). Commit and push; done line with the class, the safe sentence, families searched/unreachable, requests per host.
Do not decode, do not touch other targets, do not print or commit credentials, never log in to DECODE.
