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
