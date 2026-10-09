# TXE-G read-free proxy: recovery renderings on Birago no.87 dev_tune (9 Oct 2026)

Gate (PREREG-txeng-2 amendment): fixed > broken vs plain, p < 0.01. Topk/bench committed before scoring in becae9a4. No vision call. Regenerate:
    python3 tools/tx_recovery.py proxy --atlas ciphers/nevers-birago-fr3251-1572/atlas --work benchmark-tx/txeng/recovery --holdout f178r_ --holdout f178v_ --holdout f179r_ $(for i in $(seq -w 1 12); do echo -n " --prefix f178v_${i}_"; done) --setting plain --setting sauvola --setting clahe --setting swn

```
== stored
birago1572-no87 [eval] err_true 0.192 (66/343) 95% 0.154-0.237 | wrong 43 deleted 19 inserted 4 | excluded 11 | lines missing 17
  top confusions (truth value <- read): s<-T50 x7, o<-T83 x5, i<-<deleted> x4, a<-<deleted> x3, n<-<deleted> x3, d<-T36 x2, e<-T36 x2, e<-T85 x2
split eval: err_true 0.192 (66/343) 95% 0.154-0.237
paired bench.tsv vs bench.tsv on birago1572-no87: 343 common scored signs; base wrong 66, output wrong 62; fixed 7, broken 3; sign test p = 0.3438
== plain
birago1572-no87 [eval] err_true 0.204 (70/343) 95% 0.165-0.250 | wrong 49 deleted 17 inserted 4 | excluded 11 | lines missing 17
  top confusions (truth value <- read): s<-T50 x7, o<-T83 x6, i<-<deleted> x3, d<-T36 x2, o<-T26 x2, e<-T60 x2, e<-T36 x2, a<-<deleted> x2
split eval: err_true 0.204 (70/343) 95% 0.165-0.250
paired bench.tsv vs bench.tsv on birago1572-no87: 343 common scored signs; base wrong 66, output wrong 66; fixed 0, broken 0; sign test p = 1.0000
== sauvola
birago1572-no87 [eval] err_true 0.210 (72/343) 95% 0.170-0.256 | wrong 51 deleted 18 inserted 3 | excluded 11 | lines missing 17
  top confusions (truth value <- read): s<-T50 x7, o<-T83 x7, i<-<deleted> x4, d<-T36 x3, a<-<deleted> x3, n<-<deleted> x3, f<-T37 x3, e<-T36 x2
split eval: err_true 0.210 (72/343) 95% 0.170-0.256
paired bench.tsv vs bench.tsv on birago1572-no87: 343 common scored signs; base wrong 66, output wrong 69; fixed 7, broken 10; sign test p = 0.6291
== clahe
birago1572-no87 [eval] err_true 0.394 (135/343) 95% 0.343-0.446 | wrong 89 deleted 38 inserted 8 | excluded 11 | lines missing 17
  top confusions (truth value <- read): o<-T83 x11, e<-T60 x6, l<-<deleted> x5, s<-T50 x5, a<-T60 x4, n<-<deleted> x4, o<-<deleted> x3, s<-<deleted> x3
split eval: err_true 0.394 (135/343) 95% 0.343-0.446
paired bench.tsv vs bench.tsv on birago1572-no87: 343 common scored signs; base wrong 66, output wrong 127; fixed 4, broken 65; sign test p = 0.0000
== swn
birago1572-no87 [eval] err_true 0.204 (70/343) 95% 0.165-0.250 | wrong 47 deleted 19 inserted 4 | excluded 11 | lines missing 17
  top confusions (truth value <- read): s<-T50 x7, o<-T83 x5, i<-<deleted> x4, n<-<deleted> x4, f<-T37 x3, d<-T36 x2, e<-T60 x2, e<-T36 x2
split eval: err_true 0.204 (70/343) 95% 0.165-0.250
paired bench.tsv vs bench.tsv on birago1572-no87: 343 common scored signs; base wrong 66, output wrong 66; fixed 3, broken 3; sign test p = 1.0000
```

Verdict: FAIL for all three (sauvola 7/10 p 0.63; clahe 4/65 harmful; swn 3/3 p 1.0); no setting earns the read. tx_taxonomy per-class movement not run: no setting moved the error mass (largest |fixed-broken| outside clahe is 3). Reader task text: none (no reads). Calls: 0. Notes and literature: research/TX-RECOVERY-PRACTICE-2026-10-09.md.

Follow-up (one line): fetch a colour master of btv1b9060248g if Gallica has one; every colour method in the note is a non-test on today's greyscale files.
