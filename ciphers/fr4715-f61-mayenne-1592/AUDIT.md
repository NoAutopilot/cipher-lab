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

## VERIFY-F61-V9 (29 Sept 2026)

Verifier: PARENT WORKER VERIFY-F61-V9 (account 3), 10:16-10:4x UTC by the container clock. Separate from campaign runner 10 (H256-H262) and
from VERIFY-F61-V6/V7/V8. Brief: `.claude/briefs/runs/2026-09-29-verify-f61-v9.md`. Claims under audit (ROOM 09:58-10:12 UTC): (1) f.61's CA is a
null drawn as the letter a (H256/H260 letterform sorts, H63 hand, H259 spans); (2) the C6 conflict (HYPOTHESES.md row of 29 Sept, H261): the pooled
C6 = e against Tomokiyo's dash at every in-span C6 on f.61; (3) the null band (`family/f61_null_band.tsv`, H262).

Files in `verify_v9/`: `v9_ca_sort.py` (design, categories, gates and read-outs committed 17ccf1ea before any tile existed or any look; one amendment
before the tiles, disclosed in PROMPTS.md), `v9_items.tsv` (key, committed 194c3fa7 before the calls), `v9_text_letters.tsv` (the placement helpers'
rows), `v9_bands.json` (line boxes), `PROMPTS.md` (prompts verbatim, disclosures), `v9_reply_set{P,Q,R}.tsv` (+ `v9_reply_setR_groups.txt`, the
readers' replies verbatim), `v9_ca_sort_result.txt` (`score --check` OK), `v9_ink_measures.tsv` (script-only), `v9_c6_words.py` + result (`--check`
OK), `meter_v9.py` + result (`--check` OK). No Gallica request (tiles cut from the native region already on disk). Six subagent calls: three Sonnet
placement helpers, three Opus readers. Nothing edited in `family/key_period_v6.tsv`, `family/key_period_v7.tsv`, `CAMPAIGN.md` or the runner's files.

**Design.** 49 tiles, all cut by the verifier from the native image at +-60 native px, never from the runner's sheets or tiles: f.61's ten CA
(H253/H257 positions mapped to native by the segment boxes), eleven cipher controls from the same runs (PHI 4, C43 3, C6 2, SBS 1, INF 1), nine
clear-text a's inside words (chosen by seed from the helpers' list after excluding every word and position the runner used), ten clear-text non-a
letters (o, u, n, e, c, d), three one-letter a's outside the runs (EDGE_A, descriptive only), and six repeats under fresh ids. Three fresh Opus
readers, each with its own shuffle and ids: setP and setQ with fixed shape categories (A bowl-and-right-stem, O ring, U arch, E loop-with-tongue,
S sign, X), setR a free sort in the runner's own format. Gates registered: text a in A >= 0.8; repeats >= 5/6; text non-a in A <= 1. Read-out Z1 "CA
has the clear a's letterform": >= 8/10 CA in A and <= 1/11 cipher in A; null: 20,000 within-line label permutations over the CA + cipher tiles.

**A finding before the sort.** The three placement helpers were asked only to list clear words and the x of their letters. Unprompted, they listed
seven of the ten CA positions as the one-letter word "a" (L01 8, L03 1, L03 9, L05 7, L05 8, L07 1, L08 10, each within 6 px of the runner's CA x)
and skipped L10's three (inside a run with no clear word beside them). A reader looking for clear text reads these signs as the letter a.

| check | setP | setQ | setR (free sort, G = its group A "small closed bowl with right stem tail") |
|---|---|---|---|
| text a in A (>= 0.8) | 8/9 PASS | 7/9 **CONTROL FAIL** (not scored) | 7/9 **CONTROL FAIL** (not scored) |
| repeats | 6/6 | 6/6 | 6/6 |
| text non-a in A (<= 1) | 1/10 | 1/10 | 1/10 |
| CA in A | **10/10** | 10/10 | 10/10 |
| cipher controls in A | **0/11** (all S) | 0/11 (all S) | 0/11 (C43 -> C, PHI/SBS -> B, C6 -> D, INF -> F) |
| S = #(CA & A) + #(cipher & not A), permutation p | 21/21, **p 0.0013** | - | - |
| Z1 CA has the clear a's letterform | **YES** | not scored | not scored |
| EDGE_A (descriptive) | A 3/3 | A 3/3 | A 3/3 |

**setQ and setR's gate failure is the verifier's sample, not the readers'.** The two text a's outside A in every reader are the same two tiles:
`a:affaires` (L08 x 2662), which PROMPTS.md flagged before the calls as showing an e-like letter under the marker, and `a:amoit?` (L04 x 1824), a
word the helper itself marked uncertain. Every other text a is A in all three readers, and every CA and every cipher tile gets the same answer in all
three (30 of 30 agree). Descriptively, then, three readers put all ten CA with the clear a's and none of the eleven cipher signs there; by the
registered rule only setP is scored. A post-hoc count that drops the two misplaced tiles (7/7 text a in A in every reader) is reported here as
post-hoc and is not used for the verdict.

**Ink measures (script, `v9_ink_measures.tsv`, no reader).** In the central 60 px of each tile: CA ink height 49.8 px mean, width 36.1, 220 ink
pixels; text a 54.0 / 53.9 / 299; cipher signs 96.7 / 54.5 / 782 (descenders); mean darkness the same for all three (101-104). CA is a little
smaller and lighter than the text a's inside words and much smaller than the cipher signs. This does not decide the hand (H63's cue was weight,
baseline and spacing, by one reader); it is consistent with an a written small in the sign row.

**Word test for the in-span tokens (`v9_c6_words.py`, from the runner's H259 alignment taken as given).** Inserting the cell letter at each in-span
sign's place in Tomokiyo's letter string: **C6 = e** lands inside a word he reads at 4 of 5 (cap|able, ava|ncees, jal|ousi, ea|u) and at the
compound boundary beau|pere at the fifth; L01 2 is a span edge (no test). **CA = a** lands inside ca|pable once and at a word boundary three times
(trop|avancees x2, beau|pere). So a letter at C6 would break his words four times; a letter at CA once.

### Verdict (1) CA is a null drawn as the letter a: **endorse in part**

- **Endorsed: the letterform.** In the verifier's own tiles, with fresh readers, all ten CA sort with the scribe's clear a's and no cipher sign does
  (setP registered PASS, p 0.0013; setQ/setR the same counts, unscored; the placement helpers read seven CA as the word "a" unasked). H256/H260's
  finding replicates. The runner's "hand" leg (H63, cipher 5 of 6 by one reader) is neither confirmed nor contradicted here; the ink measures say only
  that CA is a small, light a.
- **Endorsed with its condition: no letter in the spans.** At the four in-span CA, Tomokiyo's markup is a dash and his words are complete without an
  a (H259, re-run above). This rests on his reading of those words and on the runner's sign-to-markup alignment (48/55 letters fall in one table
  column per class, F61-CAL). It covers four of the ten CA; the six out of span (L01 8, L03 1, L07 1, L10 2, L10 9, L10 12) are null only by the
  assumption that one sign has one function on the leaf.
