# BnF Baluze 103, f.50 — Michel Le Tellier (Secretary of War) to Pierre de Marca, governor of Catalonia, April 1644

Status: open
Chéruel, Lettres du cardinal Mazarin t.1 (Dec 1642-June 1644, IA lettresducardin01maza) full text searched by this worker for "Marca" (5 Oct 2026): Marca appears only at p.628 note (his 1 Feb 1644 instruction as visiteur général), no Le Tellier letter and no decipherment of f.50; DECODE R2742 (key only, four empty TranscriptionsLists) and Tomokiyo's louisxiv0.htm ("f.50 (undeciphered)") read this session.
Check-solved re-verdict D2-BAL103T, 5 Oct 2026 (section "Check-solved re-verdict (D2-BAL103T, 5 Oct 2026)" at the end). Earlier blocker
(DECODE R2742's "Decrypted" status) resolved by D2-BAL103 and D2-BAL103T: R2742 holds the images and Tomokiyo's key table only.

Check-solved pass, 24 Sept 2026 (Sonnet, csKT/LANE N4, cap $5 shared with KT-01). Row KT-02 from
`sources/solver-diffs/2026-09-24-tomokiyo-vs-siblings.tsv` (scTOMO, LANE N4).

## Identification

- Image: Gallica `btv1b9001389d`, canvas f111 r (recto, 50r) / f112 v (verso), confirmed by the leaf's own
  "avril 1644 ... 50" dateline+foliation (eye-read at high zoom by scTOMO, not re-verified this pass).
- Native size: 4864x6996 both sides.
- Image URLs: `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9001389d/f111/full/full/0/native.jpg`,
  `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9001389d/f112/full/full/0/native.jpg` — copy-free, full
  resolution, no login. The volume's own Gallica title (found by web search this pass): "Affaires de
  CATALOGNE. — Correspondance de MARCA. Baluze 103."
- Key: Le Tellier-Marca Cipher (`sources/cryptiana/web/louisxiv0.htm`, table image
  `louisxiv_0marca1644.png`, "not using syllable representations").

## Tomokiyo (`louisxiv0.htm`), quoted verbatim

*"Le Tellier's letters use the following cipher in April to October 1644 (f.50 (undeciphered), f.171, f.189,
f.200, f.230 (deciphered on separate pages))."* — f.50 is the one leaf of this five-leaf group Tomokiyo tags
undeciphered; the other four are explicitly "deciphered on separate pages."

## DECODE finding — the blocker

`sources/decode/records-decrypted-2026-09-24.tsv` (this session's own DECODE-worker sweep, on disk, no login
used to read it) row:

```
id=2742  status=Decrypted  holder="Paris, Bibliothèque nationale de France, Baluze 103, f.51-52"
shelfmark_code=BnF_Baluze103_f50  date_range="1644 -"  plaintext_lang=French  pages=2
```

Cross-checked against `aaymeloglu/unsolved-ciphers`'s cached `catalogue/decode-catalog.csv` /
`catalogue/decode-records.jsonl` (fresh shallow clone this pass), same record: sender field "Le Tellier",
country "France", record URL `https://de-crypt.org/decrypt-web/RecordsView/2742`.

The four siblings Tomokiyo calls "deciphered on separate pages" are also in this file, and their DECODE tags
match their folio numbers exactly:

| DECODE id | holder folios | shelfmark tag |
|---|---|---|
| 2743 | f.171-173 | BnF_Baluze103_f171 |
| 2744 | f.189-191 | BnF_Baluze103_f189 |
| 2745 | f.200-206 | BnF_Baluze103_f200 |
| 2746 | f.230-233 | BnF_Baluze103_f230 |
| **2742** | **f.51-52** | **BnF_Baluze103_f50** |

For 2743-2746 the tag's folio number is the first folio of the holder string's own range (171=171, 189=189,
200=200, 230=230) — the tag and the description agree. For 2742 they do not: holder says "f.51-52", tag says
"f50". Two readings are possible: (a) this is our leaf (f.50, tagged correctly, with "f.51-52" a cataloguing
slip for "f.50-52" or similar), and DECODE holds it as already Decrypted, contradicting Tomokiyo; or (b) this
is a different, adjacent leaf that happens to generate the same tag pattern. Given DECODE's own tagging
convention on the four siblings (tag = first folio of the holder range), reading (a) is the more likely one —
the tag was very likely built from the same "f.50" locator Tomokiyo uses, and the holder string's "51-52" is
the slip, not the tag.

