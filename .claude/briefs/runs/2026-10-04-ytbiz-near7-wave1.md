# LANE-NEAR7 wave 1 (4 Oct 2026, written 12:2x UTC by LANE-NEAR7, account 2 / ytbiz, session_011jxC5ygqRnFKn5qTCJAPNz)

Common rules: the "Common to every job below" section of `.claude/briefs/runs/2026-10-04-ytbiz-near4-wave1.md`, with
"LANE-NEAR4" read as "LANE-NEAR7" everywhere (claims, done line addressed "for LANE-NEAR7 (account 2)").
Intake gates (pasted by LANE-NEAR7, 12:1x UTC, both rc=0):
`fr16104-vivonne-spain-1572: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
`hellen-frederick-1752: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`

Lane goal (orchestrator's brief): move one Vivonne piece from D1 to D2 (rule 4a). Audits so far read N3 / D1 because transcription noise
(err_2reader 0.15-0.30, label splits) leaves no clause above the authentication distance (about 42 letters, AUDIT 2 4a). **The depth
verdict is not yours**: a fresh account-3 audit sets it. You produce a cleaner transcription, a re-decode under label rules you
pre-registered before re-decoding, and an honest list of the longest repair-free stretches (letters, liberties counted as AUDIT 2 counts
them). Never write D2, "deciphered" or any rule-10 word.

## Shared by both Vivonne jobs (N7-VIV53L, N7-VIV54L) -- same folder, same time
- Read NOTES.md sections N5-VIVK, N5-VIV54, N6-VIV53, N6-VIV53B, AUDIT.md AUDIT 1 and AUDIT 2 (4a and Next steps), tx/SIGNS.md, TRANSCRIPTION.md,
  and `python3 tools/lookalike_pass.py --help` (subcommands confusion, packet, reconcile, audit, audit-score).
- Isolation: files named `*<NN>L*` / `tx/lookalike<NN>/`; never edit what regenerates reading_piece53/54/63.tsv (`--check` on all three must still
  pass at your push); your re-decode writes `reading_piece<NN>_L.tsv` via a new `tx/viv<NN>L_decode.py --check`. Do not touch key.tsv or any ink 63
  file (VIV63-A1 is auditing ink 63 now). NOTES section appended at the end after `git pull --rebase` immediately before the edit.
- Step 1, PREREG-N7VIV<NN>L.md pushed BEFORE any re-read or re-decode, naming: (i) the label rules -- at least the ': :' pair read as ONE sign
  (state which key cell), the a/u, 4/+/p, z/3, S/d pairs settled only by the lookalike 2-of-3 rule, nothing settled by "what decodes better";
  (ii) the D2-candidate statistic: the longest stretches of decoded text needing no letter repair, with word division and every other liberty
  listed per stretch exactly as AUDIT 2 4a lists them (the auditor re-counts; you list); (iii) an error measure: `lookalike_pass.py audit` on
  agreed signs with plants (--plant 0.05) and audit-score, so a true-error estimate sits beside the 2-of-3 residual (the residual is agreement,
  not accuracy); (iv) the b2 gate + 200-wrong-key specificity re-run on the re-decode exactly as PREREG-N6VIV53B, rule unchanged.
- Units (state in NOTES before the first subagent call): confusion + packet are scripts; ONE Sonnet re-read call per page's flagged tiles
  (crops only, never a full page: TRANSCRIPTION.md / Usage 6), ONE audit re-read call for the whole piece, ONE reconciliation step by you, priced at
  ~USD 1.2 per call. Stop before a unit that would cross 80% of cap or box.
- If the ': :' pair or a label rule needs a key-cell decision you cannot settle from tx/SIGNS.md and the key image, it stays M and goes in your
  section as a key question; never pick the reading that decodes better.
- print_check on any new repair-free stretch >= 20 letters (phrases_<NN>L.txt). Report what was found and where it was not found; do not
  classify novelty. Done line: err_2reader before/after, 2-of-3 residual, planted-audit error estimate, H/M/U before/after, b2 and specificity
  numbers beside their controls, the three longest repair-free stretches (letters + liberties). If b2+specificity pass: "piece <NN> ready for
  audit (depth re-check)".

## N7-VIV53L -- ink 53 (fr.16104 ff.170r-171v, to Anjou, 5 Sept 1572): look-alike pass + pre-registered re-decode (Opus; cap USD 7; box 110 min)
Four cipher pages (170r, 170v, 171r, 171v): 4 tile re-read calls + 1 audit call + reconciliation = 6 units ~USD 7. Inputs: tx/f170r..f171v
_passA/_passB(_c)/_rec.tsv, images/p53 crops (regenerate from the manifest's commands if absent). Also re-check the f.170r-171r gloss rows only
if a label rule changes a glossed position (the registered gloss gate result 0.577 stands and is not re-run as a gate).

## N7-VIV54L -- ink 54 (fr.16104 f.173r-v, to the King, 7 Sept 1572): the same, two pages (Opus; cap USD 4.5; box 80 min)
Two cipher pages: 2 tile re-read calls + 1 audit call + reconciliation = 4 units ~USD 4.5. The a/u "qae" confusion (AUDIT 1) is the named target.
If b2 was never run on ink 54 (N5-VIV54 used the gloss gate), run it now under the same PREREG with its two positive controls, as N6-VIV53B did.

## N7-HELDK -- hellen-frederick-1752: R4386 (f.75) and R4388 (f.79) full-size dockets/band heads for the 1763 letters (Opus; cap USD 3; box 45 min)
NOTES N6-HEL81 and its Remaining gaps. One DECODE login (`NODE_PATH=$(npm root -g) node tools/decode_browser_login.js`, try `--guess-fullsize`),
both records' pages to scratch only (never committed), read docket, header, holder, code range and whether cells carry meanings. If either is a
filled 1763 Hellen table that fits R1045-R1048/R1060/R1061 (code range, French, a holder or date), name it and price the transcription + --key
test as the next step; do not transcribe in this job. Output `key_search/R4386-R4388.tsv` (same columns as R4381-R4408.tsv), NOTES "N7-HELDK",
gaps refresh + gaps_check OK. The codes 1-800 gap is NOT this job (R4370/R4372 retired under rule 3; its named next step is the Fagel 5177
phrase corpus). Report what was found and where it was not found. Scrub the account name from anything saved.
