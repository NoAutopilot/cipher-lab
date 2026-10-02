open
Gomberville, *Les Mémoires de Monsieur le duc de Nevers* (Paris 1665), Partie 1 (Gallica bpt6k6435941k) and Partie 2 (bpt6k9738856z), full-text search (Gallica ContentSearch "1571", "Birago", "Lodouico", "Avril 1571", "Ianvier 1572", "Mars 1572") read by this worker on 2 Oct 2026: no Birago letter of 1571-72 in either part (the 1571 hits in Partie 1 are the English marriage negotiation, PAG_562-618); no other edition of the Birago-Nevers correspondence exists (searched, see below).

# Lodovico Birago to the Duke of Nevers, BnF fr.3252, three cipher letters (26 Apr 1571, 8 Jan 1572, 13 Mar 1572)

NEVBIR-3252 (2 Oct 2026, account 2 worker for the account-3 orchestrator), brief
`.claude/briefs/runs/2026-10-02-acct3-nevbir-3252.md`. Source of the candidates: `../nevers-birago-fr3251-1572/BIRAGO-POOL.tsv`
(BIRAGO-SCOUT). Sibling folders: `../ceppo-nevers-fr3251-1570s` (Ceppo-Nevers key, fr.3251 1570-71 letters, and the fr.3252
f.36-37 witness of 5 Apr 1571), `../birago-nevers-1571` (fr.3251 f.119, the Nov 1571 numerical cipher),
`../nevers-birago-fr3251-1572` (Nevers-Birago 1572 key). Tools and keys are used from those folders by path.

## Sources

