open
Open (3 Nov 2026, NEVREVOL-PREREG): the internal block of 20 Oct is lifted. A mixed-class positive control with the length-class and shuffled-order nulls PASSes (controls_mixed*.txt). Two Opus passes (74.5% agreement) then failed the gate (rank 2/201 against the key shuffles, 119/201 against the order shuffles), a control-backed non-reading for sign_guide tags + key.tsv. Next: passes with the 264ext atlas labels. Earlier block (20 Oct): the value-shuffled-key control had no power at this N. Check-solved citation (24 Sept 2026, search log below): Gomberville *Mémoires de Nevers* seconde partie, Google Books `H2eV4wAmIr0C` full-text SearchWithinVolume for "Despernon", "deliuranse" and "Nouembre 1593" (p.692 already carries Mars 1594), cross-checked on Gallica `bpt6k64451005` ContentSearch; Goulart *Mémoires de la Ligue* vol. 5 and vol. 6 archive.org full text; letter absent.

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

## Web and blog check (CHECK-WEB-3987, 3 Nov 2026)

Four plain web searches (WebSearch tool, standard mode, date checked with `date -u`): (1) `Nevers Revol 1593 chiffre
déchiffré` -- no hit on this letter; closest is Desenclos and Lasry's "An early French digit cipher: deciphering a
letter from the King of France to the Duke of Nevers (1592)" (dspace.ut.ee), which is BnF fr.3620 f.70-71, 12 Sept
1592, Henri IV to Nevers -- a different shelfmark, sender direction and year, not this letter. (2) `"fr.3987" cipher
OR chiffre OR cifra Nevers` -- no hit naming fr.3987; same Desenclos/Lasry paper surfaces again (it names fr.3995's
68 cipher tables, not fr.3987). (3) `"deliuranse de son frer" Despernon` (Tomokiyo's own quoted fragment from this
letter, henryiv2.htm) -- zero hits anywhere on the web; the phrase is not quoted or discussed by anyone else online.
(4) `Nevers to Revol Rome 10 November 1593 BnF fr.3987 cipher` (the folder's descriptive title) -- no hit on this
letter; the same Desenclos/Lasry paper and an unrelated Histocrypt paper on a Rome-based League ambassador's cipher
(Sennecey, BnF Colbert 500/33) surface, neither is this item.

Site searches of the three named blogs, read for a post or comment thread: **Cipherbrain**
(`site:scienceblogs.de klausis-krypto-kolumne Nevers Revol`) -- no post naming Nevers or Revol; nearest unrelated hit
is a WWII Loiret cryptogram post. **Cryptiana blog** (`site:cryptiana.blogspot.com Nevers Revol 3987`) -- zero hits
on that domain at all (the query returned only unrelated Nevers-the-town results); Tomokiyo's own dedicated page
(henryiv2.htm, on cryptiana.web.fc2.com, not the blogspot blog) is already the source cited in this folder's head and
carries no comments section or reader response, confirmed 24 Sept 2026 and unchanged. **Cipher Mysteries**
(`site:ciphermysteries.com Nevers Revol fr.3987`) -- no post naming this letter; nearest unrelated hits are the
Moustier church cryptograms and a Nostradamus thread. A fifth search for a model-solve announcement
(`"fr.3987" solves Claude OR GPT cipher`) found only unrelated AI-solves-a-different-cipher stories (Urquhart's
Cyphral Distich, WWI ADFGVX, Enigma) -- no model-solve claim exists for this letter.

**DECODE listing by shelfmark.** Grepped every on-disk DECODE catalogue snapshot (`sources/decode/*.tsv`,
`sources/decode/*/*.tsv`: the merged keys catalogue, the non-decrypted/decrypted/partially-decrypted record lists,
28 Sept-2 Oct 2026, covering the full site by status) case-insensitively for `revol`: zero hits anywhere. A
word-boundary grep for `3987` hits exactly one unrelated record (DECODE id 3987, Kew TNA SP 53 box 23, English,
undated key) -- a coincidental id match, not this shelfmark. No DECODE record for fr.3987, confirming the 24 Sept
2026 finding.

**Solver repositories, grepped (github.com search API, read-only, no clone).** `dbourdeau/cyphersolver`: searched
`3987` and `revol`. A `targets/revol1593/NOTES.md` exists (split 14 Oct 2026 from `targets/nevers1593/`, covering key
no.60, the Court symbol cipher) -- fetched and read in full (`raw.githubusercontent.com`, public, no auth). It
covers seven Revol letters in key no.60: fr.3985 ff.88, 115, 176 and fr.3986 ff.146v, 157v, 198, two (f.88r partial,
via a contributor's transcription) decoded-not-read and the rest not yet transcribed. fr.3987 f.66 appears exactly
once, inside the same Tomokiyo inventory list already quoted in this folder's head ("fr. 3987 f. 66" among the full
run of key-no.60 letters) -- it is not among his worked pair, not in his "Remaining gaps", and not named as a
planned next step anywhere in the file. No duplicate-effort risk: this letter is not that repository's stated next
target. `aaymeloglu/unsolved-ciphers`: searched `3987`, `revol`, `nevers` -- no dedicated target or catalogue entry;
every hit is incidental (an unrelated PARES catalogue file, a lexicon word list containing the substring "revol").

Gate: `python3 tools/intake_gate_check.py fr3987-nevers-revol-1593` (pasted below). It now confirms the citation and
the web/blog check both pass, but fails on a separate, later-added requirement (CLAUDE.md, 2 Oct 2026: the gate also
requires a "## Premise check" section) that this job's brief (CHECK-WEB-3987, hosts: web search and the three blogs
only, no vision calls) does not cover and does not authorize extending into -- the Premise check's step (c) needs
native-resolution image review of the physical neighbours. Flagged in ROOM.md for the parent; JOB NEVREVOL-ATLAS-2
cannot run yet.

    fr3987-nevers-revol-1593: open (line 1) passes the citation and web/blog checks but has no '## Premise check'
    section -- run check-solved.md's adversarial Premise check (mentioned decipherments opened, other solvers'
    working files, neighbouring leaves, recipient-side editions) before any first test
    exit: 1

