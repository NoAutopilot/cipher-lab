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

## f.100r (no.67, 8 Jan 1572): transcription and pooled design analysis with f.119 (BIRAGO-NUM, 2 Oct 2026)

Brief `.claude/briefs/runs/2026-10-02-acct3-birago-num.md`. Working files in `num/`. Prior work cited, not re-derived:
D. Bourdeau, cyphersolver `targets/birago/NOTES.md` (16 Sept 2026; code MIT, text CC BY 4.0) -- his glyph-level f.119
transcription is copied unchanged, credited, as `num/f119_ct2_bourdeau.txt` (`num/f119_ct2_bourdeau.SOURCE`), and his
exclusions (prefix/suffix codes, structured homophony, polyphonic figures; annealer below unicity at 228 tokens / 62
symbols) stand as he wrote them.

**Crops** (command pasted before any subagent call, Usage 6):
`python3 tools/iiif_lines.py --ark btv1b9060232m --canvas 101 --region 4380,2950,3700,1500 --out ciphers/birago-fr3252-1571-72/images/f100 --prefix f100 --max-width 1900 --overlap 0 --debug`
-> 13 bands, fixed-y (no --follow-slope; the NEVBIR-3252 merge fault avoided); debug overlay checked by eye: L01 = the
clear line ending "harebbe a caro 76÷4005...", L02-L11 the cipher, L12-L13 clear (deleted). Both readers found the s2
segments clip the sloping right end of several lines and read those ends from the cached native source strip
(`images/f100/src_*.jpg`, the same fetch), deskewed about 1.9 degrees. Tool note (one line, not done here): a fixed-y cut
of a 3700 px line that rises ~120 px needs --follow-slope or a narrower --max-width.

**Transcription.** Notation = Bourdeau's ct2 for f.119 (digits; a mark appended to the digit it sits over: `.` dot,
`:` two dots; `|` the inline wavy sign; letters as written), so the two letters are in one notation (rule 3); the
dotted 1 is kept as `i` (Bourdeau folds it into 1; `num/parse.py` reads `i` as 1). Two blind Sonnet passes
(`num/f100_passA.tsv`, `num/f100_passB.tsv`, brief `num/f100_pass_brief.md`; B read the lines in reverse order),
one reconciliation by this worker from native zooms of the 6 disputed spots (`num/f100_disagreements.tsv`, all settled
for pass A: L03 8., L04 4. i i 0., L10 8. dots seen; L01/L02 i vs 1 is the same figure). Result `num/f100_recon.txt`:
**565 digits** (539 unmarked-or-dotted-1, of which 23 dotted 1s; 26 dot-marked), **15 letters** (m 7, n 4, h 2, f 2),
2 wavy signs, 1 clear phrase ("Io dico la pura et mera uerità", L08) splitting two runs. **Two-reader error: 8 of 585
aligned positions (1.4%), all on a dot or on i/1; zero disagreements on a digit value.** Caveat: this is agreement, not
accuracy (LESSONS.md "Look-alike pass"), and both readers worked from the same native strip under one brief. One open
reading: L08 "...3 8 0 7 6 [7] 7 6 CLEAR" -- both read the middle sign as 7; by eye it is a 7-like stroke without the wavy
sign's dots, possibly the wavy sign itself (f.119 brackets with ÷76); graded M.
Run delimiters match f.119: run 1 opens "76 ÷" and closes "...380 76 ? 76"; run 2 opens "÷ 70 89..." and closes "...30 76 ÷"
(f.119: "÷76 ... ÷76").

**Design findings** (`num/analyze.py` -> `num/analyze_out.txt`; `num/phase.py`; every number beside its control):

