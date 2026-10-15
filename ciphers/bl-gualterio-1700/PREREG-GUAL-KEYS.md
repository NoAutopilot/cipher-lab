# PREREG-GUAL-KEYS (15 Oct 2026, 02:5x UTC; worker GUAL-KEYS for LANE DEFAULT-A4-0235-15, account 4)

Job: image-check the M rows of `keys/hmc6_gualterio.tsv` (122: leaves n84 41, n85 39, n87 42) and `keys/hmc6_sicily.tsv`
(33: leaf n82) against the printed leaves of HMC *Calendar of the Stuart Papers* vol. VI (archive.org `calendarofstuart06grea`).
Registered before any strip is read or scored.

- Material: the four leaf images (archive.org, <= 6 requests), cut into line strips with `tools/iiif_lines.py --image`;
  strips and leaves stay in the session scratchpad (never committed).
- Pass: one Sonnet subagent per leaf, given only that leaf's strip paths and a row list (code | meaning) in random order:
  the leaf's M rows plus >= 5 planted wrong rows (one character-level or pairing change each: a cant name swapped with
  another row's, a letter changed, a word dropped). For each row it answers EXACT (the print pairs exactly this term with
  exactly this cant name, spelling as printed) or DIFFERS (with what the print shows) or NOT-SEEN.
- Gate per leaf: planted rows caught (DIFFERS) >= 80%. A leaf below the gate regrades nothing.
- Regrade on a leaf that passes: M -> H only for rows answered EXACT. DIFFERS rows are checked by this worker on the strip
  and either corrected (FIXES in `keys/build_hmc6_keys.py`, graded H when the worker's own read and the subagent's
  agree, else kept M with a note) or left M. NOT-SEEN stays M.
- Rebuild: `python3 keys/build_hmc6_keys.py` then `--check` (exit 0). No ciphertext is on disk: nothing here is a reading.