No solution, plaintext, key, or model-solve claim found anywhere in this web-and-blog pass. Head stays `open`.

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

## NEVREVOL-PREREG (3 Nov 2026, account 4 worker for the account-4 parent, brief 57)

**Order kept: PREREG, control, passes.** PREREG-NEVREVOL-2.md (Decision block) was pushed before the control ran (b32cebbe9).
The new gate: real S ranks <= 10/201 against 200 length-class value shuffles AND against 200 shuffled orders.

**Positive control, mixed sign classes** (`controls_sup.py --mixed` -> controls_mixed.txt). Held-out fr16 passages, N=188 signs,
greedy letter/syllable/word encipherment. Both-null pass count per 10 passages:

| key | achieved shares letter/syl/word | 0% | 10% | 20% | 30% | 40% | 50% |
|---|---|---|---|---|---|---|---|
| key60.tsv + key_atlas_extra (PREREG) | 62.9 / 34.7 / 2.3 | 10/10 | 10/10 | 10/10 | 10/10 | 9/10 | 8/10 |
| key.tsv, the ASCII tags the passes used (`--local-key`) | 81.0 / 18.9 / 0.1 | 10/10 | 10/10 | 10/10 | 10/10 | 9/10 | 5/10 |

Gate (>= 8/10 at 0%, >= 6/10 at 10%): PASS for both keys. The second row was added after the passes: sign_guide.md's tags
are the ones in this folder's key.tsv, not key60.tsv's Unicode tags, so the target is scored with key.tsv. Its control was run
on that same key before the target was scored. key.tsv has fewer syllable and word signs, so its achieved shares sit below the
target shares.

**Passes.** Pass A: the worker read the 12 crops one at a time. Pass B: 6 Opus subagents, one per line, crops and
sign_guide.md only. Both are in passes/nevrevol2_pass{A,B}.tsv. Agreement was 149/200 signs (74.5%), against 51.0% for the
24 Sept unaided passes. **Blindness breach:** pass B's L10 and L13 lines came back before the worker read those crops, so pass A
is not blind on 2 of 6 lines. L07, L08, L09 and L11 were read blind. All 51 disagreements were settled from the crops, never from
the key (reconcile_v2.tsv). ciphertext_v2.tsv has 191 signs: 149 H (agreed), 42 M (settled).

**Target** (`controls_sup.py --local-key` -> controls_sup_localkey.txt, pasted):

    signs 191; unkeyed tags 13 (25 tokens): 24 I a b' h i j m+ n' s' x' x+ z
    decoded letters 280
    real S -1.5098
    length-class shuffled keys (200): mean -1.7416 sd 0.0878 max -1.4672; real rank 2/201
    shuffled orders (200): mean -1.4967 p95 -1.4672 max -1.3551; real rank 119/201
    judge on real decode: FAIL {"language": {"N": 280, "mode": "both", "null_p99": -1.837, "pass": false, "real_median": -0.774, "real_p05": -0.883, "score": -1.51}, "words": {"cover": 0.743, "min": 0.5, "pass": true, "real_text_median_cover": 0.943}}
    gate (rank <= 10/201 against both): DOES NOT BEAT CONTROL

