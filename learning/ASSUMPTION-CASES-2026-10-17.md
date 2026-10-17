# Assumption cases: could the record have caught it before the owner did? (CASES-TX, 17 Oct 2026)

Brief: `.claude/briefs/runs/2026-10-17-acct4-research-director-1.md`, JOB CASES-TX (owner's directive 8.5). Disk only, no new
experiment, no network. Written 01:2x UTC 17 Oct 2026 by `date -u`.

Method: for each case, find the date the error was pointed out from outside the agent loop. Then list what was already on disk
before that date, using only dated sections (NOTES.md headings, LEDGER.md rows, ROOM.md stamps, PREREGs), and name the check
that would have flagged it. This clone's git history is shallow (every `git log -S` lands on the 16 Oct graft commit), so every
date below comes from a dated heading or row inside a file, not from commit dates.

Verdict vocabulary: **diagnosable** means the number that shows the problem was already on disk, or a check under about USD 3
on files already on disk would have produced it. **Not diagnosable** means it needed something the record did not hold.

## Table

| case | who caught it, and when | evidence on disk before that | check that would have caught it | verdict | cost of the check |
|---|---|---|---|---|---|
| (a) debosnys-1883: about 28% reader disagreement carried through many machine passes | The owner, 1-2 Oct 2026: settle the alphabet in the sign sorter before reading (LESSONS.md "Settle the alphabet before reading", 1 Oct) | 25 Sept, GOLD-4C (NOTES.md "GOLD-4C, inventory"): 76% of cryptogram 4's 228 disagreement columns were *inventory confusion*, 15% segmentation, 9% reading error. "GOLD-4A's 22.4% agreement measured the inventory, not the legibility of the page." The same day the GOLD-4E LEDGER row says: "the inventory, not the pass, is the bottleneck -- next needs a composite/base re-count or a smaller alphabet hypothesis before any more passes." Even so, 28-29 Sept saw H2, H21/H21b, H23, H57 and H63 (more reader calls) and H50 (pricing a fourth pass at USD 14-18) | A **disagreement class breakdown** (inventory / segmentation / reading) on the earliest two-pass reconcile, with a stop rule: if inventory confusion is the largest class, the next step is a settled alphabet, not another pass. The 25 Sept prose rule in Usage 6 ("two passes, not three, unless the two disagree on more than a tenth") pointed the other way: it *licensed* a third machine pass at exactly this disagreement | **diagnosable, and in fact diagnosed on 25 Sept.** What failed was acting on it: the finding lived in a NOTES section and a ledger lesson, and nothing turned it into a gate | 0: GOLD-4C's `scripts/gold4c_inventory.py` had already computed it |
| (a') debosnys-1883: tight base boxes dropped the marks that tell signs apart (the X-DOT dot, the bar over X) | The owner, 1 Oct 2026, on the opening sorter tiles (LESSONS.md l.237) | `marks.tsv` and glyph_atlas's attribute model existed, so the marks were known to sit outside the base box | Before a sorter or reader sees a tile: render a few random tiles with `marks.tsv` overlaid and check that each mark falls inside its crop | diagnosable | under USD 0.1 (CPU plus one look) |
| (b) fr2933-salviati-1525: syllabary and mixed-mark controls run at 0/5/7% injected error while raw pass A/B disagreement was 14.6% | **Not the owner.** The 26 Sept retrospective (RETRO-2026-09-26a, NEAR review), then SALV-DIAG on 26 Sept 09:53-10:06 found the control's collapse sits at about 8-9% | 25 Sept 21:24-21:41, CM3 (NOTES.md "CM3: measured-error control"): 14.6% raw A/B disagreement, against a *model-estimated* residual of 4.9% per sign that the 5-7% controls were matched to. 25 Sept 18:18, ROOM (LANE R6): the code+mark control "falls to 27-43 pct at 10 pct type noise ... NOT a negative". CM2's own error-tolerant curve (10% noise: 41.5-58.3%). DSN ran at 22:24 that evening, after all three of these were on disk | A **control error sweep that brackets the raw measured disagreement**, not only the modelled residual: run the control at the low estimate, the high estimate and the raw two-reader figure, and call the target negative only where all three read | **diagnosable**; caught by the agents' own retrospective about 11 hours later, before any outward claim | USD 2.99 (SALV-DIAG's ledger row; CPU control runs only) |
| (c) espagnol142-mercy-1648: four out-of-range codes (48, 52, 65, 72) were two digits written together | D. Bourdeau, 1 Oct 2026 (reply on dbourdeau/cyphersolver issue 16), passed on by the owner. MERCY-IMG on 15 Oct confirmed the splits with two blind readers (known-answer control 172/173 each) | 25 Sept, Y6 (NOTES.md "The ciphertext: structure"): "36 numeric values, range 2-72", while the settled key (M2, 25 Sept) runs 2-34. 27-28 Sept, H2 (NOTES.md l.1250): "48, 52, 65, 72 -- all above the 2-34 letter range". The folder's own lesson says so: "a range check on the token stream against the key's own range ... would have flagged 48, 52, 65 and 72 as two digits written together on the day the key settled (M2, 25 Sept 2026), instead of carrying them for six days as 'M codes'." H36 and H41-H42 spent steps giving them letter and syllable values instead | A **range check** on every token against the key's own range, with every split into in-range key codes listed: now `tools/decode_key.py --split-check` | **diagnosable** on 25 Sept. The fact was even written down twice. The error was in what it was taken to mean (nomenclature), and the only thing that tested that reading was an outside solver | seconds of CPU |
| (d) fr16104-vivonne-spain-1572: machine label piles merge signs (R14: piles "mix shapes that I can clearly see"); f.191r needed a deskew re-cut | The owner, 14 Oct 2026 (VIV-HUMAN2 notes R13/R14, NOTES.md l.2884). The deskew re-cut was VIV-F191 on 14 Oct (LEDGER l.4428). The brief puts both on 3 Oct; the dated record puts them on 14 Oct | 4 Oct, N5-VIVK: "Slope-tracked bands produced duplicate lines (readers marked DUP ...) -- so up to five real lines may be missing", which is the cut problem the deskew fixed ten days later. 4 Oct, N6/N7 pages: err_2reader 0.10-0.30 (f.193r 0.297), above the 2 Oct "next pass is a person's" line, with the same unsettled pairs every time (S/d, 3/z, g/y, r/x; NOTES.md l.872). 4 Oct, N5-VIVK built a known-answer leaf (ink 40 against its clerk decipherment ink 41), which could have given err_true. VIV-SYNTH (17 Oct) puts reader error near 0.14 on clean truth | (1) **err_true on the known-answer leaf** before any decode of an unread piece (tx_bench against the clerk-truth leaf); (2) a **stable confusion-pair check**: the same pairs splitting on every page points to a label inventory problem, not page noise; (3) a **DUP/line-count check** on every cut, with a re-cut before reading if any line is duplicated or missing | **diagnosable** for both the label merge and the cut defect. The owner's contribution that the record could not have supplied is the *perceptual* judgement that the piles were impure "clearly" (T5 in RESEARCH.md: a person reads this hand where machine readers fail) | err_true on the existing truth leaf: under USD 1 (CPU); the DUP check: 0 (the readers had already marked DUP) |
| (e1) na-oldenbarnevelt-2442-1605: sorter tiles cut from the clear Spanish line above the cipher line (off by one line); sorter withdrawn | The owner, 6 Oct 2026 01:50 (ROOM.md; LEDGER R7-OLDSORT D-) | The `iiif_lines.py` debug overlay. CLAUDE.md Usage 8 says "Check the debug overlay before handing crops to a pass", a rule dated 24 Sept | Open 3 random tiles against their line image before any owner card (the withdrawal's own lesson); in effect the overlay rule, applied to sorter builds | diagnosable | under USD 0.1 |
| (e2) na-oldenbarnevelt-2442-1605: leaves 4/5/7 noted 25 Sept, read only when the owner asked on 8 Oct | The owner, 8 Oct 2026 04:02 (ROOM.md; learning/INTERVENTIONS.tsv 10 Oct) | The 25 Sept note itself; NEXT-STEPS.tsv (26 Sept) | `tools/next_steps.py` / `tools/loose_ends.py`: a written next step with no run. A dropped step, not a wrong assumption | diagnosable (but not a transcription or assumption error) | 0 |
| (e3) sorter defects, 1/3/6/9/10 Oct (learning/INTERVENTIONS.tsv) | The owner, on the published sorter pages | TRANSCRIPTION.md; later `sorter_preflight.py` | Preflight on cut, colour and pile purity before publishing (R13/R14 now require a pile-purity check) | diagnosable for cut and colour; pile purity counts only after R14 named it | low |

What the rest of learning/INTERVENTIONS.tsv records is not an assumption or transcription error, so it is out of scope: idle
capacity, silent orchestrators, usage-report format, and strategy or spend decisions that belong to the owner (15-17 Oct).

## What the cases share

- In the four named cases, the number that showed the problem was on disk **before** the outside catch. The gap was 1 to 10
  days (Debosnys 25 Sept -> 1 Oct; Mercy 25 Sept -> 1 Oct; Salviati 25 Sept 21:41 -> 26 Sept 10:06; Vivonne 4 Oct -> 14 Oct). In
  two cases (Debosnys, Mercy) the folder had *written the right conclusion down* and kept working on the opposite assumption.
- None of the checks is expensive: every one is CPU on files already on disk, at most about USD 3.
- The outside contribution the record lacked is narrow: the owner's perceptual sorting (Debosnys sameness, Vivonne pile
  purity) and Bourdeau's split reading. Both *confirm* a diagnosis the numbers already allowed. Neither was needed to *see* it.
- One existing rule made things worse. Before the sorter rule, Usage 6's ">10% disagreement -> third pass" rule pointed toward
  more machine passes in exactly the situation (inventory confusion) where they cannot help.

## Two or three checks that would have caught most cases

One-line rules the common tail could carry (`.claude/briefs/README.md` is not edited here; the parent decides):

1. **Class the disagreement before the next pass.** "After any two-pass reconcile, report disagreement by class (inventory /
   segmentation / reading, per GOLD-4C) and the top recurring confusion pairs. If inventory or one stable pair set dominates,
   the next step is a settled alphabet or a re-cut, never another machine pass." Catches (a), (d), (e1), and the DUP half of (d).
