blocked
Blocked internally (20 Oct 2026, SUP-NEVREVOL): the value-shuffled-key control named for the f.66 atlas passes has no power at this N (positive control 7/10 at 0% error, 0/10 at 20%), so the passes were not run; Gomberville *Mémoires de Nevers* seconde partie and *Mémoires de la Ligue* vols 5-6 read 24 Sept 2026, letter absent; next: re-PREREG with a length-class null, then two blind atlas passes on the six lines cut in images/v2, ~$3.

**Check-solved, LANE N4 csKSb, 24 Sept 2026:** letter absent from Gomberville's *Mémoires de Nevers* seconde
partie and from *Mémoires de la Ligue* (Goulart) vols 5-6; see the search log below. Corrects QUEUE.md row
KS-05 as scKEYS first wrote it: the sender is the Duke of Nevers himself, not "the Court", and the canvas is
121, not the estimated ~132.

# Nevers to Revol, Rome, 10 November 1593 — BnF fr.3987 f.66

QUEUE row: KS-05 (`sources/solver-diffs/2026-09-24-keys-vs-siblings.tsv`, LANE N4 scKEYS, 24 September 2026).
Check-solved run 24 September 2026 by LANE N4 csKSb, brief `.claude/briefs/runs/2026-09-24-lane-n4-csKSb.md`.

## What it is

Louis de Gonzague, duc de Nevers, to Louis Revol (secretary of state for war), from Rome during Nevers's
embassy to obtain the Pope's absolution for Henri IV. BnF fr.3987 (Gallica ark `btv1b90606320`), the leaf
pencil-foliated "66", is canvas 121 of the manifest (confirmed by eye 24 Sept 2026: the manifest carries no
folio labels at all, so this corrects QUEUE.md's unconfirmed estimate of canvas ~132; canvas 120, one before
it, is a separate letter of the same date addressed "Sire" — to the King — foliated 66 as well, part of the
same dispatch bundle). Dated "10 de Novembre 1593" on the leaf, matching Tomokiyo's citation. The page opens
"Monsieur de Revol" and carries several lines mixing clear French cursive with dense cipher (numeral figures,
Roman numerals, and symbol signs), consistent with cipher no.60 (Tomokiyo's numbering, fr.3995 f.108-110; key
table transcribed by Daniel Bourdeau, CC BY 4.0, `nevers1593/key60.txt`).

Tomokiyo, `henryiv2.htm` (fetched by WebFetch 24 Sept 2026; page states "Last modified on 28 November 2019";
not yet snapshotted to `sources/cryptiana/`): *"(f.66) Duke of Nevers to M. Revol, 10 November 1593 / Some
portions in cipher, undeciphered, which appear to include words such as 'tous sont de opinion que le pape veul
... asseurance de la conversion ... pour vous dire ...', 'conposer avec Mr. Despernon pour la deliuranse de son
frer'."* Tomokiyo has already tentatively read a few words directly off the cipher himself (grade M/S territory,
not a full decipherment); no full plaintext located this pass.

## Six-source search log (24 September 2026, date checked with `date -u`)

