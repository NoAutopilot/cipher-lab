# George W. Erving to James Madison, Madrid, 10 August 1807

Status: **found-solved**

## Rule 1: search before solving (21 Sept 2026)

QUEUE.md rank 9 named this target as "no decode on the NARA copy" and set the next step to
transcription (NARA M31 reel 12 frames 0362-0366, naId 188605361; Bourdeau's `pinckney_chain.tsv`).
Before any transcription, the mandatory checks were run:

1. **Web search**, sender + recipient + date, several phrasings: `Erving to Madison "10 August 1807"
   Madrid founders.archives.gov`; `"Erving" Madison Madrid "August 1807" despatch cipher decode`;
   `site:founders.archives.gov Erving Madison 1807 Madrid August`; `American State Papers Foreign
   Relations Erving Madrid 1807 Spain despatch cipher`. These surfaced the Founders Online document
   list for Erving-to-Madison 1807 and, via the "More between these correspondents" links on the
   1 September 1807 letter (99-01-02-2092), the document itself (below).

2. **Printed editions.** Founders Online / *The Papers of James Madison, Secretary of State Series*
   (Rotunda/University of Virginia Press, Early Access) has the despatch in full:
   [To James Madison from George W. Erving, 10 August 1807](https://founders.archives.gov/documents/Madison/99-01-02-1993).
   Fetched with `tools/browser_fetch.js` (curl gets HTTP 202 with an empty body from this site; the
   browser tool renders it, consistent with CLAUDE.md's Access playbook notes on founders.archives.gov
   needing a real browser). The document is headed exactly as our target describes it:

   > In the ⟨Cypher⟩ of the Legation. No. 24 Duplicate. Madrid Augt. 10th. 1807

   and the entire body — roughly 700 words on the Prince of Peace, the Electorate of Hanover, the
   planned "Kingdom of Ebro", Beauharnais, and a postscript on the Russian mediation — is printed as
   continuous plain English, with only isolated words in ⟨angle brackets⟩ marking manuscript damage
   supplied by the editors (the same editorial convention used throughout this edition, e.g. in the
   already-worked 24 March 1807 letter, `/tmp/scout-check/cyphersolver/erving1807/NOTES.md`). Source
   note at the foot: "DNA: RG 59--DD-Diplomatic Despatches, Spain" — the same National Archives record
   group as the M31 microfilm this target names, not a different collection. This is a full
   contemporary decipherment of exactly the letter in QUEUE.md rank 9: same sender, recipient, place,
   date, and cipher ("Cypher of the Legation" = Pinckney's legation code, as on the 24 March 1807
   letter already worked in cyphersolver/erving1807/).

   American State Papers, Foreign Relations vol. 3 and Google Books were not separately queried once
   this was found: the Founders/PJM-SS Early Access text is the more authoritative and more complete
   printed source and already settles the question.

3. **DECODE (de-crypt.org), no login.** One query tried (`RecordsSearch?keyword=Erving`, curl with a
   browser UA, HTTP 200) returned the generic site shell, not a results list — the site's real search
   endpoint needs the browser tool or a login to drive the search form, neither of which was pursued
   further since DECODE indexes European manuscript archives (BL, TNA, BnF, PARES, etc.), not NARA
   diplomatic despatches, and the target was already settled by step 2. Not a load-bearing check here.

4. **Solver repositories**, shallow clone (`git clone --depth 1`) into `/tmp/scout-check/`, 21 Sept 2026:
   - `github.com/dbourdeau/cyphersolver`: `erving1807/NOTES.md` (dated 18 Sept 2026) covers only the
     24 March 1807 letter in full; its "Not done" section names the 10 Aug 1807 letter explicitly as
     "the next target for a rebuilt Pinckney key" and says to "check first whether Founders prints a
     decode (99-01-02 series)" — advice this session followed, which is what led to step 2 above.
     Bourdeau had not yet done that check as of his 18 Sept note.
   - `github.com/aaymeloglu/unsolved-ciphers`: `grep -rli "erving\|pinckney\|188605361"` returns no
     hits anywhere in the repository. Not covered there.

## Verdict

The 10 August 1807 despatch is not "unread": it has a full contemporary decipherment already in print,
via Founders Online's Early Access edition of *The Papers of James Madison, Secretary of State Series*.
QUEUE.md's "no decode on the NARA copy" is correct as far as it goes (the specific M31 reel 12 frames
0362-0366 that Bourdeau examined lack Madison's own interlinear decode, same situation as the 24 March
letter before its RC2 comparison) but does not mean no decode exists anywhere — the Madison Papers
editors' modern edition draws on the same RG 59 file and gives the full plaintext. No campaign is
justified: no images were fetched, nothing was transcribed, and no key was applied, per this brief's
instruction to stop before transcribing once print-in-clear is established.

Grades: none produced this session (H/C/S/M/I do not apply — this is a "found already solved by others"
verdict, not a reading).

## What a verifier would need to search (rule 10)

This NOTES.md records a *search result* ("not found unread"), not a novelty class — a verifier assigning
an N-class to Bourdeau's already-published 24 March 1807 reading (or to any future claim about this
27-letter correspondence) would still need: the full PJM-SS printed volume/Rotunda edition covering
Aug-Sept 1807 (this session used the Early Access web text, not a page-numbered print volume); American
State Papers, Foreign Relations vol. 3, for whether Congress's published diplomatic correspondence also
carries this despatch; and a phrase search on distinctive text ("Kingdom of Ebro", "Prince of Peace",
"Beauharnais... perfectly odious") across Google Books/HathiTrust/Internet Archive for any other
19th/20th-century printing (e.g. a State Department or scholarly compilation of the Erving-Madison
correspondence) that might predate or duplicate the Founders Online text as the "first" print.

## Sources checked and dates

- founders.archives.gov, document 99-01-02-1993 ("To James Madison from George W. Erving, 10 August
  1807") and 99-01-02-2092 (1 September 1807, whose "Preceding" link led to it) — fetched 21 Sept 2026
  via `tools/browser_fetch.js` (curl returns HTTP 202 with an empty body on this host).
- github.com/dbourdeau/cyphersolver, shallow clone 21 Sept 2026, `erving1807/` folder read in full
  (small: NOTES.md plus data/script files, not a full-repo read).
- github.com/aaymeloglu/unsolved-ciphers, shallow clone 21 Sept 2026, grepped only.
- de-crypt.org, one unauthenticated query, 21 Sept 2026 (inconclusive, not load-bearing).
- Web search (WebSearch tool), four queries, 21 Sept 2026, listed above.
