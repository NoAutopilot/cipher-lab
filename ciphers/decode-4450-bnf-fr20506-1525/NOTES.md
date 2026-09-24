# decode-4450-bnf-fr20506-1525

Status: open

## What this is

DECODE R4450: unsigned letter, BnF Français 20506, f.136, 1525-1550, French envoy/despatch series
(Non-decrypted, 5 images, no attached document found on the record page). QUEUE.md row DC1 ("DECODE
non-decrypted records with images", LANE N diff of 24 Sept 2026) flagged it as a "recovery, finish-existing-key"
lead because 18 other DECODE records in the same volume (BnF fr.20506, ids 4434-4449 + 4815-4816) are already
Decrypted. Checked as part of LANE N check-solved batch DC1 (`.claude/briefs/runs/2026-09-24-lane-n-csDC1.md`).

## Check-solved sweep, 24 September 2026

1. **Tomokiyo.** `sources/cryptiana/web/venetian.htm` identifies this exact folio directly: "Several
   undeciphered letters of Hieronimo Ranzo use similar ciphers with superscript figures (BnF fr.2988 ... f.2,
   f.9-10; BnF fr.3019 ... f.73-74; BnF fr.20506, f.136 (a copy of BnF fr.2988, f.9, which Norbert Biermann
   pointed out to me))." This places f.136 as a copy of a specific, still-undeciphered Ranzo letter (fr.2988
   f.9) — Tomokiyo does not say the volume's 18 Decrypted siblings share Ranzo's system, and QUEUE.md's own
   "finish-existing-key" framing did not check this before scoring.
2. **Bourdeau.** dbourdeau/cyphersolver's `CATALOGUE.md` entry 1.6 (a scored row, not the solved list) is this
   exact item: "DECODE R4450 = BnF fr. 20506 f. 136, a copy of fr. 2988 f. 9 (the R1894 letter). No key,
   decipherment or transcription on the DECODE record (checked 21 Sept 2026). The fr. 2988 Ranzo letters were
   transcribed here in vasto1527/ (n20/ranzo_c0*.txt, ~2,600 groups) with the Garbino letter (fr. 3022 no. 20),
   which uses the same initial-letter + number code. The numbering is not alphabetical, and a word annealer
   recovers only function words. No clear copy, crib or base key was found. Needs Ranzo's table or a clear
   copy; see entry 7." Bourdeau has therefore already attempted the Ranzo cipher system this letter belongs to
   (via its fr.2988 archetype and the related Garbino letter) and stalled — R4450 is not new ground, and the
   "key almost certainly exists" hypothesis in QUEUE.md's DC1 row is not supported by either named source.
3. **Aymeloglu.** aaymeloglu/unsolved-ciphers's `catalogue/decode-catalog.csv` and `decode-records.jsonl`
   carry id 4450 (routine catalogue row) but it is absent from `decode-ranked.md`'s printed rows and from
   `exclude.txt`, consistent with a catalogue entry that has not been attempted there either.
4. **Web.** WebSearch `"Hieronimo Ranzo" OR "Girolamo Ranzo" Gattinara chiffre déchiffré 1525 fr.2988` returned
   only tangential hits (Wikipedia disambiguation pages, a snippet confirming from dbourdeau's own published
   site that Ranzo used "an initial-letter code" as Gattinara's kinsman) — no third-party solution located.
5. **DECODE.** A prior LANE N pass this session read R4450's RecordsView page directly (QUEUE.md DC1 row): no
   attached key/transcription/decryption document found.
6. **Community lists.** Tomokiyo's site is the list of record here (item 1); no separate forum thread found.

## Verdict

**Open**, not found-solved. But the "finish-existing-key" plan in QUEUE.md's DC1 row needs revision before any
transcription pass: this folio is a copy of a specific undeciphered Ranzo letter (fr.2988 f.9) in a system
Bourdeau has already tried and failed to break (function words only recovered, no base key), not a plain
sibling-alignment problem against the volume's 18 already-Decrypted records — nobody has shown those 18 share
Ranzo's cipher. If this target is promoted, the next step is to check the 18 Decrypted siblings' own system
against Ranzo's transcribed corpus (Bourdeau's `vasto1527/n20/`) before assuming either helps the other.

Requests this pass: WebSearch 1, github.com 0 (reused this session's shared shallow clones, logged in
ROOM.md). No fresh DECODE login (reused the prior worker's RecordsView read). No promotion, no decoding.

flag for LANE N orchestrator: DC1's QUEUE.md rationale over-states the strength of the "finish-existing-key"
lead; recommend the row be corrected or the nomination carry this caveat.
