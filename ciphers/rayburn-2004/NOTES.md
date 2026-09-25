open

Intake (25 Sept 2026, LANE B3 worker bRAY, minimal check-solved per breadth.md's intake step):
Cipherbrain post "The Top 50 unsolved encrypted messages: 43. The Rayburn murder cryptogram"
(6 March 2017) and its full 7-comment thread read in full from
`sources/schmeh/posts/43-rayburn.txt` (already on disk); the post's own text states "So far,
nobody has come up with a plausible solution" and none of the 7 comments (Hendrik, Serapio,
Thomas, Nick Pelling, Aaron Turner, and two from Juha in 2019) claims a solution -- Juha's two
comments offer an unworked "overlined letters are notes" idea, not a reading. The post also
covers Bruce Schneier's original 2006 post (schneier.com/blog/archives/2006/01/handwritten_rea.html)
and its own long comment thread, which Schmeh says produced no plausible solution either. Both
solver repositories grepped (shallow clone, `grep -ril rayburn`, deleted after): dbourdeau's
`top50/NOTES.md` and `TARGETS.md` (row 43) both read "plausibly a handwritten password list, not
a cipher", citing "the recurring and plausible reading across both the Schneier and Cipherbrain
threads" -- no claimed decipherment of any standing; no match anywhere in
aaymeloglu/unsolved-ciphers. One OpenAlex query (`search=Rayburn cryptogram solved`) returned 1
result, unrelated (a survival-research essay-competition reflection paper). One Semantic Scholar
query (`query=Rayburn cryptogram decrypted`) returned 23 results, none naming Rayburn or this
cryptogram (cryptanalysis papers on unrelated ciphers). No solve found by any of the six checks.

Cheap test 1 (25 Sept 2026, LANE B3 worker bRAY): image fetched (1 request, scienceblogs.de,
browser UA, HTTP 200; free for the next holder) to `images/Rayburn-Cryptogram.jpg` and
transcribed blind, one pass, no subagent, recording each symbol's identity, position and its
underline/strikethrough/overline state separately -- see `ciphertext.txt` and `ciphertext.tsv`.
N = 74 tokens (58 in the main grid inside/below the drawn enclosure, 8 in a left-margin column,
8 in a right-margin column; a small circled mark at the bottom was excluded as a likely page
mark, not a cipher symbol -- see ciphertext.txt's caveat). K = 59 distinct type ids (case
preserved; symbols that look like two letters combined are kept as their own type). IC:

  target IC = 0.0056
  English control (same N=74, 200 samples, tools/data en corpus, 26-letter alphabet):
    mean 0.0618 [0.0311, 0.0911]
  uniform-random control (same N=74, K=59, 200 draws): mean 0.0171 [0.0115, 0.0255]
    (expected ~1/K = 0.0169)

Target IC is below both controls' ranges, and below the uniform-random floor -- consistent
with Schmeh's own observation ("most characters appear only once") and with either a
high-homophone substitution or non-linguistic content (Schmeh's diagram-of-objects
hypothesis; the source's own alternative reading is a password/directory list). This is not a
control-backed negative in the rule-3 sense (no substitution family was fit or judged here,
only a raw IC comparison as the spec's cheap test 1 asks for); it does rule out plain
monoalphabetic substitution on frequency grounds alone, matching Schmeh's "frequency analysis
is obviously useless" caveat. Test 2 (diagram-layout hypothesis) and test 3 (matched
homophonic/keyboard-substitution judge) are out of this brief's scope -- next test per the
spec's `cheap_tests_in_order`.

Transcription caveats: several symbols are genuinely ambiguous by eye at this resolution
(flagged with `?` in ciphertext.tsv/.txt); the mark state on most of the left- and
right-margin column is unclear because a continuous ruled line runs down each margin. K=59 is
this pass's best count, not a settled number -- a second blind pass would be the way to
tighten it (not run here, out of a $1-2 single-pass test's scope).

