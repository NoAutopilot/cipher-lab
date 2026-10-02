partial
GAPS4 2 Oct 2026: body L01-L14 segmented as Spanish (body/reading_body.txt; SENSE C 115 / M 120 / I 18): a cover-address instruction ending "...pondra solamente en sobre escrito en esta forma: a doña antonya de albanylla"; judge on es17c7 (nearest era, 1634-1648) KEY -1.482 / GLOSS -1.346 / SENSE -1.204 vs real_p05 -0.903/-0.922 FAIL, 20 shuffled nulls max -1.985 and 20 shuffled targets max -1.838 all 0 PASS; the leaf's own gloss FAILs too, so the judge cannot decide at this N (not a negative); key, reading and --check (exit 0) unchanged.
GAPS2 2 Oct 2026: the leaf's own gloss re-aligned to its groups with tools/interlinear_align.py (align/): agreement 0.699 vs a within-line shuffled-gloss control max 0.301 (n=300), 44 codes at the C bar vs control max 11; key.tsv rebuilt, leaf now C 136 / M 127 / U 16 (was 99/142/38), L18-L19 C 21 / M 7; three of the five crib codes (24, 51, 65) rise to C, 34 and 11 stay M; decode_key.py --check exit 0; judge on the 28-letter closing string FAIL unchanged (-1.05 vs real_p05 -1.014), 0 of 20 shuffled targets PASS.
GAPS 2 Oct 2026: both closing lines now read -- L18 is glossed on the leaf after all ("forma." in the gloss hand over its 5 groups, image
check) and L19 aligns to the clear address "A Doña Antonija de Albanylla" (15/16 vs controls max 0.286 and 0.438, crib_align.py); 28/28 tokens
valued, C 15 M 13, judge FAIL on a 28-letter name string (pasted below). VX-RD01, 25 Sept 2026: L01-L14 period gloss transcribed (H-grade key source).
Nationaal Archief 1.02.04 finding aid (26-page PDF, `www.nationaalarchief.nl/onderzoeken/archief/1.02.04/download/pdf`) read in full by this worker (grepped for cijfer/cijferschrift/geheimschrift/chiffre/sleutel across all ~152 inventory numbers); Internet Archive full-text search `"Schonenberg brieven"` (0 hits, no printed edition of this envoy's correspondence exists on IA); Huygens retroboeken *Briefwisseling van Anthonie Heinsius 1702-1720* full-text search (`resources.huygens.knaw.nl/retroboeken/heinsius/search_in_text`) for `Schonenberg` (413 hits, all his official correspondence with Heinsius, none mention Albanilla/Albanylla) and `Albanilla`/`Albanylla` (0 hits each) read by this worker.

QUEUE row: VX-E01. Worker: LANE VX VX-CS01 (Sonnet, session_01HitmZCRTQ5GgjaHVG5yRcB), 25 Sept 2026. Job: `.claude/briefs/runs/2026-09-25-lane-vx-cs01.md`.

## What this is

Nationaal Archief, toegang **1.02.04** ("Archief van F. van Schonenberg [1653-1717]: Gezant in Spanje en Portugal, 1678-1716"), **invnr 63**. Full leaf image (single recto, 1946x2618 px):
`https://service.archief.nl/api/file/v1/default/fc3a8d42-b89e-4715-9753-0320355365c7` -> `images/NL-HaNA_1.02.04_63_0001.jpg`. Crops of five regions at 1.6-2x upscale are also on disk (`images/crop_*.jpg`, see `images/manifest.json` for the pixel regions each covers).

**Direction (H-grade, from the finding aid itself, not from reading the letter):** invnr 63 sits in section "A", subsection **"Minuten van uitgaande brieven aan overige correspondenten, 1702-1716 en z.d."** (minutes/drafts of outgoing letters to other correspondents), item 63 of a numbered run 58-64 each "Aan [named correspondent]". The finding aid's own entry for invnr 63 reads verbatim:

> 63  Aan dona Antonya de Albanylla, z.d., 1 stuk
>     In cijferschrift

So this is a **retained draft/copy of an outgoing letter FROM Schonenberg's own chancery TO Doña Antonia de Albanylla**, undated ("z.d." = zonder dato), explicitly flagged by the archive's own cataloguer as "in cijferschrift" (in cipher) -- the only item in the whole 152-item toegang so flagged (see Sibling inventory below). The item page's embedded `drupal-settings-json` (`viewer.response`) independently confirms `"unittitle":"Aan dona Antonya de Albanylla, z.d."`, `"availability":"DIGITALIZED"`, 1 scan -- matching the image already on disk.

The letter itself carries no visible signature, only an unsigned paraph/flourish above the address line; the salutation that opens the enciphered text reads "Amigo." (a male form of "friend") even though the addressee named at the foot is "A Doña Antonija de Albanylla &a" -- worth a second look when this is transcribed (job 3), not resolved here.

## Structure (eye-check only, full size and 1.6-2x crops; NOT a decode -- job 3 does that)

Two interleaved layers on every line of the body:
1. A larger cursive line that mixes **plain Spanish words already in clear** (connectors and closers: "que", "y", "de", "las", "es", "a", "partes", "Amigo") **with runs of 2-digit cipher numbers** (occasional 3-digit-looking tokens are two glyphs, not three -- not counted separately here).
2. A **much smaller interlinear gloss written directly above the numbers**, apparently spelling the decoded Spanish out close to letter-by-letter (e.g. the opening line glosses "n o a b y e[n]" over "89.46.56.13...", plausibly "no abyendo" = "no habiendo"). This reading is **M-grade at best (uncertain, by eye, not a built key)** and is offered only as an observation for job 3, not as an established transcription.

**Eye-count of cipher groups (approximate, not authoritative -- a real count belongs to whoever transcribes it in job 3):** roughly **266 numeric groups across 17 cipher lines**, of which roughly **246 (about 15 of 17 lines) carry an interlinear gloss** and the **last ~20 groups (the final 2 lines, immediately before "forma." and the address) carry NO gloss at all** -- eye-checked twice, the space above those two lines is blank. **So the interlinear decipherment is PARTIAL, not complete**: essentially all of the letter's body is glossed, but its closing lines are not.

**Number range and apparent system:** two-digit numbers, roughly 1-99 (many repeats: 6, 60, 89, 56, 16 etc. recur often, consistent with common-letter homophones rather than a large word-nomenclator). At least 8 distinct non-numeral symbols also appear standalone or as digit modifiers: a right-parenthesis-like tick before/after some digits (e.g. ")6", "6)"), a tilde/wave (∾), and single glyphs that render as △, □, ○, X, Z, E, L, T. This is consistent with a **homophonic nomenclator of roughly 90-110 codes for the Spanish alphabet plus a handful of symbol codes** (word-signs or nulls), not a large numbered code book -- but that is a call for whoever builds the key, not this worker.

**Date clue (M-grade, tentative):** the interlinear gloss over the first cipher line may read "...23. de Nobe[mbre]" ("23 [de] Noviembre") -- if real this would be a specific day-and-month within van Schonenberg's own dated range for this section (1702-1716), but the finding aid itself already calls the item "z.d." (undated) and this worker did not build a key to confirm it. Flag for job 3, do not cite as established.

## Sibling inventory, toegang 1.02.04 (the point of this row)

Read the finding aid's full text (26 pages, ~152 inventory numbers, `/tmp` extraction via `pdftotext -layout`, grepped for `cijfer`, `cijferschrift`, `geheimschrift`, `chiffre`, `sleutel`):

- **`cijfer` (any form) appears exactly once in the entire toegang: invnr 63 itself** ("In cijferschrift", line 592 of the extracted text).
- `sleutel` (key) appears once, but not as a cipher key: it is the physical keys to the three chests Consul Heystermans used to ship Van Schonenberg's papers to The Hague after his 1717 death (archival-history section, not a catalogue entry).
- No hits at all for `geheimschrift` or `chiffre`.

| invnr | description | digitised | cipher state | same system? | tested URL |
|---|---|---|---|---|---|
| 63 | Aan doña Antonya de Albanylla, z.d. ("In cijferschrift") | Yes (confirmed, `availability: DIGITALIZED`) | Partly glossed (see Structure above) | n/a -- this is the target itself | `https://www.nationaalarchief.nl/onderzoeken/archief/1.02.04/invnr/63` ; image `https://service.archief.nl/api/file/v1/default/fc3a8d42-b89e-4715-9753-0320355365c7` |

No other invnr in 1.02.04 carries a cipher indicator in its description. This is a description-text search across the whole finding aid, not a scan-by-scan eye-check of every digitised item in the toegang (out of this job's scope/budget) -- so a cipher passage that the 19th/20th-century cataloguer did not think worth flagging in the summary description could still exist unflagged in some other item's scan; that residual gap is not closed here.

**Verdict: key source for siblings: no -- 0 undeciphered digitised siblings under the same system found in this toegang.** Invnr 63 is a singleton within its own archive.

## Check-solved, six sources (25 Sept 2026)

1. **Web search engine:** `Schonenberg "Albanylla" cipher letter`, `"Antonia de Albanilla" OR "Antonia de Albanylla"`, `Francisco van Schonenberg gezant Spanje cijferschrift`, `"Francisco van Schonenberg" gezant Madrid privécorrespondentie OR minnares OR vertrouwelinge`, `Schonenberg Lissabon Madrid gezant brieven cijferschrift cijfer` -- no hit connects the two names or any cipher content; only generic Zodiac-cipher noise, Wikipedia name-collisions, and Van Schonenberg's general diplomatic biography (a Sephardic-Jewish family, born Belmonte, envoy Madrid 1687-1702 then Lisbon 1702-1717).
2. **Sender's printed Lettres/Correspondance on Internet Archive:** `archive.org/advancedsearch.php` full-text query `Schonenberg brieven` returns **0 results** -- no printed edition of Van Schonenberg's Iberian or private correspondence exists on IA.
3. **Calendars and state-paper series:** the nearest equivalent for a Dutch envoy is the printed *Briefwisseling van Anthonie Heinsius 1702-1720* (Huygens retroboeken, 19 vols, the edition of his OFFICIAL correspondence with the Grand Pensionary) -- full-text searched for `Schonenberg` (413 hits, all his ordinary diplomatic reporting to Heinsius, nothing involving Albanilla/Albanylla or cipher) and `Albanilla`/`Albanylla` (0 hits each). `sources/huygens/NOTES.md` and `sources/wvo/NOTES.md` (the existing repo harvests of this and the Willem van Oranje database) were read; neither lists this item or correspondent (WVO covers a different century/correspondent entirely, van Oranje 1568-1584, not relevant here beyond confirming no collision).
4. **Comment threads of the list posts (Cryptiana blog, Cipherbrain):** web search `cryptiana Schonenberg cipher Nationaal Archief` returns nothing specific to this item; Cryptiana's own catalogue was not separately re-crawled this pass (out of scope for a single-item check), but nothing found anywhere else suggests it is listed there.
5. **DECODE (de-crypt.org):** checked against the repo's own catalogue dump `sources/decode/records-non-decrypted-2026-09-24.tsv` and `records-decrypted-2026-09-24.tsv` (2548 rows total, crawled 24 Sept 2026, one day before this check) -- no row for toegang 1.02.04, "Schonenberg" or "Albanilla"/"Albanylla" anywhere in either file.
6. **The two solver repositories:** shallow-cloned both (`dbourdeau/cyphersolver`, `aaymeloglu/unsolved-ciphers`) fresh this session and grepped case-insensitively for `schonenberg`, `albanilla`, `albanylla`. One hit, in `cyphersolver/roell1809/NOTES.md`, is an unrelated aside distinguishing toegang 1.02.04 (Schonenberg's Portugal legation) from 1.02.20 (the Turkey legation) for a different target (roell-vandedem-1809) -- not this item, not a duplicate.

No collision found anywhere with this item. Distinct from `HU3` (Schonenberg-to-Heinsius letter no. 185, NA 3.01.19 invnr 1445, "Het cijferschrift is niet opgelost", already logged in QUEUE.md) -- different archive, different correspondent, not the same letter.

## Status

**open.** No key, decipherment or printed edition of this letter found anywhere searched. The item's own interlinear gloss (partial, ~92% of groups by eye-count) is a **contemporary decipherment already on the leaf**, per CLAUDE.md rule 2/README's result-kind guidance -- so any future reading of this letter is a **transcription of an existing decipherment plus whatever the closing ~20 ungossed groups yield**, not a fresh cryptanalytic break; the "found-solved" framing (README F0/F1/F2) likely applies once job 3 transcribes the gloss, not "open" cryptanalysis. Left as `open` here because the check-solved question ("is a solution already published/known elsewhere") is negative; whether the on-leaf gloss itself counts as "solved" is a job-3/verifier call, not this worker's.

## Hosts and requests

- `www.nationaalarchief.nl`: 2 (finding-aid PDF, item-63 page for `drupal-settings-json`).
- `service.archief.nl`: 1 (full leaf image).
- `resources.huygens.knaw.nl`: 5 (2 on the wrong accessor path before finding `search_in_text` in the repo's own notes, then 3 correct: Schonenberg, Albanilla, Albanylla), all >=2s apart.
- `archive.org`: 1 (`advancedsearch.php`).
- `github.com`: 2 fresh shallow clones (grep only, no browsing).
- `dspace.library.uu.nl`: 1 attempt, HTTP 403 (a 1990s-look UU thesis on Van Schonenberg's diplomacy, "Diplomatie eind zeventiende eeuw... De casus Francisco van Schonenberg, gezant in Madrid" -- blocked, not retried per the one-retry rule; worth a person's browser if this target is promoted, since it might describe his private correspondence).
- WebSearch tool: 8 queries (not a single host).

All well under the job's caps (nationaalarchief.nl/service.archief.nl combined <=60, huygens <=40).

## Reading (VX-RD01, 25 Sept 2026)

**Kind: recovery, key source `period`** (the leaf's own contemporary interlinear Spanish gloss over lines
L01-L14; the two unglossed closing lines, L18-L19, are this worker's own application of a key built from that
gloss, not a transcription of an existing decipherment).

**Transcription.** Two blind Sonnet subagent passes (passA.tsv, passB.tsv) transcribed the whole leaf from the
crop images independently, recording every cipher group and the Spanish letter glossed directly above it.
Reconciling them found that passA's line numbering drifted from L04 on: content-matching shows it skipped or
reordered one physical line (P4/P5), then read every later line's gloss one position off starting around
position 7 of that line -- diagnosed by comparing both passes against this worker's own pixel-verified recount of
L06, the one line on the leaf where the gloss letter count (20) exactly equals the cipher group count (20) with
no word-signs, so the correspondence is unambiguous. That recount agrees with passB position-for-position, 20/20;
it disagrees with passA from position 7 on, in a pattern consistent with a single off-by-one slip that then
persists (passA's own group *set* for that line is right, only its gloss alignment drifts). `ciphertext.tsv`
therefore reconciles as: passB's transcription taken as primary; this worker's L06 recount substituted where the
two conflict; a direct 4x re-crop of the two unglossed target lines themselves (`images/crop_u1.jpg`,
`crop_u2_top.jpg`, `crop_u2_bottom.jpg`) settling their own signs, with one correction to passB there -- a solid
ink blot immediately followed by a legible "9" in L19 is one 2-digit group with its tens digit obscured, not two
separate signs.

**Key.** `key.tsv`: 87 distinct codes found in the L01-L14 gloss (period key source). Grade C assigned only where
a code's gloss agrees >=75% of the time across >=2 occurrences in passB's own tally, or where this worker's L06
recount fixes it unambiguously (29 codes). Grade M where a code has a real plurality short of that margin (39
codes). Left unkeyed `[?]`, grade U, where the gloss ties between two or more letters with no majority, or the
code never appears in the glossed lines at all (19 codes). `conflicts.tsv` lists 49 codes glossed more than one
way anywhere in passB; spot-checking one against the image (code `50`, this worker's L06 recount reads it `r`,
its only pixel-verified occurrence, against a `4/8` majority for `s` everywhere else it recurs in passB) shows
the leaf's dense middle lines (L04-L05, L07-L14) carry real transcription/alignment noise on top of genuine
homophony -- both subagent passes flagged most of that stretch M-confidence themselves, and this worker did not
adjudicate every one of the 49 conflicts against the image; L06 is the only line checked pixel-by-pixel start to
finish.

**L18 and L19** (the two lines after the plain word "forma." and before the address, no gloss on the leaf at
all): applying key.tsv to the reconciled ciphertext (`tools/decode_key.py ciphers/na-schonenberg-1678-1716
--check`, 0 diff) gives, token by token (`reading_tokens.tsv`):

- L18 (5 groups): `[?] o(C) r(C) m(M) a(M)` -> **"?orma"**
- L19 (23 groups): `a(C) d(M) [?] [?] [?] a(M) n(C) [?] o(C) [?] y(C) a(C) d(C) e(C) a(M) [?] b(C) a(M) n(C) y(C) p(M) [?] [?]` -> **"ad???an?o?yadea?banyp??"**

Counts across L18+L19 (28 tokens): C 12, M 7, U 9, H 0, S 0, I 0.

`specs/na-schonenberg-1678-1716.json` + `python3 tools/judge_plaintext.py specs/na-schonenberg-1678-1716.json
--text "ormaadanoyadeabanyp"` (the 19 non-`[?]` letters of L18+L19 run together): **PASS** (`min_word_cover: 0.4`
and, checked separately, a language-model pass too). A PASS here is not a claimed reading (rule 10): with 9 of 28
tokens unkeyed and dropped and most of the rest grade M, this is what an incomplete key produces on a short
window, not evidence the candidate is real Spanish -- reported as a FAIL would have been, per rule 7. The one
observation worth a second reader's eye, not claimed as a reading: L18's four resolved letters spell "-ORMA", one
letter short of repeating the plain word "forma." that sits immediately to its left on the page; a coincidence at
this length is not ruled out.

**Fresh-instance re-derivation (rule 7).** A separate Sonnet subagent, given only `ciphertext.tsv`'s group+gloss
columns and the crop images -- not `key.tsv`, not this reasoning, not this worker's grades -- independently
rebuilt its own key from L01-L14 (`rederivation_key.tsv`) and decoded L18/L19 (`rederivation_reading_L18L19.txt`,
`rederivation_report.md`). Its tally found 38 unanimous codes, 27 clear-majority codes and 22 genuine ties among
the same 87 codes (a different threshold from this worker's C/M/U split, so the *counts* per bucket are not
directly comparable), but its **decoded values agree with this worker's reading at every one of the 28 L18+L19
positions**, including which five positions are unresolvable (`61` in L18; `[n]`, `24`, `34`, `51`, one of the two
`65`s, and `11` in L19 -- the independent pass calls these six genuine ties/absences against this worker's five
U-grade + one M-grade weak call at the same spots, close enough to count as the same finding): "?orma" and
"ad???An?o?yadea?banyP??" (case of A/P aside). Zero disagreement beyond the M-graded tokens -- this reading
clears rule 7's fresh-instance bar.

**Letter's gist** (M-grade paraphrase from the leaf's own gloss, L01-L14, not a full translation -- do not rely on
this for anything beyond a rough sense of subject matter): an unsigned, undated chancery letter opening "Amigo."
and closing "...en esta forma", discussing "aver mudado este go[bi]erno" (this government having changed),
"circunstancias", and a reply with more "seguridad" (security/certainty) -- consistent with NOTES.md's existing
read (see "What this is" above) of a guarded political or personal dispatch from Schonenberg's own chancery to
Doña Antonia de Albanylla.

**What was not found.** No code beyond the 29 grade-C ones is established with real confidence; the two unglossed
lines' reading is a partial, mostly M/U-grade application of an incomplete key, not a recovered plaintext. This
worker did not classify novelty (rule 10) -- that is the verifier's job on AUDIT.md, including whether the
existing period gloss over L01-L14 (already on the leaf before this worker touched it) itself counts as
"solved" for board purposes.

**Suggested next step** (not run here, brief did not name it): a third, targeted transcription pass over just the
dense L04-L05/L07-L14 stretch, cross-checked position-by-position against the image the way L06 was, would likely
raise several of the 39 M-grade and some of the 19 unkeyed codes to grade C -- the leaf itself is legible enough
(L06, L18, L19 all read cleanly at 4x zoom); the bottleneck was gloss-to-group positional alignment in crowded
handwriting, not image quality.

Files: `passA.tsv`, `passA_summary.txt`, `passB.tsv`, `passB_summary.txt`, `ciphertext.tsv`, `key.tsv`,
`conflicts.tsv`, `decode.json`, `reading.txt`, `reading_tokens.tsv`, `rederivation_key.tsv`,
`rederivation_reading_L18L19.txt`, `rederivation_report.md`, `images/crop_u1.jpg`, `images/crop_u2_top.jpg`,
`images/crop_u2_bottom.jpg`, `images/manifest.json` (updated), `specs/na-schonenberg-1678-1716.json`.

Hosts this job: none (all work from the image already on disk; no new fetches from service.archief.nl or any
other host).

## GAPS-na-schonenberg-1678-1716 (2 Oct 2026, account-4)
Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; the Verdict step of the 1 Oct 2026 Remaining-gaps section, run 01:58-02:2x UTC.
Intake gate: exit 1 on the missing web/blog check, the check run first (section at the end of this file), gate re-run exit 0.

**1. Layout (vision call 1 of 2, `images/crop_layout_L14_to_address.jpg`, native resolution y 1660-2200).** The word "forma."
is NOT a clear word of the main text: it stands in the small interlinear gloss hand, letter-for-letter over L18's five
groups (f over 61, o over 68, r over 2), m over 88, a over )8), with a long flourish filling the line to its left, exactly
as the gloss sits over L01-L14. L14's gloss tail reads "en, esta", so the period gloss runs "...en esta forma". L18 was
therefore glossed on the leaf all along (ciphertext.tsv L18 gloss column now filled, conf H, one reader at native
resolution); the leaf's only unglossed cipher is L19. Above L19 the space is blank. The address "A Doña Antonija de
Albanylla &a" at the foot is in the large main hand, spanning the width, not positioned over the groups: an address, not
a displaced gloss, so for L19 it is a crib (grade C with controls), not H by layout. L19's "&a" in clear and the
address's "&a" match. Vision call 2 (`images/crop_L19_blot_and_row2_2x.jpg`, 2x): L19 pos9's blot covers a round
tens digit consistent with 8 (so 89 = n); pos20 is 8) with the tick after, as transcribed.

**2. Alignment with controls (`crib_align.py --shuffles 2000 --seed 1`, output `crib_alignment.tsv`).** Statistic:
agreements between crib letter and key.tsv value over the resolved (C/M) positions.

| line | crib | target agree/resolved | U positions whose body tie set contains the crib letter | slid-window control (L01-L14, same crib, key.tsv values) | shuffled-crib control (same position) |
|---|---|---|---|---|---|
| L18 | forma | 4/4 = 1.000 | 0/0 (61 never glossed) | n=247, mean 0.078, p95 0.333, max 0.500, 0 windows >= target | all 120 permutations: mean 0.200, max 1.000, only the identity reaches 4/4 |
| L19 | adoñaantonyadealbanylla (23 = 23 groups) | 15/16 = 0.938 (8) = p vs l the one miss) | 4/6 (24, 34, 51, 11 yes; 65 twice no) | n=229, mean 0.104, p95 0.235, max 0.286, 0 windows >= target | n=2000, mean 0.162, p95 0.312, max 0.438, 0 permutations >= target |

