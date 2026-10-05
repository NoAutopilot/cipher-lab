# AUDIT 1 (A3V-VNV01, 4 Oct 2026): BnF fr.3993 ff.71v-72r, Charles de Gonzague-Clèves to the duc de Nevers, 2 Aug 1595 (NV-01)

Verifier: A3V-VNV01 (account 3 worker, for LANE-A3V; brief `.claude/briefs/runs/2026-10-04-acct3-a3v-wave2.md`), a session separate
from NV-INTAKE and NV01-READ. Run 03:13-03:18 UTC by `date -u`. Cost: see the lane ledger.

**Claim under audit** (NOTES.md "Status", PROGRESS.tsv row 37): `found-solved` -- a period interlinear decipherment stands above every
cipher line; our key-no.70 decode (H 180 M 1 U 8 of 189 tokens, z 14.4 against 200 shuffled keys) agrees with it; a calibration for
key no.70, not a new reading.

## 1. Extract
- Item: BnF Français 3993 f.71 (dépouillement no.40), cipher on f.71v foot (1 line) and f.72r (~9 digit lines); Gallica
  ark:/12148/btv1b9059229n canvas 81. Sender Charles de Gonzague-Clèves (the duke's son), recipient Louis de Gonzague, duc de Nevers;
  dateline "A 8 heures du soir, 2 aoust 1595"; place not stated in the catalogue (Cambrai context from the sibling f.254).
- Cipher: two-digit substitution with homophones and nulls plus a few nomenclator signs; key fr.3995 f.131r (Tomokiyo's no.70,
  "fol.130"), transcribed by NV01-READ to `keys/key_no70.tsv`.
- Reading (reading_plain.txt), distinctive runs: "gasdes sont venuz advertir", "font amener des gabions entre la porte du mas et le
  ravelin", "la noue [sign] battre demain", "lon sera en danger de perdre".
- What the solvers searched: NV-INTAKE (3 Oct) -- web x4, blog sites x3, Gomberville 1665 (4 Google Books ids, with positive control
  "Rethelois" 3 hits), IA title search, Tomokiyo nevers.htm, DECODE snapshots, Bourdeau, Aymeloglu, Cabinet Noir clones. NV01-READ:
  nothing new.

## 2. Independent search (4 Oct 2026)
**The basis first -- the gloss, by eye.** I viewed `images/crops/c81_72r_block.jpg` (local crop of the native canvas 81) myself. A
second, smaller hand writes one letter above each digit pair on every cipher line of f.72r; legible by eye on line 1:
"g a s d e s s o n t u e n u z a d u e r t i r" over 47 32 83 17 45 82 ... 85 52 75, matching the decode's T1 exactly; on line 3
"b i o n s e n t r e l a p o r t e d u m a s e t l e"; on line 7 "d e p e r d r e ... t o n t". "les" is written over 15 64 38 2[?]
at the top right, and a word ("nomis"/"noins"?) over the line-6 nomenclator sign. So the period decipherment of this very item is on
the leaf. This is the N0 basis, and I confirm it from the image, not only from NOTES.md.

Rule-7 spot check: `python3 tools/decode_key.py ciphers/fr3993-gonzague-nevers-1595 --check` -> "tokens 189: H 180, M 1, U 8 /
reading up to date". No other decoding.

| family | searched | result |
|---|---|---|
| (a) canonical series | BnF *Catalogue général des manuscrits français* (1881), found by phrase search (IA p1cataloguegnr03bibluoft; Google Books HQo4AQAAMAAJ, JUgMAQAAMAAJ) on the dateline "A 8 heures du soir 2 aoust 1595"; dépouillement on disk (sources/bnf-aem/cc504266_francais3974-3995.html) | catalogue entry only: "Lettre, avec chiffre" -- no déchiffrement noted, no text printed. The printed catalogue does not record the interlinear gloss. |
| (b) sender's and recipient's printed correspondence | Recipient: Gomberville, *Mémoires de M. le duc de Nevers* (1665) -- phrase runs through Google Books global search: none of its four volume ids among the hits; my per-volume `id:` filter queries returned errors/0 also on the positive control "Rethelois" (invalid test, logged, not counted); NV-INTAKE's per-volume full-text search with a passing positive control stands. Sender: no printed correspondence of Charles de Gonzague (later Charles I of Mantua) for 1595 located by the global phrase runs or NV-INTAKE's web queries | not found |
| (c) documentary editions | Google Books global phrase search (`print_check.py`): "sont venuz advertir" 18 vols (Bulletin historique et philologique 1888 etc. -- the three words recur in other letters), "font amener des gabions" 93, "entre la porte du mas et le ravelin" 126 (loose matching: Histoire de Chartres, Mas-d'Azil 1625); manual combined queries with `&country=US`: `"la noue" "battre demain" gabions 1595` 0; `"en danger de perdre" gabions ravelin "la noue" 1595` 0; `"sont venuz advertir" gabions` 33, snippets from Michaud-Poujoulat *Nouvelle collection des mémoires* (other text, "gabions" elsewhere) | no print of this letter's text found; the two longest runs failed twice with HTTP 503 in print_check and were re-run as the combined queries above |
| (d) holding archive | BnF dépouillement (on disk) and printed catalogue (above); Gallica item page not re-fetched | catalogued "avec chiffre"; the gloss is visible only on the image |
| (e) full text IA / HathiTrust / Google Books | IA be-api full text, all items, 6 phrases: "sont venuz advertir" 10 items (Bulletin 1888, La Picardie, Archives de la maison d'Orange-Nassau -- generic phrase), dateline 1 item (the BnF catalogue), other 4 phrases 0. HathiTrust full text: unreachable from the cloud (Cloudflare; standing CLAUDE.md finding), not tried | not found |
| (f) solver repositories and cipher blogs | Tomokiyo nevers.htm (local mirror) re-read: lists "Charles Gonzague Cleves to the Duke of Nevers, 2 August 1595 (BnF fr.3993 fol.71)" under no.70, no reading or mention of the gloss; league.htm hits 3993 (other letters). Bourdeau / Aymeloglu / Cabinet Noir / DECODE: NV-INTAKE's clone greps of 3 Oct (HEADs 4aedb40, d2800bb, 47b6db9) and DECODE snapshots accepted, not repeated (same day+1, no new commits checked) | key named by Tomokiyo; no reading |
| (g) scholarship | OpenAlex (keyed) 6 phrases 0; keywords "Charles de Gonzague Nevers 1595 Cambrai" 4 works, "duc de Nevers chiffre lettres 1595" 98 works, top titles unrelated (Desenclos & Lasry 2023 HistoCrypt is a 1592 Henri IV letter, per NV-INTAKE); CrossRef 3 keyword queries, top 5 unrelated; Semantic Scholar: 1 phrase answered (5 unrelated papers), then HTTP 429, stopped (good-citizen rule) -- **partially unreachable**. JSTOR: 2 rows queued (below) | not found |

JSTOR-QUEUE.tsv rows appended (no earlier audit for this item): family (i) `"Charles de Gonzague" AND Nevers AND 1595 AND chiffre`;
family (ii) `"font amener des gabions"`.

Requests by host: be-api.us.archive.org 6; www.googleapis.com 6 (print_check) + 3 (combined) + 24 (per-volume attempt incl. metadata,
invalid) = 33; api.openalex.org 8; api.semanticscholar.org 2 (429); api.crossref.org 3. No Gallica requests. Subagent calls: 0.

## 3. Classification
**NV-01 (fr.3993 ff.71v-72r): N0.**
- Prior plaintext: yes -- the period interlinear decipherment written above every cipher line on the leaf itself (BnF fr.3993 f.72r,
  f.71v foot), seen by eye in this audit. Not in print: no printed text of the letter found (Gomberville 1665, the BnF catalogue,
  global phrase search).
- Prior decipherment: yes, contemporary (on the leaf). Earliest citation: the manuscript itself, 1595; the BnF catalogue (1881) and
  Tomokiyo list the letter (Tomokiyo assigns it to no.70) without noting the decipherment.
- Evidence quality: high (image, legible gloss letters on every line checked agree letter for letter with the key-no.70 decode;
  NV01-READ's gloss agreement 0.685, z 14.4, is limited by the blind reader's misreads of the gloss, not by the key).
- Confidence: high.
- **Key source: period** -- the key no.70 table on fr.3995 f.131r, transcribed by us (NV01-READ); identified as this letter's key by
  Tomokiyo (nevers.htm, credited). `text: known` (on the leaf; not in print).
- **Safe sentence:** "BnF fr.3993 ff.71v-72r (Charles de Gonzague-Clèves to Nevers, 2 Aug 1595) carries its own period interlinear
  decipherment; our application of the period key no.70 (fr.3995 f.131r, identified by Tomokiyo) agrees with it and serves as a
  known-answer check on that key -- N0, no new text."
- **Unsafe sentence:** "We deciphered a previously unread 1595 letter of Charles de Gonzague."

## 4. Postmortem
No over-claim found: NOTES.md ("found-solved ... stands as a known-answer control for key no.70, not a new reading"), PROGRESS.tsv
row 37 note ("calibration, not a new reading") and the NV01-READ section already describe this as N0-shaped. The one failure is
upstream and already corrected by NV01-READ: the intake (NV-INTAKE) called the item `open` from the catalogue's "avec chiffre"
without viewing the image, and the BnF catalogue omits the gloss -- a catalogue "avec chiffre" without "déchiffrement" does not
exclude an interlinear decipherment (LESSONS-worthy; the premise check's image step is what caught it).
Found, not applied: none. NEAR.md: no row for this target. STATUS.md handoffs: not edited (no over-claim). No SECOND-OPINIONS-QUEUE
row (N0, below N3).

## AUDIT 2 (VER1-REG, 5 Oct 2026)

Verifier: VER1-REG (account 2 worker, for LANE-VER1; brief `.claude/briefs/runs/2026-10-05-ytbiz-ver1-jobs.md`), run 18:40-19:0x UTC
by `date -u`; a session separate from A3V-VNV01, NV-INTAKE and NV01-READ. Claim under audit: Audit 1's **N0** (period interlinear
decipherment on the leaf), key `period` (no.70, fr.3995 f.131r, identified by Tomokiyo).

**The basis, checked again by eye.** I viewed `images/crops/c81_72r_block.jpg` myself. A second hand writes one letter above each
digit pair on every cipher line of f.72r: line 1 "g a s d e s s o n t u e n u z a d u e r t i r", line 3 "b i o n s e n t r e l a p o r t
e d u m a s e t l e", line 4 "r a u e l i n l a n o u e ...", the last line "d e p e r d r e ... t o n t"; "les" stands over the top-right
group 15 64 38 2, and "nomis" (or "noins") over the line-6 sign. These agree with reading_plain.txt. The N0 basis holds from the image.
Rule-7 (fresh session): `python3 tools/decode_key.py ciphers/fr3993-gonzague-nevers-1595 --check` -> "tokens 189: H 180, M 1, U 8 /
reading up to date".

| family | searched (5 Oct 2026) | result |
|---|---|---|
| (a)/(d) catalogue | Audit 1's reading of the 1881 *Catalogue général* and the BnF dépouillement accepted (verbatim quotation in NOTES.md) | "Lettre, avec chiffre" only |
| (b) sender/recipient print | Google Books: `Charles de Gonzague Clèves duc de Nevers lettre 2 août 1595` 26 vols, top 10: the 1881/1895 BnF catalogues and biographical dictionaries, no letter text | not found |
| (c)/(e) phrase search | IA be-api fts, all items: `"porte du mas" ravelin Cambray 1595` 0; `"la noue" "battre demain"` 22 (other texts: Orange-Nassau *Werken*, Granvelle correspondence, 19th-c. memoirs; none this letter); `"en danger de perdre" gabions ravelin` 202 loose (Castelnau mémoires etc.). Google Books: `"porte du mas" Cambray 1595` 17 loose (Ruiz Ibáñez, *Felipe II y Cambrai* 1999, the 1595 Cambrai siege study, snippet unrelated); `"amener des gabions" "porte du" ravelin 1595 Cambray` 0 | not found |
| (f) solver repos | fresh clones (cyphersolver a439937, 3 Oct; unsolved-ciphers d2800bb, 27 Sept): grep 3993 / fr3993 / nevers1595 / "gonzague.*1595" -> only Bourdeau's mirrors of Tomokiyo nevers.htm / league.htm and a BnF notice harvest; no reading or gloss note for f.71-72 | key named by Tomokiyo; no reading |
| (g) scholarship | OpenAlex (key) 2 queries, top hits unrelated (Savoy diplomacy, 1618-21 militia); HAL `"Charles de Gonzague" AND 1595 AND chiffre` 0. JSTOR: both Audit 1 rows answered (no relevant hit / no hits); no new row needed | not found |
| unreachable | HathiTrust full text (cloud); Ruiz Ibáñez 1999 full text | -- |

Requests: be-api.us.archive.org 3, www.googleapis.com 3, api.openalex.org 2, api.archives-ouvertes.fr 1, github.com (clones shared with
the Janssens audit). Subagent calls 0.

### Classification (Audit 2)

**NV-01 (fr.3993 ff.71v-72r): N0 -- Audit 1 endorsed.** Prior plaintext and prior decipherment: the contemporary interlinear gloss on
the leaf (seen by eye in both audits); no print of the text located. Key source **period** (key no.70, transcribed by us, identified by
Tomokiyo, credited). `text: known` (on the leaf).

**Depth (rule 4a): D3, 95.2%** of tokens H (180 of 189; M 1 = a nomenclator sign read "vous"; U 8 = six nomenclator/roman signs plus
two two-digit "15" groups outside the key). External check non-statistical: the period gloss, letter for letter on every line checked;
fresh rule-7 check passes. Not D4: the two numeric U tokens are cipher-letter groups, not name codes. Depth sentence (true, specific,
from the gloss): the writer reports that scouts ("gasdes") have come to warn that gabions are being brought up "entre la porte du mas et
le ravelin", with "la noue ... battre demain" and "lon sera en danger de perdre" following. Outward words: "largely deciphered (about 95%)" -- by the period gloss
and period key; the safe sentence of Audit 1 governs (N0, no new text).

### Postmortem
No over-claim found (NOTES.md "found-solved", PROGRESS.tsv note "calibration, not a new reading"). Register gap, not a claim: status.json
has no target or result row for `fr3993-gonzague-nevers-1595` (only a link to `fr3993-villeroy-1595`), so the depth fields are recorded
here and in PROGRESS.tsv; the lane orchestrator adds the row (a verifier does not create board rows). No SECOND-OPINIONS-QUEUE row (N0).

`python3 tools/depth_check.py` (5 Oct 2026, after this audit; neither item is a counted result, N0/N1): `unique solves (N3+ and D2+): 16 -- D4 1, D3 2, D2 13; not counted D0/D1: 13; legacy ungraded: 0 exit 0`
