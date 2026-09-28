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
