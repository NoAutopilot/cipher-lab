# AUDIT -- na-schonenberg-1678-1716 (NA 1.02.04 invnr 63)

Verifier: VERIFY-SCHONENBERG (account-4), 2 Oct 2026, 23:17-23:4x UTC (container clock). This session did no solving and
did not decode beyond the rule-7 re-derivation. Brief: the account-4 parent's VERIFY-SCHONENBERG instruction (rule 10 template
plus rule 7). No earlier AUDIT.md existed.

Claim under audit: "the leaf's body read from its own interlinear gloss (grade C), leaf C 270 / M 11, body C 243 / M 10
(7 illegible + 3 NULL), target parked; code 36 = c by a gloss-hand letterform test (known answer 10/10, narrow: the c class
rests on 2 tiles)."

## 1. Extract

| field | value |
|---|---|
| Archive | Nationaal Archief, toegang 1.02.04 (Archief van F. van Schonenberg, gezant in Spanje en Portugal, 1678-1716), invnr 63, 1 leaf, 1 scan |
| Catalogue entry (re-read this session, item page drupal-settings-json `unittitle`) | "Aan dona Antonya de Albanylla, z.d." -- finding aid adds "In cijferschrift"; section "Minuten van uitgaande brieven aan overige correspondenten, 1702-1716 en z.d." |
| Image | https://www.nationaalarchief.nl/onderzoeken/archief/1.02.04/invnr/63 ; file https://service.archief.nl/api/file/v1/default/fc3a8d42-b89e-4715-9753-0320355365c7 (native 1946x2618) |
| Date | undated (z.d.); the section covers 1702-1716 (Lisbon years); a possible "23 de Nobe[mbre]" in the L01 gloss was not confirmed by the readings (L01 reads "no abyendo nobe-") |
| Sender | Francisco van Schonenberg's chancery (retained draft/minute of an outgoing letter), by the finding aid's placement; no signature on the leaf |
| Recipient | Doña Antonia (Antonya / Antonija) de Albanylla, per the catalogue and the clear address on the leaf |
| Place | not stated on the leaf; Lisbon by the section's date range (inference) |
| Language | Spanish |
| Plaintext as read (reading.txt letters, one /-separated run per line L01-L14, L18, L19; NULLs omitted) | "noabyendonobe/dadenestaspartesque/ladeabermudadoeste/gouyernoconlaszyrcun/stanzyasqueaysesabra/nmexoresperoconansya/lasqueybyeredelnor/teydeytalyapuesesau/andeocasyonarlasque/puedanocuryrz/parayasseguradadde/lalorespondenzyase/pondrasolamenteyn/sobrescrytoenesta/forma/adoñaantonyadealbanylla" -- word segmentation and expansion ("No aviendo novedad en estas partes que la de aver mudado este govierno con las circunstancias ... para mas seguridad de la correspondencia ... pondra solamente en sobrescrito en esta forma: A Doña Antonya de Albanylla") is M/I-grade sense, body/reading_body.txt, not part of the graded token reading |
| Distinctive phrases | "no abyendo novedad en estas partes", "aver mudado este gouyerno", "las que ubiere del norte y de ytalya", "para mas seguridad de la corespondenzya", "pondra solamente en sobre escrito en esta forma", "dona antonya de albanylla" |
| Ciphertext | ciphertext.tsv, 281 tokens (2-digit numbers with tick modifiers and a few symbols), homophonic, 87 codes |
| What the solvers searched | check-solved 25 Sept 2026 (6 sources: web, IA full text, Heinsius Briefwisseling on Huygens retroboeken, Cryptiana/Cipherbrain, DECODE dumps, both solver repositories); web and blog check 2 Oct 2026 (10 queries, three blogs, two Utrecht theses 403); Premise check 2 Oct 2026 (solver repos re-cloned, NA neighbours invnr 58-64, Willem III-Bentinck, Staten-Generaal, Heinsius, Google Books) |

## 2. Rule-7 re-derivation (fresh session, committed key and ciphertext only)

- `python3 tools/decode_key.py ciphers/na-schonenberg-1678-1716 --check` -> "ciphertext.tsv: tokens 281: C 270, M 11 / reading up to date", exit 0.
- Independent re-application by this session (a 20-line script reading only key.tsv, exceptions.tsv, ciphertext.tsv; not
  decode_key.py): every one of the 281 token values agrees with reading_tokens.tsv. The only differences are (a) NULL
  tokens, which decode_key.py omits from reading.txt and the script printed (L10 pos0-2, L14 pos3, L01 blot) -- display only;
  (b) two grades (L04 pos19 code 45, L08 pos15 code 26) that decode_key.py caps at M because the transcription confidence of
  the group is M -- by design. Differences beyond the M-graded tokens: **0**. The reading is not sent back.
