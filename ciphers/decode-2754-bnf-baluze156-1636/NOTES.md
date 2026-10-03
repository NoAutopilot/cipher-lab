open

Tomokiyo's `louisxiii.htm` (`sources/cryptiana/web/`, read in full by this worker, LANE YX worker YX-DEC2754,
25 Sept 2026) names this exact folio and says only "It has some passages in cipher, undeciphered," unlike his
explicit "applies to these" wording for the sibling letters (fr.4134/fr.4135) already opened by Lasry's first
key; both of Lasry's published Sabran-circle keys (Baluze 155 f.79; Baluze 156 f.40) were then tried directly
on f.157-158's own transcription with a matched control each time (25 Sept 2026) and came back negative
(bits/char sitting at the shuffle-control median against a positive control cleanly separated) -- so this
folio is not already opened by either published key. Verdict-format correction, LANE CX2 25 Sept 2026 (moves
the bare status word to line 1 per CLAUDE.md rule 5 and check-solved.md; no substantive change).

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

## Web and blog check (WEBCHECK-decode-2754-bnf-baluze156-1636, 2 Oct 2026)

Worker WEBCHECK-decode-2754-bnf-baluze156-1636 (account-4, Fable 5.1), brief `.claude/briefs/runs/2026-10-01-account4-webcheck.md`,
box 30 min from 01:04 UTC. The required step of `.claude/briefs/check-solved.md` ("Open web and blog comment threads",
CHECK-SOLVED-WEB, 28 Sept 2026), run on 2 Oct 2026 for this one target only. No transcription, no decoding, no other folder.

**Result: no decipherment or plaintext of this item located by these queries on 2 Oct 2026** (a search result, never a novelty
verdict, rule 10). Status word unchanged (`open`). Every query and every hit opened is listed below.

**(a) Plain web searches (11 queries, web search tool):**