Both controls can move the statistic (it changes with the window and with the letter order), so each is a test, not a
non-test (rule 3). The L18 shuffled control is weak by construction (5 letters, 4 resolved: 1 in 120 by chance); the
L18 result rests on the layout, not on the permutation count.

**3. Key and reading (rule 4 grades, rule 7 check).** key.tsv: 61 = f C (period, from L18's own gloss); 88 M -> C (2/2);
)8 stays M (3/6); [n] = ñ C (crib; the sign is an n with a mark above, no body occurrence); 24 = o, 34 = a, 51 = t,
11 = a, 65 = l all **M** -- each agrees with the crib and (24/34/51/11) with one body gloss but disagrees with one or
two other body glosses, so rule 4's conflict clause applies until the aligner (gap 2) says whether those glosses are
alignment slips; witnesses in conflicts.tsv and HYPOTHESES.md H1. exceptions.tsv: L19 pos9 ?9 = n (M, blotted sign),
L19 pos20 8) = l (M, against body L03 pos0 "P" conf M -- a real conflict, unresolved; key.tsv keeps 8) = p). decode.json
now names exceptions.tsv. `python3 tools/decode_key.py ciphers/na-schonenberg-1678-1716 --check`: "reading up to
date", exit 0. Reading: L18 `f o r m a`, L19 `a d o ñ a a n t o n y a d e a l b a n y l l a`. Tokens L18+L19 (28):
H 0, C 15, S 0, M 13, I 0, U 0 (was C 12 M 7 U 9). Whole leaf (279): C 99, M 142, U 38 (was C 95, M 123, U 61) -- the
body change is the five crib-fixed codes now reading at M where they were [?].

