# Mary Stuart talk and paper: every proven method, where it lives in our toolbox, and what is being built (9 Oct 2026)

Written 9 Oct 2026, 00:3x-01:2x UTC (clock read with `date -u`), by a reconciling session for the account-3 orchestrator.
It supersedes nothing: `research/MARY-STUART-METHOD-2026-10-04.md` (the 4 Oct note) still holds the step-by-step reading
of the paper. This note adds the talk, the discovery thread and the critics' corrections, and maps every method to a
tool. The full matrix, one row per method, is `research/MARY-STUART-TALK-2026-10-09.tsv` (47 rows: 2 covered, 27 partial,
3 promote-from-local, 15 missing). The build briefs are `.claude/briefs/runs/2026-10-09-acct3-mqs-*.md` (eight jobs and
one lane brief, for account 4). Nothing here is a reading, and nothing here makes a novelty claim (rule 10).

Sources:
- G. Lasry, N. Biermann and S. Tomokiyo, "Deciphering Mary Stuart's lost letters from 1578-1584", *Cryptologia* 47:2
  (2023), pp. 101-202, doi 10.1080/01611194.2022.2160677, open access under CC BY-NC-ND. Kept unmodified at
  `sources/papers/lasry-biermann-tomokiyo-2023-mary-stuart.pdf`. Page numbers below are the journal's.
- George Lasry's talk, "Deciphering Mary Stuart's Lost Letters", YouTube `kiL-QdQJPB0` (channel "Cryptography for
  Everybody", uploaded 8 Feb 2023, 38 min). Timestamps are from the video's own auto-captions, read on 8 Oct 2026.
- The CTTS tool (CrypTool Transcriber and Solver): its README and LICENSE (Apache-2.0) at github.com/CrypToolProject/CTTS,
  and Lasry's CTTS paper, HistoCrypt 2026, hdl 10062/122071.
- Follow-ups: Biermann, Tomokiyo and Lasry, HistoCrypt 2024 (cross-cipher errors, doi 10.58009/aere-perennius0087);
  Lasry, "Location Matters", HistoCrypt 2026 (hdl 10062/122074).

## (a) Summary, in plain English

Lasry, Biermann and Tomokiyo found 57 letters of Mary, Queen of Scots in the BnF. They were not looking for her. They were
working through the BnF's online manuscripts for any cipher at all. The letters sat in volumes of 1520s-1530s Italian
papers, catalogued only as "Pièce en chiffre", with no name or date. Nobody had read them, because nobody could tell what
they were until they were read. The authors' method has two halves. People box and label every symbol by hand in a tool,
and a solver then finds the single-letter values. Everything else (names, words, months, special signs) was worked out by
hand, by testing one guess at every place the symbol occurs. Most of their method was already ours in some form. This
pass checked each claim about our toolbox against the code, found that several "missing" methods already exist as
scripts in single target folders (Gramont's crossword scripts, Moray's key-sheet builder, a held re-anneal on
Clairambault 1161), and turned the rest into eight build jobs for account 4. In priority order: (A) key and reading
sheets we can show Tomokiyo and the holders, with samples for Gramont, Danzay, Birago 1572 and one Huntington telegram;
(B) a sign sorter you can read without relying on red and green, which also never shows you key values while you sort;
(C) a name-and-place candidate tool that learns from our two failed earlier attempts; (D) the crossword test as a shared
option; (E) a catalogue census of BnF piles, done gently; (F) the paper's solver settings, tested against a matched
control; (G) a scout scoring fix so an unnamed pile is not ranked low; (H) lock-and-re-run. The colour rule for every
picture we make is in section (f): it uses blue and dark orange plus shapes, never red against green, and the palette
was checked with a colour-blindness simulation.

## (b) How they found the letters, and why nobody had

