# PREREG VILL-STRIPS (3 Oct 2026, committed before the f.74r / f.104r letter strips are read at native resolution)

Units: fr.3995 f.74r (canvas f147, "Doncheri 1591 20 Aoust") and f.104r (canvas f202, "...tangi 1593 23 Juillet")
letter strips, native crops by tools/iiif_lines.py, one blind read per strip -> keys/key_f74r_letters.tsv,
keys/key_f104r_letters.tsv (code -> letter, grade M/I by legibility; nothing H, the table is not a decipherment).

Gate 1 (coverage, PREREG-VILL-KEYS rule 2). coverage = share of the 753 target tokens (bourdeau/ct_*.txt) whose sign
type is a cipher value in the strip as read. A figure token counts as covered only if the strip uses that figure
as (part of) a code; non-figure signs only if an identical-looking sign is read in the strip. Coverage < 0.5 =>
"not testable" for that strip, stop, no score.
Gate 2 (power, before the target is scored; ARM-S3 lesson). Synthetic French text of the target's own token length
and the strip's own code design, enciphered with the strip as read, then decoded with the strip and scored the same
way as the target, at the measured reader error (share of strip cells graded I/illegible, applied as random code
corruption). 20 synthetic texts; power = number whose real key ranks 1 of 201 against 200 value-shuffled keys.
Power < 16/20 => non-test, stop before scoring the target.
Gate 3 (score). PREREG-VILL-KEYS rule 3: decode target, tools/judge_plaintext.py fr16, rank and z against 200
value-shuffled keys. Pass = rank 1/201 and z >= 3. No reading committed unless pass with power; grade S at best.