**4. Judge (rule 7, pasted as it came).** `python3 tools/judge_plaintext.py specs/na-schonenberg-1678-1716.json --text
"formaadoñaantonyadealbanylla"`:
```
FAIL language: score=-1.05, null_p99=-1.395, real_p05=-1.014, real_median=-0.825, mode=both, N=28
ok   words: cover=0.857, min=0.4, real_text_median_cover=0.929
FAIL - na-schonenberg-1678-1716 (a PASS is a gate for a verifier, not a reading; rule 10)
```
A FAIL, reported as one: a 28-letter string that is one common noun and a personal name is not Spanish prose, and
the judge's language gate is calibrated on prose; the evidence for the reading is the layout and the two controls
above, not the judge. The judge is also not independent here (the crib is the candidate), so a PASS would have
meant little either way.

**What was found / not found.** L18-L19 read in full against the leaf's own clear text (period gloss for L18, the
address as a crib for L19); no printed or web source for the letter located (check-solved 25 Sept, web/blog check
2 Oct). Not classified for novelty (rule 10, verifier's job). Lead for the key-hunt, not run: NA 3.01.19 (Heinsius)
carries "Stukken betreffende cijfers en sleutels van cijferschrift" and "Brieven van F van Schonenberg uit Madrid",
neither digitised (web search 2, 2 Oct 2026); official cipher, probably not this private key. Cost: see the lane
ledger. Vision calls 2 of 2. Hosts: WebSearch 10, dspace.library.uu.nl 1 (403), studenttheses.uu.nl 1 (403),
nationaalarchief.nl 1; no image refetched.

## GAPS2-na-schonenberg-1678-1716 (2 Oct 2026, account-4)
Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; the Verdict step of the Remaining-gaps section as rewritten at 02:07 UTC, run
02:44-03:1x UTC. Intake gate exit 0 at the start (the web/blog check was logged by GAPS at 02:07). Disk only, 0 vision calls, 0 requests.

**0. A transcription fix first (never silent, rule "ciphertext as transcribed").** ciphertext.tsv L01 pos6 (`23`) and pos7 (`[blot]`) carried the
letter "M" in the gloss column and nothing in conf: a column slip copied from passB.tsv, whose own note on both rows says "no gloss letter
visible". Both rows now read gloss empty, conf M. The old key's tally for 23 counted that "M" as a gloss m (`tied {'m': 2, ...}`); the real
positional tally is {r: 2, m: 1, s: 1, n: 1}, still a tie.

**1. Alignment (`align/gloss_align.py --shuffles 300 --seed 1`, output `align/summary.txt`).** For each glossed line (L01-L14 and L18) the plain
line is passB's gloss letters in order (L01 pos5 "en" = two letters) and the cipher line its groups as `@`-prefixed codes (`align/pairs.tsv`);
`tools/interlinear_align.py` in `--code-prefix` mode then re-decides which letter sits over which group (a group may take none, a letter may be
skipped), six hard-EM iterations. Three runs on the same pairs: R0 unseeded; R1 `--prior` seeded with key.tsv's grade-C codes only; R2 seeded with
the C codes plus the five crib-fixed codes 24, 34, 51, 11, 65 (the Verdict line's run). The tool's own caveat (a seeded code's counts are not
independent evidence) is why R0 and R1 are kept beside R2: R1 decides the crib codes (not seeded there), R0 shows what the gloss says with no key.
Statistic: fraction of code tokens whose aligned letter equals that code's leaf-wide top letter at >=2 occurrences (the tool's status "agrees"),
and the number of codes at the folder's C bar (>=2 occurrences, >=75%). Control (rule 3): the same run on each line's gloss letters shuffled within
the line, which changes both statistics, so it can fail.

| run | prior | code tokens | agrees | C-bar codes | tokens moved vs passB's positional letter |
|---|---|---|---|---|---|
| R0 | none | 256 | 0.570 | 30 | -- |
| R1 | C codes (32) | 256 | 0.680 | 40 | -- |
| R2 | C + crib codes (37) | 256 | **0.699** | **44** | 88 of 256 |
| control R2, within-line shuffled gloss, n=300 | as R2 | 256 | mean 0.232, p95 0.277, max 0.301, **0 at or above 0.699** | mean 5.4, p95 9, max 11, **0 at or above 44** | -- |
| control R0, same shuffles | none | 256 | mean 0.179, p95 0.223, max 0.254, 0 at or above 0.570 | mean 2.2, p95 5, max 7, 0 at or above 30 | -- |

The 88 moved tokens (`align/moves_R2.tsv`) sit in exactly the lines passB's own summary flagged plus L02: L02 18 (the whole line is one position
off in passB -- 89 read "e" and 16 "n" there against n 7/7 and e 4/4 everywhere else; re-synced, 81 takes no letter and the final "e" is left
over), L10 15, L12 15, L08 13, L13 11, L14 8, L09 6, L01 2; L03-L07 and L11 unchanged. Every C-graded anchor in a moved line now agrees with
its leaf-wide value; the moves are re-syncs, not re-readings (no letter was added or changed, only re-attached to a neighbouring group).

