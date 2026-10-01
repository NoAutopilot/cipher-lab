# BER-FRCORP: berthier-napoleon-1812 -- build the era- and register-matched French judge corpus the folder names

Written 1 Oct 2026 23:4x UTC (clock read) by the account-4 parent (session_01SEzoee67SivPooFpTkxMme).
Role field for every ROOM.md line: `BER-FRCORP (account-4)`. Model: Fable 5.1 (Opus 5.5 if Fable fails). Cap: USD 5.
Box: 45 minutes. No vision calls. Hosts: archive.org only (advancedsearch + `_djvu.txt` downloads), one request at a
time, 1.5 s apart, at most 30 requests; stop on any 403/429/challenge.

## The job, in one line

Run the folder's own named next step (NOTES.md, BER-HOMO section, 27 Sept 2026): "No French corpus on disk matches
both the 1800-1820 era and an official/military register; building one is ... the next step for a future breadth
pass." Build `tools/data/fr1810/` the way `tools/data/pt18/` was built (V6-PTCORP, 25 Sept 2026, read its README.md
and MANIFEST.tsv first), measure its reliability the way CLAUDE.md rule 3 requires, and wire it so a spec can use it.

## What to build

1. Sources (Internet Archive OCR `_djvu.txt`, public domain, French, 1800-1820 official/military register). Candidates
   to check by `advancedsearch.php` and pick from, at least four distinct volumes from at least three distinct
   works (per-fold spread needs >= 4-5 files, rule 3's es17c lesson): *Correspondance de Napoléon Ier* (the 1858-70
   edition, volumes covering 1805-1813), *Bulletins de la Grande Armée* / *Moniteur universel* reprints,
   *Mémoires du maréchal Berthier* or Berthier's printed orders, *Journal des opérations* volumes, the *Recueil des
   lettres* of a marshal (Davout, Masséna) if an 1800-1820 text. Prefer letters/orders/dispatches over narrative.
   Trim modern front matter (Google boilerplate, editorial preface written after 1830) as pt18's README describes,
   and record each cut line in MANIFEST.tsv.
2. Size: aim for >= 1,000,000 letters after `fold()` (pt18 reached 3.2M). Write README.md (why each file, dates,
   register, what was trimmed) and MANIFEST.tsv (identifier, title, date, URL, bytes, letters, fetch date).
3. Reliability (rule 3, the es17c/pt18 paragraphs): run the judge's leave-one-file-out false-negative check at the
   target's own length band (N about 300-350 letters; berthier's spec has N=325) and report the blended rate AND the
   per-fold spread; compare against `tools/data/fr18` on the same check. Use the same method `tools/data/es17c7/`
   or pt18's README documents (read it; do not invent a new one).
4. Wire it: add `fr1810` to `tools/judge_plaintext.py`'s `LANG_CORPORA` only if the file's own pattern for pt18 is a
   registry entry (follow exactly how pt18 is registered); otherwise document the `judge.corpora` path a spec needs.
   Do NOT edit `specs/berthier-napoleon-1812.json`'s judge block in a way that changes any recorded result; add a
   `judge_note` naming the corpus as available. Add one row to `tools/data/README.md`.
5. Do not run any solver family on the target. The homophonic family's control was BELOW GATE at N=325/K=207
   regardless of corpus (HYPOTHESES.md); the corpus is for the next instrument (a two-part/blockwise code family,
   SYSTEM.md "Tools wanted"), not for a rerun.

## Finish

- NOTES.md: a dated section "## BER-FRCORP (1 Oct 2026, account-4)" with the corpus summary, the two reliability
  numbers (blended and per-fold) for fr1810 and fr18 side by side, and the one-line next step. Status word stays `open`.
- Commit by explicit path (tools/data/fr1810/, tools/data/README.md, tools/judge_plaintext.py if touched,
  ciphers/berthier-napoleon-1812/NOTES.md), rebase on origin/main, `python3 tools/restricted_guard.py --outgoing`,
  push to main. If `tools/judge_plaintext.py` was touched run `python3 -m pytest tools/tests -k judge -q` first.
- ROOM.md: claim line before fetching, done line with the letter count, the two reliability numbers and the request
  count per host. Rule 10 wording only. Stop when the brief is met.
- The common tail of `.claude/briefs/README.md` applies in full.
