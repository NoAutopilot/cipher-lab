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

## VERIFY-F61-V5 (29 Sept 2026)

Verifier: PARENT WORKER VERIFY-F61-V5 (Opus 5.5, session_01GgtGry5o3rrdf23A11VKhT), 00:14-00:4x UTC by the container clock; separate
from campaign runner 6 (session_016YPPumG1PbhMJ3pBLuqaeW), whose steps H168-H182 and H177b stages 2a-2d are audited here (its ROOM
lines show H180 and the follow-ups H181, H182, H177b 2b-2d done; the open remainder of H177b, f.176v and fol. 179, is not audited).
Brief: `.claude/briefs/runs/2026-09-28-verify-f61-v5.md`. Working files, each with a `--check`: `verify_v5/`. Six Opus vision calls
(fresh subagents, prompts pushed first in `verify_v5/PROMPTS.md`, 8295ff29); 2 Gallica requests (canvases 327, 329, `family/requests.log`).
Nothing edited in `family/key_period_v4.tsv`, `CAMPAIGN.md` or the runner's files.

**Claim under audit.** fr.3984 f.176r (Baudouin Desportes to Clement VIII, Paris, 22 July 1593) is written in f.61's polyphonic
cipher and fol. 177r(-v) is its separate-sheet period decipherment (H175); `family/key_period_f176.tsv` (H177) gives single letters
where v4 carries merged sets: VBAR_A t, EBR l (form B, H180), HASH4 d/q, 4STEM p/c, DBL o, ZHOOK i (H178/H182), BETA m.

### Verdict

