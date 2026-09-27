found-solved

BEZ-READ, 27 Sept 2026: found-solved -- DECODE (de-crypt.org) record 2704, read in full at
de-crypt.org/decrypt-web/RecordsView/2704 (folio 132-133), status Decrypted, exact shelfmark/sender/
place/date/cipher-type match to this letter, live-verified with no login. See "BEZ-READ: found-solved
on the outstanding check-solved step" below. No transcription or decode attempted; U1-U5 of the job
brief not run.

INTAKE-SAVOY unit B, 27 Sept 2026: solver-ready intake only (Layout, no reading, no decoding, no class), on
the `ciphers/fr4715-montholon-1589` / `ciphers/nevers-birago-fr3251-1572` pattern. Built from KEY-ADJACENT.tsv
row 7 and `sources/cryptiana/web/louisxiv0.htm` (local mirror, the Colbert-Croissy Cipher (1668-1674) section,
read in full this session; not re-fetched).

BEZ-FOLIO, 27 Sept 2026: folio located (see "The folio search" below, resolved). No reading attempted; not a
decode.

# BnF Melanges de Colbert 155, undeciphered letter of Mr l'Evesque de Beziers, Madrid, 13 August 1670

Bishop of Beziers (addressee unspecified in the extract -- likely Colbert or Louis XIV). Digits/syllables,
per louisxiv0.htm.

Tomokiyo, verbatim (louisxiv0.htm, the paragraph immediately after the Colbert-Croissy Cipher (1668-1674)
key table and its usage list across Melanges de Colbert 149-176bis):

> "An undeciphered letter of Mr l'Evesque de Beziers, dated Madrid, 13 August 1670, in Melanges de Colbert 155
> (Gallica) can be read with this key ("afin que silent reprise ...")."

Check-solved header: Tomokiyo's own page is the only source read this pass; his prose explicitly calls this
letter undeciphered and names it as readable with the printed Colbert-Croissy key, giving only the three-word
opening as a worked example. No solver-repository grep run this pass (KEY-ADJACENT.tsv's ranking already
records neither Bourdeau nor Aymeloglu as covering Melanges de Colbert 155 specifically); a fresh grep of both
shallow clones for "Beziers"/"Colbert 155"/"1670" is the outstanding check-solved step before any campaign.

## The gate (this unit's first step)

The page's own text gives only the letter's opening three words ("afin que silent reprise") followed by
Tomokiyo's own trailing ellipsis -- no further decipherment, no per-group alignment. **Gate verdict: only the
opening is given, the expected case** -- this is a genuine open target with a three-word known-plaintext crib,
not a found-solved retirement.

## The folio search (this unit's second step) -- RESOLVED, 27 Sept 2026 (BEZ-FOLIO)

**Folio located: canvas 207-208 (folio 133 recto-verso).** Full detail, every probe and the eye-check in
`images/manifest.json`; summary here.

`archivesetmanuscrits.bnf.fr` finding-aid search (corrected form field `TEXTE_LIBRE_INPUT`, not the
`termeRecherche` guessed first) surfaced the volume's own top-level notice, `ark:/12148/cc95461x`, "Mélanges de
Colbert 155 . Correspondance de Colbert de janvier-décembre 1670" -- confirms the volume's year range but no
item-level sub-notice for the Beziers letter specifically (unlike some sibling Colbert volumes in the same
result page, which do carry dated sub-items). 3 requests used (the cap); not pursued further.

