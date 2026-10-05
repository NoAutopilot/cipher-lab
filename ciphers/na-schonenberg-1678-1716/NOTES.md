partial
Check-solved citation (carried up 2 Oct 2026, GAPS6, from the unchanged "## Check-solved, six sources (25 Sept 2026)" section below; gate repair only): no printed edition of Schonenberg's correspondence exists on Internet Archive (advancedsearch full-text `Schonenberg brieven`, 0 results, 25 Sept 2026); the standard edition for his office, *Briefwisseling van Anthonie Heinsius 1702-1720* (Veenendaal ed., 19 vols, Huygens retroboeken), full-text searched 25 Sept 2026 for `Schonenberg` (413 hits, his official reports, none this letter or correspondent), `Albanilla` and `Albanylla` (0 hits each); the NA 1.02.04 finding aid (26 pp.) read in full and grepped; DECODE dumps of 24 Sept 2026 and both solver repositories grepped; web and blog check 2 Oct 2026 (section at the end of this file).
GAPS14 2 Oct 2026: code 36 gloss-hand letterform test (body/letterform/, 14 value-blind tiles, 2 blind Opus sorts agree 14/14): known-answer 10/10 (c 2/2, e 8/8) vs 20-seed label shuffle mean 0.680, p95 0.800; all 4 tiles over 36 sort with the known c's -> 36 = c at C (pre-registered gate, commit 9abe5b16); leaf C 270 / M 11, body C 243 / M 10, decode_key --check exit 0.
GAPS13 2 Oct 2026: code 36 word-level dictionary test (es18+es17c word list, body/ce36_dict.py, disk only): 3 of 4 occurrences c-only, 0 e-only, vs label-shuffle p95 2 (max 3) and position-shuffle max 2 (20 seeds each); known answer 15/15 right but 15 of 38 decisive, under the registered half: gate not cleared, 36 stays M; leaf C 266 / M 15, body C 239 / M 14, decode_key --check exit 0.
GAPS12 2 Oct 2026: judge re-run on the GAPS11 body (disk only): es18 KEY -1.114 vs real_p05 -0.975 FAIL, leaf gloss -1.313 FAILs below it, 0/20 + 0/20 controls PASS on es18/es18p/es17c7/es: judge cannot decide, not a negative; code 36 c/e context test (es18 4-gram, body/ce36_context.py): sum D(c-e) +2.181, 2 of 4 prefer c, vs 20-seed shuffled-assignment max +8.017 (2/20 at or above): does not beat the control, 36 stays M; leaf C 266 / M 15, body C 239 / M 14, decode_key --check exit 0.
GAPS11 2 Oct 2026: native-resolution blind pair (2 Opus passes + 1 look, 3 vision calls; the disk image is the native 1946x2618) on the 18 body M positions: L01 23 (gloss-row recopy), 18 g, L06 50 s, L14 )3 t to C; 58 = l (M); L09 pos0 and L10 pos0 are symbols; key-M predictions 8/11 vs shuffled 20 seeds mean 1.15 max 3; leaf C 266 / M 15 (body C 239 / M 14), decode_key --check exit 0.
GAPS9 2 Oct 2026: image pass on the 45 M positions of L01, L02, L04, L06, L08, L09, L11, L13 (3 batches x 2 blind Opus passes + 1 reconciliation each, 9 vision calls): pass agreement 116/135; 12 codes raised to C (15 d, 28 s, 5 e, 26 q, 33 z, 82 e, )0 q, )5 u, 44 y, 66 m, [T] o; 40 e -> g), 21) n -> r M, L08 pos18 )2 = u C (exception); key M predictions 42/45 vs shuffled 20 seeds mean 4.10 max 7; leaf C 207 / M 73 (was C 184 / M 96), decode_key --check exit 0; judge re-run es18 KEY -1.137 vs real_p05 -0.957 FAIL (was -1.175), gloss -1.329, 0/20 + 0/20 controls PASS: judge cannot decide.
GAPS8 2 Oct 2026: judge re-run on the GAPS7-changed body (KEY es18 -1.175 vs real_p05 -0.957 FAIL, was -1.445; above the leaf's own gloss -1.329; 0/20 shuffled-null and 0/20 shuffled-target PASS on all four corpora); image pass on L05, L07, L10 and L03, L12, L14 (2 batches x 2 blind Opus passes + 1 reconciliation each, 6 vision calls): pass agreement 101/108, 15 codes raised to C ()2 = s and )4 = u value changes), L07 pos10 is 2) not 23; key M predictions 49/56 vs shuffled 20 seeds mean 5.45 max 10; leaf C 184 / M 96 (was C 171 / M 109), decode_key --check exit 0.
GAPS7 2 Oct 2026: image pass on the 12 unsettled codes (12 body lines, 2 blind Opus passes + 1 reconciliation, 9 vision calls): 23 n, 14 c, 55 z, 50 s, 34 a, 49 r, 11 a, 31 x, 8) l, [blot] NULL settled C, 96 o/y per position, )52 = )2 + 38; seven transcription errors corrected; sense predictions 10/11 agree vs shuffled-prediction control mean 1.50 max 4 (20 seeds); leaf C 171 / M 109 / U 0 (was C 136 / M 127 / U 16), decode_key --check exit 0.
GAPS5 2 Oct 2026: era-matched corpus tools/data/es18 built (7 archive.org items, 1690-1725, 2.54M letters, long-s repaired) and the body re-judged on it: SENSE -1.140 vs real_p05 -0.962 FAIL (gap 0.178, was 0.282 on es17c7; both sides moved together), the leaf's own gloss -1.352 FAILs beside it, 0/20 shuffled-null and 0/20 shuffled-target PASS; es18's own fold check at N=245 spreads 0.0-79.0% (36.1% blended) so its FAIL/PASS is of unknown reliability (rule 3) -- judge cannot decide at this N on any of three corpora; judge retired as the instrument for this body, next is the image pass.
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

## GAPS5-na-schonenberg-1678-1716 (2 Oct 2026, account-4)
Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; the Verdict step of the Remaining-gaps section as rewritten by GAPS4 (the
judge-calibration gap), run 06:06-06:4x UTC. Intake gate exit 0 at the start. 0 vision calls. Requests: archive.org 10 (2 advancedsearch,
8 `_djvu.txt`), one at a time, >= 1.5 s apart, descriptive UA; no other host. Files: `tools/data/es18/` (build.py, MANIFEST.tsv, README.md,
holdout_check.py, three fold logs, seven `.txt.gz`), `tools/judge_plaintext.py` (LANG_CORPORA keys `es18` and `es18p`),
`tools/tests/test_judge_plaintext_lang_es18.py`, `body/spec_body_es18.json`, `body/spec_body_es18p.json`, `body/judge_body.py` (`--corpora`),
`body/judge_body_gaps5.log`, `body/judge_body_results.tsv` (now four corpora). key.tsv, reading.txt and reading_tokens.tsv untouched
(`tools/decode_key.py ciphers/na-schonenberg-1678-1716 --check` exit 0).

**1. Corpus (V6-PTCORP pattern).** Seven distinct archive.org items, all original Spanish prose of 1690-1725: San Felipe's *Comentarios de la
guerra de España* I-II (1700-1725, written c.1725 by a Philip V diplomat; 1792 print), Caraffa's *El embaxador político-christiano* (1691),
*Crisol de la española lealtad* (1708), *Nuevo estilo y formulario de escrivir cartas missivas* (c.1700, model letters), *Gaceta de Madrid*
1710, Vera Tassis's *Noticias historiales* (1690). 2,540,604 folded letters; the five original printings long-s repaired against a clean
reference vocabulary, junk lines dropped (tools/data/es18/README.md has the per-file counts and the cross-corpus word coverage, 0.69-0.90).
Hold-out grep of all seven raw files for Schonenberg/Schonemberg/Albanilla/Albanylla: 0 hits.

**2. Fold check at N=245 (rule 3, fold-count paragraph), 200 windows per fold, logs in tools/data/es18/.**
es18 (7 folds): 505/1400 = 36.1% false negatives, per-fold spread 0.0-79.0% (San Felipe I/II 1.0/0.0%, Caraffa 19.0%, Crisol 42.5%,
letter manual 65.5%, Gaceta 45.5%, Vera Tassis 79.0%). es18p (the five originals only): 60.1%, spread 29.5-74.0%. es17c7 at the same
N=245: 7.7%, spread 4.0-14.5%. The era-matched corpus is not internally uniform (the 1792 San Felipe print dominates and sets real_p05;
the period originals are each other's outliers -- the EN-FOLDS shape), so **a FAIL/PASS against es18 at N=245 is of unknown reliability**
by rule 3's own rule. The era match is nonetheless real: a genuine 1709 period letter outside the corpus (Philip V's circular to the
cities, A10903513, N=1069) PASSes es18 (-0.920 vs real_p05 -0.947) and FAILs es17c7 (-1.033 vs -0.865); it is the offline test.

**3. Body judged under es18 beside es17c7 (same 20 shuffled-null + 20 shuffled-target controls, seed 1; gloss beside the candidate):**