| value (runner) | f.176r leaf, leave-class-out (runner passes; verifier's blind passes) | Mayenne hands vs shuffled-value controls | verdict for key v5 |
|---|---|---|---|
| VBAR_A t (cell g/t) | t85 g12 of 176, cell 0.55 vs wrong 0.20; blind 14/26 and 18/33, gate PASS both blocks | f.61 t 3/3 (p 0.14); f.108r t5 g2 7/7 (**p 0.005**), s 0/10; f.108v rank 6/51 | **endorse g/t** (replaces s/t); on f.61 grade C, with VERIFY-F61-V4's caveat that f.61's VBAR_A/VBAR_B boundary was set by sorts scored on Tomokiyo's letters |
| EBR l, form B (cell l/y) | l83 y17 of 149, cell 0.67 vs 0.18; blind 22/28 PASS, 9/20 (0.45) FAIL-by-threshold, l top in both; H180 form B 11/11, anchors 14/14 | f.61 l 2/2 (p 0.095); f.108v EBR_B l/y rank 4/51; f.108r brackets are form A and read s7 f1 l2 (Tomokiyo's f/s), so l is not a class value | **endorse EBR_B = l/y only**; f.61's EBR tokens (all form B, H22 4/4) take l/y at C; EBR_A untouched (v4 s/l/a stays; f.108r's letters point to f/s, a separate question) |
| ZHOOK i (cell i/x) | i42 x4 of 86, cell 0.53 vs 0.23; blind 16/21 and 3/5, PASS both blocks (blind readers coded Desportes's i-sign as ZHOOK) | f.61 i 3/3, f.108r i 7/7 under an alignment that leaves ZHOOK out (the p 0.155 is any i-cell's; x cannot be tested); f.108v i/x rank **1/51**, gain 0.152 vs 0.065 dropped | **endorse i/x, graded S on f.61** (not C): the glyph link across hands failed H178b's tile gate; the link rests on letter agreement and sequence gain |
| DBL o | o30 b4 of 50, cell b/o 0.68 | -- | **not a DBL value.** On f.176r the readers' DBL is the side-by-side b/o glyph (v4's SBS; SBS itself o30 b4 of 55, cell 0.62). v4's DBL (stacked loops, e/r/u) is unchanged. It supports **SBS = b/o** (v4's e is the sort artefact VERIFY-F61-V4 named): f.61 SBS b/o 5/5 (p <0.005), f.108r 2/2, f.108v rank 2/51 -> **endorse SBS b/o** |
| HASH4 d/q | d44 q7 **i14** of 90 (cell d/q 0.57 vs 0.19); blind n 4, untestable | f.61/f.108r: no HASH4 at known positions; f.108v d/q rank 1/51 (and H160/H162) | **no change** (v4 d/i/q stays): i is 16% of the leaf's HASH4, above the key's own 0.1 rule; d/q dominant, i not excluded |
| 4STEM p/c | p17 c9 of 40 (cell 0.65 vs 0.24); blind n 1, untestable; reader coding 4STEM/4TRI/4PI unstable in both sessions | f.108r a 3/3 (**contradicts**, p 1.0); f.108v c/p rank 1/51 | **not endorsed**: the two Mayenne-hand tests disagree; v4 a/c/e/n stays; a data conflict to log, not settle by majority (rule 4) |
| BETA m (cell m/z) | m5 z3 t3 of 16 (cell 0.50); blind n 2 | f.61 m1 a1; f.108r m1 z1 u1 (p <0.005 on 3); f.108v m/z rank 1/51 | **held**: pointing to m/z, period n too small to replace m/s now |
| C43 a/n, INF u, VBAR_B s, PHI e/r | cells a/n 0.66, h/u 0.55, f/s 0.68, e/r 0.60 | as v4 | no change (confirm v4) |
| 4PI p/c, CROSS s (Desportes's glyphs) | cells c/p 0.63, f/s 0.55 | 4PI: Tomokiyo n (f.61), d x4 (f.108r); CROSS: his dashes | not for f.61 (different glyph or contradicted), as the runner said |

**Key v5 may take:** VBAR_A **g/t**; EBR_B **l/y** (form-B brackets only); SBS **b/o**; ZHOOK **i/x** (grade S on f.61). **May not
take:** DBL o (a reader code for the SBS glyph), 4STEM p/c (conflict), HASH4 narrowed to d/q (the leaf's own i share), BETA m/z (n), 4PI
p/c, CROSS s. Key source for all four endorsed rows: `period` (fr.3984 f.176r / fol. 177r, Desportes's hand), cross-checked on the
Mayenne hands against Tomokiyo's published letters (`published`, credited) and f.108v's sequence gain.

**f.61 meter under the endorsed values** (`meter_v5.py`, from `family/f61_decode_period_v4_frac0.1_sbs.tsv`, C6 kept unread/null per
VERIFY-F61-V4): **firm 12 / two-way 50 / wider 12 / unread-or-null 25** of 99 (v4 as regraded: 12 / 36 / 23 / 28). Tokens changed:
VBAR_A t/s -> g/t x6, EBR l/s/a -> l/y x4, SBS o/b/e -> b/o x7, ZHOOK unread -> i/x x3 (S). Still wider than two: 4TRI c/p/t 6, 4PI 2,
OTHER 2, 4STEM 1, HASH4 1. The firm count does not move: every endorsed value is a two-letter period cell (the design is polyphonic),
so a two-way token under v5 is a period cell, not an undecided merge. Known spans with j=i, v=u, y=i folded (2000 permuted keys, seed
20260929): f.61 v4 50/55 -> **53/55** (p95 0.455, 0/2000 at or above); f.108r v4 65/84 -> **74/84** with EBR left at v4 (p95 0.429,
0/2000). The f.61 gain is ZHOOK's three i positions.

### 1. Same design, and fol. 177r is its decipherment

- **Dates and item.** f.176r is headed "22 de Juillet 1593 / Tressainct pere" (the verifier's own look at the fresh native, canvas
  327). The BnF finding aid on disk (`sources/bnf-aem/cc504266_francais3974-3995.html`) gives item 84, fol. 176: "Lettre, avec chiffre
  et déchiffrement, de « BAUDOUYN DESPORTES » au pape Clément VIII. « De Paris, ce XXIIe juillet 1593 »", running to fol. 179.
- **Hands and text.** fol. 177r (canvas 329) opens "Tressainct pere / Vne larme aux yeux et lame plaine de desespoir ...", the cipher
  leaf's clear salutation, in a different, clear secretary hand with underlined stretches; no date line at its head. The verifier's
  blind read of fol. 177r L05-L12 and L23-L29 matches the runner's at a mean folded-letter similarity of 0.85 (0.62-0.99 per line,
  `agree_v5_result.txt`).
- **Text match.** `h175_gate.py --check`, `h173_power.py --check` fresh. With the verifier's own DP (`align_v5.py`, not the runner's
  f61crib.align), key v4's sets match 0.864 of aligned signs under fol. 177r vs 0.717 under the wrong text (runner material), and 0.796 /
  0.692 and 0.887 / 0.768 on the verifier's two blind blocks.
- **Design.** Under leave-class-out alignment every class's letters fall mainly into one of Tomokiyo's eleven two-letter cells
  (a/n, b/o, c/p, d/q, e/r, f/s, g/t, h/u, i/x, l/y, m/z): shares 0.50-0.68 under fol. 177r against 0.13-0.40 under the wrong text
  (0.13-0.24 for all but 4TRI 0.30, PHI 0.29, 4PI 0.40), for all 15 classes with n >= 16 (`align_v5_runner_result.txt`). That is the family's paired-cell design, shown from Desportes's own
  period decipherment rather than from his table. **Confirmed: same design; fol. 177r(-v) deciphers f.176r.**

### 2. Blind re-derivation, row by row (`agree_v5.py`, `align_v5.py verifier`)

Twelve rows (L06-L11, L28-L33; about 790 signs) read by two fresh blind passes on the verifier's own crops, with an atlas stripped of
its one letter-value remark. Sign counts per row agree with the runner's within 0-3 on every row. The verifier's consensus matches the
same code at 372 of the runner's 624 consensus signs (0.60; per row 0.30-0.73, lowest L31-L32). Systematic coding differences, not value
differences: the runner's VBAR_B is the verifier's ISH (33/33; reads s 25/34, cell f/s); the runner's DBL is the verifier's PHI or SBS;
4STEM / 4PI / HASH4 are unstable between the sessions (too few agreed columns to test). Key rows re-derived at n >= 5 on the blind
material: VBAR_A t, EBR l, ZHOOK i, INF u, PHI e, VBAR_B/ISH s -- **every one agrees with key_period_f176.tsv's top letter**. EBR's
second block falls under the 0.5 share threshold (9/20, l still top). HASH4, 4STEM, BETA, DBL: not reproducible from the blind sample (n
<= 4), so for those the leaf evidence is the runner's passes re-aligned by the verifier's own DP.

Pre-registered single-letter gate on the runner's material: only DBL, INF, VBAR_B, SBS reach share >= 0.5. VBAR_A (0.48), HASH4
(0.49), ZHOOK (0.49) and EBR (0.56, but a permuted-anchor p95 of 1.00 at small n) miss it by the letter, because each class carries
its cell partner (g, q, x, y). The verdict above therefore rests on the cell shares and the wrong-text contrast, which were computed
after the gate was fixed (`align_v5.py`'s cell column); that post-hoc step is named here.

### 3. Transfer to the Mayenne hands (`transfer_v5.py`)

Positions set by alignment with the class left out; Tomokiyo's letters there against 200 random two-letter cells drawn from fol.
177r's letter frequency; f.108v by the H127 sequence gain with the class set to each of Tomokiyo's 11 cells and 40 random pairs.
Figures in the verdict table. Two limits: f.61 has 2-8 known positions per class (p-values of 0.1-0.2 at n = 2-3 are all such a
leaf can give); and Tomokiyo's letters are his reading, not a period gloss, so agreement with them is agreement with a published
reading (the same status VERIFY-F61-V4 gave them).

### Findings about the runner's files (for the orchestrator; not edited)

1. **The N cap truncates the key's coverage.** `build_f176_key.py` trims the clear to N = 0.8 x signs (2,476 letters). The
   alignment ends at f.176r L40 against fol. 177r L33 (`verify_v5/rowmap.py`), so rows L41-L47 and every fol. 177v line contribute no
   pairs. "key_period_f176.tsv now covers all of f.176r (3,095 signs) against ... fol. 177r-v" (NOTES H177b stage 2d, ROOM 23:34)
   should read "f.176r L01-L40 against fol. 177r L01-L33". The rows themselves are sound.
2. **DBL o** in the key file is a reader code for the SBS glyph (runner's own note), and a merge script that takes class names at face
   value would write o into v4's DBL cell. Merge it as SBS, or not at all.
3. **H182's 10/10** was computed under a test key that already held ZHOOK i/x, which lets the DP place i opposite ZHOOK. Re-run with
   ZHOOK left out of the aligning key, the letters are the same (f.61 i 3/3, f.108r i 7/7; VERIFY-F61-V4's two-way table had the same
   three f.61 letters under v4), so the result stands; the method needed the leave-out.
4. One blind pass (P, L06-L11) wrote its TSV through a Python helper rather than the Write tool (the subagent's own report); it read no
   other file. Kept, noted.

### Novelty

None to class. No passage of f.61r outside Tomokiyo's spans is read by these values; the known-span figures are a test of the key
against his published letters (text: known). No SECOND-OPINIONS-QUEUE.tsv row.

**Safe sentence.** "The period decipherment of a second letter in the same polyphonic cipher (BnF fr. 3984 f.176r, Desportes to Clement
VIII, 22 July 1593, deciphered on fol. 177r) fixes four cells of the rebuilt period key -- g/t, l/y for the plain bracket, b/o and i/x --
after which the key reads 53 of the 55 letters Tomokiyo marked on fr. 4715 f.61r; the rest of that leaf remains a choice between the two
letters of each cell."

**Unsafe sentence.** "The fr. 3984 decipherment now gives single letters for f.61r's two-way signs" (the endorsed values are two-letter
cells; firm letters did not increase; 4STEM, HASH4 and BETA were not narrowed).

### Confidence

f.176r / fol. 177r as a same-design cipher and decipherment pair: high. VBAR_A g/t, EBR_B l/y, SBS b/o as period values carried to
f.61: high to moderate (small known-position counts on f.61, strong on f.108r for VBAR_A). ZHOOK i/x on f.61: moderate (letter
agreement and sequence gain, no glyph link). The meter: mechanical from the committed decode, with the four changes above.

## VERIFY-F61-V6 (29 Sept 2026)

Verifier: PARENT WORKER VERIFY-F61-V6 (account 3; Opus), 04:12-04:4x UTC by the container clock; separate from campaign runner 8
(session_011Taenrv3JSdk7VjpiBjids, retired) and runner 9. Brief: `.claude/briefs/runs/2026-09-29-verify-f61-v6.md`. Working files, each
with a `--check`: `verify_v6/`. Eight Opus subagent calls (three blind shape readers, one judge control, two judge targets; prompts
committed before the calls in `verify_v6/PROMPTS.md`, 919fe064 and 8e51a62a), 2 Gallica requests (canvases 327, 328; `verify_v6/requests.log`).
Nothing edited in `family/key_period_v5.tsv`, `CAMPAIGN.md` or the runner's files. H209-H227 (the hash family) are not audited.

**Claim under audit.** The 4-family shape rule (runner 8, ROOM 02:50 and 03:48 UTC): a figure-4 sign whose stem ends in a closed bowl
below the line reads c/p, one without reads a/n, read by blind shape answer rather than by pass code; in cell form for the known-span
lines, 4TRI c/p, C43 a/n, 4STEM a/n (`family/h219_shape_testkey.py`).

### Verdict: endorse in part

| leaf (letters) | runner | verifier's blind re-read on fresh crops (all three calls: runner's H193 anchor strips 18, 17, 18 of 20; the same anchors in the verifier's framing 18, 18, 18 of 20; gate 17) | verdict |
|---|---|---|---|
| f.176r (period decipherment, fol. 177r) | H193: bowl yes c/p 5 a/n 0; no c/p 4 a/n 23 (p 0.00063) | H193's 40 targets re-cut: same answer 39/40; bowl yes c/p 5 a/n 0, no c/p 4 a/n 24 (p 0.00053). 40 **fresh** 4-family columns of any reader code (20 c/p, 20 a/n): yes c/p 13 a/n 3, no c/p 6 a/n 15 (**p 0.0025**). Pooled: yes 18/3, no 10/39 (p 4e-7) | **endorse** as a period-attested shape distinction in Desportes's hand; not exclusive (10 of 49 no-bowl columns read c/p, 3 of 21 bowl columns a/n) |
| f.61 (Tomokiyo's published letters) | H194: 14/14 (p 0.0005) | list method on the verifier's own line cut: the same 14 positions, bowl = 4TRI exactly, Tomokiyo c/p 5/5 and a/n 9/9 (p 0.0005); L01 again unmatched (4 listed vs 3 codes), L07 lists one 4-shape the readers never coded | **endorse** for f.61's hand: 4TRI c/p (t dropped), the one 4STEM token (L11) a/n; grade **S** (period value from another hand, linked by a blind attribute, checked against a published reading, not a period gloss of f.61) |
| f.108r (period gloss, Tomokiyo's overlay) | H202: yes c/p 3 a/n 0, no c/p 2 a/n 11 (p 0.018), registered rule NOT met | yes 0, no c/p 5 a/n 11 (p 1): no bowl seen at any position, including the four 4TRI c/p. The f108sheetB bands clip the stem foot of some 4TRI (verifier's look after scoring) | **not endorsed**: untestable at these crops; two blind readers disagree (3 vs 0 of the 4TRI) |
| f.108v (no letters; sequence) | H199: 4STEM yes 19 of 21 | 9 yes (4STEM 8 of 24 answered, OTHER 1), same answer as H199 on 58/74 | **not reproduced** as a shape read |

**Task 2, the H193 alignment.** (`align_check.py`, `context_check.py`.) The anchors are aligned to fol. 177v from V06 on and the targets to fol.
177r plus 177v V01-V05: no line in common; the aligning key (`key_period_v4.tsv`) holds no f.176 row; the bowl attribute was named from the
f.176v anchors only. **No period letter was used both to set and to test the rule.** Key v4's 4TRI set is {a, c, n, p, t}, so the DP scores c/p
and a/n alike at a 4TRI column and cannot steer the split. Re-aligning with every 4-family class removed from the key moves 10 of the 40 targets
and leaves 4 unpaired (Fisher p 0.26), but that alignment drifts about 45 letters on L31-L32 once a fifth of the anchoring signs are blank, so
it is the worse alignment, not a correction. Word context under the runner's alignment settles the five bowl/c-p positions: "les [c]hoses",
"aue[c] sa saincteté", "l'obsta[c]le", "s[ç]ait", "de [c]este matiere"; two of the four no-bowl c/p are genuine ("de [p]auureté", "au[c]un").
**Alignment confirmed at every position that carries the result.**

**Task 3, H201 and H208 re-scored** with the verifier's seeds and a null of random relabels holding the yes/no counts (19 c/p of the 68
answered f.108v 4-family columns). H201 (`rescore_h201.py`, shuffle seeds 6000-6019, 1000 relabels seed 6202): the runner's bowl labelling
0.278 ranks 1 of 1001 (best random 0.243) and beats the readers' cells 30/30 -- **reproduced against that null**. But a code-level labelling
(4STEM c/p, every other 4-family a/n, agreeing with the bowl answers on 64 of 68 columns) scores 0.290, and the bowl labelling beats it 0 of 30.
H208 (`judge_v6.py`; control seed 6207 PASS, fitted map 6.5 rank 1 of 21): runner's bowl labelling 8.0 and 8.0, above every one of 17
same-count random relabels (max 5.0 and 3.5) in both seeds -- **reproduced against that null**; code-level 9.0 and 7.0; the verifier's own
bowl answers 6.5 and 4.0; pass codes 4.0 and 2.5. Both judge calls read their sets file in two pages (two Reads of the one file; not voided).
So f.108v's sequence evidence says **the H59 passes' 4STEM is the c/p sign on f.108v**; it does not separate a shape read from that code swap,
and the shape read itself did not reproduce.

**Test key re-run.** `h219_shape_testkey.py` reproduces byte-identical: f.61 53/55 under v5 and under the test key; f.108r 74/84 both, with
H202 S14 the one known exception. The cells lose no known letter.

**What should merge (for the orchestrator; key v5 not edited).** Into the f.61 reading: 4TRI **c/p** (drop t) and f.61's single 4STEM token (L11)
**a/n**, grade S, key source `period` (fr.3984 f.176r / fol. 177r) linked by the blind bowl attribute. Not as a pooled v6 cell: **4STEM a/n**
(f.108v's 4STEM is the c/p sign by sequence; a code conflict between leaves, rule 4, not settled by majority), nor the general rule "read the
4-family by blind shape answer instead of pass code" on f.108r/f.108v/f.101r, which a second blind reader did not reproduce off Desportes's
leaves and f.61. C43 a/n unchanged.

**f.61 meter under key v5 plus the endorsed part** (`meter_v6.py`): **firm 12 / two-way 57 / wider 5 / unread-or-null 25** of 99 (v5: 12 / 50 /
12 / 25), with L01's 4TRI taken at code level (every f.61 4TRI tested by shape, 5 per reader, was the bowl sign); holding that one token back
because neither session matched it by shape: 12 / 56 / 6 / 25. Still wider than two: 4PI 2, OTHER 2, HASH4 1.

### Novelty

None to class: no passage of f.61r outside Tomokiyo's spans is read by these values, and the firm count does not move. No
SECOND-OPINIONS-QUEUE.tsv row.

**Safe sentence.** "In Desportes's 1593 letter and its period decipherment, a figure-4 sign with a closed bowl below the line stands for c or p
and one without mostly for a or n; the same shape distinction on fr. 4715 f.61r narrows its 4TRI signs to c/p, leaving f.61r at 57 two-way
positions out of 99."

**Unsafe sentence.** "The 4-family is read by shape across all the Mayenne leaves" (f.108r and f.108v did not reproduce under a second blind
reader), or any sentence giving f.61's 4TRI a single letter.

### Confidence

The bowl/c-p association on f.176r: high (two blind readers, a fresh any-code sample, alignment checked by word context). The narrowing on
f.61: moderate (five 4TRI tokens, shape = code on all 14 matched positions in both sessions, agreement with a published reading). The shape
rule off those two leaves: not shown.

## VERIFY-F61-V7 (29 Sept 2026)

Verifier: PARENT WORKER VERIFY-F61-V7 (account 3; Opus), 05:13-05:30 UTC by the container clock; separate from campaign runner 9 (which posted H224)
and from VERIFY-F61-V6 (the bowl rule; not re-audited here). Claim under audit (H224, runner 9, 04:04 UTC): on f.188r the HASH4 rows the period
decipherment reads i/x are the "2#" sign and the 4-head reads d/q, so key v5's HASH4 i 10 / x 3 (f.188r/f.184r) is H24 support mis-coded as HASH4,
and HASH4 proper reads d/q on f.101r, f.188r and f.274r. The runner disclosed that its category D (2#) was added after a look at the sheet.

Files: `verify_v7/v7_hash_sort.py` (design and read-outs committed a87fa876 and 127f5a44 before any vision call), `v7_items.tsv` (key, committed
229bec99 while the calls ran, before any answer), `PROMPTS.md` (prompts verbatim, disclosures), `v7_reply_setD.tsv` / `v7_reply_setN.tsv` (blind
replies verbatim), `v7_hash_sort_result.txt` (`--check` OK), `v7_perleaf.py` + result (per-leaf check, written after scoring), `meter_v7.py` + result.

### Verdict: endorse

**Design.** Fresh Gallica natives (f.188r, f.101r, f.106r; sha1 = MANIFEST; f.274r from disk), crops cut from the cipher row only, so no
interlined gloss letter is in view, grey + autocontrast on every tile. 124 tiles: every f.188r HASH4 i/x/d/q row (27) plus H24 i/x 10 and H24 d/q 3;
f.101r HASH4 d/q 10, HASH4 i 4, H24 i 10, H24 d/q 4; every f.274r HASH4/H24 lettered row (21; there H24 came from a pass-A/pass-B code split,
not from any shape sort); f.106r HASH4 5, H24 5; the 24 H212 f.108 tiles (23 = the runner's anchor set); f.61's one HASH4. 8 tiles repeated
under new ids. Two fresh blind Opus readers, one per sheet set, with separate shuffles and ids. Categories were fixed by the brief before any look:
**setD** = 4-head / 2-hook "2#" / looped / other; **setN** = the same without 2# (answers task 3: "with and without D" as two separate calls, not
by folding answers afterwards). Null: 20,000 permutations of the shape labels within each lettered leaf. The verifier looked at one strip of seven
tiles before the calls, for marker placement only (disclosed in PROMPTS.md).

| check | setD (with 2#) | setN (without 2#) |
|---|---|---|
| anchor gate, H212 tiles as their H212 group (>= 0.8, the runner's 8/10) | 21/23 PASS | 20/23 PASS |
| repeat control (8 tiles shown twice) | 8/8 identical | 8/8 identical |
| pooled, 89 lettered tiles | 2# i/x-share 38/42 = 0.90; 4-head d/q-share 37/45 = 0.82; within-leaf permutation p 5e-05 | i/x tiles on the 4-head 4/47 = 0.09; p 5e-05 |
| f.188r | 2# i/x 18 d/q 2; 4-head i/x 4 d/q 16 (Fisher p 1.7e-05) | not-4-head i/x 20 d/q 2; 4-head i/x 2 d/q 16 (p 3.8e-07) |
| f.101r | 2# 9/2; 4-head 4/12 (p 0.0063) | 12/2; 2/12 (p 0.00042) |
| f.274r | 2# 11/0; 4-head 0/9 (p 6e-06) | 11/1; 0/9 (p 3.4e-05) |
| H224 replicate: f.188r HASH4-coded i/x rows | 2# 10 of 12 (H224: 8 of 11) | not-4-head 10 of 12 |
| f.106r (held, no letters) | HASH4 looped 5/5; H24 2# 5/5 | HASH4 looped 4, 4-head 1; H24 other 5/5 |
| f.61 L01 HASH4 | 4-head | 4-head (reader: "less sure") |

Registered read-outs: setD **"split holds (2# i/x, 4-head d/q)"**; setN **"split visible without D"**. Each lettered leaf clears on its own
(checked after scoring, rule 3's per-unit paragraph), so none of the three leaves rides on the others. **On the post-look category D:**
without D, the setN reader put 43 of 47 i/x tiles outside the 4-head and 9 of 45 d/q tiles there. Its hand-back described most of those
"other" answers, unprompted, as "a hash with a '2'-shaped head, which is neither the figure-4 head nor the looped form". The 2# class came back
from a reader who was never offered it. For comparison, the runner's own H224 reply with D folded into "other" still gives
i/x 2 of 11 on the 4-head against d/q 12 of 14. D's late addition therefore does not carry the result.

**Caveats.** (1) The 4-head still takes i/x at 4 of 20 on f.188r and 4 of 16 on f.101r, and the 2# takes d/q at 2 of 20 on f.188r: the cells are
d/q-dominant and i/x-dominant, not clean. H226's stray HASH4 letters (p, s, b, f ...) mostly sit on the 4-head and are not explained by this
split. (2) The pass codes cut across shape in both directions: HASH4-coded i/x rows are the 2# (11 of 16), and H24-coded d/q rows are mostly the
4-head (4 of 7, setD). A key built by pass code keeps mixing the two signs whichever code it trusts. (3) The looped hash (f.106r's HASH4, most of
f.108r's) has no period value. This audit does not give it one and does not endorse reading it d/q or i/x.

**What key v5 would change (for the orchestrator; `family/key_period_v5.tsv` not edited).** Key the hash family by shape, not pass code:
- **HASH4 (the 4-head hash) = d/q**, grade C on f.101r/f.188r/f.274r (period decipherments), linked to other hands by the blind shape attribute.
  Remove f.188r's HASH4 **i 10, x 3** from the HASH4 row. f.101r's HASH4 i 4 stays as stray support (1 of the 4 answered 2#, 2 answered 4-head).
- **H24 (the 2# sign) = i/x** (j/y as period spellings of i), with f.188r's i/x rows from the HASH4 row added (by shape: 10 of 12 are the 2#). Its
  d/q strays that sit on the 4-head move the other way.
- The **looped hash** is a third class. It needs its own row, marked unread, never pooled into HASH4's counts (f.106r's and f.108r's HASH4 are
  mostly this form).
- By the same test, H235's f.61 ZHOOK = 2# link would make ZHOOK the H24 cell (i/x). That is a grade question for ZHOOK's row, not tested here.

**f.61 meter** (`verify_v7/meter_v7.py`, bands as meter_v5.py): f.61's one HASH4 (L01) is the 4-head in both blind readers, as in H233, so it
reads **d/q** (grade S: period value from three leaves' decipherments, linked by blind shape). H24 does not occur on f.61.
- v5: firm 12 / two-way 50 / wider 12 / unread-or-null 25.
- v5 + this audit alone: **12 / 51 / 11 / 25**.
- v5 + VERIFY-F61-V6's endorsed part (4TRI c/p, the one 4STEM a/n, form A): 12 / 57 / 5 / 25.
- **v5 + V6 + V7: 12 / 58 / 4 / 25**. Still wider than two: 4PI x2 (H233: a 4 over a Pi, not audited here), OTHER x2.

### Novelty
Not assessed. This audit is about a key cell, not a reading, and no plaintext claim is made (rule 10).

### Confidence
High that the three period-lettered leaves separate a 2# i/x sign from a 4-head d/q sign: the result holds with and without the post-look
category, on each leaf alone, with a stable reader and a passed anchor gate. Moderate on the single f.61 token: one tile, cut from a different
source image at a larger scale, and one reader marked it "less sure".

## VERIFY-F61-V8 (29 Sept 2026)

Verifier: PARENT WORKER VERIFY-F61-V8 (account 3; Opus), 08:13-08:2x UTC by the container clock. Separate from campaign runner 9 (which posted H235/H254 and
H233/H239/H240/H255) and from VERIFY-F61-V6 and V7. Brief: `.claude/briefs/runs/2026-09-29-verify-f61-v8.md`. Claims under audit (ROOM 05:48 and 05:51 UTC;
`family/v6_shape_candidates.tsv`): (1) ZHOOK = the 2# sign; (2) 4PI is two signs, the 4-head hash (d/q) on f.101r/f.108r and a 4 over a Pi on f.61
(a/n, from Tomokiyo S5's n).

Files in `verify_v8/`: `v8_shape_sort.py` (design, categories and read-outs committed 585a5abe before any tile existed or any look), `v8_items.tsv`
(key, committed 48b13154 before the calls), `PROMPTS.md` (prompts verbatim, disclosures), `v8_reply_set{F,G,N}.tsv` (blind replies verbatim),
`v8_shape_sort_result.txt` (`score --check` OK), `meter_v8.py` + result (`--check` OK). Two Gallica requests (f.188r, f.101r natives; sha1 = MANIFEST;
`family/requests.log`). Three Opus subagent calls. Nothing edited in `family/key_period_v6.tsv`, `CAMPAIGN.md` or the runner's files.

**Design.** 115 tiles plus 8 repeated under new ids, all fresh cipher-row crops at about +-60 native px, grey + autocontrast, red markers:
- f.274r's 21 lettered H24/HASH4 rows form the **gate**: i/x -> 2#, d/q -> 4-head, set by letter class and not by any earlier reader's answer.
- **Lettered 4PI rows:** every one on f.188r (18) and f.101r (7), with 6 H24 i/x, 6 HASH4 d/q and 4 C43 a/n per leaf.
- **f.61:** ZHOOK 3, 4PI 2, HASH4 1, C43 3.
- **f.108r:** ZHOOK 7 and 4PI 9. Every 4STEM/4TRI on L02/L03 and 5 C43 serve as in-hand distractors. The L02/L03 segments are joined end to end, so signs at a segment boundary are whole.

The categories were fixed before any look, and the verifier's one look (six tiles, marker placement only) is disclosed in PROMPTS.md. There were three
readers, each with its own shuffle and ids. **setF** and **setG** used A 4-head / D 2# / E figure-4 on stems not crossed by hash bars / B looped / N other.
**setN** used A / B / N only, with a few words per N. The null is 20,000 within-leaf permutations of the shape labels.

| check | setF | setG | setN |
|---|---|---|---|
| gate, f.274r (>= 0.8) | 20/21 PASS | 20/21 PASS | 9/21 **CONTROL FAIL** (not scored; see below) |
| repeat control | 8/8 | 8/8 | 8/8 |
| Z1 ZHOOK -> D (shape only), Mayenne hand | 10/10 (f.61 3/3, f.108r 7/7); in-hand distractors D 0/27; p 5e-05 | 10/10 (3/3, 7/7); 0/27; p 5e-05 | every ZHOOK "A", noted "2-like curved head on hash" |
| Z3 f.108r overlay letters, #(D & i/x) + #(A & d/q) | S 11, p 5e-05 | S 11, p 5e-05 | - |
| period 4PI rows lettered d/q | A 12/12 | A 12/12 | A |
| period 4PI rows lettered a/n (f.188r) | E 7/7, noted "4r-like" | N 7/7, noted "4 + r-like tail" | N, "plain 4 followed by r" |
| f.108r 4PI (9) | A 9/9 | A 9/9 | A |
| f.61 4PI (2) | E, E, noted "4 over Pi" | E, E, "4 over pi" (chance both E 0.007) | N, "4 on two long stems" |

Registered read-outs (both setF and setG): **ZHOOK sorts with the 2#: yes** (f.108r only: yes); **P2 f.61's 4PI is a different sign from f.108r's:
yes**; **P1 "two signs on the period leaves" (E <-> a/n): no** (setG's E holds 1 tile), **P1 "period 4PI rows are the 4-head": no** (setF's E 10 of 25 is
at or above the 0.15 limit).

**setN's gate failure.** The reader without D put the 2# i/x tiles under A. Its hand-back says about 30 of its A answers carry "a 2-like curved head" and
are noted so. By the registered rule the call is not scored. Descriptively, its notes give every ZHOOK tile the same "2-like curved head" words it gave
the period 2#.

**Where results rest on the overlay alignment.** Z1 and P2 use no letters. Z3 and the f.108r d/p values rest on Tomokiyo's overlay reprint. That alignment
was re-checked without vision (`align_check` in the script). On L02 every ZHOOK/4PI letter is the same three ways: under key v6, under key v6 with ZHOOK
and 4PI removed, and by position alone (39 signs = 39 letters). On L03 (43 signs against 45 letters) the first two ways agree. The ZHOOK letters are
i 5 and j 2, and the 4PI letters d 4 and p 1, unchanged. **The overlay letters at these positions do not follow the key under audit.**

### Verdict (1) ZHOOK = the 2# sign: **endorse**

Two blind readers put all ten Mayenne-hand ZHOOK tiles, f.61's three included, in the 2# class. They put none of 27 in-hand distractors there, and each
passed the gate and the repeat control. f.108r's overlay letters at ZHOOK are i/j (= i) under a key-free positional alignment. This gives ZHOOK's
i/x on f.61 the glyph link that H178b could not find: the period i/x value (the H24 cell, grade C on f.101r/f.188r/f.274r) reaches f.61's ZHOOK by a blind
shape attribute. **Grade S** (period value from other hands, linked by blind shape), as for HASH4 in V7. The value is unchanged, so no meter token
moves. What should merge: ZHOOK's row keeps i/x and its note records "the 2# sign = H24 cell, glyph link VERIFY-F61-V8", replacing "no glyph link".

### Verdict (2) 4PI is two signs: **endorse in part**

- **Endorsed: the split.** Every period 4PI row lettered d/q (12 of 12 in both readers) and every f.108r 4PI (9 of 9 in both) is the 4-head hash.
  f.61's two 4PI are something else: E in both readers, and they are the only tiles either reader called "4 over Pi". f.61's 4PI is therefore not
  HASH4/4-head and should not carry d/q. f.108r's 4PI reads d/q as the 4-head (grade C from the overlay letters d 4, p 1, alignment checked above).
- **Not endorsed: a/n for f.61's form by glyph.** The period 4PI rows lettered a/n (f.188r, 7) are a third form, a 4 followed by an r/3-like tail. The
  readers describe it in the same words as several period C43 tiles, which read a/n. Neither reader matched it to f.61's 4-over-Pi: setG kept them apart
  (N vs E), and setF's notes do too ("4r-like" vs "4 over Pi"). The registered E <-> a/n read-out failed. f.61's a/n therefore rests on one published
  letter, Tomokiyo S5's n at L11 9. L01 12 lies outside the published spans. That is grade **M** for L11 9, and L01 12 has no value.
- **Finding for the key (not tested as a registered read-out).** Key v6's pooled 4PI row mixes two period signs on f.188r: the 4-head (d 9, q 2) and the
  4-with-r-tail form (a 5, n 1, and the e/h/r strays). The next key should split it the way V7 split the hash family, keeping 4PI (4-head) at d/q. The
  r-tail rows might be C43 miscoded as 4PI; that deserves one test, and this audit only describes it.

### Meter (`verify_v8/meter_v8.py`, key v6, f.61 reading key; bands as meter_v5/v7)

- v6: firm 12 / two-way 58 / wider 4 / unread-or-null 25.
- v6 + ZHOOK = 2#: 12 / 58 / 4 / 25 (value unchanged; grade note only).
- v6 + both cells as endorsed here (4PI split, f.61's two 4PI held unread): **12 / 58 / 2 / 27**.
- v6 + split, with L11 9 at a/n grade M on Tomokiyo alone and L01 12 unread: 12 / 59 / 2 / 26 (variant added after scoring).
- v6 + H240 as proposed (both f.61 4PI a/n): 12 / 60 / 2 / 25. **Not endorsed**: L01 12 has no source for a/n.
- Still wider in every variant: OTHER x2.

**What should merge (for the orchestrator; key v6 not edited).**
1. ZHOOK note: glyph link to the 2#/H24 cell, grade S.
2. 4PI: the 4-head reads d/q (f.101r, f.108r, and f.188r's d/q rows).
3. f.61's 4-over-Pi becomes a separate class. L11 9 reads a/n at grade M from Tomokiyo's letter alone; L01 12 stays unread.
4. The pooled 4PI row should be split before any further pooling.

### Novelty
Not assessed. This audit concerns key cells, not a reading, and makes no plaintext claim (rule 10).

### Confidence
- **ZHOOK:** high. Two readers agree 10/10 against 0/27 distractors, the gates pass, and the letter test is supported by an alignment that does not use
  the code.
- **The 4PI split:** high for "f.61's 4PI is not the 4-head" (two readers, two tokens, the only "4 over Pi" answers). Moderate for f.108r = 4-head
  (shape clean; values from one overlay).
- **a/n for f.61's 4PI:** low. One published letter, no period glyph.
