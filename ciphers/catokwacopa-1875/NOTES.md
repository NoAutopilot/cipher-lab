partial

# Catokwacopa advertisements, Evening Standard (*The Standard*), 8 and 20 May 1875

- Source: QUEUE.md rank 18 (score 32), scored 20 September 2026; catalogued from Bourdeau's `catokwacopa/`
  target folder and Klaus Schmeh's Top 50 list.

## Check-solved sweep (23 September 2026)

1. **Web search.** "Catokwacopa cipher Evening Standard 1875 solved plaintext" — surfaces Cipherbrain's own
   coverage directly: "Revisited: The Catokwacopa cryptograms from 1875" (2018), "The Top 50 unsolved encrypted
   messages: 8. The Catokwacopa cryptograms" (2018), and the original 2015 "Wer löst die
   Catokwacopa-Kryptogramme..." post, plus Bourdeau's own catalogue index. The search summary itself states
   "the Catokwacopa cipher remains largely unsolved, with only partial plaintext solutions identified as of the
   most recent updates" — consistent with every other source below. found=false for a full solve; found=true for
   extensive partial/documented work.

2. **Print.** No calendar or documentary edition applies (a Victorian newspaper personal advertisement, not a
   state paper); the relevant "print" sources are the two 1875 *Evening Standard* issues themselves. The British
   Newspaper Archive listing and newspapers.com index were not queried directly this sweep (both require login
   beyond a bare index search and were not in the budget for this pass); Bourdeau's `catokwacopa/NOTES.md`
   already records that the working transcription used is Thomas Ernst's BNA-verified text (`ads.py`), which
   corrects roughly a dozen errors in the transcription that had been circulating before it (e.g. "Hrsclam" for
   the correct reading, "138" not "139"). Not re-verified against BNA directly this sweep.

3. **Community lists.** Klaus Schmeh's Cipherbrain (scienceblogs.de/klausis-krypto-kolumne) is the primary
   source and is where this item's whole public history lives: the original 2015 post asking readers to solve
   it, a 2018 "Top 50" entry (#8), and a 2018 "Revisited" follow-up recording partial readings that had
   accumulated by then (Thomas Bosbach's "DYING DECLARATION"; Lance Estes and "Dave"'s Oxford-vocabulary reading
   — SUMMER TERM, 1853, CONINGTON, JOWETT, BALLIOL, SHIRLEY). A 14 August 2026 post republished the puzzle with
   an active comment thread (per QUEUE.md's own rationale, sourced from klausschmeh.net); Schmeh's own verdict,
   quoted in Bourdeau's `catokwacopa/` folder and in a Facebook comment cited by Aymeloglu's `SHORTLIST.md`
   (line 148), is that "the cipher mechanism has been solved, but the complete, unique plaintext cannot be
   mathematically reconstructed." Full-page fetch of the Cipherbrain posts themselves is blocked by this
   environment's egress policy (`EGRESS_BLOCKED domain=scienceblogs.de`; see
   ciphers/charles-rupert-1645/NOTES.md item 3), so only WebSearch snippets and the two solver repositories'
   own citations of Schmeh could be checked directly this sweep, not the original posts' full text or comment
   threads. found=true (extensive, but explicitly not a unique-plaintext solve; source partially unreachable).

4. **DECODE.** Not applicable — a 19th-century newspaper advertisement, not a DECODE-catalogued manuscript
   archive item. Not checked.

5. **Bourdeau (`github.com/dbourdeau/cyphersolver`, shallow clone 23 Sept 2026, MIT code / CC BY 4.0 text).**
   **found=true, substantial, no unique solve.** `catokwacopa/NOTES.md` ("The Catokwacopa advertisements (1875)
   — which readings the letters force, and which are guesses") is a detailed, dated (September 2026) audit, not
   a fresh solve. It confirms the structural mechanism (line *i* of the first ad and line *i* of the second are
   order-preserving halves of one plaintext phrase, letters dropped by W.) is agreed and statistically real (a
   permutation test on the paired line lengths: "no random re-pairing in 100,000 comes that close"), catalogues
   the accumulated proposed readings since 2018 (Bosbach, Estes/"Dave", Ernst's diplomatic line numbering and
   BNA-checked transcription, Krajčovič's QUI FIT/Horace *Satires* reading and 2026 "exact-cost audits"), and
   states the central unsolved problem: the omission rule (three to twelve letters freely inserted per line)
   lets "plausible English... fit almost anything," so readings are only trustworthy where the letters force
   them, and Bourdeau's own audit (15 September 2026, cited in QUEUE.md's rationale) found only a handful of
   lines are actually forced. No committed reading claims full, unique plaintext recovery. `TARGETS.md` and
   `top50/` reference the item consistently with this "audited, unresolved" status; `catalogue/`'s scraped
   listing does not mark it read/solved.

6. **Aymeloglu (`github.com/aaymeloglu/unsolved-ciphers`, shallow clone 23 Sept 2026; no licence, cite only, no
   code copied).** No target folder (this is not one of Aymeloglu's eight active targets), but `SHORTLIST.md`
   discusses it twice: line 81, "Substantial partial reconstruction already exists (Gaffney, Ernst and others,
   discussion through Sept 2026), so this is finishing work, not a first break"; and line 148, in the exclusion
   table, quoting Schmeh's Facebook comment above and recommending "effectively cracked, remove" — i.e.
   Aymeloglu's own project assessment is that this item is not worth pursuing as an open cryptanalysis target,
   precisely because the mechanism is known but no unique plaintext is recoverable. found=true (assessment, not
   a target folder).

## Verdict

**Partial**, not open and not found-solved. The encoding *mechanism* is publicly established and agreed by
every source that discusses it (Bourdeau, Aymeloglu, Schmeh/Cipherbrain), and substantial partial plaintext
readings have been proposed since 2018 by multiple named researchers (Bosbach; Estes/"Dave"; Ernst; Krajčovič),
but no source claims a complete, forced, unique plaintext, and the strongest quantitative audit available
(Bourdeau, 15 September 2026, cited in QUEUE.md) argues the omission rule structurally prevents one from being
demonstrated. This is not a negative result under rule 3 (no matched-control test of a solver against synthetic
ciphers of the same design was run, by this sweep or by the audits cited), so "closed-negative" is not used; it
is reported as partial. No Stage 2 line applies (verdict is not "open"). QUEUE.md row 18 has been annotated with
this finding rather than moved to Dropped, since no source claims the item solved.
