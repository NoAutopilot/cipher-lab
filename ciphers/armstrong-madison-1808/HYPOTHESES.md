# armstrong-madison-1808 -- hypothesis families (append-only below the ladder)

LANE ARM, opened 26 Sept 2026 06:49 UTC (owner's decision 06:40). One section per family; CONTROL and TARGET
numbers side by side (CLAUDE.md rule 3). The top block is rewritten only by a cycle consolidator.

## Ladder (LANE ARM orchestrator, 26 Sept 2026)

- A. Crib placement -- AS BRIEFED, NO CRIB EXISTS: QUEUE row 27's "Krajcovic's crib from the 15 Feb letter to
  Jefferson" is a scout mix-up (TOMO-REPLY, NOTES.md). Replaced by A1 (ARM-REC: crib hunt in the later
  correspondence) and A2 (direct-transfer sweep of every published sibling table against a structure-preserving
  shuffled table, after ARM-CODES).
- B. Sibling-code vocabulary: corpus ARM-CODES (tools/data/uscodes-1800/), design ARM-DESIGN (Fable; one-part vs
  two-part, tested on two siblings as control).
- C. Nomenclator solver with the vocabulary prior (family_run.py `nomenclator`), after B.
- D. Model-in-the-loop, only if C's control clears and the target reads partially.
- E. Recovery (ARM-REC).
- S. Shorthand passages (35 short + 2 lines) against period systems -- not in the brief's ladder; queued after B.
- Judge: en18 corpus (ARM-EN18) before any en verdict on this target is trusted.

## ARM-CODES corpus (26 Sept 2026, worker ARM-CODES)

No decoding or family run this pass -- corpus build only, per this job's brief. Full sourcing, licences and
unreachable items in `tools/data/uscodes-1800/README.md`; stats regenerate offline with
`python3 tools/data/uscodes-1800/stats.py`, reading only the TSVs there and this target's own
`ciphertext.txt`. Four value->word tables were built: `WE028.tsv` (1600 entries, Monroe<->Madison, H grade),
`THE972_bourdeau.tsv` (580 entries, Armstrong<->Madison except the target, H/C/M/I grades kept from
Bourdeau), `THE972_tomokiyo_partial.tsv` (227 entries, C/M) and `THE972_tomokiyo_clean.tsv` (95 entries, C)
-- the latter two are two different published renderings of the same underlying reconstruction (from
Armstrong's known-plaintext letter of 4 May 1806), kept separately since neither is a strict cleanup of the
other by inspection. No table exists for WE027 (Livingston<->Madison) or for any other WE-numbered code
Tomokiyo names -- his site publishes worked decoded-letter specimens for those, never a downloadable table
(see the README's "Not reachable" section). Weber 1979 itself is on Internet Archive
(`unitedstatesdipl0000webe`) but print-disabled-tier and unborrowable by this account; no HathiTrust volume
exists for its OCLC number either -- not chased further, per the brief.

**Target stats (`stats.tsv` row `armstrong-madison-1808_target_ALL_369_tokens` / `..._216_distinct`):** 369
tokens, 216 distinct, values 1-1900. Last-digit distribution over all 369 tokens: `0:93 1:66 2:17 3:10 4:41
5:12 6:32 7:46 8:45 9:7`. Hundred-block counts (distinct values): a trough of 3 values in 900-999 and 1 in
1000-1099 (4 total, matching the brief's own count), against 8-16 in every neighbouring block.

**No sibling shows the target's skew, in its table or its real usage.** All four tables' own defined-value
sets run 53-65 entries per last digit (WE028 is exactly flat, 160 per digit, by construction: one contiguous
1-1600 run). THE=972's real *usage* in Armstrong's other four 1808 letters (pooled, 474 tokens, rendered
into `decodes/`) is closer to flat-with-noise than to the target's shape: highest digit is 2 at 70 (15%), not
digit-0 (44, 9%) -- the target's digit-0/digit-1 dominance (25%/18%) is not a generic feature of this code
family's construction or of how Armstrong's own hand actually uses it. Likewise no table or usage instance
shows a comparable 900-1099 trough (all run 25-53 combined in that range, against the target's 4) -- the gap
is target-specific, not inherited from a codebook we already have.

**Construction: blockwise-alphabetical, all four tables, consistent with NOTES.md's qualitative read.**
Spearman rho (value order vs. plaintext alphabetical order) is near zero for every table (-0.09 to -0.25),
not the +1.0 a single alphabetical one-part code would give; alphabetical-run-block counts are 98 (WE028,
~16 entries/block), 99/48/18 for the three THE=972 tables (~5-6 entries/block on the denser ones) -- many
short ascending runs, i.e. a two-part-style code built in alphabetical blocks, the same convention across
Livingston's, Monroe's and Armstrong's own codes.

**Homophones concentrate on short common syllables in THE=972, are near-absent in WE028** (a near-1:1 word
code). Top of `THE972_bourdeau.tsv`: `re`=6, `tion`=4, `be`=4, `ta`/`con`/`pro`/`ne`=3 each -- the shape a
nomenclator solver (family C) will need to model when it gets to the target.

CONTROL: none run this pass (no family, per the brief). These are corpus-comparison numbers, not a
cryptanalytic test with a matched control -- rule 3 does not apply to a corpus-build job.

## Orchestrator structural note (LANE ARM, 26 Sept 2026 07:00 UTC; target only, no control yet -- an observation, not a result)

Values >= 100 (237 tokens, 169 distinct): last digit 0 on 92 tokens, 1 on 47, 4 on 26, 6 on 22, 7 on 22, 8 on 12,
2/3/5/9 on 9/3/2/2. Values < 100 (132 tokens, 48 distinct): last digit roughly flat (7 and 8 commonest: 17, 18,
38, 47, 48). Distinct big values sit in 99 decades, 45 with two or more variants, e.g. 1760/1761/1762/1764/1767,
1470/1471/1472/1476, 1840/1841/1842/1848, 160/161/162/164, 1350/1351/1354. Hypothesis H-DEC for the design
worker: a "decade" code -- root words at multiples of ten, units digit an inflection or derived form (0 root,
1 plural or -ed, ...), with a separate block 1-99 for particles; alternative H-HOM: units digit a homophone
choice with a writer's preference. Needs a sibling of either design as the control before it licenses anything.
