## NEAR3-C1TX-c187R (4 Oct 2026)

Account 2 worker for LANE-NEAR3. Briefs: `.claude/briefs/runs/2026-10-04-ytbiz-near3-wave2.md` (wave-2 change: crops plus overlay
must total <= 1.5 MB) and the wave-1 job NEAR3-C1TX-<LEAF> with LEAF = c187R. This section is written here, not in NOTES.md, per the
brief; the lane folds it in. Clock: claim at 01:34 UTC, reconciliation done at 01:42 UTC, box 60 min.

**Leaf.** c187R = IIIF f188, the right mounted leaf, native region 3950,50,3150,4650 (ark btv1b90010063; NOTES.md "IMG-GALLICA1").
It has **26 cipher lines**: paragraph 1 is L01-L08, and paragraph 2 is L09-L26. Paragraph 2 opens with a large initial and the clear
date "Juil 23". The leaf ends "... 6r q monsr", with "monsr" in clear script. Old foliation "164" and "187" are top right, and a BIBLIOTHEQUE ROYALE
stamp is below the text.

**Route and crop command**, pasted before any subagent call:
`python3 tools/iiif_lines.py --ark btv1b90010063 --canvas 188 --region 3950,50,3150,4650 --out ciphers/clair1161-avis-flandre-1688/images --prefix c187R --bottom-margin 75 --debug`
- The run found 29 bands. Three of them were not text: the folio number at y 69 and the stamp at y 4303 and 4578.
- The default segments overlapped by 1650 px.
- **Side effect, reverted.** With the native file on disk, the folder was over 30 MB, so the tool's size guard downscaled the
  *committed* `src_*` files of f186 and f187 (another leaf's sources) and rewrote their manifest entries. I restored both files and
  `manifest.json` from git and removed the `_ref1600` copies, so no other leaf's file changed. A lane should know that running
  `iiif_lines.py --out` into this folder while it sits near 30 MB touches other leaves' committed sources. Writing to a scratchpad
  `--out` avoids that.
- **Re-cut.** Row-ink profiles over the left, middle and right thirds show the lines slope up to the right by 60-90 px across the
  region. The tool's single centre at y 2831 fell between two lines. I re-cut into the scratchpad from a second native fetch (the
  first native file had been downscaled by the guard), using the middle-third centres:
  `... --out <scratchpad>/cut --prefix c187R --centres 358,469,598,721,843,976,1102,1230,1551,1677,1813,1937,2069,2187,2335,2457,2603,2727,2878,3028,3166,3309,3437,3583,3709,3851 --bottom-margin 75 --max-width 1700 --overlap 150 --follow-slope 400 --debug`
  This gave 26 lines x 2 segments = 52 sheared strips (s1 x 0-1700, s2 x 1550-3150), with drift fitted per line (-17 to -93 px).
  Every line was checked by eye on the reconciliation views. The two passes both read L07 and L08 as distinct lines.
- **Size.** Crops are committed as grayscale JPEG **q35 at the same dimensions**: q60 gave 2.41 MB and q40 gave 1.75 MB including
  the overlay. The overlay is resized to 1000 px, q50. The total is 1.43 MB. The `src_*` native file is not committed; each manifest
  entry carries its `source_url` and a `source_file_note`. q35 is legible at reading size (checked on L03_s2).
- **Folder.** Tracked files total 29.15 MB after c188L's crops (ad631ae3) and these. This is under the 29.5 MB line, but there is
  little room left for the pooled job.

**Requests:** gallica.bnf.fr 2 (native region twice, 2 s apart, descriptive UA, no challenge). **Subagent calls (Sonnet): 2.**
Pass A read top-down and pass B bottom-up. Each saw only the 52 crop paths and `tx/labels_v2.md`, through the prompt in
`tx/c187R_pass_prompt.md`. I did the reconciliation from 12 two-line composite views plus one single crop, with no subagent.

**Numbers.**

| item | value |
|---|---|
| lines | 26 |
| tokens reconciled (`tx/c187R_rec.tsv`) | 745: 740 cipher signs + 5 clear tokens (Juil, 23, toute x2, monsr) |
| err_2reader (A vs B, `tools/reconcile_passes.py --keep-plain`, nw) | **57/751 = 0.076**; 53/751 = 0.071 without the 4 notational `0`/`o` columns. Under 0.10, so no look-alike pass was run. |
| single pass vs reconciled | A 38/749 = 0.051, B 29/747 = 0.039. These are upper bounds: they count provisional NEW labels and `0`/`o` as differences. |
| confidence (`tx/c187R_rec_long.tsv`) | H 697, M 48 |
| err_true | not measurable: there is no benchmark item for this hand |

