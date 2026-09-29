# VERIFY-F61-V13 pre-registration (29 Sept 2026, written before any reader call)

Verifier VERIFY-F61-V13 (account 3, Opus; separate from campaign runner 16 and from VERIFY-F61-V5..V12). Task: the one more read V12 held
for three f.61 signs (L11/8 4STEM-or-CROSS; L01/11 4PI-or-4-over-hash; the mark opening L02, a probable missed LL). Runner 16's reads
(H428, H428b, H431) and its meter H432 are the claims under audit; its tiles, prompts, item files and replies were NOT opened (I read only
the HYPOTHESES.md rows to learn what was claimed, and that the 4-over-hash exemplar it used sits on f.108v L03). No reading claim, no
novelty class, no key file, corrections file or CAMPAIGN.md edited.

## Materials (mine)
- Centres placed by me on gridded crops: `v13_positions.tsv` (f.61 native region; f.108r stitch; f.108v L03 desk-pack sheet, label strips
  excluded). Disclosed looks: the f.61 overview, gridded crops of each placed sign, one labelled W1 contact sheet (centring only; four
  centres moved 5-20 px, and the f.108r window scale reduced from 0.85 to 0.6 so its signs fill the tile like f.61's).
- Tiles `cut.py` (W1 tight, W2 wide, W3 shifted; grey + autocontrast so the source leaf is not given away by colour). Sheets `sheets.py`
  (seed 20261329). Answer key held outside the repository until the replies are in: sha256
  99e9abf7cb852be9913a25ca993b99ae5c69b201481781a639425b9d692e6ae0.
- Panel A (12 references, W1): 4STEM (f.108r, pass108A's L02/2), CROSS (f.61 L07/10), 4PI (f.61 L11/9), looped hash (f.108r pass108C
  L05/19, HASH4), 4-over-hash (f.108v L03/6, HASH4), LL (f.61 L05/16), PHI, C43, ZHOOK, 4TRI, BETA, VBAR_A (f.61 in-span tokens).
  Options besides the letters: N = none of these; O = ordinary handwriting letters, not a cipher sign.
- Panel B: panel A minus CROSS, LL and the 4-over-hash (the three classes runner 16 chose).

## Call (one blind Opus subagent; sheets only, told to open no other file)
Part A (28 items): the three targets at W1/W2/W3 (9); a repeat of each target's W1 tile (3); in-span controls L07/10 W2 (CROSS), L11/9 W2
(4PI), L05/16 W3 (LL) (3); 13 anchors: second 4STEM f.108r (pass108A L02/7) W1 and W3; looped hash f.108r (pass108C L05/9) W1; 4-over-hash
f.108v L03/33 W1 and W3; CROSS f.61 L01/1 W1; 4PI f.61 L01/12 W1; plain 'Il' f.61 L02 (the clear 'Il seroit') W1 -> O; plain 'les' f.61
L03 W1 -> O; C43 L05/9, PHI L03/4, ZHOOK L07/11, 4TRI L03/10 at W2.
Part B (8 items, panel B): L07/10 W3 and L05/16 W2 (in-span; their classes are off the panel), f.108v L03/33 W2 (4-over-hash off the
panel), anchors 4STEM L02/7 W2 and 4PI L01/12 W2, and the three targets at W2 (observational).

## Gates (fixed now)
- G1 anchors: >= 12 of 13 Part A anchors correct (either hash form counts as HASH4 for the hash anchors only if it is the SAME form).
- G2 in-span controls in A: L07/10 -> CROSS, L11/9 -> 4PI, L05/16 -> LL, all three.
- G3 repeats: >= 2 of 3 target repeats equal their own W1 answer.
- G4 anti-steering (Part B; the brief's control): L07/10 (Tomokiyo's letter is served by CROSS as it stands) must NOT move to 4STEM, and
  L05/16 (served by LL as it stands) must NOT move to O or a panel sign: both N. Part B anchors 2/2.
Any gate failing: CONTROL FAIL, no target scored, the three stay held.

## Decision rules (fixed now; majority over the three Part A windows)
1. L11/8: CROSS at >= 2/3 -> endorse runner 16 (relabel CROSS, null). 4STEM at >= 2/3 -> reject (4STEM stands). Otherwise hold.
2. L01/11: 4-over-hash at >= 2/3 -> endorse runner 16 (HASH4 as coded; no change). 4PI at >= 2/3 -> reject runner 16 (two instruments
   then split 1-1 against a 3-window read each: logged as a conflict, rule 4, held at M). Looped hash or N or mixed -> hold (HASH4 stands
   as coded, no change either way).
3. L02 opening: LL at >= 2/3 AND the plain 'Il' anchor -> O -> endorse the insertion (LL, null). If the plain 'Il' anchor itself -> LL, the
   reader cannot separate this hand's plain 'Il' from the LL sign by shape: hold, whatever the target reads. O at >= 2/3 -> reject.
4. Meter: `meter_v13.py` reuses verify_v12/meter_v12.py's meter and span scorer (meter_v8 bands, key v8) for V12's endorsed state (c) plus
   whichever of the three I endorse; denominator 99, or 100 if the L02 insertion is endorsed.
