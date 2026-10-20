# AUDIT: fr4735-monluc-lansac-poland-1573, Monluc Cipher 1 letter on f.138r-v (VERIFY-MONLUC, 20 Oct 2026)

Verifier: VERIFY-MONLUC (account 4, session_01CzeKNTJv7UYD3DLXkfwRqi), a session separate from every solver session on this
folder (SUP-MONLUC, MONL-C268C, MONL-C269A/B/C and earlier). Brief `.claude/briefs/runs/2026-10-20-acct4-research-director-38.md`,
JOB VERIFY-MONLUC. Clock read with `date -u`: 12:48 UTC (start) to about 13:1x UTC, 20 Oct 2026. Repository state audited:
origin/main 63a591b33.

**Claim under audit.** Monluc's Cipher 1 letter on BnF fr.4735 c268 (f.138r, L01-L30) and c269 (f.138v, L01-L33) is read by
aligning a period clear copy in the same volume (ff.140r-141r) to the decoded cipher, grade C where the alignment places it;
target tokens C 984 / M 1041 / U 108 of 2133 (decode_key.py). The 2133 include f.86 (c172, 150 tokens, C 83, graded against its own
margin gloss), which this audit re-derives but does not re-examine.

## Verdict

| item | scope | class | key | text | depth | confidence |
|---|---|---|---|---|---|---|
| f.138r-v (c268 + c269, 1983 tokens), Monluc to Catherine de Médicis, election of Anjou, April 1573 | key application checked against a period clear copy | **N0** | published (Tomokiyo, Monluc Cipher 1) | known (period clear copy on ff.140r-141r, in the same volume); not found in print | **D2**, about 35% of the leaf's tokens C (verifier count) | high on the placement; moderate per token |

