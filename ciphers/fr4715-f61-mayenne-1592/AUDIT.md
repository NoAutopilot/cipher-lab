# AUDIT -- fr4715-f61-mayenne-1592

## Fragment L10, audit 1 (27 Sept 2026)

Verifier: PARENT WORKER VERIFY-F61-FRAG-1 (Opus, session_01RLi8CixTqT7GzVC2UJm91K), 23:46-00:0x UTC by the container
clock. Separate session from the solver (campaign runner, session_01UgTmQhR7wFtVFrTVdtsq9i). Adversarial audit of a
cryptanalytic FRAGMENT, not of a reading of the letter. The novelty search was limited by the brief to Tomokiyo's pages
on disk (`sources/cryptiana/web/`) and Gallica; no web search.

**Claim under audit** (runner's reading-ready line, ROOM.md 27 Sept 2026 23:26 UTC): f.61r line L10, the 13-sign run after
the clear words "pas paresseux si", reads l-e-t-r-e-s-u-r under the H15b cell map (8 letters: grade S for the cell,
M for the letter within each pair; 5 nulls). Two blind passes identical 13/13. Controls: H15b 42/55 against a permuted
maximum of 0.400; blind judge rank 1 of 21 on the known lines and 1 of 21 on this run (p 0.048 each).

### Verdict

| item | tokens | grades claimed | grades after audit | N-class | key |
|---|---|---|---|---|---|
| f.61r L10 run (13 signs) | 8 letter signs, 5 nulls | cells 8 S; letter within each pair 8 M; nulls 5 S | cells **5 S** (pos 1 EBR l/y, 3 PHI e/r, 4 VBAR_A g/t, 5 PHI e/r, 8 INF h/u) + **3 M** (pos 6 and 11, the side-by-side two-loop "qo" form coded PHI; pos 7 VBAR_B, which the blind sample read as ZHOOK); letter within each pair **8 M**; nulls **5 S** (Tomokiyo's own dashes over 12-13 agree) | **held -- not classed** | `ours` (cell map fitted by us on Tomokiyo's tentative markup under the table's pairings) |

Per-token count after audit, letter level: 0 H, 0 C, 0 S, 8 M; cell level 5 S, 3 M; nulls 5 S. A cryptanalytic result.

**Why held, not N3.** (1) The judge positive control did not reproduce at its pre-registered gate (below). The L10 judge
ranking was the only evidence specific to this run's letters, and it used the same judge design. (2) At letter level
every token is M, so there is no settled plaintext string to phrase-search or to class. "le tresur" is one of several
readings the pairs allow ("l'etre sur", "letre sur" = lettre sur); the judge's own split is interpretation, not evidence.
(3) Three of the eight cells rest on a sign form or a single read that a blind reader disputes. Because of that, no
SECOND-OPINIONS-QUEUE.tsv row was filed (verifier.md: rows are filed only at N3 or better). What would move it: a
pre-registered judge re-run whose prompt is written down before the call, with a gate that counts ties as the rule
says; a decision, with a control, on whether the "qo" form is PHI or a class of its own; and a pair-choice test the
judge does not make alone (for example L10 against a second letter in this cipher, fr.3983 f.108, step H19).

### What was re-derived and what differed

1. **Fragment.** `python3 scripts/f61fragment.py --check` -> `fresh` (exit 0). `fragment_L10.tsv` matches.
2. **Pass reconciliation.** `tools/reconcile_passes.py scripts/passU1_classes.tsv scripts/passU2_classes.tsv --method nw`:
   16/18 over L02/L04/L10. **L10 13/13 identical.** Pass 1 flags positions 1, 6 and 11 as M, the other ten H.
   `scripts/f61pass2.py --a passU1_classes.tsv --b passU2_classes.tsv --gate-line L10` gives output byte-identical to
   the committed `f61pass3_result.txt`. Small discrepancy: the pre-registration comment in f61pass2.py names
   `--a read_call_U.tsv`, but the run used `passU1_classes.tsv`, which NOTES H17 describes as that read "without its comment
   lines". Not material.
3. **Map permutation control, fresh seeds** (scratch script importing `f61crib`/`f61crib3`/`f61crib4` unchanged):
   seed 20260927 with 20 permutations: target 42/55 = 0.764, controls mean 0.298, max 0.418. Seed 4242 with 2000
   permutations: mean 0.280, p95 0.364, p99 0.400, max 0.436, **0 of 2000 at or above the target (p <= 0.0005)**.
   **Reproduced**, and it holds more strongly than the committed 20-map figure. Caveat: this control shows the map is
   consistent with Tomokiyo's five marked spans. Those spans are his own tentative work ("Solved with Polyphonic
   Cipher?"), graded M in NOTES.md, so the reference is not a key source.
4. **Judge control.** Script and inputs are on disk (`f61judge.py`, `_sets.txt`, `_key.json`, `_verdict.tsv`). The runner's
   judge prompts are NOT on disk verbatim. `score` is reproducible from the verdict files. Two observations: the result
   files print scores rounded to integers (`:.0f`), so SET-06/07 (2.5) show as 2 and SET-04 (0.5) as 0; the rank is
   unaffected. Both judge runs used the same order seed (7), so the target was SET-13 in both.
   **One fresh judge call** (Opus, no tools, key withheld in a scratch file it was not told of), on the known lines
   (`passA_classes.tsv`) with 20 **fresh** cell permutations (seed 99) and a **fresh** order (seed 20260927; target =
   SET-02). My prompt told the judge that most sets were expected to be nonsense. Result: target **3**, SET-01 **3**, SET-10 1,
   others 0-1. **Rank 2 of 21 with ties counted against the target: FAIL at the pre-registered gate.** The target
   resolution was "aurcet | estcanaol | tropaunapres | ileusi | rauoenupere | elentroit", close to Tomokiyo's avec, est
   capable, trop avancees and elentroit. The tying set SET-01 scored on "uostre"/"suite", obtained by giving the heaviest
   class h/u. The judge wrote: "Neither SET-01 nor SET-02 reads as French from end to end." So the runner's 7 vs 2 margin
   depends on the prompt. The judge is sensitive to how the question is put, and its rank-1 p = 0.048 cannot be taken
   at face value until the prompt is fixed on disk before the call. **Not reproduced.**
   Also, on the committed L10 ranking, 2 of the 20 permutations also give PHI (4 of the 8 letter signs) e/r (SET-01 3,
   SET-07 2.5). Among the three sets that share that cell, the target's win is 1 of 3, so much of the p = 0.048 comes
   from PHI = e/r, the best-attested cell. The ranking adds little independent support for the other four cells.
5. **Independence of the two passes.** The READMEs say each pass was shown only its sheets and `scripts/f61_atlas.tsv`,
   with "no letters, no key, no first pass shown". The prompts themselves are not on disk, so this is the runner's
   statement and not verified. Red flag: on L10 the two passes give **identical x_px on 7 of 13 signs** (1188, 1431, 2200,
   675, 986, 1229, 1499) and within 15 px on the rest. Two free-hand position estimates rarely agree that exactly. The
   sheet itself carries no ruler or ticks (checked by eye, `images/f61sheetB_L10.jpg`). The likeliest explanation is
   that pass 2's prompt carried sign positions or a segmentation from pass 1. That would leak segmentation, though not
   necessarily classes. Treat the 13/13 agreement as agreement on classes given a shared segmentation, not as two
   fully independent reads, until the prompt is recorded.
6. **Image check** (one Sonnet vision call, 6 crops cut from `images/f61sheetB_L10.jpg`, shuffled labels, shown only the
   crops and the atlas; the key is kept in scratch): pos 8 INF (h), pos 1 EBR (h), pos 11 PHI (**m**, alt OTHER:
   "two loops side by side at the top ... trident/psi-like"), pos 4 VBAR_A (m), pos 7 **ZHOOK** (h, alt CROSS; passes:
   VBAR_B), pos 3 PHI (m, "three loops ... cloverleaf"). **5/6 agree with both passes.** My own look at the sheet shows
   pos 7 as a down-pointing triangle with a second bar at the point, so I read it as VBAR_B. The dissent still makes the
   cell M. Pos 3/5 are the trefoil (clover) form and pos 6/11 are a visibly different two-loops-side-by-side form. The
   atlas folds both into PHI ("loops (one or several) on a long vertical stem"). Pass 1 itself flagged 6 and 11 as
   "could be DBL-like". If they are DBL (b/o), the run is not the same string.
   Cross-check with the key of record: `keys/key_mayenne_1592.tsv` describes the table's glyphs, for example f/s as an
   E-shaped bracket. The fitted map puts the leaf's E-bracket (EBR) at l/y and f/s on VBAR_B. So the map's cells come
   from fitting Tomokiyo's markup, not from glyph likeness to the table. This is consistent with NOTES.md, but it means
   no cell is supported by the table's drawings.

### Search log (novelty question limited to Tomokiyo's pages, 27 Sept 2026)

- `grep -il 4715 sources/cryptiana/web/*` (cp932-decoded): bnf4715.htm, mayenne.htm and nevers.htm name f.61/no.38.
  coleman, crypto, jtelegraph(_e), korean2, unsolved(-2026-09-24) and vowel match "4715" elsewhere; none of them names
  f.61. None contains "paresseux", "tresor", "tresur" or "lettre sur".
- bnf4715.htm#no38 prose: no reading of L10. mayenne.htm: cross-link only. nevers.htm: "no.38 (f.61) Undeciphered. See
  another article".
- **Tomokiyo's annotated image `img/BnFfr4715f61.png`** (872x403, viewed whole): the five spans are as recorded, and
  there are also **two dashes over the last two signs of L10 ("a 6", our CA C6, positions 12-13)**. These are his marks
  for positions he leaves unread. He puts no letters on L10. So he looked at the end of this run and read none of
  it. The intake's and H17's "marks only the five spans" is corrected in NOTES.md (below).
- Gallica: not re-queried. The leaf is the solver's cached canvas f137, which carries no interlinear gloss.
- Result: no prior reading of the L10 run located in the page set searched. This is a search result, not a class,
  since the verdict is held.

### Over-claiming sentences corrected in NOTES.md

Before (H17 section): "Not found in Tomokiyo's `bnf4715.htm#no38`, which marks only the five spans (searched on disk,
27 Sept 2026); nothing here is said to be new, first or unpublished (rule 10: the verifier's call)."

After: "No letters of this run are marked on Tomokiyo's annotated image (...), which spells out only the five spans but
also sets two dashes, and no letters, over the last two signs of L10 (...); nothing here is said to be new, first or
unpublished (rule 10: the verifier's call). [Audit 1 ...: cells of positions 6, 7 and 11 downgraded S -> M (5 S, 3 M),
letters within pairs all M; the judge positive control did not reproduce at its gate ...; verdict held, no N-class.]"

The ROOM.md line (23:26) and the H16/HYPOTHESES rows describing "8 S" cells and "le tresur" are left as the runner's
record, per the brief (CAMPAIGN.md untouched). This file supersedes their grades. The orchestrator decides any
status.json change.

### Postmortem

The fragment is regenerated exactly, and the map-level control is robust (p <= 0.0005 on 2000 permutations). The
fragment-level claim leaned on a model judge whose prompt was never recorded. On a fresh order and prompt that judge
tied instead of winning. Its L10 ranking is carried mostly by one cell (PHI = e/r). And the "two identical blind
passes" share x-coordinates too closely to be fully independent. Lesson for the campaign brief: record each judge and
vision prompt verbatim on disk before the call, the same way the scorer scripts already are. A judge gate that
depends on the wording of an unrecorded prompt is not pre-registered.

### Confidence

Map cells PHI e/r, INF h/u, VBAR_A g/t and EBR l/y applied to L10: moderate (the map control is strong and the image
agrees). The eight-letter string as letters: low (every pair choice is M, and three cells are M). No novelty statement
of any kind is licensed by this audit.

### Solver-side revision after audit 1 (campaign step H26, 2026-09-28 05:08 UTC; rule 10 propagation -- the verifier's text above is unchanged)

Audit 1 held the L10 fragment partly because positions 6 and 11 carry a two-loops-side-by-side form coded PHI. Campaign step
H26 (NOTES.md, `scripts/f61qo.py`, `read_call_QO.tsv`) ran the blind-sort design on all 45 PHI/DBL signs of f.61 and f.108r:
38/38 labelled positions split by group (P < 0.0005 over 2000 permutations), the trefoil under e/r, the side-by-side form under
b/o (6/6), the stacked figure-8 under e/r. L10 positions 6 and 11 are the side-by-side form. Their cells are therefore b/o
(grade S with that control), not e/r; the sequence becomes [l/y] [e/r] [g/t] [e/r] [b/o] [f/s] [h/u] [b/o], the judge's
string 'le tresur' is withdrawn by the solver, the letters within pairs stay M, and `fragment_L10.tsv` is regenerated in H51.
The fragment remains held; any N-class is the verifier's. No SECOND-OPINIONS-QUEUE.tsv row exists for this target.


## VERIFY-F61-V4 (28 Sept 2026)

Verifier: PARENT WORKER VERIFY-F61-V4 (Opus 5.5, session_014nSPzcuub15LNNfvGjJbRp), 16:12-16:3x UTC by the container clock.
This session is separate from every solver on this target (campaign runner session_01NQpd6L9ZvLvjU1L7ttFmZs, F61-FAMILY-6
session_01TPNoYGTE6dLBPfyEgZTLAc). Brief: `.claude/briefs/runs/2026-09-28-parent-verify-f61-v4.md`. Working files, each with a
`--check`: `verify_v4/` (README.md is the step log). Vision and text calls: 6 Opus subagents, every prompt in
`verify_v4/PROMPTS.md`, pushed before the calls (08e31a63, ce288ec1).

**Claim under audit** (F61-FAMILY-6, ROOM.md 15:18 UTC): f.61r under period key v4 in two-way form, meter firm 20 / two-way 59 /
unread 20 of 99 (v3 14/65/20); Tomokiyo's five known spans 48/55 = 0.873 against 200 permuted keys (p95 0.436, max 0.527, 0 of
200 at or above); f.108r 65/84; coverage 0.80. Key v4 = `family/key_period_v4.tsv` (459 rows, 25 classes).

### Verdict

| item | result | grade / scope | key |
|---|---|---|---|
| key v4 as a period key (the rows) | **holds**: every row from a sister leaf's gloss, re-merged byte-identical, relabel scores `--check` fresh, 5/5 blind split re-sorts agree | pairs grade C (period gloss), as KEY.md says | `period` |
| known-span test 48/55 = 0.873 | **reproduced** (fresh seeds: 2 x 2000 permuted keys, p95 0.455, max 0.618, 0/4000 at or above); **conservative figure 42/55 = 0.764** (0/2000) without the f.61-side SBS relabel, whose class naming was first scored on Tomokiyo's letters | test of the key, not a reading | `period` |
| meter 20 / 59 / 20 | **recount reproduces 20/59/20 mechanically; does not hold as a grade statement.** 8 of the 20 firm tokens are C6 = e (three gloss tokens in about 4,000, and every one of the six C6 signs inside Tomokiyo's spans falls on his dash or is skipped: C6 is unread or a null on f.61, not a firm e). Defensible meter: **firm 12 / two-way+ 59 / unread-or-null 28**, and the 6 INF moves are a threshold effect (see below) | C6 tokens regraded I (inferred from 3 tokens, contradicted by the known answer) | `period` |
| recovered passages outside Tomokiyo's spans | **none** | no French word is forced by firm letters anywhere (no run of 3 firm letters on the leaf); blind phrase control: the true key ranks 9 of 21 and passes the brief's rule no better than permuted keys (below) | -- |
| Tomokiyo's five spans | his letters, our key agrees at 48/55 | N0-type for the plaintext: his published tentative reading (`sources/cryptiana/web/bnf4715.htm#no38`, img `BnFfr4715f61.png`) | `published` (his, credited) for the reading; `period` for our key |

**Claim scope for f.61r: none** beyond "a period key rebuilt from the family's own decipherments reads Tomokiyo's five marked spans
at 0.76-0.87 of letters against a permuted-key p95 of 0.40-0.46". No passage of the letter outside his spans is recovered. Nothing
here is a reading of the letter.

### 1. Reproduction

`decode_period.py --key key_period_v4.tsv --frac 0.1 --sbs --check` fresh; `test_period_key.py --key key_period_v4.tsv
--collapse-ebr --min 2 --frac 0.1 --sbs --perms 200 --check` fresh; `recode_split.py score --check` fresh; `merge_period_keys.py`
re-run from the three per-leaf v4 files into scratch: identical to `key_period_v4.tsv` below the header. `verify_v4/repro.py`
(the committed scorer's own functions, fresh seeds): 48/55 = 0.873; seed 20260928, 2000 keys: mean 0.324, p95 0.455, p99 0.545,
max 0.618, 0/2000 at or above; seed 7331: mean 0.320, p95 0.455, max 0.618, 0/2000. The committed p95 0.436 and max 0.527 (200
keys, seed 1) are a little low; the conclusion does not change. f.108r 65/84 is in the committed file (`--check` fresh), not
re-run with other seeds.

### 2. Leakage

- **Key rows.** 459 rows: fr.3982 f.101r 267, fr.3984 f.188r/f.184r 169, fr.3984 f.274r 23. No row from f.61r or f.108r.
- **Tile anchors.** Every anchor tile in `recode_split.py`'s PRIOR list (H65/H67 SBS, H69 4TRI, H70 VBAR, H77 LOOPS) is on
  f.101r or f.188r (the tile files' `leaf` column). Group-to-class names on the anchors were set by the sister leaf's period letter.
- **Where Tomokiyo's letters enter: the f.61 side, not the key.** f.61's own class boundaries came from blind shape sorts whose
  group-to-cell naming was scored against his letters: H13/H15 (VBAR_A/VBAR_B) and H26 (SBS = the side-by-side loops). The whole
  +5 of v4 over v3 comes from the `--sbs` relabel (`verify_v4/leak.py`: L03/13-15, L05/5, L08/5, L11/10 gained, L03/14 'e' lost).
  The SBS boundary is independently backed on the sister leaves (H65: the period gloss writes o under the side-by-side glyph,
  blind sort; this audit's blind f61 re-sort, below, puts f.61's G2 signs with the sister leaves' SBS form 7/7), so no letter
  leaked into a cell. It is still a class decision first found on the test letters, so the figure for "the period key reads f.61
  with no Tomokiyo information at all" is the no-relabel one. Ablations, 2000 fresh permutations each:

  | variant | f.61 spans | perm p95 / max | >= key |
  |---|---|---|---|
  | v4 as committed | 48/55 = 0.873 | 0.455 / 0.618 | 0/2000 |
  | without `--sbs` on f.61 | **42/55 = 0.764** | 0.455 / 0.655 | 0/2000 |
  | SBS = b/o (its sort-artefact e removed) | 48/55 | 0.455 / 0.618 | 0/2000 |
  | VBAR_A/VBAR_B merged on both sides | 48/55 | 0.473 / 0.673 | 0/2000 |
  | VBAR_A, VBAR_B, SBS cells removed from the key | 36/55 = 0.655 | 0.400 / 0.600 | 0/2000 |

  **Leakage: none into the key; one Tomokiyo-validated class decision on the f.61 side, worth 6 letters, independently backed.**
- Scorer note: Tomokiyo's 'v' (avec, avance) is scored as a miss against INF = u (2 letters); with u = v the key reads 50/55.

### 3. The relabel moves (blind re-sort, `verify_v4/split_sample.py`, one Opus vision call each, 5 calls)

Tiles re-cut from the committed `family/recode` query sheets, reshuffled (seed 4), reference forms relabelled X/Y/Z at random;
the family reader's answers and every letter withheld. Decoys from the other forms mixed in.

| split | tiles agreeing with the v4 relabel | decoys |
|---|---|---|
| SBS (b/e/o) out of PHI | 10/10 | 5/5 |
| PHI (e/r) trefoil | 10/10 | 5/5 |
| INF (u), incl. LOOPS sorted INF | 10/10 | 5/5 |
| 4TRI (c/p/t) vs 4HOOK (a/n) | 14/14 | -- |
| f.61r's own loop signs: H26 G2 -> SBS (7), G1 -> PHI (5), against the sister leaves' reference forms | 12/12 | -- |

**All five hold (>= 0.8); no cell graded down on this count.** Limits: the sample was drawn from tiles the family reader had
placed (its "none" tiles excluded), and the reference forms are the runner's anchors, so this tests that the relabel is
reproducible by a second blind reader, not that the anchor definitions are right. The f61 reader noted that f.61's hand is "a
different hand or scan" with rounder loops, and still put every G2 sign with the sister leaves' side-by-side form.

### 4. The meter (`verify_v4/meter.py`, `verify_v4/c6_check.py`)

Recount from the committed decodes: v3 firm 14 (C 10, C+ 4) / M 65 / unread 20; v4 firm 20 (C 10, C+ 10) / M 59 / unread 20;
M set sizes v4 two 36, three 18, four 3, seven 2. **The six signs that moved to firm** are all INF, u/e M -> u C+: L01/4,
L05/10, L07/8, L08/4, L08/8, L10/8. Evidence: the tile sort (recode), not a period gloss and not print -- LOOPS tokens sorted as
INF raise f.188r's INF total from 38 to 50, so its e (n 4) falls from 10.5% to 8% of the class, under the 0.1 rule; the e is
still attested. f.101r's INF also carries h 10/156 (6%), and Tomokiyo's table cell is h/u. u is overwhelmingly the dominant
value (f.101r 130/156, f.188r 31/50, f.274r 16/17), and Tomokiyo reads u/v at all five INF positions inside his spans, so C+ for
u is defensible **as "u, h/e not excluded"**; it is not a new fact about the cipher.

**The firm 20 by class:** C6 = e 8, INF = u 6, VBAR_B = s 4, ELOOP = r 2. C6 = e rests on 3 gloss tokens (f.101r 2, f.188r 1) in
the family's ~4,000 aligned signs, yet f.61r writes C6 8 times in 99 signs; inside Tomokiyo's spans all six C6 positions are his
dashes (5) or skipped by the alignment (1): L01/2, L03/11, L07/6, L08/3, L08/9, L05/12. He also dashed L10/12-13 ("a 6", audit
1). A firm e there would give "eaeubeau" for his "ea-ubeau". **C6 on f.61 is regraded I (a null or an unread sign), not C.**
ELOOP = r (2 tokens, L01/7, L03/3, outside the spans) rests on n = 2 of 7 on one leaf: kept firm under the key's own rule, but
thin. So the meter, as a grade statement: **firm 12 (INF u 6, VBAR_B s 4, ELOOP r 2) / two-way-or-wider 59 / unread or null 28.**

### 5. Reading in two-way form (`verify_v4/f61r_v4_twoway.txt`, `twoway.py --check`)

Every line of f.61r under v4, with Tomokiyo's markup set under the signs of his five spans. His letters beside ours (T = his, sets
= ours, * = no match): S1 "avec": a [a/n], v u*, e [e/r], c [c/p/t]. S2 "estcapable": e [e/r], s s, t [t/s], c [c/p/t], a [a/n],
p [c/p/t], a [a/n], b [o/b/e], l [l/s/a]. S3 "tropavancees": t [t/s], r [e/r], o [o/b/e], p [c/p/t], a, v u*, a, n, c, e, e, s all
in set. S4a "jalousi": j ZHOOK* (unread), a [m/s]*, l [l/s/a], o [o/b/e], u u, s s, i ZHOOK* (unread). S4b "eaubeaupere": all 11
in set. S5 "melentenoit": m [m/s], e, l, e, n, t, e, n [d/a/q/n], o [o/b/e], i ZHOOK* (unread), t [t/s]. The seven misses: two v
against u (S1, S3), three ZHOOK positions with no period pair (S4a j and i, S5 i), BETA against a (S4a), and S2's final e, which
falls past the end of line L03's signs.

**Outside the spans** (L01/7-12, L02, L03/1-3, L04, L07/1-2, L10): **no run of 3 or more firm letters exists anywhere on the
leaf**, so no French word or phrase is forced by the firm letters alone, in any line. Blind control (`verify_v4/phrase_ctl.py`,
one Opus text call on 21 renderings of that material -- the true sets and 20 keys with the sets permuted across f.61's classes,
shuffled, key withheld; `verify_v4/phrase_result.txt`):

- Mode (a), no choice inside any set: **0 items under the true key**; 1 in the 20 permuted ("sur", one permuted rendering).
- Mode (b), choosing within sets: under the true key the reader listed 6 items, all short and at confidence 1-2 -- "rue" (L01/1-3),
  "lors" (L10/1-4), "etre" (L10/3-6), "tres" (L10/4-7), "sur" (L10/7-9), "une" (L10/8-10), three of them by taking an unread
  sign as a chosen letter. Each passes the brief's literal rule (at most 1 of 20 permuted renderings gives the same string).
- **The rule has no power at this material.** Applied to each permuted rendering as if it were the true one, the same rule passes
  3-7 items per rendering (mean 4.7; 3 of 20 at or above the true key's 6). Three permuted renderings give confidence-3 items the
  true key does not ("ennemis" across L10/4-10, "rendre" across the whole of L01's tail, "quand"). The reader's own
  French-likeness ranking puts the true rendering **9th of 21**.
- So **no word or phrase outside Tomokiyo's spans is recovered**. The L10 stretch "etre/tres/sur" is the same material audit 1
  held as "le tresur"; it stays a choice among sets, not a reading. (The rule-power line was added to `phrase_ctl.py score` after
  the call and before this verdict; the call, its prompt and the rule itself were fixed beforehand.)

### 6. What a completed reading still needs

1. The **59 two-way (or wider) choices**, made with a control (audit 1's judge failed its gate on this leaf; H25 L10 3/3 FAIL;
   the context route failed its control, H33/H57). Largest single sets: RSIGN (seven letters), 4STEM, 4PI, HASH4.
2. The **five rare classes** CA, CROSS, LL, LOOPBAR, ZHOOK (20 of 99 signs) have no period pair: none of the glossed hands writes
   them (rare_classes.tsv); plus **C6** (8 signs), which this audit moves to unread/null.
3. The **person reads**: ASKS 88 (f.108r gloss, the pre-registered H107 prediction waiting on it) and ASKS 89; ASKS 93 (f.211r
   glossed run) would add a held-out known answer.
4. A period key sheet or decipherment of f.61 itself, if one exists (F61-FAMILY-7's fr.3641/fr.4699 leads).

The runner's f.108v evidence (H85/H93/H94/H100-H103) was not re-audited here: it tests the f.61-fitted cell map, not key v4,
and f.108v carries a sparse period gloss of its own (BnF "chiffre et déchiffrement"), so it is a partly known-answer check, to
be weighed once that gloss is read.

### Novelty

The only plaintext on this leaf is Tomokiyo's own five spans (published, his tentative reading): for those, the plaintext is
known (text: known) and our key's agreement with it is a test of the key. No passage outside the spans is recovered, so there is
nothing to class; no N-class is assigned to the leaf and no SECOND-OPINIONS-QUEUE.tsv row is filed. A class for any future
passage would need: the passage read at S or better with a control that a blind reader cannot pass on permuted keys, then the
logged novelty search (CHECK-SOLVED-WEB in NOTES.md, 28 Sept, found no prior reading on the open web; still needed: the Mayenne
correspondence editions and calendars for 1592-93, the BnF finding aid for fr.4715, Google Books/IA/HathiTrust phrase search on
the passage, the open scholarship indexes, JSTOR rows) and a second adversarial audit before anything above N1 goes outward.

**Safe sentence.** "A period key rebuilt from the interlinear decipherments of three sister leaves in the Mayenne cipher reads
Tomokiyo's five marked spans on BnF fr. 4715 f.61r at 42-48 of 55 letters, against a permuted-key 95th percentile of about 25; no
passage outside his spans can yet be read, and 59 of the leaf's 99 signs remain a choice between two or more letters."

**Unsafe sentence.** "f.61r is now 20% read with firm letters and the rest two-way, so the letter is essentially recovered"
(the firm share includes 8 C6 tokens contradicted by the known answer; no word outside the spans is forced; two-way sets are not
readings).

### Over-claims in the folder

None corrected in NOTES.md or KEY.md (outside this brief's files). For the orchestrator: KEY.md "## v4" and ROOM 15:18 state the
meter as firm 20; this section supersedes that figure with 12/59/28 as a grade statement. Their 0.873 stands with the 0.764
conservative figure beside it.

### Confidence

Key v4's rows as period attestations: high. The known-span test as evidence that the key fits this cipher: high (0/4000 permuted
keys; holds at 0.764 without the Tomokiyo-validated relabel). The meter as graded: moderate after the C6 regrade. Any reading of
f.61r outside the spans: none exists.
