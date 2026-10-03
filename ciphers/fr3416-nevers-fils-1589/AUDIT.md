# AUDIT -- fr3416-nevers-fils-1589, f.35r figure runs under key no.25

Verifier: VERIFY-NV02 (account 3, for the account-3 orchestrator), 3 Oct 2026, 05:10-05:17 UTC. I'm not the solver.
Claim under audit (NOTES.md, NV02-READ, commit 0214a626): the figure runs at the foot of BnF fr.3416 f.35r (the duc de
Nevers to his son Charles, duc de Rethelois; undated, c. Oct-Dec 1589) decode under key no.25 (BnF fr.3995 canvas f104,
label 51r) as 102 tokens, H 62 / M 40, rank 1/201, z 5.04 against shuffled keys.

## 1. Extract

- Item: BnF Français 3416 f.35r, Gallica ark:/12148/btv1b9058240c canvas f43; BnF catalogue item 30 "Lettre, avec
  chiffre, du duc DE NEVERS a son fils". No contemporary decipherment on the leaf (contrast f.38, item 32 "avec chiffre
  et dechiffrement").
- Key: Tomokiyo, nevers.htm, "no.25 (fol.50) (October 1589)": "This appears to be used in ... BnF fr.3416: no.30
  (fol.35) Duke of Nevers to his son". Tomokiyo published the key's image and gave this attribution. He printed no
  decode of f.35. NV02-READ transcribed the alphabet and nulls from the period key sheet into keys/key_no25.tsv.
- Reading (f35r_reading.txt): 8 short runs of letter fragments, e.g. ".aisi.nlesauroit[ciiij].e", "s.es.auoir[0]"
  (followed by clear "bons deniers"), "b.onnefaSUN.as.". There are no continuous sentences. The clear text around the
  runs isn't transcribed, and the nomenclator codes (Roman numerals, overbar figures) are not read.
- Solver's search: Gomberville 1665 *Mémoires* (4 copies, Books API full text), Tomokiyo pages and hidden comments,
  Cabinet Noir / Bourdeau / Aymeloglu clones, DECODE snapshots, web and blog queries (NV-INTAKE and NV02-READ, 3 Oct 2026).

## 2. Re-derivation and statistics (script verify/verify_nv02.py, output verify/verify_nv02_out.txt)

- `python3 decode_f35.py --check`: `check: OK`, exit 0 (rule 7).
- Fresh seeds 2 and 3 (seed 1 was the solver's):

| text | seed 2 rank / z | seed 3 rank / z |
|---|---|---|
| target, all tokens (72 letters, -1.150) | 1/201, 4.87 | 1/201, 4.56 |
| target, H only (51 letters, -0.938) | 1/201, 5.14 | 1/201, 4.85 |
| positive control NV-03 f.38v (34 letters, -0.769) | 1/201, 5.80 | 1/201, 5.60 |
| shuffled token order, true key | 0/200 >= real (max -1.377) | 0/200 >= real (max -1.330) |

- **The four key-coverage choices the solver disclosed** were each flipped (seed 2). None of them changes the rank:
  - L03 pairing offset 0 instead of dropping the stray 1: rank 1, z 3.58.
  - L03 '59' read as 52, 53 or 54: rank 1, z 5.03, 4.89 and 4.88.
  - L05 dropped: rank 1, z 4.91.
  - L10 dropped: rank 1, z 5.28.
  - Offset 0 with L05 and L10 dropped: rank 1, z 3.87.
  - Runs 2, 4 and 8 removed entirely (41 letters): rank 1, z 4.67.
- **Key-blind check.** These are the two blind Sonnet passes as written, paired naively from each line's first digit,
  with no reconciliation:
  - Pass B as read: rank 1, z 2.54.
  - Pass B with the 0->8 convention: rank 1, z 2.97.
  - Pass A with 0->8: rank 1, z 3.25.
  - Pass A as read: rank 32/201, z 1.19.

  Both passes give a rank-1 signal before anyone looked at the key; pass B does so even without the glyph convention.
  So the reconciliation did not create the signal.
- **Error figure.** The 0.239 per digit is the raw blind passes measured against the reconciled transcription, and most
  of it is one systematic confusion (the looped 8 read as 0). That was settled from the key sheet's own hand. The
  residual error of the reconciled transcription has not been measured: there is no third independent read. So 0.239
  is an upper bracket, not the honest current figure.
- **Power** at N=72 letters, 20 synthetic fr16 windows enciphered with no.25:
  - 0.239 error: 11/20 rank 1.
  - 0.10 error: 20/20.
  - 0.05 error: 20/20.
  - H-only size (51 letters) at 0.10 error: 19/20.

  The noise model is uniform digit substitution only, with no pairing slips.
- Verdict on the statistic: the solver's numbers reproduce, and the rank-1 result survives every disclosed choice and
  the key-blind passes. The reading is still fragmentary. What it establishes is that key no.25 enciphers these runs.
  It does not give a plaintext of the letter.

Grades per token, unchanged: H 62, M 40, C 0, S 0, I 0. No C grade, so the H grade rests on the key sheet, not on a
known plaintext of this letter.

## 3. Novelty search (3 Oct 2026, this session; requests: googleapis 11, be-api.us.archive.org 3, api.openalex.org 2,
api.semanticscholar.org 2, api.core.ac.uk 2, cryptiana.web.fc2.com 1, github.com 3 shallow clones)