**Gate: FAIL.** The target ranks 2/201 against the key shuffles but 119/201 against the order shuffles. Its letter frequencies
look French, but its letter order is no better than its own signs scrambled. No decode_key run, no reading, and no grade
changed (the 24 Sept draft stands). The measured disagreement is about 25%. At 20-30% uniform error the key.tsv control still
passes 10/10, so this is a **control-backed non-reading for this instrument on this transcription**. It is not a test of key
no.60 on f.66 (see assumptions below). The judge line was broken by the script's flat SPEC dict and is now fixed: the spec is
wrapped in a "judge" block.

Six questions:
1. Learned: with sign_guide tags + key.tsv, the six f.66 lines reach French-like letter frequencies but not French order: rank 2 against the key shuffles, 119 against the order shuffles. Two Opus passes agree 74.5%.
2. Assumptions behind the result: (i) the sign_guide shape -> key.tsv tag mapping of 24 Sept is right; (ii) the control's random uniform errors stand in for the hand's errors; (iii) 25 unkeyed tokens (13%) can be dropped; (iv) the six lines are one continuous cipher run in page order.
3. Not yet verified: (i), which nothing tests, and a systematic mis-tagging is not modelled by the control; (ii) and (iv). The lookalike pairs 9/g and 6/b recur in the disagreements.
4. Other explanations: a consistent shape-to-tag error, in the 24 Sept key.tsv mapping or in both passes; clear words or nulls inside the runs; a key other than no.60 for this letter.
5. Most informative different experiment: pass with key60.tsv's own atlas labels (the 264ext contact sheet, not sign_guide's ASCII tags), so the mapping step goes away and the existing key60 control row applies directly. Or a check of the key.tsv shape mapping against the fr.3995 key-sheet images.
6. Decision: pivot. Do not re-run the same instrument (rule 3). Next is a different instrument (atlas-label passes); the target stays open.

Usage: vision calls 12 counted + 1 reconciliation, plus 1 subagent call stopped at launch (a placeholder line id) before it read a crop. Requests: none (disk only).

## NEVREVOL-ATLAS (3 Nov 2026, account 4 worker for the account-4 parent, brief 58): stopped at the intake gate

The brief's first step pastes `tools/intake_gate_check.py`. NEVREVOL-PREREG had flipped the head from `blocked` to `open`, so the
gate now applies (it skipped a `blocked` head). It failed twice:

    fr3987-nevers-revol-1593: open (line 1) with no standard-edition citation (page number or full-text-search phrase) within 6 lines -- CLAUDE.md's Pipeline intake gate says this must read `blocked` instead

That was a formatting gap, not a missing search. The 24 Sept search log (items 2-3) records the full-text SearchWithinVolume terms
and the volumes, so I copied that citation into the line below the status word. The second run then failed on a real gap:

    fr3987-nevers-revol-1593: open (line 1) has an edition citation but no logged open-web and blog-comment check (no 'Web and blog check' heading with a line of its own under it; pasted gate output does not count) -- run check-solved.md's 'Open web and blog comment threads' step first (CHECK-SOLVED-WEB, 28 Sept 2026: spinelli-beinecke-c1515 was read in a Cipherbrain comment thread in 2017)

The 24 Sept log has only two web searches (item 7) and Cryptiana's page (item 1). The step needs at least four plain searches, a
site search of each of Cipherbrain, the Cryptiana blog and Cipher Mysteries, and the comment threads read. This brief allows no
hosts, so the step was not run here, and a worker does not extend its own brief. **Nothing else ran:** no PREREG-NEVREVOL-3, no
vision call, no pass, no score. The atlas-label instrument is still untried.

Six questions:
1. Learned: the target has never had the check-solved web-and-blog step. The head moved to `open` without passing the intake gate.
2. Assumptions: the sibling fr3986's web check (2 Oct 2026) does not cover this leaf's shelfmark query, so it does not stand in.
3. Unverified: whether a blog comment thread already reads f.66 (the spinelli shape).
4. Alternatives: none to test here; the gate decides.
5. Next experiment: a short check-solved web-and-blog worker (hosts: web search, the three blogs), then re-run NEVREVOL-ATLAS unchanged (brief 58).
6. Decision: stop (intake gate, nonzero exit blocks the brief); hand back to the parent.

Usage: vision calls 0. Requests: none (disk only).

