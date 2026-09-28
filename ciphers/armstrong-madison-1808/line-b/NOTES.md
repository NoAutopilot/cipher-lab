# Armstrong line B -- step notes (account 3, session_019cJYkajEQyd7wXeaDJjfZF)

One section per step, numbers and controls side by side (CLAUDE.md rule 3), files under `line-b/<id>/`. Nothing here is
a reading; rule 10 wording throughout. The plan and its status column: `line-b/PLAN.md`.

## Step B1 (28 Sept 2026, 02:22-02:38 UTC) -- trailing-zero padding: the zero-specific hypothesis dropped, a decade-family structure found instead

**Hypothesis as registered.** The frame-127 compact Livingston key permits zeros appended on the right without changing
the meaning (ChatGPT PR 50; campaign H7 screened that key's values, not this rule on the target). If the target's key
does the same, a frequent 2-digit value v is also written 10v, and the 0-heavy units digit ARM-DESIGN reads as a fixed
member slot would be padding. Scripts: `b1/padding_test.py` (statistic, nulls, negative and positive controls, gate),
`b1/pairs.py`, `b1/shift_control.py`, `b1/decade_test.py`, `b1/family_test.py`; logs `b1/*_log.txt`. Offline, no
network, no subagent (0 of 4 vision calls).

**Statistics.** S_w = share of particle tokens (values 1-99) whose x10 form is present; r0 = Pearson correlation over
v = 10..99 between n(v) and n(10v); r_nz = the same against n(10v+1..10v+9); r_fam = against the whole decade
10v..10v+9; r_1xyz = against the 4-digit tier 1000+10v..1000+10v+9; r_row = against the same-row values 100h+v
(the layout of a printed 100-row form). Nulls (rule 3, each CAN differ from the target on these statistics):
(a) redraw the distinct x0 book values among multiples of 10, uniform or weighted by the target's own hundreds-block
profile (1,000-3,000 draws); (b) redraw every value >= 100 within its hundreds block with the units digits permuted
within the block (2,000 draws; `decade_test.py`, `family_test.py`).

**Gate, pre-registered (padding_test.py docstring) and met.** Positive control: en18 letters (369 tokens, a 99-word
particle list at 1-99, a book at 100-1899 with flat or 0-heavy units) with particles padded at p = 0.3: S_w 0.67-0.81,
percentile 100 on 6 of 6 seeds (both book variants). Negative control: the same letters unpadded (p = 0): S_w 0.07-0.39,
percentiles 22-81, 0 of 6 above p95. The four real THE=972 letters carry 0-5 tokens below 100 and cannot vary on this
statistic (S_w = 0 throughout) -- named here as a control that cannot fail, not counted (CLAUDE.md rule 3, bCAS/AX-5799).

| statistic | target | null (a) uniform: mean / p95 / pct | null (a) hundreds-weighted: mean / p95 / pct | null (b): mean / p95 / p99 / pct |
|---|---|---|---|---|
| S_w (particle tokens with x10 present) | 0.621 | 0.328 / 0.477 / 100 | 0.425 / 0.576 / 98.6 | -- |
| S_u (distinct particles with x10 present) | 0.417 | 0.288 / 0.375 / 99.0 | 0.326 / 0.417 / 92.1 | -- |
| S3 (3-digit tokens with x10 present) | 0.076 | 0.045 / 0.090 / 89 | 0.054 / 0.103 / 79 | -- |
| r0 n(v) ~ n(10v) | 0.574 | 0.001 / 0.199 / 100 (p99 0.314) | 0.109 / 0.313 / 100 (p99 0.387) | 0.155 / 0.375 / 0.458 / 99.9 |
| r_nz n(v) ~ n(10v+1..9) | 0.493 | -- | -- | 0.160 / 0.359 / 0.449 / 99.8 |
| r_fam n(v) ~ n(10v..10v+9) | 0.630 | -- | -- | 0.219 / 0.399 / 0.463 / 100 |
| r_1xyz n(v) ~ n(1000+10v..+9) | 0.208 | -- | -- | 0.129 / 0.295 / 0.368 / 78.7 |
| r_34 n(10v..+9) ~ n(1000+10v..+9) | 0.422 | -- | -- | 0.078 / 0.241 / 0.296 / 100 |
| r_row n(v) ~ n(100h+v) | -0.063 | -- | -- | -0.050 / 0.056 / 0.117 / 42.8 |

Shift control (`shift_control.py`): r for n(v) ~ n(10v+10k) is 0.12 / 0.11 / 0.41 / **0.57** / 0.20 / 0.08 / 0.10 for
k = -3..+3; the k = -1 shoulder is the lag-1 autocorrelation of the particle counts themselves (0.351: 17/18, 47/48,
11/12 are adjacent frequent values), not a smooth trend. Unit offsets +1..+9 at k = 0: 0.17, -0.03, 0.19, 0.25, 0.03,
0.34, 0.38, 0.22, 0.12.

**Result.** (1) The zero-form alignment is real (r0 at the 99.9th-100th percentile of three nulls), BUT the non-zero
forms align just as strongly (r_nz 0.493, 99.8th percentile), which trailing-zero padding does not produce: padding
predicts r_nz at the null level. The padding hypothesis is **dropped as the explanation**; the 0-heavy units digit is
not a padding artefact. (2) What the numbers do show, control-backed: the 3-digit values 100-999 are used in
proportion to the 2-digit value that shares their first two digits (r_fam 0.630 vs null p99 0.463), and the 4-digit
values 1xyz are used in proportion to the 3-digit values xyz (r_34 0.422 vs p99 0.296), while the 4-digit tier aligns
only weakly with the 2-digit heads (r_1xyz 0.208, n.s.). The same-row parse of a printed 100-row form (value = 100 x
column + row, the reel-9 THE=812 layout and the Wouves layout) shows nothing (r_row -0.063, 43rd percentile). The
organising unit of this code is the DECADE at all three tiers -- a hierarchical layout in which the 2-digit number is
the head of a group and the third digit and the leading 1 subdivide it -- not a flat contiguous list and not a 100-row
form. This extends ARM-DESIGN's two-level verdict: its "particle block" and "book" are not independent lists.

**Census under the decade parse (`family_test.py`).** 73 of the 90 possible roots 10-99 are in use, carrying 352 of the
369 tokens (17 tokens are single digits 1-5); 43 roots occur as a bare 2-digit head; 51 roots show two or more distinct
forms; 17 roots have one token. Tokens per root: 17 x1, 12 x2, 10 x3, 6 x4, 5 x5, 6 x6, 4 x7, 3 x8, 2 x9, 2 x11,
2 x14, 1 x16, 2 x17, 1 x26. Suffix-digit profile (3-digit tier / 4-digit tier): 0: 46/46, 1: 24/23, 2: 4/5, 3: 3/0,
4: 14/12, 5: 1/1, 6: 15/7, 7: 7/15, 8: 4/8, 9: 1/1 -- the same skew in both tiers (ARM-DESIGN's 0 >> 1 > 4,6,7 >> 2,3,5,9),
so whatever the third digit means, it means it the same way in 100-999 and 1000-1999. Richest families: 17 (26 tokens:
17 x13, 170 x5, 176 x4, 1170 x3, 1176), 38 (17), 18 (17), 76 (16: 76, 760, 764, 768, 1760, 1761, 1762, 1764, 1767),
14 (14), 16 (14), 48 (11), 47 (11).

**Vocabulary under collapse rules** (`decade_test.py`): as transcribed 216 distinct / 139 singletons; trailing zeros
stripped 189 / 114; one trailing digit stripped from every value >= 100 (the "any suffix is a null" reading) 116 / 40 --
the last is too small a vocabulary for a 369-word English letter unless the shorthand runs carry most content words,
and ARM-DESIGN's decade_units_modal statistic (0.570 vs 0.501 null, z 2.76) already says repeated words keep their
suffix digit, so the suffix is not a free null; it is part of the value.

**Three readings consistent with the numbers, to be discriminated in B2 (re-scoped):** (a) stem + slot: the 2-digit
head is a stem and the suffix digit a fixed inflection or derivative class (the skew is the class frequency); (b)
alphabetical hierarchy: the 2-digit head is an alphabetical bucket whose members are the 3-digit and 4-digit values
(function words cluster in a few initial-letter buckets -- th-, an-, of-, in-, wh- -- so a frequent head predicts a
frequent bucket); (c) three separately alphabetical tiers whose letter-frequency profiles correlate. (c) predicts
r_1xyz about as high as r_fam, which is not observed; (a) and (b) both make the meaning of a 3-digit value depend on
its 2-digit head, a constraint no solver on file (ARM-C1, ARM3-LOOP, H27, the decimal-field and glyph models) has used.

**What this is not.** Not a reading, not a key, not a class change; nothing here is called new or first (rule 10).
The finding rests on Bourdeau's transcription, 98.4% matched to the manuscript witness (H17), and every statistic
above is on the numeric groups only (the shorthand runs and the marks are untouched). Rule 5: the target stays `open`.

**Requests:** none (0 to any host). **Cost:** one Fable session, about 16 minutes by the clock (date -u at 02:37), no subagent; the row's estimate
(2 USD) is what PLAN.md records; the real figure is the orchestrator's to read from get_session.

## Step B2 (28 Sept 2026, 02:40-02:5x UTC) -- which hierarchical layout reproduces B1? None of six; the column profile is the discriminating unknown

**Method.** `b2/designs.py`: six generative layouts encoded on en18 text (60 windows of 369 coded tokens per design,
words outside the design's vocabulary dropped as the target's shorthand-run wildcards), scored with B1's statistics
(r_fam, r_1xyz, r_34, r_row, S_w) plus the suffix-digit profile per tier (z0 share; share of the rare digits 2,3,5,9),
the 2-digit token share, distinct and singleton counts; target percentile per statistic. Designs: A stem + fixed
inflection-class digits, two stem series; A2 one stem series with a second class dimension at 1000+; B alphabetical
buckets headed by the bucket's most frequent word, members alphabetical in 10h+z then 1hz; Bf the same with members
in frequency order; C three separately alphabetical tiers (the two content tiers dealt alternately over the alphabet);
C2 as C with a frequency split between the tiers. Offline, 2.4 s, no subagent. Log: `b2/run_log.txt`.

| statistic | target | A | A2 | B | Bf | C | C2 |
|---|---|---|---|---|---|---|---|
| r_fam (head ~ 3-digit family) | 0.630 | -0.107 (p95 -0.06) | -0.112 | 0.064 (p95 0.27) | **0.491 sd 0.13, p95 0.715, pct 83** | -0.042 (p95 0.12) | 0.011 (p95 0.27) |
| r_34 (3-digit ~ 4-digit family) | 0.422 | -0.021 (p95 0.24) | 0.000 | 0.090 (p95 0.30) | 0.056 (p95 0.30) | -0.032 (p95 0.22) | 0.019 (p95 0.27) |
| r_1xyz (head ~ 4-digit family) | 0.208 | 0.093 (pct 80) | 0.000 | 0.252 (pct 35) | 0.024 (pct 92) | -0.032 | 0.010 (pct 95) |
| S_w | 0.621 | 0.005 | 0.006 | 0.085 | **0.604 (pct 55)** | 0.062 | 0.098 |
| z0 share, 3-digit tier | 0.387 | 0.541 | 0.538 | 0.109 | **0.354 (pct 77)** | 0.132 | 0.100 |
| z0 share, 4-digit tier | 0.390 | 0.809 | 0.017 | 0.085 | 0.157 (pct 100) | 0.088 | 0.095 |
| rare digits 2,3,5,9, 3-digit tier | 0.076 | 0.083 | 0.081 | 0.405 | 0.287 (pct 0) | 0.389 | 0.416 |
| rare digits 2,3,5,9, 4-digit tier | 0.059 | 0.000 | 0.000 | 0.326 | 0.392 (pct 0) | 0.393 | 0.404 |
| 2-digit token share | 0.358 | 0.827 | 0.959 | 0.522 | 0.497 | 0.626 | 0.620 |
| distinct / singletons | 216 / 139 | 98 / 44 | 68 / 20 | 168 / 115 | 170 / 116 | 169 / 116 | 171 / 118 |

**Result.** Every design is excluded on at least two statistics at percentile 0 or 100 over 60 letters. A and A2
(stem + inflection): r_fam is NEGATIVE in 60 of 60 letters -- the most frequent stems are function words, which do not
inflect, so under a stem design the richest heads have empty families, whereas in the target the three most frequent
heads (17, 18, 38) own the three richest families (26, 17, 17 tokens); the 2-digit share (0.83-0.96) and the
vocabulary (68-98 distinct) are also far off. C and C2 (three alphabetical tiers): r_fam and r_34 sit at 0 +/- 0.1, so
letter-frequency alignment between separately alphabetical lists does NOT produce the decade alignment -- the tiers
are linked by construction, not by the alphabet. B (alphabetical buckets, alphabetical members) fails r_fam. Bf
(alphabetical buckets whose members are ordered by frequency) is the only design that reproduces the ROW statistics --
r_fam 0.49 +/- 0.13 with the target inside its band, S_w 0.60 vs 0.62, z0 (3-digit) 0.35 vs 0.39, distinct and
singletons within range -- but it fails the COLUMN statistics decisively: it gives the rare digits 2,3,5,9 a 29-39%
share where the target has 6-8% in BOTH tiers, it puts z0 in the 4-digit tier at 0.16 vs 0.39, and it gives no 3-digit
to 4-digit alignment (r_34 0.06 vs 0.42). Any layout that fills ten slots per row with distinct words in frequency or
alphabetical order gives the tail digits 30-40% of the tokens; the target's rows put 85-90% of their tokens on the head
and the digits 0, 1, 4, 6, 7, 8, in the same proportions in the 3-digit and 4-digit tiers.

**What survives, as constraints for the next step (not a design yet):** (i) rows (decades 10-99) are the organising
unit and a row's popularity is shared by its bare head, its 3-digit members and its 4-digit members (B1); (ii) the
column digit carries a FIXED profile across the whole table -- 0 >> 1 > 4, 6, 7 > 8 >> 2, 3, 5, 9 -- identical in both
tiers, which a table of distinct words filled row by row does not produce; (iii) the bare head is the row's most used
member. (ii) is what an OPERATOR digit looks like (a fixed set of modifications applied to a root, with four of the ten
rarely needed), the same shape as the printed-form marks H14/H19 found this writer using in his office code -- a
compositional reading in which a group is root + optional prefix operator + optional suffix operator, 73 roots in use.
It is also what a sparsely filled grid looks like (rows with the head and a few members, the compiler using columns
0, 1, 4, 6, 7, 8 by habit). The two readings differ in a testable way: under operators, forms of one row are the same
word in different grammatical shapes and share their contexts; under a sparse grid they are different words that
happen to share a bucket. B2b (next) tests context similarity within rows against a row-label permutation null.
The cheap Bf-style simulations cannot separate them (they have no notion of context), so B2 is logged done with no
surviving design rather than re-tuned (rule 3's repeated-attempt clause).

**What this is not.** No reading, no key, no class change; the simulations are en18 English, so a French plaintext or
a syllabic root set is not addressed here. Requests: none. Cost: one Fable session, about 15 minutes by the clock, no
subagent; PLAN.md records the row's 3 USD estimate.
