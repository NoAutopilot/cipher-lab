# PREREG-MQS-NAMES -- gates for tools/name_candidates.py's known-answer controls (pushed before any control is scored)

Written 9 Oct 2026, 03:2x UTC (date -u), by MQS-NAMES (LANE MQS, account 4), before
`tools/tests/mqs_names_control_a.py score` or any control (b) run. Brief: `.claude/briefs/runs/2026-10-09-acct3-mqs-names.md`.

## Frozen inputs (sha256)

| file | sha256 |
|---|---|
| tools/data/name_cues_fr.tsv | 03712cd32f3f64bd075cdb3976eb31da925d30992cb8e28025b2a7f4d8ef5182 |
| tools/data/name_cues_de.tsv | 8e8f538a386461efd2e0f57a39e3de774723dfcfd40285e86e841f9496fc83f7 |
| tools/data/name_cues_en.tsv | 7e2003b5f10bc6ca9e73e774fb2db70d69353a72fcfa421bb337bc2ec9dcac3f |
| fixtures/name_candidates/lodewijk/pool_202.tsv | b77b821dcbcf1a97cadabb797164802925ecb258f1df4dd080a419d05e350151 |
| pool_223.tsv = pool_241.tsv (mask 5810) | 2111e9ee382ab55acafd9831c592dacc34f37113f1e281d732a1a3408a24cb74 |
| pool_153.tsv (mask 5549,5550,5797) | f33a4e8fef9f901a04695a501655e83d2efa7a8ae1ad7e14db68993bf90d4372 |
| pool_154 = pool_161 = pool_200 (mask 5797, or 5550+5797 for 161) | b6615daae110505bedd98e12e3652fbd9b3d9d448617879b1f4622f692919b3d |
| pool_171.tsv (mask 5550) | 36015cbd6c18e098c958188288b963ae0b9d40911bb2b326d3c58270dbc76b22 |

Cue files were committed in e08777fb9 (03:14 UTC) before any control context was rendered (03:17) and are not edited
after. **Disclosure:** the worker opened `ciphers/lodewijk-van-nassau-1573-74/names.tsv` at 03:01 UTC, before writing
the cue files, to learn the folder's context format. To keep that from steering them, every cue class is a complete
general vocabulary of the language (German titles: every rank Kaiser to Freiherr; kinship; possessives; prepositions),
not a selection, each row with its period-corpus count (tools/data/fr16, de17+de1600, en18). After the contexts were
rendered at 03:17 (e.g. 5810 "uillede de <223>", "ville de" + code), no cue was added ("ville" is NOT a cue, and stays
out for this job).

Pools were built and frozen (03:20 UTC) from the unmasked Groen edition text on disk (`groen/groen_IV_*.txt`, Groen
Suppl. 45* = 5549) through the promoted H41 surname step, titled phrases and recurrent capitalised names, plus
KEY-OFFICES.tsv correspondents. **Wikidata is absent from every pool:** query.wikidata.org answered HTTP 429 on the
first request and on the one permitted retry (03:15, 03:18 UTC); the host was stopped (ROOM.md 03:16, 03:18). So kin,
life dates and offices come only from what titled phrases carry; the person features alive-at-date and kin relation
are inert in control (a), and person results test far less of the instrument than the place results.
Masks (every letter carrying the held-out code, from the decode configs + 5550 runs): 202 -> 5549, 5550; 223, 241 ->
5810; 153 -> 5549, 5550, 5797; 154, 200 -> 5797; 161 -> 5550, 5797; 171 -> 5550.

## Truth aliases (known-answer match: equal fold, or alias fold >= 5 letters inside the candidate name)

202 franckreich|frankreich|france|frankrijk|francia|franckrych; 223 harlem|haarlem; 153 pfaltzgraf|pfalzgraf|palsgrave|
elector palatine|electeur palatin|kurfurst von der pfalz|keurvorst van de palts; 154 herzog von sachsen|duc de saxe|
elector of saxony|kurfurst von sachsen|augustus, elector of saxony; 161 landgraf|landgrave|lantgrave|landgraaf; 200 herzog
von alba|duc d'albe|duke of alba|duque de alba|hertog van alva|fernando alvarez de toledo; 241 zeelande|zeeland|zelande|
zealand; 171 prinz zu oranien|prince d'orange|william the silent|willem van oranje|guillaume d'orange.

## Control (a): Lodewijk van Nassau 1573-74, leave one out (`mqs_names_control_a.py score`, 200 null draws, seed 1)

Coverage is reported first per code (true value anywhere in its frozen pool); a value outside the pool is a pool
failure, not a ranking failure.

