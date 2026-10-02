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

## GAPS-fr4715-vieuville-pool (2 Oct 2026, account-4): the Verdict step -- one strong-model clear-French pass over the 96 crops

**Brief:** `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; the step as LIKELY-1's Verdict line named it, "one Opus
clear-French pass over the 96 crops to read the 11 barred word-codes from context and settle the 4 disagreements".
Disk only: 0 requests to any host; the 96 crops in images/ read as cut. Vision calls 5 of 5: four Fable 5.1 subagent
calls of 24 crops each, blind to every earlier reading (pass C, `witness/f67r_pass_c_L01-L08.tsv` ... `L25-L32.tsv`,
merged into `witness/f67r_pass_c.tsv`, running transcriptions beside them), and one Fable 5.1 call over the seven crops
that carry the four A/B disagreement sites, shown all three earlier readings (pass D,
`witness/f67r_disagreements_pass_d.tsv`).

**Answer.** The clear French now reads at word level: pass C 630 word tokens, **H 327 / M 201 / L 102** (52 pct H, 84
pct H or M), against the two Sonnet passes' 51.4 pct mutual agreement at conf L. Every cipher group the two Sonnet
passes agreed on is confirmed digit for digit by the blind pass C (the L01 run's digits identical, grouped
`6 7 25 93 842 2550 93 2595` with the 84 2 / 25 50 / 25 95 splits named as allowed); pass C adds nothing the A/B
file lacked except three marks (a hooked `d`+`o` sign between "de" and `.13` on L07, an et-sign-like hook on L08, and
line-end fillers), and finds **no cipher group on L09-L16, L25-L26, L30 or L32** (the `15` of L32 is the date in clear).
The four disagreements are settled, each from a named crop (pass D, call 5):

| site | A | B | C | D verdict (crop, x) | now in f67r_ciphertext.tsv |
|---|---|---|---|---|---|
| L18/17 | (nothing) | [sym: overbarred c/9-like] | `.03` L | `.03` M, second `.63` (f67r_L18_s3.jpg x230-300): round closed sign + 3-shape under one bar, comma after | `.03` conf L |
| L23/16 | `.?5` | `.73` | `.03` L | `.03` M, second `.63` (f67r_L23_s3.jpg x255-335): same two shapes, larger, under a heavy bar; A's 5 and B's 7 excluded | `.03` conf L |
| L27/20 | `.67` | [sym: o with dot above] `7` | `.07` M | `.07` M (f67r_L27_s3.jpg x235-300): closed circle with one detached dot, then a 7, no bar; A's 67 ranked third | `.07` conf L |
| L31/9 | `.7` | w:fbikt | `2` L (no bar) | no cipher group (f67r_L31_s1.jpg x620-1400, f67r_L31_s2.jpg x60-330): dash, "auec le vo~ seruite~", a paraph, then a word opening 2-shape/capital L + two minims | `w:2ii` conf L |

So the leaf carries **27 cipher tokens, not 28** (`tools/decode_key.py ciphers/fr4715-vieuville-pool --check`: tokens 27,
AB 8, U 19, exit 0; reading regenerated). Of the 19 U: 14 barred or dotted word-codes (the 11 LIKELY-1 listed plus the
three settled sites `.03 .03 .07`), 4 unbarred groups without a key row (`6 7 14 15`; pass C confirms no mark over any
of them), 1 date numeral. The judge was not re-run: its candidate drops the bracketed U tokens and the clear words in
the file are unchanged, so the output would repeat LIKELY-1's FAIL line.

**The word-codes in context (`witness/f67r_wordcodes_context.tsv`, 14 rows).** Rule 4: a value inferred from the clear
context is I (class only) or M (a word with two supports), never H. Result: **14 of 14 get a context class at grade I;
0 of 14 get a word value** -- the clear French around each group names no antecedent, only the slot. The slots:
`.71` the informant ("Jay sceu de [.71] quil a discouru ... ce quil a apris"); `.7` four times (L02, L21, L23, L27),
every time a person or title ("[.7] a eu quelque ombrage", "complaisance destinee a [.7]", "lhumeur de [.7]", "la
resolution immuable [.7], quil ne vous en scaura point de gre") -- the leaf's principal referent; `.27` a masculine
subject ("Que sy [.27] a quelque desir ... quil se resolue"); `.6` a conjunction slot ("bien avant [.6] Il fault"),
possibly the et-sign itself rather than a group; `.13` a person ("ce quil resentoit de [.13] ... quil continue a le
seruir"); `.03` twice, a person or party ("de [.03], Mend de ses amis"; "Car [.03] ..."); `.07` after "par"; `.25` a
masculine subject ("Que sy [.25] peult aller [.49]", then "luy"); `.49` a destination after "aller"; `.57` a masculine
person ("de [.57], qui pour peu quil face est beaucoup estime"). Two of these conflict with the no.58 glosses
(fr4715-montholon-1589/scripts/decode_rest.py OWN_GLOSS, Tomokiyo's dotted-code values, grade M): `'27 = les` and
`'25 = la` cannot fill the subject slots "Que sy [X] a quelque desir" / "Que sy [X] peult aller" -- a data conflict
between two witnesses (rule 4), logged in HYPOTHESES.md, not settled here. One observation that may explain it, marked
inference: on this leaf pass C and pass D distinguish a continuous **bar** over both digits (`.71 .7 .27 .13 .03 .25
.57`, all in person/title slots) from a **dot** over the first digit only (`.07 .49`, the "par [X]" and "aller [X]"
slots), and nevers.htm's fr.3633 witness describes the common-word codes as dot-marked; `'7` and `'13` are attested
dotted but unglossed in no.58's own dump. Whether bar and dot mark two code lists (names vs common words) is a
hypothesis for the no.37 step, not a finding.

