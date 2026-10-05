# AUDIT 1 (A3V-VJAN, 4 Oct 2026): leaf 188, dispatch No.1 "Numero Un. Triplicata"

Verifier: A3V-VJAN (account 3 worker for LANE-A3V, Opus), run 02:53-03:02 UTC 4 Oct 2026 (clock read). Brief
`.claude/briefs/runs/2026-10-04-acct3-a3v-wave1.md`, job A3V-VJAN. A session separate from every solver of this target
(VX-CS05, VX-RD02/02B/02C, GAPS..GAPS17, SPLIT); no earlier AUDIT.md existed. Nothing decoded; key.tsv, ciphertext and
reading not touched.

## 1. Extract

| field | value |
|---|---|
| item | NA 2.01.27.05 (Hollandse Divisie, Paris), invnr 12, leaf 188 right: cipher-only fair copy headed "Numero Un. Triplicata", 15 lines, 163 code groups, signed |
| sender / recipient | Gouverneur-Generaal J.W. Janssens (Batavia) to the Minister of Marine and Colonies (Decrès), Paris |
| date | not read on the leaf; the finding aid gives the cipher run as 20 June-7 Aug 1811; see section 3 (Collet dates this text 22 June 1811) |
| reading as committed | `reading.txt` (GAPS17, 3 Oct 2026): tokens 163: H 0, C 84, S 0, M 23, I 0, U 56; keyed 107/163 (65.6%). Judge FAIL language -0.956 vs real_p05 -0.887, cover 0.918 |
| key | `key.tsv`, 2-4 digit numeric nomenclator (1-1197) with syllable spelling and homophones, rebuilt from the bundle's own period decipherments of No.2 (190-192), No.3 (199-201), No.4 (205-207) and No.5 (210-212) plus the plain copies 194-195, 202R, 208R-209L, 214 |
| distinctive runs (C) | l.1 "l'ancien Gouverneur Gal [853] [1121] l'état des"; l.2 "les re sources Sont e puis"; l.3 "l'armée n' [1021] pillé"; l.7 "le débarquer des"; l.10-11 "l'ancien Gouverneur Gal par chargent / de [125] [1065] et de la mal é [72]"; l.14-15 "ar ri vé a [929] peu vent sauve er / l'Isle de Java . fin" |
| what the solvers searched | Colenbrander Gedenkstukken VI (35 hits, names the dossier, prints none); IA advancedsearch + be-api; DECODE crawl; both solver repos (25 Sept, 2 Oct); 8 web queries + Cipherbrain/Cryptiana/Cipher Mysteries site searches (2 Oct); Van Deventer 1891 full text; Google Books 3-4 queries (found Collet 1910, unreachable as pages); print_check on No.2-No.5 and leaf 187 phrases (2 Oct); whole of invnr 12 and invnr 7 paged for a No.1 gloss or plain copy (none) |

The item is leaf 188 only. Leaf 192 carries no reading of ours beyond its own period gloss (it is the end of the No.2
decipherment, the key source), so it is not a separate item; the same holds for the other gloss leaves.

## 2. Independent search log (4 Oct 2026)