| corpus | KEY (235) | GLOSS (245, the leaf's own period gloss) | SENSE (245, candidate) | real_p05 | null_p99 | shuffled-null PASS | shuffled-target PASS |
|---|---|---|---|---|---|---|---|
| es18 | -1.445 FAIL | -1.352 FAIL | -1.140 FAIL | -0.948 / -0.962 | -1.679 / -1.711 | 0 of 20 | 0 of 20 |
| es18p | -1.436 FAIL | -1.341 FAIL | -1.168 FAIL | -0.957 / -0.973 | -1.733 / -1.718 | 0 of 20 | 0 of 20 |
| es17c7 (GAPS4) | -1.482 FAIL | -1.346 FAIL | -1.204 FAIL | -0.903 / -0.922 | -1.858 / -1.894 | 0 of 20 | 0 of 20 |
| es (GAPS4) | -1.413 FAIL | -1.311 FAIL | -1.153 FAIL | -0.919 / -0.894 | -1.828 / -1.832 | 0 of 20 | 0 of 20 |

(real_p05 and null_p99 are given at N=235 / N=245.) Both sides of the gate moved together under es18: the candidate rose 0.064 (-1.204
to -1.140) and the gate fell 0.040 (-0.922 to -0.962), closing the gap from 0.282 to 0.178 -- the calibration-fix shape, not
threshold-shopping -- but SENSE still FAILs, and the leaf's own genuine gloss scores 0.21 below the candidate under every corpus
(the ZX-DEC349 clause: the candidate sits far nearer real prose than the shuffles, -1.14 against -1.85 to -2.14, and the known-genuine
text from the same leaf fails harder than it does). Verdict of the step: **judge cannot decide at this N and register; not a negative**.
The shuffled-target check stays clear (0 of 20 under every corpus), so a PASS here would not have been voided -- there is just no PASS.

**4. Rule 3, third-attempt clause.** This is the third corpus (es fiction, es17c7 1634-1648, es18 1690-1725) on which the same instrument
(tools/judge_plaintext.py, add-k 4-gram, N=245) returns the same shape: candidate FAIL, gloss FAIL below it, controls all FAIL. The
era knob was the one bet of this re-run and it moved both sides the right way without reaching the gate; a fourth corpus is a further
tuning of the same knob. The judge is logged as untestable-by-this-instrument for this body at N=245 (not refuted) and the gap below is
[retired] for that instrument; what reopens it is new material (more ciphertext from the same hand, e.g. the sibling HU3 letter to
Heinsius of 1709, or the image pass settling the 12 unsettled codes, which changes the text being judged rather than the corpus).
Nothing found or not found here is a novelty claim (rule 10). Status word unchanged (`partial`).

## GAPS7-na-schonenberg-1678-1716 (2 Oct 2026, account-4)
Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; the Verdict step of the Remaining-gaps section (the image pass on the 12
unsettled codes), run 20:50-21:1x UTC. Intake gate exit 0 at the start. Disk only (the leaf on disk), 0 network requests. Vision calls:
9 (two blind Opus passes x 4 batches of 3 lines, plus 1 reconciliation look by this worker over the L03/L08/L09 crops). Files:
`images/lines/` (tools/iiif_lines.py --image ... --centres run `g7_*` with its debug overlay, and `g7x_*`: the same 14 gloss+cipher
line pairs with 55 px above the gloss row and 1.6x upscale, boxes in `g7x_manifest.json`), `body/image_pass/` (passA_b1-4.tsv,
passB_b1-4.tsv, settled.tsv, compare.py, compare.log, passes_agreement.log, key_before_GAPS7.tsv, exceptions_before_GAPS7.tsv).

**Design.** Lines read: the 11 named in gap 1 plus L04 (it carries three of the coded sense predictions; 12 lines = 4 batches of 3, so
no extra call). L05 and L07 were not read (L05: 50, 11, 50; L07: 23). The readers saw only the crops and each line's group sequence
with the positions to look at; they did NOT see body/sense_inferences.tsv, passB's gloss, the key or each other. Pass A paired
letters with groups as it saw fit; pass B was told to place each letter by x-position on vertical slices at 2-3x zoom.

**Pass agreement.** 186 of 213 common positions give the same letter (b=v, i=y=j, c=z); 29 of 32 starred positions. Of the
disagreements, L02 accounts for 17: pass A paired its letters in order and dropped the D flourish over 81; shifted one group, its
L02 letters match pass B 16 of 16. L01 pos7 is one difference of notation only (both passes: the blot carries no second letter).

**Transcription corrections (both passes independently, confirmed in the reconciliation look; ciphertext.tsv edited in place,
the earlier version is in git).** L03 pos5 is `5)`, not 55; L03 pos12 is `3)`, not 31 (so the 55 b/z and 31 x/d conflicts were
transcription errors); L08 pos15 is not 23 (a 2 with a looped second digit, 22 or 26; kept as `2?`, gloss e); L09 pos12 is `2)`, not
23 (r, as 2) reads everywhere); L09 pos13-14 `)8 9` is one group `8)` (gloss l); L09 pos18 `)10` is `)` then `10` (u, e); L12 pos16
`)52` is `)2` followed by a separate `38` (s, e). L01 pos6-7: the decipherer wrote "23." again in the gloss row above the blotted group
with n over it; the blot is that group (key `[blot]` = NULL, the n stays on pos6). L09 renumbered from pos14 on (11, 50, 26, ), 10);
L12 gains pos17. Noted, not applied (the passes disagree or it is outside the 12 codes): L04 pos16-17 may be `2) 36 )` with u over the
lone `)` (pass B; gloss "zyrcun", i.e. "circun[stancias]"), pass A kept `21) 36)` with a u over no group; L10 pos0-2 is a curl, a
`)` and `)0` with a small 2 above (neither pass sees `)2`), with no gloss over them; L11 pos3-4 a y between 6 and 44.

**The 12 codes, settled (rule 4; C = the leaf's own gloss read the same by both blind passes):**

| code | was | settled | grade | evidence |
|---|---|---|---|---|
| 23 | U (n/r tie) | n | C | L01, L04, L09 pos10, L13 pos16; the two r witnesses were 2) and 2? (L07 unchecked, kept r M in exceptions) |
| 14 | U (e/l) | c | C | L04 pos8, L09 pos5 |
| 55 | U (b/z) | z | C | L10 pos15 (L03's "55" is 5) = b, now keyed C) |
| 96 | U (o/y) | o and y | C per position, M as a code | L13 pos1 o, pos15 y, both clear in both passes |
| [blot] | U | NULL | C | no letter over either blot (L14 pos3; L01's blot is the recopied 23) |
| )52 | U | -- | -- | not a group: )2 (s) + 38 (e) |
| 50 | M s/r | s | C | 5 occurrences s; L06 pos17 s in both passes against VX-RD01's pixel r: that position M |
| 34 | M a/d | a | C | L02, L11, L12, L14 (and the L19 crib) |
| 49 | M n/r/u | r | C | L04, L06, L11 ("espero" at L06) |
| 11 | M a/s | a | C | L09 (and the L19 crib; L05 unchecked) |
| 31 | M x/d | x | C | L06 pos3; the d was at a 3) |
| 8) | M p/l | l | C | L03 pos0, L09 pos13 (and the L19 crib) |

Also settled in passing: 81 = d (C; L11 both passes, L02 pass B), )2 = s at L03, L12, L14 (C exceptions; key )2 stays r M from
unchecked positions), 5) = b, ) = u. Ten C codes, one code (96) with two C position values, one non-group.

**Sense predictions vs the image (rule 3), `python3 body/image_pass/compare.py --seeds 20`:** of the 12 sense-side letters at these
codes, 11 positions were read (L07 pos10 was not); **10 of 11 agree** (only L13 pos15: predicted e, read y). Control: the same 11
predicted letters shuffled across the 11 positions, 20 seeds: mean 1.50, max 4, 0 of 20 at or above 10. At the code level the
predictions for 23 (n), 14 (c), 49 (r), 50 (s), 8) (l) are confirmed; 31's predicted d and 55's predicted v were right letters at
positions whose group was misread (3), 5)); 96 is o once and y once (e refuted).

**Leaf after the pass (`python3 tools/decode_key.py ciphers/na-schonenberg-1678-1716 --check`: "reading up to date", exit 0):** 280
tokens, C 171 / M 109 / U 0 (was 279: C 136 / M 127 / U 16); body L01-L14 C 147 / M 105, L18-L19 C 24 / M 4. The regenerated body
(reading.txt, M-grade where M) now runs: "no abyendo nobedad en estas partes que la de aber mudado este gouyerno con las zy[rcun]-
stanzyas que ay sera bra[n] mexores pero con ansya las que ybyere del norte y de ytalya pues esa[u]an de ocasyonar las que puedan
ocurryr. para [y] mas seguridad de la corespondenzya se pondra solamente yn sobre scryto en esta forma: a doña antonya de albanylla"
(bracketed = the passes' gloss where the key still reads otherwise). The body is not complete at S/C (105 M tokens remain, the
aligner's sub-C-bar codes), so no "verifier wanted" line from this job. The judge is not re-run here (retired, GAPS5); the changed
text is what reopens it. Nothing here is a novelty claim (rule 10); status word unchanged (`partial`).

## GAPS8-na-schonenberg-1678-1716 (2 Oct 2026, account-4)
Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; the Verdict step of the Remaining-gaps section, run 21:10-21:2x UTC (container clock).
Intake gate exit 0 at the start ("partial (line 1) -- edition/page or full-text-search citation found within 6 lines"). Disk only, 0 network
requests. Vision calls: 6 (2 batches x 2 blind Opus passes, plus 1 reconciliation look per batch by this worker over two crops each).

**(1) Judge re-run on the changed body (rule 7; `python3 body/judge_body.py --shuffles 20 --seed 1 --corpora es18,es18p,es17c7,es`,
log body/judge_body_gaps8.log, the pre-image-pass run kept as body/judge_body_gaps8_pre_image.log).** Script fix first: the KEY text had
carried the blot's key value `NULL` as four letters (GAPS7 keyed [blot] = NULL); judge_body.py now drops it, as it drops `[?]`. Only the KEY
and GLOSS texts changed (reading_tokens.tsv and the ciphertext.tsv gloss column); body/reading_body.txt's SENSE lines were not re-segmented,
so SENSE scores are unchanged. Final run (after this job's image pass), es18 (era-matched): KEY N=247 -1.175 vs real_p05 -0.957 FAIL (GAPS5:
-1.445 at N=235, so the gap fell from 0.497 to 0.218), GLOSS -1.329 FAIL, SENSE -1.140 FAIL; shuffled-null -2.078..-1.883 and shuffled-target
-2.098..-1.863, 0 of 20 PASS each. Same shape on es18p (KEY -1.191 vs -0.959), es17c7 (-1.232 vs -0.905) and es (-1.185 vs -0.904), every
control 0 of 20. Before the image pass (GAPS7 text, NULL dropped): es18 KEY -1.202 vs -0.972. The key-regenerated body now scores above the
leaf's own contemporary gloss on every corpus, and both still FAIL: judge cannot decide at this N (the ZX-DEC349 shape), not a negative.
Pasted (es18 block, verbatim):
```
$ judge_plaintext.py body/spec_body_es18.json --text <KEY>  (exit 1)
  ok   length: got=247, min=100, max=1000000000
  FAIL language: score=-1.175, null_p99=-1.749, real_p05=-0.957, real_median=-0.833, mode=both, N=247
```
(remaining rows in body/judge_body_gaps8.log and body/judge_body_results.tsv.)

**(2) Image pass, method as GAPS7.** Crops: the GAPS7 `tools/iiif_lines.py --image` crops on disk (images/lines/g7x_*, boxes in
g7x_manifest.json), no new cut. Batch 1 = L05, L07, L10 (L05 and L07 first, as the Verdict named; L10 for its 12 M positions); batch 2 =
L03, L12, L14 (8, 9 and 11 M positions). Readers saw only the crops and the expected group sequence with the M positions starred; not
body/sense_inferences.tsv, the key, the 25 Sept gloss column or each other. Files: body/image_pass/g8_passA_b1-2.tsv, g8_passB_b1-2.tsv,
g8_settled.tsv, compare_g8.py, compare_g8.log, and the before-snapshots *_before_GAPS8.tsv.
- Pass agreement: 101 of 108 positions (L05 19/20, L07 16/18, L10 16/16, L03 18/18, L12 15/18, L14 17/18). Reconciliation settled five
  splits (L12 pos2 i, L12 pos17 e, L14 pos14 e, L07 pos8 y, L07 pos10 r) and left two (L05 pos1 )3 t vs l+c; L12 pos14 )6 i vs r).