**2. Crib codes (gap 1's question: slips or homophony).** Under R1, where they are not seeded: 24 reads o at all three body occurrences
(L01:11, L12:3, L13:7 -- passB had i and l at the last two), 65 reads l at both (L08:8, L13:8 -- passB y and a), 51 reads t at L03:16 and L13:13
with L08:6 taking no letter (passB a, e), each with R0's top the same letter: **24 = o, 51 = t, 65 = l rise to C** (crib + body, conflicts
dissolved as alignment slips). 34 keeps d at L11:14 in every run (a 3/4) and 11 keeps s at L09:15 in R0/R1 (a 1/2, tie): **34 and 11 stay M**,
conflicts standing (rule 4; HYPOTHESES.md H2).

**3. Key rebuilt (`align/rebuild_key.py`, rule in its docstring; the key as it stood is `align/key_before_2026-10-02.tsv`).** key.tsv: 89 codes, C 40
/ M 43 / U 6 (was 32 / 38 / 19 by the same file). A seeded code keeps C only when R2 is at the bar and the unseeded R0 agrees without a tie; a
code VX-RD01 graded C from its pixel-verified L06 recount whose aligner tally disagrees is a two-witness conflict at M, never overruled:
**50 = s (M)** -- s at its six other glossed occurrences in every run (R0 5/7, R2 6/7 even when seeded r) against the pixel-verified r at L06
pos17, which keeps its own value through exceptions.tsv; 49 and 31 tie three and two ways, broken toward the L06 letter at M; 28, 36, 6) and 81
drop C -> M (R0 below the bar or tied, or one occurrence left); )0 reads q 2/2 where passB had u 2/3 (M). Rises: 60, 56, )8, 30, 45, 12, 59, 46 M
-> C; 25 = p, 29 = t, 95 = t, 98 = y from U -> C; 94 = s, 5 = e, 26 = q, 33 = z, 82 = e, )3 = t from U -> M; 10 single-occurrence codes in moved
lines change value at M ()10, )4, )5, 52, 58, 66, 69, 9, [circle], [square]); 55 and )52 fall to U (tie / took no letter). The whole list is
`align/rebuild_key.py`'s printout. `python3 tools/decode_key.py ciphers/na-schonenberg-1678-1716` then `--check`: "reading up to date", **exit 0**.
Tokens (rule 4), reading_tokens.tsv: whole leaf 279: H 0, C 136, S 0, M 127, I 0, U 16 (was C 99 / M 142 / U 38); L01-L14 (251): C 115, M 120,
U 16; L18-L19 (28): C 21, M 7, U 0 (was C 15 / M 13). L18-L19's letters are unchanged ("f o r m a" / "a d o ñ a a n t o n y a d e a l b a n y
l l a"); only grades moved.

