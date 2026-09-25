# AUDIT: espagnol142-mercy-1648 -- novelty of the LANE R6 reading of BnF Espagnol 144 f.22 (6 June 1648)

Verifier session V6-MERCY (Opus, session_01LugT366o3rK34S42JuE343), 25 Sept 2026, from 19:05 UTC (`date -u`).
Parent: LANE V6 orchestrator session_01V2BHwhVh1k72qSYuBFCyGd. Brief: `.claude/briefs/runs/2026-09-25-lane-v6-mercy.md`.
Adversarial audit. This session did not solve, did not decode, and did not touch key.tsv, corrections.tsv,
ciphertext.tsv or reading.txt. Levels N0-N5 are CLAUDE.md rule 10.

Claim under audit (LANE R6 orchestrator, ROOM 18:52 UTC 25 Sept 2026): BnF Espagnol 144 f.22 (Gallica
`btv1b10035717h`, canvases 58-59; the folder name says 142, the item is in tome III = Espagnol 144, finding aid
`cc347546`, item 11), an instruction to the Baron/abbé de Mercy dated Barneton 6 June 1648, reads under a key
recovered by our own cryptanalysis (homophonic anneal plus logged corrections) at S 494, M 27 of 521 codes (H 0,
C 0: a cryptanalytic result); `decode_key --check` exits 0; a fresh re-derivation is byte-identical; the language
judge FAILs on es17 and es17c and also FAILs the letter's own clear words.

## 1. Verdict

| item | prior plaintext | prior decipherment | class | key | evidence quality |
|---|---|---|---|---|---|
| f.22r-22v, instruction to Mercy, Barneton 6 June 1648: the cipher runs as read by LANE R6 M2 | not located | not located | **N3** | **ours** | moderate: reproducible cryptanalytic reading (S/M only), control-beating anneal gap, numeric crib-gain gate not met, judge cannot decide |

Key source: **ours** -- recovered by LANE R6 (Y8 homophonic anneal against a matched control, M2 hand corrections
logged in `corrections.tsv`); no period key sheet, no interlinear decipherment, no published key. DECODE's Brussels
Secrétairerie d'État et de Guerre key series "chiffres 1647-98" (records 958-965) is the nearest period key family
and has not been fetched or compared.

**Safe sentence:** "BnF Espagnol 144 f.22, an unsigned Spanish instruction to the abbé (Baron) de Mercy dated
Barneton 6 June 1648, has been read in part by our own cryptanalysis (a 38-value letter cipher; 494 of 521 code
tokens at grade S, 27 at M, none from a key source or known plaintext); no prior print of its deciphered text and no
prior decipherment were located in the sources logged in this AUDIT.md, searched 25 Sept 2026. The reading is a
cryptanalytic result, not confirmed by a key or a clear copy."

**Nearest honest equivalent of a first (rule 10, key source):** an `ours` key at N3 -- "our own cryptanalysis read
this letter's cipher; no prior decipherment located in the logged search". Never "first", "new", "unpublished" or
"previously unread".

**Unsafe sentence:** "We have deciphered for the first time Leopold Wilhelm's secret instruction ordering Mercy to
raise 3,000 infantry from the Elector of Brandenburg." (four faults: "first" is barred below N4 and the key is
cryptanalytic; the sender is inferred, not read -- the letter is unsigned; the Cleves/Chevreuse names rest on five
transcription changes made by the reader, graded M; and roughly two fifths of the code stream does not read.)

## 2. Why N3, not lower or higher

- **Not N0/N1:** no decipherment of this item and no print of its deciphered text was located. The leaf carries no
  interlinear gloss (Y5, Y6).
- **Not N2:** no clear copy, draft or register entry of the 6 June 1648 instruction was found in print, so there is
  no known plaintext to map. The closest print is Lonchay 1896 p.445 (section 4), which cites the *15 April 1648*
  instructions to Mercy (a plain sibling) and a Leopold-to-king dispatch of 30 Aug 1648, and prints neither text.
