partial
BnF dépouillement of Français 4715 (archivesetmanuscrits.bnf.fr ark:/12148/cc577658, item 44, folio 67: "Lettre, avec chiffre, du Sr DE MONTHOLON. Tours, 15 avril 1590.") read by this worker from the cached notice in a fresh shallow clone of dbourdeau/cyphersolver (research/gallica_sweep/notice_cc577658.html and notice_cc577658_cd0e531.html, 2 Oct 2026); Tomokiyo's bnf4715.htm and nevers.htm (local mirror, cp932) read in full and grepped for no.44 / f.67 / "15 April 1590" (nevers.htm lists the item under the Vieuville-Nevers Cipher heading with no reading; bnf4715.htm has no no.44 section); Desenclos and Lasry, "An early French digit cipher: deciphering a letter from the King of France to the Duke of Nevers (1592)" (HistoCrypt, dspace.ut.ee PDF, 54 kB of text) grepped in full text: 0 hits for 4715, Montholon named twice as a digit-cipher user, no 1590 Montholon letter printed.

# BnF fr.4715 Vieuville-Nevers open sub-pool -- first cheap test on no.44 (f.67r), Montholon, Tours, 15 April 1590

Sibling of `ciphers/fr4715-montholon-1589` (no.58, f.81r). Pool register: `ciphers/fr4715-montholon-1589/POOL.md`
(CS-4715-POOL, 27 Sept 2026): 8 open/partial single-leaf letters in the same hand and key family -- no.21 f.44,
no.27 f.50, no.28 f.51, no.35 f.58, no.37 f.60, no.39 f.62, no.44 f.67, no.60 f.83 -- about 10,600 signs besides
no.58's 2,524. Key of record: `ciphers/fr4715-montholon-1589/keys/key_vieuville_nevers.tsv` (Tomokiyo's printed
Vieuville-Nevers table, nevers.htm; 35 rows, 33 numeric letter-homophones plus two glyphs; no j, k, v, w, z;
dotted groups are an undocumented word-code layer). This folder covers the pool's leaves other than no.58; each
leaf gets its own section, ciphertext file and reading. Row: `ciphers/_triage/likely-solves-2026-10-02.tsv` rank 1
(brief `.claude/briefs/runs/2026-10-02-account4-likely-phase2.md`).

Source image: Gallica ark:/12148/btv1b52509819x, canvas f149, manifest label '67r' (`tools/gallica_folio.py`,
cached manifest, no request), 4079x5720 native. Region 300,900,3500,4820 fetched once at native resolution
(`images/manifest.json`; 1 request to gallica.bnf.fr, 03:40 UTC 2 Oct 2026). The leaf is 32 lines of clear French
in a secretary hand with numeral cipher groups in the running text, the date line "ce 15 apuril a cinq heures du
soir" at the foot of the text block, and blank paper below (band 33 of the row profile is the blank lower leaf).

## Check-solved (LIKELY-1, 2 Oct 2026, account-4; minimal, per the brief's step 2)

1. BnF dépouillement, item 44: "Fol. 67 • 44 Lettre, avec chiffre, du Sr DE MONTHOLON. Tours, 15 avril 1590." --
   "avec chiffre" and nothing else, unlike the "en partie déchiffrée" and "Chiffre et déchiffrement" rows around
   it (items 21, 27-28, 35, 37, 39, 45-46, 47-48). No period decipherment is recorded for this leaf. Read from the
   cached notice in the fresh `dbourdeau/cyphersolver` clone (research/gallica_sweep/notice_cc577658.html, line
   "Fol. 67 • 44 ..."); a WebFetch of the live record (ark:/12148/cc577658/cd0e531) answered HTTP 403 this session,
   1 request, not retried.
2. Tomokiyo: `sources/cryptiana/web/nevers.htm` lists "no.44 (f.67) Letter of Montholon, Tours, 15 April 1590"
   under the Vieuville-Nevers Cipher heading with no status sentence and no reading; `bnf4715.htm` has no `no44`
   section (both files decoded cp932 and grepped, 0 hits for a reading).
