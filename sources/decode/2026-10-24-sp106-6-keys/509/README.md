# DECODE record 509, TNA_SP106/6_CharlesII_(0099-0101) -- match no. 32

**Verdict: match no. 32** (the alphabetical encoding table with person/town/country sequences, per
`sources/cryptiana/web/chauran.htm`'s structural description, quoted in
`ciphers/sp84-fuente-1662/NOTES.md` "## DECODE fetch (DECODE-KEY32, 24 Oct 2026)").

**Reason.** DECODE already carries a complete 2020 transcription of this record (two attached text documents,
`DOC_R509_D2952_2952.txt` for pages 2-3, `DOC_R509_D2953_2953.txt` for page 1, transcriber "AP", fetched this
pass, not re-transcribed here -- no new reading was done). Its structure, read directly from that text:

1. A single-letter substitution alphabet of 23 named marks (e.g. `InvertedLazySWithCurledEnds` = K,
   `OghamLetterUr` = B, `PlusSign` = C, `Verdigris` = E, `Soap` = F, `Arsenic` = G), each given as a
   `mark|code` pair -- A through Z (minus J/U, as usual for the period).
2. A labelled person-name sequence, codes in the 20s-70s (`2__0__` Le Roy, `2__6__` la Reyne, `2__2__`
   Madame, `2__8__` M^r le D. Dorleans, ... through 76, M^r Brilliamson), continuing past 76 with a `^'`
   superscript mark for high-ranking foreign figures (9' Estates of Holland, 10' Roy Despayne/Spain, 20'
   Reyne D'espaygne, 55' De Viequefort -- i.e. de Wicquefort/Wickfort, the correspondence's own addressee).
3. An explicit `<CLEARTEXT FR Villes>` heading, codes 61-89 (Calais, Amsterdam, Bordeaux, Boulogne, Bruxelles,
   ... Londres, Dieppe, Venise).
4. An explicit `<CLEARTEXT FR Royaulmes>` heading, codes 90-108 (la Pologne, la France, la Suède, la
   Hollande, ... l'Italie, l'Irlande, l'Alsace).
5. Several further word/syllable lists, each numbered roughly 1-100 and keyed by its own superscript
   homophone mark (`^..`, `^^`, `^"`, `^◡`, `^+`, plus the unmarked 1-100 series) -- common French function
   words and syllables (que, qui, les, des, nous, pour, ...), explicitly including nulls ("Nulls have already
   been transcribed in 3711.png").

This is exactly chauran.htm's "alphabetical encoding table (plain-to-code, alphabetical by word/syllable,
persons/towns/countries as separate sequences)" for no. 32 -- the persons/Villes/Royaulmes split is named in
the transcription itself, not inferred. No code anywhere in the transcription runs past 108 (persons/places) or
100 (the marked word lists): there is no sign of the "numbers up to 999" range chauran.htm assigns to the
different, second cipher (nos. 31/35), which rules those two out for this record.

**506.** DECODE's own "Additional Information" for 509 names id 506 as carrying "the same cipher" -- opened
this pass (see `../506/README.md`): confirmed, same 23-mark letter alphabet and the same person-code numbering
on 506's single page. 509 (3 pp, complete) is the fuller copy; 506 (1 p) duplicates its first section.

No key.tsv edit, no decode, no reading beyond citing DECODE's own existing transcription for the match
assessment (per brief: "no transcription, no reading, no key.tsv").

Images and documents stay in the session scratchpad (`sources/decode/NOTES.md`: raw DECODE images are not
committed); this folder keeps only this README and manifest.json (url, bytes, sha256, content-type, pixel
size) for a re-fetch.