- **Not N4:** principal families are only partly covered. Acta Pacis Westphalicae's full-text search was down
  (HTTP 505 on every query, including a control term) and so is unreachable, not negative; Lonchay-Cuvelier IV
  (the calendar of Philip IV's letters 1647-1665) is not on IA and is in copyright on HathiTrust and was covered only at token level (HTRC EF) and
  by Google Books snippet; CODOIN 82-84 are not on IA; Cuvelier-Lefèvre VI p.647 (a calendar summary naming Mercy, Leopold Wilhelm and a cipher) is lending-only and was seen only as a snippet; Simancas Estado and the Brussels SEE
  registers (where Leopold's dispatches with enclosed instructions are filed, per Lonchay's own footnotes) are
  unprinted archives, not searched.

## 3. Standing of the reading (task 2; not a novelty question)

What the reading rests on, in order of weight:

1. **Anneal gap with a matched control (Y8):** target best -1154.3 (4 of 6 seeds, K=38) and -1154.5 (K=36)
   against control best -1321.7 / -1335.5 on real Spanish of the same N, K and design; inter-seed control spread
   17-35 points. Reproduced by `cheap_test_1/rerun.sh`. This shows the stream is more fittable toward Spanish than
   a real Spanish homophonic cipher of that shape usually is. It does *not* by itself show the reading is right.
   **Missing control:** nobody has annealed a *shuffle of the target's own code stream* (same multiset, order
   destroyed). A score near -1154 on a shuffle would mean the gap comes from the target's skewed symbol profile
   (38 codes, only about 17 letters used), not from sequential plaintext structure. This is the cheapest test that
   could disprove the reading's basis.
2. **Legibility in context (M2):** about a dozen connected clauses in the letter's own frame ("pasareis a Cleues a
   veros con el elector de Brandenburg ... tres mil hombres de infanteria en dos o tre[s] [r]egimient[o]s y con que
   condiciones"), coherent with the clear words around them and with the dated sibling instructions (M3: item 9,
   Brussels April 1648, sends the same Mercy to Kempen to treat with the duchesse de Chevreuse and Saint-Ibal;
   Lonchay 1896 p.445 independently places Mercy's talks with Chevreuse and Saint-Ibal at Kerpen and Spa in 1648).
   Historical fit is supporting context, not verification: a reader who knew the catalogue titles could steer
   toward those names.
3. **Numeric gates:** the crib-loop gain gate (rule 3) is **not met** -- control gain 0.0, target anneal score
   fell (-1154.3 to -1199.1) and judge moved -1.048 to -1.057. The judge FAILs the reading (-1.034 / -1.057)
   and FAILs the letter's own clear words by a hair (es17: -0.892 vs real_p05 -0.888; es17c: -0.891 vs -0.867;
   es17c held-out false-negative rate 23.5%), so the judge cannot decide on this text. The decode still scores
   about 0.17 below the clear words.
4. **Rule 7:** `decode_key.py --check` exits 0 and MR's fresh-instance re-derivation is byte-identical (0 tokens
   differ vs 27 M). This proves the reading is reproducible from the files, not that it is correct.

