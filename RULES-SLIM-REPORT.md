# RULES-SLIM report (5 Oct 2026, account 3 worker)

Brief: `.claude/briefs/runs/2026-10-05-acct3-rules-slim.md`. Nothing is swapped in yet: CLAUDE.md is unchanged.

## Sizes

| File | Bytes | Approx. tokens (bytes / 4) |
|---|---|---|
| CLAUDE.md now (loads into every session) | 119,247 | ~30,000 |
| CLAUDE-SLIM.md (proposed CLAUDE.md) | 14,067 | ~3,500 |
| RULEBOOK-FULL.md (current CLAUDE.md verbatim + ids + R0 note; not auto-loaded) | ~121,000 | read on demand |
| docs/HOSTS.md (host table, copied from ACC.hosts; not auto-loaded) | 18,906 | read on demand |

Saving: about 26,000 tokens of fixed context per session and per subagent that loads CLAUDE.md, before any work.

## What was done

- 154 rule ids (`[R0]`, `[R1]` ... `[R3.a]`-`[R3.m]`, `[R4a]`, `[OUT.0]`-`[OUT.8]`, `[OPS.*]`, `[PIPE.*]`, `[COL.*]`,
  `[WRK.*]`, `[USE.*]`, `[ACC.*]`, `[IMP.*]`, `[GIT.*]`, `[L.*]`, `[INTRO]`) tag every rule and clause in both files.
  RULEBOOK-FULL.md is byte-for-byte CLAUDE.md once the tags and the top note are stripped (checked by script).
- `tools/rules_sync_check.py` (+ `tools/tests/test_rules_sync_check.py`, 6 offline tests pass): exit 1 when an id is in
  one file only or tagged twice; wording changes inside an id never block. Today:
  `python3 tools/rules_sync_check.py --slim CLAUDE-SLIM.md` -> "in sync: 154 rule ids in both files". Added to SYSTEM.md.
- Kept verbatim or near-verbatim in the slim copy: credential handling (ACC.3, ACC.3.i never-list), status vocabulary
  (R5), grade letters (R4), N0-N5 (R10) and D0-D4 with outward wording (R4a), outreach gates 1-8, git rules,
  personal-data rules (R9, R9a), good-citizen rule (ACC.5).

## Compressed, but you may want them verbose (listed, not dropped)

1. **Story pointers.** The brief asked for "story: RULEBOOK-FULL.md#R3.c" on each rule; at 154 ids that alone is ~5 KB,
   so the slim file states the convention once at the top ("search the id in RULEBOOK-FULL.md"). Easy to add per line
   if you prefer; the size goes to about 19 KB.
2. **Verifier brief template (WRK.4)** is a pointer to RULEBOOK-FULL.md#WRK.4, not inlined (~2.5 KB). Orchestrators
   writing a verifier brief must open the full file. Inline it if verifier briefs are written often.
3. **Gate tool list (USE.8a.b)** and **host recipes (ACC.1.a-c, ACC.3.c-h)** are one-liners pointing at the full text.
4. **R3.a-R3.m** (thirteen control lessons) are one clause each; the reasoning that makes them applicable is in the full file.
5. **ACC.3.j/k/l** (duplicate OpenAlex/S2/Google Books key notes in the original) are folded into ACC.3.a-b.
6. **Host table** moved to docs/HOSTS.md and also stays in RULEBOOK-FULL.md: two copies to keep in step by hand
   (rules_sync_check does not compare table contents).

## How to swap (the parent does it, after your approval)

    git mv -f CLAUDE-SLIM.md CLAUDE.md      # replaces the 119 KB file
    python3 tools/rules_sync_check.py       # must print "in sync"
    git commit -m "rules: slim CLAUDE.md (RULES-SLIM)" CLAUDE.md CLAUDE-SLIM.md

After the swap, every rule edit (retro-apply jobs, lessons) touches both files in one commit; retrospective and
retro-apply briefs should name `tools/rules_sync_check.py` as a pre-push check.
