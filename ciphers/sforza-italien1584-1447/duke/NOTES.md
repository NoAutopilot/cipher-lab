open

# The Duke's 1447 cipher (Filippo Maria Visconti to Francesco Sforza, BnF italien 1584): key rebuild attempt -- SFZ-D, 7 Oct 2026

Worker SFZ-D for LANE ST-REBUILD (account 2), brief `.claude/briefs/runs/2026-10-07-acct2-st-rebuild-workers.md` (Wave 2,
S1-S2). Times by `date -u`: 21:52-22:0x UTC, 7 Oct 2026. Target folder: `ciphers/sforza-duke-1447-f15/` (f.15, not read).
Status meaning here: `open` = no key passed its gate; nothing is read.

## Units (pairs identified on the images; Mazzatinti 1883 cod. 1584 list read the same day)

| unit | cipher slip | contemporary translation | later clear copy (used) | canvases | slip signs (our read) | copy letters |
|---|---|---|---|---|---|---|
| f8 | f.8 (Abiate 11 Jan 1447), top of c11 right | f.9, below the slip on the same page | f.10, c12 right | 11 / 12 | 865 | 831 + dateline |
| f5 | f.5 (Abiate 10 Jan 1447), middle of c9 right | f.6, below the slip | f.7, c10 right | 9 / 10 | 896 | ~1,000 + dateline |

SFZ-0's "f.5/f.7, f.8/f.10" pairing is right for the later copies; f.6 and f.9 are the contemporary translations
("Traduzione della lettera precedente" in Mazzatinti). The later copyist writes "gi" where f.6/f.9 read "vuy"/"vui":
corrected to "vui" in the clear files (the copy is otherwise used as read).

Commands (pasted):
```
python3 tools/iiif_lines.py --ark btv1b100373864 --canvas 11 --region 4000,860,3120,1450 --out ciphers/sforza-italien1584-1447/duke/images --prefix f8 --overlap 0 --max-width 1600 --debug
python3 tools/iiif_lines.py --ark btv1b100373864 --canvas 12 --region 5600,330,1830,3450 --out ... --prefix f10 --overlap 0 --max-width 2400 --debug
python3 tools/iiif_lines.py --ark btv1b100373864 --canvas 9 --region 4000,2280,3420,1300 --out ... --prefix f5 --overlap 0 --max-width 1750 --debug
python3 tools/iiif_lines.py --image .../src_ark_12148_btv1b100373864_f9_4000_2280_3420_1300.jpg --out <scratch> --prefix f5 --overlap 0 --max-width 1750 --deskew --debug
python3 tools/iiif_lines.py --ark btv1b100373864 --canvas 10 --region 4650,230,2850,4100 --out ... --prefix f7 --overlap 0 --max-width 2400 --debug
```
Overlays checked: f.8 16 lines, clean bands. f.5 slopes upward to the right: the fixed bands took the left half of one line
and the right half of the line above from line 8 on, so lines 9-15 were read from the `--deskew` re-cut (scratch, not
committed; regenerate with the command above) and line 8, which neither cut isolated, from a manual strip of the same
source file. Request counts: see target NOTES.md.

## Sign reading (deviation from the brief)

- One blind Sonnet pass on the f.8 line crops (labels.md sheet, one call) returned about 19-30 tokens on lines that carry
  45-55 signs (lines 4-16) and rated itself low-confidence; it was not used and no file of it was kept.
- SFZ-D (Opus) then read f.8 and f.5 itself, sign by sign, from the native crops stacked four lines at a time. f.8 was read
  before any Duke alignment; f.5 after f.8 had been read but before any Duke key existed. Single reader: `err_2reader` not
  measured, `err_true` not measurable (no benchmark item of this hand).
- Labels: `../amidani/labels.md` plus N1-N13 (its "Additions (SFZ-D)" section). The sign inventory of this hand is not settled
  (TRANSCRIPTION.md): whether "par"/"per"/"co"/"g#"/"·ll·" are one sign or several is a guess (written letter by letter).

## S1 shared-key test (pre-registered): FAIL -- the Duke does not use Amidani's key at this transcription

`s1_test.py`, output `s1_test.out`: f.8 decoded with `../amidani/key.tsv`'s learning (g1.py learn/score imported), scored
against its own copy (f.10), 200 shuffles of the Amidani key.