3. Solver repositories, fresh shallow clones 2 Oct 2026 (grep `4715|montholon|vieuville|trespigny|52509819`):
   `dbourdeau/cyphersolver` -- hits only in research/gallica_sweep (the cached BnF notice and SRU results, the
   nevers/bnf4715 page mirrors), targets/r2276 (fr.4715 f.2 used as a reference alphabet image, a different
   cipher) and targets/nevers1589 (fr.3977, intercepts for Nevers 1589); no folder, key or reading for no.44, and
   SOLVED_CATALOGUE.md's Montholon row (POOL.md quotes it) names nos. 19, 27, 37, 47, 48, 58, 60, 62 only.
   `aaymeloglu/unsolved-ciphers` -- the only `4715` match is DECODE record id 4715 (Marburg, 1715), unrelated; no
   Montholon hit.
4. Scholarship: Desenclos and Lasry (HistoCrypt, "An early French digit cipher ... (1592)", dspace.ut.ee) -- full
   text grepped: 0 x "4715"; "Montholon" twice (digit ciphers "used by the French Monarchy (like Montholon or La
   Vieuville ...)"); the one 1590 Montholon item they cite is unrelated. Bourdeau PR #9 (fr.3977 no.96, Nevers
   intercepts 1589) read via WebFetch: no fr.4715, no April 1590, no folio 67.
5. DECODE: the 24 Sept 2026 cached crawl (POOL.md step 4) has no fr.4715 row; not re-crawled.

## Web and blog check (LIKELY-1, 2 Oct 2026)

Plain web searches (4): `Montholon Nevers 1590 lettre chiffre Tours "15 avril 1590"` -- hits: the BnF finding aid
(cc577658 and its cd0e531 item page, the catalogue entry above), Wikipedia pages; `"fr. 4715" OR "français 4715"
BnF chiffre Montholon Vieuville Nevers` -- the same finding aid, fr.4716, fr.3974-3995, fr.3623 notices; `"Vieuville-
Nevers" cipher Montholon 1589 decipherment` -- the Desenclos-Lasry PDF (opened, item 4 above), Bourdeau PR #9
(opened), dbourdeau.github.io index, an aryasn2026 fork of cyphersolver (same content), Wikipedia; `Montholon garde
des sceaux Ligue lettres 1589 1590 duc de Nevers correspondance chiffrée édition` -- BnF notices fr.3616, fr.3416
(a Montholon letter of 20 Jan 1590), fr.3623 (10 Aug 1590), fr.4715, and the Archives nationales Montholon-Sémonville
fonds (34 letters to Montholon 1588-89); none prints a reading of f.67.
Blog site searches (3): Cipherbrain / klausis-krypto-kolumne (scienceblogs.de): 0 hits for Montholon, Nevers or
4715. Cryptiana blog (cryptiana.blogspot.com): the 30 Nov 2018 post "Unsolved ciphers in the French archives
(ca.1586-1593)" names BnF fr.4715 as containing undeciphered material; opened, "No comments" -- 0 comments, no
decipherment. Cipher Mysteries (ciphermysteries.com): 0 hits (the only match is an unrelated 1715 Vieuville
genealogy post).
Verdict of the check: no decipherment or plaintext of fr.4715 no.44 (f.67) located in any of the above; a search
result (rule 10), not a novelty verdict. Status `open`.

## LIKELY-1 (2 Oct 2026, account-4): first cheap test on no.44 f.67r -- the key against the leaf, control first

