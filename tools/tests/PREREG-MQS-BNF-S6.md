# PREREG MQS-BNF-S6 (S6b run) -- check-solved, premise check and intake gate on the pile survivors

Job: MQS-BNF-S6b (account 4, worker session_01CdUJXkzHzHFnXCAmMvMfCW), brief .claude/briefs/runs/2026-10-09-ytbiz-mqs-next-bnf-s6.md.
Written 21:4x UTC 9 Oct 2026 by date -u, pushed BEFORE any control below is scored. Disk only; no host request; Gallica not hit.
Credit: Lasry, Biermann and Tomokiyo 2023 (Cryptologia 47:2) pp.101-109, 191; Tomokiyo, cryptiana.web.fc2.com GL.htm and
francis.htm (cached sources/cryptiana/web/, fetched 2026-10-06); ours.

## Survivors (from S2A/S2B/S5, read on disk)
S2A/S2B found no undigitised pile above threshold; fr.2988 is the planted development pile (already ours,
ciphers/_triage/bnf-fr2988-f1-fr20506-f146.md, and contact_first). S5 listed BnF fr.3029 (notice cc494882) as the one
survivor with bare cipher items: nos 34 (f.67), 49, 59 (f.134), 66, 68, 70 (f.182), 72. The 26 S2B image-triage notices
carry no item list (volume-level only) and cannot take an item-level check-solved without images: logged, not run.

## Premise check finding (made while reading the caches, before any scoring)
Tomokiyo's GL.htm ("Decipherment of Hitherto Unsolved Historical Ciphers (by George Lasry)"), section "De la
Tremoille's(?) Cipher (??1520-1521): BnF fr.3029, BnF fr.3092", lists exactly these seven fr.3029 items (f.67 no.34;
f.100,105 no.49; f.134 no.59; f.162 no.66; f.172,176 no.68; f.182 no.70; f.186 no.72) and francis.htm says the cipher
"was broken by George Lasry in 2023 ... also broken by Norbert Biermann independently", with two raw decipherment
excerpts (f.67, f.186) in GL.htm's notes of 6 Dec 2023. --pile and --attribute kept them `open` because prior_work
check 3 grades the item line ("f.67 no.34 Lettre en chiffre.") CONTEXT: the "broken by" wording sits at section/page
level, never on the item's own line. Check-solved verdict for the survivor: found-solved (prior decipherment, Lasry 2023).

