# AUDIT -- fr15575-syllabic-1592-95 (VERIFY-NV05, account-2 worker, LANE-A2PUSH3, 3 Oct 2026 15:35-15:5x UTC)

Verifier, a session separate from NV05-CS, NV05B, NV05C, NV05D and NV05E. Light audit per the brief
(.claude/briefs/runs/2026-10-03-acct2-verify-nv05.md). Nothing was decoded or transcribed here.

**Claim under audit** (NOTES.md, NV05C/NV05D/NV05E): key no.54 (the Spanish syllabic numerical cipher of 1592 identified
by Tomokiyo; period key sheet BnF fr.3995 f.96v-97r) reads the clerk-glossed control letter fr.3641 f.111r at 237/266
codes; fr.15575 f.228 is the same syllabary and carries a period interlined decipherment over every line (L01-L04 decode
agrees with the gloss at 0.430, above the shuffled null p99 0.186, below the 0.60 floor); fr.15576 f.2 is a different
3-digit system, also with a period interlined decipherment.

## 1. Re-derivation (rule 7) and controls (rule 3)

    $ python3 tools/decode_key.py ciphers/fr15575-syllabic-1592-95/control_fr3641 --check
    ciphertext.tsv: tokens 419: H 223, M 41, U 155 / reading up to date        (exit 0)
    $ python3 tools/decode_key.py ciphers/fr15575-syllabic-1592-95/f228 --check
    ciphertext.tsv: tokens 135: H 77, M 9, U 49 / reading up to date           (exit 0)
    $ python3 control_fr3641/score_control.py --check   -> score.tsv up to date (exit 0)
    $ python3 f228/score_f228.py --check                -> score.tsv up to date (exit 0)
    $ python3 f2_fr15576/p1_check.py --check            -> exit 0

Fresh seeds (verifier's scratch script, importing the committed `score()` unchanged; 1000 draws each):

| statistic S | real key | value-shuffled key, seeds 7 / 1234 / 101 / 202 / 303 (p99) | real key against another line's gloss (all rotations) |
|---|---|---|---|
| fr.3641 f.111r (control), 266 codes | **0.891** | 0.267 / 0.271 / 0.267 / 0.259 / 0.259; means 0.196-0.198; 0 draws >= real in any seed | n=11, mean 0.273, max 0.301 |
| fr.15575 f.228 L01-L04, 86 codes | **0.430** | 0.186 at seeds 101 / 202 / 303 (score_f228.py has no seed option; seed 1 committed: 0.186); 0 >= real | n=3, mean 0.167, max 0.198 |

The committed numbers reproduce. Rule 3 "can the control differ" check: a value permutation among the 95 coded syllable
rows changes the decoded letters of every scored token, and S is computed from those letters, so the control is not
orthogonal to the statistic (not the bCAS/AX-5799 shape). The verifier's added second control (right key, wrong line's
gloss) also stays far below the real score on both leaves, so S measures line-specific agreement, not just the
frequency of common syllables in Spanish. On f.228 the margin over both nulls is real but the pre-registered 0.60 floor is
not met: FAIL as registered stands. NV05E's diagnosis (an incomplete gloss read) is the worker's look after scoring and is
untested until the pre-registered gloss re-read is run; it is a plausible explanation, not a result.

Grades (rule 4): the syllable values come from the period key sheet (fr.3995), so they are H read from a key source,
which is what decode_key.py prints; NV05E re-labelled the same 77 tokens "S" in NOTES.md. That is an under-label, not an
over-claim; the verifier's count for f.228 L01-L04 is **H 77, C 0, S 0, M 9, I 0, U 49** (control letter: H 223, M 41,
U 155). The letter-sign values in NV05E's illustrative runs ("ta[n] ta[r]de") are the worker's reading of the key
header, unscored: I.

