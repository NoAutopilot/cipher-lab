# PREREG-ALIGN3 -- PREREG-ALIGN2's decoy-gated gloss check with an Opus reader at native-resolution segments (FER126-ALIGN3, 6 Oct 2026, written and pushed before any reader call)

Brief: .claude/briefs/runs/2026-10-06-acct3-fer126-align3.md. Third and last machine attempt at item 126's interlinear gloss (CLAUDE.md rule 3,
third-attempt clause). Unchanged from PREREG-ALIGN2.md: target lines (39: f.1r R01-R28, f.1v V01-V11), candidates and decoys
(`align2_candidates.py`, 299 real / 295 decoy syllables, the same 78 items, the same shuffle seed 20261006 and the same 8 packs), the reader
question (y / n / ? per syllable), the statistic and the gate: real yes - decoy yes >= 0.30 AND decoy yes <= 0.15, pooled, AND real > decoy on
at least 2/3 of tested lines. If decoy yes > 0.15 the reader agrees with what it is shown: untested-by-this-tool, no grades.

Changed (the instrument): (1) the reader is Opus 5.5, not Sonnet; (2) the image. ALIGN2 gave each line as one 2400 x ~125 px strip, which
the image reader shrinks to about 80 px tall, and every Sonnet answer was "?" ("too faint and small at the displayed resolution"). ALIGN3 cuts
the same gloss-centred bands at native resolution into three overlapping segments per line and upscales each 2.4x (about 1536 x 391 px,
under the reader's shrink limit; autocontrast 1%), shown left to right as one item. Commands (sources: the owner's colour shots, private
repository images-126-shots; centres = ALIGN2's gloss-centred box centres):

    python3 tools/iiif_lines.py --image 1.webp      --out n1 --centres 80,157,233,312,395,476,556,641,733,824,897 --top-margin 45 --bottom-margin 45 --max-width 640 --overlap 80
    python3 tools/iiif_lines.py --image 2.webp      --out n2 --centres 95,176,259,342,424,507,588,669,748,824     --top-margin 45 --bottom-margin 45 --max-width 640 --overlap 80
    python3 tools/iiif_lines.py --image 3.webp      --out n3 --centres 108,183,261,344,426,510,597                --top-margin 45 --bottom-margin 45 --max-width 640 --overlap 80
    python3 tools/iiif_lines.py --image f1v-3.webp  --out nv --centres 72,134,196,261,329,399,469,538,604,671,741 --top-margin 45 --bottom-margin 45 --max-width 640 --overlap 80

117 segments (39 lines x 3). One segment spot-checked by eye before this file: R05 s1 shows the grey line between two cipher lines
("a res su di que ... y po"). Crops stay in the session scratchpad (images never into this repository).

Cost plan (Usage 6, per call): 8 Opus calls (one per pack, about 10 items = about 30 segment images each), estimate about $0.8 per call,
about $6.4 for reads + scoring by script; stop before starting a call that would cross 80% of the $8 cap or the 60-minute box.
No reconciliation step: answers are scored as given by `score.py` (the ALIGN2 script, unchanged).
If the gate fails: "untested-by-this-tool (machine gloss reading, 3 attempts)", the step [retired] with the instrument named, next step the
owner reading the gloss in a sorter-style page; no fourth machine pass. If it passes: ALIGN2 brief steps 3-4.