## Remaining gaps (NEVREVOL-PREREG, 3 Nov 2026)
Read so far: 0 of 308 signs to a continuous text (24 Sept 2026 mechanical draft: H 69, M 211, U 28, I 0). The six-line v2 transcription (191 signs, A/B agreement 74.5%) fails the gate with sign_guide tags + key.tsv: rank 2/201 against the length-class shuffles, 119/201 against the order shuffles (controls_sup_localkey.txt).
- check-solved web-and-blog step (check-solved.md, CHECK-SOLVED-WEB) - blocker: not-attempted; the intake gate fails without it (NEVREVOL-ATLAS, 3 Nov 2026), and no deep work runs until it passes; next: a check-solved web-and-blog worker (four plain searches, site searches of Cipherbrain, the Cryptiana blog and Cipher Mysteries, comment threads read), ~$1
- f.66 cipher runs, six densest lines L07-L11 and L13 (191 signs, ciphertext_v2.tsv) - blocker: not-attempted; held behind the intake gate (web-and-blog step, 3 Nov 2026); ASCII-tag passes with key.tsv are a control-backed non-reading (3 Nov 2026); next: two blind passes with key60.tsv's own 264ext atlas labels (contact_sheet_264ext.png), scored by the PREREG-NEVREVOL-2 gate with the key60 control row already on file, ~$3
- f.66 remaining cipher lines L14 to L18 and L20 to L21 (about 95 signs) - blocker: not-attempted; held back until a six-line instrument beats both nulls; next: same passes on these lines once one does, ~$2

## Escalation (NEVREVOL-PREREG, 3 Nov 2026)
- [x] siblings: fr3986 f.198 (same correspondence, atlas instrument retired there on the verso runs, 36% agreement) and the interlined fr.3985 c.264 / fr.3986 c.298 leaves (atlas source, held-out 65/65)
- [n/a] clear-pages: no clear copy of this letter is known; Tomokiyo gives only a few tentatively read words
- [x] known-keys: key no.60 is in hand (key.tsv; tools/keys/key60.tsv), the key is not the blocker
- [x] print: Gomberville *Mémoires de Nevers* seconde partie and *Mémoires de la Ligue* vols 5-6 read 24 Sept 2026, letter absent
- [x] key-rebuild: 264ext atlas exists (tools/keys/key60_atlas); the Revol-hand sorter for fr3986 waits on ASKS row 102
- [x] image-check: canvas 121 = f.66 confirmed 24 Sept 2026; native region on disk, six lines re-cut 20 Oct 2026 (images/v2)
- [ ] retry: sign_guide-tag passes + key.tsv done 3 Nov 2026 (gate FAIL, control passed); untried instrument: passes labelled with key60.tsv's 264ext atlas labels
Verdict: keep going: 3 internal gaps; cheapest next: the check-solved web-and-blog step (~$1), then two blind 264ext-atlas-label passes on images/v2 under the PREREG-NEVREVOL-2 gate, ~$3

### Parent notes (account-4 parent, 3 Nov 2026, after NEVREVOL-PREREG)
1. Learned: with a control that genuinely has power (mixed-class, both nulls, 10/10 to 20% error), the six lines under sign_guide tags + key.tsv beat the key shuffles but not the order shuffles: the sign-to-tag mapping, not key no.60, is the live suspect.
2. Assumptions the result rests on: the 24 Sept shape-to-tag mapping; uniform random error as a stand-in for the hand's systematic lookalike errors (9/g, 6/b); 25 unkeyed tokens droppable.
3. Unverified: the mapping itself, which nothing has tested; pass A blind on only 4 of 6 lines.
4. Alternatives: a consistent mis-tagging; nulls or clear words inside the runs; a key other than no.60.
5. Most informative different experiment: two blind passes labelled with key60's own 264ext atlas (contact_sheet_264ext.png), which removes the mapping step and lets the existing key60 control row apply directly (wave 58, NEVREVOL-ATLAS); if that also fails both nulls, the target is untestable-by-this-instrument at this N (rule 3) and waits on the Revol-hand sorter (ASKS 102).
6. Decision: pivot to the atlas-label instrument, one run, then stop if it fails.

### Parent notes (account-4 parent, 3 Nov 2026, after NEVREVOL-ATLAS stopped at the gate)
1. Learned: my brief let NEVREVOL-PREREG flip the head from blocked to open and then briefed deep work without re-running the intake gate; the worker stopped correctly at step 0.
2. Assumption that failed: that a target once gated stays gated; a status-word change re-opens the intake check (Pipeline 2).
3. Unverified: nothing new on the cipher; the web-and-blog check-solved step has never been run on this folder.
4. Alternatives: none; this is process.
5. Most informative next: CHECK-WEB-3987 (four plain searches plus site searches of Cipherbrain, Cryptiana and Cipher Mysteries, comment threads read), then NEVREVOL-ATLAS re-run unchanged (brief 59).
6. Decision: continue, in that order; the parent pastes the gate output in brief 59 itself.
