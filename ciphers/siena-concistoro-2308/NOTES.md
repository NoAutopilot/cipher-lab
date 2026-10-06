open
Bourdeau CATALOGUE.md #336 (dbourdeau/cyphersolver, clone fc0c9e865d0fae67ca92d19750d2b09ab11972e0, siena1421/NOTES.md read in full) read by this worker: whole busta on DECODE, 25 photographed pieces; nos. 6/24, 20/23, 7, 9, 11, 15, 17, 19, 21 filed as open/blocked in Bourdeau's own escalation log (no filed key fits at their length); no. 1 (1421) and nos. 2, 26-28 not among the DECODE photographs. Aymeloglu/unsolved-ciphers (clone 2495c45e8b94ffbc4f09a085224aa5ebce5cdf9f) grepped for "siena"/"concistoro"/"4790".."4814": no hits. OpenAlex `search=Siena Concistoro cipher` and Semantic Scholar `query=Siena Concistoro cifra` (26 Sept 2026): no matching work. DECODE listing (login-free, tools/decode_list.py not run this pass -- read via Bourdeau's own catalogue note instead, which already gives the record status "images" for R4790-R4814); full-size DECODE images not fetched this pass (account-wide block, see CLAUDE.md Access playbook).

## Intake gate

    $ python3 tools/intake_gate_check.py siena-concistoro-2308
    siena-concistoro-2308: open (line 1) -- edition/page or full-text-search citation found within 6 lines
    exit=0

## QUEUE row 2's first cheap test: Bourdeau nos. 25/14/4 key transfer

Slug: siena-concistoro-2308. Target: QUEUE.md "Scored backlog for LANE B6, second pass" row 2, Archivio di
Stato di Siena, Concistoro 2308 fasc. 2 "Lettere in cifra" (DECODE keys R4746-R4789, letters R4790-R4814;
Bourdeau #336). No transcription of this busta exists in ciphers/ yet; the test below works entirely from
Bourdeau's own already-published transcripts and keys (MIT code / CC BY 4.0 text, dbourdeau/cyphersolver,
credited above), read at the pinned commit, per this brief -- no image fetch, no DECODE login.