- BnF français 3252, Gallica `https://gallica.bnf.fr/ark:/12148/btv1b9060232m` (184 canvases, labels all NP; canvas = folio + 1,
  confirmed by eye on the ink foliation of canvases 48 (47), 101 (100), 118 (117) this session). Finding aid
  (as harvested in Bourdeau's `research/gallica_sweep/bnf_candidates.txt`, BnF notice text): no.30 "Lettre, avec chiffre, de
  « LODOVICO BIRAGO » au « duca di Nevers,... Da Saluzzo, li 26 aprile 1571 ». En italien"; no.67 "... Da Saluzzo, li 8 di
  genaio 1572 ». En italien"; no.77 "... à monseigneur le duc de Nyvernois,... De Saluces, le XIIIme mars 1572".
- Images on disk: `images/` (overviews, 1600 px, canvases 47-49, 100-102, 117-119; two native crops of canvas 101). Manifest
  `images/manifest.json`.

## Layout

| no. | folio (canvas) | date | language | cipher | est. signs | decipherment on the leaf | first-test key |
|---|---|---|---|---|---|---|---|
| 30 | f.47r (48 right) | Saluzzo 26 Apr 1571 | Italian | symbol cipher, ~21 lines from "Visto che non ui è che ri pensi." to "Il Grande mi scriue", foot of f.47r; letter continues in clear on f.47v, ends f.48r with signature | ~850 | none seen (overview + premise (c)) | Ceppo-Nevers printed key (Tomokiyo), as applied in `../ceppo-nevers-fr3251-1570s` |
| 67 | f.100r (101 right) | Saluzzo 8 Jan 1572 | Italian | digits with `+` separators, two runs: L1-L8 (after "harebbe a caro 76") and L9-L12 (after "Io dico la pura et mera uerità") | ~800 digits | none seen | Nov 1571 numerical (f.119) or Nevers-Birago 1572 |
| 77 | f.117r (118 right) | Saluces 13 Mar 1572 | French (secretary hand) | symbol cipher, ~13 lines between "Seullement Monseigneur je vous diray" and "Monseigneur je supplie Dieu" | ~330 | none seen | inventory and design check only |

## Check-solved (NEVBIR-3252, 2 Oct 2026)

1. **Web search** (four plain queries, 2 Oct 2026): `Lodovico Birago Nevers "26 aprile 1571" OR "8 gennaio 1572" OR "13 mars 1572"
   Saluzzo lettera` (Wikipedia Saluzzo marquises, unrelated catalogue rows; nothing on these letters); `"français 3252" OR
   "fr. 3252" Birague Nevers chiffre` (no relevant hit); `Birago Nevers 1571 1572 cipher letters BnF 3252 deciphered` (Tomokiyo's
   HistoCrypt paper on the 1592 Henri IV-Nevers digit cipher, another letter and key; nothing on fr.3252); model-solve family
   covered by the same queries (no hit). HARVEST-D (28 Sept 2026, `../ceppo-nevers-fr3251-1570s/NOTES.md`) had already found the
   Treccani DBI life of Lodovico Birago cites fr.3252 among its manuscript sources, with no text of any letter.
2. **Standard edition.** None for the sender; the recipient's edition (Gomberville 1665, both parts) searched inside, line 2 above.
   OCR positive control from VERIFY-NEVBIR-90REST (same day, `../nevers-birago-fr3251-1572/AUDIT.md`): "Birague" and "Lodovico"
   signatures are found by the same search, so a printed Birago letter would be expected to show.
3. **Community lists.** Tomokiyo, `sources/cryptiana/web/nevers.htm` (local mirror): its BnF list covers fr.3251 and other
   volumes; fr.3252 is not listed (HARVEST-D, 28 Sept 2026, and BIRAGO-SCOUT, 2 Oct 2026; re-grepped this session: "3252" absent).
4. **DECODE** (login-free RecordsList, 2 Oct 2026): `x_c_holder LIKE 3252` 0 records; positive control `x_c_holder LIKE 3621`
   8 records.
5. **Bourdeau** (`dbourdeau/cyphersolver`, shallow clone 2 Oct 2026, grep "3252", "birago", "btv1b9060232m"): the three letters
   appear only as rows of his BnF candidate sweep (`research/gallica_sweep/bnf_candidates.txt` lines 274-277, "## 1501-1600
   btv1b9060232m ... 3 items", nos.30/67/77, notice text only); no target folder, no reading, no status. His README's Birago rows
   are fr.3315 (Renato Birago 1574) and fr.3251 f.119.
6. **Aymeloglu** (`aaymeloglu/unsolved-ciphers`, shallow clone 2 Oct 2026, grep "3252", "birago", "birague"): no hit.

Verdict: **open** for all three letters. Not found-solved.

## Web and blog check (NEVBIR-3252, 2 Oct 2026)

(a) Plain web searches: the four queries in Check-solved item 1. (b) Blog site search:
`Birago Nevers chiffre site:cryptiana.blogspot.com OR site:ciphermysteries.com OR site:scienceblogs.de` -- hits were unrelated
Cipher Mysteries pages (Voynich, Cryptologia tags) and a 2016 Klausis Krypto Kolumne month index; none names Birago, Nevers or
fr.3252. The Cryptiana blog's own Birago posts (July and August 2024) are on fr.3251 f.119, not these letters (HARVEST-A,
28 Sept 2026, `../nevers-birago-fr3251-1572/NOTES.md`). (c) No plausible hit had a comment thread to read. Result: no reading
or decipherment of fr.3252 nos.30, 67 or 77 located on the open web or the three blogs.

## Premise check (NEVBIR-3252, 2 Oct 2026)

**(a) the folders' own files.** This folder is new. The sibling folders mention fr.3252 only for the f.36-37 witness (5 Apr
1571, interlinear clerk's decipherment, HARVEST-D) and in BIRAGO-POOL.tsv, whose rows for f.47r/f.100r/f.117r read
"decipherment_attached: no (none seen)". Not found.

**(b) other solvers' working files.** Bourdeau: candidate-list rows only (Check-solved item 5), no apply-key output, no
rendering. Aymeloglu: nothing. Not found.

**(c) physical neighbours, at native resolution where anything was written.** Canvases 47-49, 100-102, 117-119 viewed (1600 px
overviews); every opening was inspected for an interlinear gloss over the cipher, a slip, or a decipherment on the facing page.
- f.47r (canvas 48): no interlinear letters over the cipher lines at overview size; facing page (f.46v, canvas 48 left) is the
  dorse of the preceding item with show-through and a docket "26 April 1571"; canvas 47 is a French letter (unrelated);
  canvas 49 is the clear continuation (f.47v) and the end of the letter with signature (f.48r). No slip.
- f.100r (canvas 101): facing page (f.99v) carries only show-through (a mirrored French letter, checked on a native crop,
  `images/c101_leftblock.jpg`) and a docket, read on a native crop (`images/c101_endorse.jpg`, rotated): "Copie des lettres
  escriptes ... par le S.r Ludovic de Birague ... Janvier 1572" -- a docket for the copies the letter encloses ("la coppia
  della lettera di Sua Maestà"), not a decipherment. Canvas 100 is a French letter of 1572 (f.98v-99r, unrelated text);
  canvas 102 is the clear continuation and signature (f.100v-101r). No slip.
- f.117r (canvas 118): facing page (f.116v) is the address/docket leaf of the preceding item; canvas 117 shows f.116r blank but
  for show-through; canvas 119 shows f.117v (show-through only) and f.118r (faint show-through and a small docket). No slip,
  no clear copy.
Not found, for all three. Caveat: interlinear glosses on the fr.3252 f.36 witness were invisible at 1x and legible only at 2x
(HARVEST-D); the f.47r line crops (native) below were checked for them before transcription.

**(d) recipient's side.** Gomberville's *Mémoires* of the recipient, both parts, searched inside (line 2). Court
correspondence: *Lettres de Catherine de Médicis* vol. 4 (1570-74) was grepped for Birague by VERIFY-NEVBIR-90REST
(2 Oct 2026): five hits are René de Birague, one names Ludovic in command at Saluces after 24 Aug 1572 -- no letter or summary
of these three. Not found.

## Design checks: f.100r (no.67) and f.117r (no.77) (NEVBIR-3252, 2 Oct 2026)

Inventory by eye from native crops only (`images/f100_run1.jpg`: canvas 101, box 4400,3060,3800,560, the first six lines
of run 1; `images/f117_top.jpg`: canvas 118, box 4400,1380,3000,800, the first seven cipher lines). No transcription pass, no
decoding, no subagent call on either letter.

**f.100r, no.67 (8 Jan 1572): fits the Nov 1571 numerical system by inventory; the 1572 key does not fit.** The run opens
"... harebbe a caro 76÷4005441501..." and is continuous digits 0-9 with lower-case letters set into the stream (m, n, h, f
seen: "...0i2mo 0134...", "...94n2", "h24394", "f3054..."), a dotted i/1, and the ÷ sign. That is the look of the fr.3251
f.119 cipher of 13 Nov 1571 (`../birago-nevers-1571/ciphertext.txt`: "÷762¯59150894032f48932...n419093800...0m054493...",
digits with n, m, c, f, a, l and ÷ in the stream). The Nevers-Birago 1572 key cannot be the system here: Tomokiyo's printed
1572 table (`../nevers-birago-fr3251-1572/keys/key_nevers_birago_1572.tsv`) is a table of drawn **symbols** (theta, +, X,
#, triangle, pi, dumbbell...), with digits only as three word codes (85 carmagnola, 86 turino, 89 bugonotti); BIRAGO-POOL.tsv's
"Nevers-Birago 1572 (from Feb 1572, digits)" is a mis-description to correct. So the brief's two candidates reduce to one:
f.100r is a second, longer text in f.119's undeciphered numeric system (Bourdeau closed his f.119 attempt negative at 483
digits, 16 Sept 2026). No key for that system exists (`../birago-nevers-1571/NOTES.md`), so no first test with a known key is
possible -- a design check, not a negative. Next: transcribe the ~800 digits (two passes, digit sheet as for f.119) and
pool with f.119's 483 for the structural tests Bourdeau ran at 483 (prefix/suffix codes, two-digit alphabet), with matched
controls at the pooled length.

**f.117r, no.77 (13 Mar 1572, in French): fits the Nevers-Birago 1572 key by inventory.** Signs seen in the first seven lines,
each matched by description to a cell of the printed 1572 table: theta (a), + (a), bowtie/two interlocked loops (r),
9-like loop on a stem (c or n), omega (s), V/checkmark (d), phi (d), b-loop (e), # (e/n), epsilon (f), plain o (g),
triangle (g), lambda (i), capital D (i), capital B (l), pi (o), two prongs on a base (u), flag/square loop on a stem (u or
che), the R-form (m), and the plain digits "85" (word code carmagnola). Superscript abbreviations "m^a" and "l^o" occur. A
sign-for-sign check against the sorter's labels is still to do; this is a design fit, not a reading, and the plaintext
language (French, unlike every 1572 letter read so far) is untested. Next: two blind passes on the ~330 signs against the
1572 group's own sign sheet (`../nevers-birago-fr3251-1572/sorter/`), then the first test under the printed 1572 key + T42=m
with a French judge corpus (fr16), power control at the measured two-reader error.

## f.47r (no.30, 26 Apr 1571): first test under the printed Ceppo-Nevers key, lines 1, 3, 4 (NEVBIR-3252, 2 Oct 2026)

**Crops** (command pasted before any subagent call, per Usage 6):
`python3 tools/iiif_lines.py --ark btv1b9060232m --canvas 48 --region 4830,2660,3400,1940 --out ciphers/birago-fr3252-1571-72/images/f47 --prefix f47 --max-width 1800 --overlap 0 --follow-slope 400 --slope-local --slope-margin 15`
-> 17 lines x 2 segments (the block is 17 lines, about 50 signs each, ~850 signs; the lines rise about 84 px across the
region, so the fixed-band cut clipped line 1 and the slope cut was used). Two faults the readers found and this worker
confirmed by eye: (1) the slope tracker put band L02 on line 1 (line 2, "ϕζ8.../ ... χij ...", was never cut); (2) each s2
crop repeats the last 3-4 signs of s1 despite `--overlap 0`. L02 was dropped and the seam duplicates removed mechanically
(`harvest/clean_passes.py`: the s2 head of k signs matching the s1 tail in >= k-1 ids; dropped 4/4/4 in pass A, 4/3/4 in pass B).
Tool fault to fix (one-line suggestion, not done here): `--follow-slope` can lock two bands onto one line when the first
line sits at the region's top edge, and its sheared segments do not honour `--overlap 0`.

**Blind passes.** Two value-blind Sonnet passes against `../ceppo-nevers-fr3251-1570s/harvest/sign_sheet_blind.png`, brief
`harvest/blind_pass_brief.md` (copied from HARVEST-D2's), 8 crops each: `harvest/passA_L01-04.tsv`, `passB_L01-04.tsv`
(cleaned: `passA_clean.tsv` 165 signs, `passB_clean.tsv` 159). No interlinear gloss letters were seen over these lines by
either reader or by this worker on the native crops. Value-blind reconciliation (`reconcile_blind.py`): 167 aligned, **94
agreed (0.56)** -- most splits are pass B's X_NEW (about 40) where pass A chose a sheet cell (barred 8, dot groups, plain
triangle). A third blind Sonnet reader settled 62 of 63 disputed positions (`adjudicate_in.tsv` / `adjudicate_out.tsv`;
by its own report about 25 at M and the rest at L, "could not reliably see bars, dots ... without zooming"); merged sequence
`harvest/recon_L01-04.tsv` (157 signs, 10 still '?'). This worker saw no value before the merge was fixed.

**Test** (`../ceppo-nevers-fr3251-1570s/harvest/decode_control.py recon_L01-04.tsv --shuffles 200 --windows 20 --extra X_THETA2=r`,
corpus it16dip, seed 1):

| run | signs | real key | shuffled mean (sd) | shuffled max | z | rank | power control (20 windows) |
|---|---|---|---|---|---|---|---|
| merged L01+L03+L04 | 157 (11 nulls, 10 '?') | -1.5162 | -2.0766 (0.1604) | -1.5201 | 3.49 | **1/201** | err 0.44 (measured two-reader): **9/20** rank 1, z median 2.67, min 0.43; err 0.20 (for reference only): 20/20, z median 6.28 |
| pass A alone (information) | 165 | -1.5849 | -2.0796 (0.1484) | -1.6181 | 3.33 | 1/201 | not run |
| pass B alone (information) | 159 | -1.7198 | -2.0859 (0.2190) | -1.4486 | 1.67 | 10/201 | not run |

**Verdict for this test: not licensed, not a negative.** The printed key ranks first, but only 0.004 above the best of 200
shuffled keys, and at the measured two-reader error (0.44) the same key on real Italian of this length ranks first in only
9 of 20 windows, so a rank 1 here is what a right key and a wrong key both produce often enough. The 0.44 is a two-reader
disagreement inflated by one reader's X_NEW habit, not a measured accuracy (LESSONS.md "Look-alike pass": the adjudicated
residual is agreement, not accuracy, and is not used as the error figure). The decode (`harvest/reading_f47_L01-04.txt`) is
not a reading and no token is graded. What would settle it: the other 14 lines (rank and power both grow with length; at
~850 signs the control at 0.44 should clear), and a lower reader error (the f.21v readers agreed 0.83-0.88 on the same sheet;
a sheet with the barred 8, the dot groups and the plain triangle drawn in would remove most of this pass's splits).

Requests this job: gallica.bnf.fr 16 (9 overviews, 1 info.json, 4 regions, 1 HTTP 500 retried once after 8 s, 1 iiif_lines
region; 10 ContentSearch), de-crypt.org 3, github.com 2 shallow clones, web search 4. Subagents: 3 Sonnet calls (2 passes +
1 adjudication).

## f.117r (no.77, 13 Mar 1572): first test under the printed 1572 key (NEVBIR-3252-B, 2 Oct 2026)

Brief `.claude/briefs/runs/2026-10-02-acct3-nevbir-3252-b.md`. Folder `harvest/f117/`.

**Crops** (command pasted before any subagent call; the profile detector found 9 of the 10 lines and drifted from line 6,
so the centres were set by eye on its debug overlay, and a new `--bottom-margin` option was added to the shared tool
because fixed bands clipped the descenders -- offline test `tools/tests/test_iiif_lines.py` 3c):
`python3 tools/iiif_lines.py --ark btv1b9060232m --canvas 118 --region 4380,1400,3150,1300 --out ciphers/birago-fr3252-1571-72/images/f117 --prefix f117 --centres 103,223,347,462,580,702,815,944,1062,1210 --max-width 1100 --overlap 60 --debug`
(fetched once; the cut was re-run from the local file with `--image ... --top-margin 15 --bottom-margin 45`). 10 lines x 3
segments; debug overlay `images/f117/f117_lines_debug.jpg` checked by eye (one band per line, block complete: 10 lines,
not ~13 as the overview estimate said); 2x reader copies in `images/f117/lines2x/` (gitignored, regenerable).

**Blind passes.** Two value-blind Sonnet readers (`harvest/f117/blind_pass_brief_f117.md`, copied from the 1572 group's brief;
`sign_sheet_blind_1572.png`; reader B read the lines in reverse order): `passA.tsv` 279 signs, `passB.tsv` 278. Value-blind
reconciliation (`../ceppo-nevers-fr3251-1570s/harvest/reconcile_blind.py`): 281 aligned, **211 agreed (0.75)**. Most splits are
systematic class pairs (hash T60/T86 x16, the two x forms T83/T81 x17, barred p T95/T51 vs T65 x14, barred vs plain loop-on-
stem T90/T45 x6, phi T98/T18 x3). **Reconciliation:** no third subagent (account 2 at `allowed_warning`, flagged in ROOM.md
22:13); this worker settled the 70 rows from the native crops against the sheet before any decode (`harvest/f117/settle_f117.py`,
rules in its docstring; caveat there: this worker had seen part of the 1572 map while setting up, so it is one eye, not a
blind third reader). Structural: L03's plain digits "8 5" are one sign, cell T11 (word code 85). Result
`recon_f117_final.tsv`: **277 signs, 251 keyed, 26 unkeyed (25 X_, 1 '?')**. Measured two-reader error used for the power
control: 1 - 0.75 = **0.25** (agreement, not accuracy; LESSONS.md "Look-alike pass").

**Test** (`harvest/f117/run_tests.sh 0.25`: `decode_control.py --corpus fr` = fr16 Catherine de Medicis letters, 200 value-
shuffled keys, power control 20 fr16 windows at err 0.25, seed 1; judge `specs/birago-fr3252-f117.json` (fr) with
`shuffled_judge.py`, 20 shuffled-target decodes):

| key variant | real key | shuffles mean (sd) / max | z | rank /201 | power, err 0.25 | judge real | shuffled-target judge |
|---|---|---|---|---|---|---|---|
| printed 1572 (Tomokiyo) | -1.3782 | -1.7757 (0.143) / -1.3732 | 2.77 | 2 | 11/20, z med 2.58 | -1.466 FAIL | 0/20 pass (max -1.744) |
| T42 = m (pre-registered; T42 does not occur here) | -1.3782 | -1.7721 / -1.3805 | 2.74 | 1 | 12/20 | -1.466 FAIL | 0/20 |
| clerk sheet C variant (T42 m, T50 s, T95 l; NEVBIR-87ALIGN) | -1.3640 | -1.7669 / -1.3927 | 2.78 | 1 | 12/20 | FAIL | 0/20 (max -1.788) |
| T88 = q (fitted on this letter, post-hoc) | -1.3337 | -1.7728 / -1.3739 | 3.09 | 1 | 13/20 | -1.406 FAIL | 0/20 (max -1.747) |
| printed key, Italian corpus it16dip (language check) | -1.4705 | -1.5762 / -1.2112 | 0.66 | 53 | 3/20 | -- | -- |

judge thresholds (fr, N=269): real_p05 -0.901, null_p99 -1.853. `--fit-sign T88 --fit-values q`: q is the best single letter
for T88 (-1.334; l -1.353, p -1.357; as printed g -1.378) -- the 1572 table has no q, and the g-signs read where French
needs q ("ce qui", "quelqu'un"); T70/T76/T66/T42 do not move to a letter.

**Verdict for this test: the language is French, not Italian; the n-gram test does not license the reading at this
reader error, and this is not a negative.** The printed key beats the mean of 200 shuffled keys by z 2.8-3.1, but the best
shuffled key comes within 0.01-0.04 of it, and at the measured 0.25 error the same key on real French of this length ranks
first in only 11-13 of 20 windows. The judge FAILs on every variant, well below real_p05, with 0 of 20 shuffled-target
decodes passing (not a non-test). What would settle it is a lower reader error. Most of the 25% is class confusion of a few
look-alike pairs, which a look-alike pass with the 1572 group's confusion map (`../nevers-birago-fr3251-1572/harvest/confusion_1572.tsv`)
or a blind third reader would cut. After that, re-run this table.

**Decode (printed key + T88=q, `harvest/f117/reading_f117_T88q.txt`); not a licensed reading:**
```
L01 ___mquilam_uelqunn_psnnua_arde
L02 sannintentiondeconuenibauns__
L03 poursuoibsngounbne_entsecarmagnolappi_b
L04 cequisnstperso_equisernndroit
L05 _susfaciheets_insele_ertou_es_es
L06 sionsdestre_lusenpsbnihespeieec
L07 quec_deuantinuoussu_sinda_snb
L08 et_auorisercesta_airesiseneett
L09 _esoingetsisuoussnmbsetantquis
L10 reusisn_quello__
```
**Grades (printed key): 277 signs; H 0, C 0, S 0, M 251, I 0, U 26** (25 off-sheet X_ and 1 unread). No S, because the control
does not license the key at this error. Of the 251 M tokens, 188 sat at two-reader agreement H.

**English gist of the readable fragments (M, a gist only, not a translation):** "...that he has ... someone (quelqu'un) ...
[the] intention to agree (de convenir) ... pursue ... Carmagnola ... that which is ... [the] person ... and who will be ... [in that]
place (endroit) ... to facilitate ... [some]thing ... before us (devant nous) ... and to favour these affairs (et favoriser ces
affaires) ... the need (besoing), and if you ... and as much as (et tant que) ... quello [word code]". It concerns Carmagnola
and an agreement or arrangement to be favoured. Nothing beyond these fragments is claimed.

Requests this job: gallica.bnf.fr 3 (one f.118 region fetched and then superseded by a wider one; one f.48 region with the top
moved up). Subagents: 2 Sonnet calls (passes A and B); no third reader.

## f.47r (no.30): re-cut with line 2 (NEVBIR-3252-B, 2 Oct 2026)

Crop fault fixed, from a new native region with the top moved up 100 px so line 1's right end is not at the edge:
`python3 tools/iiif_lines.py --ark btv1b9060232m --canvas 48 --region 4830,2560,3400,2040 --out ciphers/birago-fr3252-1571-72/images/f47/recut --prefix f47r --centres 190,290,400,510,640,750,850,960,1080,1200,1300,1410,1520,1640,1760,1870,1980 --max-width 1200 --overlap 60 --follow-slope 400 --slope-local --slope-margin 20 --debug`
**17 lines x 3 segments**, each band on its own line (checked by eye on L01 s1/s3, L02 s1/s3, L03 s3, L16 s3, L17 s1/s3).
Line 2 is now its own band. L17 s3 is prose only ("...scriue esser capitate..."). Eye-set left-edge centres stopped the
slope tracker locking two bands on line 1 (the NEVBIR-3252 fault); `--overlap 0` was not used. Blind passes were **not run**:
account 2's rate limit read `allowed_warning` at 22:13 UTC and this job started no new subagents beyond f.117's two. The crops are
ready for the next worker, together with the CEPPO-SPLITS look-alike shapes as the known answer.

## Remaining gaps (NEVBIR-3252-B, 2 Oct 2026)
Read so far: 0 tokens graded S or better of about 1,980 cipher signs. f.117r: 277 signs decoded, all M/U, not licensed; f.47r: 157 signs tested, not licensed.
- f.117r reader error 0.25 - blocker: not-attempted; no third reader this job (rate limit allowed_warning); next: look-alike pass on the T60/T86, T83/T81, T95/T51/T65, T90/T45 tiles using the 1572 confusion map, or a blind third reader, then re-run harvest/f117/run_tests.sh at the new error, ~$3
- f.117r T88=q - blocker: not-attempted; fitted post-hoc on this letter only; next: test T88=q pre-registered on another French or Italian 1572 leaf with q-words, disk only, ~$1
- f.47r lines 2 and 5-17 (~690 signs) - blocker: not-attempted; re-cut done (images/f47/recut, 17 lines x 3); next: two blind passes in 3-4 line chunks + reconciliation against the Ceppo sheet with the CEPPO-SPLITS shapes as known answer, then re-run decode_control on the whole block, ~$10
- f.47r reader error 0.44 - blocker: not-attempted; sheet lacks three forms the readers saw; next: add the barred 8 / dot-group / plain-triangle forms to the sheet before the next passes, ~$2
- f.100r (~800 digits, Nov 1571 numerical system, no key) - blocker: no-key-material; f.119's system is unread (Bourdeau closed-negative at 483 digits); next: pooled with f.119 under BIRAGO-NUM (queued 2 Oct 2026)

## Escalation (NEVBIR-3252-B, 2 Oct 2026)
- [x] siblings: fr.3252 f.36-37 witness and the fr.3251 1572 group's sheet, maps, clerk key and controls used
- [x] clear-pages: neighbours and facing pages of all three viewed; no clear copy or slip (Premise check (c))
- [x] known-keys: Ceppo-Nevers on f.47r (tested), 1572 key on f.117r (tested: French, z 2.8-3.1, not licensed at 0.25), Nov 1571 system has no key
- [x] print: Gomberville 1665 both parts searched inside; no Birago letter of 1571-72
- [ ] key-rebuild: T88=q pre-registered test on another leaf; f.100r + f.119 pooled (BIRAGO-NUM)
- [x] image-check: f.117r native crops, 10 lines; f.47r native re-cut with line 2
- [ ] retry: f.117r at lower reader error; f.47r whole block
Verdict: keep going: 4 internal gaps; cheapest next: f.117r look-alike pass + re-run, ~$3