This cannot be resolved further from files on disk: RecordsView and DocumentsList (needed to see whether an
actual decipherment document is attached, and to check the leaf image DECODE is describing) both require a
DECODE login, and per this lane's common rules only the DECODE worker logs in — this worker does not have
DECODE_USER/DECODE_PASS access this session. No unauthenticated fetch of `de-crypt.org/decrypt-web/*` was
made (host not in this brief's list; per common rule 4, DECODE beyond files-on-disk is out of scope for a
non-DECODE worker).

## Other sources checked, 24 Sept 2026

1. **Web search.** "Le Tellier Marca 1644 chiffre déchiffré Baluze 103" and "Sanabre Le Tellier Marca 1644
   Catalogne chiffre lettre déchiffrée Baluze": both return only generic biographical pages (Wikipedia on
   Baluze, Marca, Le Tellier) and the BnF archivesetmanuscrits catalogue title for Baluze 103 itself
   ("Affaires de CATALOGNE. — Correspondance de MARCA. Baluze 103", with a snippet noting "eighty-one original
   letters addressed to Marca by the comte d'Harcourt, vice-roi of Catalonia, 14 Dec 1644-19 Oct 1645" — a
   different correspondent, not this letter). No page found naming this specific letter as solved or citing a
   reading of it in a Le Tellier/Marca/Catalonia-1644 secondary literature.
2. **Print editions named in the brief** — not opened this pass: Sanabre's *La Acción de Francia en Cataluña*,
   the printed *Lettres de Le Tellier* series, *Mémoires de Marca*, and Chéruel's *Lettres de Mazarin* t.1-2
   were not located as free full-text and not read; this is a gap in the pass, not a negative result — see
   "blocked" status. Google Books API search ("Le Tellier Marca 1644 chiffre Baluze") returned only unrelated
   sale catalogues and modern Catalan-history volumes, no snippet naming this letter.
3. **Cryptiana blog / Cipherbrain.** `louisxiv0.htm` quoted above. No scienceblogs.de/klausis-krypto-kolumne
   post found for "Le Tellier" "Marca" "chiffre" (not separately re-searched this pass beyond the KT-01 query
   pattern; treat as unchecked, not a negative).
4. **Bourdeau shallow clone.** Grepped all folder READMEs/NOTES for "marca", "baluze 103", "le tellier"/
   "letellier": the repo's `letellier/` folder is a *different* item — its own NOTES.md header reads "Le
   Tellier -> Marquis de Castelnau, 12 May 1657 — tracker item #15" (BnF fr.5160-family, cryptiana
   transcription `LeTellier_Castelnau1657.txt`), confirmed by opening the file this pass, not merely cited from
   an earlier worker's grep. `louis1615/NOTES.md` mentions "Baluze" only for Baluze 155 (a different volume,
   Louis XIII to Sabran, 1631). No Baluze 103 folder or NOTES hit anywhere in the clone.
5. **Aymeloglu shallow clone.** No dedicated folder for Baluze 103/Marca/Le Tellier 1644; the only hits are the
   cached DECODE catalogue files used above (`catalogue/decode-catalog.csv`, `catalogue/decode-records.jsonl`),
   which is the census this worker is relying on for the blocking finding, not an independent solve claim.
6. **DECODE files on disk.** See "DECODE finding" above — this is the source of the block, not a clean negative.

## Leaf check (24 Sept 2026, scTOMO)

Both sides at native resolution: recto and verso entirely in cipher, no interlinear or marginal gloss. Not
re-verified by this worker.

## Verdict

**blocked** — DECODE record R2742 (shelfmark tag `BnF_Baluze103_f50`, sender Le Tellier, 1644, 2 pages) is
tagged "Decrypted" and most likely names this very leaf, contradicting Tomokiyo's "undeciphered" tag for
fr./Baluze 103 f.50; confirming or ruling this out needs `RecordsView`/`DocumentsList` for record 2742, which
require the DECODE login this worker does not hold. No nomination line posted. Do not promote KT-02 until the
DECODE worker opens record 2742 and reports what it holds.

