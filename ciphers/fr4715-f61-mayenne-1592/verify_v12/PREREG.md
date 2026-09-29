# VERIFY-F61-V12 pre-registration (29 Sept 2026, written before any reader call)

Verifier VERIFY-F61-V12 (account 3, Opus; separate from runner 15 and from V5-V11). Claims under audit: runner 15's f.61 transcription
corrections H407-H415 (NOTES.md, HYPOTHESES.md, `scripts/f61_positions_corrections.tsv`). No reading claim, no novelty class, no key file,
corrections file or CAMPAIGN.md edited.

## Materials (mine, not the runner's)
- Sign centres placed by me on the native region `images/src_ark_12148_btv1b52509819x_f137_500_1880_3320_1420.jpg` from gridded strips
  (`strip.py`), in `v12_positions.tsv`. Disclosed looks: the whole-region overview (I saw the leaf, including that a phi-like sign stands
  after L03's bracket before "a les entendre", and that L07/4 looks 43-like at overview scale); one contact sheet of W1 tiles labelled with
  codes, for centring only (14 centres moved 20-40 px); the five count crops, for box placement only. The runner's tiles, prompts,
  position files for these signs and replies were not opened.
- Tiles `cut.py` (W1 tight, W2 wide, W3 shifted), sheets `sheets.py` (random ids, seed 20260941), count crops `counts.py`.
- References R1-R15 are all in-span f.61 tokens: R1 BETA L11/1, R2 C43 L03/8, R3 ZHOOK L11/11, R4 4TRI L08/11, R5 C6 L08/3, R6 PHI L08/1,
  R7 EBR L11/3, R8 SBS L08/5, R9 LOOPBAR L03/12, R10 VBAR_A L11/6, R11 CA L08/10, R12 INF L08/4, R13 VBAR_B L03/5, R14 CROSS L07/10,
  R15 4PI L11/9. Options besides R1-R15: N = none of these, P = punctuation / not a cipher sign.
- Answer key sha256 11077ef1f67c82f0f4ab756cb1df995bc8381e16c795acc8e458cf8969aed17d, held outside the repository until the replies are in.

## Calls (Opus subagents, blind: sheets only, told not to open any other file)
C1 Part A (39 items): T1 L07/4, T2 L03/16, T3 L05/1, T4 L02/2 and L04/2, each at W1/W2/W3; 18 known anchors (in-span f.61 tokens other
than the references, plus one punctuation dot, L05 before "Et"); 4 repeats (anchors at W3); the BETA control L11/1 at W2 and W3.
C1 Part B (3 items; R1 BETA NOT allowed): L07/4 W2, L11/1 W3, L05/9 W3 (anchor, expected R2).
C2 (38 items): the 27 out-of-span codes (L01/1-2, L01/7-12, L03/1-3, L05/1-2, L11/8, L10/1-13) at W1; 8 anchors at W3; L05/1 at W2; 3 repeats.
C3 (5 count crops): list every mark after the red box up to the first word in ordinary handwriting, each cipher sign or punctuation.

## Gates (fixed now)
- C1: anchors >= 16/18 AND repeats consistent with their own anchor answer >= 3/4 AND BETA control L11/1 -> R1 at 2/2 in Part A;
  else CONTROL FAIL, nothing in C1 scored.
- C2: anchors >= 7/8 and repeats consistent >= 2/3; else nothing in C2 scored.
- C3: controls X1 = 3 and X2 = 3 cipher signs, exact, both; else nothing in C3 scored.

## Decision rules (fixed now)
1. L07/4. Endorse "C43, not BETA" if T1 -> R2 at >= 2 of 3 windows AND Part B L07/4 -> R2 AND Part B L11/1 is not R2 (the steering /
   lumping control: L11/1 is Tomokiyo's 'm' in S5, so a BETA -> C43 move there would NOT serve the published letter; a reader that lumps
   beta into 43 would fail here). Reject if T1 -> R1 at >= 2 of 3. Otherwise in part / unsettled.
2. L03/16. Endorse the insertion if C3 X3 = 3 and X4 = 8 cipher signs (pass A: 2 and 7), and T2 -> R6 PHI at >= 2 of 3 windows endorses
   the class; T2 -> P at >= 2 of 3 rejects. Count endorsed but class not R6 -> in part (a sign, class open).
3. Out-of-span QA. Per token, confirmed = C2 answer equals the expected reference (classes with no in-span token -- ELOOP, HASH4, CH,
   4STEM, LOOPSTEM1 -- expected N). Endorse "26 of 27 confirmed, L05/1 unsettled" if >= 25 of the 26 non-L05/1 tokens confirm. L05/1 from
   its 4 reads (C1 x3, C2 x1): >= 3 R9 -> LOOPBAR null; >= 3 N -> LOOPSTEM1 stands; otherwise unsettled.
4. Claim 4. L04/2 punctuation endorsed if T4(L04/2) -> P at >= 2 of 3 AND C3 X5 lists 0 cipher signs. L02/2 "matches none of the
   references" endorsed if -> N at >= 2 of 3; if one reference at >= 2 of 3, rejected (class found). Denominator: the meter counts cipher
   signs, so a removed punctuation mark leaves it; with the L03/16 insertion the count is 99 - 1 + 1 = 99 unless my verdicts differ.
5. Span count and meter: my own script `meter_v12.py` recomputes the five-span match under key v8's f.61 reading key and the meter bands
   (meter_v8's band rule) for (a) uncorrected, (b) the runner's corrections, (c) the corrections I endorse.
6. Steering question answered from rule 1's control, from C2's no-change rate (a reader that only moved codes toward Tomokiyo would have
   no reason to confirm out-of-span codes), and from whether any correction the runner did NOT propose shows up in my reads.

## Addendum C4 (written after C1-C3 replies were in, before any was scored against the key; C4 key sha256 f19b06f97868aff274b7920b64437d99796ba935101d0d1cd19a732e07f7b5cd)
Placement look: pass A's L02 begins at PHI, but the line opens with an 'll'-shaped mark before the PHI, and the cipher run of L01 continues onto
L02. Out of every Tomokiyo span, so no published letter bears on it: a test of whether the transcription carries slips the runner had no reason to
look for (decision rule 6). C4: the R panel plus R16 = LL (L05/16, in-span) and option O = ordinary handwriting letters (not a cipher sign).
Items: L02 opening mark at W1/W2/W3; anchors L05/16 W3 (R16), L03 'les' and 'en(tendre)' (O, O), L05/7 W2 (R11), L08/5 W3 (R8).
Gate: anchors >= 4/5. Rule: >= 2 of 3 R16 -> pass A missed an LL at L02 start (a slip the runner did not propose; logged, not merged by me);
>= 2 of 3 O -> plain letters, pass A stands; else unsettled.
