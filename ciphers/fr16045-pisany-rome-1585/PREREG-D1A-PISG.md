# PREREG D1A-PISG -- f.275v period gloss as a second witness (8 Oct 2026, pushed before any gloss read or score)

Material. fr.16045 f.275v (Gallica btv1b9060906j c563). Gloss = the second-hand period decipherment at the head of the page (4 lines
above block A), its left-margin continuation beside block A, and the long left-margin text beside block B. Interlinear letters inside
block B L17-L20 were read by R8-PIS (gl275) and are not re-scored here.
Copy = kp86i/colbert_f275v.txt (Colbert 16 pt II pp.122-123, "ne le me communiquer" .. "tant plus volontiers").

Reader. One blind Sonnet subagent call over the gloss line crops only (no copy, no key, no decode, no hint of content beyond "16th-century
French secretary hand"). Its reply is kept verbatim (pisg/reader_A.txt). The SCORED text is that blind read, unedited. The worker's own
reconciliation (pisg/gloss_reconciled.txt) is made with the copy already seen, so it is reported only descriptively, never gated.

Normalisation (both sides, pisg/pisg.py `norm`): lowercase; strip accents; j->i, y->i, v->u; expand V.M./V. Mate/V.Mte/VM -> vostremajeste,
S.S./S. Ste -> sasaintete, S. -> sieur when followed by de, & -> et; drop every non-letter. Unreadable marks the reader writes as [?] or ?
are dropped.

Statistic. Per gloss segment (head, marginA, marginB), semi-global alignment of the segment's letters against the copy's letters (gloss
end-to-end, free end gaps on the copy; match +1, mismatch -1, gap -1). identity = matched letters / gloss letters, pooled over segments.

Controls (both can differ from the target on this statistic, since both destroy the letter correspondence the alignment measures):
 N1 span null: the same gloss segments aligned against 200 random windows, each the copy's normalised length, drawn from the other
    Colbert clear text on disk (kp86/kp86b/kp86g/kp87a/kp87b colbert_*.txt, other letters; windows wrap), seed 0.
 N2 order null: each gloss segment's letters shuffled within the segment, 200 draws, against the true copy, seed 1.
Gates.
 G1 (witness): pooled identity > p99 of N1 AND > p99 of N2. PASS -> the blind gloss read is an independent witness of the Colbert text
    at this page.
 G2 (agreement, PX-BRODEC 80% precedent): pooled identity >= 0.80 after normalisation. Reported beside G1.
Outcome. No key86 change in this job in any outcome (a running-text gloss carries no sign-level value except where it is interlinear).
If the blind read yields fewer than 150 normalised letters the test is a non-test (too short), reported as such.
T40: report any T40 token the gloss sits directly over (interlinear), else "gloss not sign-level for T40".
