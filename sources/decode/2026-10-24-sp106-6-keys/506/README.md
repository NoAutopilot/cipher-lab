# DECODE record 506, TNA_SP106/6_CharlesII_(0096) -- match no. 32

**Verdict: match no. 32**, confirmed (previously an unopened lead, see
`ciphers/sp84-fuente-1662/NOTES.md` "## DECODE fetch (DECODE-KEY32, 24 Oct 2026)": "id 509's own Additional
Information names this record as carrying 'the same cipher'; not independently opened this pass").

**Reason.** 506's own attached text document (`DOC_R506_D2951_2951.txt`, transcriber "AP", 10 Aug 2020,
status complete) opens with the identical 23-mark single-letter substitution alphabet as record 509 --
`CapitalLetterSCrossedByACrossBar` = A, `OghamLetterUr` = B, `PlusSign` = C, `Verdigris` = E, `Soap` = F,
`Arsenic` = G, etc., same `mark|code` pairing -- followed by the same person-name codegroup numbering (20
Le Roy, 26 la Reyne, 23 la Reyne mere, 22 Madame, 24 M^r le Prince, ...) continuing into the same range as 509's
persons list. 506 is a single page (3705.png) and does not carry 509's Villes/Royaulmes/word-list continuation
(pages 2-3 of 509 only) -- it is the shorter, overlapping copy DECODE's own cross-reference described, not a
second cipher. Same conclusion as 509's README: this is no. 32 (the alphabetical, person/town/country encoding
table), not the up-to-999 numeral system of nos. 31/35.

No key.tsv edit, no decode, no reading beyond citing DECODE's own existing transcription for the match
assessment (per brief).

**Correction (job KEY32-TSV-PROMOTE, 24 Oct 2026):** the "does not carry 509's Villes/Royaulmes/word-list
continuation" claim above is wrong. Re-reading 506's full attached text to build
`ciphers/sp84-wickfort-bacquoy-1660-63/key.tsv` found 506 does carry its own `<CLEARTEXT FR Villes>` and
`<CLEARTEXT FR Royaulmes>` sections and a complete word/syllable homophone list through to Z and the null row --
506 is one physical page of very dense writing, not a partial table. Cross-checking the two sources' overlapping
codes found 210 of 549 shared (class, code, mark) keys (38%) carry a different `meaning` string between 509 and
506 -- mostly small spelling/reading variants on the same name (e.g. person code 21: "le Duc Danjou" in 509 vs
"M^r le d. Danine" in 506), logged per CLAUDE.md rule 4 as data conflicts in key.tsv's `note` column, not
resolved by majority. See `ciphers/sp84-wickfort-bacquoy-1660-63/NOTES.md` "## Key" for the full detail.

Images and documents stay in the session scratchpad (`sources/decode/NOTES.md`); this folder keeps only this
README and manifest.json for a re-fetch.
