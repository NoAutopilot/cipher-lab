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
| ff.138, 144, 152, 160, 168, 174, 184 (nos. 71-90) | not read | not classed | -- | -- | nothing read |

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