| family | searched | result |
|---|---|---|
| (a) canonical series / catalogue | BnF *Catalogue des manuscrits français* entries surfaced by Books API (HQo4AQAAMAAJ, aG1oAAAAcAAJ, gHu4hDItOvMC, T0cMAQAAMAAJ) | catalogue description only ("avec chiffre"); no decipherment |
| (b) sender's / recipient's printed correspondence | Gomberville 1665 (NV-INTAKE, 4 copies); Books API `"a mon fils le duc de Rethelois"`, `"duc de Rethelois" 1589 Nevers lettre`, `"duc de Rethelois" chiffre`; IA fts same phrases | no printing of f.35 found; *Histoires de vies* (1996, owPi1a0vLgsC) cites fr.3416 fol.49 and 47, not 35; *Répertoire des ressources généalogiques...* (2003, pxPgAAAAMAAJ) matches "Fr. 3416" + "fol. 35" with no snippet -- a catalogue repertory, unread |
| (c) documentary editions / monographs | Boltanski, *Les ducs de Nevers et l'État royal* (2006, dsInahmnar8C) surfaced; inauthor search for 3416 / chiffre returned 0 | not read in full (gap to N4) |
| (d) holding archive | BnF catalogue item 30 (as quoted by NEVERS-VEIN scout) | "avec chiffre", no déchiffrement |
| (e) full text IA / Google Books / HathiTrust | IA be-api fts 3 queries; Books API 9 queries (incl. `"Fr. 3416" "fol. 35"`, `"fr. 3416" Rethelois`, `"bons deniers" Nevers Rethelois`); HathiTrust unreachable from cloud | nothing about this letter |
| (f) solver repos and blogs | fresh shallow clones 3 Oct 2026: el-descifrador/cabinet-noir 47b6db9, dbourdeau/cyphersolver e8b4287, aaymeloglu/unsolved-ciphers d2800bb, grep 3416 / btv1b9058240c / Rethelois / no.25; Tomokiyo nevers.htm live fetch, identical to sources/cryptiana mirror after CR strip, all 72 HTML comments read (Shift-JIS) | Bourdeau: sweep listings only (ark_shelfmarks.json, bnf_candidates.txt line 215, raw nevers.htm copy); Cabinet Noir and Aymeloglu: no relevant hit. Tomokiyo's comments on fr.3416 hold only the catalogue lines for no.30/no.32 and a note on how he spotted the key ("found while checking codes with large numbers in the Index"); no decode of f.35. Blogs: NV-INTAKE site searches |
| (g) scholarship | OpenAlex (2 queries), Semantic Scholar (2), CORE (2): "duc de Nevers chiffre 1589", "Nevers cipher Gonzaga sixteenth century letters" | only Desenclos & Lasry (1592 Henri IV letter to Nevers) and general Nevers scholarship; nothing on f.35. JSTOR: 2 rows queued, families (i) and (ii) |
| DECODE | sources/decode snapshots grepped for Français 3416 | no record (not re-queried live) |

## 4. Classification

| item | class | key | prior plaintext | prior decipherment | evidence / confidence |
|---|---|---|---|---|---|
| fr.3416 f.35r figure runs, key no.25 | **N3** | published (Tomokiyo's attribution of key no.25 to this letter, nevers.htm; the alphabet read by us from the period key sheet fr.3995 f.51r) | no, located nowhere | no, located nowhere | statistic robust (above); reading fragmentary; medium confidence in the class |

Why N3 and not N4: Boltanski 2006 (the principal modern study of the Nevers papers) has not been read for fr.3416 f.35. The
2003 *Répertoire* hit is unread. The JSTOR rows are unanswered (they do not block N3).
Next to reach N4: a full-text search of Boltanski 2006 for "3416" and "Rethelois" (owner's desk or library copy), plus one
look at the *Répertoire* page.

**Safe sentence:** "Under key no.25, which Tomokiyo identified for this letter, the figure runs at the foot of BnF
fr.3416 f.35r (the duc de Nevers to his son, c. late 1589) read as French letter fragments, graded 62 of 102 tokens H,
that outscore 200 shuffled keys at three seeds. No prior decipherment was located in the catalogue, Gomberville's 1665
*Mémoires*, Tomokiyo's pages, three solver repositories or the open scholarship indexes (searched 3 Oct 2026)."

**Unsafe sentence:** "We deciphered a previously unread letter from Nevers to his son", or any wording that presents
the runs as a readable plaintext or calls the result unread, new or first. The runs are fragments, 40 tokens are M,
and the clear text and nomenclator are unread.

## 5. Postmortem

The solver's NOTES.md already disclosed the four key-assisted choices and the look-before-control order, and it does not
over-claim. One sentence needs a qualifier: "Power at the measured 0.239 digit error" should say that 0.239 is the raw
blind-reader error against the reconciliation, an upper bracket, and that the residual error is unmeasured. I corrected
this in NOTES.md. No other file over-claims. The SECOND-OPINIONS-QUEUE row SO-NV02-F35 is filed in this session.
