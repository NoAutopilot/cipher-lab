# AUDIT: nevers-birago-fr3251-1572, no.87 cipher passage (VERIFY-NEVBIR-1572, 2 Oct 2026)

Verifier: parent worker VERIFY-NEVBIR-1572 (account 2, for the account-3 orchestrator), a session separate from
the account-4 workers that produced the reading (LIKELY-3, GAPS, GAPS3, GAPS4). Brief
`.claude/briefs/runs/2026-10-02-acct3-verify-nevbir-1572.md`. Clock read with `date -u` at 08:10 and 08:15 UTC,
2 Oct 2026.

**Claim under audit** (brief, from NOTES.md and the NEAR.md row): Birago's 1572 cipher to Nevers (BnF fr.3251,
no.87, f.178v and canvas 182) reads under the printed 1572 key: the whole f.178v (667 signs) at S 532 / M 121,
rank 1 of 201 value-shuffled keys (z 4.84); the clerk's clear decipherment of the whole no.87 passage on canvas 182
matches the decode on 0.837 of letters vs shuffled max 0.114.

## Verdict

| item | scope | class | key | text | confidence |
|---|---|---|---|---|---|
| no.87 cipher passage, f.178r foot + f.178v + f.179r head, 853 signs (Lodovico Birago to the duc de Nevers, Saluzzo, 8 Sept 1572) | the whole passage | **N0** | published (one sign value fitted by us) | known: period decipherment laid in with the letter, BnF fr.3251, Gallica btv1b9060248g canvas 182; no print of it located | high |
| ff.138, 144, 160, 168, 174, 184 (nos. 71-90) | not classed in this section | not classed | -- | -- | -- |
| f.152r cipher run, no.77 (9 June 1572), 97 signs | the run | **N0** (section VERIFY-NEVBIR-152 below) | published | known: later-hand decipherment slip pasted on f.151v; not printed or catalogued | high |

**N0 reason.** Two independent prior decipherments of this very item exist, and neither is ours:
1. *The period one.* The laid-in sheet on canvas 182 (right page, BnF stamp at its foot, lying over the head of
   f.179r; checked by eye on `images/f178v_179r_canvas182.jpg` this session) is a contemporary clear decipherment of
   the whole no.87 passage, 19 lines, "che in di bellaguarda ... che altrimente". It is in the holding archive with the
   letter.
2. *The modern one.* Tomokiyo, `sources/cryptiana/web/nevers.htm` section BnFfr3251, verbatim: "In 1572 ... they used
   a new cipher, which can be reconstructed from the decipherment attached to no.87". The printed table
   (`NeversBirago.png`, our `keys/key_nevers_birago_1572.tsv`) is that reconstruction: he mapped this ciphertext to
   this plaintext to build it.

So the plaintext and the decipherment of no.87 were both known before any session here touched it. Our reading is an
independent re-decipherment of a known item with a published key: a calibration of our transcription and of the
key-as-transcribed against the period answer, which is exactly what LIKELY-3 framed it as ("known-answer step").
That is a real and useful result for the seven unread letters (it shows the readers, the sheet cut and the key work
on this hand), not a reading of an unread text.

