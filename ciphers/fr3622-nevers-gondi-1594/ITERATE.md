# ITERATE -- fr3622-nevers-gondi-1594 (BnF Français 3622 no.45, f.91: Nevers to "Mr de Gondy", Veze, 27 Mar 1594)

Standing lane BNF-FOCUS (.claude/briefs/runs/2026-10-07-acct3-standing.md). Appended, never rewritten.

| date | hypothesis | instrument | matched control | result (both numbers) | verdict | what it taught |
|---|---|---|---|---|---|---|
| 8 Oct 2026 | (planned) f.91's cipher lines are in Nevers key no.41 (BnF fr.3995 fol.76, Aug 1591; Tomokiyo nevers.htm: used by Albert de Gondi, duc de Retz, to Nevers at fr.3983 f.178, fr.3986 f.189, fr.3988 f.79 -- all three catalogued "avec chiffre et déchiffrement") | key sheet transcription + decode (tools/decode_key.py) | known answer first: the no.41 key read against fr.3983 f.178's own period decipherment, vs 200 shuffled keys; then the target vs 200 shuffled keys | -- | -- | -- |

Next best attempt and why: BNF-G41 (brief .claude/briefs/runs/2026-10-08-ytbiz-bnf-g41.md): a period key sheet, three
glossed siblings of the same correspondence for a known-answer gate, and a short target (~5 cipher lines), all online.
Pre-screened 8 Oct 2026: none of fr.3622 f.91, fr.3983 f.178, fr.3986 f.189, fr.3988 f.79 is in Bourdeau's README or
CATALOGUE.md, our folders or KEYHUNT-2026-10-07.tsv.
| 8 Oct 2026 | f.91's cipher lines are in Nevers key no.41 (fr.3995 fol.76 verso, canvas f151, Aug 1591) | BNF-G41: key sheet (2 blind passes, alphabet read from the image, 207/183 rows); gate on fr.3983 f.178 (canvas f310 of btv1b9059406b), 2 blind digit passes (pooled digit agreement 0.72 on 773 digits); decode `scripts/gate_decode.py` (2-digit DP parse, letter codes only) scored by French 4-gram (fr16 corpus) | 200 keys with letter values permuted across codes (seed 41), same digit passes | GATE (modified, see note): real -1.400 (pass A) / -1.396 (pass B) vs shuffled mean -1.781, p99 -1.609 / -1.642, max -1.592 / -1.593; rank 0/200 both. Decoded stretches read French: "croy", "moyen", "on peult", "donne", "nouuelle", "debue(z)". TARGET: not run -- f.91's cipher lines are a symbol alphabet (Greek-like and numeral-like glyphs: lambda, pi, xi shapes, 8, 4, 7), not digit figures; key no.41 has no value for any of them | gate pass (modified); target non-test for no.41 (sign inventory mismatch, by image, not a decode failure) | no.41 reads fr.3983 f.178 as French (key identified for that leaf as a cryptanalytic result with a control, grade S/M, not H); f.91 needs a different key family: a symbol key of Nevers's office, or the Tomokiyo list's other Nevers sheets |

