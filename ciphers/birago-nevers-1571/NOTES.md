open
No printed edition of the Birago-Nevers correspondence exists (searched, none found); Tomokiyo's catalogue (`sources/cryptiana/web/nevers.htm`, BnF fr.3251, folio 119) was read in full by this worker and names this exact letter (no.63, Saluzzo 13 Nov 1571) as using "a numerical cipher (not deciphered)", quoted verbatim below, and Bourdeau's own matched-control cryptanalysis of the same Gallica image (16 Sept 2026) independently confirms no prior solution.

# Lodovico Birago to the Duke of Nevers (13 November 1571)

## Check-solved (LANE CX, 25 Sept 2026)

Formal six-source sweep per `.claude/briefs/check-solved.md` — this folder previously had no formal check-solved
section, only the "Solver status" line below citing Bourdeau's summary third-hand.

1. **Web search.** `"Birago" "Nevers" 1571 cipher chiffre déchiffré Saluzzo` (this worker) surfaced Bourdeau's own
   published site (`dbourdeau.github.io/cyphersolver`, the same closed-negative already on file), Wikipedia pages
   for Louis de Gonzague and René de Birague (a different Birago), and general Saluzzo history — no edition,
   article or solution. A second query, `"Lodovico Birago" lettere Nevers Saluzzo edizione carteggio pubblicato`,
   found only Birago's Treccani biographical entry and unrelated Birago-surname genealogies — **no published
   edition of Birago's letters to Nevers exists**, confirmed by this search, not merely assumed. Model-solve-
   announcement family (checked once for all four targets) found nothing relevant.
2. **Standard edition/calendar.** None exists to check (previous item) — this correspondence survives only in the
   Gallica-digitised archival volume itself (BnF fr.3251, `archivesetmanuscrits.bnf.fr/ark:/12148/cc49712p`), not
   in a modern or period printed edition. Not a gate failure by the intake-gate's own logic (there is no edition
   to have failed to open); the controlled cryptanalytic negative below stands in its place.
3. **Community lists.** Tomokiyo's `nevers.htm` (mirrored locally, read in full, not re-fetched) states, of the
   November 1570-May 1571 Ceppo-Nevers cipher letters and this one specifically: *"In November 1571, they used a
   numerical cipher (not deciphered). f.119 (no.63) Saluzzo, 13 November 1571."* — this is the letter under audit,
   named by shelfmark, date and folio, quoted verbatim per rule 10 and the check-solved.md "named source"
   lesson. No Cipherbrain/Schmeh-specific page found for this item.
4. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` (local cache) and Aymeloglu's cached DECODE
   catalogue mirror (`catalogue/decode-catalog.csv`, fresh clone) both grepped for "birago"/"3251": the catalogue
   mirror has four hits, all for **different** Lodovico Birago items — BnF fr.3623 no.27 f.41 (1591), fr.3621
   nos.31/35/36 (1592, Sainte-Menehould), fr.3619 f.73 (1591, Langres) — different shelfmarks, a different decade,
   status "Decrypted" on DECODE. None is fr.3251 f.119 or this letter's 13 Nov 1571 date; flagged as a fact about
   the correspondent's other, later, already-decrypted correspondence, not evidence bearing on this item. Zero
   hits for "3251" itself in either source.
5. **Bourdeau** (`github.com/dbourdeau/cyphersolver`, fresh depth-1 clone by this worker, 25 Sept 2026, not the
   19 Sept citation already in this file): `birago/NOTES.md` and `birago/profile.json` read in full. Confirms and
   extends the existing "Solver status" line below: glyph-level re-transcription from the 8521x5849px Gallica
   image (`btv1b9060248g` view 120) corrects four errors in Tomokiyo's own transcription; five cipher designs
   (prefix/suffix variable-length codes, structured homophony, polyphonic single figures, a two-digit
   letter-with-marked-code-groups design, a syllabic two-digit alphabet) were each tested against matched
   synthetic controls of the same length/symbol profile and excluded or left unread; `profile.json`'s own
   `conditions.prior_solution` field records `"exists": "no"`, `"found": "not found"`, and `outcome.method`:
   `"not solved"`. A sweep of all 118 remaining openings of the same volume (fr.3251) for a second letter in the
   same figure cipher, and a check against the 1574 Nevers key (fr.3315), both failed to find a sibling or a
   matching key. Code MIT / text CC BY 4.0, cited not copied.
6. **Aymeloglu** (`github.com/aaymeloglu/unsolved-ciphers`, fresh depth-1 clone by this worker, 25 Sept 2026):
   `grep -rli "birago"` across json/md/csv/txt/tsv finds only the DECODE catalogue mirror hits already covered
   under item 4 (the different, later Birago items); no dedicated treatment of this letter anywhere in the
   repository.

**Verdict: open, unchanged.** No printed edition exists to check; the one community source that names this exact
letter (Tomokiyo) states it as not deciphered; DECODE, Bourdeau and Aymeloglu all independently confirm no prior
solution of fr.3251 f.119 specifically (as opposed to the correspondent's other, later, already-decrypted
letters). Bourdeau's own attempt is a genuine matched-control cryptanalytic negative (rule 3), not merely an
absence claim, and is the strongest evidence here. Grade: no reading exists to grade. Novelty not classified
(rule 10; not this brief's job).

Requests this pass: github.com 2 (fresh shallow clones, dbourdeau + aaymeloglu, deleted after grep). WebSearch 2
queries. No other hosts, no subagents, no logins, no credentials.

## Background (pre-existing)

- **Source:** BnF fr.3251, f.119. Letter in Italian. One paragraph is in a numerical cipher that the keys reconstructed for Birago's other 1570-1572 letters do not solve. Image: https://gallica.bnf.fr/ark:/12148/btv1b9060248g/f120.item
- **Status:** Open.
- **Transcription:** `ciphertext.txt` (Tomokiyo's). Note his warning: the diacritics (÷ ¯ ¨ + and letters n, f, c, m, a, l) should be placed over the following one or two characters. Check the Gallica image before trusting any parse.
- **Background page:** `sources/cryptiana/web/nevers.htm` (section BnFfr3251).
- **Ideas:** Digits run continuously without separators, so the first problem is tokenisation. Try two-digit groups, then variable-length. The diacritics probably modify the following digit pair (syllable vs. letter, or a vowel change). Plaintext is Italian.
- **Solver status (19 Sept 2026):** Closed-negative by Bourdeau (cyphersolver/birago), 16 Sept 2026, after glyph-level re-transcription from Gallica (the "+" signs are superscript crosses). Variable-length designs excluded against controls; the only consistent design is beyond the annealer at this length. Needs a sibling letter or a crib.
