# PREREG test 1 -- es132-vargas-mexia-1578 (RUN1-ES132, account 1, 4 Oct 2026, written ~00:55 UTC before any f.89-91 / f.119r decode)

Brief: `.claude/briefs/runs/2026-10-04-acct1-run1-wave1.md` job RUN1-ES132. Key: `key.tsv` (Cp.30, unchanged from test 0).

## Scope check (before any vision call)
`cabinet_noir_map.tsv` rows 89 and 119: `cn_read = no` for both (f.89 "not in CN folder list", f.119 "not in CN folder list").
Neither page is dropped.

## Where things are (located by this worker from 1000 px Gallica canvases, 4 Oct 2026)
- The f.89 letter runs f.89r (canvas 86 right), f.89v + f.90r (canvas 87), f.90v (canvas 88 left), f.91r (canvas 88 right,
  ends "De Madrid a xix de Septe. MDLXXVIII", signed). Opening (clear): "A dos del presente se recibieron juntas cinco cartas
  vras de 17, 19, 20, 23, 24 de Agosto ...".
- Teulet vol.5 pp.161-162 (Simancas B.47 n.8, 19 Sept 1578, "Déchiffr. officiel") prints ONE paragraph, now in
  `teulet_19sep1578.txt` ("De consideracion es lo que passastes con el embaxador de Escocia ... al recaudo que soleis").
  By eye it is the f.90v paragraph that begins about line 11 with "... lo que pa-sa-tes con el [Bul] de [Dul] y ..." -- the
  same code pair [Bul]/[Dul] = "embaxador"/"Escocia" as the test 0 known answer. Its exact line extent is set from the crops.
- f.119r = canvas 116 right; f.120r = canvas 117 right. Neither is printed by Teulet (test 0).

## Units and order (Usage 6, priced per pass)
Page A = f.90v (carries the printed known answer + an unprinted paragraph above it). Page B = f.119r (unprinted).
Each page: 2 blind Sonnet passes (crop paths only, never the key or Teulet) + 1 reconciliation by this worker = 3 units at
~USD 1.5. Page A first. Page B only if starting it stays under 80% of cap (USD 9.6) and box (02:15 UTC). f.89r, f.89v, f.90r,
f.91r, f.120r are named next, not attempted, if pacing stops.

## (a) Printed known answer (f.90v Teulet paragraph)
Statistic S_a: character-level alignment score = fraction of key-decoded letters (code tokens excluded from both sides) that
fall inside difflib matching blocks (autojunk off) of the decode vs the reference text, after normalising BOTH sides to one
convention (lower case, accents/cedilla dropped, v->u, j->i, doubled letters collapsed, non-letters dropped; rule 3 PX-BRODEC
lesson; Teulet's OCR "Yos" for "Vos" and "6" for "o" left as printed). Also reported: test 0's per-token agreement.
Reference: the whole `teulet_19sep1578.txt` paragraph, scored against the decode of the cipher lines that carry it.
Nulls (both computed before the target number is looked at, same script run):
- N1: 200 key shuffles (letter values permuted among numeric bases, seed 1578, as test 0), same ciphertext, same reference.
- N2: the true-key decode scored against wrong references: every window of other Teulet vol.5 Spanish text (es16 corpus,
  which excludes both known-answer letters) of the same normalised length as the reference, stepped by 50 letters
  (at least 200 windows).
Gate (a): S_a on EACH blind pass > max(p99(N1), p99(N2)). Pre-registered also: S_a >= 0.80 on at least one blind pass, the
test 0 known-answer bar. Orthogonality: N1 changes the decoded letters, N2 changes the reference text; S_a depends on both,
so each null can move it (not orthogonal by construction).

## (b) Unprinted paragraphs (f.90v rest; f.119r if done)
Word-cover is at ceiling (test 0: null mean 0.92), so it is not used as a gate.
Judge: es16 = `es16/teulet5_es_fold{1..5}.txt.gz` (Teulet vol.5 Spanish paragraphs, 1560s-80s embassy letters, the two
known-answer letters cut out; `es16/build_es16.py`). Model: tools/judge_plaintext.py NgramModel (4-gram, as the shared judge).
Pre-run calibration (before any target score): leave-one-file-out false-negative rate at N=300 and N=600 with per-fold
spread (rule 3 es17c lesson); 5 folds of one source volume, so a wide spread means "reliability unknown".
Statistic S_b: mean log10 4-gram score of the target's key-decoded letters (codes dropped; candidate files as test 0).
Nulls for S_b, computed first:
- ARM-C1 check: Cp.30 decode of the SHUFFLED target (token order permuted, 200 shuffles, seed 1578) through the same model.
  If the standard judge (score > null_p99 AND > real_p05) PASSes the median shuffled-target decode, the es16 judge is VOID as
  a gate for this family at this N and (b) is reported as a non-test.
- N1b: 200 key shuffles of the target decode (as N1).
Gate (b) (primary): S_b > p99 of BOTH the shuffled-target-order decodes and the shuffled-key decodes. Secondary, reported
not gated: the standard judge line (real_p05) for the target and for the known-answer decode of page A, so the reader sees
how far real Cp.30-decoded text with dropped codes and transcription error sits from clean corpus prose.
Orthogonality: token-order shuffle changes 4-gram contexts across syllable joins (the statistic is order-dependent), key
shuffle changes letters; neither is identical to the target by construction. Caveat stated now: within-token letters
(syllable + vowel + marks) are kept by the order shuffle, so the shuffled-target null is expected to sit closer to the
target than the key null; that is why it is the stricter one.
Calibration on a known answer: the page A known-answer decode is scored the same way; if it does NOT beat both (b) nulls,
gate (b) has no demonstrated power at this length and a target miss is a non-test, not a negative.

## Grading (rule 4)
Key-decoded tokens M (C where they agree with Teulet's printed decipherment); codes >= 38 / cursive word codes unread (U)
unless a value is attested in this folder (test 0 C-grade: [Bul] embaxador, [Dul] Escocia, [Val] hasta) or in cabinet-noir's
complements (cited, CC BY 4.0). No H.
