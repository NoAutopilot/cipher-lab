# PREREG MQS-IA-MARKERS (9 Oct 2026, written 07:15 UTC by date -u, before any fetch or score)

Job: `.claude/briefs/runs/2026-10-09-ytbiz-mqs-next-ia-markers.md` (research/MARY-STUART-TALK-2026-10-09.tsv row M04).
Credit: Lasry, Biermann and Tomokiyo 2023 (Cryptologia 47:2), p.108 n.38: Labanoff 1844 printed BnF fr.3158 f.57 in
vol. 6 pp.45-49 with the cipher passages shown as ellipses. `ia_numeral_runs.py` sees numeral runs only, so an edition
that printed dots or a bracketed note where cipher stood is invisible to it.

## Option

`ia_numeral_runs.py --markers` (default numeral behaviour unchanged when the flag is absent). Per OCR line it counts
**gap markers**:
- an *ellipsis*: a run of three or more dots, optionally space-separated (`...`, `. . .`, `....`), or `…`;
  NOT counted when the dot run is a leader followed only by a page reference to the end of the line
  (`.......... 45`, `. . . . xii`), the table-of-contents shape;
- a *cipher note*: a bracketed or parenthesised note containing chiffr / cipher / cypher / ziffer / cifra
  (`[en chiffre]`, `(en chiffres)`, `[in cipher]`, `(Chiffre)`), weighted 3 (one note is a flag on its own).

Marked lines fewer than `--marker-gap 6` lines apart form a cluster; cluster score = weighted marker count; a cluster
is **flagged** when score >= `--min-markers 3`. Output: same TSV columns plus `kind` (numeral|marker).

Must catch (offline test): a letter with three ellipses within a few lines; a single `[en chiffre]` note.
Must NOT flag (offline test): a table of contents of dot leaders ending in page numbers; one isolated editorial
ellipsis; numeral-only text when `--markers` is absent (existing output byte-identical).

## Known answer and gates (fixed now)

Known answer: Labanoff, *Lettres, instructions et mémoires de Marie Stuart*, vol. 6 (1844), pp.45-49, IA djvu text
(identifier found by one archive.org advancedsearch call; up to two candidate ids fetched, 1.5 s apart). The span is
located by the printed page numbers in the OCR (page-header lines `45`..`49`, or `\f` page breaks counted from a
header anchor), recorded before scoring; if pp.45-49 cannot be located in the OCR at all, the test is a non-test
(logged so), not a FAIL.

- **G1 (catch):** at least one flagged cluster overlaps the pp.45-49 span.
- **G2 (rank):** that cluster ranks in the top 10 of all flagged clusters in vol. 6 by score.
- **G3 (null):** its score exceeds the 95th percentile of the volume-wide *maximum* cluster score over 200
  line-order permutations of vol. 6 (seeded 1-200). Why this null can fail differently: the cluster score depends on
  markers sitting close together in line order; permuting line order keeps every marker but scatters them, so it can
  drive the max down (a genuine local concentration) or leave it high (a volume where markers are everywhere, e.g.
  dense editorial ellipses) -- it is not identical to the target by construction.

PASS = G1 and G2 and G3. Expected: G1 likely (the paper says ellipses); G2/G3 uncertain, since 1840s editions use
ellipses for editorial omission too. Ceiling check: not a recovery rate, no headroom question; noted.

Descriptive only (no gate): flagged clusters per 1,000 OCR lines on the djvu texts already on disk in this repo
(ciphers/*/…_djvu.txt, sources/herzog-1929), as a false-flag load figure for a sweep.

Outcome: PASS -> shelf `controlled-only` (one known answer); FAIL -> shelf `weak` with both numbers, option kept, not
re-briefed (brief). No target status, key, reading or AUDIT.md change either way.

Hosts: archive.org only, at most 4 requests, 1.5 s apart, one at a time.

## Results (appended after scoring, 9 Oct 2026; nothing above this line changed)

Hosts: archive.org 3 requests (1 advancedsearch, 2 `_djvu.txt`), 1.5-2 s apart, no errors. Cache: `sources/ia-fulltext/`
(gitignored). Span located by printed page headers ("DE MARIE STUART. 45" ... "49"): uoft scan lines ~1715-1990,
second scan ~1735-1995. The letter is Marie Stuart to Mauvissière, Wingfield 30 Oct 1584, "Ms. Béthune no 8678 fol. 57".

| scan | lines | marked lines | flagged clusters | KA (pp.45-49) score | vol max real | null max p95 (200 perms) | G1 | G2 | G3 |
|---|---|---|---|---|---|---|---|---|---|
| lettresinstructi06maryuoft | 19,954 | 6 | 0 | 0 | 1 | 1 | FAIL | FAIL | FAIL |
| lettresinstructi06mary | 20,245 | 7 | 1 | 0 | 3 | 3 | FAIL | FAIL | FAIL |

**Verdict: FAIL (G1).** Why: in both OCR texts the printed dotted lines are gone -- the text runs "sir Ralf Sadler'" straight
into "Quoy qu'il en soit" (p.46) with no dot characters at all; the djvu OCR does not carry rows of printed points. The only
OCR-visible trace is the editor's unbracketed footnote "Les lignes marquées par des points sont en chiffres dans l'original,
et on n'en connaît point la clef", which the pre-registered marker set (bracketed notes only) does not match. The second
scan's one flagged cluster is a source note "(Déchiffrement original. -- State paper office ...)" -- a decipherment
pointer, not a gap.

Descriptive (no gate): on-disk djvu texts, 13 flagged clusters in 333,832 OCR lines (0.04 per 1,000 lines); not inspected.
Post-hoc descriptive only, NOT a test: unbracketed `en chiffres?` occurs on 16 lines in each vol. 6 scan. A footnote-phrase
detector ("sont en chiffres dans l'original", "in cipher in the original") would need its own pre-registration and a
known answer other than this volume, since this one was used to find it.

Shelf: `--markers` `weak` (rule: FAIL ships weak with both numbers, option kept, not re-briefed).