Files: `tx/c187R_passA.tsv` and `tx/c187R_passB.tsv`; `tx/c187R_rec/` (reconcile_passes output); `tx/c187R_rec.tsv` (wide, same columns as
`tx/c185R_rec.tsv`); `tx/c187R_rec_long.tsv` (ids `c187R_Lnn` for the pooled merge). `tx/c187R_reconcile.py` holds every settlement with
its reason and regenerates both rec files.

**Settlements and conventions** (all 57 are in `tx/c187R_reconcile.py`):
- **sqc, 7 occurrences.** A read `iib` and B read `sqc` 7 times (L05, L06, L14, L15, L20, L23). On the crop the sign is the small
  open square that follows `wb` almost every time ("wb ⊏"), so it was settled as `sqc`.
- **K, 6 occurrences.** A read `rot` and B read `K` for the ornate crossed "Rs" sign 6 times (L04, L12, L13 line-initial, L14,
  L18). It was settled as `K` (M). The "p⁸"-shaped crossed 8 at L06 and L11 (A `8`, B `rot`) was settled as `rot` (M), the same
  shape the passes agreed as `rot` at L25.
- **vdash, 2 occurrences.** The v-with-long-bar (L03 end, L12 start) is `vdash`, as in c186L NEW1 and c187L.
- **Crossed p.** A crossed `p` is one sign, `p` (L01, L02), following c187L.
- **Small looped l, 4 occurrences.** The small looped ℓ (L03, L12 x2, L16 initial) is `l` (M). The passes split it as `l`/`c`/`f`.
- **Smaller settlements.** L04's line-initial `th` was missed by A. The barred three-stroke at L04 is `iii`; c186L flagged barred and
  bare `iii` as perhaps two signs, and it is barred here too. L07's `tz` is a bar over a 3-body. L10's `th` carries a dot above (M).
  L18 col 22 is `eloop`, the same crossed loop the passes agreed as `eloop` at L12. L19 has no `+` between `4` and `d` on the crop.
  L26 col 23 is a barred `z`.
- **Notation.** `0` is written as `o`.

**New shapes** (provisional labels, not forced into labels_v2):
- **`NEW_c187R_2`, 3 occurrences:** an "xe"/fish ligature, an x-like crossing run straight into an e. It is at L22 col 24 (crop
  `c187R_L22_s2`, after `p`), L25 col 8 (`c187R_L25_s1`, after `p`) and L26 col 6 (`c187R_L26_s1`, after `th`). Pass A read `x e`
  each time, and pass B read `K`, `rot` and `K`. I set it as one sign because the stroke is continuous. It may be a K variant; the
  pooled job or the sorter should decide.
- **`NEW_c187R_1`, 1 occurrence:** a flat bar with an ink blob, at L04 col 25 (`c187R_L04_s2`, before `4 4 qb`). It may be a heavily
  inked sign or a blot.
- **`NEW_c187R_blot`, 1 occurrence:** a large ink blot covering one sign, at L20 col 5 (`c187R_L20_s1`, between `a` and `sqc`). It is
  illegible on this image.
- **Not new.** Neither c186L's NEW1 (it is `vdash` here) nor c187L's NEW1 (the open arc at L24) was seen as such on this leaf.
- **Recorded for the pooled job, not settled here:**
  - `s` (the 5-hook) occurs 4 times, 3 of them in `s z` (L08, L18, L20), as in c186L and c187L; `ss` occurs 6 times.
  - The arc-hooked `2` does **not** occur at all on c187R (0 in 740 signs). c187L had 9 in 713, while c185R+c186R had 1 in 924. So
    c187L's count stands alone.
  - `S` occurrences are not split by shape (NEAR3-C1SPLIT recommends keeping them merged).

**Clear words inside the cipher** (all grade M): L09 "Juil" with a large decorative initial, then "23", as a date heading for paragraph 2;
L17 and L24 "toute" (both passes partly read it as "tour"); L26 "monsr" at the line end. These were kept as `PLAIN:` tokens.

**Decode for information** (`tx/c187R_decode_info.txt`). It is ungraded and not a reading. The leaf is decoded under the current
key.tsv, which was annealed on c185R+c186R only. This leaf took no part in fitting the key, and no control was run. `ss` is split to
`s s`, and the NEW labels and `/` are left unkeyed.
- Runs of French show up unprompted: "ceulx" (L05, L06, L15, L23), "aultres" (L10, L17), "plus" (L11), "trois" (L09),
  "leur conseil et tout" (L20), "accroire" (L19), "conseil" (L20), "lesd ... ostel" (L26).
- The rest is not segmentable by eye.
- A held-out judge run of this decode against a shuffled-key control would be a cheap check. It was not in this brief, so I did not
  run it.

**Not done (brief):** no edit to ciphertext.tsv, key.tsv, tx/stream_all.txt, NOTES.md or NEAR.md. No look-alike pass (err_2reader
< 0.10). No sorter focus list. No glyph atlas: the brief names line reads, and the family atlas belongs with the pooled job.
