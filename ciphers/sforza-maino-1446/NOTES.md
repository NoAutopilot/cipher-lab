open

# Sforza reply to Zorzo (Giorgio) del Maino, 4 May 1446 (BnF italien 1583 f.68, DECODE R7898) and Vincenzo
# Amidani to Francesco Sforza, Milan, 4 May 1446 (BnF italien 1583 f.70, imaged inside DECODE R7899)

Two items, same shelfmark, same date, same graphic-sign cipher family:

- **f.68** (DECODE R7898): reply from the Sforza side (Francesco Sforza, then condottiere in the Marche, or
  his chancery) to what his agent Giorgio (Zorzo) del Maino had reported. 404 signs, 26 types.
- **f.70** (imaged as the second slip, image P1, inside DECODE R7899, whose primary catalogue heading is
  "f.75"): Vincenzo Amidani to Francesco Sforza, Milan, 4 May 1446. 390 signs, 31 types, a different hand,
  same sign family as f.68.

## Source

Transcriptions, sign inventories, DECODE image identifiers and the Mazzatinti inventory pointer are all
Bourdeau's work (`dbourdeau/cyphersolver`, folder `it1583/`, commit `2e9ec01`, checked 23 Sept 2026 in this
sweep; code MIT, text CC BY 4.0, cite per CLAUDE.md rule 8). No transcription is copied into this folder; a
solver session does that with attribution. Inventory identification of both items ("f. 68. Risposta a quanto
ha riferito Zorzo Maino (4 maggio). In cifre." / "f. 70. Lettera di Vincenzo Amidani a Fr. Sforza (Milano 4
maggio). In cifre.") is from Girolamo Mazzatinti's inventory of the BnF Sforza papers, *Archivio storico
lombardo* X (1883), p. 230 (OCR at `cs-recheck/it1583/asl1883.txt`, verified directly by this worker at lines
10500-10506, matching Bourdeau's citation exactly, no decipherment noted).

## Check-solved sweep (23 September 2026)

Six sources, each logged with what was searched, found or unreachable. This environment egress-blocks every
archive host (de-crypt.org, archive.org, web.archive.org, gallica.bnf.fr, catalog.hathitrust.org,
wikisource.org, Google Books); only github.com and the WebSearch tool are reachable.

1. **Web search engine.** Queries run: `"italien 1583" cifra Sforza 1446 Maino Amidani`; `"Zorzo Maino" OR
   "Giorgio del Maino" 1446 cifra Sforza`; `"Vincenzo Amidani" 1446 Sforza cifra`; `Cerioni "La diplomazia
   sforzesca" cifrari Maino Amidani`; `DECODE R7898 R7899 de-crypt.org BnF italien 1583`; plus follow-ups
   `Cipher Mysteries "Milanese enciphered letters" call for help Cerioni Sforza`; `lombardiabeniculturali
   "Vincenzo Amidani" 1446 maggio Francesco Sforza cifra`; `"Giorgio del Maino" OR "Zorzo Maino" 1446
   Francesco Sforza risposta cifra lettera`; `Voynich Ninja diplomatic ciphers Sforza Milanese enciphered
   letters thread`; `"cifrari" Sforza "1446" Cicco Simonetta Tranchedini nomenclatore Amidani studi storia
   medioevale diplomatica`. Found: general biographical pages for Giorgio del Maino and Vincenzo Amidani (both
   served the Sforza chancery; Amidani joined Sforza's service in 1437 and was in Venice for Sforza's interests
   in 1446 -- consistent with, not a reading of, the cipher), Lombardia Beni Culturali's "La memoria degli
   Sforza" letter registers (searched for a May 1446 Maino/Amidani entry; nothing found for that month --
   the registers indexed there run mostly 1450 onward), Cerioni's 1970 *La diplomazia sforzesca* cited only
   bibliographically (Cancelleria segreta keys from ASMi Sforzesco busta 1591 and 1597-1598, same busta numbers
   Bourdeau already worked from), a 2011 Cipher Mysteries post "Milanese enciphered letters, call for help..."
   (a general call to locate Sforza-era ciphers, cites Cerioni, no mention of Maino, Amidani, f.68, f.70,
   R7898 or R7899), and a paper on Nicodemo Tranchedini's cipher (a different named correspondent, not this
   pair). No search surfaced a plaintext, a transcription, or a key specific to f.68 or f.70.
2. **Print.** Cerioni, *La diplomazia sforzesca* (1970), located bibliographically (Librinlinea, SearchWorks,
   WorldCat, Google Books records) but not obtainable in this environment (no full text online; the volume's
   own key facsimiles are print-only) -- unreachable, would need the person or a library visit; recorded as a
   reopening route, not searched further. Mazzatinti 1883 (`asl1883.txt`, already on disk from Bourdeau's
   fetch): grepped directly by this worker for "maino" (line 10271 index entry, line 10502 the f.68 heading
   itself, plus five further Maino letters elsewhere in the volume), "amidani" (line 10506 the f.70 heading,
   plus six further Amidani letters "in cifre" elsewhere in the same volume -- additional related leads, not
   decipherments of these two folios), and the text around f.68/f.70 (lines 10495-10515, transcribed above) --
   confirms both headings read "In cifre" with no decipherment or edition noted anywhere in the inventory.
   Meroni and the Sforza letter editions (Carteggio degli oratori mantovani etc.) were not separately reachable
   from this environment (no online full text found by web search) and were not searched further; logged as a
   gap, not a finding.