- Transcription correction (both passes): L07 pos10 is `2)`, not 23 (gloss r) -- 23's last r witness was a misread group, as at L09 in GAPS7.
- The 25 Sept gloss column (ciphertext.tsv `gloss`) is offset by one or more groups in L10, L12 and L14; read offset-corrected it agrees
  with the two passes except at L10 36 (c vs e) and L10 2) (r vs n).
- Codes raised to C (rule 4; both passes agree at every image-read occurrence, no read occurrence contradicts): )9 b, 2 u, 52 u, 69 p, 90 o,
  99 z, [X] e, [Z] y, [circle] o, [square] e, [tilde] a (single occurrences); 94 s (3 of 5 occurrences read); 6) n (L05, L10, L12 n; L07's
  "h" is the hand's capital N, that position M); and two value changes: )2 r -> s (L03, L05, L12, L14 all s; the aligner's r witnesses were
  offset letters) and )4 r -> u (L10, u in both passes and in the offset-corrected 25 Sept column).
- Not settled: 36 (c, M): both passes read e at L10 and L14, the 25 Sept column c at L10 and sense needs c at both ("ocurrir", "escrito");
  the hand's c and e are close -- kept M. L10 2) (pos12): both passes n, key and 25 Sept r -- exception r M. 28, 15, 5, )0, 26, 33, 82, )3:
  under half their occurrences image-read, kept M.
- New exceptions: L10 pos0-2 NULL M (no gloss over the line-start groups in either pass, GAPS7 and GAPS8 alike; the groups themselves are a
  curl and a )0 with a small 2 above), L10 pos12 r M, L07 pos15 n M, L08 pos18 s M (not image-read, no gloss letter there); the L07 pos10
  exception is removed (now 2) = r C).
- Predictions vs image (rule 3, `python3 body/image_pass/compare_g8.py --seeds 20`): at the 56 key-M positions with a settled image letter,
  the key's M value agrees at 49 of 56; the same letters shuffled across the 56 positions, 20 seeds: mean 5.45, max 10, 0 of 20 at or above
  49. SENSE predictions (sense_inferences.tsv where it names a letter): 48 of 56 vs mean 5.60, max 10, 0 of 20. Misses: )2 r (now s), )4 r
  (now u), 36 c (read e twice), L10 2) and the L10 line-start groups, 58 (sense c, read i).

**Leaf after the pass (`python3 tools/decode_key.py ciphers/na-schonenberg-1678-1716 --check`: "reading up to date", exit 0):** 280 tokens,
C 184 / M 96 / U 0 (was C 171 / M 109); body L01-L14 C 157 / M 95 (was 147 / 105); L18-L19 C 27 / M 1 (was 24 / 4). The regenerated body
(reading.txt) is a key reading at C/M, not a fresh decipherment: the leaf carries its own period gloss. Nothing here is a novelty claim
(rule 10); status word unchanged (`partial`); 95 body M tokens remain, so no "reading ready" line from this job.

## GAPS9-na-schonenberg-1678-1716 (2 Oct 2026, account-4)
Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; the Verdict step of the Remaining-gaps section ("image pass on the M positions of
L01 L02 L04 L06 L08 L09 L11 L13 (9 vision calls) then judge re-run"), run 21:28-21:4x UTC (container clock). Intake gate exit 0 at the start
("partial (line 1) -- edition/page or full-text-search citation found within 6 lines"). Disk only, 0 network requests. Vision calls: 9 (3 batches
x 2 blind Opus passes, plus 1 reconciliation look per batch by this worker over a composite of the split positions).

**Method, as GAPS7/GAPS8.** Crops: the GAPS7 `tools/iiif_lines.py --image` crops on disk (images/lines/g7x_L01..L13, boxes in g7x_manifest.json);
no new cut (all eight lines present). Batch 1 = L01, L02, L04; batch 2 = L06, L08, L09; batch 3 = L11, L13. 45 M positions (from
reading_tokens.tsv grade M) starred. Readers saw only the crops and the expected group sequence with the M positions starred; not
body/sense_inferences.tsv, the key, the 25 Sept gloss column or each other. Pass A paired letters with groups as it saw fit; pass B placed each
letter by x-position on 500 px slices at 2-3x zoom. Files: body/image_pass/g9_passA_b1-3.tsv, g9_passB_b1-3.tsv, g9_settled.tsv, compare_g9.py,
compare_g9.log, the before-snapshots *_before_GAPS9.tsv. Pass A of batch 2 left L09 pos7-15 (all C positions) unread.

**Pass agreement:** 116 of 135 common positions (L01 14/14, L02 13/18, L04 12/19, L06 20/20, L08 17/19, L09 9/10, L11 15/18, L13 16/17); most
splits sit at C positions where the gloss row drifts right (L02, L04 pos2-6). At the 45 starred positions the passes agree at 39; the reconciliation
looks settled L02 pos9 s (s/l), L04 pos0 g (g/q), L04 pos18 n (u/n), L09 pos0 a (A/d: a swash capital A over the "Lo"-shaped 20), L04 pos16 r (r/n: the
w-form r, the same letter both passes read over 93 = r at L11), and identified the "L" both passes read over 15 at L01 as the hand's looped d.

**Settled (rule 4; C = both blind passes and the leaf gloss agree at every image-read occurrence, none contradicts):**
- Codes raised to C: 15 d (L01, L08, L11 + L03 GAPS7: all 4), 28 s (all 7; L02 settled on reconciliation), 5 e (all 3), 26 q, 33 z, 82 e (both occurrences
  each), )0 q (L02, L07; L10 pos1 a doubtful group, NULL M exception), and single occurrences )5 u, 44 y, 66 m, [T] o; value change 40 e -> g (L11, both passes
  and the reconciliation look: "seg-uridad").
- Value change at M: 21) n -> r (passes split r/n; reconciliation r).
- Exception: L08 pos18 )2 s M -> u C (pass A "v", pass B "u": a v-form u; GAPS8 had it as not image-read).
- Read but kept M: 18 g and 20 a (single occurrences, passes split, reconciliation agrees with the key), 36) e (pass B "eu": GAPS7's doubt that
  36) is 36 + ) stands), 36 c (L06 c in both passes, but L10 and L14 e in both passes, GAPS8), L06 pos17 50 s (both passes s again; VX-RD01's
  pixel r stands against it), L04 pos18 45 n (split, reconciled n).
- Noticed at C positions, not applied (outside the M list; the gloss row drifts there): both passes read a, not e, over 60 at L08 pos4 and L09 pos3;
  over 54 at L08 pos2 o vs a (key y); an m stands between 44 and )8 at L11 over no group of its own ("y mas").

**Predictions vs the image (rule 3, `python3 body/image_pass/compare_g9.py --seeds 20`):** at the 45 key-M positions with a settled image letter,
the key's M value agrees at **42 of 45**; the same letters shuffled across the 45 positions, 20 seeds: mean 4.10, max 7, 0 of 20 at or above 42.
SENSE predictions: 40 of 45 vs mean 4.00, max 7, 0 of 20. Misses: 21) (n, read r), L08 )2 (s, read u), 40 (e, read g); SENSE also 44 (m, read y) and
)5 (u+[e], read u).

**Leaf after the pass (`python3 tools/decode_key.py ciphers/na-schonenberg-1678-1716 --check`: "reading up to date", exit 0):** 280 tokens, C 207 /
M 73 / U 0 (was C 184 / M 96); body L01-L14 C 180 / M 72 (was 157 / 95); L18-L19 C 27 / M 1. Of the 72 body M tokens, 56 sit on C-graded codes
whose group carries a transcription-confidence M in ciphertext.tsv (not touched here: the readers were shown the expected group, so their
"group_seen" cannot clear a transcription doubt), 10 on key-M codes (36 x3, )3 x2, 18, 20, 21), 36), 58), 6 on M exceptions.

**Judge re-run (`python3 body/judge_body.py --shuffles 20 --seed 1 --corpora es18,es18p,es17c7,es`, log body/judge_body_gaps9.log):** es18 KEY N=247
-1.137 vs real_p05 -0.957 **FAIL** (GAPS8 -1.175), GLOSS -1.329 FAIL, SENSE -1.140 FAIL (SENSE text not re-segmented); shuffled-null -2.081..-1.882 and
shuffled-target -2.114..-1.885, 0 of 20 PASS each. es18p KEY -1.166 vs -0.959, es17c7 -1.201 vs -0.905, es -1.149 vs -0.904, every control 0 of 20. The
key text still scores above the leaf's own contemporary gloss on every corpus and both FAIL: judge cannot decide at this N (the ZX-DEC349 shape), not
a negative. Pasted (es18 block, verbatim):
```
$ judge_plaintext.py body/spec_body_es18.json --text <KEY>  (exit 1)
  FAIL language: score=-1.137, null_p99=-1.749, real_p05=-0.957, real_median=-0.834, mode=both, N=247
es18: shuffled-null (letters of KEY) n=20 min=-2.081 max=-1.882 mean=-1.952 PASS 0 of 20 (null_p99=-1.749 real_p05=-0.957 at N=247)
es18: shuffled-target (group order within line, key.tsv) n=20 min=-2.114 max=-1.885 mean=-1.968 PASS 0 of 20 (null_p99=-1.749 real_p05=-0.957 at N=247)
```
The regenerated body is a key reading at C/M from the leaf's own period gloss, not a fresh decipherment. Nothing here is a novelty claim (rule 10);
status word unchanged (`partial`); 72 body M tokens remain, so no "reading ready" line from this job.

