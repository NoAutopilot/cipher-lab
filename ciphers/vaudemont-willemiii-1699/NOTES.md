open

# Vaudemont to Willem III / Bentinck, mostly in unsolved cipher, *25 March 1699

QUEUE row: HU6 (`QUEUE.md`, "Huygens and Nationaal Archief correspondence editions: letters noted in cipher
(LANE N harvest of 24 September 2026)"). Brief `.claude/briefs/runs/2026-09-24-lane-n-csHU.md`.

## Source

Correspondence of Willem III and Hans Willem Bentinck (1st Earl of Portland), printed in N. Japikse (ed.),
*Correspondentie van Willem III en van Hans Willem Bentinck, eersten graaf van Portland*, eerste gedeelte, deel
2 (KS 24), via the Huygens `retroboeken/willemiii` viewer (no login, `resources.huygens.knaw.nl`). No letter
number or archive shelfmark is given on the index page itself (see below).

## Check-solved sweep, 24 September 2026

Run directly by this worker (Sonnet, no Workflow tool, no subagents), resolving the ambiguity flagged as caveat
2 in `sources/huygens/NOTES.md`.

1. **Editions first -- the primary edition's own alphabetical index, re-fetched and read in full this pass**
   (`images/willemiii_ks24_0812.jpg`, page text also read as OCR): the "Alphabetische lijst van brieven", under
   the heading "Charles Henri de Lorraine, prins van Vaudemont, en Anna Elisabeth de Lorraine, prinses van
   Vaudemont", lists every letter to/from Willem III and Bentinck from this correspondent circle, 1692-1701,
   with an asterisk marking cipher letters. The 1699 entries, quoted verbatim:
   > "1699: 7 Januari, 11 Januari, 18 Januari, 4 Maart (van de prinses), 11 Maart (van de prinses), *18 Maart
   > (met bijlage), **\*25 Maart (grootendeels in onopgelost cijferschrift; ook een ontcijferde brief is
   > aanwezig)**, *15 April, *24 Juni, 22 Juli (van de prinses), 23 September, 11 November, 15 December (van
   > de prinses), 23 December."
   This confirms the target's own catalogue entry directly, word for word. **The 25 March letter itself is
   stated as "grootendeels in onopgelost cijferschrift" (mostly in unsolved cipher) -- this is not
   found-solved.** The clause "ook een ontcijferde brief is aanwezig" (a deciphered letter is ALSO present)
   most plausibly reads as: a *separate*, unspecified letter elsewhere in this same correspondence run has
   been deciphered and survives alongside the 25 March cipher letter -- not that the 25 March letter itself
   has since been solved (if it had been, the index would more naturally say so directly, e.g. "ontcijferd" or
   "opgelost", rather than maintaining "onopgelost" in the same breath). This reading is this worker's own,
   not confirmed against the edition's front-matter legend for the asterisk convention (not checked this pass,
   budget) or against which of the many *other* asterisked entries in the same list (1695-1701, at least
   twenty more) is the "ontcijferde brief" referred to -- that identification is a genuine open task for a
   future recovery-focused worker, not resolved here.
   Also newly visible this pass, not previously logged: at least 20 further asterisked (cipher) entries across
   1695-1701 in the same Vaudemont run, none individually read -- a substantially larger lead than the single
   25 March instance already flagged in the harvest, consistent with `sources/huygens/NOTES.md`'s own note
   that this index page "is a lead for a much larger future sweep."
2. **Archive location -- decisive for copy status.** The index page gives no NA-style shelfmark. CLAUDE.md's
   own Access playbook already establishes, as a standing fact from a previous pass, that "for Willem III/
   Bentinck, the Portland papers in Nottingham are NOT copy-free" -- these letters are held at the University
   of Nottingham (Portland (Welbeck) collection), not digitised at nationaalarchief.nl. No independent
   re-verification of this fact was run this pass (it is already logged project-wide guidance, not
   re-searched); the target is treated as copy-order on that basis.
3. **DECODE overlap risk, checked again this pass.** `aaymeloglu/unsolved-ciphers/catalogue/decode-catalog.csv`
   row for id 2827 ("Nationaal Archief... collection 1.10.29 Familie Fagel, inv. nr. 5345...
   cipher_Bentinck_1748") re-confirmed as a *different* NA collection (1.10.29 Fagel, not the Nottingham
   Portland papers) and a later date (1748, after this edition's own span, which ends with Willem III's death
   in 1702) -- very unlikely to be the same item, consistent with the harvest's own flag; not excluded outright
   since still unconfirmed, but not treated as a match.
4. **Post-edition literature search.** `WebSearch "Vaudemont Willem III Bentinck 1699 cijferschrift ontcijferd
   brief"` returned only general catalogue/library pages for the printed edition itself and secondary
   biographical pages on Bentinck -- no hit naming a decipherment of this or a related Vaudemont letter.
5. **Community lists.** `sources/cryptiana/web/dutch.htm` re-read: no mention of Vaudemont or this
   correspondence. (Cryptiana's `nevers.htm` page mentions an unrelated 16th-century Cardinal "de Vaudemont"
   in a Nevers cipher key list -- a different person and a different cipher, noted so a later worker does not
   confuse the two.)
6. **Solver repositories.** Fresh shallow clones this pass grepped for "vaudemont", "bentinck", "willem iii",
   "portland": the only "Vaudemont" hits in either repository are Charles III, Duc de Lorraine's brother
   Charles II writing to a *different* "de Vaudemont" in 1592 (BnF Français 3621, `cyphersolver/lorraine1592/`
   and the matching DECODE catalogue row, id 9449/jsonl row) -- a wholly different correspondence, a century
   earlier, in France, not the Willem III/Bentinck circle. Not a hit on this target.

## Verdict

**Status: open.** The 25 March 1699 letter is confirmed, directly from the edition's own index, to remain in
unsolved cipher; the note of a separately deciphered letter in the same run is a genuine recovery-shaped lead
but names no specific date, so it is not yet actionable as a sibling pairing. No later print, community list,
DECODE record or solver repository names a solution for this letter.

**Copy status: copy-order.** The originals are in the Portland Papers, University of Nottingham, per CLAUDE.md's
own playbook -- not copy-free. `REQUEST.md` written (no personal data; logs only what is needed and why).

**Kind: recovery.** A solved sibling is stated by the edition to exist in the same correspondence run; finding
it (one of the ~20+ other asterisked Vaudemont entries 1695-1701) is the natural next step before any
cryptanalysis is attempted on 25 March itself.

Search log (rule 10): reported above, per source. Not classified for novelty. Requests this pass:
`resources.huygens.knaw.nl` ~3 (book_data.js, 1 pages.json, 1 html_url OCR fetch, 1 image fetch -- some steps
shared with HU4/HU5 fetches earlier in this same pass), `www.nationaalarchief.nl` 0 (not applicable, archive is
in Nottingham not the Netherlands), `github.com` 0 (reused clones already on disk this session). WebSearch 1.
No subagents.
