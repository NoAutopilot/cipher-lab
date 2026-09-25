to: github.com/NoAutopilot/cipher-lab, Settings and Branches pages (four clicks, no email)
subject: History swap: make the purged rewrite the main branch
checked: 24 Sept 2026, orchestrator. Branch purged-main-2 verified by tools/purge_history.sh: same files as main at 9866425, 259 commits, no addresses, no first name, no credential-length line, no BL/Spink/KHA images in any commit. Sessions cannot force-push or delete branches under their permission policy, so this part is yours.
status: dropped 25 Sept 2026 (owner: no purge needed; no secrets in history)

# Your four clicks (any time; no need to wait for a quiet moment)

Tick the box when done. The next orchestrator check-in sees the new root, runs tools/finish_history_swap.sh to carry over anything pushed after 9866425, and writes "swap done" in ROOM.md.

## Text
1. github.com/NoAutopilot/cipher-lab > Settings > General > Default branch > switch to purged-main-2.
2. Branches page: delete main, purged-main, and preserve/f1fe9b1-unrelated-local-history-2026-09-23.
3. Rename purged-main-2 to main.
4. Later, optional: ask GitHub support to purge unreachable commits from the repository (they keep old commits reachable by hash until asked).
