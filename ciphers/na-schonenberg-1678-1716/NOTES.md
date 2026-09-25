partial
VX-RD01, 25 Sept 2026: the leaf's own period gloss transcribed for L01-L14 (H-grade key source per rule 4); the
two unglossed closing lines (L18-L19) partially decoded from a key built off that gloss, mostly grade M/U -- see
"Reading (VX-RD01, 25 Sept 2026)" below. check-solved's own verdict (unchanged, this worker did not repeat it):
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