**flag for the lane orchestrator**: route record 2742 (`https://de-crypt.org/decrypt-web/RecordsView/2742`) to
the DECODE worker as a priority check before any further work on this target; if it does hold an attached
decipherment of Baluze 103 f.50, this is `found-solved`, not a stage-2 nomination target, and the same check
should be run before nominating any other Le Tellier-Marca-cipher leaf from `louisxiv0.htm`.

Grades: none (no reading attempted). Novelty: not assessed (rule 10 — this is a check-solved verdict, not a
verifier pass).

## Web and blog check (GF-A2-13, 3 Oct 2026)

Worker GF-A2-13 (account 2, LANE-A2PUSH), 01:31-01:3x UTC. Gate-fix only (gate already exit 0: status `blocked`,
terminal). No transcription, no key application.
(a) Plain web searches (WebSearch, standard):
1. `Le Tellier Marca avril 1644 lettre chiffrée Baluze 103 déchiffrement` -- Wikipedia (Étienne Baluze), Universalis
   (Michel Le Tellier), a Cambridge Le Tellier family tree, engraving sale pages. Nothing on this letter.
2. `"Baluze 103" chiffre OR cipher Le Tellier` -- Baluze biographies, a HAL paper (Boutier), and Cipherbrain's "Norbert
   Biermann solves encrypted letters from the 17th century" (Louvois to Lauzun, 27 May 1690: a different Le Tellier,
   a different correspondent and decade -- not this item).
3. `Le Tellier Marca cipher 1644 Catalonia decrypted letter Tomokiyo` -- HistoCrypt papers (liu.se), the Mary Queen of
   Scots coverage (Lasry/Biermann/Tomokiyo 2023), TNA "secret diplomatic message deciphered after 350 years". None
   concerns Baluze 103 or Le Tellier-Marca 1644.
4. `"Baluze 103"` + the catalogue title was covered on 24 Sept (two queries); not repeated.
(b) Site searches: `site:cryptiana.blogspot.com Le Tellier Marca` -- no Cryptiana blog page (Tomokiyo's own page
louisxiv0.htm, quoted above, remains the one source naming f.50 "undeciphered");
`site:scienceblogs.de/klausis-krypto-kolumne "Le Tellier" OR Marca 1644` -- the Biermann/Louvois post and the Louis
XIII 6 April 1635 post, neither this item; `site:ciphermysteries.com "Le Tellier" OR Marca Catalonia cipher` --
ciphermysteries.com/page/54, ?p=6866, a Moustier PDF; by the summaries none is about Le Tellier-Marca 1644.
(c) The Biermann post concerns Louvois 1690 by its own title and summary; its comment thread was not read because the
item differs by sender (Louvois, not Michel Le Tellier), recipient and date.
Result: no decipherment or plaintext of Baluze 103 f.50 on the open web or the three blogs.
Requests: WebSearch 6.

## Premise check (GF-A2-13, 3 Oct 2026)

