# Estate view and per-project entry, for Windows PowerShell.
# Claude Code runs natively on Windows; PowerShell is its default shell.
#
#   notepad $PROFILE
#   . "$HOME\src\hub\shell\projects.ps1"      # add this line, save, then run  . $PROFILE
#
# Reads shell\projects.conf (copy projects.conf.example).
# NOTE: written on Linux and not executed on Windows. If a line misbehaves, say so and it gets fixed.

$script:HubDir  = Split-Path -Parent $PSScriptRoot
$script:HubConf = Join-Path $PSScriptRoot 'projects.conf'

function Get-HubRows {
  if (-not (Test-Path $script:HubConf)) { Write-Host "no projects.conf yet (copy projects.conf.example)"; return @() }
  Get-Content $script:HubConf |
    Where-Object { $_ -notmatch '^\s*#' -and $_.Trim() } |
    ForEach-Object {
      $p = $_ -split '\|'
      [pscustomobject]@{
        Name = $p[0].Trim()
        Dir  = ($p[1].Trim() -replace '^\$HOME', $HOME)
        Repo = if ($p.Count -gt 3) { $p[3].Trim() } else { '' }
      }
    }
}

function Show-HubBrief([string]$dir) {
  if (-not (Test-Path (Join-Path $dir '.git'))) { Write-Host "  not cloned: $dir" -ForegroundColor DarkGray; return }
  Push-Location $dir
  try {
    git fetch origin main -q 2>$null
    if (Test-Path 'STATUS.md') {
      $line = Select-String -Path 'STATUS.md' -Pattern 'Last updated' | Select-Object -First 1
      if ($line) { Write-Host "  $($line.Line.Trim())" }
    }
    $behind = git rev-list --count HEAD..origin/main 2>$null
    if ($behind -and $behind -ne '0') { Write-Host "  $behind commit(s) behind origin/main" -ForegroundColor Yellow }
    if (Test-Path 'ASKS.md') {
      $open = @(Select-String -Path 'ASKS.md' -Pattern '\| open \|').Count
      if ($open -gt 0) {
        Write-Host "  open asks: $open" -ForegroundColor Yellow
        Select-String -Path 'ASKS.md' -Pattern '\| open \|' | Select-Object -First 3 | ForEach-Object {
          $f = $_.Line -split '\|'
          if ($f.Count -gt 4) { Write-Host "    - $($f[4].Trim())" -ForegroundColor DarkGray }
        }
      }
    }
  } finally { Pop-Location }
}

function estate {
  foreach ($p in Get-HubRows) {
    Write-Host ""
    Write-Host $p.Name -ForegroundColor Cyan -NoNewline
    Write-Host "  $($p.Repo)" -ForegroundColor DarkGray
    Show-HubBrief $p.Dir
  }
  Write-Host ""
}

function asks {
  foreach ($p in Get-HubRows) {
    $f = Join-Path $p.Dir 'ASKS.md'
    if (-not (Test-Path $f)) { continue }
    Select-String -Path $f -Pattern '\| open \|' | ForEach-Object {
      $c = $_.Line -split '\|'
      if ($c.Count -gt 5) { "{0,-12} {1} -> {2}" -f $p.Name, $c[4].Trim(), $c[5].Trim() }
    }
  }
}

function go {
  param([Parameter(Mandatory)][string]$Project, [Parameter(ValueFromRemainingArguments)]$Rest)
  $match = Get-HubRows | Where-Object { $_.Name -ieq $Project } | Select-Object -First 1
  if (-not $match) {
    Write-Host "unknown project: $Project" -ForegroundColor Red
    Write-Host "known:"; Get-HubRows | ForEach-Object { Write-Host "  $($_.Name)" }
    return
  }
  $Host.UI.RawUI.WindowTitle = "[$($match.Name)]"
  Set-Location $match.Dir
  git fetch origin main -q; git rebase FETCH_HEAD -q 2>$null
  if (Test-Path 'STATUS.md') { Get-Content 'STATUS.md' -TotalCount 16 }
  Write-Host ""; Show-HubBrief $match.Dir; Write-Host ""
  if (Test-Path 'ROOM.md') {
    Write-Host "  last room lines:" -ForegroundColor DarkGray
    Get-Content 'ROOM.md' -Tail 3 | ForEach-Object { Write-Host "    $_" -ForegroundColor DarkGray }
    Write-Host ""
  }
  claude @Rest
  $Host.UI.RawUI.WindowTitle = "PowerShell"
}

function hubnew {
  param([Parameter(ValueFromRemainingArguments)]$Idea)
  Set-Location $script:HubDir
  $Host.UI.RawUI.WindowTitle = "[HUB]"
  claude "Run NEW-PROJECT.md for this idea: $($Idea -join ' ')"
  $Host.UI.RawUI.WindowTitle = "PowerShell"
}