**Answer.** The leaf is 32 lines of clear French with 28 cipher groups in the running text, not the ~100 the
shortlist row estimated: one run of ten letter-homophone groups on L01 (both blind passes read it identically,
`6 7 25 93 84 25 50 93 25 95`), eleven single barred groups (`.71 .7 .27 .6 .13 .7 .7 .7 .25 .49 .57`, the
word-code layer nevers.htm names and does not enumerate), two unbarred groups `14 15` on L03, four groups the
passes read differently (L18, L23, L27, L31) and the numeral of the date line. The printed key reads the eight
in-key groups of the L01 run as `a u s a l u a t` (grade H, the key's own AB rows; `6` and `7` have no key row).
That is 8 letters: the rank-1 shuffled-key gate cannot decide at that length (control below, subsampled to N=8),
so the test is a **non-test for the key on this leaf, not a negative**; what the leaf actually carries in cipher is
the word-code layer the letter key does not cover.

**Control first (rule 3), `scripts/keytest.py known-answer`.** Scorer = French word-cover (tools/data/fr16 words,
3-14 letters, freq >= 3) of the decoded in-key runs, against the key's letter values permuted among its letter rows.
On no.58's Tomokiyo group transcription (fr4715-montholon-1589/witness/aligned_dump_codes.txt, 818 in-key groups):
REAL 729/818 = 0.891 vs 200 shuffled keys mean 0.353 sd 0.100 max 0.631, z 5.37, rank 1 of 201 -- the instrument
separates the real key on a leaf it is known to read. Subsampled to this leaf's N (`--window 8 --windows 200`, 20
shuffles each): real mean 0.816 vs shuffle mean 0.355; the real key is above the shuffle mean in 195/200 windows
but rank 1 of 21 in only 85/200, and 11/200 windows have some shuffled key at cover 1.0 (ARM3-ADJ lesson: a
control's power is shown at the target's own N before a miss is read as a negative).

**Target, `scripts/keytest.py target f67r_ciphertext.tsv --shuffles 200`:** 13 unbarred cipher groups, 8 in key,
4 out of key (`6 7 14 15`); decoded letters 8; word-cover REAL 6/8 = 0.750 vs 200 shuffled keys mean 0.326 sd
0.293 max 1.000, z 1.45, rank 43 of 201; against the first 20 shuffles (max 0.875) the real key is not rank 1.
Side by side: control (N=818) 0.891 vs 0.353; control at N=8 beats the shuffle mean 97.5 pct of the time and
beats every shuffle 42 pct of the time; target (N=8) 0.750 vs 0.326, above the mean, not above the max. Exactly
where a true key on an 8-letter window lands most of the time, and where the gate has no power.

