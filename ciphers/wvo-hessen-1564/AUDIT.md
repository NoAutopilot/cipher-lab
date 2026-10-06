# AUDIT -- wvo-hessen-1564, f.23 cipher enclosure (WVO briefnr 1109)

## AUDIT 2 (verifier R10-WVOV, account 4, 6 Oct 2026, 10:01-10:1x UTC by date -u)

Verifier session separate from the solver (R10-WVOTX, session_01DMESDnz54WgbwPpkiXAZUY). Brief:
`.claude/briefs/runs/2026-10-06-account4-run10-jobs.md` job R10-WVOV. AUDIT 1 below is kept unchanged; where the two
differ, this section is current.

**Claim under audit** (NOTES.md "f.23 careful gloss transcription and alignment re-run", R10-WVOTX): the f.23 gloss,
transcribed in two blind passes and reconciled (`r10tx/gloss_r10.tsv`), re-aligned under PREREG-R9-WVOALIGN parameters
gives CONSISTENT piles 17 vs shuffle p95 3 (R9: 10); `r9align/key.tsv` 16 C / 12 M (was 10 / 18); decode C 142, M 115 of
257; k28 changed value a -> b at grade C.

### 1. Verdict

| Item | Class | Key source | Text | Depth | Prior plaintext | Prior decipherment |
|---|---|---|---|---|---|---|
| f.23 cipher enclosure, 10 cipher rows, 257 tiles (+1 clear "E.L.") | **N0** (unchanged) | **period** (pile-level key rebuilt by us from the leaf's own interlinear decipherment) | known (in manuscript, on the leaf; not found in print) | **D2**, about 42% (107 of 257 tiles C *and* agreeing with the gloss letter over them; pile-level grade count C 142 = 55%) | yes, in manuscript (the gloss) | yes: the gloss is the decipherment of this item |

- **Safe sentence:** "f.23 of WVO 1109 (Willem van Oranje to Landgrave Wilhelm IV of Hesse, 18 Sept 1564, HSAM Marburg)
  carries a contemporary letter-over-sign German decipherment above each of its ten cipher rows. Aligning that
  decipherment with the signs gives a partial homophonic letter key (16 sign groups at grade C, 12 at M); the enciphered
  passage, as the gloss reads it, reports that '[die] kin' fell so gravely ill ('heftig kranck') that she was bled twice and
  purged twice. The decipherment is the period one on the leaf; this is a key recovered from it, not a reading of unknown
  text."
- **Unsafe sentence:** "deciphered", "read for the first time", "previously unread", or "55% deciphered" (the 142 counts
  piles, not tiles: see 2d).

### 2. Checks run by this verifier

a. **Commits on origin/main.** R10-WVOTX's work is on origin/main (979c049f1 and the "update" commits that `tools/room.py
   --push` folded it into). The PREREG's own hashes (724553df5, add122311) no longer exist in the shared history (folded by
   the rebase, CLAUDE.md rule 6's known gap); push order is the clock instead: `PREREG-R10-WVOTX.md` landed at 09:47:22
   (eaac4ed1d, margins edit 09:47:36 f448eca69), passB 09:48:01, gloss_r10.tsv + passA 09:52:41, the scored alignments,
   key and decode 09:54:29 (979c049f1). **PREREG predates the scored run: yes.**
b. **Byte-identical re-run.** In a scratch copy: `build_pairs.py` (pairs_piles/passA/passB identical), then
   `tools/interlinear_align.py align ... --code-prefix @ --seg-bonus 0 --keep-fs --null-cost -1.0 --shuffle 1000 --seed 1564`
   for each label set: piles real 17, mean 1.39, p95 3, max 5, p 0.001; passA 15, 2.43, 5, 7, 0.001; passB 13, 1.35, 3, 6,
   0.001 -- the solver's numbers exactly. align_*.tsv, key_*.tsv, then `make_key.py` key.tsv, tile_letters.tsv and
   ciphertext.tsv all **byte-identical** to the committed files. `tools/decode_key.py ciphers/wvo-hessen-1564/r9align --check`
   exit 0 (C 142, M 115). `r10tx/gloss_r10.tsv` gloss column = `r9align/gloss_reconciled.tsv` gloss column.
c. **Control can vary on the statistic: yes.** The row-derangement shuffle moves each gloss onto another row's signs, so
   label->letter agreement across rows (CONSISTENT) can and does fall; the controls stayed flat between R9 and R10 (piles
   mean 1.46 -> 1.39, p95 3 -> 3) while every real count rose (10 -> 17, 7 -> 15, 11 -> 13): the bMAT2/bCAS shape of a
   non-test does not apply. One caveat the shuffle cannot see: the reconciler read the gloss with `r9align/crops_m/`
   (row-pair crops showing the signs) and with the R9 pile key on file, so a letter could have been nudged toward the
   key. The changes I checked by eye (2e) are letter-form facts, not key-driven, so I find no sign of that; it is recorded
   as a limit, not a fault.
d. **Per-tile check of the C grade.** make_key grades a whole pile C, so every tile in a C pile decodes at C. Of the 142
   C-pile tiles, the gloss letter aligned over the tile equals the pile's value on 107; 17 are aligner conflicts and 18
   are unaligned (`tile_letters.tsv`, statuses). Only the 107 are C at tile level; this audit uses 107 for depth.
   **k28 (a -> b at C):** all five k28 tiles opened against the gloss on the image. The two aligned ones (C03 idx 25,
   C04 idx 9) are the same triangle sign under a clear gloss "b" ("bekommen", "haben"): b is right for that shape. The
   three unaligned k28 tiles (C06 idx 2, C06 idx 12, C09 idx 3) are **not** triangles (a small looped sign, a small ring, a
   theta-like sign): the k-means pile mixes shapes, and the decode gives them "b" at grade C. Those three are over-graded;
   they are already outside the 107. R9's "a" for k28 rested on 3 of 4 misaligned positions; a C value that flips between
   runs on 2 occurrences shows the C threshold (>= 2 times on >= 2 rows) is thin for piles. Not a finding against the
   solver: the gaps section already names the sorter-settled rebuild as the fix.
   **Random C tiles:** 8 tiles drawn (Python `random.seed(20261006)` over C-pile tiles with status agrees), each cropped
   with the gloss row above it from `images/01109_p3_400full.jpg`: k12 e (C06), k03 t (C01), k22 d (C08), k28 b (C03), k26
   e (C06), k09 s (C02), k26 e (C09), k19 g (C07). **8 of 8 sit under the gloss letter the key gives** (k09's "s" is the
   round final s of "das", a shape close to the gloss b; k19's "g" is the 8-shaped g). AUDIT 1 found one-position slips in
   4 of 10 on R9's sketch gloss; none in this sample.
e. **Gloss words changed by R10-WVOTX, by eye on `r10tx/view/row_L07.jpg` and `row_L09.jpg`:** "haben das die kin so"
   (C04) and "heftig kranck worden sei das" (C05) read as the solver gives them; R9's "gaben" and "gefrid" were wrong. In
   "kin" the k is followed by a raised stroke in both places it is written (C04 end, C05 start), which looks like an
   abbreviation mark ("K'in"); the expansion is not settled here (M), and the content sentence keeps "a woman ('ir')"
   rather than naming anyone.

### 3. Novelty search delta (rule 10; only what changed since AUDIT 1)

New gloss phrases searched exactly: "heftig kranck worden", "zweimahl purgieren", "adern zweimahl schlagen" on Internet
Archive full text (be-api fts) and Google Books (API, country=US, keyed). IA: "heftig kranck worden" 10 hits, all 17th-18th
c. prose (Urlsperger's Salzburger Nachrichten, Jung-Stilling, a BSB chronicle) unrelated to 1564, Oranje or Hessen; the
other two 0. Google Books: generic matches (the API loosens quoted phrases), no volume on Oranje, Hessen or 1564.
Requests: www.googleapis.com 3, be-api.us.archive.org 4, >= 2 s apart. Class **N0 unchanged**: the item's own decipherment
is on the leaf; no search can lower that and none can raise it.

### 4. Depth (rule 4a)

- Tokens: 257 cipher tiles (+1 clear). Pile-level grades (decode_key.py): C 142, M 115, H/S/I 0. Tile-level C (pile C and
  the gloss letter over the tile agrees): **107 (41.6%)**; this is depth_pct. The residue is not name/code groups but
  letters the pile key mixes (k28-type piles) or the aligner places one off.
- **D2** (unchanged). A clause above the authentication distance reads under the signs: "das die kin so heftig kranck
  worden sei das man ir die adern zweimahl schlagen" (C04-C06), with code values reading in two contexts (k26 = e in C06
  and C09; k28 triangle = b in "bekommen" and "haben"). True sentence: *the enciphered passage reports that a woman ('ir',
  her) fell gravely ill and had to be bled twice and purged twice.* Not D3: under 80% of tokens at tile-level C, and C03,
  C07-C09 still hold uncertain gloss letters.
- Check used: re-run byte-identical; row-shuffle control (p95 3 vs 17); 8 random + 5 k28 tiles eye-checked on the image;
  two gloss rows eye-checked. Outward wording: "partially deciphered (about 40%)", only with "by the period decipherment on
  the leaf".

### 5. Postmortem and corrections

- Over-claim check on R10-WVOTX's section: wording clean (no novelty word; "the decode is a check on the key"). One figure
  over-reads in the same way AUDIT 1 found: "decode C 142" counts pile grades, and 35 of those tiles disagree with or are
  not aligned to the gloss; corrected here to 107 at tile level and noted in NOTES.md.
- status.json result row updated (depth D2, depth_pct 41.6, counts, audit_status "two audits"). No SECOND-OPINIONS-QUEUE
  row exists or is owed (class below N3). Status stays `partial`.
- No subagent; no login.


## AUDIT 1 (verifier R9-WVOV, account 4, 6 Oct 2026, 06:20-06:4x UTC by date -u)

Verifier session separate from the solver (R9-WVOALIGN, session_018jdurbcUgRBMVtqcdMv3yV) and from the sorter builder
(R9-WVOSORT). Brief: `.claude/briefs/runs/2026-10-06-account4-run9-jobs.md` job R9-WVOV.

**Claim under audit** (NOTES.md "f.23 interlinear alignment", R9-WVOALIGN, 6 Oct 2026): f.23 of WVO 1109 (Willem van
Oranje to Landgrave Wilhelm IV of Hesse, Brussels, 18 Sept 1564; HSAM Bestand 3II, Nassau-Niederlande, Korr. 1564-1565,
f.22r-24v) carries its own letter-over-sign interlinear decipherment; PREREG-R9-WVOALIGN gate PASS (pile ids 10 vs
row-shuffle p95 3); `r9align/key.tsv` 10 C / 18 M; decode C 102 M 155.

### 1. Verdict

| Item | Class | Key source | Text | Depth | Prior plaintext | Prior decipherment |
|---|---|---|---|---|---|---|
| f.23 cipher enclosure, 10 cipher rows, 257 tiles (+1 clear "E.L.") | **N0** | **period** (pile-level key rebuilt by us from the leaf's own interlinear decipherment) | known (in manuscript, on the leaf; not found in print) | **D2**, about 40% (C 102 of 257 tiles) | yes, in manuscript: the German row written letter by letter over each cipher row | yes: that same gloss is the decipherment of this very item |

Evidence quality: high for the existence of the gloss and the row pairing (checked by eye, section 2); moderate for the
per-tile key (section 2c). Confidence in N0: high, on the repository's own precedent (section 3).

- **Safe sentence:** "f.23 of WVO 1109 (Willem van Oranje to Landgrave Wilhelm IV of Hesse, 18 Sept 1564, HSAM Marburg)
  carries a contemporary letter-over-sign German decipherment above each of its ten cipher rows. Aligning that
  decipherment with the signs gives a partial homophonic letter key (10 sign groups at grade C, 18 at M); the enciphered
  passage, as the gloss reads it, reports that a woman fell so ill that she was bled twice and purged twice. The
  decipherment is the period one on the leaf; this is a key recovered from it, not a reading of unknown text."
- **Unsafe sentence:** "We deciphered William of Orange's 1564 cipher letter to Hesse" / "the f.23 enclosure has been
  read for the first time" / "previously unread". The text was deciphered in the 16th century on the leaf itself; our work
  is the alignment and the key.

### 2. Checks run by this verifier

**(a) Re-runs (rule 7).**
- `python3 tools/decode_key.py ciphers/wvo-hessen-1564/r9align --check` -> `ciphertext.tsv: tokens 257: C 102, M 155`,
  `reading up to date`, exit 0.
- `tools/interlinear_align.py align <pairs> ... --code-prefix @ --seg-bonus 0 --keep-fs --null-cost -1.0 --shuffle 1000
  --seed 1564`, re-run into the scratchpad on all three label sets:
  - piles: `shuffle control: real 10; control mean 1.46, p95 3, max 6, n 1000; p = 0.0010; real > p95: True`
  - pass A: `real 7; control mean 2.51, p95 5, max 7, n 1000; p = 0.0030; real > p95: True`
  - pass B: `real 11; control mean 1.41, p95 3, max 6, n 1000; p = 0.0010; real > p95: True`
  The solver's numbers reproduce exactly.
- **Can the control vary on the statistic?** Yes. CONSISTENT counts labels whose top aligned letter recurs on >= 2 rows;
  dealing gloss rows to the wrong cipher rows changes which letters stand over which signs, so the count moves (control
  draws range 0-6 on piles, 0-7 on pass A; a non-test would give a degenerate spread equal to the real value). Not the
  bCAS/AX-5799 shape. Caveat: on pass A the control max (7) equals the real value, so the secondary set passes only at
  p = 0.003; the primary is the clear one.

**(b) Is the German a period decipherment, and does it read as continuous text?** Viewed on `images/01109_p3_400full.jpg`
(top 1100 px, downscaled) and on ten tile crops. The German rows are written letter-spaced to sit over the signs ("m i r k o
n n e n", "w o r d e n  s e i"), so they were written after and over an existing cipher row; there is a correction above
row 1 (a "d" inserted over "unfreundtlich"), the work of someone deciphering. Same 16th-century German hand-type and ink
tone as the cipher; whether by the sender's secretary or the recipient's decipherer is not settled by the image. It is a
period decipherment (contemporary hand, on the original as received, in the recipient's archive). Rule 4 grade: the
letters it supplies to signs are **C** (known plaintext); none is H (no key sheet), and the gloss is not a reading by us.
The gloss as reconciled by the solver (`r9align/gloss_reconciled.tsv`), pasted:

```
C01 wir konnen auch [E.L. in clear] unfreundtlich
C02 en vertrauen nit vorgalten das wir
C03 sehdgevoanspzeit ztungen bekom
C04 men gaben das die kein so
C05 gefrid kranck worden sei das
C06 man ir die adern zweimahl
C07 schlagen und tausch zweimahl
C08 purgiren mussen dermassen
C09 dass ei verfruchterfed idet
C10 worden sei
```

Continuous German, with three rows (C03, C05, C09) still a sketch: "wir konnen auch E.L. unfreundtlich [?] vertrauen nit
vor[h]alten das wir ... zeitungen bekommen haben das die kein[?] so gefrid[?] kranck worden sei das man ir die adern
zweimahl schlagen und [tausch?] zweimahl purgiren mussen dermassen das ... worden sei". The verifier read on the image
"kranck worden sei das", "man ir die adern zweimahl", "schlagen", "purgiren mussen dermassen" and "worden sei" and agrees
with them. Observation, not a reading (grade M, for the careful gloss pass the folder names): "die kein so gefrid kranck"
may be "die Konigin so gefe[h]rlich kranck"; unchecked, and nothing here depends on it.

**(c) Ten random gloss-over-sign pairs by eye** (random.seed(20261006) over the 220 tiles in `r9align/tile_letters.tsv`
that carry a gloss letter; each tile boxed on the full-resolution page with the gloss row above it):

| # | tile | pile | aligner letter | status | verifier, by eye |
|---|---|---|---|---|---|
| 0 | C06_01_008 | k22 | d | agrees | d over barred Z: right |
| 1 | C01_01_024 | k01 | l | agrees | under "...tl..." of unfreundtlich; l plausible, not certain |
| 2 | C08_01_008 | k12 | e | agrees | e (of "-ren") over looped L: right |
| 3 | C03_01_027 | k28 | e | conflict:a | triangle under the gap before "bekom"; unclear |
| 4 | C06_01_014 | k22 | d | agrees | d (8-shaped d of "adern") over barred Z: right |
| 5 | C02_01_031 | k14 | i | conflict:r | sign stands under the "r" of "wir"; the pile value r is right, the aligner's i is off by one |
| 6 | C09_01_015 | k11 | h | agrees | barred h stands under "c" of "-frucht"; aligner off by one (the sign is c, as the 174 key has it) |
| 7 | C07_01_003 | k08 | c | agrees | barred II under the "h" of "sch-"; aligner off by one |
| 8 | C03_01_012 | k27 | o | conflict:a | C03 is an uncertain row; unclear |
| 9 | C06_01_020 | k02 | z | agrees | thorn-p under "w" of "zweimahl"; aligner off by one (w = thorn-p, as R9-WVOALIGN's by-eye list says) |

Result: 3 right, 1 plausible, 2 unclear, 4 where the sign is the neighbouring gloss letter's (one of them already
corrected by the pile's key value). The **pairing of gloss and cipher row is real** (every tile examined sits under its
gloss row and the by-eye values d = barred Z, e = looped L, r = one-bar cross, w = thorn-p, c = barred h recur), but the
**per-tile letters in `tile_letters.tsv` are noisy, with frequent one-position slips**, and so are the M rows of
`key.tsv` (k11 is h in key.tsv, c by eye; k02 is z in key.tsv, likely w). This does not touch the gate (the gate asks
only whether the pairing beats a wrong pairing); it limits what the C/M token counts can claim. Consequence: the C 102
figure is the aligner's, not a checked letter count; depth_pct below is set from it with that caveat.
Independent corroboration: R9-WVOX (same window, disk only) matched f.23's shapes to the 1563 key of letter 1069
(`willem-van-hessen-1567/siblings/key_1069.tsv`) at 8 of 18 same-letter pairs (permutation p95 3): p-shape = w, Mars = i,
R = s, one-bar cross = r, Jupiter-like = d, nine = a -- agreeing with the by-eye values above.

### 3. Novelty search log (rule 10; template step 2)

| Family | Searched | Result |
|---|---|---|
| (a) canonical series | Groen van Prinsterer, *Archives* 1e serie I (IA `archivesoucorre00housgoog`): ToC and full-text, read by the 26 Sept 2026 pass (NOTES.md head) | 1109 absent; 1107 printed (Lettre XCI) in clear. Not re-run today. |
| (b) sender/recipient editions | WVO (Huygens) record 1109: Brongegevens list no edition; Opmerkingen "Met een eigenhandig ondertekende in cijferschrift geschreven bijlage" -- describes the enclosure as cipher, not the gloss. Demandt, *Nassau-oranische Korrespondenzen* II: not found as a scan (R8-WVO1111: IA advancedsearch 3 queries, Google Books API 3 queries); OpenAlex "Nassau-oranische Korrespondenzen Demandt" 0 hits, Semantic Scholar 0 (this pass) | no printing of 1109's enclosure or of its gloss located. Demandt unread: **unreached** (HathiTrust is Cloudflare-blocked from the cloud). |
| (c) documentary editions for the period | covered with (a)/(b); WVO is the period's letter register for Orange | nothing |
| (d) holding archive | HSAM catalogue / Archivportal-D record of Hessian cipher keys: HTTP 503 on 2 Oct 2026 (GF-A2-3), not retried today | **unreached** |
| (e) full text: IA, Google Books, HathiTrust | phrase searches on the gloss, IA be-api fts and Google Books API (keyed, country=US), 6 Oct 2026: `"adern zweimahl"` (IA 0; GB 351, all modern botany/entomology/fiction, none 16th-c.), `"zweimahl purgiren"` (IA 0; GB 196, veterinary/medical 18th-19th c.), `"adern zweimal schlagen"` (IA 0; GB 503 error, not retried), `"zweimal purgieren"` (IA 3, GB 4: Mondeville, Therapeutische Monatshefte, Paracelsus -- unrelated), `"unfreundtlich nit vorhalten"` (IA 0, GB 0); GB `Oranien Hessen 1564 Chiffre OR Ziffern OR verschlüsselt` 0. HathiTrust full text: unreachable from the cloud (EF API gives no phrase search) | no hit on the gloss text |
| (f) solver repositories, cipher blogs | dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers re-grepped 2 Oct 2026 (Premise check (b)); Cryptiana, Cipherbrain, Cipher Mysteries site searches 2 Oct 2026 (GF-A2-3). Not re-run today | nothing on 1109 |
| (g) scholarship | OpenAlex (keyed): "Wilhelm von Oranien Landgraf Wilhelm Hessen 1564 Chiffre" 2 (Geheimschriften in sächsischen Akten der Neuzeit, 2012; a 2021 media-history paper -- titles only, neither names this letter), "William of Orange Landgrave William Hesse cipher 1564" 1 (unrelated); Semantic Scholar (keyed) the same queries: 1 unrelated, 0. JSTOR: two rows appended to JSTOR-QUEUE.tsv (family i: sender/recipient/date + cipher keyword; family ii: a quoted gloss phrase with no cipher keyword), queued, not blocking | nothing |

**Classification reasoning.** The decipherment of this very item exists: the period German written over every cipher
row on the leaf. The repository's settled practice classes such an item N0 without print (two-audit precedents:
clair1067-brienne-poland-1646, clair1108-duvergier, fr5160-letellier-1653, fr3993-gonzague-nevers-1595); the Dupuy 468
counter-precedent (an undescribed manuscript gloss, first audit declined N0) was not followed in clair1067, where, as
here, the catalogue says only that the item is in cipher. N0 stands even though nothing here was found in print; if a
second audit prefers the Dupuy 468 reading, the most it could become is N2 (plaintext known on the leaf, no prior
mapping found), never N3.

Key source (rule 10): **period** -- the key is rebuilt by us from the period decipherment on the leaf (not `ours`: no
cryptanalysis supplied any value; not `published`). Text: **known** (in manuscript).

### 4. Depth (rule 4a)

- Tokens: 257 cipher tiles (+1 clear): C 102, M 155, H 0, S 0, I 0 (aligner counts; section 2c: per-tile values noisy).
  depth_pct 39.7. Unread residue is not names/codes but letters the pile-level key mixes or misplaces.
- **D2.** At least one clause above the authentication distance reads: "kranck worden sei das man ir die adern zweimahl
  schlagen ... zweimahl purgiren mussen dermassen" (about 70 letters, a sign under each), checked by eye in section 2b/2c,
  with a code value reading in two contexts (barred Z = d in "die" and "adern", C06; thorn-p = w in "worden" and
  "zweimahl"). True sentence: *the enciphered passage reports that a woman ("ir", her) fell so ill that she had to be bled
  twice and purged twice.* Not D3: under 80% of tokens at C/H/S, and C03/C05/C09's gloss is still a sketch.
- Check used: interlinear gloss on the leaf, by eye (10-tile sample); row-shuffle control (p95 3 vs 10); decode_key.py
  --check exit 0. Outward wording: "partially deciphered (about 40%)" -- and only together with "by the period
  decipherment on the leaf".

### 5. Postmortem and corrections

- Failure named: the 26 Sept 2026 image pass ("Images opened"), its Verdict and the 2 Oct 2026 Premise check (a) recorded
  "no interlinear gloss" on f.23 and treated its German words as clear words among the signs; the NX-WVO174 transcription
  cut gloss and cipher into the same bands (likely cause of its 290 vs 335 split). R9-WVOSORT caught it while cutting
  tiles; R9-WVOALIGN tested it and already wrote a dated correction beside all three statements (kept, not deleted). This
  audit checked those three corrections against the image and endorses them; no further sentence needed correcting.
- Over-claim check on the solver's section: none found in wording (it says "check on the key; the period decipherment is
  the gloss", no novelty word). One figure over-reads: "on the tiles the 92 C-graded tokens agree with the gloss letter
  over them 72 times" is the aligner's agreement, not an eye-checked one; this audit's 10-tile sample shows one-position
  slips in 4 of 10. Noted in NOTES.md.
- No SECOND-OPINIONS-QUEUE row (class below N3). Status stays `partial`.
- Requests this pass: be-api.us.archive.org 5, www.googleapis.com 6, api.openalex.org 3, api.semanticscholar.org 3, all
  >= 2 s apart; no subagent; no login.