Gallica date bisection: canvas 1 (cover, "COLB. 155 MEL.", no date), canvas 828 (last, address panel to "M. le
duc de Montausier", "decembre 1670"), then canvas 414 (midpoint) read as a memoire (not a letter) internally
dated after 12 Sept 1670 -- directionally after the target, so the target lies in canvas range [2, 414]. The
very next bisection probe, canvas 208 (exact midpoint of that range), landed directly on the target: cipher
numeral groups followed by a clear closing "Monsieur, vostre tres humble et tres obeissant serviteur, P. de
Bonzy E. de Béziers", dateline "A Madrid le 13 aoust 1670", and a sideways marginal filing note repeating the
same. One bisection probe.

Extent and eye-check: canvas 207 carries the pencil foliation "133" (canvas 209 carries "134"), so canvas
207-208 read as folio 133 recto-verso by this one run (not re-anchored elsewhere in the volume). Folio 133r
(canvas 207) is clear-text French (colonial-affairs narrative -- the Indies, a corsair scare, the Honduras
post) continuing from at least folio 132v (canvas 206, same narrative, confirmed), switching to cipher
numerals only at the very bottom of the page; folio 133v (canvas 208) continues the cipher for about 9 lines
then closes in clear as above. Canvas 209/folio 134r opens a different, unrelated, entirely-clear letter
("Charles ce 23 aoust ...", a different date and salutation), confirming folio 133v is this letter's own last
leaf. The letter's actual opening salutation (before the colonial-affairs narrative visible on 132v/133r) was
not located within this job's network cap -- it lies on an earlier folio not yet fetched; named as the next
step below.

Eye-check against the key (grade S, cryptanalytic, not a reading): the first line of cipher numerals at the
bottom of folio 133r, read by eye and looked up in `keys/key_colbert_croissy_1668.tsv` --
2(a) 62(fi) 14(n) = "afin"; 107(que) = "que"; 27-macron(si) 91-macron(le) 14(n) 20(t) = "silent";
21-macron(re) 16(p) 22-macron(ri) 28-macron(se) = "reprise" -- assembles to **"afin que silent reprise"**,
an exact match to `known_plaintext.txt`'s printed crib. This both confirms the folio and confirms the key
applies to at least this opening fragment, partly answering (for this one fragment) the sender/place-outlier
caveat below -- it does not resolve whether the whole letter uses this key consistently.

`images/manifest.json` written (ark, the canvas rule as observed, all bisection probes, the target canvases,
and the eye-check); one image per probed canvas fetched (7 canvases: 1, 414, 828, 206, 207, 208, 209),
1.1 MB total. Requests: gallica.bnf.fr 8 (one retry after a proxy-side connection reset on canvas 206,
`ws_closed_mid_exchange`, per the access playbook's single-retry rule; the manifest itself was read from the
existing cache, no network call); archivesetmanuscrits.bnf.fr 3 (the cap).

**Next step:** the letter's opening folio (before folio 132v) is unlocated; a future worker could step back a
few more canvases from 206 to find the salutation and establish the letter's full leaf count, but this is not
required to begin a transcription -- folio 133r-133v already carries the identified cipher passage and its
close. The calibrated read named in NOTES.md's own "Next step" section (below) can proceed from here.

## What's on disk

- `known_plaintext.txt`: Tomokiyo's own printed three-word opening (grade H per CLAUDE.md rule 4 -- his
  reading, not ours), transcribed verbatim. No group-by-group "DUMP" alignment exists for this letter
  anywhere on the page (checked in full) -- unlike the fr4715-montholon-1589 precedent, a reader has only
  these three words and the key table to calibrate against, no aligned cipher-group anchors.
- `keys/key_colbert_croissy_1668.tsv`: the Colbert-Croissy Cipher (1668-1674) table from `louisxiv0.htm`
  (image `louisxiv_0croissy1668.png`, a clean printed/digital table, not a hand-drawn one) -- 133 rows across
  three diacritic-marked numeral code-spaces (bare/none, macron/overbar, circumflex/caret) sharing the same
  digit range, transcribed by direct inspection of three overlapping upscaled crops plus one independent
  blind Sonnet subagent read of the same crops as a cross-check. The two reads agreed on every row (all
  grade AB); three macron-marked cells (signs 40, 54, 55) print no meaning at all in the source itself,
  recorded as "(blank in source)" at grade H (read correctly as blank). `tools/key_design.py` should read
  this `usable=yes`; design family is a mixed letter/syllable/word nomenclator (homophonic letters plus a
  syllabary plus a small proper-name/common-word code), not a plain substitution -- flag this for
  `design_prior.py` before any attack family is chosen (CRYPT B1/README "Keys as an attack corpus").