Test: apply Bourdeau's own recovered sign->letter key values for Siena nos. 25 (`keys/no25_key.txt`), no. 14
(`key14.txt`) and no. 4 (`keys/no04_key.txt`, short/simple sign tokens only -- its longer descriptive names,
e.g. "S (5-like)", cannot literally match another piece's own sign legend) against Bourdeau's own transcripts
of the shorter still-open pieces 7 (R4796), 9 (R4798), 11 (R4800), 15 (R4803), 17 (unlisted R-number, Bourdeau's
own no.17 slot), 19 (R4807) and 21 (R4809) (`transcripts/no07.tok`, `no09.txt` TRANSCRIPTION section, `no11.tok`,
`no15.tok`, `no17.tok`, `no19.txt`/`no21.txt` TRANSCRIPTION sections; token sequences reproduced in
`specs/cheap-tests/siena-concistoro-2308/pieces.py`, key tables in `keys.py`). Coverage (fraction of a piece's
sign tokens present in a given key) is reported but is NOT the test statistic (CLAUDE.md rule 3, bCAS/AX-5799:
coverage from a per-token key cannot depend on token order, so a coverage-only gate is not a test). The test
statistic is order-sensitive: `tools/judge_plaintext.py`'s `it` corpus 4-gram score and its greedy word-cover
(`min_word_cover`), computed on the decoded letters in real transcript order vs. the same key applied to the
same piece with token order scrambled (3 seeds: 1, 2, 3) -- coverage is identical real vs. scrambled by
construction (checked with an assert in the script) but score/word-cover can differ, which is what makes this
a real control per rule 3's own worked examples.

Era flag (queue row 2): these letters are 15th/early-16th c. (busta spans back to 1421); `it` on disk
(tools/data/it16, 6 volumes of 16th-c. Italian letters, ~mid-late 16th c. register) is a real era gap, wider
than the pt17/es17c precedent (CLAUDE.md rule 3) -- graded by eye alongside the numbers below, not trusted on
the score alone even if it had passed.

Script: `specs/cheap-tests/siena-concistoro-2308/run_test.py`. Reference thresholds at N=100 letters on the
`it` corpus (200 samples, seed 1): real_p05 = -1.007, null_p99 = -1.630, real_median = -0.823.

| piece | key | sign_cov (matched/total) | decoded letters | real score | scrambled score mean (3 seeds) | real word-cover | scrambled word-cover mean |
|---|---|---|---|---|---|---|---|
| no07 | no25 | 0.270 (98/363) | 98 | -2.139 | -2.193 | 0.367 | 0.354 |
| no07 | no14 | 0.468 (170/363) | 170 | -2.120 | -2.112 | 0.518 | 0.490 |
| no07 | no04 | 0.457 (166/363) | 166 | -1.885 | -2.022 | 0.572 | 0.488 |
| no09 | no25 | 0.304 (14/46) | 14 | -2.007 | -2.325 | 0.214 | 0.000 |
| no09 | no14 | 0.435 (20/46) | 20 | -1.562 | -2.141 | 0.700 | 0.533 |
| no09 | no04 | 0.435 (20/46) | 20 | -2.311 | -2.161 | 0.250 | 0.483 |
| no11 | no25 | 0.166 (68/409) | 68 | -2.208 | -2.232 | 0.485 | 0.456 |
| no11 | no14 | 0.281 (115/409) | 115 | -1.909 | -1.916 | 0.713 | 0.716 |
| no11 | no04 | 0.152 (62/409) | 62 | -1.927 | -1.869 | 0.790 | 0.839 |
| no15 | no25 | 0.180 (38/211) | 38 | -2.140 | -2.166 | 0.158 | 0.140 |
| no15 | no14 | 0.417 (88/211) | 88 | -1.989 | -2.016 | 0.568 | 0.617 |
| no15 | no04 | 0.204 (43/211) | 43 | -1.968 | -1.975 | 0.605 | 0.659 |
| no17 | no25 | 0.416 (117/281) | 117 | -2.177 | -2.065 | 0.248 | 0.239 |
| no17 | no14 | 0.438 (123/281) | 123 | -2.193 | -2.254 | 0.179 | 0.198 |
| no17 | no04 | 0.416 (117/281) | 117 | -2.316 | -2.151 | 0.436 | 0.442 |
| no19 | no25 | 0.299 (35/117) | 35 | -2.159 | -2.081 | 0.600 | 0.590 |
| no19 | no14 | 0.350 (41/117) | 41 | -2.445 | -2.138 | 0.488 | 0.447 |
| no19 | no04 | 0.188 (22/117) | 22 | -2.435 | -2.087 | 0.682 | 0.636 |
| no21 | no25 | 0.327 (35/107) | 35 | -1.832 | -1.940 | 0.714 | 0.610 |
| no21 | no14 | 0.308 (33/107) | 33 | -2.124 | -2.160 | 0.455 | 0.414 |
| no21 | no04 | 0.206 (22/107) | 22 | -1.938 | -2.355 | 0.636 | 0.455 |

Result: **negative, matched control.** All 21 real-order scores (-1.56 to -2.45) sit below the `it` corpus's
own null_p99 (-1.63) for the majority of cells, and every one sits below real_p05 (-1.007) -- worse than the
letter-shuffled-null threshold, not just below real prose. The real-order vs. scrambled-order comparison shows
no consistent, one-directional margin: real beats scrambled in 11 of 21 cells and loses in 10, by amounts
(median |delta| about 0.1-0.2 score points, 0.03-0.24 word-cover) that are well inside the seed-to-seed noise
of the scrambled control itself (compare no09/no25's own scrambled_cover_mean of 0.000, from 3-4 seeds on only
14 letters). None of nos. 25/14/4's key values decode any of pieces 7, 9, 11, 15, 17, 19, 21 into Italian: no
gain from real order over scrambled order, at any of the three keys, on any of the seven pieces. Grade: S
(cryptanalytic negative with a matched control), per CLAUDE.md rule 4 -- no H or C token read.

Caveat (rule 2, image over transcription): this test used only Bourdeau's own already-published transcripts
and sign legends, not the DECODE page images. A different transcription convention, or the physical possibility
that one of these seven pieces literally reuses no. 25/14/4's key under a different sign-naming scheme than
Bourdeau assigned it, is not excluded by this test -- only that Bourdeau's own transcript + Bourdeau's own key,
read literally, do not fit.

Judge (rule 7), the single best-scoring cell of the 21 (no09/key14, real_score -1.562, real word-cover 0.700):

    $ python3 tools/judge_plaintext.py specs/siena-concistoro-2308.json --text "oueepunavaoeeuaavele"
    FAIL language: score=-1.562, null_p99=-1.188, real_p05=-1.115, real_median=-0.832, mode=both, N=20
    ok   words: cover=0.7, min=0.6, real_text_median_cover=0.9
    FAIL - siena-concistoro-2308 (a PASS is a gate for a verifier, not a reading; rule 10)

FAIL on language even at this best-scoring cell (below both null_p99 and real_p05 at this short N=20); words
alone would have passed the 0.6 bar but the language check does not, and this is only 20 letters against a
piece's real 46 tokens (44% coverage) -- not a candidate reading, the closest of 21 negative cells.

Next step (not run this pass, per brief -- ciphertext-only anneal on nos. 6/24 and 20/23 needs a synthetic-
Italian control of matching length/design and is out of this $3 cap): queue row 2's own fallback.

Search-before-solving (rule 1): Bourdeau CATALOGUE.md #336 read in full (see above); Aymeloglu repo grepped,
no hits; one OpenAlex + one Semantic Scholar query, no hits; web search "Siena Concistoro 2308 lettere in
cifra" and "Siena Concistoro cipher 1421-1530", no solved-status hits found. DECODE record status read from
Bourdeau's own catalogue note (images present, R4790-R4814); the site's own listing not re-fetched this pass.
Checked 26 Sept 2026.

## Ciphertext-only homophonic, nos. 6/24, 20/23 (bSIE2, 26 Sept 2026)

Intake gate re-run (06:56 UTC): `siena-concistoro-2308: open (line 1) -- edition/page or full-text-search
citation found within 6 lines`, exit 0.

Transcripts (Bourdeau, dbourdeau/cyphersolver, `siena1421/transcripts/`, commit
`fc0c9e865d0fae67ca92d19750d2b09ab11972e0` (same pin as bSIE's test-1 clone), read 26 Sept 2026; MIT code /
CC BY 4.0 text) copied into `ciphers/siena-concistoro-2308/transcripts/` with a one-line credit/provenance
header on each file: `no06.tok`, `no24p2.tok` (his P2 only -- his own NOTES.md: "no. 24 P1 = dorse, not
decipherment", so P1 is excluded), `no06_24all.tok` (his own pooled file), `no20.tok`, `no23.tok`,
`no20_23all.tok` (his own pooled file).

**Per-piece N/K and pooling check.** Bourdeau's own NOTES.md already pools these two pairs under one system
each ("No. 24 (R4812): same system as no. 6 (probable)" -- shared opening formula, the 'p p' pair and the W
sign, "every sign in the no. 6 legend"; Escalation section: "systems pooled (nos. 6+24, 20+23)"). Checked
independently this pass, since full-multiset sign-overlap is a poor pooling test on its own (rare one-off name
codes inflate the union): top-20-most-frequent-sign overlap is 17/20 for both pairs, which is the discriminating
number (full-multiset Jaccard is 0.74 for 6/24 but only 0.36 for 20/23 -- driven by each piece's own long tail
of once-or-twice signs, not by the core system differing). Both pairs pool on Bourdeau's own note plus this
check.

| piece | N (tokens) | K (distinct signs) |
|---|---|---|
| no06 | 1056 | 65 |
| no24 (P2 only) | 2638 | 62 |
| no06+24 pooled | 3689 | 73 |
| no20 | 1230 | 51 |
| no23 | 3702 | 67 |
| no20+23 pooled | 4932 | 86 |

**Test.** `tools/family_run.py specs/siena-concistoro-2308.json --family homophonic --cipher
ciphers/siena-concistoro-2308/transcripts/<pooled>.tok --tokens space --param profile=target --seeds 3`
(`--cipher` overrides the spec's own `ciphertext_pending` field with the pooled transcript on disk; N/K/design
are read from that file, so this satisfies "write the ciphertext where family_run can read it" without
clobbering the shared spec between the two pooled-pair runs). Control = synthetic it16 homophonic cipher at
the same N, K, sign-count profile (`profile=target`), 3 seeds, run first; target run only if the control's mean
recovery met the 0.6 gate.

| pair | CONTROL recovery (3 seeds) | CONTROL mean | gate | TARGET judge |
|---|---|---|---|---|
| no06+24 | 0.988, 0.996, 0.992 | 0.985 | met (>=0.6) | FAIL |
| no20+23 | 0.997, 0.555, 0.975 | 0.842 | met (>=0.6) | FAIL |

Judge lines (rule 7, `tools/judge_plaintext.py specs/siena-concistoro-2308.json --file <decode>`), era flag
beside each per the spec's judge block (it16 is mid-late-16th-c. register; these pieces are 15th/early-16th c.,
same era gap already flagged in the test-1 section above -- graded by eye, not trusted on the score alone even
had it passed):

    no06+24: FAIL language: score=-1.372, null_p99=-1.847, real_p05=-0.925, real_median=-0.822, mode=both, N=3689
              ok   words: cover=0.841, min=0.6, real_text_median_cover=0.945
              FAIL - siena-concistoro-2308 (a PASS is a gate for a verifier, not a reading; rule 10)

    no20+23: FAIL language: score=-1.384, null_p99=-1.852, real_p05=-0.954, real_median=-0.814, mode=both, N=4932
              ok   words: cover=0.851, min=0.6, real_text_median_cover=0.945
              FAIL - siena-concistoro-2308 (a PASS is a gate for a verifier, not a reading; rule 10)

Both controls solve near ceiling (mean 0.985 and 0.842 recovery -- the design has plenty of headroom at this
N,K, so a FAIL here is informative, not a control-below-gate non-test per CLAUDE.md rule 3's own headline
paragraph). Word-cover alone clears the 0.6 bar on both (0.841, 0.851) but the language check does not (both
below their own null_p99 and real_p05), so the overall verdict is FAIL on both pooled pairs. Rows appended to
`ciphers/siena-concistoro-2308/HYPOTHESES.md` (control mean+range and target score/judge side by side, per
rule 3). Decodes: `ciphers/siena-concistoro-2308/families/homophonic-1-profile=target-bsie2nos624poolc.txt`,
`.../homophonic-1-profile=target-bsie2nos2023pool.txt`.

K is 73 and 86 for the two pools respectively, both above 30, so the brief's masc fallback (K<=30) does not
apply to either pair.

**Cross-check against Bourdeau's own prior attempt.** His NOTES.md ("Solver calibration") already ran the same
kind of test with his own tools and reports the identical shape of result: his synthetic Italian homophonic
control (2,673 tokens, 58 signs, 3% nulls) "breaks ... perfectly (-1.74/token)" while "the real nos. 6/24 and
20/23 stay at -2.9/token under every variant tried (Italian, Latin, Catalan, Spanish; f-groups merged; 'p p'
merged or dropped; crossed or superscripted signs as nulls; null-aware homsolve3)". This pass's independent
run, different tool and corpus (it16 word/4-gram judge rather than his per-token score, our own homophonic
anneal rather than his homsolve2/3), reaches the same negative on both pooled pairs with a matched control
that solves near ceiling: **negative, matched control**, consistent with a prior negative already on file, not
a novel finding.

Result: **negative, matched control**, both pools. Grade S (cryptanalytic negative with a matched control) per
CLAUDE.md rule 4 -- no H or C token read. Per rule 5's near-solve amendment this is a control-backed negative,
not a control-below-gate non-test, but nothing here beat its control by a margin either, so it does not qualify
as a NEAR.md row on its own (the orchestrator's call, not this worker's per LANE B3's rule that workers do not
edit NEAR.md).

Caveat (rule 2, image over transcription): as with test 1, this used only Bourdeau's own published transcripts,
not the DECODE page images (account-wide image block, see CLAUDE.md Access playbook) -- a transcription
convention difference from the physical signs is not excluded.

Next step (not run this pass): Bourdeau's own escalation log names "a single-hand re-transcription with a
fixed sign inventory" as the way forward for both pools -- that needs the DECODE images, blocked account-wide.

Hosts this pass: github.com 1 shallow clone (dbourdeau/cyphersolver, siena1421 folder only, deleted after
copying the six transcript files above). No other network calls.

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class a (they read it, fully or in part).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/targets/siena1421/NOTES.md ; SOLVED_CATALOGUE.md #125
- Their extent, in their words: read in part: keys recovered from ciphertext for nos. 14, 18, 25; no. 4 from its own fragment; no. 1 of 1421 not photographed
- Their date: 24 Sept 2026 (updated 30 Sept)
- Note: already cited in our NOTES.md (26 Sept 2026)
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## Web and blog check (GF-A2-11, 3 Oct 2026)

Run for LANE-A2PUSH (account 2), 3 Oct 2026, 00:22-00:30 UTC, because the intake gate had no logged web/blog check
for this folder. WebSearch (plain web), WebFetch for opened pages.

(a) Plain web searches, five:
1. `Siena Concistoro 2308 lettere in cifra decifrate` -- hits: Yale Dataverse (Ilardi collection listing "Siena, Lettere
   Cifrate"), cultura.gov.it (Concistoro onomastics volumes 1385-1557), revistas.um.es, Atlas Obscura (Venice), a Tartu
   Oxenstierna decipherment. None names a decipherment of any Concistoro 2308 piece.
2. `Archivio di Stato di Siena cifrari Concistoro cipher letters 15th century deciphered` -- hits: Yale Dataverse, the
   HistoCrypt 2019 proceedings PDF, JSTOR Daily (Venice), Cipher Mysteries "milanese enciphered letters call for help"
   (2011) and ?p=3700, voynich.ninja thread 3943. Nothing on Siena's letters.
3. `"Magnifici et potentes domini" Siena cifra lettera oratore 1456 Borghesi Benvoglienti cifra` (no. 4's opening and
   correspondents) -- hits: Penn Colenda notarial charter 1456, Patrizi timeline (Harvard), Petrucci articles, HAL
   preaching paper. No cipher content.
4. `Siena cipher letter 1421 oldest Sienese nomenclator Meister Geheimschrift Siena` (the folder's own title / no. 1) --
   hits: arXiv 2205.12527, Yale Dataverse, a Czech maths-history PDF, voynich.ninja threads 3533/4618, Cipher Mysteries
   "fifteenth century cryptography" (2016). No item about a Sienese cipher letter.
5. `"Klausis Krypto Kolumne" Siena verschlüsselt Brief Italien 15. Jahrhundert` -- hits: Cipherbrain 24 Mar 2017 (the
   Beinecke spinelli letter, a different item, already handled in this repo), Villa Vigoni "Information, Ciphers and
   Decipherment in Renaissance Italy", Tartu Florentine polyalphabetic paper, Simonetta's rules. No Siena letter.

(b) Blog site searches:
- Cipherbrain: `site:scienceblogs.de klausis-krypto-kolumne Siena` -- only tourist pages; plus search 5 above. No post.
- Cryptiana: `site:cryptiana.blogspot.com Siena cipher` -- no cryptiana page returned. The repo's Tomokiyo snapshot
  (`sources/cryptiana/`) grepped for siena/sienese: galileo.htm (Galileo in Siena, 1633), spanish3.htm ("Cardinal of
  Burgos in Siena", 1550s Spanish), and the cyphersolver index page's "Siena Concistoro ciphers ... partial" (Bourdeau,
  below). No Tomokiyo page on these letters.
- Cipher Mysteries: `site:ciphermysteries.com Siena cipher` -- ?p=34, ?p=200, ?p=59, tags cryptologia/evelyn-welch/cicco-
  simonetta; and the site's own search `ciphermysteries.com/?s=Siena` (WebFetch): four posts (Voynich Q20 recipes,
  Casini da Siena, Scaglia, Urbino intarsia) -- none on Sienese cipher letters.

(c) Opened: Cipher Mysteries "fifteenth century cryptography" (2016/07/06), the one plausible hit: WebFetch reports no
mention of Siena, Sienese letters or the Concistoro in the post or the comments it rendered (header: 907 comments, only
part rendered). A plain curl of the page for a full grep was refused by the host (HTTP "Not Acceptable", Mod_Security);
not retried. So that thread is read in part only.

Result: no decipherment or plaintext of nos. 6/24, 20/23, 7, 9, 11, 15, 17, 19, 21 (the pieces this folder holds open)
found on the open web or in the three blogs. The only public reading of any piece of the busta is Bourdeau's (nos. 4,
14, 18, 25 in part; nos. 8, 10, 12, 13/16, 22 read at the time), already cited in this folder.

## Premise check (GF-A2-11, 3 Oct 2026)

- **(a) Decipherments the folder already mentions: found for other pieces only, not for the open ones.** The folder
  cites Bourdeau's: no. 16 = clear decipherment of no. 13; no. 8's sheet carries its own decipherment; glosses on nos.
  4, 7 (nine letter values, L08), 10; no. 22's clear drafts; no. 24 P1 = dorse ("not decipherment", his words). None of
  these is a decipherment of nos. 6/24, 20/23, 9, 11, 15, 17, 19, 21; no. 7's gloss is partial (nine values) and was
  already the basis of his and our tests.
- **(b) Other solvers' working files: found, partial, already on file.** dbourdeau/cyphersolver HEAD 2341682 (2 Oct
  2026; `targets/siena1421/` last changed 2 Oct), NOTES.md read in full this pass, plus its file list (keys R4750-R4764,
  no04/no18/no25 keys, key14, homsolve2/3, sylsolve, wordsolve, decode/views.jsonl). Status line "read in part (key
  recovered from the ciphertext alone for nos. 14, 18, 25; no. 4 from its own fragment; no. 1 of 1421 not
  photographed)". His own "Remaining gaps" lists nos. 6+24, 20+23, 11 as no-key-material, 7, 9, 15, 17, 19, 21 as
  too-short -- i.e. the same pieces this folder holds open are open there too; no output or rendering of them reads as
  Italian. Already flagged to the parents by SOLVERDIFF-BOURDEAU (2 Oct 2026, ROOM.md) and in "Solver-repo check"
  above; not re-flagged. aaymeloglu/unsolved-ciphers HEAD d2800bb (27 Sept 2026) grepped for `siena`, `concistoro`,
  `4790`-`4814`: no hit.
