found-solved

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

## Update, 25 September 2026 (LANE OX OX-VAU, session_01QWGkEdftoGy7RQ2rKaGyuh) -- the "ontcijferde brief" resolved, status changed to found-solved

Job: read the edition's front-matter/footnote conventions for the asterisk and "ontcijferd/onopgelost"
wording, and identify what letter the KS24 p.812 index's "ook een ontcijferde brief is aanwezig" ("a
deciphered letter is ALSO present") refers to. Host `resources.huygens.knaw.nl` only, one request at a
time, >=1.5s apart.

**Correction inherited from `sources/huygens/NOTES.md`'s round 2 (24 Sept 2026):** that pass found the KS24
p.812 asterisk does not reliably mark cipher letters at all (3 of 4 spot-checked asterisked letters in this
same Vaudemont run are ordinary prose) and that the real per-letter index is a third viewer accessor,
`retroboeken/willemiii/toc1/index_html` ("Chron. lijst brieven"), which gives real letter numbers. Used it
here: query `correspondent:ustring:utf-8=Vaudemont` (172 hits, batch_start=0 and 100) maps the 25 March 1699
letter to **n. 220, Eerste gedeelte, deel 2, KS 24, p. 242**, immediately preceded by **n. 219, 18 Maart
1699, p. 241** ("*18 Maart (met bijlage)" in the p.812 index) and followed by n. 221, 15 April 1699, p. 244.