- **Not decidable from the leaf: "clear a drawn among the signs" versus "null drawn as an a".** Both are the letter a in the scribe's hand written
  inside a sign run with the same pen; the leaf's ink cannot separate them, and no sort or hand check can (the runner's H256 says so too). The
  difference is functional -- does the plaintext carry an a there -- and only the known spans answer it: at every in-span CA the answer is no. The
  three EDGE_A tiles show the limit from the other side: the same a-form stands alone at run edges (L05 560 after "sont", L03 2257 before "les",
  L08 2427 before "affaires"), where it may be the clear preposition; H63 dropped two of them as edge a's. Whether an a at a run edge is a clear
  word or a null is a plaintext question, open for those three and not part of the 99-sign transcription.
- **Caveat for the key, not for f.61.** The pooled key's CA class on the glossed leaves is not a null: f.101r glosses it - 2, c, q, s, t and f.188r
  c, p, s (key_period_v6/v7 rows). Either that class on f.101r/f.188r is not this glyph, or the null is f.61's own usage. "CA = null" is a published
  f.61 fact (Tomokiyo's dashes, H44) with a letterform now tied to the clear a; it is not a family cell and should not be pooled as one.

### Verdict (2) the C6 conflict: **endorse, with a sharper statement than the runner's**

- H261's "C6 = e neither gains nor loses a known-span letter" is true only because a dash is a wildcard in the scorer. Put the letter into his
  words instead and C6 = e breaks four of the five in-span words (cap|able, ava|ncees, jal|ousi, ea|u) and sits at a compound boundary at the fifth.
  On f.61, conditional on his reading, C6 is not e.
- **Which witness applies to f.61 and why.** Witness 2 is Tomokiyo's markup on f.61 itself: the same leaf, the same hand, a dash (an unread sign, not
  a value) at all five in-span C6, and the words around them complete. Witness 1 is the pooled cell from fr.3982 f.101r (Bishop of Lisieux to
  "monseigneur", Rome, 27 Oct 1592, glossed by Lisieux's secretary) and fr.3984 f.188r/f.184r (Desportes to Lisieux, Paris, 22 July 1593): another
  sender, the other side of the correspondence, another year, another hand -- and H237's blind sort put f.61's plain 6 apart from the glossed delta-
  shaped C6, so the glyph link is missing as well. Under rule 4 a cell with conflicting support is M in any letter whose direction, date or hand does
  not match the supporting witness; f.61 matches neither, and the word test then turns M into "not e here". The pooled cell stands for the leaves
  that glossed it. Not decided by majority (3 glossed tokens against 5 dashes are not commensurable: one side is values, the other is absences).
- What the runner's row should carry: "C6 = e is excluded on f.61 at 4 of 5 in-span positions by Tomokiyo's own words (v9_c6_words), not merely
  unsupported"; C6 stays unread-or-null on f.61.

### Verdict (3) the null band: **endorse**

`family/f61_null_band.tsv` re-counted from `family/f61_decode_period_v4_frac0.1_sbs.tsv` under key v6: unread-or-null 25 = CA 10, C6 8, LOOPBAR 4,
CROSS 2, LL 1 (ZHOOK's three "-" rows in the decode file carry i/x from the key and are two-way, correctly left out); wider 4 = 4PI 2, OTHER 2; no
token missing, none extra; every evidence file named exists (`NOTES.md#H238` is an anchor). The band is a hand-off table and changes no count.

### Meter (`verify_v9/meter_v9.py`; key v6 loaded plus the V8 cells = key v7 as merged, F61-FAMILY-11 10:17 UTC, whose own figure 12/59/2/26 is the baseline; bands as meter_v8, the last band split into published-null + unread)

- v6 as meter_v8: 12 / 58 / 4 / 25 [null 7 + unread 18].
- baseline (= v7 as merged): 12 / 59 / 2 / 26 [null 7 + unread 19].
- baseline + CA as null (endorsed): **12 / 59 / 2 / 26 [null 17 + unread 9]** -- no band count moves; ten tokens move from unread to null.
- baseline + C6 = e on f.61 (not endorsed): 20 / 59 / 2 / 18 [null 7 + unread 11].
- baseline + both: 20 / 59 / 2 / 18 [null 17 + unread 1].
- Meter verdict for the orchestrator: **unread** for C6 (8) and 4PI L01 12 (1); **null** for CA (10), LOOPBAR (4), CROSS (2), LL (1); the four-band
  figure stays 12 / 59 / 2 / 26.

**What should merge (for the orchestrator; no key file edited).**
1. CA: a published null (Tomokiyo, H44) whose letterform is the scribe's clear a (H256/H260, replicated here); f.61 reading only, never a pooled cell,
   and the glossed leaves' CA rows stay as they are.
2. C6 on f.61: unread-or-null, with the word-test sentence above in the HYPOTHESES.md conflict row; the pooled C6 = e untouched for f.101r/f.188r.
3. The null band as filed; nothing moves.

### Novelty
Not assessed. This audit concerns a null, an unread cell and a hand-off table, and makes no plaintext claim (rule 10).

### Confidence
- **CA has the clear a's letterform:** high (three readers 10/10 and 0/11, one scored at p 0.0013, two unscored by a text-sample gate failure of the
  verifier's own making; seven CA read as "a" by helpers not asked).
- **CA carries no letter (null):** moderate, conditional on Tomokiyo's reading and the alignment, direct for 4 of 10 tokens.
- **C6 is not e on f.61:** high conditional on his reading (4 of 5 words broken); the pooled cell's status elsewhere unchanged.
- **Null band counts:** high (script recount).

## VERIFY-F61-V11 (29 Sept 2026)

Verifier VERIFY-F61-V11 (account 3, Opus; separate from runners 13/14 and from V5-V10). Claim under audit: `family/PROPOSAL_v8_4tri.md` (runner 13,
H356-H366) -- the readers' 4TRI is two signs told apart by a stem-foot bowl, no-bowl = a/n (C43's cell), bowl = c/p/t. Gates fixed before looking:
`verify_v11/PREREG.md` (commit 7635912f; addendum E pre-registered before its calls). Scripts regenerate every figure with `--check`:
`verify_v11/v11_crosstab.py`, `v11_bowl.py score`, `v11_bowl_e.py score`, `v11_gain.py`, `meter_v11.py`; the tool runs are
`verify_v11/pkt_f101r_split.txt`, `pkt_f124r_split.txt`. No reading claim, no novelty class (rule 10); no key file or CAMPAIGN.md edited.

**A. Runner's bowl labels x period letter, f.101r (own join, within-leaf permutation null, 10,000 perms).** The brief's literal "non-conflict rows"
restriction cannot test this: `f101r_align.tsv`'s status is relative to the alignment's own EM key, in which 4TRI = n, so every non-conflict 4TRI row
reads n by construction (rule 3: a control that cannot vary). Reported anyway (n 67, all n: p 1.00). Pre-registered substitute, rows whose nearest
non-4TRI/C43 code rows on both sides `agree`: n 58, no&a/n 36, no&c/p/t 2, yes&c/p/t 14, yes&a/n 6 -- share 0.862, p 0.0001, **tracks**. All rows:
n 182, share 0.830, p 0.0001 (reproduces the runner's 118/12/33/19 exactly). P(a/n | no) 0.91-0.95; P(a/n | yes) 0.30-0.37.

**B. Fresh bowl reads (own tiles from the Gallica natives, own prompt, Opus reader, 5 calls; every call carried 10 known-answer anchors from Desportes's
hand, fr.3984 f.176v, H193's coordinates re-cut by me, and 6 repeats).** Every call passed both gates (anchors 9, 8, 9, 10, 9 of 10; repeats 6/6 each;
one reply id mistyped VOO for VQO, corrected in the reply file with a note).
- Random 40 f.101r tokens (pre-registered B(i)): only 5 of 31 lettered tokens were c/p/t, and the read **does not track** (share 0.613, p 0.60);
  P(a/n | no) 0.85 but P(a/n | yes) 0.82 -- this reader called "bowl" on 9 a/n tokens against 2 c/p/t.
- Letter-stratified 40 f.101r tokens (addendum E, reader blind to letter): share 0.750, p 0.0018 -> **tracks** at the bar; no&a/n 10, no&c/p/t 1,
  yes&c/p/t 17, yes&a/n 8. Pooled B+E (n 67): share 0.687, p 0.0007 -> unclear by the pre-registered bar.
- Agreement with the runner's labels on the same tokens: f.101r kappa 0.49 (random set, 34 tokens) and 0.35 (stratified, 36) -- below the 0.6 bar
  both times; f.124r 0.58 raw agreement on 24, and this reader called "bowl" on 10 of the 17 tokens the runner's reads relabelled no-bowl.
- f.124r has no usable period-letter join in this box (`f124r_align.tsv` is numeral-mode over a sign set that does not map onto `recf124r`,
  conflict 1417 of 1550 rows), so B(iii) was not computed.

**C. Order gain (tools/partial_key_test.py --cells, key v7 cells `key_v7_cells_h354.tsv`).** Runner's split drafts: f.101r 0.0970 (binned keys p95
0.0408, 0/100 >= real; shuffled target 0/3 signal, control clean); f.124r 0.0709 (p95 0.0435, 0/100; shuffled 0/3, clean). Against 30 random
splits of the same size (155 of 462 on f.101r, 202 of 441 on f.124r, relabelled C43): f.101r bowl split (0.0970 at seed 342) exceeds the random
p95 0.0884 (1/30 random >= it; median 0.0820); f.124r 0.0709 exceeds p95 0.0642 (0/30; median 0.0539). Drawing the random splits only from the
answered (agreed) tokens gives the same result (1/30, 0/30). So random relabelling to a/n raises the gain too (4TRI already carries many a/n by the
period gloss), but **the runner's labels pick better tokens than any random split** on both leaves.

**Per hand (rule 4: witnesses kept apart, not settled by majority).**
- *Desportes, fr.3984 f.176v:* the bowl separates the c/p anchors from the a/n anchors -- my reader 45/50 in direction across five calls (the same
  20 anchors reused, so not 50 independent tests), the runner's 17-19/20 per call. Two signs in this hand.
- *f.101r's hand:* the no-bowl answer carries a/n under both readers and both prompts (runner 118/130; mine 10/11 stratified, 27/31 pooled). The
  bowl answer is mixed (a/n 12-47% of bowl answers by reader and sample). Two signs in this hand, with the no-bowl sign the a/n sign; the bowl
  class as a reader answers it still holds a/n tokens.
- *de Diou, f.124r:* order evidence only (C: beats 30/30 random splits); readers disagree token by token (0.58); no letter test run here.
- *f.61's hand:* not read by this verifier. Runner 14's H367 (gate 19/20): 5 of 6 4TRI bowl, L05 14 no-bowl -- and the same position read bowl in
  H194, so L05 14 has two readings from the runner's own reads that disagree.

**Verdict: endorse in part.**
- *Endorsed:* 4TRI as the readers transcribe it holds two signs, and **a 4TRI token answered no-bowl in a gated blind read takes C43's cell a/n**.
  Witnesses: f.101r period letter under two independent readers/prompts/tile sets (runner 0.91 a/n; mine 0.91 stratified), the permutation null
  (p <= 0.002 each), and the gloss-free order gain beating random same-size splits on f.101r and f.124r with clean shuffled targets.
- *Not endorsed:* "bowl = c/p/t" as a firm or narrowed cell, or the bowl as a token-level criterion that transfers between readers. The
  bowl class still carries a/n (runner 19/52 of its lettered bowl answers; mine up to 9/11), and the two readers agree on the attribute only at kappa
  0.35-0.49 on f.101r. A bowl-read 4TRI keeps v7's 4TRI cell unchanged.
- *Exact cell change for a key v8:* add a split class, e.g. `4TRI_NB` (4TRI answered no-bowl in a blind read whose anchor gate passed) = a/n,
  C43's period cell, grade C on f.101r (period gloss) and grade M wherever the class assignment rests only on a shape read (every f.61 token);
  4TRI (bowl, or not bowl-read) unchanged at v7's c/p/t (f.61 reading cell c/p). Record per token which reader and which call made the
  no-bowl assignment.
- *f.61 meter (bands as meter_v8/meter_v9; baseline = v7 as merged + V8 4PI split + V9 CA null):* no split 12 / 59 / 2 / 26 [null 17 + unread 9];
  split with f.61's 4TRI not bowl-read (each token a/c/n/p) 12 / 53 / 8 / 26; split with H367's reads (L05 14 a/n, five c/p) 12 / 59 / 2 / 26.
  The six f.61 4TRI tokens stay **two-way** whichever sign they are; the split changes letters, not bands. L05 14 should stay at c/p (grade M, a/n
  noted as the alternative) until a third read settles H194's bowl against H367's no-bowl -- a conflict between reads, logged here, not settled
  by the later one.

**Safe sentence:** "On f.101r, 4TRI tokens that blind readers see without a stem-foot bowl pair with a/n in the period gloss (91% under two
independent readers), and the split raises a gloss-free order statistic more than random splits do on two leaves; tokens read with the bowl are
mixed." **Unsafe sentence:** "The bowl reliably separates c/p/t from a/n" or "f.61's L05 14 is a/n."