- **(c) Physical neighbours: not viewed by us.** The neighbours are the busta's other DECODE records (keys R4746-R4789,
  letters R4790-R4814, R1858 key photos); Bourdeau states every record was opened and the clear pages used (his
  Escalation "siblings" and "clear-pages" rows), with no clear copy beside nos. 6/24 or 20/23. We have not seen the
  images ourselves (full-size DECODE images were account-blocked when this folder was worked; A2-HDK, 2 Oct 2026,
  got one record's full image after a browser login -- a per-record re-test is the route if a next step needs it).
- **(d) Recipient's side: not found.** The recipient is the Sienese government itself; the busta is its own archive.
  Printed apparatus named in this folder and by Bourdeau: Cecchini's 1952 Concistoro inventory ("solo parzialmente
  decifrate"), Meister 1902, Senatore 2009 (no. 4) -- no printed decipherment of any open piece. For no. 11 (Acciaiuoli
  to Lorenzo, Rome 13 June 1478) the recipient-side edition would be the Medici correspondence: one IA full-text query
  (`"Donato Acciaiuoli" cifra 1478`) returned only unrelated hits (Poliziano's Coniuratio commentary, Rinascimento 1982
  index lines, Florentine chancery diaries); Lorenzo's own Lettere (Fubini) print his outgoing letters, not this one --
  not checked further this pass.