What they were doing. "Actually we were not even looking for ciphers from Mary Queen of Scots" (talk [00:07:03]-[00:07:09]).
They were "just looking at the online collection of the Bibliothèque nationale de France in order to find cipher
documents; when we find such cipher documents, if they have not yet been deciphered, we crack them" ([00:07:11]-[00:07:27]),
as part of Tomokiyo's Cryptiana survey and the DECRYPT project ([00:07:27]-[00:08:02]; paper p.101 and n.1). The paper
names no search string, and says they "only had access to the BnF collections that are available online" (p.191).

Where the letters are (p.108-109; talk [00:08:06]-[00:08:44]). Français 2988, 26 letters, ff.21-130; Français 20506,
28 letters, ff.151-249; Cinq Cents de Colbert 470, ff.307-308; Français 3158 f.57, a letter mostly in clear with short
cipher passages that Labanoff printed in 1844 with the cipher shown as ellipses (p.108 n.38). More than 150,000 symbols in
all (p.110). All digitised.

Why they had gone unread.
- The catalogue lists the fr.2988 items only as "Pièce en chiffre", and fr.20506 only at volume level, as "dépêches
  chiffrées" among papers on Italian affairs (p.102, p.108).
- The cipher items carry no date, writer or recipient, and they sit among clear Italian letters from the first half of the
  16th century, "giving the wrong impression that the plaintext documents were the deciphered versions of those letters"
  (p.108-109).
- A trained 16th-century codebreaker could have broken the cipher "with a moderate effort", but no modern scholar had a
  reason to try before the letters were attributed (p.102 n.6). In the talk: "not enough incentive", and "there is no
  way to know that they are from Mary"; "the catalog information is not really useful" ([00:08:49]-[00:09:22]); "the only
  way ... was actually systematic efforts to survey all those documents" ([00:09:24]-[00:09:37]).
- Transcription was the slow part: "it took us about five to six months to transcribe everything" ([00:13:04]-[00:13:07]).

How they attributed and widened the pile.
- The attribution came out of the partial decipherment itself (p.101: such letters "cannot be attributed unless they are
  first deciphered"; p.110). By the time they reached the name symbols, "we already knew that those letters were from
  Mary Stuart" ([00:22:32]-[00:22:40]).
- They tried Italian first, the language of the neighbours, and got nothing; French worked (p.112-115).
- Only then did they search the collections known to hold Castelnau's papers for the same graphical symbols, which found
  Colbert 470 ff.307-308 and fr.3158 f.57 (p.190 n.345).
- They name other leads in the same volumes: Venetian-looking cipher letters signed Hieronimo Ranzo (fr.2988 f.2 and f.9;
  fr.20506 f.136, a copy of f.9) and English cipher letters "that appear to address Mary" (fr.2988 f.1, fr.20506 f.146)
  (p.108 n.37). Files already on disk show both English letters were read before: Tomokiyo's unsolved list credits
  Torbjörn Andersson (2017, via Cipherbrain) for fr.2988 f.1, and DECODE lists records 2323 (fr.2988 f.1) and 4451
  (fr.20506 f.146) as Decrypted, English. The Ranzo letters are open and are Bourdeau's ground
  (`ciphers/decode-4450-bnf-fr20506-1525`).
- Their stated next steps: other BnF collections, the letters known to be missing for 1578-1581, and physical inspection
  where scans are poor (p.191; talk [00:37:15]-[00:37:27]).

What the catalogue says today (fetched 8 Oct 2026, 23:44-23:47 UTC, five requests to archivesetmanuscrits, all HTTP 200).
- The fr.2988 notice (ark `cc49442s`) still lists 26 bare "Pièce en chiffre." items. But it now carries, at collection
  level, a "Présentation du contenu" that says the volume contains cipher letters of Marie Stuart to Castelnau, 1578-1584,
  and a "Bibliographie" citing the paper. (The 8 Oct discovery reader said the record "still does not name Mary"; that
  was wrong, and it matters: a census that reads only the item lines would rank this solved pile first.)
- A quoted search for "pièce en chiffre" returns 26 results, every one of them this pile. A quoted search for "dépêches
  chiffrées" returns 7 records, fr.20506 among them. Quoted phrases behave as phrases on this site, which corrects our
  25 Sept note that the search box "is not phrase-adjacent".
- Gallica answered HTTP 403 (a Cloudflare block page) to this container at 23:45:56 UTC; it has blocked cloud sessions
  since about 12:45 UTC on 8 Oct. The image side of any sweep waits for it.

What it means for us. The pile was hidden by context, not by absence. Our own sweeps would have missed it the same way:
on 23 Sept the Gallica SRU pass dropped both of fr.2988's arks as "bourdeau-profile" (Bourdeau works on the Ranzo
letters in that volume), and on 24 Sept a later pass dropped Français 3005-3993 wholesale. Exclusion has to be per item.
And our scout rubric scores an unnamed, undated, all-cipher pile low on every axis that needs a name (matrix M40). A ten
times larger sweep is reachable; ten times more finds cannot be promised. The most distinctive catalogue phrase is
already used up by this pile, and no second large pile shows among the 72 cipher-bearing notices on disk (the next best
scored 3). The real upside is in volume-level notices with no item list, in volumes whose notice never says "chiffre",
and in volumes that are not online at all, which nobody has swept (M42). Prior work matters too: the Mary corpus is being
edited for a Routledge book due in 2027 (Northeastern Global News, 21 Aug 2024), and Lasry is machine-transcribing a
second Mary collection of more than 100,000 symbols (HistoCrypt 2026, PDF p.6 n.8). Any hit near Mary's material is
"contact first" (M37).