(a) Decipherments the folder already mentions: **found in the catalogue, not opened.** DECODE R2742 (status
"Decrypted", holder "Baluze 103, f.51-52", tag BnF_Baluze103_f50, 2 pages): its documents need a DECODE login
(account-gated; not used by this worker). Tomokiyo says the four sibling letters (f.171, f.189, f.200, f.230) are
"deciphered on separate pages"; f.50 he tags "undeciphered".
(c) Physical neighbours, viewed this pass (Gallica btv1b9001389d, 600-900 px, 5 requests): canvas 110 (f.49v) blank
mount with a blank pasted slip; canvas 113 (f.51r) blank, foliated "51", with the stub of the f.50v cipher lines at
the gutter; canvas 114 (f.51v) the address leaf, docket "Lettre de M. le Tellier receue le 3 may 1644, resp. le 4
may"; canvas 115 (f.52r) a pasted slip: "Plus la lettre à M. le Cardinal du 20 may 1644 qui est dans les mesmes
cayers" (struck-through words in the slip); canvas 116 (f.52v) a pasted slip: "Il faut mettre icy les nouvelles de
Barcelone du 3 May 1644 qui sont dans les grands cayers de Catalogne. Cella regarde l'arrivée de M. de Marca à
Barcelone ..." (filing notes, about the papers' order). **Not found: no clear decipherment of f.50 on f.49v, f.51
or f.52** at this resolution. So DECODE's "f.51-52" holder string names the address leaf and two filing slips, not a
decipherment leaf; the "Decrypted" status must rest on a document DECODE holds, not on a period decipherment bound
next to the letter. The docket dates receipt to 3 May 1644 (reply 4 May), which fixes the letter to late April 1644.
(b) Other solvers' working files: **not found for this leaf.** Fresh shallow clones (3 Oct 2026): dbourdeau/
cyphersolver `targets/letellier/` is Le Tellier to Castelnau, 12 May 1657 (different item, confirmed 24 Sept); no
Baluze 103 folder. aaymeloglu/unsolved-ciphers: `baluze 103` only in catalogue/decode-catalog.csv (R2742-R2746
rows). No rendering of f.50 under Tomokiyo's Le Tellier-Marca table anywhere in either repository. The key we would
borrow (Tomokiyo, louisxiv0.htm, table `louisxiv_0marca1644.png`) is published; whether Tomokiyo or DECODE's
transcriber already applied it to f.50 is exactly what R2742's documents would show.
(d) Recipient side: **not checked further (unreachable as free full text, per 24 Sept).** The recipient is Marca;
his papers are this very Baluze series, and the docket shows Marca's office received and answered the letter. The
standard sender/recipient editions (Sanabre, *La acción de Francia en Cataluña*; Marca's correspondence) were not
located as free full text on 24 Sept and were not retried. The siblings' own separate-page decipherments (f.171ff.,
f.189ff., f.200ff., f.230ff.) are the same office's work 2-6 months later and are the calibration set for the key.
Result: no plaintext of f.50 found; the blocker stays DECODE R2742 (login needed to see its documents). Status line
unchanged.
Requests: gallica.bnf.fr 5 (IIIF image, 200 each, 2 s apart); github.com shared clones.

## fr17 re-judge (FR17-RJ2, 3 Oct 2026)

No reading on disk -- no reading: status blocked (DECODE record question). Mazarin tome I circularity check therefore not run; it applies as soon as a reading exists. No judge run (fr16 or fr17), no shuffled-decode control, no per-fold rate at a reading's N; the fr17 per-fold rates at N=138/300 are in tools/data/fr17/README.md.

## Next step (NO-CRACKS, 5 Oct 2026)

next: one browser login with `tools/decode_browser_login.js 2742 <dir>` (the DECODE login works since 24 Sept 2026, CLAUDE.md Access playbook item 3) to read record R2742's documents and see whether its "Decrypted" status carries a plaintext of f.50, ~$1. Who acts: agent. Source: this file's own blocker line ("the blocker stays DECODE R2742 (login needed to see its documents)"); written by NO-CRACKS (account 3) because tools/next_steps.py found no next-step line in this file.

## DECODE R2742 opened (D2-BAL103, 5 Oct 2026)

Worker D2-BAL103 (account 1, LANE DEFAULT-account-1-20261005-2217), 23:03-23:0x UTC 5 Oct 2026 by `date -u`. One
browser login (`tools/decode_browser_login.js 2742 <scratch> --guess-fullsize --listen`), accepted first time;
nothing decoded, no reading attempted. Credit: DECODE database (de-crypt.org, DECRYPT project); record created
22 May 2021 by DECODE user id 83 (uploader of both the images and the document); key image watermarked "S.Tomokiyo".

What R2742 holds (RecordsView/2742, DocumentsList and ImagesList for fk_id=2742, read this session):
- Metadata: name BnF_Baluze103_f50; holder "Bibliothèque nationale de France, Baluze 103, f.51-52"; sender and author
  Le Tellier; receiver Pierre de Marca; date 1644-04-15 (start year/month/day fields); type Cipher; status
  Decrypted; cipher type homophonic substitution + nomenclature; symbol sets graphic signs, alphabet, numerical
  (notes: "diacritics"); pages 2; plaintext language French; Inline Cleartext No; Inline Plaintext No;
  "Available Documents: Key"; access mode authentication required. Associated records: 0.
- Documents: 1. ID 3821 "Le Tellier-Marca Cipher (1644)", category Key, uploaded 22 May 2021, public True, file
  DOC_R2742_D3821_3821.png (72,190 bytes, sha1 bca557c67c045785c87fe0e8f1038c3f2df1ed4b). Content (viewed): an
  alphabet row a-z with numeral homophones 10-23 and graphic-sign homophones under each letter, a few nulls/
  doubles circled; "roy" and "Roine?" with two codes; "pour que qui" = 9 11 12 and "vous Barcelone ambassadeur
  catalogne faire" = 26 32 34 39 81 (codes as drawn, overlined); watermark "S.Tomokiyo". This is the Le
  Tellier-Marca 1644 table Tomokiyo publishes on louisxiv0.htm (built, per his page, from the four sibling letters
  deciphered on separate pages). Not compared pixel-for-pixel with his page's PNG (no copy on disk).
