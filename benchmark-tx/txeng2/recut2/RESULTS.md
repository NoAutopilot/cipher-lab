# TXE2-RECUT2 results: fr.3623 f.23r stroke-level gloss removal (9 Oct 2026, 19:13-19:2x UTC by date -u)

LANE TX-ENGINEER-2 incarnation 2, round 6, PREREG `benchmark-tx/PREREG-txeng2-6.md` section R3b (binding). Item
bir1591-f23r-gloss, truth-unknown (PREREG-txeng2-0 Amendment 3): no err_true, no pool entry. Read-free: 0 subagent
calls, 0 reads, 0 network requests (the 16 inputs are `benchmark-tx/txeng2/recut/try2_midpoint/f23r_L*.jpg`).

**Outcome: masked re-cut untestable by image means; needs a person's mask or a different witness. The family retires
for this leaf (third attempt: TXP-B23, TXE2-RECUT, this job). No crops committed under recut2/crops/.**

## Instrument (different from R3's whole-component mask)
`tools/gloss_cut.py` (new, `--help`, test `tools/tests/test_gloss_cut.py`, SYSTEM.md and tool_shelf.tsv rows): a
row-wise cut *through* joined components. Per 160 px column window (step 40) it finds the cipher row's core band
(the contiguous run of rows around the ink-profile peak with >= 0.3 x peak ink, ink < 150), median-smooths the band
edges across x, keeps an envelope core top - UP .. core bottom + DOWN, and inpaints every ink pixel outside it (2 px
rim) from the local paper shade (`iiif_lines.local_paper`). `--stem-width W` keeps an outside piece that touches the
envelope and is at most W px wide (a sign's ascender/descender), removing wider pieces and pieces wholly outside.

Settings tried (each on all 16 crops; overlays judged by eye, crop by crop):
| setting | command tail | gloss letters left | cipher strokes cut |
|---|---|---|---|
| m10 | `--up 10 --down 10` | 0 | every cipher crop: descenders of ‡/ƒ/ч/ψ-type signs, base bars of Δ-with-bar signs (e.g. L04_s1 ƒ read as + after the cut) |
| m10s | `--up 6 --down 6 --stem-width 12` | 0 | every cipher crop: the curved descenders and bars are wider than 12 px, so the stem filter spares almost none |
| m14 | `--up 14 --down 14` (sites checked only) | 0 at the five letter sites | not tabulated (between m10 and m22) |
| m22 | `--up 22 --down 22` | 0 | every cipher crop still: 3-8 strokes per crop by eye (`residue_m22.tsv`) |

Command (m22; the others differ only in the tail): `python3 tools/gloss_cut.py
benchmark-tx/txeng2/recut/try2_midpoint/f23r_L*.jpg --out <scratch>/m22 --up 22 --down 22 --debug`

## Per-crop table (m22, the widest margin; `residue_m22.tsv`)
| crop | gloss letters left | gloss fragments left | cipher strokes cut (approx., by eye) |
|---|---|---|---|
| L02_s1 | 0 | ll stem tops | 4 |
| L02_s2 | 0 | l stem tops | 3 |
| L04_s1 | 0 | q stem stub | 4 |
| L04_s2 | 0 | q stem stub joined to the sign beneath; d stem top | 3 |
| L06_s1 | 0 | none seen | 6 |
| L06_s2 | 0 | a remnant (small mark) | 4 |
| L08_s1 | 0 | l stem tops | 4 |
| L08_s2 | 0 | l stem tops | 5 |
| L10_s1 | 0 | none seen | 4 |
| L10_s2 | 0 | i dot; p stem stub inside a sign | 4 |
| L12_s1 | 0 | none seen | 7 (base bars under Δ-type signs) |
| L12_s2 | 0 | none seen | 8 |
| L14_s1 | 0 | none seen | 3 |
| L14_s2 | 0 | n/a (plain subscription) | n/a |
| L16_s1 | 0 | none seen | 4 |
| L16_s2 | 0 | n/a (plain signature) | n/a |

## Verdict and why the gate's letter count is not taken as a pass
The declared gate counts legible gloss letters, and that count reaches 0 on all 16 crops at every setting. It reaches 0
only by cutting cipher strokes: at m10 and with the stem filter the descenders and base bars of ‡, ƒ, ч, ψ and
Δ-with-bar signs go in every cipher crop, and at m22, the widest margin tried, 3-8 such strokes per crop still go
(the q, a and up sites are cleared at m22 only because the cut also takes the strokes below them). On this hand
the gloss rows and the cipher ascender/descender rows overlap in y, so no envelope separates them. A sign with
its descender or bar cut becomes another sign (ƒ -> +, Δ-with-bar -> Δ). A read of these crops would therefore
measure the cut, not the effect of masking the gloss, which is what R3 asks. The tool's own scope line says it must not be used where cipher
strokes reach past UP/DOWN, and that is the case here. So I log the brief's "any letter left" outcome
wording rather than commit read crops: **masked re-cut untestable by image means; needs a person's mask or a different
witness**. The lane may overrule this reading of the gate. The m22 crops are reproducible from the command above,
and nothing was committed as a read input.

## Files (before/after)
- `before_overlay_try2_gloss_marked.jpg` -- copy of recut/try2_gloss_marked.jpg (R3's residue, blue letter / orange fragment).
- `after_overlay_m10.jpg`, `after_overlay_m10s.jpg`, `after_overlay_m22.jpg` -- all 16 crops stacked, blue envelope,
  removed ink orange (Okabe-Ito; the cue is the line and the tint, not hue alone).
- `gloss_sites_m14_m22.png` -- the five letter sites (L04_s2 q, L06_s2 a, L06_s2 fr, L10_s2 i/up, L04_s1 q) after the
  cut, m14 (top five strips) then m22 (bottom five).
- `gloss_cut_m10.tsv`, `gloss_cut_m10s.tsv`, `gloss_cut_m22.tsv` -- per crop core band median, removed/kept ink px.
- `residue_m22.tsv` -- the per-crop table above.

## Suggestions (one line each, not done, Usage 7)
- R3 on this leaf needs a person's stroke mask (sorter-style, the gloss strokes painted out by hand) or another witness
  of the same cipher without the gloss.
- Do not re-brief gloss_cut.py or a component mask on f.23r without one of those (third-attempt rule).

## Calls, requests, cost
Subagent calls 0; reads 0; requests per host 0 (Gallica 0). Cost: the orchestrator get_session reading.

Openings of eval truth: 0

## sha256
Every file in this folder and the tool/test are listed with sha256 in `SHA256SUMS` (this folder), written before
the commit; the commit hash is in the done line.
