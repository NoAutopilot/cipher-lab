# PREREG-D3BLA -- residue re-grade of the 42 non-C tokens (BLA 184 p1, 186 p1/p3, 191(a) p5)

Written by D3-BLA (account 4, LANE DEPTH, session_01WazRD8pNQhMA2tenLBpki3), 8 Oct 2026, before any crop was read and before
any score was computed (time read with date -u at writing; pushed before scoring). Brief: .claude/briefs/runs/2026-10-08-acct4-depth-wave1.md "## D3-BLA".

## Universe
The 42 tokens of reading_tokens.tsv graded other than C at origin/main beefb778f: M 22, S 3, U 17 (172 tokens, C 130).

## Instruments, in order
- **I1 image (signs).** Crops of BLA191 p5 lines L01, L05, L06, L07, L11, L12 and BLA186 p1 L01 cut from the 1200 px disk copies
  (images/, no fetch) with tools/iiif_lines.py --image (command pasted in NOTES.md). One blind Sonnet subagent pass on the crops
  only (no key, no prior reading, no glosses), then one reconciliation by this worker on the same crops. A sign marked M in
  ciphertext.tsv becomes H only if the blind pass, pass A and pass B give the same digits AND the reconciler sees no competing
  reading of any digit on the crop (R17's ')'/'>' = 7 rule for this hand applies). Otherwise unchanged. Changes go only into
  settle_image.tsv, then `python3 settle.py && python3 build_key.py && python3 ../../tools/decode_key.py . --check`.
- **I2 key.** A token is C only if its sign is H and key.tsv gives its code one value (decode_key.py's existing rule; a period
  gloss is the only source of a key value). Tie rule: a key tie 'a|b' counts as one value only if the two glosses are the same
  word in two spellings: after lowercasing, removing accents and apostrophes and collapsing doubled letters, one form equals or
  is a prefix (>= 5 letters) of the other; the token is then C with the longer form, written to exceptions.tsv with the reason.
  Any other tie stays M (rule 4: not settled by majority or by context).
- **I3 siblings.** For each U code, every ciphertext.tsv column carrying that code (as read or as an alternative) is checked
  for a gloss. A gloss on an H column of a sibling would already be in key.tsv; a gloss on an M column, or on an alternative
  reading only, gives the value at grade M, never C.
- **I4 BLA190 p7 (the anomaly: a self-contained cipher+decipherment page dated 3 Nov 1729, later than the item's 4 Aug 1729).**
  One-system test: the share of p7's glossed H columns whose gloss equals the value the rest of the run (p7 left out) gives the
  same group, over groups keyed elsewhere. Share >= 0.65 (below the lowest accepted item, BLA194 0.694): same system, its
  glosses stay in the key. Share < 0.65: p7 is dropped from the key, the key is rebuilt, and every one of the 42 re-graded.
  The test says nothing about which letter the leaf belongs to (that is a catalogue question).
- **Context-only values are never C.** No new context fill in this job; R10-HUNT2's four fills keep their S/M grades unless a
  period gloss now gives the value.

## Shuffled-code control (computed after I1-I4 are fixed, same rule)
- (a) **Random-code control** (the gate): each of the 42 positions gets a code drawn uniformly from the distinct codes attested
  in ciphertext.tsv, keeping that position's post-I1 sign grade; rule I2+I3 applied; 1000 seeds (numpy default_rng, seeds
  0-999). Statistic: number of the 42 positions that come out C. Pass: target count of C among the 42 > the control's 95th percentile.
- (b) **Within-42 permutation** (reported only): the 42 codes permuted among the 42 positions. Declared in advance as nearly
  non-discriminating by construction: per-code key lookup over a fixed code multiset can differ from the target only through
  the position's sign grade (CLAUDE.md rule 3, the bCAS/AX-5799 lesson), so it licenses nothing either way.
- If the target fails (a), no promotion is written to the reading and the result is logged "non-discriminating at N=42".

## Depth bar (copied from .claude/briefs/runs/2026-10-08-acct3-depth-bar.md, applies to any depth remark; this job rules no depth)
> Source: acct3-next-jobs-scout critic (wf_e0950d6a-d50) found four depth rulings would otherwise disagree on whether an external check or an H/C code grade admits D2. This applies CLAUDE.md rule 4a literally; research/DECIPHERMENT-STANDARDS-2026-10-04.md section 3's alternatives are NOT adopted. Changing this is an owner decision (ASKS row).
> 
> - CLAUDE.md 4a governs where it differs from the research note.
> - Cipher clause: a contiguous H/C/S stretch longer than the authentication distance (AD) for the design, about 1.5 x unicity.
>   - H(K) = the design's key space plus every liberty the reading took: U wildcards, M tokens, r|re|ro and o|ou|ous choices, repairs.
>   - An unfitted external or period key does NOT shrink H(K) to the liberties alone.
>   - The zero-liberty (H_lib+20)/R reading (about 6-8 letters here) is not used.
> - External check: an external check (key agreement with period glosses, a period key sheet) is a D3/D4 element under CLAUDE.md 4a. It does NOT replace the clause at D2, although research section 3 offers it as an alternative.
> - Code clause: a code value that reads sensibly in >= 2 independent contexts.
>   - An H or C grade on the value does not satisfy this on its own, although research section 3 says 'or carry H/C grade'.
>   - A verbatim repeated phrase counts once (lodewijk precedent).
> - D2 = one clause plus your own true, specific sentence about the content, written from the reading. Droysen or Fagel 5177 may confirm the sentence, never supply it. Otherwise hold D1.
> - If you think the convention is wrong, post one ROOM flag for the parent and still rule under this bar.
> 