Postmortem: the proposal's own counts are reproduced exactly; its reading of them is too strong on the bowl side only. One structural flag for
later briefs: `*_align.tsv` status columns are relative to the alignment's own EM key, so "non-conflict rows only" silently selects on the letter
for any class whose cell is under test.

## VERIFY-F61-V10 (29 Sept 2026)

Verifier: PARENT WORKER VERIFY-F61-V10 (account 3, session_01BBihDVXNJZJwuUvhLshzw4), 17:14-17:47 UTC by the container clock. Separate from campaign
runner 13 (session_01MSoJWwZxNPSjQd4hszNdvQ) and from VERIFY-F61-V5..V9. Brief: `.claude/briefs/runs/2026-09-29-verify-f61-v10.md`. Claims under
audit: runner 13's held-leaf evidence for key v7, NOTES.md H325-H359 (plus H360/H361/H365 where they bear on claim 4). Set-level audit: no letter on
f.61 is read, no token graded, no cell or key file touched, no vision call made.

**Files in `verify_v10/`.** `order_v10.py` (parts a-f) and `order_v10g.py` (part g), each committed and pushed before it was run (8829bba9, 8517cc20),
design, controls and gates in their docstrings; results `order_v10_{a,b,d,e,f,g}_result.txt`. The scripts share no scoring code with the runner's
`family/h3xx_*.py` or `tools/partial_key_test.py --cells`: a separate interpolated letter 4-gram model of `tools/data/fr16` (lambdas .55/.25/.12/.06/.02,
every letter of a run scored), an exact Viterbi decoder (the runner's is a width-400 beam scoring from the 4th letter), and fresh seeds. Inputs taken as
committed: the reconciled sign drafts `family/passes/<leaf>/ciphertext_draft.tsv` and key v7 through the key's own loader `build_key_v7.load_key_v7`
(the loaded cells equal the runner's `family/key_v7_cells_h354.tsv`). Independent data check: my run building reproduces the runner's run and sign counts
on every leaf (f.101r 241/2402, f.188r 87/885, f.124r 227/2105, f.97r 203/1809, f.108v 19/286 and 8/285, f.106r rows 1-18 51/622).
Reproduction of the runner's own scripts (`--check`, run 17:3x-17:45 UTC): h325, h328, h330, h341, h342, h344, h359, h361 all OK.

**One contamination found before running (control e).** f.124r and f.97r are not in key_period_v7.tsv's leaf column, but VBAR_A's g/t (v5) was chosen
over v4's s/t partly by a sequence-gain test on a pool that included f.97r and f.124r (H146, 28 Sept; H151's replication 41/50 did not stand). So for
VBAR_A these leaves were not fully held. Control (e) re-runs the held-leaf test with VBAR_A = s/t: the signal survives (below), so this contamination
does not carry it. H132 (same pool) tested swaps of f.61's 14-cell map and changed no v7 cell.

### Numbers beside the runner's

| check | runner 13 | this verifier (own statistic) |
|---|---|---|
| (a) in-sample f.101r gain / null p95 | 0.080 / 0.052, 0/100 | 0.045 / 0.029, 0/100 -- PASS |
| (a) in-sample f.188r | 0.179 / 0.080, 0/100 | 0.096 / 0.043, 0/100 -- PASS |
| held f.124r (bins of 3) | 0.032 / 0.020, 0/100 | **0.0300 / 0.0296, 3/100** -- signal, at the edge |
| held f.124r (bins of 2) | -- | 0.0300 / 0.0280, 1/100 -- signal |
| held f.97r (bins of 3) | 0.057 / 0.037, 0/100 | 0.0295 / 0.0241, 0/100 -- signal |
| held f.97r (bins of 2) | -- | 0.0295 / 0.0284, 5/100 -- signal, at the edge |
| f.108v rec108v | 0.134 / 0.098, 1/100; H344 voided 1/3 | 0.069 / 0.038, 1/100; shuffled 1/10 -> valid |
| f.108v recf108vg | 0.096 / 0.076, 2/100 | 0.073 / 0.046, 0/100 |
| f.108v agreed signs (H353) | 0.079 / 0.071, 5/100 | 0.045 / 0.046, 9/100 -- no signal |
| f.106r rows 1-18 (bins of 3) | 0.028 / 0.049, 31/100 | 0.037 / 0.038, 9/100 -- no signal |
| f.106r rows 1-18 (bins of 2) | -- | 0.037 / 0.036, 2/100 -- signal |
| (b) shuffled-order targets, false 'signal' | H344: 0/3 on most leaves, 1/3 rec108v | 0-2/10 on every leaf (f.124r 2/10, at the gate) -> valid everywhere |
| (d) in-sample power at 227 / 203 runs | -- | f.101r 1.00 / 1.00 (f.188r too short) |
| (d) in-sample power at 51 runs | f.101r 0.80, f.188r 1.00 (H350) | f.101r 0.95, f.188r 1.00 |
| (d) held power at 51 runs | f.124r 0.10, f.97r 0.53 (H351) | f.124r 0.60, f.97r 0.60 |
| (d) in-sample power at 19 / 8 runs | -- | f.101r 0.60 / 0.30; f.188r 0.95 / 0.95 |
| (e) VBAR_A = s/t (v4) held f.124r / f.97r | -- | 0.0302 / 0.0294, 3/100; 0.0270 / 0.0254, 2/100 -- signal survives |
| (f) HASH4 d/q, size-matched, f.124r / f.97r | 1.00 / 1.00 | 1.00 / 0.97 -- supported both |
| (f) C43 a/n | 0.92 / 1.00 | 1.00 / 1.00 -- supported both |
| (f) H24 i/x | 0.51 / 1.00 | 0.78 / 0.82 -- not supported either |
| (f) ZBAR f/s | 0.92 / 0.97 | 1.00 / 0.93 -- f.124r only |
| (f) in-sample positive control, same four classes | f.101r 4/10 classes pass (H355) | f.101r 4/4 (C43, ZBAR at 0.95), f.188r 4/4 |
| (g1) 4TRI + a/n vs 30 freq-drawn widenings, f.124r | 0.0748 vs max 0.0602, beats 1.00 | 0.0472 vs max 0.0401, beats 1.00 -- stands |
| (g1) same, f.101r / f.97r / f.188r | -- | 1.00 stands / 0.93 / **0.50, a/n lowers the gain** |
| (g2) split draft f.124r (no-bowl 4TRI -> C43) | 0.071 (H360), shuffled 0/3 | 0.0484 / p95 0.0227, 0/100; shuffled 1/10 |
| (g2) split draft f.101r | 0.097-0.108 (H365) | 0.0551 / 0.0255, 0/100; shuffled 0/10 |

My gains run lower than the runner's on most leaves (0.3-0.9x; a smoother letter model, all letters scored); what matters is the rank against each leaf's own null,
and there the two instruments agree on the in-sample control, on f.97r, on f.124r (mine at the edge), on the recf108vg draft and on the shuffled
targets; they disagree at the edge on f.108v's agreed-sign draft and on f.106r.

### Verdict (1) gloss-based held-leaf check on f.124r (H325/H328), fragile under bootstrap (H330): **endorse as the runner states it (a fragile lead)**

H325, H328 and H330 reproduce (`--check` OK). 148 agreed gloss letters in v7's cells against a binned-permutation p95 of 143 (7/1000) and a frequency
key of 132 is a pass of 5 letters; the bootstrap (real > binned p95 in 86% of resamples, > frequency key in 90%, against pre-stated bars of 80% and 95%)
makes it fragile, and H331 puts the margin on PHI and C43. I add two limits: the gloss letters are two model passes on a hand they disagree on at 58%
of words (grade M), and the count is order-free, so it is a frequency-and-cell test, not a sequence test -- it cannot tell v7 from any key with the
same cells in a different arrangement of equally common letters beyond what the binned control already holds. H361 (after the window: 156 on the
split draft, binned p95 148, 1/1000) moves in the same direction as the order statistic; it does not remove H330's fragility, which was a property of
the gloss words, not of the sign draft. Standing: **a lead for v7's cells on f.124r, not a confirmation.**

### Verdict (2) gloss-free beam check (H335-H341), voided by its shuffled-order control: **endorse the void; nothing of the beam arm survives as evidence**

H341's own table shows v7 beating the binned p95 on shuffled order on f.124r 4/5, f.101r 3/5 (in-sample), f.106r 2/5 and rec108v 2/5: the absolute
beam score against within-bin permuted keys measures how well cell letters match sign frequencies, and a shuffled draft keeps the frequencies. The
arm is therefore voided as a gate on every leaf, not only on the four where it fired: once it fires on an in-sample leaf with no order, a pass on
f.97r (1/5) or recf108vg (0/5) is a pass of a test that cannot fail for the right reason. The runner's "f.97r and recf108vg survive on their own leaves"
should read "not evidence either". The frequency-key arm was already shown to fail its own in-sample control (H336) and was rightly retired. What
survives is the lesson (a within-bin key permutation is not an order control) and the replacement statistic, which is claim (3).

### Verdict (3) within-run order statistic (H342/H344), power (H346/H350/H351), per class (H345/H349/H355): **endorse in part**

- **Endorsed: order signal for key v7 as a set of cells on f.97r and f.124r**, two leaves v7 was not built from (de Diou's hand, fr.3982), by a
  statistic that passes its in-sample positive control (both instruments), whose shuffled-order null can and does differ from the target (mine: 0-2
  of 10 false signals on every leaf, the gains of shuffled drafts centred on zero), against keys whose cells are permuted within frequency bins, and
  which survives replacing VBAR_A's contaminated g/t by v4's s/t. f.97r clears in both instruments and both bin widths. **f.124r clears in both but
  at the edge in mine** (3/100, gain 0.0300 against p95 0.0296): a real but thin signal on the unsplit draft; claim 4 explains why (the readers' 4TRI
  code mixes two signs on this leaf), and on the split draft it is clear (0.0484 against 0.0227).
- **What it shows:** that v7's cells, taken together, make the sign ORDER of these two leaves read more like 16th-century French than frequency-matched
  rearrangements of the same cells do. It is cryptanalytic, set-level evidence that the family key carries across leaves it was not fitted on.
- **What it does NOT show:** any letter on f.61, any token's value, or that any single cell is right (a set-level gain is compatible with several wrong
  cells); it says nothing about f.61's own hand beyond f.108v below, and it is not a reading of f.124r or f.97r either.
- **f.108v (f.61's hand): fragile, and instrument-dependent.** Both whole drafts show a signal in mine (rec108v 1/100, recf108vg 0/100), the runner's
  H344 voids rec108v at 1/3 while mine passes it (1/10); the agreed-sign draft (H353) passes in the runner's (5/100) and misses in mine (9/100). At 8-19
  runs in-sample power is 0.30-0.60 on f.101r and 0.95 on f.188r: the leaf is below the length where either instrument is reliable. Standing: **a lean,
  not evidence** -- the runner's "thin order signal in f.61's own hand on agreed signs" should drop to that.
- **f.106r (the secretary's hand): untestable at 51 runs -- endorse H351's correction.** My held-leaf power at 51 runs is 0.60 on both f.124r and f.97r
  (runner's 0.10 / 0.53), still under 0.80, so a miss there is not a negative. Note the target itself is instrument-dependent at the edge: 9/100 with
  bins of 3, 2/100 (a pass) with bins of 2, against the runner's 31/100. Neither a negative nor a signal; H350's "negative" stays withdrawn.
- **Per class: endorse HASH4 d/q; endorse C43 a/n more strongly than the runner; H24 and ZBAR not endorsed.** HASH4 d/q is supported on both held leaves
  in both instruments. C43 a/n is supported on both in mine (runner: one), and my in-sample control passes all four tested classes on both in-sample
  leaves. H24 i/x is not supported on either held leaf in mine (0.78, 0.82) while supported in-sample; the runner's f.97r pass (1.00) does not replicate.
  ZBAR's single-leaf support flips leaf between instruments (runner f.97r, mine f.124r). Read under rule 4: H24's cell is a period cell (f.101r/f.188r/
  f.274r); a weak cryptanalytic score on another hand does not outrank it -- recorded as a pointer, not a conflict. The runner's EBR_B note (low scores
  not evidence against l/y) stands. Only classes that pass in both instruments should be quoted: HASH4 and C43.

### Verdict (4) f.124r 4TRI widening by a/n (H356-H358) and H359's bowl forced choice: **endorse, with a specificity control added**

- H358's control replicates in my instrument: on f.124r the a/n widening (0.0472) beats all 30 frequency-drawn 2-letter widenings (max 0.0401). The
  added check: the same widening also beats all 30 on in-sample f.101r (where H365's period gloss pairs the readers' no-bowl 4TRI with a or n, 118 of 130
  -- grade C per pair, not our statistic), sits at 0.93 on f.97r, and on f.188r it LOWERS the gain (0.0852 vs v7 0.0957; beats 0.50). So the a/n widening
  is not a generic win for a/n letters; it helps where the readers' 4TRI is known or seen to hold the no-bowl sign and hurts where the class is clean.
- H359 (read from its files, not re-run; no vision call made here): gate 18/20 on f.176v anchors (Desportes's hand), f.124r 4TRI no-bowl 31 of 46
  answered, C43 20/20 no-bowl. The C43 figure shows "no bowl" is what the reader answers for the a/n sign in this hand; the 15 "bowl" answers show it does
  answer "bowl" here too. Limit, as the runner says: the known-answer gate is in another hand. H360/H365 extend it to 270 and 241 tokens with every
  chunk's gate passing, and f.101r's period letters (bowl-letter agreement 0.83) are the one link that is not our own statistic.
- On the split draft my order test gives a clear pass on f.124r and f.101r with valid shuffled targets (g2). Standing: **the readers' 4TRI code on
  f.124r (and f.101r) conflates the bowl sign (c/p/t) with the no-bowl a/n sign** -- a transcription finding with period support on f.101r.
  `family/PROPOSAL_v8_4tri.md` (a key-build change) is outside this brief; it is the verifier lane's (VO3) call, and this audit's numbers are available
  to it. v7's 4TRI and C43 cells are unchanged here.

### Meter under key v7
Unchanged: **12 / 59 / 2 / 26** (VERIFY-F61-V9's baseline, with CA as null: null 17 + unread 9). No cell moves; this audit is set-level.

### What runner 13 (or its successor) should record
1. NOTES/HYPOTHESES: H341's void covers the binned beam arm on every leaf, f.97r and recf108vg included ("not evidence either").
2. H342/H344: endorsed on f.97r and f.124r by an independent instrument; f.124r's margin on the unsplit draft is thin in the second instrument (3/100).
3. H353: f.108v downgraded to "a lean, instrument-dependent at 8 runs", not "a thin order signal".
4. H349/H355: quote HASH4 d/q and C43 a/n only; H24's f.97r pass and ZBAR's leaf do not replicate.
5. The VBAR_A contamination (H146 pool included f.97r/f.124r) as a named limit, with control (e)'s result that the signal survives VBAR_A = s/t.
6. H358: add the f.188r specificity result (a/n widening lowers the gain on a clean-4TRI leaf).

### Novelty
Not assessed. No reading and no plaintext claim (rule 10).

### Confidence
- **v7's cells as a set carry order on held f.97r:** moderate-high (two instruments, two bin widths, all controls valid).
- **Same on held f.124r:** moderate (both instruments, thin in one on the unsplit draft; clear on the split draft).
- **f.108v, f.106r:** no call (below reliable length).
- **HASH4 d/q, C43 a/n by order on held leaves:** moderate; **H24, ZBAR:** not established.
- **The f.124r 4TRI conflation:** moderate-high (order, shape with gates, and f.101r's period letters agree).

## VERIFY-F61-V12 (29 Sept 2026)

Verifier VERIFY-F61-V12 (account 3, Opus; session_015X77JxuWFPxGK2ZEDo8Rwy; separate from campaign runner 15 and from V5-V11). Claims under
audit: runner 15's f.61 transcription corrections, NOTES.md/HYPOTHESES.md H407-H415 and `scripts/f61_positions_corrections.tsv`. Gates and
decision rules fixed before any reader call: `verify_v12/PREREG.md` (commit 72495510; addendum C4 committed 6087b3ae after the C1-C3 replies were on
file and before any was scored; answer keys held outside the repository until the replies were in, sha256 recorded in PREREG.md and matched).
Every figure regenerates with `--check`: `verify_v12/score.py`, `verify_v12/meter_v12.py`. No reading claim, no grade of a letter, no novelty class
(rule 10); no key file, corrections file or CAMPAIGN.md edited.

**Instrument (independent of the runner's).** My own sign centres placed by eye on the f.61 native region (`verify_v12/v12_positions.tsv`,
`strip.py`), my own tiles at three windows (`cut.py`), my own prompts; the runner's tiles, prompts, position rows for these signs and replies were
not opened. References R1-R15 are in-span f.61 tokens (R1 BETA L11/1, R2 C43 L03/8, ... R15 4PI L11/9; PREREG.md), options N (none) and P
(punctuation / not a cipher sign). Four blind Opus calls: C1 (claims 1, 2-class, 4, L05/1; 18 anchors, 4 repeats, a BETA control and a Part B
panel with BETA removed), C2 (the 26 other out-of-span codes plus L05/1; 8 anchors, 3 repeats), C3 (five count crops from a red-boxed sign to the
first plain word), C4 (the L02 opening mark; R16 = LL L05/16, option O = plain handwriting). Disclosed looks: the whole-region overview, one
labelled W1 contact sheet and the count crops, for placement only.

**Gates.** C1 anchors 18/18, repeats 4/4, BETA control L11/1 -> R1 at W2 and W3: PASS. C2 anchors 8/8, repeats 3/3: PASS. C3 controls L08 from
L08/11 = 3 and L11 from L11/9 = 3 cipher signs, both exact: PASS. C4 anchors 4/5 (gate 4): PASS (the miss is my shifted W3 tile of L08/5, the
reader's own note says no mark sat at the centre).

| claim | this verifier's reads | verdict |
|---|---|---|
| (1) L07/4 is C43, not BETA | R2 (43) at W1/W2/W3; Part B (BETA not allowed) L07/4 -> R2 while L11/1 -> N, not R2 | **endorse** |
| (2) pass A missed a sign at L03/16, PHI | counts from L03/13 = 3 and from L03/8 = 8 cipher signs (pass A 2 and 7); class R6 PHI at 3/3 windows | **endorse** (sign and class) |
| (3) out-of-span QA 26/27, L05/1 unsettled | 24 of 26 non-L05/1 codes confirmed on one read; L11/8 (4STEM) -> R14 CROSS, reader "uncertain, could be a lone 4"; L01/11 (HASH4) -> R15 4PI. L05/1 -> R9 LOOPBAR at 4 of 4 reads (C1 x3, C2 x1) | **in part**: the pre-registered 25/26 bar is missed by one; L05/1 is not unsettled under this instrument -- it is the LOOPBAR sign |
| (4) L04/2 punctuation; L02/2 matches none of 15 references | L04/2 P at 3/3, and the count crop from L04/1 lists 0 cipher signs before "Mais"; L02/2 N at 3/3 ("II": two verticals between bars, EBR has one) | **endorse** both; denominator **99** |

**Per point.**
- *L07/4 and the steering question.* The runner found both span corrections by looking where key v8 missed Tomokiyo's letters, so the positions
  were selected toward the published span. Three things say the corrections were not steered by it: (i) my reader had no access to Tomokiyo and
  returned the same two changes; (ii) the pre-registered control where a change would NOT serve the published letter -- L11/1, Tomokiyo's 'm'
  in S5, read in a panel with BETA removed -- came back N, not the 43 sign, so the reader does not lump beta into 43, and L07/4's 43 call in the
  same panel is a shape call; (iii) the runner declined a change that would have agreed with the published markup (H413 left L05/1 as LOOPSTEM1
  beside Tomokiyo's dash), which a runner steered by the span would not have done. Nothing in this audit suggests either correction is a fit to
  the span.
- *L05/1 (a conflict between reads, logged, rule 4).* Runner reads: H411 LOOPBAR; H413 none / n / LOOPBAR. Mine: LOOPBAR 4/4 at three windows
  and in two calls. Pooled 6 of 8 reads LOOPBAR, and Tomokiyo marks the position with a dash (published markup, consistent with a null). By
  PREREG rule 3 (>= 3 of 4 R9) this verifier endorses **L05/1 = LOOPBAR (null)** as a transcription correction. The tile shows a loop on a stem
  crossed by two bars, the drawing of L03/2 and L03/12.
- *L11/8 and L01/11.* One read each against classes with no in-span token; both land on a neighbouring hash/stem class, which is what a
  forced-choice panel lacking the true class tends to do. Not applied; a second read against a panel that includes an in-hand 4STEM and
  HASH4 (f.108r/f.108v) would settle them. If both held, two more two-way tokens would become null/unread.
- *A slip the runner did not propose (C4).* Pass A starts L02 at PHI, but the line opens with an 'll' mark before it, where L01's cipher run
  continues. C4 reads it as the LL sign (R16, L05/16) at 3 of 3 windows, and the plain-letter anchors 'les' and 'ent' as O. Out of every
  span, so no published letter bears on it. By the C4 rule this is logged as a probable missed LL (a null) at L02 start, **not endorsed for
  merge on this one call**; a second blind read would settle it. It adds one sign: 100.

**Span count and meter (`verify_v12/meter_v12.py`, key v8 as merged, meter_v8 bands).**
- (a) uncorrected: spans 53/55 (p95 0.418); meter 12 / 59 / 2 / 26 of 99.
- (b) runner 15's corrections file: spans **55/55** (permuted mean 0.280, p95 0.436, 0/2000); meter 12 / 60 / 1 / 26 of 99 -- reproduces
  H408/H415 exactly.
- (c) **V12 endorsed = (b) + L05/1 LOOPBAR: spans 55/55 (unchanged, L05/1 sits on Tomokiyo's dash); meter firm 12 / two-way 59 / wider 1 /
  unread-or-null 27 of 99.**
- (d) (c) + the L02 LL, if a second read confirms it: 12 / 59 / 1 / 28 of 100.
The right denominator for the endorsed state is **99**: the meter counts cipher signs, the L03/16 insertion adds one, the L04/2 punctuation
removes one. It becomes 100 only if the L02 opening LL is merged.

**Caveats.** The 55/55 is still in-sample for part of the f.61 reading key (H408's own caveat stands). Each shape call is one reader family
(Opus) on one set of tiles; the two instruments (runner's and mine) agree on (1), (2), (4), and on 24/26 of (3).

**What should merge (for the orchestrator; this verifier edits no key or corrections file).** Keep the three rows of
`scripts/f61_positions_corrections.tsv` (L07/4 relabel C43, L03/16 insert PHI, L04/2 delete); add `L05 1 relabel LOOPBAR` citing H411 + H413
W3 + VERIFY-F61-V12 C1 x3 + C2 (6 of 8 reads). Hold L11/8, L01/11 and the L02 opening LL for one more read each.

**Safe sentence:** "Two blind shape readers with known-answer gates agree that f.61's pass-A transcription had two slips inside Tomokiyo's spans
(L07/4 is the 43 sign; a phi-shaped sign after L03's bracket was missed); with them corrected key v8 matches all 55 published span letters, and a
control position where the change would not serve the published letter did not move." **Unsafe sentence:** "Key v8 is confirmed by an
independent test at 55/55" (in-sample, selected positions) or "every out-of-span sign on f.61 is confirmed".

## VERIFY-F61-V13 (29 Sept 2026)

Verifier VERIFY-F61-V13 (account 3, Opus; separate from campaign runner 16 and from VERIFY-F61-V5..V12). Task: the one more read V12 held for
three f.61 signs, against runner 16's reads (H428 L11/8 CROSS 3/3, H428 L02 opening LL 3/3, H428b/H431 L01/11 4-over-hash 3/3 low confidence)
and its meter H432 (12/58/1/29 of 100). Gates and rules fixed before the reader call: `verify_v13/PREREG.md` (commit f40152f7; answer key held
outside the repository until the reply was in, sha256 99e9abf7... matched). Regenerate: `verify_v13/score.py --check`, `verify_v13/meter_v13.py
--check`. No reading claim, no grade of a letter, no novelty class (rule 10); no key file, corrections file or CAMPAIGN.md edited.

**Instrument (independent of the runner's).** My own centres (`v13_positions.tsv`) on the f.61 native region, the f.108r stitch and the f.108v L03
desk-pack sheet (label strips cut out); my own tiles (`cut.py`, three windows, grey + autocontrast so a tile does not show its leaf by colour);
my own sheets and prompt. Runner 16's tiles, prompts, item files and replies were not opened; from its HYPOTHESES rows I used only that its
4-over-hash exemplar sits on f.108v L03. The panel carried in-hand exemplars of every competing class: 4STEM (f.108r pass108A L02/2), CROSS
(f.61 L07/10), 4PI (f.61 L11/9), both HASH4 forms (looped, f.108r pass108C L05/19; 4-over-hash, f.108v L03/6), LL (f.61 L05/16), plus PHI, C43,
ZHOOK, 4TRI, BETA, VBAR_A; options N (a cipher sign not on the panel) and O (ordinary handwriting). One blind Opus call, 28 + 8 items.

**Gates.** G1 anchors 12/13 (gate 12; the miss: the plain 'Il' of 'Il seroit' -> N, "cursive H-like sign", not O): PASS. G2 in-span controls in
the full panel L07/10 -> CROSS, L11/9 -> 4PI, L05/16 -> LL: PASS. G3 target repeats 3/3 consistent: PASS. G4 anti-steering (panel B, CROSS, LL and
4-over-hash removed): L07/10 and L05/16 -- positions where Tomokiyo's printed letter is served by the class as it stands, so a move would not serve
it -- both N, not moved to 4STEM, PHI or O; the 4-over-hash anchor also N; 4STEM and 4PI anchors correct: PASS.

| held sign | V12 | runner 16 | this verifier (W1/W2/W3, repeat, panel B) | verdict |
|---|---|---|---|---|
| L11/8 (pass A 4STEM) | CROSS, 1 read, "could be a lone 4" | CROSS 3/3 (H428) | N N N, repeat N, B N: "simple 4 with long crossbar, plain stem" -- set apart from both bare-plus CROSS tokens (L07/10, L01/1 -> CROSS) and from the f.108r 4STEM (curved leg) | **reject the relabel to CROSS** (not reproduced; PREREG rule 1 outcome "hold": 4STEM stands as coded, M) |
| L01/11 (pass A HASH4) | 4PI, 1 read | N 3/3 vs looped hash (H428b); 4-over-hash 3/3, low (H431) | N N N, repeat N, B N: "struck-through hash cluster, cancelled sign", with the 4-over-hash on the panel and its two anchors read right | **in part**: no change, as runner 16 says (HASH4 stands as coded, grade M; V12's 4PI not reproduced), but its 4-over-hash identification is not reproduced |
| L02 opening mark | LL 3/3 (C4), held | LL 3/3 (H428) | LL LL LL, repeat LL; B (LL off panel) N, not O | **in part**: the shape call reproduces on a third instrument, but PREREG rule 3's endorsement condition (plain 'Il' foil -> O) is unmet (it went N); not endorsed for merge |

**Rule 4 conflicts, logged.** L11/8: pooled reads CROSS 4 (V12 1, runner 3) vs N 4 (this verifier, three windows + repeat, with CROSS
exemplars on the panel and read correctly). Two instruments that each pass their own gates disagree; the more frequent value does not settle it,
and the sign is held at M in its pass-A class. L01/11: 4PI 1, 4-over-hash 3 (low), N 6 (runner's H428b 3, mine 3); nothing merges, and every
instrument agrees it is not a clean exemplar of any panel sign (overwritten or cancelled, the runner's own H431 note and my reader's).

**L02 opening.** Three instruments now read the LL sign there, 9 windows of 9, and with LL withdrawn my reader answered N (a cipher sign), not O.
What keeps it from merging under my own rule is the foil: I pre-registered that the reader must call a plain 'Il' in this hand O, and it called it
N instead (it did not call it LL, so the disqualifying outcome did not occur either). A foil the reader recognises as handwriting -- a clear 'll'
inside a word in this hand, read as O -- together with the target still at LL would settle it; or the orchestrator may weigh the three concordant
instruments against this one unmet condition, which this verifier leaves to it.

**Meter (`verify_v13/meter_v13.py`, meter_v12's own functions, key v8, meter_v8 bands).**
- Endorsed by this verifier = V12's endorsed state (c), nothing added: spans 55/55 (permuted mean 0.280, p95 0.436, 0/2000); **meter firm 12 /
  two-way 59 / wider 1 / unread-or-null 27 of 99**. Denominator **99**.
- For comparison, runner 16's H432 state ((c) + L11/8 CROSS + L02 LL): 12 / 58 / 1 / 29 of 100, spans 55/55 -- reproduces H432 exactly; not endorsed.

**What should merge into `scripts/f61_positions_corrections.tsv` (F61-FAMILY-14 does the merge).** From V13: no row. Unchanged from V12: the
three existing rows plus `L05 1 relabel LOOPBAR` (H411 + H413 W3 + V12 C1 x3 + C2). Do not add `L11 8 relabel CROSS` (conflict, held M) or an L01/11
row. `L02 0 insert LL` stays held pending the foil condition above.

**Safe sentence:** "A third blind reader, with in-hand exemplars of every competing class and a passing anti-steering control, reproduced the LL
sign at the opening of f.61 L02 but not the CROSS reading of L11/8 or the 4-over-hash reading of L01/11; the endorsed meter stays 12/59/1/27 of 99."
**Unsafe sentence:** "Runner 16's three reads are confirmed" or "L11/8 is a 4STEM" (the pass-A class stands only because nothing displaced it).

## VERIFY-F61-LL ruling on A2-F61 (2 Oct 2026, 22:09-22:10 UTC by date -u, verifier VERIFY-F61-LL, account 2, separate from the solver)

**Ruling: ENDORSE `L02 0 insert LL` (a null, grade S: an instrument reading with a passing control and a met foil condition; no letter, no H/C).
Merge allowed; not merged by this verifier.**

Checked: (1) order -- PREREG.md and the deterministic `build.py` (seed 20261002) are in eb9091fe at 21:53:15, reply.tsv and key.json in 53c2d53c at
21:54:42; the sha was not itself in the prereg commit, but re-running `build.py` here regenerates a key identical to the committed key.json (sha
62bdcfbd...), so the answer key was fixed before the reply. (2) `score.py --check`: OK; gates G1 9/9, G2 PASS, G3 PASS; target LL LL LL, foil O O O,
reproduced. (3) Sheets regenerated and read by eye.
Leak question (rule 3): the foil's W1/W2/W3 tiles show the whole word "ella" with its flanking e and a, and the reader's notes name the word, so
O was the likely answer from context alone. That weakens the foil as a test of stroke shape, but it is not a non-test: the foil was free to read
LL or N on every window, and V13's own condition asked for exactly this ("a clear 'll' inside a word ... read as O"). What tips it is shape,
which I checked on the tiles directly: the in-word 'll' of "della" is two plain straight stems with no heads, while the L02 mark (#424/#723/#588)
has the hooked, looped heads of the LL reference exemplar L05/16 (#881) -- this hand's ordinary 'll' is not drawn like the LL sign. The target's
context (line start, after the stamp's edge, followed by PHI) carries no word for the reader to complete either.
Chance: the three windows are overlapping crops of one mark, not independent trials, so "3/3 vs 3/3" is closer to one read each than to a
p-value; the weight comes from four instruments concordant at 12 windows of 12 (V12 C4, H428, V13, A2-F61), the anchors at 9/9 and the repeats.
Residual caveat, carried: A_PLAIN_IL (the capital 'Il') still reads N, so the reader's O class is shown only for lower-case in-word script.
Verdict: endorsed; next: F61-FAMILY merges `L02 0 insert LL` into `scripts/f61_positions_corrections.tsv` and re-runs the meter (expected 12 / 59 /
1 / 28 of 100, spans 55/55), ~$1. Novelty not touched (no reading changes).

Desenclos check, 4 Oct 2026 (DESENCLOS-PREMISE, account 3): no hit. Searched 17 open full texts of the 36 items in sources/desenclos/2026-10-04/bibliography.tsv (HAL PDFs, DSpace Tartu HistoCrypt 2024/2025 PDFs, OpenEdition HTML; built from HAL, theses.fr, OpenAlex, Semantic Scholar, CrossRef, Google Books) for this item's shelfmark, sender/recipient, place and date (terms.tsv, search-log.tsv, search.py); none names this item, its key or its plaintext. Not read: her 2014 thesis (theses.fr: not online) and 2017/2021 cryptography chapters (not open; JSTOR-QUEUE rows of 4 Oct 2026).