## (c) Every proven method and where it lives

"Proven" means the authors used it to get their result. "Lives in" is the shared tool and flag once the named job lands;
until then the job is the place it is being put. Grades are our shelf's (`tools/data/tool_shelf.tsv`).

| Method (their source) | Lives in, or will | Job |
|---|---|---|
| Sweep a digitised holding for any cipher item; attribute after reading (talk [00:07:03]-[00:09:40]; p.101-102, 108-109, 191) | `bnf_findingaid.py --census` / `--pile` | MQS-BNFPILE (S0-S1; S2-S6 later) |
| Exclude solved material item by item (our lesson from their pile) | `bnf_findingaid.py --pile` per-item exclusion; `prior_work.py` | MQS-BNFPILE |
| People box symbols and give arbitrary type labels (talk [00:12:45]-[00:13:27]; p.110-112) | `sign_sorter.py` + `sign_sorter_apply.py` (piles are the types); adding or splitting a box is still missing | MQS-SORTER scores the owner's no.87 sort; later SORTER-BOX |
| Per-type gallery, odd ones first (talk [00:13:27]; Fig. 4 p.113; CTTS review) | `sign_sorter.py` already orders odd ones first (since 1 Oct); its recall gets measured | MQS-SORTER |
| Colour per type (talk [00:13:09]; Fig. 4) | made safe: `tools/cvd_check.py`, sorter palette, `sorter_preflight.py --cvd` | MQS-SHEETS, MQS-SORTER |
| Diacritic variants as separate types (talk [00:13:54]; p.112 n.48) | `glyph_atlas.py segment --mark-*`, `sign_sorter.py --marks`; base/mark split later | later BASE-MARK |
| Annealing with restarts, swap and reassign moves (talk [00:14:21]; App. A p.195-197) | `homophonic_anneal.py` (reassign today) + `--moves swap/both` | MQS-SOLVER |
| Score divided by sum of squared letter counts (App. A p.195-196) | `homophonic_anneal.py --norm nc2` is an approximation; `--norm nc2paper` is the paper's | MQS-SOLVER |
| Solver settings: u/v and i/j merged, per-letter cap, minimum count, budget, ignored letters, doubled letters (talk [00:15:58]; p.118; CTTS) | `homophonic_anneal.py` (folding today) + `--max-homophones`, `--min-count`, `--homophone-budget`, `--drop-letters`, `--collapse-doubles` | MQS-SOLVER |
| Marked symbols kept out of the homophones but kept as gaps (p.115-118) | `homophonic_anneal.py --as-unknown`, `family_run.py --param exclude=` | MQS-SOLVER |
| Language by trial, not from the neighbours (talk [00:15:58]; p.112-115) | `judge_plaintext.py` corpora; `family_run.py --corpus`; a one-call `--langs` later | later LANGS |
| Confirm fragments, lock them, re-run on the rest (p.115-117; CTTS 'Locked') | `homophonic_anneal.py --fix`, nomenclator `cribs`; `family_run.py --param lock=FILE` | MQS-LOCK |
| Special symbols found from context: repeat, delete, nulls (talk [00:17:24]; p.111, 115) | nulls in `decode_key.py`; repeat/delete later | later SPECIAL-SIGNS |
| Crossword and avalanche: test a guess at every occurrence, follow what opens (talk [00:19:20]-[00:23:49]; p.118-122) | `decode_key.py --try` / `--avalanche` (promoted from `ciphers/fr2980-gramont/infer_unkeyed.py` and `test_f30r_top.py`) | MQS-CROSSWORD |
| Names from historical context ('mon beau-frère' = Anjou; talk [00:22:08]; p.122) | `tools/name_candidates.py` (proposes; `--try` tests; a verifier grades) | MQS-NAMES |
| Plaintext copies in print, diffed against the reading (p.102, 110, 122, 124) | `interlinear_align.py`, `stream_align.py`, `decode_witness.py`, `print_check.py` (Pisany, 4 Oct) | partial: alignment proven on Pisany; labels and the 'sent in cipher' criteria later (WITNESS-LABELS) |
| Months by a chain of deductions (p.124-125, Fig. 12) | `freq.py --tail` later, known answer the Janssens pool | later TAIL |
| Sibling keys compared (p.128-130) | `key_crossmatch.py` (key vs text, proven); key vs key later | later KEY-COMPARE |
| Cross-cipher contamination explained (App. B p.198-200; HistoCrypt 2024) | none shared; two target runs failed their gates; needs a positive control first | later CCE-MATRIX |
| Key sheet (Figs 8, 12-14) | `tools/decipher_sheet.py key` (promoted from `ciphers/moray-wood-1568/no804/refsheet/build_refsheet.py`) | MQS-SHEETS |
| Reading sheet, occurrence highlighting, annotated strip (Figs 5-11, B24) | `tools/decipher_sheet.py reading` (`--highlight`, `--annotate`) | MQS-SHEETS |
| Confirmed in capitals, tentative in lower case (p.115; CTTS) | `decode_key.py --style case` | MQS-SHEETS |
| Second-wave search of the recipient's papers by symbol shape (p.190 n.345) | `glyph_atlas.py match` later, with a non-circular known answer | later GLYPH-MATCH |
| Human-in-the-loop detector, retrained on corrections (Lasry 2026) | `glyph_atlas.py classify` + rounds later | later CLASSIFY-ROUNDS |

