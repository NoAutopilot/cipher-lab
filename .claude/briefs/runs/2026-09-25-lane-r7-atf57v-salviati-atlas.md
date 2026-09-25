LANE R7 ATF57V -- fr2933-salviati-1525: glyph-atlas re-pass on leaf f57v to merge near-duplicate types (Sonnet, cap $6, box 60 minutes).
Common: 2026-09-25-lane-r7-common.md. NEAR.md row "fr2933-salviati-1525", next step (1). No solving, no key, no reading.
Intake gate (live, 25 Sept 20:00 UTC): "fr2933-salviati-1525: open (line 1) -- edition/page or full-text-search citation found within 6 lines" (exit 0).
State (NOTES.md "Code+mark at the pooled N (LANE R6 CM)" and "CM2"): pooled 2,820 sign tokens, 36 base codes, **223 code+mark types**; the cm solver
reads its noise-free control at 94% but 27-43% at 10% type noise, and CM2's error-tolerant variants still miss the 60% gate. The lever is the
transcription: if many of the 223 types are the same glyph written or read two ways (mark strings that differ only in how a pass spelled them, a
dot vs a small ring, '1' vs 'i' above a sign; base pairs CM2 found confused: #/+, g/y, bh/g, #/Z, f/y, bh/phi), merging them cuts the type count and
the effective noise. f57v is one of the two lowest-agreement leaves (f55v 77.5%, f57v settled by a three-way pass C).
Job:
(1) List every code+mark type that occurs on f57v (ciphertext_f57v.tsv; `python3 control/codemark_curve.py stats --leaves all` for pooled counts).
(2) For each type, cut crops of its occurrences on f57v with `tools/glyph_atlas.py crop --out glyphs --sid ...` (rebuild glyphs/crops first with
    glyphs/build.sh's segment line if missing; do not change clusters.tsv/labels.json -- build.sh says they must reproduce byte-identically) and
    put them beside the atlas exemplars (glyphs/atlas_part1.png/part2.png). Where the 1600 px reference is too coarse to tell two marks apart, you may
    fetch native-resolution regions of this leaf only from Gallica IIIF (ark btv1b90600674; find the canvas with tools/gallica_folio.py; <=30 requests,
    >=2 s apart, browser UA as the playbook says) to ciphers/fr2933-salviati-1525/images/ with manifest.json entries; keep the folder under 30 MB.
(3) Decide merges by eye on the crops, never by frequency: a merge is two type labels you cannot tell apart on the image across at least 3
    occurrences each, or one label that is a pass's spelling of the other. Write ciphers/fr2933-salviati-1525/merges_f57v.tsv:
    from_type, to_type, n_occurrences_f57v, evidence (crop file names), confidence (sure/likely). A merge applies codebook-wide.
    Also write the opposite case: types that look like one type but are consistently distinct (keep_distinct rows), so the next worker does not merge them.
(4) Re-score: pooled type count and per-leaf counts with the merges applied.
    AT55V owns the --merge option of control/codemark_curve.py; do NOT edit that file. When your merges_f57v.tsv is done, git pull; if --merge exists run `stats --leaves all --merge merges_f55v.tsv merges_f57v.tsv` (whichever exist) and report; if not yet, report the pooled count from a scratch script (not committed) and say so.
(5) Do NOT run the control ladder or the target: the orchestrator decides that from your count (gate: pooled types drop by a fifth or more, 223 -> <=178).
Write a section "## ATF57V: atlas re-pass on f57v (25 Sept 2026, LANE R7)" to ciphers/fr2933-salviati-1525/leafnotes/atlas_f57v.md (not NOTES.md; two
workers share the folder), with a table: types on f57v before/after, pooled before/after, merges by confidence, keep_distinct count.
ROOM done: "done: for LANE R7: salviati atlas f57v merges <n sure>/<n likely>, f57v types <a> -> <b>, pooled 223 -> <c> (gate <=178)".
