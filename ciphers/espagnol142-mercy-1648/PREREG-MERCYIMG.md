# PREREG MERCY-IMG (image re-read of the M glyphs on BnF Espagnol 144 f.22r rows r16-r24), written 14:4x UTC 15 Oct 2026 by date -u, before any reader ran

Worker MERCY-IMG (for LANE VIV-KEYSTONE, account 4). Brief: `.claude/briefs/runs/2026-10-15-acct4-depth-steps.md` "## JOB MERCY-IMG".
No key.tsv, reading, AUDIT.md or status.json edit. No network (the native canvas is on disk: images/f22r_canvas58.jpg, sha1 4ad5486d...).

## Material
Crops (command, pasted in NOTES.md): `tools/iiif_lines.py --image images/f22r_canvas58.jpg --out mercyimg/crops --region 400,3030,2950,1790
--prefix f22r_r16r24 --max-width 1550 --overlap 150 --debug` -> 9 lines x 2 segments (s1 x 400-1950, s2 x 1800-3350, 150 px overlap),
debug overlay checked: band L01..L09 = rows r16..r24. Units: the 192 cipher tokens of r16-r24 in ciphertext.tsv: 173 at confidence H,
19 at confidence M (r16:21-22, r17:10-11, r17:21-22, r18:5-6, r20:6, r20:7, r20:15-16, r22:2, r23:1, r23:2, r24:4-5, r24:14-15).
Also reported, not gated: the key-level-M / exceptions glyphs on these rows (r16:3, r16:6, r17:5 = 14 read as 19; r16:9, r17:4, r19:10 = 25).

## Readers
Two blind Sonnet subagents (A, B), independent, same prompt; each gets only the 18 crop paths: "transcribe the handwritten numerals
left to right as written; one group per space the writer left; digits of a group written together stay together (e.g. 52); '?' for an
illegible digit". No key, no transcription, no letters, no reading shown. One reconciliation by this worker against the crops (zoomed
crops of the disputed spots only), after both reads are saved (mercyimg/readA.tsv, readB.tsv).

## Alignment
Per row, the reader's s1 and s2 group lists are merged at the overlap (longest exact suffix/prefix match of >= 2 groups; else by the
x-position stated in the overlap note), then the row's digit string is aligned to the transcription's digit string (edit-distance
alignment on digits, group boundaries carried as a separate flag). Each transcription token gets the reader's digits over its span and
whether the reader puts a group boundary on each side of it.

## Known-answer control (gate)
For the 173 H tokens: glyph reproduction = share whose aligned reader digits equal the committed sign exactly. Gate per reader:
>= 0.90. A reader below the gate is a non-test: its reads are reported, but no M position is settled with it.
Secondary (reported, gates only segmentation settlements): boundary reproduction = share of H tokens the reader writes as their own group
(both boundaries present). Gate >= 0.90 per reader.

## Settlement rule for an M position
Both readers pass the glyph gate AND agree on the digit string of the group covering the position. Then:
(a) the digit string has exactly one parse into key.tsv codes (2-34 with a value; e.g. 52 -> 5|2, 48 -> 4|8, 72 -> 7|2, 65 -> 6|5,
    186 -> 18|6): the positions take that parse (settled by image + key range);
(b) the string has more than one parse (e.g. 26 = i vs 2|6 = o s, 23 vs 2|3): settled only if both readers also agree on the grouping
    and both pass the boundary gate; otherwise it stays M (unsettled segmentation).
Re-label: a settled glyph that differs from the one the transcription carries AND that key.tsv maps to one letter is a re-label
candidate (letter reported; never written to key.tsv or the reading). Grade of a settled position: candidate S (image), held as M pending
a verifier; unsettled stays M. A settled glyph equal to the transcription confirms it.

## Run statistic
`mercym33/runs.py` on a scratch copy of reading_tokens.tsv/ciphertext.tsv (re-labels applied in the copy only), positions settled per the
rule passed as accepted: longest H/C/S run in letters before and after, against AD 84 (R 3.4) and 135.1 (es17c). Sensitivity, not
licensed: the same with MERCY-M33's four T6 accepts added. Key-level-M codes (25, 15, 9) stay M; this job does not touch values.