- Images: 4, uploaded 13 Jul 2021, full size served with `--guess-fullsize` (12-15 MB PNGs, not committed: folder
  30 MB rule; re-fetchable from DECODE with a login): I17097 P1 = f.50r (cipher, heading struck/flourish at top,
  ~20 lines), I17098 P2 = f.50v (cipher, ~13 lines, line-end dashes), I17099 P3 = f.51r (blank, gutter stub of the
  f.50v lines), I17100 P4 = f.51v (address/docket leaf). Viewed at thumbnail size only. sha1 P1-P4:
  59ea1b59645f..., 0e117ff441f9..., 8145cae036aa..., d3f67e0b8ece.... Each image has a Transcriptions sub-list
  (TranscriptionsList?showmaster=images&fk_id=1709N); **not opened** (the listener had already quit; a second login
  is against the single-login rule) -- ImagesList shows no transcription count, so whether any exists is unknown.

Where a plaintext of f.50 was not found: not as a DECODE document (the only document is the key), not inline
(Inline Plaintext: No), not in the record's metadata. Not checked: the four per-image TranscriptionsList pages.
So DECODE's "Decrypted" status means "key available" (Tomokiyo's reconstructed table), consistent with Tomokiyo's
"f.50 (undeciphered)": the record contradicts nothing. The holder string "f.51-52" plus a 2-page count and images of
f.50r-51v supports reading (a) of the DECODE section above: the record is this leaf, mis-foliated in its holder field.

Requests: de-crypt.org 1 login + record page + 4 thumbnails + 4 full-size images (tool auto-fetch) + 3 listener
requests (key PNG, DocumentsList, ImagesList), 1.5 s apart.

### Gaps as of D2-BAL103, 5 Oct 2026 (superseded by D2-BAL103T below)
Read so far: 0 of the f.50r-v cipher tokens (no transcription on disk, no reading attempted; DECODE R2742 carries only the key)
- f.50r-v ciphertext, never transcribed or decoded against the published 1644 table - blocker: not-attempted; Tomokiyo's table (louisxiv0.htm, also DECODE document 3821) is published and the leaf is digitised (Gallica btv1b9001389d); next: two blind transcription passes of f.50r-v line crops (tools/iiif_lines.py) then decode against the table, key credited to Tomokiyo, ~$4
- DECODE TranscriptionsList for images 17097-17100 - blocker: not-attempted; not opened this session (listener had quit, single-login rule); next: fetch the four TranscriptionsList pages in the next DECODE session that logs in for another record, ~$0.3

### Escalation as of D2-BAL103, 5 Oct 2026 (superseded by D2-BAL103T below)
- [ ] siblings: f.171, f.189, f.200, f.230 carry period decipherments on separate pages (Tomokiyo); not yet used here. Planned: use them as the calibration set for the table before decoding f.50
- [n/a] clear-pages: neighbours f.49v, f.51, f.52 viewed 3 Oct 2026 carry only a docket and filing slips, no decipherment
- [ ] known-keys: Tomokiyo's 1644 table is published (and is DECODE R2742's only document, 5 Oct 2026); planned: apply it to a transcription of f.50
- [x] print: web, three blogs, both solver repositories and DECODE checked (24 Sept, 3 Oct, 5 Oct 2026): no plaintext of f.50 found
- [n/a] key-rebuild: a published key exists, so no statistical rebuild is needed before applying it
- [ ] image-check: DECODE full-size images and Gallica native images both available; planned: line crops for the transcription passes
- [ ] retry: nothing read yet, so nothing to re-derive; planned after the first decode (rule 7 --check)
Verdict: keep going: 2 internal gaps; cheapest next: fetch the four DECODE TranscriptionsList pages in a session already logged in, ~$0.3; then transcribe f.50r-v and apply Tomokiyo's table, ~$4

Status word: left `blocked` for the orchestrator to send a check-solved re-verdict, since the DECODE blocker named at the
top is gone and no plaintext of f.50 was found in R2742. (Superseded by D2-BAL103T below: status `open`.)

