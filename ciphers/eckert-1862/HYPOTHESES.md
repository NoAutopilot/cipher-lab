# HYPOTHESES -- eckert-1862

## Legend: two print-read values, 1864-65 (R12A-ECKV2, 6 Oct 2026, verifier) -- data conflict, not resolved

Book value: Maj Gen S. A. Hurlbut, H (Cipher No. 1 book mssEC 41 p.17 l.5 R; ciphers/eckert-1864/key.md). No print-read use
in 1864-65 reads Hurlbut. (key.md's 1862 row Legend = Kentucky, C, 07 Feb - 08 Jun 1862, is a different book and period.)
All witnesses below are sent telegrams from the War Department, Washington (direction: Washington outward), each read in the
print of that very telegram (OR ser. I vol. and page in ec18/legend_uses.tsv); per-token grades in ec18/hurlbut_row_grades.tsv.

| Value | Witnesses (pointer, date, addressee operator per ledger header, OR) |
|---|---|
| Butler (13) | 9674 11 Feb 1864 Caldwell (OR 33); 8906 29 Feb 1864 Caldwell (33); 8930 16 Apr 1864 Beckwith (33); 8942 22 Apr 1864 Beckwith (33); 9718 23 Apr 1864 Beckwith (33); 8945 24 Apr 1864 Beckwith (33); 8946 25 Apr 1864 Beckwith (33); 9736 15 May 1864 Beckwith (36.2); 8970 24 May 1864 Beckwith (36.3); 8975 29 May 1864 Beckwith (34.4); 9789 no ledger date, OR July 1864 (37.2); 9120 x2 10 Nov 1864, header "2 PM Washington" (42.3) |
| Canby (10) | 9746 27 May 1864 Geo H Smith (34.4); 9825 19 Aug 1864 Sholes, near Atlanta (39.2); 9079 26 Sept 1864 Sholes, Atlanta (39.2); 9102 24 Oct 1864 Clowry, St Louis (41.4); 9105 27 Oct 1864 Clowry, St Louis (41.4); 9893 9 Nov 1864 Fowler (41.4); 9937 19 Jan 1865 Plum, Eastport (45.2); 9181 7 Feb 1865 Plum, Eastport (49.1); 9202 19 Mar 1865 cipher operator, Knoxville (49.2); 10010 19 May 1865 Clowry (48.2) |

Overlap: 27 May - 10 Nov 1864 carries both values (Butler 8970, 8975, 9789, 9120; Canby 9746, 9825, 9079, 9102, 9105, 9893).
Observation, grade I, not used to grade anything: in this sample the Butler uses go to the operators with Grant/Meade and the
eastern armies (Caldwell, Beckwith) and the Canby uses to western operators (Smith, Sholes, Clowry, Fowler, Plum, Knoxville);
whether that is two books, two tables or one word reused by addressee is not settled by these 23 uses, and is not settled by
count. Consequence (rule 4): each print-read use is C from its own print; the 9 unread uses are M, whatever their addressee.
What would settle it: the cipher book (or table) in use on the Caldwell/Beckwith line in 1864 read at Legend.
D12-E62H (7 Oct 2026, solver) adds four Legend witnesses, each the print of its own telegram: Butler 9671 3 Feb 1864 and
9672 5 Feb 1864, Caldwell 2 (OR 33 pp.502, 514, Halleck to Sedgwick); Butler 9786 11 Jul 1864 to Grant's HQ via Beckwith (Dana's
telegram as deciphered in Papers of U. S. Grant vol. 11, not in OR); Canby 9945 25 Jan 1865 to Thomas, Eastport (OR 49.1 p.581 [D12-V62: was p.580],
second IA scan). Totals Butler 16, Canby 11, unread 5. 9786 falls inside the overlap window (Beckwith line, Butler); the addressee
pattern above holds for all four (still grade I, not used). The conflict stays unresolved.

E62-ALN (8 Oct 2026, account 1): Merlin conflict from the print, not folded into key.md (rule 4). key.md: Merlin = Virginia, C,
05 Feb-17 Jun 1862, OR 7 p.584 ("Western Virginia"). Ledger 5021 entry 1 (25 Feb 1862, aligned to OR ser. I vol. 51 pt 1 p.537 by
print/or_align.py): Merlin <-> "Maryland". Witness A (Virginia): OR 7 p.584, Western Virginia telegram, Feb. Witness B (Maryland):
OR 51 pt 1 p.537, the ledger's 25 Feb entry 1 (single occurrence, one telegram; one-word replace block, no held-out test possible).
Unresolved: could be a date/line split (Feb Western Virginia vs 25 Feb Maryland) or an OCR/alignment slip; the page image is not read.

E62-STALE (9 Oct 2026, account 4, Sonnet): Merlin conflict, page image read (rule 4: both witnesses logged, not settled by count).
Image: Huntington mssEC 15 item 5021 (IIIF full/2583, fetched 9 Oct 2026, scratch only, not committed), 25 Feb 1862 entry, line "...on the
Merlin side before tomorrow": the ledger word is Merlin, so the volunteer text is right and the 3 Oct E62-ALN pair is not a transcription slip.
Witness A (Virginia): OR ser. I vol. 7 p.584, Western Virginia telegram, Feb (key.md row, C). Witness B (Maryland): the 25 Feb entry itself against
OR ser. I vol. 51 pt 1 p.537, Marcy to Lander at Paw Paw, Washington, 25 Feb 1862, "will not probably be on the Maryland side before
to-morrow" (IA warofrebellion511unit `_djvu.txt`, read 9 Oct 2026), a Potomac crossing at Harper's Ferry. Pages 5079 and 5083 (OR 12 pt 1 pp.34,
662-663, June) read Merlin = Virginia. One Maryland occurrence, one telegram, no held-out test possible. Not folded into key.md. Handling: Merlin
is graded M in any entry about the Potomac / Harper's Ferry line (25 Feb on); key.md's Virginia row stands for the Western Virginia witnesses.
Side finds on the same page, not acted on: Humboldt addressee = Lander (paw paw; print "Brig. Gen. F. W. Lander") fits key.md's Humboldt = Lander (M);
Opal = "Winchester" (print "toward Winchester") fits Opal = Winchester (M); "no whistle was discovered" = print "no enemy was discovered", while
key.md has Whistle = wounded -- a candidate conflict for a future job, one occurrence.
