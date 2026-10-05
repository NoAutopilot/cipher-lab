partial
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
Read so far: 0 tokens graded S or better of about 1,980 cipher signs (unchanged after NEVBIR-47C, 3 Oct 2026). f.117r: 277 signs decoded, all M/U, not licensed; f.47r: 157 signs tested, not licensed.
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
- [ ] key-rebuild: f.47r S74/S54, S80/S65, S76/S91 pair check against the f.36 gloss; T88=q pre-registered test on another leaf; f.100r + f.119 pooled (BIRAGO-NUM: same key shown, homophonic run a non-test at the phase error; BIRAGO-NUM2: crib drag weak by control, no crib-backed value; BIRAGO-NUM3: joint phase+key anneal [retired] for this hypothesis, instrument tools/families/phased_homophonic.py, control 0.386 below gate; next decoy-null joint-consistency crib test)
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
Read so far: 0 tokens graded S or better of about 1,980 cipher signs (unchanged after NEVBIR-47C, 3 Oct 2026). f.117r: 276 signs decoded at 2-of-3, all M/U, not licensed (z 3.2, rank 1/201, judge FAIL); f.47r: 157 signs tested, not licensed.
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
- [ ] key-rebuild: f.47r S74/S54, S80/S65, S76/S91 pair check against the f.36 gloss; T88=q pre-registered test on another leaf; f.100r + f.119 joint phase+key anneal
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
Read so far: 0 tokens graded S or better of about 1,980 cipher signs (unchanged after NEVBIR-47C, 3 Oct 2026). The Ceppo-Nevers key is control-backed for f.47r (z 3.4-4.6, rank 1/201 in every run, power 19-20/20 at 0.33-0.34), but the text is not: 771 signs decoded, all M/U, judge FAIL. f.117r: 276 signs, all M/U.
- f.47r reader error 0.33 - blocker: not-attempted; third reader done (NEVBIR-47C); witness pair check done (CEPPO-WITNESS-PAIRS, 3 Oct 2026): R-8 and R-6 agree with the third reader on 28/28 and 39/39 tiles (the shuffle control is non-discriminating by construction); R-hash settles 6 unsettled upright hashes as S24 (o), which are 6 S candidates; key z 4.36-4.93, judge FAIL -1.524; 6 S accepted by VERIFY-CEPPO-WP (AUDIT.md, 0 -> 6 endorsed); next: a second eye on the f.36 witness glosses for blob-6 = m (still by elimination only), ~$2
- f.47r 73 unsettled positions (13 third-reader UNSETTLED after CEPPO-WITNESS-PAIRS settled 6; was 19 in harvest/f47/la/focus.tsv + 60 one-reader gaps) - blocker: not-attempted; written as sign-sorter focus rows; next: tools/sign_sorter.py --focus harvest/f47/la/focus.tsv
- f.47r prose/cipher edges - blocker: not-attempted; the readers marked no prose words, so L01-L03 and L17 run edges are unchecked; next: eye-check the s1 crops of L01-L03 and L17 s1-s2 against the passes, disk only, ~$1
- f.117r measured error after the 2-of-3 step - blocker: not-attempted; the 2-of-3 residual is agreement, not error; next: power control at a known-answer look-alike error with 100 windows, disk only, ~$1
- f.117r 12 unsettled tiles - blocker: not-attempted; sorter focus rows (harvest/f117/la/focus.tsv); sorter inputs built 3 Oct 2026 (SORTER-BIRAGO2, `sorter/README.md`, 277 tiles, 12 in the focus box), unpublished; next: the account-3 orchestrator publishes it with {"db": {}}, the owner sorts
- f.117r T88=q - blocker: not-attempted; fitted post-hoc on this letter only; next: test T88=q pre-registered on another French or Italian 1572 leaf with q-words, disk only, ~$1
- f.100r + f.119 (565 + 483 digits, same key) - blocker: not-attempted; joint anneal retired for this hypothesis (BIRAGO-NUM3); next: decoy-null joint-consistency crib test, ~$2

## Escalation (NEVBIR-47, 2 Oct 2026)
- [x] siblings: fr.3252 f.36-37 witness (gloss shapes as reference tiles), the fr.3251 1572 group's sheet, maps, clerk key and controls used
- [x] clear-pages: neighbours and facing pages of all three viewed; no clear copy or slip (Premise check (c))
- [x] known-keys: Ceppo-Nevers on f.47r whole letter (control-backed, NEVBIR-47), 1572 key on f.117r (z 3.2, judge FAIL), Nov 1571 system has no key
- [x] print: Gomberville 1665 both parts searched inside; no Birago letter of 1571-72
- [ ] key-rebuild: f.47r S74/S54, S80/S65 and hash pairs checked against the f.36 gloss (CEPPO-WITNESS-PAIRS), S76/S91 has no glossed witness instance yet; T88=q pre-registered test on another leaf; f.100r + f.119 decoy-null crib test
- [x] image-check: f.117r native crops, 10 lines; f.47r native re-cut, all 17 lines read twice
- [x] retry: f.47r third reader on 197 split tiles (NEVBIR-47C); [ ] f.117r power at a measured post-look-alike error; [x] f.47r pair check on the f.36 glossed witness (CEPPO-WITNESS-PAIRS)
Verdict: keep going: 7 internal gaps; cheapest next: a glossed blob-6 on f.36r/f.37r for R-6 (the 6 f.47r S candidates were accepted by VERIFY-CEPPO-WP, 3 Oct 2026), ~$2

## NEVBIR-NAMES (3 Oct 2026, account 2 for the account-3 orchestrator): whole-name gap fill, f.117r exploratory only

Main section and pre-registered gazetteer: `../nevers-birago-fr3251-1572/NOTES.md` "NEVBIR-NAMES" and `harvest/names/` there.
f.117r has no S tokens (all 251 keyed signs M), so the pre-registered rule (fixed = S/C) has nothing to fit; an exploratory run
(`match_names.py --f117`, M letters of `la/recon_f117_3r.tsv` under `map_printed.json` taken as fixed, flagged not pre-registered)
finds one U run >= 3 on the leaf (L01 start, before "mguila") and no admissible name; both controls p95 0.0. The leaf's names are
already given by word signs (turino L01, carmagnola L03). f.47r not run: 0.66 two-reader agreement and a live NEVBIR-47C third-reader
claim at 00:13 UTC. HYPOTHESES.md row (created this job). No reading changed; disk only, 0 requests.

## NEVBIR-47C (3 Oct 2026, account 3 orchestrator's worker): f.47r third reader on the split tiles

Brief `.claude/briefs/runs/2026-10-03-acct3-nevbir-47c.md`. Disk only, 0 network requests. Pre-registration pushed before the
read: `harvest/f47/la/PREREG.md` (commit 4916ba6a). No class, no novelty wording.

**Third reader.** `tools/lookalike_pass.py confusion` + `packet` on `recon_norm_agreement.tsv` / `recon_norm.tsv`, filtered to the
197 split tiles (`la/f47_split_tiles.tsv`; the brief's 257 = these 197 + 60 one-reader gaps, which are not in recon_norm.tsv and stay
out). The tool's candidate-cell cut (`--cell 110 --cols 9`) does not match this sheet's grid (1350x1190) and came out garbled, so it
was deleted and the reader got the full blind sheet with ids instead (tool limitation, noted here, not fixed). One value-blind Opus
subagent call, prompt `la/f47_reread_prompt.md` (51 recut crops, the blind sheet, the f.36 reference tiles ref_W1-3): 197 rows,
95 H, 86 M, 16 L, 0 SPLIT, 6 X_NEW (`la/f47_reread.tsv`).

