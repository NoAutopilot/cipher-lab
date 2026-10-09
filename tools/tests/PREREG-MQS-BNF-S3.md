# PREREG MQS-BNF-S3 (LANE MQS-2, account 4) -- written before any scoring

Date: 9 Oct 2026, 07:48 UTC by date -u. Worker MQS-BNF-S3, for LANE MQS-2 (session_01KtMrFJc3ZZmcYgUvGJNdCz).
Brief: .claude/briefs/runs/2026-10-09-ytbiz-mqs-next-bnf-s3.md. Disk only; no host contacted.

## Option

`tools/bnf_findingaid.py --pile ... --prior-work` adds, per cipher item (bare or named), two checks `--pile` does not
already call (it calls only prior_work.py check 3, `check_portals`):

1. **own work across the repository**: every top-level `*.md` and `items.tsv` file in every `ciphers/<slug>/` folder
   and every `ciphers/_triage/*.md`, matched with `tools/shelfmark.py match(unit, line) == 'exact'` (volume + folio
   bound in one clause, side-compatible; never folio alone). Skipped: any folder with RESTRICTED.md, any path with a
   `restricted` component, `ciphers/debosnys-1883`. A hit marks the item `ours` (the slugs are listed) and removes it
   from `open_bare` / `open_named`, as a KNOWN does today. New columns: `ours_items`, `ours_slugs`.
2. **active edition** (prior_work.py check 3a, `check_active_edition`, MQS-SCOUT): a LEAD on any item of the volume
   sets column `contact_first` to the project name; items are NOT removed from open counts (an edition in
   preparation is not print), the class is unchanged.

## Corpus

Every saved notice under sources/bnf-findingaids/2026-10-07/ and 2026-10-09/ (S2A + S2B + earlier passes), 109
notices with >= 1 cipher item (one row per ark).

## K1 known answer (recall, volume level)

Volumes with a notice on disk AND a `ciphers/` folder whose name carries the volume number (folder list read before
scoring): fr.2751, fr.2933, fr.2980, fr.2988, fr.2996, fr.3022, fr.3034, fr.3053, fr.3083, fr.3416, fr.3613, fr.3620,
fr.3621, fr.3622, fr.3624, fr.3625, fr.3631, fr.3669, fr.3789, fr.3974-3995 (the Nevers notice; folders fr3975..fr3993),
fr.4102, fr.4133-4138 (fr4137-sabran), fr.4687, fr.4698, fr.4712, fr.4715, fr.4734-4736 (fr4735), fr.5160, fr.5761 --
29 volumes. Statistic R = share of these volumes with >= 1 cipher item marked `ours`.
Expected: R about 0.7 (finding-aid foliation and our ink foliation differ on some volumes; a folder may name its leaf
only as "no. N" or by canvas). **Gate: R >= 0.60.**

## N1 folio-shift null (precision floor)

Same corpus, every item folio shifted by +37 (beyond the side and +-2 fuzzy window, not a gathering multiple), same
matcher. Statistic S = number of cipher items marked `ours`. Why it can differ from the real run: `ours` needs the
exact folio bound to the volume, so moving the folio changes which lines match (rule 3, a control that can vary).
**Gate: S_null <= 0.25 x S_real.**

## N2 volume-swap null

Each item's volume replaced by the next volume number not in the corpus (fr.N -> fr.N+1 if absent, else +2 ...).
Statistic S as above. Can differ: a line must bind the folio to that volume. **Gate: S_swap <= 0.10 x S_real.**

## K2 active edition

fr.2988 (cc49442s) gets `contact_first` = the Mary Stuart - Castelnau project; fr.3413 (cc49884s) and every non-Mary
volume get none. Gate: exactly fr.2988 (+ any volume whose items name Marie Stuart / Castelnau, listed) flagged.

## Offline tests (Usage 8a)

Must catch: a NOTES line 'BnF fr.3040 f.18r' marks fr.3040 f.18 ours; a _triage note naming fr.2988 f.1. Must NOT:
fr.29880 f.18 against that line; 'fr.3040 f.19r'; a line naming fr.3041 f.18r; a RESTRICTED.md folder; debosnys-1883.

## Outcome rule

All three gates met -> shelf grade `weak` remains the ceiling for a disk-only own-work scan (one development corpus,
no held-out set); a missed gate -> `weak` with both numbers, not re-briefed. No target status, key, reading or AUDIT.md
changes; `ours` is a lead for the scout, not a DONE (prior_work.py check 1 semantics stay per-slug).

## Amendment A (07:5x UTC, before any scoring; read from the parser, not from results)

Range notices (fr.3974-3995, fr.4050-4051, fr.4052-4053, fr.4133-4138, fr.4734-4736, fr.3693-3694, Clair./Dupuy
ranges) list items with a folio but no volume, so an item's volume is not known. For these the unit carries every
volume of the range; a hit is reported `ours?` (range-ambiguous) in column `ours_range`, and is NOT removed from the
open counts. K1 counts a range volume as recalled on an `ours?` hit and reports those volumes separately. A line that
names no volume is used only inside a `ciphers/<slug>/` folder whose slug carries a volume (fr3040-...), with that
volume as context; such lines in ciphers/_triage/ are skipped.