| unit | signs | nulls | signs absent from Amidani key | real | shuffle mean | shuffle p95 |
|---|---|---|---|---|---|---|
| f8 | 865 | 156 | 157 | 0.267 | 0.295 | 0.334 |

Below its own shuffle mean (with the dateline-corrected copy; before the correction 0.267 / 0.294 / 0.334, 194 nulls). Conditional on the label mapping by eye (157 Duke tokens have no Amidani label at all).

## S2 key + gate G1 (pre-registered, unchanged from SFZ-1; `g1_duke.py` imports `../amidani/g1.py`): FAIL

Leave-one-letter-out over the two Duke units, 200 shuffles of the training key.

| run | held out | signs | nulls | trained signs | unseen | real | shuffle mean | shuffle p95 | > p95 |
|---|---|---|---|---|---|---|---|---|---|
| 1 (copies without dateline) | f8 | 865 | 194 | 37 | 0 | 0.398 | 0.363 | 0.388 | yes |
| 1 | f5 | 896 | 151 | 35 | 7 | 0.471 | 0.363 | 0.401 | yes |
| 2 (dateline added to both copies) | f8 | 865 | 156 | 37 | 0 | 0.384 | 0.375 | 0.408 | **no** |
| 2 | f5 | 896 | 141 | 35 | 7 | 0.498 | 0.361 | 0.404 | yes |

Run 1 mean 0.435, run 2 mean 0.441: both below the 0.60 gate, **FAIL**. Run 2 is the committed `gate_g1.tsv` (`g1_duke.py --check` reproduces it); run 1's output is kept as `gate_g1_run1.tsv`. It is a
correction of an input error, not a tuning: both slips end in the same ~30-sign run (f.8 line 16, f.5 line 15) while the two
copies' last sentences differ, so the run is the shared dateline "Data Abiate die ... Januarii mille quatrocento quaranta
septe", which run 1 had wrongly left out. Run 2 is the only rerun, and the dateline is not proven to be enciphered.

Shared signs agree badly: 31 (sign, unit-pair) cases with >= 2 counts in both unit keys, only 6 with the same value
(Amidani's three units: 88 of 105). Two letters of the same sender written one day apart are unlikely to use two keys this
different. The likelier causes are the reading and the segmentation:
- one reader, an unsettled inventory;
- multi-letter shapes possibly being single signs;
- the commonest sign N1 (ħ, 11-16%) possibly being several signs.
Stopped here per the brief: no S3, no f.15 decode.

Grading: no key value is claimed; `key.tsv`/`key_*.tsv` are the alignment's output for the record, every value M at best.

## Remaining gaps (SFZ-D, 7 Oct 2026)
Read so far: 0 of the Duke's unglossed letters read; key gate G1 FAIL at 0.441 mean held-out accuracy over 2 glossed units (1,761 slip signs, single reader)
- the Duke's sign inventory (is ħ one sign, are par/per/co/g# single signs) - blocker: not-attempted; G1 failed with shared-sign agreement 6/31, pointing at reading/segmentation; next: settle the alphabet per TRANSCRIPTION.md (tools/glyph_atlas.py segment once opencv is available, or tools/sign_sorter.py for the owner's piles) on f.5+f.8, then a second blind reader per line crop, ~$4
- further glossed pairs f.23/f.24 with copy f.26, f.30-31 with f.29, f.36-37 with f.35 (Mazzatinti: Milano 5, 9, 12 Feb 1447) - blocker: not-attempted; more units at the same unsettled reading would retune the same knob (rule 3 third-attempt clause); next: only after the alphabet step, ~$3 per pair

## Escalation (SFZ-D, 7 Oct 2026)
- [x] siblings: two glossed Duke pairs used (f.5/f.7, f.8/f.10); three more listed above
- [x] clear-pages: later-hand copies f.7, f.10 used; contemporary translations f.6, f.9 used only to fix the copyist's "gi"
- [ ] known-keys: Cerioni 1970 (Sforza keys from 1450) and the ASMi Visconti cipher registers not checked
- [n/a] print: the brief excluded print and novelty work for the key units (all N0 by construction)
- [x] key-rebuild: attempted, G1 FAIL (run 1 0.435, run 2 0.441)
- [ ] image-check: alphabet settling and a second reader, above
- [ ] retry: G1 rerun only after the image-check step
Verdict: keep going: 2 internal gaps; cheapest next: settle the Duke's sign inventory on f.5+f.8 and a second blind reader, ~$4
