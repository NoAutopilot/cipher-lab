# PREREG-GAPS199 (3 Oct 2026, 18:47 UTC, account-4): second blind native-zoom read of the 625 margin word 1

Written and pushed before the vision call. Target: image 0003 (hstam_4_f_daenemark_nr_125_0003.jpg), margin gloss
beside p2:7 (in-text "und hat 625. hierbey signalirte dienste gethan"): the margin repeats "625" over two words in
the bold glossing hand; word 2 reads Ahlefeldt (pass B + GAPS168, M); word 1 is unread.

## Prior looks at word 1 (rule 3 third-attempt check)
- GAPS155 pass A (blind, 2-line band crop p2_L04): "gesandschaffter?"; pass B (blind, same crop): "y?rkestelr?";
  reconciler 2x zoom: "?-?-?-?-stelt". These were whole-page transcription passes, not a targeted gated read.
- GAPS168 (worker's own native zoom, context known, not blind): 9-10 letters ending -halt?/-stelt, "Stathalter possible", one eye, left unread.
No earlier look was a targeted read judged against a gate, so this is the first gated attempt by the targeted
native-zoom method, not a third failure of it. If it fails, a further look by the same method is [retired] (rule 3,
third-attempt clause) and only new material or a different instrument (a palaeographer, a sign-by-sign atlas of this
hand) reopens it.

## Crops (equal size, 420 x 100 px, native resolution, no upscaling)
Cut with tools/iiif_lines.py, one band per region, --centres by eye, debug overlays checked:
`python3 tools/iiif_lines.py --image ciphers/hessen-daenemark-1672/images/hstam_4_f_daenemark_nr_125_0003.jpg --out <scratch>/crops --region R --prefix P --centres C --lines-per-crop 1 --overlap 0 --debug`
with (P, R, C) = (t, 280,1130,420,200, 100) target; decoys (a, 590,700,420,200, 88) p2:3 gloss;
(b, 1910,1970,420,200, 100) p2:17 gloss; (c, 510,3030,420,200, 112) p2:28 first gloss; (d, 1450,3040,420,200, 96)
p2:28 second gloss; (e, 2050,620,420,200, 100) p2:2 gloss. Each run printed "wrote 1 crops".
Copied to images/crops_gaps199/X1..X6.jpg in an order shuffled with random.Random(199); the map's sha256 prefix is
620980e5ec1cec31 (revealed in NOTES.md after the read). Decoys are 5 already-settled gloss words of this hand (C-graded in
transcription/p2_ciphertext.tsv): Cur Brandenburg (p2:3), Berlin (p2:17), Holland (p2:28), Gen. Staden (p2:28),
K. Dennemarck (p2:2).

## Read
One Opus 5.5 subagent call, crops only (six paths), told only: 17th-century German chancery hand, each crop's
main bold dark-ink word or short phrase is a gloss; read it letter by letter, give a best reading, alternatives and
a confidence. No context on 625, the letter, Ahlefeldt or Statthalter.

## Gates (normalised: lower case, letters only, u/v and i/j folded, doubled consonants collapsed)
- Decoy gate: at least 4 of 5 decoys read correctly (best reading within edit distance 2 of the settled gloss:
  curbrandenburg, berlin, holland, genstaden/genstadt, kdennemarck/dennemarck). Below 4/5 the read is a non-test.
- Agreement with the first read: the target's best reading normalises to stathalter (edit distance <= 2 after
  collapsing, so Statthalter / Stathalter / Stadthalter count). A partial (only an ending such as -halt or -stelt) is
  not agreement. A different full word is disagreement.
- Grade: 625 stays [?_Ahlefeldt] at M unless BOTH the decoy gate passes AND the target agrees. Then key_gloss.tsv
  625 becomes "Stathalter Ahlefeldt" at C (two independent eyes on each word); the person identification
  (Frederik von Ahlefeldt) stays I and is not entered in the key. Disagreement or partial: 625 stays M, word 1 stays
  unread, the step is logged [retired] for this method. decode_key.py --check must exit 0 after any change.