## GAPS10-na-schonenberg-1678-1716 (2 Oct 2026, account-4)
Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; the Verdict step ("blind group re-read of the 56 transcription-conf-M body positions
(9 vision calls)"), run 21:46-21:5x UTC (container clock). Intake gate exit 0 at the start ("partial (line 1) -- edition/page or full-text-search
citation found within 6 lines"). Disk only, 0 network requests. Vision calls: 9 (3 batches x 2 blind Opus passes + 1 reconciliation look per batch
by this worker over a composite of the doubtful spans).

**Target set.** Every L01-L14 position with ciphertext.tsv conf M: 65 (52 on C-graded codes, 5 on key-M codes, 8 on exceptions); GAPS9's "56" was
a looser count of the same column, and all 56 are inside the 65. Crops: the GAPS7 `tools/iiif_lines.py --image` crops on disk
(images/lines/g7x_L01..L14, boxes in g7x_manifest.json), no new cut needed (all 14 lines present); for pass B, 2x half-line slices of the same crops
(images/lines/g10/g10_L??_a|b.jpg, `convert g7x_LNN.jpg -crop ... -resize 200%`, cipher row only). Readers were given the image(s), the group COUNT
of each line and the starred positions only -- NOT the expected groups, the key, the gloss column or body/sense_inferences.tsv -- and transcribed
every group of the row (batch 1 = L01-L05, batch 2 = L06-L10, batch 3 = L11-L14). Files: body/image_pass/g10_targets.tsv, g10_passA_b1-3.tsv,
g10_passB_b1-3.tsv, g10_settled.tsv, compare_g10.py (+ .log), apply_g10.py, and the *_before_GAPS10.tsv snapshots.

**Pass agreement:** 243 of 245 aligned groups (A vs B, whole rows). At the 65 starred positions: 57 both passes read the committed group, 1 both
read another group, 7 split or did not align (count differences).

**Settled (a position changes only where both blind passes agree against the transcription and the reconciliation look agrees):**
- 56 positions confirmed blind by both passes -> conf H (their tokens go from M to the code's key grade).
- L01 pos6-7: the transcription's `23` and `[blot]` are ONE sign -- both passes see a single blot between 60 and 15 (14 items including the clear
  "Amigo"); reconciliation look: a blot with strokes standing above it, consistent with 23 = n, which "abye[n]do" needs. One position `23` kept at
  conf M (the digits are under the blot); L01 positions 8-13 renumber to 7-12 (no exception or sense row referred to them).
- L02 pos17: `)5` is `) . 5` (both passes and the look: a dot between). `)0 ) 5` = q u e -- the "que" the GLOSS row already had, so the sense
  inference "u+[e]" becomes a key reading (`)` = u C, 5 = e C). L02 now 19 groups; code )5 has no occurrence left.
- L04 pos16-18: `21) 36) 45` is `2) . 36 . ) . 45` (both passes; look agrees): 2) = r (C), 36 = c (key M), `)` = u (C) -- with 33 54 before them,
  z y r c u n | s t a n z y a s = "circunstancias" (sense, this worker's segmentation: an I-grade check, not a witness). The L04 final group is
  45 (pass B) or 95 (pass A): kept 45 at conf M. Codes 21) and 36) have no occurrence left (36) was GAPS9's doubt; it is 36 + )).
- L08 pos15: `2?` -> `26` (both passes; dark retraced ink, possibly a correction). The gloss e exception stays (26 = q elsewhere); conf kept M.
- Not changed, kept M: L09 pos0 (both passes: a large looped L-shaped flourish in darker ink, not a clear 20, perhaps not a group at all; the gloss
  A stands over it); L10 pos0 (both passes: a G-shaped curl followed by a [tilde] where the transcription has `)2`; NULL exception either way, so no
  letter changes).

**Predictions vs the blind reads (rule 3, `python3 body/image_pass/compare_g10.py --seeds 20`):** committed group = settled blind group at 57 of 61
settled starred positions; the same groups shuffled across the 61 positions, 20 seeds: mean 2.70, max 6, 0 of 20 at or above 57. KEY M value vs the
key value of the settled group (non-exception, keyed positions): 53 of 54 vs mean 5.35, max 9, 0 of 20; SENSE predictions: 53 of 54, same control.
The one miss is L04 pos17 (36) read e -> 36 read c).

**Leaf after the pass (`python3 tools/decode_key.py ciphers/na-schonenberg-1678-1716 --check`: "reading up to date", exit 0):** 281 tokens
(L02 +1, L04 +1, L01 -1), C 262 / M 19 / U 0 (was 280: C 207 / M 73); body L01-L14 C 235 / M 18 (was C 180 / M 72); L18-L19 C 27 / M 1. The 18 body
M: 5 conf-M groups left (L01 pos6 blotted 23, L04 pos19 45/95, L08 pos15 retraced 26, L09 pos0 flourish/20, L10 pos0 curl), 8 on key-M codes (36 c x4,
)3 t x2, 18 g, 58 i), and 5 M exceptions (L06 pos17 50 s, L07 pos15 6) n, L10 pos1-2 NULL, L10 pos12 2) r) -- L10 pos0 counted once above.

**Judge re-run (`python3 body/judge_body.py --shuffles 20 --seed 1 --corpora es18,es18p,es17c7,es`, log body/judge_body_gaps10.log):** es18 KEY N=249
-1.117 vs real_p05 -0.975 **FAIL** (GAPS9 -1.137), GLOSS -1.329 FAIL, SENSE -1.140 FAIL (SENSE text not re-segmented); shuffled-null -2.043..-1.905 and
shuffled-target -2.062..-1.851, 0 of 20 PASS each. es18p KEY -1.140 vs -0.959, es17c7 -1.167 vs -0.891, es -1.126 vs -0.901, every control 0 of 20.
The key text scores above the leaf's own contemporary gloss on every corpus and both FAIL: judge cannot decide at this N (the ZX-DEC349 shape),
not a negative. Pasted (es18 block, verbatim):
```
$ judge_plaintext.py body/spec_body_es18.json --text <KEY>  (exit 1)
  FAIL language: score=-1.117, null_p99=-1.735, real_p05=-0.975, real_median=-0.839, mode=both, N=249
es18: shuffled-null (letters of KEY) n=20 min=-2.043 max=-1.905 mean=-1.973 PASS 0 of 20 (null_p99=-1.735 real_p05=-0.975 at N=249)
es18: shuffled-target (group order within line, key.tsv) n=20 min=-2.062 max=-1.851 mean=-1.965 PASS 0 of 20 (null_p99=-1.735 real_p05=-0.975 at N=249)
```
The regenerated body is a key reading at C/M from the leaf's own period gloss, not a fresh decipherment. Nothing here is a novelty claim (rule 10);
status word unchanged (`partial`); 18 body M tokens remain, so no "verifier wanted" line from this job.

## GAPS11-na-schonenberg-1678-1716 (2 Oct 2026, account-4)
Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; the Verdict step ("native-res re-cut + blind pair on the 18 M positions, 3 vision
calls, ~$5"), run 22:03-22:2x UTC (container clock). Intake gate exit 0 at the start ("partial (line 1) -- edition/page or full-text-search
citation found within 6 lines"). Vision calls: 3 (2 blind Opus passes + 1 reconciliation look by this worker over a composite of six crops).
Requests: 2 (`www.nationaalarchief.nl` item page for the IIIF path, `service.archief.nl` info.json), 1.5 s+ apart.

**Native resolution.** The NA IIIF service for this scan (`service.archief.nl/iip/iipsrv?IIIF=11/23/aa/.../fc3a8d42-...jp2/info.json`, path read
from the item page's drupal-settings-json) reports width 1946, height 2618: the file on disk (images/NL-HaNA_1.02.04_63_0001.jpg) is already
the native image, so no image was refetched. Re-cut: `python3 ../../tools/iiif_lines.py --image images/NL-HaNA_1.02.04_63_0001.jpg --region
400,430,1546,1400 --centres 122,449,544,628,736,830,923,1014,1196,1366 --out images/lines/g11 --prefix g11 --groups 8 --group-ink 170
--group-upscale 3 --debug` (centres = each target line's gloss-row ink peak + 58 px; overlay g11_lines_debug.jpg). Its `--groups` split gave
17-26 pieces for lines of 13-20 groups (the dots between groups split pieces; the tool's own unimodal-histogram warning), so the pieces were
deleted and NOT given to readers. Reader crops: gloss+cipher pairs, y = gloss peak -30..+90 px, cut from the native file with PIL beside the
tool's centres (images/lines/g11/g11_manifest.json): set a = halves at 2.4x for pass A, set b = thirds at 3.0x for pass B (60 px overlap),
10 lines (L01, L04-L10, L12, L14). The readers got the crops, each line's group count and the 18 starred positions only. They were not given
the committed groups, the key, the gloss column or the sense file. They transcribed every group of each row and, at each star, the gloss
letter above it.

**Pass agreement** (`python3 body/image_pass/compare_g11.py --seeds 20`, log compare_g11.log): whole-row groups 180 of 181 (any bracketed
symbol counted as one group; the one split is L06 pos16 89/83, not a target). At the stars, the gloss letter agrees at 11 of the 17 letter
positions (L01 pos6 has a numeral in the gloss row, not a letter).

**Settled (body/image_pass/g11_settled.tsv; apply_g11.py, idempotent from the *_before_GAPS11.tsv snapshots).** A position changes only where
both blind passes agree, and also the look where one was taken:
- L01 pos6: the group is under a blot in both passes, but the gloss row over it carries the numeral `23.`, the period decipherer's own recopy
  of the group (both passes). Group 23 is taken from that recopy (conf H), and the value comes from key 23 = n (C). M -> C.
- L04 pos0 18 under gloss g, both passes: code 18 raised to C (single occurrence, image-confirmed; GAPS9 precedent). M -> C.
- L06 pos17 50: both passes read s, the same as GAPS7's two. That makes four blind reads of s against VX-RD01's one r, so the exception is
  raised to C. M -> C.
- L14 pos10 )3: crossed t in both passes and in the look. The committed gloss column had o, which was a one-place slip (o sits over 46). The
  gloss column is corrected to t and a C exception added; key )3 stays M (L05 pos1 splits e/t, look t). M -> C.
- L12 pos2 58: both passes and the look read a tall looped l over 58, where the committed gloss had j. The gloss column and key 58 change
  from i to l; the grade stays M (single occurrence, and the sense wanted c).
- L09 pos0: both passes (and both GAPS10 passes) read an L-shaped looped symbol, not 20. The group becomes `[L]` and a stays by exception at
  M (gloss A in pass A, a flourish in pass B). Code 20 has no occurrence left.
- L10 pos0: both passes (and GAPS10) read a curl/tilde symbol with a dot in its loop, not )2. The group becomes `[curl]`; NULL stays M.
- Held, unchanged, at M:
  - L04 pos19: both passes read 25 under gloss n, but the look reads 45 (GAPS10 read 45 and 95). The first digit is faint in every pass,
    and 25 = p elsewhere, so 45 = n is kept.
  - L05 pos1 )3: gloss e or t.
  - L07 pos15 6): gloss capital N or M.
  - L08 pos15: the retraced 26 was read 2b by one pass and 22 by the other.
  - L10 pos1-2: NULL. A pale superscript 2 sits between them.
  - L10 pos10 36: gloss c or e.
  - L10 pos12 2): gloss r or n.
