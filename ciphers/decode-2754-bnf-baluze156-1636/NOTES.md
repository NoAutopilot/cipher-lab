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

## Letter-symbol half (24 Sept 2026)

LANE G3 worker C (Opus, cap $5), brief `.claude/briefs/runs/2026-09-24-lane-g3-c-dc8-letters.md`. Worked from disk
plus two Cryptiana image fetches; no Gallica requests.

**Key alphabet.** `key_sabran_1631_letters.tsv` transcribes the 23-column letter alphabet of George Lasry's key
"BNF Francais 4134" (25/05/2022, published on Tomokiyo's Cryptiana GL.htm, image `code/GL/BnF_fr4134.jpg`, 624x261
px; not committed, cite it): 52 glyphs, all grade M because each is ~15 px. It replaces the placeholder `letter`
rows of `key_sabran_1631.tsv` (whose glyph counts per column were partly wrong; e.g. E has five glyphs, I four, V
four). The Sabran alphabet is itself a disguise alphabet: most glyphs are ordinary letter and digit shapes (a, o,
5, c, 8, 4, u, 9, 6, m, e, d, 10, x, 7, 11) plus barred doubles (barred II for L, crossed tt-like # for P, crossed
ff-like # for S). Lasry's own decipherment image of Baluze 155 f.79 (`BnF_fr4134_decipher.png`, fetched once,
viewed only) shows it in use: "d g d r o 6 10 44 ..." = MONACHO LA ... So DC8's mix of lower-case letters, digits
and doubled letters is the same *style* of cipher, which is why the lead deserved the test.

**Shape match.** Each DC8 token class in `ciphertext_draft.tsv` was matched by eye (key zoom vs. crops of
`images/dc8_f157r.jpg`) to the closest key glyph; the match is the `dc8_token` column. 29 token classes map;
nn, h, Φ, 12, 94, 36, Sr, do, ttu, C, c̃ have no counterpart in the key (21 of 137 tokens unmapped).
**Doubled letters:** ll fits the key's barred II (L) well, tt the crossed # of P, ff the looped crossed # of S; nn
(4 occurrences) has no key glyph at all.

**Result: does not read. Negative with matched control** (`letters_trial.py`, `letters_trial.tsv`, `--check` exits 0):

| | French 5-gram bits/char (lower = more French) |
|---|---|
| DC8 decoded with the key-derived mapping (116 letters) | **5.649** |
| same mapping, values shuffled over the same token classes, 1000 draws | median 6.191, best 5.100; 6.8 % of shuffles score as well or better |
| positive control: 116 letters of held-out period French, enciphered with the key's homophones under the same token classes and run breaks, decoded with the same mapping | **3.066** (0.0 % of 1000 shuffles as good) |

