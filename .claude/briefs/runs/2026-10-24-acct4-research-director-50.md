# Research director, wave 50 (24 Oct 2026, 10:5x UTC by date -u): classify the no. 32 key's 429 copy conflicts

Common tail .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself). Done line addressed for the account-4 parent. Offline job: no network, no login, no images.

## JOB KEY32-CONFLICTS (account 4; Sonnet 5; cap USD 3; box 30 minutes; hosts: none (disk only); Price: vision calls: 0 x USD 0 = 0)

ciphers/sp84-wickfort-bacquoy-1660-63/key.tsv (grade H, built by build_key_no32.py from DECODE 509 and 506's transcriptions of TNA
SP 106/6 no. 32) carries 429 rows flagged `conflict`: 210 of the 549 (class, code, mark) keys shared by the two copies disagree. Rule 4
keeps both; this job says what kind of disagreement each is, so the key is usable when a letter image arrives.
1. Write ciphers/sp84-wickfort-bacquoy-1660-63/conflicts.py: for every conflicting key, pair the 509 and 506 rows and label the pair
   `identical-after-normalisation` (case, accents, u/v, i/j, final -s, abbreviation marks, whitespace), `spelling-variant` (same
   referent, Levenshtein <= 2 after normalisation or a listed period variant such as Reyne/Reine, Dorleans/d'Orleans),
   `same-code-different-meaning`, `same-meaning-different-code`, `one-side-blank`, or `other`; write conflicts.tsv (code, mark, class,
   meaning_509, meaning_506, kind, note) and append a `conflict_kind` column to key.tsv through build_key_no32.py (so `--check`
   still regenerates it; do not hand-edit key.tsv), with the counts per kind in a "## Conflicts (KEY32-CONFLICTS, 24 Oct 2026)"
   section of NOTES.md.
2. For `same-code-different-meaning` and `same-meaning-different-code` pairs only: list them in full in NOTES.md with the page each
   copy came from; say which copy (509 pp.2-3 or 506) is internally consistent with its own neighbours (alphabetical order inside the
   Villes/Royaulmes/word sequences, number runs) and record that as a note, never as a resolution -- grade stays H with the conflict
   flag until a letter decides.
3. Sanity table for the next reader: per class, code range, count, and the share with a conflict; flag any class whose range
   disagrees with chauran.htm's description (persons 20-76, Villes 61-89, Royaulmes 90-108) -- a disagreement is a finding, not a fix.
Never decode, never apply the key to a letter, never touch any other folder. Report: counts per kind, the number of genuine value
disagreements, the one class most affected, five lines.