**Not changed:** `key_vieuville_nevers.tsv` (no row from context -- the brief's own rule and rule 4); the clear-word
tokens of `f67r_ciphertext.tsv` (still the A/B reconciliation; pass C is a single pass, folding it in needs the
three-pass reconciliation named below). **Requests:** none (0 to gallica.bnf.fr or any host). Vision calls 5. No
credentials used. No AskUserQuestion. Rule 10: this section reports what the crops show and where no value was found;
it classifies nothing as new.

## Premise check (GAPS-fr4715-vieuville-pool-2, 2 Oct 2026)

Adversarial pre-reading pass per `.claude/briefs/check-solved.md` "Premise check", run before the Verdict step; the
question is whether no.44 (f.67) or no.37 (f.60) is already read somewhere. Each of (a)-(d) as found / not found /
unreachable.

(a) **Decipherments the folder and the dépouillement mention -- opened.** The BnF dépouillement (cached notice,
`sources/bnf-aem/cc577658_francais4715.html`, item 37: "Lettre avec chiffre, en partie déchiffrée, du Sr DE MONTHOLON.
Tours, 12 décembre 1589. Au dos cachets aux lettres M. M. I. O. entrelacées") names a partial decipherment of no.37.
Opened on Gallica (canvas f135, label '60r', `tools/gallica_folio.py` on the cached manifest; one native region fetch
560,1600,3250,1850 = the pasted-in strip, `images/src_ark_12148_btv1b52509819x_f135_560_1600_3250_1850.jpg`; and f136,
'60v', at 600 px, `images/pool_f60v_600.jpg`). **Found, and it is not a reading of the letter:** the 600 px pool sample
(POOL.md, "dense continuous cipher for about 22-24 lines") misdescribed the leaf. At native resolution f.60r is 31 lines
on a strip: lines 1-5 clear French with barred/dotted word-codes and one digit run, lines 6-14 dense cipher, lines 15-24
clear French with word-codes (line 15 and 24 mixed), lines 25-31 dense cipher, the clear close and date on line 31. The
"partie déchiffrée" is a set of small interlinear glosses in a lighter period hand written above word-code groups on the
clear lines only (13 glosses on 6 lines per the gloss pass below: codes 27, 71, 93, 7, 99, 5023, and two cut by the
band edge over the line-1 run 66 65 40 25 50 90) -- it glosses the word-code layer, not the dense cipher blocks, and
nothing on f.60v (blank verso of the mount; the strip's own back with the seals is pasted down). No.44 (f.67) is
not touched by it. So neither leaf is text-known from (a); the glosses are the known answer for the word-code layer
this pool's letter key does not cover (nevers.htm names and does not enumerate it).
The other mentions in this folder (no.58's OWN_GLOSS table from Tomokiyo's alignment; the Desenclos-Lasry PDF; Bourdeau
PR #9) were opened by LIKELY-1 and read nothing of no.37 or no.44.

(b) **Other solvers' working files for fr.4715 -- not found.** Fresh shallow clones, 2 Oct 2026 (`github.com`, 2
requests): `dbourdeau/cyphersolver` -- every `4715`/`Montholon` hit is in `research/gallica_sweep` (the cached notice,
SRU results, page mirrors) or `targets/r2276` (`fr4715_aligned.txt`: BnF fr.4715 **f.2r**, Cardinal de Guise to Nevers
1586, the Nevers-Piles cipher with its interlinear decipherment -- a different cipher and leaf, used by him as a key
witness for R2276); no output, rendering or apply-key file for f.60 or f.67, and no key of this pool's family has been
run on either leaf. `aaymeloglu/unsolved-ciphers` -- the only Montholon/Vieuville/4715 hit is a DECODE catalogue row
for fr.3975 f.101 (Nevers to La Vieuville, 1587), not these leaves.

(c) **Physical neighbours -- not found.** Dépouillement items around both leaves: f.59 (no.36, cipher with decipherment,
"le même que celui des nos 9 et 17" -- a different cipher), f.61 (no.38, "Lettre avec chiffre" = Tomokiyo's f.61, the
Mayenne polyphonic cipher of 1592, `ciphers/fr4715-f61-mayenne-1592`), f.66 (no.43, Mayenne to Nevers 1586, "chiffre et
déchiffrement", a 1586 cipher), ff.68-69 (nos.45-46, "le chiffre est le même que celui du n° 36"). No neighbour is a
clear copy or decipherment of no.37 or no.44; f.60v is blank (above); f.67v was not fetched (LIKELY-1: the date line
closes no.44 on the recto).

(d) **Recipient side -- not found / one lead unreachable.** Internet Archive: `advancedsearch` for the Nevers memoirs
(Gomberville 1665, "Les Mémoires de Monsieur le duc de Nevers") -- not on archive.org under that title (0 of 11 rows);
Mémoires de la Ligue (Goulart, 1758 ed., `memoiresdelaligu01-06goul`) -- `be-api` full-text search for "Montholon" in
vols 3 and 4 (1589-1591): 0 hits each. Google Books API (keyed, `country=US`, 8 queries, one 503 not retried): the
Gomberville 1665 edition is full view (`2KtPOA-povUC`) but a `filter=full` query for Montholon + Nevers returns no
volume with the name, and "Montholon" "12 décembre 1589" returns only manuscript catalogues plus **Boltanski 2006, Les
ducs de Nevers et l'État royal (`dsInahmnar8C`, PARTIAL view)**, whose snippet reads "Montholon, intendant de la maison
de Nevers à partir de 1589 et jusqu'en 1613 au moins, se voit confier des tâches ... 12 décembre 1589": she cites a
letter of this date, almost certainly this leaf, in a footnote; whether she quotes its text cannot be read from the
cloud (books.google.com page view is bot-blocked, CLAUDE.md host table) -- **unreachable**, a LOCAL-QUEUE edition-read
row is the way to settle it (named in Remaining gaps). The 1712 Anselme Histoire généalogique (full view) names
Montholon only as garde des sceaux.

**Verdict of the premise check:** no prior reading or plaintext of no.44 or of no.37's cipher located; no.37's own
period glosses read its word-code layer only and are the known answer used below. Clear to run the step. Rule 10: a
search result, not a novelty verdict.

## GAPS-fr4715-vieuville-pool-2 (2 Oct 2026, account-4): the Verdict step -- no.37 f.60r, the period glosses as the known answer

**Brief:** `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; the step as the previous Verdict line named it. Clock read
14:19-14:5x UTC 2 Oct 2026. Gallica: 2 requests (the f135 native region 560,1600,3250,1850 through `tools/iiif_lines.py`,
browser UA; f136 at 600 px) plus the cached manifest. Vision calls 4 of 4: (1) gloss pass, Opus 5.5, 2x crops
(`witness/f60r_gloss_pass.tsv`); (2) and (3) two value-blind Sonnet passes over the same 48 crops of the 16 clear lines
(`witness/f60r_pass_a.tsv`, `f60r_pass_b.tsv`) -- **both failed**, every line at L, pass B stopped after 4 lines
("could not read the secretary hand reliably"), the f.81r shape (MONT-4715, 27 Sept 2026: Sonnet declined 2400-px crops);
(4) one Opus 5.5 pass over a re-cut at 600-px segments upscaled 3x, 96 crops (`images/f60r_bands3/`, `witness/f60r_pass_c.tsv`,
5 lines M, 11 L). The third-eye call was therefore not available; the gloss disagreements were settled by the worker's own
look at 3x site crops (11 own image inspections, counted separately from the four calls, regenerable from
`scripts/cut_f60r_bands.py` and the band table). Crop cut: `tools/iiif_lines.py --dry-run` gave the 32 row-profile centres
(pitch 47 px); its first centre is the gloss row above line 1, and midpoint bands split every gloss between two crops, so
`scripts/cut_f60r_bands.py` cuts each band from 16 px above the midpoint (the interline with its gloss stays with its line),
the same private-cut precedent as the sibling's `images/regen_f81r_crops.sh`; crops are regenerable and not committed
(manifest keys `f60r_bands`, `f60r_bands3`).

**What the leaf is.** Not the dense-cipher leaf POOL.md's 600 px sample described: 31 lines, clear French with word-codes
(L01-L05, L15-L24, L31's close "Ce 12 Decemb[re]"), two dense cipher blocks (L06-L14, L25-L30, about 1,400 signs, not
transcribed this step) and three digit runs inside the clear lines (L05, L15-L16, L31). The "en partie déchiffrée" of the
dépouillement is the set of period interlinear glosses above word-codes on the clear lines (Premise check (a)).

**Known answer first (README common tail, 27 Sept 2026).** `witness/f60r_glosses_reconciled.tsv`: 13 gloss rows on 6 lines
(G 13, C 15 brace words, E 11 sites). Settled values, rule 4 (C = two witnesses and the worker's eye agree letter for
letter; M = legible in part; L = a few letters): **.7 = Roy (C, two sites L23), .71 = montolon (C, written twice on L01 over
each 71 -- the sender's own surname), .93 = Mr (C), .27 = nauarre? (M, two sites L01/L20; Opus reads nauarre at both, the
worker's eye cannot exclude nemours), .99 = bours (M, L24; L21 site bou??)**; legat (M) over the start of the run 50 23 30
on L20, group unsettled, not keyed; labr?/de? (L) over the L01 run 66 65 40 25 50 90, cut by the band edge; pen? (L) at L22,
possibly an interlinear insertion; dn (L, pass C only) at L20. `tools/interlinear_align.py align --floor 1` over
`witness/f60r_pairs.tsv` (13 tokens, 8 values): 4 agree (7 x2, 27 x2), 6 single, 2 doubtful, 1 conflict (99: bou vs bours,
the L21 site) -- `witness/f60r_align_key.tsv`. Key file: `key_wordcodes_f60r.tsv` (C 3, M 2 values; `_all.tsv` keeps every
row for the control).

**Rule 3 test, `scripts/wordcode_slot_test.py --shuffles 20`.** Statistic: of no.44's 14 word-code slots
(`witness/f67r_wordcodes_context.tsv`, slot class at grade I), the ones whose code is glossed on f.60r and whose gloss class
fits the slot. REAL 6/7 = 0.857 (.71 informant slot = montolon; .7 x4 person slots = Roy; .27 "Que sy [X] a quelque desir" =
nauarre?; .25 "Que sy [X] peult aller" = de? L, no fit). CONTROL, the gloss values permuted among the glossed codes (every
row of `_all.tsv`, so non-person classes can land on a slot): mean 3.20/7, max 6/7, **4 of 20 shuffles reach REAL** -- the
control varies, and the real key sits at its top but not alone (p about 0.2 at N=7). Side by side: REAL 0.857 vs shuffle
mean 0.457. Not a pass at this N; what carries the result is the per-value agreement (the same code glossed the same way at
two places on the leaf, 7 and 27 and 71) and the fit of Roy to no.44's four .7 slots.

**Decode (rule 7).** `decode.json` job 2: `f60r_ciphertext.tsv` (pass C tokenised: 441 clear words, 175 cipher tokens) under
`key_vieuville_nevers.tsv` + `key_wordcodes_f60r.tsv`; `tools/decode_key.py ciphers/fr4715-vieuville-pool --check` exit 0 for
both jobs: f.60r tokens 175: AB 133 (the digit runs under the printed letter table -- a decode, not read against anything),
M 11 (the glossed word-codes: the key grade C/M is lowered to M per token because pass C's line confidence is L on those
lines), U 31; f.67r unchanged, 27 tokens AB 8 U 19. No judge run (no continuous reading claimed; the clear lines are a
transcription at 5 M / 11 L). No "reading ready" line.

**Carried back to no.44 (`witness/f67r_wordcodes_context.tsv`, new column `f60r_gloss`).** .7 (4 slots) = Roy, .71 = montolon,
.27 = nauarre?, .25 = de? -- graded M on no.44 (a period gloss on a sibling leaf of the same cipher plus a fitting slot; not
read from no.44's own leaf), the rest untouched. The no.58 conflict (HYPOTHESES.md: Tomokiyo's '27 = les, '25 = la) now has
a C/M-grade period witness against it on .27: on this leaf 27 under a bar is glossed as a name at two sites.

**Requests this job.** gallica.bnf.fr 2; archive.org 2 (advancedsearch) + be-api 2; googleapis.com 8 (one 503, not retried);
github.com 2 shallow clones. No 403/429. No credentials printed. No AskUserQuestion. Rule 10: what was found and where it
was not; nothing here is called new or first.

## GAPS-fr4715-vieuville-pool-3 (2 Oct 2026, account-4): the Verdict step -- the four L-grade gloss sites on no.37 re-read from tall native crops

**Brief:** `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`, the Verdict step as GAPS-2 wrote it. Clock read 20:23-20:4x UTC
2 Oct 2026. Intake gate exit 0. Requests: none (the native region of canvas 135 was on disk; no Gallica fetch). Vision calls:
1 of 1, the strong model of this session reading one labelled sheet of four tall crops. Crops: `scripts/cut_f60r_gloss_sites.py`
(committed, regenerable, crops not committed) cuts each site from the line above to below the line itself at 1.5x, so the
interline gloss is no longer split by a band edge.

| Site | Before (GAPS-2) | This read | Grade (rule 4) | Reason |
|---|---|---|---|---|
| L01 run 16 65 40 25 50 90 | labr? L, de? L (cut by the band top) | three words: 'labr' over 65 40, 'de' over 25/50, ?gal? over 50 90 | labr M, de M, ?gal? M | 'de' is clear as text but straddles the 25/50 boundary; 'labr' is four legible letters, not a word as written; the third word's first and last letters are unsure |
| L20 legat over 50 23 30 | legat M | legat, clear letter for letter, written from the 0 of 50 to the 3 of 30 | M | the text would be C, but it spans 23 30, so no single group carries it; not entered in the key |
| L20 dn | dn L, over a barred 16 after 'du' (pass C only) | du or dn over the dotted 16 of '95 16', before the clear 'du' | M | u/n ambiguous; mark corrected from bar to dot, position corrected |
| L22 pen? | pen? L, a gloss over a barred 2? | 'peu d' with a superscript e/v: an interlinear insertion 'ny a [peu de] remede' | M | the sense fits an insertion; the barred-2 shape reads as the insertion mark, not a word-code |

No value is C, because no site pairs a legible gloss with one settled group. No decode-key value changed:
`key_wordcodes_f60r.tsv` is untouched, `key_wordcodes_f60r_all.tsv` (control only) and `witness/f60r_glosses_reconciled.tsv`
carry the new rows, and no.44's slot table (`witness/f67r_wordcodes_context.tsv`) records .25 = de as a preposition that
cannot fill its person slot. `scripts/wordcode_slot_test.py --shuffles 20`: REAL 6/7 = 0.857 vs 20 value-shuffled keys mean
3.20/7, max 6/7, 4 of 20 at or above REAL (unchanged; not a pass at N=7). `tools/decode_key.py ciphers/fr4715-vieuville-pool
--check` exit 0 on both jobs (f.67r 27 tokens AB 8 U 19; f.60r 175 tokens AB 133 M 11 U 31). Seen in passing on the sheet,
not graded: a large '95' in darker ink in the right margin of L01-L02 (a later hand?), and a 'Roy' gloss over the barred
figure after 'de' on L20 that pass C read as 6. Rule 10: nothing here is called new or first; only the glosses are read.

```
$ python3 tools/intake_gate_check.py fr4715-vieuville-pool   # exit 0
fr4715-vieuville-pool: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
$ python3 tools/gaps_check.py fr4715-vieuville-pool   # exit 0
OK keep-going fr4715-vieuville-pool: keep going: 5 internal gap(s), 1 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
```

## GAPS-fr4715-vieuville-pool-4 (2 Oct 2026, account-4): the Verdict step -- the no.37 dense cipher block L06-L14 read and decoded

**Brief:** `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; the Verdict step as GAPS-3 wrote it. Clock read 20:50-21:4x UTC
2 Oct 2026. Intake gate exit 0. Requests: none (canvas 135's native region on disk). Vision calls 8 of 8, all Opus 5.5 subagents:
pass A b1-b3 and pass B b1-b2 over the first cut (images/f60r_blocks3, 3x, 600 px segments, centred on a straight slope), passes
A' and B' over a re-cut of s4-s6 (images/f60r_blocks3t), one reconciliation call. **Scope cut (brief's fallback): L06-L14 only;
L25-L30 is the next step.** Why: both pass-A batches and pass B b1 reported independently that from about x 1900 the lines curve
up (up to 60 px at the right edge), so the first cut's s4-s6 crops sat on the next line down. `scripts/cut_f60r_bands.py --track`
(new) follows each line by its ink row profile in 270 px strips and cuts a straightened band; L06-L14 s4-s6 were re-cut and re-read
by both passes, and the s1-s3 reads of the first cut kept (`scripts/f60r_blocks.py merge`). L25-L30 has only pass A b3 on the
misaligned cut, not used. **Found on the way:** the 31 row centres in `cut_f60r_bands.py` (iiif_lines dry run, GAPS-2) miss a whole
cipher row in the lower block -- "Day parle 2593..." at y about 1563, between the centres called L28 (1521) and L29 (1593) -- so the
lower block is 7 rows, not 6, and its line labels from L29 down are off by one.

**Control first (rule 3).** (a) The judge on no.58's known text (Tomokiyo's printed decipherment, fr4715-montholon-1589/known_plaintext.txt)
at the target's N: PASS (N=700 -0.837, N=604 -0.844 vs real_p05 -0.878). (b) The design-matched control, no.58's own cipher (Tomokiyo's
group dump) decoded under the same key with word-codes dropped, the exact construction of the target candidate: **FAIL** (N=818 -1.085,
N=700 -1.072, N=604 -1.056 vs real_p05 about -0.88). So the judge cannot pass a correct decode of this design at this N: a judge FAIL on
the target is a **non-test** (rule 3, Salviati paragraph: match the design), and only (c) carries the result. (c) `scripts/keytest.py
known-answer`, re-run: no.58 dump, real key 729/818 = 0.891 vs 200 letter-shuffled keys mean 0.353 sd 0.100 max 0.631, z 5.37, rank 1 of
201. (d) Segmenter control, `scripts/f60r_blocks.py segcontrol`: no.58's dump with its grouping removed is re-segmented by the same
inventory-only DP to 950 of Tomokiyo's 952 groups (0.998).

**Transcription.** `tools/reconcile_passes.py` over the merged passes (witness/f60r_blocks_pass{A,B}_long.tsv): 9 lines, A 1,404 / B 1,422
units, **agreement 1,334/1,432 = 93.2 pct** (nw; a dot on one pass and not the other counts as a disagreement). The 98 disagreements went
to one reconciliation call (witness/f60r_blocks_recon.tsv): 41 to A, 53 to B, 4 other; 16 H, 62 M, 20 L, the L ones mostly one shape (an
open c-shaped 0 with a rising stroke: a separate 5/6 or a ligature). Settled values: witness/f60r_blocks_settled.tsv.
**The 8 problem.** Neither pass wrote a single 8 in about 1,400 digits (no.58's dump: 8 is 7.8 pct of digits; MONT-4715's confusion
matrix already lists 8->0, 8->1, 8->5 for this hand). No key code starts with 0, so the segmenter reads an out-of-key pair 0x as 8x when
8x is a key code (inventory only, the same stream for every shuffled key); 66 tokens rest on this rule, graded I for that digit. A blind
shape check inside the reconciliation call (8 zeros, 4 of them pair-initial = implied 8, 4 pair-final, classes hidden) was
**non-discriminating**: 7 of 8 read as the same closed pointed oval with a tail, the one different form (Z4) a pair-initial; the shape
test neither supports nor excludes the rule.

**Decode (rule 7).** `decode.json` job 3: `f60r_blocks_ciphertext.tsv` (749 tokens) under key_vieuville_nevers.tsv;
`tools/decode_key.py ciphers/fr4715-vieuville-pool --check` exit 0 (all three jobs; job 3: AB 604, U 145). Reading of record:
`f60r_blocks_reading.txt`. **Rule 4 grades, 749 tokens:** 604 letter tokens read from the printed key (key-source values, AB in the key
file), of which 538 at H for the value and 66 at I (the 8 rule); transcription confidence of the 604: M 134, L 470 (line-level, the lower
crop confidence of the line inherited by every token -- most lines have one L crop); 110 dotted/barred word-codes U (not in any key; the
five glossed on f.60r's clear lines are not among them by value check, not applied); 35 undotted out-of-key groups U. No C, no S.
Fragments legible in the decoded string (letters as decoded, grade H by value, not a reading): "dissimulation peult", "leglise",
"empesche ledit duc", "religion", "pas expedient", "royaume soit divise", "coulpable", "du feu", "declaration", "remedier".

**Numbers, side by side.**

| test | target L06-L14 (N=604 letters) | matched control | shuffled |
|---|---|---|---|
| keytest word-cover, 200 letter-shuffled keys | 479/604 = 0.793, mean 0.331 sd 0.090 max 0.604, **z 5.11, rank 1 of 201** | no.58 dump 0.891 vs 0.353, z 5.37, rank 1 of 201 | -- |
| judge (fr16, `witness/f60r_blocks_judge_output.txt`) | FAIL -1.275 (real_p05 -0.878, null_p99 -1.874), cover 0.849 | no.58 decode same design N=604: FAIL -1.056; no.58 known text N=604: PASS -0.844 | target tokens shuffled, 5 seeds: -1.92 to -2.01, all below the null p99 |

```
$ python3 tools/judge_plaintext.py specs/fr4715-vieuville-pool.json --file ciphers/fr4715-vieuville-pool/witness/f60r_blocks_judge_candidate.txt
FAIL language: score=-1.275, null_p99=-1.874, real_p05=-0.878, real_median=-0.787, mode=both, N=604
ok   words: cover=0.849, min=0.5, real_text_median_cover=0.945
FAIL - fr4715-vieuville-pool (a PASS is a gate for a verifier, not a reading; rule 10)
```

**Verdict of the step.** The printed key reads the block: rank 1 of 201, z 5.11, beside its known-answer control's z 5.37 at N=818; the
judge FAILs, but its design-matched control FAILs too, so the judge is a non-test here (not a negative), while the target sits far above
its own shuffled-token decodes. No "reading ready" line: the brief asks for the judge AND the shuffled-target check, and the judge cannot
clear. Rule 10: nothing here is called new or first; Tomokiyo lists no.37 under the Vieuville-Nevers heading with no reading (nevers.htm,
LIKELY-1's check) -- what was found and where it was not found only.

```
$ python3 tools/intake_gate_check.py fr4715-vieuville-pool   # exit 0
fr4715-vieuville-pool: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
$ python3 tools/decode_key.py ciphers/fr4715-vieuville-pool --check   # exit 0
reading up to date
$ python3 tools/gaps_check.py fr4715-vieuville-pool   # exit 0
OK keep-going fr4715-vieuville-pool: keep going: 6 internal gap(s), 1 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
```

## GAPS-fr4715-vieuville-pool-5 (2 Oct 2026, account-4): the Verdict step -- the 8-glyph sheet, then the lower block L25-L30 + L28b

**Brief:** `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`. Clock read 21:45-22:1x UTC 2 Oct 2026. Intake gate exit 0.
Requests: none (canvas 135's native region on disk). Vision calls 4 of 4, all Opus 5.5 subagents: 1 glyph sheet, 2 blind passes,
1 reconciliation.

**(1) The 8-glyph sheet (value-blind, one call).** `scripts/f60r_zero_locate.py` placed every zero that both GAPS-4 passes agree on
(L06-L14, straightened native bands) by aligning ink blobs to the pass-A digit string by width, then picking the zero-like blob within
one place; the worker eye-checked the boxes (position only, with the classes hidden on the tiles) and kept 35 of 72. `scripts/f60r_zero_sheet.py`
cut 30 tight tiles (all 12 kept pair-initial zeros, class P: the rule reads them 8; 18 of 23 pair-final zeros, class F: second digit
of a key code x0), shuffled them as Z01-Z30 (`images/f60r_zero_sheet.png`; hidden truth `witness/f60r_zero_sheet_truth.json`). Not
the brief's 15/15: only 12 P sites were placed reliably. One call, classes hidden, asked for two shape classes (`witness/f60r_zero_sheet_read.tsv`):
A 17 closed ovals, B 13 open cups with a rising stroke, own confidence M. **Against the hidden truth: 21 of 30 agree** (P->B 8/12,
F->A 13/18). **Shuffled-label control (rule 3), 10,000 permutations of the P/F labels: mean 17.1, sd 1.8, p95 21, max 27; p(>=21)
= 0.060.** Not better than the control at the 95 pct line, so by the brief **the 66 tokens of L06-L14 stay at I.** The direction leans to
the rule (open cup = P) but the tight tiles cut off the exit stroke, and two tiles (Z04, Z11) sit off their glyph.

**(2) The lower block.** `scripts/cut_f60r_lower.py` (new): the GAPS-4 ink tracking with the unlisted row inserted under its own label
**L28b** (y about 1563) so L29-L31 keep their labels in the other jobs; 7 rows x 6 segments = 42 straightened 3x crops
(`images/f60r_lower3t/`, regenerable, not committed). Row check, `tools/iiif_lines.py` over the left third of the region:
```
$ python3 tools/iiif_lines.py --image ciphers/fr4715-vieuville-pool/images/src_ark_12148_btv1b52509819x_f135_560_1600_3250_1850.jpg --out <scratch> --region 0,1340,1200,360 --distance 30 --dry-run
... region 1200x360, 7 lines, 7 bands x 1 segments; pitch 50 distance 30 prominence 90.6
  centres (region y): 29 83 133 179 229 279 331
```
Seven rows, as GAPS-4 found. Two blind Opus passes, one call each over the 42 crops (B in reverse order): `witness/f60r_lower_pass{A,B}.tsv`,
merged by `scripts/f60r_blocks.py merge lower`. `tools/reconcile_passes.py` (nw, --keep-dots --keep-plain): **A 792 / B 797 signs,
agreement 666/809 = 82.3 pct**, 143 disagreement columns. 46 are word-against-word on the clear French (L25 s1-s3, L27, the
frames of L28/L28b), not reconciled: the draft's value stands and a clear word breaks a cipher run whatever its spelling. The other 97
went to one reconciliation call (`witness/f60r_lower_recon.tsv`): A 17 / B 75 / other 5; H 7 / M 82 / L 8, plus two corrections to
agreed context (L30 col 105 .4, L29 col 136 9->4 at L); settled in `witness/f60r_lower_settled.tsv`, segmented by `scripts/f60r_blocks.py segment lower`.

**The 8 rule, tested by a blind reader (no vision call).** Here pass B wrote 87 eights and pass A 14: B reads this hand's open c with
a rising flick as 8 (its own note), A as 0. `scripts/f60r_eight_check.py`: segment pass A's own stream with the GAPS-4 inventory-only
segmenter, label each A zero P (rule says 8) or F (true 0 in a key code x0), and read what blind pass B wrote at the same place:
**B reads 8 at 35/39 P sites (0.897) and 4/50 F sites (0.080)**; statistic 0.817 vs **shuffled P/F labels x10,000: mean 0.001, p95
0.178, max 0.452, p < 0.0001** (`witness/f60r_lower_eight_check.txt`). A reader who never saw the key puts its 8s where the key's
inventory says 8 goes. On this block the 8s are read off the page (48 tokens), and only 3 tokens still rest on the rule. This
corroborates the rule for the same hand, but the 66 L06-L14 tokens stay at I: the brief's test for them was the sheet, and their
own glyphs have not been re-read.

**Decode (rule 7).** `decode.json` job 4, `f60r_lower_ciphertext.tsv` (443 tokens) under key_vieuville_nevers.tsv;
`tools/decode_key.py ciphers/fr4715-vieuville-pool --check` **exit 0** (all four jobs; job 4: AB 308, U 70). Reading of record:
`f60r_lower_reading.txt`. **Rule 4 grades, 443 tokens:** 308 letter tokens read from the printed key: 305 at H for the value, 3 at
I (the 8 rule); transcription confidence of the 308: M 157, L 151 (line-level). 67 dotted/barred word-codes U, 3 undotted out-of-key
groups U (46, 6, 78), 65 clear words (the frames of L25, L27, L28, L28b, not graded as cipher). No C, no S. Fragments legible in the
decoded string (letters as decoded, grade H by value, not a reading): "contre vostre ame", "ledit sieur", "plus pres", "un docteur"
(between the clear words "Day parle" and "estime le l'homme de biens et capable"), "m'a dit", "esperance", "il y a trop plus mal",
"infinis malheurs sont advenus a ceulx", "ont favorise", "doit apprehender", "esperer", "dieu favorisera".

**Numbers, side by side.**

| test | target L25-L30 + L28b (N=308 letters) | matched control | shuffled |
|---|---|---|---|
| keytest word-cover, 200 letter-shuffled keys (`witness/f60r_lower_keytest.txt`) | 268/308 = 0.870, mean 0.334 sd 0.102 max 0.633, **z 5.24, rank 1 of 201** | no.58 dump 0.891 vs 0.353, z 5.37, rank 1 of 201 (GAPS-4, N=818); L06-L14 z 5.11 (N=604) | -- |
| judge (fr16, `witness/f60r_lower_judge_output.txt`) | FAIL -1.261 (real_p05 -0.876, null_p99 -1.832), cover 0.88 | no.58 decode of the same design FAILs at N=604 (-1.056, GAPS-4): non-test | -- |
| 8 rule vs blind pass B | P 35/39 read 8, F 4/50 | shuffled P/F labels p95 0.178 | p < 0.0001 |
| glyph sheet, L06-L14 | 21/30 | shuffled labels p95 21, p 0.060 | -- |

A window control at N=311 cannot be built from no.58 (`keytest.py known-answer --window 311` fails: no run of 311 in-key groups without
a word-code); the target result is rank 1, a positive, so it is not a miss whose power is in question (rule 3, ARM3-ADJ).

```
$ python3 tools/judge_plaintext.py specs/fr4715-vieuville-pool.json --file ciphers/fr4715-vieuville-pool/witness/f60r_lower_judge_candidate.txt
FAIL language: score=-1.261, null_p99=-1.832, real_p05=-0.876, real_median=-0.782, mode=both, N=308
ok   words: cover=0.88, min=0.5, real_text_median_cover=0.945
FAIL - fr4715-vieuville-pool (a PASS is a gate for a verifier, not a reading; rule 10)
```

**Verdict of the step.** The printed key reads the lower block too: rank 1 of 201, z 5.24, beside its known-answer control's z 5.37.
Both cipher blocks of no.37 are now decoded: 912 letter tokens. The judge stays a non-test for this design. No "reading ready"
line, for the same reason as GAPS-4. Rule 10: nothing here is called new or first; this records what was found and where it was not
found (Tomokiyo, nevers.htm: no.37 listed without a reading).

```
$ python3 tools/intake_gate_check.py fr4715-vieuville-pool   # exit 0
fr4715-vieuville-pool: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
$ python3 tools/decode_key.py ciphers/fr4715-vieuville-pool --check   # exit 0
reading up to date
$ python3 tools/gaps_check.py fr4715-vieuville-pool   # exit 0
OK keep-going fr4715-vieuville-pool: keep going: 6 internal gap(s), 1 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
```

## GAPS-fr4715-vieuville-pool-6 (2 Oct 2026, account-4): the Verdict steps -- the f67r frame reconcile, then the 66 L06-L14 8-rule sites in line context

**Brief:** `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`. Clock read 22:21-22:4x UTC 2 Oct 2026. Intake gate exit 0.
Requests: none (all images on disk). Vision calls 2 of 3, both Opus 5.5 subagents (two blind passes); the reconciliation call
was not spent, because the two passes did not disagree at a single rule site (below).

**(1) The f67r clear-French frame.** `tools/reconcile_passes.py` over passes A, B, C (`--keep-dots --keep-plain`) aligns token
by token and gives 256/723 = 35.4 pct three-way agreement, but the passes divide the words differently (A `Jaysouel`, C
`Jay sceu de`), so that figure measures word division, not reading. `scripts/f67r_frame_fold.py` (new) takes pass C (the
strong blind pass) as the backbone and asks, per C word, whether A or B wrote the same normalised word at the aligned place
(difflib per line, plus a no-space substring test for words of 4+ letters): **C 609 frame words, A agrees 322, B 275, A or B
341 (56.0 pct)**; frame confidence **H 325 / M 86 / L 198** (H = C plus a Sonnet pass, C not L; M = agreement with C at L, or
C alone at H; L = C alone at M/L). L31 keeps its old A/B frame (23 words at L): C reads a cipher `2` there that pass D settled
as the clear word `w:2ii`. **The 27 cipher tokens are carried over unchanged** (checked by diff), so `tools/decode_key.py
--check` exits 0 with the same grades: f67r 27 tokens, AB 8, U 19 (rule 4: 8 H by key value, 19 U; unchanged).
`witness/f67r_judge_candidate.txt` regenerated from the reading (bracketed U tokens dropped), judge re-run:
```
$ python3 tools/judge_plaintext.py specs/fr4715-vieuville-pool.json --file ciphers/fr4715-vieuville-pool/witness/f67r_judge_candidate.txt
FAIL language: score=-1.012, null_p99=-1.914, real_p05=-0.867, real_median=-0.782, mode=both, N=2677
ok   words: cover=0.895, min=0.5, real_text_median_cover=0.946
FAIL - fr4715-vieuville-pool (a PASS is a gate for a verifier, not a reading; rule 10)
```
Up from -1.145 (cover 0.872) on the A/B frame, still below real_p05. Of the 2,677 letters only 8 come from the key, so this
measures how well the clear frame is transcribed, not the key. The judge is already a non-test on this design (the no.58
design-matched control FAILs, GAPS-4), so it is reported here and not used as a gate.

**(2) The 66 L06-L14 8-rule sites, re-read in line context.** Crops: rows checked with
```
$ python3 tools/iiif_lines.py --image ciphers/fr4715-vieuville-pool/images/src_ark_12148_btv1b52509819x_f135_560_1600_3250_1850.jpg --out <scratch> --region 0,415,1200,415 --distance 30 --dry-run
... region 1200x415, 9 lines, 9 bands x 1 segments; pitch 45 distance 30 prominence 109.8
  centres (region y): 37 80 120 162 205 246 291 337 386
```
(nine rows, L06-L14), then cut as the GAPS-4 straightened bands (`scripts/cut_f60r_bands.py --lines 6..14 --seg 600 --scale 3
--track --centred 30 28 --shift 6`, 54 crops 1800x174, scratch, regenerable, not committed; the worker eye-checked four).
Two blind Opus passes, one call each over all 54 crops (B in reverse order), **not told the 8 rule, the key or any earlier
value**, with one neutral line: decide every round glyph (0/6/8/9) from its full shape including any entry or exit stroke,
and do not normalise doubtful shapes (`witness/f60r_blocks_g6_pass{A,B}.tsv`). `scripts/f60r_eight_relook.py` (new)
labels each zero of the settled stream P (first digit of an `8<` token, 66) or F (second digit of an undotted key code x0,
a true 0, 97), aligns each pass per line, and reads what it wrote there (`witness/f60r_blocks_eight_relook.tsv`).

| | P sites (rule says 8) | F sites (true 0) | shuffled P/F labels x10,000 |
|---|---|---|---|
| pass A reads 8 | 0/66 | 0/97 | mean 0.000, p95 0.000 |
| pass B reads 8 | 0/66 | 0/97 | mean 0.000, p95 0.000 |
| both read 8 (the move rule) | **0/66** | 0/97 | statistic 0.000, p(>=obs) 1.0 |

64 P sites read 0 by both passes, 2 unaligned in both; neither pass marked any P site unsure. Over the whole block pass A wrote 3
eights (plus 3 `(0/8)` alternatives, none at a P site), pass B 1. **Sites moved I -> H: 0 of 66.** The control is a non-test, not
a negative: when neither reader writes an 8 anywhere, the shuffled labels cannot differ from the target any more than the
target can differ from them (rule 3, "a control that cannot vary"). Contrast GAPS-5's lower block, where a blind reader wrote 87
eights and put 35/39 at rule sites. **Rule 4 grades, before and after:** L06-L14 604 letter tokens, 538 H + 66 I (unchanged);
lower block 308, 305 H + 3 I (unchanged); f67r 27 tokens, AB 8 / U 19 (unchanged). `tools/decode_key.py --check` exit 0.

**Rule 3, third-attempt clause.** Three instruments have now read these 66 glyphs blind and none separates them: the GAPS-4
passes (no 8 in about 1,400 digits; a shape check 7/8 alike), the GAPS-5 value-blind tile sheet (21/30, p 0.060), and these
line-context passes (0/66 both). Blind visual re-reading of L06-L14 by a model is logged **untestable by this instrument at
this cut**, not refuted; the rule is not weakened (GAPS-5's lower-block result stands). The next attempt has to be a different
instrument, not a fourth re-read.

Rule 10: nothing here is called new or first; this records what was found and where it was not found.

```
$ python3 tools/intake_gate_check.py fr4715-vieuville-pool   # exit 0
fr4715-vieuville-pool: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
$ python3 tools/decode_key.py ciphers/fr4715-vieuville-pool --check   # exit 0
reading up to date
$ python3 tools/gaps_check.py fr4715-vieuville-pool   # exit 0
OK keep-going fr4715-vieuville-pool: keep going: 6 internal gap(s), 1 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
```

## GAPS-fr4715-vieuville-pool-7 (2 Oct 2026, account-4): the Verdict step -- key-side word-cover test of the 66 L06-L14 8-rule sites

**Brief:** `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`. Clock read 22:38-22:4x UTC 2 Oct 2026. Intake gate exit 0.
Disk only: requests 0, vision calls 0. A different instrument from the three retired blind re-reads (GAPS-6, rule 3 third-attempt
clause): `scripts/eight_cover_test.py` (new). For each of the 66 sites the first digit is set to 8, 0, 6, 9 or 3 (second digit
kept), the token decoded with key_vieuville_nevers.tsv (0x and 33/34/35 are out of key and break the run), every other token held at
its record value, and the run(s) touching the site scored by letters covered by fr16 words (`scripts/keytest.py` cover(), 3-14
letters, freq >= 3). A candidate wins a site when its cover is strictly above every other's. The script rebuilds both blocks' token
streams from the reconciled drafts and asserts they equal the committed ciphertexts (so the 66 '8<' flags are the segmenter's own).
Per-site table: `witness/f60r_eight_cover.tsv`.

| | 8x | 0x | 6x | 9x | 3x | tie |
|---|---|---|---|---|---|---|
| target sites won (of 66) | **23** | 0 | 1 | 6 | 0 | 36 |
| target covered letters, summed | **610** | 489 | 574 | 565 | 492 | -- |

**Control (rule 3), 20 seeds:** 66 sites drawn from the 691 settled tokens (undotted in-key codes not resting on the rule, first
digit not 8, second digit matched to the target's 0/3/4/5 counts 1/24/3/38), same scoring: **8x win share mean 0.105, sd 0.031,
min 0.061, max 0.167; target 0.348, rank 1 of 21, above every seed.** Over the whole pool 8x wins 45/691 (0.065). The control varies on
the axis measured (which first digit wins at a site), so it can fail differently from the target.
**Known answer (the instrument's power):** at settled tokens whose true first digit is a candidate, the true digit wins 17/46 page-read
8x tokens (lower block, 0.370), 40/122 6x (0.328), 57/153 9x (0.373), 3/10 30 (0.300); 8x wins 11 of the 181 settled upper-block 6x/9x
sites (0.061). So the test finds a true 8 about 37 pct of the time and a false 8 about 6-11 pct; the target's 35 pct sits at the
known-answer rate for real 8s, not at the chance rate.

**Result.** The licence's three conditions hold: 8x wins more sites (23) than every alternative (9x 6, 6x 1, 0x 0, 3x 0), beats all 20
control seeds, and the known-answer check separates true 8s from non-8s. **Sites moved: 23 of 66, I -> S, not H** -- the value under
8x is the printed key's (H), but the first digit is restored by a key-side word-cover test with a control, which is rule 4's S
(cryptanalytic with a control; each moved site's letter sits inside a covered word of 3+ letters in its run), not read from the page or a
key source. 36 ties (the run gives no word either way) and 7 sites another digit wins (9x at L08 238, L09 262, L09 324, L10 401, L11 479,
L13 626; 6x at L07 103, all `85`/`83` records, mostly by 3 letters or fewer) stay at I; the 7 are flagged, not changed (a single-site
win at the chance rate is not a licence to re-read either way). No token value changed, so `tools/decode_key.py --check` exits 0 with the
same counts. **Rule 4 grades, L06-L14, 604 letter tokens: before 538 H + 66 I; after 538 H + 23 S + 43 I.** Lower block 305 H + 3 I and
f67r AB 8 / U 19 unchanged. The judge stays a non-test on this design (GAPS-4) and was not run. Rule 10: nothing here is called new or
first; this records what was found and where it was not found.

```
$ python3 scripts/eight_cover_test.py
target sites (L06-L14, 8 rule): 66
target wins by candidate: 8x 23, 0x 0, 6x 1, 9x 6, 3x 0, ties 36 (of 66)
target total covered letters: 8x 610, 0x 489, 6x 574, 9x 565, 3x 492
control pool (settled, first digit not 8, second digit 0/3/4/5): 691; by second digit {'0': 144, '3': 354, '4': 17, '5': 176}; target needs {'0': 1, '3': 24, '4': 3, '5': 38}
control 8x win share, 20 seeds x 66 sites: mean 0.105 sd 0.031 min 0.061 max 0.167
target 8x win share 0.348; beats every seed: True; rank 1 of 21
whole pool (691 settled non-8 sites): 8x wins 45 (0.065)
$ python3 tools/decode_key.py ciphers/fr4715-vieuville-pool --check   # exit 0
f60r_blocks_ciphertext.tsv: tokens 749: AB 604, U 145
reading up to date
$ python3 tools/intake_gate_check.py fr4715-vieuville-pool   # exit 0
fr4715-vieuville-pool: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
$ python3 tools/gaps_check.py fr4715-vieuville-pool   # exit 0
OK keep-going fr4715-vieuville-pool: keep going: 6 internal gap(s), 1 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
```

## GAPS-fr4715-vieuville-pool-8 (2 Oct 2026, account-4): the Verdict step -- print check on no.44/no.37 phrases

**Brief:** `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`. Clock read 22:57-23:0x UTC 2 Oct 2026. Intake gate exit 0. Vision
calls 0. Inputs: `phrases.txt` (19 lines: 9 interior clear-French phrases of no.44 f.67r from the three-pass H frame, 9 of no.37 f.60r's
clear lines, grade M/L and conditional on pass C's transcription (rule 2), 1 positive control), `sources.tsv` (Mémoires de la Ligue 1758
vols 3-4, the 1589-91 volumes, cached djvu text from NEXT-F61; one OpenAlex keyword line). Output: `print-check.tsv` (every query, 87
rows), `print-check-hosts.tsv`. Openings and date lines left out (VERIFY-CLINTON: incipits miss).

**Positive control.** No letter of this sub-pool is known to be in print (Premise check (d) above), so the control is the nearest printed
text of the same period and subject: "cache dix ou douze jours avec le duc de nevers", Mémoires de la Ligue vol.4 (1590 narrative,
also in Cayet's Chronologie novenaire). It hits on every instrument that can carry it: cached Ligue vol.4 exact (1), IA full text 15
items, Google Books 10 volumes, Gallica `text adj` 3 records. OpenAlex misses it, so OpenAlex is a non-test for phrase search here
(it indexes metadata and abstracts, not edition text); its target misses below license nothing.

| instrument (requests) | control | no.44 (9 phrases) | no.37 (9 phrases) |
|---|---|---|---|
| Mémoires de la Ligue v.3, v.4, cached djvu, exact + proximity (0) | v.4: 1 exact | 0 / 9 | 0 / 9 |
| IA full text, all items, be-api (19) | 15 items | 0 / 9 | 1 / 9 generic only ("plaire a dieu et au monde": 44 devotional items, Curé d'Ars etc.) |
| Google Books API, keyed, country=US (19) | 10 volumes | 0 / 9 specific; 4 loose word-bag returns of 300+ volumes; "se resolue de luy descouurir ouuertement": 11 volumes led by Mémoires de l'estat de France sous Charles IX (1578), which predates the letter -- a phrasing coincidence or loose match | 0 / 9 specific; 6 loose returns of 300+ volumes; "plaire a dieu et au monde": 2 volumes of 1521 |
| Gallica SRU `text adj`, Gallica-wide, covers Gomberville 1665 (5: 2 + 2 + control) | 3 records | 0 / 2 | 0 / 2 |
| OpenAlex, quoted phrase + 1 keyword line (6) | 0 (non-test) | 0 / 2 | 0 / 2 |

**Result.** No printed text of either letter located by these instruments on 2 Oct 2026: 0 specific hits for no.44, 0 for no.37, while
the control phrase is found by four of the five instruments. Requests: be-api.us.archive.org 19, www.googleapis.com 19, api.openalex.org
6, gallica.bnf.fr 5 = 49 of the 60 allowed. Not covered: Boltanski 2006 (page view bot-blocked, gap below), Henry IV's Lettres missives
(the King's outgoing letters only, neither sender), any Montholon or La Vieuville edition (none located). Gomberville 1665 is covered
only through Gallica-wide phrase search, whose OCR quality for 1665 type was not tested beyond the control (a 19th-c. printing), so it
is a weak negative for that edition. Rule 10: a search result for the verifier, not a novelty verdict; nothing here is new or first.

## Remaining gaps (LIKELY-1, 2 Oct 2026; updated in place by GAPS-fr4715-vieuville-pool-2, -3, -4, -5, -6, -7 and -8, 2 Oct 2026)
Read so far: (updated GAPS-5) no.37 f.60r both dense blocks decoded: L06-L14 604 letters (rank 1/201, z 5.11), L25-L30 + L28b 308 letters (rank 1/201, z 5.24); no.44: 8 of 27 cipher groups decode under the letter key (grade H) and 4 of its 14 word-code slots now carry a period-gloss value from no.37 at M (.7 x4, .71, .27, .25 = 7 of 14 occurrences); no.37 f.60r: 16 of 31 lines transcribed (pass C, 5 M / 11 L), 5 word-codes glossed at C/M from the leaf's own period glosses (witness/f60r_glosses_reconciled.tsv); the lower dense block read 2 Oct 2026 (GAPS-5)
- the no.37 dense cipher blocks - READ 2 Oct 2026: L06-L14 (GAPS-4) 604 letters, rank 1 of 201 z 5.11; L25-L30 + the unlisted row L28b (GAPS-5) 443 tokens, 308 letters (305 H + 3 I), rank 1 of 201 z 5.24, pass agreement 82.3 pct, decode --check exit 0; judge non-test (its design-matched control FAILs too); the 177 dotted/barred word-codes of the two blocks stay U - blocker: open-codes; what would read them is the same codes glossed on a sibling leaf (gap 4 below)
- the 8-glyph rule on no.37 (43 L06-L14 tokens at I, 23 at S since GAPS-7) - blocker: open-codes; GAPS-5: the value-blind tile sheet did not beat its control (21/30, p 0.060); 2 Oct 2026 (GAPS-6): two blind Opus passes in line context (not told the rule) read 0 at 64/66 P sites and 0/97 F sites, both, so 0 moved I -> H; with no 8 written the shuffled-label control cannot vary (non-test). Blind visual re-reading of L06-L14 is [retired] for this question (rule 3 third-attempt clause: GAPS-4 passes, GAPS-5 sheet, GAPS-6 line passes); the lower block's blind 8s (35/39 at rule sites, GAPS-5) still corroborate the rule for this hand; 2 Oct 2026 (GAPS-7): the key-side word-cover test ran (scripts/eight_cover_test.py): 8x wins 23/66 sites vs 9x 6, 6x 1, 0x/3x 0, 36 ties; control 20 seeds mean 0.105 max 0.167 vs target 0.348 (rank 1 of 21); known answer: true 8 wins 17/46 (0.370), 8x on settled non-8 sites 0.061; 23 sites I -> S, 43 stay I (36 ties, 7 won by 9x/6x); what remains for the 43 is new material (the same letter run elsewhere, or a sibling leaf in the same hand), not a further pass at these glyphs
- the four L-grade glosses (labr/de over the L01 run 66 65 40 25 50 90; legat over 50 23 30 on L20; pen? L22; dn L20) - blocker: open-codes; re-read 2 Oct 2026 (GAPS-3) from tall native crops, 1 call: all four now M (de and legat clear as text but each straddles two groups; L20 du/dn sits over the dotted 16; L22 is an insertion 'peu de', not a gloss), no decode-key value changed; what would settle the group cover is the same code glossed again on a sibling leaf (no.21/35/39, gap 3 below)
- no.44's remaining word-codes .13 .03 .07 .49 .57 .6 (7 of 14 occurrences) - blocker: open-codes; not glossed on no.37; next: the other glossed pool leaves (no.21 f.44, no.35 f.58, no.39 f.62, all "en partie déchiffrée" per the dépouillement) read the same way as this step, one leaf a job, ~$10 each
- the clear-French frame of f67r_ciphertext.tsv (198 C-only L words after the fold) - blocker: not-attempted; 2 Oct 2026 (GAPS-6): pass C folded in as the frame with three-pass support (scripts/f67r_frame_fold.py: 609 words, A or B agree 341 = 56.0 pct; H 325 / M 86 / L 198; L31 kept as A/B); cipher tokens unchanged; judge FAIL -1.012 (was -1.145) vs real_p05 -0.867, a non-test on this design; what remains is transcription of the clear frame, not decipherment; next: one strong second pass on the crops of the L words only, ~$3
- Boltanski 2006 (Les ducs de Nevers et l'État royal, Google Books dsInahmnar8C, PARTIAL) cites the 12 Dec 1589 letter - blocker: not-attempted; the cloud cannot open the page (books.google.com page view bot-blocked) and no LOCAL-QUEUE row is filed yet; next: file the LOCAL-QUEUE edition-read row for the page citing 12 décembre 1589 and read whether she quotes the text, ~$1

## Escalation (2 Oct 2026, updated GAPS-fr4715-vieuville-pool-2 2 Oct 2026)
- [x] siblings: no.58's Tomokiyo dump as the known-answer control (z 5.37, LIKELY-1); no.37 f.60r imaged native and its period glosses read (this step): 5 word-codes at C/M, 4 carried to no.44 at M; no.21/35/39 (also "en partie déchiffrée") not yet imaged
- [x] clear-pages: no.44 is 95 pct clear French (two Sonnet passes + one Fable pass); no.37's 16 clear lines transcribed by one Opus pass at 5 M / 11 L after two Sonnet passes failed at 2x
- [x] known-keys: key_vieuville_nevers.tsv applied through tools/decode_key.py on both leaves (--check exit 0); key_wordcodes_f60r.tsv built from the period glosses
- [x] print: (GAPS-8, 2 Oct 2026) tools/print_check.py on 9 interior phrases per letter + 1 positive control (phrases.txt, print-check.tsv): control found by 4 of 5 instruments (Ligue v.4 cached, IA 15 items, Google Books 10, Gallica 3; OpenAlex a non-test); no.44 0 specific hits, no.37 0 specific hits; 49 requests; Boltanski 2006 still unread (gap above)
- [n/a] key-rebuild: the letter key is proven on no.58; the word-code layer is being read from period glosses, not rebuilt
- [x] image-check: (GAPS-3, 2 Oct 2026: the four L gloss sites re-read from tall native crops, all M) no.37 native region fetched once, 32 row centres by tools/iiif_lines.py, bands cut twice (2x, then 3x), overlay eye-checked, 60v fetched (blank); the gloss sites re-read from 3x crops by the worker
- [x] retry: the Sonnet passes on no.37 failed twice at 2x (A, B) and the re-cut at 3x with a stronger reader (pass C) is the retry that read; a further Sonnet pass of the same shape is not the next instrument (rule 3's third-attempt clause)
Verdict: keep going: 6 internal gaps; cheapest next: file the LOCAL-QUEUE edition-read row for Boltanski 2006 (dsInahmnar8C, the page citing 12 décembre 1589), ~$1; then the strong second pass on f67r's 198 C-only L frame words, ~$3 (print check done 2 Oct 2026, GAPS-8: 0 specific hits per letter, control hit)
