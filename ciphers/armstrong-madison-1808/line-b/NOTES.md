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

## Step B2 (28 Sept 2026, 02:40-02:43 UTC) -- which hierarchical layout reproduces B1? None of six; the column profile is the discriminating unknown

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
a syllabic root set is not addressed here. Requests: none. Cost: one Fable session, about 4 minutes by the clock (02:40-02:43, the ROOM done line's '02:58' is a typing error), no subagent;
PLAN.md records the row's 3 USD estimate.

## Step B2b (28 Sept 2026, 02:44-02:45 UTC) -- operator digit vs grid slot by context similarity: CONTROL BELOW GATE, non-test

**Method.** `b2b/context_sim.py`: every group parsed as (row, form); each distinct value's context = a 12-cell histogram
of the classes of its left and right neighbours (bare head, 3-digit, 4-digit, single digit, shorthand run, line edge);
statistic = the count-weighted mean over the 51 rows with two or more forms of the pairwise similarity (1 - JSD) between
the row's forms; null = row labels permuted among values of the same tier and count bin (2,000 draws). Gate,
pre-registered in the docstring: positive control (en18 letters encoded with a real stem + suffix-class grammar,
design A of B2, 3 seeds) above its own null p95 on 3 of 3 seeds, negative control (B2's Bf layout, different words per
row) not, before the target is read.

| letter | rows >= 2 forms | statistic | null mean | null p95 | percentile |
|---|---|---|---|---|---|
| positive: stem grammar seed 0 / 1 / 2 | 21 / 30 / 30 | 0.606 / 0.518 / 0.552 | 0.549 / 0.488 / 0.544 | 0.629 / 0.561 / 0.596 | 87.5 / 74.8 / 59.6 |
| negative: Bf buckets seed 0 / 1 / 2 | 51 / 51 / 40 | 0.455 / 0.445 / 0.404 | 0.479 / 0.451 / 0.427 | 0.511 / 0.488 / 0.462 | 9.8 / 39.4 / 12.2 |
| target (printed by the script, NOT licensed by the gate) | 51 | 0.372 | 0.358 | 0.382 | 82.8 |

**Result: GATE NOT MET (positives at the 60th-88th percentile of their own null, 0 of 3 above p95).** Six neighbour
classes on either side of a token carry too little information at 369 tokens to tell inflected forms of one word
from different words in one bucket; the negative control behaves as it should (below its null), so the instrument
points the right way but has no power at this N. Per rule 3 the target's own number (pct 82.8) is not read as
evidence; the operator-vs-grid question is logged **untestable by this instrument at N=369**, not answered, and is not
re-run with a finer class set or another knob (rule 3's repeated-attempt clause: a genuinely different instrument or
new material is needed -- the two readings differ in what the rows MEAN, which a key, a second letter or a decode
would settle at once). Row dropped (non-test). Requests: none; no subagent; about 2 minutes by the clock (02:44-02:45).

## Step B3 (28 Sept 2026, 02:51-03:0x UTC) -- Armstrong's own papers and the Livingston family papers: catalogued, nothing reachable from the cloud, two `needs: doc` branches named

**Positive control (route check) first.** `www.loc.gov/search/?q=Livingston+cipher&dates=1800/1810&fo=json` returns the
known cipher witnesses (mjm014121 Livingston to Madison 17 Sept 1803 "partly in cipher", mjm014115, mjm014276,
mjm014252/3, mjm014224, mjm014277, mjm014123, mtjbib012450, mjm022021/022119/022027) in its first 14 rows -- the
route surfaces what it should before any miss below is read as a search result. `findingaids.library.nyu.edu`
answers a direct finding-aid URL with a browser User-Agent (200) but its search endpoint 403s with either UA;
`archives.nypl.org`, `researchworks.oclc.org` (ArchiveGrid), `findingaids.loc.gov` and `nyhistory.org` all 403 from
this container (one attempt each, no retry loop); `fdrlibrary.org` serves its PDF (200, 952 KB) but this container has
no PDF text tooling (no poppler; `pypdf`/`pdfminer.six` install but fail on the container's broken `cryptography`
module; a hand-rolled stream inflater found no text operators) -- the FDR aid was NOT read here, so the ChatGPT
22:44 checkpoint's sentence about it ("Aldrich family/Rokeby material is one microfilm roll, roughly 200 items, over
half concerning the French ministry") stands unverified.

**What was found.**
1. **Armstrong's own papers.** Skeen's biography (*John Armstrong, Jr., 1758-1843*, 1981; IA `johnarmstrongjr10000skee`,
   lending-only, searched through the be-api full-text endpoint, 10 queries) cites the **Rokeby Collection** (the
   Armstrong-Astor-Chanler-Aldrich family papers at Rokeby, Barrytown NY, private) for "Memoirs of Rokeby" and for
   Armstrong letters of 1811-1836 (to Spencer, Mar. 1811 / Jan. 1812 / Mar. 1836); no Rokeby citation dated 1807-1808
   surfaced (phrase queries "Rokeby Collection 1808" / "1807": 0 hits, a loose test). The word "cipher" does not occur
   in the book; "cypher" once, in the 1813-14 War Department context (a suggestion to develop a cypher for naval
   commanders). The 20 Feb 1808 letter is not discussed ("February 20, 1808": 0 hits). Skeen's Paris-years sources are
   the DUSMF despatches, the Madison and Jefferson Papers (LC) and the **Warden Papers, MdHS** (Armstrong to Warden,
   Sept. 1, 2, 4, 12-15, 24, 1808 among about twenty 1804-1810 letters, per Hoyt 1943 as the ChatGPT 22:44 checkpoint
   also records) -- Maryland Center for History and Culture MS 871, microfilm, not digitised, catalogue reachable
   (ChatGPT 22:44). NYPL MssCol 6743 "John Armstrong letters" (1 folder, 0.1 linear ft; minister-to-France and
   Secretary-of-War correspondence per the search snippet) -- the record itself 403s. Dartmouth holds four 1764-1814
   items, none from the Paris years (read). CBH 1974.002 (Brooklyn) Box 1 Folder 26 is a 1804 Jefferson dinner
   invitation to Armstrong, not a cipher item (read in the finding aid); Folder 25 is the Livingston 1803 letter
   already in ASKS 80 / campaign H8.
2. **Livingston family papers.** The Robert R. Livingston papers (1707-1862, NYHS; 57-reel microfilm edition 1658-1888,
   copies at LOC Manuscript Reading Room and NJHS MG 1194) have **no public finding aid** (Gotham Center page: "a
   finding aid is not publicly available"; NJHS page: reel list absent) and are not digitised anywhere reached. Whether
   they hold Armstrong-to-Livingston letters of 1807-1808 -- the natural home of a second letter in a cipher "concerted
   with another correspondent" who was Armstrong's brother-in-law and the previous minister -- cannot be settled from
   the cloud: it needs a person at NYHS or at the LOC microfilm (a reel index exists in the reading room).
3. **LOC sweep** `q=Armstrong+Livingston&dates=1805/1812` (228 results): no manuscript item pairing the two names; the
   hits are newspapers and the collection-level records already known.

**Result: search result, not a negative.** No key and no second letter reachable; two document branches for the
orchestrator (this line cannot edit ASKS.md): (a) `needs: doc` -- NYHS Robert R. Livingston papers, Armstrong
letters 1807-1808 and any cipher/key sheet (reading room or LOC microfilm; reel index on site); (b) `needs: doc` --
Rokeby Collection (private; Skeen's access was by the family's leave; approach through the Papers of James Madison
editors, ASKS 66, who may already know it). The Warden Papers (MdHS MS 871) are the third pool, already named by the
ChatGPT sprint and by ARM3-COR's LOC-side Warden check; a person's microfilm reading, not a cloud step.
Requests: loc.gov 2, tile.loc.gov 0, findingaids.library.nyu.edu 3 (one 403), fdrlibrary.org 1, be-api 10, archive.org
2, nypl 1 (403), oclc 1 (403), nyhistory 1 (403), jerseyhistory 1, gothamcenter 1, dartmouth 1; all >= 1.5 s apart;
no logins; 0 subagents. Cost: about 20 minutes by the clock; PLAN.md records the row's 3 USD estimate.

## Step B4 (28 Sept 2026, 02:53-03:00 UTC) -- Jefferson's own cipher items at LOC, 1785-1810: no numeric key of the target's shape; the 1803 Jefferson-Monroe coded note screens flat

**Method.** `www.loc.gov/collections/thomas-jefferson-papers/?q=cipher|cypher&dates=1785/1810&fo=json&c=100` (ARM-JEF
had searched the same collection only for "Armstrong cipher", 0 hits): 53 + 36 results, 83 distinct items, titles
and dates read; every item whose title names a cipher or key was classified; item JSON fetched for five; images
fetched from the item metadata's own file URLs (the guessed `image-services/iiif/service:mss:mtj:...` path 404s
for this collection -- use the `resources[].files[]` URLs). Scratch: `scratch/b4/` (not committed).

**Result.**
- Items titled as cipher material fall in 1785-1803 only: Code No. 8 with Adams (1785), the Madison word-list ciphers
  (1787, 1793), the Short/Carmichael/Pinckney/Humphreys ciphers (1791-94), Patterson's cipher (1802), "Thomas
  Jefferson, 1802, Ciphers and Data" (mtjbib012030, 8 images: pages 1, 3 and 7 looked at -- a Patterson-style
  letter, a 13-column mixed-alphabet grid and a 26 x 26 Vigenere table with a worked example; letter ciphers, not a
  numeric code; pages 2, 4, 5, 6, 8 not looked at), the Lewis cipher (1803) and "Thomas Jefferson to James Monroe,
  June 5, 1803, Cipher" (mtjbib012463). Nothing catalogued as a cipher between 1804 and 1810 except the Briggs-
  Wilkinson 1807 cipher (the Burr affair, a Wilkinson-Burr key, not Armstrong's). The two 1808/1810 "cypher" hits
  (Monroe to TJ 22 Mar 1808; TJ to Madison 25 May 1810) are the figurative word ("reduces the resident minister ...
  to a cypher"; "such a cypher in so important an office") in the transcriptions, read from the item JSON.
- mtjbib012463 is a four-line coded note in a numeric code (about 60 groups, 3- and 4-digit, values to about 1576),
  with Jefferson's clear postscript about a letter for Madame de Corny. LOC's master JPEG (2039 x 2543) is a
  microfilm-quality scan; 27 groups read by this session at M grade from 2x line crops (621 869 1402 640 226 1406
  1449 956 924 1299 1006 1136 1379 1576 1370 986 169 996 288 809 377 1113 1276 1067 1440 653 984) and run through
  `pool/signature_test.py`: units digits 0: 11%, 1: 4%, 6: 33%, 9: 22%, digit-0/1 share 15% (target 43%), digit-2/3/5/9
  share 33% (target 13%), THE=972 coverage 8/27. **Screen only (N=27, M-grade digits): not the target's signature.**
  This is presumably the Jefferson-Monroe code the ChatGPT sprint tied to the Monroe reel-9 printed form (campaign H12,
  THE=812, one-part 1-1700, already excluded on range); a full read of the note would settle which table, and is not
  this line's target.

**Verdict:** search result, not a negative -- the Jefferson Papers hold no numeric key catalogued in the target's
years, and the one 1803 numeric witness screens flat. Requests: loc.gov 7 (2 collection searches, 5 item JSON; one
timed out at 40 s and was not retried), tile.loc.gov 10 (9 previews, 1 master); >= 1.6 s apart; 0 subagents (this
session's own looks only). Cost: about 7 minutes by the clock (02:53-03:00); PLAN.md records the row's 3 USD estimate.
Container note for later steps: no PDF tooling and no Pillow at start (`pip install pillow` works; `pypdf` and
`pdfminer.six` install but fail on the container's broken `cryptography` module; `apt-get` refused).

## Step B9 (28 Sept 2026, 03:01-03:03 UTC) -- NARA frame 0029 read: a clear-text enclosure of the 17 Feb 1808 despatch, no lead

`images/M34-014-0029.jpg` (on disk since ARM-IMG; ARM-TR set it aside as "a later cover memo referencing a 17 Feb
letter") read in three bands by this session, grade H for the heading and M for the body (a fair copy in a clerk's
hand, the left half of the spread blank): "Paris 15th Feby 1808. Translation of an Extract of a Letter from the
Minister of Marine to Genl Armstrong, inclosed in Genl Armstrong's letter of the 17th Feby 1808 to the Secretary of
State. -- Observe to you moreover that the question ... [is not] as to a vessel sequestered in Port, but is to a Prize
made at sea and seized for a contravention of the Decree of the 17th Decr last; that the provisional sale ordered on
account of the average is for the interest as well of the captured as of the captors and it is directed ...
according to the case provided for by the Regulation of the 2d Frimaire 11th year." A translated extract of Decres
(Minister of Marine) to Armstrong on prize procedure under the Milan decree, enclosed in the 17 Feb 1808 despatch
(THE=972 family, the docket of frame 0645 already lists it); it names neither the 20 Feb letter nor a cipher.
Result: no lead; done. Requests: none; 0 subagents; 2 minutes by the clock.

## Step B7 (28 Sept 2026, 03:08-03:10 UTC) -- the 1700-1900 block is not a distinct sub-block: negative with nulls that can differ

After B1 the question is whether rows 70-89 of the 4-digit tier (values 1700-1899, plus 1900; 27 distinct values,
34 tokens) behave differently from the rest of that tier. `b7/block1700.py`: units-0 share of the block 0.294 (rest
of the tier 0.429) against a null that permutes the block label among 4-digit values of the same count bin (2,000
draws: mean 0.318, p05 0.176, p95 0.441, target at the 31st percentile); adjacent-pair count 5 against a
position-shuffle null (mean 2.73, p95 5, target at the 87th percentile). Neither statistic leaves its null. Power:
the hypothesised alternatives -- a spelling block with flat units (share about 0.10, below the null's p05 0.176 at
this N) or spelled names of three or four groups (about 12 adjacent pairs from eight names, above p95 5) -- would
have fallen outside these nulls, so the nulls can fail and the result is a control-backed negative at N=34: the
1700-1900 values are ordinary prefix-1 rows, as B1's tier alignment already implied. Row dropped as a negative (not
a non-test). Requests: none; 0 subagents; 2 minutes by the clock.

## Step B8 (28 Sept 2026, 03:13-03:16 UTC, re-scoped after B1/B2) -- the 2-digit heads follow neither an alphabetical nor a frequency order of the function words: negative, control-backed

`b8/head_order.py`: predicted count of head v under (a) an alphabetical 99-word function list (the 99 most frequent
en18 words in alphabetical order, head v = the v-th word) and (b) a frequency-ordered list; Spearman rho against the
observed bare-head counts and against the family totals (head + members) over v = 1..99; null = the 99 predicted
counts permuted (10,000 draws). Positive control: 60 en18 letters of 369 tokens whose heads ARE the alphabetical
list, rho mean +0.54 (p05 +0.42, p95 +0.65) -- the statistic separates at this N.

| prediction | observed | rho | null p05 / p95 / p99 | percentile |
|---|---|---|---|---|
| alphabetical | bare heads | -0.090 | -0.168 / +0.169 / +0.235 | 18.1 |
| alphabetical | families | -0.188 | -0.168 / +0.161 / +0.229 | 3.1 |
| frequency-ordered | bare heads | -0.022 | -0.168 / +0.165 / +0.230 | 41.9 |
| frequency-ordered | families | +0.135 | -0.165 / +0.168 / +0.228 | 91.0 |

**Result: negative with a control that can differ.** The heads are not the en18 function words in alphabetical order
(rho -0.09 against a positive control at +0.54) nor in frequency order. Either the row order is not alphabetical
(a two-part layout), or the rows are alphabetical buckets of uneven size headed by something other than the bucket's
commonest word, or the head list is not a function-word list at all (a syllabary or a root list). The observed heads
with three or more tokens: 17 (13), 18 (12), 38 (10), 1 (9), 14 (8), 12 (5), 47 (5), 11 (4), 48 (4), 3, 41, 45, 76 (3).
The original B8 (transition-profile assignment of particle identities with an LM-free instrument) is not run: B2b
showed neighbour-class contexts carry no usable signal at N=369, and the same coarse contexts would feed it.
Requests: none; 0 subagents; 3 minutes by the clock.

## Step B11 (28 Sept 2026, 03:17-03:20 UTC) -- row order: the alphabetical-bucket positive control has no power (non-test); the rows' own clustering recorded as an observation

`b11/row_autocorr.py`: lag-1 and lag-2 autocorrelation of family totals (head + 3-digit + 4-digit members) over rows
10-99, null = rows permuted (10,000 draws for the target, 2,000 per control letter). Positive control: B2's Bf layout
(alphabetical buckets headed by the commonest word), 60 en18 letters: lag-1 mean +0.096, only 12 of 60 letters above
their own p95 (gate 45); negative control (same layout, rows shuffled): -0.061, 0 of 60. **GATE NOT MET**: an
alphabetical-bucket layout of 90 buckets does not itself produce row-neighbour correlation at this N (22-word buckets
average out), so the instrument cannot license an alphabetical verdict either way. Non-test for the row-order
question; dropped. What the script printed for the target, recorded as an OBSERVATION and not as a licensed result:
lag-1 +0.308 (own null p95 +0.169, 99.6th percentile), lag-2 +0.253 (p95 +0.168, 99.1st) -- family popularity
clusters in row index (rows 11-18, 36-38, 45-48, 74-78 are jointly rich; rows 80-99 and 20-29 poor), the same fact
ARM-DESIGN's hundreds profile of the 3-digit tier and B1's head autocorrelation (0.351) show from other angles. It
means the row index is not random with respect to usage (a two-part layout with rows in random order would give
about 0), and it is stronger than an alphabetical-bucket layout gives; a layout that groups words by frequency class
into blocks of rows, or a table read column-wise from a printed page, would produce it -- to be tested only with an
instrument that has a passing positive control. Requests: none; 0 subagents; 3 minutes by the clock.

## Step B14 (28 Sept 2026, 03:20-03:27 UTC) -- the 20 Feb letter's own docket: "Armstrong 20th Feby 1808", nothing more

Frame 0033 (on disk) is the two-page spread whose LEFT page ends the target letter (last numeral lines "79 14 1160 ...
580 170", the closing "I have the honor to be, Sir, with very high consideration your most obedient & very humble
servant, John Armstrong", and the address "Mr. Madison Secretary of State of the United States Washington") and whose
RIGHT page opens the 22 Feb 1808 despatch (ARM-POOL2). The vertical endorsement beside the address, cut and rotated
(`scratch/b9/f33_docket_vert2.png`, read by this session, grade H): "Armstrong 20th Feby 1808" -- the office's plain
receipt docket; no "in cypher", no "not decyphered", no key or correspondent named. A second marginal text at the
fold belongs to the 22 Feb despatch's left margin ("...nes have ... to the ... Sec. M. ... 's letter ... rch", M) and
is the extract-forwarding note of the docket-0645 kind, not a cipher note. No lead; done.

## Step B15 (28 Sept 2026, 03:22 UTC onward, in progress) -- Graham's "duplicate in cypher with a postscript on the back": roll 14 frames 0632-0664 hold no second copy of the 20 Feb letter; the 22 Feb despatch's own back page carries a cipher postscript and a "by M. Patterson" docket

**Lead (from B6's Wayback pass).** John Graham, chief clerk, to Madison at Montpelier, 20 May 1808 (Founders Madison
99-01-02-3101, Early Access): "Among the Letters forwarded by this Mail you will find one in Cypher from Genl
Armstrong. It is the Duplicate of the one sent before & is forwarded to you now because there is a Postscript on the
back of it, which I beleive was not on the one before sent." Five days after Madison's "undecyphered letter from A."
sentence to Jefferson (15 May, 99-01-02-3082, confirmed by this pass's positive control fetch), and three days after
Jefferson wrote Madison (17 May, Jefferson 99-01-02-8015) that he retained "Pinckney's, Armstrong's, Livingston's &
mr Gallatin's letters" till another post.

**Search 1: NARA M34 roll 14, the unsurveyed duplicates batch.** Frames 0632-0664 fetched at 600 px through the
keyless IIIF v3 route (`catalog.archives.gov/iiif/3/lz%2F...%2FM34-014-NNNN.jpg/full/600,/0/default.jpg`, 33 requests,
1.6 s apart) and read as four contact sheets by this session. Positive control met: the known 9 March 1808 duplicate
(numeral code, "Friday" heading) is recognisable at 0643-0644 and the docket at 0645. Content: 0632-0641 are 1810
items (Armstrong to Daniel Parker, Somers's deposition, Parker's reply), 0642 an 1811 letter, 0646-0664 the printed
Douanes Imperiales sale catalogue of 1 Aug 1810. **No copy of the 20 Feb letter there.**

**Search 2: the frames between the 22 Feb despatch and 29 Feb.** Frames 0035 and 0036 (unsurveyed by ARM-POOL's
1-in-6 stride and by ARM-POOL2) fetched at 1400 px and read (H for the headings and docket, M for the body). 0035 LEFT
page = the last page of the 22 Feb despatch: a postscript "P.S. Another attempt on the two offensive decrees will I am
assured be made on wednesday next -- It will be 3.1001.1429.1351.963.307.1268.1490.1538.608.744.794.1217.855.659.
1288.1429.965.860.864.1001.962. The news of the Embargo came in good time -- by verifying one of my predictions, it
gave new weight to others. The ministerial belief now is that the present policy is dangerous, but till this
conviction shall be wrought in the Emperor also, no change will take place for the better." (THE=972 usage by its
values: 1001, 1429, 963, 962 ...), with the dockets "22d feb. to M. Madison by M. Patterson" and, vertically, "Genl
Armstrong 22d Feby 1808". 0035 RIGHT and 0036 = the 28 Feb 1808 despatch (Armstrong's complaints to the Prince of
Benevent and the answer). The 22 Feb despatch opens "Mr Patterson offers so good a conveyance that I cannot but
employ it" (frame 0033).

**Reading of the lead so far (M, to be settled by the Founders entry for 22 Feb).** Graham's "Duplicate ... with a
Postscript on the back" matches the roll-14 copy of the 22 FEBRUARY despatch (a postscript on its back, sent "by M.
Patterson", i.e. a second conveyance) at least as well as the 20 Feb letter, and the 20 Feb letter's own copy on roll
14 (frames 0030-0033) carries no postscript. If so, the duplicate is not a second witness of the target's ciphertext,
and Madison's undecyphered letter (15 May) and Graham's duplicate (20 May) are two different letters. What settles it:
the Founders Early Access entry for Armstrong to Madison, 22 Feb 1808 (id 2733, the one fetch in the 2729-2745 run
that failed twice; retried next) -- the editors print "Duplicate"/"RC"/postscript notes -- and, failing that, the
LOC Madison Papers Series 1 for a May 1808 receipt. Requests so far: catalog.archives.gov 35, web.archive.org 17 for
this step (plus B6's loop); 0 subagents.

**B15, continued (03:30-03:4x UTC).** The Founders Early Access entry for the 22 Feb despatch (id 2733, fetched on
the third try) prints the roll-14 text including the postscript and cites only "DNA: RG 59--DD--Diplomatic
Despatches, France"; no "Duplicate" note either way, so the Founders apparatus does not settle which letter Graham's
duplicate was. The Founders entry for the 20 Feb letter (id 2728) was already read by ARM-REC3: bare citation, no
apparatus. LOC's James Madison Papers catalogue (`?q=Armstrong&dates=1808/1808`, 21 results) lists no Armstrong item
between January and August 1808, so a duplicate that reached Madison at Montpelier is not catalogued in his own
papers as an item (search result; the LOC item list for 1808 is complete at the item level for the Series 1
correspondence, but a duplicate could have been returned to the Department's files). Roll 14 was then closed for
February-March 1808 as far as the route allows: frames 0049 (clear), 0050 (a French clerical enclosure, clear) read;
frames 0051-0054 and 0056-0060 are being fetched one per 75 s (`scratch/b15/slow_fetch.sh`) because
catalog.archives.gov began answering the 600-px IIIF request with its HTML app shell after about 35 requests in
quick succession -- a throttle, cleared by a 45-s pause on one retry, re-triggered by a 3-s cadence; good-citizen
rule: no further bursts on that host this session. Weber 1979 (IA `unitedstatesdipl0000webe`, be-api full text, 8
queries) says only that Armstrong "wrote 40 letters in code to James Madison beginning in late 1804", that some
DUSMF despatches "still remain only in code form", and lists "Gen. Armstrong XI" among the Brant worksheets (the
Box 37 material of ASKS 77) -- no private cipher named.

**B2 addendum (03:5x UTC, `b2/addendum_log.txt`).** Row-usage shape of the target against the same 60-letter
simulations: rows used 73 (Bf mean 73.8, p05-p95 68-79; B 73.7; A 71.9), rows without a bare head 0.411 (Bf 0.460,
0.368-0.558; B 0.448; A 0.200, p95 0.290 -- excluded again), rows whose only token is the head 0.110 (Bf 0.098,
0.042-0.153; B 0.106), head share of family tokens 0.327 (Bf 0.497, p05 0.444; B 0.522; A 0.827 -- all three at
percentile 0). So the target's rows are used the way an alphabetical-bucket layout uses them in three of four
statistics, but its bare heads carry a third of the family tokens where a bucket headed by its commonest word gives
half: the head is NOT the bucket's most frequent word (a bucket headed by its alphabetically first word, or a smaller
bucket, would lower the share). This narrows B2's surviving constraint without settling it.

## Step B6 (28 Sept 2026, 03:03 UTC onward; Madison half done 04:10) -- the reply chain on Founders Online via Wayback: one new sentence (Graham's duplicate), nothing else from mid-May to 9 August 1808

**Route.** LOC's own transcription search failed its positive control (`q=undecyphered` returns 0 in the Madison and
Jefferson collections for 1808-09 although the 15 May 1808 sentence exists), so the instrument is Founders Online's
Early Access pages through the Wayback Machine (`web.archive.org/web/2025id_/https://founders.archives.gov/documents/
<series>/99-01-02-<id>`), enumerated from the CDX index (4,290 captured Madison ids; 1,395 in 2700-4300), fetched one
at a time 1.6 s apart with one retry (`scratch/b6/wb_loop.sh`; the host resets about half the connections, as
ARM-REC3 found). Positive control: id 3082 returns "The undecyphered letter from A. ..." verbatim (met).

**Read: Madison series ids 2729-2745 (21-25 Feb 1808) and 3084-3400 (16 May-9 Aug 1808), 319 pages, grep for
cypher / cipher / decypher / "20th Feb" / "no key" etc.** Armstrong-titled documents in the run: 16 May, 31 May,
6 June, 25/27/29 June, 7/8/18/23/25/26/31 July, 7 Aug (x2) from Armstrong; Madison to Armstrong 21 and 22 July 1808
(the two instruction letters: neither mentions the February letter, a cypher, or a key). Hits: only (1) Madison to
Jefferson 15 May (the known sentence) and (2) **John Graham to Madison, 20 May 1808 (id 3101)**: "Among the Letters
forwarded by this Mail you will find one in Cypher from Genl Armstrong. It is the Duplicate of the one sent before &
is forwarded to you now because there is a Postscript on the back of it, which I beleive was not on the one before
sent" -- followed up as B15. Graham's 27 May letter refers to Madison's "letter of the 20th" on another matter (a
Genl T. inquiry), not the cipher. 26 ids failed both fetches and are being retried after the Jefferson run
(`chain2.sh`). Jefferson series ids 8000-8040 (15-23 May 1808) read in the first pass: Jefferson to Madison 17 May
(8015) "I retain till another post Pinckney's, Armstrong's, Livingston's & mr Gallatin's letters"; 8003-8090
re-run with retries in progress. **Result so far: search result, no new sentence about the cipher beyond Graham's;
the reply chain as far as 9 Aug 1808 is silent on the undecyphered letter after 15-20 May.** Requests:
web.archive.org about 420 so far this step (single-threaded, 1.6 s apart, one retry per id); 0 subagents.

**B6 complete (04:2x UTC).** The 26 failed Madison ids were all recovered on the retry pass (`madison_retry.tsv`, 0
failures left): no further hit. Jefferson series ids 8003-8090 (15 May-early June 1808, 89 pages, 2 still failing
after two retries): only the cross-listed 15 May sentence (8003) and a figurative "decypher" (8025, to Randolph
Harrison); Jefferson's letters to Madison of 17-31 May say nothing more about Armstrong's cipher; Lafayette to
Jefferson (8071) mentions Armstrong in the ordinary way. **Verdict: done, search result** -- in the whole reply chain
reachable (Madison 21-25 Feb and 16 May-9 Aug 1808, Jefferson 15 May-early June 1808) the undecyphered letter is
named twice only: Madison to Jefferson 15 May and, five days later, Graham's duplicate-with-postscript (B15). No
letter names the correspondent, the key, or a later decipherment. B12 (Aug-Dec 1808) stays open at its rank.
Requests this step: web.archive.org about 760 in total (3 passes, single-threaded, 1.6 s apart), loc.gov 9;
0 subagents. Time: 03:03-04:25 UTC by the clock, mostly background waiting.

**B15 closed (03:5x-04:27 UTC): the whole of roll 14 screened; no second copy of the 20 Feb letter on the reel.**
Route change: NARA serves the entire roll as one PDF (`catalog.archives.gov/medialz/dc-metro/rg-059/603720/M34/
M34-014/M34-014.pdf`, 68.9 MB, 668 pages, page N = frame N, checked on frames 0030-0033; one request, no throttle),
the same form ARM-CORR used for M30/M31. Rendered with PyMuPDF (`pip install pymupdf` works in this container) at
26-40 dpi into contact sheets (`scratch/b15/sw_*.jpg`, `lo_sheet_*.jpg`, `pdf_sheet_50_61.jpg`) and every page 1-668
looked at by this session: at that scale a page of numeral groups is unmistakable (frames 0030-0032 of the target,
0024, 0039-0040, 0045, 0643-0644 all stand out as the positive control), and the only dense-numeral pages on the reel
are those known ones plus 0121 (23 Aug 1808, THE=972 per ARM-POOL2), 0232 (1809, short runs), 0436-0437 (a numeral
letter of Dec 1809) and 0494 (a numeral letter of Feb 1810) -- the last two never surveyed, screened at 110 dpi below.
**Result: search result with its positive control -- roll 14 holds ONE copy of the 20 Feb letter (frames 0030-0033)
and no duplicate.** (An automatic ink-run statistic, `page_screen.py`, was tried first and failed its known-answer
control -- 5 of 7 cipher pages inside the clear-page range -- so the eye sweep, not the statistic, is the screen.)
Reading of Graham's sentence, M: the "Duplicate ... with a Postscript on the back" was most probably the 22 Feb
despatch's second copy -- roll 14's 22 Feb copy carries a cipher postscript on its back and the docket "by M.
Patterson" (frame 0035), the 20 Feb copy carries none, and no second copy of either letter is on the reel or
catalogued in the LOC Madison Papers -- so the undecyphered letter (15 May) and the forwarded duplicate (20 May) are
two different letters, and no second witness of the target's ciphertext is reachable. B15 done. Lesson for the
lane (for the orchestrator): a NARA microfilm survey should fetch the whole-reel PDF once and screen every frame at
26 dpi, not sample 1 frame in 6 through the throttled IIIF route; 18 contact sheets close a 668-frame reel in one
session. Requests: catalog.archives.gov 1 (PDF) + 14 IIIF (9 of them answered with the app shell, throttled).

## Step B18 (28 Sept 2026, 04:28-04:30 UTC) -- the two unsurveyed numeral letters on roll 14 are office code: screened out at sight

Pages 0436-0437 (Paris, 10 November 1809, "Sir," then about 20 lines of numeral groups with a clear close "and
whether it will be better with 305, for whom it is no doubt equally intended is very doubtful. 972 305 821 820 1404
1165") and 0494 (Paris, 2 February 1810, to Robert Smith: "501 962 1187 576 [interlined: Mr Petry] called on me
to-day to inform me that a proposition would be made to me in a day or two 1064 1065 1478 1201 470 [interlined: for
forming a convention] on principles of reciprocal advantage 111 945 274 1116 1354 292 806 1219 811"), read at
110 dpi from the reel PDF. Both are THE=972 usage: the group 972 ("the") recurs a dozen times on page 0436 and the
period interlinear glosses on 0494 are the office key's readings; the target never uses 972 and has no interlinear
gloss. Page 0232 (1809) likewise (972, 1116, 1201 in short runs inside clear prose). No pool candidate; done.
Requests: none (local PDF); 0 subagents; 2 minutes by the clock.

## Step B17 (28 Sept 2026, 04:28-04:3x UTC) -- roll 13 (Nov 1804-Dec 1807) screened whole: every numeral despatch is THE=972 with period interlinear decodes; no earlier letter in the target's code

Whole-reel PDF `M34-013.pdf` (91.2 MB, 395 pages, one request), 14 contact sheets at 26 dpi read by this session
(`scratch/b17/r13_*.jpg`), then the top third of every dense-numeral page at 110 dpi. Positive control met: the 27 Dec
1807 duplicate at page 390 stands out on its sheet (ARM-POOL2's known THE=972 item). Dense-numeral pages found: 12,
16, 58, 97 (10 Sept 1805), 110, 121-122 (17 Feb 1806, "Duplicate"), 141, 150-151, 160 (1 June 1806), 189, 193-201
(a long 1806 despatch, pages numbered 6-13 in the hand), 224-225, 232-233 (29 March 1807, "Duplicate Private"),
378, 390-391. Every one read at 110 dpi carries the office group 972 many times per page and a period interlinear
pencil decode ("All the points in controversy between his Catholic Majesty and the U. States were..."; "Mr Monroe has
no doubt communicated to you..."), the roll-13 marginal decodes Bourdeau harvested for his THE=972 table. None shows
the target's 0/1-heavy units or shorthand runs. **Result: search result with its control -- Armstrong's despatches
Nov 1804-Dec 1807 on roll 13 are all in the office code; no earlier use of the private code survives in DUSMF.**
Requests: catalog.archives.gov 1; 0 subagents.

## Step B19 (28 Sept 2026, 04:31-04:32 UTC) -- B1's statistics under the REAL period tables: the family's own tables do not produce the target's row structure

`b19/real_tables.py`: 60 en18 letters of 369 coded tokens encoded with WE028 (Monroe's table as transcribed by
Tomokiyo, 1,228 single-word entries to value 1260 in `tools/data/uscodes-1800/WE028.tsv`) and with Bourdeau's THE=972
table (527 words to 1600), scored with B2's statistics (words the table lacks dropped as wildcards; caveat: both
tables are partial and word-only, so their letters carry 90-127 distinct values against the target's 216).

| statistic | target | WE028 letters: mean, p05-p95 (pct) | THE=972 letters: mean, p05-p95 (pct) |
|---|---|---|---|
| r_fam | 0.630 | -0.021, -0.10 to 0.15 (100) | -0.023, -0.05 to 0.00 (100) |
| r_34 | 0.422 | -0.012, -0.08 to 0.09 (100) | -0.057, -0.09 to -0.02 (100) |
| r_1xyz | 0.208 | -0.046, -0.09 to 0.11 (97) | 0.131, -0.04 to 0.41 (65) |
| r_row | -0.063 | 0.058, -0.06 to 0.27 (5) | 0.000, -0.06 to 0.09 (2) |
| S_w | 0.621 | 0.072, 0.00 to 0.25 (100) | 0.023 (98) |
| z0 share 3-digit / 4-digit | 0.387 / 0.390 | 0.089 / 0.144 (100 / 100) | 0.094 / 0.100 (100 / 100) |
| rare digits 2,3,5,9, 3-digit / 4-digit | 0.076 / 0.059 | 0.462 / 0.335 (0 / 0) | 0.615 / 0.332 (0 / 0) |
| 2-digit token share | 0.358 | 0.042 (100) | 0.006 (100) |

**Result, control-backed (the 60-letter bands are the control):** a real blockwise-alphabetical table of the State
Department family gives r_fam and r_34 at zero, flat suffix digits and almost no 2-digit tokens; the target sits at
percentile 100 or 0 on every row statistic. The target's decade-family structure (B1) is therefore not a property
of the family's tables that ARM-A2 already excluded by value; it is a different design from the office codes. Requests:
none; 0 subagents; about 1 minute by the clock.

## Step B21 (28 Sept 2026, 04:31-04:33 UTC) -- Gallatin as the "other correspondent": nothing in print or in the reachable finding aid

Step 1, offline: `tools/data/en18/writingsalbertg01gallgoog.txt.gz` (Adams, *Writings of Albert Gallatin* I, 1879):
no Armstrong passage dated 1807-08 or naming France/Paris; the volume's seven cipher/cypher mentions are the 1813-14
Ghent-mission correspondence (Crawford's cipher). Step 2: be-api full text on Adams's *Life of Albert Gallatin*
(IA `bwb_P8-BXX-928`; queries "Armstrong 1808", "Armstrong cipher", "General Armstrong"): Armstrong appears only in
the 1804 nomination fight, the 1810 Cadore letter and the Clinton politics; no cipher. Step 3: the NYHS Gallatin
Papers Project records finding aid (`findingaids.library.nyu.edu/archives/rg_21_3_1/all/`, 70 KB, read): no Armstrong
and no cipher entry; the Gallatin Papers themselves (NYHS, microfilm edition) have no item-level aid reachable from
the cloud. Positive control for step 1 not run explicitly (the volume's 1808 embargo letters were not grepped); the
result is a search result at the print level only: **no evidence that Gallatin was the correspondent; not excluded.**
Requests: archive.org 1, be-api 3, findingaids.library.nyu.edu 1; 0 subagents.

## Step B22 (28 Sept 2026, 04:34-04:38 UTC) -- row burstiness: CONTROL BELOW GATE, non-test

`b22/burstiness.py`: mean over rows with >= 3 tokens of (median gap between occurrences) / (uniform expectation),
null = positions permuted. Positive control (rows = stems, 60 letters): only 18 of 60 below their own p05 (gate 45);
negative control (Bf buckets): 13 of 60 (gate <= 6). Neither control separates -- English stems in a 369-token
window are not bursty enough for a median-gap statistic, and the bucket layout is nearly as bursty as stems. Target
printed, not licensed: 0.811 over 44 rows, 34th percentile. Dropped as a non-test; not re-tuned (rule 3).

## Step B24 (28 Sept 2026, 04:35-04:38 UTC) -- row-count distribution: the target's rows are FLATTER than either reading's control band

`b24/rowcounts.py`, 60 letters per control:

| statistic | target | rows = stems (A): mean, p05-p95, pct | Bf buckets: mean, p05-p95, pct |
|---|---|---|---|
| top-10 rows' share of row tokens | 0.409 | 0.511, 0.444-0.618, 2 | 0.489, 0.444-0.550, 0 |
| largest row's share | 0.074 | 0.128, 0.084-0.187, 2 | 0.120, 0.079-0.165, 5 |
| Zipf slope (rows with >= 2 tokens) | -0.725 | -0.860, -0.98 to -0.77, 98 | -0.839, -0.92 to -0.76, 100 |
| rows used | 73 | 72.2, 63-78, 42 | 73.2, 66-78, 37 |

**Result, both controls outside the target:** the target uses its 73 rows more evenly than either a one-word-per-row
or a 22-word-bucket layout of English produces -- its largest row (17, 26 tokens) carries 7.4% of row tokens where
"the" alone gives 8-19% in both controls, and its top ten rows carry 41% against 44-62%. The two readings B2 left
standing are both excluded in this form (control-backed); the flatness is what row-level homophony would produce
(the commonest words spread over two or more rows -- the adjacent rich rows 17 and 18, 47 and 48, 11 and 12 are the
candidates), or a plaintext whose function words are largely NOT coded (carried by the shorthand or omitted), or a
non-English-like token stream. Named next step (not run here): a homophone test -- do rows 17 and 18 (or 47/48)
ever stand adjacent, and do their neighbour profiles match -- needs an instrument with a passing control, which B2b
showed neighbour classes are not at this N. Requests: none; 0 subagents; about 3 minutes by the clock each.

## Step B23 (28 Sept 2026, 04:36-04:45 UTC) -- roll 12 (Livingston, Oct 1801-Nov 1804) screened whole: every numeral passage is Livingston's THE=968 usage; nothing in the target's code

Whole-reel PDF `M34-012.pdf` (92.1 MB, 455 pages, one request), 16 contact sheets at 26 dpi read by this session
(`scratch/b23/r12_*.jpg`), four numeral pages checked at 110 dpi. Positive control met: the 1803 despatches ARM3-LIVCODE
screened stand out as numeral pages. Numeral pages on the reel: 49, 62, 75, 88, 118, 144 (1803-04 Livingston to
Madison with the period interlinear pencil decodes: "but your Minister must be ... 1157. 477. 764. 317. 1059 ...",
"968. 654. 689. 1087. 1667. 1583 ..."), 321-322, 349-350 ("1043. 1433. 470 ... 968. 1318. 1556. 1456 ... Rob R
Livingston / The Honble James Madison"), 368, 391, 394-395 (a five-page numeral despatch, "In consideration of this
937. 599. 924. 601. 849 ... 968 ..."), 405-407. Every one carries the THE=968 signature values (968, 849, 1221, 1667,
1583, 1456, 1011) and flat units; none shows the target's 0/1-heavy units, its 2-digit block or shorthand runs.
**Result: search result with its control -- DUSMF rolls 12, 13 and 14 (Oct 1801-Sept 1810) are now screened frame
by frame; the 20 Feb 1808 letter is the only item in its code in the whole Paris legation series.** Requests:
catalog.archives.gov 1; 0 subagents.

## Step B25 (28 Sept 2026, 04:39-04:47 UTC) -- the richest rows do not collocate the way English function words do: control-backed

`b25/homophone_bigram.py`: adjacency count of two rows in either order against a position-permutation null. Gate
(pre-registered): positive control -- en18 letters (369 coded tokens) with "the" on row 17 and "of" on row 18 --
adjacency mean 24.1, 59 of 60 above their own p95; negative control -- "the" split at random between rows 17 and 18
(homophones) -- mean 1.6, 0 of 60 above p95. **GATE MET.** Target:

| rows | adjacent | null p95 | percentile |
|---|---|---|---|
| 17 / 18 (the two richest) | 2 | 5 | 28 |
| 47 / 48 | 1 | 2 | 51 |
| 11 / 12 | 0 | 1 | 0 |
| 17 / 38 | 0 | 5 | 0 |
| 18 / 38 | 4 | 4 | 94 |
| the five richest rows as a set (17, 18, 38, 14, 16) | 17 | p05 11, p95 22 | 51 |

Addendum control: the five commonest function words (the, of, to, and, in) on those five rows give 52.9 adjacencies
(53 of 60 above p95) against the target's 17 (inside its own null, 51st percentile).

**Result.** The target's richest rows behave like the homophone control or like non-collocating words, never like
the/of/to/and/in: the two richest rows are adjacent twice in 369 tokens where "the"/"of" would give about 24, and the
five richest rows together sit exactly at chance where five function words give three times chance. Two readings
survive, both control-backed: (a) the rich rows are homophones or grammatical variants of a few words (the split-"the"
control reproduces the numbers), or (b) the numerals do not carry the letter's function words in the ordinary way --
the commonest coded rows are content words or the function words are elsewhere (the shorthand runs, or omitted, as a
telegraphic register would). What is excluded: any assignment of the five richest rows to five distinct common
English function words (a family-C solver that seeds "the"/"of"/"to" onto the top particles -- ARM-C1's particle
class -- is working against this structure). Requests: none; 0 subagents; about 8 minutes by the clock.
