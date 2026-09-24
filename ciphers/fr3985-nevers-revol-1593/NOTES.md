# fr.3985 (Nevers -> Revol, 21 Aug and 2 Sept 1593) — Louis de Gonzague, duc de Nevers, to Louis Revol

Status: **partial**

Checked by LANE N4 csKSa (check-solved), 24 Sept 2026, following `.claude/briefs/check-solved.md` and
`.claude/briefs/runs/2026-09-24-lane-n4-csKSa.md`. Two rows, same target (two leaves of the same
correspondence): row KS-01 (f.88, 21 Aug 1593) and row KS-02 (f.176, 2 Sept 1593), both from
`sources/solver-diffs/2026-09-24-keys-vs-siblings.tsv`.

## 1. What is established

- BnF fr.3985, "Collection Mémoires de la Ligue" -- Duke of Nevers' Rome-embassy correspondence, Aug-Nov 1593.
  Gallica ark `btv1b90606498` (485 canvases, all labelled "NP" in the IIIF manifest -- no printed foliation in
  the metadata).
- Sender: Louis de Gonzague, duc de Nevers. Recipient: Louis Revol, secretary of state.
- Key: Tomokiyo's no.60 ("the Court's symbol cipher", fr.3995 f.108-110: symbol alphabet, ~5 homophones/letter,
  a full syllabary, Roman-numeral names/places, word signs, nulls; separate deciphering table sorted by symbol
  similarity). Table already transcribed in full by Daniel Bourdeau (CC BY 4.0, `key60.txt` in his
  `nevers1593/` folder) and confirmed against contemporary office decipherments elsewhere in the same volumes
  (the interlined Henri IV letter fr.3986 f.151/152 and the Instruction of 31 Aug, fr.3985 f.126-130). This is
  **kind recovery**: the key exists, these two leaves do not have a reading yet.

## 2. Leaf confirmation (this session)

Canvas numbers in the source TSV were unconfirmed estimates (Bourdeau's own ratio `c = 218 + 2.01*(folio-109)`,
since every canvas in this manifest is labelled "NP"). Confirmed this session by fetching the estimated canvas
and reading the leaf's own handwritten folio number and date, at modest resolution (`,1000` IIIF width):

- **KS-01**: canvas 176 = **folio 88** (number visible top right), dated **"21 d'aoust 1593"** top left,
  salutation to "Monsr Revol", a symbol-cipher paragraph below the clear opening. Image:
  `https://gallica.bnf.fr/iiif/ark:/12148/btv1b90606498/f176/full/,1000/0/native.jpg`, saved
  `images/f88_canvas176.jpg`.
- **KS-02**: canvas 353 = **folio 176** (number visible top right), dated **"2 de Sept 1593"** top left,
  salutation "Monsr Revol", a symbol-cipher paragraph (e.g. "0141 yx z9 10..." mixed digit/letter groups) partway
  down the page. Image: `https://gallica.bnf.fr/iiif/ark:/12148/btv1b90606498/f353/full/,1000/0/native.jpg`,
  saved `images/f176_canvas353.jpg`.

Both leaves genuinely carry cipher in Tomokiyo's no.60 symbol style (not plain digits), no interlinear
plaintext gloss visible over the cipher passages at this resolution (checked per the Thurloe/Birch and Gondi
lessons in LESSONS.md -- see fr.3983 f.169 in the sibling target for a case where that check *did* turn up a
gloss).

## 3. Six-source check-solved sweep (this session, 24 Sept 2026)

1. **Web**: WebSearch `"fr.3985" OR "fr. 3985" Nevers Revol 1593 chiffre déchiffré` -- BnF catalogue pages,
   Wikipedia (Nevers, Louis de Revol), no reading or decipherment of these two leaves found.