## DECODE R2742 TranscriptionsList (D2-BAL103T, 5 Oct 2026)

Worker D2-BAL103T (account 1, LANE DEFAULT-account-1-20261005-2217), 23:39-23:40 UTC 5 Oct 2026 by `date -u`. One browser
login (`tools/decode_browser_login.js 2742 <scratch> --fetch-page <4 URLs>`), accepted first time (page JSON
`IS_LOGGEDIN:true`); nothing decoded. Credit: DECODE database (de-crypt.org, DECRYPT project).

| Image | Page | Leaf | TranscriptionsList?showmaster=images&fk_id= | Result |
|---|---|---|---|---|
| 17097 | P1 | f.50r | 17097 | "No records found" (master: IMG_R2742_I17097_17097.png, last modified 7/13/21, status Ok) |
| 17098 | P2 | f.50v | 17098 | "No records found" (same master shape, 7/13/21) |
| 17099 | P3 | f.51r | 17099 | "No records found" |
| 17100 | P4 | f.51v | 17100 | "No records found" |

So R2742 holds no transcription of any page: no ciphertext transcription, no plaintext, by anyone. With D2-BAL103's
finding (one document, the key table; Inline Plaintext No) the whole record is: four images plus Tomokiyo's 1644 key.
Its "Decrypted" status reflects the key, not a reading of f.50. Saved pages stay in the worker's scratch dir (not
committed: nothing in them beyond the table above, and they carry the account name).