**4. Judge, pasted as it came (`align/shuffled_target_judge.py --shuffles 20 --seed 1`).** Real: `FAIL language: score=-1.05, null_p99=-1.395,
real_p05=-1.014, real_median=-0.825, mode=both, N=28` / `ok words: cover=0.857` -- the same FAIL as at 02:07 on the same 28-letter string (a noun
and a personal name, not prose). Shuffled target (L18+L19 group order shuffled, decoded with the same key): **0 PASS of 20**, language scores
-1.70 to -2.37. The judge is not voided for this family at this N, but the reading does not clear it either, so no "reading ready" line.

**What was found / not found.** The gloss-to-group alignment was the limit, as the 1 Oct gap said: re-aligning passB's own letters, with no new
reading of the image, lifts the leaf from 99 to 136 C tokens and from 38 to 16 U tokens against a control that never comes within half the
target. Still unsettled, for the image pass: 6 U codes (23, 14, 55, 96, [blot], )52) and 5 conflict codes (50, 34, 49, 11, 31), spread over
every body line (no line is free of one), plus 8) = p vs l (L03:0 vs L19:20, unchanged). No printed or web source found (unchanged; rule 10,
novelty is the verifier's). Files: `align/` (gloss_align.py, rebuild_key.py, shuffled_target_judge.py, pairs.tsv, prior_C.tsv, prior_Ccrib.tsv,
align_R0/R1/R2.tsv, key_R0/R1/R2.tsv, moves_R2.tsv, control.tsv, summary.txt, key_before_2026-10-02.tsv), key.tsv, exceptions.tsv (L06 pos17
row), ciphertext.tsv (L01 pos6-7 fix), reading.txt, reading_tokens.tsv. Cost: the lane ledger. Vision calls 0. Hosts: none.

## GAPS4-na-schonenberg-1678-1716 (2 Oct 2026, account-4)
Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; the Verdict step of the Remaining-gaps section as rewritten by GAPS2 (gap 3),
run 05:18-05:4x UTC (a re-spawn of GAPS3, which stopped at a permission prompt at 04:20 with nothing pushed). Intake gate exit 0 at the
start. Disk only, 0 vision calls, 0 requests. Files: `body/` (reading_body.txt, sense_inferences.tsv, judge_body.py, judge_body.log,
judge_body_results.tsv, spec_body_es17c7.json, spec_body_es.json). key.tsv, reading.txt and reading_tokens.tsv are untouched
(`tools/decode_key.py ... --check`: "reading up to date", exit 0).

