# LANE V4 verifier V1: Posthius to Eysenmenger 1614 and 1618 (Opus, cap $10)

Common rules: `.claude/briefs/runs/2026-09-24-lane-v4-common.md`. Target: ciphers/trew-posthius-1614-18 (UB Erlangen,
Trew Briefsammlung; bavarikon objects UBE-TRE-00000BAV80016364 (13 March 1614) and UBE-TRE-00000BAV80016370 (Feb 1618)).
Claim under audit (NOTES.md "Reading (24 Sept 2026, LANE R4 F)"): both cipher passages read with the 12-pair reciprocal
tables written on the leaves, 109 tokens H 96 M 13, `tools/decode_key.py --check` exit 0; 1614 German "ich hab nit
gewist das ihr mein nachtbar wolt werden bei der dihlin ..." and 1618 "der heis ist ein feiner man der abraham kein gelt".
The solver flagged interlinear marks above the 1614 cipher lines that may be a contemporary decipherment: look at the
images in ciphers/trew-posthius-1614-18/images (full native resolution is on disk; fetch nothing from Erlangen unless a
crop is missing, one host, spaced) and decide whether a decipherment stands on the leaf (precedent: the Brienne 1646
AUDIT.md, interlinear decipherment = N0 without print). Then search independently: (a) Schmidt-Herrling 1940 (Trew
catalogue) entries for both letters; (b) editions and studies of Johannes and Erasmus Posthius (Karrer, Johannes Posthius
1537-1597, 1993; any Eysenmenger literature; Heidelberg university history); (c) trew-letters.com and the bavarikon record
notes; (d) Internet Archive full text, Google Books (with the key and country=US), HathiTrust bibliographic API, for the
distinctive phrases ("nachtbar", "dihlin", "Eysenmenger", "Posthius", "Chiffre") and the names; (e) DECODE
(read-only listing, no login) and the two solver repositories; (f) OpenAlex, Semantic Scholar, CrossRef, Persée/HAL for
Posthius/Eysenmenger/Trew cipher; JSTOR queries as rows in JSTOR-QUEUE.tsv. Classify each letter separately N0-N5 in
AUDIT.md with the safe and unsafe sentences; if N3 or higher write second-opinions/PROMPT-chatgpt.md and a
SO-POSTHIUS-1614-18 row in SECOND-OPINIONS-QUEUE.tsv; add or update the results row for this target in status.json (rule
10 wording); correct any over-claim in the folder. Do not decode. ROOM done line `for LANE V4:` with the classes.