fr.15576 f.2: "a different 3-digit system" rests on L01-L04 only (0/64 numeric tokens in the 10-99 syllabary range) and
one 1600 px overview of the no.54 nomenclator (3-digit codes not seen; a few 70x-like entries not eye-checked). Safe as
"L01-L04 are not in the no.54 syllabary"; the identity of the system is open.

"Period interlined decipherment over every line": for f.228 this rests on one 1600 px overview plus L01-L04 crops; for
f.233 and fr.15576 f.2 on overviews (f.2: plus four crops). Read as "over every cipher line seen at overview
resolution".

## 2. Search log (what was searched, 3 Oct 2026)

Solver's own log (NOTES.md "Premise check", "Web and blog check"): Tomokiyo pages on disk (henryiv.htm, nevers.htm,
spanish3.htm, phelippes.htm, league.htm, bnf4715.htm, GL.htm) -- no reading of any of the three leaves; Bourdeau
snapshots 2026-10-01..03 -- no hit; Lasry HistoCrypt syllabic paper -- no hit; Cipherbrain, Cipher Mysteries -- no hit;
Google Books API: van Durme 1964 and Lefèvre IV (1960) calendar two letters of Archduke Ernest to the King, Brussels,
5 Jan 1595 (analyses only, pages not openable from the cloud; LOCAL-QUEUE L47).

Verifier, independently (Google Books API with key and country=US, 1.6 s apart, 10 calls; archive.org advancedsearch 2):
- `"fr. 15575" chiffre`, `"15575" "228" espagnol chiffre`, `"15575" "Saint-Germain" lettres espagnoles`, `"15576"
  Ernest 1595` -- only the BnF *Catalogue général des manuscrits français, Ancien Saint-Germain français* (1898, Google
  Books full view, uTZWAAAAYAAJ / nq9OG1RvhGUC; volume description, not a text edition; its vol. II covering 15575-15576
  is not on archive.org -- only vol. III is, CatalogueGeneralDesManuscritsAncStGermFr3) and statistical noise.
- Phrase queries from the gloss as read: `"tan tarde" "por los despachos" 1594`, `"despachos" "con don Juan" "por mar"
  1594 Flandes cifra`, `"Ernest" "Fuentes" "frontera" "Francia" 1595 carta descifrada` -- no hit on these letters.
- Recipient/date: `"Conde de Castel Rodrigo" 1594 cifra carta Bruselas` (0), `"Castel Rodrigo" Mendoza 1594 Bruselas
  carta` (0), `"conde de Fuentes" "5 de enero de 1595"` (1 unrelated legal-history hit).
- Not reached this session (light brief, box 40 min): CODOIN full text, Simancas Estado K / Estado Flandes calendars
  beyond the van Durme and Lefèvre snippets above, HathiTrust (cloud-blocked), JSTOR (queued below), the Lefèvre and van
  Durme pages themselves (LOCAL-QUEUE L47).