**0. Era check first (rule 3, pt18/es17c lessons).** The letter is 1702-1716 Spanish diplomatic/private prose. tools/data has no 18th-c.
Spanish corpus. Nearest in era and register: `es17c7` (1634-1648 *Cartas de algunos PP. de la Compañía de Jesús*, letters about court,
war and diplomacy; 55-80 years before the target; 4.9M letters), then its three-volume subset `es17c` (1643-1647), then the spec default
`es` = `es17` (Cervantes/Quevedo, 1605-1626 fiction: right language, wrong register and a century off). Per-fold false-negative spread
from the READMEs, leave-one-file-out at N=519: es17c7 2.0-23.0% (11.5x, blended 11.1%), es17c 10.0-39.5% (4x, blended 23.5%); `es17` has
no fold check on file. The target's own N is 235-245, below the N those rates were measured at. **A FAIL or PASS here is of unknown
reliability** (era gap plus wide fold spread); both es17c7 and es are run and reported side by side, neither is a gate.

**1. Per-line Spanish reading (`body/reading_body.txt`).** Three renderings per body line: KEY (reading.txt's key-regenerated letters, word
boundaries inserted), GLOSS (passB's positional gloss letters, the leaf's own period gloss) and SENSE (segmented and expanded: a letter in
[ ] is this worker's inference from sense, grade I; a letter in ( ) is the gloss letter preferred over the key value, grade M, both named).
Grades (rule 4): KEY tokens L01-L14 = 251: H 0, C 115, S 0, M 120, I 0, U 16 (unchanged); SENSE: C 115, M 120, I 18 (16 U positions filled
or read as no-letter, plus 81 = d and 58 = c on sense), 7 positions where the gloss letter is preferred over the key letter counted M;
every inference is one row of `body/sense_inferences.tsv` with its reason. What the body says, as read (M-grade paraphrase): "Amigo. No
abye[n]do nobe[d]ad en estas partes qu[e] [l]a de a[v]er muda(d)o e(s)te gouye(r)[n]o ... las que ybye(r)e del norte y de ytalya pues ...
las qu[e] puedan ocurryr. Para (m)a(s) se(g)u(r)(y)da(d) de la [c]orespondenzya ... p[o]ndra solamente [e][n] sobre (s)cryto en esta
forma: a doña antonya de albanylla" -- a cover-address instruction (write only this name on the outer wrapper), which is what L14 "en esta"
+ L18 "forma" + L19 the address already said in sequence. Unread spans, left as letters: L04-L05 "zynenstanzyas" ("ynstanzyas"?
"circunstanzyas"?), L05-L06 "que ay sera bran mexores pe no con anrya", L08-L09 "pues [23]saran de o[14]as yo[23]a[23]a". Sense-side
predictions for the image pass (gap 2), none applied to key.tsv: 8) = l at L03 pos0 (as at L19; "que la de aver"), 55 = v ("aver"), 31 = d
at L03 ("mudado", the gloss's own d), )2 = s at L03 pos15 and L14 pos6 ("este", "scryto") against r at L05/L08/L10 (a homophone, or two
signs), 49 = r at L04 ("gouyerno"), 23 = n at L01/L04/L13 and r at L07 (the gloss's own r, "ybyere" = ubiere), 14 = c at L04 ("con"),
81 = d at L02 pos0 ("nobedad"), 58 = c at L12 ("corespondenzya"), 96 = o / e at L13. Logged in HYPOTHESES.md H3.

**2. Judge, pasted as it came (`python3 body/judge_body.py --shuffles 20 --seed 1`, log `body/judge_body.log`).** Texts: KEY = the 235
key-regenerated letters of L01-L14 (U dropped); GLOSS = passB's 245 gloss letters (the leaf's own known-genuine period text, the
ZX-DEC349 calibration witness); SENSE = 245 letters with the I fills. Controls: 20 letter-shuffled nulls of KEY and 20 shuffled-target
decodes (group order shuffled within each line, decoded with key.tsv; the ARM-C1 check). Spec variants `body/spec_body_es17c7.json`,
`body/spec_body_es.json` (judge block only: language, letters_min 100, min_word_cover 0.4); the folder's own spec is unchanged (it
judges the closing lines).

