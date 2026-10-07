# KHF-4 held-out family check, fr.3988 f.143r (Henri IV to Nevers, Dec 1593) -- pre-registration
Written and pushed before the blind read, 7 Oct 2026 ~19:5x UTC (clock read by date -u). Worker KHF-4 (account 4).

Question (KH1-F's named next step): does the f.143r hand write signs of the no.60 key family at all?

Why a new instrument: KH1-F's profile reported key60 share 89.9-91% on f.143r, but no one has measured what a sign set
from a *different* key scores when a reader is offered only the no.60 sheet and table -- so that share has no known
discriminating power (CLAUDE.md rule 3: a control must be able to fail differently from the target).

Material (sources): f.143r = Gallica btv1b9060634t canvas f304, region 450,1250,3500,700 native (../img/c304_reg.jpg);
positive control = fr.3986 f.152 leaf 298 (no.60, interlined), tools/keys/key60_atlas/src/f3986_c298_region.jpg, cipher
lines 1-2; negative control = BnF fr.4715 f.61r (Mayenne 1592 key, Tomokiyo no.38; not no.60), Gallica btv1b52509819x
canvas f137, region pct:12,33,82,25 (../img/m61_reg.jpg), scaled 0.6 to match sign height. 65 tiles: f143r 25, leaf298 20,
mayenne61 20, each 90 px around one sign, grey, autocontrast, 96 px, shuffled (seed 20261007) to t01-t65
(make_tiles.py; tile_map.tsv; key_sealed.tsv holds the sealed tags).

Blind read: one Sonnet subagent gets only the tiles, contact_sheet_264ext.png, atlas264.tsv, atlas264ext.tsv and
tools/keys/key60.tsv in a scratch folder. For each tile: the no.60 tag of the centred sign if its form matches the
sheet/table, else NONE; confidence H/M/L.

Statistics (score.py): S1 = share of tiles whose read tag equals the sealed tag (synonym classes: ⊥=inT, alpha=∝=α,
do=ꝺo, r=ꝛ, pi=π, lam=λ); S2 = in-family rate = share read as a non-NONE tag at H or M confidence. Wilson 95% CIs.

Gate (fixed now, not to be lowered):
 (a) positive control leaf298 S1 >= 80%; else NON-TEST (reader/tiles cannot read the known hand), stop.
 (b) negative control mayenne61 S2 <= 50% and >= 30 points below leaf298 S2; else NON-TEST (in-family statistic does not
     discriminate a foreign key), stop, logged as such -- not a pass and not a fail for f.143r.
 (c) with (a) and (b) met: f.143r PASSES (licensed as no.60 family -> two blind passes on f.143r + shuffled-key control)
     only if f143r S1 >= 80% AND f143r S2 >= mayenne61 S2 + 30 points. Otherwise FAIL: log the key family as
     not-shown-no.60 and stop.
Limits stated in advance: the f.143r sealed tags are one reader's (KHF-4) eye tags, not gloss-confirmed (no gloss exists);
the negative control differs in hand as well as key, so a low S2 there may partly reflect the hand.
