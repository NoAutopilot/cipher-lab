# PREREG MQS-SHEET-REFUSAL (LANE MQS-2, account 4), written 2026-10-09 07:3x UTC by date -u, pushed before any test is scored

Change: tools/decipher_sheet.py refuses a key or reading sheet when the target's key family has an open blind sort in
tools/data/sorter_families.tsv (column open_blind_sorts non-empty), the same way it refuses a RESTRICTED.md folder.

Target -> family: a table in decipher_sheet.py (KEY_FAMILY_TARGETS) naming the folders of each sorter family:
nevers-birago-1572 -> ciphers/nevers-birago-fr3251-1572 (the key folder; sorter rows f.117r/f.168/f.144r, ASKS 118) and
ciphers/birago-fr3252-1571-72 (its no.77 f.117r fits the 1572 key, NOTES.md "Design checks", and it uses the key by path).
A job whose key path resolves inside a mapped folder is also that family (catches a sibling folder not yet in the table).
Not in the family: ciphers/birago-nevers-1571 (the Nov 1571 numerical system, a different key). `--key-family NAME`
names it explicitly; `--families TSV` points at another register (tests only).

Known answer (register as committed at this prereg): K1 Birago 1572 (nevers-birago-fr3251-1572, key and reading) refused,
exit via SystemExit naming the family and the open sort ids; K2 birago-fr3252-1571-72 refused; K3 Gramont (fr2980-gramont)
and K4 Danzay (fr20140-danzay-1557) render (rc 0, non-empty HTML).

Control that can differ (rule 3: the manipulation acts on the statistic, refused or not): the same four targets against
(N1) a temp register with the Birago row's open_blind_sorts emptied -> K1/K2 render; (N2) a temp register listing an
open sort for a family mapped to fr2980-gramont via --key-family -> Gramont refused. If the refusal followed the slug
alone, N1 would still refuse; if it ignored the register, K1 would render.

Gate: all of K1-K4 and N1-N2 as stated, and every pre-existing test in tools/tests/test_decipher_sheet.py keeps its
result (pre-existing Birago renders run against an N1-style temp register, since the live register refuses them). Miss ->
shelf weak, not re-briefed. Offline, no host, no render written for the owner, nothing outside TMP.
Credit: Lasry, Biermann and Tomokiyo 2023 (Cryptologia 47:2); ours (blind-first rule, TRANSCRIPTION.md).
