# TXB2 pre-registration: benchmark item dint-f128-print (account-2 worker TXB2, 3 Oct 2026, before any score)

Written and committed before `tools/tx_bench.py` is run on this item. Nothing has been scored on it yet.

Source: ciphers/fr3621-dinteville-1592/f128 (BnF fr.3621 f.128r, Dinteville to Nevers, 1 July 1592).
Known answer: the 1882 *Revue de Champagne* XII p.340 print of the letter's plaintext, aligned to the reconciled
sign sequence by DIN-PRINT (`f128/print_align/align_print.tsv`, its own PREREG.md; syllabic mode, gate passed on the
print-equivalent gloss norm). The print is independent of every reader in this project; the key is not a period key
sheet, it is `key_print.tsv`, rebuilt from that alignment (period decipherment = gloss/print, key = ours from it).

Truth per reference position (reference = `gloss_pairs.tsv` cipher signs, per physical line L02..L05, segments
concatenated in order; this is the reconciled read):
1. scored only if the align_print status is `agrees` AND the reference sign's key_print row has agree == n and n >= 2
   (a sign the print alignment never contradicts, seen at least twice);
2. truth = the set of all signs whose key_print row passes rule 1 and whose meaning equals that position's print
   chunk (homophones the print cannot tell apart are all right);
3. every other position (null-or-unaligned, conflict, single, a sign with agree < n or n < 2) is excluded and counted.

Circularity (stated, not hidden): the reference sequence and the key both come from the reconciled read, so the
reconciled read scores 0 on scored positions by construction and is NOT scored. A reconciled-read error on a sign
seen >= 2 times with no conflict would be absorbed into the key; rule 1 limits but does not remove this. The raw
blind passes A and B (Sonnet, crops only, no key, no print) are independent of the key and are what is scored.
err_true here is conditional on the reconciled segmentation and on key_print; it is a lower bound (tx_bench scope).

Two scores, both reported side by side (rule 3, PX-BRODEC transcription convention):
- raw: pass labels as written vs the reconciler's label set;
- norm: `benchmark-tx/dint128_label_map.tsv` maps the reconciler's split labels back onto the blind pass
  instructions' inventory (`f128/pass_instructions.md` gave one label for each pair): D->4, al->a, zh->m, div->-:-,
  plus->+. Labels with no instruction equivalent (r, h, B, n) are not mapped. Applied to output, ref and truth alike
  by a new `tools/tx_bench.py --label-map` option. The raw/norm gap is notation; the norm figure is the err_true
  figure for this hand.
Pass conversion: per physical line, every non-CLEAR row's signs in order; '-' rows with no signs dropped; nothing else
edited (overlap duplicates stay; the aligner counts them as insertions).
Split: dev (new key family, Dinteville 1592; no eval item exists for it).
