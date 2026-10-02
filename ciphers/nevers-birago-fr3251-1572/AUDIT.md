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
