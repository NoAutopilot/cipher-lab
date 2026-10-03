# hessen-daenemark-1672: hypotheses and data conflicts

## Nomenclator conflicts with HCPortal key 255 (logged GAPS163, 3 Oct 2026, account-4; rule 4)

Key 255 (HStAM 4 d Nr. 1234 ff.13-16, "Clavis ... mit Secretario Lincker 1666") and this letter's own bold-hand glosses
give different values for two codes. These are not settled by majority, and neither value is merged into the other's
row: key_gloss.tsv carries the letter's gloss value, and key.tsv carries only key 255's letter table, no nomenclator.

| code | letter gloss (witness) | key 255 (witness) | reading |
|---|---|---|---|
| 229 | Berlin: p2:17 and p3:5, both blind passes read the gloss both times (C) | Frankreich: key 255 f.13-16, 1666, same sender family (Lyncker to the Kassel chancery) | different list; the letter's 229 stays Berlin (C) in this letter only |
| 303 | allian?e: p3:26, one letter unsettled (M) | Munster: preview read of keys/hcportal_key255_0014.jpg (M) | different list; 303 stays M |

Context: every other gloss-pinned nomenclator code here (437, 447, 601, 602, 605, 625, 634, 641, 651, 653, 681, 690,
768, 774, 775, 834, 5756) lies above key 255's 180-407 range. Key 255 also has Dennemarck at 184 and 212, where the
letter has 601, 602 and 605. So the 1672 letter used a different nomenclator, with the letter table kept, or nearly
kept: see NOTES.md GAPS163, where 2 of 7 letter-glossed groups disagree with the 1666 table. Witness direction and
date: the letter is Lyncker (Hamburg) to Chancellor Vultejus (Kassel), 4/14 May 1672 (M, siblings lookup). Key 255 is
dated 1666 and names the same secretary. Neither witness is an H-grade period decipherment of this letter's codes,
except the gloss itself.

## Nomenclator list identification (GAPS176, 3 Oct 2026, account-4)

| hypothesis | control | target | verdict |
|---|---|---|---|
| a key table on disk carries the 1672 nomenclator (18 gloss-pinned codes) | positive control, 3/4/6/9 planted values in a decoy key: real 3/4/5/8 vs shuffle p99 2/2/2/3, all flagged | 224 key tables: 0 hits in total, 0 candidates (shuffle p99 0 for every key) | no list on disk; DECODE 1650-1690 Marburg/Danish keys = 4687-4692, all opened, none matching; list needs the archive (keys/nomen_list_match.py) |
