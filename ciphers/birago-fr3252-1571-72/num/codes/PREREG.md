# PREREG -- N8-BIRNUM (4 Oct 2026, account 2 worker for LANE-NEAR8): dotted groups and 1x/5x/8x units as nomenclator codes

Written and pushed before any statistic below is computed. Inputs: `../f100_recon.txt` (f.100r, two blind passes +
reconciliation, BIRAGO-NUM) and `../f119_ct2_bourdeau.txt` (f.119, Bourdeau's ct2, MIT / CC BY 4.0, credited). Disk only.
Retired instruments not reused: joint anneal (BIRAGO-NUM3), spelled-crib drag and decoy-null joint crib (NUM2, NUM4).
This is a different instrument: code reading from context around each occurrence, plus the clear text of the same leaf.

## Candidate units (fixed by rule, not by inspection)
- **Family D (dotted groups).** f.100r: every maximal run of dotted tokens (`i` = dotted 1, or a digit carrying `.` or `:`),
  cut into pairs from the left (a lone leftover digit is dropped). f.119: a digit carrying `.` or `:` paired with an
  adjacent such digit, or a lone `.`-digit followed by `1` (Bourdeau folds the dotted i into 1; BIRAGO-NUM eye check on
  his "4. 1"), plus `2~ 5-` (25, BIRAGO-NUM's shared marked group). Other lone marks (`0:`, `8-`, `8+`, `4+`, `7+`, `2+`, `2-`)
  are not groups. Candidate types: D types with pooled count >= 2.
- **Family U (1x/5x/8x units).** BIRAGO-NUM-TOOLS's `158` parse of each plain run (a 1, 5 or 8 opens a two-digit unit,
  every other digit is single), dotted groups and letters removed first. Candidate types: two-digit units with pooled
  count 2..8 (name-code frequency; the very common units are letter-like and excluded by this cap).
- 76 / the wavy sign are the run delimiters (BIRAGO-NUM) and are not candidates.

## Statistic (Step B, cipher context)
Digit stream per letter = plain digits in order, with breaks at letters (m n h f c a l), `|`, CLEAR and line ends of the
run (line ends are NOT breaks: the cipher runs across lines). For each occurrence, left flank = the 2 digits immediately
before it, right flank = the 2 digits immediately after (None if a break or another candidate unit falls inside).
For a type t with n_t occurrences: s_t = max(largest group of identical left flanks, largest group of identical right
flanks) - 1, floored at 0. **T = sum of s_t over candidate types**, per family.
Rationale: a name/title word code is preceded or followed by a small set of words (di, a, il, la, Monsignor ...);
under a low-homophony letter table (~30-50 cells, BIRAGO-NUM) that shows as repeated flank digits.

## Null (control that can fail)
Shuffled run positions: for each draw, each type t gets n_t random non-overlapping positions in the same two letters'
digit streams (any 2 adjacent plain digits outside real candidate units), flanks taken the same way, T recomputed.
2000 draws, seed 20261004. Target PASS for a family if T_real > null p99.

## Power control (gates whether a target miss means anything)
Synthetic it16dip Italian, 520 letters, homophonic table of 40 cells over digits {0,1,2,3,4,5,8,9}, 5% stray digits;
the 3 most frequent words of length >= 4 in the span that occur >= 3 times are replaced by 3 fixed two-digit word codes
(Family D analogue). Same statistic, same null (500 draws per trial). 20 trials, seeds 1..20. Power = share of trials
with T > own null p99. **If power < 0.5 the Step B result on the target is a non-test (untested-by-this-tool), not a
negative and not a pass.**

## Licensing a meaning (Step A, clear context)
Clear text of f.100r read by this worker from `../../images/c101.jpg` (1600 px; the clear text is itself M-grade).
- Slot rule: a unit within 2 units of a clear-text boundary takes a meaning only if the clear sentence frame forces one
  word, and the same unit stands in an equivalent slot a second time.
- Entity rule: a type that occurs in f.100r takes a meaning only if exactly ONE entity (person, place, office) is named
  twice or more in f.100r's clear text, and it occurs in f.119 only if f.119's clear text names it too (not on disk:
  f.119 types cannot satisfy the rule this job).
- Any meaning is grade M; S only if a second occurrence agrees AND Step B passes AND the power control >= 0.5.
- Expected under the rules as written (stated before computing): the entity list of f.100r has several twice-named
  entities, so the entity rule cannot single one out; all four f.100r clear boundaries are flanked by the 76/wavy
  delimiter. If so, no meaning is licensed whatever Step B returns, and Step B is reported as a structural result.
