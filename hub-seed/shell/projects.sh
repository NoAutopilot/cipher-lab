#!/usr/bin/env bash
# Estate view and per-project entry. Source this from ~/.zshrc or ~/.bashrc:
#   source ~/src/hub/shell/projects.sh
# Reads shell/projects.conf (see projects.conf.example).

HUB_DIR="${HUB_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")/.." && pwd)}"
HUB_CONF="$HUB_DIR/shell/projects.conf"

_hub_rows() { [[ -f "$HUB_CONF" ]] && grep -v '^\s*#' "$HUB_CONF" | grep -v '^\s*$'; }

_proj_pre() {
  printf '\e]2;[%s]\a' "$1"
  if [[ -n "$TMUX" ]]; then
    tmux set-option status-style "bg=$2,fg=white" 2>/dev/null
    tmux set-option status-right " #[bold]$1#[default] | %H:%M " 2>/dev/null
  fi
}
_proj_post() {
  printf '\e]2;\a'
  if [[ -n "$TMUX" ]]; then
    tmux set-option -u status-style 2>/dev/null
    tmux set-option -u status-right 2>/dev/null
  fi
}

_hub_brief() {   # one project's state, from its files
  local d="$1"
  [[ -d "$d/.git" ]] || { echo "  not cloned: $d"; return; }
  ( cd "$d" || return
    git fetch origin main -q 2>/dev/null
    local behind; behind=$(git rev-list --count HEAD..origin/main 2>/dev/null || echo 0)
    grep -m1 'Last updated' STATUS.md 2>/dev/null | sed 's/^/  /'
    [[ "$behind" != "0" ]] && echo "  $behind commit(s) behind origin/main"
    local asks; asks=$(grep -c '| open |' ASKS.md 2>/dev/null || echo 0)
    [[ "$asks" != "0" ]] && echo "  open asks: $asks"
    grep -m3 '| open |' ASKS.md 2>/dev/null | awk -F'|' '{print "    -"$5}' )
}

estate() {        # everything, without entering anything
  local name dir color repo
  while IFS='|' read -r name dir color repo; do
    dir="${dir/#\$HOME/$HOME}"
    printf '\n\033[1m%s\033[0m  %s\n' "$name" "$repo"
    _hub_brief "$dir"
  done < <(_hub_rows)
  echo
}

asks() {          # every open ask, across every project
  local name dir color repo
  while IFS='|' read -r name dir color repo; do
    dir="${dir/#\$HOME/$HOME}"
    [[ -f "$dir/ASKS.md" ]] || continue
    grep '| open |' "$dir/ASKS.md" | awk -F'|' -v p="$name" '{printf "%-12s %s -> %s\n", p, $5, $6}'
  done < <(_hub_rows)
}

go() {            # go <PROJECT> [args to claude]
  local want="$1"; shift || true
  local name dir color repo
  while IFS='|' read -r name dir color repo; do
    dir="${dir/#\$HOME/$HOME}"
    if [[ "${name,,}" == "${want,,}" ]]; then
      _proj_pre "$name" "$color"
      cd "$dir" || { _proj_post; return 1; }
      git fetch origin main -q && git rebase FETCH_HEAD -q 2>/dev/null
      sed -n '1,16p' STATUS.md 2>/dev/null
      echo; _hub_brief "$dir"; echo
      [[ -f ROOM.md ]] && { echo "  last room lines:"; tail -3 ROOM.md | sed 's/^/    /'; echo; }
      command claude "$@"
      _proj_post
      return
    fi
  done < <(_hub_rows)
  echo "unknown project: $want"; echo "known:"; _hub_rows | cut -d'|' -f1 | sed 's/^/  /'
}

hubnew() {        # hubnew "one sentence idea"
  cd "$HUB_DIR" || return 1
  _proj_pre "HUB" "#3a1e5f"
  command claude "Run NEW-PROJECT.md for this idea: $*"
  _proj_post
}
