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

## Capture and passes (24 Sept 2026)

LANE G2 worker K, brief `.claude/briefs/runs/2026-09-24-lane-g2-k-dc8-dc9-capture.md`, cap $7 shared with DC9.

**Ark and folio.** Found via archivesetmanuscrits.bnf.fr's free-text search (plain `POST resultatRechercheSimple.html`
with a JSESSIONID cookie from a prior GET): query "Baluze 156" surfaces the notice `ark:/12148/cc340913`
("Baluze 155-156 . Correspondance et papiers divers de Melchior, comte DE SABRAN..."), whose sub-unit "Baluze 156
(cote)" (`ajaxGetCompDisplay.html?eadCompId=FRBNFEAD000034091_a19857858`) gives the digitised-document link:
**gallica.bnf.fr/ark:/12148/btv1b9001409q**. Baluze 156 itself has no item-level finding aid (unlike Baluze 155,
which is broken into numbered correspondence groups) — the catalogue could not name f.157-158's correspondent or
confirm the date directly, only the volume.

**Manifest fetch failed; canvases found by folio-stamp reading instead.** `gallica.bnf.fr/iiif/.../manifest.json`
and `/services/Pagination` both answered `curl: (35) Recv failure: Connection reset by peer` every time this
session (`/__agentproxy/status` logs it as `ws_closed_mid_exchange` against `gallica.bnf.fr:443` — proxy-side,
not a Gallica denial: the plain host, `.thumbnail`, and the direct `/iiif/.../fN/.../native.jpg` image endpoint
all answered 200, just not reliably on the first try for larger payloads; one retry per URL, smaller sizes or
narrower region crops routed around most failures). `tools/gallica_folio.py` could not run without the manifest,
so canvas-to-folio mapping was done by eye: candidate canvases fetched directly by Gallica image index, corner
region cropped and read for the manuscript's own handwritten folio-number stamp. Canvas f157 (the volume's own
lowest-numbered candidate tried) reads folio "153"; canvas f161 reads "157" (confirmed) and its right-hand page
opens "Copie du 9e febvrier 1636 ... Monseigneur ... Monsieur D'Isabran est party de Turin..." — matching this
item's date and tentative author exactly; canvas f162's right-hand page reads "158" (confirmed) and is blank
(the address/outer-fold leaf); canvas f162's left-hand page is the same letter's continuation (157v), entirely in
plain French, no cipher. **Images kept:** `images/dc8_f157r.jpg`, `images/dc8_f157v.jpg`, `images/dc8_f158r.jpg`;
`images/manifest.json` records the fetch URLs and this reasoning (offset not verified as constant across the
volume — do not assume it holds elsewhere).

**Two blind Sonnet passes.** `passA.tsv` and `passB.tsv`, each a full line-by-line transcription of f157r made
independently (neither subagent was shown the other's output, an existing key, or any prior reading), following
the mixed-plain-cipher convention used in `fr4687-paleologue-nevers/passA.tsv` (`[PLAIN:"..."]` runs, individual
cipher tokens elsewhere). Both passes agree that the cipher is not pure digits: it mixes 1-3 digit numbers with
single/doubled upright letters (t, tt, ll, nn, ff, etc.) and a few non-alphanumeric marks (an ink blot, a
circle-with-stroke glyph), scattered across the same nine or so cipher-dense stretches of the page (naming a
Gascon informant, a Marseille/Villefranche/Vitry report, correspondence toward Florence and Modena). The two
passes' line numbering differed by a constant offset (pass A split the heading/salutation into separate `LH1`/
`LH2` lines before its `L01`; pass B numbered the same two lines `L01`/`L02` and started the body at `L03`);
re-numbering pass A's lines by +2 to align, `tools/reconcile_passes.py` (long format) gives **87.6% token
agreement (120/137) across the 14 lines with cipher content** — both passes end on the same closing run
("Z g c͡ g c͡", the caron/breve marks over the last two c's agreed independently by both readers) and disagree
mainly on ambiguous single glyphs (9 vs q, o vs 0, g vs 9) already flagged M/L by both. `disagreements.tsv`,
`ciphertext_draft.tsv` and `agreement.tsv` are the reconciler's output on the aligned numbering (their `line`
labels follow pass B's scheme, i.e. two higher than pass A's own `LH`-prefixed labels for the same content).
Plain-French prose in both passes is only M/L confidence throughout (dense secretary hand); neither pass
attempted a full French reading, per brief (cipher-digit precision was the priority).

**Mechanical trial of the Sabran (1631) key — negative, matched control.** `key_sabran_1631.tsv` transcribes
George Lasry's published key for BnF fr.4134 / Baluze 155 f.79 (the "Sabran (1631)" cipher named in this
worker's brief and in this folder's own "sibling-key lead" — a *different* cipher from the undeciphered Farnese-
to-Sabran one at Baluze 156 f.40, GL.htm's next section). Only the key's 20 two-digit nomenclator codes (word/
syllable numbers such as 17=BON, 44=LA, 58=QUI) can be mechanically tested against a plain-text transcription;
the key's separate hand-drawn letter-symbol alphabet cannot be matched this way without re-inspecting the image
glyph by glyph, out of scope for a mechanical trial. `trial.py` extracts every 1-2 digit numeral from `passA.tsv`
(31 tokens, mostly single digits from split multi-character cipher runs) and checks how many equal one of the
20 key numbers, against a shuffled-key control (1000 draws of 20 random values from 0-99): **0/31 real hits
(0.0%) vs a control mean of 19.1% and control max of 83.9% over 1000 draws — the real rate is not merely
unremarkable, it is below the chance baseline.** `trial.tsv` (reproducible, `trial.py --check` exits 0). This is
a clean negative for "this folio uses the same nomenclator numbers as fr.4134/Baluze 155 f.79", not a negative
for the sibling-key lead as a whole: the letter-symbol alphabet (the larger part of Lasry's key) was not tested,
and this folio's cipher — mixed digits and doubled upright letters — does not obviously resemble either of
Lasry's two published Sabran-circle systems at a glance. Next step for a future worker: match the cipher's
doubled-letter tokens (tt, ll, nn, ff) against Lasry's letter-symbol table by shape, and/or search for a
nomenclator with a different number range before ruling out the sibling-key lead entirely.

No decoding attempted beyond this mechanical trial; status word unchanged: **open**, recovery lead partially
tested (nomenclator numbers only) and not confirmed.

Requests this pass (shared host budget with DC9, one fetcher): gallica.bnf.fr ~20 (several connection resets on
manifest/services/large-crop fetches, one retry per URL per the good-citizen rule, routed around with smaller
sizes thereafter); archivesetmanuscrits.bnf.fr ~10 (search+notice+ajax fetches, ≥1.5s apart, UA
`cipher-lab research script (contact via repository)`); cryptiana.web.fc2.com 5 (the five Sabran/Farnese key and
decipherment images from GL.htm, ≥1.5s apart); 2 Sonnet subagents (the two blind passes, never concurrent with
any other subagent this worker ran).
