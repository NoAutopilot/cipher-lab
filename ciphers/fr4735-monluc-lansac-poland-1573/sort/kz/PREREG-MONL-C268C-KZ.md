# PREREG MONL-C268C-KZ (20 Oct 2026, 05:3x UTC by date -u; account 2, Opus)

Context: MONL-C268C step 1 found c268 (f.138) ends at L30 (overview f268 0,3900,4418,2590 at 1400 px: blank paper below L30), so
the brief's L31-L35 do not exist; the brief's follow-on (value-blind K12|K22 sort of the 9 L26-L30 splits) runs instead.
Question: are the 9 L26-L30 tokens split K12 (pass A) | K22 (pass B) -- L26:17, L27:15, L27:33, L28:6, L28:11, L28:34, L29:3,
L29:23, L29:29 -- K12 or K22 by shape?
Material: tiles cut by sign position (column ink segmentation, checked on a numbered overlay by this worker for position only) from the
levelled crops of regen_monll26.sh (L26-L30) and from the committed c268 L01-L04 crops (images/c268cipher_L0x_s{1,2}.jpg) for the references.
No in-band H/H K12 or K22 exists in L26-L30, so the references are on-page, out-of-band: K22 H/H L01:26, L02:11, L02:17, L03:8;
K12 H/H L01:29, L02:21, L03:6, L04:4 (ciphertext_c268.tsv conf H, both passes). 17 tiles shuffled under ids T00-T16 (Random(20261020));
the id->token map is written to a file the readers never see.
Readers: two blind subagents (strongest model), A in id order, B in reverse; each sees only the K12 and K22 sheet cells (ids, no value)
and the 17 tiles; calls each tile K12, K22 or X (sign not centred / unreadable) with H/M/L. No value, decode, facing letter or clear
text is shown. The reader returns its TSV in the reply; this worker saves it.
Gate: each reader gets every one of the 8 references right or X, with at most 1 X per reader and 0 wrong (a K22 ref called K12 or the reverse).
Decision rule: gate met -> a lead called the same id by both readers at H or M is settled to that id (relabel tag monl-c268c, conf M if
K22 is chosen, the K12 split closed as "K12 by shape" if K12); a split between readers, an L or an X stays as is. Gate not met -> no
change. key.tsv is never edited. After the relabel, the L26-L30 alignment is re-run with the same statistic and control (reported, not a gate).

## Decision
Belief: the 9 L26-L30 K12|K22 splits can be settled by shape against on-page H/H references
Would change it: any reference called the wrong id, or more than 1 X on the 8 references by either reader
Observed: refs A 8/8 right; B 6 right, 0 wrong, 2 X (T07 = L03:8, T11 = L02:28: 'triangle over o / over m', the tick sat between signs); leads: both readers agree on all 9 -- K22 at L26:17, L27:33, L28:6, L28:11, L29:3, L29:23, L29:29 (M/M), L28:34 (L/L); K12 at L27:15 (M/M)
Decision: change -- gate not met (B's 2 X on references are a tick-placement fault, not a misread), no relabel; round 2 re-places the T07/T11/T10 ticks and re-runs two fresh readers under PREREG-MONL-C268C-KZ2.md
Lesson: a tick placed from a downscaled ruler view lands between signs at 9-sized spacing; check every reference tile at sheet scale before the readers see it
