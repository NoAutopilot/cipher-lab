# Validation decision recorded before fresh-control results

2026-09-27. The three tuning controls recover 240/257, 221/257 and
239/257 exact token pieces with bonus 0 and 1,000 restarts of 120,000
iterations, half initialized from the earlier candidate pool. The scoring
function prefers each recovered approximation to the actual plaintext;
therefore even success is a **partial-recovery** capability check, not an
exact-key guarantee.

Fresh controls are seeds 4 and 5, excluded from tuning. Both must recover
at least 80% of their exact token pieces before this configuration is used
on the target. This bar licenses an exploratory search for substantial
readable fragments only. It does not license excluding digraph ciphers,
historical shorthand, or the provisional glyph transcription on failure.

If both pass, run the same two-stage budget and bonus on target and three
position-shuffled targets, with fixed fragment boundaries and symbol
counts. Do not claim significance from three shuffles. A possible reading
must also fit repeated glyphs, the manuscript, and numeric contexts; a good
language-model score alone is not a decipherment. No target run at this
configuration has been made as of this decision.
