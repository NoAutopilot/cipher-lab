# GAPS149 periodicity test: pre-registered decision rule (written 3 Oct 2026 ~15:10 UTC, before any run)

Target: `basecode_cipher.txt` (N=229, K=26, one stream, line breaks ignored). Script: `periodicity_check.py`.

Statistics, for p = 1..20: IC_p = mean over the p columns (token i -> column i mod p) of the unbiased column IC
sum c(c-1) / (n(n-1)). Excess E_p = IC_p - IC_1 (removes the overall profile, so masc, running key and homophonic
-- aperiodic designs with different unigram peaks -- share one null). Friedman estimate
L_F = N(k_p - k_r) / ((N-1) IC_1 - N k_r + k_p), k_p = 0.0778 (fr16 window mean IC, GAPS145 masc clean), k_r = 1/26.

Controls (fr16, N=229, noise 0.23, profile-redraw recipe of homophonic.py; uniform-replacement reported as a
sensitivity row for the periodic controls): masc, running key (Vigenere, key window from another book),
homophonic K=26 (homophonic.make_control, noise 0.23), 40 seeds each = the pooled aperiodic NULL (120);
periodic Vigenere with a random key of length p for p = 2..12, 40 seeds each = POWER controls.

z_p = (E_p - mean_null E_p) / sd_null E_p. Max statistic Z = max over p=2..20 of z_p (family-wise over 19 periods);
its null distribution is Z computed on each of the 120 null seeds (standardized against the null itself).

Decision rule. The target is "periodic at p*" only if ALL of:
 1. target Z > null Z p95 (family-wise), with p* = the argmax;
 2. the multiples of the smallest period showing it hold: for p0 = the smallest p with z_p > 2 that divides p*
    (p0 = p* if none smaller), at least half of the multiples 2p0, 3p0, ... <= 20 also have z > 2
    (none required when 2p0 > 20);
 3. power: the same rules 1-2 applied to the periodic-Vigenere control at period p0 (when p0 <= 12) detect a
    period dividing-or-equal p0 in >= 50% of its 40 seeds. If p0 > 12 (no control) the reading is "periodic
    signal, untested power".
If 1 fails: "no periodic signal at N=229, err 0.23", and it is a control-backed exclusion of a periodic Vigenere
only at those periods p whose own power control detects in >= 80% of seeds (rule 3: name the periods where the
test had no power as untested, not excluded). If 1 passes but 2 or 3 fail: "ambiguous", no claim.
Friedman L_F is reported with its distribution under each control; it is descriptive, not a gate.
Caveat fixed in advance: the 11 dropped MARK^ flourishes and any dropped/inserted sign in the transcription shift
column phase; the controls model substitution error only, so a negative is conditional on no phase slips.
