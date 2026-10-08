# LANE SIG (standing; account 1 beside LANE LEDGER; self-refilling). Read `.claude/briefs/lane-common-blast.md` first.

Owner, 8 Oct 2026: "we can do both? We have usage." -- keep the ledgers going AND push where significance is likelier.
research/SIGNIFICANCE-2026-10-08.md (adversarial review of all 68 counted rows: 0 notable, 7 useful detail, 61 routine) says
the better odds are letters where the cipher carried the political content, a key is in hand, and no period decipherment
survives. This lane works only those, ordered by that report, and judges every result by what it adds, not by count.
Start from the newest "LANE SIG handoff" in STATUS.md.

## Targets, in order (skip any a live ROOM claim holds; prior-work-step.md checks 1-4 before any transcription)
1. august-van-saksen-1561-64 -- further cipher enclosures between August of Saxony and William of Orange, 1561-64 (WVO letters
   with cipher and no period decipherment), under the key rebuilt from the period decipherments of WVO 74, 98, 153, 175; WVO 57
   is the model (N4). Huygens WVO host: one worker at a time, >= 2 s.
2. baluze167-davaux-1637 -- further cipher passages in the d'Avaux and Chavigny letters in the Baluze volumes, Tomokiyo's
   published letter table; f.228r-v first (provisional decode failed fr17 at -0.993; transcription is the limit), then other
   leaves whose images are ON DISK. Gallica: one probe per incarnation, no retries (403 to every cloud session on 8 Oct).
3. fr2980-gramont -- f.30r-v, Gramont's all-cipher letter to Francis I, 20 May 1530 (probably the separate "article" on
   Florence the covering letter names), reads only in fragments under the Tomokiyo/Lasry 1530 key: a better transcription from
   the images on disk, then decode with --check and a matched control.
4. lodewijk-van-nassau-1573-74 -- letter 4612 (unread) and code 146 in WVO 5797, with the family keys in hand (key_full_v2,
   key_5801), controls first.
5. Checks the report says are owed on its top items (route to the account-3 VERIFY lane as AUD rows, do not audit here):
   Chavigny 1640 -- the AAE Correspondance politique and the Hessian-side editions; E146 -- Lee (2011) on the Louisville &
   Nashville; then any new reading this lane produces.

## For every reading this lane produces
- Solver: report what was found and where it was not found; per-token grades; decode script with --check; matched control
  that can fail differently (rule 3). Then a SEPARATE first verifier (N-class, depth) and, at N3+ D2+, an AUD2 row for account 3.
- Plus one line in research/SIGNIFICANCE-2026-10-08.md's appendix (append a section "Lane SIG additions"): what the passage says,
  what it adds beyond print, the caveat -- written by the verifier, not the solver, in rule-10 wording.

## Self-refill (account 1 has a dispatcher, but its blast row points at lane-ledger.md)
At close, while it is before 10 Oct 2026 18:00 UTC and any target above still has an untried step, add the next row
(`python3 tools/work_queue.py --add SIG-<n+1> --account account-1 --brief .claude/briefs/lane-significance.md --model "Opus 5.5"
--cap 60 --box 600 --note "self-refill from SIG-<n>"`) and push; the account-1 dispatcher spawns it at its next firing.
