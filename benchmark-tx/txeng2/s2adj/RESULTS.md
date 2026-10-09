# TXE2-S2ADJ: the frozen step-3 adjudication on the S2 reads, as a protocol repair (no score)

LANE TX-ENGINEER-2 (account 4), Opus 5.5 worker, Sonnet adjudicators; 9 Oct 2026, 22:13-22:2x UTC by date -u. Binding:
PREREG-txeng2-S2.md "Protocol repair" and PREREG-txeng2-10.md S2-ADJ (TX-RED F33 (a)).

**A protocol repair of the frozen pipeline's step 3, made before any score; no score run.** Openings of eval truth: 0. Not
opened: the truth TSV, the builder's committed/passA/passB.tsv, any decode under ciphers/fr16104-vivonne-spain-1572/tx/, key
values; tx_bench not run. Hosts: 0 requests.

## Inputs (unchanged)
- Queue: `../s2read/adjud_queue.tsv` (375 rows: 208 disagree + 167 agreed-uncertain). Only the 208 disagree rows were sent;
  the 167 agreed-uncertain rows keep the agreed reading (not sent).
- Crops: `ciphers/fr16104-vivonne-spain-1572/images/c106_f103r_L??_s{1,2}.jpg` (as the S2 readers saw them; never re-cut).
- Sheet: `../s2read/sheet_SIGNS.md` (the S2 readers' value-blind sheet, sha256 5e5090094fa5...).
- A/B per row from `../s2read/rec/disagreements.tsv`; base for agreed positions `../s2read/rec/ciphertext_draft.tsv`
  (the reconciler's aligned draft = the readers' common reading where they agree).

## Packets and calls
`build_packets.py`: the 208 disagree rows in queue order, 16 per packet -> **13 packets of 16** (a line may span two packets;
each packet's task names every crop, s1 and s2, of each of its lines). Task text `adjud_task_template.txt` (sha256 fe23b170ed90ff86091fd7de0d8d5ffa0f0650e053fd9376038c9a13776a300f),
the TXE-Q packet shape adapted to the text sheet: rows located by left/right neighbours and col; choose a candidate, another
sheet token, {words} or NONE from the image; "do not settle any row by a rule"; per row conf, viewed, note. Packets, tasks and
template committed with `SHA256SUMS_packets.txt` in f0f817f8e **before any call**.

One fresh claude-sonnet-5 subagent per packet, one call each, no resume (13 calls):

| packet | lines | tokens | A | B | other | NONE | viewed |
|---|---|---|---|---|---|---|---|
| P01 | L01-L03 | 108,174 | 8 | 7 | 0 | 1 | 16/16 |
| P02 | L03-L04 | 107,367 | 3 | 12 | 1 | 0 | 16/16 |
| P03 | L04-L06 | 107,590 | 8 | 6 | 0 | 2 | 16/16 |
| P04 | L06-L08 | 108,431 | 7 | 8 | 1 | 0 | 16/16 |
| P05 | L08-L11 | 111,014 | 5 | 10 | 0 | 1 | 16/16 |
| P06 | L11-L13 | 108,778 | 10 | 6 | 0 | 0 | 16/16 |
| P07 | L13-L15 | 108,617 | 4 | 12 | 0 | 0 | 16/16 |
| P08 | L15-L18 | 110,358 | 4 | 10 | 0 | 2 | 16/16 |
| P09 | L18-L22 | 110,147 | 9 | 5 | 0 | 2 | 16/16 |
| P10 | L22-L25 | 110,318 | 8 | 3 | 3 | 2 | 16/16 |
| P11 | L25-L29 | 110,186 | 12 | 4 | 0 | 0 | 16/16 |
| P12 | L30-L32 | 108,882 | 14 | 2 | 0 | 0 | 16/16 |
| P13 | L32-L37 | 111,185 | 5 | 10 | 0 | 1 | 16/16 |
| **total** | | **1,421,047** | **97** | **95** | **5** | **11** | **208/208** |

Each adjudicator's reply listed the crop files it opened: every packet listed every crop of its lines. Conf: H 3, M 120, L 85;
several adjudicators said the crops were hard to resolve at the resolution they saw, mainly S/s, y/g, 2/z, e/c. The 5 "other"
verdicts: L04 col 16 (A {2}, B z -> 2), L08 col 16 (A S, B none -> s), L22 col 23 (2/z -> x), L24 col 26 (2/z -> x),
L24 col 46 (2/x -> P). viewed = yes is the adjudicator's own report per row (`adjud_out.tsv`: packet, A, B, verdict,
class, conf, viewed, note); it is not otherwise checkable.

## Output
`assemble.py`: passZ_S2b = the draft with the verdicts applied at the 208 splits (NONE drops the position), agreed and
agreed-uncertain positions unchanged, pos renumbered per line. **passZ_S2b 1,907 signs** (passZ_S2 1,891); 79 positions
differ from the draft's sign at a split (draft = pass A there), 11 dropped as NONE. Against the earlier passZ_S2 adjudication
the verdict differs at 105 of the 208 split rows (passZ_S2 kept pass A at 199 of them unviewed). passZ_S2.tsv stays on disk,
untouched, unscored.

| file | sha256 | commit |
|---|---|---|
| packets/ (13 queues + 13 tasks) + adjud_task_template.txt + build_packets.py | SHA256SUMS_packets.txt | f0f817f8e |
| adjud_out.tsv | a498e789380a897f8eda87f78ef7681c99883d4273f726d3df2fc30313e79d76 | c98ae9ba2 |
| assemble.py | 8747d2cbfb10247677e401ef066e192adf93639566ad3594ba2c4d01cb3b095b | c98ae9ba2 |
| outputs/vivonne1573-f103r-confirm2/passZ_S2b.tsv | da404e3504b6dfc9702fd24e345bffb9eab14d9db8b1b36abdb4a5bff7ffe520 | c98ae9ba2 |
| outputs/vivonne1573-f103r-confirm2/passZ_S2.tsv (untouched) | b5e6ab9f847fadb2175253e4aa0de8edf7743c14fe8fa9491130d393691ec928 | 6ff5fb060 |

Not done here: a fresh doubt feed for passZ_S2b (doubt_S2.tsv is keyed to passZ_S2's positions); the brief did not name one.
Cost: the orchestrator get_session reading (13 Sonnet subagent calls).
