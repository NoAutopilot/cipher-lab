open

# fr.3986 f.198 (Nevers -> Revol, 23 Oct 1593) — Louis de Gonzague, duc de Nevers, to Louis Revol

Status: **open**

Checked by LANE N4 csKSa (check-solved), 24 Sept 2026, following `.claude/briefs/check-solved.md` and
`.claude/briefs/runs/2026-09-24-lane-n4-csKSa.md`. Row KS-03 from
`sources/solver-diffs/2026-09-24-keys-vs-siblings.tsv`.

## 1. What is established

- BnF fr.3986, same "Collection Mémoires de la Ligue" Rome-embassy series as fr.3985. Gallica ark
  `btv1b9060631k` (481 canvases, all "NP").
- Sender: Louis de Gonzague, duc de Nevers. Recipient: Louis Revol.
- Key: Tomokiyo's no.60, same as fr.3985 (see that target's NOTES.md for the key description). Kind:
  **recovery**.

## 2. Leaf confirmation (this session)

The TSV's canvas estimate (397, from a ~1.7-2x-folio guess) was explicitly flagged unconfirmed -- Bourdeau's
own session never reached this canvas (his fetcher was throttled, HTTP 429, and stopped at c.388). Confirmed
this session:

- Canvas 397: no visible folio stamp on the recto itself (top-right corner is blank/cropped at this
  resolution), but the **facing verso, canvas 398, is stamped "199"** top right
  (`images/probe_c398.jpg`, `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060631k/f398/full/,1000/0/native.jpg`)
  -- confirming canvas 397 = **folio 198**, matching KS-03 exactly.
- Canvas 397 (`images/f198_canvas397_try.jpg`,
  `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060631k/f397/full/,1000/0/native.jpg`) carries running clear
  French text with short cipher passages inserted inline (not a full-page cipher block like fr.3985's two
  leaves) -- e.g. one line of Tomokiyo's no.60 symbol/figure mix, `images/f198_crop_mid.jpg` (native crop,
  `.../f397/0,2500,4948,1200/2200/0/native.jpg`): "...45 10 5 H p 4 61 g d H v q 11 3 7 d + o 4 q 11 3 6 g 4 44
  4T...". Margin "+" marks appear beside some lines (insertion/correction marks, not a decipherment). Checked a
  second high-res crop of the page's top third (`images/f198_crop_top.jpg`,
  `.../f397/0,450,4948,1300/2200/0/native.jpg`): pure clear text there, no cipher, no interlinear gloss over
  any cipher group anywhere checked on this leaf (the Thurloe/Birch/Gondi check).
- Could not independently confirm the date "23 Octobre 1593" from the crops taken (the date line, if present,
  is likely at the top of the letter's first leaf, not on f.198 which reads as a continuation page); the
  folio-198 identification itself is solid via the facing-verso stamp.

## 3. Six-source check-solved sweep

Same sweep as fr.3985 (see that target's NOTES.md section 3 for full detail on each source); result for this
specific letter:

1. **Web**: no hit for fr.3986 f.198 specifically.
2. **Print**: Gomberville seconde partie (Google Books `H2eV4wAmIr0C`) search-within for "Revol" (5 hits, none
   dated Oct 1593) and "Octobre 1593" (not separately queried this pass -- see gap note below); Berger de
   Xivrey vol.3 (archive.org `recueildeslettre03henr`) and Memoires de la ligue v.5-6 (archive.org
   `memoiresdelaligu05goul`/`06goul`) full-text "Revol" hits are all different letters (see fr.3985 NOTES.md).
   Letter absent from all three as far as searched.
3. **Cryptiana**: `nevers.htm` names no.60 only generically ("used in many letters in BnF fr.3985 etc."),
   `henryiv2.htm` not cached, not fetched this session.
4. **DECODE**: `sources/decode/` grepped, no hit.
5. **Bourdeau**: `nevers1593/NOTES.md`, "Remaining gaps", verbatim: "fr. 3985 f. 88 (21 Aug), f. 115 (27 Aug,
   one line), f. 176 (2 Sept, no. 88/94), **fr. 3986 f. 198 (23 Oct, no. 101)** - blocker: not-attempted;
   located and cut but never transcribed; key no. 60 is fully in hand." His session located and cropped this
   leaf but never transcribed or decoded it.
6. **Aymeloglu**: repo grepped for "3986"/"Revol"/"Nevers", no hit (his Nevers-cipher rows are fr.3623, fr.3616,
   fr.3975, fr.3979, fr.3976 -- different items).

**Gap for the next pass**: an "Octobre 1593" / "23. iour d'Octobre" date-phrase search in Gomberville was not
run this session (budget); worth a quick follow-up before this leaf is transcribed.

## Verdict

KS-03: **open -- Gomberville seconde partie (Google Books H2eV4wAmIr0C) search-within read for "Revol", Berger
de Xivrey Recueil des lettres missives de Henri IV vol.3 (archive.org recueildeslettre03henr) full-text read for
"Revol", Memoires de la ligue (Goujet) v.5-6 (archive.org memoiresdelaligu05goul/06goul) full-text read for
"Revol", letter absent from all three; Bourdeau's own "not-attempted" gap list confirms unread.**

Grade: no reading exists yet. Kind: **recovery**. This session does not apply the key or read the letter.

## Credit

Key no.60: Satoshi Tomokiyo (`nevers.htm`), Daniel Bourdeau (CC BY 4.0, `key60.txt`; also the folio-198
location, cropped but unread in his session scratch).

## Next step (one line)

Run the "Octobre 1593" date-phrase search in Gomberville before transcribing; then transcribe against
`key60.txt` (LANE R5), noting the leaf mixes clear and cipher rather than being solid cipher throughout.

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

fr.3986 f.198 (canvas 397): continuation leaf, clear text with short inline cipher runs; the letter's close ("... le 23
[octobre] 1593") is at crop line L21-22, then a postscript in clear. Cipher found in crop lines L05, L07, L09, L10, L13,
L15 (the longest run, ~32 signs), L16, L18, L19. Pass agreement 27/66 = 40.9% (A 64 signs, B 53). Tokens graded:
**H 5, M 56, U 5, I 0** (66). L09 ends "de R phi phi+" = "de [Duc de Mantoue] [Duc de Ferrare|ca] [?]" (M: the passes
disagree on R). The rest gives letter strings only.

Result: the key applied sign by sign does **not** give a continuous reading. The blocker is the one Bourdeau recorded on
17 Sept 2026 ("the copyist's cursive forms map to two or three table entries each"): the Revol copyist writes no.60 in
a cursive whose shapes the two passes cannot even agree on, and many shapes have more than one table value. Status stays
`open` (no reading; a mechanical application is not one). Grade I: 0 (nothing repaired).

Suggestion (one line, not done): build the copyist glyph atlas from the interlined Instruction of 31 Aug 1593 (fr.3985
c.264-268, same hand, printed in Memoires de Nevers ii 492-499) as Bourdeau's 'Next pass' says, then re-run both passes
with atlas tags instead of table shapes; only then settle `passes/disagreements.tsv` on the image.