- No `images/` content this pass (folio not located, see above).

## An important caveat for any future decode

Every other letter Tomokiyo cites as using this key (Melanges de Colbert 149, 158-167, 176bis, October
1668-December 1673) is Colbert de Croissy's own London-Paris despatch correspondence (to Lionne, later
Seignelay) or the one Duchess-of-Orleans passage in the same volume family. The Beziers letter is the single
outlier: a different sender (the Bishop of Beziers, not Croissy), a different place (Madrid, not London), and
two years earlier than the key's earliest dated London use (1670 vs October 1668 is actually within range, so
not a date problem -- but sender and place both diverge from every other cited use). Tomokiyo's own page does
not explain why this key would also serve a Madrid-Beziers letter; a reader should treat this as an open
question, not confirmed by this transcription, and watch for signs the actual cipher differs (an unusually
high residue of unmatched groups, in the AX-5799/CLAUDE.md rule 3 control-tests-the-manipulation sense) before
trusting a low match rate as evidence of transcription error rather than a wrong-key hypothesis.

## Next step (superseded by the found-solved verdict below)

One careful reader with the key in view, calibrated on the three-word printed opening (`known_plaintext.txt`);
given the very short crib and the sender/place outlier above, the calibration is weak on its own -- a
20-shuffled-key control is still required (CLAUDE.md rule 3) but should be read cautiously at this sample
size, and the reader should flag early whether the letter's own code groups look like this key's mixed
letter/syllable/word design at all before committing to a full decode. Folio located (BEZ-FOLIO, 27 Sept 2026,
"The folio search" above): canvas 207-208 (folio 133 recto-verso), ark:/12148/btv1b100340323 -- the reader can
fetch native-resolution crops of these two canvases directly and begin transcription; the letter's opening
salutation (an earlier folio, not yet located) is not required to start, since the crib's own cipher passage
is on folio 133r-133v.

This step was never run: BEZ-READ's own U0 (the outstanding check-solved step named above) found a
found-solved hit before any crop was fetched. See below.

## BEZ-READ: found-solved on the outstanding check-solved step, 27 Sept 2026

Per this session's brief (`.claude/briefs/runs/2026-09-27-parent-ytbiz-bez-read.md`), U0 was a grep of fresh
shallow clones of `github.com/dbourdeau/cyphersolver` and `github.com/aaymeloglu/unsolved-ciphers` for
"Beziers", "Bezier", "Bonzy", "Colbert 155", "btv1b100340323", to run before any transcription; a hit is a
found-solved stop.

**dbourdeau/cyphersolver** (commit at clone time, 27 Sept 2026): `targets/colbert/arks.txt` lists
`btv1b100340323` (row "155") among a plain enumeration of Colbert-volume Gallica arks, with no accompanying
text about the Beziers letter, Bonzy, or a reading; `targets/colbert/NOTES.md` has no mention of "Beziers",
"Bonzy" or foliation 132/133 anywhere. Not a hit -- this repository's Colbert work does not touch this letter.

**aaymeloglu/unsolved-ciphers**: `catalogue/decode-catalog.csv` (a scrape of DECODE's own RecordsList, no
date recorded in the repo for when it was pulled) row id 2704:

> `2704,"Paris ,Bibliothèque nationale de France, Melanges de Colbert 155, f.132-133 BnF_Mel155_f132","1670
> -","l&lsquot;Evesque de Beziers Spain Madrid","Cleartext: French Plaintext: French",Cipher,**Decrypted**,2,
> https://de-crypt.org/decrypt-web/RecordsView/2704`

