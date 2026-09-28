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

