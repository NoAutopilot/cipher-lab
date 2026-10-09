# PREREG-MQS-ALIAS (LANE MQS-2, account 4) -- written before any control is scored (NOT pushed before: see Deviation 1)

Written 9 Oct 2026 (07:1x UTC by date -u) by the MQS-ALIAS worker. Brief: `.claude/briefs/runs/2026-10-09-ytbiz-mqs-next-alias.md`
(research/MARY-STUART-TALK-2026-10-09.tsv row M22; Lasry, Biermann and Tomokiyo 2023, Cryptologia 47:2, p.131 n.70,
p.183 n.305-306, pp.189-190; Browne 1840 via ciphers/sp54-maclean-1745/browne_feigned_names.tsv).

## What is built (rendering only)

1. A shared alias table schema, `alias.tsv`: `alias  meaning  grade  first_use  last_use  evidence  source`. The loader
   also reads `feigned_name` as `alias` (so browne_feigned_names.tsv loads unchanged); an alias cell may list variants
   ("Watson, or Walker"). The rendered grade is the identification's own grade: the last standalone H/C/S/M/I/U letter
   in the grade cell ("H-print, alignment I" -> I).
2. `decode_key.py TARGET --aliases ALIAS.tsv [--alias-out F] [--alias-tsv F]`: renders the job's reading with
   `alias [= meaning, G]` after each alias occurrence, and lists hits (line, alias, meaning, grade, token grades).
   Never writes the committed reading or tokens file; token grades are unchanged (the alias grade is shown beside them,
   not merged). `--alias-text FILE` does the same on any plain text (no target decode).
3. `decode_key.py TARGET --alias-scan LANG` (and `--alias-text FILE --alias-scan LANG`): flags announcement phrases
   in the decoded text ("qui s'apellera entre nous X", "whom we shall call X", ...) from a cue file
   `tools/data/alias_cues_<lang>.tsv` (fr, en, it, es), written to disk at 07:12 UTC, before any score; reports the cue, the
   following name span and the preceding referent span. A flag is a candidate for a person, never an alias.tsv row.
   F125 fixture: the paper's own sentence is not on disk; the offline test uses a constructed French sentence of the
   same shape ("... qui s'apellera entre nous la Tour ..."), stated as constructed, not quoted.

## Matching rule (fixed before scoring)

Letters folded as fold_word (case, accents, j->i, v->u). Where the text has word boundaries an alias matches only as
whole words; in an unbounded letter run (concat/spaced styles without word_sep) an alias of fewer than 5 letters is
not matched (`--alias-min-len`, default 5).

## Control A -- `--aliases` (design: English 1745-era prose, the Browne table, decoded-text form)