| corpus | text | N | language score | real_p05 | null_p99 | word cover (real median) | verdict |
|---|---|---|---|---|---|---|---|
| es17c7 | KEY | 235 | -1.482 | -0.903 | -1.858 | 0.813 (0.953) | FAIL |
| es17c7 | GLOSS (leaf's own gloss) | 245 | -1.346 | -0.922 | -1.894 | 0.841 (0.955) | FAIL |
| es17c7 | SENSE | 245 | -1.204 | -0.922 | -1.894 | 0.865 (0.955) | FAIL |
| es17c7 | 20 shuffled nulls of KEY | 235 | -2.266 .. -1.985 (mean -2.086) | -0.903 | -1.858 | -- | 0 PASS of 20 |
| es17c7 | 20 shuffled targets (key.tsv) | 235 | -2.263 .. -1.838 (mean -2.100) | -0.903 | -1.858 | -- | 0 PASS of 20 |
| es (es17) | KEY | 235 | -1.413 | -0.919 | -1.828 | 0.757 (0.936) | FAIL |
| es (es17) | GLOSS | 245 | -1.311 | -0.894 | -1.832 | 0.812 (0.939) | FAIL |
| es (es17) | SENSE | 245 | -1.153 | -0.894 | -1.832 | 0.853 (0.939) | FAIL |
| es (es17) | 20 shuffled nulls of KEY | 235 | -2.175 .. -1.902 (mean -2.021) | -0.919 | -1.828 | -- | 0 PASS of 20 |
| es (es17) | 20 shuffled targets (key.tsv) | 235 | -2.170 .. -1.894 (mean -2.036) | -0.919 | -1.828 | -- | 0 PASS of 20 |

```
$ python3 tools/judge_plaintext.py ciphers/na-schonenberg-1678-1716/body/spec_body_es17c7.json --text <KEY>
ok   length: got=235, min=100, max=1000000000
FAIL language: score=-1.482, null_p99=-1.858, real_p05=-0.903, real_median=-0.791, mode=both, N=235
ok   words: cover=0.813, min=0.4, real_text_median_cover=0.953
$ ... --text <GLOSS>
FAIL language: score=-1.346, null_p99=-1.894, real_p05=-0.922, real_median=-0.797, mode=both, N=245
$ ... --text <SENSE>
FAIL language: score=-1.204, null_p99=-1.894, real_p05=-0.922, real_median=-0.797, mode=both, N=245
```

**Reading of the numbers (rule 3).** Every real text FAILs the real_p05 gate on both corpora, and every one of the 80 control texts sits
0.35-0.6 below the worst real text: KEY, GLOSS and SENSE all clear null_p99 by 0.4-0.7 and no shuffled null or shuffled target comes
within 0.35 of them (shuffled max -1.838 vs KEY -1.482 on es17c7). The leaf's own contemporary gloss -- genuine Spanish of this hand,
not a candidate -- scores -1.346, well below real_p05 (-0.922) and only 0.14 better than the key regeneration; that is the ZX-DEC349
shape: at this N and in this register (a terse secretarial letter with y-for-i, b-for-v, z-for-c spellings the corpora do not share, and a
gloss hand that passB read with ~15 letter slips), the judge's real-prose threshold is not reachable by the real text either. The FAIL is
"judge cannot decide", not a negative on the key; the ordering SENSE > GLOSS > KEY >> shuffles says the segmentation adds prose-likeness
in the direction expected and the key regeneration carries the gloss's order, nothing more. Shuffled-target 0 of 20 PASS: the judge is
not voided for this family at this N, and the reading does not clear it either, so no "reading ready" line. The L19 crib signal that
account-3's 03:27 note asks to have verified is untouched by this job (nothing here changes L18-L19); its verifier is still owed.

**Found / not found.** Found: the body reads as a connected Spanish cover-address instruction once segmented, with L14-L18-L19 forming one
sentence ("...pondra solamente en sobre escrito en esta forma: a doña antonya de albanylla"), which is internal corroboration of the
L19 crib reading from the body's own words (sense, grade M; not a control). Not found: a judge PASS on any rendering; a resolution of
the three unread spans without the image. Cost: the lane ledger. Vision calls 0. Hosts: none.

## Remaining gaps (finish-or-blocker pass, 1 Oct 2026; updated GAPS, GAPS2 and GAPS4 2 Oct 2026)
Read so far: 279 of 279 cipher groups (100%) carry a value: 251 body groups under the leaf's own period gloss (L01-L14, ciphertext.tsv, re-aligned to the groups 2 Oct 2026 by tools/interlinear_align.py, align/), L18's 5 under its own gloss "forma." (found 2 Oct 2026), L19's 23 under the address crib with controls (15/16 resolved agree); by grade the leaf is C 136 / M 127 / U 16 (reading_tokens.tsv, GAPS2 2 Oct 2026; was 99/142/38), L18-L19 alone C 21 / M 7 / U 0. Read-as-sense is still unmeasured for the body: the gloss has never been segmented into Spanish words ("Letter's gist" is M-grade).
Resolved 2 Oct 2026 (GAPS-na-schonenberg-1678-1716): the L18-L19 gap -- "forma." is L18's own interlinear gloss (layout, image check), L19 = "a doña antonya de albanylla" against the address (crib_align.py, slid-window and shuffled-crib controls both at 0 of 229 / 0 of 2000 at or above target), decode_key.py --check exit 0; 65 and 8) logged as conflicts (conflicts.tsv, HYPOTHESES.md H1).
Resolved 2 Oct 2026 (GAPS2-na-schonenberg-1678-1716): the L01-L14 code-to-gloss alignment -- tools/interlinear_align.py on passB's own gloss letters (align/), R2 agreement 0.699 and 44 C-bar codes vs a within-line shuffled-gloss control max 0.301 / 11 (n=300, 0 at or above target); key.tsv rebuilt (C 40 / M 43 / U 6), 24, 51, 65 raised to C, 34 and 11 held at M, 50 = s at M against the pixel-verified L06 r (exceptions.tsv); decode_key.py --check exit 0; 88 of 256 tokens re-attached, all in the lines passB flagged plus L02.
- Gloss and group transcription of the codes the aligner leaves unsettled: 6 U codes (23, 14, 55, 96, [blot], )52) and 5 conflict codes (50 s-vs-r, 34 a-vs-d, 49 n/r/u, 11 a-vs-s, 31 x-vs-d), plus 8) = p vs l (L03 pos0 / L19 pos20) and the tick-before/tick-after doubts passB names; one or more of these sits in every body line L01-L14 (reading_tokens.tsv) - blocker: not-attempted; the leaf reads cleanly at native resolution and 2x (L06, L18, L19), the limit was alignment, now reduced to these 12 codes; next: cut crops with `tools/iiif_lines.py --image images/NL-HaNA_1.02.04_63_0001.jpg --out images/lines`, one line crop per Sonnet subagent call for the 11 lines that carry a conflict or U code at a position the aligner moved (align/moves_R2.tsv) or a conflict witness (L02, L03, L06, L08, L09, L10, L11, L12, L13, L14, L01), each call asked only for the gloss letter over the named groups, plus 1 reconciliation unit, at ~$1.5 per call, ~$18
Resolved 2 Oct 2026 (GAPS4-na-schonenberg-1678-1716): body plaintext L01-L14 segmented and expanded as Spanish (body/reading_body.txt, KEY/GLOSS/SENSE per line; SENSE grades C 115 / M 120 / I 18, inferences in body/sense_inferences.tsv) and judged with controls on the two nearest corpora (es17c7, 1634-1648 letters, 55-80 years off; es = es17 fiction): KEY -1.482 / GLOSS -1.346 / SENSE -1.204 vs real_p05 -0.903/-0.922 FAIL on es17c7, 20 shuffled nulls -2.266..-1.985 and 20 shuffled targets -2.263..-1.838 all 0 PASS; the leaf's own gloss FAILs too, so "judge cannot decide" at this N and register (not a negative); the body reads as a cover-address instruction ending "...pondra solamente en sobre escrito en esta forma: a doña antonya de albanylla", corroborating L19 from the body's own sense (M). Unread spans: L04-L05 "zynenstanzyas", L05-L06 "que ay sera bran mexores pe no con anrya", L08-L09 "pues [23]saran de o[14]as yo[23]a[23]a".
- Judge calibration for the body: no era-matched Spanish corpus on disk (es17c7 is 1634-1648; the letter is 1702-1716) and the leaf's own gloss FAILs the nearest one, so the body's read-as-sense figure is measured but not gated - blocker: not-attempted; next: build tools/data/es18 from 1690-1720 Spanish letters or gazettes on archive.org (the V6-PTCORP pattern, ~12 minutes, outside requests to archive.org only), run its leave-one-file-out fold check at N=245 and re-run body/judge_body.py on it, ~$3; a corpus that passes the gloss and fails the shuffles is the gate the body lacks

