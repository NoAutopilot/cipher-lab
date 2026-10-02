partial
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

## Remaining gaps (finish-or-blocker pass, 1 Oct 2026; updated GAPS 2 Oct 2026)
Read so far: 279 of 279 cipher groups (100%) now carry a value: 251 body groups under the leaf's own period gloss (L01-L14, ciphertext.tsv; 244-246 with a gloss letter, see 1 Oct text in git history), L18's 5 under its own gloss "forma." (found 2 Oct 2026), L19's 23 under the address crib with controls (15/16 resolved agree); by grade the leaf is C 99 / M 142 / U 38 (reading_tokens.tsv, 2 Oct 2026), L18-L19 alone C 15 / M 13 / U 0. Read-as-sense is still unmeasured for the body: the gloss has never been segmented into Spanish words ("Letter's gist" is M-grade).
Resolved 2 Oct 2026 (GAPS-na-schonenberg-1678-1716): the L18-L19 gap -- "forma." is L18's own interlinear gloss (layout, image check), L19 = "a doña antonya de albanylla" against the address (crib_align.py, slid-window and shuffled-crib controls both at 0 of 229 / 0 of 2000 at or above target), decode_key.py --check exit 0; 65 and 8) logged as conflicts (conflicts.tsv, HYPOTHESES.md H1).
- L01-L14 code-to-gloss alignment: 22 tied codes, 55 codes in conflicts.tsv (49 + the 6 crib rows), 5 tail groups with no gloss letter (L08 pos18 `)2`, L10 pos14-15 `)1` `55`, L13 pos16 `23`, L14 pos17 `34`), regenerated through key.tsv as 38 U / 129 M body tokens; the five crib-fixed codes (24, 34, 51, 11, 65) sit at M only because one or two body glosses each disagree with the crib - blocker: not-attempted; key.tsv and rederivation_key.tsv are both a plurality tally of passB's position-by-position alignment, which passB itself says is off by 1-2 groups on L04, L08, L10, L11, L13, L14 (passB_summary.txt); only L06 was pixel-verified (20/20); tools/interlinear_align.py has never been run here; next: run tools/interlinear_align.py line by line on (group sequence, gloss letter sequence) for L01-L14, seeded with the C codes and the crib-fixed codes, rebuild key.tsv from its counts, raise the crib codes to C where the disagreeing glosses prove to be alignment slips, list only the codes it leaves unsettled for the image pass, ~$4
- Gloss and group transcription in the dense stretch L04-L05 and L07-L14 (66 of 251 glossed-line rows at M confidence) plus the specific doubts passB names: tick-before vs tick-after and tick vs digit (the 8) = p vs l conflict at L03 pos0 / L19 pos20 is one of them), the 9 drawn-shape signs; L01's later-ink `23`/"N"/blot; L09 pos0 "20" vs "Lo" - blocker: not-attempted; NOTES "Suggested next step" and NEXT-STEPS.tsv (line 115, runnable, never run); the leaf reads cleanly at native resolution and 2x (L06, L18, L19), so the limit is alignment in crowded hand, not image quality; next: after the aligner, cut crops with `tools/iiif_lines.py --image images/NL-HaNA_1.02.04_63_0001.jpg --out images/lines` (command pasted in the brief), one line crop per Sonnet subagent call, only for lines with unsettled codes, at most 12 lines + 1 reconciliation unit at ~$1.5 per call, ~$20
- Body plaintext L01-L14 as Spanish (gloss is an unsegmented letter run, e.g. L14 "sobre...en esta" + L18 "forma"; the L01 date "Nobe[mbre]" is M) - blocker: not-attempted; no word-segmented or expanded reading exists and the spec judged only the closing lines, so the read-as-sense figure cannot be measured; next: after the alignment and image pass, segment and expand the gloss against the image into a per-line reading, run tools/judge_plaintext.py on it with shuffled-null controls (es corpus era check per rule 3 first, the letter is 1702-1716), ~$3

