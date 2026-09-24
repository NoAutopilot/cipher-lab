open

# Willem van Hessen to Willem van Oranje, partly unsolved cipher, 28 January 1567

QUEUE row: NB3 (`QUEUE.md`, "Dutch and Belgian archives (LANE N scout of 24 September 2026)").

## Source

WVO briefnr **1127** (https://resources.huygens.knaw.nl/wvo/app/brief?nr=1127), 28 January 1567, from Kassel.
William IV "the Wise", Landgrave of Hesse-Kassel (1532-1592; Anna of Saxony, William of Orange's second wife,
was his niece), to William of Orange. WVO's Inhoud field: "Bericht over de geboorte van een jonge dochter en
over het geschil tussen August van Saksen en Johan Frederik II van Saksen-Weimar" (news of the birth of a young
daughter, and of the dispute between August of Saxony and Johann Friedrich II of Saxe-Weimar) -- this is the
**Grumbach Feud / siege of Gotha** (Dec 1566-Apr 1567: Johann Friedrich II sheltered the outlawed Wilhelm von
Grumbach, was placed under the Imperial ban 12 Dec 1566, and August of Saxony besieged him at Burg Grimmenstein,
Gotha, until its fall 13 Apr 1567 -- a well-documented episode, confirmed by WebSearch, but no source located
naming this specific letter).

**One WVO record covers both copies:**
- The **original** (where the cipher sits): Koninklijk Huisarchief Den Haag, A 11/XIV B/15-43. **No PDF listed
  in the WVO database this pass** -- not copy-free for the cipher passage itself.
- The **draft/minuut**: Hessisches Staatsarchiv Marburg, Bestand 3II, Nassau-Niederlande, Korr. 1567, f.
  151r-152v. Free PDF, no login: `resources.huygens.knaw.nl/media/wvo/images/01000-01999/01127.pdf`.

WVO's Opmerkingen field states plainly: **"Een gedeelte van het origineel is in onopgelost cijferschrift. De
minuut geeft de complete tekst."** (Part of the original is in unsolved cipher. The draft gives the complete
text.) **Confirmed by eye this pass** (`images/01127_p1-1.png`): page 1 of the draft PDF is the outer address
leaf, docketed "An Printzen zu Uranien" (To the Prince of Orange) with a receipt note "28 Januarij ... 1567",
confirming the correct record and date. The draft's running text (its other pages) was not opened further this
pass -- not required to confirm the record, and this brief's instruction is to confirm presence, not transcribe.

**This is explicitly flagged by the WVO curators as the crib case named in the brief**: if the draft is a
compositional draft (not simply an earlier version covering different content -- see caveat below) of the same
letter whose original is partly enciphered, the plain draft text corresponding to the enciphered original
passage is a known-plaintext crib, and the task becomes alignment against the (unseen) original ciphertext, not
cryptanalysis from scratch. **Caveat, not resolved this pass**: a "minuut" can be an earlier compositional stage
that was then revised before the fair copy was made and partly enciphered, so the draft and the enciphered
passage are not guaranteed to cover identical wording -- this needs checking directly against the original once
imaged (see REQUEST.md).

## Check-solved sweep, 24 September 2026

Run directly by this worker (Sonnet, no Workflow tool, no subagents).

1. **Editions first.** No printed-edition citation in WVO's own Brongegevens for 1127 (manuscript only, both
   copies). Rommel's *Geschichte von Hessen* (named in CLAUDE.md's editions-first list for Hesse) covers only
   up to Philip the Magnanimous's death in 1567 in its original four volumes (1820-1830); its continuation,
   *Neuere Geschichte von Hessen* (1835-1843), was not located specifically for William IV's Kassel
   correspondence by WebSearch this pass -- flagged as unread, a genuine gap. The Grumbach Feud / siege of
   Gotha is separately well documented in German historiography (Wikipedia's Grumbach Feud article, Deutsche
   Biographie, Gotha local-history pages, all read via WebSearch this pass) but none of the sources surfaced
   name this specific letter, its cipher, or a decipherment.
2. **WVO curatorial field.** As above: the curators explicitly label the cipher "onopgelost" (unsolved) in
   their own Opmerkingen field -- the strongest and most direct of any of this batch's four targets (contrast
   NB1/NB2, which are silent rather than explicit).
3. **Community lists.** `sources/cryptiana/web/dutch.htm` read in full: no mention. WebSearch (`Rommel
   Geschichte von Hessen Wilhelm von Hessen Willem van Oranje 1567 brief Chiffre`; `Grumbach Fehde 1567 Gotha
   Johann Friedrich Wilhelm Landgraf Hessen Brief 28 Januar`) found nothing naming this letter or a solution.
4. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` grepped for the same terms as NB1/NB2:
   zero hits.
5. **Solver repositories.** Same fresh clones as NB1/NB2 (24 Sept 2026): no hits relevant to Willem van Hessen
   or this correspondence.
6. **General web search.** As item 3.

## Verdict

**Status: open.** WVO's own curators state the cipher is unsolved; no printed edition, community list, DECODE
record or solver repository names a decipherment. The Rommel continuation volumes (*Neuere Geschichte von
Hessen*) remain unread -- flagged as the clearest next step for a future edition check.

**Copy status: partial / not fully copy-free.** The draft is copy-free (free PDF, confirmed reachable and
viewed). **The original, where the cipher itself sits, has no PDF in the WVO database this pass** -- see
REQUEST.md for a copy-order ask to the Koninklijk Huisarchief Den Haag (A 11/XIV B/15-43).

**Kind: cryptanalysis (crib available)**, pending confirmation that the draft and the enciphered original
passage cover the same content once the original is imaged.

## csWV3: two further circle letters, not candidates (LANE N2, 24 September 2026)

Print-status pass across all 73 un-nominated WVO cipher letters (`.claude/briefs/runs/2026-09-24-lane-n2-csWV3.md`;
full table `sources/wvo/print-status-2026-09-24.tsv`). Two more Willem van Hessen letters, not in this folder's
existing table (which covers 1127 above):

- **Briefnr 174** (9 Apr 1567, "to Willem van Hessen", Antwerpen, GPA;HHSAWB;HSAM;KHAG). WVO's own remark:
  "solved on leaf" -- a contemporary decipherment accompanies the manuscript. Not fetched or imaged this pass.
  Flag for LANE R3 as a possible key source for the circle's cipher design (same correspondent as 1127, the
  cryptanalysis target above).
- **Briefnr 1069** (23 Mar 1563, "from Willem van Hessen", Marburg, HSAM;KHAG, no edition code). WVO Opmerkingen
  (fetched 24 Sept 2026, https://resources.huygens.knaw.nl/wvo/app/brief?nr=1069): "bij het origineel een
  exemplaar in cijferschrift en met ontcijfering" (beside the original, a copy in cipher AND WITH a
  decipherment). Not fetched or imaged this pass. Flag for LANE R3 as a second, earlier (1563 vs 1567) key
  source in the same correspondent circle.

Neither is a candidate; neither changes 1127's own cryptanalysis status above. Requests this pass:
resources.huygens.knaw.nl 1 (briefnr 1069 detail page, shared with the wider 9-page batch logged in
`sources/wvo/NOTES.md`); 174 read from `sources/wvo/cipher-letters-2026-09-24.tsv` only, no fresh fetch.