## Tool change (one option, bnf_findingaid.py)
`section_known`: a Tomokiyo CONTEXT row for an exact unit is read as known when, and only when, (a) the item's own
line carries no negation word (NEGATION), and (b) the enclosing section chain -- the nearest heading's body up to the
item line, each ancestor heading's own text and its body up to its first child heading, and the page's `#` title --
carries POSITIVE wording or the GL.htm title/achievement wording ("decipherment of hitherto unsolved", "provided
solutions"). Applied in item_status() (so --pile, --prior-work and the S6 report all see it), and a new
`--check-solved NOTICE.html` report that writes, per bare item, the anonymous-pile holder checklist (DECODE, Cryptiana,
cyphersolver, unsolved-ciphers, holder notice; searched / UNCHECKED with the cache path) and the verdict per item.

## Controls (gates fixed here; statistic = share of item lines graded known by the section rule)
- K-dev (development case, not a test): fr.3029 notice through --pile: open_bare 7 -> 0 expected.
- K1 held-out known answer: every GL.htm item line (volume from heading carried down, folio on the line) in the
  "Achievements in 2023" sections OTHER than the fr.3029/fr.3092 section, with no line negation. Expected >= 0.90.
  Weakness stated now: the page title alone licenses these, so K1 checks the plumbing more than the judgement.
- N1 line-negation null: GL.htm item lines that DO carry a negation word ("undeciphered", "remain unsolved"). Gate: 0
  graded known (the section rule would flip them if the line guard were broken, so this null can differ).
- N2 wrong-page null: every item line of unsolved.htm and unsolved-2026-09-24.htm (Tomokiyo's unsolved lists) with no
  POSITIVE word on the line itself. Gate: <= 0.10 graded known by the section rule alone (a section that mentions one
  solved sibling must not clear the rest).
- N3 folio-shift null: the seven fr.3029 folios +37 through prior_work check 3 + section rule. Gate: 0/7 known (the
  match is folio-bound, so a shift can differ from the real folios).
Gate for the option: K1 >= 0.90 AND N1 = 0 AND N2 <= 0.10 AND N3 = 0. Miss -> shelf `weak`, both numbers, no re-brief.

## Results (filled after scoring; nothing above is edited)
Scored 21:4x UTC 9 Oct 2026 by date -u. `python3 tools/tests/mqs_bnf_s6_controls.py` (disk only, 0 host requests).

| Control | Gate | First scoring | Final code |
|---|---|---|---|
| K1 GL.htm held-out items (2023 sections, not fr.3029/3092) | >= 0.90 | 47/49 = 0.959 | 47/49 = 0.959 (misses fr.3022 f.26, f.39: blocked by other pages' 'undeciphered' rows for the volume, conservative) |
| N1 own-line-negation items | 0 | **1/4 FAIL** (fr.3040 f.16 cleared via francis.htm, the GL.htm item line found by tomo_item_lines was not under the negation guard) | 0/4 (guard extended to those lines) |
| N2 unsolved-list items, no POSITIVE on the line | <= 0.10 | 0/8 | 0/8 (N small) |
| N3 fr.3029 folios +37 | 0/7 | 0/7 | 0/7 |

A second fix came from an existing test, not a null: test_bnf_findingaid_pile (fr.2988 open_named 2) failed when the
section rule cleared f.4 from misplaced.htm's "f.1 ... was solved by"; a section sentence naming another folio no longer
counts. Gate read on the first scoring: MISS (N1). Shelf grade **weak**, both numbers above; not re-briefed.

K-dev (fr.3029, notice cc494882 = cc504266/cc57784f copies): --pile open_bare 6 -> 4; --check-solved: nos 34 (f.67),
59 (f.134), 70 (f.182) found-solved; nos 49, 66, 68, 72 blocked by the tool (the notice gives no folio). By hand, from
GL.htm's own item list (no.N matched to no.N): no.49 = ff.100,105, no.66 = f.162, no.68 = ff.172,176, no.72 = f.186, all
in the same section; portal_status on those folios reads known. So all seven survivors sit in a cipher Tomokiyo reports
"broken by George Lasry in 2023" and "by Norbert Biermann independently" (francis.htm; GL.htm notes of 6 Dec 2023 give
raw decipherment excerpts of f.67 and f.186). Check-solved verdict for the S5 survivor: **found-solved** (prior
decipherment, not ours; key: published, Lasry 2023). No target folder was opened or changed (brief: no status change);
the orchestrator decides whether fr.3029 gets a ciphers/ folder or a CATALOG/LANDSCAPE row.

Intake gate: not run on a target (no fr.3029 folder exists and none was made). The --check-solved draft block names
DECODE, Cryptiana, both solver repositories, the notice and a folio range, and is held by intake_gate_check's holder
path only on 'glyph set' (no sign inventory without images): test_bnf_findingaid_s6.py asserts exactly that, so an
anonymous pile drafted from this tool stays `blocked` until a sign inventory exists. The 26 S2B image-triage notices
have no item list: no item-level check-solved is possible from disk; they wait on S4 (Gallica).

Premise check, for the record: the miss was a premise failure upstream -- S2A/S2B/S5 carried fr.3029 as an open pile for
three sessions while Tomokiyo's GL.htm, on disk since 6 Oct, listed every item. Suggestion (not done): run
--check-solved before any S4/S5 work on a pile survivor.