This is an exact match on shelfmark (Melanges de Colbert 155, f.132-133 -- f.132 is this letter's continuing
clear-text narrative into f.133r/133v where BEZ-FOLIO located the cipher passage), sender ("l'Evesque de
Beziers"), place (Madrid), and date (1670), with `status=Decrypted`.

**Live verification, 27 Sept 2026 (this session, no login):** `curl -A "cipher-lab research script (contact
via repository)" https://de-crypt.org/decrypt-web/RecordsView/2704` returns HTTP 200 (the RecordsView metadata
page itself is public, unlike its Documents/Images sub-pages -- a route not previously recorded in CLAUDE.md's
DECODE row, worth adding). Full page content, verbatim:

> ID: 2704; Name: BnF_Mel155_f132; Country: France; City: Paris; City: Bibliothèque nationale de France,
> Melanges de Colbert 155, f.132-133; Dates: - ; Author: l'Evesque de Beziers; Sender: (blank); Receiver: Jean
> Baptiste Colbert?; Region: Spain; City: Madrid; Type: Cipher; **Status: Decrypted**; Cipher Type: Homophonic
> substitution, Nomenclatures; Symbol Sets: Graphic signs, Numerical; Pages: 2; Owner: 83; Creator: 83;
> Creation Date: 2021-04-23 00:00:00; Access mode: Authentication required.

The record's own "Cipher Type" field ("Homophonic substitution, Nomenclatures") matches this target's key
design exactly (mixed letter/syllable/word nomenclator, per "What's on disk" above) -- a second independent
confirmation this is the same cipher, not a coincidental shelfmark match. Creation date 2021-04-23 predates
every session in this repository; this is a prior decipherment by the DECODE project, not ours.
`DocumentsList?showmaster=records&fk_id=2704` (the actual decrypted text/documents) returned HTTP 302 (login
required), consistent with the access playbook's DECODE row ("full-size images and non-image documents are
account-wide blocked even when logged in, confirmed from the owner's own browser session") -- not pursued
further; the record's own `Status: Decrypted` field, cross-confirmed by cipher-type match, is sufficient for a
found-solved verdict without viewing the plaintext itself.

**Verdict: found-solved.** This letter already carries a period/modern decipherment recorded on DECODE
(de-crypt.org), record 2704, predating this repository's work by about 5.5 years. No transcription or decode
was attempted this session (U1-U5 of the brief not run, per the brief's own "a hit is a found-solved stop").
Credit: DECODE (de-crypt.org) record 2704, decrypted status set by DECODE account/user id 83 (name not shown
on the public metadata page), creation date 2021-04-23. Key source for AUDIT.md purposes if this target is
ever revisited: `published` (someone else's key/reading, credited) or possibly `ours`-adjacent only in the
narrow sense that this session's own key transcription and folio location independently corroborate DECODE's
cipher-type field and shelfmark -- neither of those establishes the actual plaintext, which this session never
saw. Rule 10 wording: this session found a prior decipherment recorded elsewhere; it does not confirm, dispute
or reproduce that decipherment's content, and no novelty class is claimed or claimable for it.

**If the plaintext itself is later wanted:** DECODE's own account (`DECODE_USER`/`DECODE_PASS`) is confirmed
logged-in-capable (24 Sept 2026 resolution) but the access playbook's DECODE row states full-size
images/documents are account-wide blocked even logged in, so a login attempt here would not be expected to
retrieve record 2704's actual text; the live route to the plaintext, if any, is the owner's own DECODE account
permissions (an ASKS.md-style question, not a repeatable script) or contacting the DECODE project directly.
Not filed as an ASKS.md row this session since no further repo work is blocked on it -- the target's status is
already correctly set to `found-solved` without needing the plaintext in hand.

Requests this session: gallica.bnf.fr 0 (stopped before U1, no crops fetched); de-crypt.org 2
(RecordsView/2704, DocumentsList/2704, 1.5s apart, descriptive UA, no login attempted); GitHub 2 (shallow
clones of both solver repositories, depth 1).
