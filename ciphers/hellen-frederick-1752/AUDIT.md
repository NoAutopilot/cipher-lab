# AUDIT: hellen-frederick-1752, R1953 (Hellen, The Hague, to Frederick II, 4 Jan 1752) partial reading under DECODE R4369

Verifier NEAR3-VHEL (account 2, for LANE-NEAR3), 4 Oct 2026, 01:51-02:1x UTC (clock read with `date -u`). Brief
`.claude/briefs/runs/2026-10-04-ytbiz-near3-verifier-hellen.md`. This session took no part in any solver pass on this
target. It did not decode, did not touch the key or the reading, and did not log in to DECODE. Levels are those of
CLAUDE.md rule 10.

Claim under audit (NOTES.md "READ2-HEL", NEAR.md row): R1953 read with DECODE R4369 (BL Add MS 32276 f.44, "Hellen avec
le Roy de Prusse", 1751, codes 801-1796): H 152, S 304, M 16, U 374 of 846 tokens. The right-hand entries are attributed
to code+100 (LR100), and that attribution beats its value-shuffle and order-shuffle controls (p 0/200, power 1.00). Judge
FAIL near the gate ("cannot decide" at this coverage). Rule-7 re-derivation 845/846, and the one difference is a `~`
convention, now stated in key_r4369/README.md. R4370 (READ2-HEL2) and R4372 (NEAR3-HEL4) were tested as the codes 1-800
half and both FAIL.

## 1. Verdict

| item | prior plaintext | prior decipherment of this item | key source | class |
|---|---|---|---|---|
| R1953, Hellen to Frederick II, The Hague, 4 Jan 1752 (DECODE R1953; KHA Prins Willem V inv. 196, now A31-1148) | **none found** in print (Politische Correspondenz vol. 9, Preussische Staatsschriften, BL/TNA catalogues, De Leeuw 2000, Google Books, IA, OpenAlex, CrossRef, HAL) | **none located.** Period decipherments of Hellen's letters exist for 30 Oct-28 Dec 1751 (NA Fagel 1.10.29 inv. 5177, English Black Chamber copies, Lyonet's fills) and from 24 Oct 1752 (inv. 5206), but neither volume holds a Hellen letter dated between 28 Dec 1751 and Sept 1752 (section 3e). The receiving-side decipherment (GStA PK) and any English decypher outside the Fagel copies were not reachable item by item. | `period` (R4369 is a period key sheet; we transcribed it and chose the right-entry attribution by a controlled test) | **N3** |