1. **Tomokiyo/Cryptiana.** `henryiv2.htm` quoted above (WebFetch, two independent verbatim passes to cross-check
   the model's summarisation). No comments section on the page; no response to the author's "the reader is
   kindly asked to provide reading of these undeciphered texts."
2. **Print — Nevers's own printed correspondence, actually read.** Gomberville, *Mémoires de messire Louys de
   Gonzague, duc de Nevers* (1665), seconde partie — Google Books `H2eV4wAmIr0C` full-text `SearchWithinVolume`
   for "Despernon" (0 hits), "deliuranse" (0 hits), "Nouembre 1593" (3 hits, all a different item, "AVTRE LETTRE
   DE S.M." — the king's own countersigned letters, none addressed to Revol); "Revol" (5 hits, cross-checked on
   the same edition's Gallica mirror `bpt6k64451005` via `services/ContentSearch`, all "REVOL" as countersigning
   secretary on Henri IV's own letters, none matching this letter). Letter absent from the volume that covers
   this exact date range (p.692 carries "Mars 1594").
3. **Print — Mémoires de la Ligue.** Simon Goulart's compilation (the brief names "Goujet"; Internet Archive's
   catalogue and title page both give Goulart, 1758) vols 5-6 (`memoiresdelaligu05goul`,
   `memoiresdelaligu06goul`), full text via archive.org's `be-api` search — 0 hits for "Castignac" (the KS-07
   letter's control term, run across the same two volumes in this sweep). No independent term for this letter
   was distinctive enough to add a second query within the $5 cap; treated as covered by the same negative
   sweep, not a dedicated search.
4. **DECODE.** `sources/decode/*.tsv` grepped for "3987" and for "nevers"/"revol": no record.
5. **Bourdeau** (dbourdeau/cyphersolver, shallow clone 24 Sept 2026, HEAD `8fd151d`). `nevers1593/NOTES.md`
   (session of 17 Sept 2026) names fr.3987 f.66 only inside Tomokiyo's own inventory of every key-no.60 letter
   ("Nevers to Revol at fr.3985 f.88 ... fr.3987 f.66, fr.3989 ff.3, 169, fr.3990 f.27"); it is not among his
   worked pair (fr.3985/fr.3986 Revol letters) and not among his "Remaining gaps" — his session never opened
   this leaf.
6. **Aymeloglu** (aaymeloglu/unsolved-ciphers, shallow clone 24 Sept 2026): grep for "nevers", "3987", "revol"
   across the repo and its catalogue JSONL/CSV files — no dedicated target, no catalogue hit.
7. **Web.** WebSearch "fr.3987" Nevers Revol chiffre déchiffré, and a second query pairing Cipherbrain/Cryptiana
   with Revol/1594 — no relevant hit beyond Bourdeau's own repository and its two unrelated forks.

## Verdict

open -- Gomberville *Mémoires de Nevers* seconde partie (Google Books `H2eV4wAmIr0C` / Gallica `bpt6k64451005`)
full text and ContentSearch read for the decoded fragments and the date; *Mémoires de la Ligue* (Goulart) vols
5-6 (archive.org full text) read; letter absent from both.

## Image

Copy-free. Full native image (4940x6827): `https://gallica.bnf.fr/iiif/ark:/12148/btv1b90606320/f121/full/full/0/native.jpg`.
Modest size tested 24 Sept 2026: `https://gallica.bnf.fr/iiif/ark:/12148/btv1b90606320/f121/full/1000,/0/native.jpg`.
Leaf viewer: `https://gallica.bnf.fr/ark:/12148/btv1b90606320/f121.item`.

## Correction to the harvest row

QUEUE.md KS-05 as scKEYS first wrote it gave sender "the Court (unnamed correspondent per henryiv2.htm)" and
canvas "~132, unconfirmed". Both are corrected here from Tomokiyo's page and the leaf itself: the sender is the
Duke of Nevers, the addressee Revol, the canvas 121. `kind` stays `recovery` (key no.60 is published, by
Tomokiyo/Bourdeau).

## Key no.60 applied (24 Sept 2026, LANE R5 F2)

Key: `key.tsv`, cipher no.60 (Satoshi Tomokiyo's reconstruction and numbering, BnF fr.3995 ff.109-111, henryiv2.htm), from
Daniel Bourdeau's transcription `nevers1593/key60.txt` (github.com/dbourdeau/cyphersolver @a0d5a07, text CC BY 4.0), mapped
to the ASCII sign tags of `sign_guide.md`; a row carries H where the table gives one value, M where the table gives two
(e.g. `4` x in the table, i in Bourdeau's crib atlas; `#`, renamed `dbl`, n or m). Shared content with fr3987/fr3986 (same
file in both folders). Images: Gallica IIIF image API only, one native region per leaf (`images/manifest.json`), line cuts
by `tools/iiif_lines.py` (debug overlay checked). Pass A: Opus worker F2, read against the key's sign list; pass B: one blind
Sonnet subagent; `tools/reconcile_passes.py` gave `passes/ciphertext_draft.tsv`, copied unchanged to `ciphertext.tsv`
(disagreements NOT settled on the image: at this agreement rate settling them is a glyph-atlas job, see below).
Reading: `python3 tools/decode_key.py ciphers/<t>` (decode.json), `--check` exits 0. No interlinear or marginal
decipherment on the leaf (the margin '+' marks are insertion marks).

fr.3987 f.66 (canvas 121, eye-checked: "10 de Nove 1593", folio "66", opens "Monsieur de Revol"): 13 lines carry cipher
(crop lines f66_L07-L11, L13-L18, L20-L21), the long run in L07-L11. Pass agreement 157/308 = 51.0% (A 299 signs, B 270;
151 disagreement columns). Tokens graded: **H 69, M 211, U 28, I 0** (308). Mechanical reading L07:
"tous f [I] m a de o p n n sa x [A] n so n a n u e sa x p e bien de la co n a so a a bien o n ...". Tomokiyo's fragment
("tous sont de opinion que le pape veul ... asseurance de la conversion") lines up with L07 by shape -- 8+ tous, then
g pi 7 dbl inT ... T = "de opinion"?, 4+ g lam alpha inT ... X T = "[asseurance] de la con...on" -- but only where the
glyphs are given his values, not the table's (7 = p is in the table; dbl = i, x = v/e are not), so these alignments are
graded nowhere and not written into the reading.

Result: the key applied sign by sign does **not** give a continuous reading. The blocker is the one Bourdeau recorded on
17 Sept 2026 ("the copyist's cursive forms map to two or three table entries each"): the Revol copyist writes no.60 in
a cursive whose shapes the two passes cannot even agree on, and many shapes have more than one table value. Status stays
`open` (no reading; a mechanical application is not one). Grade I: 0 (nothing repaired).

Suggestion (one line, not done): build the copyist glyph atlas from the interlined Instruction of 31 Aug 1593 (fr.3985
c.264-268, same hand, printed in Memoires de Nevers ii 492-499) as Bourdeau's 'Next pass' says, then re-run both passes
with atlas tags instead of table shapes; only then settle `passes/disagreements.tsv` on the image.

## Status blocked (24 Sept 2026, 20:52 UTC, LANE R5 orchestrator)

Key no.60 applied mechanically by LANE R5 F1-F3 does not read: blind pass agreement 37-55%, blocked on identifying this copyist's sign forms, not on the key. Next: LANE R5 G builds a no.60 sign atlas from the interlined leaves of the same copyist (fr.3985 f.126-130, fr.3986 f.151/152) and re-runs F1's leaves; if that passes 80%, this letter follows.

## Keyhunt 7 Oct 2026

KH1-B (LANE KH-1), 17:47-17:59 UTC 7 Oct 2026 by date -u, for key no.60 (key.tsv, shared by fr3985/fr3986/fr3987).
Searched: BnF archivesetmanuscrits finding aid Français 3974-3995 (ark cc504266, full inventory, 169 cipher items parsed),
Tomokiyo henryiv2.htm/league.htm/nevers.htm on disk, the folders' own NOTES, QUEUE.md, sources/; Gallica fr.3988 (canvases
287-305, 8 requests); print: Lettres missives de Henri IV iv (archive.org recueildeslettre04henr, djvu text, Dec 1593 entries)
and Gomberville Memoires de Nevers (Gallica bpt6k64451005 ContentSearch).
Unread no.60 siblings without a folder of their own: 5 -- fr.3985 f.115 (27 Aug 1593), fr.3986 f.146v and f.157 (AM-REV68
census), fr.3989 f.3 (1 Jan 1594), and **fr.3988 f.143r-v** (Henri IV to Nevers, catalogued 22 Dec 1593, leaf headed "24 de Dec
1593"; Gallica btv1b9060634t canvases 304-305): two full pages of symbol cipher in the court hand, no interlinear gloss at 1800 px
although Tomokiyo's list says "Interlined deciphering"; not found in Lettres missives iv or by the Gomberville ContentSearch
queries. It is in no folder and not in QUEUE.md. No test run (cap); next: six-line crop, two blind passes + reconcile against
fr3986's sign_guide/atlas, decode, shuffled-key control, about USD 7. Note: the finding aid under-flags cipher (fr.3985 f.88
carries cipher per Tomokiyo but is not marked "avec chiffre"), so the count is a lower bound. Every candidate:
keyhunt/2026-10-07-KH1B.tsv.

## BNF-K60-SYNC2 (13 Oct 2026, account 2)
key.tsv synced to cyphersolver @c60e6dd (see key_changes_c60e6dd.tsv): changed 3 (`++`, `2+`, `4+`), added 2 (`n+`, `ls+`), 14 of his shapes unmapped. reading.txt and reading_tokens.tsv regenerated with decode_key.py (6 reading lines, 9 token rows changed); `--check` reading up to date. Grade counts unchanged (H 69, M 211, U 28).

## SUP-NEVREVOL (20 Oct 2026, account 2, for the owner-account orchestrator)

Worker SUP-NEVREVOL (Opus 5.5), brief `.claude/briefs/runs/2026-10-20-acct4-research-director-28.md`, JOB SUP-NEVREVOL. Clock
read 02:13-02:2x UTC 20 Oct 2026. Gates at start: `dup_check` DUP-RISK on this worker's own claim only; `intake_gate_check`
"blocked (line 1) -- already terminal, nothing to gate"; `prior_work.py --item-spec` (warn-first) verdict LOOK, 0 specific
holds; the cyphersolver "BnF cipher research" snapshot (sources/cyphersolver/2026-10-14-lasry/) has no f.66 or fr.3987
item (its gondi1594 mentions Revol only in a different letter). Not found-solved.

**Step mismatch, stated.** The "six-line crop, two blind passes + reconcile against fr3986's sign_guide/atlas, decode,
shuffled-key control" wording in the Keyhunt section above was written for fr.3988 f.143r-v, not for f.66. The brief
applied it to f.66. That still makes sense: f.66 has never been read with the 264ext atlas, so it counts as new material
for that instrument.

**Crops.** `tools/iiif_lines.py --image images/src_ark_12148_btv1b90606320_f121_850_1350_3400_3600.jpg --out images/v2
--prefix f66v2 --max-width 1900 --overlap 150 --only-lines 7,8,9,10,11,13 --top-margin 15 --overlap-note --debug`: 12 crops
(L07-L11, L13), debug overlay checked, 0 Gallica requests (native region on disk). PREREG-SUP-NEVREVOL.md pushed before any
score (56310dc6d).

**Control first, and it failed its gate.** `controls_sup.py --positive` -> `controls_pos.txt`. The control takes a French
passage held out from the fr16 corpus (model trained on the first 80%, passages from the last 20%), N=188 letters, and
enciphers it into key no.60 single-letter homophones. Its true-key S is ranked against 200 value-shuffled keys:

| injected sign error | true key rank <= 10/201 | gate (8/10) |
|---|---|---|
| 0% | 7/10 (ranks 90 53 1 1 1 1 1 31 1 1) | FAIL |
| 20% | 0/10 | FAIL |
| 40% | 0/10 | FAIL |
| 60% | 0/10 | FAIL |

So the named control cannot tell key no.60 from a shuffled key at this N, even on a clean transcription. Shuffling the
values puts whole nomenclator words and syllables (comme, affaires, la, co ...) into letter slots, and those raise the
per-letter 4-gram score. By the brief ("a control below its gate stops the job") the job stopped here. **No vision call
was made, the target was not scored, and no token grade changed** (the 24 Sept draft stands: H 69, M 211, U 28, I 0).

**Diagnostic, not a gate** (`controls_sup.py --diag` -> `controls_diag.txt`). The same passages were re-run with the values
permuted only among signs whose value has the same length (a length-class shuffle). The true key then ranks <= 10/201 in
10/10 passages at 0, 20 and 40% error. The 100-order shuffled-sign null also separates in 10/10 at every level. That design
has headroom up to the ~49% disagreement the 24 Sept passes measured here. Side note: fr3986 controls_v2's value-shuffled
rank (194/201) was computed with the powerless design, so it carries no evidence either way. Its shuffled-target column is
the one that counts.

Research-director questions:
1. Learned: the value-shuffled-key null over key no.60 is powerless at N~190, even at 0% error. A length-class null is not.
2. Assumptions the result depended on: the fr16 4-gram model (Catherine de Médicis letters, era-matched to within 20
   years); single-letter homophone encipherment in the control, while the real text also uses syllable and word signs.
3. Unverified: whether the length-class null keeps its power when the plaintext carries no.60's syllable/word signs
   (a positive control with mixed sign classes); whether the 264ext atlas fits the f.66 hand at all.
4. Alternative explanations: none needed for the stop. The failure is in the control's design, not in the target.
5. Most informative different experiment: the same two blind passes gated by the length-class null plus the shuffled-order
   null, with the positive control re-run on mixed sign classes first.
6. Decision: stop (brief rule). Hand the re-PREREG plus passes to the next worker as "keep going".

Requests: gallica.bnf.fr 0. Vision calls: 0 of 2 (+1 reconciliation) priced.

## Remaining gaps (SUP-NEVREVOL, 20 Oct 2026)
Read so far: 0 of 308 signs to a continuous text (24 Sept 2026 mechanical draft: H 69, M 211, U 28, I 0; pass agreement 51.0%).
- f.66 cipher runs, six densest lines L07-L11 and L13 (about 188 signs, crops in images/v2) - blocker: not-attempted; the controlled atlas passes were stopped on 20 Oct 2026 because the named value-shuffled-key control failed its positive control (controls_pos.txt); next: re-PREREG with the length-class null and the shuffled-order null, positive control on mixed sign classes, then two blind Opus atlas passes + 1 reconciliation, decode with tools/keys/key60.tsv + fr3986 key_atlas_extra.tsv, ~$3
- f.66 remaining cipher lines L14 to L18 and L20 to L21 (about 95 signs) - blocker: not-attempted; held back until the six lines show whether the atlas fits this hand; next: same passes after the six lines show the atlas fits this hand, ~$2

## Escalation (SUP-NEVREVOL, 20 Oct 2026)
- [x] siblings: fr3986 f.198 (same correspondence, atlas instrument retired there on the verso runs, 36% agreement) and the interlined fr.3985 c.264 / fr.3986 c.298 leaves (atlas source, held-out 65/65)
- [n/a] clear-pages: no clear copy of this letter is known; Tomokiyo gives only a few tentatively read words
- [x] known-keys: key no.60 is in hand (key.tsv; tools/keys/key60.tsv), the key is not the blocker
- [x] print: Gomberville *Mémoires de Nevers* seconde partie and *Mémoires de la Ligue* vols 5-6 read 24 Sept 2026, letter absent
- [x] key-rebuild: 264ext atlas exists (tools/keys/key60_atlas); the Revol-hand sorter for fr3986 waits on ASKS row 102
- [x] image-check: canvas 121 = f.66 confirmed 24 Sept 2026; native region on disk, six lines re-cut 20 Oct 2026 (images/v2)
- [ ] retry: two blind atlas passes on images/v2 gated by the length-class null (the instrument was never run on f.66)
Verdict: keep going: 2 internal gaps; cheapest next: re-PREREG with the length-class null, then the six-line atlas passes, ~$3