1. *Dotted two-digit code groups (structural, both letters).* In f.100r a dot sits over both figures of a
   two-digit group: of 23 dotted 1s, 21 stand next to another dotted figure, while 63 other 1s are undotted; the dotted
   tokens form 24 runs, 20 of them exactly two long (2. i = 21, 4. i = 41, i 8. = 18, i 0. = 10, 2. 5. = 25, i 9. = 19;
   one 4-run 4. i i 0. = 41 10, one 3-run i 0. 5: ). Control: the same number of dots placed at random digit positions,
   2,000 draws, gives a mean of 3.4 even-length runs (p99 8, max 10) against **21** observed. This is the convention
   Tomokiyo describes for Nevers key no.7 (1586, `sources/cryptiana/web/nevers.htm`: "A dot should be put over a
   two-digit figure"), and it is how Tomokiyo transcribed f.119 (":41 :41 :25 :36 ..." as two-figure groups).
   Checked by eye on f.119 (Bourdeau's `cipher_full.png`): both of Bourdeau's "4. 1" are a dotted 4 followed by a
   dotted i, i.e. the same dotted group 41 as f.100r. Shared marked groups across the letters: 41 (dotted, both), 25
   (marked, both), 21 (dotted in f.100r, crossed in f.119). Bourdeau's single-digit reading of the marks (and so his 75
   pairings) does not hold for the dotted marks; his maxw=2 spans happen to include the right pairs.
2. *Bourdeau's 75-pairing count is not a design test.* With the wavy sign ignored, 200 of 200 draws that put f.119's 16
   marks at random digit positions also admit a segmentation (f.100r: 13,692 segmentations, control 200/200). A
   random-digit-VALUE control would be identical by construction (parity depends on mark positions only; rule 3
   orthogonal-control paragraph), so the position control was used. With the wavy sign as a hard break f.119 has 0
   segmentations (control 15-34% have one): weakly against the wavy sign as a token boundary.
3. *Even-pair parity does not hold for f.100r either way.* With the dotted pairs as code groups, letters dropped and
   the wavy sign as a break, 16 of 27 plain runs are odd (letters as breaks: 24/42; dropping any one digit as a
   single-sign token: best 11/27, digit 4; line ends as breaks: 22/36). The letter stream is not a clean two-digit
   stream between the marked groups: stray single digits (or unmarked codes) exist. `phase.py` models this.
4. **Same key in both letters.** Plain-digit streams (letters out, marked figures in): **21 shared 6-mers** between
   f.119 and f.100r against a shuffled-f.100 null of mean 0.93 (p95 3, max 5, 200 draws); 8 shared 7-mers (null max 2),
   4 shared 8-mers (null max 1), one shared 10-mer `1503985803` (f.119 L4 "...4 0 3 1 5 0 3 9 8 5 8 0 3 4...", f.100r L07
   "1 5 0 3 9 8 5 8 0 3 9 5..."). Residual digit-bigram profile (observed minus unigram expectation) **r = 0.728**
   against a shuffled null p95 0.259 -- higher than each letter's own half-vs-half r (f.119 0.526, f.100r 0.577).
   Matched power control (synthetic Italian, 240+280 letters, two-digit homophonic over the 64 cells without 6/7, 30
   trials per row): one key vs two keys -- 30 cells: shared 6-mers 20.2 (11-36) vs 1.1 (0-4), r 0.758 vs 0.003 (max
   0.274); 40 cells: 7.8 vs 0.9, r 0.574 vs -0.022; 62 cells: 4.1 vs 1.7, r 0.086 vs 0.008. The observed pair (21,
   0.73) lies inside the one-key band at about 30 cells and outside every two-key trial (max 8 shared 6-mers, max r
   0.52). Conclusion at S grade (cryptanalytic, controlled): f.100r is in the same key as f.119, and the key's letter
   table is far less homophonic than Bourdeau's 62-symbol pairing implied (his figure includes phase errors).
5. *Design prior* (`tools/design_prior.py --no-write num/pooled_pairs_only.txt`, `num/design_prior_out.txt`): multi-sign
   class plausible (d 0.18, envelope 0.47, null p05 0.42), code excluded; nearest key on file the Nevers-Birago 1572
   clerk table (homophonic, d 0.12).
6. *Phase recovery* (`num/phase.py`): hard-EM Viterbi cutting each plain run into pairs or stray single digits.
   Control first (synthetic Italian, 520 letters, 5% stray digits, 3 seeds each): phase accuracy 0.97-0.99 at 30
   cells, 0.91-0.98 at 40, **0.66-0.78 at 62**. Target (pooled 48 runs, 985 plain digits): 476 pairs, 64 types (7
   hapax), 33 strays, H 5.49 bits -- between the 40-cell (5.2) and 62-cell (5.85) controls, and the type count moves
   64-71 between seeds (the 30-cell controls are stable), so the target's phase is not settled; expected phase error
   roughly 10-30%. Output `num/pooled_tokens.txt`, spec `specs/birago-num-pooled.json`.

**Family run (rule 3, `tools/family_run.py`, both rows in `../birago-nevers-1571/HYPOTHESES.md`):**

| run | control (N=476, K~60, it16dip, profile=target) | target | verdict |
|---|---|---|---|
| homophonic, clean control, 3 seeds x 8 restarts | **0.896** (0.809-0.960), gate 0.6 met | best -1191.3 (-2.50/token vs control -2.13..-2.28); judge it: **FAIL** -1.272 vs real_p05 -0.959 (null_p99 -1.77) | the decode does not read (LM attractors "merito", "amato", as in Bourdeau's runs); not licensed |
| homophonic, control noise 0.25 (the phase error the target likely carries) | **0.249** (0.195-0.311), below gate | not run | at the target's probable phase error this family has no power |

**Verdict: no reading; not a negative.** The clean-control FAIL is conditional on a segmentation whose own control says
it is 66-90% right at this K; the noise-matched control falls below gate, so the target FAIL is a non-test of the key
(rule 3, error-bracketing paragraph). What moved: f.100r is in f.119's key (controlled), the dotted marks are two-figure
groups (controlled), and the pooled letter stream is ~476 pairs with roughly 30-50 effective cells. What would settle
it: an instrument that does not fix the phase first -- a joint phase+key anneal (each run's cut points resampled under
the key's current n-gram score, stray digits as nulls), controlled at N=476 with 5-10% strays at 40-60 cells -- or a
crib from the clear text around both runs (Carmagnola, Bellagarda, la Valletta, Sua Maestà; f.100r's clear text on the
same leaf names "Monsignor di Bellagarda", "la Valletta", "Carmagnola", "Giulio Centurione", "il Maresciale di logis").
No grade is assigned to any token (no reading). Novelty not classified (rule 10).

Requests this job: gallica.bnf.fr 2 (IIIF region of canvas 101, one superseded by a taller region); github.com 1
shallow clone (dbourdeau/cyphersolver, scratch, not committed beyond the credited ct2 copy). Subagents: 2 Sonnet calls
(passes A and B); reconciliation by this worker (6 positions).

## f.119 + f.100r: pre-registered crib drag (BIRAGO-NUM2, 2 Oct 2026)

Brief `.claude/briefs/runs/2026-10-02-acct3-birago-num2.md`. Files in `num/crib/`. The rules (cribs, where to drag, score,
null, accept threshold, power control) were written and pushed in `num/crib/PREREG.md` (commit e8633359) before any crib
was scored. Prior work cited: Bourdeau's f.119 transcription (cyphersolver `targets/birago`, MIT / CC BY 4.0), as in
BIRAGO-NUM.

**Method** (`num/crib/crib_drag.py`). Twelve cribs (carmagnola, bellagarda, bellegarda, ualletta, sauoia, turino, duca,
regina, ugonotti, centurione, maresciale, maesta; v->u) were dragged over every pair offset of the pooled phase.py stream
(both letters together, 61 runs, 473 pairs). A placement is admissible when no code stands for two letters. Each
placement was scored by applying its induced key to both letters: the sum of it16dip bigram PMI over every adjacent pair
elsewhere whose two codes it fixes. The statistic is the best placement's score. The null is the same statistic over 200
streams with the pair tokens permuted (run structure kept). A placement is accepted only if it beats all 200.

**Power control first** (rule 3; `num/crib/control_power.txt`). Synthetic it16dip text, 476 pairs, one homophonic key,
5% stray digits, phased by the same `phase.em`, crib inserted, 10 trials, 100 permutations:

| cells | copies | carmagnola (10) | ualletta (8) | turino (6) | duca (4) | maresciale / centurione / bellagarda (10) |
|---|---|---|---|---|---|---|
| 40 | 1 | accepted 3/10 | 0/10 | 0/10 | 0/10 | 0, 0, 0 /10 (wrong placement accepted 1, 1, 1) |
| 40 | 2 | 5/10 | 0/10 | 1/10 | 0/10 | - |
| 30 | 1 | 4/10 | 0/10 | 1/10 | 0/10 | - |
| 30 | 2 | 4/10 | 1/10 | 2/10 | 0/10 | - |
| 55 | 1 | 0/10 (wrong 1) | - | - | - | 0, 1, 1 /10 (wrong 1, 0, 2) |

Reading of the control: a 10-letter crib that sits in the text intact is accepted 0-50% of the time. A crib of 8 letters
or fewer is accepted 0-20% of the time (duca never). A *wrong* placement passes the accept rule in about 1 trial in 10,
far above the nominal p < 1/201. The cause is that permuting the tokens strips the stream's language structure, so any
placement onto a language-bearing stream beats the null somewhat. In this design the accept rule is weak and
anti-conservative. This applies to the pre-registered rule as written. It is recorded here, not used to rewrite the rule after the fact.

**Target** (`num/crib/crib_target.tsv`, 200 permutations, seed 20261002):

| crib | admissible | real max | null p95 | null max | p | accept |
|---|---|---|---|---|---|---|
| carmagnola | 56 | 5.08 | 6.63 | 10.09 | 0.080 | no |
| bellagarda | 55 | 4.83 | 13.22 | 19.52 | 0.677 | no |
| bellegarda | 56 | 6.44 | 13.39 | 22.37 | 0.537 | no |
| ualletta | 107 | 7.18 | 10.81 | 16.54 | 0.532 | no |
| sauoia | 182 | 3.31 | 6.65 | 7.73 | 0.602 | no |
| turino | 173 | 5.95 | 6.17 | 8.90 | 0.070 | no |
| duca | 284 | 2.39 | 2.55 | 3.85 | 0.080 | no |
| regina | 173 | 7.19 | 8.18 | 10.74 | 0.119 | no |
| ugonotti | 101 | 5.97 | 9.18 | 11.45 | 0.348 | no |
| centurione | 55 | 4.14 | 4.37 | 10.13 | 0.070 | no |
| maresciale | 55 | 5.76 | 5.79 | 9.55 | 0.055 | no |
| maesta | 182 | 10.09 | 7.31 | 8.90 | 0.005 | **yes (pre-registered rule)** |

The one accept, *maesta* at run 52 token 1 (15=m 19=a 43=e 48=a 90=s 94=t), does not survive a post-hoc decoy check
(`num/crib/decoy.py`, `decoy_out.txt`; not part of PREREG's rule, reported as a qualifier). 300 random six-letter it16dip
words dragged the same way reach maesta's score 17 times (5.7%). Run 52 tokens 0-2 is the best placement for 35 of the 300
decoys, and also for regina and bellagarda on the target. It is a hot spot: the two most frequent codes, 15 and 19, sit
beside frequent neighbours, so any word there scores well. That fits the control's 1-in-10 wrong-placement rate. With 12
cribs, about one wrong accept was expected. **No pair value is crib-backed.** No key file was written (writing one at
grade S would over-claim). The six values maesta would fix are below the 8 needed for step 2, so the joint anneal was
**not run** (brief step 2).

**Verdict: no reading; the crib route is a weak test in this design, not a negative.** The cribs may still be in the
text. The control says a 10-letter name in the text is missed 50-100% of the time and a short word almost always. There
is also a premise risk the control cannot cover. In Birago's 1572 key the names are single word codes ("85 carmagnola,
86 turino, 89 bugonotti", f.117r design check above). If the Nov 1571 key works the same way, the names sit in the dotted
two-figure groups (41 x6 in f.100r and x2 in f.119; 25, 21, 18, 10, 19), not spelled out in the letter stream, and no
spelled crib can find them.

**Design note (what would settle it).** (1) The joint phase+key anneal named by BIRAGO-NUM, run without crib seeds. Each
run's cut points are resampled under the key's current score, with stray digits as nulls. Its own control at N=476, 40-55
cells and 5% strays comes first. The family's fixed-phase control already falls to 0.249 at 0.25 phase noise, so the gain
has to come from resampling the phase. ~$6. (2) A crib test that does not use a permutation null. The null should be
decoy words of the same length dragged over the *real* stream, as in `decoy.py`. Several name cribs should be required to
agree on shared codes (joint consistency), and the test calibrated on the same synthetic set. ~$2, disk only. (3) Treat
the dotted groups as nomenclator codes. Their positions against the clear text around each run (f.100r L01 "harebbe a caro
76÷4005...") are the cheapest contextual crib. Dotted 41 recurs in both letters and is the likeliest name or title.

Cost and requests: disk only, no network, no subagents. Novelty not classified (rule 10).

## f.119 + f.100r: joint phase+key anneal (BIRAGO-NUM3, 2 Oct 2026)

Brief `.claude/briefs/runs/2026-10-02-acct3-birago-num3.md`. Files in `num/joint/`. `PREREG.md` and the input
`runs_digits.txt` were pushed in d27489c6 before any control or target run. Prior work cited: Bourdeau's f.119
transcription (cyphersolver `targets/birago`, MIT / CC BY 4.0), as in BIRAGO-NUM.

**Instrument.** This is a new `tools/family_run.py` family, `phased_homophonic` (`tools/families/phased_homophonic.py`,
offline test `tools/tests/test_phased_homophonic.py`). It does not fix the phase first. Each restart starts from the
num/phase.py hard-EM cut. It then alternates two steps. (a) It anneals the key on the current pairs with homophonic_anneal,
seeded with the last key. (b) It re-cuts every digit run by Viterbi under the current key, scoring trigram context plus
log P(pair | letter); stray digits are nulls. The input is 48 runs and 985 digits, phase not fixed; the corpus is it16dip.
In the control, a pair counts as recovered only when both its phase and its letter are right. The settings (16 restarts,
100000/30000 iterations, 8 rounds) were tuned on dev seeds 101 and 102 only (`num/joint/dev_log.md`). That dev work
also found and fixed a miscalibrated objective: with a plain P(pair) prior, the true cut scored below a wrong one.

**Control first** (rule 3). Synthetic it16dip text in the target's own 48 run lengths, 5% stray digits, cells over the
target's own eight digits (no 6 or 7), 3 seeds. The pre-registered gate is a mean of 0.6 at 55 cells:

| cells | seed 1 | seed 2 | seed 3 | mean | role |
|---|---|---|---|---|---|
| 55 | 0.827 | 0.100 | 0.232 | **0.386** | gate (pre-registered): **not met** |
| 40 | 0.912 | 0.090 | 0.934 | 0.645 | curve only, not gating (`num/joint/control_40cells.txt`) |

**Target: not run** (CONTROL BELOW GATE; both rows in `../birago-nevers-1571/HYPOTHESES.md`). Each seed locks into
either the right phase (0.83-0.93) or a whole-stream phase flip (0.00-0.23). On dev seed 101 at 55 cells, the true cut
and key score -2142.9 and the solver's flipped answer scores -2136.5. Those are level, so at ~476 pairs this objective
cannot tell the true phase from the flip; more restarts would not fix that. An anneal given the true cut reads 0.918 on
the same seed (`num/joint/oracle_check.py`). At 40 cells the design reads on 2 of 3 seeds. The target's own pair-type
entropy sits between the 40- and 62-cell controls, and its effective cell count is not known (BIRAGO-NUM).

**Verdict: non-test, not a negative.** This was the third attempt at a key for the Nov 1571 numerical system (fixed-phase
homophonic, then the crib drag, then the joint anneal). By rule 3's third-attempt clause, `phased_homophonic` is
**retired for this hypothesis at this length**, logged as untested-by-this-tool, not refuted. Only new material or a
different instrument reopens it. Instruments not yet tried: (1) a crib test with a decoy null and joint consistency
across several names (BIRAGO-NUM2 design note 2, ~$2, disk only); (2) the dotted two-figure groups read as nomenclator
codes against the surrounding clear text (design note 3). A third letter in this key would raise N, and with it the
objective's power to separate the phases. No token is graded. Novelty is not classified (rule 10).

Cost and requests: disk only, no network, no subagents.

## Remaining gaps (NEVBIR-3252-B, 2 Oct 2026)
Read so far: 0 tokens graded S or better of about 1,980 cipher signs. f.117r: 277 signs decoded, all M/U, not licensed; f.47r: 157 signs tested, not licensed.
- f.117r reader error 0.25 - blocker: not-attempted; no third reader this job (rate limit allowed_warning); next: look-alike pass on the T60/T86, T83/T81, T95/T51/T65, T90/T45 tiles using the 1572 confusion map, or a blind third reader, then re-run harvest/f117/run_tests.sh at the new error, ~$3
- f.117r T88=q - blocker: not-attempted; fitted post-hoc on this letter only; next: test T88=q pre-registered on another French or Italian 1572 leaf with q-words, disk only, ~$1
- f.47r lines 2 and 5-17 (~690 signs) - blocker: not-attempted; re-cut done (images/f47/recut, 17 lines x 3); next: two blind passes in 3-4 line chunks + reconciliation against the Ceppo sheet with the CEPPO-SPLITS shapes as known answer, then re-run decode_control on the whole block, ~$10
- f.47r reader error 0.44 - blocker: not-attempted; sheet lacks three forms the readers saw; next: add the barred 8 / dot-group / plain-triangle forms to the sheet before the next passes, ~$2
- f.100r + f.119 (565 + 483 digits, same key, controlled) - blocker: not-attempted; fixed-phase homophonic a non-test at the phase error (BIRAGO-NUM); crib drag weak by its own control (BIRAGO-NUM2); joint phase+key anneal retired for this hypothesis, control 0.386 at 55 cells below its 0.6 gate, a phase-flip tie in the objective (BIRAGO-NUM3, num/joint/); next: decoy-null joint-consistency crib test (several names agreeing on shared codes, calibrated on the same synthetic set), ~$2

## Escalation (NEVBIR-3252-B, 2 Oct 2026)
- [x] siblings: fr.3252 f.36-37 witness and the fr.3251 1572 group's sheet, maps, clerk key and controls used
- [x] clear-pages: neighbours and facing pages of all three viewed; no clear copy or slip (Premise check (c))
- [x] known-keys: Ceppo-Nevers on f.47r (tested), 1572 key on f.117r (tested: French, z 2.8-3.1, not licensed at 0.25), Nov 1571 system has no key
- [x] print: Gomberville 1665 both parts searched inside; no Birago letter of 1571-72
- [ ] key-rebuild: T88=q pre-registered test on another leaf; f.100r + f.119 pooled (BIRAGO-NUM: same key shown, homophonic run a non-test at the phase error; BIRAGO-NUM2: crib drag weak by control, no crib-backed value; BIRAGO-NUM3: joint phase+key anneal [retired] for this hypothesis, instrument tools/families/phased_homophonic.py, control 0.386 below gate; next decoy-null joint-consistency crib test)
- [x] image-check: f.117r native crops, 10 lines; f.47r native re-cut with line 2
- [ ] retry: f.117r at lower reader error; f.47r whole block
Verdict: keep going: 5 internal gaps; cheapest next: f.117r look-alike pass + re-run, ~$3

## f.117r: blind third reader on the look-alike tiles, 2-of-3, re-test (NEVBIR-117C, 2 Oct 2026)

Brief `.claude/briefs/runs/2026-10-02-acct3-nevbir-117c.md`. Folder `harvest/f117/la/`. Pre-registration `la/PREREG.md`
pushed (ec09c3aa) before either reader ran and before any decode.

**Packet.** `tools/lookalike_pass.py packet --agreement recon_f117_agreement.tsv --confusion ../../../nevers-birago-fr3251-1572/harvest/confusion_1572.tsv --passc recon_f117.tsv --top 10 --crops ../../images/f117 --sheet .../sign_sheet_blind_1572.png --sheet-map .../sign_id_map_1572.json --out la --run f117c`:
130 tiles (66 two-reader splits + 64 agreed tiles whose label sits in a top-10 confusion pair, which covers the Verdict's
T60/T86, T83/T81, T95/T51/T65, T90/T45), 25 candidate cells cut from the blind sheet (ids only). passC was the unsettled
two-reader merge (`recon_f117.tsv`), not the one-eye settle, so NEVBIR-3252-B's settlement did not orient the reader.
**Third reader:** value-blind Opus, one context per half-leaf (L01-L05 77 tiles: H 19 M 55 L 3; L06-L10 53 tiles: H 16 M 30
L 7; no SPLIT), `la/reread_a.tsv`, `la/reread_b.tsv`.
**Rule (fixed before scoring), `lookalike_pass.py reconcile`:** 130 flagged, 40 relabelled, **12 unsettled** (`la/focus.tsv`,
for `tools/sign_sorter.py --focus`), 2-of-3 residual 0.043 (agreement, not accuracy; not used as the power error).
Then `la/fill_unsettled.py`: L03's "8 5" merged into T11 (the NEVBIR-3252-B structural step; T11 is the word cell
"carmagnola" on the printed sheet), and the 2 unsettled tiles still '?' (L02.1, L03.31) took the one-eye label. Result
`la/recon_f117_3r.tsv`: **276 signs, 251 keyed, 25 unkeyed** (off-sheet X_NEW/X_S/X_K/X_EQ and one '?'). It differs from
NEVBIR-3252-B's one-eye settle at 20 tiles (mostly T81->T83, T60->T86, T51/T95->T65, T98->T18) and by one L10 tail sign
the one-eye settle had added.

**Test** (`la/run_tests_3r.sh 0.25`, same tools and seeds as `run_tests.sh`; power at the TWO-READER error 0.25, unchanged):

| key variant | before (NEVBIR-3252-B, one-eye settle): real / best shuffle / z / rank / power | after (2-of-3): real / best shuffle / z / rank / power |
|---|---|---|
| printed 1572 | -1.3782 / -1.3732 / 2.77 / 2 / 11/20 | **-1.3373 / -1.4087 / 3.21 / 1 / 6/20** |
| T42 = m (pre-registered) | -1.3782 / -1.3805 / 2.74 / 1 / 12/20 | -1.3373 / -1.4164 / 3.15 / 1 / 11/20 |
| clerk sheet C variant | -1.3640 / -1.3927 / 2.78 / 1 / 12/20 | -1.3392 / -1.4293 / 3.05 / 1 / 13/20 |
| T88 = q (post-hoc, this letter) | -1.3337 / -1.3739 / 3.09 / 1 / 13/20 | -1.2867 / -1.4094 / 3.60 / 1 / 12/20 |

Judge fr16 (spec `specs/birago-fr3252-f117.json`; real_p05 -0.87, null_p99 -1.798): printed **-1.448 FAIL** (was -1.466),
T88q **-1.382 FAIL** (was -1.406); shuffled-target decodes 0/20 PASS on both (max -1.709, -1.712), so the judge is not a
non-test here. The power-control windows are French (fr); the script's printed label said "it16dip" whatever `--corpus`
was, fixed this job in `../ceppo-nevers-fr3251-1570s/harvest/decode_control.py` (label only, scores unchanged).

**Verdict for this test: every target number moved the same way (real score up 0.04-0.05 on every variant, the gap to the
best of 200 shuffled keys from about 0 to 0.07-0.12, z 2.8-3.1 -> 3.1-3.6, rank 1/201 on all four), and the judge moved
toward real prose but still FAILs far below real_p05. Not licensed, not a negative.** The power control was held at the
two-reader 0.25 by rule, so its 6-13/20 does not credit the third reader: the printed-key row dropping from 11 to 6 at the
same error is most likely the control's own sampling (its windows are drawn at the new letter count, 269 -> 274, so they
are different windows), at 20 windows; it was not re-run with more windows to confirm. A fair power figure at a lower error needs a known-answer measurement of what the 2-of-3
step actually achieves (LESSONS.md "Look-alike pass"). That error has not been measured here.

**Decode (printed key + T88=q, `la/reading_3r_T88q.txt`); not a licensed reading:**
```
L01 ___mquilam_uelqunnturinopsnnua_arde
L02 sannintentiondeconuenibaund__
L03 poursuoirsegouerne_entdecarmagnolapp__b
L04 cequisestperso_equiserendroit
L05 _susfaciheets_insete_ertou_es_es
L06 sionsdestre_tusenpsrnihespeieec
L07 quec_deuantinuoussu_tinda_snb
L08 et_auorisercesta_airesiteneett
L09 _esoingetsituoussnmbtetantquit
L10 reusisn_quello_
```
**Grades (printed key): 276 signs; H 0, C 0, S 0, M 251, I 0, U 25.** No S, because the judge FAILs and power is below 15/20.
Transcription confidence: 181 tiles H, 92 M, 3 L.

**English gist of the readable fragments (M, a gist only):** "...that he ... someone ... [the] intention to agree (de convenir)
... to pursue (poursuivre) ... [the] government (gouvernement) of Carmagnola ... that which is ... [the] person who will go
straight (se rend droit) [there] ... to facilitate ... before us (devant nous) ... and to favour these affairs ... the need
(besoing), and if you ... and as much as ... quello". The third reader's labels bring in "poursuivre", "gouverne[ment]" and
"ce qui est ... qui se rend droit". The letter concerns the government of Carmagnola and an agreement to be favoured.

Subagents: 2 Opus calls (third reader, one per half-leaf). Network requests: none. f.47r passes not run this job (budget).

## Remaining gaps (NEVBIR-117C, 2 Oct 2026)
Read so far: 0 tokens graded S or better of about 1,980 cipher signs. f.117r: 276 signs decoded at 2-of-3, all M/U, not licensed (z 3.2, rank 1/201, judge FAIL); f.47r: 157 signs tested, not licensed.
- f.117r measured error after the 2-of-3 step - blocker: not-attempted; the 2-of-3 residual is agreement, not error, so no figure exists yet; next: power control at a known-answer error for the look-alike step (LESSONS.md "Look-alike pass" no.87 figure) with 100 windows instead of 20, disk only, ~$1
- f.117r 12 unsettled tiles - blocker: not-attempted; the third reader marked them L or split from both readers, so they are written as sign-sorter focus rows (harvest/f117/la/focus.tsv); next: tools/sign_sorter.py --focus harvest/f117/la/focus.tsv
- f.117r T88=q - blocker: not-attempted; fitted post-hoc on this letter only; next: test T88=q pre-registered on another French or Italian 1572 leaf with q-words, disk only, ~$1
- f.47r lines 2 and 5-17 (~690 signs) - blocker: not-attempted; re-cut done (images/f47/recut, 17 lines x 3); next: two blind passes in 3-4 line chunks + reconciliation against the Ceppo sheet with the CEPPO-SPLITS shapes as known answer, then decode_control on the whole block, ~$10
- f.47r reader error 0.44 - blocker: not-attempted; sheet lacks three forms the readers saw; next: add the barred 8 / dot-group / plain-triangle forms to the sheet before the next passes, ~$2
- f.100r + f.119 (565 + 483 digits, same key, controlled) - blocker: not-attempted; fixed-phase run a non-test and crib drag weak by control (BIRAGO-NUM/NUM2); next: joint phase+key anneal with its own control at N=476, 40-55 cells, 5% strays, ~$6

## Escalation (NEVBIR-117C, 2 Oct 2026)
- [x] siblings: fr.3252 f.36-37 witness and the fr.3251 1572 group's sheet, maps, clerk key, confusion map and controls used
- [x] clear-pages: neighbours and facing pages of all three viewed; no clear copy or slip (Premise check (c))
- [x] known-keys: Ceppo-Nevers on f.47r (tested), 1572 key on f.117r (tested twice: z 2.8 one-eye, 3.2 at 2-of-3; judge FAIL), Nov 1571 system has no key
- [x] print: Gomberville 1665 both parts searched inside; no Birago letter of 1571-72
- [ ] key-rebuild: T88=q pre-registered test on another leaf; f.100r + f.119 joint phase+key anneal
- [x] image-check: f.117r native crops, 10 lines; f.47r native re-cut with line 2
- [ ] retry: f.117r done at 2-of-3 (NEVBIR-117C); power at a measured post-look-alike error not run; f.47r whole block
Verdict: keep going: 6 internal gaps; cheapest next: f.117r power control at a known-answer look-alike error, ~$1

## Scout for a third letter in the Nov 1571 numerical key (BIRAGO-NUM-SCOUT, 2 Oct 2026)

Brief `.claude/briefs/runs/2026-10-02-acct3-birago-num-scout.md`, after BIRAGO-NUM3 retired the joint anneal at 985 digits.
Both BnF finding aids were read in full (fr.3251 `ark:/12148/cc49712p`, fr.3252 `ark:/12148/cc49713x`, 2 Oct 2026). Every
Birago<->Nevers letter dated Sept 1571-Mar 1572 that BIRAGO-POOL.tsv did not already list was viewed at 1400-px Gallica overview
(canvas = folio + 1 in both volumes, confirmed on the ink foliation of every canvas viewed). That was 13 Birago letters (fr.3251 f.3,
f.91, f.95, f.98, f.100, f.117; fr.3252 f.70, f.81, f.86-89, f.109, f.113, f.115, plus f.107v-108r in the gap where the finding aid
has no no.72) and 2 Nevers-side letters to Birago (fr.3252 f.105 copy of 9 Feb 1572, f.119-120 of 28 Mar 1572). **None carries
cipher.** None shows digit runs, m/n/h/f modifiers, the divide sign or superscript crosses. No native fetch was needed. In this window the only
cipher letters in the two volumes are the ones already on file: fr.3251 f.119 (13 Nov 1571), fr.3252 f.100r (8 Jan 1572), fr.3251
f.138 (7 Feb 1572) and f.144 (27 Mar 1572) (Nevers-Birago 1572 folder), and fr.3252 f.117r (13 Mar 1572, a symbol cipher).
Rows are in `../nevers-birago-fr3251-1572/BIRAGO-POOL.tsv`. Not covered: other volumes (the Guazzo letters in fr.4688, Dec 1571-Apr 1572,
are in the pool already but are not on Gallica), and whether f.138 (7 Feb 1572) is in the 1572 key or the numerical key. That
assignment comes from Tomokiyo and the 1572 folder, and this scout did not re-test it. Suggestion only: f.138's digit shape against
f.100r/f.119 is the cheapest remaining in-volume check for more numerical-key text. Requests: gallica.bnf.fr IIIF 33, archivesetmanuscrits.bnf.fr 2.

## f.47r (no.30, 26 Apr 1571): whole letter, two blind passes, decode under the printed Ceppo-Nevers key (NEVBIR-47, 2 Oct 2026)

Brief `.claude/briefs/runs/2026-10-02-acct3-nevbir-47.md` (account 2 for the account-3 orchestrator). No class, no novelty wording.
Crops: the NEVBIR-3252-B re-cut (`images/f47/recut`, 17 lines x 3 segments), no new network request (0 Gallica requests).

**Blind passes.** Two value-blind Sonnet readers, one call each over all 51 crops, brief `harvest/f47/blind_pass_brief_47.md`:
the printed sheet plus three reference tiles cut from the fr.3252 f.36r/v period-gloss witness under neutral names
(`harvest/f47/ref/ref_W1-3.jpg`, from `../ceppo-nevers-fr3251-1570s/harvest/f21v/lookalike/witness_crops/`). The tiles stand for the
CEPPO-SPLITS shape rule as extra cells: `X_DSLASH` (diagonal slash, a dot each side; glossed n x5), `X_DCARET` (caret/lambda with a
dot; glossed n x3), S97 (curled lambda, no dot; glossed a). Also offered: `X_TRI` (plain triangle) and `X_DOTS` (dot group), the
forms NEVBIR-3252 found missing from the sheet. Results: `passA.tsv` 785 signs (63 X_, 0 '?'), `passB.tsv` 814 signs (42 X_, 0 '?').
Both readers said the crops are small and dense. Neither marked any row H, and neither quoted the prose words at run edges.
Reader B never used X_DSLASH and put the same form under S49 (31 rows), which has the same value under the rule.
The account's rate limit read `allowed_warning` at 23:47 UTC, after both passes had started. No third (reconciliation) subagent was
started, so the reconciliation is script-only and leaves nothing settled by eye.

**Reconciliation** (`../ceppo-nevers-fr3251-1570s/harvest/reconcile_blind.py`; this job added the extra cells to its look-alike
pairs). Raw: 829 aligned, 550 agreed (**0.66**), 279 unsettled -> `recon.tsv` 771 signs, 220 '?'. Normalized (X_DSLASH -> S49,
X_DCARET -> S23 in both passes before alignment, the CEPPO-SPLITS rule, which leaves both values n): 830 aligned, 573 agreed
(**0.69**), 257 unsettled -> `recon_norm.tsv`. The 257 unsettled positions are written as sign-sorter focus rows
(`harvest/f47/focus.tsv`, for `tools/sign_sorter.py --focus`). None of them blocks the next step.

**Test** (`decode_control.py SEQ --shuffles 200 --windows 20 --err E --extra X_THETA2=r [--extra X_DSLASH=n --extra X_DCARET=n]`,
corpus it16dip). E is the measured two-reader disagreement (0.34 raw, 0.33 normalized), never a look-alike residual:

| run | signs / letters | real key | shuffled mean (sd) | shuffled max | z | rank | power at E (20 windows) |
|---|---|---|---|---|---|---|---|
| recon, seed 1 | 771 / 582 | -1.4609 | -2.0608 (0.178) | -1.5529 | 3.38 | **1/201** | 19/20, z median 4.77 (min 1.78) |
| recon, seed 2 | 771 / 582 | -1.4609 | -2.0915 (0.149) | -1.6043 | 4.24 | **1/201** | 20/20, z median 4.65 (min 3.72) |
| recon, seed 3 | 771 / 582 | -1.4609 | -2.0743 (0.151) | -1.5778 | 4.05 | **1/201** | 20/20, z median 5.21 (min 2.99) |
| recon_norm, seed 1 | 770 / 605 | -1.4228 | -2.0521 (0.157) | -1.6166 | 4.02 | **1/201** | 19/20, z median 5.22 (min 2.85) |
| pass A alone (information) | 785 / 806 | -1.5525 | -2.0820 (0.117) | -1.7410 | 4.52 | 1/201 | 20/20 |
| pass B alone (information) | 814 / 826 | -1.4237 | -2.0687 (0.140) | -1.6062 | 4.62 | 1/201 | 20/20 |

The first 157 signs gave z 3.49, a 0.004 margin over the shuffled maximum and power 9/20. Over the whole letter the printed key ranks
first in every run, with a margin of 0.09-0.19 over the best of 200 shuffled keys. The power control at the measured error now
reaches 19-20/20, so the key test is control-backed. **The printed Ceppo-Nevers key is the key of f.47r (S, cryptanalytic, with
control).** Caveat: the control's error is random replacement, while the readers' errors are look-alike swaps, and the 0.33-0.34 is
disagreement, not accuracy.

**Judge** (`python3 tools/judge_plaintext.py specs/ceppo-nevers-fr3251-1570s.json --file ciphers/birago-fr3252-1571-72/harvest/f47/reading_<run>_letters.txt`, pasted):
```
recon: FAIL language: score=-1.525, null_p99=-1.773, real_p05=-0.921, real_median=-0.83, mode=both, N=582
passA: FAIL language: score=-1.563, null_p99=-1.78, real_p05=-0.908, real_median=-0.827, mode=both, N=806
passB: FAIL language: score=-1.45, null_p99=-1.777, real_p05=-0.912, real_median=-0.83, mode=both, N=826
FAIL - ceppo-nevers-fr3251-1570s (a PASS is a gate for a verifier, not a reading; rule 10)
```
All three are above the null p99 and well below real p05, which is what about a third of signs misread would produce. **The text is
not a reading. No token is graded above M** (0 H, 0 C, 0 S, all decoded letters M, '?' positions U).

**Readable fragments (M, English gist only).** Pass A L10 "molto tempo" (a long time); L07 "sempre" (always); L14 "ultim[am]ente"
(lately); L04/L05 "quali/quale" (which); L05 "furono" (they were); L13 "nemi[co]" (enemy); L06 and L08 both end "...del fin et le"
or "Delfin[o]" (the end, or the Dauphin), unresolved; L10 "nos[tro]" (our). These are word islands in noisy letters, not sentences.
Files: `harvest/f47/reading_{recon,recon_norm,passA,passB}.txt`.

Requests this job: 0 network. Subagents: 2 Sonnet calls (passes A and B). No third call (rate limit `allowed_warning`).

## Remaining gaps (NEVBIR-47, 2 Oct 2026)
Read so far: 0 tokens graded S or better of about 1,980 cipher signs. The Ceppo-Nevers key is control-backed for f.47r (z 3.4-4.6, rank 1/201 in every run, power 19-20/20 at 0.33-0.34), but the text is not: 771 signs decoded, all M/U, judge FAIL. f.117r: 276 signs, all M/U.
- f.47r reader error 0.33 - blocker: not-attempted; two Sonnet passes with no H rows and no third eye (rate limit); next: blind third reader (Opus) on the 257 split tiles of harvest/f47/recon_norm_disagreements.tsv, 2-of-3, then re-run decode_control and the judge, ~$3
- f.47r 257 unsettled tiles - blocker: not-attempted; written as sign-sorter focus rows (harvest/f47/focus.tsv); next: tools/sign_sorter.py --focus harvest/f47/focus.tsv
- f.47r prose/cipher edges - blocker: not-attempted; the readers marked no prose words, so L01-L03 and L17 run edges are unchecked; next: eye-check the s1 crops of L01-L03 and L17 s1-s2 against the passes, disk only, ~$1
- f.117r measured error after the 2-of-3 step - blocker: not-attempted; the 2-of-3 residual is agreement, not error; next: power control at a known-answer look-alike error with 100 windows, disk only, ~$1
- f.117r 12 unsettled tiles - blocker: not-attempted; sorter focus rows (harvest/f117/la/focus.tsv); next: tools/sign_sorter.py --focus harvest/f117/la/focus.tsv
- f.117r T88=q - blocker: not-attempted; fitted post-hoc on this letter only; next: test T88=q pre-registered on another French or Italian 1572 leaf with q-words, disk only, ~$1
- f.100r + f.119 (565 + 483 digits, same key) - blocker: not-attempted; joint anneal retired for this hypothesis (BIRAGO-NUM3); next: decoy-null joint-consistency crib test, ~$2

## Escalation (NEVBIR-47, 2 Oct 2026)
- [x] siblings: fr.3252 f.36-37 witness (gloss shapes as reference tiles), the fr.3251 1572 group's sheet, maps, clerk key and controls used
- [x] clear-pages: neighbours and facing pages of all three viewed; no clear copy or slip (Premise check (c))
- [x] known-keys: Ceppo-Nevers on f.47r whole letter (control-backed, NEVBIR-47), 1572 key on f.117r (z 3.2, judge FAIL), Nov 1571 system has no key
- [x] print: Gomberville 1665 both parts searched inside; no Birago letter of 1571-72
- [ ] key-rebuild: T88=q pre-registered test on another leaf; f.100r + f.119 decoy-null crib test
- [x] image-check: f.117r native crops, 10 lines; f.47r native re-cut, all 17 lines read twice
- [ ] retry: f.47r third reader on 257 split tiles; f.117r power at a measured post-look-alike error
Verdict: keep going: 7 internal gaps; cheapest next: f.47r blind third reader on the split tiles, ~$3