## Escalation (1 Oct 2026; updated GAPS 2 Oct 2026)
- [x] siblings: NA 1.02.04 finding aid (26 pages, ~152 invnrs) grepped for cijfer/cijferschrift/geheimschrift/chiffre/sleutel: invnr 63 is the only cipher-flagged item (NOTES "Sibling inventory"); DECODE dumps of 24 Sept 2026 have no row for it; the nearest same-writer cipher, HU3 (Schonenberg to Heinsius no. 185, 1709, NA 3.01.19 invnr 1445, one cipher word, unsolved), is another correspondent and office, not this key. Optional, unrun: an eye-check of the other digitised 1.02.04 scans for cipher the cataloguer did not flag; and NA 3.01.19's undigitised "Stukken betreffende cijfers en sleutels van cijferschrift" (web search, 2 Oct 2026), official cipher material, probably not this private key.
- [x] clear-pages: done 2 Oct 2026 (GAPS): "forma." is L18's own gloss by layout; the address is L19's crib, 15/16 resolved positions agree against slid-window (max 0.286, n=229) and shuffled-crib (max 0.438, n=2000) controls; 28/28 closing tokens valued (C 15 M 13); conflicts 65 and 8) logged. No other clear text on the leaf is unused ("Amigo.", "Aquy", "&a" are single words already in clear).
- [x] known-keys: KEY-CROSSMATCH.tsv ran every key on file against ciphertext.tsv: only this target's own key fits (line 144, coverage 0.989); the best outside key, fr5160-letellier key_1659_ext, reaches 0.527 and does not pass (line 465); KEY-DESIGN.tsv records the design (homophonic, 87 codes); the key source is the leaf's own period gloss, so no outside key book is needed; Cryptiana/Cipherbrain nothing found (check-solved; web/blog check 2 Oct 2026, 0 hits).
- [x] print: check-solved 25 Sept 2026, six sources: IA full text "Schonenberg brieven" 0 hits; Heinsius Briefwisseling (Huygens retroboeken) Schonenberg 413 hits, none relevant, Albanilla/Albanylla 0; 8 web queries, DECODE dumps, both solver repositories; web and blog check 2 Oct 2026 (10 queries, three blogs, 0 hits). Not read: two Utrecht theses on Schonenberg (dspace.library.uu.nl and studenttheses.uu.nl, both HTTP 403 from the cloud), background only.
- [ ] key-rebuild: only a plurality tally so far (key.tsv now 29+ C / M / U as regenerated; rederivation_key.tsv 38 unanimous / 27 majority / 22 ties, same method) plus the crib's five fixes at M; no DP/EM alignment, annealing or LM context tried, so no instrument has failed its gate even once. Planned: tools/interlinear_align.py on L01-L14 seeded with the C codes and the crib-fixed codes (gap 1), ~$4.
- [ ] image-check: partly done: L06 pixel-verified 20/20 (25 Sept); L18-L19 at 4x (25 Sept) and the L14-to-address layout at native resolution plus L19's blot and second row at 2x (2 Oct 2026, GAPS). Not checked: the 55 conflicts.tsv codes, the tick-position/tick-vs-digit doubts and the dense L04-L05/L07-L14 stretch. Planned: one line crop per subagent call, only for codes the aligner leaves unsettled (gap 2), ~$20.
- [ ] retry: done once for L18-L19 (tools/decode_key.py --check exit 0 after the crib, 2 Oct 2026); not yet for the body because the key has not been re-aligned. Planned: after the aligner, rerun tools/decode_key.py --check, regrade the 38 U and the crib-fixed M tokens of the regenerated L01-L14, re-judge, ~$2.
Verdict: keep going: 3 internal gaps; cheapest next: run tools/interlinear_align.py line by line on L01-L14 seeded with the C codes and the crib-fixed codes, rebuild key.tsv and regrade, ~$4

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