Verdict of this pass: no decipherment of any piece this folder holds open; status stays `open`. Requests: WebSearch 8,
ciphermysteries.com 2 (1 WebFetch post, 1 WebFetch site search; 1 curl refused, not retried), be-api.us.archive.org 1.

`python3 tools/intake_gate_check.py siena-concistoro-2308` after both sections (3 Oct 2026, GF-A2-11): `siena-concistoro-2308: open (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0 (exit 1 before).

## Image check (IMG-DECODE2, account 2 worker for LANE-IMAGES, 3 Oct 2026)

This closes the gap "We have not seen the images ourselves" in (c) above. Route that worked: one headless-browser login,
`tools/decode_browser_login.js 4795 <scratch> --max-files 0 --listen CMDFILE`, then `page`/`get` lines with absolute URLs. One
login served this target and the three Clairambault key records (clair571-estrades-1645/keys_decode/). R-numbers come from
Bourdeau's piece table (dbourdeau/cyphersolver `targets/siena1421/NOTES.md`, commit a439937, read 3 Oct 2026). No.17 is R4805
there ("20 Aug 1528 ... questa cifra è quella di Balìa"), and nos. 6, 20 and 23 are R4795, R4808 and R4811.

| no. | record | DECODE name | pages (record) | images served | native px |
|---|---|---|---|---|---|
| 6 | R4795 | Concistoro_2308_49 | 1 | 2 (P1, P2) | 4000x2248 |
| 7 | R4796 | Concistoro_2308_50 | 2 | 2 | 2248x4000 |
| 9 | R4798 | Concistoro_2308_52 | 1 | 2 | 4000x2248 |
| 11 | R4800 | Concistoro_2308_54 | 1 | 2 | 4000x2248 |
| 15 | R4803 | Concistoro_2308_57 | 8 | 8 | 2248x4000 |
| 17 | R4805 | Concistoro_2308_59 | 1 | 2 | 2248x4000 |
| 19 | R4807 | Concistoro_2308_61 | 1 | 1 (unnumbered `_P`) | 4000x2248 |
| 20 | R4808 | Concistoro_2308_62 | 1 | 1 | 4000x2248 |
| 21 | R4809 | Concistoro_2308_63 | 1 | 1 | 4000x2248 |
| 23 | R4811 | Concistoro_2308_65 | 1 | 1 | 2248x4000 |
| 24 | R4812 | Concistoro_2308_66 | 2 | 2 | 2248x4000 |

RecordsView fields are the same on all eleven: Italy, Siena, State Archives of Siena; Type Cipher; Status N/A; Cipher Type
Unknown; Symbol Sets "Graphic signs, Alphabet, Numerical"; no date, author, sender or receiver; access "Authentication
required"; created 31 Mar 2023. Additional Information is empty, so there is no licence line on these Siena records (the
Clairambault key records carry DECODE's "not in the public domain" sentence). **Full size was served for all 24 images, and
none was forbidden.png** (sha1s, URLs and sizes are in `images/manifest.json`). The images are not committed: they stay in the
worker's scratchpad under the LANE-IMAGES rule for DECODE images, and the manifest gives the re-fetch command.

Image-type check: one vision call on a contact sheet of all 24 images at about 250 px each. No transcription, nothing graded.
At that size every record looks the way Bourdeau's table describes it. Nos. 6, 20 and 23 are pages densely written from edge
to edge. No. 24 is two dense pages, and its P1 has a short block lower down (his "dorse"). Nos. 9 and 21 are narrow slips or
short letters. No. 11 is a folded letter with an address panel (P1) and a written face (P2). No. 15 is eight written pages. No.
17 is a written page and a folded outer leaf. No. 19 is a strip that is part clear and part sign-runs. No. 7 is a long page,
with a docket on its P2. Contact-sheet resolution cannot tell cipher signs from clear script on most pages, so this check only
confirms that the pieces are what the catalogue says. It is not a check of Bourdeau's transcripts. Next step that this enables
(not run, out of brief): read Bourdeau's `no06`/`no20`/`no23`/`no24p2` transcripts against these images line by line. That
would give a reader-error figure for the pooled-pair negatives above (CLAUDE.md rule 3, error bracket), at about USD 3-4 per
pair with line crops (`tools/iiif_lines.py --image`).

Requests: de-crypt.org 52 for the whole job (login flow 2; RecordsView 14 = 11 Siena + 3 Clairambault; full size 36 = 24 Siena
+ 12 Clairambault), 1.7 s apart, no challenge, one login. Thumbnails and ImagesList pages were not fetched. Vision calls: 2 in the
job, 1 for this target.

## READ2-SIENA (3 Oct 2026)

Account 2 worker for LANE-READ2, brief `.claude/briefs/runs/2026-10-03-acct2-read2-siena.md`, 23:16-23:3x UTC (container clock).

**Route.** One headless-browser login, `tools/decode_browser_login.js 4795 <scratch> --fetch <24 absolute filesrv URLs> --max-files 30
--listen` (listener closed with `quit`, unused). All 24 full-size images came back HTTP 200, and **24 of 24 sha1s match
`images/manifest.json`**. Images stay in the worker scratchpad, not committed; the one saved RecordsView page was deleted (it carried the
account name). Requests: de-crypt.org about 29 (login flow 2, RecordsView 1, 24 full-size, 2 thumbnails auto-discovered), 1.5 s apart,
no challenge. github.com 1 sparse shallow clone (dbourdeau/cyphersolver `targets/siena1421`, HEAD a439937, read/grep only, not copied).

**Vision looks: 12** (one per record at <=1500 px long side; no. 15's eight pages in two 2x2 sheets), by the worker itself, no subagents.

**Records table: `records.tsv`** (19 rows, one per page or page group). Summary:
- Every page matches Bourdeau's piece table in content class. **None of the eleven records carries a key table**, and **no interlinear or
  marginal decipherment is visible at 1500 px on any of them** (no. 7's faint letter glosses, reported by Bourdeau, are below that size,
  so not contradicted). Dorses and address panels: nos. 6 P1, 7 P2 (address part), 9 P2, 11 P1, 17 P2, 24 P1 (lower part).
- Open cipher, estimated from the transcripts' token counts and checked against the image for extent: nos. 6 (1,056), 24 P2 (2,638),
  **24 P1 (637)**, 20 (1,230), 23 (3,702), 7 (363), 9 (46), 11 (409), 15 (229, pp. 2 and 6), 17 (282), 19 (118), 21 (107), about
  10,800 signs in all.
- **Two corrections to the folder's reading of the material, from the images:**
  1. **No. 24 P1 is not excluded material.** Its top eight lines are the letter's own cipher running over onto the dorse (Bourdeau's
     agent E transcribed them: 637 tokens, one pass, `transcripts/no24.txt` in his repository, in a different sign-naming convention).
     bSIE2 read Bourdeau's "no. 24 P1 = dorse, not decipherment" as a reason to leave P1 out. That sentence only says P1 is not a
     decipherment of anything. So the 6+24 pool on disk (3,689 tokens) lacks about 637 open tokens of the same system.
  2. **No. 17's signature reads as the sender.** "Deditissimo Bart.o Tantucci" is written at the foot of P1, and the P2 address
     is to a "magnifico et generoso cavaliere ... oratore". Bourdeau's table has "to Bartolomeo Tantucci?". This was read at 1500 px
     only and is uncertain. It matters for which key ("quella di Balìa") applies only in the sense of who held it.
- At a glance, the on-disk tokens fit the images. The no06/no24p2 legend (W, t, p, THETA, BOX, d+, m+) is the Latin-letter-like family
  on nos. 6 and 24, and the no20/no23 legend (o, f, o^n, DIV, digits) is the fo/fö + ÷ family on nos. 20 and 23. This is a class
  check, not a reader-error figure.
- Observation only, not tested: no. 19's run signs (∇, F, 3, digits) look like the family of no. 13's alignment with no. 16
  (Bourdeau: bologna = ∇ E 3 E 17 φ).

**Known-key test (step 3).** No image carries a key table. The one untested pairing on file is Bourdeau's filed keys 25/14/4 against the
two pooled systems: bSIE tested those keys on the seven short pieces only, and bSIE2 ran ciphertext-only on the pools. Script
`specs/cheap-tests/siena-concistoro-2308/run_test_pools.py`, output `results_pools.json`, uses the same by-name sign matching as
`run_test.py`. The statistic is the it-corpus 4-gram per-letter score of the decoded stream in order. Control (a) is 200
value-shuffled keys in real order (it keeps coverage and the value multiset, so a degenerate key cannot win). Control (b) is 20
order-shuffled cipher streams (coverage identical, asserted). Both can differ from the target for an order-sensitive score. The positive
control is a real it passage of the pool's length, thinned at the key's coverage, with the correct map vs 200 shuffled maps; its power
is the share of 20 passages where the correct map beats all 200.

| pool | key | covered/tokens | real score | value-shuffled mean (max) | shuffled >= real | order-shuffled mean (max) | pos-control power |
|---|---|---|---|---|---|---|---|
| 6+24 | no25 | 749/3689 | -2.240 | -2.162 (-1.742) | 151/200 | -2.220 (-2.138) | 0.60 |
| 6+24 | no14 | 1634/3689 | -2.106 | -1.962 (-1.580) | 171/200 | -2.072 (-2.013) | 1.00 |
| 6+24 | no04 | 1158/3689 | -1.945 | -2.115 (-1.878) | 11/200 | -1.973 (-1.922) | 1.00 |
| 20+23 | no25 | 1814/4932 | -2.132 | -2.170 (-1.763) | 58/200 | -2.112 (-2.058) | 1.00 |
| 20+23 | no14 | 3182/4932 | -2.073 | -1.957 (-1.591) | 157/200 | -2.129 (-2.096) | 1.00 |
| 20+23 | no04 | 1276/4932 | -2.098 | -2.130 (-1.728) | 67/200 | -2.113 (-2.087) | 0.75 |

Result: **negative, matched controls.** At five of six cells the positive control has power 0.75-1.00 at the cell's own covered count. No
real key beats all 200 value-shuffled keys at any cell, which is what the positive control does at those powers. The closest cell (6+24 /
no04, 11 of 200 shuffled at or above) sits inside its own order-shuffled range (-1.945 vs order-shuffled max -1.922), and its decode
("nmeangoohoogmeoooaupned...") is not Italian. Judge on that cell (rule 7, a FAIL reported as a FAIL):

    $ python3 tools/judge_plaintext.py specs/siena-concistoro-2308.json --file <6+24/no04 decode>
    FAIL language: score=-1.945, null_p99=-1.815, real_p05=-0.947, real_median=-0.82, mode=both, N=1158
    ok   words: cover=0.647, min=0.6, real_text_median_cover=0.945
    FAIL - siena-concistoro-2308 (a PASS is a gate for a verifier, not a reading; rule 10)

Caveats:
- By-name matching across different transcribers' sign names (agents B, E, H/I) is the test's weak point, as in bSIE. A shape-level sign
  concordance between no. 14 or no. 25's legend and the pools is not excluded by this test.
- Era gap of the it16 corpus, as flagged above.
- The 6+24 pool lacks no. 24 P1's 637 tokens.

Grade S (cryptanalytic negative with controls), no H or C token. Rows are in HYPOTHESES.md (prose, above the family_run table). Status
unchanged: `open`.

**Next steps per open piece (suggestions, not run):**
- 6+24: bring no. 24 P1's 637 tokens into the pool. This needs a sign-name concordance between agent E's P1 names (SQ, SIX, FO, Z3 ...)
  and the no06/no24p2 legend, done from crops of both faces. Then a line-crop reread of no06/no24p2 against the images for a
  reader-error figure (about USD 3-4 per pair, `tools/iiif_lines.py --image`), so bSIE2's negative is bracketed (rule 3, error band).
- 20+23: line-crop reread of no20/no23 for the reader-error figure (about USD 3-4); then the fo/fö groups as syllabic units (Bourdeau's
  own note), as a family with its own matched control.
- 7: crop the cipher block at native size to read the faint glosses Bourdeau used (nine values) and look for more (about USD 1-2). [done R8-SIENA7, 6 Oct 2026: 7 C, 4 M, 3 withdrawn; see below]
- 17: settle sender/recipient from a native crop of the foot of P1 and the P2 address (about USD 0.5). This names whose "cifra di Balìa"
  to look for among R4773-style 16th-century Balìa keys.
- 19: compare its run signs with the no. 13/16 alignment (Bourdeau's) as a known-key fit with value-shuffled and order-shuffled controls
  (about USD 2). This is disk plus one crop. [done R8-SIENA19, 6 Oct 2026: no fit, non-test by the pre-registered power gate; see below]
- 15: Bourdeau's candidate key R4764 (Buoninsegni, oratore a S. M.tà) has not been tested in this folder. A shape concordance from the
  R4764 key image plus pp. 2 and 6 crops is needed first (one more DECODE record, about USD 3).
- 9, 11, 21: no step on disk beyond these. 11 needs a Florentine key (Acciaiuoli 1478, none located); 9 and 21 are too short alone.

## R8-SIENA7 -- no. 7 gloss crop (account 4 worker for LANE-RUN8-account-4, 6 Oct 2026, 04:03-04:1x UTC)

Brief `.claude/briefs/runs/2026-10-06-account4-run8-jobs.md` job R8-SIENA7 (the "7:" next step of READ2-SIENA). Status unchanged: `open`.

**Route.** The image is not committed (manifest note), so one headless DECODE login: `tools/decode_browser_login.js 4796 <scratch>
--fetch <IMG_R4796_I27935_P1.jpg filesrv URL> --max-files 1`. Full size served, 2248x4000, **sha1 2b12f15a... matches
images/manifest.json**. Saved RecordsView page deleted (account name). Image and crops stay in the scratchpad. Requests: de-crypt.org
about 4 (login 2, RecordsView 1, image 1), 1.5 s apart, no challenge; github.com 1 sparse shallow clone of dbourdeau/cyphersolver
`targets/siena1421` (HEAD adbf9a1, read only: `transcripts/no07.txt`, `no07_reading.txt`).

**Crop step (pasted):**

    $ python3 tools/iiif_lines.py --image IMG_R4796_I27935_P1.jpg --out crops --region 60,2540,2190,560 --prefix no7 \
        --max-width 1150 --overlap 120 --distance 42 --prominence 20 --ink 120 --smooth 3 --lines-per-crop 2 --top-margin 20
    ...(local): region 2190x560, 12 lines ... centres (region y): 7 57 102 155 199 250 300 348 400 444 506 548
    wrote 18 crops

Two-line crops, so a gloss between lines stays whole; then autocontrast and 1.5x/2x views, and 3-5x zooms of the five spots Bourdeau
names. One vision pass by the worker itself over all 18 crops (no subagent). No gloss value differed from Bourdeau's and no further
gloss was found, so the brief's conditional second blind pass and reconciliation were not run.

**Result (`glosses_no07.tsv`, one row per gloss, grade C/M/X):**
- **C 7**: L08 q=a, 6=n, +=o (twice), 2=e, x=r, c=o; L04 QP=e. These seven agree with Bourdeau's values.
- **M 4**: L08 7=l (the "l" stands between 7 and q, aligned only by order), B3=t (t or i), 8o=i (the mark may be the sign's own head,
  not a letter); L04 "o" over the 4/2 junction. Over 2 it **conflicts with L08's 2=e**; over 4 it would give 4=o (4 is 23 of 363
  tokens). Logged as a conflict, not settled (rule 4).
- **X 3, withdrawn as glosses**: L06 "er" over 3 is the end of the clear word on the line above; L12 "+" over x is the descender of
  L11's P_; L03's marks below "o sl =" are dots and short strokes, not letters. The same kind of point marks also sit under "a t" in L09.
- **Of Bourdeau's nine L08 values, six read C on the image (q, 6, +, 2, x, c) and three M (7, B3, 8o); the two L04 glosses in his
  transcription notes add one C (QP=e) and one M.** No gloss outside lines L04 and L08 was found on any of the
  ten cipher lines (L02-L12, Bourdeau's numbering). The seven C signs cover 88 of the 363 tokens (24%) if each sign keeps one value. This
  is a key-material count, not a reading. Nothing was decoded and no key was rebuilt (brief).
- Note for a later step: the L08 gloss reads "l a n o t e r o (i) o" over a run where the clear text then says "volendo mandare". A word
  division of the gloss was not tried.

**Next step for no. 7 (suggestion, not run):** an L04 crop at higher zoom, or a second reader, to place the "o" (2 or 4). Then a
homophonic fit of the 363 tokens with the seven C values fixed, against a matched control of the same N, K=45 and fixed-value count
(rule 3). Bourdeau files no. 7 as too-short. Fixed values change that only if the control reads at this N. About USD 3.

## R8-SIENA19 -- no. 19 against the no. 13/16 alignment (account 4 worker for LANE-RUN8-account-4, 6 Oct 2026, 04:20-04:2x UTC)

Brief `.claude/briefs/runs/2026-10-06-account4-run8-jobs.md` job R8-SIENA19 (the "19:" next step of READ2-SIENA). Status unchanged:
`open`. Disk only: no crop was needed and none was cut. Requests: github.com 1 sparse shallow clone of dbourdeau/cyphersolver
`targets/siena1421` (HEAD adbf9a1, read only: `NOTES.md`, `transcripts/no19.txt`). No other host.

**What the "alignment" is.** The whole no. 13/16 alignment on disk is Bourdeau's two worked words (his NOTES.md, no. 13 + no. 16):
bologna = ∇ E 3 E 17 φ ₀⁰; accordi con = ₀ ⁿθ(cc) E ‡ + 15 ƥ E φ. That is 12 sign values over ten letters. No transcript of no. 13
exists in either repository. Only three no. 19 signs have a counterpart by legend: TRI (▽) = ∇ -> b, 3 -> l, CT (¢/‡-like) = ‡ -> r
(primary, P). A wider variant (V2) adds small 0 = ₀ -> a and TT (ŧŧ) = ‡ -> r. Concordance fixed in advance.

**Pre-registration:** `PREREG-R8-SIENA19.md` and `transcripts/no19.tok` (118 tokens, Bourdeau agent J, CC BY 4.0), pushed in
d7818f743 before the scored run. Script `specs/cheap-tests/siena-concistoro-2308/run_test_no19.py` (`--check` exit 0), output
`results_no19.json`. S1 = order-free count fit (sum of log10 binomial upper tails, it16 letter frequencies). S2 = mean it16 bigram
log10 probability over adjacent covered pairs. Control (a) is 2000 value-shuffled keys drawn from the key's own ten letters, used for S1
and S2. Control (b) is 200 order-shuffled streams, used for S2 only, because order cannot change S1 (rule 3).

| variant | covered/118 | S1 real | S1 val-shuf mean (p95), p | S2 real (pairs) | S2 val-shuf mean, p | S2 order-shuf mean, n>=real | power S1 / S2 (H1a; H1b) |
|---|---|---|---|---|---|---|---|
| P | 17 | -6.812 | -2.379 (-0.164), 0.939 | -1.814 (bl lb bl lb) | -1.589, 0.702 | -1.375, 162/185 | 0.00/0.05; 0.00/0.02 |
| V2 | 24 | -6.818 | -2.673 (-0.333), 0.924 | -1.753 (6 pairs) | -1.553, 0.710 | -1.378, 183/200 | 0.15/0.78; 0.18/0.23 |

**Result.** Neither statistic reaches the gate (p <= 0.05) in either variant. The real key scores below the mean of both controls on
both statistics. By the pre-registered rule, positive-control power is below 0.8 in every cell (best 0.78, V2/H1a/S2), so this is
logged as a **non-test at this N** and not as a control-backed negative.

**Post hoc, not in the PREREG (reported as such).** The misfit is in the counts. TRI occurs 10 times in 118 tokens, against 1.13
expected for b. Homophones could only make a b-sign rarer, never commoner. In 100 it16 passages under H1, the true key never scored S1 as
low as no. 19's real -6.81 (0/100 in all four cells). The repeated "TRI 3 TRI" = "blb" (L08, L10) points the same way. This points to
▽ in no. 19 not being no. 13's b-sign. It is one sign identification, not a test of the key family, and it does not reach a gate.

Grades: no token read. No H or C; this is a cryptanalytic result about one sign. No key was rebuilt and nothing was decoded (brief).

**Next step for no. 19 (suggestion, not run):** none cheap on this key. A fuller no. 13 transcript (DECODE R4801) aligned to no. 16
(R4804) would give more than three concordant signs, at about USD 3-4 (two images, one login, crops). Until then, no. 19 stays
too-short with no fitting key.


## R9-SIENA15 -- no. 15 against key R4764, shape concordance (account 4 worker for LANE-RUN9-account-4, 6 Oct 2026, 05:43-05:5x UTC)

Brief `.claude/briefs/runs/2026-10-06-account4-run9-jobs.md` job R9-SIENA15 (READ2-SIENA's "15:" next step). Status unchanged: `open`.

**Route.** One headless DECODE login, `tools/decode_browser_login.js 4764 <scratch> --fetch <4 filesrv URLs> --max-files 4 --delay 1700`:
R4764 P1 and P2 (2248x4000; P2 sha1 14be97b682e3..., P1 d3ce92595136...; not in images/manifest.json before this job) and R4803 P2/P6
(**sha1s 71b6b062... and 0148d2e4... match images/manifest.json**). Saved RecordsView page deleted (account name). Images and crops stay
in the scratchpad. Requests: de-crypt.org about 7 (login 2, RecordsView 1, images 4), 1.7 s apart, no challenge; github.com 1 sparse
shallow clone of dbourdeau/cyphersolver `targets/siena1421` (HEAD adbf9a1, read only: NOTES.md, keys/R4764.txt, transcripts/no15*.txt).

**Crop step (pasted):**

    $ python3 tools/iiif_lines.py --image IMG_R4803_I27950_P2.jpg --out crops --region 60,1990,2150,600 --prefix p2 --max-width 1100 \
        --overlap 100 --distance 45 --prominence 20 --ink 120 --smooth 3 --top-margin 20
    ...(local): region 2150x600, 10 lines ... wrote 30 crops
    $ python3 tools/iiif_lines.py --image IMG_R4803_I27950_P6.jpg --out crops --region 60,800,2150,560 --prefix p6 (same options)
    ...(local): region 2150x560, 8 lines ... wrote 24 crops

The line bands were viewed as two native-resolution half-width strips per page (the same regions, autocontrast). The key was viewed as
four native crops of R4764 P2 (alphabet left half, alphabet right half, Doppie row, Nulle row; PIL crop, autocontrast). Vision looks: 9,
by the worker itself, no subagents.

**Transcript defect found (Bourdeau's files).** His `transcripts/no15.tok` omits L2.15's whole run (21 signs, "8 O2 DOT H LAM Q+ PSI TH
DIV A OL ST 4 LAM M3 OO 4 R P U LV"; the run is plainly on the image at the end of the "prudentia loro" line and is in his own verified
`no15v.txt`). `transcripts/no15.tok` in this folder is built from no15v.txt's ENTRIES instead: 232 sign tokens, clear text as breakers.

**Concordance (`concordance_R4764_no15.tsv`, fixed before scoring).** The key sheet reads as Bourdeau's `keys/R4764.txt` gives it;
no disagreement with his letter values was seen at native size. Primary set P: DOT=e, TH=i, D=t, LV=g, PSI=p, #=a, Y=a, P+=&, and
no. 15's capitals read as the Doppie row's capitals (H=ff, A=bb, a=ll, Z=nn, E=qq, K=ss); nulls STAR, OO, 8, DIV, 4, 7. These cover
71 + 27 of 232 tokens. **Most of no. 15's commonest signs have no counterpart on the sheet at all:** LAM, R, U, XT (10 each), O2 (8), 1,
o, MM, TO, ST, RHO, OL... -- the key has no bullseye, no ⊔, no barred x, no capital R. Variant V adds 11 looser likenesses (A=a,
Q+=u, P=&, LAM=g, U=n, TRI=b, 9=a, DF=t, O2=e; OO: and OI null; # null instead of a): 110 valued + 34 null tokens.

**Test (PREREG-R9-SIENA15.md, pushed in cc19de4a4 before the scored run; `specs/cheap-tests/siena-concistoro-2308/run_test_no15.py`,
`results_no15.json`, `--check` exit 0).** S2 = mean it16 bigram log10 probability over adjacent letters inside valued stretches
(it16 = 16th-century Italian letters, era-matched to 1546-47). Controls: (a) 2000 value-shuffled keys, (b) 200 order-shuffled
streams; both can move S2. Gate p_a <= 0.05 and real > p95(b). Positive control: 100 it16 passages enciphered under "R4764 is the
key" at the target's own valued count; power < 0.8 means non-test.

| variant | valued / null / 232 | S2 real | val-shuf mean (p95), p_a | ord-shuf mean (p95) | gate | power |
|---|---|---|---|---|---|---|
| P | 71 / 27 | -1.354 | -1.484 (-1.252), 0.267 | -1.402 (-1.285) | FAIL | 0.63 |
| V | 110 / 34 | -1.508 | -1.529 (-1.331), 0.478 | -1.443 (-1.351) | FAIL | 0.96 |

**Result.** P misses its gate at power 0.63: **a non-test at this N** (pre-registered), not a negative. V misses at power 0.96: a
**control-backed negative for the V mapping** (V's real S2 sits below its own order-shuffled mean). Neither says R4764 is not
no. 15's key: 134 (P) or 88 (V) of the 232 tokens are signs with no shape counterpart on the sheet, so no mapping of R4764 as drawn
can be fitted to no. 15 by shape alone. Bourdeau's own verdict ("sign mapping inconclusive") stands, now with numbers.

Implementation note (fixed before the reported run): the script's first run read the sign "#"'s two rows as comment lines (P then
had 69 valued tokens, not the PREREG's 71); the parser was corrected to match the PREREG and only the corrected run is reported.

**Post hoc, not in the PREREG (reported as such).** Under P, A=bb occurs 15 times and H=ff 8 times in 232 tokens; it16 has bb 1.3 and
ff 0.9 per 1000 letters (expected under 0.5 each here). no. 15's capitals are therefore not R4764's Doppie signs at their written
values. Taken with the missing ◎, ⊔, barred-x and R families, this points to no. 15 using a different (perhaps related) key from
the one drawn on R4764 P2, or a later alphabet of the same style. One observation, no gate.

Grades: no token read; no H or C. Nothing decoded as a reading and no key.tsv written.

**Next step for no. 15 (suggestion, not run):** a shape pass over Bourdeau's second look R4765 ("Spagna, Imperador ..."; nulls
5 8 7 2 # ◎ 4, shares ◎ and #) and the other 1540s orator keys of fasc. 1 for a sheet carrying ◎, ⊔, barred x and R, about USD 2-3 (one
login, key-sheet crops only). If none has them, no. 15 stays too-short with no fitting key.

## R9-SIENA7 -- no. 7 anchored homophonic fit (account 4 worker for LANE-RUN9-account-4, 6 Oct 2026, 05:43-05:56 UTC by date -u)

Brief `.claude/briefs/runs/2026-10-06-account4-run9-jobs.md` job R9-SIENA7 (R8-SIENA7's "Next step for no. 7"). Status unchanged:
`open`. Disk only. Requests: github.com 1 sparse shallow clone of dbourdeau/cyphersolver `targets/siena1421` (HEAD adbf9a1, read
only); no other host. `transcripts/no07.tok` copied unchanged from that clone (agent J, CC BY 4.0, 20 runs, 363 tokens, K=45).

**Pre-registration:** `PREREG-R9-SIENA7.md` + `specs/cheap-tests/siena-concistoro-2308/run_test_no07.py`, pushed in d99f591d4 before
the scored run. Output `results_no07.json` (`run_test_no07.py --check` exit 0). Solver `tools/homophonic_anneal.py` solve(), unchanged,
20 restarts x 60,000 iterations, order 3. Fixed: the seven C glosses (q=a, 6=n, +=o, 2=e, x=r, c=o, QP=e; 88 tokens, 24%).
Corpus: tools/data/it16dip (16th-c. Italian diplomatic letters) minus the held-out Desjardins II file. **Not era-matched**: no
15th-c. Italian corpus is on disk, and no. 7 is a 1450s Sienese despatch (Milan embassy, per Bourdeau's description).

| run | seeds | result |
|---|---|---|
| matched control, anchored (N=363, K=45, 7 signs fixed, 64-72 fixed tokens, run lengths = no. 7's) | 1-5 | mean **0.916** (0.884-0.959); gate 0.60 **met** |
| same control, blind (no fixes) | 1-5 | mean 0.875 (0.722-0.959) |
| target, anchored | 1-3 | best score -907.1 (seed 1); seeds 1/2 near-identical decodes |
| order-shuffled target, same fixes (ARM-C1 null) | 1-3 | scores -975.4 / -970.2 / -980.6 |
| post hoc, not in the PREREG: control anchored with injected sign error 10 / 20 / 30% | 1-3 | 0.597 / 0.425 / 0.346 |

Judge (rule 7, FAIL reported as FAIL; spec language `it` = it16):

    $ python3 tools/judge_plaintext.py specs/siena-concistoro-2308.json --file <target seed-1 decode>
    FAIL language: score=-1.242, null_p99=-1.764, real_p05=-0.932, real_median=-0.816, mode=both, N=363
    ok   words: cover=0.873, min=0.6, real_text_median_cover=0.945
    shuffled-target decodes, same judge: FAIL -1.411 / -1.326 / -1.345 (words cover 0.81-0.84, also "ok")

Target decode, seed 1 (no grade; not Italian): `acconetaeiandenutticheodeilluedionuiaceioderacceraleediionutontinteiertiai
ctaimenteeforaesaeadriifratifutcceettatraealeicconiaontooilediongoililmciairecconisotalidereataalertdogliti...` (full text in
results_no07.json). The fit piles 7#, 8, 9 and q on a (49 tokens) and the word-cover check passes on the shuffled nulls too, so
cover is no signal at this N.

**Cross-check against the four M glosses (not fixed in the run):** the fit gives 7=s (gloss l), B3=p (gloss t/i), 8o=p (gloss i),
4=t (L04 "o" over 4/2). It reproduces none of them. The L08 glossed run decodes "s a n o p e r o p o" against the gloss "l a n o t e r o i o".

**Result.** The matched control reads (0.916 against a 0.60 gate), the target does not reach the judge (-1.242 against real_p05
-0.932), and the target sits only about 0.1 above its own shuffled-order decodes. That is a negative for a plain homophonic
substitution with the seven C anchors, under two caveats that keep it from being a design exclusion:
1. **Headroom (rule 3).** The control already reads 0.875 blind at this N and K, so the anchors add about 4 points. This run
   could not show what the anchors are worth. It only shows that a clean homophonic text of this size would read with or
   without them. Bourdeau's "too-short" filing is not borne out for a clean simple-homophonic design; whatever stops no. 7 is
   something else.
2. **Error band (rule 3, SALV-DIAG).** The control falls to the gate at about 10% injected sign error (0.597) and below it at 20%.
   No. 7 is a single-pass transcription (agent J) with no measured reader-error figure. A negative at an unmeasured error level
   is conditional on the transcription being under about 10% wrong.
   Other differences the control does not model: a nomenclator (Bourdeau notes the related R4750 key is a Latin-word nomenclator
   with multi-sign codes), nulls, and 15th-c. Sienese spelling against a 16th-c. model.

Grades: no token read. No H or C beyond the seven glosses already on file (unchanged), and no key.tsv was written. Cryptanalytic
result only.

**Next step for no. 7 (suggestion, not run):** measure the transcription error first: a second blind line-crop pass of L02-L12
against agent J (crops from R8-SIENA7's region, `tools/iiif_lines.py --image`, one DECODE login, about USD 3 for 2 passes + 1
reconciliation). Then, if the error is under about 10%, a homophonic + nomenclator family (multi-sign codes for frequent words,
R4750-style) with its own matched control. If it is over 10%, this negative is a non-test and is logged as one.
