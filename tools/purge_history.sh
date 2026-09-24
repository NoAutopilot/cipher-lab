#!/usr/bin/env bash
# One-time history purge for the public repository (owner's decision, 23 Sept 2026; CLAUDE.md, Git section).
# Rewrites a fresh clone of origin/main so that no commit carries: any Gmail address, the owner's first name
# (except an "et al." editor citation that happens to share it), the per-variable credential-length line of 21 Sept 2026, or the
# restricted images removed on 23 Sept 2026 (BL Randolph 1569 leaf and crops, Spink 1812 photographs, KHA 1572 leaves).
# It never touches origin: it writes the rewritten history to a scratch clone and pushes it to the branch named in
# $2 (default purged-main). Swapping that branch in for main is a separate, deliberate step (see the usage note).
#
# Usage: tools/purge_history.sh <scratch-dir> [branch-name]
# Needs: git >= 2.22 and git-filter-repo (pip install git-filter-repo).
set -euo pipefail
SC=${1:?scratch dir}; BR=${2:-purged-main}
SRC=$(git rev-parse --show-toplevel)
REMOTE=$(git -C "$SRC" remote get-url origin)
R=$(mktemp); chmod 600 "$R"; trap 'rm -f "$R"' EXIT

rm -rf "$SC"; git clone -q --no-local "$SRC" "$SC"
git -C "$SC" remote set-url origin "$REMOTE"
git -C "$SC" fetch -q origin main && git -C "$SC" reset -q --hard origin/main

TREE_BEFORE=$(git -C "$SC" rev-parse 'origin/main^{tree}')

# Replacement rules, built at run time so no address is written into the repository.
S=$(git -C "$SC" rev-list --all | tr '\n' ' ')
N="R"; N="${N}yan"   # the first name, assembled so this file never carries it and is not rewritten itself
{ git -C "$SC" grep -o -h -i -E '[a-z0-9._+-]+@gmail\.com' $S 2>/dev/null | sort -u | sed 's/$/==>[address removed 23 Sept 2026]/'
  printf '%s\n' "regex:\b${N}'s\b==>the owner's" \
                "regex:\b${N}\b(?! et al)==>the owner" \
                "regex:DECODE_USER\|[0-9]+\|[^\n]*==>[per-variable lengths redacted 23 Sept 2026 when the repository went public]"
} > "$R"

( cd "$SC" && git filter-repo --force --quiet --replace-text "$R" --replace-message "$R" \
    --invert-paths \
    --path ciphers/randolph-sussex-1569/images/crops \
    --path ciphers/randolph-sussex-1569/images/img \
    --path-glob 'ciphers/wellington-maitland-1812/images/*.jpg' \
    --path ciphers/orange-nassau-1572/images/kha_original_leaf1.png \
    --path ciphers/orange-nassau-1572/images/kha_original_leaf3.png )

# Verification: nothing sensitive in any revision, and the rewritten tip has the same tree as origin/main.
S2=$(git -C "$SC" rev-list --all | tr '\n' ' ')
X=':!tools/purge_history.sh'   # this script names the patterns it removes
fail=0
[ "$(git -C "$SC" grep -c -i '@gmail.com' $S2 -- "$X" 2>/dev/null | wc -l)" = 0 ] || { echo "FAIL: address survives"; fail=1; }
[ "$(git -C "$SC" grep -h -w "$N" $S2 -- "$X" 2>/dev/null | grep -v "$N et al" | wc -l)" = 0 ] || { echo "FAIL: name survives"; fail=1; }
[ "$(git -C "$SC" grep -c 'DECODE_USER|' $S2 -- "$X" 2>/dev/null | wc -l)" = 0 ] || { echo "FAIL: length line survives"; fail=1; }
[ "$(git -C "$SC" rev-parse 'HEAD^{tree}')" = "$TREE_BEFORE" ] || { echo "FAIL: tree differs from origin/main as fetched"; fail=1; }
[ $fail = 0 ] || exit 1
echo "rewritten: $(git -C "$SC" rev-list --all | wc -l) commits, tip $(git -C "$SC" rev-parse --short HEAD), tree identical to origin/main as fetched"

git -C "$SC" remote add origin "$REMOTE"
git -C "$SC" push -q -u origin "HEAD:refs/heads/$BR"
echo "pushed to origin/$BR. To make it main (owner only, at a quiet moment, after every open worker has pushed):"
echo "  GitHub: Settings > General > Default branch > $BR; Branches > delete main; rename $BR to main."
echo "  Or locally: git push --force origin origin/$BR:main   (then every clone: git fetch origin && git reset --hard origin/main)"
echo "GitHub keeps the old commits reachable by hash until its support team purges them; ask them once the swap is done."
