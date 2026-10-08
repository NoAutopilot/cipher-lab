# LANE FAMILY (standing; blast refill brief for account-2). Read `.claude/briefs/lane-common-blast.md` first.

Scope: everything that is NOT the Huntington ledgers and NOT a Gallica fetch -- letters and leaves in the Dutch (WVO/Huygens
retroboeken, Nationaal Archief, KHA requests already answered), German (Dresden SHStA images on disk, Bavarikon/BSB, Hessen/Marburg,
Arcinsys), Iberian (ANTT digitarq, RAH via OAI-didl + browser_fetch, BNE), British and Irish (TNA Discovery, BL catalogue, Thurloe and
other printed pairs on IA, Huntington Blathwayt/Stowe), DECODE-held and Scandinavian families, plus BnF items whose images are already
on disk. Start from the newest LANE FAMILY handoff in STATUS.md.

Supply, in order: (a) `python3 tools/next_steps.py --hot-only` runnable rows in these families; (b) SIBLINGS-2026-10-08.tsv rows with
state unread-unglossed and a key in hand (the SIBS-PREMISE list in .claude/briefs/runs/2026-10-08-acct3-sibs-ledger3.md "Next sibling
round"); (c) pools: KEY-OFFICES.tsv rows whose office/key family has unread letters on the same host -- list them, run check-solved on
the best three, then read under the key in hand with a control; (d) `tools/design_prior.py` on unread letters of a key family before an
attack family is chosen. Every item goes through prior-work-step.md (checks 1-4 before any transcription; 5 after decode).
Prefer items in sign pools of 2,000+ signs and items with a key or period key in hand (CLAUDE.md selection rule); BnF-held items win
ties when images are on disk.