**The letter itself (p.242), read directly (not the OCR snippet):** the printed text opens "J'ay receu par
l'ordinaire de dimanche passe la lettre que vous m'aves fais l'honneur de m'escrire..." and a long middle
passage (military/financial figures for the Milanese: troop numbers, artillery, tax revenue committed to
Mr. de Leganes) is set in distinctive letter-spaced type, unlike the rest of the letter and unlike n.219 and
n.221 either side of it. **Footnote 1 on p.242, quoted in full:**
> "Deze brief is grootendeels in cijferschrift aanwezig; er is ook een exemplaar in opgelost cijferschrift
> (van Robethon's hand), dat ik in den tekst volg."
> ("This letter survives mostly in cipher; there is ALSO a copy in solved cipher [in the hand of Robethon,
> Willem III's secretary], which I follow in the text.")

This is the edition's own explanation of "grootendeels in onopgelost cijferschrift; ook een ontcijferde
brief is aanwezig" from the p.812 index -- word for word the same two facts, in the editor's own voice, at
the letter itself. **The "ontcijferde brief" is not a separate letter elsewhere in the Vaudemont run (round
1's own guess); it is a second exemplaar of this exact letter (25 March 1699), already deciphered in
Robethon's hand, which Japikse used as his copy-text.** Round 1's inference is superseded; this is the
"decisive check against the actual leaf" that both round 1's own verdict and `sources/huygens/NOTES.md`
caveat 2 called for.

**The letter-spacing convention, confirmed independently at two other places in the same volume (KS24),
searched via the retroboeken "Zoek" full-text accessor with `source_id=2`:** footnote 1, p.38 (letter no.
32, Sunderland to Willem III, 20 June 1693): "De gespatieerd gedrukte woorden zijn in den brief uit
cijferschrift opgelost" ("The letter-spaced printed words are, in the letter, deciphered from cipher");
p.131 (search snippet only, not opened in full this pass, budget): "...onderstreepte passages, in den tekst
gespatieerd, waren klaarblijkelijk bestemd [...] gecijferd te worden, en zijn daarom gespatieerd gedrukt."
This is edition-wide house style, not something specific to the Vaudemont letters: letter-spaced printed
text = a passage that was in cipher in the source Japikse worked from, now printed decoded. A "Zoek" search
for `cijfer`/`gespatieerd` restricted to source_id=2 found no hit in the front matter's own roman-numeral
pages (I-XXXI or so, not individually fetched this pass) -- the general statement of the convention, if
written out once rather than repeated per footnote, most likely sits in deel 1's (KS23) front matter, not
re-stated in this deel; not read this pass (out of scope, flagged below).

**No numeric ciphertext is printed anywhere in this edition for this letter.** Only Robethon's already-
deciphered French text is printed (with the letter-spacing marking which words came from cipher); the
manuscript ciphertext itself is not transcribed or reproduced. `ciphertext.tsv` is therefore not populated
from this source -- there is nothing here to grade H/C/S/M/I as ciphertext, only a printed plaintext, graded
H (read directly from the edition page). `plaintext_print.txt` holds the letter-spaced passage in full plus
a description of what surrounds it; the full p.243-244 continuation (ordinary roman type, not cipher-
marked) was read from the OCR html but not fully retyped, since it is not needed to answer the cipher-
system question this pass covers.

**Confirmed also from n.219 (p.241, 18 Maart 1699, "met bijlage" in the p.812 index):** the letter itself is
ordinary plain French (a report on Comte Boselli's deposition and banishment from Venice, with a Latin
extract still attached as an enclosure per footnote 4) -- not cipher, no letter-spacing, no footnote about a
decipherment. But its closing lines are the first mention of a cipher between these two correspondents:
"...comme je suis persuade que vous scaures bien des choses sur cette matiere, je vous prie de vous
souvenir, Milord, que nous avons un chifre et que ce que vous me feres l'honeur de me mander, ne cour pas
risque d'estre jamais sceu ailleurs" ("...remember, my lord, that we have a cipher, and that what you do me
the honour of writing to me will run no risk of ever being known elsewhere"). Read together with n.220's
footnote, the sequence is: 18 March, Vaudemont proposes/reminds Bentinck they have a cipher for sensitive
material; 25 March, one week later, he uses it for the first time (or an early time) in this run, for the
Milanese financial/military figures; the letter survives at the archive mostly in that cipher, but a
solved exemplaar in Robethon's own hand also survives and is what Japikse actually printed. n.221 (15 April
1699, p.244, the tail of which was read alongside n.220's own tail) is ordinary prose, no cipher.

**Verdict: found-solved, not open.** A contemporary decipherment of this letter survives (Robethon's hand)
and its text is already in print (Japikse 1937-ish KS24, exact publication year not checked this pass).
This is a "cryptanalytic result" grade question that does not arise -- nothing here was cryptanalysed by us
or by anyone we can attribute; per rule 10 this is reported as found in this source, not classified for
novelty (a verifier's job, not this worker's).

**REQUEST.md implication:** the copy-order case is weaker now than round 1's framing assumed, since the
letter's content is already published via Robethon's decipherment. A copy of the original manuscript cipher
(and, if it survives separately, Robethon's own decipherment sheet) at the Portland (Welbeck) collection,
University of Nottingham, would still be useful for a system/key comparison against other Willem III-era
ciphers (e.g. the Heinsius `sources/huygens/NOTES.md` "Cijferschrift" leads, invnrs 2315-2317, or any
Bentinck-circle key), but it is no longer a blocker to reading this specific letter's content -- updated in
REQUEST.md.

**Not done this pass (flagged, not a blocker):** the general statement of the letter-spacing convention in
KS23 deel 1's front matter (if it exists there rather than only being repeated per-footnote); a check of
whether any of the other asterisked-but-unopened Vaudemont letters in the p.812 index (round 2's ~20 count)
also carry a Robethon-hand decipherment, which would be the natural next step for the broader Vaudemont
cipher-letter sweep flagged repeatedly in `sources/huygens/NOTES.md`; reading the whole of p.243 (not
letter-spaced, judged out of scope for the cipher question).

Requests this pass: `resources.huygens.knaw.nl` 11 (1 reachability/toc1 fetch, 2 toc1 batches, 1
pages.json?source=2, 3 page-html fetches [241, 242, 244], 2 "Zoek" search-term fetches [gespatieerd,
cijfer], 1 page-html fetch for p.38, 4 image fetches [38 x2 -- first attempt wrongly 3-digit-padded, second
correct; 241, 242; 244 returned HTTP 200 with Content-Length 0, a real server-side gap, not retried further
per the one-retry rule]). All >=1.5s apart, descriptive User-Agent. No other hosts. No subagents (brief
allowed none). Well under the $5 stall-alarm cap.
