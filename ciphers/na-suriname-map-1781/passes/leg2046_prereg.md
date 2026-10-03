# GAPS18-na-suriname-map-1781 (account-4), 3 Oct 2026 -- pre-registration for the 4.VEL 2046 legend, written and committed
# BEFORE either blind pass was merged and before any 2046 token was decoded (no ciphertext_2046_legend.tsv exists at this commit).

Key: key_period_codes_nieuw.tsv as committed (Nieuw Secreet Alphabet, NA 1.05.03 inv. 86 scan 0003), plus exceptions_nieuw_image.tsv
only for the tokens it already names (none on 2046). No new key row will be added from 2046 itself in this job.

Control (rule 3; the one GAPS14 pre-registered at f0840cdc and GAPS16 re-ran): control_prereg_vocab.py, unchanged vocabulary
vocab_prereg.txt (95 words built mechanically from crib_2038_legend.tsv and crib_2042_legend.tsv -- 2042 is a plain Purmerent
legend, so the list was pre-registered for this sheet too), unchanged statistic, seed 14, 1000 draws each, run on the 2046 file
ALONE: `python3 control_prereg_vocab.py 1000 key_period_codes_nieuw.tsv ciphertext_2046_legend.tsv`.
Pass rule, stated now: the real hit count must exceed the max of BOTH nulls (shuffled-value, shuffled-order), with 0/1000 null
draws >= real. Either null reaching the real count = FAIL, reported as such.
Judge: specs/na-suriname-map-1781.json names language nl; tools/judge_plaintext.py has no nl corpus wired (its own comment), so
the judge is expected not to run; its output is pasted either way and no PASS is claimed from it.
Grading: decode_key.py's own grading via a decode.json job (H where the sign is the sheet's own character, M by shape name or
two-valued, U unkeyed), transcription H/M carried in the note. No S grade is claimed from this sheet.
