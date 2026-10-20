# Save incident, Vivonne ksplit sorter, 20 Oct 2026

Worker SORTER-SAVEFIX (account 4, session_0125yNvDSkqpz1QQBc8UwCuT), 03:04-03:4x UTC 20 Oct 2026. Page:
https://claude.ai/artifact/6cP2xmEZertkDcPoc9uYRC ("Vivonne 1573: split two signs", ASKS 173), template 2026-10-15.1 as published
(the published HTML was read with the Artifact tool and is identical to the repo copy `sorter_viv_ksplit.html` at d28084ba2 apart
from the publish wrapper).

## What storage holds (read 03:0x UTC with ArtifactData, before any change)

| collection | docs | content |
|---|---|---|
| moves | 6 | 5 at version 2, written 02:54:00-02:54:14 (f103r_L13_002 and f103r_L30_021 -> tray B-b, f103r_L01_022 -> tray B-c, f102v_L28_047 and f103r_L10_019 -> tray A-b); 1 at version 3, f102v_L09_004 -> NOT-LETTER at 02:59:31 |
| newpiles | 4 | tray A-b, tray B-b, tray B-c (02:53:59-02:54:08), NOT-LETTER (02:59:31) |
| piles | 1 | NOT-LETTER, verdict mark (02:59:31; written by the page whenever the not-letter pile is first made) |
| clusters, checked, added, recuts | 0 | |

Version 2 on a move means two writes to that document: the tap that took the sign out (to OUT) and the placement. So every
take-out that storage has, it also has placed. The owner's account (several new piles, every non-fitting tile taken out of each
tray) needs many more take-out writes than storage has. None of them reached it, not even as OUT. The NOT-LETTER pile in his
03:0x screenshot is real: one tile was trashed at 02:59:31, after the 02:54 burst.

## Cause

The page has two ways to lose a choice without the person noticing. Both are in the template's save section
(`tools/sign_sorter/template.html` 2026-10-15.1, published lines 1398-1467 and 2286-2300):

1. **A refused write is dropped after one retry.** `pump()` retries once after 300-800 ms (`attempt(1)`), then puts the path in
   `failedPaths` and never tries again on its own. The change stays only in the page's memory and is gone on reload. In
   db mode nothing is written to the browser: `persistLocal()` is called only in local mode (published line 1439). The only signal is
   the small `.save` line in the bar ("Not saved: N changes … Try again"), and any later note does not clear it. The store's contract
   (`db.d.ts`, runtime 0.2.84) names the likely refusal: `resource_exhausted` covers "the per-viewer call rate … too many concurrent
   writes". The page put no limit on concurrent writes. A step-1 tap writes the move and, for a tile in its pile's outliers, the pile
   too. A placement can write a new pile, a move and a cluster. So a fast sorter sends bursts.
2. **This-browser-only mode is never handed back.** If `claude.use('db')` answers `null` (the runtime gives null after 10 s with no
   answer), the page sets `dbMode = 'local'` (line 2299) and keeps everything in `localStorage['sorter:all']` (`persistLocal`, line
   1467). The label is the same small line ("Storage not connected: changes are kept in this browser only"). On the next load that
   does connect, the db branch never reads `sorter:all` (line 2295 reads it only in the no-db branch). Whatever was sorted in local mode
   stays in that browser and never reaches storage.

Paths checked and ruled out:

- **Writes before storage answers.** `track()` holds them (line 1440), but `notYet()` refuses every move until the saved answers are
  in (template 2026-10-09.5), so nothing piles up in memory while connecting.
- **A snapshot overwriting a local change.** Snapshots for a path in `inflight` are skipped (line 2311). One that arrives after the
  write is confirmed matches it.
- **Doc-key collisions.** `key()` escapes every non-`[A-Za-z0-9_-]` character as `_<code>_`. 'tray A-b' -> 'tray_32_A-b', and the
  sids are already plain, so no two pile names or sids share a document.
- **Moves that skip `saveMove`.** Every assignment to `moves[...]` goes through `saveMove` (`setDest`, `keepAt`, `undo`, the
  snapshot listener).

**Which path hit the owner cannot be proven from storage alone.** The store keeps no log of refused calls, and the page logged
nothing. Two things fit path 1. The writes that landed are 2-4 s apart (slow enough to pass). None of the many take-outs he describes
landed. Path 2 fits a whole session that wrote nothing. Path 2 is the only one that can have left his arrangement anywhere: in his
browser, under `sorter:all`. Path 1 kept the lost changes only in memory, so a reload erased them.

## Recovery

- **Possible only if path 2 happened** in the browser he sorted in. The republished page reads `sorter:all` on load, after the saved
  answers are in. If that copy holds choices storage does not have, a box shows under the bar: "This browser kept N choices that
  storage does not have", with a button **Recover my sort from this browser**. The button lists the recovered piles with their sign
  pictures (no values, no machine guesses). Nothing is written until he presses **Write these to storage**. A choice that differs from
  a document storage already holds (dashed tile) is replaced only if he ticks the box for it; it is unticked by default. The older copy
  is kept in the browser under `sorter:all:recovered:<time>`, not deleted.
- **If no box appears** (or it says "matches storage: nothing to recover"), the lost choices were dropped by path 1 and exist nowhere.
  The sort has to be redone. That is the plain answer; nothing was reconstructed from his description or the screenshot (brief item 5).

## Fix (template 2026-10-20.1, `tools/sign_sorter/template.html`; this page re-rendered on it with `tools/sorter_rerender.py`)

- Every write is confirmed by a read-back (`doc.get()` must return what was written, or the document must be gone after a delete).
  A write that does not read back is retried like a refused one.
