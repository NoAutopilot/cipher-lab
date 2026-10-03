# Pre-registration, DUCH-F13 (account-1 worker for LANE-A1), 3 Oct 2026, written before any f.13r pair was read

Source: fr.4712 f.13r = Gallica btv1b9058289m canvas 22, right page, native region 4250,200,3350,2900.
Pairs file: f13_code_gloss.tsv (code, line, gloss_A, gloss_B, gloss, grade). Grade H = both blind passes give the same
code number AND the same gloss (orthographic variants and abbreviation marks aside) AND neither marks it illegible;
anything else M; a code with no gloss over it is listed with gloss "-" and never carried.

Carry rule (f.13r -> f.10r): an f.10r token takes an f.13r gloss only if
 (a) its number equals the glossed f.13r code number exactly (two-digit token = two-digit code; f.13r single-digit
     codes 1-9 match only a single-digit f.10r token, i.e. Tomokiyo's "8");
 (b) the f.13r pair is grade H;
 (c) the same-hand/date condition holds: the main hand of f.13r and of f.10r are judged the same writer on a
     side-by-side look at crops already cut (recorded in NOTES.md before the carry is applied); the date window is
     "same volume, same correspondent, undated" for both and is recorded as unverifiable, not as met.
 If (a)+(b)+(c) hold the carried value is graded C at best; if (c) fails or is undecided, M. Codes with two different
 H glosses on f.13r are M everywhere. Segmentations: S1 (Tomokiyo), S2 (pairs from line start), S3 (offset 1),
 exactly as PREREG_duchkey1b.md defines them; each reported separately.

Statistics, with the control each can and cannot fail:
 1. Coverage = number of f.10r tokens (of 37 under S1; of each segmentation's count under S2/S3) that receive a
    gloss. The briefed control (f.13r glosses rotated among codes) CANNOT change coverage: coverage depends only on
    which numbers carry a gloss, not on which gloss (CLAUDE.md rule 3, last paragraph: a control orthogonal to the
    statistic is a non-test). So coverage under rotation is reported as identical by construction, and licenses
    nothing; it is descriptive.
 2. Overlap control that can differ: the share of f.10r tokens covered by f.13r's glossed code set vs 1000 random
    code sets of the same size drawn from the numbers that occur as f.13r codes' range (1-99, uniform without
    replacement); report the observed coverage and the p (share of random sets with coverage >= observed).
    A p <= 0.05 says only that f.10r's numbers concentrate on f.13r's code set more than chance; it does not read f.10r.
 3. Key-family check (can differ under rotation): the share of f.13r H codes whose gloss agrees with key no.1's
    value for the same number (keys/key_no1.tsv; a letter value never agrees with a name/word gloss), vs 1000
    rotations of the glosses among the H codes. Report observed agreement and the rotation p. This tells whether
    f.13r is in key no.1's family; it does not change the carry rule.
Gate for "f.10r gets a crib": statistic 2 p <= 0.05 AND at least 3 carried C tokens under S1. Otherwise the carry is
reported as a lookup only (no reading claimed), and no reading is claimed beyond the glossed tokens in any case.
