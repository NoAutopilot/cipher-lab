# TX-DECODE atlas mix (atlas_mix.py) -- RESCORE (11 Oct 2026, 17:4x UTC by date -u)

**Measurement correction: box-to-position map fixed (off by one), not a new gate look.**

Job BOXMAP-RESCORE (others) for the account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M). Script-only: no vision call, no reader,
no image viewed, no network beyond git. No truth file or BENCHMARK-TX.tsv row edited.

`atlas_mix.py` puts each atlas box's top-3 at a no.87 position through `atlas/no87_box_token.tsv`, which is one token off on 10 of
26 lines (`atlas/RESCORE.md`). The held-out lines it scores (f178v L13, L17, L21; f179r L01-L03) are among them, so the atlas
probabilities sat on the neighbouring token there. **Only the map changed:** `atlas_mix.py --map FILE [--topk FILE] --out FILE` is
new (without it the run writes the committed `atlas_mix.json` byte-identically: checked). Run from `harvest/`:

    python3 ../atlas/no87_map.py --compat /tmp/compat_map.tsv           # label-aware map in old columns (reads the clerk alignment; temp only)
    python3 tx_decode/atlas_mix.py --map /tmp/compat_map.tsv --out tx_decode/rescore_boxmapLA/atlas_mix.json
    python3 tx_decode/atlas_mix.py --map /tmp/compat_map.tsv --topk ../atlas/rescore_boxmapLA/no87_heldout_LA.tsv \
        --out tx_decode/rescore_boxmapLA/atlas_mix_named.json           # plus the atlas re-named on the fixed map

Each run is about 80 s (200-key control per lattice). The scored set is the atlas-mapped held-out positions, so it moves with the map
(388 -> 387 positions); the two-pass lattice itself does not depend on the map.

| lattice | before: top-1 err / +U | before: lattice err | before: truth in lattice | **after: top-1 err / +U** | **after: lattice err** | **after: truth in lattice** |
|---|---|---|---|---|---|---|
| two-pass | 0.0722 / 0.1031 | 0.0670 | 0.933 | 0.0749 / 0.1034 | 0.0698 | 0.933 |
| atlas only | **0.3918** / 0.3918 | 0.3814 | **0.704** | **0.1912** / 0.1912 | 0.1757 | **0.876** |
| two-pass 0.8 + atlas 0.2 | 0.0670 / 0.0979 | 0.0670 | 0.946 | 0.0672 / 0.0956 | 0.0698 | 0.948 |
| (atlas re-named on the fixed map) atlas only | | | | 0.1823 | 0.1667 | 0.870 |
| (same) mix | | | | 0.0677 / 0.0938 | 0.0677 | 0.945 |

Key rank stays 1 of 201 everywhere (z 3.0-4.6).

**Does the conclusion change?** The atlas-alone figures were mostly the map: its top-1 error halves (0.39 -> 0.19) and its lattice
coverage rises from 0.70 to 0.88. The finding that matters for the decoder does **not** change: mixed in at 0.2 the atlas adds about
1.5 points of coverage over the two-pass lattice (0.933 -> 0.948; was 0.933 -> 0.946) and about 3 signs in 387 at top-1 (0.0749 ->
0.0672; was 2 in 388), and after the lam-4 decode nothing (0.0698 both; was 0.0670 both). "On this hand the atlas adds about 1 point
of coverage and about 1 sign in 400 of accuracy; the decoder then recovers about half a point; neither is near the 5% target" stands
in substance (read "about 1.5 points" and "about 3 signs in 400 at top-1, none after decoding").
