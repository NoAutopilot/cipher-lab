LANE R6 P5 -- antt-fcc-costacabral-1865: the self-glossed draft as a key dataset (Sonnet, cap $5, box 45 minutes). Common: 2026-09-25-lane-r6-common.md.
Intake gate (live, 25 Sept 16:18 UTC): "antt-fcc-costacabral-1865: open (line 1) -- edition/page or full-text-search citation found within 6 lines" (exit 0).
Lead class: interlinear gloss (the draft carries its plaintext syllables over the codes, e.g. di-ga-mo 926-923-1212). Disk only (images/ m0112-m0114
from P4). Job: (1) crop the draft (m0113, m0114) line by line; (2) two passes of (code, gloss syllable) pairs -- you pass A, ONE blind Sonnet
subagent pass B, each to TSV on disk, committed per page; reconcile (tools/reconcile_passes.py or a small script), settle disagreements on the
image; (3) write key.tsv (code, value, grade: C where the gloss gives it on the leaf, M where unclear) and ciphertext.tsv (the codes in order);
decode.json + `tools/decode_key.py ciphers/antt-fcc-costacabral-1865 --check` exit 0, grade counts; the reading is the draft's own plaintext
(a found-solved shape: the leaf deciphers itself). (4) Describe the system: code range, syllabary vs words, homophones, and whether m0112's
cover letter names the key or the correspondent. Rule 7: pt judge is not a corpus for 1865 (COMMON item 3) -- say so, do not run it as a gate.
NOTES.md section "## P5: key and reading from the draft (25 Sept 2026, LANE R6)". Hosts: none. ROOM done: "for LANE V6: ciphers/antt-fcc-costacabral-1865
reading ready (self-glossed draft), C <n> M <n>".
