# FT4aa pre-registration (account-4, 3 Oct 2026, written 17:2x UTC by the clock, pushed before any run of align/ft4aa_scan.py)

Step (FT4z's Verdict / VERIFY-ROU121): a two-release scan on the two f.206 conflicts FT4z found -- pair A = F206 + F216V (restored
only by releasing 338 alone) and pair B = F206 + f.266r S1 (restored by no single release). Question: which pair of key rows,
released together in F206, restores a joint exact fit.

Instrument: FT4x/FT4z's exact (0-edit) CP-SAT, unchanged (`align/ft4x_pool.py` solve_exact; blocks from `align/ft4z_pool.py`):
blocks joined by '#SEP' pinned '|', a shared code carries one chunk in both blocks. C pins 22 de, 66 r, 581 au (FT4z set,
unchanged); 722 free; 121 free in the primary run (as in FT4z; VERIFY-ROU121 confirmed 121 = s, see secondary); MAXLEN 12;
30 s per solve; unresolved counts high (as a fit).
Release = renaming code c in the F206 block only to a fresh symbol (F206's chunk for c no longer tied to the partner's).
Releasing more is strictly a relaxation, so any set containing a restoring single release restores trivially.

Scan scope (fixed now, from FT4z's release output): shared non-pinned codes,
  pair A: 10, 121, 208, 306, 338, 420, 444, 501, 781, 824 (10 codes; 45 unordered pairs; 9 contain 338 = implied fits, not run);
  pair B: 10, 114, 121, 123, 271, 347, 534, 722 (8 codes; 28 unordered pairs).
Statistic per pair-block: the set of MINIMAL restoring releases of size <= 2 (single releases, plus pairs that contain no
restoring single).

Controls, run FIRST, seed 3, n 40 each, the PARTNER block perturbed (F206 real): (s) partner slip words shuffled; (g) partner
group order shuffled; for pair A partner = F216V (its slip words split on spaces), for pair B partner = S1 (FT4z's words).
Per draw: release-all (every shared code released) solved first; if nofit, no <= 2-release can fit (monotone) -> draw negative.
Else 0-release, singles, then pairs until the first fit. Draw positive = some release of size <= 2 restores (fit or unresolved).
Share = positives / 40. A draw whose release-all is fit but whose singles/pairs are all nofit is negative (specific).
Power: if any of the four control shares > 2/40 -> **NON-INFORMATIVE (power)** for that pair-block; the real minimal set is a
readout only. Note on the control: it can differ from the target (a shuffled partner can fit alone and be restored by a
small release), so it is not orthogonal to the statistic (rule 3).

Outcomes (each pair-block separately, only if its two controls are <= 2/40):
  - exactly one minimal restoring release (size 1 or 2) -> **decisive locator**: the f.206 split values of those row(s)
    are the joint-inconsistency site against that partner. Mapping to key rows: rule-4 conflict note on those key.tsv rows
    ("f.206 split conflicts with <partner>, FT4aa locator"); grade unchanged (M stays M; a C row is not demoted by a locator --
    if a C row is in the locator, VERIFY flag, no edit); no value change (a release says where, not what). Any key.tsv edit
    -> ROOM.md VERIFY flag line. Never a status change.
  - several minimal restoring releases -> not located (the set listed, no key edit).
  - none (all pairs nofit) -> the conflict needs >= 3 releases or is not a release-type conflict (e.g. an f.206 slip/segment
    boundary); logged, no key edit.
  - any real solve unresolved in the scan -> listed; minimal set NOT SCORED if an unresolved could change it.
Secondary readout (registered, no gate): the real scan repeated with 121 = s added to the pins (now C, VERIFY-ROU121).
Rule 3 count: the pooled-exact instrument's third use overall (FT4x f.252r, FT4z 121) but its first on the f.206 locator
question (FT4z's single-release readout was an unregistered-gate secondary); a different question, not a re-tuning.
Box 17:13-17:43 UTC, stop line 17:37. Cap USD 3. Script only, no vision, no subagents.