## (d) What was already ours

So you can see what this pass did not need to build:
- **The sorter is their method.** A person sorting tiles into arbitrary piles is what they did in CTTS. Ours already
  orders each pile odd ones first, lets you fix a bad cut, and carries every state as a glyph and a border as well as a
  colour (LESSONS.md line 245). What is missing is adding or splitting a box, and a measured error rate for your sorts.
- **The machine stage.** Annealing with restarts, held values (`--fix`), starting keys (`--init`), u/v and i/j folding,
  an approximation of their score (`--norm nc2`), and the control-first harness (`family_run.py`).
- **The checks they did not have.** Our judge (`judge_plaintext.py`) scores a reading against shuffled controls, which is
  stronger than reading the output by eye, and we grade every token (H, C, S, M, I, U). The paper reports no per-symbol
  error rate and no control in our sense (4 Oct note, section 1).
- **Plaintext copies.** Alignment against a printed copy is proven on Pisany (several known-plaintext runs, 4 Oct).
- **Sibling keys against a ciphertext** (`key_crossmatch.py`, proven) and the design prior (`design_prior.py`, proven).
- **Glyph segmentation and classification** (`glyph_atlas.py`), and a per-sign error benchmark (`tx_bench.py`).
- **The crossword, the key sheet and the alias list already existed, in single target folders**: Gramont's
  `infer_unkeyed.py` (hidden-sign control: 50 of 53 right on held-out draws), Moray's `build_refsheet.py`, and the Browne
  feigned-names table for Maclean 1745. Our rule (CLAUDE.md Usage 8) is to promote these into the shared tools, not to
  rebuild them, and jobs D and A do that.
