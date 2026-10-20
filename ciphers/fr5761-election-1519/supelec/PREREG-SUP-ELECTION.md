# PREREG SUP-ELECTION (20 Oct 2026, written 03:2x UTC by date -u, before any fetch or read)

Brief: .claude/briefs/runs/2026-10-20-acct4-research-director-28.md, JOB SUP-ELECTION = ELEC-2R Next (1) only. Step (2) (Lisch) not in this job.

## Question
Is the fr.3897 f.116r l.29 sign (nr. 357, printed Palatin, labelled "4" in elecpair/pairs.tsv) the l.11 "4" shape or the f.84r l.21/22 "Lbar"
shape (nr. 356, printed Trèves)? Reader 1 (ELEC-27, non-blind): Lbar. Reader 2 (ELEC-2R, blind): grouped it with both, low-medium.

## Material
- openapi.bnf.fr btv1b90096539 f142 `pct:50,0,50,100/max` (f.116r = right half, native resolution; gives l.29, l.11 and l.32 in one request).
- openapi.bnf.fr btv1b90096539 f106 `pct:57,25,42,72/max` (f.84r region, native; ELEC-39's region; the Lbar at 2000-px x 1570-1710 y 1045-1095).
  The brief names 1 region request; the reference crops of ELEC-27/ELEC-2R were scratch-only and are gone, so the Lbar reference needs the
  second request. Declared here, reported in the done line. >= 3 s apart. Images in the scratchpad only; sha1 logged.
- Crops cut locally (PIL, the same tool path as tools/iiif_lines.py's local crop), each centred on one sign with a few neighbouring letters,
  all three scaled to one line height. T = f.116r l.29; R4 = f.116r l.11 "4"; RL = f.84r Lbar. No full page goes to a reader.

## Readers (2 vision calls, strongest model, fresh subagents, blind)
Each reader sees three crops under neutral names (X, P, Q), is told only that each crop is centred on one non-letter sign in a 16th-century
French cipher letter, and is told no label, printed name, prior reading or leaf. Reader 3a: P = R4, Q = RL. Reader 3b: P = RL, Q = R4 (position
swap, controls for a first/second-position bias). Task: (a) describe the strokes of each centred sign; (b) are P and Q the same sign? (yes/no);
(c) forced choice: is X the same sign as P or as Q (must choose one), confidence 0-100, and the strokes that decided.

## Decision rule (fixed now)
- Non-test: if a reader answers (b) "yes" (the references do not discriminate for it), that reader's choice does not count.
- Relabel elecpair/pairs.tsv f.116r l.29 from "4" to "Lbar" only if both counting readers choose RL with confidence >= 60.
  Then re-run elecpair/pair_control.py and elec356/pair_control.py (seed 357, 1000 permutations) and report 4 and Lbar; Lbar would carry
  Trèves 1 / Palatin 1: a rule-4 data conflict (one sign, two printed names), recorded with witnesses in HYPOTHESES.md, graded M, never
  resolved by frequency; 4 = Palatin would rest on 1 pair (l.11).
- Keep "4" and log "settled 4 (readers 2 of 3 or better)" only if both counting readers choose R4 with confidence >= 60; the ELEC-27 shape
  observation is then logged as not confirmed.
- Any other outcome (split, low confidence, a non-test): label unchanged, slot logged "readers disagree", conflict stays open.
- No key.tsv change in any outcome. Grades stay M (rule 4: >= 2 pairs, one name, shuffle < 5% before anything above M).
