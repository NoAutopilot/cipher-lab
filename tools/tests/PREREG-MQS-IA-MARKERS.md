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
