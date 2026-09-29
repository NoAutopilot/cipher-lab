# H57 pre-registration (29 Sept 2026, DEBOSNYS-RUNNER-3b; pushed before any crop is read)

Row: CAMPAIGN.md H57 -- tilde re-labelling on the verse (cryptogram 4, 20 lines, settled c34 draft).
Targets: every c4 box whose settled id contains TILDE or CURL, and every c4 box aligned (h26_alignment.tsv) to a
Bourdeau code beginning N_ or containing TILDE (union, de-duplicated). Decoys (the control that can differ): 15 c4
boxes drawn at random (seed 57) from boxes whose id and aligned code carry neither, excluding marks and `_`; mixed in.
Crops: swarm/R2/R2-2/t_low.py crop_real (target in a red box, two neighbours each side, 4x), renamed q01.. in shuffled
order; the key (which crop is which box, target or decoy) stays outside the reader's file list.
Reader: value-blind, claude-opus-5-5 (the row said Fable; Fable is rejected on account 3 until 3 Oct 08:00 UTC, so the
brief's rule "else Opus 5.5" applies -- substitution recorded), split into up to 4 calls of about 15 crops (per-call
scoping, CLAUDE.md Usage 6) instead of the row's single call. The only question: "Is there a tilde-like wavy mark drawn
above the base of the sign inside the red box? Answer yes, no or unsure." No ids, no inventory, no counts shown.
Gate (control first): the decoys' "yes" rate must be <= 20 pct; above that the reader cannot tell a tilde from no tilde
at these pixels and the row stops as a non-test.
Result, if the gate holds: per verse line, the number of "yes" boxes (unsure counted separately, reported both ways);
mean per line with a bootstrap 95 pct interval over lines, against Sektu's 1.5 per line and against the nasal-syllable
rate per alexandrine in tools/data/fr19v (orthographic nasal vowels an/am/en/em/in/im/on/om/un/um/ain/ein/oin/aim/eim
before a consonant or word end, counted by script) times the verse's measured signs-per-syllable ratio (H30: about 1
non-X sign per syllable). A per-line tilde count inside the nasal interval supports tilde = nasal; well below it does
not. Descriptive, grade S, never a reading.