Side observation (catalogue file on disk, no login): DECODE R2775 (`sources/decode/records-decrypted-2026-09-24.tsv`
line 764; tag BnF_Baluze343_f31, Gaston d'Orléans 1644) carries the identical holder string "Baluze 103, f.51-52". The
string looks copied between records, which supports reading (a) above: R2742's "f.51-52" is a holder-field slip, and
R2742 is f.50 (its images show f.50r-51v). R2775 itself not opened (single-login rule; a different item).

Requests: de-crypt.org 1 login + record page + 4 thumbnails (tool auto-fetch) + 4 TranscriptionsList pages, 1.6 s apart.

## Web and blog check (D2-BAL103T, 5 Oct 2026)

(a) Plain web searches (WebSearch): 1. `Le Tellier lettre à Marca avril 1644 chiffre déchiffrement` -- BnF catalogue
records (Français 4219: Marca to Le Tellier 1650-51, a later, different set; Français 4140-41), ARCSI key PDF, Persée
authority, Wikipedia. Nothing on f.50. 2. `"Baluze 103" chiffre OR cipher OR "de-crypt"` -- unrelated cipher pages
(dcode.fr, a GitHub "103cipher"), Wikipedia. Nothing. 3. `Le Tellier Marca 1644 cipher solves Claude OR GPT` (model-solve
family) -- HN/36kr/dev.to model-solve announcements (other items: Cyphral Distich, Napoleon letter, a WWI cipher),
aaymeloglu's repo (Forster 1644, a different item), Bourdeau's index. None about Le Tellier-Marca. 4. `BnF Baluze 103 f.50
Le Tellier Marca Catalogne 1644 lettre chiffrée` (folder title) -- Gallica btv1b9001389d (the volume itself) and BnF
catalogue records for other volumes. Nothing.
(b) Site searches: Cipherbrain (`site:scienceblogs.de klausis-krypto-kolumne Le Tellier Marca 1644`) -- Biermann/Louvois
1690 post (different item, read 3 Oct), Thirty Years' War unsolved list, Tomokiyo-list post on a king's letter; none this
letter. Cryptiana blog (`site:cryptiana.blogspot.com Le Tellier Marca`) -- only the Le Tellier-Castelnau 1657 solution
(different item); `cryptiana.blogspot.com/2026/` fetched and grepped: no "Marca". Tomokiyo's louisxiv0.htm re-fetched
5 Oct 2026: text unchanged, "f.50 (undeciphered)". Cipher Mysteries (`site:ciphermysteries.com Le Tellier Marca
Catalonia 1644`) -- one unrelated Voynich page. (c) No plausible hit about this letter, so no comment thread to read.
Requests: WebSearch 7; cryptiana.blogspot.com 1; cryptiana.web.fc2.com 2 (one 302 to https); archive.org 2.

## Check-solved re-verdict (D2-BAL103T, 5 Oct 2026)

Six sources, this session unless stated:
1. Web: four queries above, nothing on f.50.
2. Print: Chéruel, *Lettres du cardinal Mazarin* t.1 (1872, Dec 1642-June 1644; IA `lettresducardin01maza`, djvu text,
   2.8 MB) grepped for "Marca": index entry "Cité p. 628, note" and the p.628 note only (Marca named visiteur général,
   instruction of 1 Feb 1644 in "manuscrit ... fr. A 169" as the OCR reads it, f.83v-93r). No Le Tellier-to-Marca letter of April 1644, no
   cipher text and no decipherment. Chéruel prints Mazarin's own letters, so this is a search of the nearest printed
   ministerial series for the months, not the sender's own edition: no printed edition of Le Tellier's 1644 letters to
   Marca is known to this folder. Sanabre, *La acción de Francia en Cataluña* (1956), the one modern study of the
   correspondence, is not free full text and was not opened by this worker or any earlier one; a decipherment of f.50 in
   it is possible but nothing points to one (Tomokiyo, who built the key from the four siblings, still tags f.50
   undeciphered).
3. Community lists: Tomokiyo louisxiv0.htm ("f.50 (undeciphered)"), Cryptiana blog 2026, Cipherbrain, Cipher Mysteries:
   no reading of f.50.
4. DECODE: R2742 = four images + Tomokiyo's key table; Inline Plaintext No; all four per-image TranscriptionsLists empty
   (D2-BAL103 and this worker). No plaintext of f.50.
5. Bourdeau (dbourdeau/cyphersolver, shallow clone, last commit 5 Oct 2026 17:49 -0500): grep for Baluze 103 / Le
   Tellier-Marca / R2742: no hit (its `letellier/` target is Castelnau 1657).
6. Aymeloglu (aaymeloglu/unsolved-ciphers, shallow clone, last commit 27 Sept 2026): only `catalogue/decode-catalog.csv`
   rows R2742-R2746 (the DECODE census), no working folder or reading.

**Verdict: open.** No decipherment or plaintext of Baluze 103 f.50 found in print (Chéruel t.1), on the web or the three
blogs, on DECODE (key only, no transcriptions) or in either solver repository. The key is published (Tomokiyo,
louisxiv0.htm; also DECODE R2742 document 3821, credit Tomokiyo), so this is a key-application job, not cryptanalysis.
Grades: none (no reading). Novelty: not assessed (rule 10).

## Remaining gaps (D2-BAL103T, 5 Oct 2026)
Read so far: 0 of the f.50r-v cipher tokens (no transcription on disk, no reading attempted; DECODE R2742 carries only the key, no transcriptions)
- f.50r-v ciphertext, never transcribed or decoded against the published 1644 table - blocker: not-attempted; Tomokiyo's table (louisxiv0.htm, also DECODE document 3821) is published and the leaf is digitised (Gallica btv1b9001389d); next: two blind transcription passes of f.50r-v line crops (tools/iiif_lines.py, about 33 lines, 2 passes + 1 reconciliation) then decode against the table, key credited to Tomokiyo, ~$4

## Escalation (D2-BAL103T, 5 Oct 2026)
- [ ] siblings: f.171, f.189, f.200, f.230 carry period decipherments on separate pages (Tomokiyo; DECODE R2743-R2746); not yet used here. Planned: use them as the calibration set for the table before decoding f.50
- [n/a] clear-pages: neighbours f.49v, f.51, f.52 viewed 3 Oct 2026 carry only a docket and filing slips, no decipherment
- [ ] known-keys: Tomokiyo's 1644 table is published (and is DECODE R2742's only document); planned: apply it to a transcription of f.50
- [x] print: web, three blogs, both solver repositories, DECODE (record, documents and all four TranscriptionsLists) and Chéruel t.1 checked (24 Sept, 3 Oct, 5 Oct 2026): no plaintext of f.50 found
- [n/a] key-rebuild: a published key exists, so no statistical rebuild is needed before applying it
- [ ] image-check: DECODE full-size images and Gallica native images both available; planned: line crops for the transcription passes
- [ ] retry: nothing read yet, so nothing to re-derive; planned after the first decode (rule 7 --check)
Verdict: keep going: 1 internal gap; cheapest next: transcribe f.50r-v (two blind passes on line crops + reconciliation) and apply Tomokiyo's 1644 table, calibrated on a sibling, ~$4
