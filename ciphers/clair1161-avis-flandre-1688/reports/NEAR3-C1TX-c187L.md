## NEAR3-C1TX-c187L (4 Oct 2026)

Account 2 worker for LANE-NEAR3. Brief `.claude/briefs/runs/2026-10-04-ytbiz-near3-wave1.md`, job NEAR3-C1TX-<LEAF> with
LEAF = c187L. Clock: claim 01:15 UTC; reconciliation done by 01:25 UTC (box 60 min). Leaf: IIIF f188 (canvas c187) left leaf,
headed "Autres advis".

**Route.** `python3 tools/iiif_lines.py --ark btv1b90010063 --canvas 188 --region 100,1200,3250,4450 --out
ciphers/clair1161-avis-flandre-1688/images --prefix c187L --bottom-margin 75 --debug` (one native fetch). I checked the overlay
and a stack of every band by eye. L01 is the clear heading "Autres advis". L02-L17 are paragraph 1 (16 lines) and L18-L27 are
paragraph 2 (10 lines). Each band holds one whole line. The next line's tops show at the bottom edge, and the passes were told
to ignore them. The default segments overlapped by 1550 px (s1 x 0-2400, s2 x 850-3250), which invites double reading. So I re-cut
from the cached native file, with no second request, with `--max-width 1700 --overlap 150`. That gives s1 x 0-1700 and s2 x 1550-3250,
27 bands x 2 = 54 crops. The crops were re-encoded as grayscale JPEG q75 at the same dimensions (4.2 MB). The `src_*` native file was
removed from the folder and is not committed (sha1 kept in the worker's scratchpad). Its URL is in `images/manifest.json` under
`iiif_lines`. Requests: gallica.bnf.fr 1 (a native region, descriptive UA, no challenge).

**Tool shelf** (`tools/tool_shelf.py "transcribe a 16th-century French pen-sign symbol cipher from line crops"`). It offers
`glyph_atlas.py` (proven) first. Not used: the brief names line reads, as for c185R/c186R, and no atlas exists for this hand. On
the one benchmark where both were measured (Birago no.87), atlas top-1 read 0.162 against 0.040 for line reads (TRANSCRIPTION.md row 3).
TRANSCRIPTION.md asks for a family atlas before line reads when a key family has siblings. Building one for the six clair1161 leaves is
for the pooled job, not this one.

**Subagent calls (Sonnet): 3.** Pass A was 1 call. Pass B took 2 calls: the first call failed on an API safeguard error before
writing anything, and the second ran with the same prompt plus a one-line context sentence. Each pass saw only the crop paths
and `tx/labels_v2.md`, and the prompt is in this report's commit as `tx/c187L_pass_prompt.md`. I did the reconciliation from
the crops myself (5 composite views), with no subagent.

**Numbers.**

| item | value |
|---|---|
| lines | 26 cipher lines (L02-L27) |
| tokens reconciled | 725, of which 713 are cipher signs and 12 are clear words (PLAIN:) |
| err_2reader (pass A vs B, `tools/reconcile_passes.py`, nw) | 69/733 = **0.094** (under 0.10, so no look-alike pass was run) |
| single pass vs reconciled | A 38/728 = 0.052, B 39/731 = 0.053. Upper bounds: they count A's provisional NEW labels as differences. |
| confidence in tx/c187L_rec_long.tsv | H 685, M 40 |
| err_true | not measurable: no benchmark item of this hand |

Files: `tx/c187L_passA.tsv`, `tx/c187L_passB.tsv`, `tx/c187L_rec/` (reconcile_passes output), `tx/c187L_rec.tsv` (wide, same
columns as `tx/c185R_rec.tsv`), `tx/c187L_rec_long.tsv` (line/pos/sign/conf/note, with ids `c187L_Lnn` ready for the pooled
merge), and `tx/c187L_reconcile.py`, which holds every settlement with its reason and regenerates both rec files.

**Settlements and conventions** (each one is listed in `tx/c187L_reconcile.py`):
- Pass A's `NEW:5hook` (6x, always followed by z) is the small s of the `s z` pair that c185R already reads. It is settled as `s`.
- Pass A's `NEW:v-bar` (4x) is c185R's `vdash`. The L10 line-initial `NEW:triangle`, which both passes read, is c185R's `tri`.
  Both labels are already in key.tsv.
- `0` is written as `o`, following ciphertext.tsv, which has no `0`.
- `6r` is one sign, the "6z" shape: pass B's `6 z` was settled to pass A's `6r` 3x. The "6y" shape at L23 is kept as `6 7` (M).
- Pass A's `sqc` was pass B's `2` 6x. Each of these is the arc-hooked 2 of labels_v2, so it is settled as `2`. The true open
  square `sqc` (L06, L15, L26, where both passes agree) is kept.
- In this hand `p` is drawn with a crossbar through the stem. Pass B read two of these as `+ p` (L16), and pass A's single `p`
  was kept.
- Count shift: `2` occurs 9 times in 713 signs here against 1 in the 924 signs of c185R+c186R. Either this leaf uses the
  sign more, or the earlier leaves read it as something else. The pooled job should check this.

**New shapes:** `NEW1`, one occurrence. It is an open arc "(" at L24 pos 9, before `o th e`, on crop `images/c187L_L24_s1.jpg`
about x 830-900. Pass B read it as `2?`. It is not forced into an existing label.

**Clear words inside the cipher** (all grade M): L03 "pour" at the line end; L04 "Disant(z) cete ?ugte"; L08 "Cet Dandre?
fermeu?" at the line start; L18 a large initial plus "m", and "tout"; L27 "amou[r?]" at the line end.

**Decode for information** (`tx/c187L_decode_info.txt`). This is ungraded and not a reading. The leaf is decoded under the current
key.tsv, which was annealed on c185R+c186R only. This leaf took no part in fitting that key, but I did not run a control.
By eye, the output has runs of French: "aultres ...", "per secret", "espai[g]nol", "pretext", "plus",
"encore ... apres", "princip(a)ulx", "anllois", "trois". A held-out judge score of this decode with a shuffled-key control
would be a cheap check of the key. It was not in this brief, so I did not run it.

Not done (brief): ciphertext.tsv, key.tsv and tx/stream_all.txt were not edited. No lookalike pass was needed (err_2reader < 0.10).
No sorter focus list. The `S` shape merge and q/ls stay as in labels_v2 (NEAR3-C1SPLIT's question).
