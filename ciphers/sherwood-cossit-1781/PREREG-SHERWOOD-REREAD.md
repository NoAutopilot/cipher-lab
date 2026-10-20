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