- **The pools rule** (CLAUDE.md pipeline 3) is their lesson in our words: their solver worked because it had about 57
  letters in one key.
- **Tomokiyo's ciphertext-only instruments** went into the toolbox on 8 Oct (the closed TOOLS-TOMO lane: `freq.py`
  `--contacts/--kwic/--repeats/--split-at`, `interlinear_align.py --cipher-pair`, `key_design.py --matrix`,
  `running_key.py --drag`, `decode_key.py --consistency`). None of this pass's jobs repeats them.

## (e) Twelve moments in the talk worth a screenshot (optional)

These are for you, if you want to look. Nothing here needs them. Frames stay out of this repository: the talk shows the
paper's figures, which are CC BY-NC-ND, so a frame is described in words here and kept, if at all, in a scratchpad or the
private repository. No video was downloaded, so every item is "if a single fetch of the video works; otherwise use the
paper's figure page cited".

| Time | What to look for, and why |
|---|---|
| 00:08:49 | The why-nobody-found-them slide: whether it shows the catalogue strings ("Pièce en chiffre", the Italian neighbours). The paper only quotes them (p.102, p.108-109). |
| 00:13:09 | Their transcription screen with coloured boxes per symbol type. Shows whether the type is carried by colour alone, which the sorter must not copy (section f). Paper Fig. 4, p.113. |
| 00:13:27 | The bottom-panel gallery of every instance of one type: the model for the sorter's odd-ones-first pile view. |
| 00:13:47 | The symbol inventory slide (the talk says 191 types; the paper says 219, p.112 and p.122). Outward text quotes the paper. |
| 00:15:58 | The solver settings screen ("other parameters", the per-letter homophone cap): fixes the option list for job F. |
| 00:16:58 | How plausible fragments are marked on screen: by capitals, by colour, or both. |
| 00:17:39 | The repeat-previous symbol (the "two fours") in "sur l'arrivée prochaine": a fixture for a later special-symbol detector. |
| 00:19:20 | Every occurrence of one symbol outlined (the 'y with a dot' = DE test): how they highlight, for `--highlight` in the reading sheet. |
| 00:22:08 | "The upcoming arrival of K, my brother-in-law": the context the name tool's Mary fixture is built from (paper p.122). |
| 00:24:04 | The final decryption with corrections in brackets (the paper corrects silently, p.136 n.95): the bracket convention our sheets use. |
| 00:25:14 | The reconstructed key sheet: section order and notation ('?', braces, 'or vice versa') against Figs 13-14 (p.126-127). |
| 00:26:06 | The letter count slide (talk: 8 known, 49 unknown). The paper's figures are 7 plaintext copies and, on its own base, 45 (p.102, p.131-132); quote the paper. |

## (f) Colour-blind design rule for every visual tool

The owner is red-green colour-blind. Their transcription tool picks one hue per symbol type, which fails for him.

The rule, for every page, sheet or figure an agent makes for a person:
1. **Never carry meaning by hue alone.** Every state or class also differs in at least one of: a glyph (check, cross,
   question mark, bang), a border or underline style (solid, dashed, dotted, double), letter case, weight, italics or
   brackets, a fill pattern (solid, hatch, dots), or a printed label. Hint text never names a colour ("the orange ?").