3. **Community lists.** `grep -rn "1583\|Maino\|Amidani\|Sforza"` in `sources/cryptiana/` (this repo's local
   snapshot of Cryptiana): matches are all coincidental -- other manuscripts or people that happen to share the
   string "1583" as a year (Henry III correspondence, Mary Stuart letters, a different "Maximilian Sforza"
   cipher in BnF fr.3034, Marino Caracciolo). No match for the shelfmark "italien 1583", for Cerioni, for
   Tranchedini in the context of this pair, or for the diplomazia sforzesca title. WebSearch of Cryptiana and
   Cipherbrain directly (queries above) returned nothing on this pair either.
4. **DECODE.** de-crypt.org is fully egress-blocked from this environment (no login attempted, per the
   playbook). Would-be URLs: `https://de-crypt.org/decrypt-web/RecordsView/7898` and
   `https://de-crypt.org/decrypt-web/RecordsView/7899`. A cached DECODE catalogue snapshot inside
   `ay/catalogue/decode-catalog.csv` (Aymeloglu's repository, scraped from DECODE, no licence, cite only) does
   reach both records: row 7898 = "Paris, BnF (BnF), italien 1583, f 68. BnF_1583_068", status
   **Non-decrypted**; row 7899 = "Paris, BnF (BnF), 1583, f 75. BnF_1583_075" (the record under which f.70's
   image is also filed), status **Non-decrypted**. Both fields for cleartext/plaintext are empty in that
   snapshot. This is the closest this sweep could get to DECODE's own status field and it agrees with
   Bourdeau's report that DECODE marks both "Non-decrypted".
5. **Bourdeau (dbourdeau/cyphersolver, it1583/, fresh clone commit 2e9ec01, 23 Sept 2026).** Read `NOTES.md`
   and `profile.json` in full. He: downloaded both DECODE images with an authenticated session cookie; found
   Mazzatinti's 1883 heading for both folios (as above); transcribed f.68 (404 signs/26 types) and, separately,
   found and transcribed f.70 inside the R7899 image (390 signs/31 types); ran homophonic simulated annealing
   (it-cinquecento model) on f.68 alone -- unconstrained, capped-homophone, and nulls-allowed variants all
   collapsed to nonsense; ran one-to-one substitution annealing, 16 restarts, all nonsense; tried a word-pattern
   match on repeated sign-groups (FpBHcdSp fits "uisconti" but contradicts the other repeats); ran annealing on
   f.70 alone, also nonsense; downloaded and thumbnail-scanned all 208 ASMi Carteggio Sforzesco key records
   (cart. 1591, 1597, 1598) on DECODE, reading headings and alphabets of the 15th-century copies (cart. 1597
   nos. 2-36) -- none headed Maino or Amidani; the nearest match by system design, 1597 no. 14 ("Angelus cum
   cifra Vincentij", shared among Johannes de Stavolis, Augustinus, Baptista, Matheus and Vincentius), has the
   same homophonic-plus-syllable-plus-word-sign-plus-null structure but different letter signs from f.68/f.70,
   so it is ruled out as the actual key, not confirmed as the system. **He never annealed f.68 and f.70
   jointly as one key** -- each was only ever attacked alone, which is the standard next move for two ciphers
   sharing a chancery system (this is why the target was harvested as G7 rather than left closed). His control:
   the same one-to-one solver verified on a synthetic 400-letter Italian cipher, solved in 1 of 3 restarts.
   That is a control for **one-to-one substitution only** -- it says nothing about whether the homophonic/
   nomenclator annealing attempts (points 1-2 and 5 above, which are the more plausible system for a
   26-31-type sign inventory this size) were properly tuned, since no synthetic homophonic-nomenclator control
   of matching design was run for those. Per rule 3, the homophonic negative on this target is not backed by a
   matched control and should be treated as unconfirmed until one is run.
6. **Aymeloglu (aaymeloglu/unsolved-ciphers, `ay/`, no licence, cite only).** No target folder for this pair
   (top-level folders are `burgess-1912`, `ferdinand-1635-1640`, `forster-1644`, `moray-1568`, `ottobon-1589`,
   `royalist-1646`, `starhemberg-1758`, `vande-perre-1653`; none named for Sforza, Maino, Amidani or it1583).
   `grep -rn "1583\|Maino\|Amidani\|R7898\|R7899"` across the whole repository: the only real hits are inside
   `ay/catalogue/decode-catalog.csv` and `decode-records.jsonl`, a scraped mirror of the DECODE database
   itself (see point 4) -- confirms both records' "Non-decrypted" status but is not independent solving work
   by Aymeloglu on this pair. `TARGETS.md`, `SHORTLIST.md` and `CATALOGUE.md` at the repository root: no
   mention of this pair.

## Verdict

No decipherment, transcription-into-plaintext, or key specific to BnF italien 1583 f.68 or f.70 was found in
any of the six sources. DECODE's own status field (via the cached catalogue snapshot) still reads
"Non-decrypted" for both R7898 and R7899. Mazzatinti's 1883 inventory, the only pre-existing catalogue entry
located, gives only "In cifre" for both, no reading. Bourdeau attempted both, separately, and closed the target
unread; the negative rests on a one-to-one-substitution control only, not a homophonic/nomenclator one, so it
does not by itself rule out the more plausible system (rule 3). Aymeloglu has not worked this pair. Per rule
10, this is a search result, not a claim of novelty: absence from these six sources does not mean unpublished,
only not found here.

**Stage 2, verified unsolved (conditional: DECODE, Gallica and print sources unreachable from this
environment; verdict rests on WebSearch, GitHub and the local Cryptiana snapshot)**
