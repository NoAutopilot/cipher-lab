# PREREG -- MQS-WITNESS-LABELS (LANE MQS-3, account 4), `tools/decode_witness.py --label-diffs`

Written 9 Oct 2026, 10:09 UTC by date -u, before any control below was run (the option was smoke-run once on
the unplanted kp86 pair to check it parses: 96 witness words, 32 equal, 8 equal words of 3+ letters).
Method credit: Lasry, Biermann and Tomokiyo 2023 (Cryptologia 47:2) pp.102, 110, 122-124, 131 n.70.

## Known answer

Pisany kp86 (ciphers/fr16045-pisany-rome-1585): decode `reading_f244r_M.txt` (decode_key.py, key86 Tomokiyo)
against the period clear copy `kp86/colbert_p49_50.txt` (Colbert 16 pt II pp.49-50). Plaintext KNOWN by
prior_work.py (`--item-spec 'shelfmark=BnF fr.16045;folio=244r;date=1586-09-17;sender=Pisany;recipient=Henri III'
--step-type decode --known-answer gate:MQS-WITNESS-LABELS --fetch`: exit 4, "verdict plaintext: KNOWN",
13 own-work LEADs -- our own kp86 files, which is the point of a known answer). No reading, key, status or AUDIT
change.

## Control: planted differences

At witness words (3+ letters) the unplanted run labels `equal`, isolated (more than 2 words apart), plant in equal
numbers per class: omission (decode letters deleted), addition (a 3+ letter witness word inserted after the
word), substitution (half whole-word from the passage's own vocabulary, half one letter changed outside the
normalisation pairs i/j/y, u/v and doubles), spelling-only (a change full() undoes: i->j, i->y, u->v, a doubled
or undoubled consonant), name/code (letters replaced by one code mark). Re-label; score label == planted label
at the site.

- Arm A: base = the witness letters themselves (a clean decode, word division dropped), `--plant-base witness`,
  20 seeds x 4 per class, `--shuffles 1000`, seed 1.
- Arm B: base = the real f.244r decode (err_2reader 0.284, many natural differences), 40 seeds x 1 per class,
  `--shuffles 1000`, seed 1. Sites repeat across seeds (8 eligible words): the seeds are not independent.

Null: the tool's own predicted labels permuted across the planted sites (label-shuffled), 1000 times.
Why the null can fail differently (rule 3): the statistic is per-site agreement of predicted and planted label;
the permutation keeps the label multiset but breaks the site-label pairing, so it scores the class-marginal
agreement (about 0.2 with five balanced classes) and can only equal the tool's accuracy if its labels carry no
information about the site.
Ceiling: Arm A is expected near ceiling; this is a labelling known answer, not a gain gate (the tool is
deterministic, no restarts), so the rule-3 headroom clause does not apply; Arm B is the realistic arm.

## Gates (expected in brackets)

- Arm A: accuracy >= 0.90 [~0.95], every class >= 0.80, accuracy > null p95 [null ~0.2], one-letter
  substitutions labelled spelling-only <= 5% [0].
- Arm B: accuracy >= 0.70 [0.6-0.8, uncertain], > null p95, one-letter substitutions labelled spelling-only <= 5%;
  per-class counts reported.
- Shelf: both arms pass -> `controlled-only`; any gate missed -> `weak` with both numbers, nothing run on a target
  from it, not re-briefed.
- Criteria scan (`--criteria-scan`): no known answer of its own -> `weak` whatever it prints; it is run once on
  the kp86 copy for description only.