2. **Never red against green.** No red, no green in any palette that distinguishes states.
3. **The palette.** On light backgrounds, marks (borders, underlines, outlines, badges) use ink (#24211c, or black on
   white), blue #0072B2 and dark orange #B35900, plus mid grey (#767676 on the sorter's beige, #595959 on white) as a
   fourth. On dark backgrounds: light ink #ece6dc, sky blue #56B4E9 and orange #E69F00. Yellow #F0E442 and sky blue are
   used only as background tints under ink text, never as the only mark. Blue, orange, sky blue and yellow are Okabe and
   Ito's colour-universal-design set; #B35900 is their orange family darkened, because their own orange #E69F00 reaches
   only 2.25:1 against white.
4. **The test**, run by `tools/cvd_check.py` (built in job A) and by `sorter_preflight.py --cvd` (job B):
   every pair of mark colours must differ by CIEDE2000 >= 20 in normal vision and after the Machado, Oliveira and
   Fernandes (2009) simulation of protan, deutan and tritan vision at severity 1.0 (in linear RGB); every mark must reach
   WCAG 3:1 against its actual background, and any text 4.5:1; a tint must give its ink text 4.5:1.
5. **What the test gives** (recomputed in this pass with scikit-image's CIEDE2000; the critic's own script agreed):

| Set | Background | Worst pair, CIEDE2000 (all four visions) | Weakest contrast | Verdict |
|---|---|---|---|---|
| Sorter today: ok #2f6b3a vs bad #b3261e | #f3f1ec | 8.7 (protan), 11.3 (deutan) | 5.66:1 | FAIL (the must-catch) |
| First proposal: ok #0072B2, bad #E69F00, warn #F0E442, accent #CC79A7 | white | 10.9 (orange vs reddish purple, tritan); 11.6 (orange vs yellow, deutan); 12.2 (blue vs reddish purple, protan) | yellow 1.32:1, orange 2.25:1 | FAIL |
| Sorter, light: ink, blue #0072B2, dark orange #B35900, grey #767676 | #f3f1ec | 20.7 (blue vs grey, protan); 30.8 without grey | grey 4.02:1, dark orange 4.28:1 | PASS (marks); dark orange and grey are not text colours on this background |
| Sheets, light: black, blue #0072B2, dark orange #B35900, grey #595959 | white | 22.7 (blue vs grey) | dark orange 4.83:1 | PASS (marks and text) |
| Dark theme: ink #ece6dc, sky #56B4E9, orange #E69F00 | #1b1916 | 25.5 (ink vs orange, tritan) | 7.60:1 | PASS |
| Tints yellow #F0E442, sky #56B4E9 under ink #24211c | (fill) | not a mark | ink on them 12.13:1 and 6.95:1 | allowed as fills only |

6. **The owner's eye is the final test**, not the simulation. Job B adds one ASKS row: open the rebuilt Birago sorter and
   say whether done / to do / not-a-letter / bad can be told apart without reading the chips.
7. **Grades on sheets** (job A) are carried by form first: H and C capitals in bold with a superscript letter; S capitals
   with a solid blue underline; M lower case with a dashed dark-orange underline and a trailing '?'; I lower-case italic
   in [brackets] with a dotted ink underline (no third hue); U as `<code>` in grey monospace; NULL as a middle dot.
8. Other visual tools (the dashboard, atlas sheets, reference sheets) get the same check in a later CVD-AUDIT job.

## (g) Credit

Every method in this note is the authors' unless marked ours (CLAUDE.md rule 8):
- G. Lasry, N. Biermann and S. Tomokiyo, *Cryptologia* 47:2 (2023), pp. 101-202 (the discovery, the method, the key
  sheets, the decipherments). Tomokiyo's Cryptiana survey and the DECRYPT project (Megyesi et al.) are where the search
  ran.
