# [Melchior de Sabran?] to "Mr de ch. g^r", 9 February 1636, BnF Baluze 156, f.157-158

**Status: open.**

## Item

DECODE R2754 ("Non-decrypted"). Metadata (Aymeloglu `decode-records.jsonl`): tentative author "Melchior de
Sabran?" (DECODE uploader's own guess), receiver "Mr de ch. g^r", 9 Feb 1636, 1 page, cleartext French,
plaintext "probably French", symbol set alphabet + numerical, inline cleartext and (tentative) inline
plaintext both "Yes". QUEUE.md row **DC8**, scored `held_by: none`, next step "transcription", 4 images.

Brief: `.claude/briefs/runs/2026-09-24-lane-n-csDC2.md`. de-crypt.org and archive.org not queried directly
(held by other LANE N workers); worked from committed TSVs, QUEUE.md, both solver-repo clones and Tomokiyo's
Cryptiana snapshot.

## Check-solved sweep, 24 September 2026

- **Editions first.** BnF Baluze 156 is the fonds Baluze (Colbert's secretary's collection of foreign-affairs
  papers), not itself a printed edition. No calendar or edition for Sabran's outgoing/incoming correspondence
  1630-37 was located or checked this pass (out of this brief's host list — Gallica-hosted catalogue browsing
  was not attempted). This gap is a genuine unknown, not a "blocked" verdict on its own, since the record is
  otherwise readable (copy-free, images already viewable) and the strongest lead below is internal to the
  volume/cipher family, not the print record.
- **Web / lists (Cryptiana).** `sources/cryptiana/web/GL.htm`, section "Melchior de Sabran (1631)" and
  "Odoardo Farnese, Duke of Parma (1637)" (read in full; quoted): *"BnF Baluze 155 ..., f.79, contains a
  letter, dated Dijon, 28 March 1631, of Louis XIII (undersigned Bouthillier) to Melchior de Sabran, a
  diplomat then resident in Genoa (1630-1637). It has a paragraph in cipher. It is solved as follows. ...
  George Lasry confirmed this cipher is also used for many letters of Sabran in BnF fr.4134 and fr.4135."*
  and *"BnF Baluze 156 ..., f.40, is wholly enciphered, undeciphered. It seems to be an enclosure of a letter
  ... of Odoardo [Édouard] Farnese, Duke of Parma, to Sabran, dated Plaisance, 27 May 1637. It is solved as
  follows."* Neither passage names f.157-158 or this specific 9 Feb 1636 letter; **this exact folio is not
  mentioned anywhere in GL.htm**. But the volume (Baluze 156), the correspondent (Sabran, tentatively per
  DECODE's own uploader), and the date (Feb 1636, squarely inside Sabran's 1630-1637 Genoa residency) all fall
  inside the same cluster that Lasry has already broken twice (Baluze 155 f.79 and Baluze 156 f.40 itself,
  plus "many letters" in fr.4134/fr.4135) — a sibling-key lead in the LESSONS.md sense (look for the sibling
  with an already-recovered key in the same cipher family), not a confirmed match.
- **Bourdeau (github.com/dbourdeau/cyphersolver).** `CATALOGUE.md` items 191-192 (read in full; quoted): item
  191 covers Baluze **155** f.79 ("already solved by others... R2748 ... solved by George Lasry in 2022"; also
  fr.18043/fr.18044, read by Tomokiyo); item 192 covers Baluze **156 f.40** only, "solved by George Lasry in
  2022 ... **Found while checking 191; not viewed here.**" i.e. Bourdeau explicitly did not view or transcribe
  our target folio (f.157-158); no folder or write-up exists for it in his repo.
- **Aymeloglu (github.com/aaymeloglu/unsolved-ciphers).** R2754 appears only in the raw catalogue harvest
  files (`decode-catalog.csv`, `decode-records.jsonl`, and, as an unrelated substring hit, `forster-1644/lex_old.txt`
  and `ottobon-1589/reading.pdf`, both false positives on "2754" not "R2754"); no write-up.
- **DECODE.** Not queried live (per brief). Census diff (`records-non-decrypted-2026-09-24-diff.tsv`) has
  `held_by: none`, which is correct here: no repository or catalogue held this exact folio, unlike DC6/DC7/DC9
  in this same batch (see their NOTES.md).

**Verdict: open**, with a documented recovery lead: this is very likely enciphered with (a variant of, or
exactly) the Sabran cipher that George Lasry has already recovered twice in the same volume/correspondence
circle (Baluze 155 f.79, Baluze 156 f.40, and "many letters" in fr.4134/fr.4135). The lead has not been tested
against this folio's own ciphertext by anyone as far as this pass could find — next worker should read
Lasry's/Tomokiyo's key from `louisxiii.htm`/`GL.htm` (or a solver-repo copy if one has transcribed it) and try
it directly on f.157-158's own images before any fresh cryptanalysis, per CLAUDE.md's access playbook (image
over transcription) and LESSONS.md's "look for the sibling" pattern. No novelty claim made (rule 10).

Six-source status: 6/6 checked (editions unchecked for a specific calendar, noted above as a gap, not a
block); 0/6 found a decipherment of this exact folio; 1/6 (Cryptiana/GL.htm) found a directly relevant,
already-broken sibling cipher in the same volume.

## LANE N audit, 24 September 2026

**DocumentsList check** (`DocumentsList?showmaster=records&fk_id=2754`): **"No records found"**. RecordsView:
`Available Documents:` (empty), `Inline Cleartext: Yes`, `Inline Plaintext: Yes` (the source letter carries
inline plaintext passages around the cipher, per DECODE's own field, not a decipherment of the cipher itself
— `Status: Non-decrypted` agrees). No change to the verdict: still **open**, recovery lead. Status word
unchanged.

**Edition gap (job 3): does Lasry's published Sabran break already cover f.157-158?** Re-read
`sources/cryptiana/web/GL.htm` §"Melchior de Sabran (1631)" in full (already quoted in this file above).
Lasry's two published Baluze breaks are explicitly **f.79 of Baluze 155** (28 March 1631, Sabran the
recipient) and **f.40 of Baluze 156** (27 May 1637, Sabran the recipient again — Bourdeau's `CATALOGUE.md`
entry 192 corroborates, "found while checking 191; not viewed"), plus "many letters" of Sabran located in
BnF fr.4134 and fr.4135 (a different pair of volumes). **f.157-158 of Baluze 156 (this record) is not named
anywhere in GL.htm.** This is a genuine negative for the specific folio: Lasry's sibling key is a strong
alignment lead (same collection, same correspondent, cipher already broken twice), but no source found so far
states it was tried against, or already reads, f.157-158 itself. Next step unchanged: try the Sabran key on
this folio's own images before fresh cryptanalysis (still untried, still the strongest lead). Status word
unchanged (open).

Requests this pass: 0 new (Cryptiana snapshot is local; the one DECODE login was shared with DC1/DC2/DC4/DC5/
DC9, see decode-2678's NOTES for the combined de-crypt.org count).