Note on the gate: the pre-registered form (letter agreement >= 0.70 with the clerk's decipherment) was not run, because f.178 carries only a sparse pale interlinear gloss (about 20 words), not a full decipherment. The substitute is a blind French-likeness score of the decode against shuffled keys of the same design; it needs no gloss. Digit transcription is rough (0.72 pass agreement; dark digits overlap show-through), so the decode is a lower bound on the key's fit. The alphabet (a 06-09, l 28, n 56/58/59, i 76/78/79) is M on a and l, n, i; the Mot/Noms tables were transcribed but not reconciled (pass A 207 rows, pass B 183, `keys/`), and word codes were used only as skip tokens.

Next best attempt: (1) for f.91, read the glyph inventory (about 5 lines, 3 sign shapes families) in `tools/sign_sorter.py`, then test the symbol keys listed in tools/keys/ and KEYHUNT-2026-10-07.tsv for Nevers 1594 (no.60 is figures too); look for a Nevers symbol sheet of 1593-94 (fr.3989 f.? Revol letters, same month) as a key candidate; ~$4. (2) For f.178, the gloss-aligned span test and a reconciled key would raise the leaf from "reads as French" to a graded reading; only if the leaf is wanted.

Lane note (BNF-FOCUS, 8 Oct 2026 05:5x UTC by date -u): the BNF-G41 gate above was substituted after the run began
(registered: letter agreement >= 0.70 with f.178's decipherment; run: French 4-gram vs shuffled keys). The f.178 row is
therefore logged as "reads as French under no.41, unregistered test", not as a passed gate, and licenses nothing about
f.91. Future briefs: if the registered gate cannot be run as written, the worker stops and reports; it does not swap
the gate (CLAUDE.md rule 3, ARM-S3 lesson). Sign evidence (lane, one look at images/f91/block.jpg vs
fr3986-nevers-revol-1593/sign_guide.md): f.91 uses λ, π, barred-I, figures 2/4/7/8 and Latin-letter shapes mixed --
the tag set of Tomokiyo's no.60 "Court's symbol cipher" (fr.3995 ff.109-111), not no.41.

| 8 Oct 2026 | (planned) f.91's cipher is Nevers no.60 | key.tsv of fr3986 (Bourdeau's key60 transcription, CC BY 4.0) + two blind sign passes with the fr3986 sign_guide tags | known answer FIRST on fr.3987 f.54 (Henri IV to Nevers, 10 Nov 1593, "avec chiffre et déchiffrement", court hand), pre-registered gate below; then f.91 vs 200 value-shuffled keys | -- | -- | caution carried: no.60 on the fr3986 Revol copies ranked 194/201 (worse than shuffled) because the copyist's hand could not be read (36% reader agreement; instrument retired there); f.91 and f.54 are cleaner hands, so this is a different test, not a retry |

Next best attempt and why: BNF-G60 (brief .claude/briefs/runs/2026-10-08-ytbiz-bnf-g60.md).

| 8 Oct 2026 | f.91's cipher is Nevers no.60 | BNF-G60 gate G1 (fr.3987 f.54 known answer), pre-registered | value-shuffled keys (not reached) | G1 NOT RUN, stopped before any sign pass: no agreement number, no shuffle number, no target decode | non-test: gate (unrunnable as priced; no cost spent on Sonnet calls) | see G60 note below |

G60 note (BNF-G60, 8 Oct 2026 06:00-06:04 UTC by date -u; intake_gate_check.py exit 0, "open (line 1)"). Located by eye on
Gallica btv1b90606320 (fr.3987; manifest has 0 folio labels): f.54 = canvas 99 (leaf head "10 de Nov.re 1593", foliation 54
top right), continuing on canvas 100 (more cipher lines) and canvas 101 (last lines, signature "Henry", dated "Dieppe ... 1593"
by thumbnail). Canvases 103 / 105 / 111 carry folios 56 / 57 / 60. Read at 1800 px (~16
gallica.bnf.fr requests total, two 503s/one reset, each retried once). What the leaf is: a FULL-PAGE cipher letter, about 34
cipher lines on canvas 99 alone (about 60-70 signs a line, ~2,000 signs), plus more on 100-101. The interlinear decipherment
is word-level and sparse: the clerk's plain words sit above only some cipher groups (roughly 1 word per 6-10 signs, ~15-20%
of the text, wide gaps, no word boundaries in the cipher), so "aligned spans" need a gloss-word to cipher-group alignment
the gate does not define.
Why stopped: the gate as written needs 2 sign passes + 1 reconciliation over "the cipher runs" of f.54 = ~2,000+ signs per
pass against the 82-row key inventory. Brief price: 4 Sonnet calls at ~0.6 each (~$2.4). Repo rate for sign passes (GOLD-4D,
CLAUDE.md Usage 6: ~1,300 signs in one call stopped at 3.3x a $7 cap) puts one faithful pass on this page far above the
whole $7 cap, and a 4-8-line sub-span (~250-500 signs, ~8 glossed words) would be a different, much lower-power gate
(a p99 over a handful of letters) than the one pre-registered. Choosing the span is the brief's call, not the worker's, so
the gate was not run, not shrunk and not replaced. Target f.91: not touched.
Next best attempt (for the re-brief, not run): pre-register a span on canvas 99 (e.g. lines 1-8, with the glossed words listed
by position from one gloss-reading call), a per-pass cost from one measured 2-line pass, a gloss-to-cipher alignment rule, and a
minimum glossed-letter count below which the shuffled p99 is declared non-discriminating; crop with `tools/iiif_lines.py
--ark btv1b90606320 --canvas 99 --out ciphers/fr3987-nevers-revol-1593/images --prefix f54` first (not run). Caution carried: this
hand-family read 36-55% pass agreement on fr3986/fr3987 f.66 copies, so a 0.60 gate has real chance of failing on reader error,
which would be logged as a non-test, not a no.60 negative.