- Code 36: the gloss over it reads e at L04, c at L06 and e at L14 (both passes each), and splits c/e at L10. In this gloss hand c and e look
  alike, so the image cannot settle the code. It stays M at value c.

**Key-M predictions vs the image (rule 3).** At the 11 positions where both passes agree on the gloss letter, the committed values match it at
8. Control: the same 11 predicted letters shuffled across the positions, 20 seeds, mean 1.15, max 3, 0 of 20 at or above 8. The three misses:
36 at L04 pos17 and L14 pos7 (gloss e, value c) and 58 at L12 pos2 (gloss l, value i). The control can vary on this statistic (it reassigns
letters to positions), so it is a real test.

**Leaf after the pass** (`python3 tools/decode_key.py ciphers/na-schonenberg-1678-1716 --check`: "reading up to date", exit 0): 281 tokens,
C 266 / M 15 / U 0 (GAPS10: C 262 / M 19). Body L01-L14 is C 239 / M 14 (GAPS10: C 235 / M 18); L18-L19 is C 27 / M 1 (unchanged). The 14 body
M are:
- 36 at four positions;
- L04 pos19 45/25, L05 pos1 )3, L07 pos15 6), L08 pos15 26, L09 pos0 [L], L12 pos2 58, L10 pos12 2);
- L10 pos0-2 NULL, and L10 pos10 36 (counted once, under 36).

The judge was not re-run (that is the next step, below). Nothing here is a novelty claim (rule 10); the status word is unchanged (`partial`).
14 body M tokens remain, so this job posts no "verifier wanted" line.

