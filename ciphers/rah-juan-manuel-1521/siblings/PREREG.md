# R11-RJMSIB pre-registration (6 Oct 2026, written 09:5x UTC by date -u, pushed before any scored run)

Material: Tomokiyo's two hand-drawn alphabet tables, cryptiana.web.fc2.com/code/JuanManuel.png (fetched 6 Oct 2026, sha1
7524f16d...) and AlonsoSanchez.png (the copy in Bourdeau's cyphersolver targets/sanchez1522/tomokiyo/, MIT; sha1 d6bbaea0...);
Tomokiyo's two nomenclator tables already on disk (sources/cryptiana/keys/AlonsoSanchez_1.tsv = Sanchez, _2.tsv = Juan Manuel);
this folder's alphabet.tsv (JM-ALPHA, labels of passes/inventory.md). Images not committed (third-party); sha1s here.

Honest note: the worker looked at both tables before writing this file. The shape labels are written in siblings/shapes.tsv
from a fixed vocabulary (one row per sign drawn: table, letter, shape label, firm/uncertain), before scripts/siblings.py is
run; firm-only is the primary analysis.

Statistics (scripts/siblings.py, 10,000 permutations, seed 1522):
1. V, shape-value concordance JM vs Sanchez: number of plaintext letters (and the null class) for which the two published
   tables share at least one sign shape with the same value. Control: the Sanchez table's values permuted among its signs
   (inventory fixed, values move, so V can change). Gate "shared design key" = V > null p99. Descriptive only: inventory
   overlap (shapes present in both tables, any value) -- a value permutation cannot change it (rule 3, orthogonal control),
   and no shape-labelled unrelated 1520s Spanish alphabet is on disk, so it is reported, not gated.
2. W, this folder's alphabet.tsv against each published table: number of C-graded signs (JM-ALPHA) whose value equals the
   published table's value for the same shape (multi-letter values count if they start with the table letter). Control: the
   published table's values permuted. Reported for both tables; a W(JM) above its p95 is external corroboration of the
   in-sample alphabet, not a gate on anything downstream (no key or reading change in this job).
3. T, nomenclator table fit: among plaintext words present in both code tables (normalised: lower case, parentheses and
   '?' removed), number with the identical code group. Control: JM codes permuted among JM's words. Gate "shared
   nomenclator" = T > null p99. Descriptive: Spearman rho of code rank vs word alphabetical rank in each table (Tomokiyo's
   ordering rule), and the final-letter sets of the code groups.
No key, alphabet or reading in this folder is changed by this job, whatever the result.
