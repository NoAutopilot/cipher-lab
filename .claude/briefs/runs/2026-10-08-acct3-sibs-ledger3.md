# Siblings and ledger round 3 (account-3 orchestrator, 8 Oct 2026 09:5x UTC). default-lane common tail; Opus 5.5 lane orchestrators.

Why: the board stands at 58 counted (75 by 14 Oct is the owner's benchmark). Every one-audit N3+ D2+ item already has its second
audit; the twelve two-audit D1 items need more reading, not more auditing. New counted items now come only from NEW readings of
UNGLOSSED leaves under keys already in hand. A leaf with a period decipherment on it reads N0 (rule 10), so glossed siblings do
not move the board; use their glosses as C-grade known answers, not as targets. Source list: SIBLINGS-2026-10-08.tsv
(SUCCESS-SIBS, 8 Oct; p and cost are the compiler's estimates, not claims). Depth rulings follow
.claude/briefs/runs/2026-10-08-acct3-depth-bar.md. Expected counted gain is modest (0.1-0.3 per unit); report honestly either way.

Common to both lanes:
- Before spawning: check this account's usage bar; on allowed_warning write one ROOM line and stop.
- Paste `python3 tools/intake_gate_check.py <target>` before any deep-work worker brief; nonzero exit blocks it.
- Per unit: transcription with the mandatory crop step (`tools/iiif_lines.py ... --out`, paste the command), two blind
  passes + one reconciliation priced per pass (Usage 6), decode with `tools/decode_key.py <t> --check`, and the matched control
  (shuffled-key or shuffled-order, one that CAN differ for the statistic, rule 3) before any reading is claimed.
- A reading that beats its control goes to a SEPARATE first-verifier session (CLAUDE.md verifier template: N-class, key source,
  depth per the depth bar, AUDIT.md, status.json row, SO row at N3+). Never verify in the session that read. After a first audit
  at N3+ D2+, add one WORK-QUEUE row for its second audit on a different account (shape: AUD2-LS-C in
  .claude/briefs/runs/2026-10-08-acct3-ledger2.md) and name it in ROOM for the account-3 orchestrator.
- Workers report what was found and where it was not found; do not classify novelty. Rule 10 wording only.
- Stop before a unit that would cross 80% of cap or box. Hand-off in STATUS.md, LEDGER rows, no orphaned triggers at close.

## SIBS-READ (account 1), lane orchestrator, cap $45, box 8 h: unglossed siblings under keys in hand
Units, in this order (skip any whose NOTES show it already run since 8 Oct 04:45 UTC; read the target's "## Siblings" section):
1. fr16104-vivonne-spain-1572: fr.16104 ff.157-159v, 5 Sept 1572 ("sans le dechiffrement", same pool), key.tsv/key_tomokiyo.tsv via
   the viv54 pipeline, shuffled-key control. ~$3.
2. lodewijk-van-nassau-1573-74: WVO 5810 (6 Jan 1574) with key_full_v2.tsv/key_5801.tsv, shuffled-key control (5811 is printed:
   skip it). ~$1.5.
3. august-van-saksen-1561-64: WVO 53 page 2 unread cipher block, key_53.tsv. ~$3.
4. fr3621-dinteville-1592: the fr.3621 letters of 5 and 13 July 1592 ("not checked") and fr3631 no.27 f.28 (14 June 1593), each
   with f130/key_dk.tsv and a shuffled-key control; check length before reading. ~$3 each.
5. hellen-frederick-1752: transcribe the R4376 (f.56, 1754) table, test it on R1049 (7 Sept 1756) with control. ~$8.
6. ceppo-nevers-fr3251-1570s: fr.4715 f.20 (unnamed to Nevers, Mar 1571): count cipher signs first; key rank test only if long
   enough. ~$2.
Then the first verifiers for whatever cleared its control.

## ST-LEDGER-3 (account 2), lane orchestrator, cap $40, box 8 h: the Eckert leftovers ST-LEDGER-2 named
Read the ST-LEDGER-2 handoff in STATUS.md (around line 6150) and ciphers/eckert-1864/NOTES.md first. Work, in order:
(a) the "10" book check for E69 and E75 (~$1.5); (b) the 1865 key-book check (~$1); (c) Cipher No. 9 entries of mssEC 19
(decode_no9.py, ~43 guessed, ~$2); (d) remaining unread 1862-ledger entries (mssEC 15) with the eckert-1862 key (~$5);
(e) mssEC 18, the parallel sent ledger (Huntington object 10074): fetch the 21-22 Apr 1864 pages via the documented
CISOSEARCHALL route, transcribe, apply key.md, with the same pre-filter as mssEC 19 (~$6); (f) object 5952 (Fort Monroe 1864-65)
only if (a)-(e) run dry. Readers Sonnet where the filter makes them mechanical; first verifiers Opus, separate sessions, LS-V
pattern, then WORK-QUEUE second-audit rows as above. An entry whose clear text is in print (OR, the Huntington transcription,
the press of the day) is N1/N2: record it and move on.