- Grade counts confirmed from reading_tokens.tsv: body L01-L14 C 243 / M 10; L18 C 5; L19 C 22 / M 1; leaf C 270 / M 11, H 0.
- Note for readers of the files (not an error): ciphertext.tsv's `gloss` column is passB's raw positional gloss before the
  2 Oct re-sync, so against the key it agrees at only 143 of 246 glossed positions; the drift is a column offset in whole
  runs (e.g. L02, L08, L12, L13 shift by one), which align/ (tools/interlinear_align.py) corrects. The C grades rest on the
  aligner plus five image passes, not on that column as written.
- Code 36 = c (GAPS14): the 4 tokens change no letter (36 was c at M before); the test is narrow (2 c reference tiles,
  1 of 20 shuffle seeds reaches the target, tile boxes placed by a label-aware worker). Accepted at C as registered; if a
  later reader disputes it, the cost is 4 tokens C -> M, no text change.

## 3. Independent search log (this session, 2 Oct 2026)

| family | searched | result |
|---|---|---|
| (a) canonical series / state papers | Huygens retroboeken *Briefwisseling Heinsius 1702-1720* `search_in_text`: Albanilla, Albanylla, Albanila, Albanija -> 0 each; positive control Schonenberg -> 413 (works). *Correspondentie Willem III en Bentinck* `searchText`: same four -> 0 each; control Schonenberg -> 11. Staten-Generaal edition ends 1625 (out of range; Premise check) | no hit |
| (b) sender/recipient printed correspondence | none exists on IA (check-solved); Heinsius and Willem III editions above carry Schonenberg's official letters only | no hit |
| (c) documentary editions | print_check.py ia-global (IA full text, all items) on 9 phrases (phrases.txt): 0 hits each | no hit |
| (d) holding archive | NA item page invnr 63 re-read (unittitle as above, "cijferschrift"); finding aid read in full by check-solved; no decipherment or transcription mentioned | catalogue flags cipher only |
| (e) IA / HathiTrust / Google Books | print_check.py: IA fts 0/9; Google Books (key, country=US) returns loose word matches for the long phrases (legal codes, 19th-c. gazettes, blazon books for the surname Albanilla) -- none is this letter, the API does not enforce the quote; HathiTrust full text unreachable from the cloud (CLAUDE.md hosts table) | no hit |
| (f) solver repos, blogs | fresh shallow clones of dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers, grep albanil/albanyl/schonenberg/1.02.04: only the roell1809 aside (wrong-archive-number note), not this item. WebSearch: 3 queries ("Albanylla" OR "Albanilla" Schonenberg carta cifra; the "seguridad de la correspondencia" + sobrescrito phrase; Herrero Sánchez Conectores sefarditas cifrada) -> nothing on this letter | no hit |
| (g) scholarship | OpenAlex (key): 2 keyword searches -> Herrero Sánchez, "Conectores sefarditas ... El caso Belmonte/Schonenberg", *Hispania* 76/253 (2016) 445-472, doi 10.3989/hispania.2016.014, and the UU thesis "Diplomatie eind zeventiende eeuw ... De casus Francisco van Schonenberg" (2016). CORE (key): "Schonenberg AND (cifra OR cijferschrift OR cipher)" 0; "Albanilla OR Albanylla" 4 (geology/zoology place-name hits); "Schonenberg AND Belmonte" 0. Semantic Scholar: mostly 429, 2 answered (0 relevant). CrossRef: 1 answered (noise), 3 429. JSTOR: rows appended to JSTOR-QUEUE.tsv, families (i) and (ii) | no hit |
| unreachable | Herrero Sánchez 2016 full text: hispania.revistas.csic.es fails TLS from the cloud (curl 000, browser 502 x3), ResearchGate 403; Wayback CDX connection reset. UU thesis: 403 (2 Oct, earlier pass). These are the two studies of Schonenberg himself; neither has been read by anyone in this repo | unreachable |

Requests this session: resources.huygens.knaw.nl 12 (>=2.1 s apart); www.nationaalarchief.nl 1; github.com 2 clones;
be-api.us.archive.org 9, www.googleapis.com 9, api.openalex.org 12, api.semanticscholar.org 9, api.crossref.org 2,
api.core.ac.uk 4; hispania.revistas.csic.es 2 (+ browser 3 attempts), researchgate.net 1, dialnet.unirioja.es 1,
web.archive.org 1; WebSearch 3. One retry at most per host after a block.

## 4. Classification

