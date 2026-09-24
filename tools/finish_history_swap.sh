#!/usr/bin/env bash
# After the owner has swapped main for the purged rewrite (tools/purge_history.sh): carry over any commits that
# landed on the OLD main after the rewrite was cut, then reset this clone. Cherry-picks work across the two
# histories because the rewrite kept every tree identical; a rebase would not (no common ancestor).
#
# Usage: tools/finish_history_swap.sh <old-snapshot-commit> <old-tip-commit>
#   old-snapshot-commit: the old-main commit the rewrite was cut from (tools/purge_history.sh prints it)
#   old-tip-commit:      the last commit on old main before the swap (this clone's last fetched origin/main)
# Both must be present in this clone's object store (they are, if this clone fetched them before the swap).
set -euo pipefail
SNAP=${1:?old snapshot commit}; TIP=${2:?old tip commit}
git fetch -q origin main
NEWROOT=$(git rev-list --max-parents=0 origin/main | head -1)
OLDROOT=$(git rev-list --max-parents=0 "$TIP" | head -1)
[ "$NEWROOT" != "$OLDROOT" ] || { echo "origin/main still has the old root $OLDROOT; the swap has not happened. Nothing done."; exit 2; }
git merge-base --is-ancestor "$SNAP" "$TIP" || { echo "snapshot $SNAP is not an ancestor of tip $TIP"; exit 1; }
git stash -q --include-untracked || true
git checkout -q --detach origin/main
n=0
for c in $(git rev-list --reverse "$SNAP".."$TIP"); do
  if git cherry-pick -x --allow-empty "$c" >/dev/null 2>&1; then n=$((n+1)); else
    echo "cherry-pick of $c failed; resolving by taking its tree"; git cherry-pick --abort || true
    git read-tree -u -m "$c^{tree}" && git commit -q -C "$c" --allow-empty; n=$((n+1)); fi
done
git branch -f main HEAD && git checkout -q main && git branch -q -u origin/main main
git push -q origin main
git stash pop -q 2>/dev/null || true
echo "carried $n commits ($SNAP..$TIP) onto the purged main and pushed; this clone now tracks the new history"