Best case over 432 combinations of the ambiguous shape assignments (r as A/C/R, c as D/V, n as E/P, 6 as H/D,
9 as I/H/O, g as O/X/I, b as H/T): 5.220, still inside the shuffle range and 2.2 bits/char from the positive
control. No French word of four or more letters appears in the decode (runs: `X EF VAPGCAGOOM EROOELOAGVCM ...`,
full list in `letters_trial.tsv`). The internal repeat `7 4 t o` (L23 "...g 7 4 t o e amy", L32 "par ledit 9 7 4 t
o p") decodes to AGVC under the key, which is not French.

Together with the nomenclator trial above (0/31 numeral hits vs control mean 19 %), the Sabran (1631) key, in the
form Lasry published it, does not open f.157r. What stays untested: (a) the Farnese-to-Sabran key of Baluze 156
f.40 (Lasry's second break in the same volume, GL.htm "?Odoardo Farnese", images `BnF_Baluze156_f40.png` /
`_decipher.png`, not fetched this pass); (b) a different Sabran-circle key in fr.4135-4138; (c) fresh
cryptanalysis of the 137 tokens (short: a homophonic solve at this length is weak, so a control is essential).
One-line suggestion for a solver: the repeat `7 4 t o` sits where the plain text elsewhere names "Levanto" and
"ledit", so a crib (a name ending -ANTO) is the cheapest way into a fresh solve.

Requests: cryptiana.web.fc2.com 4 (2 answered 302 to https, then 2 images at 200). No other host.
Reported what was found and where it was not found; no novelty classification.

## Second Sabran-circle key (Baluze 156 f.40, Farnese-to-Sabran) -- negative, matched control (25 Sept 2026)

LANE YX worker YX-DEC2754 (Sonnet), brief `.claude/briefs/runs/2026-09-25-lane-yx-dec2754.md`, box 45 min.
Job: test Lasry's second Sabran-circle key on f.157r, the one thing the 24 Sept passes above left untried.

**Locate the key.** On disk first: `sources/cryptiana/web/GL.htm` (already quoted above) and
`sources/cryptiana/web/louisxiii.htm` (not previously read for this target). `sources/cryptiana/web/GL/` holds
only one cached image (`BnF_fr3071_f17.png`), not this key -- confirmed by directory listing, not assumed.
`louisxiii.htm` names both ciphers under one "Sabran" section but in **separate, dated H4 subsections**: "1636"
(this exact item -- *"BnF Baluze 156, f.157, is a copy of (presumably Sabran's) letter of 9 February 1536
[sic, presumably a typo for 1636 given DECODE's own 9 Feb 1636 date] to 'Mr de ch.gr.' It has some passages in
cipher, undeciphered."* -- no key or solver named) and "1637" (f.40, *"This was solved by George Lasry in
2022"*). This matters for the search-before-solving record: for fr.4134/fr.4135 (1633/1635) the same page says
outright *"Lasry found that Louis XIII-Sabran Cipher (1631) ... applies to these"* -- i.e. Tomokiyo states
explicitly, letter by letter in that section, wherever a key is known to apply. For f.157 he says only
"undeciphered", with no such sentence. That is not proof the Farnese key fails on f.157 (Tomokiyo may simply
not have checked), but it is independent secondary evidence pointing the same way as the mechanical result
below, worth having found before running the trial rather than after.

Live page: `cryptiana.web.fc2.com/code/GL.htm` section "?Odoardo Farnese, Duke of Parma (1637)" prints "It is
solved as follows" followed by two images -- `GL/BnF_Baluze156_f40.png` (the key table itself, "BNF Baluze
156-f40 Parma", George Lasry 24/05/2022: columns A-X, 1-3 hand-drawn glyph homophones per letter, plus a
separate "Monsieur/Vostre Majeste" nomenclator mark and a null/end mark) and `GL/BnF_Baluze156_decipher.png`
(Lasry's worked decipherment of f.40 itself, confirming the alphabet reads coherent French: "LES NOVVELLES QUE
VOUS ME DONNES DE LA PRISE DE ISLE MONTEST[?] EXTREMEMENT CHERES ... CHIFFRE PARCE QUE LES LETRES PASSENT PAR
DES VOIES PEU SEURES"). Both images fetched (`images/BnF_Baluze156_f40.png`, `images/BnF_Baluze156_decipher.png`,
not committed further than this folder's own copy -- Lasry's work, cite and link it, per CLAUDE.md rule 8). This
is a genuine key table (unlike the brief's fallback case of "no key table published"), so the mechanical test
below was run rather than stopping at the search step.

**Key transcription and shape match.** `key_sabran2_letters.tsv`: each of the 24 key columns' homophone glyphs
(read from a 5x upscaled crop, `images/key_strip0-3.png`) matched by eye to the closest-shaped DC8 token in
`ciphertext_draft.tsv`, same method as `key_sabran_1631_letters.tsv`'s "Letter-symbol half" pass on 24 Sept.
Grade M throughout (glyphs ~15-30 px after upscaling, read by eye, not measured). 19 of 24 letters got a
DC8-token match (some homophones share the same underlying roman-letter/digit shape as another homophone
already claimed by a different column -- ties broken toward the more distinctive stroke, noted per row; ambiguous
or already-claimed shapes left `-` rather than forced). This covers 79 of 137 DC8 tokens (58%), a much larger
share than the first key's letter trial (116 of 137) mainly because several of this key's homophones happen to
be common digit/letter shapes (4, 9, 6, 8, p, g, m, h, t, o, e, d, b, q, r, y, f, tt, ff) that are frequent in
DC8's own transcription -- exactly the kind of superficial overlap CLAUDE.md's matched-control rule exists to
catch, which is why the result below is the one that counts, not the coverage number.

**Result: does not read. Negative with matched control** (`letters_trial.py --key2`, `letters_trial2.tsv`,
`--key2 --check` exits 0):

| | French 5-gram bits/char (lower = more French) |
|---|---|
| DC8 decoded with the key2-derived mapping (79 letters) | **5.412** |
| same mapping, values shuffled over the same token classes, 1000 draws | median **5.412** (50.0% of shuffles score as well or better -- indistinguishable from a random relabeling) |
| positive control: 79 letters of held-out period French, enciphered with the key's homophones under the same token classes, decoded with the same mapping | **3.754** (0.0% of 1000 shuffles as good) |

The positive control shows the test is well calibrated (real French separates cleanly from noise at this
length under this key), but the real DC8 mapping sits exactly on the shuffle median: this key's letter
assignment carries no French signal on f.157r. No word of four or more letters appears in the decode; the
decode runs are gibberish (`MEPIDS B I FA O M F IIBA ERV IMFO S P I LSI M LL S DH BV M F SOI M SL LP I MLE L
IIBM F RLSF LM IH M M FVBQIM O H F F F`, full output in `letters_trial2.tsv`).

**Both of Lasry's published Sabran-circle keys are now tried on f.157r and both are negative with a matched
control**: the first (fr.4134/Baluze 155 f.79) on its nomenclator numbers (0/31 vs control mean 19.1%, 24
Sept) and its letter alphabet (5.649 bits/char vs positive control 3.066, 24 Sept); the second (Baluze 156
f.40, this pass) on its letter alphabet (5.412 bits/char, exactly the shuffle median, vs positive control
3.754). Neither the numeral trial nor the letter trial found any of Lasry's published Sabran-circle homophones
in DC8's own transcription in a way that reads French. What stays untested: (a) a possible unpublished third
key for fr.4135-4138 -- but re-reading `louisxiii.htm` this pass found no evidence such a key exists; the 1633
and 1635 volumes (fr.4134/fr.4135) are both stated to use the *first* (1631) key, not a separate one, so this
lead may not exist rather than merely being unfetched; (b) fresh cryptanalysis of the 137 tokens (still weak at
this length without a crib -- the "7 4 t o" repeat noted 24 Sept, sitting where the plain text names "Levanto"
and "ledit", remains the cheapest lead for a future solver); (c) the shape-match step above is inherently
approximate (eye comparison of small hand-drawn glyphs) -- a solver with more budget could re-derive both
matches from cleaner crops before concluding the shapes themselves rule out both keys, though the negative
control result would need a very large transcription error to reverse.

Status word unchanged: **open**. This job's mandate (test the second Sabran-circle key) is complete; no
reading, so no judge run and no reading reported (per this job's own brief and CLAUDE.md rule 7).

Requests this pass: cryptiana.web.fc2.com 4 (2 target URLs, each answered 302 to plain-http, followed once to
https 200 per the good-citizen one-retry rule, `>=1.5s` apart, UA `cipher-lab research script (contact via
repository)`). No other host. No subagents (mechanical/image-reading work only, within the 45-minute box, done
in about 15 minutes). Reported what was found and where it was not found; no novelty classification (rule 10).