What the reading is. It is a partial reading. 456 of 846 tokens (53.9%) carry a key value: H 152 (18.0%) read straight
from the sheet, and S 304 (35.9%) whose value comes from the sheet but whose code was assigned by the control-backed
LR100 attribution. M 16 (1.9%). U 374 (44.2%) are codes 1-800, which are not on R4369, plus 14 blank cells. No token
is C, so this is a **period-key result with a cryptanalytic attribution step**, not a key-source reading of the whole
letter. The decoded spans are fragments: syllables and words between unread codes ("si feu pce d'Orange a [643] un ...",
"a re ie t te [324] la proposition d une nouvelle", "de re nouvelle r le [373] [46] traite"). No continuous sentence of the
letter can be given. The ciphertext is DECODE's transcription, not the image (rule 2). Rule 7: `tools/decode_key.py
ciphers/hellen-frederick-1752/key_r4369 --check` passes ("reading up to date"; re-run by this verifier, 846 tokens, H 152
M 16 S 304 U 374).

Evidence quality: good for the attribution (two statistics, two controls, a positive control with power 1.00, a second
seed, and the other seven letters as negatives). It is weak for content: the judge cannot decide at this coverage, and
the transcription error of the key is measured only as reader agreement (err_2reader 4.8%; err_true is not measurable).
Confidence that R4369 is the key for R1953's codes 801-1796: high. Confidence in any sentence-level sense of the letter:
low, because 44% of the tokens are unread.

**Safe sentence:** "Using a period key sheet in the British Library (Add MS 32276 f.44, catalogued on DECODE as R4369), we
assigned values to 456 of the 846 code groups (54%) of Hellen's 4 January 1752 despatch to Frederick II (DECODE R1953).
152 of them come straight from the sheet; for 304 we decided which code each sheet entry belongs to with a controlled
statistical test. Codes 1-800 are not on that sheet and remain unread. In the editions, catalogues and decipherment
volumes we searched (log in AUDIT.md) we found no printed plaintext or period decipherment of this despatch; the
recipient's archive in Berlin has not been searched."

**Unsafe sentence:** "We have deciphered Hellen's 4 January 1752 despatch for the first time." (Unsafe on three counts:
44% of the letter is unread; a period decipherment may survive in GStA PK or in English decypher series not searched
item by item; rule 10 permits "first" only at N4/N5 and only with the qualifier.)

Why N3 and not N4: the principal *editions* are covered (Politische Correspondenz, Preussische Staatsschriften), and so
are the obvious *decipherment volumes* (Fagel 5177 and 5206). But two holdings where a decipherment of this very letter
would most likely sit were not covered item by item. (1) The recipient's own deciphered original or Eichel's extract in
GStA PK (I. HA, Hellen's Hague reports). No online finding aid was reached. A 2025 Saint-Germain edition prints other
Hellen reports from GStA (Premise check (d)), so decoded receiving-side copies of his reports exist and some are in print.
(2) The English Black Chamber's own decyphers for January 1752 (TNA SP 107 / SP 84, BL Newcastle papers): catalogue
keyword searches found no item, and those series are not itemised by sender in the online catalogues. The JSTOR rows are
queued (section 3g) and do not block the class.

## 2. Extracted from the repo

- Date, place: The Hague, 4 Jan 1752 (DECODE date). Sender W. B. (Bruno) von der Hellen, Prussian secretary of legation /
  chargé d'affaires. Recipient Frederick II.
- Identifiers: DECODE R1953 (ciphertext record, "Non-decrypted"); KHA Prins Willem V inv. 196 (now A31-1148, "Briefwisseling
  van de zaakgelastigde W.B. von der Hellen, 1751-1757 en 1763", not digitised); key DECODE R4369 = BL Add MS 32276 f.44.
- Ciphertext: `ciphertext_R1953.txt` (846 segments, numeric codes 8-1732), taken from Bourdeau's audited transcription
  (CC BY 4.0).
- Plaintext as read: `key_r4369/reading_R1953.txt` (tokens graded in `reading_R1953_tokens.tsv`).
- Distinctive runs (H/S words, joined where the decode splits syllables), as put in `phrases.txt`: "si feu prince d'Orange";
  "a rejette la proposition d'une nouvelle"; "de renouveller le traite"; "sur les ex[...]tations de S.M."; "le prince Lou[is]";
  "qu'il se fla[tt]oit toujours"; "des troupes"; "le commerce ... d'Ostende"; "princesse d'Orange". The letter also carries
  a duplicated three-line passage that Bourdeau checked on the manuscript (the run "et quoique sur les ex... traite et 2
  [247] er [405] l a contre" appears twice in the decode, as expected).
- What the solvers searched (all in NOTES.md): Politische Correspondenz vols. 9-10 (archive.org be-api full text plus djvu
  read, 24-25 Sept 2026), vols. 13 and 23 (25 Sept); NA Fagel inv. 5206 page by page (25 Sept: it starts 24 Oct 1752);
  six-source check (24 Sept: Bourdeau page, DECODE listing, Aymeloglu, Cryptiana `dutch.htm`, web); web and blog check
  (1 Oct: 8 web queries, Cipherbrain, Cryptiana, Cipher Mysteries, De Leeuw 1995 DBNL, De Leeuw 2000 chapter on 1707-15
  only, Thomassen 2009, Klawitter 2026); Bourdeau solver-repo diff (2 Oct); premise check (2 Oct: KHA catalogue, DECODE
  neighbours R1050/R1051, Google Books 3 queries, OpenAlex 1).

## 3. Independent search (4 Oct 2026), by family

**(a) Canonical series, Frederick's side: searched.** Politische Correspondenz vol. 9 (archive.org `politischecorres09fred`,
djvu.txt fetched once and grepped): 46 "Hellen" lines. Frederick's replies of 8 Jan 1752 (no. 5273, to Hellen's report of
31 Dec 1751) and 22 Jan 1752 (no. 5291, to his reports of 11 and 14 Jan) are printed. **No printed reply acknowledges a
report of 4 Jan**, and no editorial footnote quotes or summarises it. A grep for "du 4", "4 janvier", "4. Januar" and
"4 de ce mois" found no Hellen context. The 22 Jan reply asks "à combien ira la réduction des troupes qu'on proposera",
which is the topic of R1953's decoded "des troupes" spans: context, not plaintext. The phrase "le prince Louis [de
Brunswick]" occurs in a later 1752 reply "selon vos rapports" (line 9569, after Feb 1752), again context only.
*Preussische Staatsschriften* (Google Books snippet, 1885 and 2025 eds.): prints Hellen's **memorial of 6 Jan 1752** to the
States General (a public document, not the despatch).

**(b) Sender's and recipient's correspondence; the English and Dutch sides: searched.**
- **De Leeuw 2000, *Cryptology and statecraft in the Dutch Republic* (UvA thesis), all 15 chapter PDFs** (dare.uva.nl
  record 2d5163aa..., pure.uva.nl files 3074959-3074987, text extracted locally). "Hellen" occurs only in ch. 6 (3x) and
  ch. 8 (15x, "The Black Chamber in the Dutch Republic and the Seven Years' War"; also printed in *Diplomacy & Statecraft*).
  Chapter 8 states: the Dutch began intercepting Hellen's mail in Nov 1751; the code they had bought (D'Ammon's) did not fit;
  the intercepts were sent to London and deciphered there; **NA Fagel inv. 5177** holds the copies ("the first 14 items ...
  all written by or to De Hellen between 30 October and 30 November 1751, bear the remark 'Deciphered' ... the other 19 ...
  between November and December 1751"; n.32); the London solutions "were not complete; in every letter several words were
  left out and Lyonet started by filling in the blanks" (n.45, inv. 5177); Lyonet finished Hellen's and Michell's codes about
  March 1753; and in spring 1757 the codes changed and neither Lyonet nor London broke them. **No decipherment or plaintext
  of the 4 Jan 1752 despatch is quoted.** Earlier passes read only the 1707-1715 chapter.
- **BL catalogue** (searcharchives.bl.uk JSON, "Hellen" 34 hits, "Hellen Prussia" 13): Add MS 32833 f.119 (Newcastle papers,
  Jan-14 Feb 1752) is "B- de Hellen ... Memorial to the States General: 1752"; Add MS 15873 f.17 is a copy of his memorial of
  4 Nov 1751; Egerton MS 3446 ff. 9, 12b hold copies of Hellen's letters to Frederick II **of 1754** (Yorke-Holdernesse);
  Add MS 6844 has a 1756 "Precis of Mons. Hellen's report" (Mitchell papers). No 1752 Hellen despatch or decypher is catalogued.
- **TNA Discovery API** ("Hellen Prussia", "Hellen decypher", "Hellen Hague 1752", "decyphers Prussian", "intercepted Prussian
  1752", "Hellen"): no State Papers item. The date filter was ignored by the API; the 27 "Hellen" hits are unrelated people
  and places.
- GStA PK (Hellen's reports, the recipient's originals): **unreachable** this pass (no online finding aid reached; not tried
  beyond the Google Books snippet already in the Premise check).

**(c) Documentary editions for the period: searched (by Google Books).** `"Hellen" "4 janvier 1752"` (45 volumes: only PC vol.
9 replies, the *Nederlandsche jaerboeken* memorial of 4 Nov 1751, and unrelated hits); `"von der Hellen" 1752 Bericht Haag
Januar` (8: PC, Preussische Staatsschriften); `"Hellen" Haye 1752 déchiffré OR dechiffre` (0); `"Hellen" decypher OR
decyphered Prussian 1752` (0); `"von der Hellen" Friedrich chiffre entziffert Haag` (0); `"Hellen" "Deciphering Branch"` (10,
all false). Recueil des instructions (Prusse) and the Willem IV/Anna van Hannover correspondence were not searched by title.

**(d) Holding archive and project pages: searched.** DECODE listing on disk (`sources/decode/`): R1953 "Non-decrypted", no
attached decipherment. Not logged in (brief). KHA A31-1148: not digitised (Premise check). **NA Fagel 1.10.29 inv. 5177**
("1751-1752", DIGITALIZED, 187 scans; inv. 5178 = 1753, 5179/5180 = 1754, 5181 = 1755): manifest read from the item page.
Header strips were read at full resolution for scans 1, 30, 60, 64, 70, 76, 82, every scan 88-106, 120, 150, 175 and 187
(three montage reads by this verifier). The sequence is chronological:
scan 70 "No 30, à la Haye le 3 Decembre 1751"; scan 88 "No 35, du 21 Decemb. 1751, Lettre du Sr H."; scan 91 and 92
replies "Au Sr de H." of 24 and 22 Dec 1751; scan 93 "No 36, du 24 Decemb. 1751"; **scan 89 "No 37, du 28 Decemb. 1751,
Lettre du Sr H."**; scans 95-101 letters to and from Michell (London), including Frederick to Michell of 25 Dec 1751, with cipher
groups; scan 102 "Lettre du Sr Cauderbach du 5 Septembre 1752"; scans 106 and 120 "Lettre du Sr de Hellen" of 8 and 13 Sept
1752; scan 175 a Hellen letter of October 1752. So **inv. 5177 has no Hellen letter between 28 Dec 1751 and 8 Sept 1752,
and the 4 Jan 1752 despatch is not in it.** This is a header sample: the body pages between the headers were not read, and
a misfiled item inside a body run cannot be excluded. Inv. 5206 starts 24 Oct 1752 (25 Sept pass). The gap from Jan to Aug
1752 in both Fagel series fits De Leeuw's account (Hellen's code changed, and the London solutions arrived incomplete) but
does not prove it.

**(e) Full text: searched.** `tools/print_check.py ciphers/hellen-frederick-1752` with the new `phrases.txt` (7 phrases) and
`sources.tsv` (PC vols. 9-10, OpenAlex and CrossRef keywords): 50 rows, 21 with hits. All hits are PC context (the
"réduction des troupes" and "prince Louis" replies above) or generic phrase hits in unrelated books (ia-global, Google Books,
OpenAlex). No hit is a print of this letter. Output: `print-check.tsv`, `print-check-hosts.tsv`. IA advancedsearch
`"von der Hellen" AND (Haye OR Haag)`: 0. be-api full text `"Hellen" "4 janvier 1752"`: only Frederick II creator buckets
(PC). HathiTrust: not used (HTRC EF gives no phrase search; the PC volumes are already read in full text on IA).

**(f) Solver repositories and cipher blogs: searched.** dbourdeau/cyphersolver fresh shallow clone (HEAD a439937, 3 Oct 2026):
`targets/hellen1752` last changed 3 Oct 2026, "Status: in progress. No cipher plaintext or key has been verified"; no file
mentions R4369 or Add MS 32276. aaymeloglu/unsolved-ciphers (HEAD d2800bb, 27 Sept 2026): "Hellen" only in the DECODE
catalogue scrape. Blogs (Cipherbrain, Cryptiana, Cipher Mysteries) were covered on 1 Oct (WEBCHECK) and not repeated.

**(g) Scholarship: searched, one index blocked.** OpenAlex (keyed): `"von der Hellen" Prussian Hague` (1, unrelated), `Prussian
diplomatic cipher Frederick the Great intercepted Hague 1752` (2, unrelated), `Lyonet black chamber Dutch Republic Prussian
cipher` (0), `de Leeuw cryptology Dutch Republic eighteenth century` (7: De Leeuw's thesis review, BMGN 2002, nothing on
Hellen's text), `Deciphering Branch eighteenth century Willes intercepted Prussian` (29, unrelated); plus print_check's 9.
CrossRef (4, via print_check): no item on Hellen's despatches. HAL: `"von der Hellen"` 0, `Lyonet chiffre Prusse` 0. Semantic
Scholar: keyed search `Hellen Prussian Hague 1752 intercepted letters` 0 results (HTTP 200); print_check's own S2 pass hit a
429 on its first call and stopped (logged in print-check-hosts.tsv). JSTOR: four rows appended to `JSTOR-QUEUE.tsv`, two
in family (i) and two in family (ii) (bare phrase, no cipher keyword). Queued; they do not block this class.

Requests (one at a time, at least 1.5 s apart): archive.org 4, be-api.us.archive.org 8, www.googleapis.com 13,
api.openalex.org 14, api.semanticscholar.org 2 (one 429), api.crossref.org 4, api.archives-ouvertes.fr 2,
discovery.nationalarchives.gov.uk 6, searcharchives.bl.uk 15, dare.uva.nl 1, pure.uva.nl 15, www.nationaalarchief.nl 5,
service.archief.nl 22 full-size scans, github.com 2 shallow clones, web search 1. No DECODE request. No 403, challenge or
repeated 429.

## 4. Postmortem

The over-claim risk on this target is low. No file calls the reading new, first, solved or unpublished, and the NEAR.md
row and the STATUS.md READ2 handoff say "partial", "period-key result" and "nothing verified". Corrections made this pass:

1. NOTES.md line 120 (24 Sept check-solved): "this worker is the first to open the NA viewer for it" is a claim about
   the world that the worker could not check. Reworded to "no earlier pass in this repository had opened the NA viewer
   for it".
2. NOTES.md, 25 Sept Fagel 5206 section: the explanation "this Fagel decrypted-letters series for Hellen only begins once his
   traffic started being broken" is contradicted by De Leeuw 2000 ch. 8 n.32: English-deciphered copies of Hellen's letters
   from 30 Oct 1751 are in inv. 5177. An annotation now points to section 3d here. The 5206 finding itself (the volume starts
   24 Oct 1752) stands.
3. The Premise check (2 Oct) named NA Fagel inv. 5206 as the "decipherments the folder itself mentions" but never inv. 5177,
   the volume De Leeuw names for Hellen's 1751-52 decipherments. This is now covered (section 3d). It is a search gap, not
   an over-claim.
4. "English Deciphering Branch's key" (NEAR.md, STATUS.md) rests on the BL volume's provenance (Add MS 32276 is a volume of
   the Deciphering Branch's key sheets) as DECODE catalogues it. That attribution is reasonable, but it is DECODE's and the
   BL's, and it is now cited as such in the safe sentence.

Nothing in the reading changed, so there is nothing to propagate into a SECOND-OPINIONS row beyond the new one filed here.

## 5. Leads for the solver lane (not run; one-line suggestions, Usage 7)

- NA Fagel inv. 5177 holds English/Lyonet decipherments in clear of Hellen's letters Nos. ~1-37 (30 Oct-28 Dec 1751), the
  letters just before R1953 (probably No. 38 or 39). If any of their cipher originals survive (KHA A31-1148, not digitised;
  DECODE records of inv. 196 dated 1751?), they are a known-plaintext source for the same code's codes 1-800. Even without
  them, the clear texts are period-, topic- and writer-matched context (troop reduction, Austrian Netherlands commerce, the
  Princess Governess) for a cribbed rebuild of codes 1-800. Cost: one contact sheet of scans 2-93 first (~$3), then a
  pre-registered test.
- GStA PK, I. HA (Hellen's Hague reports, 1752): the recipient's deciphered original. An archive request (REQUEST.md, owner
  side) would settle the prior-decipherment question and supply a full plaintext.

# AUDIT 2 (A3V-VHEL2, 4 Oct 2026): R1953, Hellen to Frederick II, The Hague, 4 Jan 1752 -- second adversarial audit

Verifier A3V-VHEL2 (account 3 worker, for LANE-A3V), 4 Oct 2026, 02:53-03:3x UTC (clock read with `date -u`). Brief
`.claude/briefs/runs/2026-10-04-acct3-a3v-wave1.md`, job A3V-VHEL2. This session took no part in any solver pass on this target
and is not the session that wrote AUDIT 1 (NEAR3-VHEL). It did not decode, did not touch key, ciphertext or reading, did not log
in to DECODE, and used no subagents. Rule 10 levels.

Claim under audit: AUDIT 1's class **N3, key source period**, for the R1953 partial reading under DECODE R4369 (H 152, S 304,
M 16, U 374 of 846 tokens; codes 1-800 unread). The brief asked this audit to be adversarial where AUDIT 1 was thin: the Fagel
volume it found (inv. 5177), the Berlin receiving side, Politische Correspondenz read by phrase rather than by date, the English
decypher side, and scholarship beyond De Leeuw 2000.

## A2.1 Verdict

| item | prior plaintext | prior decipherment of this item | key source | class |
|---|---|---|---|---|
| R1953, Hellen to Frederick II, The Hague, 4 Jan 1752 | **none located** (PC vol. 9 by phrase and by date; Droysen, *Geschichte der preussischen Politik* V.4 (1886); Ring, *Asiatische Handlungscompagnien Friedrichs des Grossen* (1890); Preussische Staatsschriften via AUDIT 1; Google Books, OpenAlex, S2, CrossRef, HAL) | **none located; two holdings likely to contain one are now identified and unread**: GStA PK, I. HA Rep. 96 Nr. 38 G and Nr. 38 H (the King's Cabinet file of Hellen's correspondence, 1752; not digitised, not itemised online), and the Dutch/English decipherments of Hellen's Jan-Aug 1752 letters, which are numbered in the interceptors' own 1752 series but are in neither Fagel 5177 nor 5206 (A2.3a) | `period` (unchanged: R4369 is a period key sheet, transcribed by us; right-entry attribution by our controlled test) | **N3 confirmed** -- neither raised nor lowered |

Why not N4. N4 needs the principal editions, catalogues and project pages covered. The editions are now covered more widely than
in AUDIT 1 (Droysen and Ring added; neither prints or cites a report of 4 Jan 1752). But the two places where a period
decipherment of this very despatch most probably survives are now pinned to shelfmark level and could not be read: (1) the
recipient's file, GStA PK I. HA Rep. 96 Nr. 38 G / 38 H, where Hellen's enciphered reports would have been deciphered on
arrival for the King (Droysen cites Hellen's reports of 18 Jan, 17 Mar, 28 Apr, 11 Aug and 22 Dec 1752 from the Berlin
archive, so the 1752 run survived into the 1880s); (2) the interceptors' series for 1752, whose numbering shows that roughly
seventy items were numbered before 5 Sept 1752 that are not in the Fagel registers (A2.3a). Calling this "no prior
decipherment located" at N4 would claim coverage of the one archive (Berlin) most likely to hold one. N3 stands.

Why not lower. Nothing found prints or deciphers the 4 Jan 1752 despatch. Every hit is context (topics Frederick or Droysen
mention from neighbouring reports: Ostend commerce, troop reduction, the late Prince of Orange, Prince Louis of Brunswick),
consistent with the decoded fragments but not a plaintext of them.

Key source: `period` -- agreed with AUDIT 1. BL catalogue (searcharchives.bl.uk, 4 Oct 2026) describes Add MS 32276 only as
"Vol. vi. (ff. 128) Cipher-keys", 1724-1844; the attribution of the volume to the English Deciphering Branch rests on the
series it belongs to and on DECODE's record, as AUDIT 1 said.

**Safe sentence (revises AUDIT 1's last clause; the rest stands):** "Using a period key sheet in the British Library (Add MS 32276
f.44, catalogued on DECODE as R4369), we assigned values to 456 of the 846 code groups (54%) of Hellen's 4 January 1752
despatch to Frederick II (DECODE R1953). 152 come straight from the sheet; for 304 we decided which code each sheet entry
belongs to with a controlled statistical test. Codes 1-800 are not on that sheet and remain unread. In the editions,
catalogues and decipherment volumes we searched (log in AUDIT.md) we found no printed plaintext or period decipherment of
this despatch. The King's own file of Hellen's 1752 reports in Berlin (GStA PK, I. HA Rep. 96 Nr. 38 G-H) is not digitised
and was not read, and it may hold the decipherment made on arrival."

**Unsafe sentence:** "No decipherment of Hellen's 4 January 1752 despatch exists" (or any "first"/"previously unread" form).
Unsafe because the Berlin file and the interceptors' Jan-Aug 1752 decipherments are unaccounted for, and because 44% of the
letter is unread.

## A2.2 Extracted (checked against AUDIT 1, not repeated)

AUDIT 1 section 2 re-checked against the folder: identifiers (DECODE R1953; KHA Prins Willem V inv. 196 / A31-1148; key
R4369 = Add MS 32276 f.44), counts (846 tokens, H 152 S 304 M 16 U 374) and `phrases.txt` (7 phrases) agree with the files on
disk. Not re-run: `decode_key.py --check` (AUDIT 1 ran it today; no reading commit since).

## A2.3 Independent search, by family (4 Oct 2026)

**(a) Holding / decipherment archive, Dutch side: NA Fagel 1.10.29 -- searched, a numbering gap found.**
- Finding aid read in full (EAD download, one request, `www.nationaalarchief.nl/onderzoeken/archief/1.10.29/download/xml`,
  6,182 components; parsed locally for Hellen / ontcijfer / dechiffr / Pruis). The only decipherment series are section
  "Ontcijferde brieven van vreemde gezanten aan hun regeringen": **inv. 5177-5203** "Registers van ontcijferde brieven ...
  1751-1767" (5177 = 1751-1752, 5178 = 1753, then 1754 onwards; no other volume dated 1752) and **inv. 5204-5208**
  "Afschriften ... bestemd voor de griffier Hendrik Fagel de Oude, 1751-1753" (5204 Bonnac, 5205 Elsacker, **5206 Hellen
  1752-1753**, 5207 Kauderbach, 5208 Maltzahn 1751-1753). Later Prussian runs (5224-5265) are 1780-1788. Elsewhere in the aid,
  Hellen's name occurs nowhere in a unit title. **So no Fagel volume besides 5177 and 5206 can hold a 1752 Hellen decipherment.**
- Inv. 5177, 187 scans (manifest from the item page's drupal-settings-json, one request). AUDIT 1 read headers of ~30 scans;
  this audit read the top 30% of 20 further scans through the IIIF image API (`.../pct:0,0,100,30/1100,/0/default.jpg`): 108,
  111, 114, 117, 123, 127, 131, 135, 139, 143, 146, 154, 158, 162, 166, 170, 178, 182, 185, 186. Findings:
  - **scan 108: "No 71. du 5 Septemb. 1752. Lettre du Sr de Hellen. Sire, La dépêche de V.M. du 29 Août m'est bien
    parvenue."** The register's 1752 numbering is therefore already at **No 71** on 5 Sept 1752 (inv. 5206 continues the same
    count: No 83 on 24 Oct, No 98 on 8 Dec 1752, then resets to a 1753 series). The 1751 run in 5177 is Nos 1-37 (30 Oct-28 Dec
    1751). Either the 1752 count started afresh in January (Nos 1-70 for Jan-early Sept) or it continued from 1751 (Nos 38-70);
    on either reading, **some 33-70 numbered intercepts of Jan-Aug 1752 are in neither 5177 nor 5206.** At the autumn 1752
    rate in 5206 (about two items a week), counting back from No 71 lands near the start of January 1752, which favours a fresh
    January count -- an estimate, not a finding. What the counter numbers (Hellen's letters only, or every intercepted item
    to and from him) is not established; 5177's 1751 run mixes letters from Hellen and replies to him.
  - scan 111: "Copie d'une Lettre du Sr de Hellen à Mr Eversman Secretaire Privé et Maître des Postes du Roi à Emmerick, à la
    Haye ce 12 Sept. 1752" -- a letter to the Prussian postmaster, not a report to the King.
  - scans 114, 117, 123, 178: continuation pages (French clear text; 117 on Ostend and the Bruges canal, 123 a verse satire
    and Paris Parlement news); no header.
  - scans 127, 131, 135, 139, 143, 146, 154, 158, 162, 166, 170, 185, 186: blank leaves (some with show-through).
  - Correction to AUDIT 1 section 3d: the sequence is not strictly chronological (scan 89 is No 37 of 28 Dec, scan 93 No 36
    of 24 Dec), and the 1752 entries begin with No 71, not with a first 1752 letter; neither changes AUDIT 1's conclusion that
    the 4 Jan 1752 despatch is not in 5177. About 140 of 187 scans have now been header-read or seen blank across both audits;
    the rest are body pages.
- Where the missing Jan-Aug 1752 items went is not known. De Leeuw 2000 ch. 8 (read by AUDIT 1) says the intercepts were sent
  to London and that the London solutions came back incomplete; the KHA (Prins Willem V inv. 196 / A31-1148, where R1953 itself
  sits) is the other candidate. Neither is online.

**(b) Recipient's side, Berlin: GStA PK -- searched to shelfmark level; contents unreachable.**
- Archivportal-D (www.archivportal-d.de, Anubis-protected; curl got the challenge page, one `tools/browser_fetch.js` load of the
  search and one of each item page passed it): query `Hellen Haag` returns the Cabinet series **GStA PK, I. HA Rep. 96 (Geheimes
  Kabinett), 03.01.02.18 Niederlande, Generalstaaten: "Schriftwechsel mit dem preußischen Geschäftsträger (Chargé d'Affaires)
  Bruno von der Hellen in Den Haag"** -- Nr. 38 F (Sep.-Dez. 1751), **Nr. 38 G (1752), Nr. 38 H (1752)**, 38 J (1753), 38 K (1754),
  38 L-M (1755), 38 N-O (1756), 39 A-B (1757), 39 C (1758), 39 D (1759), 39 E (1760), 39 F (1761), 39 G (1762), 39 H (1763).
  Item records for 38 G and 38 H (Archivportal-D ids CIGZWUN2DTINPHFLQH32LNYXV6UTZSNM, 62LFHYY5UFN2ID56EFCPQXZL4SE6W2QE;
  last updated 20 Aug 2025): Laufzeit 1752, no Digitalisat, no "Enthält" note. The GStA's own MidosaSEARCH class page
  (`archivdatenbank.gsta.spk-berlin.de/.../xml/inhalt/GStA_i_ha_rep_96_und_96_a_3_1_2_18.htm`, one request) gives the same titles
  and dates and no item list. The legation's own archive, I. HA Rep. 81 Gesandtschaft Den Haag, has a Laufzeit of "1648-1740,
  1766, 1800-1883" -- no 1752 files. Further Hellen hits (I. HA GR Rep. 41 Nr. 849, 861; Rep. 63 Nr. 1236) are 1756-1762.
- DDB API: `DDB_API_KEY` unset in this container; keyless Archivportal-D/DDB HTML used instead (logged).
- Conclusion for the class: the King's file for 1752 exists, is identified, and is not readable from here. A deciphered copy
  (or interlinear decipherment) of R1953 would be expected in Nr. 38 G (Jan-mid 1752 by its position). This is the step that
  would move the class (an archive request, owner side) -- see A2.5.

**(c) Canonical edition, read by phrase: Politische Correspondenz vol. 9 -- searched.** archive.org `politischecorres09fred`
djvu text (one request), whitespace-normalised, grepped for the decoded runs: "proposition d'une nouvelle" 0; "renouveller /
renouveler le traité" 0; "feu prince d'Orange" 0; "se flattoit toujours" 0; "Ostende" 0; "réduction des troupes" 2 (no. 5331,
15 Feb 1752, and line 12173, later); "prince Louis" 11 (first at line 9569, after Feb 1752). Hellen headings in Jan-Feb 1752:
no. 5273 (8 Jan, answers the report of 31 Dec 1751: Zeeland's complaints about Brussels' "vexations" against Dutch commerce in
the Austrian Netherlands), no. 5291 (22 Jan, answers the reports of 11 and 14 Jan: "à combien ira la réduction des troupes"),
no. 5311 (8 Feb, answers 1 Feb: Emden company), no. 5331 (15 Feb, answers 8 Feb: the Gouvernante's authority and the troop
reduction). **No printed reply acknowledges a report of 4 Jan 1752.** Two of R1953's decoded topics (Austrian Netherlands /
Ostend commerce; troop reduction) are the topics of the neighbouring replies -- context that fits the date, not plaintext. (My
first, un-normalised grep returned 0 for "prince Louis"; the djvu text has double spaces. AUDIT 1's line 9569 is correct.)

**(d) Documentary history drawing on the Berlin file: searched (new family).**
- **J. G. Droysen, *Geschichte der preussischen Politik*, Th. V Bd. 4 (Friedrich der Grosse, 1886)**, archive.org
  `droysen-geschichte-der-preussischen-politik-v-5-no-4` (found by be-api full-text search on "Compagnie von Ostende meldet
  Hellen"; djvu text, one request; long s normalised). 19 "Hellen" lines. Citations of Hellen's Hague reports: 22 Oct 1751
  (quoted in French, on the late Prince of Orange: "il ne sera guère regretté ... il marchoit à grands pas vers la
  souveraineté"), **18 Jan 1752** ("Über den Handel von Ostende und Texel"), 17 Mar 1752 (with Eichel's minute of the King's
  oral resolution), 28 Apr 1752 (quoted: Austrian Netherlands works "au préjudice du commerce de la République"), 11 Aug 1752
  (quoted: the Ostend company), 22 Dec 1752, 2 Jan 1753, and later years. **No citation or quotation of a report of 4 Jan 1752.**
  Phrase grep (normalised): none of the decoded runs occurs.
- **Ring, *Asiatische Handlungscompagnien Friedrichs des Grossen* (1890)**, archive.org `asiatischehandl00ringgoog` (one
  request): cites Hellen to the King of 9 and 26 Nov 1751, the King to Hellen of 22 Jan, 8 Feb and 24 Mar 1752 (from PC), and
  1755-1757 letters, from GStA Rep. 96 Kabinettsakten. No 4 Jan 1752 report.

**(e) English decypher side: searched by catalogue; not itemised.**
- TNA Discovery API (11 queries; `sps.recordSeries` filter returned 0 for every query and appears not to be honoured, so
  keyword + date queries were used): "decyphers" 1750-1755 -> SP 106/42 (cipher sheets "For Decyphering, numbers 1-1800", 18th
  century, undescribed by holder) and SP 36/131/1/32 (1755, Robinson returning intercepted Prussian letters to Yorke at The
  Hague); "intercepted" Oct 1751-Jun 1752 -> SP 107/63 "Intercepted correspondence of foreign ministers in England, 1751-1755
  Apr" (ministers *in England*: would cover Michell, not Hellen); "Prussia" Oct 1751-Jun 1752 -> SP 100/48-49 (Prussian
  ministers in England), SP 90/63, SP 78 calendar items; none names Hellen or a Hague decypher. SP 84 (Holland) is not itemised
  by enclosure online.
- BL catalogue (searcharchives.bl.uk JSON, 5 queries): `"Add MS 32276"` -> "Vol. vi. (ff. 128) Cipher-keys", 1724-1844;
  `decyphers Hague 1752`, `intercepted Prussian 1752`, `Deciphering Branch Prussia` -> 0; `Lyonet` -> 3, unrelated. The
  Newcastle papers' intercept volumes are not itemised by sender online (as AUDIT 1 found).
- Unreachable item by item: the Deciphering Branch's own decyphers for January 1752 (BL Add MS, TNA SP 107/SP 84 enclosures).

**(f) Scholarship beyond De Leeuw 2000: searched.** OpenAlex (keyed, 5 queries: "Bruno von der Hellen" 1201 unrelated; Prussian
legation The Hague 1752 6 unrelated; three German/English cipher-history queries 0). Semantic Scholar (keyed, 2): only De
Leeuw's own two Black Chamber articles (1999). CrossRef (2): unrelated (Carl von der Hellen, Benezit). HAL (2): 0. Google Books
(country=US, keyed, 11 calls incl. 2 retries after two 503s): `"Hellen" "Rep. 96" 1752` -> Ring 1890 (read, above);
`"De Hellen" "January 1752"` -> Droysen V.4 (read, above); `"de Hellen" deciphered 1752 intercepted` -> **De Leeuw & Bergstra
(eds.), *The History of Information Security* (2007)**, De Leeuw's chapter on the Dutch Black Chamber (snippet: "... De Hellen
written by the Prussian envoy in London, Michel ... 1752 the decision was taken to extend the interception of mail to the
despatches of the envoys of Cologne ..."): the same author's later version of the 2000 chapter; snippet view only, no sign
of a quoted Jan 1752 decipherment. The rest: 0 or unrelated.

**(g) Full text and phrase search.** `tools/print_check.py` was not re-run: AUDIT 1 ran it this morning on the same seven
phrases and no reading has changed since (`print-check.tsv`). This audit's phrase searches were run on disk against PC vol. 9
and Droysen V.4 (above) and through Google Books. **JSTOR:** AUDIT 1's four rows (two per family) read; two family-(ii) rows
added from runs it did not use ("feu prince d'Orange", "renouveller le traité"), queued; they do not block the class.

**Solver repositories and blogs:** not repeated (AUDIT 1 cloned both on 4 Oct; nothing has changed in this folder since).

Requests (one at a time, >= 1.6 s apart): www.nationaalarchief.nl 2 (item page, EAD), service.archief.nl 20 (IIIF header
crops), www.archivportal-d.de 1 curl (Anubis page) + 3 browser loads, www.deutsche-digitale-bibliothek.de 1 (Anubis page),
recherche.gsta.spk-berlin.de 1 (proxy 502), archivdatenbank.gsta.spk-berlin.de 6 (one 500), archive.org 7, be-api.us.archive.org 1,
discovery.nationalarchives.gov.uk 11, searcharchives.bl.uk 5, api.openalex.org 5, api.semanticscholar.org 2,
api.crossref.org 2, api.archives-ouvertes.fr 2, www.googleapis.com 11 (two 503s, each query retried once). No DECODE request. No 429 or
403; Anubis challenges were passed by the browser tool, not bypassed.

## A2.4 Postmortem

AUDIT 1 did not over-claim; its N3 and its unsafe sentence stand. What was thin, and is now corrected or extended:
1. AUDIT 1 said the Berlin archive was "unreachable (no online finding aid reached)". The finding aid is online (Archivportal-D
   and GStA MidosaSEARCH); the King's file is **I. HA Rep. 96 Nr. 38 G-H (1752)**, not digitised. The safe sentence now names it.
2. AUDIT 1 read Fagel 5177 as "no Hellen letter between 28 Dec 1751 and 8 Sept 1752" and suggested that fits Hellen's code
   having resisted. The register's own numbering (No 71 on 5 Sept 1752) shows that dozens of 1752 intercepts were numbered
   before September and are not in the register. That makes a period decipherment of R1953 *more* likely to have existed, not
   less, and it is now stated in the verdict. Found, applied here only (no change to NOTES.md beyond the annotation below).
3. AUDIT 1 did not search Droysen V.4 or Ring 1890, the two 19th-century works that cite Hellen's 1752 reports from the Berlin
   file. Both now read; neither has 4 Jan 1752.
4. Minor: AUDIT 1 section 3d "The sequence is chronological" -- not strictly (scan 89 No 37 before scan 93 No 36). Noted above.
No sentence in NOTES.md, NEAR.md or STATUS.md uses new/first/unpublished/solved for this reading (grep on the folder and the NEAR
row, 4 Oct 2026). The NEAR.md row gains one evidence sentence. PROGRESS.tsv has **no row** for this target (checked); not
added by this verifier -- flagged to the lane orchestrator. SECOND-OPINIONS-QUEUE.tsv already has `SO-HEL-R1953` (queued 4 Oct)
for this exact item; no new row. The SO prompt's wording should be checked against the revised safe sentence by whoever lands
it (the reading did not change, so no propagation is owed under rule 10's revision clause).

## A2.5 Leads (one line each, not run; Usage 7)

- Archive request (owner side): GStA PK, I. HA Rep. 96 Nr. 38 G (1752) -- a reproduction of Hellen's report of 4 Jan 1752 and
  any decipherment with it. This is the one step that would settle prior decipherment and could give a full plaintext (and a
  known-plaintext source for codes 1-800).
- Fagel 5177 Nos 71+ (Sept-Dec 1752, scans ~102-125) and 5206 are clear decipherments of letters in, probably, the same code as
  R1953 (if it did not change); paired with any surviving cipher originals of Sept-Dec 1752 (KHA A31-1148; DECODE inv. 196
  records), they are known plaintext for codes 1-800. Worth a check of DECODE's listing for KHA inv. 196 records dated Sept-Dec
  1752 (on disk in `sources/decode/`), ~$1.