2. **Bracket the control at the raw error.** "A control that licenses a negative runs at the target's raw two-reader
   disagreement and its err_true (when a known-answer leaf exists), not only at a modelled residual. A negative holds only at
   error levels the control still reads." Catches (b) and the ink-63 negatives in (d).
3. **Every token inside the key's range before an M value.** "Before any out-of-key or out-of-range token is given a
   nomenclature or letter value, run `decode_key.py --split-check` (and a line-count/DUP check on the cut). An in-range split
   comes before an added code value." Catches (c) and the cut half of (d).

## Six research-director questions

- **What we learned:** in every named case the diagnosis was available from the record, and in two it was already written
  down. The failure is in turning a finding into a gate, not in detecting it.
- **Assumptions it depended on:** that dated NOTES headings and LEDGER rows reflect when evidence existed (git history is shallow
  here, so commit dates could not be used to check them); that "the owner caught it" is the right framing for (b) and (c).
- **Unverified:** the exact date of the owner's Debosnys message (taken from LESSONS.md's 1 Oct heading); the brief's 2-3 Oct
  Vivonne dates, which the record does not show (the R14 note and the deskew are both 14 Oct); whether the owner said anything
  about Vivonne cuts before VIV-F191's brief, which this pass did not find.
- **Alternative explanations:** hindsight bias. Picking the one telling number out of hundreds of NOTES lines is easier once
  you know the answer. A fair test is whether the three rules above would have fired *without* also firing on cases that were
  fine (this pass did not measure their false-alarm rate).
- **Most informative different experiment:** replay the three rules mechanically over every target's dated sections from
  24 Sept to 16 Oct (a script over NOTES/LEDGER, disk only), and count true catches against false alarms before any of them
  becomes a gate.
- **Decision:** continue. Hand the three rules to the parent as proposals and queue the replay as the next cheap question.