## GAPS12-na-schonenberg-1678-1716 (2 Oct 2026, account-4)
Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; the Verdict step ("re-run body/judge_body.py on the GAPS11-changed body (disk only),
~$1"), then the cheapest disk-only step for code 36. Run 22:22-22:3x UTC (container clock). Intake gate exit 0 at the start ("partial (line 1) --
edition/page or full-text-search citation found within 6 lines"). Vision calls 0; requests 0.

**Judge re-run** (`python3 body/judge_body.py --shuffles 20 --seed 1 --corpora es18,es18p,es17c7,es`, full log body/judge_body_gaps12.log, table
body/judge_body_results.tsv). Language line per text (CLI verbatim), then the controls:

| corpus | KEY (N=249) | GLOSS, leaf's own period gloss (N=246) | SENSE (N=245) | real_p05 (KEY) | shuffled-null PASS | shuffled-target PASS |
|---|---|---|---|---|---|---|
| es18 | -1.114 FAIL | -1.313 FAIL | -1.140 FAIL | -0.975 | 0 of 20 (-2.053..-1.888) | 0 of 20 (-2.079..-1.858) |
| es18p | -1.137 FAIL | -1.308 FAIL | -1.168 FAIL | -0.959 | 0 of 20 (-2.043..-1.886) | 0 of 20 (-2.102..-1.860) |
| es17c7 | -1.160 FAIL | -1.328 FAIL | -1.204 FAIL | -0.891 | 0 of 20 (-2.194..-2.008) | 0 of 20 (-2.278..-2.012) |
| es | -1.126 FAIL | -1.306 FAIL | -1.153 FAIL | -0.901 | 0 of 20 (-2.159..-1.859) | 0 of 20 (-2.188..-1.886) |

GAPS10's es18 KEY was -1.117, so the GAPS11 changes moved it by 0.003. The leaf's own period gloss FAILs on every corpus, and below the candidate.
The shuffled controls sit 0.75-0.95 lower. By the rule 3 period-gloss paragraph this FAIL is "judge cannot decide" at N=249 in this register, not a
negative. No shuffled-target decode PASSes (ARM-C1), so the judge is not voided as a gate; it just cannot license a PASS here. The instrument
stays [retired] for this body (GAPS5).

**Code 36, c or e: context test** (`python3 body/ce36_context.py --seeds 20 --corpus es18`, log body/ce36_context.log). D = log10 P of the
4-grams covering the letter with 36=c minus with 36=e, in the key-regenerated body, all other tokens at their committed values.

| occurrence | context (36 bracketed) | D(c-e) | prefers |
|---|---|---|---|
| L04 pos17 | laszyr[c]unstan | -0.397 | e |
| L06 pos12 | espero[c]onansy | +2.393 | c |
| L10 pos10 | uedano[c]uryrzp | +1.750 | c |
| L14 pos7 | sobres[c]rytoen | -1.564 | e |

- Target: sum D +2.181; 2 of 4 occurrences prefer c.
- Control (a), shuffled assignment over 20 seeds (the same c-vs-e swap at 4 random C-graded body positions): sum D runs -12.325 to +8.017, mean
  -3.125. 2 of 20 seeds sit at or above the target. Prefer-c count mean 1.65, max 3.
- Control (b), known answer (every C-graded body c or e swapped): the true letter is preferred 35 of 38 times (0.921). The classes are unbalanced:
  true c 2/2, true e 33/36. So the instrument's power to pick c at a single position rests on only two tokens (the AX-NAMES per-class caution).
- es17c7 gives the same shape: sum D +0.371, 3 of 20 seeds at or above, known answer 36/38.

The target does not beat control (a). The 4-gram model splits 2/2 on the four words, while the sense reading ("circunstancias", "con", "ocurrir",
"escrito") wants c at all four. Code 36 stays M at value c. The test can vary on its statistic, since each seed moves the swap to different
neighbours, so it is a real test that did not discriminate. It is not a non-test. A different instrument is untried: a word-level dictionary test,
each occurrence's whole word with c and with e looked up in the es18 word list, against the same shuffled control.

**Leaf after the step** (`python3 tools/decode_key.py ciphers/na-schonenberg-1678-1716 --check`: "reading up to date", exit 0): 281 tokens, C 266 /
M 15 / U 0; body L01-L14 C 239 / M 14, unchanged (no reading change). Body M is 14, not 0, so this job posts no "verifier wanted" line. Nothing here
is a novelty claim (rule 10); the status word is unchanged (`partial`).

## GAPS13-na-schonenberg-1678-1716 (2 Oct 2026, account-4)
Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`. Verdict step from GAPS12: "word-level dictionary test for 36, disk only". Run 22:39-22:4x UTC (container clock). Intake gate exit 0 at the start ("partial (line 1) -- edition/page or full-text-search citation found within 6 lines"). Vision calls 0, requests 0.

**Instrument** (`python3 body/ce36_dict.py --seeds 20`, log body/ce36_dict.log). The word list is 27,593 folded types seen at least twice in tools/data/es18 (7 files, 1690-1725) and es17c (3 files, 1640s). One orthographic fold is applied identically to the list and to both readings: accents folded, h dropped, y->i, v/b->u, z->c, j->x, doubled letters collapsed. The body words come from the key-regenerated body, cut at word boundaries that were written once, before the run, and are the same under c and e. The gate was registered in the script's docstring before the run: S for c only if the target beats the max of control (b), reaches the p95 of control (a), and the known answer scores at least 0.8 with at least half its positions decisive and no class wrong-majority.

| occurrence | word with c (freq) | word with e (freq) | verdict |
|---|---|---|---|
| L04 pos17 | zyrcunstanzyas (45) | zyreunstanzyas (0) | c-only |
| L06 pos12 | con (13557) | eon (17, OCR debris) | both |
| L10 pos10 | ocuryr (7) | oeuryr (0) | c-only |
| L14 pos7 | sobrescryto (2) | sobreseryto (0) | c-only |

- Target: 3 of 4 occurrences c-only; e-only 0.
- Control (a), label shuffle over 20 seeds: c/e is redrawn per occurrence. A plain permutation of an all-c prediction cannot change the score, so it would be rule 3's orthogonal non-test. Score min 0, max 3, mean 1.45, p95 2; 1 of 20 seeds at or above the target.
- Control (b), position shuffle over 20 seeds: the same word test at 4 random C-graded body positions. c-only count min 0, max 2, mean 0.20; 0 of 20 at or above the target.
- Control (c), known answer: the 38 C-graded body c/e tokens, the same set GAPS12 used. 15 are decisive, 15 right and 0 wrong (1.000). By class: true c 1 right + 1 both; true e 14 right, 17 both, 5 neither.

**Result:** the test does not clear its pre-registered gate, so code 36 stays M at c. The target does beat both shuffles (3 vs (a) p95 2, and vs (b) max 2). The known answer is never wrong, but only 15 of 38 positions are decisive (0.39, under the registered half). The true-c class rests on one decisive token, the same per-class weakness GAPS12 found. All four words fit c, or fit both letters; e is never the only dictionary word. That agrees with the sense reading, but by rule 3 it is not grade S. The gate is not relaxed after the run. This is a real test that fell short on power, not a non-test, since each control can and does vary on the score. With the 4-gram test (GAPS12), two disk instruments have now been tried on 36. No third disk-only instrument is known that does not reuse the same body text, so the next step is an image step (Verdict below).

**Leaf after the step** (`python3 tools/decode_key.py ciphers/na-schonenberg-1678-1716 --check`: "reading up to date", exit 0): 281 tokens, H 0 / C 266 / S 0 / M 15 / I 0 / U 0. Body L01-L14: C 239 / M 14, unchanged (no reading change). Nothing here is a novelty claim (rule 10). Status word unchanged (`partial`).

## GAPS14-na-schonenberg-1678-1716 (2 Oct 2026, account-4)
Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`. Verdict step from GAPS13: "gloss-hand letterform comparison for 36 (3 vision calls)". Run 22:57-23:1x UTC (container clock). Intake gate exit 0 at the start ("partial (line 1) -- edition/page or full-text-search citation found within 6 lines"). Requests 0 (disk image only).

**Instrument** (body/letterform/). The crop command was run first, as the brief requires: `python3 tools/iiif_lines.py --image ciphers/na-schonenberg-1678-1716/images/NL-HaNA_1.02.04_63_0001.jpg --out <scratch>/lines --region 440,439,1460,1366 --prefix g14 --ink 90 --centres 100,200,290,380,470,560,660,750,850,940,1030,1120,1210,1300 --dry-run`, which gave 14 lines and 14 bands. Its row bands cannot isolate single gloss letters, so a column-blob segmenter was tried next (body/letterform/segment.py). It did not work: the gloss letters touch or fade below the ink threshold, and an overlay check showed boxes off the letters. The tile boxes were therefore set by eye on ruled zoom strips (body/letterform/tiles_boxes.tsv, native px). Each box sits on the gloss letter standing over the named group. There are 14 boxes:
- the 4 occurrences of code 36;
- the only 2 C-graded c tokens in the body (code 14, L04 pos8 and L09 pos5);
- 8 C-graded e tokens (codes 60, 38, 5, 16 and 10, in L03-L14).

Three e boxes were re-centred by 12 px after a look at the first sheet; the tile order and contents were unchanged. make_sheet.py (seed 14) cut fixed 56x48 px windows at 3x, numbered them in random order and printed no label. The tile key stayed out of the repository until both sorts were in. The gate was registered in body/letterform/PREREG.md and pushed before any pass (commit 9abe5b16):
- known-answer accuracy at least 0.90;
- c class 2/2;
- accuracy above the p95 of a 20-seed label shuffle;
- all four 36 tiles in one group.

**Passes.** Two blind Opus 5.5 subagent calls each saw only the sheet. Each was told the tiles hold one of two letters in unequal numbers and was asked to sort them into A/B by letterform. The two sorts agree on 14 of 14 tiles (passA.tsv, passB.tsv). With no split left to settle, no reconciliation call was made: recon.tsv is the agreed sort, and 2 of the 3 allowed vision calls were used. Both passes give the same deciding feature. Group A has a closed eye at the top with a long tail. Group B has no eye: a filled blob or hooked head on an open c-curve.

**Score** (`python3 body/letterform/score.py`, score.log):
- Group A holds all 8 known e's, so A is the e group.
- Known-answer accuracy is 1.000: c 2/2, e 8/8.
- Label-shuffle control, 20 seeds: mean 0.680, p95 0.800, max 1.000. One seed of 20 reaches the target, because with 2 c's among 10 tiles a permutation sometimes reproduces the same split.
- The tiles over 36 at L04, L06, L10 and L14 all fall in group B with the two known c's.

**Gate: PASS**, so 36 = c at C. This agrees with the sense reading (L04 circunstancias, L06 con, L10 ocurrir, L14 sobrescrito) and with the GAPS13 dictionary test (3 of 4 c-only, 0 e-only). Stated in advance: the c class rests on two reference tiles, so the pass is narrow. The tile boxes were placed by a worker who knew the labels; only the sorting was blind. The earlier image passes (GAPS11) read the gloss over 36 as e, c, e and c/e. This test explains why: at the letter level the 36 glosses are the eyeless hooked form that this hand uses for c, while its e closes an eye. A reader expecting a word sees an e in that hooked form.

**Leaf after the step** (key.tsv 36 -> C, old key in body/image_pass/key_before_GAPS14.tsv; `python3 tools/decode_key.py ciphers/na-schonenberg-1678-1716 --check`: "reading up to date", exit 0): 281 tokens, H 0 / C 270 / S 0 / M 11 / I 0 / U 0. Body L01-L14: C 243 / M 10, and the reading text is unchanged (36 was already c at M). The body is not yet at 0 M. Nothing here is a novelty claim (rule 10). Status word unchanged (`partial`).

## Remaining gaps (finish-or-blocker pass, 1 Oct 2026; updated GAPS, GAPS2, GAPS4, GAPS5, GAPS7, GAPS8, GAPS9, GAPS10, GAPS11, GAPS12, GAPS13 and GAPS14 2 Oct 2026)
Read so far: 279 of 279 cipher groups (100%) carry a value: 251 body groups under the leaf's own period gloss (L01-L14, ciphertext.tsv, re-aligned to the groups 2 Oct 2026 by tools/interlinear_align.py, align/), L18's 5 under its own gloss "forma." (found 2 Oct 2026), L19's 23 under the address crib with controls (15/16 resolved agree); by grade the leaf is C 136 / M 127 / U 16 (reading_tokens.tsv, GAPS2 2 Oct 2026; was 99/142/38), L18-L19 alone C 21 / M 7 / U 0. Read-as-sense is still unmeasured for the body: the gloss has never been segmented into Spanish words ("Letter's gist" is M-grade).
Resolved 2 Oct 2026 (GAPS-na-schonenberg-1678-1716): the L18-L19 gap -- "forma." is L18's own interlinear gloss (layout, image check), L19 = "a doña antonya de albanylla" against the address (crib_align.py, slid-window and shuffled-crib controls both at 0 of 229 / 0 of 2000 at or above target), decode_key.py --check exit 0; 65 and 8) logged as conflicts (conflicts.tsv, HYPOTHESES.md H1).
Resolved 2 Oct 2026 (GAPS2-na-schonenberg-1678-1716): the L01-L14 code-to-gloss alignment -- tools/interlinear_align.py on passB's own gloss letters (align/), R2 agreement 0.699 and 44 C-bar codes vs a within-line shuffled-gloss control max 0.301 / 11 (n=300, 0 at or above target); key.tsv rebuilt (C 40 / M 43 / U 6), 24, 51, 65 raised to C, 34 and 11 held at M, 50 = s at M against the pixel-verified L06 r (exceptions.tsv); decode_key.py --check exit 0; 88 of 256 tokens re-attached, all in the lines passB flagged plus L02.
Resolved 2 Oct 2026 (GAPS7-na-schonenberg-1678-1716): the 12 unsettled codes, image pass on 12 body lines (4 batches x 2 blind Opus passes + 1 reconciliation, 9 vision calls): 23 n, 14 c, 55 z, 50 s, 34 a, 49 r, 11 a, 31 x, 8) l, [blot] NULL all C; 96 o/y C per position; )52 is )2 + 38; seven transcription errors corrected (L03 5) and 3), L08 2?, L09 2), 8), ) 10, L12 )2 38); sense predictions 10/11 agree vs shuffled 20 seeds mean 1.50 max 4; leaf C 171 / M 109 / U 0; decode_key --check exit 0.
Resolved 2 Oct 2026 (GAPS8-na-schonenberg-1678-1716), part of the body-M gap: judge re-run on the changed body (es18 KEY -1.175 vs real_p05 -0.957 FAIL, was -1.445; 0/20 + 0/20 controls PASS on four corpora; judge cannot decide, not a negative); image pass on L05, L07, L10, L03, L12, L14 (6 vision calls, pass agreement 101/108): 15 codes to C incl. )2 = s and )4 = u, L07 pos10 = 2) not 23; key M predictions 49/56 vs shuffled mean 5.45 max 10; leaf C 184 / M 96; decode_key --check exit 0.
Resolved 2 Oct 2026 (GAPS9-na-schonenberg-1678-1716), the key-M part of the body-M gap: image pass on the 45 M positions of L01, L02, L04, L06, L08, L09, L11, L13 (9 vision calls, 116/135 pass agreement): 15, 28, 5, 26, 33, 82, )0, )5, 44, 66, [T] to C, 40 = g (C), 21) = r (M), L08 )2 = u (C); key M predictions 42/45 vs shuffled mean 4.10 max 7; leaf C 207 / M 73; judge es18 KEY -1.137 vs real_p05 -0.957 FAIL, 0/20 + 0/20 controls (judge cannot decide); decode_key --check exit 0.
Resolved 2 Oct 2026 (GAPS10-na-schonenberg-1678-1716), the transcription-confidence part of the body-M gap: blind group re-read of the 65 conf-M body positions (readers not shown the expected groups; 9 vision calls, 243/245 pass agreement): 56 confirmed (conf H), L01 23+[blot] = one blotted 23, L02 )5 = ) 5 ("que"), L04 21) 36) = 2) 36 ) ("circunstancias"), L08 2? = 26; groups 57/61 vs shuffled mean 2.70 max 6, key M predictions 53/54 vs mean 5.35 max 9 (0/20 each); leaf C 262 / M 19 (281 tokens); judge es18 KEY -1.117 vs real_p05 -0.975 FAIL, 0/20 + 0/20 controls (judge cannot decide); decode_key --check exit 0.
Resolved 2 Oct 2026 (GAPS11-na-schonenberg-1678-1716), the image part of the body-M gap: a native-resolution blind pair on the 18 body M positions (the disk file is the native 1946x2618 image per IIIF info.json; 3 vision calls; groups 180/181, gloss letter 11/17 agree). L01 pos6 = 23 by the gloss row's own recopy, 18 = g, L06 50 = s, and L14 )3 = t (gloss column slip o -> t) all rise to C. 58 now reads l (M); L09 pos0 and L10 pos0 are symbols, not 20 or )2. Key-M predictions 8/11 vs shuffled mean 1.15, max 3 (0/20). Leaf C 266 / M 15, body C 239 / M 14; decode_key --check exit 0.
Resolved 2 Oct 2026 (GAPS12-na-schonenberg-1678-1716), the judge on the GAPS11-changed body: es18 KEY -1.114 vs real_p05 -0.975 FAIL (was -1.117), the leaf's own gloss -1.313 FAILs below it, 0/20 shuffled-null and 0/20 shuffled-target PASS on es18, es18p, es17c7 and es (body/judge_body_gaps12.log): judge cannot decide, not a negative.
Resolved 2 Oct 2026 (GAPS14-na-schonenberg-1678-1716): code 36 (L04 pos17, L06 pos12, L10 pos10, L14 pos7), the last open code. The disk tests had fallen short: the 4-gram test GAPS12 did not beat its control, and the dictionary test GAPS13 found 3 of 4 c-only but its known answer was decisive on only 15 of 38. A gloss-hand letterform test then put 14 value-blind tiles before 2 blind Opus sorts, which agree 14/14. The known answer scores 10/10 (c 2/2, e 8/8) against a 20-seed label shuffle with p95 0.800, and all 4 tiles over 36 sort with the known c's. The pre-registered gate passes, so 36 = c at C. Leaf C 270 / M 11, body C 243 / M 10; decode_key --check exit 0.
- Body M, 7 doubtful groups or split gloss letters (L04 pos19 45/25 faint, L05 pos1 )3 e/t, L07 pos15 6) N/M, L08 pos15 retraced 26, L09 pos0 [L] symbol, L10 pos12 2) r/n, L12 pos2 58 l vs sense c) - blocker: illegible; the native-resolution blind pair plus the look (GAPS11, body/image_pass/g11_settled.tsv) split or held at each. This was the fifth image pass and the first at native scale; no higher resolution exists (IIIF info.json 1946x2618)
- Body M, L10 pos0-2 NULL (3 tokens) - blocker: no-key-material; no gloss letter over the line-start groups in any blind pass (GAPS7, GAPS8, GAPS10, GAPS11)
Resolved 2 Oct 2026 (GAPS4-na-schonenberg-1678-1716): body plaintext L01-L14 segmented and expanded as Spanish (body/reading_body.txt, KEY/GLOSS/SENSE per line; SENSE grades C 115 / M 120 / I 18, inferences in body/sense_inferences.tsv) and judged with controls on the two nearest corpora (es17c7, 1634-1648 letters, 55-80 years off; es = es17 fiction): KEY -1.482 / GLOSS -1.346 / SENSE -1.204 vs real_p05 -0.903/-0.922 FAIL on es17c7, 20 shuffled nulls -2.266..-1.985 and 20 shuffled targets -2.263..-1.838 all 0 PASS; the leaf's own gloss FAILs too, so "judge cannot decide" at this N and register (not a negative); the body reads as a cover-address instruction ending "...pondra solamente en sobre escrito en esta forma: a doña antonya de albanylla", corroborating L19 from the body's own sense (M). Unread spans: L04-L05 "zynenstanzyas", L05-L06 "que ay sera bran mexores pe no con anrya", L08-L09 "pues [23]saran de o[14]as yo[23]a[23]a".
Resolved 2 Oct 2026 (GAPS5-na-schonenberg-1678-1716) as far as this instrument goes: tools/data/es18 built (7 items, 1690-1725, 2.54M letters, fold check at N=245 36.1% blended, spread 0.0-79.0% -- unknown reliability by rule 3) and body/judge_body.py re-run on it beside es17c7 and es: SENSE -1.140 vs real_p05 -0.962 FAIL (gap 0.178, was 0.282), the leaf's own gloss -1.352 FAILs below the candidate, 0/20 shuffled-null and 0/20 shuffled-target PASS. Judge cannot decide at this N on any of three corpora; [retired] instrument tools/judge_plaintext.py at N=245 for this body (rule 3 third-attempt clause: es, es17c7, es18), not a negative; reopened only by new material or a changed text (the image pass).

