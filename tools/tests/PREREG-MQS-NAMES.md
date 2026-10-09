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