- Material: tools/data/en18 (era-matched English letters), 20 windows of 1,500 words, seeds 1-20, lower-cased,
  punctuation stripped (a decoded cipher's form). Table: the 24 Browne rows (27 variant strings).
- Known answer: 10 alias occurrences planted per window (random row, random word slot). Statistic: recall (planted
  occurrences annotated with the right meaning) and false hits on the unplanted words.
- Null 1 (unplanted): the same 20 windows, nothing planted: false hits per 10k words. Can differ from the known
  answer: planting adds true hits, so hits/recall can only match if the tool ignores alias strings.
- Null 2 (permuted): the same slots planted with each alias's letters shuffled (same length, seed fixed): hits on the
  planted slots. Can differ: the statistic is string identity, which a letter permutation breaks.
- Expected: recall >= 0.98; null 2 <= 0.02; null 1 false hits non-zero because several Browne aliases are ordinary
  words or common surnames once case is lost (morris, morton, lister, jennings, barclay, watson...) -- registered
  expectation 2-20 per 10k words.
- Gate (PASS = all three): recall >= 0.95; null-2 hit rate <= 0.05; null-1 false hits <= 10 per 10k words.
  A miss ships `--aliases` weak with both numbers.

## Control B -- `--alias-scan fr` (design: French 16th-c. prose, decoded-text form)

- Material: tools/data/fr16 (Catherine de Medicis I-II, Marguerite), 20 windows of 1,500 words, seeds 1-20,
  lower-cased, punctuation except the apostrophe stripped.
- Known answer: 3 announcement sentences planted per window from two phrasing lists written here, before scoring:
  - in-list (forms the cue file carries): "qui s'apellera entre nous X", "que nous appellerons X",
    "lequel nous nommerons X", "sous le nom de X", "qui sera appelle X";
  - out-of-list (deliberately NOT in the cue file, to measure generalisation): "que j'ay baptise X",
    "a qui nous donnerons le nom de X", "dorenavant dit X", "que vous entendrez par X".
  X drawn from: la tour, le banquier, monsieur de la riviere, le jardinier, la poste.
  Statistic: recall per list (a planted sentence whose cue and X span are both reported).
- Null 1 (unplanted): the 20 windows as they are: flags per 10k words (all counted as false; the real corpus may
  hold genuine "sous le nom de" uses, which is the cost a reader pays).
- Null 2 (permuted): the in-list plants with the cue's words in reversed order (e.g. "nous entre s'apellera qui X"):
  recall. Can differ: the cue match is an ordered word sequence, which reversal breaks.
- Expected: in-list recall >= 0.98 (circular by construction: the same author wrote the cue file and the plants);
  out-of-list recall <= 0.30; null 2 <= 0.02; null 1 1-15 per 10k words.
- Gate (PASS = all three): in-list recall >= 0.95; null-2 <= 0.05; null-1 <= 15 per 10k words. Because the in-list
  known answer is circular and no real announcement from a decoded cipher is on disk, `--alias-scan` ships at most
  `weak` whatever the gate says; out-of-list recall is reported, not gated.

## Headroom (rule 3)

Neither statistic is a solver gain, so the near-ceiling/more-restarts check does not apply; both tools are
deterministic (no restarts). Nothing is run on a target: no status, key, reading or AUDIT.md change; no host.

## Results (appended after scoring, 9 Oct 2026 07:1x UTC by date -u; tools/tests/MQS-ALIAS-controls.tsv)

| control | known answer | null 1 (unplanted) | null 2 (permuted) | gate |
|---|---|---|---|---|
| A --aliases (en18, Browne) | recall 200/200 = 1.000 | 4.0 false hits per 10k words (12 in 30,000: 'mr adams' 10 = John Adams in Madison/Jefferson prose, 'morris' 2) | 0/200 | PASS |
| B --alias-scan fr (fr16) | in-list 60/60 = 1.000; out-of-list 0/60 (reported) | 0.33 per 10k (1, 'sous le nom de') | reversed cue 0/60 | PASS |

Shelf: `--aliases` controlled-only (recall is string identity, near-circular; the false-hit rate is what the control
measures, and it shows a real alias that is also a real person's name in the same prose -- 'Mr Adams' -- is rendered
wrongly unless the reader checks the hit table). `--alias-scan` weak as pre-registered (circular in-list known answer,
out-of-list recall 0: it finds only phrasings its cue file carries). No deviation from the gates; nothing run on a target.

## Deviation 1 (pre-registration not pushed before scoring)

This file was written to disk at 07:10 UTC and the cue files at 07:12 UTC (file times), and the controls were scored at
07:14 UTC; but the two `tools/room.py "<role>" "<text>" --push <paths>` calls at 07:10 and 07:12 committed only their
ROOM.md line (the line form ignores the path list; the paths need `tools/room.py --push <paths>` on its own), so
nothing here was in git until the push carrying the results. Commits 18c3a52c and b7e887a1 hold only ROOM lines. The
gates and expectations above the Results section are as written before scoring; the only edit to them after 07:10 was
the 07:12 note about the cue files' timing (now corrected to this paragraph). The rule-3 order -- pushed before scored
-- was therefore not met and cannot be shown from git; it rests on this worker's account. Nothing is run on a target
from either option.