## Escalation (1 Oct 2026; updated GAPS and GAPS2 2 Oct 2026)
- [x] siblings: NA 1.02.04 finding aid (26 pages, ~152 invnrs) grepped for cijfer/cijferschrift/geheimschrift/chiffre/sleutel: invnr 63 is the only cipher-flagged item (NOTES "Sibling inventory"); DECODE dumps of 24 Sept 2026 have no row for it; the nearest same-writer cipher, HU3 (Schonenberg to Heinsius no. 185, 1709, NA 3.01.19 invnr 1445, one cipher word, unsolved), is another correspondent and office, not this key. Optional, unrun: an eye-check of the other digitised 1.02.04 scans for cipher the cataloguer did not flag; and NA 3.01.19's undigitised "Stukken betreffende cijfers en sleutels van cijferschrift" (web search, 2 Oct 2026), official cipher material, probably not this private key.
- [x] clear-pages: done 2 Oct 2026 (GAPS): "forma." is L18's own gloss by layout; the address is L19's crib, 15/16 resolved positions agree against slid-window (max 0.286, n=229) and shuffled-crib (max 0.438, n=2000) controls; 28/28 closing tokens valued (C 15 M 13); conflicts 65 and 8) logged. No other clear text on the leaf is unused ("Amigo.", "Aquy", "&a" are single words already in clear).
- [x] known-keys: KEY-CROSSMATCH.tsv ran every key on file against ciphertext.tsv: only this target's own key fits (line 144, coverage 0.989); the best outside key, fr5160-letellier key_1659_ext, reaches 0.527 and does not pass (line 465); KEY-DESIGN.tsv records the design (homophonic, 87 codes); the key source is the leaf's own period gloss, so no outside key book is needed; Cryptiana/Cipherbrain nothing found (check-solved; web/blog check 2 Oct 2026, 0 hits).
- [x] print: check-solved 25 Sept 2026, six sources: IA full text "Schonenberg brieven" 0 hits; Heinsius Briefwisseling (Huygens retroboeken) Schonenberg 413 hits, none relevant, Albanilla/Albanylla 0; 8 web queries, DECODE dumps, both solver repositories; web and blog check 2 Oct 2026 (10 queries, three blogs, 0 hits). Not read: two Utrecht theses on Schonenberg (dspace.library.uu.nl and studenttheses.uu.nl, both HTTP 403 from the cloud), background only.
- [x] key-rebuild: done 2 Oct 2026 (GAPS2): tools/interlinear_align.py on L01-L14 + L18, three runs (unseeded, C-seeded, C+crib-seeded), R2 agreement 0.699 / 44 C-bar codes vs within-line shuffled-gloss control max 0.301 / 11 (n=300); key.tsv rebuilt from the tallies with the rule in align/rebuild_key.py (C 40 / M 43 / U 6; leaf tokens C 136 / M 127 / U 16); the earlier plurality tally is kept as align/key_before_2026-10-02.tsv. Nothing further for an aligner to do without new letters from the image.
- [x] image-check: done (GAPS7-GAPS11); history: L06 pixel-verified 20/20 (25 Sept); L18-L19 at 4x (25 Sept); the L14-to-address layout at native resolution plus L19's blot and second row at 2x (2 Oct, GAPS). Not checked: the 12 codes the aligner leaves unsettled (gap 2 above: 6 U, 5 conflict, 8) p-vs-l) and passB's tick doubts. Planned: one line crop per subagent call for the 11 lines named in gap 2, gloss letter over the named groups only, ~$18. GAPS7 (2 Oct 2026): done for the 12 codes (L01-L04, L06, L08-L14, two blind passes + reconciliation, 9 vision calls; all 12 settled, 7 transcription errors corrected). Not checked: L05, L07, the remaining M codes; L04 pos16-17 and L10 pos0-2 group doubts. GAPS8 (2 Oct 2026): L05, L07, L10, L03, L12, L14 M positions done (6 vision calls, 15 codes to C); L10 pos0-2 confirmed to carry no gloss letter (NULL M). GAPS9 (2 Oct 2026): the M positions of L01, L02, L04, L06, L08, L09, L11, L13 done (9 vision calls, 12 codes to C, 40 = g, 21) = r M). GAPS10 (2 Oct 2026): the 65 transcription-confidence M groups re-read blind without the expected sequence (9 vision calls): 56 confirmed, 4 structural/group corrections (L01, L02, L04 incl. 36) = 36 + ), L08), 5 unsettled. GAPS11 (2 Oct 2026): the 18 remaining body M positions re-cut at native scale (the disk image is native) and read by a blind pair + look (3 vision calls): 4 to C, 2 group corrections (symbols), 1 gloss correction (58 l), the rest at the image's limit.
- [x] retry: done for L18-L19 (tools/decode_key.py --check exit 0 after the crib, 2 Oct 2026) and for the body after the aligner (--check exit 0, regraded: 38 U -> 16, GAPS2 2 Oct 2026; the closing-line judge re-run FAILs as before, 0 of 20 shuffled targets PASS). Body judged as Spanish 2 Oct 2026 (GAPS4): KEY/GLOSS/SENSE all FAIL real_p05 on es17c7 and es while 40 shuffled controls per corpus all sit 0.35-0.6 lower, 0 PASS; the leaf's own gloss FAILs too, so the judge cannot decide at this N (body/judge_body.log). Not yet: the same judge on an era-matched es18 corpus (gap 3, ~$3). GAPS5 (2 Oct 2026): re-judged on the era-matched es18 (SENSE -1.140 vs real_p05 -0.962, gloss -1.352, 0/20 + 0/20 controls PASS): same shape on a third corpus, judge retired as the instrument for this body at N=245; the retry that remains is the image pass.
Gate repair (GAPS6, 2 Oct 2026): tools/intake_gate_check.py exited 1 at 14:19 UTC ("no standard-edition citation ... within 6 lines" -- the GAPS paragraphs added above the status word on 2 Oct had pushed the 25 Sept citation from line 6 to line 8, and the 13:38 UTC head-only change reads only 6 lines past the status word); the citation is carried up to line 2 unchanged in substance, the "## Premise check" section is written at the end of this file (verdict: clear to test), and the gate now exits 0. The Verdict step below is unchanged and still unrun.
Retry updated 2 Oct 2026 (GAPS14): after 36 rose to C, decode_key --check exits 0 (reading text unchanged). The judge stays [retired] for this body at N=245 (GAPS5), and the image is read to its native limit (GAPS11), so the retry has nothing left to run.
Verdict: parked: every gap has an outside blocker (7 illegible groups at the native image's limit, 3 line-start NULLs with no key material); code 36 resolved to c at C by GAPS14. Reopened only by new material: a second Schonenberg letter in this key, or a higher-resolution scan of NA 1.02.04 inv.63. Body C 243 / M 10; the reading awaits a separate verifier's re-derivation and novelty audit (rules 7 and 10).

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

## Premise check (GAPS6-na-schonenberg-1678-1716, 2 Oct 2026)
The adversarial pre-reading pass of `.claude/briefs/check-solved.md` ("Premise check", 2 Oct 2026), run 14:19-14:3x UTC 2 Oct 2026, asked to prove the item is already done. Each of (a)-(d) as found / not found / unreachable; this pass is a search result, not a novelty verdict (rule 10). It is written after the folder's earlier reading work (VX-RD01 25 Sept; GAPS-GAPS5 2 Oct), so "before any first test" here means before the image pass the Verdict line names.
(a) Decipherments, glosses and clear copies the folder itself mentions -- all opened: (1) the leaf's own interlinear gloss over L01-L14 (passA.tsv/passB.tsv, reading.txt, align/): a contemporary letter-by-letter Spanish decipherment of 251 of the 279 groups in a smaller hand on the same leaf -- it IS a period decipherment of the body, already the folder's H/C-grade key source since 25 Sept 2026, and is NOT a clear copy or a translation (it stops before L18-L19, is unsegmented into words, and leaves 12 codes unsettled; the body as Spanish sense is M-grade, GAPS4). (2) "forma." over L18's five groups (image check, GAPS 2 Oct): the gloss hand's one word on the closing lines, not a copy. (3) The clear address at the foot, "A Doña Antonija de Albanylla &a." (passB_summary.txt): the recipient's name in clear, used as L19's crib (15/16 positions vs controls, crib_align.py); it is the addressee line of the draft, not a decipherment of anything. (4) The marginal "Aquy" and the opening "Amigo." are single clear words. (5) HU3 (Schonenberg to Heinsius, 24 Jul 1709, NA 3.01.19 invnr 1445, one unsolved cipher word; sources/huygens/NOTES.md): another correspondent, office and archive; not opened as an image (undigitised), no decipherment of this leaf there. (6) The web-check lead "Stukken betreffende cijfers en sleutels van cijferschrift" in NA 3.01.19 (Heinsius, official cipher keys): undigitised, not opened -- unreachable from the cloud, and official rather than this private key. (7) The two Utrecht theses on Schonenberg's diplomacy (dspace.library.uu.nl, studenttheses.uu.nl): HTTP 403 on 2 Oct 2026 (GAPS web check), not retried this pass -- unreachable; search snippets show no cipher content. Verdict (a): found only what the folder already uses (the leaf's own partial gloss and its clear address); no further decipherment, clear copy or translation of this item mentioned anywhere in NOTES.md, HYPOTHESES.md or the images manifest.
(b) Other solvers' working files: fresh shallow clones of github.com/dbourdeau/cyphersolver and github.com/aaymeloglu/unsolved-ciphers (2 requests, 14:2x UTC), grepped case-insensitively for schonenberg / albanilla / albanylla / "1.02.04" across every file (targets, docs, research harvests, decode queue, papers, catalogue). Every hit (cyphersolver README.md, docs/search.json, docs/index.html, targets/roell1809 and dedem1788 NOTES.md and profile.json, decode_updates/queue.json, research/catalogue_harvest/decode/batch_6.json, papers/lasry/classification_review.csv; unsolved-ciphers catalogue/decode-catalog.csv rows 1469-1470) is the Roell-to-Van Dedem 1809 pair, which DECODE mislabels "NA 1.02.04 legatie Turkije inv. 804" (Bourdeau's own note: 1.02.04 is Schonenberg's Portugal legation, the Turkey legation is 1.02.20). Neither repository has a target, rendering, apply-key script or key for invnr 63 or for any Schonenberg item; no key of theirs has been run on this text (KEY-CROSSMATCH.tsv already shows no outside key on file fits). The on-disk snapshots sources/cyphersolver/2026-10-02 and sources/unsolved-ciphers/2026-10-02 (partial, other targets) and sources/decode/records-*-2026-09-24.tsv carry nothing for this item either. Verdict (b): not found.
(c) Physical neighbours in the NA inventory: invnr 63 is a single recto leaf (1 scan, DIGITALIZED; images/manifest.json), so there is no verso or second canvas to carry a clear copy. The six neighbouring inventory numbers in the same run "Minuten van uitgaande brieven aan overige correspondenten" were read through the item pages' embedded drupal-settings-json viewer.response (www.nationaalarchief.nl/onderzoeken/archief/1.02.04/invnr/N, 6 requests 1.6 s apart, all HTTP 200): 58 "Aan P.J. van Borssele van der Hooghe, buitengewoon gezant bij de Engelse legatie, 1714-1715." PHYSICAL, 0 scans; 59 "Aan Diego de Mendoca Corte Real, Portugees secretaris van Staat, 1706-1716." PHYSICAL, 0 scans; 60 "Aan Lord Nottingham (Daniël Finch) en Alexander Stanhope, Engelse secretarissen van Staat, 1702, 1714." PHYSICAL, 0 scans; 61 "Aan Lord Portmore (David Colyear), luitenant-generaal, 1713-1715." PHYSICAL, 0 scans; 62 "Aan Pieter du Feu, 1706." PHYSICAL, 0 scans; 64 "Aan N.N., 1702-1703, z.d." PHYSICAL, 0 scans. None is digitised, so none can be eye-checked from the cloud for a clear copy or decipherment bound beside invnr 63; the finding aid flags none of them "in cijferschrift" (Sibling inventory above). Lead, not a find: invnr 64, drafts to an unnamed correspondent, 1702-1703 and undated, physical only -- the one neighbour whose addressee is not a named official, so the one place a second letter to the same private correspondent could sit; a reading-room check or a scan order (REQUEST.md, the owner) would settle it. Verdict (c): not found in what the cloud can read; neighbours unreachable (undigitised).
(d) The recipient's side. Dutch state series: the Staten-Generaal resolutions edition on Huygens retroboeken covers 1576-1625 only (its own volume list, read this pass), so it cannot carry a 1678-1716 item; searched for `Schonenberg` anyway, 0 hits. Correspondentie Willem III en Bentinck (retroboeken/willemiii, 5 vols) full-text: `Schonenberg` 11 hits, all his official letters to Willem III and Portland from Madrid in the 1690s (KS 23 pp. 272, 286; KS 24 pp. 222-255, index pp. 766-792; KS 27 p. 356) -- none this letter, none a cipher; `Albanilla` 0, `Albanylla` 0. Briefwisseling Heinsius (retroboeken/heinsius, 19 vols), beyond the 25 Sept searches (`Schonenberg` 413, `Albanilla` 0, `Albanylla` 0): spelling variants `Alvanilla` 0, `Albanella` 0, `Albanil` 0 (the index's nearest tokens are "albani", "bangil" -- noise). 7 Huygens requests, 2.2 s apart, all HTTP 200. Spanish side: the Estado series at PARES is a dead host from the cloud (CLAUDE.md host table), so the cached PARES sweep in aaymeloglu/unsolved-ciphers (catalogue/pares-hits/pages/images.jsonl, 2152 rows) was grepped for albanilla / albanylla / schonenberg / belmonte: 0 rows. Google Books API (country=US, keyed): `Schonenberg Albanilla OR Albanylla Lisboa OR Madrid` totalItems 0; the quoted-name query `"Antonia de Albanilla" OR "Antonia de Albanylla"` answered HTTP 503 twice (one retry after a pause, per the good-citizen rule) -- unreachable this pass, not a negative. Verdict (d): not found in the Dutch editions reachable from the cloud; Spanish Estado unreachable beyond the cached sweep (0 rows); one Google Books query unreachable.
Premise verdict: no prior decipherment, clear copy or printed plaintext of NA 1.02.04 invnr 63 located by this pass beyond the leaf's own partial interlinear gloss already in the folder -- CLEAR TO TEST (the image pass on the 12 unsettled codes, the Verdict line of "## Remaining gaps"). Nothing here changes the status word (`partial`), the key, the reading or the Verdict step. Requests per host this pass: github.com 2 (clones), www.nationaalarchief.nl 6, resources.huygens.knaw.nl 7, www.googleapis.com 3 (one 200, two 503), service.archief.nl 0; 0 vision calls.