- G. Lasry, the talk (YouTube `kiL-QdQJPB0`, Feb 2023).
- G. Lasry and the CrypTool project: CTTS, the transcriber and solver (Apache-2.0); its annealing follows N. Kopal (2019),
  as the CTTS paper says.
- N. Biermann, S. Tomokiyo and G. Lasry, HistoCrypt 2024 (cross-cipher errors); G. Lasry, HistoCrypt 2026 ("Location
  Matters", the detector loop and the second Mary collection).
- E. Paranque, A. Courtney and M. Questier, the edition in preparation (Northeastern Global News, 21 Aug 2024).
- T. Andersson (fr.2988 f.1, 2017, via Cipherbrain); DECODE (records 2323 and 4451).
- D. Bourdeau (the Ranzo work; his code is MIT and his text CC BY 4.0); A. Aymeloglu (Moray labels; cited, no code
  copied: his repository has no licence).
- M. Okabe and K. Ito, Color Universal Design (2002, 2008); G. M. Machado, M. M. Oliveira and L. A. F. Fernandes (2009),
  the colour-vision simulation; G. Sharma, W. Wu and E. N. Dalal (2005), CIEDE2000; W3C, WCAG 2.1 contrast.

Ours: the per-item exclusion lesson, the oddness score in the sorter, the graded-token convention, the controls, and the
target-local scripts being promoted (Gramont, Moray, Clairambault 1161, Mercy H41, NEVBIR-NAMES).

## Corrections this pass made to the 8-9 Oct synthesis

Each critic's claim was checked in the repository before it was applied (details per row in the TSV).
- Methods called missing that exist as target-local scripts: crossword (Gramont), key sheet (Moray), alias table
  (Maclean), month codes (Janssens), calendar handling (`prior_work.py`, with a real bug for Julian Jan-Feb 1700), the
  held re-anneal (Clairambault 1161), and four earlier name-candidate runs, two of which failed their own controls.
- Methods called covered that are partial: transcription by a person (boxing is machine-only), fragment highlighting (no
  fragment list), the swap move (absent), plaintext-copy diffing (no labels; three aligners unshelved).
- Wrong facts fixed: the sorter already orders odd ones first; corpus codes `fr16`/`it16` do not exist (the codes are
  `fr`, `it`, `it16dip` ...), and `fr` reads one file; Birago no.87 is Italian, not French; `--norm nc2` is not the
  paper's score; the Ranzo items in fr.2988 are the open ones and the 26 Mary items are prior work, not the reverse; the
  two English leads are already found-solved; the f.117r known answer was circular; the TX-CROSSWORD gate used an old
  baseline (0.081; the best measured is 0.045); clair349 records no encipherer slips; the talk's 49 and the paper's 45
  count different things; the BnF notice for fr.2988 does name Mary now.
- Plans changed: the sorter shows no key values unless a declared non-blind mode is switched on after a blind sort is
  saved (TRANSCRIPTION.md, blind first); every palette in the specs was replaced by one that passes its own test; the
  name tool's controls are reported by occurrence count and by persons vs places, and the Mary example is a fixture, not
  a gate; the crossword control is gated per value class; the Eckert E52 sample (page image not committed) is replaced
  by E4 (mssEC 19 p.49, committed); the 'register' sheet is deferred to a later job built on `holder_export.py`.

On the JSTOR question of 8 Oct (for the owner; corrects the earlier answer): nothing is needed from you. The JSTOR runner
was logged back in at 23:38 UTC on 8 Oct (ASKS 76, answered). The Chavigny letter has six searches queued, not two
(JSTOR-QUEUE.tsv lines 423-424, 439-440 and 443-444; four were added after your "JSTOR skip, yes" at 23:35), and the
Huntington list gained two more for E146. Your waiver already clears both notes; the queued searches run first on the
runner, and if any of them prints text a note mentions, we tell the recipient (the gate-2 lines in both drafts say so).
The Huntington reply goes in through Ask a Librarian ticket #1926; the Tomokiyo note is an email.