- JSTOR-QUEUE.tsv rows appended 3 Oct 2026, both families: (i) `"Ernest" AND "Fuentes" AND 1595 AND (cipher OR chiffre
  OR cifra)`, `"Castel Rodrigo" AND 1594 AND (cipher OR chiffre OR cifra) AND Flandes`; (ii) bare phrases, no cipher
  keyword: `"de buena gana como por"` (f.228 L04 gloss as seen by NV05E on the crop), `"apercibido para ir a la frontera"`
  (f.2 gloss fragment, NV05D's interpretation, not transcribed).

## 3. Classification (rule 10)

| item | class | prior plaintext | prior decipherment | key source | evidence / confidence |
|---|---|---|---|---|---|
| fr.15575 f.228 | **N0** | yes: the period interlined decipherment on the leaf itself (16th-c. clerk); no print located by the searches above | yes, period, on the leaf | `period` (key no.54 sheet BnF fr.3995 f.96v-97r, transcribed by NV05B; key identified and reconstructed by Tomokiyo, credited) | high that a contemporary decipherment exists (seen at overview and on L01-L04 crops); our decode covers L01-L04 only and agrees with that gloss at 0.430 |
| fr.15575 f.233 | **N0** | yes: period interlined decipherment seen at 1600 px overview; no print located | yes, period, on the leaf | none applied (nothing transcribed); Tomokiyo assigns it to no.54 | medium (overview only, gloss not read) |
| fr.15576 f.2 | **N0** | yes: period interlined decipherment on the leaf; the dispatch is very probably calendared (van Durme 1964; Lefèvre IV p.~277, Ernest to Philip II, Brussels 5 Jan 1595), analyses unread | yes, period, on the leaf | none (not in the no.54 syllabary per NV05D P1; system unidentified) | high for the gloss (seen on four crops); identity with the calendared letter is consistent, not proven |
| fr.3641 f.111r (control letter) | **N0** | yes: interlined on the leaf, and Tomokiyo publishes a cleaned decipherment (league.htm no.80) | yes | `period` | high; this is the known-answer control, not a target |

Note on the brief: it named the key source for no.54 as `published` (Tomokiyo's key). The repo's key file was read off
the period key sheet itself, not off Tomokiyo's table (his key image is still only in IMAGE-QUEUE.tsv), so rule 10's
definition gives `period`; Tomokiyo is credited for identifying the key and its letters. `text`: the plaintext is known
from the period decipherment on each leaf; print not located.

No item reaches N3, so no SECOND-OPINIONS-QUEUE.tsv row.

**Safe sentence.** "Three Spanish cipher leaves in BnF fr.15575-15576 (f.228, f.233; f.2) each carry a contemporary
interlined decipherment; we applied the period key no.54 (BnF fr.3995, identified by Tomokiyo), which reads its own
glossed control letter fr.3641 f.111r at 237/266 codes, to the first four lines of fr.15575 f.228, where it agrees with
the clerk's gloss on 37/86 codes against a shuffled-key p99 of 0.186 -- short of our pre-registered 0.60 floor; fr.15576
f.2 is in a different 3-digit system."

**Unsafe sentences.** "We deciphered / recovered the plaintext of fr.15575 f.228" (the plaintext is on the leaf; we
checked a key against it, and the gate failed). "First decipherment of these letters" (N0; a period decipherment
exists on each). "fr.15576 f.2 is Ernest's 5 Jan 1595 letter calendared by van Durme" (consistent, unread). "f.228's
gate failed because of the gloss read" (an untested diagnosis).

## 4. Postmortem

No over-claim of novelty found in the target's files: the solvers repeatedly called the work a known-answer test and
a reading aid, which is right. Two wording corrections, made in NOTES.md under "Verifier corrections (VERIFY-NV05)":
(1) f.228 grades are H 77 (key sheet), not S 77; (2) "interlined decipherment over every line" is "over every cipher
line seen at overview resolution", and "a different 3-digit system" is "L01-L04 are outside the no.54 syllabary".
Failure to name: the brief for this audit named the key source `published` for a key that was read off the period
sheet; the rule-10 definition, not the brief, decides the field.

Requests: www.googleapis.com 12 (2 volume-record lookups), archive.org 2. Scratch control script in the verifier's
scratchpad (not committed); its numbers are in the table above.

Desenclos check, 4 Oct 2026 (DESENCLOS-PREMISE, account 3): no hit. Searched 17 open full texts of the 36 items in sources/desenclos/2026-10-04/bibliography.tsv (HAL PDFs, DSpace Tartu HistoCrypt 2024/2025 PDFs, OpenEdition HTML; built from HAL, theses.fr, OpenAlex, Semantic Scholar, CrossRef, Google Books) for this item's shelfmark, sender/recipient, place and date (terms.tsv, search-log.tsv, search.py); none names this item, its key or its plaintext. Not read: her 2014 thesis (theses.fr: not online) and 2017/2021 cryptography chapters (not open; JSTOR-QUEUE rows of 4 Oct 2026).
