# PREREG SHERWOOD-REREAD (20 Oct 2026, 01:2x UTC by date -u; worker session_01Kw99VShSN1ECFM4s3LRfiY, account 4)

Written and pushed before any blind read.

**Hypothesis.** A share of the 33 M rows whose two Entick candidates both have margin 0.00 under the bigram and trigram
choosers (mrows/mrows.tsv; list in tx2/targets.tsv) are misread cypher digits in ciphertext.tsv, not encoder slips or rare words.

**Material.** The 22 line crops (images/crops/, tools/iiif_lines.py, 18 Oct 2026) holding those rows: p345_L01 L02 L03 L05 L09 L10;
p346_L01 L03 L04 L05 L06 L07 L08 L09 L10 L14 L15 L17 L18 L22 L27; p347_L05 (= ciphertext line p347_L05b). No full page sent.

**Readers.** Two independent blind passes (A, B), one Opus subagent call per page per pass (6 calls). Each sees only that page's
crops and transcribes every cypher group on each line, '?' for an unreadable digit. No transcription, decode, Entick word or sketch.

**Known-answer set.** The 50 groups on the same 22 lines that read grade S in reading.tsv with bigram margin >= 4 in mrows/gate1.tsv
(tx2/known_answer.tsv).

**Statistic.** Reader error per pass = share of known-answer groups where the pass's digit string differs from ciphertext.tsv
(trailing '?' stripped; a missing group counts as different). Change rate = share of groups where A and B agree with each other
and both differ from ciphertext.tsv, computed separately on the known-answer set and on the 33 targets.

**Gate.** If either pass's reader error exceeds 10% (more than 5 of 50), stop: log "untested-by-this-tool (blind Opus line reads)"
and change nothing.

**Acceptance.** A target change is accepted only where A = B != ciphertext.tsv and one reconciliation call (crop plus the two digit
strings, no words) confirms. The 33-group change rate must be clearly above the known-answer change rate (pre-set: at least 3x it
and at least 3 groups) or the changes are reported as reader noise and not applied.

**Re-decode.** decode_entick.py unchanged; a corrected group whose new cell is a headword and wins its column by >= 2 nats is S,
otherwise M. Sketch agreement reported afterwards only.

## Decision
- Gate fails -> no change; NOTES.md logs the tool as untested at this resolution; the next step names a different instrument.
- Gate passes, change rate not above control -> no change; digit misreading is not supported by this re-read.
- Gate passes, change rate clearly above control -> apply confirmed changes, re-decode, report M -> S moves and the new H/C/S share.
Belief: (the hypothesis as pushed in 250794a73; this line written after the read) a share of the 33 both-unseen M rows are digit misreads.
Would change it: the gate and acceptance rule above.
Observed: (20 Oct 2026, appended after the read) known-answer reader error A 4/50 = 8.0%, B 5/50 = 10.0% (gate: not above 10%, PASS at the
boundary); 2 of each pass's misses are line ends both passes read short (crop edge: p346_L01 final 35, p346_L15 final 15), and 2 are
agreed reads on S rows (412-33 as 412-35, 225-17 as 225-19), so the known-answer A=B change rate is 2/50 = 4.0%. Targets: A=B != tx on
4/33 = 12.1% (3.0x control, >= 3 groups: meets the pre-set bar exactly). Reconciliation confirmed 3 (366-33 -> 360-33, 166-13 -> 165-13,
33-35 -> 53-35), rejected 1 (131-22 kept). Scoring repairs made after the passes came back, before any target was scored: p347 id
p347_L05 -> p347_L05b; ciphertext g: tokens and trailing '?' parsed; for the two-line crop p346_L15 each reader's own other-line
reading (from its report) joined in. Re-decode: all 3 new cells are OCR-only (Tan, "interj", Chalkcutter), grade M; 0 rows M -> S;
H 8 C 4 S 145 M 57 I 2 = 72.7% unchanged; judge FAIL as on file.
Decision: stop -- apply the 3 confirmed corrections to ciphertext.tsv (transcription corrections from the image, logged in tx2/changes.tsv and
NOTES.md); no grade moves. The digit-misread hypothesis is supported for at most 3 of 33 rows and does not move depth.
Lesson: a known-answer set built from S rows still carries the transcription's own errors (2 agreed misses here): read a both-pass
agreement on a known answer as a lead on the known answer, not only as reader error; and check whether the corrected cell has an image
read before expecting an S, since an OCR-only cell is M by rule whatever the digits.
