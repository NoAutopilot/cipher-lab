# LANE DEFAULT-account-1-20261015-0447 jobs (account 1, lane orchestrator session_01E6MxMUXsNYgh6jrFhCcg4c) -- 15 Oct 2026 05:0x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 04:47-14:47 UTC 15 Oct. Gate 0a: SESSION-SWEEP-account-1 stale-claimed since 5 Oct
22:40, proceeded. VERIFY-BACKLOG.tsv (02:40 15 Oct): high rows Birago/ceppo (off limits), rest audit2 on N0/N1 items (known text; guardrail).
Backlog = the A1-0206 handoff next list (STATUS.md) + `next_steps.py --hot-only` runnable rows + the A2-0209 handoff's unsent googleapis
queries. Parallel lane DEFAULT-A4-0437-15 (account 4) holds lodewijk-van-nassau-1573-74, antt-linhares-chave, hellen-frederick-1752,
fr16142-noailles-constantinople-1571, colbert26-lathuillerie-1644 and na-suriname-map-1781: none of them is picked here. Excluded: Birago
family, Armstrong, Debosnys, VIV-KEYSTONE (fr16104/fr16105/fr16106), BNF-FOCUS folders and holdings (fr2933, clair1161, fr5160, fr4687,
clair1067, clair1108, dupuy155, dupuy468, fr3982, fr3985-3990, no.60), cipher-lab-private.
Intake gate 04:5x UTC (tools/intake_gate_check.py, exit 0 each): pro3055-clinton-1779, baluze167-davaux-1637, fr4712-nevers-duchesse,
fr5761-election-1519, fr4735-monluc-lansac-poland-1573, eckert-1864.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-14-acct1-default-1840-jobs.md` (read it in full, and the
files it points to), with these substitutions:
- address every ROOM line "for LANE DEFAULT-A1-0447-15 (account 1)"; export `CIPHERLAB_ACCOUNT=account-1` before any tools/room.py call;
- first actions: `git fetch origin && git checkout -B main origin/main`, `date -u`, read the last 60 ROOM.md lines (if another session
  claimed your folder in the last 6 h with no done line, post a "stood down" line and stop), post a claim line with your box end time;
  fetch and rebase immediately before every push (`python3 tools/room.py --push <paths>`; if it reports a failure, fetch, rebase, keep both
  sides of any ROOM.md or NOTES.md conflict, and push once more);
- every claim/halfway/done ROOM line ends with "usage: not readable here" (get_session is not available to workers);
- price every look: a vision call is a unit (~0.5-1.0); state units x rate in your claim line; stop before a unit that would cross 80% of
  cap or box. The orchestrator reads get_session at 30 min and interrupts at 1.3x cap.
- every other rule there holds unchanged (shared-host take/release lines, halfway line, no images in git, gaps_check on `partial`, no
  novelty words, no AskUserQuestion, `date -u` before any time, "cost not visible to this session").

## Wave 1 (05:0x UTC 15 Oct)

### CLIN-247 (Opus, cap 5, box 75 min, image-uab.canadiana.ca <= 20): pro3055-clinton-1779 p.247 cols 3-8 (letter 3077)
A1-0206 next 1: "p.247 cols 3-8 for 3077 (~3.5, same method)". Exactly CLIN-SIB/CLIN-SIB2/CLIN-SIB3's method (read their NOTES sections and
PREREGs): iiif_lines.py crops (command pasted before the first subagent call), two blind passes + one reconciliation unit, the same B2 gate
and page-permuted-key control, registered before decoding. p.247 cols 3-8 only. No images in git. NOTES "## CLIN-247", gaps + Verdict,
gaps_check.

### BAL-169 (Opus, cap 3, box 60 min, openapi.bnf.fr <= 15): baluze167-davaux-1637 the last f.22r numerals on 169 c172-188
Verdict: "the f.22r last numerals (13:, plain 16, 65) on 169 c172-188 by the same test (~$2)". Same instrument and shuffle control as BAL-F22R
(read its section first). One numeral per call, value-free crops. NOTES "## BAL-169", gaps + Verdict, gaps_check. Do not start the c275 7/5
search, the c283 tail or the googleapis phrases (wave 2).

### F4712-HAND (Opus, cap 3, box 60 min, openapi.bnf.fr <= 12): fr4712-nevers-duchesse digit-rich f.13r / f.10r hand comparison
Verdict: "1 internal gap (same-writer basis, not-attempted) ... cheapest next: a digit-rich f.13r/f.10r hand comparison, ~$2". Read the
census sections (F4712-C83, F4712-END) and whatever names the same-writer gap first. Pre-register in NOTES (or PREREG-F4712-HAND.md) the
features compared (digit forms 0-9, ligatures, any recurring sign) and a control (the same comparison against a different hand in the volume)
before looking. Value-free crops, <= 12 crops per call. Result is a same-writer lead graded M at most, never a reading. NOTES "## F4712-HAND",
gaps + Verdict, gaps_check.

### ELEC-END (Opus, cap 2, box 45 min, openapi.bnf.fr <= 16): fr5761-election-1519 ff.172v-179v canvases
ELEC-WALK's next (1): "read the remaining ff.172v-179v canvases at 600 px (about 13 requests, ~$1) for nr. 357/383". Same method as ELEC-WALK
(read it). If nr. 357/383 are absent, look up the fr.5756 Gallica ark only (one SRU/catalogue request) and write it into the Verdict as the
next step; do not start the fr.5756 census. Status stays as written unless a pair is found (>= 2 occurrences per sign before any C grade).
NOTES "## ELEC-END", Verdict.

### MONL-L11 (Opus, cap 6, box 90 min, disk only): fr4735-monluc-lansac-poland-1573 c268 L11-L15
Verdict: "c268 L11-L15 two blind passes + reconciliation, then align_c268.py, ~$3". MONL-VB ran 2.3x cap: price by crops per call (<= 12 crops
per call, ~0.5 per call); 5 lines x 2 blind passes + 1 reconciliation = 11 units -- state the count in your claim and stop before the unit that
would cross 80% of the cap. Read MONL-SORT, MONL-ALIGN, MONL-VB first; same crop and blind rules (no key value, no machine label, no decode in
a blind call). Then align_c268.py --check and the shuffled-clear control (200). NOTES "## MONL-L11", gaps + Verdict, gaps_check.

### GB-PASS4 (Opus, cap 2, box 45 min, www.googleapis.com only, <= 40 requests at >= 2 s, key + `&country=US`): eckert-1864 + thurloe-printed
googleapis answered 200 at 04:5x UTC 15 Oct. Retry of GB-PASS3's unsent queries (read GB-PASS2/GB-PASS3 in each NOTES.md): eckert-1864
`fortmonroe/eck_gbpass_gb.py --gbpass3` (E592 and looser E589), GB-2-form control first; thurloe-printed `gb2_verbael_snip.py` on
vZzvg46MRdEC / T2JVAAAAYAAJ (Beverning 27 June / 22 Aug 1653, No. 37 pp.252-253). Hold the host with ROOM "googleapis take"/"release" lines.
On 503/429 one retry after >= 60 s; a second failure stops the job; if eckert fails twice, write the LOCAL-QUEUE row its gap names. The
baluze167 googleapis phrases are NOT in this job (BAL-169 holds the folder). A snippet hit is a location, not a reading; quote what it
carries. Each folder: its NOTES section, Remaining gaps / Escalation, gaps_check.