**2-of-3** (`reconcile`, rule as pre-registered): 178 settled (148 with reader A, 30 with B), 19 unsettled -> `la/focus.tsv`;
residual 19/770 = 0.025 (agreement, not error; never the control's error). Caveat: the third reader resolved every frequent pair
the same way each time: S74 over S54 (39/39), S80 over S65 (28/28), S76 over S91 (21/21), S56 over S52 (14/14), S23 over S97 (9/10).
A consistent preference is either a real shape distinction or a reader bias; this job cannot tell which. Since 2-of-3 then only
picks the reader who shares that preference, those ~110 positions are effectively one reader's call.

**Test** (`decode_control.py la/passD.tsv --shuffles 200 --windows 20 --err 0.33 --extra X_THETA2=r --seed N`; E = the TWO-READER
error, LESSONS.md "Look-alike pass"):

| run | signs / letters | real key | shuffled mean (sd) | shuffled max | z | rank | power at 0.33 |
|---|---|---|---|---|---|---|---|
| passD seed 1 | 770 / 776 | -1.5267 | -2.0499 (0.126) | -1.6782 | 4.17 | 1/201 | 20/20, z median 7.72 (min 6.05) |
| passD seed 2 | 770 / 776 | -1.5267 | -2.0808 (0.117) | -1.7303 | 4.73 | 1/201 | 20/20, z median 7.66 (min 6.19) |
| passD seed 3 | 770 / 776 | -1.5267 | -2.0739 (0.124) | -1.6548 | 4.42 | 1/201 | 20/20, z median 8.18 (min 6.56) |

(NEVBIR-47 recon: z 3.38-4.24.) The key stays control-backed, margin over the best shuffle 0.13-0.20.

**Judge** (`python3 tools/judge_plaintext.py specs/ceppo-nevers-fr3251-1570s.json --file ciphers/birago-fr3252-1571-72/harvest/f47/la/reading_passD_letters.txt`, pasted):
```
FAIL language: score=-1.543, null_p99=-1.756, real_p05=-0.9, real_median=-0.83, mode=both, N=776
FAIL - ceppo-nevers-fr3251-1570s (a PASS is a gate for a verifier, not a reading; rule 10)
```
No better than recon (-1.525, which dropped the '?' positions instead of filling them). Pre-registered condition (iii) fails, so
**no token is graded above M**: 0 H, 0 C, 0 S; 751 decoded positions M, 19 '?' U. Not a reading; no verifier is wanted yet.

**Fragments (M, English gist only; readings `la/reading_passD_s1.txt`).** L10 "molto temp[o]" (a long time); L05 "furono" (they
were) and "quali" (which); L01 "intende" (understands/intends); L02 "mondo" (world); L13 "nemi[co]" (enemy) and "qual"; L07
"[s]empre" (always, read with z); L08 "delfin et le" (the Dauphin, or "del fine"), unresolved; L14 "ulti[mam]ente" (lately). Same
word islands as NEVBIR-47 plus "intende" and "mondo"; the run-on letters between them do not segment. The frequent z (S80 over
S65 at 28 positions) may be the pair-choice issue above rather than the text.

Subagents: 1 Opus call (third reader). Requests: 0. Rate limit read `allowed_warning` during the job.

## CEPPO-WITNESS-PAIRS (3 Oct 2026, account 2 for the account-3 orchestrator): pair shapes from the f.36 glossed witness

Brief `.claude/briefs/runs/2026-10-03-acct3-ceppo-witness-pairs.md`. Disk only, 0 network requests, 0 subagents (one Opus
session's own eye). No class, no novelty wording. Files: `harvest/witness_pairs/`.

**Rules, pre-registered before any tile was opened** (`harvest/witness_pairs/PREREG.md`, pushed e1760f2e). Source: the fr.3252
f.36v top block (HARVEST-D native region), cut at 2.5-3x with autocontrast. One reader (this worker) read the glosses, so they
are grade M. Tallies: an 8 with a bar through the waist that runs out past both sides is glossed **a** x6 (S80). A plain 8 is
glossed with an &-like mark x1 (S65 et, faint). A hash with an **upright** stem is glossed **o** x4 (S24). A hash with a
**slanted** stem is glossed **t** x2 (S88). A 6 with a flat crossbar on top has no gloss letter x2 (S54 null). A 6 with a blob
top was never seen glossed blank, but its gloss was illegible x4, so S74 m rests on elimination only. S76/S91 and S31/S32: no
legible glossed instance, so no rule.

**f.47r.** The third reader's per-tile shape notes (`la/f47_reread.tsv`, NEVBIR-47C) record exactly the deciding features.
`apply_rules.py` parses them, and the rule decides, not the reader's label (`f47_rule_labels.tsv`):
- 8 family, 28 split tiles: all "bar through 8", so R-8 gives S80 in 28/28. 6 family, 39 tiles: all "no crossbar", so R-6
  gives S74 in 39/39. The third reader's one-sided choice therefore follows the witness shape, and nothing is relabelled.
- **Shuffle control: non-discriminating by construction.** Reader A labelled every one of these tiles S80/S74 and reader B
  every one S65/S54, so shuffling either reader's labels leaves agreement unchanged (28 vs 28, 0 vs 0). This is a non-test
  (CLAUDE.md rule 3), not a pass. The features come from one reader's descriptions plus an eye check of L10 by this worker
  (no crossbar on the 6s; both hash forms present).
- **Hash: 6 of the 19 UNSETTLED tiles settled.** L03.6, L04.32, L08.38, L10.10, L10.35 and L12.29 are upright, and the third
  reader noted "S24-type" each time, so R-hash gives S24 (o). L10.10 was also checked by eye. Result: `f47_passE.tsv`
  (unsettled 19 -> 13).
- Value control: the same 6 positions were filled with each of the 20 key values. o ranks 1 of 20 (-1.5133; e -1.5228, the
  readers' t -1.5436, r -1.5629; `f47_hash6_valuefill.txt`). Random signs at the same 6 positions reached the rule's score 0/300
  times (p 0.003); random positions 4/300 (p 0.017) (`f47_relabel_null.txt`).
- Key control at the TWO-READER error 0.33 (`decode_control.py f47_passE.tsv --shuffles 200 --windows 20 --err 0.33 --extra
  X_THETA2=r`): real key -1.5133 (passD -1.5267); seeds 1/2/3 z 4.36 / 4.93 / 4.65, rank 1/201 in each, power 20/20 (z median
  7.64-8.20).
- Judge (pasted): `FAIL language: score=-1.524, null_p99=-1.788, real_p05=-0.906, real_median=-0.826, mode=both, N=782`
  (passD -1.543).
- Grades: the 6 hash tokens clear all three pre-registered gates, so they are **S candidates (6)**; everything else is
  unchanged. Total 6 S, 751 M, 13 U. Still not a reading. **VERIFIER WANTED** for the 6 tokens. The committed passD files are
  not edited; the proposed sequence is `f47_passE.tsv`.
- Fragments (M, English gist only): L10 now reads "molto tempo" in full ("a long time"; the o is one of the six). L08 has
  "...l o delfin et le..." (the Dauphin?), unresolved. The rest is as NEVBIR-47C.

f.87 (fr.3251) results are in `../ceppo-nevers-fr3251-1570s/NOTES.md`, section CEPPO-WITNESS-PAIRS.

**Verifier (VERIFY-CEPPO-WP, 3 Oct 2026): the 6 hash S candidates are accepted, so f.47r endorsed S goes 0 -> 6 (`AUDIT.md`).**
The verifier checked all six tiles upright by eye, reproduced the readings, and re-ran the controls at fresh seeds: z 4.56-5.31, rank 1/201, power 20/20.
In-family flips came out 0/1000 on two seeds. Endorsed sequence: `harvest/witness_pairs/f47_passE.tsv`.

## F36-READ (3 Oct 2026, account-3 orchestrator's worker): f.36-37 (5 Apr 1571) whole letter under the printed Ceppo-Nevers key

Brief `.claude/briefs/runs/2026-10-03-acct3-f36-read.md`. Disk only, 0 network requests. No class, no novelty wording.
Files: `harvest/f36/` (prompts, four raw passes, `compare_f36.py` [`--check` exits 1 if stale], `recon.tsv`, `passD.tsv`,
`reading_key.txt`, `control_s{1,2,3}.txt`). Crops: `../ceppo-nevers-fr3251-1570s/harvest/witness_f36/cut_lines.py`'s `cut()` re-run
with no overlap: `cut('../../../birago-fr3252-1571-72/harvest/f36/crops', 850, 0, 120, 65, 2)` -> 108 crops at 2x (not committed,
`.gitignore`). Passages: f.36r foot (r36 L01-L15), f.36v top 6 lines, f.36v middle 6, f.37r 2.

**Passes.** Two blind Sonnet readers x two pages (4 calls; the sheet `sign_sheet_blind.png` with ids only, glosses visible), each
asked for sign id + the clerk's letter above it. Rows: A r36 521, A v36 407, B r36 563, B v36 406.
- **The readers could not read the interlinear gloss.** 1,810 of 1,897 gloss cells came back '?'; the few letters they gave
  do not spell Italian (A v36 L01 "zxdozlgnozud" where the gloss reads "parlandone il signor"). This is the second failure of Sonnet
  gloss reading on this leaf (HARVEST-D, 28 Sept, at 1x; this job at 2x). The gloss is legible to an Opus eye at 2x (HARVEST-D read
  line 1; this worker confirmed "parlandone il signor" on `v36top_L01` and "...signor Sau[oia]" running into s2), so the instrument
  that failed is the Sonnet reader, not the image.
- **f.36r line geometry is off.** From about L10 the r36 crop centres (HARVEST-D's eye-set grid) sit between two manuscript lines;
  reader A took L15 as prose, reader B made L14 and L15 the same row (reading_key.txt rows r36_L14/L15 are near-duplicates). The
  r36 lower lines are therefore double-counted or shifted by one; the count below includes that duplication.
- Reconciliation (mechanical, `compare_f36.py`): ids aligned per line (difflib); agree 663, one-sided 89, split 241 -> '?'.
  **Two-reader error E = (241 + 89) / 993 = 0.33** (used for the control; one-sided rows counted as error).

**Control (rule 3)** (`decode_control.py passD.tsv --shuffles 200 --windows 20 --err 0.33 --extra X_THETA2=r --seed N`):

| seed | signs / letters | real key | shuffled mean (sd) | shuffled max | z | rank | power at 0.33 |
|---|---|---|---|---|---|---|---|
| 1 | 993 / 722 | -1.5051 | -2.0593 (0.121) | -1.7201 | 4.59 | 1/201 | 19/20, z median 5.93 (min 2.52) |
| 2 | 993 / 722 | -1.5051 | -2.0730 (0.120) | -1.7155 | 4.74 | 1/201 | 20/20, z median 5.51 (min 4.53) |
| 3 | 993 / 722 | -1.5051 | -2.0757 (0.112) | -1.7937 | 5.11 | 1/201 | 20/20, z median 5.70 (min 3.11) |

The printed Ceppo-Nevers key (with X_THETA2 = r) is control-backed for the whole letter: rank 1 of 201 on every seed, margin over
the best shuffle 0.21-0.29, power 19-20/20 at the same error.

**Known-answer check against the period gloss** (HARVEST-D's eye read of f.36v line 1, 18 signs "parlandone il signor",
`../ceppo-nevers-fr3251-1570s/harvest/witness_f36/alignment_pairs.tsv`, mapped to `v36top_L01` pos 1-18): of the 11 positions both
readers agree on, 10 decode to the gloss letter (a r l d o e l s g o; pos 12 via S40 = l where HARVEST-D had S84 = l, same value),
1 does not (pos 11, both readers S66 = c where the gloss has i and HARVEST-D saw S17: a shared shape slip). 7 positions split.

**Judge** (`python3 tools/judge_plaintext.py specs/ceppo-nevers-fr3251-1570s.json --file ciphers/birago-fr3252-1571-72/harvest/f36/reading_key_letters.txt`, pasted):
```
FAIL language: score=-1.559, null_p99=-1.754, real_p05=-0.915, real_median=-0.83, mode=both, N=722
FAIL - ceppo-nevers-fr3251-1570s (a PASS is a gate for a verifier, not a reading; rule 10)
```
Above null p99, below real p05: what about a third of signs misread produces (same shape as f.47r, NEVBIR-47/47C).

**Grades (rule 4).** 993 sign positions: 18 null; 268 unsettled (U); 707 decoded: **10 C** (v36top_L01, key value = period gloss),
**697 M**; 0 H, 0 S. Not a reading. Fragments (M, gist only): r36_L01 "...[v]ostra ten..."; v36top_L01 "[p]arl[an]do[n]e ... s[i]g[n]o[r]",
then "...qua..."; v36top_L04/05 "...esordece qu..." "altro"; r37_L02 "...arda". Not sentences.

**Is the letter a period decipherment?** Every cipher passage carries the clerk's letter-by-letter gloss (HARVEST-D, confirmed on
the crops this job). So yes: the plaintext of this letter exists on the leaf, in the clerk's hand, and the job of "reading" it
is reading that gloss, not breaking anything. That is not done yet: 18 of about 990 glossed signs have been read.

Subagent use: 4 Sonnet calls (~780k subagent tokens). Pass A v36 was still writing at the first reconciliation; all numbers here are from the final files. Own session read `rate_limit allowed_warning` at 01:20 UTC after launch
(ROOM flag); no further subagent started.

## Remaining gaps (F36-READ, 3 Oct 2026)
Read so far: f.36-37: 10 C, 0 S of about 990 cipher signs; the key is control-backed (z 4.59-5.11, rank 1/201, power 19-20/20 at 0.33). f.47r: 0 S of about 770 (unchanged). f.117r: 276 signs, all M/U.
- f.36-37 period gloss (about 970 glossed signs unread) - blocker: not-attempted; Sonnet gloss reading [retired] for this leaf (two attempts, 1x and 2x, both all-'?'); a different instrument is untried: Opus eye read of the gloss band, one line per call on 3x crops, transcribed as running Italian then aligned to the sign passes; next: Opus gloss read, 29 lines, ~$4 (wait until rate limit reads allowed)
- f.36r lines L10-L15 crop geometry - blocker: not-attempted; HARVEST-D's eye-set centres drift between rows; next: re-centre with tools/iiif_lines.py --image c37_f36r_cipher.jpg (row ink profile), re-cut, ~$0.5
- f.47r reader error 0.33 - blocker: not-attempted; S74/S54, S80/S65, S76/S91 one-sided third-reader preference unverified; next: known-answer pair check on the f.36 gloss once the gloss is read (CEPPO-WITNESS-PAIRS has a pre-registered f.36v-top tally, 3 Oct), disk only, ~$2
- f.47r 79 unsettled positions - blocker: not-attempted; sign-sorter focus rows written; next: tools/sign_sorter.py --focus harvest/f47/la/focus.tsv
- f.47r prose/cipher edges - blocker: not-attempted; the readers marked no prose words, so run edges are unchecked; next: eye-check L01-L03 and L17 s1-s2 crops, disk only, ~$1
- f.117r measured error after the 2-of-3 step - blocker: not-attempted; the 2-of-3 residual is agreement, not error; next: power control at a known-answer look-alike error, disk only, ~$1
- f.117r 12 unsettled tiles - blocker: not-attempted; sorter inputs built (SORTER-BIRAGO2), unpublished; next: the account-3 orchestrator publishes it with {"db": {}}, the owner sorts
- f.117r T88=q - blocker: not-attempted; fitted post-hoc on this letter only; next: pre-registered test on another 1572 leaf with q-words, disk only, ~$1
- f.100r + f.119 (565 + 483 digits) - blocker: not-attempted; joint anneal retired (BIRAGO-NUM3); next: decoy-null joint-consistency crib test, ~$2

## Escalation (F36-READ, 3 Oct 2026)
- [x] siblings: fr.3252 f.36-37 witness read whole under the same key (F36-READ), the fr.3251 1572 group's sheet, maps, clerk key and controls used
- [x] clear-pages: neighbours and facing pages of all three viewed; no clear copy or slip (Premise check (c)); f.37r slip is clear text
- [x] known-keys: Ceppo-Nevers on f.36-37 whole letter (control-backed, F36-READ) and f.47r (NEVBIR-47); 1572 key on f.117r (z 3.2, judge FAIL); Nov 1571 system has no key
- [x] print: Gomberville 1665 both parts searched inside; no Birago letter of 1571-72
- [ ] key-rebuild: f.36 gloss read by Opus eye (gives the true member of each look-alike pair); f.47r pair check against it; T88=q pre-registered test; f.100r + f.119 decoy-null crib test
- [x] image-check: f.36-37 2x crops all 29 lines (F36-READ); f.117r native crops; f.47r native re-cut
- [ ] retry: f.36r L10-L15 re-centre and re-cut; f.117r power at a measured post-look-alike error
Verdict: keep going: 9 internal gaps; cheapest next: re-centre the f.36r lower lines (~$0.5), then an Opus eye read of the f.36-37 period gloss (~$4) once the rate limit reads allowed

## F36-GLOSS (3 Oct 2026, account-3 orchestrator's worker): Opus eye read of the f.36-37 clerk gloss -- gate FAIL, no key

Brief `.claude/briefs/runs/2026-10-03-acct3-f36-gloss.md`. Disk only, 0 network requests. f.36-37 is itself a letter the period
clerk deciphered on the leaf: whatever its gloss says is the period reading (N0-type), not a find of this project.
Files: `harvest/f36gloss/` -- `cut_gloss.py` (crops, gitignored), `prompt*.md`, `pass{A,B}_{r36,v36}.tsv`, `recon_gloss.py`
(`--check`) -> `gloss_recon.tsv`, `align_f36.py` (`--check`) -> `pairs.tsv`, `align.tsv`, `control.tsv`, `conflicts.tsv`,
`../../keys/key_ceppo_f36_clerk.tsv`; `variant_decode.py` written, **not run** (step 4 is gated on step 3, which failed).

1. **Re-centre (step 1).** `python3 tools/iiif_lines.py --image ciphers/ceppo-nevers-fr3251-1570s/harvest/witness_f36/c37_f36r_cipher.jpg
   --out <scratch> --prefix r36 --debug` -> centres 44 158 252 353 438 558 678 780 861 966 1068 1164 1271 1390 1490 1571 1682
   (44, 558, 678 are prose rows). f.36r carries **14** cipher lines (4 at the top, 10 after "delle cose di francia"), not
   HARVEST-D's 15: its grid drifts from L08 (1045 vs 1068) to L14 (1630 vs 1682), so passD's r36_L09-L15 straddle rows and one row
   is counted twice. Gloss crops re-cut on the profile centres as r36n_L01-L14; f.36v/f.37r on their own profile centres
   (within 10-45 px of HARVEST-D's). The sign passes (passD) were not re-read: r36n gloss lines pair with passD r36_L(i or i+1) by
   the closer printed-key decode (line pairing only, never a value).
2. **Gloss read (step 2).** Round 1 (3x, 700-px segments, 64 images per call) failed mechanically: the reader's earliest images
   were dropped from its context ("media removed: request limit") before it wrote, and 700 px held only ~7 signs; stopped, discarded.
   Round 2: 102 crops (1000 native px x1.5, the whole cipher row as anchor), two blind Opus passes x two pages (4 calls, written
   line by line). '?' share A 39% / 33%, B 26% / 26%; every reader called its own pass low-confidence. Reconciled per line
   (difflib): agree 338, one '?' 32, split 19, one-sided 536, both '?' 170; **two-pass gloss error (split+one-sided)/total = 0.51**.
3. **Alignment and gates (step 3).** `tools/interlinear_align.py` (`--code-prefix @`, floor 0, null-cost 0, wildcard '?'), unsettled
   signs as unique codes. Two statistics per leaf against 200 gloss-line shuffles within the leaf (the control can differ: shuffling
   changes which gloss letters sit on which signs): self-consistency (share of aligned tokens equal to the sign's majority letter) and
   a known-answer check (share equal to the printed Ceppo-Nevers value, control-backed on this letter by F36-READ, z 4.6-5.1):
```
leaf	statistic	real_n	real_k	real_share	shuf_mean	shuf_p95	shuf_max	gate
f36r	self	178	97	0.545	0.592	0.651	0.681	TIE/FAIL
f36r	printed	172	14	0.081	0.070	0.131	0.171	TIE/FAIL
f36v	self	103	60	0.583	0.642	0.740	0.785	TIE/FAIL
f36v	printed	89	5	0.056	0.055	0.119	0.205	TIE/FAIL
f37r	self	23	13	0.565	0.667	0.842	0.938	TIE/FAIL
f37r	printed	20	3	0.150	0.077	0.176	0.278	TIE/FAIL
```
   **Every leaf ties or fails both gates.** The known-answer share (5.6-15%) sits at the shuffle mean (5.5-7.7%), i.e. at chance: the
   reconciled gloss does not register with the sign row. Per CLAUDE.md rule 3 (merge paragraph) no leaf's values may enter a shared
   key: `keys/key_ceppo_f36_clerk.tsv` (41 signs, 19 "conflicts" with the printed table) is the alignment's raw output, kept for
   rule 7 only, **all rows unusable** -- not C, not merged, and its "conflicts" are alignment noise, not data conflicts under rule 4.
   Step 4 not run: there is no passing C value to fill a sign the printed table lacks (X_NEW, b/x/y homophones).
4. **Grades (rule 4).** Unchanged from F36-READ: 10 C (HARVEST-D's f.36v line-1 eye read), 697 M, 268 U, 18 null of 993; 0 H, 0 S.
   One spot agreement: both Opus passes give "...il s?gnor..." on v36top_L01, matching HARVEST-D's "parlandone il signor"; the rest of
   that line diverges from the printed-key decode.

Lesson: an interlinear gloss of ~15-px letters at Gallica's native resolution is not read by a model fed running-line segments, Sonnet
(F36-READ, HARVEST-D) or Opus (this job); the failure is registration and legibility, and a gate on the known-answer key catches it.
Cost: session read USD 16.94 at the stop (2.8x the USD 6 cap; round 1's discarded 3x calls plus round 2's four ~125k-token calls); rate
limit `allowed_warning` at the same read; stopped there.

## Remaining gaps (F36-GLOSS, 3 Oct 2026)
Read so far: f.36-37: 10 C, 0 S of about 990 cipher signs (the clerk gloss unread beyond f.36v line 1); f.47r: 0 S of about 770; f.117r: 276 signs, all M/U.
- f.36-37 period gloss (about 970 glossed signs unread) - blocker: not-attempted; running-line model reads [retired] (Sonnet twice, F36-READ/HARVEST-D; Opus once here, known-answer gate at chance on all three leaves); a different instrument is untried: per-sign tiles (each sign box with the band above it, from passD positions, 40 per grid image, the sign id printed under each) so the gloss letter is registered to its sign by construction, two blind passes, known-answer gate first on v36top_L01 and on signs whose printed value is control-backed; next: per-sign tile gloss read, ~$8 (wait until rate limit reads allowed)
- f.36r passD sign rows r36_L09-L15 - blocker: not-attempted; they straddle the 14 real rows found by the row-ink profile (F36-GLOSS step 1); next: re-read the signs of r36n_L09-L14 on the re-centred crops (cut_gloss.py centres), one Sonnet pass x2, ~$2
- f.47r reader error 0.33 - blocker: not-attempted; S74/S54, S80/S65, S76/S91 one-sided third-reader preference unverified; next: known-answer pair check on the f.36 gloss once the gloss is read, disk only, ~$2
- f.47r 79 unsettled positions - blocker: not-attempted; sign-sorter focus rows written; next: tools/sign_sorter.py --focus harvest/f47/la/focus.tsv
- f.47r prose/cipher edges - blocker: not-attempted; the readers marked no prose words, so run edges are unchecked; next: eye-check L01-L03 and L17 s1-s2 crops, disk only, ~$1
- f.117r measured error after the 2-of-3 step - blocker: not-attempted; the 2-of-3 residual is agreement, not error; next: power control at a known-answer look-alike error, disk only, ~$1
- f.117r 12 unsettled tiles - blocker: not-attempted; sorter inputs built (SORTER-BIRAGO2), unpublished; next: the account-3 orchestrator publishes it with {"db": {}}, the owner sorts
- f.117r T88=q - blocker: not-attempted; fitted post-hoc on this letter only; next: pre-registered test on another 1572 leaf with q-words, disk only, ~$1
- f.100r + f.119 (565 + 483 digits) - blocker: not-attempted; joint anneal retired (BIRAGO-NUM3); next: decoy-null joint-consistency crib test, ~$2

## Escalation (F36-GLOSS, 3 Oct 2026)
- [x] siblings: fr.3252 f.36-37 witness read whole under the same key (F36-READ), the fr.3251 1572 group's sheet, maps, clerk key and controls used
- [x] clear-pages: neighbours and facing pages of all three viewed; no clear copy or slip (Premise check (c)); f.37r slip is clear text
- [x] known-keys: Ceppo-Nevers on f.36-37 whole letter (control-backed, F36-READ) and f.47r (NEVBIR-47); 1572 key on f.117r (z 3.2, judge FAIL); Nov 1571 system has no key
- [x] print: Gomberville 1665 both parts searched inside; no Birago letter of 1571-72
- [ ] key-rebuild: f.36 gloss by per-sign tiles (running-line reads retired, F36-GLOSS); f.47r pair check against it; T88=q pre-registered test; f.100r + f.119 decoy-null crib test
- [x] image-check: f.36-37 gloss crops re-cut on row-ink centres (F36-GLOSS); regions are already Gallica native resolution; f.117r native crops; f.47r native re-cut
- [ ] retry: f.36r r36n_L09-L14 sign re-read on the re-centred rows; f.117r power at a measured post-look-alike error
Verdict: keep going: 9 internal gaps; cheapest next: re-read the f.36r r36n_L09-L14 sign rows (~$2), then the per-sign tile gloss read (~$8) once the rate limit reads allowed

## F36R-REREAD (3 Oct 2026, account-3 orchestrator's worker): f.36r cipher rows r36n_L09-L14 recut and re-read

Brief `.claude/briefs/runs/2026-10-03-acct3-f36r-reread.md`. Disk only, 0 network requests. No gloss read. No class, no novelty wording.
Files: `harvest/f36r/` -- `cut_f36r.py` (crops, gitignored), `prompt_{A,B,R}.md`, `pass{A,B}.tsv`, `adjudicate_{in,out}.tsv`,
`merge_f36r.py` (`--check`) -> `recon_r36n.tsv`, `error.tsv`, `passD_v2.tsv`, `ciphertext_f36_v2.tsv`, `reading_key_v2*.txt`;
`control_mech_s{1,2,3}.txt` (before reconciliation), `control_s{1,2,3}.txt` (after); `../../decode.json` -> `reading_f36_v2*.{txt,tsv}`.

1. **Recut.** `python3 tools/iiif_lines.py --image ciphers/ceppo-nevers-fr3251-1570s/harvest/witness_f36/c37_f36r_cipher.jpg --out <scratch>
   --prefix r36 --debug` -> 17 centres, the same as F36-GLOSS (44 158 252 353 438 558 678 780 861 966 1068 1164 1271 1390 1490 1571 1682).
   The debug overlay was checked by eye: each red centre line sits on a sign row; the lowest is the last cipher row. `cut_f36r.py` cut
   profile bands 12-17 (= r36n_L09-L14) +-12 px, four non-overlapping 760-px segments, 2x: 24 crops, one main row per crop.
2. **Passes.** Two blind Sonnet readers (sheet `sign_sheet_blind.png` + the 24 crops only, sign ids only): A 245 signs, B 244
   (rows 44/44, 44/43, 41/41, 40/40, 38/38, 38/38). One Sonnet reconciliation call on the crops settled the 38 disagreements by shape
   (`adjudicate_out.tsv`: 5 H, 21 M, 12 L; only H/M are applied; the error below is counted *before* it, so it is the blind figure).
3. **What the old rows were.** The new rows decode like F36-READ's r36_L09-L13 one for one, and **r36_L14 and r36_L15 were the same manuscript
   row read twice** (both decode "traf_eda...mesequemt..."; new r36n_L14 "tracredaamesequemta_e..."). F36-READ's 993 positions included a
   duplicated row of ~38 signs; the spliced transcription has 947 (after reconciliation; 948 before).
4. **Two-reader error** (`error.tsv`, rule as F36-READ: (split + one-sided) / positions):

| scope | positions | agree | one-sided | split | E |
|---|---|---|---|---|---|
| r36n_L09-L14 (new) | 248 | 210 | 7 | 31 | **0.153** |
| kept F36-READ rows | 700 | 467 | 40 | 193 | 0.333 |
| whole letter | 948 | 677 | 47 | 224 | **0.286** |

   Per row 0.079-0.227. Systematic splits: S24/S73 (5), S80/S65 (5), S73/S49 (4), S94/X_POUND (2), S16/S42 (2) -- the known look-alike pairs.
5. **Control (rule 3)**, `decode_control.py passD_v2.tsv --shuffles 200 --windows 20 --err 0.286 --extra X_THETA2=r --seed N`, power at the
   measured whole-letter error:

| seed | input | signs / letters | real key | shuffled mean (sd) | shuffled max | z | rank | power at 0.286 |
|---|---|---|---|---|---|---|---|---|
| 1 | blind (before reconciliation) | 948 / 690 | -1.3919 | -2.0546 (0.114) | -1.7446 | 5.80 | 1/201 | 20/20, z median 5.86 (min 4.24) |
| 2 | blind | 948 / 690 | -1.3919 | -2.0719 (0.115) | -1.7312 | 5.91 | 1/201 | 20/20, z median 6.43 (min 4.38) |
| 3 | blind | 948 / 690 | -1.3919 | -2.0790 (0.099) | -1.7967 | 6.92 | 1/201 | 20/20, z median 6.16 (min 3.70) |
| 1 | reconciled | 947 / 710 | -1.3696 | -2.0554 (0.110) | -1.7448 | 6.25 | 1/201 | 20/20, z median 6.71 (min 5.09) |
| 2 | reconciled | 947 / 710 | -1.3696 | -2.0699 (0.108) | -1.7747 | 6.51 | 1/201 | 20/20, z median 6.55 (min 4.30) |
| 3 | reconciled | 947 / 710 | -1.3696 | -2.0793 (0.091) | -1.7916 | 7.82 | 1/201 | 20/20, z median 6.64 (min 3.95) |

   Against F36-READ (real -1.5051, z 4.59-5.11, power 19-20/20 at 0.33): the real-key score rises by 0.11-0.14 per letter and z by
   about 1.2-2.7 with the same shuffle distribution, i.e. the recut rows read better under the printed key; the key stays control-backed.
6. **decode_key** (`python3 tools/decode_key.py ciphers/birago-fr3252-1571-72 --check`, pasted): `harvest/f36r/ciphertext_f36_v2.tsv: tokens 947:
   M 718, U 229` / `reading up to date`. `merge_f36r.py --check`: `OK, not stale`.
7. **Judge** (`python3 tools/judge_plaintext.py specs/ceppo-nevers-fr3251-1570s.json --file ciphers/birago-fr3252-1571-72/harvest/f36r/reading_key_v2_letters.txt`, pasted):
```
FAIL language: score=-1.487, null_p99=-1.777, real_p05=-0.929, real_median=-0.826, mode=both, N=710
FAIL - ceppo-nevers-fr3251-1570s (a PASS is a gate for a verifier, not a reading; rule 10)
```
   Up from -1.559 (F36-READ), still between null p99 and real p05: a third of the kept rows' signs are still unsettled or misread.
8. **Grades (rule 4).** 947 positions: 19 null; 229 U (204 '?' + 25 X_NEW, no key value); 699 decoded: **10 C** (v36top_L01, unchanged), **689 M**;
   0 H, 0 S. Not a reading. decode_key writes the 10 C as M (it has no C grade; the C is compare_f36.py's period-gloss match).
   Fragments of the new rows (M, gist only): r36n_L11 "tempo...", r36n_L12 "...ueseresel...", r36n_L14 "...mesequemta..." ("me se que"?) -- not sentences.

Subagent use: 3 Sonnet calls (2 blind passes + 1 reconciliation), as priced in the brief. One mishap: a `git stash -u` to push while pass B
was still appending removed its first two rows; restored from the stash the same minute (row counts verified 44/43/41/40/38/38).

## Remaining gaps (F36R-REREAD, 3 Oct 2026)
Read so far: f.36-37: 10 C, 0 S of 947 cipher signs (two-reader E 0.286, key control-backed z 5.8-7.8, power 20/20); f.47r: 0 S of about 770; f.117r: 276 signs, all M/U.
- f.36-37 period gloss (about 940 glossed signs unread) - blocker: not-attempted; running-line model reads [retired] (Sonnet twice, F36-READ/HARVEST-D; Opus once, F36-GLOSS, known-answer gate at chance); a different instrument is untried: per-sign tiles (each sign box with the band above it, from passD_v2 positions, 40 per grid image, the sign id printed under each), two blind passes, known-answer gate first on v36top_L01; next: per-sign tile gloss read, ~$8 (wait until rate limit reads allowed)
- f.36-37 kept rows at E 0.333 (700 positions, 193 splits) - blocker: not-attempted; r36_L01-L08, v36top, v36mid and r37 were read on HARVEST-D's eye grid, which the row-ink profile matched within 10-45 px there; next: one reconciliation call on their splits (as this job did for r36n), disk only, ~$1.5
- f.47r reader error 0.33 - blocker: not-attempted; S74/S54, S80/S65, S76/S91 one-sided third-reader preference unverified; next: known-answer pair check on the f.36 gloss once the gloss is read, disk only, ~$2
- f.47r 79 unsettled positions - blocker: not-attempted; sign-sorter focus rows written; next: tools/sign_sorter.py --focus harvest/f47/la/focus.tsv
- f.47r prose/cipher edges - blocker: not-attempted; the readers marked no prose words, so run edges are unchecked; next: eye-check L01-L03 and L17 s1-s2 crops, disk only, ~$1
- f.117r measured error after the 2-of-3 step - blocker: not-attempted; the 2-of-3 residual is agreement, not error; next: power control at a known-answer look-alike error, disk only, ~$1
- f.117r 12 unsettled tiles - blocker: not-attempted; sorter inputs built (SORTER-BIRAGO2), unpublished; next: the account-3 orchestrator publishes it with {"db": {}}, the owner sorts
- f.117r T88=q - blocker: not-attempted; fitted post-hoc on this letter only; next: pre-registered test on another 1572 leaf with q-words, disk only, ~$1
- f.100r + f.119 (565 + 483 digits) - blocker: not-attempted; joint anneal retired (BIRAGO-NUM3); decoy-null joint-consistency crib test untested-by-this-tool, control 0/8 found against a 15/20 gate (BIRAGO-NUM4); next: dotted two-figure groups read as nomenclator codes against the clear text around each run, disk only, ~$1

## Escalation (F36R-REREAD, 3 Oct 2026)
- [x] siblings: fr.3252 f.36-37 witness read whole under the same key (F36-READ), the fr.3251 1572 group's sheet, maps, clerk key and controls used
- [x] clear-pages: neighbours and facing pages of all three viewed; no clear copy or slip (Premise check (c)); f.37r slip is clear text
- [x] known-keys: Ceppo-Nevers on f.36-37 whole letter (control-backed, F36-READ; re-run on the recut transcription, F36R-REREAD) and f.47r (NEVBIR-47); 1572 key on f.117r (z 3.2, judge FAIL); Nov 1571 system has no key
- [x] print: Gomberville 1665 both parts searched inside; no Birago letter of 1571-72
- [ ] key-rebuild: f.36 gloss by per-sign tiles (running-line reads retired, F36-GLOSS); f.47r pair check against it; T88=q pre-registered test; f.100r + f.119 dotted groups as nomenclator codes against the clear text (spelled-crib tests: crib drag weak by control, BIRAGO-NUM2; decoy-null joint crib test untested-by-this-tool, BIRAGO-NUM4)
- [x] image-check: f.36r rows r36n_L09-L14 recut on the row-ink profile and re-read (F36R-REREAD); f.36-37 gloss crops re-cut (F36-GLOSS); f.117r native crops; f.47r native re-cut
- [ ] retry: reconciliation call on the kept f.36-37 rows' 193 splits; f.117r power at a measured post-look-alike error
Verdict: keep going: 9 internal gaps; cheapest next: one reconciliation call on the kept f.36-37 rows' splits (~$1.5), then the per-sign tile gloss read (~$8) once the rate limit reads allowed

## TX-DECODE (3 Oct 2026, account 2 for the account-3 orchestrator): f.117r re-tested by key-constrained lattice decode

Full section with controls in `../nevers-birago-fr3251-1572/NOTES.md` "TX-DECODE". f.117r (279 signs, passA/passB of
`harvest/f117/`, printed 1572 key, fr16): top-1 of the two passes rank 10/201 z 1.63. Lattice decode at lam 4 (tuned on
no.87; the pre-registered lam 1 failed the no.87 known-answer gate): **rank 1/201, z 3.66**, 32 signs changed from top-1,
each grade S at best. Position-shuffled lattice control: rank 4-64, z at most 1.91 over 5 seeds. Synthetic power at 279
signs, err 0.25: 20/20 (top-1 16/20). Judge FAIL -1.081 (real_p05 -0.903). No reading committed; status unchanged.
Outputs `../nevers-birago-fr3251-1572/harvest/tx_decode/f117_*`.

## f.119 + f.100r: decoy-null joint-consistency crib test (BIRAGO-NUM4, 3 Oct 2026)

Brief `.claude/briefs/runs/2026-10-03-acct3-birago-num4.md`. Files in `num/num4/`. `PREREG.md` and the instrument
`joint_crib.py` were pushed in 168bbcfc before the target was scored. This is a different instrument from the retired
anneal. 15 cribs (carmagnola, bellagarda, ualletta, sauoia, turino, saluzzo, monsignore, maesta, neuers, birago, ceppo,
centurione, maresciale, ugonotti, regina) were dragged over the pooled phase.py stream (61 runs, 473 pairs). Two
placements are jointly consistent when they do not overlap and no code gets two letters across them. The statistic is the
best jointly consistent pair, scored by it16dip bigram PMI over every adjacent token pair in both letters that the joint
key fixes. Each crib's own bigrams are removed. The null is 200 decoy sets, each crib swapped for a random it16dip word of
the same length and dragged over the same real stream. This replaces BIRAGO-NUM2's permutation null, which was
anti-conservative.

**Dev (synthetic only, seeds 98/99, `dev_*.txt`).** A count statistic (pairs that agree on >= 2, 3 or 4 shared codes) is
swamped by chance pairs. On 3 dev trials the real set scored *below* the decoys at K=2, 3 and 4. The PMI-max statistic was
pre-registered instead. It also missed on its one dev trial, p 0.40.

**Power control (gate, `control_out.txt`).** Synthetic it16dip, 476 pairs, 40 cells, 5% strays, re-phased by `phase.em`,
3 of the 15 cribs planted, 200 decoys. Run as 4 x 5 trials, seeds 4001-4004; PREREG named seed 4001 for one run of 20,
and the split was made so it fit the box. **Found (p <= 0.05) in 0 of 8 trials**, p 0.065-0.900. The runs were stopped at
8 trials because even 12 more finds would leave 12/20, below the 15/20 gate.

**Target (`target_out.txt`, decoy seed 20261003).** J = 33.86 against a decoy mean of 41.44 (p95 56.67, max 67.98),
rank 182 of 201, **p = 0.905**. This is scored for the record only.

**Verdict: untested-by-this-tool, neither a pass nor a negative.** Joint consistency between spelled cribs cannot
separate 3 planted names from same-length decoys at 476 pairs and 40 cells. The test has no power at this N, so the
target's p = 0.905 says nothing about whether the names are present. No pair value comes out of this test and no token is
graded. Together with BIRAGO-NUM2 this covers both spelled-crib designs, and neither has power here. BIRAGO-NUM2's premise
risk also remains: the 1572 key gives names their own word codes. The next instrument is BIRAGO-NUM2 design note 3, the
dotted two-figure groups read as nomenclator codes against the clear text around each run. More N (a third letter in this
key) would also help. Novelty is not classified (rule 10).

Cost and requests: disk only, no network, no subagents, 0 vision calls.

## f.119 + f.100r: three built-but-unused tools (BIRAGO-NUM-TOOLS, 3 Oct 2026)

Brief `.claude/briefs/runs/2026-10-03-acct3-birago-num-tools.md`. Files in `num/tools/` and `num/seg/`. Prior work cited as
in BIRAGO-NUM (Bourdeau's f.119 transcription, cyphersolver `targets/birago`, MIT / CC BY 4.0).

**1. Key crossmatch.** The stale entry was real. KEY-CROSSMATCH.tsv had scored `../birago-nevers-1571/ciphertext.txt`, which is
Tomokiyo's transcription with its marks run into the digits, as **8 whitespace "signs"** against every key (45 rows, all
meaningless). That file is kept as transcribed. `num/tools/make_ct_pairs.py` now writes each letter as two-digit code tokens:
plain runs are cut by phase.py's pooled phase with strays dropped, and the marked groups stay in place. The outputs are
`../birago-nevers-1571/ciphertext_f119_pairs.txt` (240 tokens) and `num/ciphertext_f100_pairs.txt` (274 tokens).
`tools/key_crossmatch.py` gained `CT_SKIP_FILES`, which drops the untokenisable file and names its replacement (test in
`tools/tests/test_key_crossmatch.py`). In KEY-CROSSMATCH.tsv the 45 stale rows were replaced by the 132 new ones.
Result (`num/tools/out/crossmatch_pairs.tsv`): 66 keys reach coverage >= 0.5 on each letter (35 `none`, 28 `unusable-key`,
3 `no_corpus`). The **best stat is 2.54** (f.100r under lodewijk-van-nassau `axmerge3/key_full_v2.tsv`), against the gate of
3.292. **No pair is at or above the gate.**
Matched positive control (`num/tools/xmatch_control.py`, `out/xmatch_control.txt`): synthetic it16dip text of 255 pairs (one
letter's length), one homophonic key, 5% strays, scored with the *true* key. At the true phase the control hits 6 of 6; at
phase.em's recovered phase (accuracy 0.675-0.969) it also hits 6 of 6, with stats 7.2-16.7 at 40 and 55 cells. So a key on
disk that was the Nov 1571 key would have cleared the gate even at this phase error. **Control-backed negative:** none of the
66 digit keys on disk is this key. This holds for keys whose language has a corpus. The 3 `no_corpus` keys (colbert155
croissy 1668, intercepted-royalist 1646, maurice-rupert 1645) are other offices and decades and were not scored.

**2. seg_homophonic (joint segmentation + homophonic).** *Is it a different instrument?* For the pairs-plus-strays
hypothesis, **no**. With every digit a prefix it cuts each run in pairs from the run start, which is weaker than the retired
phased_homophonic, and that hypothesis stays retired. For a **different hypothesis, a prefix code**, it is: a deterministic
parse has no phase to flip. The design was chosen from structure before any solve (`num/seg/PREREG.md`, pushed 429bef29).
Of 46 runs longer than one digit, only **2 end in 1, 5 or 8**, against a within-run shuffle null of mean 13.6 (p01 7,
minimum 3 in 10,000 draws). The candidate is `158:letter`: 1x/5x/8x are two-digit units and the other digits single. It
gives 734 units, 29 types and 1 parse exception.
Control first: held-out it16 Italian, 734 units, the target's line lengths. **Noise 0.05: mean 0.782** (0.92 0.20 0.93 0.93
0.92), gate 0.6 met. Noise 0.02: 0.97 on the 4 seeds that finished. Noise 0.05 brackets the measured error (1.4% two-reader
disagreement plus 1 parse exception). Caveat on the match: in the control, single units carry about 25% of the text. In the
target they carry 483 of 734 units (66%), so the target's unit-frequency profile is not reproduced.
Target, model it16 all, score per unit with nulls:

| design | units | types | score/unit | null | z |
|---|---|---|---|---|---|
| 158 (pre-registered) | 734 | 29 | -3.604 | -4.051 ± 0.014 (signs) | 32.4 |
| 158 | 734 | 29 | -3.604 | -4.229 ± 0.024 (units) | 25.7 |
| 15 (neighbour) | 790 | 23 | -3.717 | -4.225 ± 0.016 (signs) | 32.3 |
| 1589 (neighbour) | 665 | 39 | -3.647 | -3.809 ± 0.018 (signs) | 9.2 |
| control 158, noise 0.05 | 746 | 39 | **-2.457** | -3.894 ± 0.061 (units) | 23.5 |

Pre-registered criterion (a) is met: the target's unit-null z (25.7) exceeds the control's (23.5). It means little,
because the target's null sd is 2.5 times smaller. Criterion (b) **FAILs**: judge it16 gives -1.357 against real_p05 -0.985
(null_p99 -1.806) on `num/seg/runs/target_unitnull_reading.txt`, which begins `dinsegoeiaogiaognisorne...` with no run of
words. The control's own decode, which reads by eye ("dochesochefaraperaimormiocacconoscendo..."), *also* FAILs the judge,
narrowly: -1.018 against real_p05 -1.007. So at noise 0.05 the judge sits at the edge of the control's ceiling. The
informative gap is the score per unit: -3.60 for the target against -2.46 for the control. The target sits where the fr4687
calibration put a 10%+ noise control or a non-letter design.
**Verdict: no reading. This is a control-backed negative for a 158 prefix code with a letter-homophonic table in it16
Italian**, conditional on the transcription and on the unit-profile caveat above. The run-end structure (1/5/8 open units)
stays unexplained by any design tried. A nomenclator reading of the 1x/5x/8x units (as with the dotted groups) is a
different design and was not tested. No token is graded.

**3. cipher_page_detector.** The tool gained `--manifest-file` and `--canvas-range` (offline test added). The three volumes
have 676 canvases and the cap is 400 requests, so the scan covered **fr.3995 whole (285)**, **fr.3251 canvases 96-155
(f.95-f.154)** and **fr.3252 canvases 70-121 (f.69-f.120)**, at 400 px. Requests: gallica.bnf.fr 3 manifests + 397
thumbnails = 400, 1.5 s apart, no block. Scores: `num/tools/out/scan_{fr3995,fr3251,fr3252}_scores.tsv`.
**In-volume positive control FAILs.** The six known cipher leaves in those windows score 0.26-0.35, all predicted "plain" and
all in the lower half: fr.3251 f.119 rank 51/60, f.138 42/60, f.144 33/60, f.152 53/60; fr.3252 f.100r 46/52, f.117r 42/52.
The detector cannot see these hands' cipher at 400 px. Its 16 "cipher" calls in fr.3252 and 51 in fr.3995 (covers and
flyleaves among the top 10) license nothing, and no canvas is reported as an uncovered cipher or key page. In fr.3995 every
leaf is a key table anyway. Pointer from Tomokiyo's list, not from the detector (`sources/cryptiana/web/nevers.htm`): the
earliest dated fr.3995 key is June 1580 (no.1). A Nov 1571 table, if the volume holds one, would be among the undated
entries: nos.32-34 (f.62v-63r), 48-51 (f.90-91v) and 71-76 (f.132-142). One eye pass at overview size over those ~25
canvases, looking for a digits-only Italian table with two-figure groups, is the next job (not read here).

Cost and requests: gallica.bnf.fr 400 (3 manifests fetched once for the canvas counts, then read from disk; 397
thumbnails); no subagents; 0 vision calls. Novelty not classified (rule 10).

## fr.3995 undated key tables, eye pass for the Nov 1571 numerical key (BIRAGO-NUM-KEYEYE, 3 Oct 2026)

**Text first.** `sources/cryptiana/web/nevers.htm` (Shift-JIS, hidden comments read too). Tomokiyo's undated fr.3995 entries
and what he says of them: no.32 f.62v "partial reconstruction of substitution cipher mainly by figures", Italian annotation
("Rafaello", "fiorenza", "di parigi"); no.33 f.63r "partial reconstruction ... by figures", Italian ("luigi", "fiorenza");
no.34 f.63r reconstruction of no.47 (1592); no.48 f.90, no.49 f.91r, no.51 f.91v symbols (Mayenne/Aumale/Villars
intercepts); no.50 f.91v letters and figures (Pericard intercept, French); no.71 f.132 figures, French; no.72 f.134 = no.56
(1592); **no.73 f.136 "letters and syllables are represented by figures", Italian instructions**; no.74 f.138 "Zifra con
M[da]ma", figures, polyphonic, Italian; no.75 f.140 French secretaries of state; no.76 f.142 figures/letters/symbols. No hidden
comment ties any of them to Birago or to 1571. Canvases (tools/gallica_folio.py, btv1b525085665): 62v f127, 63r f128,
90r-91v f175-f178, 132r f254, 136r f261, 136v f262, 137r f263, 138r f265, 138v f266, 139r f267, 140r f269, 141r f271, 142r f273.

**Eye pass** (4 contact sheets of 4 leaves at 1000 px, 4 vision calls; 16 Gallica requests + 1 native crop):
- f.136r (no.73) is a **two-figure syllabary**: 1-17 a, ba, ca ... za; 21-40 e, be, ce, che ... ze; 44-61 i ... zi; 65-81
  o ... zo; 87-99 u ... su, then 34 tu, 35 zu; single letters 18 b, 19 c, 20 d, 41 f, 42 g, 43 h, 62 l, 63 m, 64 n, 82 p,
  83 qu, 84 r, 85 s, 86 t, 00 z; letters a-z, et, Greek-like signs for persons (Imperatore, Re di Francia, Re di Spagna,
  Re di Scozia, ..., il Papa, D. Ferrara, D. Urbino, D. Parma, D. Guisa, D. Lorrena, Principe di Ferrara, Principe di Condé,
  Mar[esci]al S. Andrea, Mar. Brisac, D. Savoia, S. Ruy Gomez, D. Sessa, Mar[che]se di Pescara, D. d'Alva, Conte di Feria,
  Gran Turco). The persons named (Saint-André d. 1562, Ruy Gómez d. 1573, Feria d. 1571) date the table to the 1560s, not
  1580s: the right era, and exactly the shape the brief asked for. It was transcribed from one native crop (region
  0,0,4066,4100) into `keys/key_fr3995_no73_f136r.tsv` (100 codes 00-99; 92 H read from the table, 8 M: the overwritten
  numbers 36-40 of the e-row, 34 tu / 35 zu, 00 z).
- f.63r (no.33, "Al S. Luigi ... in Fiorenza - di Parigi") is a regular letter table, two homophones per letter, about 20/42 a,
  21/43 b, 22/44 c ... 40/62 z (read off the overview only). Only 44% of the 514 f.119 + f.100r tokens fall in 20-62, under
  key_crossmatch's 0.5 coverage floor, so it cannot be the letters' key as tabled; not scored.
- f.62v (no.32) is a figure table with letters and marks, too faint at overview size to read; not transcribed.
- f.138v (no.74, "Zifra con Madama") has a letter alphabet A-Z with one- and two-figure codes beneath (A 4 7, B 22 ...),
  names 31-100 and nulls; not transcribed (the brief's one native crop went to no.73).
- f.90-91v (nos.48-51) are symbol alphabets; f.132r, 137r, 139r, 140r, 141r, 142r are blank, covers or offset (the French
  tables of nos.71, 75, 76 are on the versos, not viewed).

**Score** (`num/keyeye/xmatch_no73.py`, output `num/keyeye/xmatch_no73_out.txt`; tools/key_crossmatch.py's own pair_stats,
it model, calibrated gate stat_min 3.292):

| text | key | n | coverage | stat | verdict |
|---|---|---|---|---|---|
| f.119 pairs | no.73 as written | 240 | 0.85 | 1.10 | below gate |
| f.119 pairs | no.73, 01-09 = 1-9 | 240 | 1.00 | 0.85 | below gate |
| f.100r pairs | no.73 as written | 274 | 0.89 | -0.44 | below gate |
| f.100r pairs | no.73, 01-09 = 1-9 | 274 | 1.00 | -0.39 | below gate |
| matched control: synthetic Italian (it16dip) enciphered with this key, 240 tokens, 3 seeds per level | 0 / 10 / 20 / 30% tokens replaced | 240 | 1.00 | 10.5-14.6 / 10.0-12.0 / 8.1-8.4 / 7.2-7.5 | 12/12 hit |

The no.73 syllabary does not read the Nov 1571 letters: control-backed negative at the pair tokenisation on disk.
Conditional on that tokenisation (phase unsettled, 10-30% expected error; the control's random-token corruption to 30% stands
in for it but is not the same as a mis-phased pair stream) and on the f.119 Bourdeau transcription. Caveat: the control's
plaintext comes from it16dip, which may share text with the scoring model and inflate the control. The decode begins
"quodefugicuzepedihuche..." with no words. No token graded; no reading claimed.

Requests: gallica.bnf.fr 17 (16 overview images, 1 native crop; manifest from cache), 1.6 s apart, no block. Vision calls 5.
Novelty not classified (rule 10).

## Remaining gaps (BIRAGO-NUM-TOOLS, 3 Oct 2026)
Read so far: f.36-37: 10 C, 0 S of 947 cipher signs; f.47r: 0 S of about 770; f.117r: 276 signs, all M/U; f.100r + f.119: 0 graded of 1,048 digits.
- f.36-37 period gloss (about 940 glossed signs unread) - blocker: not-attempted; running-line model reads [retired] (Sonnet twice, F36-READ/HARVEST-D; Opus once, F36-GLOSS, known-answer gate at chance); a different instrument is untried: per-sign tiles, two blind passes, known-answer gate first on v36top_L01; next: per-sign tile gloss read, ~$8 (wait until rate limit reads allowed)
- f.36-37 kept rows at E 0.333 (700 positions, 193 splits) - blocker: not-attempted; r36_L01-L08, v36top, v36mid and r37 were read on HARVEST-D's eye grid, which the row-ink profile matched within 10-45 px there; next: one reconciliation call on their splits, disk only, ~$1.5
- f.47r reader error 0.33 - blocker: not-attempted; S74/S54, S80/S65, S76/S91 one-sided third-reader preference unverified; next: known-answer pair check on the f.36 gloss once the gloss is read, disk only, ~$2
- f.47r 79 unsettled positions - blocker: not-attempted; sign-sorter focus rows written; next: tools/sign_sorter.py --focus harvest/f47/la/focus.tsv
- f.47r prose/cipher edges - blocker: not-attempted; the readers marked no prose words, so run edges are unchecked; next: eye-check L01-L03 and L17 s1-s2 crops, disk only, ~$1
- f.117r measured error after the 2-of-3 step - blocker: not-attempted; the 2-of-3 residual is agreement, not error; next: power control at a known-answer look-alike error, disk only, ~$1
- f.117r 12 unsettled tiles - blocker: not-attempted; sorter inputs built (SORTER-BIRAGO2), unpublished; next: the account-3 orchestrator publishes it with {"db": {}}, the owner sorts
- f.117r T88=q - blocker: not-attempted; fitted post-hoc on this letter only; next: pre-registered test on another 1572 leaf with q-words, disk only, ~$1
- f.100r + f.119 (565 + 483 digits) - blocker: not-attempted; joint anneal retired (BIRAGO-NUM3); spelled-crib tests without power (BIRAGO-NUM2, -NUM4); no key on disk (crossmatch control-backed, BIRAGO-NUM-TOOLS); 158 prefix letter design control-backed negative (BIRAGO-NUM-TOOLS); next: the dotted groups and the 1x/5x/8x units read as nomenclator codes against the clear text around each run, disk only, ~$1
- Nov 1571 key table - blocker: not-attempted; page detector failed its in-volume control (BIRAGO-NUM-TOOLS); next: eye pass over fr.3995 undated entries nos.32-34, 48-51, 71-76 (~25 canvases at overview size, 2 vision calls), ~$3

## Escalation (BIRAGO-NUM-TOOLS, 3 Oct 2026)
- [x] siblings: fr.3252 f.36-37 witness read whole under the same key (F36-READ); f.100r pooled with f.119 (BIRAGO-NUM); third numerical letter scouted in both volumes, none (BIRAGO-NUM-SCOUT)
- [x] clear-pages: neighbours and facing pages of all three viewed; no clear copy or slip (Premise check (c)); f.37r slip is clear text
- [x] known-keys: Ceppo-Nevers on f.36-37 and f.47r; 1572 key on f.117r; Nov 1571 system against all 66 digit keys on disk, none at gate, control 6/6 (BIRAGO-NUM-TOOLS)
- [x] print: Gomberville 1665 both parts searched inside; no Birago letter of 1571-72
- [ ] key-rebuild: f.36 gloss by per-sign tiles; f.47r pair check against it; T88=q pre-registered test; f.100r + f.119 dotted groups and 1x/5x/8x units as nomenclator codes against the clear text; fr.3995 undated key tables for a Nov 1571 table
- [x] image-check: f.36r rows recut and re-read (F36R-REREAD); f.36-37 gloss crops re-cut; f.117r native crops; f.47r native re-cut
- [ ] retry: reconciliation call on the kept f.36-37 rows' 193 splits; f.117r power at a measured post-look-alike error
Verdict: keep going: 10 internal gaps; cheapest next: the f.100r + f.119 nomenclator-code reading against the clear text (~$1), then the fr.3995 undated-table eye pass (~$3)

## Remaining gaps (BIRAGO-NUM-KEYEYE, 3 Oct 2026)
Read so far: f.36-37: 10 C, 0 S of 947 cipher signs; f.47r: 0 S of about 770; f.117r: 276 signs, all M/U; f.100r + f.119: 0 graded of 1,048 digits.
- f.36-37 period gloss (about 940 glossed signs unread) - blocker: not-attempted; running-line model reads [retired] (Sonnet twice, F36-READ/HARVEST-D; Opus once, F36-GLOSS, known-answer gate at chance); a different instrument is untried: per-sign tiles, two blind passes, known-answer gate first on v36top_L01; next: per-sign tile gloss read, ~$8 (wait until rate limit reads allowed)
- f.36-37 kept rows at E 0.333 (700 positions, 193 splits) - blocker: not-attempted; r36_L01-L08, v36top, v36mid and r37 were read on HARVEST-D's eye grid, which the row-ink profile matched within 10-45 px there; next: one reconciliation call on their splits, disk only, ~$1.5
- f.47r reader error 0.33 - blocker: not-attempted; S74/S54, S80/S65, S76/S91 one-sided third-reader preference unverified; next: known-answer pair check on the f.36 gloss once the gloss is read, disk only, ~$2
- f.47r 79 unsettled positions - blocker: not-attempted; sign-sorter focus rows written; next: tools/sign_sorter.py --focus harvest/f47/la/focus.tsv
- f.47r prose/cipher edges - blocker: not-attempted; the readers marked no prose words, so run edges are unchecked; next: eye-check L01-L03 and L17 s1-s2 crops, disk only, ~$1
- f.117r measured error after the 2-of-3 step - blocker: not-attempted; the 2-of-3 residual is agreement, not error; next: power control at a known-answer look-alike error, disk only, ~$1
- f.117r 12 unsettled tiles - blocker: not-attempted; sorter inputs built (SORTER-BIRAGO2), unpublished; next: the account-3 orchestrator publishes it with {"db": {}}, the owner sorts
- f.117r T88=q - blocker: not-attempted; fitted post-hoc on this letter only; next: pre-registered test on another 1572 leaf with q-words, disk only, ~$1
- f.100r + f.119 (565 + 483 digits) - blocker: not-attempted; joint anneal retired (BIRAGO-NUM3); spelled-crib tests without power (BIRAGO-NUM2, -NUM4); no key on disk (crossmatch control-backed, BIRAGO-NUM-TOOLS); 158 prefix letter design control-backed negative (BIRAGO-NUM-TOOLS); next: the dotted groups and the 1x/5x/8x units read as nomenclator codes against the clear text around each run, disk only, ~$1
- Nov 1571 key table - blocker: not-attempted; fr.3995 undated entries eye-passed (BIRAGO-NUM-KEYEYE): no.73 syllabary control-backed negative, no.33 under the coverage floor, no.48-51 symbol keys; no.74 (f.138v, Italian, two-figure letter alphabet, canvas f266) and no.32 (f.62v, canvas f127) not transcribed; French nos.71/75/76 tables on versos not viewed; next: native-crop transcription of no.74 and no.32 and the same xmatch_no73.py scoring, ~$3

## Escalation (BIRAGO-NUM-KEYEYE, 3 Oct 2026)
- [x] siblings: fr.3252 f.36-37 witness read whole under the same key (F36-READ); f.100r pooled with f.119 (BIRAGO-NUM); third numerical letter scouted in both volumes, none (BIRAGO-NUM-SCOUT)
- [x] clear-pages: neighbours and facing pages of all three viewed; no clear copy or slip (Premise check (c)); f.37r slip is clear text
- [x] known-keys: Ceppo-Nevers on f.36-37 and f.47r; 1572 key on f.117r; Nov 1571 system against all 66 digit keys on disk, none at gate, control 6/6 (BIRAGO-NUM-TOOLS); fr.3995 no.73 syllabary, stat 1.10/-0.39 vs gate 3.292, control 12/12 (BIRAGO-NUM-KEYEYE)
- [x] print: Gomberville 1665 both parts searched inside; no Birago letter of 1571-72
- [ ] key-rebuild: f.36 gloss by per-sign tiles; f.47r pair check against it; T88=q pre-registered test; f.100r + f.119 dotted groups and 1x/5x/8x units as nomenclator codes against the clear text; fr.3995 no.74 and no.32 tables transcribed and scored for a Nov 1571 table
- [x] image-check: f.36r rows recut and re-read (F36R-REREAD); f.36-37 gloss crops re-cut; f.117r native crops; f.47r native re-cut
- [ ] retry: reconciliation call on the kept f.36-37 rows' 193 splits; f.117r power at a measured post-look-alike error
Verdict: keep going: 10 internal gaps; cheapest next: the f.100r + f.119 nomenclator-code reading against the clear text (~$1), then the fr.3995 no.74 + no.32 transcription and scoring (~$3)

## fr.3995 no.74 and no.32 key tables transcribed and scored (BIRAGO-NUM-KEYEYE2, 3 Oct 2026)

Brief `.claude/briefs/runs/2026-10-03-acct3-birago-num-keyeye2.md`. Crops: `tools/iiif_lines.py --ark btv1b525085665
--canvas 266 --region 150,150,3500,4950` and `--canvas 127 --region 150,1250,3800,2700` (native; regions placed from a
800 px ink profile, no vision call), autocontrast and downscaled to `images/fr3995/read_f138v.jpg` and `read_f62v.jpg`;
one vision call each (2 total). Both tables read at about 0.5-0.6x native, so every letter code is graded M.

- **no.74, f.138v, "Zifra con M[ada]ma"** (`keys/key_fr3995_no74.tsv`, 22 letter codes + 3 nulls + 70 persons; 23 H, 72 M).
  Polyphonic letter alphabet on 1-22: a 4, b|p 7, c|q 22, d|y 8, e 3, f 10, g|m 1, h 12, i 5, l 18, n 2, o 6, r 20, s 17,
  t 11, u 9, x|z 21, vowel homophones 13 e, 14 a, 15 i, 16 o, 19 u written above the vowels (every figure 1-22 used, which
  supports the reading); 23-27 digraph/syllable signs not legible at this scale; 28-30 nulls; 31-100 persons (31 il Papa ...
  59-70 cardinals, 71-74 marshals, 76 D. d'Alva, 77 Ruigomes, 80 C. di Feria, 85 "il S.r Fed.co Gonzaga mio fr.llo", 100 il
  Gran Turco). Card. Tournon and Marshals Saint-André and Termes (all d. 1562) and Card. Borromeo (cr. 1560) put the table
  about 1560-62, and "mio fratello" Federico Gonzaga makes the writer a Gonzaga brother of Nevers. Structural fact: 57% of
  the f.119 tokens and 54% of the f.100r tokens fall in 31-100, which this key spends on persons; the decode is a string of
  titles ("ilducadaluailcontecarloilducadiguisa...").
- **no.32, f.62v, "Al S. Raffaello ... in Fiorenza - di Parigi"** (`keys/key_fr3995_no32.tsv`, 24 codes, all M). Letter
  table with a superscript figure or dot on most codes (a 15/14/10, b 63/61, c 61, d 61, e 99, f 90, g 35, l 10/36, m 64,
  n 25/46, o 54, p 9, q 94, r 53/23, s 56/43, t 41, u 80, & 13; words 36 di, 25 che, 11 con, 7 et): a code+mark design,
  where the mark separates letters sharing two figures (61 b/c/d, 99 e/i). The pair-token files carry no marks, so it is
  scored as polyphonic. Coverage of the targets is 0.24-0.32, under key_crossmatch's 0.5 floor. The faint mirrored
  syllable grid on the right of the leaf (ba 10, ca 19, ... ma 55 me 56 ...) is an offset from a facing sheet; not read.

**Score** (`num/keyeye/xmatch_no74_no32.py`, output `num/keyeye/xmatch_no74_no32_out.txt`; same pair_stats, it model and
gate stat_min 3.292 as xmatch_no73.py; matched control run first in the script):

| key | text | best variant | coverage | stat | verdict |
|---|---|---|---|---|---|
| no.74 | f.119 pairs (240) | as written | 0.78 | 0.26 | below gate (other variants -0.12 to 0.23) |
| no.74 | f.100r pairs (274) | as written | 0.78 | -0.16 | below gate (others -0.69 to -0.45) |
| no.32 | f.119 pairs | as written | 0.24 | 0.79 | below gate, under coverage floor |
| no.32 | f.100r pairs | as written | 0.31 | 1.23 | below gate, under coverage floor |
| matched control no.74: it16dip Italian enciphered with this key (random homophone/polyphone), 240 tokens, 0/10/20/30% replaced, 3 seeds | | | 1.00 | 8.8-12.0 / 5.7-12.0 / 3.8-7.3 / 3.7-6.3 | 12/12 hit |
| matched control no.32 | | | 1.00 | 7.9-12.9 / 6.0-9.4 / 6.9-8.7 / 3.8-9.5 | 12/12 hit |

Variants: codes 01-09 aliased to 1-9; last polyphonic alternative instead of the first; persons dropped. None reaches
the gate. Neither table is the Nov 1571 key at this tokenisation: no.74 is a control-backed negative (and the person
range would fill over half the letters with titles); no.32 cannot be it as tabled (coverage 0.24-0.32, and the control,
at full coverage, does not match that). Conditional on the pair tokenisation (phase unsettled), on the f.119 Bourdeau
transcription, and on table figures read at reduced scale (M). Control caveat as for no.73: it16dip may share text with
the scoring model. No token graded; no reading claimed. Not found in: fr.3995 nos.73, 74, 32 (and no.33 by coverage).

Requests: gallica.bnf.fr 4 (2 x 800 px overview, 2 native regions), >=1.6 s apart, no block; manifest from cache. Vision
calls 2. Novelty not classified (rule 10).

## Remaining gaps (BIRAGO-NUM-KEYEYE2, 3 Oct 2026)
Read so far: f.36-37: 10 C, 0 S of 947 cipher signs; f.47r: 0 S of about 770; f.117r: 276 signs, all M/U; f.100r + f.119: 0 graded of 1,048 digits.
- f.36-37 period gloss (about 940 glossed signs unread) - blocker: not-attempted; running-line model reads [retired] (Sonnet twice, F36-READ/HARVEST-D; Opus once, F36-GLOSS, known-answer gate at chance); a different instrument is untried: per-sign tiles, two blind passes, known-answer gate first on v36top_L01; next: per-sign tile gloss read, ~$8 (wait until rate limit reads allowed)
- f.36-37 kept rows at E 0.333 (700 positions, 193 splits) - blocker: not-attempted; r36_L01-L08, v36top, v36mid and r37 were read on HARVEST-D's eye grid, which the row-ink profile matched within 10-45 px there; next: one reconciliation call on their splits, disk only, ~$1.5
- f.47r reader error 0.33 - blocker: not-attempted; S74/S54, S80/S65, S76/S91 one-sided third-reader preference unverified; next: known-answer pair check on the f.36 gloss once the gloss is read, disk only, ~$2
- f.47r 79 unsettled positions - blocker: not-attempted; sign-sorter focus rows written; next: tools/sign_sorter.py --focus harvest/f47/la/focus.tsv
- f.47r prose/cipher edges - blocker: not-attempted; the readers marked no prose words, so run edges are unchecked; next: eye-check L01-L03 and L17 s1-s2 crops, disk only, ~$1
- f.117r measured error after the 2-of-3 step - blocker: not-attempted; the 2-of-3 residual is agreement, not error; next: power control at a known-answer look-alike error, disk only, ~$1
- f.117r 12 unsettled tiles - blocker: not-attempted; sorter inputs built (SORTER-BIRAGO2), unpublished; next: the account-3 orchestrator publishes it with {"db": {}}, the owner sorts
- f.117r T88=q - blocker: not-attempted; fitted post-hoc on this letter only; next: pre-registered test on another 1572 leaf with q-words, disk only, ~$1
- f.100r + f.119 (565 + 483 digits) - blocker: not-attempted; joint anneal retired (BIRAGO-NUM3); spelled-crib tests without power (BIRAGO-NUM2, -NUM4); no key on disk (crossmatch control-backed, BIRAGO-NUM-TOOLS); 158 prefix letter design control-backed negative (BIRAGO-NUM-TOOLS); next: the dotted groups and the 1x/5x/8x units read as nomenclator codes against the clear text around each run, disk only, ~$1
- Nov 1571 key table - blocker: not-attempted; fr.3995 Italian undated tables all tested (BIRAGO-NUM-KEYEYE, -KEYEYE2): no.73 and no.74 control-backed negatives, no.32 and no.33 under the coverage floor, no.48-51 symbol keys; French nos.71/75/76 tables on the versos (f.132v, 140v, 142v) not viewed; next: one overview vision call on the three versos and, if a two-figure table is there, the same crossmatch, ~$2
- fr.3995 no.74 digraph signs 23-27 and no.32 superscript marks - blocker: not-attempted; read at ~0.5x, values not legible; only matters if a letter in either key turns up; next: none unless a matching letter is found

## Escalation (BIRAGO-NUM-KEYEYE2, 3 Oct 2026)
- [x] siblings: fr.3252 f.36-37 witness read whole under the same key (F36-READ); f.100r pooled with f.119 (BIRAGO-NUM); third numerical letter scouted in both volumes, none (BIRAGO-NUM-SCOUT)
- [x] clear-pages: neighbours and facing pages of all three viewed; no clear copy or slip (Premise check (c)); f.37r slip is clear text
- [x] known-keys: Ceppo-Nevers on f.36-37 and f.47r; 1572 key on f.117r; Nov 1571 system against all 66 digit keys on disk, none at gate, control 6/6 (BIRAGO-NUM-TOOLS); fr.3995 no.73 stat 1.10/-0.39, no.74 0.26/-0.16, no.32 0.79/1.23 (coverage 0.24-0.32) vs gate 3.292, controls 12/12 each (BIRAGO-NUM-KEYEYE, -KEYEYE2)
- [x] print: Gomberville 1665 both parts searched inside; no Birago letter of 1571-72
- [ ] key-rebuild: f.36 gloss by per-sign tiles; f.47r pair check against it; T88=q pre-registered test; f.100r + f.119 dotted groups and 1x/5x/8x units as nomenclator codes against the clear text; fr.3995 French versos nos.71/75/76 for a two-figure table
- [x] image-check: f.36r rows recut and re-read (F36R-REREAD); f.36-37 gloss crops re-cut; f.117r native crops; f.47r native re-cut
- [ ] retry: reconciliation call on the kept f.36-37 rows' 193 splits; f.117r power at a measured post-look-alike error
Verdict: keep going: 11 internal gaps; cheapest next: the f.100r + f.119 nomenclator-code reading against the clear text (~$1), then the fr.3995 French versos overview (~$2)

## fr.3995 French tables nos.71, 75, 76 viewed; no.71 alphabet transcribed and scored (BIRAGO-NUM-KEYEYE3, 3 Oct 2026)

Brief `.claude/briefs/runs/2026-10-03-acct3-birago-num-keyeye3.md`. Canvases from the cached manifest labels: 132v f255,
133r f256, 133v f257, 140v f270, 142v-143r f274 (one opening), 143v f275. Overview: six 800 px images on one contact sheet
(`images/fr3995/sheet_versos_71_75_76.jpg`, 1 vision call). Native crop: `tools/iiif_lines.py --ark btv1b525085665 --canvas
256 --region 200,300,1150,5800` (the alphabet strip and the first word columns), rotated 90 degrees, autocontrast, split in
two halves at 0.85x into `images/fr3995/read_f133r.jpg` (1 vision call). Vision calls 2.

What each table is:
- f.132v (f255): the wrapper of no.71, blank but for an endorsement. f.133v (f257) and f.143v (f275): offset/blank.
- **no.71, f.133r (f256): French nomenclator, code + mark.** Letter alphabet with plain two-figure codes (a 25, b 10, c 65,
  d 75, e 23/24, f 20, g 30, h 40, i 63/64, l 50, m 60, n 73/74, o 85, p 70, q 80, r 1, s 83/84, t 95, u 93/94, x a triangle
  sign, y 97?, z 90?); word columns ("Motz": 11 au, 12 bon, 13 car, 14 ce, 15 ces, 16 de, 17 dit ... 52 si, 53 trop, 54 temps,
  55 ayme, 56 amis, 57 avec, 58 argent ... 92 quant, 93 quil, 94 quoy, 95 recherche, 96 ruyne, 97 rien, 98 suis, 99 vous), towns
  (Auxerre, Orleans, Bourges, Lyon, Dijon, Nevers, Decize, La Charite, Gien ...), military words (73 cavallerie ... 80 Allemans)
  reuse the same figures with a DOT above; persons and offices carry an OVERLINE (6/7/8 Roy, 9 Royne, 10/11/12 Royne mere, 13
  Royne de Navarre, 41 Chevalier d'Aumale, 42 Mr d'Espernon, 43 Mr de Montmorency, 44 Mr de Retz, 45 Mr de Biron, 46 Mr de
  Joyeuse ...). Epernon and Joyeuse as "Mr" with the favourites' rank put the table in the 1580s (about 1581-87), not Nov 1571.
  A second strip "6 7 8 9 a b c ... x" with no legible figures beneath was not read. Key: `keys/key_fr3995_no71_f133r.tsv`
  (24 letter codes H, 2 M).
- **no.75, f.140v (f270):** letter alphabet in display capitals with several homophones per letter running to three figures
  (about 100-129), then "Noms" (M. de Mayenne, Prince de Conde ...), "Villes", "Provinces", "Nulles", "Doubles". Mayenne
  (duke from 1573) and three-figure codes: not a candidate for the two-figure Nov 1571 tokens; not transcribed.
- **no.76, f.142v-143r (f274):** a two-page repertory (alphabet headings A, B, C ... over word columns), too faint at 800 px to
  read its code range; not transcribed (the brief's one native crop went to no.71).

**Score** (`num/keyeye/xmatch_no71.py`, output `num/keyeye/xmatch_no71_out.txt`; same pair_stats and gate stat_min 3.292 as
KEYEYE/KEYEYE2; matched control first, in Italian (it16dip, as before) and in French (fr16, the table's language)). The pair
tokens carry no marks, so only the plain letter codes are scored.

| text | model | key | coverage | stat | verdict |
|---|---|---|---|---|---|
| f.119 pairs (240) | it / fr | as written | 0.26 | -1.09 / -0.44 | below gate, under coverage floor |
| f.119 pairs | it / fr | 0d=d alias | 0.30 | -0.30 / 0.04 | below gate, under coverage floor |
| f.100r pairs (274) | it / fr | as written | 0.27 | 1.65 / -0.71 | below gate, under coverage floor |
| f.100r pairs | it / fr | 0d=d alias | 0.31 | 0.82 / -1.08 | below gate, under coverage floor |
| matched control it16dip, 240 tokens, 0/10/20/30% replaced, 3 seeds | it | | 1.00 | 12.5-15.6 / 9.1-15.4 / 6.8-12.9 / 4.5-7.8 | 12/12 hit |
| matched control fr16, same | fr | | 1.00 | 3.6-19.1 / 3.3-15.5 / 2.2-12.0 / 3.1-9.0 | 9/12 hit (seed 2 weak at every level) |

Structural fact behind the coverage: the f.119 and f.100r token sets have no code in 60-73 at all (they use 00-59 and
74-99), while no.71 puts m, i, c, p and n there; the letters could not be enciphered with this alphabet. no.71 is not the
Nov 1571 key (coverage, and the table dates from the 1580s). Not found in: fr.3995 nos.71 (letter alphabet), 73, 74, 32 (and
nos.33, 75 by range/coverage); no.76 not read. No token graded; no reading claimed. Novelty not classified (rule 10).

Requests: gallica.bnf.fr 7 (6 x 800 px overview, 1 native region), >=1.7 s apart, no block; manifest from cache.

## fr.3995 no.76 not reached (TWO-LOOKS, account 3, 3 Oct 2026)

Brief `.claude/briefs/runs/2026-10-03-acct3-two-looks.md` part (B). Not attempted: the brief's three vision calls were
all used in part (A) (ciphers/fr3621-dinteville-1592, date line). No Gallica request to fr.3995, no crop, no reading;
no.76's code range is still unknown and the fr.3995 sweep stays open on that one table. Next step unchanged (Remaining
gaps, "Nov 1571 key table").

## fr.3995 no.76 alphabet heading read; fr.3995 sweep closed (BIRAGO-76, 3 Oct 2026, account 1)

Brief `.claude/briefs/runs/2026-10-03-acct1-birago-76.md`. Intake gate run 09:23 UTC: "partial (line 1) -- edition/page or
full-text-search citation found within 6 lines", exit 0. Native size of canvas f274 7302 x 5419 (info.json). Crop step:

    python3 tools/iiif_lines.py --ark btv1b525085665 --canvas 274 --region 90,150,1750,5250 \
        --out ciphers/birago-fr3252-1571-72/images/fr3995 --prefix f274h --debug
    -> src_ark_12148_btv1b525085665_f274_90_150_1750_5250.jpg (fetched): region 1750x5250, 18 lines, 18 bands x 1 segments

The opening is written sideways, so the 18 row bands were not reading units (deleted); the fetched strip was rotated 90
degrees clockwise and its top 560 px (the alphabet heading) cut into two crops under 2500 px,
`images/fr3995/f274h_alpha_rot_s1.jpg` and `_s2.jpg` (manifest.json). One vision call on those two crops (plus a
quarter-scale view of the rotated strip to place them).

What no.76's heading is: a **single-sign letter alphabet**, not two-figure codes. Row 1 the letters a-z; under them two or
three substitutes per letter: a 8 / y / +; b 7 / x; c 9 / z; d 5 / K; e 3 / t / w-like sign; f 4 / one sign; g 1 / s-like
sign; h 6 / n; i 2 / r / rho; l a symbol / m; m a symbol / q; n a symbol / o / triangle; o (column cut at the gutter) / #;
p lambda / h; q pi-like / iota; r a symbol / f / rho-like; s small square / e / pi; t a symbol / g; u an s-like sign / d /
tilde; x caret / c; y a symbol / a; z a symbol / b. Then "NVLLES": eight symbols. No figure 0 anywhere in the alphabet; the
figures 1-9 stand only for a-i. Below it, "Motz communs" with **two-figure word codes** in two series: plain (A: Au 12,
Amis 13 ... Artillerie 20; D: Dans 41 ... Don 51; G: Garnison 75 ... Guerre 79; H: Hardy 80 ... Heureux 83) and overlined
(M: Ma 6 ... Mort 17; P: Par 39 ... Propos 51; S: Sa 74 ... Sur 84); the right page holds names and towns ("Noms
generaux", "Noms particuliers", "Dames", "Villes"), not read.

Why it cannot be the Nov 1571 key: f.119 + f.100r are 1,048 digits and nothing else (pooled pairs 476; digit 0 occurs 149
times, 00-05 as pairs 51 times). Under no.76 every letter from l to z is a symbol or a letter, so French or Italian prose
enciphered with it could not come out digit-only; and the brief's step-2 condition (two-figure letter codes able to
produce the 00-59/74-99 set) fails at the heading, so KEYEYE3's crossmatch was not run (no key file written, no control
run, no score: nothing to score). The word series are two-figure, but a letter written only in word codes is not what
f.119/f.100r show (their 158-prefix letter design is already a control-backed negative, BIRAGO-NUM-TOOLS). Not found in:
fr.3995 nos.32, 33, 48-51, 71, 73, 74, 75, 76 -- the fr.3995 sweep for the Nov 1571 key is closed. No token graded; no
reading claimed. Novelty not classified (rule 10).

Requests: gallica.bnf.fr 2 (info.json, one native region), no block.

## Remaining gaps (BIRAGO-NUM-KEYEYE3, 3 Oct 2026)
Read so far: f.36-37: 10 C, 0 S of 947 cipher signs; f.47r: 0 S of about 770; f.117r: 276 signs, all M/U; f.100r + f.119: 0 graded of 1,048 digits.
- f.36-37 period gloss (about 940 glossed signs unread) - blocker: not-attempted; running-line model reads [retired] (Sonnet twice, F36-READ/HARVEST-D; Opus once, F36-GLOSS, known-answer gate at chance); a different instrument is untried: per-sign tiles, two blind passes, known-answer gate first on v36top_L01; next: per-sign tile gloss read, ~$8 (wait until rate limit reads allowed)
- f.36-37 kept rows at E 0.333 (700 positions, 193 splits) - blocker: not-attempted; r36_L01-L08, v36top, v36mid and r37 were read on HARVEST-D's eye grid, which the row-ink profile matched within 10-45 px there; next: one reconciliation call on their splits, disk only, ~$1.5
- f.47r reader error 0.33 - blocker: not-attempted; S74/S54, S80/S65, S76/S91 one-sided third-reader preference unverified; next: known-answer pair check on the f.36 gloss once the gloss is read, disk only, ~$2
- f.47r 79 unsettled positions - blocker: not-attempted; sign-sorter focus rows written; next: tools/sign_sorter.py --focus harvest/f47/la/focus.tsv
- f.47r prose/cipher edges - blocker: not-attempted; the readers marked no prose words, so run edges are unchecked; next: eye-check L01-L03 and L17 s1-s2 crops, disk only, ~$1
- f.117r measured error after the 2-of-3 step - blocker: not-attempted; the 2-of-3 residual is agreement, not error; next: power control at a known-answer look-alike error, disk only, ~$1; TXD-HOLDOUT (3 Oct 2026, ../nevers-birago-fr3251-1572/harvest/tx_decode/holdout/RESULTS.md): TX-DECODE's lattice lam-4 rank 1/201 for f.117r survives the pre-registered held-out control (held-out no.87 lines choose lam 4; printed 1572 key beats all 218 same-design wrong keys, z 6.92; rank 1 at every lam 1-8, z 3.28-3.66), judge still FAIL -1.081 vs real_p05 -0.903; the wrong-key gate alone is weak (passes on 4 of 5 shuffled lattices); no reading, S at best; next: verifier pass on the 32 lam-4 changed positions against the native crops, ~$2
- f.117r 12 unsettled tiles - blocker: not-attempted; sorter inputs built (SORTER-BIRAGO2), unpublished; next: the account-3 orchestrator publishes it with {"db": {}}, the owner sorts
- f.117r T88=q - blocker: not-attempted; fitted post-hoc on this letter only; next: pre-registered test on another 1572 leaf with q-words, disk only, ~$1
- f.100r + f.119 (565 + 483 digits) - blocker: not-attempted; joint anneal retired (BIRAGO-NUM3); spelled-crib tests without power (BIRAGO-NUM2, -NUM4); no key on disk (crossmatch control-backed, BIRAGO-NUM-TOOLS); 158 prefix letter design control-backed negative (BIRAGO-NUM-TOOLS); next: the dotted groups and the 1x/5x/8x units read as nomenclator codes against the clear text around each run, disk only, ~$1
- Nov 1571 key table - blocker: not-attempted; fr.3995 undated tables all viewed (BIRAGO-NUM-KEYEYE, -KEYEYE2, -KEYEYE3): no.73 and no.74 control-backed negatives, no.32, no.33 and no.71 under the coverage floor (no.71 also dated 1580s by Epernon/Joyeuse), no.75 three-figure codes with League-era names, no.48-51 symbol keys; no.76 (f.142v-143r) a faint two-page repertory not read (TWO-LOOKS, 3 Oct 2026, did not reach it: the shared brief's 3 vision calls went to the Dinteville date line); no key table in fr.3995 fits; next: native crop of no.76's alphabet heading only (canvas f274, `tools/iiif_lines.py --ark btv1b525085665 --canvas 274`, region from `images/fr3995/lo_f274.jpg`) to check its code range against the 00-59/74-99 token set (gap 60-73), then KEYEYE3's xmatch with its control first if two-figure, ~$1.5
- fr.3995 no.74 digraph signs 23-27 and no.32 superscript marks - blocker: not-attempted; read at ~0.5x, values not legible; only matters if a letter in either key turns up; next: none unless a matching letter is found

## Escalation (BIRAGO-NUM-KEYEYE3, 3 Oct 2026)
- [x] siblings: fr.3252 f.36-37 witness read whole under the same key (F36-READ); f.100r pooled with f.119 (BIRAGO-NUM); third numerical letter scouted in both volumes, none (BIRAGO-NUM-SCOUT)
- [x] clear-pages: neighbours and facing pages of all three viewed; no clear copy or slip (Premise check (c)); f.37r slip is clear text
- [x] known-keys: Ceppo-Nevers on f.36-37 and f.47r; 1572 key on f.117r; Nov 1571 system against all 66 digit keys on disk, none at gate, control 6/6 (BIRAGO-NUM-TOOLS); fr.3995 no.73 stat 1.10/-0.39, no.74 0.26/-0.16, no.32 0.79/1.23 (coverage 0.24-0.32) vs gate 3.292, controls 12/12 each (BIRAGO-NUM-KEYEYE, -KEYEYE2); no.71 letters coverage 0.26-0.31, stat -1.09 to 1.65, controls it 12/12, fr 9/12 (BIRAGO-NUM-KEYEYE3)
- [x] print: Gomberville 1665 both parts searched inside; no Birago letter of 1571-72
- [ ] key-rebuild: f.36 gloss by per-sign tiles; f.47r pair check against it; T88=q pre-registered test; f.100r + f.119 dotted groups and 1x/5x/8x units as nomenclator codes against the clear text; fr.3995 no.76 (f.142v-143r) alphabet heading for the code range
- [x] image-check: f.36r rows recut and re-read (F36R-REREAD); f.36-37 gloss crops re-cut; f.117r native crops; f.47r native re-cut
- [ ] retry: reconciliation call on the kept f.36-37 rows' 193 splits; f.117r power at a measured post-look-alike error
Verdict: keep going: 11 internal gaps; cheapest next: the f.100r + f.119 nomenclator-code reading against the clear text (~$1), then the fr.3995 no.76 heading crop (~$1.5)

## Remaining gaps (BIRAGO-76, 3 Oct 2026)
Read so far: f.36-37: 10 C, 0 S of 947 cipher signs; f.47r: 0 S of about 770; f.117r: 276 signs, all M/U; f.100r + f.119: 0 graded of 1,048 digits.
- f.36-37 period gloss (about 940 glossed signs unread) - blocker: not-attempted; running-line model reads [retired] (Sonnet twice, F36-READ/HARVEST-D; Opus once, F36-GLOSS, known-answer gate at chance); a different instrument is untried: per-sign tiles, two blind passes, known-answer gate first on v36top_L01; next: per-sign tile gloss read, ~$8 (wait until rate limit reads allowed)
- f.36-37 kept rows at E 0.333 (700 positions, 193 splits) - blocker: not-attempted; r36_L01-L08, v36top, v36mid and r37 were read on HARVEST-D's eye grid, which the row-ink profile matched within 10-45 px there; next: one reconciliation call on their splits, disk only, ~$1.5
- f.47r reader error 0.33 - blocker: not-attempted; S74/S54, S80/S65, S76/S91 one-sided third-reader preference unverified; next: known-answer pair check on the f.36 gloss once the gloss is read, disk only, ~$2
- f.47r 79 unsettled positions - blocker: not-attempted; sign-sorter focus rows written; next: tools/sign_sorter.py --focus harvest/f47/la/focus.tsv
- f.47r prose/cipher edges - blocker: not-attempted; the readers marked no prose words, so run edges are unchecked; next: eye-check L01-L03 and L17 s1-s2 crops, disk only, ~$1
- f.117r measured error after the 2-of-3 step - blocker: not-attempted; the 2-of-3 residual is agreement, not error; next: power control at a known-answer look-alike error, disk only, ~$1; TXD-HOLDOUT (3 Oct 2026, ../nevers-birago-fr3251-1572/harvest/tx_decode/holdout/RESULTS.md): TX-DECODE's lattice lam-4 rank 1/201 for f.117r survives the pre-registered held-out control (held-out no.87 lines choose lam 4; printed 1572 key beats all 218 same-design wrong keys, z 6.92; rank 1 at every lam 1-8, z 3.28-3.66), judge still FAIL -1.081 vs real_p05 -0.903; the wrong-key gate alone is weak (passes on 4 of 5 shuffled lattices); no reading, S at best; next: verifier pass on the 32 lam-4 changed positions against the native crops, ~$2
- f.117r 12 unsettled tiles - blocker: not-attempted; sorter inputs built (SORTER-BIRAGO2), unpublished; next: the account-3 orchestrator publishes it with {"db": {}}, the owner sorts
- f.117r T88=q - blocker: not-attempted; fitted post-hoc on this letter only; next: pre-registered test on another 1572 leaf with q-words, disk only, ~$1
- f.100r + f.119 (565 + 483 digits) - blocker: not-attempted; joint anneal retired (BIRAGO-NUM3); spelled-crib tests without power (BIRAGO-NUM2, -NUM4); no key on disk (crossmatch control-backed, BIRAGO-NUM-TOOLS); 158 prefix letter design control-backed negative (BIRAGO-NUM-TOOLS); next: the dotted groups and the 1x/5x/8x units read as nomenclator codes against the clear text around each run, disk only, ~$1
- Nov 1571 key table - blocker: no-key-material; fr.3995 undated tables all viewed and the sweep is closed (BIRAGO-NUM-KEYEYE, -KEYEYE2, -KEYEYE3, BIRAGO-76): no.73 and no.74 control-backed negatives, no.32, no.33 and no.71 under the coverage floor (no.71 also 1580s), no.75 three-figure codes with League-era names, no.48-51 symbol keys, no.76 a single-sign letter alphabet (digits 1-9 for a-i, symbols and letters for l-z, no 0) with two-figure word codes in a plain and an overlined series (BIRAGO-76); no key table in fr.3995 fits the digit-only 00-59/74-99 token set; the next instrument is new material: a Nov 1571 key in another volume of the Nevers/Birago papers (fr.3252 neighbours, fr.3251, fr.3256, fr.4712-4715 key sheets) located by a catalogue/eye sweep for "chiffre" leaves dated 1571-72
- fr.3995 no.74 digraph signs 23-27 and no.32 superscript marks - blocker: not-attempted; read at ~0.5x, values not legible; only matters if a letter in either key turns up; next: none unless a matching letter is found

## Escalation (BIRAGO-76, 3 Oct 2026)
- [x] siblings: fr.3252 f.36-37 witness read whole under the same key (F36-READ); f.100r pooled with f.119 (BIRAGO-NUM); third numerical letter scouted in both volumes, none (BIRAGO-NUM-SCOUT)
- [x] clear-pages: neighbours and facing pages of all three viewed; no clear copy or slip (Premise check (c)); f.37r slip is clear text
- [x] known-keys: Ceppo-Nevers on f.36-37 and f.47r; 1572 key on f.117r; Nov 1571 system against all 66 digit keys on disk, none at gate, control 6/6 (BIRAGO-NUM-TOOLS); fr.3995 no.73 stat 1.10/-0.39, no.74 0.26/-0.16, no.32 0.79/1.23 (coverage 0.24-0.32) vs gate 3.292, controls 12/12 each (BIRAGO-NUM-KEYEYE, -KEYEYE2); no.71 letters coverage 0.26-0.31, stat -1.09 to 1.65, controls it 12/12, fr 9/12 (BIRAGO-NUM-KEYEYE3); no.76 single-sign letters, not two-figure, crossmatch not applicable (BIRAGO-76)
- [x] print: Gomberville 1665 both parts searched inside; no Birago letter of 1571-72
- [ ] key-rebuild: f.36 gloss by per-sign tiles; f.47r pair check against it; T88=q pre-registered test; f.100r + f.119 dotted groups and 1x/5x/8x units as nomenclator codes against the clear text
- [x] image-check: f.36r rows recut and re-read (F36R-REREAD); f.36-37 gloss crops re-cut; f.117r native crops; f.47r native re-cut
- [ ] retry: reconciliation call on the kept f.36-37 rows' 193 splits; f.117r power at a measured post-look-alike error
Verdict: keep going: 10 internal gaps; cheapest next: the f.100r + f.119 nomenclator-code reading against the clear text (~$1); the Nov 1571 key table now needs new material (a key sheet in another Nevers/Birago volume)

## TXD-HOLDOUT (3 Oct 2026, account-1 worker for LANE-A1): f.117r lam-4 rank 1 held-out control
See `../nevers-birago-fr3251-1572/NOTES.md` "TXD-HOLDOUT" and `.../harvest/tx_decode/holdout/RESULTS.md`. For f.117r (no.77):
held-out no.87 lines choose lam 4; the printed 1572 key beats all 218 same-design wrong keys at lam 4 (z 6.92 vs W1; that
gate also passes on 4 of 5 position-shuffled f.117r lattices, so it is weak on its own); rank 1 of 201 value-shuffled keys
at every lam 1-8 (z 3.28-3.66); judge FAIL -1.081 (real_p05 -0.903; shuffled-target decode -1.382). **Verdict: lam-4 rank 1
survives held-out control.** No reading committed, S at best, no class.

## A1-POSNULL (3 Oct 2026, account-1 worker for LANE-A1): position-shuffled-lattice null for the printed 1572 key at lam 4
Brief `.claude/briefs/runs/2026-10-03-acct3-a1-wave7.md` job 1; PREREG `../nevers-birago-fr3251-1572/harvest/tx_decode/posnull/PREREG.md` (d05de564, before
any score); results `posnull/RESULTS.md`, `posnull.json`. Replaces TXD-HOLDOUT's gate (a), which passed on 9/15 shuffled lattices.
200 position-shuffled lattices per leaf (same per-position candidate sets, positions permuted), printed key, lam 4. Gate: real
rank 1/201 among value-shuffled keys AND real score > shuffled p95.
- f.144r: real -0.945 vs shuffled p95 -1.096 (max -0.956); rank 1; shuffled rank-1 2/200. **PASS** (thin: 0.011 over max).
- f.168: real -1.019 vs shuffled p95 -1.299 (max -1.209); rank 1; shuffled rank-1 0/200. **PASS.**
- f.117r (fr.3252): real -1.081 vs shuffled p95 -1.334 (max -1.297); rank 1; shuffled rank-1 0/200. **PASS.**
Licenses only that the real sign order carries the key's language signal beyond the position-shuffled null; no reading, no
grade change (a separate verifier would be needed), nothing above S, no class. Next as before: the verifier pass on the lam-4
changed positions against the crops (~$2 each).

## A1-BIR-EYE (3 Oct 2026, account-1 worker for LANE-A1): f.117r lam-4 changed positions, blind eye check

See `../nevers-birago-fr3251-1572/NOTES.md` "A1-BIR-EYE" and `.../harvest/tx_decode/eye/RESULTS.md`, pre-registered at
632c8786 before any crop was shown. On f.117r one blind Opus reader picked the key-implied sign at 27 of the 32 positions
the printed 1572 key's lam-4 decode changed, against 3 of 32 swap picks at decoy positions (binomial p 8.9e-21): **PASS**.
There are 19 S candidates for a verifier (eye/score.json, `f117`). No grade was applied, no reading committed and no novelty
classed. Next: a separate verifier on those 19 against the crops, ~$2.


## A1-BIR-VERIFY (3 Oct 2026, account-1 verifier for LANE-A1, a separate session): A1-BIR-EYE's 28 S candidates checked
Full record in `nevers-birago-fr3251-1572/harvest/tx_decode/eye/verify/RESULTS-VERIFY.md` (prereg 594c0f26). The decoy draw
reproduces (same seed, same counts) but was not matched on ambiguity: A1-BIR-EYE's decoys were easy positions. A new blind reader with an
ambiguity-matched decoy arm found: f.117r (re-cut at the original band height) G1 27/32 vs 5/32 PASS, matched 24/26 vs 15/30 PASS, so
19/19 kept; f.168 G1 10/11 vs 1/11, matched 5/5 vs 3/7 PASS, so 5/5 kept; f.144r G1 6/12 vs 0/12 but matched 5/8 vs 6/12 FAIL, so 0/4 kept
(dropped: L05:32, L04.1:7, L05:7, L06:7). The 24 kept positions are applied at S in `decode_verify.json` (decode --check exit 0). Grades:
f.117r H0 C0 S179 M74 I0 U26; f.168 H0 C0 S90 M22 I0 U10; f.144r H0 C0 S40 M36 I0 U14. Judge FAIL on all three (f.117r -1.294 vs
real_p05 -0.907, f.168 -1.238 vs -0.975, f.144r -1.454 vs -0.955). This is a cryptanalytic result, not a reading. Next: a third blind reader on
f.144r's 4 dropped positions plus matched decoys, ~$3, only if new crops (native re-capture) are available.

## BIR-ROUND2 (3 Oct 2026, account-3 worker): round-2 lattice on the M tokens, and the U-token check against the printed key
Full record in `nevers-birago-fr3251-1572/harvest/tx_decode/eye/round2/RESULTS-ROUND2.md` (prereg 923a783f, pushed before any score).
With A1-BIR-VERIFY's 24 S positions pinned, H positions pinned and look-alike partners added at the M positions, the lam-4 lattice
changes 13 / 6 / 13 positions (f.117r / f.168 / f.144r). All of them were already asked in A1-BIR-EYE or A1-BIR-VERIFY and not
kept. There are **0 new positions on every leaf, so the round is untestable at this N** under the pre-registered rule, and no reader call
was made. Nothing changed: decode --check exit 0, grades f.117r H0 C0 S179 M74 I0 U26, f.168 H0 C0 S90 M22 I0 U10, f.144r H0 C0
S40 M36 I0 U14, and the judge lines are as A1-BIR-VERIFY's (FAIL on all three). Position null on the round-2 base: PASS on all three: real key rank 1/201 and real S above every one of 200 shuffled lattices (f.117r -1.081 vs p95 -1.521, z 4.97 vs shuffled p95 1.42; f.168 -1.019 vs -1.425, z 3.61 vs 0.96; f.144r -0.998 vs -1.197, z 3.08 vs 1.56; 111 s). Pinning the 24 S and H positions keeps the key separable from the null (A1-POSNULL z on the unpinned lattices: 3.66 / 2.77 / 3.10), but this gate licenses nothing without reader questions.
The A/B lattice instrument is exhausted on these leaves at lam 4. Next is a different instrument: an open-choice blind re-read of the
M positions against the full sign sheet, which adds candidates, and then the lattice (~3 vision calls, ~$5).
U tokens (`round2/u_tokens.tsv`, report only): the printed key has no null and 8 word or name codes. A digit pair "4 7" recurs on
f.117r L02 and f.144r L04.1 (both readers), and "1 6" appears on f.144r L05. Their shape class is the printed digit name codes
(85/86/89), but they are not in the printed key; values unknown. An "up triangle over cross" resembles quello (T84) in reverse
orientation. No other off-sheet shape matches a printed code. Next: pooled 47/16 count across the 1572 leaves, disk only, ~$1.
Cryptanalytic result only; no reading claimed, no novelty classed.
## BIR-OPEN (3 Oct 2026, account-3 worker): open-choice blind re-read of the M positions, then lattice lam 4
The full record is in `nevers-birago-fr3251-1572/harvest/tx_decode/eye/open/RESULTS-OPEN.md`. The prereg (e5076ee1) was pushed before any crop or score.
This is the different instrument BIR-ROUND2 named. Each reader saw a masked orientation, the native line crops and the whole sign sheet, and
was asked for any sheet id, OTHER or U at each of the 74 f.117r / 22 f.168 M positions. Equal sign-matched H decoys were mixed in. There were 3 fresh blind Opus readers.
- Calibration on the H decoys: f.117r 70/74 (0.95), f.168 22/22 (1.00), both PASS (gate 0.80). T60 decoys read T60 9/10 and 2/2.
- Change rate on M targets: f.117r 41/74, f.168 12/22. The lattice (open answers added as candidates) agrees at H/M on 24 / 6. Posnull PASS on
  both (rank 1/201; z 4.88 / 3.25).
- New S candidates (value changes): f.117r 12 (T60->T86 x5, T65->T51 x5, T95->T51, T98->T18). f.168 4 (T60->T86 x2, T56->T97, T19->T33).
  They are in `open/exceptions_open_<leaf>.tsv` (`open/decode_open.json`), decode --check exit 0.
- The M targets included A1-BIR-VERIFY's 24 exception positions. Open reads replicate 11/19 (f.117r) and 2/5 (f.168). 11 conflict, mainly
  T95 vs T51 (6) and T83 vs T24 (2). The T65/T95/T51 three-way is unsettled, so it goes to the owner's sorter. A1's rows are left unchanged.
- **Grades unchanged** in the tokens file (f.117r H0 C0 S179 M74 U26, f.168 H0 C0 S90 M22 U10). decode_key.py grades an exception on a
  conf-M transcription row as M. So A1's 24 "applied at S" and these 16 are value changes, not S grades. Flagged for the orchestrator.
- Judge: f.117r FAIL -1.224 (before -1.301; real_p05 -0.899). f.168 FAIL -1.150 (before -1.242; real_p05 -0.992). The gain is partly circular.
Cryptanalytic result only. No reading claimed, no novelty classed.
Next: owner sign sorter on T65/T95/T51 and T83/T24 (focus list = the 11 conflicts + 6 T5x survivors). Then decide whether open-read
survivors on conf-M rows may carry grade S (tool/grade policy, orchestrator). Then f.144r with the same instrument (~3 vision calls, ~$5).

## BIR-APPLY (3 Oct 2026, account-3 worker): orchestrator grade policy applied to the f.117r / f.168 lattice corrections
Policy (account-3 orchestrator, 3 Oct 2026, answering BIR-OPEN's flag): a lattice correction is S only where two independent blind
instruments agree on the sign: A1-BIR-VERIFY's two-option check (ambiguity-matched decoys) AND BIR-OPEN's open-choice re-read (H-decoy
calibrated). Everything else stays M.
- Files: `nevers-birago-fr3251-1572/harvest/tx_decode/eye/apply/` -- `exceptions_apply_f117.tsv` (S 11, M 20), `exceptions_apply_f168.tsv`
  (S 2, M 7), `decode_apply.json` (`exception_grade_overrides_conf: true` on the f.117r and f.168 jobs; the f.144r job unchanged). The reason
  column names the instrument(s): "A1 and BIR-OPEN agree" (S), "A1 vs BIR-OPEN conflict (owner sorter)" (M, 11 rows), "BIR-OPEN single
  instrument only" (M, 16 rows). Values are BIR-OPEN's (`open/`) unchanged; only grades move, so the reading text is identical to
  `open/reading_<leaf>_open.txt` below its header.
- `python3 tools/decode_key.py ciphers/nevers-birago-fr3251-1572 --config ciphers/nevers-birago-fr3251-1572/harvest/tx_decode/eye/apply/decode_apply.json --check`:
  exit 0, "reading up to date". Per leaf (rule 4): **f.117r H 0, C 0, S 190, M 63, I 0, U 26** (was S 179, M 74);
  **f.168 H 0, C 0, S 92, M 20, I 0, U 10** (was S 90, M 22); f.144r unchanged (S 40, M 36, U 14).
- Judge (letters only, brackets and separators stripped, the same extraction as BIR-OPEN; values unchanged, so the scores are BIR-OPEN's):

      $ python3 tools/judge_plaintext.py specs/birago-fr3252-f117.json --file <f117 letters>
      FAIL language: score=-1.224, null_p99=-1.813, real_p05=-0.899, real_median=-0.782, mode=both, N=246
      FAIL - birago-fr3252-f117 (a PASS is a gate for a verifier, not a reading; rule 10)
      $ python3 tools/judge_plaintext.py specs/nevers-birago-fr3251-1572.json --file <f168 letters>
      FAIL language: score=-1.15, null_p99=-1.622, real_p05=-0.992, real_median=-0.824, mode=both, N=111
      FAIL - nevers-birago-fr3251-1572 (a PASS is a gate for a verifier, not a reading; rule 10)
- Sorter focus: `harvest/tx_decode/eye/open/sorter/focus.tsv` (+ README): 17 tiles, the 11 conflicts (T95/T51 x5, T66/T76, X_NEW/T84,
  T13/T64 on f.117r; T83/T24 x2, T51/T95 on f.168) and the 6 f.117r BIR-OPEN-only T65/T95->T51 moves, with crop paths from the two existing
  sorters' signs.tsv. f117 L09 and f168 R03 have one tile fewer than transcribed positions, so those rows may be one tile off and L09.30
  has no tile. Ready for the orchestrator to build and publish; nothing published here.
Cryptanalytic result only (no H or C). No reading claimed; not classed for novelty.
Next: owner sign sorter on the focus list; then f.144r with the BIR-OPEN instrument (~3 vision calls, ~$5).

## BIR-OWNER (3 Oct 2026, account-3 worker): the owner's partial sign-sorter picks scored as a third reader on f.117r, f.168, f.144r
Full record: `nevers-birago-fr3251-1572/harvest/tx_decode/eye/open/sorter/RESULTS-OWNER.md` (prereg 8bbb3861, pushed before any score).
The owner's save (partial; the owner's words: "doesn't mean they're right") went through `tools/sign_sorter_apply.py` unchanged: 488 tiles, 68 moved,
58 taken out, 11 bad cuts, 5 set aside. Grade rule: S where the owner's sign equals a blind instrument's read at that position (A1-BIR-VERIFY,
BIR-OPEN, BIR-OPEN-144), M owner-only, U a move into a new pile. Gate: (b) the owner's picks must beat (a) the base and the p95 of (c), 200 random
same-size change sets drawn from the lattice's top-k look-alikes.
- f.117r: 24 changes (S 3, M 11, U 10). (b) is worse than the base and inside the control: FAIL.
      a  FAIL language: score=-1.215, null_p99=-1.797, real_p05=-0.907, real_median=-0.791, mode=both, N=266
      b  FAIL language: score=-1.32, null_p99=-1.776, real_p05=-0.893, real_median=-0.782, mode=both, N=256   (control p95 -1.234; rank 118/201)
- f.168: 14 changes (S 1, M 9, U 4). (b) is worse than 198 of 200 random draws: FAIL.
      a  FAIL language: score=-1.149, null_p99=-1.64, real_p05=-0.975, real_median=-0.821, mode=both, N=114
      b  FAIL language: score=-1.418, null_p99=-1.622, real_p05=-0.992, real_median=-0.824, mode=both, N=111  (control p95 -1.146; rank 199/201)
- f.144r: 17 changes (S 1, M 7, U 9). (b) beats the base and the control: PASS (rank 2/201). Applied in `.../sorter/decode_owner144.json`, decode
  --check exit 0: H 0 C 0 S 39 M 32 I 0 U 19 (was S 42 M 34 U 14).
      a  FAIL language: score=-1.418, null_p99=-1.614, real_p05=-0.954, real_median=-0.817, mode=both, N=91
      b  FAIL language: score=-1.266, null_p99=-1.614, real_p05=-0.954, real_median=-0.817, mode=both, N=91   (control p95 -1.346)
- Pooled: (a) -1.239, (b) -1.333, control p95 -1.255: FAIL. The owner's picks agree with the blind machine reads 1-5 times in 6-24 per leaf and
  instrument. On the T65/T95/T51 conflicts the owner mostly gave a third answer (T65 or a new pile). Of the 25 focus tiles the owner touched 21
  (15 moved, 5 aside, 1 bad cut). Those letter scores are averages over the 4-gram LM. The f.144r gain is on one leaf of three and still far
  below real_p05.
Cryptanalytic result only. No reading claimed, H 0 C 0, no novelty classed.
Next: what to sort next, ranked by score gain in `.../sorter/sort_next.tsv`: f.144r L06.1 (bad cut, recut), L05.7 (aside), L04.1.1, L05.6;
f.168 R03.6, V03.5, V03.23; f.117r gains are small (<=0.02). Also a native re-capture of the 11 bad-cut tiles. Per the README, a fourth look goes to the
owner-only disagreements, the 11 M picks on f.117r and 9 on f.168. Sorting the new piles (T60-c holds 7 tiles across leaves: 4 from T65, 1 each from T95, T36 and T60) against the sheet
would turn U back into values, ~$1 apply after the next save.

## N8-BIRNUM (4 Oct 2026, account-2 worker for LANE-NEAR8): dotted groups and 1x/5x/8x units as nomenclator codes

Brief `.claude/briefs/runs/2026-10-04-ytbiz-near8-wave1.md` (job N8-BIRNUM). Files in `num/codes/`. `PREREG.md` pushed in 433a6233 before
any statistic. Inputs as BIRAGO-NUM (f.100r reconciliation; Bourdeau's f.119 ct2, cyphersolver `targets/birago`, MIT / CC BY 4.0). A different
instrument from the retired anneal and the two spelled-crib tests: code reading from the context around each occurrence plus the leaf's clear text.

**Units (rule-fixed).** Family D, dotted groups: 5 types with pooled count >= 2 -- 41 x8 (both letters), 21 x8, 18 x4, 10 x4, 25 x3 (27
occurrences). Family U, 1x/5x/8x units of the 158 parse with pooled count 2-8: 12 x5, 10 x5, 84 x4, 14 x4, 83 x3, 53 x2 (23 occurrences).

**Step B, cipher context** (`num/codes/codes_test.py` -> `out.txt`). Statistic T = sum over types of (largest group of identical 2-digit left or
right flanks - 1). A name/title code after a fixed article or preposition would repeat its flanks. Null: the same counts at random positions in the
same streams, 2000 draws.

| family | T | null mean | p95 | p99 | max | p | gate (> p99) |
|---|---|---|---|---|---|---|---|
| D dotted groups | 4 | 1.70 | 3 | 4 | 6 | 0.045 | no pass |
| U 1x/5x/8x units | 3 | 0.93 | 2 | 3 | 4 | 0.050 | no pass |

Power control as pre-registered (synthetic it16dip, 40 cells, 5% strays, the 3 most frequent words of length >= 4 occurring >= 3 times planted as
codes): **0/20** trials beat their own p99, but in 13 of the 20 no word qualified, so nothing was planted and that control did not match the
target's 27 code occurrences. Post-hoc qualifier, not gating (`matched_control.py` -> `matched_control_out.txt`): the 5 most frequent words planted
with the target's own profile (8, 8, 4, 4, 3; 13-22 code occurrences realised): **2/20 at 40 cells, 4/20 at 30 cells**. Both are below the
pre-registered 0.5 power floor. **Step B is untested-by-this-tool at this N.** Neither family passes, and a real word code under a 30-40-cell
homophonic table would also miss 80-90% of the time, because its flanks are spread over the homophones. The two p ~ 0.05 results are not evidence
either way.

**Step A, clear context** (f.100r clear text read by this worker from `images/c101.jpg`, 1600 px, itself M-grade). Entity rule: f.100r's clear
text names several entities twice or more -- Monsignor di Bellagarda, la Valletta, Carmagnola, the Commissario (Battista), Sua Maestà, the Re, V.E.,
"fraschetta" -- so no candidate set is a singleton. f.119's clear text is not on disk, so f.119-only types cannot qualify. Slot rule: all four f.100r
clear boundaries ("harebbe a caro | 76 ÷ ...", "... 7 6 7 7 6 | Io dico la pura et mera uerità | ÷ 7 0 8 9 ...", "... 3 0 7 6 ÷ | Ho mandato ...")
are taken by the 76 / wavy delimiter. No dotted group or 1x/5x/8x unit stands within 2 units of clear text. **No meaning is licensed. 0 tokens
graded** (H 0, C 0, S 0, M 0). This is the outcome the PREREG stated in advance under its own rules.

Observation for the record, not a test: dotted 25 is followed by 15 or 9 15 at all three of its occurrences (f.100r L03 "2. 5. 1 5", L11 "2. 5. 1
5", f.119 "2~ 5- 9 1 5"). Dotted 41 has left flank "8 2" once in each letter. Both are inside the null's range (s = 1 per type).

**Verdict: no reading; untested-by-this-tool, not a negative.** Over two letters (1,048 digits) the clear context licenses no code meaning, and the
cipher-context flank statistic has 10-20% power. This is the fourth instrument on the Nov 1571 system without a result (anneal retired; two crib
designs and this code reading without power). Every one of them is limited by N. The next step is new material: BIRAGO-NUM-SCOUT's f.138 (7 Feb 1572)
check, digit shape and shared 6-mers against f.100r/f.119, to see whether it is a third letter in this key rather than in the 1572 key. Suggestion
only, not started: read f.119's clear text (1 Gallica region + 1 Sonnet read) so that the entity rule can be applied to 41/21/25 across both
letters. NEAR.md row unchanged: this result is on the numerical letters, not on the f.47r/f.117r near-solve evidence. Novelty not classified (rule 10).

Cost and requests: disk only, 0 network requests, 0 subagent calls, 1 image read by this worker (c101.jpg, on disk). Cost: see the lane ledger.

## Remaining gaps (N8-BIRNUM, 4 Oct 2026)
Read so far: f.36-37: 10 C, 0 S of 947 cipher signs; f.47r: 0 S of about 770; f.117r: 276 signs, all M/U; f.100r + f.119: 0 graded of 1,048 digits.
- f.36-37 period gloss (about 940 glossed signs unread) - blocker: not-attempted; running-line model reads [retired] (Sonnet twice, F36-READ/HARVEST-D; Opus once, F36-GLOSS, known-answer gate at chance); a different instrument is untried: per-sign tiles, two blind passes, known-answer gate first on v36top_L01; next: per-sign tile gloss read, ~$8 (wait until rate limit reads allowed)
- f.36-37 kept rows at E 0.333 (700 positions, 193 splits) - blocker: not-attempted; r36_L01-L08, v36top, v36mid and r37 were read on HARVEST-D's eye grid, which the row-ink profile matched within 10-45 px there; next: one reconciliation call on their splits, disk only, ~$1.5
- f.47r reader error 0.33 - blocker: not-attempted; S74/S54, S80/S65, S76/S91 one-sided third-reader preference unverified; next: known-answer pair check on the f.36 gloss once the gloss is read, disk only, ~$2
- f.47r 79 unsettled positions - blocker: not-attempted; sign-sorter focus rows written; next: tools/sign_sorter.py --focus harvest/f47/la/focus.tsv
- f.47r prose/cipher edges - blocker: not-attempted; the readers marked no prose words, so run edges are unchecked; next: eye-check L01-L03 and L17 s1-s2 crops, disk only, ~$1
- f.117r measured error after the 2-of-3 step - blocker: not-attempted; the 2-of-3 residual is agreement, not error; next: power control at a known-answer look-alike error, disk only, ~$1; TXD-HOLDOUT (3 Oct 2026, ../nevers-birago-fr3251-1572/harvest/tx_decode/holdout/RESULTS.md): TX-DECODE's lattice lam-4 rank 1/201 for f.117r survives the pre-registered held-out control (held-out no.87 lines choose lam 4; printed 1572 key beats all 218 same-design wrong keys, z 6.92; rank 1 at every lam 1-8, z 3.28-3.66), judge still FAIL -1.081 vs real_p05 -0.903; the wrong-key gate alone is weak (passes on 4 of 5 shuffled lattices); no reading, S at best; next: verifier pass on the 32 lam-4 changed positions against the native crops, ~$2
- f.117r 12 unsettled tiles - blocker: not-attempted; sorter inputs built (SORTER-BIRAGO2), unpublished; next: the account-3 orchestrator publishes it with {"db": {}}, the owner sorts
- f.117r T88=q - blocker: not-attempted; fitted post-hoc on this letter only; next: pre-registered test on another 1572 leaf with q-words, disk only, ~$1
- f.100r + f.119 (565 + 483 digits) - blocker: not-attempted; joint anneal retired (BIRAGO-NUM3); spelled-crib tests without power (BIRAGO-NUM2, -NUM4); no key on disk (crossmatch control-backed, BIRAGO-NUM-TOOLS); 158 prefix letter design control-backed negative (BIRAGO-NUM-TOOLS); dotted groups and 1x/5x/8x units as nomenclator codes untested-by-this-tool (flank statistic, matched control power 2-4/20, N8-BIRNUM), no meaning licensed by the f.100r clear context; next: new material -- f.138 (7 Feb 1572) digit shape and 6-mer overlap against f.100r/f.119 (BIRAGO-NUM-SCOUT's suggestion; a third letter in this key raises N for every instrument above), ~$1
- Nov 1571 key table - blocker: no-key-material; fr.3995 undated tables all viewed and the sweep is closed (BIRAGO-NUM-KEYEYE, -KEYEYE2, -KEYEYE3, BIRAGO-76): no.73 and no.74 control-backed negatives, no.32, no.33 and no.71 under the coverage floor (no.71 also 1580s), no.75 three-figure codes with League-era names, no.48-51 symbol keys, no.76 a single-sign letter alphabet (digits 1-9 for a-i, symbols and letters for l-z, no 0) with two-figure word codes in a plain and an overlined series (BIRAGO-76); no key table in fr.3995 fits the digit-only 00-59/74-99 token set; the next instrument is new material: a Nov 1571 key in another volume of the Nevers/Birago papers (fr.3252 neighbours, fr.3251, fr.3256, fr.4712-4715 key sheets) located by a catalogue/eye sweep for "chiffre" leaves dated 1571-72
- fr.3995 no.74 digraph signs 23-27 and no.32 superscript marks - blocker: not-attempted; read at ~0.5x, values not legible; only matters if a letter in either key turns up; next: none unless a matching letter is found

## Escalation (N8-BIRNUM, 4 Oct 2026)
- [x] siblings: fr.3252 f.36-37 witness read whole under the same key (F36-READ); f.100r pooled with f.119 (BIRAGO-NUM); third numerical letter scouted in both volumes, none (BIRAGO-NUM-SCOUT)
- [x] clear-pages: neighbours and facing pages of all three viewed; no clear copy or slip (Premise check (c)); f.37r slip is clear text
- [x] known-keys: Ceppo-Nevers on f.36-37 and f.47r; 1572 key on f.117r; Nov 1571 system against all 66 digit keys on disk, none at gate, control 6/6 (BIRAGO-NUM-TOOLS); fr.3995 no.73 stat 1.10/-0.39, no.74 0.26/-0.16, no.32 0.79/1.23 (coverage 0.24-0.32) vs gate 3.292, controls 12/12 each (BIRAGO-NUM-KEYEYE, -KEYEYE2); no.71 letters coverage 0.26-0.31, stat -1.09 to 1.65, controls it 12/12, fr 9/12 (BIRAGO-NUM-KEYEYE3); no.76 single-sign letters, not two-figure, crossmatch not applicable (BIRAGO-76)
- [x] print: Gomberville 1665 both parts searched inside; no Birago letter of 1571-72
- [ ] key-rebuild: f.36 gloss by per-sign tiles; f.47r pair check against it; T88=q pre-registered test; f.100r + f.119 codes: clear-context code reading run (N8-BIRNUM, untested-by-this-tool at this N), next f.138 as a possible third letter
- [x] image-check: f.36r rows recut and re-read (F36R-REREAD); f.36-37 gloss crops re-cut; f.117r native crops; f.47r native re-cut
- [ ] retry: reconciliation call on the kept f.36-37 rows' 193 splits; f.117r power at a measured post-look-alike error
Verdict: keep going: 10 internal gaps; cheapest next: f.138 digit-shape / 6-mer check as a third numerical-key letter (~$1); the Nov 1571 key table needs new material (a key sheet in another Nevers/Birago volume)

## RUN6-BIR138 (5 Oct 2026, account-1 worker for LANE-RUN6): f.138 (no.71, 7 Feb 1572) is not in the Nov 1571 numerical system

Brief `.claude/briefs/runs/2026-10-05-acct1-run6-wave1.md` (RUN6-BIR138). PREREG `num/f138/PREREG.md` pushed first (be5cf257). Files `num/f138/`.
Context: no.71's cipher is the 5 lines at the foot of f.139v (NEVBIR-138, `../nevers-birago-fr3251-1572` NOTES), read there against the 1572
symbol sheet (161 signs, key rank 1/201, z 3.60, verifier N3). A sheet-bound transcription cannot show digits, so S1 asked a sheet-free blind reader.

S1 shape gate (1 blind Sonnet call, 3 shuffled montages of lines L02-L06 s1, no key/sheet/folio names; `s1_result.tsv`):

| montage | role | digit fraction | dots over figures | divide/wavy sign |
|---|---|---|---|---|
| f.100r | positive control (Nov 1571 numerical) | 0.95 | y | n |
| f.178v (no.87) | negative control (1572 symbol key) | 0.00 | n | n |
| **f.139v (no.71, f.138 letter)** | target | **0.03** | n | n |

Controls discriminate (0.95 >= 0.8, 0.00 <= 0.3); target 0.03 <= 0.3. **Verdict (pre-registered): not in the numerical system by shape.** The reader
described the target as invented glyphs (pi-like, crossed circles, hash, infinity loops, lambda), the same family as f.178v, with "4 7" once
mid-strip. S2 (6-mer overlap vs f.100r+f.119) has no digit stream and is not applicable; not run. Consistent with NEVBIR-138's 1572-key rank 1/201.
The Nov 1571 system stays at two letters (f.119 + f.100r, 1,048 digits); no tokens graded here. Reader-only caveat: one reader, a shape
estimate, not a transcription; the result rests also on the independent key-rank evidence above. Novelty not classified (rule 10).
Requests: 0 network. Vision: 1 Sonnet subagent call (3 images). Cost: see the lane ledger.

## Remaining gaps (RUN6-BIR138, 5 Oct 2026)
Read so far: f.36-37: 10 C, 0 S of 947 cipher signs; f.47r: 0 S of about 770; f.117r: 276 signs, all M/U; f.100r + f.119: 0 graded of 1,048 digits.
- f.36-37 period gloss (about 940 glossed signs unread) - blocker: not-attempted; running-line model reads [retired] (Sonnet twice, F36-READ/HARVEST-D; Opus once, F36-GLOSS, known-answer gate at chance); a different instrument is untried: per-sign tiles, two blind passes, known-answer gate first on v36top_L01; next: per-sign tile gloss read, ~$8 (wait until rate limit reads allowed)
- f.36-37 kept rows at E 0.333 (700 positions, 193 splits) - blocker: not-attempted; r36_L01-L08, v36top, v36mid and r37 were read on HARVEST-D's eye grid, which the row-ink profile matched within 10-45 px there; next: one reconciliation call on their splits, disk only, ~$1.5
- f.47r reader error 0.33 - blocker: not-attempted; S74/S54, S80/S65, S76/S91 one-sided third-reader preference unverified; next: known-answer pair check on the f.36 gloss once the gloss is read, disk only, ~$2
- f.47r 79 unsettled positions - blocker: not-attempted; sign-sorter focus rows written; next: tools/sign_sorter.py --focus harvest/f47/la/focus.tsv
- f.47r prose/cipher edges - blocker: not-attempted; the readers marked no prose words, so run edges are unchecked; next: eye-check L01-L03 and L17 s1-s2 crops, disk only, ~$1
- f.117r measured error after the 2-of-3 step - blocker: not-attempted; the 2-of-3 residual is agreement, not error; next: power control at a known-answer look-alike error, disk only, ~$1; TXD-HOLDOUT (3 Oct 2026, ../nevers-birago-fr3251-1572/harvest/tx_decode/holdout/RESULTS.md): TX-DECODE's lattice lam-4 rank 1/201 for f.117r survives the pre-registered held-out control (held-out no.87 lines choose lam 4; printed 1572 key beats all 218 same-design wrong keys, z 6.92; rank 1 at every lam 1-8, z 3.28-3.66), judge still FAIL -1.081 vs real_p05 -0.903; the wrong-key gate alone is weak (passes on 4 of 5 shuffled lattices); no reading, S at best; next: verifier pass on the 32 lam-4 changed positions against the native crops, ~$2
- f.117r 12 unsettled tiles - blocker: not-attempted; sorter inputs built (SORTER-BIRAGO2), unpublished; next: the account-3 orchestrator publishes it with {"db": {}}, the owner sorts
- f.117r T88=q - blocker: not-attempted; fitted post-hoc on this letter only; next: pre-registered test on another 1572 leaf with q-words, disk only, ~$1
- f.100r + f.119 (565 + 483 digits) - blocker: not-attempted; joint anneal retired (BIRAGO-NUM3); spelled-crib tests without power (BIRAGO-NUM2, -NUM4); no key on disk (crossmatch control-backed, BIRAGO-NUM-TOOLS); 158 prefix letter design control-backed negative (BIRAGO-NUM-TOOLS); dotted groups and 1x/5x/8x units as nomenclator codes untested-by-this-tool (flank statistic, matched control power 2-4/20, N8-BIRNUM), no meaning licensed by the f.100r clear context; f.138 (no.71) is not a third letter in this system (RUN6-BIR138: symbol cipher, digit fraction 0.03 vs controls 0.95/0.0; 1572 key rank 1/201, NEVBIR-138); fr.3251/fr.3252 have no other numerical letter in Sept 1571-Mar 1572 (BIRAGO-NUM-SCOUT); next: new material -- a numerical-key letter in another Nevers/Birago volume (fr.3256, fr.4688 Guazzo, fr.4712-4715) by a catalogue/eye sweep, ~$2
- Nov 1571 key table - blocker: no-key-material; fr.3995 undated tables all viewed and the sweep is closed (BIRAGO-NUM-KEYEYE, -KEYEYE2, -KEYEYE3, BIRAGO-76): no.73 and no.74 control-backed negatives, no.32, no.33 and no.71 under the coverage floor (no.71 also 1580s), no.75 three-figure codes with League-era names, no.48-51 symbol keys, no.76 a single-sign letter alphabet (digits 1-9 for a-i, symbols and letters for l-z, no 0) with two-figure word codes in a plain and an overlined series (BIRAGO-76); no key table in fr.3995 fits the digit-only 00-59/74-99 token set; the next instrument is new material: a Nov 1571 key in another volume of the Nevers/Birago papers (fr.3252 neighbours, fr.3251, fr.3256, fr.4712-4715 key sheets) located by a catalogue/eye sweep for "chiffre" leaves dated 1571-72
- fr.3995 no.74 digraph signs 23-27 and no.32 superscript marks - blocker: not-attempted; read at ~0.5x, values not legible; only matters if a letter in either key turns up; next: none unless a matching letter is found

## Escalation (RUN6-BIR138, 5 Oct 2026)
- [x] siblings: fr.3252 f.36-37 witness read whole under the same key (F36-READ); f.100r pooled with f.119 (BIRAGO-NUM); third numerical letter scouted in both volumes, none (BIRAGO-NUM-SCOUT)
- [x] clear-pages: neighbours and facing pages of all three viewed; no clear copy or slip (Premise check (c)); f.37r slip is clear text
- [x] known-keys: Ceppo-Nevers on f.36-37 and f.47r; 1572 key on f.117r; Nov 1571 system against all 66 digit keys on disk, none at gate, control 6/6 (BIRAGO-NUM-TOOLS); fr.3995 no.73 stat 1.10/-0.39, no.74 0.26/-0.16, no.32 0.79/1.23 (coverage 0.24-0.32) vs gate 3.292, controls 12/12 each (BIRAGO-NUM-KEYEYE, -KEYEYE2); no.71 letters coverage 0.26-0.31, stat -1.09 to 1.65, controls it 12/12, fr 9/12 (BIRAGO-NUM-KEYEYE3); no.76 single-sign letters, not two-figure, crossmatch not applicable (BIRAGO-76)
- [x] print: Gomberville 1665 both parts searched inside; no Birago letter of 1571-72
- [ ] key-rebuild: f.36 gloss by per-sign tiles; f.47r pair check against it; T88=q pre-registered test; f.100r + f.119 codes: clear-context code reading run (N8-BIRNUM, untested-by-this-tool at this N), f.138 ruled out as a third letter (RUN6-BIR138); next a numerical letter in another volume
- [x] image-check: f.36r rows recut and re-read (F36R-REREAD); f.36-37 gloss crops re-cut; f.117r native crops; f.47r native re-cut
- [ ] retry: reconciliation call on the kept f.36-37 rows' 193 splits; f.117r power at a measured post-look-alike error
Verdict: keep going: 10 internal gaps; cheapest next: reconciliation call on the kept f.36-37 rows' 193 splits (~$1.5, disk only); the Nov 1571 system needs new material (a letter or key sheet in another Nevers/Birago volume)

## RUN6-BIR3637 (5 Oct 2026, account-1 worker for LANE-RUN6): one reconciliation call on the kept f.36-37 rows' 193 splits

Brief `.claude/briefs/runs/2026-10-05-acct1-run6-wave4.md` (job RUN6-BIR3637). Disk only, 0 network requests. Call count stated
first: 1 Sonnet subagent call (= 1 unit). `harvest/f3637/`: `PREREG.md` (pushed in 34f61cf2 before the call), `build_in.py` ->
`adjudicate_in.tsv` (193 rows: both readers read, ids differ, kept rows r36_L01-L08, v36top, v36mid, r37), `prompt_R.md`
(F36R-REREAD's prompt), `adjudicate_out.tsv`. Crops regenerated with `cut_lines.cut('.../harvest/f36/crops', 850, 0, 120, 65, 2)`
(108 crops, gitignored as before).

Result: the reader returned 193 rows but said it decided only 5 from the crops; 3 M (r36_L01 p5 S40, p6 S80; r36_L03 p1 S45),
2 L, 188 '?' L. **E before 0.333 (one-sided 40 + split 193 / 700); E after 0.329 ((40 + 190) / 700) if the 3 M were applied.** By the
pre-registered rule (more than half '?' or L) the call is non-discriminating: nothing spliced, no passD_v3, no control re-run, no grade
changes. This is an undersized-reader outcome (193 positions over ~80 crops in one call), not a test of the eye reconciliation that
worked for r36n (38 positions, 26 H/M); the next step splits it by page. A second call here would have crossed 80% of the USD 2 cap.

## Remaining gaps (RUN6-BIR3637, 5 Oct 2026)
Read so far: f.36-37: 10 C, 0 S of 947 cipher signs; f.47r: 0 S of about 770; f.117r: 276 signs, all M/U; f.100r + f.119: 0 graded of 1,048 digits.
- f.36-37 period gloss (about 940 glossed signs unread) - blocker: not-attempted; running-line model reads [retired] (Sonnet twice, F36-READ/HARVEST-D; Opus once, F36-GLOSS, known-answer gate at chance); a different instrument is untried: per-sign tiles, two blind passes, known-answer gate first on v36top_L01; next: per-sign tile gloss read, ~$8 (wait until rate limit reads allowed)
- f.36-37 kept rows at E 0.333 (700 positions, 193 splits) - blocker: not-attempted; one reconciliation call over all 193 returned 3 M / 190 L-or-? (RUN6-BIR3637: the reader did not open most crops; non-discriminating by PREREG item 4, nothing spliced) -- the unit was oversized, not the method; next: the same prompt split by page into 4 calls (r36_L01-L08 58, v36top 72, v36mid 52, r37 11 positions; harvest/f3637/adjudicate_in.tsv), disk only, ~$2
- f.47r reader error 0.33 - blocker: not-attempted; S74/S54, S80/S65, S76/S91 one-sided third-reader preference unverified; next: known-answer pair check on the f.36 gloss once the gloss is read, disk only, ~$2
- f.47r 79 unsettled positions - blocker: not-attempted; sign-sorter focus rows written; next: tools/sign_sorter.py --focus harvest/f47/la/focus.tsv
- f.47r prose/cipher edges - blocker: not-attempted; the readers marked no prose words, so run edges are unchecked; next: eye-check L01-L03 and L17 s1-s2 crops, disk only, ~$1
- f.117r measured error after the 2-of-3 step - blocker: not-attempted; the 2-of-3 residual is agreement, not error; next: power control at a known-answer look-alike error, disk only, ~$1; TXD-HOLDOUT (3 Oct 2026, ../nevers-birago-fr3251-1572/harvest/tx_decode/holdout/RESULTS.md): TX-DECODE's lattice lam-4 rank 1/201 for f.117r survives the pre-registered held-out control (held-out no.87 lines choose lam 4; printed 1572 key beats all 218 same-design wrong keys, z 6.92; rank 1 at every lam 1-8, z 3.28-3.66), judge still FAIL -1.081 vs real_p05 -0.903; the wrong-key gate alone is weak (passes on 4 of 5 shuffled lattices); no reading, S at best; next: verifier pass on the 32 lam-4 changed positions against the native crops, ~$2
- f.117r 12 unsettled tiles - blocker: not-attempted; sorter inputs built (SORTER-BIRAGO2), unpublished; next: the account-3 orchestrator publishes it with {"db": {}}, the owner sorts
- f.117r T88=q - blocker: not-attempted; fitted post-hoc on this letter only; next: pre-registered test on another 1572 leaf with q-words, disk only, ~$1
- f.100r + f.119 (565 + 483 digits) - blocker: not-attempted; joint anneal retired (BIRAGO-NUM3); spelled-crib tests without power (BIRAGO-NUM2, -NUM4); no key on disk (crossmatch control-backed, BIRAGO-NUM-TOOLS); 158 prefix letter design control-backed negative (BIRAGO-NUM-TOOLS); dotted groups and 1x/5x/8x units as nomenclator codes untested-by-this-tool (flank statistic, matched control power 2-4/20, N8-BIRNUM), no meaning licensed by the f.100r clear context; f.138 (no.71) is not a third letter in this system (RUN6-BIR138: symbol cipher, digit fraction 0.03 vs controls 0.95/0.0; 1572 key rank 1/201, NEVBIR-138); fr.3251/fr.3252 have no other numerical letter in Sept 1571-Mar 1572 (BIRAGO-NUM-SCOUT); next: new material -- a numerical-key letter in another Nevers/Birago volume (fr.3256, fr.4688 Guazzo, fr.4712-4715) by a catalogue/eye sweep, ~$2
- Nov 1571 key table - blocker: no-key-material; fr.3995 undated tables all viewed and the sweep is closed (BIRAGO-NUM-KEYEYE, -KEYEYE2, -KEYEYE3, BIRAGO-76): no.73 and no.74 control-backed negatives, no.32, no.33 and no.71 under the coverage floor (no.71 also 1580s), no.75 three-figure codes with League-era names, no.48-51 symbol keys, no.76 a single-sign letter alphabet (digits 1-9 for a-i, symbols and letters for l-z, no 0) with two-figure word codes in a plain and an overlined series (BIRAGO-76); no key table in fr.3995 fits the digit-only 00-59/74-99 token set; the next instrument is new material: a Nov 1571 key in another volume of the Nevers/Birago papers (fr.3252 neighbours, fr.3251, fr.3256, fr.4712-4715 key sheets) located by a catalogue/eye sweep for "chiffre" leaves dated 1571-72
- fr.3995 no.74 digraph signs 23-27 and no.32 superscript marks - blocker: not-attempted; read at ~0.5x, values not legible; only matters if a letter in either key turns up; next: none unless a matching letter is found

## Escalation (RUN6-BIR3637, 5 Oct 2026)
- [x] siblings: fr.3252 f.36-37 witness read whole under the same key (F36-READ); f.100r pooled with f.119 (BIRAGO-NUM); third numerical letter scouted in both volumes, none (BIRAGO-NUM-SCOUT)
- [x] clear-pages: neighbours and facing pages of all three viewed; no clear copy or slip (Premise check (c)); f.37r slip is clear text
- [x] known-keys: Ceppo-Nevers on f.36-37 and f.47r; 1572 key on f.117r; Nov 1571 system against all 66 digit keys on disk, none at gate, control 6/6 (BIRAGO-NUM-TOOLS); fr.3995 no.73 stat 1.10/-0.39, no.74 0.26/-0.16, no.32 0.79/1.23 (coverage 0.24-0.32) vs gate 3.292, controls 12/12 each (BIRAGO-NUM-KEYEYE, -KEYEYE2); no.71 letters coverage 0.26-0.31, stat -1.09 to 1.65, controls it 12/12, fr 9/12 (BIRAGO-NUM-KEYEYE3); no.76 single-sign letters, not two-figure, crossmatch not applicable (BIRAGO-76)
- [x] print: Gomberville 1665 both parts searched inside; no Birago letter of 1571-72
- [ ] key-rebuild: f.36 gloss by per-sign tiles; f.47r pair check against it; T88=q pre-registered test; f.100r + f.119 codes: clear-context code reading run (N8-BIRNUM, untested-by-this-tool at this N), f.138 ruled out as a third letter (RUN6-BIR138); next a numerical letter in another volume
- [x] image-check: f.36r rows recut and re-read (F36R-REREAD); f.36-37 gloss crops re-cut; f.117r native crops; f.47r native re-cut
- [ ] retry: reconciliation of the kept f.36-37 rows' 193 splits in 4 per-page calls (one 193-row call was non-discriminating, RUN6-BIR3637); f.117r power at a measured post-look-alike error
Verdict: keep going: 10 internal gaps; cheapest next: the kept f.36-37 rows' 193 splits in 4 per-page reconciliation calls (~$2, disk only); the Nov 1571 system needs new material (a letter or key sheet in another Nevers/Birago volume)

## D2-B117KAPC (5 Oct 2026, account-1 worker for LANE-D2PUSH): f.117r power control at the measured post-look-alike error; 27 M -> S

Brief `.claude/briefs/runs/2026-10-05-acct1-d2-b117kapc.md`. Disk only, 0 network requests, 0 vision calls. Box 18:47-19:47 UTC, cap USD 4.
Intake gate: `python3 tools/intake_gate_check.py birago-fr3252-1571-72` -> "birago-fr3252-1571-72: partial (line 1) -- edition/page or
full-text-search citation found within 6 lines" (pass). PREREG `harvest/f117/la/PREREG-KAPC.md` pushed in 473e7a149 before any score.

**Step 1, measured error (known answer).** The same pipeline (two value-blind passes + look-alike third reader + 2-of-3) was already
scored on no.87 f.178r + f.179r against the clerk's clear sheet (LOOKALIKE-TOOL, ../nevers-birago-fr3251-1572/NOTES.md); re-scored here
from disk with `harvest/lookalike_known/score_known.py`: f.178r 16/90 wrong (0.178, 7 empty), f.179r 6/84 (0.071, 5 empty).
E1 pooled = 22/174 = **0.126**; E2 bracket (wrong + empty / all) = 34/186 = **0.183** (>= the worse leaf). No new pass was needed.

**Step 2, test** (`decode_control.py la/recon_f117_3r.tsv --map map_printed.json --corpus fr`, 200 shuffles, 20 windows; outputs
`harvest/f117/la/kapc/test_*.txt`; the seed-1 reading is byte-identical to `la/reading_3r_printed.txt`):

| err | seed | power (real key rank 1 of 201) | z median / min | target rank, z |
|---|---|---|---|---|
| 0.126 (E1) | 1 | **18/20** | 3.88 / 1.98 | 1/201, 3.21 |
| 0.126 | 2 | 20/20 | 4.44 / 2.42 | 1/201, 2.92 |
| 0.126 | 3 | 19/20 | 4.14 / 1.83 | 1/201, 2.97 |
| 0.126 | 4 | 20/20 | 4.10 / 2.61 | 1/201, 3.05 |
| 0.126 | 5 | 18/20 | 3.80 / 2.04 | 1/201, 3.16 |
| 0.183 (E2) | 1 | **16/20** (at the gate) | 3.64 / 1.04 | 1/201, 3.21 |
| 0.25 (two-reader, reference) | 1 | 6/20 (reproduces NEVBIR-117C) | 2.10 / 0.65 | 1/201, 3.21 |

**Licensed by the pre-registered gate** (>= 16/20 at E1 and E2, rank 1 on 5/5 seeds): the printed 1572 key fits f.117r's 2-of-3
transcription at the measured error. E2 sits exactly at the gate, so the licence is thin at the upper bracket. It licenses the key at
this error, not a reading: the judge still FAILs (-1.224 vs real_p05 -0.899, BIR-APPLY; reading text unchanged, so the score stands).

**Step 3, M -> S** under the existing BIR-APPLY rule (two independent blind instruments agree), operationalised in
`harvest/f117/la/kapc/m_to_s.py` (rule in its docstring, fixed before counting; per-token table `m_to_s.tsv`): of the 63 M tokens of
`../nevers-birago-fr3251-1572/harvest/tx_decode/eye/apply/reading_f117_apply_tokens.tsv`, 27 plain-M tokens whose aligned look-alike tile
is firm (2-of-3 or confirms) with the top-1 sign become S; 16 plain-M stay M (no third read, an unsettled tile, or the third reader chose
another sign); the 12 BIR-OPEN-only rows stay M (the look-alike reader sided with top-1 against BIR-OPEN on 6, unsettled or unaligned on
6); the 8 conflicts stay M (owner sorter). Values unchanged; only grades move.

    $ python3 tools/decode_key.py ciphers/birago-fr3252-1571-72 --config ciphers/birago-fr3252-1571-72/harvest/f117/la/kapc/decode_kapc.json --check
    ../nevers-birago-fr3251-1572/harvest/tx_decode/eye/verify/ciphertext_f117_top1.tsv: tokens 279: M 36, S 217, U 26
    reading up to date

**f.117r per token (rule 4): H 0, C 0, S 217, M 36, I 0, U 26** (was S 190, M 63). Cryptanalytic result only. Longest S-only
stretch: 17 letters, 'lguenturinopsenua' (L01.14-25), not a clause; longest S+M stretch 37 letters, 'esoingetsi[s]uouss[e]mb[l]ietantgui[s]reusi[s][e]'
(L09.2-L10.7). No clause above AD on S alone, so depth stays D1 (not raised here; a verifier sets depth). depth_pct 68.1 -> 77.8 in status.json.
Report: found the licence and 27 regrades; not found: any S-only clause.

## Remaining gaps (D2-B117KAPC, 5 Oct 2026)
Read so far: f.36-37: 10 C, 0 S of 947 cipher signs; f.47r: 0 S of about 770; f.117r: 279 tokens S 217, M 36, U 26 (D2-B117KAPC); f.100r + f.119: 0 graded of 1,048 digits.
- f.36-37 period gloss (about 940 glossed signs unread) - blocker: not-attempted; running-line model reads [retired] (Sonnet twice, F36-READ/HARVEST-D; Opus once, F36-GLOSS, known-answer gate at chance); a different instrument is untried: per-sign tiles, two blind passes, known-answer gate first on v36top_L01; next: per-sign tile gloss read, ~$8 (wait until rate limit reads allowed)
- f.36-37 kept rows at E 0.333 (700 positions, 193 splits) - blocker: not-attempted; one reconciliation call over all 193 returned 3 M / 190 L-or-? (RUN6-BIR3637: the reader did not open most crops; non-discriminating by PREREG item 4, nothing spliced) -- the unit was oversized, not the method; next: the same prompt split by page into 4 calls (r36_L01-L08 58, v36top 72, v36mid 52, r37 11 positions; harvest/f3637/adjudicate_in.tsv), disk only, ~$2
- f.47r reader error 0.33 - blocker: not-attempted; S74/S54, S80/S65, S76/S91 one-sided third-reader preference unverified; next: known-answer pair check on the f.36 gloss once the gloss is read, disk only, ~$2
- f.47r 79 unsettled positions - blocker: not-attempted; sign-sorter focus rows written; next: tools/sign_sorter.py --focus harvest/f47/la/focus.tsv
- f.47r prose/cipher edges - blocker: not-attempted; the readers marked no prose words, so run edges are unchecked; next: eye-check L01-L03 and L17 s1-s2 crops, disk only, ~$1
- f.117r 36 M tokens - blocker: not-attempted; 8 A1-vs-BIR-OPEN conflicts and 12 BIR-OPEN-only rows (the look-alike reader sided with top-1 against BIR-OPEN on 6, unsettled/unaligned on 6) and 16 tokens with no third read or a split look-alike (la/kapc/m_to_s.tsv); next: owner sign sorter on the existing focus list, or one value-blind tile read of the 16 passC/unsettled tiles at the measured-error licence, disk only, ~$1; longest S-only stretch 17 letters ('lguenturinopsenua', L01.14-25), no clause above AD, judge FAIL unchanged (-1.224); TXD-HOLDOUT lam-4 note unchanged: next verifier pass on the 32 lam-4 changed positions, ~$2
- f.117r 12 unsettled tiles - blocker: not-attempted; sorter inputs built (SORTER-BIRAGO2), unpublished; next: the account-3 orchestrator publishes it with {"db": {}}, the owner sorts
- f.117r T88=q - blocker: not-attempted; fitted post-hoc on this letter only; next: pre-registered test on another 1572 leaf with q-words, disk only, ~$1
- f.100r + f.119 (565 + 483 digits) - blocker: not-attempted; joint anneal retired (BIRAGO-NUM3); spelled-crib tests without power (BIRAGO-NUM2, -NUM4); no key on disk (crossmatch control-backed, BIRAGO-NUM-TOOLS); 158 prefix letter design control-backed negative (BIRAGO-NUM-TOOLS); dotted groups and 1x/5x/8x units as nomenclator codes untested-by-this-tool (flank statistic, matched control power 2-4/20, N8-BIRNUM), no meaning licensed by the f.100r clear context; f.138 (no.71) is not a third letter in this system (RUN6-BIR138: symbol cipher, digit fraction 0.03 vs controls 0.95/0.0; 1572 key rank 1/201, NEVBIR-138); fr.3251/fr.3252 have no other numerical letter in Sept 1571-Mar 1572 (BIRAGO-NUM-SCOUT); next: new material -- a numerical-key letter in another Nevers/Birago volume (fr.3256, fr.4688 Guazzo, fr.4712-4715) by a catalogue/eye sweep, ~$2
- Nov 1571 key table - blocker: no-key-material; fr.3995 undated tables all viewed and the sweep is closed (BIRAGO-NUM-KEYEYE, -KEYEYE2, -KEYEYE3, BIRAGO-76): no.73 and no.74 control-backed negatives, no.32, no.33 and no.71 under the coverage floor (no.71 also 1580s), no.75 three-figure codes with League-era names, no.48-51 symbol keys, no.76 a single-sign letter alphabet (digits 1-9 for a-i, symbols and letters for l-z, no 0) with two-figure word codes in a plain and an overlined series (BIRAGO-76); no key table in fr.3995 fits the digit-only 00-59/74-99 token set; the next instrument is new material: a Nov 1571 key in another volume of the Nevers/Birago papers (fr.3252 neighbours, fr.3251, fr.3256, fr.4712-4715 key sheets) located by a catalogue/eye sweep for "chiffre" leaves dated 1571-72
- fr.3995 no.74 digraph signs 23-27 and no.32 superscript marks - blocker: not-attempted; read at ~0.5x, values not legible; only matters if a letter in either key turns up; next: none unless a matching letter is found

## Escalation (D2-B117KAPC, 5 Oct 2026)
- [x] siblings: fr.3252 f.36-37 witness read whole under the same key (F36-READ); f.100r pooled with f.119 (BIRAGO-NUM); third numerical letter scouted in both volumes, none (BIRAGO-NUM-SCOUT)
- [x] clear-pages: neighbours and facing pages of all three viewed; no clear copy or slip (Premise check (c)); f.37r slip is clear text
- [x] known-keys: Ceppo-Nevers on f.36-37 and f.47r; 1572 key on f.117r; Nov 1571 system against all 66 digit keys on disk, none at gate, control 6/6 (BIRAGO-NUM-TOOLS); fr.3995 no.73 stat 1.10/-0.39, no.74 0.26/-0.16, no.32 0.79/1.23 (coverage 0.24-0.32) vs gate 3.292, controls 12/12 each (BIRAGO-NUM-KEYEYE, -KEYEYE2); no.71 letters coverage 0.26-0.31, stat -1.09 to 1.65, controls it 12/12, fr 9/12 (BIRAGO-NUM-KEYEYE3); no.76 single-sign letters, not two-figure, crossmatch not applicable (BIRAGO-76)
- [x] print: Gomberville 1665 both parts searched inside; no Birago letter of 1571-72
- [ ] key-rebuild: f.36 gloss by per-sign tiles; f.47r pair check against it; T88=q pre-registered test; f.100r + f.119 codes: clear-context code reading run (N8-BIRNUM, untested-by-this-tool at this N), f.138 ruled out as a third letter (RUN6-BIR138); next a numerical letter in another volume
- [x] image-check: f.36r rows recut and re-read (F36R-REREAD); f.36-37 gloss crops re-cut; f.117r native crops; f.47r native re-cut
- [ ] retry: reconciliation of the kept f.36-37 rows' 193 splits in 4 per-page calls (one 193-row call was non-discriminating, RUN6-BIR3637); f.117r [x] power at the measured post-look-alike error done (D2-B117KAPC: 18/20 at 0.126, 16/20 at 0.183, rank 1/201 on 5/5 seeds), 27 M -> S
Verdict: keep going: 10 internal gaps (f.117r now S 217/M 36); cheapest next: the kept f.36-37 rows' 193 splits in 4 per-page reconciliation calls (~$2, disk only); the Nov 1571 system needs new material (a letter or key sheet in another Nevers/Birago volume)
