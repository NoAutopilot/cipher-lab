# DECODE Nevers-office 1590s cluster: scout for BENCHMARK-TX items (TXP-DEC, 9 Oct 2026)

Worker TXP-DEC (account 4, Opus) for LANE TX-ENGINEER-2, brief `.claude/briefs/runs/2026-10-09-account4-txp-dec.md`,
PREREG `benchmark-tx/PREREG-txeng2-0.md` section 0b item 1. Scout only: no transcription, no decode, no class.
Clock read with `date -u`: fetch 15:20-15:23 UTC, report written about 15:3x UTC, 9 Oct 2026.

**Fetch.** One DECODE login (`tools/decode_browser_login.js 9444 ... --listen`, 2 s apart): 18 RecordsView pages and
29 full-size images, 46 listen requests plus the login and the primary page, all HTTP 200, no `forbidden.png`. The
brief's 18 records plus 9453 (the fr.3623 "Key" record inside the 9452-9458 range, fetched with the cluster). 1600-px
JPEGs, the manifest (native size, sha1) and a refetch note are in `sources/decode/nevers-1590s-2026-10-09/`.
Native resolution: fr.3619 pages are only 1653 x 2339 px (DECODE's copy; the 1600-px JPEG is near-native);
fr.3621 and fr.3623 pages are about 2030 x 2910 px. A build on fr.3619 should take crops from Gallica's native
image when Gallica answers again (it 403s today); the DECODE copy is enough to scout, marginal for line crops.

**Reference.** Dinteville f.128 key: `ciphers/fr3621-dinteville-1592/f128/print_align/key_print.tsv`, 29 signs:
`# . 0 1 3 4 9 B D L T a al c div f h m n o p plus r sq v w y z zh` (Latin-letter, digit and dot-mark forms plus a few
specials). Hand compared against the f.128 line crops `ciphers/fr3621-dinteville-1592/images/f128_L0?_s?.jpg`.

## Per record (one look per page, own eyes)

Signs and lines are estimates (signs in one line x lines). "Gloss" = a period decipherment on the page.
Hand (d) is "same scribe as the f.128 cipher" by eye: y / n / ?.

| rec | shelfmark | sender (DECODE) | (a) kind | (b) gloss, legible at native? | (c) est. cipher signs / lines | (d) f.128 hand | (e) signs seen; in key_print? | (f) problems |
|---|---|---|---|---|---|---|---|---|
| 9438 | fr.3619 f.73 | Birago, Langres, 25 Oct 1591 (Italian) | symbol | interlinear over all runs; legible | ~110 / 3 short runs | n (Birago's hand) | ∓ Δ ∇ ψ # o □ ¢; # o in key, rest not (Birago set) | short; Italian |
| 9439 | fr.3619 f.81 | Dinteville, Langres, 1591 | mixed (letter-forms, digits, symbols) | interlinear over all 3 lines; legible but small at 1653 px | ~110 / 2.5 | y? | ∓ ψ o □ ¢ 4 x z; o z 4 in key, ∓ ψ not | small leaf; low DECODE res |
| 9440 | fr.3619 f.89 | Dinteville, Langres, Nov 1591 | mixed, mostly digit + letter-form + dot | interlinear over nearly every cipher line; legible but small at 1653 px | ~750 / 17 (+1 in the postscript) | y | # . 0 1 3 4 □ w m v z ψ Δ; # . 0 1 3 4 m v w z in key, □ ψ Δ not | cramped interlinear, some glosses run over two cipher lines; low DECODE res |
| 9441 | fr.3619 ff.97-98 | Dinteville, Langres, Nov 1591 | P1 clear only; P2 mixed, same set as 9440 | P2 interlinear over all 6 lines; legible | ~270 / 6 (P2 only) | y | # 0 1 4 □ m w v z; most in key | P1 no cipher |
| 9442 | fr.3619 f.103 | Turenne, 29 Nov 1591 | digit (two-digit groups, dotted) | interlinear over all; legible | ~250 groups (~500 digits) / 13 | n | digits with over-dots; not the f.128 system | different office and system |
| 9443 | fr.3619 f.113 | Dinteville, Langres, 1591 | mixed, same set as 9440 | interlinear over all 4 lines; legible | ~180 / 4 | y | # . 0 1 4 □ w v ψ; most in key | low DECODE res |
| 9444 | fr.3621 f.31 | Vaudémont to Lorraine (DECODE) | **no cipher**: a clear "Déchiffrement des lettres de Mons. de Vaudémont ... [à] Mr de Dinteville", Jan 1592 | is itself a decipherment | 0 | n/a | none | unusable as a cipher item; a clear text whose cipher originals are not on this leaf |
| 9445 | fr.3621 ff.42-43 | Birago, Sainte-Menehould, 25 Jan 1592 | symbol, inside prose | interlinear over every run; legible | ~140 / 6 runs (P2) + ~35 (P3) | n | ∓ Δ ∇ ψ # o □ z 3; Birago set | cipher inside prose only, short runs |
| 9446 | fr.3621 f.48 | Birago, Sainte-Menehould, 1 Feb 1592 | symbol, inside prose | interlinear; legible | ~60 / 2 runs | n | Birago set | too short alone |
| 9447 | fr.3621 f.49 | Birago, Sainte-Menehould, 5 Feb 1592 | symbol, postscript | interlinear; legible | ~50 / 2 runs | n | Birago set | too short alone |
| 9448 | fr.3621 f.89 | Potier de Blancmesnil, 30 May 1592 | letter-form substitution (R S V w 6 8 φ #) | interlinear over all runs; legible | ~200 / 6 | n | Latin-letter and digit forms; a different system | different office |
| 9452 | fr.3623 f.23 | Dinteville (DECODE), Langres, 25 Oct [1591] (Italian) | symbol | interlinear over all 9 lines; legible | ~400 / 9 | ? (signed Dinteville; cipher hand looks Birago-style) | ∓ ψ # Δ ∇ □ o ¢ z 3; # o z 3 in key, rest not | Italian; crops already on disk `ciphers/fr3621-dinteville-1592/f3623/f23r_*` |
| 9453 | fr.3623 ff.35-36 | Bienvenut, Paris, Feb 1590 (DECODE "Key") | clear text with name codes; P2 is a code list (1 = Roy d'Espagne, 10 = Pape, ... 53 = St Sorlin) | the list is the key | ~25 code numbers | n/a | numbers only | not a cipher transcription item |
| 9454 | fr.3623 f.37 | Mayenne (DECODE), 15 June 1590 | clear with two digit runs | none seen | ~50 digits / 2 runs | n | digits | no gloss |
| 9455 | fr.3623 f.38 | 5 June 1590 | clear with ~8 digit runs | partial: letters over some runs | ~150 digits | n | digits | gloss only partial |
| 9456 | fr.3623 ff.39-40 | [Sy] to Nevers 1590 | **digit, whole letter** (two-digit groups, over-dots) | interlinear over every line, all three pages; legible, cramped | P1 ~3,200 digits / 54, P2 ~3,000 / 52, P3 ~250 / 4: **~6,400 digits, ~3,000 groups** | n | digits 0-9 with dots/strokes; not the f.128 system | dense; a digit hand, reader error unknown (likely lower than symbol hands) |
| 9457 | fr.3623 f.41 | Birago, 5 Nov 1591 | symbol | interlinear; legible | ~100 (P1) + ~260 (P2) / 3 + 7 runs | n | ∓ Δ ∇ ψ # o □ ¢ z; Birago set | runs inside prose |
| 9458 | fr.3623 f.75 | 1590 | P1 slip: clear + digit runs, partial gloss; P2 show-through of P1; P3 clear + names in code + one short symbol run | P3 interlinear on the runs | ~60 digits (P1) + ~30 (P3) | n | digits; φ B Z | too short |

## Ranked items to build as BENCHMARK-TX items

Reader error on file: Dinteville f.128, pass B mapped 0.188 (`dint-f128-print`); the Birago no.87 figure
(err_true 0.045, txcross) is for the 1572 Birago hand, not this 1591-92 set, so no figure is on file for the
1590s Birago symbol hand or for the 9456 digit hand. Build cost per item: two blind Opus passes at about 1.5 per call,
one call per page (per crop page), plus one adjudication unit at the same rate, plus the build script: about 7-9 per item.

1. **9440, fr.3619 f.89 (Dinteville, Nov 1591).** ~750 cipher signs, about 600 scorable after dropping line ends and
   glosses that overrun. Hand y by eye, repertoire mostly the f.128 set (# . 0 1 3 4 m v w z) plus □ ψ Δ. At the f.128
   rate (0.188) that is about 110 baseline errors on one leaf, enough for the 60-error pool alone. **Truth:** the
   period interlinear decipherment; key_print alone covers only 29 signs at partial agreement, so the truth key
   should be rebuilt from this leaf's own gloss with `tools/interlinear_align.py`, agree >= 2 (the dint-f128-print
   recipe), then checked against key_print where the two overlap. Cost about 9 (one page, but long: two calls per pass
   if cropped in halves).
2. **9441 P2, fr.3619 f.98v (Dinteville, Nov 1591).** ~270 signs (~220 scorable), same set and hand; ~40 baseline
   errors at 0.188. Truth as item 1 (rebuild, or reuse item 1's rebuilt key if both are the same cipher -- check on the
   first 20 aligned pairs). Cost about 7.
3. **9443, fr.3619 f.113r (Dinteville, Nov 1591).** ~180 signs (~150 scorable), same set and hand; ~28 baseline errors.
   Truth as item 1. Cost about 7. Items 1-3 together: ~1,000 scorable signs, ~180 expected baseline errors, one hand,
   one office, one month; build cost about 23.
4. **9456, fr.3623 ff.39-40 (digit, 1590).** The largest known-answer text in the cluster (~3,000 groups, fully
   glossed), but a digit hand with no reader-error figure on file; worth one cheap error probe (one blind pass on a
   10-line crop scored against the gloss) before building, since a digit hand may sit below the lane's 8% floor.
   Truth from the gloss by alignment (agree >= 2). Cost about 9 for a 15-line slice.
5. **9452, fr.3623 f.23r (Italian, signed Dinteville, Birago-style symbols).** ~400 signs, fully glossed, crops
   already on disk; a different repertoire from f.128 (Birago-type ∓ Δ ∇ ψ ¢), so it is a second hand, not more of
   the first. Truth from the gloss (rebuild). Cost about 7.

The Birago 1591-92 runs (9438, 9445-9447, 9457; ~750 signs across five letters in short runs) could pool into one
item with 9452 if they share a key; each alone is too short.

## prior_work.py (top 3)

`python3 tools/prior_work.py fr3621-dinteville-1592 --item-spec 'shelfmark=BnF fr.3619;folio=<f>;sender=Dinteville;recipient=Nevers' --step-type transcribe --offline`
(no date given: the tool takes only a full YYYY-MM-DD and the leaves carry month only), run 15:2x UTC, origin/main b4bb0effd:

| item | 3-tomokiyo | 3-solver (cached) | 3-solver unsolved-ciphers | 4-editions | 2-leaf | verdict / exit |
|---|---|---|---|---|---|---|
| fr.3619 f.89r | CLEAR | CLEAR | UNCHECKED-NET (no clone) | UNCHECKED-NET (no prior_editions row) | LOOK (no gloss/clear-copy check recorded) | LOOK, exit 4 |
| fr.3619 f.98v | CLEAR | CLEAR | UNCHECKED-NET | UNCHECKED-NET | LOOK | LOOK, exit 4 |
| fr.3619 f.113r | CLEAR | CLEAR | UNCHECKED-NET | UNCHECKED-NET | LOOK | LOOK, exit 4 |

No "own work" and no "contact first" line for any of the three. The 2-leaf LOOK hold asks for the gloss/clear-copy
check this scout has now done by eye (each leaf carries a full interlinear period decipherment); it stays owed in the
tool until recorded. All three are listed Decrypted on DECODE, so they are N0 by construction: the plaintext and its
decipherment of these very items are known (the period gloss, and DECODE's own record). They are benchmark material,
not reading targets.