**Circularity check (verifier's own).** The two proper names Cheureuse and Cleues, and "y con co...", depend on five
glyphs that *both blind passes* read as 19 and that M2 re-read on the image as 14 (`exceptions.tsv`, grade M). Code
14 = c is independently attested (con, cartas, creencia, condiciones, corra; 13 other positions transcribed 14 by
both passes), so the key value is not circular; the transcription change is reader-made at exactly the places that
produce the names. This verifier looked at one of the five (r06 pos 14, crop `images/f22r_L02_s1.jpg`): the
second digit has the angular open form of the 4 in the "34" earlier on that line and differs from the round-bowled
9 of "19" on the next line, so the 14 reading looks right. This was *not* blind (the verifier knew the claim); a
blind eye-check of all five by a session that has not seen the reading is still owed before those tokens go to S.

**What would disprove or confirm it:** (a) the shuffled-stream control above; (b) a period key -- DECODE's Brussels
SEE "chiffres 1647-98" (R958-R965) or any Leopold Wilhelm household cipher -- whose values disagree with key.tsv;
(c) a clear copy: Lonchay's footnotes show that Leopold sent copies of his instructions to Mercy to Madrid with his
dispatches (15 April 1648 instructions "jointes à la dépêche de Léopold au roi du 18", Brussels SEE register t. LXIV
f.16), so a clear copy of the 6 June instruction may sit in the SEE registers t. LXIV-LXV (Archives générales du
Royaume, Brussels) or in Simancas Estado -- a confirmed clear copy would turn this item into C-grade tokens and
drop it to N2; (d) a blind re-transcription of the five 14/19 glyphs and of r16-r17, v04, v07.

## 4. Search log (25 Sept 2026)

| family | searched / unreachable | what | result |
|---|---|---|---|
| (a) Le Clerc, Négociations secrètes III-IV (1725) | searched (LANE CX, re-used) | full djvu text grepped: Mercy, Barneton | 0 hits |
| (a) Acta Pacis Westphalicae (apw.digitale-sammlungen.de) | **unreachable** | search form found (`/search/query.html?q=`), Anubis cleared with browser tool; backend returned "Error 505 Internal Server Error" for every query incl. control "Munster"; queued: Mercy, Merci, Barneton, Warneton, "Abt von Mercy", "abbé de Mercy", Sumiller. (CX earlier: APW II B ends 1647/19 May 1648, so the French series cannot hold a 6 June 1648 item.) Google Books snippet shows APW volumes (Neerfeld/Heuser 1979) name "l'abbé de Mercy" in the Spa/Chevreuse episode -- a different episode | not searched; retry owed |
| (a/c) CODOIN vols 82-84 (Münster plenipotentiaries 1643-48) | **unreachable** | IA advancedsearch, 3 query variants over the CODOIN run on IA: tomos 2, 4-8, 13 ... 74 present, 82-84 absent under every title form | not searched; owner/HathiTrust full text owed |
| (a/c) Lonchay, Cuvelier, Lefèvre, Correspondance de la Cour d'Espagne ... IV, Précis de la correspondance de Philippe IV (1647-1665), 1933 (HathiTrust mdp.39015014126620, search-only) | searched at token level + snippet | HTRC EF: "mercy" on 27 pages, "brandebourg" 22, "chevreuse" 12, "clèves" 1 (seq 536, with brandebourg, not with mercy); no "barneton"/"warneton"/"cleves"/"brandenburg". Google Books snippets: "abbé de Mercy (fol. 85)", "(fol. 249)", "Quam flaco medio es el Abbad de Mercy" | no page reads as this instruction; pages not readable from the cloud -> LOCAL/JSTOR-style owner check |
| (a/c) Lonchay-Cuvelier III (IA `correspondancede0003unse`, fts) and V (`correspondancede0005unse`, fts) | searched | Mercy, Barneton, Sumiller | III: one Mercy hit, 1642 (Melo dispatches; a mémoire from the abbé Mercy for the duchesse de Chevreuse -- the Guise-era channel); V: 0 |
| (a/c) Cuvelier-Lefèvre, Correspondance ... tome VI (1937), IA `correspondancede0006jose` (lending only, fts snippets) | searched, snippets only | Mercy, Clèves, Brandebourg | index: "Mercy (L'abbé de), 647, 15, 20"; text: "... chiffre a cet effet. Il en est de même de l'abbé de Mercy qui a été envoyé par Léopold-Guillaume pour traiter ..." and "... paraissent émaner de ces négociations de Mercy avec Chevreuse". A calendar summary on one page (647) that ties Mercy, Leopold Wilhelm and a cipher together; not a print of this instruction as far as the snippets show (its Clèves/Brandebourg hits are the 1609-14 succession). **Owner read of p.647 owed** (lending-only; the page may name the cipher Mercy was given) |
| (a/c) Lonchay-Cuvelier III (mdp.39015014126638) | token level | clèves+brandebourg seq 114; mercy+chevreuse seq 488; no co-location of Mercy with Cleves | no hit |
| (b/c) Lonchay, La rivalité de la France et de l'Espagne aux Pays-Bas (1635-1700), 1896 (IA `la-rivalite-de-la-france-et-d-espagne-aux-pays-bas-1635-1700`) | searched, full text | Mercy, Clèves, Brandebourg, Barneton, Warneton | pp. 406, 445: Mercy as Leopold's chaplain, Holland 1647, talks with Chevreuse/Saint-Ibal at Kerpen and Spa; n.2 p.445 cites "Instructions à Mercy, du 15 avril 1648, jointes à la dépêche de Léopold au roi du 18 (S.E.E., t. LXIV, f.16)" and Léopold au roi 30 août 1648 (t. LXV f.181). Nothing on a Cleves/Brandenburg mission or the 6 June instruction |
| (b) Cousin, Madame de Chevreuse (Lonchay 1896 p.445 n.1: its appendix pp. 425 ff. prints P. Ernest de Mercy's 27 Sept 1647 memoir = sibling item 8) | searched in part | IA `madamedechevreus02cous` (Madame de Chevreuse et Madame de Hautefort t.II) full djvu grepped: Mercy, Kempen, Saint-Ibal, Barneton | no 1648 Mercy mission text; the 1856 *Madame de Chevreuse* appendix itself not located on IA this pass -- a lead: it prints a sibling from the same channel, so check it for the 6 June instruction |
| (b) Urkunden und Actenstücke ... Friedrich Wilhelm | searched | IA full djvu grepped Bd. 1, 2, 4, 5; be-api fts Bd. 6-13, 15, 17, 19 (Mercy, Merci, Barneton, Warneton, Sumiller); HTRC EF Bd. 1 (1930 ed.) | 0 hits for this Mercy (every Mercy/Merci is remercier, commercia or the general Franz von Mercy); Bd. 3, 14, 16, 18 not checked |
| (b) Aumale, Histoire des princes de Condé; Mazarin, Lettres (1883); Goulas (1879); Retz (1872); Herrero Sánchez (2000); Gayangos, Catalogue of Spanish MSS in the British Museum | Google Books snippets | same Mercy ("sommelier de cour", brother of the general killed at Allerheim), other missions; Gayangos lists a different BM instruction to "el abbad de Mercy" with "cartas de creencia" | no hit on this instruction; Gayangos BM item is a lead for a sibling (section 6) |
| (d) BnF finding aid cc347546, all three tomes | searched (M3) | only item marked "chiffrée" is the target | no decipherment noted |
| (e) Google Books API | searched, 19 queries | period and modern spellings: "abad/abbad de Mercy", "abbé de Mercy" 1648, "baron de Mercy" Cleves, "sumiller de cortina" Mercy, Barneton+Leopoldo, "pasareis a Cleves", "pasaréis a Cleves", "tres mil hombres de infanteria" Cleves, "cartas de creencia que van con esta", "elector de Brandemburg" Mercy, Chevreuse, Saint-Ibal, Kempen, "dilacion que aya es summamente", Abt von Mercy, Friedrich Wilhelm Cleve Werbung | no hit on this letter; formula phrases occur generically in unrelated books |
| (e) HathiTrust | bibliographic + EF API reached; full text/page images unreachable from the cloud (Cloudflare) | as above | |
| (e) Internet Archive | searched | advancedsearch + djvu/fts as in the rows above; global fts "Barneton" (486 hits) and "Sumiller de Cortina" (term-split) dominated by unrelated items, not pursued | no hit on this letter |
| (f) Cryptiana (snapshot + 2 live fetches) | searched | Mercy, Barneton, Warneton, Espagnol 14x, Leopold | only Leopold Wilhelm's own Ferdinand III cipher correspondence (Pecho); no hit |
| (f) dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers (fresh shallow clones) | searched | barneton, warneton, espagnol 142-144, cc347546, btv1b10035717h, abad/abbé de Merc*, baron de mercy, sumiller, Leopold Wilhelm | no hit (one "leopold" hit is Conti to Noirmoutier 1649, unrelated) |
| (f) DECODE listing (repo harvest 24 Sept + Aymeloglu's decode-catalog.csv, 10,107 rows) | searched | mercy, barneton, espagnol 14, leopold | no record of this item; R958-R965 Brussels SEE keys 1647-98 exist (key family lead) |
| (g) OpenAlex (keyed) | searched, 7 queries | abbé de Mercy 1648; abad de Mercy; Leopold Wilhelm Brandenburg 1648 Cleves; Chevreuse Saint-Ibal 1648; Espagnol 144 BnF Mercy; Spanish Netherlands levies Cleves 1648; Leopoldo Guillermo Mercy 1648 instrucción cifrada | nothing relevant ("Protecting the Fatherland ... Jülich 1642-1655", 2021, is background on Jülich-Cleves) |
| (g) Semantic Scholar (keyed) | 3 of 5 queries answered, 2 unreachable (429; one retried once, one not retried) | abbé de Mercy 1648; Leopold Wilhelm Brandenburg 1648; duchesse de Chevreuse 1648 Espagne | nothing relevant |
| (g) HAL, CrossRef, Persée | searched, 5+5+6 queries | abbé de Mercy; Mercy Chevreuse 1648; Espagnol 144; Léopold-Guillaume Brandebourg Clèves; Saint-Ibal; "Barneton" | 0 relevant; Persée unquoted multi-word queries unusable, quoted "Barneton" 0 |
| (g) JSTOR | queued (JSTOR-QUEUE.tsv) | 2 rows | never blocks a class |

## 5. Did we first-decipher?

Not established and not claimable. What the record supports: no prior decipherment of this leaf was located in the
logged search, and the key is ours (cryptanalytic). That is N3 with an `ours` key: "the nearest honest equivalent
of a first", said in those words only, with the caveat that the reading itself is cryptanalytic and partly unread.

## 6. Leads for the next worker (one line each)

- Owner/local: read Cuvelier-Lefèvre tome VI (1937) p.647 (IA `correspondancede0006jose`, lending only): the calendar summary that ties Mercy, Leopold Wilhelm and a cipher together. If it quotes the 6 June instruction, reclassify (N2 or N1); if it names the cipher sheet, that is the period-key route.
- Find and read the appendix of Cousin, *Madame de Chevreuse* (1856; pp. 425 ff. per Lonchay 1896), which prints a sibling from the same channel.
- CODOIN vols 82-84: not on IA; HathiTrust full text from the owner's machine.
- Retry APW full-text search (Mercy, Barneton, Warneton, Sumiller) when the site's backend recovers.
- Owner/local: read Lonchay-Cuvelier IV (HathiTrust mdp.39015014126620) at the "Mercy" pages for June-Sept 1648
  (the king's replies to Leopold) -- a calendar entry on a Cleves levy through Mercy would be context, and would name
  the SEE register folio of the enclosed clear copy.
- Brussels AGR, Secrétairerie d'État et de Guerre registers t. LXIV-LXV (Lonchay's "S.E.E."): the likeliest home of a
  clear copy of the 6 June instruction (archive request, not print).
- Gayangos, Catalogue of Spanish MSS in the British Museum: a different instruction to "el abbad de Mercy" -- check
  whether any BM copy is ciphered under the same 38-value code (a sibling for pooling).
- Shuffled-stream anneal control (section 3, item 1), cheap, disk only.

## 7. Postmortem and corrections

Failure found: none that over-claims in this folder. NOTES.md's status word is `open` and every R6 section says
"cryptanalytic", "not a reading" or "not classifying novelty". Two points corrected by note, not by rewrite:
(1) the folder is named for Espagnol 142 but the item is Espagnol 144 f.22 (already flagged by LANE G2 worker O);
(2) the spec's constraints line "Spanish court, likely Peñaranda/Castel-Rodrigo office per the finding aid" is not
what the finding aid says: its items 9-10 are "remises par Léopold-Guillaume", and Lonchay 1896 p.445 makes Mercy
Leopold's chaplain, so the sender is best inferred as Archduke Leopold Wilhelm's secretariat (Barneton/Warneton was
on his June 1648 campaign front) -- still an inference, since the leaf is unsigned. Spec not edited (outside this
brief's touch list); flagged in NOTES.md.

## 8. Requests (this session and its three Sonnet subagents)

archive.org about 34 (this session 6, IA sweep about 28); be-api.us.archive.org about 36; api.openalex.org 7;
api.semanticscholar.org 7 (5 + 2 retries); github.com 2 shallow clones; Google Books ~19; openlibrary.org 4;
catalog.hathitrust.org 4; data.htrc.illinois.edu ~6; apw.digitale-sammlungen.de ~7; HAL 5; CrossRef 5; Persée 6;
cryptiana.web.fc2.com 2. gallica.bnf.fr 0 (images on disk).