Key source: `published`. Every letter value comes from Satoshi Tomokiyo's Monluc Cipher 1 table (Cryptiana, "Ciphers of Monluc and
Lansac, Sent to Poland (1573)", henryiii page; our copy `key.tsv`, unchanged by any job audited here). Tomokiyo names these very
leaves (f.132, f.136, f.138) as Cipher 1 letters and quotes jargon from f.132 and a null from f.87, so his table was built from this
material. Every *meaning* graded C comes from the period clear copy ff.140r-141r. Nothing in the reading is `ours` beyond the
transcription, the alignment and the placement tests. Pipeline item 7 label: **key application** (a published key applied to a
letter, checked against the letter's own period clear text), not recovery and not cryptanalysis.

**N0 reason.** The BnF finding aid for fr.4734-4736 (notice `ark:/12148/cc57784f/cd0e2277`, read by NC-MONL2 on 7 Oct 2026)
describes items 53-55 (ff.132-141, 28 Apr 1573, Monluc to the king and the queen mother) as "avec chiffre et déchiffrement". The
clear letter on ff.140r-141r ("Madame, nous sommes venuz du point ou se retrouuent les plaideurs ...") is the period plaintext of
the f.138 cipher, which the solvers' placement tests establish beyond the controls (below). So both the plaintext and the
decipherment of this very item already exist in the holding manuscript and are catalogued as such: rule 10 N0, the same basis as
ceppo-nevers-fr3251-1570s ("period decipherment present in the MS (the N0 basis)"). The plaintext was **not** located in print
(search log below), so the text is known in manuscript only, as far as searched. The class would not rise above N0 even if no print
is ever found: the decipherment of this item is the period's, and the key is Tomokiyo's.

Date and addressee: the leaves carry no date that any job read; "Madame" is the queen mother. The 28 Apr 1573 date is inferred from
the aid's item range and the leaves' position (MONL-140). Consistency check, not proof: the clear copy says "A quoy Je pense auoir
satisfaict par ma seconde oraison" (f.140r L11), and Monluc's two election speeches at Kamień near Warsaw are dated 10 and 25 April
1573 in the scholarship the web search returned, which fits a letter written after 25 April.

## 1. Rule 7: re-derivation

In a fresh tree (`git archive origin/main tools ciphers/fr4735-monluc-lansac-poland-1573 specs/fr4735-monluc-lansac-poland-1573.json`,
63a591b33, scratchpad, no repository files read beyond those), I ran:

| command | result |
|---|---|
| `python3 tools/decode_key.py ciphers/fr4735-monluc-lansac-poland-1573 --check` | c172 150: C 83 M 64 U 3; c268 1026: C 511 M 468 U 47; c269 957: C 390 M 509 U 58; "reading up to date", exit 0 |
| `python3 align_c268.py --check` (200 shuffled-clear draws, seed 140) | "align_c268: OK", exit 0 (about 6 minutes) |
| `python3 c269/align_c269.py --check` | "align_c269: OK", exit 0 |

The totals match the claim exactly (C 984 / M 1041 / U 108 of 2133). key.tsv is the committed table; no token differs.

## 2. Gate audit

**Order (git log, first commit of each file, UTC 20 Oct 2026).** Each PREREG precedes the reads it governs:

| band | PREREG first commit | passes + reconciliation first commit | scores | later edits to the PREREG |
|---|---|---|---|---|
| c269 L01-L10 | d8b8c1d1f 08:16 | a3c4d41d0 08:26 | ec9ea5714 08:32 | Decision block appended only (diff read) |
| c269 L11-L22 | a690865da 10:15 | aabe9e5e2 10:24 | aabe9e5e2 / 65e5b8014 | Decision block appended only |
| c269 L23-L33 | 26a27ee85 11:18 (with span_rule.py) | db6c92aad 11:25 | 65e5b8014 11:29 | Decision block appended only |

**Re-run from the committed passes** (same scripts, default seeds):

| statistic | registered | re-run |
|---|---|---|
| `score_c269.py c269c_reconciled.tsv --window f.140v:L09-f.141r:L11` (L23-L33) | 0.482 vs placed-shuffled p95 0.385, max 0.414, 0/200; f.139 0.363 | identical: 0.482, mean 0.3603, p95 0.3849, max 0.4137, 0/200, f.139 0.3633 |
| `span_rule.py` band 3 (L23-L33) | prev_end f.140v L10, indep_start f.140v L10, delta 0 | identical |
| `span_rule.py` band 2 (L11-L22) | prev_end f.140v L03, indep_start f.140v L02, delta -1 | identical |
| c268 L01-L30 (`results_align_c268.json`, reproduced by `--check`) | confirm 658/971 = 0.678 vs shuffled-clear mean 0.370, max 0.396, 0/200; f.139 0.311 | as committed |

**One weakness in the order, disclosed, not disqualifying.** The span rule (PREREG v3) that graded c269 L11-L22 was written at 11:18,
after L11-L22 had been read and scored at 10:24 under PREREG B, whose span clause it failed (by one line). The rule was then tested
prospectively only on L23-L33, where it held (delta 0). So L11-L22's grades rest on a rule fitted after its data, backed by a
placement score far above its control (0.647-0.650 vs p95 0.425) and by the prospective pass of the same rule on the next band.
I accept the placement of L11-L22; I would not cite L11-L22's span result as a test.

**Placement is not in doubt.** Confirms in runs of three or more consecutive clear letters (below) are 52.7% of keyed tokens on c268
and 39.8% on c269, against 7.2-7.3% mean (max 9.1-10.7%) when the same tokens are aligned to a word-shuffled clear letter (20 draws)
and 2.9-3.2% against the other clear letter f.139. Leaf f.138r-v is the cipher of f.140r L07 - f.140v L17.

## 3. Is the C grade earned per token?

**Contradicting decodes.** decode.json grades a token C only when the table letter equals the clear letter the token faces
(`voted_grade C`, `disagree_grade M`). Joined against align_c268.tsv and c269/align_c269.tsv: **0 of the 901 C tokens on f.138r-v face a
clear letter that contradicts the decode** (c268 509 confirm + 2 name-pair fills; c269 390 confirm). The 370 contradictions (193 +
177) are all already M. Share of C with a contradicting decode: **0%**.

**What the solvers did not check: chance confirms.** The alignment is a free dynamic program that rewards a match (+2) and lets a
token slide over clear letters. Against a word-shuffled clear text it still finds a confirm for 37-38% of keyed tokens, and against
the wrong letter (f.139) 31-33%. Those chance confirms are mostly isolated: in confirm runs of one or two letters (shuffled: 0.30
of keyed tokens sit in runs of 1-2, only 0.07 in runs of 3+). So a C token that sits in a run of 1-2 is not distinguishable, as a
single token, from a slide match. Scripts: `audit/verify_runs.py` (run distribution, real vs 20 shuffled-clear draws vs f.139; output `audit/verify_runs.out`) and `audit/verify_cruns.py` (committed C tokens by run length); run as `python3 -I audit/verify_cruns.py $PWD` from the folder (logic: a run is a maximal
sequence of keyed confirms on consecutive clear positions, fill tokens with no clear letters skipped).

| job | C as committed | C in confirm runs >= 3 | C in runs 1-2 | name-pair fill (C) |
|---|---|---|---|---|
| c268 | 511 | 403 | 106 | 2 (lempereur) |
| c269 | 390 | 292 | 98 | 0 |
| total | 901 | 695 | 204 | 2 |

**Verifier count (rule 4: my grade, not a key edit).** The 204 C tokens in runs of 1-2 are regraded M; run 3+ confirms and the
lempereur name-pair fill stay C. Leaf f.138r-v: **C 697 / M 1181 / U 105 of 1983 (35.1% C)**. Whole target with f.86 as committed:
**C 780 / M 1245 / U 108 of 2133 (36.6% C)**, against the claimed 984 (46.1%). Run 3+ is itself a lenient bar (a shuffled clear
still yields 7% of keyed tokens in such runs in a free placement), but inside a band already placed by the gates that rate does not
transfer directly, so I do not discount further. Grades H: 0, S: 0 (no key-source and no cryptanalytic grade anywhere in this
reading).

## 4. Depth (rule 4a)

**D2 ("partially deciphered, about 35%").** Clause test: c268 L03 decodes, letter for letter in one confirm run,
"lon fait parler le roi de da[nnemarc]" (22+ letters) and L04 "...et done a [a]ttendre quil est", far above any authentication
distance for a substitution table; the decode reads the same words in the same order as the clear copy. Not D3: C is about 35-37%,
far below 80%, and the gaps are not mostly names/codes (they are read errors, two-form splits and slides). Depth sentence (true and
specific, written by the verifier from the clear copy the cipher was shown to carry): **"Monluc tells the queen mother that the
emperor's agents canvass the Polish electors openly, sparing neither honour nor the king's reputation, and spread word that the King
of Denmark is a candidate, which he never intended."**

`tools/depth_check.py` validates status.json only, which this job may not edit; the fields for the parent: `depth` D2,
`depth_pct` 35 (leaf) / 37 (target), `depth_check` "known-plaintext alignment, placed-shuffled and other-letter controls",
`decode_status` "Partially decrypted", `depth_sentence` as above. Not a unique solve: N0 is below N3, so it is not counted (rule 4a
and the precedent in ceppo-nevers).

## 5. Search log (rule 10)

| family | searched | result |
|---|---|---|
| (a) canonical series | Noailles, *Henri de Valois et la Pologne en 1572* (1867), vols I-III, IA `_djvu.txt` (henridevaloisetl01noai, 02noai, 03noaiuoft), fetched 20 Oct 2026; grep of the clear copy's words: plaideurs, toille/toile, Dannemarc/Dannemark, seconde oraison, Sendomir, Balagny, quatre vingt(z) mil, Moscovite/Moscouite commande, juges ont/opiner/quinze ou vingt, "avril 1573"/"28 avril" | no passage of the clear letter; hits are unrelated (Danemark in other letters, Balagny in the editor's narrative); no Monluc letter of 28 Apr 1573 printed |
| (b) sender/recipient correspondence | Noailles above (Monluc's letters are printed there); *Lettres de Catherine de Médicis* not searched (her own letters, not letters to her) | negative / not searched |
| (c) documentary editions | NC-MONL (7 Oct) whole-volume Noailles keyword grep; MONL-PC (14 Oct) phrase search | negative |
| (d) holding archive | BnF finding aid fr.4734-4736 (NC-MONL2, 7 Oct): items 53-55 "avec chiffre et déchiffrement" | **the N0 basis**: a period decipherment of this item is catalogued; Gallica 403 today, not re-read |
| (e) full text | IA be-api full text and OpenAlex, 14 phrases, no hits (MONL-PC 14 Oct); Google Books: 14 phrases via `print_check.py --only gbooks` today, 1 answered (no hits), 13 HTTP 503; one manual retry after a pause, 503; host stopped | negative where searched; Google Books largely unsearched |
| (f) solver repositories and blogs | dbourdeau/cyphersolver fresh shallow clone (0258b8a, 18 Oct 2026): Monluc only in gallica_sweep catalogue copies and Tomokiyo's henryiii text, no reading of f.138 or ff.140-141; aaymeloglu/unsolved-ciphers fresh clone (4d0ab23): no Monluc/fr.4735 hit; Tomokiyo, Cryptiana henryiii (repo copy): key and jargon notes, no plaintext of f.138; sources/lasry PAPERS.tsv and sources/cyphersolver 2026-10-14-lasry: no Monluc | negative (key published, no reading) |
| (g) scholarship | OpenAlex "Monluc Pologne 1573" (131 hits, top 10 read by title): no cipher or edition item; one lead, L. Latoch, "Approcher un objet politique non-identifié : Français et Italiens face aux premières élections royales de Pologne", RHMC 68-1 (2021), doi 10.3917/rhmc.681.0009 -- may quote fr.4735 letters; its Cairn PDF answered 403, **unreachable**; Semantic Scholar: no usable answer (no total returned), unreachable today; web search (3 queries: Monluc + reine mère + avril 1573 + seconde oraison; "fr. 4735" + déchiffrement; Lasry + Monluc + 1573): nothing on this letter or a decipherment of it | negative; one unread lead |
| JSTOR | not queued (N0: a JSTOR row cannot change the class) | -- |

Hosts and requests: archive.org 3, www.googleapis.com 15, api.openalex.org 2, api.semanticscholar.org 1, cairn.info 1, github.com 2
clones, web search 3.

## 6. Safe and unsafe sentences

**Safe:** "Monluc's April 1573 cipher letter on BnF fr.4735 f.138r-v was aligned, with Tomokiyo's published Cipher 1 key, to the period
clear copy of the same letter on ff.140r-141r, which the BnF catalogues as cipher with decipherment; about a third of the cipher's
signs confirm the clear text letter for letter. The text is the clear copy's; it was not found in Noailles (1867) or in the full-text
indexes searched (Google Books not searched)."

**Unsafe:** "We deciphered / read a previously unread Monluc letter", "first decipherment", "984 tokens read at grade C", "the cipher
is solved", "new plaintext about the 1573 election", or any wording that makes the plaintext or the key ours.

## 7. Postmortem

- No novelty over-claim found in NOTES.md (grep for first / new / unpublished / never printed / previously unread).
- **Over-claim corrected:** the C count 984 (and its forerunners 594 -> 714 -> 984 in ROOM.md and STATUS lines) counts every table
  letter the free alignment placed on an equal clear letter. 204 of the 901 C tokens on f.138r-v sit in confirm runs of 1-2, the kind of
  match a shuffled clear text also produces at 0.30 of keyed tokens; this audit grades them M. Use C 780 / 2133 (36.6%) for the
  target, or C 697 / 1983 (35.1%) for f.138r-v, when the reading is described anywhere. A NOTES.md section "VERIFY-MONLUC" records
  this; the committed reading and decode.json are not changed (the verifier does not edit the solvers' grading).
- Suggested fix for the solver side (one line, not done here): give align_c268.py a run-length floor for votes (a vote only where the
  confirm sits in a run of >= 3 consecutive clear letters), with the shuffled-clear run distribution printed beside it.
- Rule 10 status for the board: N0, key `published`, text `known` (in manuscript), result kind `key application`. No
  SECOND-OPINIONS-QUEUE.tsv row (N0 is below N3).