- A refused or unconfirmed write is retried by itself with a growing pause (4 s, 8 s, 16 s, then every 30 s) until it lands. Only
  `invalid_argument`, `quota_exceeded`, `revoked` and the lifecycle codes stop the automatic retries; those writes stay "NOT saved"
  with the Try again button.
- At most two writes are in flight at a time (`WMAX`). The rest queue.
- Every change is journaled in this browser at once (`localStorage['sorter:journal']`: the whole arrangement and the paths not yet
  confirmed), in every mode. On the next connected load, a journal with unconfirmed paths, or one written in local mode, is set aside
  and offered by the same Recover box.
- A persistent banner (`#saveBan`, in the sticky bar, glyph + words + border, not hue alone) reads:
  - "⋯ Connecting to storage. Please wait for “All changes saved” before you start." before storage answers;
  - "✕ Storage is not connected: your choices are kept in THIS browser only …" in local mode;
  - "⋯ N changes NOT saved yet: saving…" while any write is pending;
  - "✕ N changes NOT saved (reason). Retrying by itself …" with a **Try again now** button on refusal;
  - "✓ All changes saved (each one read back from storage)." only when nothing is pending.
- **Save my sort** (added 03:3x UTC on the owner's request, relayed by the account-4 parent): a button in the bar, labelled "Save"
  on a phone. It rewrites the whole arrangement (every moved tile, every new pile, verdicts, keeps, clusters and cuts) through the same
  queue and waits until each write has been read back. Then it reads the moves and new-pile collections whole and compares them with the
  page. The line under the bar says "✓ Saved: N tiles in M piles at HH:MM (read back from storage)", or "✕ NOT saved: …" naming the
  count and the first signs or piles that differ (the high-contrast style; dark orange and the cross, not red alone). The store has
  no batch write (`db.d.ts` 0.2.84), so "one batch" is these writes plus the whole-collection read-back. The per-change autosave and
  the banner stay as they are.
- The browser asks before the tab is closed while a write is pending (`beforeunload`).
- The new page no longer writes `sorter:all`. It reads that key, and only for recovery and the local-mode fallback.

## Tests (20 Oct 2026, 03:1x-03:2x UTC, this container)

- `tools/sign_sorter/browser_tests/test_save.js` (new; `mock_db.js` gains `get()` on a document and on a collection, `store.lie(n)` for a dropped write and a
  switchable `store.nullDb`): 26/26 PASS; with the Save my sort checks added (03:4x UTC), 30/30 PASS, and test_qa still ALL PASS (phone bar 118 px). Covers connecting (the banner says wait, a tap moves nothing) -> held -> pumped -> saved
  after read-back; refused -> visible NOT saved + retry -> lands by itself; an unconfirmed read-back is not saved; a burst of 8 taps
  peaks at 2 writes in flight and all land; local mode is labelled, then recovered on confirm; an older page's `sorter:all` is
  recovered and a differing stored doc is kept unless ticked; refused writes from a closed page are offered back.
- `tools/tests/test_sorter_savefix.py` (new, offline; static half + the browser half above): ALL PASS.
- Existing browser tests on the new template: test_qa (incl. its phone toolbar-height check, < 130 px), test_bad, test_undo,
  test_sorter, test_s1_extras, test_ctx, test_focus, test_s2_pilemerge, test_focus_tray and test_r12_r16 all pass.
  test_s2_fix and the region/recut tests could not run here: `make_fixtures.py` needs scipy for region.html, and scipy is not
  installed in this container. That is not a failure of the change.
- `python3 tools/sorter_preflight.py sorter_viv_ksplit.html --cipher-lines cipher_lines.tsv --step1` on the re-rendered page: preflight PASS (with --step1, the same flag as the earlier Vivonne step-1 page, since this page asks no questions; without it, check 2 fails 'focus box empty' by design).
- `tools/cvd_check.py --audit tools/sign_sorter/template.html`: 0 flags (same 24 literals as before; the banner uses existing tokens).

## Republished (20 Oct 2026, 03:25 UTC)

Republished to the same URL (artifact version 2, id 1792466734-3890), with the capability declaration (`db`) carried forward. The
stored documents are untouched: after the publish, the 6 moves, 4 newpiles and 1 piles doc read back exactly as listed above. The
round-trip check ran at access level `interact` through ArtifactData. A `set` of `moves/SAVEFIX-TEST` committed at version 1, a `get`
returned the same body, and the test doc was deleted (if_version 1). The page ignores that id (no such sid) while it exists. This
shows that an interact-level writer can write and read back this artifact's moves collection. It does not drive the page's own code
in the claude.ai viewer, which this session cannot open; the page's save logic is covered by test_save.js against the mock store.

## Stale docs cleared for a fresh sort (03:4x UTC 20 Oct 2026)

The owner chose to redo the sort (relayed by the account-4 parent at 03:0x UTC). Recovery became optional; the Recover box stays on
the page in case his browser kept anything. After the documents were recorded in the table at the top of this file, the 11
partial-sort documents were deleted so the trays open clean: 6 moves, 4 newpiles (tray A-b, B-b, B-c, NOT-LETTER) and 1 piles
(NOT-LETTER). The parent's message named the 6 moves and 3 newpiles from 02:54. The 02:59 NOT-LETTER move, pile and verdict were
cleared with them, since they were part of the same partial sort and would otherwise have left one tile out of tray A.

## Follow-up (not done here)

Every other live sorter page is still on 2026-10-15.1 and has the same two loss paths. `tools/sorter_preflight.py` fails a page built
on an older template, so re-render each live page with `tools/sorter_rerender.py` and republish it to its own URL (read first)
before it next goes to the owner. `tools/live_sorters_check.py` lists them.