Key source: `published` (Tomokiyo's printed Nevers-Birago 1572 table, credited). Ours on top of it: one sign value
(T42 g -> m, GAPS3, fitted by n-gram value-fit and confirmed by the period sheet, 0.837 vs 0.816 printed) and four
C-grade exceptions (the t-shaped X_NEW = m, from the sheet). Text: `known` in the sense of a period decipherment in
the manuscript; no printed edition of the passage's text was located (search below), so status.json's
`text: known` (reserved for plaintext in print) does not strictly apply -- the parent should record it as
"period decipherment in MS".

**Safe sentence.** "Using Tomokiyo's published reconstruction of the 1572 Nevers-Birago key, we re-deciphered the
cipher passage of Birago's letter of 8 September 1572 (BnF fr.3251, no.87) from a blind sign transcription; our
decode matches the contemporary clear decipherment laid in with the letter on 84% of letters, which calibrates the
key and our transcription for the six other 1572 letters Tomokiyo lists without decipherment."

**Unsafe sentence.** "We deciphered Birago's 1572 cipher letter to Nevers" (implies an unread item; it is the
key's own source text, with a period decipherment beside it) -- or any wording with first, new, previously unread.

## Re-derivation (rule 7)

`python3 tools/decode_key.py ciphers/nevers-birago-fr3251-1572 --check` exit 0, "reading up to date"; a full re-run
of the decode left no diff in the working tree. Grades reproduced exactly:

| job | tokens | H | C | S | M | I | U |
|---|---|---|---|---|---|---|---|
| f.178v | 667 | 0 | 0 | 532 | 121 | 1 | 13 |
| f.178r foot | 97 | 0 | 2 | 73 | 17 | 0 | 5 |
| f.179r head | 89 | 0 | 2 | 76 | 8 | 0 | 3 |
| **passage** | **853** | **0** | **4** | **681** | **146** | **1** | **21** |

Reproduces with zero differences, inside the M-graded tokens. The known-answer statistic was re-run independently at
a different seed: `harvest/align_sheet.py passC_no87.tsv --sheet-lines L01-L19 --seed 7` gives 0.837 (fitted map)
and 0.816 (printed map) against 200 value-shuffled keys mean 0.069 / max 0.106, rank 1 of 201 -- the GAPS4 figures
(seed 1: max 0.114) hold.

**Sheet transcription spot-check.** The 0.837 rests on `harvest/f179r_sheet/decipherment_sheet.tsv`, read by eye by
the GAPS4 worker *with the decode already in view* (its L05 note cites "the decode reads nsopla.."), so a contaminated
read was possible. Checked here on the crops of four lines, including the three that carry the four C-grade tokens:
L01 "...arda qual de molti giorni, e..." (de molti: C), L02 "...a ritornare, a car^la ma solo, a..." (ma solo: C),
L13 "confusione, il baron de s adres, ancor che se rend..." and L18 "retrenchiamento, sopra qu..." (retrenchiamento:
C). All four agree with the TSV letter for letter. The spot-check does not cover all 19 lines; a blind re-read of the
sheet by a session that has not seen the decode would remove the contamination caveat entirely.

## Search log (2 Oct 2026, this session)

| family | searched | result |
|---|---|---|
| (a) canonical series / catalogue | Tomokiyo nevers.htm (local mirror, section BnFfr3251, read); BnF finding aid cc49712p via the solver notes | Tomokiyo names no.87 as the key's source decipherment; lists the 7 other 1572 letters without "(with decipherment)" |
| (b) sender/recipient correspondence | Google Books API (`country=US`, keyed): "Lodovico Birago" Nevers 1572; "Birago" "duca di Nevers" lettere | catalogue des manuscrits français (1874/1895), DBI, local histories (Pinerolo, Savigliano, Renata di Francia); no edition of the 1572 letters |
| (c) documentary editions | IA full text (be-api fts): same two queries; snippet read in miscellaneadist02patrgoog and saluzzoeisuoives00saviuoft | Birago family and Nevers in Saluzzo/Piedmont history; "baron Des Adres" in other letters; no text of no.87 |
| (d) holding archive | Gallica canvas 182 image on disk (the laid-in decipherment, BnF stamp) | period decipherment present in the MS (the N0 basis) |
| (e) phrase search on the decoded/sheet text | IA fts and Google Books: "laudarei piu tosto", "saremo sempre in confusione", "retrenchiamento sopra questa gente", "baron des Adres" Birago, "de Memoransi" Birago | 0 IA hits on the three full phrases; Google Books hits on "laudarei piu tosto" and "saremo sempre in confusione" are unrelated texts (snippets read: Miscellanea 1882 is a different letter; Lanteri 1601 fortification); 0 on "retrenchiamento sopra questa gente" |
| (f) solver repos, blogs | dbourdeau/cyphersolver cloned 2 Oct 2026 (head 1 Oct 2026) and grepped for 3251/birago: only f.119 (13 Nov 1571, different cipher) and the 1574 fr.3315 Renato Birago letters; aaymeloglu/unsolved-ciphers cloned (head 27 Sept 2026), `catalogue/decode-catalog.csv` grepped: Birago records are fr.3619/3621/3623 (1591-92), none fr.3251; blogs (Cryptiana, Cipher Mysteries, Klausis) per HARVEST-A 28 Sept 2026, not repeated | no reading of no.87 or of any 1572 letter |
| (g) scholarship | OpenAlex (keyed) 4 queries; Semantic Scholar (keyed) 2; CORE (keyed) 1 | nothing on the 1572 Nevers-Birago cipher; S2's top hit is the 1592 French digit cipher paper (different item) |
| DECODE | via Aymeloglu's catalogue mirror only | no fr.3251 record |
| JSTOR | not queued: at N0 the class rests on the period decipherment and Tomokiyo's statement, which no JSTOR result could lower; a JSTOR hit could only add a print citation | -- |

Requests: be-api.us.archive.org 11, googleapis.com 8, api.openalex.org 4, api.semanticscholar.org 2, api.core.ac.uk 1,
github.com 2 clones. No credentials printed. Unreachable: none.

## Postmortem and corrections

1. **Printed vs fitted key mixed in the claim.** The brief's and PROGRESS.tsv's "under the printed key ... S 532 /
   z 4.84" and "whole passage under the printed key rank 1/201 z 4.60" are fitted-key figures (printed key + T42 = m,
   `sign_id_map_1572_fit.json`). Under the printed key alone f.178v is S 533 / z 4.60 and the passage matches the sheet
   at 0.816. Both are rank 1; the substance stands, the label was wrong. Corrected in PROGRESS.tsv.
2. **The control is by construction, not discovery.** Rank 1 of 201 for a key that was built from this very passage's
   decipherment shows the transcription is good enough for the key to work; it is not evidence about the key's
   correctness beyond what Tomokiyo already established. LIKELY-3 framed it this way; keep that framing outward.
3. **Grades understate.** With the period sheet now read, every token whose decode agrees with the sheet could be
   graded C (known plaintext) rather than S, and the M tokens that agree upgraded too. Not done here (verifiers do not
   decode); it is what the named next step (`tools/interlinear_align.py` sheet alignment) produces.
4. **The firm count** for PROGRESS.tsv is C 4 + S 681 = 685 of 853 from the decode output above (the row had 532,
   which was f.178v's S alone against the passage's 853 total).
5. No over-claiming novelty wording found in NOTES.md (grepped for first/new/novel/unread/previously/unpublished/
   solved/cracked: every hit is ordinary prose or Tomokiyo's own "a new cipher").

SECOND-OPINIONS-QUEUE.tsv: no row for this target exists, and at N0 none is filed (rule: rows are queued at N3 or
better).


# AUDIT: f.152r cipher run, no.77 (VERIFY-NEVBIR-152, 2 Oct 2026)

Verifier: parent worker VERIFY-NEVBIR-152 (account 2, for the owner-account orchestrator), a session separate from the
NEVBIR-152 solver session. Brief `.claude/briefs/runs/2026-10-02-acct3-verify-nevbir-152.md`. Clock read with `date -u` at
17:11 and 17:16 UTC, 2 Oct 2026.

**Claim under audit** (brief, from NOTES.md NEVBIR-152 and PROGRESS.tsv): Lodovico Birago to the duc de Nevers, BnF fr.3251,
no.77 (Saluzzo, 9 June 1572), f.152r (Gallica btv1b9060248g canvas 154), one inline cipher run of 97 signs: printed key +
T42=m ranks 1 of 201 value-shuffled keys, z 2.7-3.1; a later-hand decipherment slip (squared paper, dots for unread signs)
pasted on f.151v covers this run, and the decode agrees with it 0.612 vs shuffled max 0.121 (commit 103e9bd4).

## Verdict

| item | scope | class | key | text | confidence |
|---|---|---|---|---|---|
| no.77 cipher run, f.152r, 97 signs (Birago to Nevers, Saluzzo, 9 June 1572) | the run, "che io disimuli ... l'onore" | **N0** | published (Tomokiyo's 1572 table; the GAPS3 fit T42=m does not occur in this run; five t-shaped X_NEW set to m from the slip, graded M) | known in the MS: a decipherment slip filed with the letter (f.151v); no print of it, and no catalogue mention, located | high |

**N0 reason.** A decipherment of this very run exists and is not ours: the squared-paper slip pasted on f.151v, the page
facing f.152r. Looked at by eye this session on `harvest/f152r/slip_f151v_c154_1350_750_2350_1050.jpg`: four lines,
"che io disimuli poiche [struck: sen ua a leuar..o.asione] / sen.aaleu..o.asione a / ap.ns..o di leuarmi la reputa.ione
..c.ermi / incompromesa la l'onore". `harvest/f152r/decipherment_slip.tsv` agrees with the image letter for letter on all
four lines and the struck line. It is placed exactly at the run (between the letter's prose "et che bisogna" and "con
uolermi"), it leaves dots where its writer could not read a sign, and it carries its own false start struck through: the
working of a decipherer, not a copy of a clear text. So the plaintext of this run and a decipherment of it were known before
any session here, and the class is N0 for the run as a whole. The decode fills some of the slip's dots ("sen[za] alcun[a]
[oc]casione", "cercarmi") and adds a word code at each end ("[quello]", "[qual]") that the slip omits; these are a few
letters of completion of a known partial decipherment, read under a published key, and do not earn a separate class.

**Is the slip printed or catalogued?** Not located in either:
- *Catalogue.* The BnF finding aid for Français 3251 (archivesetmanuscrits.bnf.fr ark:/12148/cc49712p, fetched this session)
  describes no.77 as "Lettre, avec chiffre, de LODOVICO BIRAGO au duca di Nevers ... Da Saluzzo, li IX di giugno 1572";
  "avec chiffre et déchiffrement" is used in the same aid (no.20, fol.39), so the aid does distinguish a decipherment and
  does not record one for no.77. It does not record the no.87 period sheet either (no.87: "avec chiffre" only), so the aid
  is silent about laid-in decipherments of the 1572 letters in general; its silence is weak evidence about the slip.
  Same reading in the printed *Catalogue des manuscrits français* (1874; IA p1cataloguegnr02bibluoft, be-api snippet).
- *Tomokiyo.* `sources/cryptiana/web/nevers.htm` section BnFfr3251 lists "f.152 (no.77) Saluzzo, 9 June 1572" with no
  "(with decipherment)" tag, a tag he uses for nos. 14, 20 and 42 in the same list; `unsolved.htm` line 228 says the 1570-72
  letters "can be deciphered by using keys reconstructed from already deciphered materials". So Tomokiyo states the letter
  is readable with his key but neither prints its plaintext nor mentions the slip.
- *Print.* Phrase searches on the slip's and the decode's Italian, and on the letter's adjacent clear prose, found nothing
  (log below).

**Who wrote the slip, and when.** Not settled. Squared paper, a rounded cursive with modern letter forms, the last line in a
lighter medium (pencil or faded ink), pasted onto the volume before the Gallica capture: consistent with a 19th- or
20th-century reader, not with the 1572 clerk whose sheet sits in no.87. This matters for credit, not for the class: N0 holds
whoever wrote it. The no.82 slip on f.161v (NEVBIR-162) is the same kind of object and probably the same reader; it is not
audited here.

Key source: `published` (Tomokiyo's printed Nevers-Birago 1572 table, credited). Text: known in the sense of a decipherment
filed in the manuscript, not in print; as for no.87, status.json's `text: known` (print) does not strictly apply -- record it
as "decipherment slip in MS".

**Safe sentence.** "Using Tomokiyo's published reconstruction of the 1572 Nevers-Birago key, we re-deciphered the short cipher
run in Birago's letter of 9 June 1572 (BnF fr.3251, no.77, f.152r) from a blind sign transcription; it agrees with a
later-hand decipherment slip pasted on the facing page (f.151v), which we have not found in print or in the BnF catalogue."

**Unsafe sentence.** "We deciphered Birago's cipher of 9 June 1572", or any wording with first, new, previously unread,
unpublished plaintext: the run had been deciphered (partly) by whoever wrote the slip, and the key is Tomokiyo's.

## Re-derivation (rule 7)

`python3 tools/decode_key.py ciphers/nevers-birago-fr3251-1572 --check`: exit 0, "reading up to date"; working tree
unchanged. f.152r job: **97 tokens: H 0, C 0, S 84, M 12, I 0, U 1** -- identical to NOTES.md NEVBIR-152 and PROGRESS.tsv.
`harvest/reading_f152r.txt` reproduces exactly. The control numbers (rank 1/201, z 2.73-3.14 at three seeds; slip agreement
0.612, shuffled max 0.121) were not re-run here (no decoding beyond re-derivation, per brief); they are on file with their
commands.

## Search log (2 Oct 2026, this session)

| family | searched | result |
|---|---|---|
| (a) canonical catalogue | BnF finding aid cc49712p (curl, 1 request), items nos. 71-90; printed Catalogue des manuscrits français 1874 via IA snippet | no.77 "avec chiffre", no decipherment noted (see above) |
| (b) sender/recipient correspondence | IA be-api fts "Birago" Nevers 1572 Saluzzo; "Lodovico Birago" lettere 1572; IA advancedsearch title "memoires" + "nevers" and "duc de Nevers" 1600-1700 (for Gomberville's *Mémoires de M. le duc de Nevers*, 1665) | Saluzzo/Piedmont histories (Savio, Ricotti, Balan), catalogues, Vester's *Renaissance Dynasticism* index (Birago, Ludovico, p.128, 138n36); no edition of the 1572 letters; the 1665 Mémoires not found on IA by title search (not read) |
| (c) documentary editions (Italian/Savoyard) | same fts hits; Google Books "Birago" "IX di giugno 1572" | only the 1874 BnF catalogue (2 hits) |
| (d) holding archive | Gallica canvas 154 slip crop on disk, looked at by eye | the slip (the N0 basis) |
| (e) phrase search on decoded/slip text, IA fts + Google Books (keyed, country=US) | "che io disimuli poiche", "che io dissimuli poiche", "leuarmi la reputatione", "levarmi la reputatione", "in compromesso l honore", "tenere per altro di quello ch io sono" (the letter's next prose), "per altro di quello ch io sono", "et che bisogna" Birago, "Birago" "disimuli" | IA: 0 on all but "in compromesso l honore" (4 hits: Accolti/Council of Trent/Lincei memorie, other letters) and "et che bisogna" Birago (31, unrelated); Google Books hits are word-level matches in unrelated texts (Galileo, Accoramboni 1890, Lincei 1898), snippets read, none this letter |
| (f) solver repos, blogs | dbourdeau/cyphersolver cloned 2 Oct 2026 (head 1 Oct 2026), grepped 3251/birago: `targets/birago` is f.119 (1571), notes the 1572 letters are "in the symbol cipher Tomokiyo reconstructed", no reading; aaymeloglu/unsolved-ciphers cloned (head 27 Sept 2026), `catalogue/decode-catalog.csv`: Birago rows are fr.3619/3621/3623, none fr.3251; Tomokiyo nevers.htm and unsolved.htm (local mirror) read | no reading of no.77 |
| (g) scholarship | OpenAlex (keyed) "Birago Nevers cipher 1572", "Nevers Birago chiffre Saluzzo": 0 and 0; Semantic Scholar (keyed) "Birago Nevers cipher": top hit the 1592 French digit-cipher paper (different item) | nothing on this letter |
| DECODE | via Aymeloglu's catalogue mirror | no fr.3251 record |
| JSTOR | not queued: at N0 the class rests on the slip in the MS, which no JSTOR result could lower | -- |

Requests: archivesetmanuscrits.bnf.fr 1, be-api.us.archive.org 14, archive.org advancedsearch 3, googleapis.com 9,
api.openalex.org 2, api.semanticscholar.org 1, github.com 2 clones. No credentials printed. Unreachable: none.

## Postmortem and corrections

1. **The premise check missed the slip.** PREMISE-NEVBIR's table (NOTES.md, row f.152) checked canvases 154 and 155 and wrote
   "not found on the pages checked"; the slip is on canvas 154's left page. NEVBIR-152 found it and flagged it correctly as a
   prior decipherment for the verifier, and did not offer the reading as ours. Correction note added to that table row.
2. **"Printed key + T42=m" in the claim.** T42 does not occur in this run, so the printed and fitted keys give the same decode
   (NOTES.md says so); the label is harmless here.
3. **Known-answer check is against a partial decipherment.** 0.612 is the share of decoded letters in matched blocks against a
   slip that leaves about 15 signs as dots; it shows the transcription and key reproduce the slip, not that the dotted signs
   are right. The fills the decode makes there are S/M-graded readings under a published key, nothing more.
4. **Grades could rise.** Where the decode agrees with the slip, those tokens could be graded C (known plaintext) rather than
   S; not done here (verifiers do not decode).
5. No novelty wording found in the NEVBIR-152 section, reading file or PROGRESS row (grepped for first/new/novel/unread/
   previously/unpublished/solved/cracked: every hit is ordinary prose -- "first test" (the pipeline step), "a first guess", "the decipherer's own unread signs").

SECOND-OPINIONS-QUEUE.tsv: no row for this item; at N0 none is filed (rows are queued at N3 or better).

---

# AUDIT: no.90 f.184r cipher runs (VERIFY-NEVBIR-184, 2 Oct 2026)

Verifier: parent worker VERIFY-NEVBIR-184 (account 2, for the account-3 orchestrator), a session separate from the
solver session NEVBIR-184 (commit 62d40a28). Brief `.claude/briefs/runs/2026-10-02-acct3-verify-nevbir-184.md`.
Clock read with `date -u` at 17:11 and 17:17 UTC, 2 Oct 2026.

**Claim under audit** (brief): Birago to Nevers, BnF fr.3251, no.90 (Saluzzo, 2 Oct 1572), f.184r, 4 inline cipher
runs, 224 signs: printed 1572 key + T42=m rank 1/201 at 3 seeds, z 3.64-4.15, margin 0.20-0.25 over the best
shuffle, power 17/20 at err 0.12; grades S 190 M 13 U 21; judge FAIL -1.096 vs real_p05 -0.941; no slip found on
canvases 188-190.

## Verdict

| item | scope | class | key | text | confidence |
|---|---|---|---|---|---|
| no.90 f.184r, 4 inline cipher runs, 224 signs (Lodovico Birago to the duc de Nevers, Saluzzo, 2 Oct 1572) | f.184r only | **N3** | published (Tomokiyo's 1572 table; the fitted T42=m is ours but T42 does not occur in these runs) | not known: no period decipherment in the MS, no print located | moderate on the class; the reading itself is cryptanalytic (S/M only, judge FAIL) |
| no.90 f.184v foot, f.185r, f.185v runs | not read | not classed | -- | -- | nothing read |

**Why N3, not N4.** No prior decipherment or print of the plaintext was located (log below), and Tomokiyo lists
no.90 without "(with decipherment)", unlike the 1570-71 items he marks. But the principal printed edition for the
recipient, *Les Mémoires de Monsieur le Duc de Nevers* (Gomberville, Paris 1665, 2 vols), could not be searched
inside: Google Books lists it but returns no inside-the-book hits through the API, and Internet Archive has no full
text of it. JSTOR rows are queued, not answered. Until the Mémoires (which print Nevers papers, mostly later than
1572) are checked for Birago's 1572 letters, N4 is not reached.

**Why not lower.** No decipherment slip, gloss or laid-in sheet on any page from the facing page to the leaf after
the letter's end (check below); no solver repository or DECODE record covers no.90; the search turned up no
edition of Birago's 1572 letters at all.

Key source: `published` (Tomokiyo's printed Nevers-Birago 1572 table, reconstructed from the no.87 decipherment,
credited). Text: not known.

**Safe sentence.** "Using Tomokiyo's published reconstruction of the 1572 Nevers-Birago key, we read the four
cipher runs on f.184r of Birago's letter of 2 October 1572 (BnF fr.3251, no.90) from a blind sign transcription;
the key beats all 200 shuffled keys (z about 3.6-4.2), but the reading is fragmentary (S 190, M 13, unkeyed 21 of
224 signs) and we located no prior decipherment or print of it."

**Unsafe sentence.** "We deciphered Birago's letter of 2 October 1572" (the letter's longer cipher on f.184v-f.185v
is not read, and the f.184r text is fragmentary) -- or any wording with first, new, previously unread, unpublished.

## Re-derivation (rule 7)

`python3 tools/decode_key.py ciphers/nevers-birago-fr3251-1572 --check`: exit 0, "reading up to date";
`harvest/ciphertext_f184r.tsv: tokens 224: M 13, S 190, U 21` -- the claimed grades exactly (H 0 C 0 I 0).
Working tree clean after the run.

Control re-run independently at seeds not used by the solver
(`../ceppo-nevers-fr3251-1570s/harvest/decode_control.py f184r/passC.tsv --map sign_id_map_1572_fit.json --err 0.12`):

| seed | real key | shuffles mean / max | z | rank | power at err 0.12 |
|---|---|---|---|---|---|
| 7 | -1.0162 | -1.594 / -1.257 | 3.78 | 1/201 | 16/20, z median 3.06 min 1.67 |
| 11 | -1.0162 | -1.600 / -1.279 | 3.79 | 1/201 | 19/20, z median 3.25 min 2.21 |
| 7, printed map (no fit) | -1.0162 | -1.601 / -1.253 | 3.81 | 1/201 | not run |

The printed and fitted maps score identically, confirming T42 is absent from these runs. Margin over the best shuffle
0.24-0.26. The solver's figures hold. The grade arithmetic is consistent: 211 agreed signs less 21 off-sheet = S 190;
13 adjudicated = M 13.

## Slip check (brief: facing page and neighbouring canvases)

Gallica btv1b9060248g canvases 187-191 fetched at 2500 px wide, every page looked at by eye, with two native-detail
crops where the page carried faint writing:

| canvas | pages | seen |
|---|---|---|
| 187 | f.182v / f.183r | f.182v end of the previous item, signature and docket; f.183r blank but for a struck number and faint ghost lines (detail crop `pct:52,14,38,40` at 2400 px: show-through/offset, no legible text, no cipher, no pasted slip) |
| 188 | f.183v / f.184r | f.183v blank but for the vertical address docket "...Il Gran Comendatore" of the previous item; f.184r the letter's opening with the four runs, no interlinear gloss, no slip |
| 189 | f.184v / f.185r | prose with cipher at the foot of f.184v and about 20 cipher lines on f.185r; no gloss, no slip |
| 190 | f.185v / f.186r | f.185v the letter's end: one cipher line, "Da Saluzzo li 2 di Ottobre 1572", signature "Lodovico Birago"; f.186r the next item (Carolo Birago, 28 Nov 1572), clear, no slip |
| 191 | f.186v / f.187r | f.186v blank (show-through); f.187r faint mirrored address to the duc de Nevers and show-through (detail crop `pct:51,8,40,45` at 2400 px), no decipherment |

Nothing laid in or pasted between f.183r and f.187r. The solver's page look and PREMISE-NEVBIR's row (NOTES.md,
"not found -- nothing laid in") are confirmed.

## Search log (2 Oct 2026, this session)

| family | searched | result |
|---|---|---|
| (a) canonical / catalogue | Tomokiyo `sources/cryptiana/web/nevers.htm` section BnFfr3251 (local mirror, read); BnF *Catalogue général des manuscrits français* via IA fts (cataloguegnrald00manugoog) | Tomokiyo lists "f.184 (no.90) Saluzzo, 2 October 1572" with no decipherment note; the catalogue gives only "Lettres orig. de Lodovico Birago ... 1569-1572" |
| (b) sender/recipient editions | *Les Mémoires de Monsieur le Duc de Nevers* (1665): Google Books API `country=US` keyed, `Birago intitle:...` and `Saluces 1572 intitle:...`, 0 inside hits; IA advancedsearch for a 17th-c. "duc de Nevers" title: no copy of the Mémoires | **unreachable for search-inside** -- the reason the class stops at N3 |
| (c) Italian / Savoyard editions and histories | IA fts `"Birago" "Nevers" Saluces 1572` (905 hits, top 8 read: Savio *Saluzzo e i suoi vescovi* 1911, *Piccolo archivio storico ... Saluzzo* 1901, Balan *Storia d'Italia*, *Bulletin italien* 1901, Frangipani nunciature); Google Books `"Birago" "duca di Nevers" "1572" lettere cifra` (2), `"Birago" "Milesimo" Langhe 1572 Alemanni` | Birago's biography and death (28 Dec 1572), no text or summary of the 2 Oct 1572 letter |
| (d) holding archive | Gallica canvases 187-191 (above) | no period decipherment |
| (e) phrase search, decoded and clear text | IA fts and Google Books: `"capitano Scipione" Birago` (12 IA hits read: Camillo Orsini's Vita, Suriano despatches, Zapperi -- other captains named Scipione, other contexts), `"lettere inhibitorie" "gran comendatore"` (0), `"lettere inhibitorie al gran"` (GB 8, unrelated), `"Mons. di Sanfre"` (0), `Birago Nevers "2 di Ottobre 1572"` (0), `"pratica con il conte di" Birago` (GB, unrelated) | no print of the letter's clear or cipher text |
| (f) solver repos | dbourdeau/cyphersolver cloned (head 1 Oct 2026), grepped 3251/birago/f.184/no.90: only a mirror of Tomokiyo's page, f.119 (1571) and fr.3315 (1574); aaymeloglu/unsolved-ciphers cloned (head 27 Sept 2026): no fr.3251 record | no reading of no.90 |
| (g) scholarship | OpenAlex keyed `Birago Nevers cipher` (1 irrelevant hit); Semantic Scholar keyed `Birago Nevers 1572 cipher` (0) | nothing |
| DECODE | via Aymeloglu's catalogue mirror | no fr.3251 record |
| JSTOR | two rows queued in `JSTOR-QUEUE.tsv` (family i and ii) | pending; does not block N3 |

Requests: gallica.bnf.fr 7, be-api.us.archive.org 9, archive.org 2, googleapis.com 10, api.openalex.org 1,
api.semanticscholar.org 1, github.com 2 clones. No credentials printed. Unreachable: the 1665 Mémoires (search-inside).

## Postmortem and corrections

1. **No over-claim found.** NOTES.md's NEVBIR-184 section grepped for first/new/novel/unread/previously/
   unpublished/solved/cracked/never: "first test" is pipeline vocabulary (rule 3a) and "unread" refers to this
   letter's own unread runs; nothing to correct.
2. **The reading is weaker than its rank.** Rank 1/201 says the key fits the transcription; the text itself is
   fragmentary (look-alike slips "pranica", "sernunnuti", 21 unkeyed signs) and the judge FAILs. Outward wording must
   keep "fragmentary" (the safe sentence does).
3. **Most of no.90's cipher is still unread** (f.184v foot, f.185r ~20 lines, f.185v). The class covers f.184r
   only; a later reading of the rest needs its own audit line.
4. **Next for N4:** a page check of the 1665 Mémoires de Nevers for Birago's 1572 letters (LOCAL-QUEUE or a person
   with Gallica, which has the Mémoires digitised), plus the queued JSTOR rows.

SECOND-OPINIONS-QUEUE.tsv: row `SO-NEVBIR-F184` filed in this session (N3, CLAUDE.md "Operating model"), prompt
`second-opinions/PROMPT-chatgpt-f184.md`.

---

# AUDIT: no.71 cipher passage, f.139v foot (VERIFY-NEVBIR-139V, 2 Oct 2026)

Verifier: parent worker VERIFY-NEVBIR-139V (account 2, for the account-3 orchestrator), a session separate from
NEVBIR-138, the worker that produced the reading. Brief `.claude/briefs/runs/2026-10-02-acct3-verify-nevbir-139v.md`.
Clock read with `date -u` at 17:11 and 17:18 UTC, 2 Oct 2026.

**Claim under audit** (brief, from NOTES.md "NEVBIR-138" and PROGRESS.tsv): Lodovico Birago to the duc de Nevers,
BnF fr.3251, no.71 (Saluzzo, 7 Feb 1572 per Tomokiyo), cipher at the foot of f.139v (canvas 141), 161 signs: the
printed 1572 key + T42=m ranks 1/201 against value-shuffled keys, z 3.60; grades S 116, M 24, U 21; judge FAIL
-1.159 vs real_p05 -0.955 (commit 29e2a43f).

## Verdict

| item | scope | class | key | text | confidence |
|---|---|---|---|---|---|
| no.71 cipher passage, f.139v foot, 5 lines, 161 signs as transcribed (Birago to Nevers, Saluzzo, 7 Jan or 7 Feb 1572) | partial cryptanalytic reading: about 116 S-grade letters, readable stretches only ("d'andarsi a consultare et cercar ... contra ... il Cocinato ... quanto gli fa che ... sel servitore") | **N3** | published (Tomokiyo's 1572 table) + one sign value fitted by us (T42=m, from no.87's period sheet) | not known: no period decipherment on the leaf or its neighbours, none in print located | medium (search) / low-medium (reading: judge FAIL, 13% unkeyed signs, line ends lost in the gutter) |

**N3, not N4.** No prior plaintext or decipherment of this passage was located after the logged search below. N4 needs
the principal editions covered; the one edition most likely to print a Birago-Nevers letter, Gomberville's *Mémoires de
Monsieur le duc de Nevers* (1665), was not opened page by page here (no Internet Archive copy; Google Books full-text
queries inside the title returned no "Birago"/"Birague" hit, which is a weak negative on OCR'd old type), and the JSTOR
families are queued, not answered. N5 not sought.

**Key source: `published`.** Tomokiyo reconstructed the 1572 Nevers-Birago table from no.87's attached decipherment
(`sources/cryptiana/web/nevers.htm`, live page re-fetched this session, unchanged for this section); T42=m is our one
fitted value (GAPS3), confirmed on no.87's period sheet. This is an independent application of a published key to a
letter that key's author lists without decipherment, not a key recovery: in the words of rule 10, not an `ours` key.

**Safe sentence.** "Applying Tomokiyo's published 1572 Nevers-Birago key (with one sign value fitted against the period
decipherment of no.87) to a value-blind transcription of the five cipher lines of Birago's letter no.71 (BnF fr.3251,
f.139v), we get a partial reading (about 116 of 161 signs at grade S; the key ranks first of 201 shuffled keys, z 3.6);
no prior decipherment of this passage was located in Tomokiyo's catalogue, the two solver repositories, the BnF
manuscript itself (ff.138v-141r checked for slips) or full-text searches of Internet Archive and Google Books on
2 Oct 2026."

**Unsafe sentence.** "We deciphered Birago's letter of February 1572" (the reading is partial, its judge FAILs, about one
sign in eight is unkeyed and line ends are lost in the gutter) -- or any wording with first, new, previously unread,
unpublished. An outward note on this item would need N4 (the 1665 Mémoires read, JSTOR answered) and a cleaner reading.

## Slip and decipherment check (brief item 1)

Canvases 140, 141 and 142 fetched once at native size (8514x5847, 8518x5847, 8515x5850; Gallica IIIF `native.jpg`) and
looked at whole, then at native crops of the cipher block, the space below it, the head of canvas 140's left page and
the foot of canvas 142's right page:
- canvas 141 (f.139v | f.140r): the five cipher lines carry no interlinear or marginal gloss, no pasted slip; the space
  below is blank but for bleed-through. f.140r opens the next letter ("Ill.mo et Ecc.mo sig.", "E molti giorni...").
- canvas 140 (f.138v | f.139r) and canvas 142 (f.140v | f.141r): prose only; the faint script at the foot of f.141r is
  show-through of a subscription from the other side, not a decipherment.
So, unlike no.77 (slip on f.151v) and no.82 (slip on f.161v), no.71 has no decipherment aid on or beside the leaf, and no
known-answer check is possible for it. HARVEST-D2 and NEVBIR-138 saw canvases 139-141 at 1000-2000 px only; this pass is
the native-resolution check the brief asked for.

**New transcription caveat found here.** At native size every cipher line on f.139v runs into the binding: on canvas 141
the last visible sign of L02 ("="), L04 ("e+") and L06 ("m") is cut by the gutter shadow at about x=4310, and the prose
line above ends "di chi fall[i]" the same way. passC records the half-visible last signs (L02 ends X_EQ) but any sign
wholly inside the gutter is unseen, so each line end (and any word spanning it: "cercarn·" / "·oreea", "pf" / "tu") is
conditional on the image (rule 2). Line lengths 31-34 signs suggest at most a sign or two per line; a person at the
volume, or a gutter-opening image, would settle it.

## Re-derivation (rule 7)

`python3 tools/decode_key.py ciphers/nevers-birago-fr3251-1572 --check`: exit 0, "reading up to date"; f139v job
"tokens 161: M 24, S 116, U 21" (H 0, C 0, I 0), identical to `harvest/reading_f139v.txt` and the claim.

Control re-run at two fresh seeds (`../ceppo-nevers-fr3251-1570s/harvest/decode_control.py f139v/passC.tsv --map
sign_id_map_1572_fit.json --windows 0`): seed 7 real -0.998, 200 shuffles mean -1.585 / max -1.239, z 3.60, rank 1/201;
seed 11 mean -1.585 / max -1.234, z 3.57, rank 1/201. NEVBIR-138's figures hold. The power control (10/20 at err 0.15)
was not re-run; it says a miss would have been uninformative, and the hit is the informative direction.

## Search log (2 Oct 2026, this session)

| family | searched | result |
|---|---|---|
| (a) canonical catalogue | Tomokiyo nevers.htm, local mirror (`sources/cryptiana/web/nevers.htm`, 2 Oct 00:10) and the live page (cryptiana.web.fc2.com/code/nevers.htm, fetched 17:1x UTC) | "f.138 (no.71) Saluzzo, 7 February 1572", no "(with decipherment)"; same on both |
| (b) sender/recipient correspondence | Google Books (keyed, `country=US`): "Lodovico Birago" Nevers 1572; "Louis de Birague" Saluces 1572 lettres; "Birago" lettere Saluzzo 1572 Nevers; "Lodovico Birago" lettere 1572 Coconato; "Memoires de monsieur le duc de Nevers" Birago; Birago / Birague intitle:memoires intitle:nevers | BnF catalogue des manuscrits français (1874/1895), DBI, Grande encyclopédie, Piccolo archivio storico di Saluzzo (1901), Storia di Saluzzo (1911); the two 1665 Mémoires volumes are listed but return no Birago/Birague hit inside; no edition of the 1572 letters |
| (c) documentary editions, Italian/Savoyard | IA full text (be-api fts): Birago Coconato; Birago "Voluera"; "conte da Coconato" 1572; "Birago" Nevers Saluzzo 1572 cifra; IA metadata search for the Mémoires de Nevers (only the 1812 novel "La princesse de Nevers") | Coconato/Voluera hits are Piedmontese histories and armorials (Historiae Patriae Monumenta, Ricotti, Segre's Emanuele Filiberto, consegnamenti d'arme); no snippet carries this letter |
| (d) holding archive | Gallica canvases 140-142 at native (above); BnF finding aid cc49712p via Tomokiyo | no decipherment in the MS |
| (e) phrase search, decoded text and the clear text beside it | IA fts "andarsi a consultare" (12 hits: 20th-c. newspapers, a 1963 journal), "procedere ordinario di chi" (0), "manchera di giustitia" (11: Medici-court and unrelated); Google Books "andarsi a consultare" Birago (0), "procedere ordinario di chi falle" (18, all unrelated: 1635 devotional, 1773, modern) | no hit on this letter |
| (f) solver repos, DECODE | dbourdeau/cyphersolver cloned 2 Oct 2026 (head 1 Oct 2026 16:31 -0500), grepped 3251/birago/btv1b9060248g: `targets/birago/` is f.119 (13 Nov 1571, figure cipher) and names f.138 only as a symbol-cipher sibling, no reading; `targets/nevers1574/` is fr.3315. aaymeloglu/unsolved-ciphers cloned (head 27 Sept 2026), `catalogue/decode-catalog.csv`: Birago records are fr.3619/3621/3623 (1591-92), no fr.3251 | no reading of no.71 |
| (g) scholarship | OpenAlex (keyed): "Lodovico Birago Nevers", "Birago Nevers cipher 1572", "Ludovico Birago Saluzzo 1572" (8 records, none on this correspondence); Semantic Scholar (keyed): "Lodovico Birago Saluzzo" (4 irrelevant), "Birago Nevers cipher" 429, not retried; JSTOR: two rows appended to JSTOR-QUEUE.tsv (family i: Birago AND Nevers AND 1572 AND cipher; family ii: the clear-text phrase "procedere ordinario di chi", no cipher keyword) | nothing on the 1572 Nevers-Birago letters |

Unreachable or not done: the 1665 Mémoires de Nevers page by page (no IA copy found; Google Books in-title queries only);
Semantic Scholar one query (429). Requests: gallica.bnf.fr 3, cryptiana.web.fc2.com 2 (one redirect), github.com 2 clones,
be-api.us.archive.org 7, archive.org advancedsearch 3, googleapis.com 14 (5 answered 503, two retried once after a pause),
api.openalex.org 3, api.semanticscholar.org 2. No credentials printed.

## Postmortem and corrections

1. **Gutter loss not recorded.** NEVBIR-138 cut the lines from a 1200 px overview and its crops, and did not note that
   every cipher line ends in the binding. Added above; NOTES.md now carries a one-line pointer. The reading's line-end
   letters are conditional on the image.
2. **Date.** The endorsement (images/manifest.json, "alli 7 di Gennaro 1572") and Tomokiyo's "7 February 1572" disagree;
   still not settled. The safe sentence names neither month alone.
   *Correction, 3 Oct 2026 (FIX-NO71-DATE, from OUT-CHECK-TOMO-BIRAGO2, 04:47 UTC): the "alli 7 di Genaro" docket is on f.137v (canvas 139, left, the facing verso), not f.138r, and reads "Attestat.ne fatta dal M.s ... conto di l'andata a ... alli 7 di Genaro" -- the docket of a preceding attestation, not of letter no.71 (checked on a native crop, canvas 139 region 1050,1800,800,1800). It is no evidence against Tomokiyo's 7 February 1572 for no.71. The verdict above is unchanged; the safe sentence may now give 7 February 1572 (Tomokiyo).*
3. **Content consistency is not confirmation.** "il cocinato" matches the Conte da Coconato in the letter's own clear
   prose; NEVBIR-138 already says this; keep it so outward.
4. **Labels correct.** The claim's "printed 1572 key + T42=m" correctly names the fitted map (the mislabel the no.87
   audit corrected does not recur here). No first/new/novel/unread/solved/cracked wording in the NEVBIR-138 section
   (grepped).
5. PROGRESS.tsv row "Birago 1572 f.138": audit column set from this file.

SECOND-OPINIONS-QUEUE.tsv: row SO-NEVBIR-139V appended (N3), prompt `second-opinions/PROMPT-chatgpt-f139v.md`.

---

# AUDIT: no.82 cipher line, f.162 (canvas 164 right) (VERIFY-NEVBIR-82, 2 Oct 2026)

Verifier: parent worker VERIFY-NEVBIR-82 (account 2, for the account-3 orchestrator), a session separate from the NEVBIR-162
solver session. Brief `.claude/briefs/runs/2026-10-02-acct3-verify-nevbir-82.md`. Clock read with `date -u` at 18:12 and 18:16
UTC, 2 Oct 2026.

**Claim under audit** (brief, from NOTES.md NEVBIR-162 and PROGRESS.tsv): Lodovico Birago to the duc de Nevers, BnF fr.3251,
no.82 (Saluzzo, 27 June 1572; finding aid "Fol. 162", ink "160"), one cipher line on Gallica btv1b9060248g canvas 164 right,
25 signs in two runs (21 + 4). Under the published 1572 key, run 1 ranks 1 of 201 value-shuffled keys (z 2.6-2.9, power only
2-10/20 at 21 letters); a later-hand decipherment slip pasted on the facing f.161v reads "[monsignore di S. Andre]" /
"[M. di Bellaguarda]", and run 1 agrees with it on 0.737 of letters vs shuffled max 0.148 (commit b5e121af).

## Verdict

| item | scope | class | key | text | confidence |
|---|---|---|---|---|---|
| no.82 cipher line, f.162 (canvas 164 right), 25 signs (Birago to Nevers, Saluzzo, 27 June 1572) | both runs: "ho scorto qua che [run 1], quale e tutta cosa di [run 2]" | **N0** | published (Tomokiyo's 1572 table; T42 does not occur, so printed = fitted key here); run 2's name code ("M." + 4 7 + u) has no key source but the slip | known in the MS: a decipherment slip filed with the letter (f.161v); no print of it, and no catalogue mention, located | high |

**N0 reason.** A decipherment of this very line exists and is not ours. Looked at by eye this session on
`harvest/f162r/slip_f161v_c164_1400_3450_2100_800.jpg` and on a fresh 2500 px view of the whole of canvas 164: a rectangular
slip, mounted on the left page of the opening (f.161v, the back of no.81 with its Spanish address to Birago), directly facing
the cipher line. Two lines in a rounded modern-looking cursive: "ho scorto quà che [monsignore di S. Andre], / quale è tutta
cosi di [M. di Bellaguarda],". `harvest/f162r/decipherment_slip.tsv` agrees with the image letter for letter. The slip copies
the clear words around the cipher (with one slip of its own, "cosi" for the letter's "cosa") and brackets the deciphered parts,
covering the whole cipher of the letter -- both runs. Unlike the f.151v slip of no.77 it has no dots or struck false start: it
is a fair copy of a result, not working. Either way the plaintext of both runs and a decipherment of them were known before
any session here, so the class is N0 for the line as a whole. The decode reproduces run 1 ("·monsignobedisandre"; the struck
pair T63 T81 cancelled by the writer, T81 = b where the slip has r, X_EQ set to d from the slip) and does not read run 2 at all.

**Is the slip printed or catalogued?** Not located in either:
- *Catalogue.* BnF finding aid cc49712p (fetched again this session): "Fol. 162 • 82 Lettre, avec chiffre, de « LODOVICO
  BIRAGO,... all' illmo... sigr duca di Nevers,... Da Saluzzo, li 27 di giugno 1572 ». En italien." -- "avec chiffre" only,
  where the same aid writes "avec chiffre et déchiffrement" for no.20; as noted for no.77, the aid is silent about every laid-in
  decipherment of the 1572 letters (no.87's clerk sheet included), so its silence is weak evidence. The printed 1874 *Catalogue
  des manuscrits français* carries the same entry (IA/Google Books hits for "27 di giugno 1572").
- *Tomokiyo.* `sources/cryptiana/web/nevers.htm` line 780: "f.160 (no.82) Saluzzo, 27 June 1572", no "(with decipherment)" tag
  (he uses it for nos. 14, 20, 42). No plaintext of this letter there.
- *Print.* Phrase searches on the slip and on the letter's adjacent clear prose found nothing (log below).

**Who wrote the slip, and when.** Not settled. Compared by eye this session with the f.151v slip (no.77): the same rounded hand (the
looped d of "di", the r and the g forms), but on plain paper where f.151v is squared, and a fair copy where f.151v is working;
consistent with a 19th- or 20th-century reader, pasted before the Gallica capture; not the 1572 clerk. Matters for credit, not
for the class.

**Run 2 / code 47.** The slip's "M. di Bellaguarda" is the only source for the 4-sign name code (T54 "m" + digit-like "4" "7"
+ T49 "u"). Entering 47 = Bellaguarda in the key is allowed at grade **C** (known plaintext from the slip), with the provenance
"later-hand slip, f.161v, hand and date unsettled" written beside it, and graded M wherever it is used outside this letter until a
second attestation turns up (rule 4's single-witness caution). Not entered here (verifiers do not decode). Identifying the two
persons is not attempted here.

Key source: `published` (Tomokiyo's 1572 table, credited) for run 1; the slip for run 2. Text: known in the sense of a
decipherment filed in the manuscript, not in print -- status.json `text: known` (print) does not strictly apply; record it as
"decipherment slip in MS", as for no.77.

**Safe sentence.** "Using Tomokiyo's published reconstruction of the 1572 Nevers-Birago key, we re-deciphered the one cipher line
in Birago's letter of 27 June 1572 (BnF fr.3251, no.82, f.162) from a blind sign transcription; its first run agrees with a
later-hand decipherment slip pasted on the facing page (f.161v), which also gives the name code we could not key, and which we
have not found in print or in the BnF catalogue."

**Unsafe sentence.** "We deciphered Birago's letter of 27 June 1572", or any wording with first, new, previously unread or
unpublished plaintext: the line had been deciphered by whoever wrote the slip, and the key is Tomokiyo's.

## Re-derivation (rule 7)

`python3 tools/decode_key.py ciphers/nevers-birago-fr3251-1572 --check`: exit 0, "reading up to date"; working tree unchanged.
f.162r job: **25 tokens: H 0, C 0, S 8, M 14, I 0, U 3** -- identical to NOTES.md NEVBIR-162 and PROGRESS.tsv. Control numbers
(rank 1/201 at three seeds; slip agreement 0.737, shuffled max 0.148) were not re-run (no decoding beyond re-derivation, per brief);
they are on file with their commands. At 21 letters the n-gram control is weak (power 2-10/20), so the slip, not the control, is
what backs this line.

## Slip check (brief: facing page and neighbouring canvases)

Canvases 163, 164, 165 fetched once each at 2500 px (Gallica IIIF, 3 requests) and looked at whole:
- 163: f.160v/161r, near-blank (bleed-through, address traces); nothing laid in.
- 164: left page = back of no.81 (Spanish address to Birago, flourish) **with the mounted decipherment slip in its lower half**;
  right page = no.82's opening, the cipher line at line 9 ("ho scorto qua che ... quale e tutta cosa di ...").
- 165: left page = no.82 continued, all plain (one word written in spaced capitals, "FRANCIA", is plain text, not cipher); right
  = the "Doppo scritto sono avisato ..." postscript slip, plain, not a decipherment (as PREMISE-NEVBIR and NEVBIR-162 said).
Canvas 166 (letter end, the same postscript slip face down) was not refetched: NEVBIR-162's 1200 px view and
`images/f162v_insert2_canvas166.jpg` are on disk. No second decipherment found.

## Search log (2 Oct 2026, this session)

| family | searched | result |
|---|---|---|
| (a) canonical catalogue | BnF finding aid cc49712p (curl, 1 request), no.82 and neighbours; 1874 printed catalogue via IA/Google Books hits | no.82 "avec chiffre", no decipherment noted |
| (b) sender/recipient correspondence | IA fts + Google Books "Birago" "27 di giugno 1572"; "Bellaguarda" Birago Saluzzo; Birago Bellegarde "S. Andre" 1572 | the 1874 catalogue; Segre, *Emanuele Filiberto e la Repubblica di Venezia* (1901; IA emanuelefilibert00segruoft): its "27 di giugno 1572" is a Messina letter, its Birago/Bellegarde passages are on the Saluzzo quarrels, not this letter; *Historiae Patriae Monumenta*, Albèri *Relazioni*: general Birago mentions; no edition of the 1572 letters. The 1665 *Mémoires de Nevers* not read page by page (as for no.77/no.90) |
| (c) documentary editions (Italian/Savoyard) | same queries | as (b) |
| (d) holding archive | Gallica canvases 163-165 at 2500 px; slip crop on disk | the slip (the N0 basis) |
| (e) phrase search, IA fts + Google Books (keyed, country=US) | "ho scorto qua che", "ho scorto quà che", "quale è tutta cosa di", "quale e tutta cosa di", "monsignore di S. Andre" Birago, "Monsignor d'Autefort" Birago, "Leandro Ongarese" (the letter's own clear prose) | IA 0 on all; Google Books word-level matches in unrelated texts (Vasari, Varchi, an 1857 encyclopedia, a 1934 Rivista), snippets read, none this letter |
| (f) solver repos, blogs | dbourdeau/cyphersolver cloned (head 1 Oct 2026), grepped 3251/birago/Bellaguarda/"S. Andre"/"scorto qua": only `targets/birago` (f.119, 1571) and fr.3315 nevers1574; aaymeloglu/unsolved-ciphers cloned (head 27 Sept 2026): no fr.3251 record; Tomokiyo nevers.htm (local mirror) | no reading of no.82 |
| (g) scholarship | OpenAlex (keyed) "Birago Nevers Bellegarde 1572": 1 unrelated hit | nothing on this letter |
| JSTOR | not queued: at N0 the class rests on the slip in the MS, which no JSTOR result could lower | -- |

Requests: gallica.bnf.fr 3, archivesetmanuscrits.bnf.fr 1, be-api.us.archive.org 13, archive.org metadata 1, googleapis.com 10,
api.openalex.org 1, github.com 2 clones. No credentials printed. Unreachable: none.

## Postmortem and corrections

1. **The premise check missed the slip again.** PREMISE-NEVBIR's row f.160/162 checked canvases 163, 165, 166 and not 164, where
   both the cipher line and the slip are; NEVBIR-162 found both and flagged the slip correctly as a prior decipherment for the
   verifier, without offering the reading as ours. Correction note added to that table row. Third leaf in this volume with a
   laid-in decipherment (no.77, no.82, and no.87's clerk sheet): a premise check on this volume must look at every canvas of an
   opening, both pages.
2. **One exception is slip-derived.** `harvest/exceptions_f162r.tsv` sets X_EQ (pos 19) = d "the slip's d", graded M: that value
   comes from known plaintext, so the 0.737 agreement is not wholly independent of the slip (1 letter of 19). Harmless at N0; noted.
3. **Grades could rise.** Tokens where the decode matches the slip could be C rather than S; not done here.
4. **"cosi" vs "cosa".** The slip's clear context differs from the letter by one letter; the slip writer's copying error, recorded
   in `decipherment_slip.tsv`. No effect on the class.
5. No novelty wording in the NEVBIR-162 section, reading file or PROGRESS row (grepped for first/new/novel/unread/previously/
   unpublished/solved/cracked: hits are ordinary prose -- "a first cut", the pipeline's "first run").
6. PROGRESS.tsv row "Birago 1572 f.162": audit column set from this file.

SECOND-OPINIONS-QUEUE.tsv: no row for this item; at N0 none is filed (rows are queued at N3 or better).

---

# AUDIT: no.86, all its cipher (f.174r foot + f.174v + f.175r head + f.175v, 759 signs) (VERIFY-NEVBIR-86, 2 Oct 2026)

Verifier: parent worker VERIFY-NEVBIR-86 (account 2, for the account-3 orchestrator), a session separate from the solver
sessions NEVBIR-170, NEVBIR-174V-A (commit a1d9bef2) and NEVBIR-174V-B (commit bad39c69). Brief
`.claude/briefs/runs/2026-10-02-acct3-verify-nevbir-86.md`. Clock read with `date -u` at 19:10, 19:16 and 19:22 UTC, 2 Oct 2026.

**Claim under audit** (brief): Birago to Nevers, BnF fr.3251, no.86 (Saluzzo, 27 Aug 1572): all its cipher read blind --
f.174r foot (85) + f.174v (674 incl. f.175r head and f.175v) = 759 signs -- under the published 1572 key + T42=m: whole
letter rank 1/201 at 3 seeds, z 3.56-3.83, power 13/20 at err 0.23; S 629 M 76 U 54; judge FAIL -1.161; no slip on
canvases 178-179.

## Verdict

| item | scope | class | key | text | confidence |
|---|---|---|---|---|---|
| no.86 cipher, 759 signs (Lodovico Birago to the duc de Nevers, Saluzzo, 27 Aug 1572): f.174r foot, f.174v (22 cipher lines), f.175r head line, f.175v 3 lines | the whole letter's cipher | **N3** | published (Tomokiyo's 1572 table, credited); the fitted T42=m is ours (GAPS3) but T42 occurs once in these 759 signs and the printed map scores the same (below) | not known: no period decipherment in the MS, no print located | moderate on the class; the reading is cryptanalytic (S/M only, H 0 C 0, judge FAIL) and fragmentary |

**Why N3, not N4.** No prior decipherment or print of the plaintext was located (log below). The gap that held the sibling
audits at N3 is now half closed: Gallica's search-inside answers on both scans of volume 1 of Gomberville's *Les Mémoires de
Monsieur le duc de Nevers* (1665; `bpt6k6435941k` and `bpt6k8717151d`, 1028 and 1024 views). It has 29 Birague hits, all on
Carles (Charles) de Birague, mostly the 1574 restitution papers of Pinerolo and Savigliano, plus the Chancellor. It has no
Birago/Lodovico letter of 1572, no "Sadres", no "Voluera", no "Montesquiou", and no "Aoust 1572" item from Saluzzo.
Volume 2 was not located on Gallica under the SRU queries used, and the JSTOR rows are unanswered. N4 needs volume 2 read,
plus the open-index scholarship pass repeated once Semantic Scholar answers more than one query.

**Why not lower.** No decipherment slip, gloss or laid-in sheet anywhere from the address leaf to the letter's end (check
below). The no.87 clerk sheet (canvas 182, `harvest/f179r_sheet/`) is no.87's own decipherment: it matched no.87's decode on
0.837 of letters. It is not a key source for no.86. No solver repository or DECODE record reads no.86. Tomokiyo lists
"f.174 (no.86) Saluzzo, 27 August 1572" without "(with decipherment)".

Key source: `published` (Tomokiyo's Nevers-Birago 1572 table, reconstructed by him from the decipherment attached to no.87,
`sources/cryptiana/web/nevers.htm`, credited). Text: not known.

**Safe sentence.** "Using Tomokiyo's published reconstruction of the 1572 Nevers-Birago key, we read all the cipher of
Birago's letter of 27 August 1572 (BnF fr.3251, no.86; 759 signs on ff.174r-175v) from a blind sign transcription. The key
beats all 200 shuffled keys at five seeds (z about 3.6-3.8), but the reading is fragmentary (S 629, M 76, unkeyed 54) and fails
the language judge. We located no prior decipherment or print of it."

**Unsafe sentence.** "We deciphered Birago's letter of 27 August 1572", without "fragmentary" and the judge FAIL. Also unsafe:
any wording with first, new, previously unread or unpublished.

## Re-derivation (rule 7)

`python3 tools/decode_key.py ciphers/nevers-birago-fr3251-1572 --check`: exit 0, "reading up to date". The three no.86 jobs
reproduce the claimed grades exactly: `ciphertext_no86.tsv: tokens 759: M 76, S 629, U 54` (H 0 C 0 I 0);
`ciphertext_f174vA.tsv` 285 (M 25 S 242 U 18); `ciphertext_no86B.tsv` 389 (M 42 S 318 U 29). The working tree was clean
after the run.

Control re-run independently at seeds the solvers did not use
(`../ceppo-nevers-fr3251-1570s/harvest/decode_control.py no86/passC_all.tsv --map <map>`, 200 value-shuffled keys, it16dip):

| seed | map | real key | shuffles mean / max | z | rank | power control |
|---|---|---|---|---|---|---|
| 7 | fitted (T42=m) | -1.1134 | -1.608 / -1.311 | 3.71 | 1/201 | 11/20 at err 0.23 (z median 2.44) |
| 11 | fitted | -1.1134 | -1.603 / -1.277 | 3.72 | 1/201 | 20/20 at err 0.10 (z median 4.34, min 3.02) |
| 7 | printed (no fit) | -1.1138 | -1.615 / -1.311 | 3.75 | 1/201 | not run |

The solvers' figures hold. The real key is rank 1 at all five seeds now run (1, 2, 3, 7, 11), 0.16-0.22 clear of the best
shuffle. The printed and fitted maps differ by 0.0004, so the T42 fit carries nothing here. Power at the pre-adjudication
error (0.23) is only 11-13/20. The target took rank 1 regardless, so this is a pass at this length, not a licence to read
a miss elsewhere as a negative.

**Digit-pair codes checked on the crops (brief item).** In the printed key (`keys/key_nevers_birago_1572.tsv` rows 67-69),
the word codes are the plain digit pairs "85" = carmagnola, "86" = turino and "89" = bugonotti; on the sign sheet these are
T11, T46 and T15. On `harvest/f174v/f174v_L07_s2.jpg` the line reads plainly "... 8 9 ⊣ 8 5 ...". Half A's adjudicated T15
(L07, L09, L11) and T11 (L04, L07) calls are therefore the printed codes, not look-alikes. The letter's clear prose on f.174r
supports this: it says "buona parte uganotti" and names Carmagnola's garrison. The "88" on half B L02 (`f174vB_L02_s2.jpg`,
the "lone 8" pair) is not in the printed table. It stays unkeyed (U), correctly; it is probably a further numeric code
(open-codes).

## Correction found (not applied: transcription is the solver's)

**f.174r L04, positions 1-2.** `harvest/f174r/passC.tsv` reads this pair as T46 (turino) + X_S, with the note "8-like mark ...
small s/5-like mark then comma". The crop `harvest/f174r/f174r_L04_s1.jpg`, and canvas 177 at native, show the digit pair
"8 5," before the prose "et credo chel Voluera". Under the printed key that is **85 = carmagnola (T11)**, one token replacing
two. The run's last word should therefore be [carmagnola], not [turino]. This changes one S-graded word and one U, and does
not move the control. It is logged as a next step in NOTES.md "Remaining gaps" for the solver lane (re-cut L04 and re-run
`build_decode_inputs.py` and `decode_key.py --check`). This verifier did not edit the transcription.

## Slip check (brief: facing page and neighbouring canvases at native resolution)

Gallica btv1b9060248g. Canvases 177, 179 and 180 were fetched once whole at native size (about 8515 x 5850) and viewed in
four quadrant tiles each. Canvas 181 was viewed at 2200 px. Canvas 178 was viewed at native by NEVBIR-174V-A and at 3000 px
by NEVBIR-174V-B (not re-fetched).

| canvas | pages | seen |
|---|---|---|
| 177 | f.173v / f.174r | f.173v prose to "sei mesi"; f.174r prose, then 3 cipher lines and "85, et credo chel Voluera ... in Corte" at the foot; no gloss, no slip; mirrored show-through of f.174v's cipher on the left margin only |
| 178 | f.174v / f.175r | (solvers, native) cipher page and one head line; no slip |
| 179 | f.175v / f.176r | f.175v prose, the 3-line cipher run after "ho scritto al", then "Circa alla Carta dil Piemonte"; f.176r prose ("il baron de Sadres che la Voluera ..."); no gloss, no slip |
| 180 | f.176v / f.177r | prose; f.177r ends "Da Saluzzo li 27 di Agosto 1572", subscription and signature Lodovico Birago; lower f.177r show-through only |
| 181 | f.177v / f.178r | f.177v address leaf to the duc de Nevers, "In Corte", seal trace and docket; f.178r opens no.87; nothing laid in |

Nothing is pasted or laid in between the address leaf and the end of no.86. The solvers' slip checks are confirmed. One
detail is corrected: the clear prose names "il Baron de Sadres" on **f.174r** as well as f.176r, so NEVBIR-174V-B's
consistency observation for L16 has a second clear-text anchor. It is still not a crib.

## Search log (2 Oct 2026, this session)

| family | searched | result |
|---|---|---|
| (a) canonical / catalogue | Tomokiyo `sources/cryptiana/web/nevers.htm` section BnFfr3251 (local mirror); BnF *Catalogue général des manuscrits français* via IA fts (`p1cataloguegnr02bibluoft`, hit on "Birago" + "27 di Agosto 1572") | Tomokiyo lists no.86 without a decipherment note; the catalogue lists Lodovico Birago's letters ("En italien") only |
| (b) sender/recipient editions | Gomberville, *Mémoires de M. le duc de Nevers* (1665) vol. 1, Gallica ContentSearch on `bpt6k6435941k` and `bpt6k8717151d`: Birague (29 hits), Birago (0), Lodovico (4, all Lodovico Gonzaga), Ludovic (0), Saluzzo (0), Saluces (many, 1574 restitution and 1588), Sadres (0), Voluera (0), Montesquiou (0), Hautefort (2, 1574 Pinerolo), Bellegarde (8, 1579 and later), Carmagnolles (30, 1574), "Aoust 1572" (44, none a Saluzzo letter), 1572 (3) | no Birago letter of 1572 in vol. 1; **vol. 2 not located** on Gallica by SRU (`dc.title all "memoires duc de Nevers"`, `gallica all "memoires de monsieur le duc de nevers"`) |
| (c) Italian / Savoyard editions and histories | Google Books (keyed, `country=US`): `"Birago" "Voluera"` (10: Della Chiesa, *Dell'historia di Piemonte* 1607/1608, names Cesare Voluera as Birago's lieutenant in Carmagnola; *Scriptores* 1840), `"Lodovico Birago" Hautefort OR Autefort` (4, all the BnF catalogue), `"Birago" "Sadres" 1572` (0); IA fts `"Lodovico Birago" Voluera` (0), `"Birago" "Sadres"` (14, none relevant) | context for the names, no text or summary of the 27 Aug 1572 letter |
| (d) holding archive | Gallica canvases 177-181 (above); BnF clerk sheet canvas 182 (no.87's) | no period decipherment of no.86 |
| (e) phrase search, decoded and clear text | IA fts and Google Books: `"baron de Sadres"` (IA 1, GB 4: Salazar y Castro index, a 1558 letter; Spanish catalogue 1961), `"barone di Sadres"` (IA 0), `"mala gratia d altri"` (IA 0; GB 347 loose matches, top 5 unrelated: Paruta 1599, Atti delle assemblee costituzionali), `"Birago" Nevers "27 agosto 1572"` (GB 503, not retried) | no print of the letter's clear or cipher text |
| (f) solver repos | dbourdeau/cyphersolver cloned (head 1 Oct 2026): `targets/birago` is f.119 (no.63, Nov 1571, numeric cipher); grep 3251/birago/no.86/f.174/Sadres finds only the nevers.htm mirror line "f.174 (no.86) Saluzzo, 27 August 1572"; aaymeloglu/unsolved-ciphers cloned (head 27 Sept 2026): no fr.3251 record (decode-catalog.csv hits are other shelfmarks) | no reading of no.86 |
| (g) scholarship | OpenAlex keyed `Birago Nevers 1572 Saluzzo` (0); Semantic Scholar keyed `Birago Nevers cipher 1572` (429, one retry after 5 s: 0) | nothing |
| DECODE | via Aymeloglu's catalogue mirror | no fr.3251 record |
| JSTOR | not queued this session (the folder's earlier family i/ii rows cover Birago-Nevers 1572) | pending; does not block N3 |

Requests: gallica.bnf.fr 32 (4 canvases, 2 SRU, 23 ContentSearch, 2 Pagination, 1 OAIRecord; 2 ContentSearch 500s on one
scan were not retried, since the other scan answered), be-api.us.archive.org 13 (several returned an empty body or 502; each was retried once and answered),
googleapis.com 6 (1 x 503, not retried), api.openalex.org 1, api.semanticscholar.org 2, github.com 2 clones. No credentials printed.

## Postmortem and corrections

1. **No over-claim found.** The NEVBIR-170/174V-A/174V-B sections were grepped for first/new/novel/unread/previously/
   unpublished/solved/cracked/never. The two "first" uses are ordinal ("a first run", "the real key is first at every seed").
   Nothing to correct.
2. **One transcription error found:** f.174r L04 "8 5" = 85 carmagnola, read as T46 + X_S (above). The solver lane should fix
   it. The class does not depend on it.
3. **The reading is weaker than its rank.** The judge FAILs (-1.161 vs real_p05 -0.905, well above null p99 -1.767), there are
   54 unkeyed signs, and the text has look-alike slips. Outward wording keeps "fragmentary" and the FAIL; the safe sentence does.
4. **Next for N4:** volume 2 of the 1665 Mémoires (not found on Gallica by the SRU queries used; try the BnF catalogue record
   for the set, or Google Books full view), the queued JSTOR rows, and one more Semantic Scholar query.

SECOND-OPINIONS-QUEUE.tsv: row `SO-NEVBIR-86` filed in this session (N3, CLAUDE.md "Operating model"), prompt
`second-opinions/PROMPT-chatgpt-no86.md`.

---

# Second audit (AUDIT2-NEVBIR, 2 Oct 2026): nos.71, 86, 90

Verifier: parent worker AUDIT2-NEVBIR (for the account-3 orchestrator), a session separate from every solver (NEVBIR-138,
-174V-A/B, -184, -185) and every first verifier (VERIFY-NEVBIR-139V, -86, -184). Brief
`.claude/briefs/runs/2026-10-02-acct3-audit2-nevbir.md`. Clock read with `date -u` at 20:12 and 20:22 UTC, 2 Oct 2026.
Claims under audit: the N3 sections above for no.71 (f.139v), no.86 (27 Aug 1572) and no.90 (f.184r), plus NEVBIR-185's
f.184v foot + f.185r lines 1-8 of no.90 (NOTES.md, never audited before this section). Task: find each letter's plaintext or
decipherment in print. Nothing was decoded here.

## Search log (this session)

| family | searched | result |
|---|---|---|
| (b) recipient's edition, **vol. 2** | Gomberville, *Les Mémoires de Monsieur le duc de Nevers* (Paris 1665), **Partie 2 located**: Gallica `bpt6k9738856z` (968 views; OAIRecord title "... Partie 2"), found by SRU `dc.title all "memoires duc de Nevers" and dc.title all "partie 2"` (the first audits' SRU queries returned only vol. 1's two scans). Gallica ContentSearch inside it: Birague 4, Birago 0, Lodovico 8, Ludovic 0, Saluces 11, Saluce 11, Saluzzo 0, 1572 1, Sadres 0, Voluera 0, Cocinato 0, Coconato (HTTP 500, not retried), Carmagnolle 3, Scipion 0, Scipione 0, Sanfre/Sanfrè 0, Coconas 0, commendatore 0, "Aoust 1572" 37, "Octobre 1572" 21, "Feurier 1572" 37 (loose matches, top 6 read each) | **no Birago letter of 1572.** The 4 Birague hits are Chancellor René de Birague (PAG_76, 104), Sacremore Birague (PAG_99), and a later request about "feu M. de Birague" (PAG_439). Seven of the 8 Lodovico hits are Lodovico Gonzaga, the duke's own name or signature; the eighth (PAG_429) shows no name in its snippet and is a letter to the king. The Saluces hits are the 1588-1601 marquisate question; the one 1572 hit is the St Bartholomew (PAG_66). OCR positive control: the same search finds "Birague" and "Lodovico" signatures, so a signed "Lodovico Birago" letter would be expected to show |
| (b) vol. 1, extra terms | `bpt6k6435941k` ContentSearch: Birago 0, Scipione 1 (Scipio Africanus), Coconas 4 (La Mole and Coconnas, 1574), commendatore 0, Sanfrè 0, "Octobre 1572" / "Feurier 1572" (top 6 read: 1574 restitutions of Savigliano, later letters) | adds nothing to VERIFY-NEVBIR-86's vol. 1 result |
| (b) court correspondence | *Lettres de Catherine de Médicis* vol. 4 (1570-74), IA `lettresdecatheri04cathuoft` full `_djvu.txt` grepped: Birague 6 | five are René de Birague; one names "Ludovic de Birague" in command of the marquisate of Saluces after 24 Aug 1572. None is a letter or summary of a Birago-Nevers letter |
| (c), (e) phrase search | `tools/print_check.py` on 12 decoded phrases (`phrases.txt`, nos.71/86/90) + `sources.tsv` (BnF catalogue IA item, two OpenAlex and one CrossRef keyword sets): 66 rows (`print-check.tsv`, `print-check-hosts.tsv`); IA be-api fts once more for 3 phrases that answered 502, plus `"Birago" "Nevers" Saluzzo 1572` (2168 loose items, top 6: Savio, BnF catalogue, Vester *Renaissance dynasticism*, Ricotti) | no hit carries any of these letters. Google Books hits are loose matches, unrelated (1589-1878 devotional, legal, dictionaries); "baron de sadres" hits only the Salazar y Castro index (a 1558 letter, as VERIFY-NEVBIR-86 found). IA fts for "il cocinato", "quanto gli fa che" and "il capitano scipione" answered 502 twice: **unreachable** |
| (g) scholarship, open indexes | OpenAlex (keyed): "Ludovico Birago" (79), "Lodovico Birago" (29), "Birago Carmagnola Saluzzo" (2), "Tomokiyo cipher Nevers" (9), plus print_check's 16 calls; Semantic Scholar (keyed): "Lodovico Birago", "Birago Nevers", "Tomokiyo Nevers cipher" answered; "Ludovico Birago Saluzzo" and 7 print_check phrase calls 429; CrossRef: "Lodovico Birago", "Ludovico Birago Nevers" + print_check's 3; HAL API: "Birago Nevers", "Lodovico Birago", "Ludovico Birago", "Birague Saluces 1572", "Tomokiyo Nevers chiffre" (0 each), "Birague" (2), "Birago" (11); Persée search: `Birago Nevers` (top 10 read), `"Birago" "Nevers"`, `"Lodovico Birago"` (0) | nothing on the 1572 Birago-Nevers letters. The nearest are Tomokiyo's Nevers 1592 digit-cipher paper (another letter, another key) and the 2026 *Cryptologia* DescryptTool paper (abstract names no Nevers or Birago item) |
| (g) Italian biography | *Dizionario Biografico degli Italiani*, "Lodovico Birago", treccani.it by curl and by `tools/browser_fetch.js` | **unreachable**: the page body renders no text to either route. The first audits saw the DBI only as a Google Books listing |
| (g) JSTOR | six rows appended to `JSTOR-QUEUE.tsv`, family (i) and (ii) for each letter: Birago/Birague + Nevers + month 1572 (or Coconato, Sadres) AND a cipher keyword; and the bare phrases "andarsi a consultare", "baron de Sadres", "il capitano Scipione" AND Saluzzo | queued; does not block N3 or N4 |
| (a), (d), (f), DECODE | not repeated: the first audits' Tomokiyo, BnF catalogue, Gallica slip checks, solver-repo clones and DECODE mirror are taken as logged | -- |

Phrases file note: two lines first written to `phrases.txt` were composed from word breaks, not copied from the decoded strings
("francesco gabaleone", "molti stoditi et dubitando"). They were removed with their rows after the run. Neither matched a
relevant print anyway.

Requests: gallica.bnf.fr 37 (4 SRU, 32 ContentSearch, 1 OAIRecord; one 500, not retried), archive.org 3 (2 advancedsearch, 1
djvu.txt), be-api.us.archive.org 18, googleapis.com 14, api.openalex.org 22, api.semanticscholar.org 11 (8 x 429), api.crossref.org
5, api.archives-ouvertes.fr 8, persee.fr 3, treccani.it 3. No credentials printed.

## Verdict

| item | class | key | text | why |
|---|---|---|---|---|
| no.71, f.139v foot, 161 signs (Birago to Nevers, Saluzzo, 7 Feb 1572) | **N4** (was N3) | published (Tomokiyo's 1572 table; T42=m fitted by us) | not known | both volumes of the 1665 Mémoires were now searched inside, with the names' OCR controls answering, and the open indexes, Catherine de Médicis vol. 4, IA and Google Books phrase searches found nothing. Internal or unpublished work is not excluded |
| no.86, 759 signs, ff.174r-175v (Saluzzo, 27 Aug 1572) | **N4** (was N3) | published | not known | same; vol. 2 was the gap VERIFY-NEVBIR-86 named |
| no.90, f.184r, 224 signs (Saluzzo, 2 Oct 1572) | **N4** (was N3) | published (T42 absent from no.90) | not known | same |
| no.90, f.184v foot + f.185r L01-08, 330 signs (NEVBIR-185) | **N4** (this is its *first* audit) | published | not known | no slip on canvases 187-191 (VERIFY-NEVBIR-184's look, which covered canvas 189). NEVBIR-185's own native look at canvas 189 found the faint marks over f.185r line 19 to be show-through. The searches above cover the whole letter. A second audit of this portion is still owed (Outreach gate 2) |
| no.90, f.185r L11-14 and L17-28, f.185v run | not classed | -- | -- | unread |

Not N5: the BnF and no specialist was asked. The readings are unchanged and are not judged here. All four stay cryptanalytic,
H 0 C 0, judge FAIL, fragmentary, as the first audits' safe sentences say.

**Safe sentences (N4).** Each carries "no prior decipherment located" and the reading's weakness:
- no.71: "Applying Tomokiyo's published 1572 Nevers-Birago key (one sign value fitted by us) to a value-blind transcription
  of the five cipher lines of Birago's letter no.71 (BnF fr.3251, f.139v), we get a partial reading (about 116 of 161 signs);
  no prior decipherment located after searching both volumes of the 1665 *Mémoires de Monsieur le duc de Nevers*, Tomokiyo's
  catalogue, the BnF catalogue, the solver repositories and the open scholarly indexes, 2 Oct 2026."
- no.86: "Using Tomokiyo's published reconstruction of the 1572 Nevers-Birago key, we read the cipher of Birago's letter of
  27 August 1572 (BnF fr.3251, no.86, 759 signs) from a blind transcription. The reading is fragmentary and fails our language
  judge. No prior decipherment located after the same search, 2 Oct 2026."
- no.90: "Under the same published key we read 554 of the cipher signs of Birago's letter of 2 October 1572 (BnF fr.3251,
  no.90, ff.184r-185r; the rest unread), fragmentary, judge FAIL. No prior decipherment located after the same search,
  2 Oct 2026."

**Unsafe.** "Deciphered" without "fragmentary"/"partial". Any use of first, new, previously unread or unpublished. Calling the key
ours: it is Tomokiyo's.

## Postmortem and corrections

1. **The vol. 2 gap was a search-query gap.** All three first audits stopped at N3 for want of Mémoires vol. 2. It was on
   Gallica the whole time under its own ark. The SRU queries used matched only the "Partie 1" record title. Next time, query
   SRU with the part number (`dc.title all "partie 2"`), or read the set's `dc.relation`.
2. **No over-claim found** in the three first-audit sections, the NEVBIR-185 NOTES section or the three SO prompts (grep
   first/new/novel/unread/previously/unpublished/solved/cracked/never: ordinal "first" and "unread" for this letter's own
   unread lines only).
3. **Second-opinion row.** `SO-NEVBIR-F184` (queued, unanswered) described f.184r only. Its prompt now also names the
   NEVBIR-185 portion's fragments, so the runner checks the whole read text (rule 10 propagation). The class is not a field
   in the queue, so nothing else changed there. No new row: the letter-level questions already cover the portion.
4. **Still owed:** a second audit of the NEVBIR-185 portion (this was its first). The JSTOR rows. Semantic Scholar's 429'd
   calls. The DBI entry, read by a person or a local runner if wanted. None of these blocks N4.

---

# AUDIT: no.90, the rest of its cipher -- f.184v foot + f.185r + f.185v, 742 signs (VERIFY-NEVBIR-90REST, 2 Oct 2026)

Verifier: parent worker VERIFY-NEVBIR-90REST (for the account-3 orchestrator), a session separate from the solvers
(NEVBIR-185, NEVBIR-185B) and from the earlier verifiers (VERIFY-NEVBIR-184, AUDIT2-NEVBIR). Brief
`.claude/briefs/runs/2026-10-02-acct3-verify-nevbir-90rest.md`. Clock read with `date -u` at 21:11, 21:14 and 21:17 UTC.
Nothing was decoded beyond the re-derivation. The transcription and the reading are the solvers'; nothing in them was changed.

**Claims under audit** (NOTES.md, NEVBIR-185 and NEVBIR-185B): Birago to Nevers, BnF fr.3251 no.90 (Saluzzo, 2 Oct 1572).
The f.184v foot + f.185r L01-08 (330 signs) and f.185r L10-12, L15-25 + the f.185v run (412 signs) are read under the
published 1572 key + T42=m. Each portion ranks 1 of 201 at three seeds; the whole letter (966) ranks 1 of 201 with z 4.49-4.59.
Grades for the whole letter are S 731 M 124 U 111, judge FAIL. AUDIT2-NEVBIR gave the 330-sign portion N4 (its first audit); the 412 signs were not audited before this pass.

## Verdict

| item | class | key | text | confidence |
|---|---|---|---|---|
| no.90 f.184v foot + f.185r L01-08, 330 signs (NEVBIR-185) | **N4** (second audit; AUDIT2-NEVBIR was the first) | published (Tomokiyo's 1572 table; T42 absent from no.90, so the fitted value plays no part) | not known | moderate; cryptanalytic (H 0 C 0), fragmentary, judge FAIL |
| no.90 f.185r L10-12 and L15-25, 392 signs (NEVBIR-185B) | **N4** (first audit) | published | not known | moderate; cryptanalytic, fragmentary, judge FAIL |
| no.90 f.185v run, 20 signs (NEVBIR-185B) | **N4 as a search result only; the reading is not licensed by its own control** | published | not known | low: its own control is a non-test (below); its one S token is graded down to M here |

Why N4 and not N3: AUDIT2-NEVBIR searched inside both volumes of the 1665 *Mémoires de Monsieur le duc de Nevers*, and the
OCR controls answered. That search covers the whole letter, so this pass did not repeat it. The phrase searches below add
the 185B fragments and find nothing. Not N5: neither the BnF nor a specialist has been asked. Internal or unpublished work is
not excluded.

## Re-derivation (rule 7)

`python3 tools/decode_key.py ciphers/nevers-birago-fr3251-1572 --check`: exit 0, "reading up to date";
`harvest/ciphertext_no90.tsv: tokens 966: M 124, S 731, U 111`, which matches the claim exactly (H 0 C 0 I 0). Per portion, counted
from `harvest/reading_no90_tokens.tsv`:

| portion | S | M | U | total |
|---|---|---|---|---|
| f.184r (audited earlier) | 190 | 13 | 21 | 224 |
| f.184v foot + f.185r L01-08 | 265 | 16 | 49 | 330 |
| f.185r L10-25 | 275 | 83 | 34 | 392 |
| f.185v | 1 | 12 | 7 | 20 |
| **audited here (742)** | **541** | **111** | **90** | 742 |

These match the solvers' S 265 M 16 U 49 and S 276 M 95 U 41. Working tree clean after the run.

## Controls at fresh seeds (rule 3)

`../ceppo-nevers-fr3251-1570s/harvest/decode_control.py SEQ --map sign_id_map_1572_fit.json`, it16dip, 200 value-shuffled
keys, 20 power windows. Sequences and logs: `harvest/no90/verify/`. `portion742.tsv` is `f185r/passC_rest90.tsv` + `f185r2/passC.tsv`.

| sequence | seed | real key | shuffles mean / max | z | rank | power control |
|---|---|---|---|---|---|---|
| portion, 742 signs / 752 letters | 7 | -0.9147 | -1.567 / -1.298 | 4.67 | **1/201** | err 0.12: 20/20 (z min 2.97); err 0.26: 8/20 |
| portion | 11 | -0.9147 | -1.568 / -1.179 | 4.45 | **1/201** | err 0.12: 20/20 (z min 2.48); err 0.26: 4/20 |
| f.185r L10-25 only, 392 | 7 | -0.9190 | -1.591 / -1.273 | 4.75 | **1/201** | err 0.12: 19/20 |
| f.185r L10-25 only | 11 | -0.9190 | -1.587 / -1.233 | 4.65 | **1/201** | err 0.12: 18/20 |
| **f.185v alone, 20 signs / 22 letters** | 7 | -1.1347 | -1.534 / -0.587 | 0.87 | **35/201** | err 0.29 (its measured): 0/20; err 0.12: 2/20 |
| f.185v alone | 11 | -1.1347 | -1.540 / -0.524 | 0.81 | **38/201** | err 0.29: 0/20 |
| whole no.90, 966 / 977 | 7 | -0.9398 | -1.572 / -1.299 | 4.65 | **1/201** | err 0.12: 20/20 (z min 3.09) |
| whole no.90 | 11 | -0.9398 | -1.575 / -1.222 | 4.50 | **1/201** | err 0.12: 20/20 (z min 3.25) |

The measured disagreement of the two blind passes is 0.04 for the 330 portion, 0.12 for f.185r L10-25 and 0.29 for f.185v,
about 0.09 pooled over the 742. Power at 0.12 brackets the measured error of the f.185r runs (20/20 for the 742). At 0.26,
about twice the 185B rate, power falls to 4-8/20. The licence therefore holds only if the true reader error is near the
measured rate, which is the same caveat the solvers stated.

**f.185v fails as a test on its own.** At 20 signs the run ranks 35-38 of 201, and its power control reads the real key in 0-2
of 20 windows even at 0.12. That makes it a non-test (CLAUDE.md rule 3), not a negative. Its reading rests only on the key
that the f.184r-185r runs license. Graded down here: the one S token on f.185v counts as **M** for audit purposes, so f.185v
carries no S. The audited 742 are therefore **S 540 M 112 U 90**, and the whole letter S 730 M 125 U 111. The solvers'
committed grades are unchanged; this regrade is a verifier note. The "[carmagnola]" code word on f.185v sits beside "degli
Ugonotti" in the clear lines above. That fits the letter's subject, but it is a consistency note, not a crib.

**One correction to the solvers' logged figure.** NEVBIR-185B's whole-letter control (`harvest/no90/log/control_all2_s*.txt`,
real -0.9449) was run while the 185B passages still carried ids L01-L14. Those ids collided with NEVBIR-185's L01-L08, so
each pair of lines was scored as one passage (visible in the log's reading block). The committed `no90/passC_all.tsv` carries
the corrected ids L10-L25, and it scores **-0.9398** (re-run here at seed 1 too: z 4.47, rank 1/201). The difference is 0.005
and the rank is unchanged, so no conclusion moves. NOTES.md's whole-letter row should be read with -0.940.

## Slip and decipherment check (brief item 1)

Gallica btv1b9060248g canvases 188-191 were fetched once each at native size (about 8262 x 5849), 4 requests. Each page was
viewed in half-page tiles at 1500 px, with native-resolution detail crops where needed.

| canvas | pages | seen |
|---|---|---|
| 188 | f.183v / f.184r | f.183v blank except the vertical address docket of the previous item; f.184r the letter's opening with its four runs; no interlinear gloss, no slip |
| 189 | f.184v / f.185r | f.184v prose, then four cipher lines at the foot after "mádaro el tutto a V.E."; f.185r cipher block with clear inserts ("Mons. di Sanfré debbe partirsi qsta settimana ... dal rè", "non si sa che porti il tempo ...", "cose sue da di quà, che", "qste parti", "Chi io nó só ..."); no slip |
| 190 | f.185v / f.186r | f.185v prose; the cipher run sits between "con tutto ciò" and "che non gli provede da di là"; signature and "Da Saluzzo li 2 di Ottobre 1572"; f.186r the next item |
| 191 | f.186v / f.187r | f.186v blank with heavy show-through; f.187r faint mirrored offset; no decipherment |

**The faint writing over f.185r L15** ("cose sue da di quà, che ..."), native crop 5600,2700,2300x230. Its strokes slope
backwards in the original and slope forward like the scribe's italic in a mirrored copy. That is show-through or offset from
the facing or reverse side, not an interlinear decipherment, which confirms NEVBIR-185's call. Several darker signs on that
line (ω, π) are heavier ink, not over-writing.

**The f.185v run is complete in the solvers' crop.** At native size (1300,1150,3200x350) the run reads 20 signs from the
square-with-dot after "ciò" to a hash at the gutter, in the same order and shapes as `f185r2/passC.tsv` (pos 3 is the "85"
cell, pos 9 the ligature, pos 13 the raised-a m). The last sign touches the binding, so a further sign hidden in the gutter
cannot be excluded from this image.

Nothing is laid in or pasted between f.183v and f.187r. This agrees with VERIFY-NEVBIR-184's 2500 px look.

## Search log (2 Oct 2026, this session)

| family | searched | result |
|---|---|---|
| (a) canonical / catalogue | not repeated (Tomokiyo nevers.htm and the BnF catalogue as logged by VERIFY-NEVBIR-184 and AUDIT2-NEVBIR) | -- |
| (b) recipient's edition | not repeated: AUDIT2-NEVBIR searched inside both volumes of the 1665 *Mémoires de Nevers* for the whole letter | no Birago letter of 1572 |
| (c), (e) phrase search on the new portion, Google Books (keyed, `country=US`) | `"intendere a la regina" Birago` (70: Suriano/Barbaro despatches, Huguenot Society 1891, Maria Cristina 1895: Birago family in other contexts), `"casa di Momoransi"` (192: Davila's *Historia delle guerre civili*, other contexts), `"casa di Memoransi" 1572` (18: *La politique de St Pie V*, Freschot, Salviati nunciature: other letters), `"governo di Turino" Birago` (1: a 1605 Philip II life, a list of governors), `"Rocha Sparavera"` and `"Rocca Sparavera" Birago` (clear text of f.185v: 15 + 2, all 1490s-1500s Trivulzio / *Monumenta Aquensia*), `"huomini di Demonte" Tenda` (f.185v clear: 50, Botero and Cuneo histories), `"Sanfre" Birago 1572 Nevers` (0), `Birago Carmagnola "Ottobre 1572" Nevers` (4, the BnF catalogue), `Birago "2 ottobre 1572"` (178, top 5: the BnF catalogue, Relazioni degli ambasciatori veneti), `"Lodovico Birago" lettere "duca di Nevers"` (4: BnF catalogue; *Storia della riforma in Piemonte* 1982 snippet on Nevers's letters *to* Birago about provisioning; *La biblioteca di don Ferrante*), `"non si sa che porti il tempo"` (346 loose, top 5 unrelated), `"confusioni" "religione" Birago Saluzzo 1572` (0), `"Storia della riforma in Piemonte" Birago 1572 ottobre Nevers` (0) | no print of the letter's clear or cipher text |
| (e) IA full text (be-api fts) | `"intendere a la regina" Birago` (1: a chronicle on Madama d'Entremont and Queen Maria), `"casa di Momoransi" Birago` (10: Davila editions), `Birago Nevers Carmagnola 1572 Turino` (10: Birago's biography and death on 28 Dec 1572, nunciature lists, Nevers to Montmorency), `"Sanfre" Birago` (10: genealogies, the Chivasso siege) | nothing on this letter |
| (f) solver repos | dbourdeau/cyphersolver cloned at head **2 Oct 2026 15:12** (newer than the earlier audits' 1 Oct), grepped birago/3251/1572/f.184-185/Momoransi/Carmagnola: `targets/birago` is f.119 (13 Nov 1571, figure cipher); its sibling sweep notes that the 1572 letters use Tomokiyo's symbol cipher and reads none of them; TARGETS.md and unsolved.htm name only f.119. aaymeloglu/unsolved-ciphers (head 27 Sept 2026): DECODE catalogue rows for Birago are fr.3621/3623 (1591-92, the other Birago), no fr.3251 | no reading of no.90 |
| (g) scholarship | OpenAlex keyed `Birago Nevers 1572` (10, none relevant: Catherine de Médicis historiography 2022 and noise); Semantic Scholar keyed `Birago Nevers cipher 1572` (0) | nothing |
| DECODE | via Aymeloglu's catalogue mirror (above) | no fr.3251 record |
| JSTOR | not queued again: AUDIT2-NEVBIR's six rows already cover no.90 at letter level (families i and ii) | pending; does not block N4 |

Requests: gallica.bnf.fr 4 (native canvases 188-191, 2 s apart, no challenge), googleapis.com 15, be-api.us.archive.org 4,
api.openalex.org 1, api.semanticscholar.org 1, github.com 2 clones. No credentials printed.

## Postmortem and corrections

1. **No over-claim found.** The NEVBIR-185 and NEVBIR-185B sections were grepped for first/new/novel/unread/previously/
   unpublished/solved/cracked/never. "unread" refers only to this letter's own not-yet-read lines (now none), and "new" appears
   only in the sign label X_NEW. Nothing to correct.
2. **f.185v is graded down** (above): its own control is a non-test. Outward wording must not cite the f.185v fragment
   ("Carmagnola") as a control-backed reading.
3. **The whole-letter control figure is corrected to -0.940** (passage-id collision in the solver's log). The rank and the
   class do not move.
4. **The 19 T83-shaped tiles** (NEVBIR-185, kept unkeyed, grade M if fitted) are still owed a value-blind check by the owner's
   sign sorter or a separate value-blind reader. This verifier did not do it (outside the brief). It does not affect the class.
5. **Still owed:** a second audit of the 392 f.185r L10-25 signs (Outreach gate 2); the JSTOR rows; the DBI entry.

**Safe sentence (N4), whole letter:** "Under Tomokiyo's published 1572 Nevers-Birago key we read, fragmentarily, the cipher of
Birago's letter of 2 October 1572 (BnF fr.3251, no.90, ff.184r-185v, 966 signs) from a value-blind transcription. The key
beats 200 shuffled keys on every portion except the 20-sign run on f.185v, which is too short to test on its own. The reading
fails our language judge. No prior decipherment located after searching both volumes of the 1665 *Mémoires de Monsieur le duc de
Nevers*, Tomokiyo's catalogue, the BnF catalogue, the solver repositories and the open indexes, 2 Oct 2026."
**Unsafe:** "deciphered" without "fragmentary"; any first/new/previously unread/unpublished wording; calling the key ours;
citing the f.185v fragment as tested.

SECOND-OPINIONS-QUEUE.tsv: no duplicate row. `SO-NEVBIR-F184` (queued, unanswered) is the letter-level row; its prompt
`second-opinions/PROMPT-chatgpt-f184.md` now names the 185B fragments and says the f.185v run is untested on its own (rule 10
propagation). This follows AUDIT2-NEVBIR's precedent for the 330-sign portion.

---

# Second audit (AUDIT2-NEVBIR-90R, 2 Oct 2026): no.90 f.185r L10-25, 392 signs

Verifier: worker AUDIT2-NEVBIR-90R (for the account-3 orchestrator), a session separate from the solvers (NEVBIR-184,
NEVBIR-185, NEVBIR-185B) and from every earlier verifier on no.90 (VERIFY-NEVBIR-184, AUDIT2-NEVBIR, VERIFY-NEVBIR-90REST).
Brief `.claude/briefs/runs/2026-10-02-acct3-audit2-nevbir-90r.md`. Clock read with `date -u` at 21:50 UTC. Nothing was decoded;
the transcription, reading and grades are the solvers' as audited by VERIFY-NEVBIR-90REST (S 275 M 83 U 34 for this portion).

**Claim under audit:** VERIFY-NEVBIR-90REST's N4 for f.185r L10-12 and L15-25 (392 signs, NEVBIR-185B), read under Tomokiyo's
published 1572 key; its first audit. Task: try to find this portion's plaintext or a decipherment of it in print.

## Search log (2 Oct 2026, this session)

Phrases taken from `harvest/gloss_no90.md` (f185r L10-L25 entries), spelling as decoded, word division ours. Files:
`harvest/no90/audit2/` (phrases, sources, print-check.tsv, Gallica ContentSearch XML).

| family | searched | result |
|---|---|---|
| (c), (e) `tools/print_check.py` | 8 phrases: "credo pensi al governo", "intendere a la regina", "depende da la casa", "casa di memoransi", "casa di momoransi", "confusioni e difficulta", "il tutto e pregiuditio", "con ogni suo potere", each through IA full text (all items), Google Books (keyed, `country=US`), OpenAlex (keyed), Semantic Scholar (keyed); plus OpenAlex `Birago Nevers Montmorency 1572` and CrossRef `Lodovico Birago Nevers Saluzzo 1572` (36 rows) | no row carries this letter. "intendere a la regina": *Codice Aragonese* (1868) and *Giornale ligustico*, 15th-century texts. "casa di Momoransi/Memoransi": Davila's *Guerre civili*, Tommaseo's *Relations des ambassadeurs vénitiens*, Mattei 1637, *Acta nuntiaturae Gallicae* (1970), Druffel's *Briefe und Acten* (1874), all narrative or other letters. "credo pensi al governo", "confusioni e difficulta", "con ogni suo potere": loose matches only (parliamentary records, modern legal and scientific papers). "depende da la casa", "il tutto e pregiuditio": no relevant hit. OpenAlex keyword: one 2013 paper on Montmorency's funeral orations. CrossRef: other Biragos (Diop, Giampietrino) |
| (e) Google Books, ANDed (keyed, `country=US`) | `"casa di Momoransi" Birago` (15), `"intendere alla Regina" Birago Saluzzo` (11), `"governo di Turino" 1572` (39), `Birago Saluzzo 1572 Montmorency Carmagnola ugonotti` (0), `"Lodovico Birago" Montmorency 1572` (4) | top 6 read each: *Historiae Patriae Monumenta* (1840, a chronicle mentioning a Birago in another context), Tommaseo's *Relations* (1838), Sclopis *Stati generali* (1851, a duke of Savoy letter of 30 Sept 1572 from Turin, not Birago's), the Salviati nunciature (*Correspondance du nonce en France, Antonio Maria Salviati*, 1975, the nuncio's own despatches), the 1874 BnF catalogue. None prints Birago's 2 Oct 1572 letter |
| (e) IA full text, ANDed (be-api fts) | `"casa di Momoransi" Saluzzo` (10: Davila editions, Albèri *Relazioni*), `Birago "governo di Turino"` (0), `"intendere alla regina" Birago` (10) | the one hit carrying both words, *Bollettino storico-bibliografico subalpino* (1898 issue 3), prints letters naming **Andrea** Birago ("facendo intendere alla Regina e a quelli del Consiglio" about a brevetto), another writer and another letter; not this one |
| (b) recipient's edition, both parts | Gomberville, *Les Mémoires de Monsieur le duc de Nevers* (1665): Gallica ContentSearch in Partie 1 `bpt6k6435941k` and Partie 2 `bpt6k9738856z` for Carmagnolle, Carmagnole, Momorancy, Turin, Birague (10 queries; the names AUDIT2-NEVBIR had not used are Momorancy, Turin, Carmagnole) | **no Birago letter of 1572 in either part.** Partie 1: Birague hits are Carles/Charles de Birague in the 1574 restitution papers (PAG_109-150), the chancellor (PAG_340, 503); Carmagnolle hits are the 1574 restitution and the 1588 seizure (PAG_877-926); Momorancy 1 (PAG_153, the house of Montmorency siding with Alençon after St Bartholomew, narrative); Turin hits are treaties and later despatches. Partie 2: Birague = chancellor and Sacremore (as AUDIT2-NEVBIR found); Carmagnole = 1588 and after; Momorancy 0; Turin = 1574-1609 treaties. OCR positive control: the search finds "Birague" signatures and "Carmagnolles" dozens of times, so a printed letter on these subjects would be expected to show |
| (a), (d), (f), (g) JSTOR, DECODE, slip check | not repeated: VERIFY-NEVBIR-90REST (2 Oct 2026, cyphersolver at head 15:12, aaymeloglu, Tomokiyo, BnF catalogue, Gallica canvases 188-191 at native) and AUDIT2-NEVBIR (HAL, Persée, CrossRef, Catherine de Médicis vol. 4) are taken as logged | -- |
| (g) JSTOR | family (i) for no.90 already queued (`("Birago" OR "Birague") AND "Nevers" AND ("ottobre 1572" OR "octobre 1572") AND cipher`); family (ii) for no.90 so far only "il capitano Scipione" AND Saluzzo (f.184r). **One family (ii) row appended for this portion:** `"casa di Momoransi" AND Birago` | queued; does not block N4 |

Requests: be-api.us.archive.org 13, googleapis.com 13, api.openalex.org 9, api.semanticscholar.org 9, api.crossref.org 2,
gallica.bnf.fr 10 (ContentSearch, 2 s apart, all 200, no challenge). No credentials printed.

## Verdict

| item | class | key | text | confidence |
|---|---|---|---|---|
| no.90 f.185r L10-12 and L15-25, 392 signs (NEVBIR-185B) | **N4** (second audit; VERIFY-NEVBIR-90REST was the first) | published (Tomokiyo's 1572 table; T42 absent from no.90) | not known | moderate on the class; the reading is cryptanalytic (H 0 C 0), fragmentary, judge FAIL |

The first audit's N4 holds. Not N5: neither the BnF nor a specialist has been asked. Internal or unpublished work is not
excluded. The f.185v run (20 signs) stays as VERIFY-NEVBIR-90REST left it, N4 as a search result only (its own control is a
non-test); this pass's Mémoires and letter-level searches cover it too, but add nothing to its reading. With this pass every
portion of no.90 has had two audits.

**Safe sentence (N4), whole letter:** unchanged from VERIFY-NEVBIR-90REST above.
**Unsafe:** as above; also any wording that treats the gloss's identifications ("the Queen" = the Queen Mother, the
Montmorency reference, "the execution") as read: `gloss_no90.md` marks them inferred.

## Postmortem

No over-claim found in the NEVBIR-185B NOTES section, `gloss_no90.md` or the VERIFY-NEVBIR-90REST section (grepped
first/new/novel/unread/previously/unpublished/solved/cracked/never). The one near-miss in print is a different Birago
(Andrea) in an 1898 *Bollettino storico-bibliografico subalpino* letter series; worth a look by the next reader of the
Piedmontese Birago correspondence, not a prior print of this letter. Still owed (not blocking): the JSTOR rows, the DBI
entry, the 19 T83-shaped tiles' value-blind check.

# Reader-label ruling on no.87 T50 and T46 tiles (VERIFY-BIRAGO-SMALL, 3 Oct 2026)

Verifier: worker VERIFY-BIRAGO-SMALL (account 2 for the account-3 orchestrator, Opus 5.5), a session separate from the
solver BIRAGO-SMALL (2a750ceb). Brief `.claude/briefs/runs/2026-10-02-acct3-verify-birago-small.md`, item 2. Disk only:
0 requests, 0 subagents. **Nothing applied**: `harvest/ciphertext_f178*.tsv`, `f179r.tsv`, the keys and the firm counts are
unchanged. This section is the ruling the next decode applies. No class change.

**Method.** The solver's own read was not value-blind. This verifier rebuilt the 12 T50/T46 tiles as a shuffled montage
with panel letters only (no line, position, label or sheet value): `harvest/lookalike_87/verify_blind/mk.py` (seed 4417,
ImageMagick; regenerates byte-identical `key.tsv`). Each panel was read by shape before `key.tsv` was opened; the read is in
`verify_blind/blind_read.tsv`. Limit: this verifier had read the solver's NOTES section first, so it knew the class counts
to expect (7 + 1, and 2 + 1 + 1); it did not know which panel was which tile.

**Result: 12 of 12 shapes agree with the solver.**

| tile(s) | sheet | shape read blind | ruling for the next decode |
|---|---|---|---|
| f178v L01.23, L03.4, L04.4, L05.25, L07.29, L08.10, L10.5 (T50) | s x7 | curled "Ce": omega with a c-hook lead, no tall tail (L07.29 at the gutter edge, readable) | **upheld**: relabel X_CE, an off-sheet sign. Value s is grade C from the clerk sheet (7/7 on no.87), not from the printed table. |
| f178v L20.7 (T50) | c | omega with the tall S-tail, the T50 sheet cell | **upheld**: stays T50 = c (printed value). The variant key's T50 = s row (`harvest/key_1572_clerkvar.tsv`) is not a sign-level rule and should not be used. |
| f178r L03.22 (T46) | turino | "86" | **upheld**: stays T46 (printed "86" = turino). |
| f178v L19.22 (T46) | re | a single 8 | **upheld**: relabel X_8, value unset (U). |
| f178v L15.24-25 (T46, T46) | c / atholici | "88", two 8s written as one group | **upheld on shape, label amended**: one token X_88, not two X_8 tokens. The printed table writes its name codes as two-digit groups (85 carmagnola, 86 turino, 89 bugonotti); the sheet's "c" + "atholici" over the pair reads as one word, so "88" is most likely a further two-digit name code for "cattolici". Value: unset in the key until a second occurrence or a print supports it; the sheet's word is C for this one occurrence only. |

Error on these 12 tiles against the clerk sheet, if the ruling is applied: before 10 wrong (7 T50 + 3 T46), after 0 wrong
(7 X_CE at s, 1 X_88 at "cattolici" if the one-occurrence C value is used, else 1 U; 1 X_8 U). The solver's T52 and T98
findings were outside this brief and are not ruled on here (T52 is the key conflict already logged; T98/T18 is with the
owner's sorter).

**For the next decode.** Apply by `exceptions` rows or a relabel in passC/passD with basis "VERIFY-BIRAGO-SMALL 3 Oct 2026",
then `tools/decode_key.py --check`, the decode_control at fresh seeds and the judge, before any firm count moves. Open next
step (the solver's, unchanged, ~$2): look for the "Ce" shape under T50 or T92 labels in nos.71/86/90, where T50 = c is
needed by "per conto", "domestico", "confusion".


## JSTOR (owner's machine, 3 Oct 2026)

All 13 queued JSTOR-QUEUE.tsv rows for Birago (137-138, 141-150, 155; both families: name/date/place + cipher keyword, and
bare quoted phrases from the readings) run by the owner's desktop session in a browser signed in to JSTOR, about 05:2x UTC,
no captcha or block page. The six quoted-phrase rows (142, 144, 146, 148, 150, 155) returned 0 results each. Name/date rows
returned only indexes, bibliographies and a different Birague (René, in Bernus 1888 on Antoine de Chandieu). The one full-text
candidate, "DOCUMENTI", Archivio Storico Italiano 122 (1964), https://www.jstor.org/stable/26252393, was read in the online
viewer: Medici envoys' letters from the Council of Trent, Oct 1561-1563, so it cannot print the 1572 letters. Result: nothing on
JSTOR prints or discusses Birago's 1572 cipher letters or their decipherment. Class unchanged (N4 stands; outreach gate 2's JSTOR
condition is now met for this target).

Desenclos check, 4 Oct 2026 (DESENCLOS-PREMISE, account 3): no hit. Searched 17 open full texts of the 36 items in sources/desenclos/2026-10-04/bibliography.tsv (HAL PDFs, DSpace Tartu HistoCrypt 2024/2025 PDFs, OpenEdition HTML; built from HAL, theses.fr, OpenAlex, Semantic Scholar, CrossRef, Google Books) for this item's shelfmark, sender/recipient, place and date (terms.tsv, search-log.tsv, search.py); none names this item, its key or its plaintext. Not read: her 2014 thesis (theses.fr: not online) and 2017/2021 cryptography chapters (not open; JSTOR-QUEUE rows of 4 Oct 2026).