- **Places, the gated class:** 202 franckreich (5 contexts: 5550 x4 + 5549 PS, German) and 223 harlem (4 contexts,
  5810, French). **Gate: both true values in the top 5 AND each true-value score above its own context-null p95.**
  A pass licenses places, in the language of the code that passed, and nothing else.
- **Persons n >= 2:** 153 pfaltzgraf only (one code): reported, "untestable at this N (one code)", never gated.
- **n = 1 class:** 154, 161, 200, 241: reported only; licensed only if the **power check** passes first: 202, 223 and
  153, each cut to one random context (20 draws), put the true value in the top 5 in at least half of the draws, for
  every one of the three.
- **171** is the recipient passed as input: "trivially placed", in no count. **172** excluded (AX2-172, rule 4).
- Persons and places are reported separately, never blended. A2-LVN4 failed on 153, 200, 202 and 223 with its own
  instrument (0 hits, 1 wrong).

**Expected:** a FAIL is the expected result. With no Wikidata, a place's rank is set by the place/person frame of its
contexts (German aus/in, French en/vers/dans; 'de' is not a cue) and by co-mention in the unmasked Groen letters, so
France (heavily mentioned) may reach the top 5 for 202 while Haarlem, a frame-poor French context ("de <223>"), is
expected to sit below the frequent places. Ceiling check: the null is not near ceiling by construction -- under random
other codes' contexts the true value keeps only its co-mention and assigned-penalty terms, so a true value that wins
only by co-mention cannot beat its own p95.

**Why each null can fail differently from the known answer (rule 3, the "control that cannot vary" paragraph):** the
statistic is the true value's score, which sums context-dependent terms (kin, title/office, gender, place/person frame,
consistency over contexts) and context-independent ones (co-mention, assigned penalty, life dates). The context null
swaps in other codes' contexts and so moves every context-dependent term; it ties the real score only when the real
contexts add nothing, which is exactly the case it is meant to expose. The decoy null adds random index words of the
pool's name lengths with a random pool type; it can beat the true value when co-mention or a generic frame, not the
name, drives the score.

## Control (b): a second, language-matched known answer

Scan rule (pre-registered before reading the scan's output): `name_candidates.py --find-controls --min 8` over
`ciphers/*` -- names.tsv rows graded H/C with a non-NULL value of >= 3 letters; reading_*tokens*.tsv tokens graded H/C
whose value is capitalised or multiword and >= 4 letters (name-ish); md-blocks folders through holder_export.MdBlocks
(read-only), code words graded H/C whose meaning is name-ish. A qualifying set: >= 8 distinct codes in one folder.
Order: French first, then any other non-German language, folders in alphabetical order; the first qualifying non-German
set is run under control (a)'s shape (masking, coverage first, places gated per class: every place code with n >= 2 in
the top 5 and above its own context-null p95). For Eckert-type md-blocks folders the mask excludes any Official Records
or holder transcription text of the masked telegrams (no such text is passed as --index), and the pool never
takes names from the folder's own key or cipher book (that would be the key). If no French set qualifies: "untestable at this
N for French", and no French target run is licensed by this job. If the qualifying set's pool cannot be built without
the key itself (the only name list on disk is the key), it is logged "untestable: no independent pool" rather than run.

## Shelf rule

A control that misses its gate ships the option with shelf grade `weak` and both numbers; nothing is run on a target
from it. Results are reported by class (places / persons, n=1 / n>=2) with pool coverage, never one blended figure.

## Amendment 1 (9 Oct 2026, 03:2x UTC by date -u; written after the scan's output was read, before any control (b) run)

**Scan (b), as run.** The first scan output (03:22 UTC) listed fr3993-gonzague-nevers-1595 on eight NULL codes and
Manteuffel 1712 on isolated single-group lines; both are outside the brief's own rule ("codes that occur in decoded
context", non-NULL values), which the pre-registered wording above had left out. The scan now excludes NULL and requires
another decoded token on the same line. Its output (03:24 UTC): eckert-1864 (md-blocks, 1095 code words, English),
lodewijk-van-nassau-1573-74 (12, German: control (a) itself), vanbeuningen-dewitt-1657 (9, Dutch). **No French set
qualifies: "untestable at this N for French"; no French target run is licensed by this job.** The first qualifying
non-German set in alphabetical order is eckert-1864 (English), so control (b) runs there.