| # | Query | Hits bearing on this letter |
|---|---|---|
| 1 | `Sabran "Mr de ch" 1636 lettre chiffre Baluze` (sender + recipient + date) | only BnF finding aids: `archivesetmanuscrits.bnf.fr/ark:/12148/cc340913/cd0e44` (Baluze 155-156, Sabran papers) and `cc50537t` (Français 4140-4141); no cipher page, no blog |
| 2 | `"Baluze 156" chiffre OR cipher OR chiffré` (shelfmark + chiffre) | none: Wikipedia Great Cipher / Étienne Baluze, EPFL course notes, eBay -- no page naming Baluze 156 |
| 3 | `"Monsieur D'Isabran" OR "Monsieur de Sabran" "party de Turin" 1636` (the leaf's own clear-text opening, from passA.tsv L01) | none: Gallica's collection record `ark:/12148/btv1b9001401d` (Baluze 155, "Lettres adressées à Monsieur de Sabran") and Wikipedia Sabran family pages; no quotation of the phrase anywhere |
| 4 | `Melchior de Sabran Genoa 1636 cipher letter 9 February 1636 undeciphered` (folder's descriptive title) | none: the same Gallica record and unrelated Wikipedia pages |
| 5 | `"decode-2754" OR "R2754" OR "Record 2754" de-crypt.org Sabran` | none: other DECODE RecordsView pages (R1024, R205, R1686, R1601, R2283, R9353), none R2754 |
| 6 | `Lasry "Sabran" cipher Louis XIII 1631 Genoa key Cryptiana` | `dbourdeau.github.io/cyphersolver/index.html` (opened, below); Lasry's HistoCrypt papal-cipher papers (1721, 16th-18th c. papal) -- not this letter |
| 7 | `"Baluze 156" Sabran f. 157 lettre 1636 "Mr de ch"` | BnF finding aids only (Baluze 155-156, Baluze 69/336/380-396, NAF volumes); none names f.157 of Baluze 156 |
| 8 | `"decode-2754-bnf-baluze156-1636" OR "Baluze 156, f.157" OR "Baluze 156 f.157"` | none: Baluze finding aids, Auvray-Poupardin catalogue of the Baluze collection on Gallica (`bpt6k209163c`, not opened -- a 1921 shelf catalogue, no cipher content) |
| 9 | `Sabran Baluze 1636 cipher solved Claude OR GPT OR "solves"` (model-solve announcements, check-solved.md) | none about this letter: the hits are the Cyphral Distich (Urquhart 1653), GPT-6 on a 1918 German radio cipher, and the "No, ChatGPT didn't solve Kryptos 4" gist |
| 10 | `Lasry Sabran Genua Louis XIII Chiffre 1631 gelöst Klaus Schmeh` | Cipherbrain's George Lasry tag page and its 2016 "Three encrypted letters" post (both opened, below); nothing on Sabran |
| 11 | `site:` searches on the three blogs (Sabran / Baluze / Lasry Louis XIII) | the search engine did not honour the `site:` operator (returned Wikipedia/eBay), so each blog's own search box was used instead, (b) below |

**(b) Blog site searches (each blog's own search page, one request at a time, >= 1.5 s apart):**

- *Cipherbrain* (`scienceblogs.de/klausis-krypto-kolumne/?s=`): `Sabran` -- "Wir konnten leider keine Beiträge finden";
  `Baluze` -- same, no results; `Lasry Genua` -- same, no results; `"Louis XIII"` -- one post, "Who can decipher this letter
  from Louis XIII?" (21 Nov 2022), opened under (c). Tag page `/tag/george-lasry/` (10 posts, 2015-2022): none mentions
  Louis XIII, Sabran, Baluze, Genoa or a 1630s French diplomatic cipher.
- *Cryptiana blog* (`cryptiana.blogspot.com/search?q=`): `Sabran` -- one post, "Codebreaking through Comparison of Two
  Independently Enciphered Texts" (29 May 2021), opened under (c); `Baluze` -- one post, "Colbert de Croissy Switched to
  Numerical Cipher in Italy..." (22 May 2021), whose only Baluze sentence is "I made several additions, mainly related to
  Colbert, to [louisxiv0.htm] and [louisxiii.htm] from the Baluze collection in BnF" -- about Colbert's volumes, not this
  one; `1636` -- "No posts matching the query". Tomokiyo's own pages: the on-disk snapshot `sources/cryptiana/web/` grepped
  for `Baluze 156`, `f.157`, `157-158`, `9 February`, `9e febvrier`, `ch.g` (zero requests): hits only in `louisxiii.htm`
  line 302 (the sentence already quoted in the 25 Sept section above: "...It has some passages in cipher, undeciphered"),
  `GL.htm` (Lasry's f.79 and f.40 breaks, already quoted above) and `unsolved.htm` / `unsolved-2026-09-24.htm` line
  385/393: *"Short passages in cipher in a letter to "Mr de ch.g<sup>r</sup>" appears to be in a different cipher, yet
  unsolved."* -- Tomokiyo lists this exact letter as unsolved on his own unsolved page; no decipherment anywhere in the snapshot.
- *Cipher Mysteries* (`ciphermysteries.com/?s=`): `Sabran` -- "Apologies, but no results were found"; `Baluze` -- same;
  `Lasry Louis XIII` -- same; `Genoa 1636` -- one irrelevant Voynich post (11 Sept 2021, "Simon of Genoa", medieval medicine).

**(c) Every plausible hit opened, post and comment thread read:**

1. `cryptiana.blogspot.com/2021/05/codebreaking-through-comparison-of-two.html` (29 May 2021): announces Tomokiyo's solution
   of a cipher in a letter from Abel Servien to Melchior de Sabran (1632) and says he "added references to unsolved ciphers in
   Sabran's letters" to louisxiii.htm and unsolved.htm. **0 comments.** Nothing about f.157 or 1636; the Servien-Sabran 1632
   cipher is a different letter and a different (solved) system.
2. `scienceblogs.de/klausis-krypto-kolumne/who-can-decipher-this-letter-from-louis-xiii/` (21 Nov 2022, English; comments
   disabled, "add it to the German version") and its German original
   `.../2022/11/21/wer-kann-diesen-brief-von-ludwig-xiii-dechiffrieren/`: a two-page letter of Louis XIII, 6 April 1635,
   recipient unknown, from the autograph dealer David Chelli -- not a BnF item, not Sabran's. **11 comments** (Paolo
   Bonavoglia; Thomas Ernst x9, 21 Nov 2022 - 27 Jan 2023; Rizzie, 9 Dec 2022): Cardan-grid guess, tentative transcriptions,
   null/transposition guesses, and Ernst's final verdict that the dealer's letter is a forgery. No comment mentions Sabran,
   Baluze, Genoa, f.157, 1636 or "Mr de ch"; no decipherment of anything.
3. `scienceblogs.de/klausis-krypto-kolumne/2022/07/30/21-bisher-ungeloeste-verschluesselungen-geloest/` (30 July 2022, the
   post on Lasry's 21 solutions of Tomokiyo-listed items, the batch that includes the two Sabran-circle keys of May 2022):
   the post itself names only the Marillac-Du Bellay 1550 letter and points to `cryptiana.web.fc2.com/code/GL.htm` for the
   list. **9 comments** (Lasry x3, Schmeh x2, Jarl, Magnus Ekhall, Thomas, Aginor, 30 July - 2 Aug 2022), all on the Marillac
   letter and congratulations. Nothing on Sabran, Baluze, Genoa, Parma or 1636.
4. `scienceblogs.de/klausis-krypto-kolumne/2016/09/24/three-encrypted-letters-who-can-decrypt-them/` (surfaced by query 10):
   three Vincent LeRay de Chaumont letters of November 1813, solved in the thread by Norbert and Thomas (28 comments).
   Unrelated to this target (the search summary had wrongly attached the Louis XIII 1635 description to it; checked by opening).
5. `dbourdeau.github.io/cyphersolver/index.html` (fetched with curl, grepped): "Sabran" occurs once, inside the entry on a
   Roman-office cipher register whose clear pages name "the Mantuan succession, Sabran, Eggenberg, Susa and the Grisons" as
   topics -- a different target (Bourdeau's papal register), not this letter; no "Baluze", no "2754". Consistent with his
   `CATALOGUE.md` items 191-192 quoted in the 24 Sept section ("not viewed here").
6. BnF finding aid `archivesetmanuscrits.bnf.fr/ark:/12148/cc340913/cd0e44` (Baluze 155-156; WebFetch got 403, curl with a
   browser UA got 200): no occurrence of "chiffr", "157", "158" or "février 1636" for Baluze 156; the only 1636 entry is
   f.220 (Ferdinand II de' Medici, 4 Oct 1636). The Baluze 156 sub-component ajax URL answered 302 without a session cookie
   (as the 24 Sept capture section already found: no item-level description exists for f.157). The sibling record
   `cc50537t` (Français 4140-4141, Sabran's 1636 letter-book) lists several 1636 items "avec chiffre et déchiffrement"
   (f.163/161 "De Paris" 20-21 Aug 1636; f.355 Abbeville 3 Nov 1636; f.195 ff. "Turin" 1-15 Sept 1636; f.247 "Advis
   particullier du Sr de Sabran" on Final) -- none is this letter (9 Feb 1636, to "Mr de ch. g^r"), and none is a
   decipherment of it; logged here as the one-line suggestion below.

One-line suggestion (not run, rule 7 of Usage): Français 4140 carries 1636 Sabran-circle letters with period decipherments
in the same year as f.157; a key-hunt worker could check whether any of those deciphered pairs uses the same mixed
digit/doubled-letter cipher as f.157r before any fresh cryptanalysis (the 24-25 Sept trials above only tested Lasry's two
published Baluze keys).

Requests this pass: scienceblogs.de 10 (4 search pages, 1 tag page, 4 posts incl. the German comment page, 1 curl of the
English post for the German link); cryptiana.blogspot.com 4; ciphermysteries.com 4; archivesetmanuscrits.bnf.fr 4 (one
403 to the fetch tool, then curl 200/302/200, >= 1.5 s apart); dbourdeau.github.io 1; web search engine 11 queries;
cryptiana.web.fc2.com 0 (on-disk snapshot). No 429, no challenge page. No subagents.

Intake gate re-run after this section (`python3 tools/intake_gate_check.py decode-2754-bnf-baluze156-1636`):

```
decode-2754-bnf-baluze156-1636: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit=0
```

## Premise check (GF4-BATCH3, account-4, 3 Oct 2026)

Adversarial pass per `.claude/briefs/check-solved.md` (try to prove the item already done), before any first test.
**Result: not found on (a)-(d); status stays `open`.** One false lead found and explained under (b).

- **(a) Decipherments the folder mentions -- not found.** The only decipherments named here are Lasry's for
  Baluze 155 f.79 and Baluze 156 f.40 (different leaves; both already tried on f.157r above, negative with matched
  controls). DECODE R2754 re-opened live (`RecordsView/2754`, plain GET, 3 Oct 2026): Status *Non-decrypted*,
  "Available Documents" empty, Additional Information only Tomokiyo's pointer to louisxiii.htm, created by
  tomokiyo 2021-05-30. The leaf heads itself "Coppie du 9e febvr 1636"; the two blind passes record no
  interlinear or marginal gloss over the cipher groups.
- **(b) Other solvers' working files -- not found, one false lead.** Fresh shallow clones, 3 Oct 2026:
  dbourdeau/cyphersolver main 2341682 (plus branches `work/open-problem-progress-20260917`, `lorraine-author`) and
  aaymeloglu/unsolved-ciphers main d2800bb, grepped for `Baluze 156`, `2754`, `Isabran`, `Rocca Bert`, `Levanto`,
  `Mr de ch`. Aymeloglu: R2754 only in the raw DECODE harvest. Bourdeau: no target folder, no rendering, no
  apply-key script for this leaf -- **but** his DECODE harvest *excludes* R2754 as already solved:
  `research/catalogue_harvest/decode/overrides.json` and `excluded.json`: "Melchior de Sabran 1636: Tomokiyo's
  DECODE note records Daniel Bourdeau's solution of 15 Sept 2026", and `CATALOGUE.md` l.16 lists "Sabran 1636
  here" among groups "already solved". Checked against the source it cites: Tomokiyo's live
  `cryptiana.web.fc2.com/code/unsolved.htm` (fetched 3 Oct 2026) puts "Daniel Bourdeau notified me of his
  solution on 15 September 2026" under the entry immediately *above*, "Richelieu (1629)" (BnF fr.3829 f.87/89,
  DECODE R9461/R9462), and the Sabran entry that follows ends "Short passages in cipher in a letter to 'Mr de
  ch.gr' appears to be in a different cipher, yet unsolved." The live louisxiii.htm (same date) still says
  f.157 "has some passages in cipher, undeciphered", and the live DECODE record carries no such note. So the
  exclusion is a misattribution of the adjacent Richelieu entry, not a solution; no Bourdeau reading of f.157
  exists in his repository. (Worth a one-line courtesy note to Bourdeau in a future outreach issue; not posted.)
- **(c) Physical neighbours -- not found.** Gallica btv1b9001409q, IIIF at 1600 px, 3 Oct 2026: canvas f161 left
  half (f.156v, the facing page of the cipher) is the address cover of a *different* letter, "A Monsieur
  Monsieur de Sabran cons[eiller] de S.M., gentilhomme ord[inaire] de la chambre ... a Gennes", with a docket,
  no decipherment; canvas f160 (f.155v/156r) is another letter's close and a blank leaf with show-through;
  canvas f163 left (f.158v) carries the docket "Copie de lettre a M. de Ch g^r" and faint writing that is
  show-through of f.157v (compared line for line with `images/dc8_f157v.jpg`: "Il reste encore ... allemans
  sur le Milanois", "Modenois", "S.A. de Savoye"), not a clear copy; f.159r is a new letter ("Monsieur, J'ay
  receu la vostre du xxj ..." on Mantua/Savoy). No slip laid in. 4 Gallica requests, >=2 s apart.
- **(d) Recipient's side -- not found.** The recipient "M. de Ch. g^r" is unidentified (the letter is a copy
  sent on by Sabran's deputy after Sabran left Turin); no recipient-side edition can be named. Interior-phrase
  searches, not the opening: Google Books API (`country=US`, key) `"party de Turin par la voye de Casal"`
  (26 hits, all unrelated Salignac/Gascogne texts), `"Levanto" "Morgues" 1636 Marseille` (0),
  `"Rocca" "Marseille" 1636 "Vitry" Sabran` (0), `"Sabran" 1636 Gennes "Isles de Marguerite"` (1: the 1921
  Baluze catalogue), `"nomme Levanto"` (11, all Garcilaso/Pérou); Internet Archive advancedsearch
  `"Rocca Berti" Marseille` (0), `"Sabran" "Levanto"` (0). Avenel's Richelieu *Lettres* t.V (1635-37) not
  page-read for this letter (the plot on Marseille and the Lérins galleys is the likeliest place a summary
  would surface): a gap, not a block.

Requests this pass: de-crypt.org 1, cryptiana.web.fc2.com 2, gallica.bnf.fr 4, googleapis.com 5, archive.org 3,
github.com 2 clones. Next cheap test (not yet run on this leaf): the Servien-Sabran 1632 cipher
(Tomokiyo's own break, cryptiana) applied to f.157r's transcription with a matched control, since the two Lasry
keys are already negative; Tomokiyo's "different cipher" sentence lowers but does not exclude it.

## Servien-Sabran (1632) key -- negative at the 1% gate, matched control (FT4, account-4, 3 Oct 2026)

First cheap test named by GF4-BATCH3. Intake gate pasted before work:

```
decode-2754-bnf-baluze156-1636: open (line 1) -- edition/page or full-text-search citation found within 6 lines
EXIT=0
```

**Key source.** Not on disk as a table: `sources/cryptiana/web/servien.htm` (Tomokiyo, first posted 29 May 2021) gives
the method and plaintexts but the key only as an image. Fetched once, 3 Oct 2026:
`https://cryptiana.web.fc2.com/code/servien.png` (468x188, "Servien-Sabran Cipher (1632)") and `servien1.png` (first
parallel-text strip, kept for reference), both in `images/servien/` with x3 crops (`key_left.png`, `key_right.png`).
Key recovered by **Satoshi Tomokiyo** (from the two independently enciphered copies Baluze 155 f.123/f.127); credit his.
Transcribed to `key_servien_1632_letters.tsv` (letter, glyph, matched DC8 token, confidence, Tomokiyo's own "?" and
struck entries kept in the note, struck entries not used). The key image is a clean, small digital table, so this was
one reading by the worker (three views of the same image), self-reconciled, not two blind subagent passes; the
uncertain glyphs carry M/L in the `conf` column.

**Overlap first.** Same design family as f.157r: Latin letters, digits and a few signs as homophones, overbars as
distinguishers, plus numbers (12-31) and nulls 10/20/30. 25 of DC8's token classes match a key glyph by base shape
(100 of 135 non-null tokens); code overlap on numbers: 10 (null) and 12 (d), none of 94/36/7. Unmatched: ll, Z, tt, y,
nn, 7, r, 94, ✳, ttu, do, Sr, 36. DC8's two passes recorded no overbars, so 13 of the 25 classes match two or three
key letters (9 = a / a-bar / s / u-bar, n = g / e-bar, o = h / c-bar, ...).

**Test.** `servien_trial.py` (same French 5-gram scorer as `letters_trial.py`; nulls dropped, unmatched tokens break
runs) takes the best bits/char over the overbar choices by one fixed coordinate-ascent search, and applies the same
search to every control, so the search's freedom is matched. `tools/decode_key.py` was not used: its key.tsv needs one
value per code and the overbar ambiguity has none until a transcription records bars.

| row | bits/char | share of 200 shuffled keys as good |
|---|---|---|
| DC8 under Tomokiyo's key (100 letters) | **4.421** | **0.040** (0.048 of 1000 at another seed, not committed) |
| shuffled keys (column letters permuted, homophone structure kept), median / best | 5.101 / 4.212 | |
| positive control: 100 letters held-out French enciphered with the key, same search | **3.938** | 0.000 (74% of letters recovered) |

Decode runs: `IDEDNN GC IST E E S INCT EDLRDIES G T R IEVRITE VVGR COCR EFS E MI E G RV VN IG EVDOL V INCE SE LV SE
IVEGIC E ETE SRC NEO TDC SE SOSO I` -- no French word of four letters or more. fr16 judge (`tools/judge_plaintext.py`,
throwaway spec `{"judge":{"language":"fr"}}`, N=100): `FAIL language: score=-1.755, null_p99=-1.711, real_p05=-0.948,
real_median=-0.775` -- below the letter-shuffled null; the decode's own letter shuffle scored -2.016. Corpus era: no
fr17 corpus in tools/data (fr16 and fr18 only); fr16 is the nearer and was used, and at a score this far below real_p05
an era mismatch cannot be what fails it.

**Verdict: does not read; negative at the 1% gate with matched control** (`servien_trial.py --check` exits 0). It is a
weaker negative than the two Lasry keys (whose real score sat at the shuffle median): the real mapping sits near the
shuffles' 5th percentile, consistent with a shared design family (letters/digits as homophones) giving some French-
like letter frequencies, not with the same key. Tomokiyo's own sentence ("appears to be in a different cipher") stands.
Grades (rule 4): no reading claimed; 0 H, 0 C, 0 S, 100 M (mechanical decode, unconfirmed), 0 I. HYPOTHESES.md opened
with all four key trials side by side. Status word unchanged: **open**.

**Conditional on the transcription** (rule 2): DC8's passes did not record overbars; a pass that records them would
remove the ambiguity search and sharpen this test, but at p ~0.04-0.05 with no word emerging it would have to shift a
lot to read.

**Next key family** (not run): the 1636 Sabran letter-book Français 4140-4141 carries several 1636 letters "avec
chiffre et déchiffrement" (finding aid cc50537t: f.161/163, f.195 ff., f.247, f.355); a period decipherment there in the
same year as f.157 is the next key source -- fetch those leaves (Gallica), compare the cipher's symbol set with DC8 by
shape, and rebuild the key from cipher+decipherment pairs if it matches; ~$6, one worker. Then Avenel t.V for a plain
summary of the Marseille/Lérins plot (crib source).

Requests this pass: cryptiana.web.fc2.com 2 (servien.png, servien1.png; 2 s apart, descriptive UA). No subagents.

## fr.4140 f.146r period key (Sabran, 9 Aug 1636) -- negative, matched controls (FT4b, account-4, 3 Oct 2026)

Next key family named by FT4. Intake gate pasted before work:

```
decode-2754-bnf-baluze156-1636: open (line 1) -- edition/page or full-text-search citation found within 6 lines
```
(run by FT4 the same morning; no change to line 1 since.)

**Locating.** Gallica SRU `dc.source all "Français 4140"` -> **ark btv1b90601914** (481 canvases, every label `NP`;
fr.4141 gave no SRU hit). Canvases are openings; by the folio stamps: canvas 200 = f.109r, **266 = f.146r**, 272 = an
address cover ("Mr de Sabran ... 1636"), **273 = f.151r**, **274 = f.151v / f.152r**, 288 = f.161r (Paris 21 Aug 1636, a
clear copy whose margin glosses numerals: 80 = Espagnols, 75 = Morgues; Final). Offset is not constant (blank versos are
imaged): 200->109, 266->146, 288->161. Finding aid `cc50537t`: "Fol. 146 et 151 ... Mémoire du Sr DE SABRAN ... pour Mgr
l'archevesque de Bordeaux. Avec chiffre et déchiffrement"; the leaf itself is stamped "146 ... et 151", and f.151r is
stamped "151 ... et 146".

**What the leaf is.** f.146r ("9e Aoust 1636. Le sieur de Sabran depuis son retour n'a peu auoir aulcune ...") is the
same mixed design as DC8: plain French with cipher runs of single and doubled letters (ll, nn, ff), digits and signs
(Φ, a looped P, a crossed-tail a), plus plain-spelled cover names (Orion = la republique de Gennes, Polidor = le Roy,
"baldesche" = Sabran) and word codes 60 = galleres, 61 = vaisseaux. The decipherment is **not interlinear**: it is a
separate period clear copy on f.151r (both passes: no gloss on f.146r). One sign = one letter, homophones for s
(h, i, o, g) and e (ll, nn), no nulls seen in the 107 aligned signs.

**Transcription.** Crops: `tools/iiif_lines.py --ark btv1b90601914 --canvas 266 --region 4150,450,3300,4700 --out
images/fr4140 --prefix f146r` (and canvas 273 region 3850,250,3700,6100 for f151r, canvas 274 region 200,350,3450,5150
for f151v), then re-cut locally `--image <src> --lines-per-crop 4` (18 crops per page). Two blind Opus passes
(`images/fr4140/passA_f146.tsv`, `passB_f146.tsv`): both found 13 runs and 109 signs with identical run boundaries;
they split on five shapes (ſ/S, 6/b, 3/z, y/ʒ, and B's '4' where A read a crossed-tail a). Reconciled by the worker
from the source crops (third vision step): ſ, 6, 3, y; the crossed-tail a (clear letter i) kept distinct from 4
(clear letter g), as the clear copy demands. `images/fr4140/pairs_f146.tsv` = 11 letter runs with their f.151r clear
words.

**Key and leaf control (rule 3).** `fr4140_trial.py` aligns the runs with `tools/interlinear_align.py`'s `run_align`
(`--code-prefix @ --clear-consumes` mode, imported). Agreement share (sign occurrences matching their sign's majority
letter, n >= 2): **0.897** vs **0.196** median and **0.327** 99th percentile over 200 permutations of the clear spans
across runs: the leaf pairing beats its own control decisively. Key `images/fr4140/key_f146.tsv`: 29 signs kept, 2
dropped ('6' = m 3 / o 2, probably two shapes -- b and 6 -- that both readers merged; 'c' = m/f). Grade C (from the
period clear copy).

**Target test.** Same scorer as `letters_trial.py`/`servien_trial.py` (French 5-gram, unmapped token breaks a run).

| row | bits/char | share of 200 shuffled keys as good |
|---|---|---|
| DC8 f.157r under the f.146r key (89 of 137 tokens covered) | **5.232** | **0.815** |
| variant: DC8 '4' read as the crossed-tail a (= i) | 4.682 | 0.455 |
| shuffled keys (letters permuted over the 29 signs), median / best | 4.898 / 4.050 | |
| positive control: held-out French, same run lengths, enciphered with the key | **3.366** | 0.000 |

Decode: `V NP P TS G S OTA NES GPS OP SLGNSATE E I GO GG NL TGE R SSTNNS ...` -- no French word of 4+ letters. fr16
judge (throwaway spec `{"judge":{"language":"fr"}}`, N=89): `FAIL language: score=-2.235, null_p99=-1.63,
real_p05=-0.97`. No fr17 corpus exists in tools/data; fr16 is the nearer era, and a score below the letter-shuffle null
is not an era effect. `tools/decode_key.py` was not used for the target: a non-reading needs no committed reading, and
the shuffled-key control lives in the trial script; `python3 fr4140_trial.py --check` exits 0 (rule 7 for the key, the
trial table and `fr4140_decode.txt`).

**Verdict: the f.146r key does not read f.157r; clean negative with matched controls** (the target sits at the shuffle
median, the positive control is cleanly separated). Same design family as DC8 (doubled letters, digits, Φ), different
values -- consistent with Tomokiyo's "appears to be in a different cipher". Grades (rule 4): no reading of the target
claimed (0 H, 0 C, 0 S, 89 M mechanical, 0 I); the key itself is 29 signs at grade C. Status word unchanged: **open**.

**Conditional on the transcription** (rule 2): DC8's own passes (24 Sept, Sonnet) may have merged shapes that this
leaf distinguishes (4 vs crossed-tail a, 6 vs b); the variant row covers the first. A re-read of f.157r against
f.146r's sign shapes would sharpen this, but a key that scores worse than random permutations of itself is not one
merged pair away from reading.

**Next steps (not run, rule 7 of Usage).** (1) fr.4140 carries 17 more Sabran Genoa letters "avec chiffre et
déchiffrement" (Sept-Dec 1636, ff.197-591, the later ones in fr.4141, which SRU did not find on Gallica) and the
Paris 21 Aug letter f.161 (a numeric code with marginal glosses): if Sabran changed keys between correspondents, the
key for "Mr de ch. g^r" may be among his other 1636 tables -- a sweep of the cipher signs per letter (shape inventory
only, no alignment) against DC8's would say which, ~$4. (2) Avenel t.V for a plain summary of the Marseille/Lérins
plot (crib source). (3) The 107-sign key from f.146r is itself a period key for the 17 Sourdis letters (a contribution
row once a verifier has looked).

Requests this pass: gallica.bnf.fr 13 (2 SRU, 1 manifest, 7 probe images at 1000-1400 px, 3 native regions; >= 1.5 s
apart, browser UA, no 403/429), archivesetmanuscrits.bnf.fr 1. Subagents: 2 blind Opus passes. Cost: the
orchestrator's get_session figure.

## fr.4140 Sabran 1636 sign-inventory sweep (FT4c, account-4, 3 Oct 2026)

Step (1) of FT4b's "Next steps": a shape-inventory sweep (no alignment, no reading) of Sabran's other 1636 cipher
letters against f.157r's signs. Intake gate before work: `open (line 1) ... EXIT 0`.

**Pre-registered before scoring** (commit e7df7e20, `PREREG_sweep.md`, `sweep_inventory.py`). The statistic is R, the
share of DC8's 28 recurring sign classes (n >= 2) that appear in a letter's cipher. D counts how many of DC8's numerals
9/7/12/10/94 appear. A letter is a candidate if R >= 0.921 and D >= 2. **Calibration result, run before any letter was
read:** the three known non-keys already reach R 0.643 (f.146r, blind two-pass, D 0), 0.714 (Servien 1632, D 3) and
0.821 (Lasry 1631, D 3). The draft gate, f.146r + 0.15, would have passed the Lasry non-key, so the gate was moved to
the highest control + 0.10 in the same commit. In this family the shape inventory is close to its ceiling: Sabran's
tables share their shapes and differ in their values.

**Where the letters are.** Finding aid cc50537t (fetched 3 Oct 2026) lists 33 Genoa letters, ff.197-591, items
144-176. Seventeen of them are "avec chiffre et déchiffrement", but the aid does not say which. It also lists f.247
"Advis particullier du Sr de Sabran ... château de Final. Avec chiffre et déchiffrement". Folio stamps were read from
one contact sheet of 41 corner crops (vision call 1). That sheet fixes f.198 = canvas 350, 200 = 352, 207 = 363,
208 = 364, 213 = 371, 244 = 420, 245 = 421, 247 = 425, 254 = 436 and 262 = 448. The unstruck stamp is the aid's
numbering. With the earlier anchors, `tools/gallica_folio.py` fits canvas = 1.71 x folio + 14 (inconsistent offsets,
blank versos imaged), which puts fr.4140's last canvas (481) near f.273. **So about 24 of the 33 Genoa folios (276-591)
are in fr.4141, which Gallica SRU does not return. Most of the 17 cipher letters cannot be reached from the cloud.**

**Scored.**

| unit | R | D | candidate |
|---|---|---|---|
| control f.146r (same family, not the key) | 0.643 | 0 | control |
| control Servien 1632 (not the key) | 0.714 | 3 | control |
| control Lasry fr.4134 1631 (not the key) | 0.821 | 3 | control |
| f.247 Final advis (c425, one 1500 px look, grade M) | 0.679 | 0 | **no** |

- **f.247** (vision call 2) has a mixed cipher with an **interlinear period decipherment** (glosses "Varigoti", "Loüan",
  "Boneti", "au chasteau de Final", "trois cent hommes"). Its signs at this resolution are x, an epsilon-E, 3/z, o, r,
  ll, tt, h, n, nn, u, d, a, p, g, y, b, c, 4, 6, Φ and t.
- **f.207** (3 Sept, Genoa) and **f.254** (27 Sept, Genoa) were checked side by side in vision call 3. Both are plain
  French on the recto with no cipher run, so neither has an inventory to score. Of the 17 cipher letters, at most 7
  remain in fr.4140: ff.197, 203, 235, 238, 240 and 252 are not yet located (estimated canvases 351, 362, 416, 421,
  425 and 446 drift by ±5), plus any cipher on the versos.
- f.247 sits inside the control band (0.643-0.821) and shows none of DC8's numerals. That is the same picture as
  f.146r, a same-family table with no sign of DC8's numeric codes. Under the pre-registered calibration limit this
  is **no evidence for or against** f.247's table being f.157r's key. Shapes cannot separate Sabran's tables, which
  is why f.146r shares 18 of 28 classes and still reads at the shuffle median.

**Verdict.** The inventory sweep cannot do what step (1) asked of it. Calibrated against three known non-keys, the
statistic has no headroom in this family, and the one reachable cipher letter scored inside the control band. Only
a values test can tell Sabran's 1636 tables apart: rebuild a table from its cipher-plus-decipherment pairs, then run
the f.157r trial, as FT4b did for f.146r. **f.247 is the best next leaf for that.** Its decipherment is interlinear,
so it aligns more easily than f.146r/f.151r, it is Sabran's own work from the same months, and it shares DC8's x and
epsilon-E, which f.146r lacks. Grades (rule 4): no reading claimed; inventories are grade M. Status word unchanged:
**open**. Vision calls used: 3 of 4. Requests: gallica.bnf.fr 44 (41 corner crops, 3 page views; >= 1.6 s apart,
browser UA, no 403/429), archivesetmanuscrits.bnf.fr 1. No subagents.

## Remaining gaps (FT4c, 3 Oct 2026)
Read so far: 0 of 137 f.157r tokens read; four period/published keys tested negative (two Lasry, Servien 1632, f.146r 1636).
- f.157r cipher runs (137 tokens) - blocker: not-attempted; no key matches yet, sign inventory cannot discriminate (sweep_result.tsv); next: rebuild the f.247 Final-advis key from its interlinear decipherment (iiif_lines crops of canvas 425, 2 blind passes + reconcile, interlinear_align, leaf control) and run fr4140_trial-style test on f.157r, ~$5
- fr.4141 Genoa cipher letters (ff.276-591, most of the 17) - blocker: not-attempted; Gallica SRU returned no record for Français 4141 (3 Oct 2026), and the catalogue sub-unit's own availability flag has not been read; next: read the BnF archivesetmanuscrits sub-unit FRBNFEAD000050537_a19860114 for a digitised-document link, else file a LOCAL-QUEUE row, ~$1

## Escalation (FT4c, 3 Oct 2026)
- [x] siblings: fr.4140 f.146r key and the f.247/207/254 sweep (this section)
- [n/a] clear-pages: f.157v and f.158r are plain French with no cipher
- [x] known-keys: Lasry 1631, Lasry Baluze 156 f.40, Servien 1632, f.146r 1636, all negative with matched controls
- [ ] print: Avenel's Richelieu Lettres t.V, a plain summary of the Marseille/Lérins plot to use as a crib
- [ ] key-rebuild: f.247's interlinear-deciphered table (planned next step)
- [ ] image-check: re-read f.157r for overbars and 6/b, 4/crossed-tail-a against Sabran's own sign shapes
- [n/a] retry: no transient failure to retry this pass
Verdict: keep going: 2 internal gaps; cheapest next: read the fr.4141 catalogue sub-unit's availability flag (~$1), then rebuild the f.247 key from its interlinear decipherment and test it on f.157r, ~$5
