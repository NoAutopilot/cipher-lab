# PREREG HAR-39V (15 Oct 2026, written 11:2x UTC by date -u, before any image fetch or score)

Target: BL Harley MS 287 f.39v (DECODE R8479 image 4), line G word 3, transcribed by Bourdeau
(cyphersolver targets/needham1587/cipher.txt, MIT / CC BY 4.0) as `U ? ? ? ? O C` = b????ed, grade M.
Key: Bourdeau's closed three-grid pigpen (decode.py): shapes J U L / C O F / N 7 D; plain a-i, dot below k-s,
dot inside t-z (u=v). No homophones, nulls or codes met on f.39v.

Procedure (same for control and target): one full-size R8479 f.39v image fetched in one DECODE browser login
(images in scratchpad only). Locate line G, cut a word crop per word with tools/iiif_lines.py --image or a
PIL crop at native resolution, enlarge x2-x3. Read each sign as shape + mark (none / dot below / dot inside)
by eye (this session), BLIND to Bourdeau's transcription for the control words (their string is not
consulted until each control read is written down).

Control: 3 already-read words of line G, chosen before reading: G word 1 (`L 7 J C. O U.` channel),
G word 5 (`7 O. O: O D.` hoyes), G word 8 (`F J D. J: O C. O C` fastened). Gate C: all three read
sign-for-sign equal to Bourdeau's string (shape and mark), i.e. 20/20 signs; at most 1 sign miss total
is tolerated as a PASS-with-caveat (19/20); 2 or more misses = CONTROL FAIL, the target read is then
logged as a non-test and grade stays M.

Target read: the four middle signs of word 3 read the same way. Candidate list fixed now (7 letters,
b + 4 + ed): blocked, bridged, bounded, belayed, beseted(no), barred(6, does not fit), banked(6),
blinded, braided, bricked, buoyed(6), boarded. Outcome classes:
- T1: all four signs read with marks, decode to an English verb in the candidate list or any English
  word fitting b????ed and the sense -> grade S for those signs if Gate C PASS (else M).
- T2: 3 of 4 signs read, one blotted; the read signs admit exactly one candidate from the list -> S for
  the read signs, the word M+ (reported as "b[x]..ed, consistent only with W"), not upgraded to S.
- T3: 2 or fewer signs read, or the read signs admit 0 or 2+ candidates -> word stays M; report the sign
  reading as M.
No key edit; Bourdeau's key is not changed by this job. Report found / not found; no novelty class.
Also noted (not scored): look at R8478/R8480 record pages only if budget allows (brief: optional).
