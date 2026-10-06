# AUDIT -- wvo-hessen-1564, f.23 cipher enclosure (WVO briefnr 1109)

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