| family | searched | result |
|---|---|---|
| (a) canonical series | De Jonge / Van Deventer, *De opkomst van het Nederlandsch gezag in Oost-Indië* deel XIII (1888), full djvu text from archive.org `depkomstvanhetn00unkngoog` (Reeks 1 deel 13; 7 other Opkomst volumes fetched and grepped: no Janssens 1811 letters); NA finding aid 2.01.27.05 (Colenbrander 1901, EAD xml, 1 request) | **Opkomst XIII prints Janssens to the Minister, 16 June 1811 (no. LII, pp. 539-540), 21 June 1811 "Confidentielle, pour le Ministre seul" (LIII, pp. 540-542), 29 Aug (LIV) and 5 Oct 1811 (LV)** -- all clear letters, none is No.1's text (word overlap with leaf 188's keyed words is topical, 5-13 of 22 for every letter including the post-capitulation ones). Its Inleiding **quotes two of the bundle's cipher dispatches**: p. CXXIX "Le ci-devant Gouverneur-Général a épuisé toutes les ressources: je ne saurais répondre des événements!" footnoted "Le Gén. Janssens au Ministre Decrès (lettre chiffrée du 3 Août 1811)" = No.4 (our sealed plain copy 208R-209L reads "Le Ci-devant Gouverneur général a épuisé toutes les ressources; nous ne pouvons pas répondre des évènemens"), and p. CXXXIII n.2 "Une expédition forte de 71 voiles est arrivée le 4 devant la rade, et débarque des troupes à l'est de la ville. Nous avons détruit nos magasins de sucre, café et poivre, et nous nous sommes portés dans le camp retranché destiné pour cela depuis six mois" = No.5 (`no5_plaintext.txt`). No quotation of No.1 found in the Inleiding (grep for chiffr/cijfer, Janssens footnotes, June-Aug 1811 dates; OCR is poor, so a garbled citation is not excluded). Finding aid: invnr 12 description only, no publication note. Colenbrander Gedenkstukken VI: not re-run (solver read all 35 hits; it names the dossier only) |
| (b) sender's / recipient's printed correspondence | No edition of Janssens' letters exists as such; the Opkomst XIII Bijlagen (a) are the nearest. Recipient side: **Octave J. A. Collet, *L'île de Java sous la domination française* (Paris 1910)**, Google Books API snippet search (ids `-BCyBiSVklAC`, `uz1BAQAAMAAJ`, 5 targeted queries) | **Collet prints part of No.1's plaintext.** Snippet (both scans, p. ~407-408): "Dans une lettre chiffrée du 22 juin, Janssens, démentant ses nouvelles officielles, dit : « L'ancien gouverneur général présentera les choses bien différemment ... Il part, chargé de trésors et de la malédiction » Le nouveau gouverneur général commença un travail formidable de bureaucratie". Against leaf 188: l.1 "l'ancien Gouverneur Gal [853] [1121] l'état des [1173] ..." and l.10-11 "l'ancien Gouverneur Gal par[t] chargent de [125] [1065] et de la mal é[diction]" -- the two quoted sentences match two separate keyed runs, in the same order, with the rare collocation "chargé de ... et de la malédiction". Collet's ellipsis means he prints only part of the letter; his full page could not be read (books.google.com page view and PDF blocked from the cloud; LOCAL-QUEUE L35 already asks the owner's desk for the book) |
| (c) documentary editions | *Lord Minto in India* (1880, archive.org `lordmintoinindi00mintgoog`, full text): Janssens named 10 times, no cipher/cypher mention; Correspondance de Napoléon (gbooks hit only, Paris-side orders) | no further print of No.1. Lead, not followed: Opkomst XIII LV (5 Oct 1811) says Janssens' "cartons de la correspondance en chiffres" were stolen from his portfolio at Salatiga -- the cipher tables may have reached British hands (English-side intercept series not searched) |
| (d) holding archive | NA EAD 2.01.27.05 (1 request): invnr 12 described as the 5 Oct 1811 letter "met bijlagen; missiven in cijfer ... van 20 juni 1811 tot 7 augustus 1811 met bijgevoegde ontcijfering"; no decipherment of No.1 named. Solvers' paging of invnr 12 and invnr 7 (GAPS10-16) accepted as the leaf-level search; Paris side (AN AF IV 1722, Marine BB/4) unreachable from the cloud, LOCAL-QUEUE L31 | none of No.1 in the NA bundle; the Paris-side decipherment Collet used is presumably in AN (not reached) |
| (e) full text IA / HathiTrust / Google Books | `tools/print_check.py` with 8 phrases from leaf 188's C runs (`phrases_a3v.txt`, `sources_a3v.tsv` -> `print-check-a3v.tsv`): IA listed sources (Opkomst XIII, Van Deventer 1891) no hits; ia-global and gbooks hits all unrelated (short phrases, generic); plus 17 hand Google Books queries (keyed, country=US) | Collet hit above came from the hand queries (`"lettre chiffrée" Janssens Java colonie`), not from print_check -- print_check's phrases were the decoder's spellings ("ressources sont épuisées", "peuvent sauver") which Collet's excerpt does not contain |
| (f) solver repos, cipher blogs | not re-cloned: GAPS6 (2 Oct) grepped both repos fresh for janssens/batavia/2.01.27/java and the GAPS web step covered the three blogs; DECODE crawl grepped by check-solved | accepted, 2 days old |
| (g) scholarship | OpenAlex (print_check, keyed: 94 works for the keyword query, none on the cipher), Semantic Scholar (one keyed manual query, 154 hits, none on the dispatches; print_check's s2 calls 429'd), CrossRef (2 queries; top hit Archipel 1972 "Les archives françaises au service des études indonésiennes", a guide to the Paris holdings), HAL (0) | no study of the cipher dispatches located |
| JSTOR | 2 rows appended to JSTOR-QUEUE.tsv: family (i) `Janssens AND Java AND 1811 AND ("lettre chiffrée" OR chiffre OR cipher)`; family (ii) bare phrase `"chargé de trésors et de la malédiction"` | queued |

Unreachable: Collet 1910 page images (Google Books page view/PDF; LOCAL-QUEUE L35); Archives nationales / FranceArchives
(LOCAL-QUEUE L31); English-side intercepts (BL IOR / Raffles-Minto collections, TNA) at item level.

## 3. Classification

**Leaf 188 (dispatch No.1): N1.**

- Prior plaintext: **yes, in part.** Collet, *L'île de Java sous la domination française* (Paris 1910), p. ~407-408,
  quotes two sentences of "une lettre chiffrée du 22 juin" from Janssens, which correspond to leaf 188 lines 1 and 10-11.
  Earliest citation located: Collet 1910. Collet quotes with an ellipsis, so most of the letter's text is not known to be
  in print.
- Prior decipherment: **yes, of the dispatch, not located as a document.** Collet calls his source a "lettre chiffrée",
  so he read a decipherment of this dispatch (presumably the Paris-side Primata or Duplicata, deciphered at the Ministry;
  not seen). No decipherment of this Triplicata copy (leaf 188) exists in the NA bundle. That is why the class is N1 and
  not N0: the *dispatch's* plaintext was deciphered and partly printed; this *copy's* mapping is ours, rebuilt
  independently from other dispatches' glosses.
- Evidence quality: Google Books API snippets of two independent scans, identical text; the match rests on two keyed
  runs (leaf 188 tokens 1:1-3 and 1:6-8, all C; 10:8-12, C except 10:11 'par' M; 11:1-8, C except 11:1 'de' and 11:7 'mal' M) and the dating (22 June falls in the finding aid's cipher run, which
  starts 20 June; No.1 is the first). Page number approximate (the snippet ends "408.").
- Confidence: high that Collet quotes the same letter; low on how much of it he prints.
- **Key source: period** (rebuilt by us from the bundle's own decipherments No.2-No.5 and their plain copies; no
  published key; the reading of the matching runs owes nothing to Collet). `text: known` (in part).

**Safe sentence:** "Leaf 188 of NA 2.01.27.05 invnr 12, Janssens' cipher dispatch No.1 (the 'lettre chiffrée du 22 juin'
1811), is read by us at 107 of 163 groups (C 84, M 23, U 56) with a key we rebuilt from the same bundle's period
decipherments of dispatches 2-5; two of its sentences were already printed from a period decipherment by O. Collet,
*L'île de Java sous la domination française* (1910), pp. c.407-408, and our reading is an independent re-decipherment of
this copy."