2. **Print**:
   - *Les Mémoires de M. le duc de Nevers* (Gomberville, "seconde partie"), Google Books `H2eV4wAmIr0C`,
     search-within-volume (`jscmd=SearchWithinVolume`): `"Revol"` (5 hits, all narrative mentions of Revol as
     Nevers' correspondent/secretary of state, none dated 21 Aug or 2 Sept 1593); `"d'Aoust 1593"` (1 hit, a
     Henri IV letter of 18 Aug, not Nevers'); `"Septembre 1593"` (2 hits, neither dated 2 Sept nor addressed to
     Revol). Letters absent from this edition.
   - *Recueil des lettres missives de Henri IV* (Berger de Xivrey), archive.org `recueildeslettre03henr` (vol.3,
     covers 1593), full-text search (`be-api.us.archive.org/fts/v1/search`) for "Revol": hits are Henri IV's own
     outgoing letters *to* Revol ("A Monsr de Revol, La Tour vous portera la depesche...", dated Saint-Cloud
     2 Aug [year garbled by OCR]), not Nevers' letters. Different correspondence entirely; our two leaves absent.
   - *Memoires de la ligue* (Goujet), archive.org `memoiresdelaligu05goul`/`06goul` (v.5-6), full-text search for
     "Revol": hits are routine signed acts and a response to the duc de Mayenne, not diplomatic dispatches to
     Rome; our two leaves absent.