## Verifier (VERIFY-SCHONENBERG, account-4, 2 Oct 2026)
AUDIT.md written: body L01-L14 and L18 **N0** (the leaf's own interlinear period decipherment; key `period`), L19 **N2** (plaintext = the clear address on the same leaf; the code-to-address mapping is `ours`); leaf N0, no SECOND-OPINIONS row (below N3). Rule-7 re-derivation by a fresh session: decode_key --check exit 0 and an independent re-application of key.tsv + exceptions.tsv agree at all 281 tokens (0 differences beyond the M-graded tokens). Correction (no text deleted): the VX-RD01 section's "L18 and L19 ... no gloss on the leaf" and its 19-letter judge "PASS" are superseded by the GAPS sections (L18 glossed "forma."; the 28-letter closing string FAILs); reading.txt's header ("U = code never seen", "L18-L19 carry NO gloss") is stale decode.json text, for the solver to regenerate. Unreached: Herrero Sánchez, *Hispania* 76/253 (2016) 445-472 (TLS failure from the cloud), and the 2016 Utrecht thesis (403).

## While waiting (RUN4-WAITBF, 4 Oct 2026)

Nothing depends on anyone: the Verdict is parked -- 7 groups illegible at the native image's limit and 3 line-start NULLs with no key material; reopened only by new material (a second Schonenberg letter in this key, or a higher-resolution scan of NA 1.02.04 inv.63). The verifier's re-derivation and AUDIT.md are already on disk (rederivation_report.md, AUDIT.md).

## Verifier, Audit 2 (D2B-SCHON, account 2, 5 Oct 2026)
AUDIT.md "## AUDIT 2" confirms the classes: body/L18 N0 (period plaintext on the leaf), L19 N2, leaf N0. Depth is recounted to D3,
97.1% C (269/277; nulls excluded, was 96.1%). The three Utrecht Schonenberg theses (2012, 2015, 2016) were read in full by
script and carry no Albanilla and no cipher; the Hispania 2016 full text is still unreachable (TLS). The status word is unchanged.
