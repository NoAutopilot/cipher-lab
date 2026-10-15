# PREREG-AVS-W1 (15 Oct 2026, 16:4x UTC by date -u; worker AVS-W1, account 2, for LANE DEFAULT-A2-1616-15)

Job: brief `.claude/briefs/runs/2026-10-15-ytbiz-default-1616-jobs.md` "### AVS-W1". WVO 153 (Oranje -> August, 1 Sept 1566) is a
KEY SOURCE: its plaintext survives on the leaf in two period decipherments (W1 p7/f.5, W2 p8/f.6). This job firms `key_153.tsv`
(System B / key_98 family) for the unread letters of that family (WVO 126's key-level M tokens, WVO 58 is System A and not
affected, WVO 175 pp.3-8 and any further System B letter); it is not a reading of an unread text.

Material: 00153.pdf (resources.huygens.knaw.nl, 1 request), p7 (W1) and p6 (cipher lines 2 and 6, 14-19) cut with
`tools/iiif_lines.py --image <scratch> --out <scratch> --debug`; scratchpad only. One Opus look (this worker) at W1's
stretch matching cipher lines 10-20 ('die andern verfolgen' to 'erlangen'), and one at the '6~' tokens.

Decision rules, registered before W1 is read and before any grade changes:
1. W1/W2 check (rule 4). For every valued token of cipher lines 10-20, take W1's letter at the aligned place.
   a. W1 = W2 there: the token keeps its grade (no upgrade from this alone).
   b. W1 != W2 there and the cipher agrees with one witness: the token keeps the agreeing witness's value at C, and the place is
      listed as a W1/W2 difference (spelling); if the cipher agrees with neither: M, listed.
   c. A token held M with value withheld ONLY because the cipher spelling departs from W2 (the held spellings in recon_153.py's
      NOTE) gets W1's letter at grade C if and only if W1 spells the word exactly as the cipher does at that place; otherwise it
      stays held.
   d. A key_153 class whose lines 10-20 tokens W1 contradicts in two or more places with no spelling explanation goes to M.
   W1 words that cannot be read on the crop are 'unread', not counted either way.
2. '6~' tokens (line 2 'augspurgis(ch)e', line 6 'Caluinis(ch)'). Compared by this worker's eye (not blind) with the three 6f
   tokens of lines 14, 15, 19 and the plain 6 of the same lines. Outcomes: (i) same long-flag form as 6f -> the two tokens are
   relabelled 6f with value 'sch' at M (6f's value remains split s/sch, so class 6f stays M; no count-based settlement);
   (ii) different form (a plain 6 with a mark, or unlike 6f) -> they stay 6 with value withheld, M; (iii) not settled on the
   crop -> unchanged. In no outcome does any class move to C from this look.
3. Gates after any change: `python3 w153/controls_153.py` must still PASS (a) all valued tokens and lines 10-20 above their
   shuffled p95 and (b) key_153 vs key_98 pre-fixed map above permuted p95; `python3 check_153.py --check` exit 0. A FAIL
   reverts the change and is reported.
4. Stop rule: stop before a unit that would cross 80% of cap (USD 2.5) or box (50 min, end 17:24 UTC). Requests: huygens <= 3.