**Unsafe sentence:** "We are the first to read Janssens' cipher dispatch No.1" / "its content was unknown" / "a
previously unread dispatch".

Not classified as items (key sources, not our readings), recorded for credit: the plaintexts of **No.4** (3 Aug 1811) and
**No.5** (7 Aug 1811) are quoted in print from the period decipherments by Van Deventer, Opkomst XIII (1888), pp. CXXIX and
CXXXIII n.2; the folder's 2 Oct print-check missed both because it read Van Deventer's 1891 volume, not deel XIII.

## 4. Postmortem

Failure: the print step searched for the dispatch by its decoded spelling and by date, and dismissed the right edition
on a wrong premise. Two specific misses:
1. NOTES.md "Premise check (GAPS6...)" (d): "The De Jonge *Opkomst* series ends before 1811 (Van Deventer's 1891 volume
   is its continuation, read above)" -- wrong: deel XIII (1888, ed. Van Deventer) prints Janssens' June-October 1811
   letters and quotes the No.4 and No.5 cipher dispatches. Annotated in place (bracketed correction).
2. Collet 1910 was found (GAPS6/GAPS7) and queued (L35) but only searched with the No.2 footnote snippet; a single API
   query on the cipher keyword ("lettre chiffrée") returns the No.1 quotation. Corrected by this audit; no folder
   sentence claimed novelty, but the print-step Verdict ("no decipherment or print of leaf 188 found by (a)-(d)") is
   superseded -- noted in a closing NOTES.md section rather than rewritten.