## Escalation (1 Oct 2026; updated GAPS and GAPS2 2 Oct 2026)
- [x] siblings: NA 1.02.04 finding aid (26 pages, ~152 invnrs) grepped for cijfer/cijferschrift/geheimschrift/chiffre/sleutel: invnr 63 is the only cipher-flagged item (NOTES "Sibling inventory"); DECODE dumps of 24 Sept 2026 have no row for it; the nearest same-writer cipher, HU3 (Schonenberg to Heinsius no. 185, 1709, NA 3.01.19 invnr 1445, one cipher word, unsolved), is another correspondent and office, not this key. Optional, unrun: an eye-check of the other digitised 1.02.04 scans for cipher the cataloguer did not flag; and NA 3.01.19's undigitised "Stukken betreffende cijfers en sleutels van cijferschrift" (web search, 2 Oct 2026), official cipher material, probably not this private key.
- [x] clear-pages: done 2 Oct 2026 (GAPS): "forma." is L18's own gloss by layout; the address is L19's crib, 15/16 resolved positions agree against slid-window (max 0.286, n=229) and shuffled-crib (max 0.438, n=2000) controls; 28/28 closing tokens valued (C 15 M 13); conflicts 65 and 8) logged. No other clear text on the leaf is unused ("Amigo.", "Aquy", "&a" are single words already in clear).
- [x] known-keys: KEY-CROSSMATCH.tsv ran every key on file against ciphertext.tsv: only this target's own key fits (line 144, coverage 0.989); the best outside key, fr5160-letellier key_1659_ext, reaches 0.527 and does not pass (line 465); KEY-DESIGN.tsv records the design (homophonic, 87 codes); the key source is the leaf's own period gloss, so no outside key book is needed; Cryptiana/Cipherbrain nothing found (check-solved; web/blog check 2 Oct 2026, 0 hits).
- [x] print: check-solved 25 Sept 2026, six sources: IA full text "Schonenberg brieven" 0 hits; Heinsius Briefwisseling (Huygens retroboeken) Schonenberg 413 hits, none relevant, Albanilla/Albanylla 0; 8 web queries, DECODE dumps, both solver repositories; web and blog check 2 Oct 2026 (10 queries, three blogs, 0 hits). Not read: two Utrecht theses on Schonenberg (dspace.library.uu.nl and studenttheses.uu.nl, both HTTP 403 from the cloud), background only.
- [x] key-rebuild: done 2 Oct 2026 (GAPS2): tools/interlinear_align.py on L01-L14 + L18, three runs (unseeded, C-seeded, C+crib-seeded), R2 agreement 0.699 / 44 C-bar codes vs within-line shuffled-gloss control max 0.301 / 11 (n=300); key.tsv rebuilt from the tallies with the rule in align/rebuild_key.py (C 40 / M 43 / U 6; leaf tokens C 136 / M 127 / U 16); the earlier plurality tally is kept as align/key_before_2026-10-02.tsv. Nothing further for an aligner to do without new letters from the image.
- [ ] image-check: partly done: L06 pixel-verified 20/20 (25 Sept); L18-L19 at 4x (25 Sept); the L14-to-address layout at native resolution plus L19's blot and second row at 2x (2 Oct, GAPS). Not checked: the 12 codes the aligner leaves unsettled (gap 2 above: 6 U, 5 conflict, 8) p-vs-l) and passB's tick doubts. Planned: one line crop per subagent call for the 11 lines named in gap 2, gloss letter over the named groups only, ~$18.
- [ ] retry: done for L18-L19 (tools/decode_key.py --check exit 0 after the crib, 2 Oct 2026) and for the body after the aligner (--check exit 0, regraded: 38 U -> 16, GAPS2 2 Oct 2026; the closing-line judge re-run FAILs as before, 0 of 20 shuffled targets PASS). Body judged as Spanish 2 Oct 2026 (GAPS4): KEY/GLOSS/SENSE all FAIL real_p05 on es17c7 and es while 40 shuffled controls per corpus all sit 0.35-0.6 lower, 0 PASS; the leaf's own gloss FAILs too, so the judge cannot decide at this N (body/judge_body.log). Not yet: the same judge on an era-matched es18 corpus (gap 3, ~$3).
Verdict: keep going: 2 internal gaps; cheapest next: build an era-matched es18 corpus (1690-1720 Spanish letters, archive.org, V6-PTCORP pattern) with its fold check at N=245 and re-run body/judge_body.py on it, ~$3; then the image pass on the 12 unsettled codes with body/sense_inferences.tsv as the letters to confirm or refute, one line crop per call, ~$18

## Web and blog check (GAPS-na-schonenberg-1678-1716, 2 Oct 2026)
The CHECK-SOLVED-WEB required step (`.claude/briefs/check-solved.md`), run 2 Oct 2026 01:58-02:10 UTC via the WebSearch
tool (10 queries) and WebFetch (3 page opens); the on-disk Cryptiana snapshot `sources/cryptiana/` grepped first
(schonenberg / albanilla / albanylla: 0 files, 0 requests).
(a) Plain web searches: 1. `Schonenberg "Albanylla" OR "Albanilla" cipher letter Nationaal Archief 1.02.04` -- only the
NA finding aid itself (`nationaalarchief.nl/onderzoeken/archief/1.02.04`, the entry "Aan dona Antonya de Albanylla, z.d., In
cijferschrift" already read 25 Sept) and unrelated NA/VOC pages. 2. `"1.02.04" Schonenberg "cijferschrift" OR "cifra"
OR "chiffre" invnr 63` -- the same finding aid; plus Heinsius archive 3.01.19 entries (one of them a general "Stukken
betreffende cijfers en sleutels van cijferschrift" and "Brieven van F van Schonenberg uit Madrid", neither about this
item, neither digitised: lead logged in the GAPS section and under Escalation siblings above). 3. `"Antonia de Albanilla" OR "Antonija de Albanylla"
OR "Antonya de Albanylla"` -- 0 relevant hits (name pages only). 4. `Francisco van Schonenberg gezant Spanje Portugal
brief in cijferschrift doña Antonia` -- the finding aid, and two Utrecht theses on Schonenberg's diplomacy
(`dspace.library.uu.nl/handle/1874/334523`, `studenttheses.uu.nl/handle/20.500.12932/20077`): both answer HTTP 403 to
WebFetch (one attempt each, not retried; background works, no sign in the search snippets of any cipher or of this
letter). 5. `"mudado este gobierno" OR "aver mudado este" Schonenberg carta cifrada` (the leaf's most distinctive
glossed phrase) -- 0 relevant hits. 6. `"Aan dona Antonya de Albanylla"` (the folder's catalogue title) -- 0 hits.
7. `Schonenberg Albanylla cipher solved Claude OR GPT OR "solves"` (model-solve announcements) -- only the unrelated
Urquhart/Cyphral Distich coverage, nothing on this item.
(b) Blog site searches: `site:scienceblogs.de/klausis-krypto-kolumne Schonenberg OR Albanilla OR Albanylla` -- 0 posts
naming either (Cipherbrain); `site:cryptiana.blogspot.com Schonenberg OR Albanilla OR "Nationaal Archief" cipher` -- 0
posts naming either (Cryptiana blog; Tomokiyo's fc2 pages covered by the on-disk grep); `site:ciphermysteries.com
Schonenberg OR Albanilla OR "Nationaal Archief" Dutch envoy Madrid cipher` -- 0 Cipher Mysteries posts (the engine
returned TNA catalogue rows for Schonenberg's 1690s Madrid dispatches instead, not this letter).
(c) Comment threads: no post about this letter exists on any of the three blogs to open, so no comment thread to read;
the three page opens above were the two thesis records (403) and the 3.01.19 entry.
Result: no decipherment or plaintext of this item located by these queries on 2 Oct 2026 (a search result, not a
novelty verdict, rule 10). Status word unchanged (`partial`).
Requests per host: WebSearch 10 queries; dspace.library.uu.nl 1 (403); studenttheses.uu.nl 1 (403); nationaalarchief.nl 1.
