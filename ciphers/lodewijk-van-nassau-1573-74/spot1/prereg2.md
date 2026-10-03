# spot1 pre-registration 2 (A2P4-LVN98, LANE-A2PUSH4 account 2, 3 Oct 2026, written and committed before any score)

Same span, same input, same alignment instrument as spot1/prereg.md (A2P4-LVN97, 7d636fe2): spot1/ciphertext_spot1.tsv as
reconciled, key_full.tsv v3 as committed, Groen IV CDXLIV p.222 paragraph ("werden E.G. nhumehr ..." + "Wir seint resolvirt
alsbalt ... bringen."). No re-transcription, no key change, no vision call.

What changes, and why (rule 3, PX-BRODEC paragraph): LVN97's gate A FAILed (0.171 vs 0.50) in part because the two renderings
follow different spelling conventions. Disclosed: the rule list below was written after LVN97's diagnostic (E.G./e.f.g.,
balt/halt, darzu/dazu) and after seeing spot1/units.tsv's decoded strings; it is a fixed general list of Early New High German /
Dutch orthographic variant classes, not a per-word fit, and it is applied identically to the target and to every control.

## Normalisation N2 (applied to BOTH sides: each decoded cipher unit, and every reference word of target and controls)
1. Groen's editorial apparatus removed ("Ga naar margenoot+ [#n]", "Ga naar voetnoot..."); bracketed conjectures keep their letters.
2. Abbreviations expanded before splitting into words: "E.G." / "E.f.G." / "E.F.G." -> "euer gnaden" (two words); "S.G." -> "seine
   gnaden"; "I.G." -> "ihre gnaden"; "H." standing alone -> "herr". (None occur inside cipher units; applied to both sides anyway.)
3. One case: lowercase.
4. ä ö ü -> a o u; ß -> ss.
5. Variant classes, applied in this order, each to the whole string:
   dt -> t; th -> t; tz -> z; ph -> f; ck -> k; c -> k; qu -> ku; v -> u; w -> u; j -> i; y -> i; ie -> i; ae -> a; oe -> o; ue -> u;
   h after a vowel and not before a vowel -> removed (Dehnungs-h: persohn -> person, nhumehr -> nhumer); final e -> removed.
6. Drop everything not a-z or '?' (punctuation, digits, Roman numerals as characters); collapse doubled letters.
Key word-values that are whole words (e.g. 339 'harquebouziers', 136 'uingt') pass through N2 like any other string; NULL dropped,
'?' kept and matches nothing (as prereg.md).

## Metric (cipher units only, LVN97's B-type)
- Eligible cipher unit: a decoded unit containing at least one numeric code that decodes to a letter, with >= 3 known letters
  after N2.
- sim, the monotone DP (one reference word or 2-3 consecutive concatenated, sim >= 0.75, free skips, maximise matches, ties more
  reference words) exactly as prereg.md. No clear-word step and no F set: A is not computed.
- B2 = matched eligible cipher units / eligible cipher units.

## Controls (same decoded run, same N2, same DP)
- (s) 200 word-shuffles of the N2-normalised target paragraph (seeds 1-200).
- (d) d1-d3 exactly as prereg.md (three other Groen IV CDXLIV German paragraphs, first N words, N = target word count after N2).
Both can differ from the target on B2 (order for s, content for d).

## Gate (PASS needs all three)
1. B2_target >= 0.50 (half the eligible cipher units reproduce Groen's words in order; the absolute bar LVN97 set for A).
2. B2_target >= p95(B2 over s) + 0.15.
3. B2_target >= max(B2 over d1-d3) + 0.15.
PASS: the interior readings at the garbled spots are reported at the key's grades (C/H per token, I where a letter is repaired).
FAIL: nothing is claimed for the interior beyond the transcription.

## Third look (rule 3, third-attempt clause)
This is the third look at this span with this instrument (AX-5797's two-pass spot read; LVN97's in-order gate; this). A FAIL here
closes the in-order alignment method for spot 1: the step is logged [retired] (instrument: in-order Groen alignment, spot1
align scripts), "untested-by-this-tool at this transcription", not refuted, and the next step must be new material (another
witness of the paragraph: a contemporary copy, a decipherment, the reply) or a different instrument -- not a further tuning of N2,
the threshold or the metric.