3. **Cryptiana/Cipherbrain**: `sources/cryptiana/web/nevers.htm` (on disk) read in full for the no.60 section --
   Tomokiyo states only "Used in many letters in BnF fr.3985 etc." and points to a second article,
   `henryiv2.htm`, not cached in this repo (not fetched this session -- next worker should pull it to check for
   a letter-by-letter table). No verbatim naming of f.88 or f.176 found in the cached page.
   `sources/cryptiana/web/unsolved-2026-09-24.htm` (Tomokiyo's unsolved list) grepped for "3985"/"Revol": no
   real match (one false-positive digit-string hit).
4. **DECODE**: `sources/decode/` (7 files on disk) grepped for "3985"/"Revol"/"Nevers.*Revol": no hits. (No
   DECODE login attempted this session -- not this worker's role per COMMON rules.)
5. **Bourdeau** (`dbourdeau/cyphersolver`, shallow clone, this session, HEAD `2ea4fc2`, most recent commit
   touching `nevers1593/` dated 24 Sept 2026 12:26 -0500 but that commit is an unrelated mass update -- his
   Nevers work itself still reads as his 17 Sept 2026 session plus a same-day addendum; the repo's later commits
   move on to an Indus-script project and a Perwich 1670 write-up, confirming no further Nevers-Revol work since).
   His own `nevers1593/NOTES.md`, "Remaining gaps" section, verbatim:
   > "fr. 3985 f. 88 (21 Aug), f. 115 (27 Aug, one line), f. 176 (2 Sept, no. 88/94), fr. 3986 f. 198 (23 Oct,
   > no. 101) - blocker: not-attempted; located and cut but never transcribed; key no. 60 is fully in hand"

   He located and cropped both leaves (in his session scratch, not committed) but never transcribed or decoded
   either. Coverage stated as "2 of 7 read" (the two he does not count are the Henri IV interlined cribs and
   the Instruction, used as key sources, not read as targets).
6. **Aymeloglu** (`aaymeloglu/unsolved-ciphers`, shallow clone, this session): grepped `catalogue/*.jsonl` and
   the whole repo for "Nevers"/"Revol"/"3985" -- his DECODE-catalogue and PARES/BNE scrapes list several *other*
   Nevers-cipher items (BnF fr.3623, fr.3616, fr.3975, fr.3979, fr.3976) but neither fr.3985 folio, and no
   Revol correspondence at all. Absent from his repository.

## Verdict

KS-01: **open -- Gomberville seconde partie (Google Books H2eV4wAmIr0C) search-within read for "Revol" and
"d'Aoust 1593", Berger de Xivrey Recueil des lettres missives de Henri IV vol.3 (archive.org
recueildeslettre03henr) full-text read for "Revol", Memoires de la ligue (Goujet) v.5-6 (archive.org
memoiresdelaligu05goul/06goul) full-text read for "Revol", letter absent from all three; Bourdeau's own
"not-attempted" gap list confirms unread as of his 17 Sept 2026 session.**

KS-02: same edition set, same verdict, **open**.

Grade: no reading exists yet (grades N/A). Kind: **recovery** (key already reconstructed by Bourdeau/Tomokiyo;
what's missing is transcription and decode of these two leaves). Per this brief's scope, this session does not
apply the key or read the letters -- that is LANE R5's.

## Credit

Key no.60: Satoshi Tomokiyo (original reconstruction, `nevers.htm`), Daniel Bourdeau (CC BY 4.0 transcription,
`key60.txt`, and the canvas/folio offset ratio for fr.3985 used to place these leaves).

## Next step (one line, not this brief's scope)

Transcribe both leaves against `key60.txt` (LANE R5); cross-check any unclear symbol against the interlined
crib pages Bourdeau already identified (fr.3986 f.151-152, fr.3985 f.126-130).

## Key no.60 applied (24 Sept 2026, LANE R5 F1)

Status word set to **partial**: the key has been applied mechanically to both leaves, but nothing reads
continuously. Worker: LANE R5 F1 (Opus, session_019BqK12YeUXwrP5nNtCMiLi).

- **Key**: `key.tsv` (366 signs) converted from Daniel Bourdeau's `nevers1593/key60.txt` + `decode60.py`
  (github.com/dbourdeau/cyphersolver, commit a0d5a07349e98cfc47d41608cd88722a219c44a3; text CC BY 4.0, code MIT),
  itself a transcription of Satoshi Tomokiyo's no.60 (fr.3995 f.109-111). Where the enciphering sheet and the
  deciphering table disagree (ſ = s or m; 7 = p or s; c = s, a or y; 3 = ri or z; x = a or d; o = a or b; 4 = x
  or 4+ bien) the value is kept as `a|b` and graded M. Copyist forms from Bourdeau's atlas60.md added as such.
- **Images**: Gallica IIIF, 4 requests (2 info.json, 2 native regions), 24 Sept 2026 20:14-20:15 UTC:
  f.88 = canvas 176 region 550,4450,3800,950; f.176 = canvas 353 region 900,550,3400,4200
  (`images/src_*`). `tools/iiif_lines.py` line detection misfit this slanted hand (half-pitch at default, merged lines at
  --distance 150; overlays checked), so bands were cut by eye around every cipher run: `images/crops/` (30 crops,
  `crops.json` gives boxes). Leaf check: f.88 carries two letters, the cipher is in the second ("Monsr de Revol...",
  lower half); f.176 carries 12 short cipher runs inside clear text. No interlinear or marginal decipherment on
  either leaf (checked on the native crops).
- **Transcription**: pass A (Opus, against the key60 sign inventory) `passA.tsv`/`passA_lines.tsv`, 269 signs in
  16 runs; blind pass B (Sonnet) `passB.tsv` per crop, mapped to the same runs in `passB_lines.tsv` (211 signs; B
  marked nearly every sign uncertain and read f176.1 as clear). `tools/reconcile_passes.py`: **agreement
  104/277 columns = 37.5%** (`recon/agreement.tsv`). Disagreements were NOT settled one by one on the image (99
  differ + 66 gap columns; budget): `ciphertext.tsv` keeps pass A's sign everywhere, conf H only where both passes
  read the same sign, M elsewhere. B-only signs dropped (listed in recon/).
- **Reading**: `decode.json` + `tools/decode_key.py` -> `reading.txt`, `reading_tokens.tsv`; `--check` exits 0.
  **Tokens 269: H 73, M 162, U 34, C 0, S 0, I 0 in the reading.** No H or C run reads as French; this is a
  mechanical application, not a reading.
- **Anchors** (`anchors_I.tsv`, grade I, kept out of ciphertext.tsv): f.176 run 3 `ſ 14 1 ſ y x = 9 20 ///` =
  [l'a]mbassadeur (seven single-valued key signs b s s a d e u r in sequence; ſ taken as m, 1 as a copyist a); f.176
  run 1 after clear "touchant" possibly "[l'ab]s[olu]cion" (a guess). These show the key does fit the leaf; they are
  not a reading.
- **Blocker** (same as Bourdeau's, 17 Sept 2026): palaeographic, not cryptographic. The copyist's cursive forms of
  the symbols map to two or three table entries; two passes agree on barely a third of the signs.
- **Not done / suggestion**: settle recon/disagreements.tsv on the native crops with a glyph atlas built from the
  interlined Instruction of 31 Aug (fr.3985 c.264-268, same copyist, clear print in Memoires de Nevers ii
  492-499, Gallica bpt6k64451005) -- Bourdeau's route; a third pass is pointless before that atlas exists.
- Hosts: gallica.bnf.fr 4; github.com 1 shallow clone. No print search for the plaintext (verifier's job).