**Control (b) design (`tools/tests/mqs_names_control_b.py`).** Class: person code words whose cipher-book meaning has
the book's surname-plus-initials form ("Grant U S"); places cannot be classed without a gazetteer, so (b) gates
persons. Population: every such code word with >= 2 md-blocks contexts; sample 10 (random.Random(1)). Truth: the
meaning's surname (fold-equal, or contained if >= 5 letters). Contexts: md-blocks readings (MdBlocks, read-only), the
tested code word shown as <word> everywhere. Index: the Official Records volumes cached in
sources/ia-fulltext/print-check/ (warofrebellion*, officialrecordso*), split into pages; **mask:** every page sharing >= 2
folded word 4-grams with the decoded text of any telegram that carries the tested code is dropped from the pool and the
co-mention feature. The pool never reads key.md. Nulls: context null 100 draws, decoy null 100 draws, seed 1.
**Gate:** at least 5 of the 10 sampled person codes covered, in the top 5 and above their own context-null p95.
**Expected:** FAIL. With no Wikidata, person candidates are bare surnames from the OR index; the English cues give
title (general, gen) and frame (by, with, at, to) terms only, and ranking is then dominated by co-mention, which the
context null holds constant -- so a true value can pass only if its contexts carry a title or frame cue the others lack.

**Amendment 1a (03:3x UTC, before any (b) scoring):** the cached OR djvu texts carry no page breaks (the first freeze
saw 13 "pages", one per volume, so the mask dropped whole volumes), so "pages" are 3000-character blocks cut at a line
end; the mask rule (>= 2 shared 4-grams) is unchanged. Pools re-frozen after this change; sha256 in
fixtures/name_candidates/eckert/pools.json.

## Result, control (a) (scored 03:2x UTC, `fixtures/name_candidates/lodewijk/control_a.tsv`)

| code | class | n | pool | coverage | rank | score | context-null p95 | beats p95 | decoy beat share |
|---|---|---|---|---|---|---|---|---|---|
| 202 franckreich | place (gated) | 5 | 147 | yes (France) | 13 | 1.417 | 1.417 | no | 0.01 |
| 223 harlem | place (gated) | 4 | 159 | yes (Harlem) | 11 | 1.472 | 1.472 | no | 0.03 |
| 153 pfaltzgraf | person n>=2 | 4 | 122 | **no** (pool failure) | - | - | - | - | - |
| 154, 161, 200, 241 | n=1 | 1-2 | 128-159 | **no** for all four | - | - | - | - | - |
| 171 (trivially placed) | - | 1 | 151 | yes | 23 | - | - | - | - |

Power check (top-5 share at one context, 20 draws): 202 0.00, 223 0.00, 153 0.00 -- fails, so the n=1 class licenses
nothing. **Gate: FAIL** (places 13 and 11, not top 5; neither above its own p95). **Diagnosis, and why this is a
non-test of the context features rather than a negative on them:** the true score equals its null p95 to the last digit
because every index-derived candidate (France, Harlem) carries no person/place type -- types were to come from Wikidata
(HTTP 429, stopped) -- and score_context skips the place/person frame for an untyped candidate, so the context terms
were 0 for both true values under real and null contexts alike: the context null could not vary on the statistic for
these candidates (CLAUDE.md rule 3, "a control that cannot vary"). What the run does measure: co-mention alone ranks the
true places 13th and 11th behind DBNL page boilerplate ("Over", "Collectie", "Zoeken") and the correspondents' own
names, i.e. the index pool step needs the site chrome stripped. Logged "untested-by-this-run" for the context features,
not refuted; the next instrument step is typed candidates (Wikidata when it answers, or a gazetteer), not another
run of this pool. Shelf grade: weak.

## Result, control (b) (scored 03:59 UTC, `fixtures/name_candidates/eckert/control_b.tsv`, pool sha256 in pools.json)

Eckert 1864, 10 sampled person code words (English, H): coverage 8/10 (Averill, Ord absent); covered ranks 339-1406
of ~5,900; every covered true score equals its own context-null p95 (0/8 above); decoy beat share 0.02-0.09.
**Gate: FAIL, 0/10 (>= 5 needed).** Same mechanism as (a): bare index surnames carry no type or title, so the context
terms are 0 under real and null contexts alike -- a non-test of the context features, not a negative on them; the
ranking is co-mention only, topped by OR prose words ("General", "Have", "Mentioned", "Mayor"). Shelf grade: weak.
Nothing is licensed: no French set qualified, the German places gate (a) and the English persons gate (b) both failed.
Next instrument step (not this job): typed candidates -- Wikidata when it answers, or a gazetteer/title-phrase typing
step for index names ("General X", "à X") -- and stripping site chrome from the edition text, then re-run (a) and (b)
unchanged against new frozen pools.