**Transcription (rule 2, image).** Gallica canvas f149 (label 67r), region 300,900,3500,4820 at native resolution,
one request; `tools/iiif_lines.py` 96 crops (L01-L30 slope-following, L31-L32 fixed bands cut by hand, see
images/manifest.json); two blind Sonnet passes (witness/f67r_pass_a.tsv, f67r_pass_b.tsv; the brief's vision calls
2 and 3, call 1 the overlay check); `tools/reconcile_passes.py` nw alignment: 683 aligned columns, agreement
351/683 = 51.4 pct -- the clear French is read at mostly conf L by both passes (every cipher group but the four
above agreed; the clear words disagree, e.g. "NERESSI", "SCRIBUAYEN"), so `f67r_ciphertext.tsv` is a rough
transcription of the clear frame around an agreed set of cipher groups, not a reading of the prose. Clear words
visible with confidence in the overlay: the opening "Jay sceu ... qui a discouru [cipher] ce quil a apris ...",
the close "ce 15 apuril a cinq heures du soir". Both passes report the barred groups carry a horizontal bar, not
a dot, over the digits (the `.` prefix is the file's convention for either mark).

**Rule 4 grades, `tools/decode_key.py ciphers/fr4715-vieuville-pool` (decode.json; `--check` exit 0):** cipher
tokens 28: H 8 (key rows, printed-key grade AB), U 20 = 11 barred word-codes (two carry an M-grade gloss from
no.58's OWN_GLOSS table in fr4715-montholon-1589/scripts/decode_rest.py: `.27` = les, `.25` = la; not applied
here), 4 unbarred groups without a key row (`6 7 14 15`), 4 pass disagreements, 1 date numeral. No C, no S.
The 655 clear-word tokens are a transcription, not decipherment, and are not graded. Reading of record:
`f67r_reading.txt` (letter strings between the clear words), regenerated by `tools/decode_key.py`.

**Judge (rule 7), `tools/judge_plaintext.py specs/fr4715-vieuville-pool.json --file witness/f67r_judge_candidate.txt`
(the reading lines with the bracketed U tokens removed):**
```
FAIL language: score=-1.145, null_p99=-1.922, real_p05=-0.853, real_median=-0.784, mode=both, N=2699
ok   words: cover=0.872, min=0.5, real_text_median_cover=0.946
FAIL - fr4715-vieuville-pool (a PASS is a gate for a verifier, not a reading; rule 10)
```
Reported as a FAIL. What it measures here: 2,691 of the 2,699 letters are the clear French as the two Sonnet
passes transcribed it at conf L, 8 are the key's letters; the score sits far above the shuffled null (-1.92) and
below real_p05 (-0.85) -- the transcription of the clear frame is garbled, which the 51.4 pct pass agreement already
said. It says nothing about the key either way. No "reading ready" line: nothing here clears the judge and the
shuffled-key gate together.

**Spec:** `specs/fr4715-vieuville-pool.json`, `cheap_test_done[0]` carries both numbers (Pipeline 3a).
**Status:** `partial` (rule 5's near-solve amendment: a control showed the negative was not a real test; the 8
in-key groups decode at H). Not `closed-negative`; no NEAR.md row (no margin over control to register).

**Requests this job.** gallica.bnf.fr: 1 (the region fetch; the manifest was cached). archivesetmanuscrits.bnf.fr: 1
WebFetch, HTTP 403, not retried (the cached notice in Bourdeau's clone used instead). dspace.ut.ee: 1 (the
Desenclos-Lasry PDF). github.com: 2 shallow clones + 1 WebFetch (PR #9). cryptiana.blogspot.com: 1. Web searches: 7.
Vision calls: 3 (overlay, pass A, pass B). No credentials used or printed. No AskUserQuestion.

## Remaining gaps (LIKELY-1, 2 Oct 2026)
Read so far: 8 of 28 cipher groups decode under the key (28.6 pct of the cipher groups, grade H); the 655 clear-French tokens are a transcription at 51.4 pct pass agreement, not a reading
- the 11 barred word-code groups (`.71 .7 .27 .6 .13 .7 .7 .7 .25 .49 .57`) - blocker: not-attempted; the word-code table is not on file (nevers.htm names the layer; no.58's OWN_GLOSS covers only .27 = les and .25 = la) and reading them from the clear context needs a clear-French transcription better than 51.4 pct agreement; next: one Opus pass over the 96 crops in images/ (clear words + the barred groups in context), ~$4
- the 4 unbarred groups `6 7 14 15` (L01, L03) - blocker: open-codes; no key row for any of them (the printed table has no 6, 7, 14 or 15), possibly word-codes whose bar the passes missed or one-digit homophones the printed table lacks; context after the Opus pass decides
- the 4 pass disagreements (L18/17, L23/16, L27/20, L31/9) - blocker: not-attempted; settled only from the image, this brief's three vision calls are spent; next: the same Opus pass, ~$0 extra
- a decisive test of the key on this pool - blocker: too-short; 8 in-key letters on this leaf, the rank-1 gate has 42 pct power at N=8 (control above); next: no.37 f.60 (dense, ~1,500 signs, Gallica canvas 135 per fr4715-montholon-1589/images/manifest.json) the same way, ~$9

## Escalation (2 Oct 2026)
- [x] siblings: no.58's Tomokiyo group transcription used as the known-answer control (z 5.37) and its OWN_GLOSS word-codes checked against the barred groups (2 of 11 covered); the other six open pool leaves not yet imaged
- [x] clear-pages: this leaf is itself 95 pct clear French; the clear frame transcribed by two blind passes (51.4 pct agreement), the word-codes not yet read from it
- [x] known-keys: key_vieuville_nevers.tsv applied through tools/decode_key.py, 8 of 28 groups read at H, shuffled-key test above
- [ ] print: tools/print_check.py on the leaf's clear phrases, after the Opus pass gives phrases readable enough to search (the conf-L transcription is not)
- [n/a] key-rebuild: the letter key is proven on no.58 and nothing on this leaf contradicts it; 8 letters rebuild nothing
- [x] image-check: native region fetched once, 96 crops, overlay eye-checked; the date line closes the letter on 67r, so 67v was not fetched
- [ ] retry: a second clear-French pass with a stronger reader (Opus) over the same crops, the cheapest next step above
Verdict: keep going: 3 internal gaps; cheapest next: one Opus clear-French pass over the 96 crops to read the 11 barred word-codes from context and settle the 4 disagreements, ~$4