| item | tokens | N-class | prior plaintext | prior decipherment | key source | evidence | confidence |
|---|---|---|---|---|---|---|---|
| A. Body L01-L14 | 253 | **N0** | yes, in manuscript: the contemporary interlinear Spanish gloss over every body line of this very leaf; not found in print | **yes:** that gloss is the period decipherment of this item, letter over group | `period` | gloss over all 14 lines; aligner agreement 0.699 vs shuffled-gloss control max 0.301 (n=300); five image passes | high |
| B. L18 (5 groups) | 5 | **N0** | yes, in manuscript: its own gloss "forma." on the leaf | yes, the gloss | `period` | layout image check (GAPS) | high |
| C. L19 (23 groups) | 23 | **N2** | yes, in clear on the same leaf: the address "A Doña Antonija de Albanylla" | no: the leaf carries no gloss over L19, and no mapping of these groups to the address was located | `ours` (the crib alignment, crib_align.py, 15/16 resolved positions vs slid-window max 0.286 and shuffled-crib max 0.438; letter values themselves come from the period-gloss key) | moderate-high (1 M token, the blotted ?9) |
| Leaf as a whole | 281 | **N0** | -- | the leaf is a deciphered cipher letter; our work is a transcription and code-alignment of a decipherment already written on it | `period` (body), `ours` (L19 alignment only) | -- | high |

Why `period` and not `ours` for the body: every plaintext letter of L01-L14 and L18 is written on the leaf in the gloss
hand; the repo's alignment (tools/interlinear_align.py) and image passes only decide which gloss letter belongs to which
group and so recover the code table. The plaintext was not produced by us. Precedents: clair1067-brienne-poland-1646 and
clair1108-duvergier AUDIT.md (an interlinear decipherment on the leaf is N0 without print), fr5160-letellier-1653; the
Dupuy 468 counter-precedent (an undescribed manuscript gloss) is noted -- here the catalogue says only "In cijferschrift"
and does not describe the gloss, which is exactly the clair1067 situation, ruled N0 there.

No item is N3 or better, so no SECOND-OPINIONS-QUEUE.tsv row is filed (the brief's "at N3 or better" condition).

**Safe sentence:** "NA 1.02.04 invnr 63, a cipher letter from Schonenberg's chancery to Doña Antonia de Albanylla, carries a
contemporary interlinear decipherment on the leaf; we transcribed it, aligned it with the 87 cipher codes (key rebuilt from the
period gloss, grade C 270 / M 11 of 281 tokens), and read the unglossed address line from the clear address on the same leaf.
No printed edition or published transcription of the letter was located (search log in AUDIT.md, 2 Oct 2026)."

**Unsafe sentence:** "We deciphered / first read a previously unsolved Schonenberg cipher letter" -- the leaf was deciphered
in the period; our contribution is transcription, key table and the L19 mapping.

## 5. Postmortem and corrections

No over-claim found: NOTES.md, HYPOTHESES.md and reading.txt contain no "new / first / unpublished" wording, and the
status word `partial` with Verdict "parked" stands. Two stale sentences in early sections, superseded by later ones in the
same file, are flagged in a correction line added to NOTES.md (no text deleted): VX-RD01's "L18 and L19 ... no gloss on the
leaf at all" (L18 carries "forma.", GAPS 2 Oct) and its L18-L19 judge "PASS" on 19 letters (superseded by the GAPS/GAPS2
FAIL on the full 28-letter string); and reading.txt's header still says "U = code never seen in the gloss" and
"L18-L19 carry NO gloss" (decode.json header text; 0 U tokens remain, L18 is glossed) -- left for the target's owner to
regenerate, since editing decode.json is a solver change. Result kind for the board: **recovery** (period key), text
`known` in manuscript, key `period`.

Open, not blocking: Herrero Sánchez 2016 (*Hispania*, OA but unreachable from the cloud) and the 2016 Utrecht thesis are
the only studies of Schonenberg's correspondence; a person's browser read of either for "Albanilla" or "cifra" would close
the one family this audit could not reach. It cannot lower the class below N0 for the body.

## Register note (VER1-REG, 5 Oct 2026; no new audit)

A separate verifier session (VER1-REG, account 2, for LANE-VER1) set the registers from section 4 above, without re-searching:
PROGRESS.tsv column `1` = x (source: this AUDIT.md); status.json target row `novelty` N0, `audit_status` 'one audit'.
Depth (rule 4a), set from section 2's counts: **D3**, 96.1% of tokens C (270 of 281; H 0, S 0), residue 11 M = 7 illegible,
3 NULL, 1 blot (no name codes); external check = the period gloss over L01-L14 and L18 (aligner 0.699 vs shuffled-gloss max
0.301, n=300); not D4 because the M residue is not limited to name/code groups. Outward words: "largely deciphered (about 96%)"
-- here by the period gloss on the leaf, so the safe sentence in section 4 still governs: the text is the period's decipherment,
the code table is ours. Depth sentence (true, from the gloss): the letter tells Doña Antonia de Albanylla that, for greater
security of the correspondence, only a cover address in the form "A Doña Antonya de Albanylla" will be used.
