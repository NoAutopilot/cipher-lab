# ST-LEDGER-3 worker brief (account 2, LANE ST-LEDGER-3, session_01PJJSq4hvT8sJovCacbSYX1; written 8 Oct 2026 10:1x UTC)

Parent round: .claude/briefs/runs/2026-10-08-acct3-sibs-ledger3.md, section ST-LEDGER-3 and its "Common to both lanes" list (read
both). Method, steps 0-4 and the reader/verifier sections are those of .claude/briefs/runs/2026-10-07-acct1-st-ledger-workers.md
(header steps 0-4, "Wave 2" LS-R1/LS-R2 and LS-V1/LS-V2) with the changes A-C of .claude/briefs/runs/2026-10-08-acct1-st-ledger2-workers.md
(commit every two entries and push; never hand a step off; readers read crops themselves, no subagents; "key not in hand" below 80%
coverage of an entry's code-word tokens). Read CLAUDE.md, the LANE ST-LEDGER-2 handoff in STATUS.md, and the worked examples
ciphers/eckert-1864/NOTES.md "## LS-R7" and AUDIT.md "## AUDIT (LS-V7)". Every ROOM line ends "for LANE ST-LEDGER-3".

Intake gate (pasted 10:1x UTC): `eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`
(exit 0); `eckert-1862: partial (line 3) -- ... found within 6 lines` (exit 0).

Lane points for every reader:
- Before decoding, assign the book per entry by vocabulary share (tokens in key.md vs key-no2.md vs key-no9.md; LS-V6 caught E65 read
  with the wrong book). Record the three shares in your NOTES table.
- Pre-filter before reading: an entry whose plain words hit the OR (entries-mssEC19.tsv `or_cov`, or a script grep of the cached OR
  `_djvu.txt` set for 1865 rows incl. OR ser. I vols. 46-49) is recorded N1-likely with the page and not decoded further.
- Matched control per entry, one that can differ for the statistic (rule 3): decode the same entry with the other two books and with
  a meaning-shuffled copy of the chosen book (meanings permuted within the key's own table, seed fixed); report how many tokens give
  a grammatical clause under each. A reading is claimed only where the chosen book beats all three.
- IDs: fetch first and take the next free one (E76.., N2-BP.., O9-AK..; check every ciphertext file and reading.md).
- Do not commit OR djvu text, page images or other bulk caches; reuse sources/ia-fulltext/print-check/ and scratch.

---

## LS3-K (Sonnet 5.5, cap $3, box 60 min): two script checks, no reading
(a) The "10" book for E69 and E75 (NOTES "## LS-R7", key-not-in-hand block). Search the Huntington CONTENTdm collection p16003coll11
    (documented `CISOSEARCHALL^TERM^all^and` clause, sixth path segment 1, `dmGetItemInfo` for full notes) for mssEC 37-76 titles or
    notes naming "No. 10", "Ten", "10" or a Halleck/governor list, and Tomokiyo sources/cryptiana/web/civilwar1.htm for a Cipher No. 10.
    If a book is found and its page text or images are reachable, compute each of E69/E75's code-word coverage under it (counts only);
    no reading unless coverage >= 80%, and then only the counts plus "readable, next: reader" in NOTES. If none: one line naming every
    search run (terms, hits), and the gap stays no-key-material.
(b) The 1865 key-book check (ST-LEDGER-2 handoff, Left (a)): for every unread priority-1 1865 row of entries-mssEC19.tsv with words
    >= 30, the share of non-function tokens in key.md, key-no2.md and key-no9.md's code-word columns; the same three shares for every
    read E / N2 / O9 entry as the labelled control. Write `ciphers/eckert-1864/key-share-1865.tsv` (pointer, page, entry, header date,
    three shares, best book, margin) and in NOTES the three control distributions (median, p10, p90) and the 1865 distribution, with a
    one-line verdict per book: the 1865 rows whose best-book share sits inside that book's control p10-p90 are "readable with No. N";
    the rest "book not in hand (Nos. 3/4)". Count both. No 1865 reading in this job.
NOTES section "## LS3-K (8 Oct 2026, account 2, for LANE ST-LEDGER-3)". gaps_check after.

## LS3-R9 (Sonnet 5.5, solver; cap $4, box 90 min): the unread rows guessed old vocabulary (Cipher No. 9 / mssEC 67)
Entries (pointer/page/entry_on_page), lowest or_cov first, 1864 before 1865: 8946/54/2, 9015/123/1, 9111/219/1, 9143/251/1,
8919/27/2, 9054/162/2, 8893/1/1, 9168/276/2, 9274/382/0, 9283/391/1. Read with key-no9.md and decode_no9.py (`--write`, `--check`);
an entry that turns out No. 1 or No. 2 goes to that file under its next free ID. The 1865 rows (last three) only after LS3-K's
key-share line is in ROOM or NOTES, and only if it calls them readable with the book you would use. About 0.5 per entry; stop
before an entry that would cross 80% of cap or box. NOTES section "## LS3-R9 (8 Oct 2026, account 2, for LANE ST-LEDGER-3)".

## LS3-R18 (Sonnet 5.5, solver; cap $5.5, box 110 min): mssEC 18 (object 10074), the parallel sent ledger
Premise already on file, do not redo it: RUN6-ECK (eckert-1864 NOTES "## mssEC 18 check for E4/E5 copies", 5 Oct) took the 21-23 Apr
1864 pages (pointers 9710-9720, page n = pointer - 9660) as volunteer text only, no images; A3V3-ECK18 (eckert-1862 NOTES, 4 Oct)
ran all of mssEC 18 through key.md from the volunteer text: 28 fully keyed book-1 entries, 9 in OR, 19 not found in OR vols. 32-46,
none image-checked; 9947.505 and 10020.609 already carry audits in ciphers/eckert-1862/AUDIT.md -- skip both.
Work, in order: (1) the 21-22 Apr 1864 pages 9714-9717 from the image (fetch via the documented CISOSEARCHALL / item API route,
crops with `tools/iiif_lines.py --image <file> --out <scratch dir>`, paste the command): every entry that is book 1 or book 2 and
not in OR, transcribed from the crops and decoded; (2) then, in this order, the not-found keyed entries 9730.87, 9731.89, 9812.208,
9855.295, 9858.300, 9866.320, 9901.399, 9908.417, 9928.458, 9939.484 -- for each first grep OR vols. 47-49 too (A3V3 did not search
them) and the Butler/Grant/Lincoln editions already cached; then image, crops, transcription against the volunteer text, decode.
File them in ciphers/eckert-1864 (ciphertext.txt / -no2.txt) under the next free IDs, with "mssEC 18 p.N, pointer P" in the header
so the ledger is never confused with mssEC 19; check decode.py renders the header without assuming mssEC 19. Stop before an entry
that would cross 80% of cap or box. NOTES section "## LS3-R18 (8 Oct 2026, account 2, for LANE ST-LEDGER-3)", and one line under
eckert-1862 NOTES' A3V3-ECK18 section pointing to it.

## LS3-R62 (Opus 5.5, solver; cap $4, box 90 min): mssEC 15 residue entries against the image
ciphers/eckert-1862 Remaining gaps (D12-E62H): 124 residue entries decoded at C 155 / I 36 / M 82, none in print; the named next step
is the image of the residue pages against the volunteer text for the M-graded tokens. Pick the six residue entries with the highest
keyed share and fewest oov tokens (script over the committed residue output; paste the selection), fetch their pages, crop
(`tools/iiif_lines.py --image ... --out ...`, paste), settle every M token from the crops, re-run ciphers/eckert-1862/decode.py and
its `--check`, and run the lane's matched control (other book + meaning-shuffled key). Report per entry: tokens H/C/S/M/I before and
after, and whether a clause of authentication length reads. Before reading, grep the cached 1862 OR volumes (DIR62 set) for each
entry's plain words once more and record the result. NOTES section "## LS3-R62 (8 Oct 2026, account 2, for LANE ST-LEDGER-3)";
gaps_check eckert-1862 after.

---

## First verifiers (Opus 5.5, separate sessions, spawned by the lane after each reader) -- LS3-V9, LS3-V18, LS3-V62
The LS-V7 section of the ST-LEDGER-2 worker brief, scoped to that reader's entries (book check first, three crops word for word
including the longest, every M/I token re-read from the image, press of the day, sender/recipient papers, OR/ORN +/- 3 days incl.
vols. 47-49 for 1865, IA/Google Books with country=US + key, OpenAlex/S2/CORE with keys, JSTOR-QUEUE rows both families, never
blocking). Depth per .claude/briefs/runs/2026-10-08-acct3-depth-bar.md. AUDIT.md heading "## AUDIT (LS3-V9)" etc. in the target the
entries are filed in; status.json rows for N3+ only, audit_status "one audit"; SO row per N3+ entry; `tools/depth_check.py` passes;
file_shrink_guard before the final push. Do not decode other entries. Caps: about 0.6 per entry + 1.

---

# Wave 2 (written 8 Oct 2026 10:4x UTC)
Wave 1 done by get_session: LS3-K 1.32 (no "10" book in p16003coll11; 1865 key-share band non-selective, logged untestable by that
instrument), LS3-R9 2.85 (O9-AK, E76 read, not located; O9-AL OR I/37 pt 2 p.453 and E77 ORN I/11 p.204 located by the reader),
LS3-R18 4.42 (N2-BP, E78, N2-BQ, O9-BA, O9-BB from pp.48-51; E79-E84 from the A3V3 list; 9730.87/9731.89/9908.417/9939.484 in OR),
LS3-R62 3.77 (eckert-1862 residue 4982.1, 4999.1, 4984.3, 4992.1, 4999.2, 4982.3: 0 slips, chosen key beats all controls).
Every first verifier: the LS-V7 section of the ST-LEDGER-2 worker brief and the "First verifiers" section above. Points specific to
these readers: LS3-R18 read pages in three bands at 2000 px rather than crops -- so the verifier re-reads every code word of three
entries (incl. the longest) from line crops it cuts itself (`tools/iiif_lines.py --image ... --out ...`, paste); the readers' clause
counts are hand counts by one reader -- recount them; ORN (Navy Official Records) was not searched by LS3-R18 -- search it for every
entry, first. A verifier that finds an entry in print classes it N1/N2 and moves on.

## LS3-V18a (Opus 5.5, first verifier; cap $5.5, box 90 min): N2-BP, E78, N2-BQ, O9-BA, O9-BB (LS3-R18 part 1) + O9-AK, E76 (LS3-R9)
 Also confirm by script, N1 if word for word: O9-AL (OR I/37 pt 2 p.453) and E77 (ORN I/11 p.204). O9-BA (five tokens, no time word)
 and the key row Bologna/Bolivia = Heintzelman (one eye) are the weakest: re-read the mssEC 67 p.[10] row from the image. E76 is
 Butler's own telegram: Butler's Private and Official Correspondence vol. 5 (Nov 1864) first. AUDIT.md "## AUDIT (LS3-V18a)".

## LS3-V18b (Opus 5.5, first verifier; cap $5, box 80 min): E79, E80, E81, E82, E83, E84 (LS3-R18 part 2)
 E80 (Welles to Porter, 1 Oct 1864, Farragut/Tennessee): ORN ser. I vols. 21 and 26 first; Welles diary. E81/E83/E84 are Quartermaster
 requests with a clear sibling on the same leaf (9858 Horner, "Send all weaselers ..."): say whether the sibling is the same telegram.
 AUDIT.md "## AUDIT (LS3-V18b)".

## LS3-V62 (Opus 5.5, first verifier; cap $3, box 60 min): eckert-1862 residue 4982.1, 4999.1, 4984.3, 4992.1, 4999.2, 4982.3
 In ciphers/eckert-1862 (AUDIT.md "## AUDIT (LS3-V62)"). The key is C-grade from print alignment (key source per rule 10: say which).
 4982.1 is the only entry with a clause; decide its depth under the depth bar (two of its seven code tokens are M). The other five
 carry 1-4 code tokens in plain text: say in one line each whether they reach D2 at all; if not, no status.json row, no SO row.
 OR ser. I vol. 7 (McClellan to Buell, same day) is a parallel for 4982.1, not the telegram: confirm.

## LS3-R18b (Sonnet 5.5, solver; cap $4.5, box 100 min): the last seven A3V3-ECK18 keyed entries
 9943.494, 9948.507, 10002.578, 10026.621, 10027.623, 10028.625, 10031.632 (Jan-Jun 1865; skip 9947.505 and 10020.609). Same method
 as LS3-R18 part 2 (pre-filter over OR 32-49 incl. 47-49 + ORN + Butler/Lincoln cached, then image, crops -- cut line crops with
 `tools/iiif_lines.py` and read them, not 2000 px bands -- time-word control, 200-seed shuffle, IDs from E85 after fetching). 1865:
 LS3-K found the token-share band cannot tell No. 1 from Nos. 3/4, so the book rests on the ledger's own "No N" label and the
 time word; an entry with neither, or whose time word disagrees with the header under No. 1, is "key not in hand", not read.
 NOTES section "## LS3-R18b (8 Oct 2026, account 2, for LANE ST-LEDGER-3)".
