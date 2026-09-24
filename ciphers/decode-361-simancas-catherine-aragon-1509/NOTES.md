# Catherine of Aragon to King Ferdinand, 3 November 1509, Archivo General de Simancas

**Status: found-solved.**

## Item

DECODE R361 ("Non-decrypted" in DECODE's own status field as of the 24 Sept 2026 catalogue crawl). Metadata
(Aymeloglu `decode-records.jsonl`): Author "Catherine of Aragon", Start date 1509-11-03, holder "Archivo
General de Simancas, España", 3 pages, cleartext language Spanish, `Available Documents: Cleartext
Publication`. QUEUE.md row **DC7** (section "DECODE non-decrypted records with images (LANE N diff of 24
September 2026)") additionally records two attached documents on the RecordsView page: an "envelope
[cleartext]" image and a "paleography study [pub]" PDF, scored `held_by: none`, next step "search-print" — the
next step was correct in spirit; the record is in fact already found solved and published.

Brief: `.claude/briefs/runs/2026-09-24-lane-n-csDC2.md`. de-crypt.org and archive.org not queried directly by
this worker (held by other LANE N workers this session); worked from committed TSVs, QUEUE.md, and Tomokiyo's
Cryptiana snapshot already in `sources/cryptiana/`.

## Check-solved sweep, 24 September 2026

- **Editions first / print.** The letter is calendared in Bergenroth (ed.), *Calendar of State Papers,
  Simancas*, vol. II (Google Books, per Tomokiyo's citation; not independently re-fetched this pass, no
  Google Books access under this brief). PARES reference given by Tomokiyo: `ES.47161.AGS//PTR,LEG,54,51`
  ("Carta de la Reina de Inglaterra, Catalina de Aragon, al Rey Catolico quejandose mucho de lo que ha escrito
  Manuel de Esquivel de su Confesor").
- **Web / lists (Cryptiana).** `sources/cryptiana/web/catherine.htm`, "Solution of Ciphertext of Catherine of
  Aragon to King Ferdinand (1509)" (read in full; quoted): *"Back in 2018, I submitted to MTC3 [MysteryTwister
  C3] an unsolved ciphertext of Catherine of Aragon to King Ferdinand, her father. My challenge was published
  on 28 November 2018. To my pleasant surprise, it was quickly solved by two people: Victor and Thomas
  Bosbach. ... Since more than three years have passed ... I now present here the solution."* The page gives
  the sender/date exactly matching this record (Catherine of Aragon's letter of **3 November 1509** to King
  Ferdinand, PARES ref as above), the full deciphered text (41 lines, Spanish, with some letter-codes still
  open), the key table (Thomas Bosbach's, ~17 syllable/word codes), and the codebreaking method (a tilde
  diacritic consistently marking "señor"). First posted 12 July 2022, last modified 21 July 2022.
- **Bourdeau (github.com/dbourdeau/cyphersolver).** `CATALOGUE.md` line 15 lists "Catherine of Aragon 1509 by
  the Bosbachs" among items excluded from his catalogue as already solved; `SOLVED_CATALOGUE.md` line 222
  separately lists "Catherine of Aragon's letters of 1507 and 3 Nov 1509 ... read" among items already handled
  elsewhere. (Bourdeau's `CATALOGUE.md` line 74 entry, "Catherine of Aragon to Ferdinand, 29 July 1509 ...
  f. 60 unidentified ... solved (MTC3 2018)", conflates the date with a different, unrelated short cipher
  passage that Tomokiyo's own page attributes to Britain/Brewer, not to the Bosbach solution — a minor error
  in Bourdeau's notes, not evidence against this verdict, since Tomokiyo's own page is unambiguous about which
  letter and date the Bosbachs solved.)
- **Aymeloglu (github.com/aaymeloglu/unsolved-ciphers).** R361 appears only in the raw catalogue harvest files;
  no separate write-up, consistent with found-solved (not independently attacked there either).
- **DECODE.** Not queried live (per brief). Its own status field still reads "Non-decrypted" even though
  `Available Documents: Cleartext Publication` is set on the record — consistent with Tomokiyo's solution
  having been submitted to the record as a document without the catalogue's own status flag being flipped.
  Flagged in ROOM.md; the "paleography study [pub]" attachment noted in QUEUE.md is very likely the same
  transcription source Tomokiyo cites (Nicolás Ávila Seoane's paper on the queens' handwriting) or a closely
  related study, not independently confirmed this pass.

**Verdict: found-solved.** Solved by Victor and Thomas Bosbach (submitted via MysteryTwister C3, Dec 2018),
published in full (plaintext, key, method) by S. Tomokiyo on Cryptiana, `catherine.htm`, 12 July 2022. Per
README's F-grades: **F1** — the plaintext and key are published and the *specialist's own site* (Cryptiana)
links this exact manuscript, but DECODE's separate catalogue record for the same item still carries a stale
"Non-decrypted" status field, so a DECODE catalogue correction is the contribution to hand on. No novelty
claim made (rule 10); N-classing is a verifier's job, not done here.

## Correction to QUEUE.md

DC7's `held_by` should reflect found-solved (Tomokiyo/Bosbach 2018/2022), not `none`; "search-print" as a next
step was directionally right but the print check should have been run before scoring, per CLAUDE.md rule 12 —
flagged in ROOM.md, 24 Sept 2026.