Over-claim check of folder files, NEAR.md, PROGRESS.tsv, STATUS.md: no "new/first/unpublished" wording found for this
target (`grep -n -i -w 'first\|unpublished\|never\|newly'` over NOTES.md hits only procedural uses: "first genuine
cryptanalytic-independent control", "newly added No.5 codes", "never wrote"). PROGRESS.tsv row updated (audit 1 = x, note, source AUDIT.md). Not in NEAR.md. No
SECOND-OPINIONS-QUEUE row (class below N3).

Found, not applied (for the next solver; a known-plaintext crib, grade C if used, rule 4): Collet's two sentences give
values for unkeyed or M codes on leaf 188 -- l.1 "[853] [1121] l'état des [1173]" against "présentera les choses bien
différemment" (Collet's wording; "l'état des" may be the cipher text's own, Collet paraphrasing or abridging), and l.10-11
"par chargent de [125] [1065] et de la mal é [72]" against "Il part, chargé de trésors et de la malédiction" (suggests
381 = chargé, [125]/[1065] = tré-/sors or trésors, [72] = -diction or a syllable of it; 1096 "par" = part is now
supported against GAPS17's LM move). The full Collet page (L35) is the cheapest route to more of No.1; the Paris
decipherment (L31) the complete one.

Requests: archive.org 9 (8 djvu downloads + 1 advancedsearch) + 2 advancedsearch, be-api.us.archive.org 8 (print_check),
www.googleapis.com 8 (print_check) + 17 hand, api.openalex.org 9, api.semanticscholar.org 1 (429) + 1, api.crossref.org 2,
api.archives-ouvertes.fr 1, www.nationaalarchief.nl 1. Subagent calls 0; vision calls 0. Cost: see the lane ledger.

## AUDIT 2 (VER1-REG, 5 Oct 2026)

Verifier: VER1-REG (account 2 worker, for LANE-VER1; brief `.claude/briefs/runs/2026-10-05-ytbiz-ver1-jobs.md`), run 18:40-19:0x UTC
by `date -u`. This is a separate session from Audit 1 (A3V-VJAN) and from every solver of this folder. Nothing decoded; key.tsv,
ciphertext and reading not touched. Claim under audit: Audit 1's **N1** for leaf 188 (dispatch No.1), key `period`, text known in part
(Collet 1910). Adversarial aim: find more of No.1 in print (which would leave N1 but enlarge the known part) or a printed
decipherment of this Triplicata copy (which would lower it to N0).

### Search log (5 Oct 2026)

| family | searched | result |
|---|---|---|
| (a) canonical series | Opkomst XIII (archive.org `depkomstvanhetn00unkngoog`) via be-api fts with identifier filter: "malédiction", "trésors", "chiffrée", "différemment" 0 each; positive control "Janssens" returns the item | no print of No.1's quoted sentences in Opkomst XIII (poor OCR; a garbled citation is not excluded, same caveat as Audit 1) |
| (b) recipient-side print | Google Books API (`country=US`, key): `"chargé de trésors et de la malédiction"` 2 vols, `"présentera les choses bien différemment"` 1, `"lettre chiffrée du 22 juin"` 2, `Collet Java "lettre chiffrée" Janssens` 2 -- all are Collet 1910 (`-BCyBiSVklAC`, `uz1BAQAAMAAJ`); snippet text re-read and matches Audit 1's quotation verbatim | **Collet 1910 confirmed independently**, and he is the only printed source of the quoted sentences that the API finds |
| (c) documentary editions / later secondary | Google Books: `Janssens "22 juin 1811" Java` 78 vols, top 10 read: Collet x2, Day 1904 *Policy and Administration of the Dutch in Java* (cites "Janssens to Minister, June 1811, ib., 541" = Opkomst XIII LIII, a clear letter), Archipel 1971, *Croisières dans la mer des Indes* 1992, others unrelated; English/Dutch renderings (`"laden with" curses`, `Daendels "schatten" vloek`, `"charged with treasures"` on IA fts 75 hits, all unrelated) 0 relevant | no further print of No.1 |
| (d) holding archive | not re-queried (Audit 1 read the NA EAD the day before; no change expected) | accepted |
| (e) IA full text | be-api fts, all items: the three Collet phrases 0 each (Collet 1910 is not on IA) | none |
| (f) solver repos, blogs | fresh shallow clones today: dbourdeau/cyphersolver HEAD a439937 (3 Oct 2026), aaymeloglu/unsolved-ciphers HEAD d2800bb (27 Sept 2026); grep janssens / batavia / 2.01.27: only Batavian-Republic DECODE records (Fagel, Hogendorp, Bourdeaux 1801-03) and Croiset key notes, nothing on Java 1811 | none |
| (g) scholarship | OpenAlex (key) 3 queries: one relevant work, Peter Carey, *The Power of Prophecy* (Brill 2007), ch. VII "The end of the beginning: the last months of the Franco-Dutch government ... 1811-1812", doi 10.1163/9789067183031_008, not open access, not read; Google Books index search of Carey for Janssens/Daendels/cipher shows no hit on the dispatch. HAL `Janssens AND Java AND 1811` 0; CrossRef 1 query, top 3 unrelated; Persée `"lettre chiffrée" Janssens` 5759 loose hits, first page unrelated (Janssen astronomer). JSTOR: both Audit 1 rows are answered (family (i) context hit = the same Carey chapter; family (ii) phrase = no hits); no new row needed | Carey 2007 is the one study that could quote No.1 and is unread (owner-side read: JSTOR stable 10.1163/j.ctvbqs55t.12, pp.261-344) |
| unreachable | Collet 1910 page images (books.google.com page view, cloud-blocked; LOCAL-QUEUE L35 stands); Carey 2007 full text; AN Paris originals (LOCAL-QUEUE L31) | -- |

Requests: www.googleapis.com 15 (two 503s, not retried), be-api.us.archive.org 8, api.openalex.org 4, api.archives-ouvertes.fr 1,
api.crossref.org 1, www.persee.fr 2, github.com 2 clones. Subagent calls 0.

### Classification (Audit 2)

**Leaf 188 (dispatch No.1): N1 -- Audit 1 endorsed.** Prior plaintext in part (Collet 1910, pp. c.407-408, two sentences, re-found
by this audit in both scans); prior decipherment of the dispatch implied by Collet's "lettre chiffrée" but not located as a document;
no decipherment of this Triplicata copy located. Not lowered to N0: nothing found prints a decipherment of leaf 188 or the full text
of No.1. Key source **period** (rebuilt by us from the bundle's decipherments of No.2-No.5; no published key). `text: known` in part.

**Depth (rule 4a): D2, 51.5%** of tokens H/C/S (C 84 of 163; M 23, U 56). Check: the l.10-11 run "l'ancien Gouverneur Gal par
chargent de [125] [1065] et de la mal é[72]" and the l.1 run "l'ancien Gouverneur Gal" are matched, in the same order, by Collet's
independent print -- a non-statistical external check of a clause; not D3 (below 80%, and the 56 U tokens are not only name codes).
Depth sentence (true, specific): in this dispatch Janssens reports that the former Governor-General (Daendels) is leaving "chargé de
... et de la malédiction" -- the passage Collet prints as "Il part, chargé de trésors et de la malédiction". Outward words:
"partially deciphered (about 50%)", with Collet's prior print stated.

**Safe sentence:** Audit 1's, unchanged. **Unsafe sentence:** "first reading of Janssens' dispatch No.1"; "its content was unknown".

### Postmortem
Audit 1 holds; no over-claim found in AUDIT.md, NOTES.md headline, PROGRESS.tsv row or status.json target row (grep for
new/first/unpublished/novel: procedural uses only). One gap for the next session: Carey 2007 ch. VII is the only modern study located
that treats June 1811 at this level and may quote No.1 from the Paris decipherment; reading it cannot lower the class below N1 (Collet
already prints part) but could enlarge the known part. No SECOND-OPINIONS-QUEUE row (class below N3).

`python3 tools/depth_check.py` (5 Oct 2026, after this audit; neither item is a counted result, N0/N1): `unique solves (N3+ and D2+): 16 -- D4 1, D3 2, D2 13; not counted D0/D1: 13; legacy ungraded: 0 exit 0`
