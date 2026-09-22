# A rudimentary launcher: pick a project and an account, get a session in the right place.
#
#   powershell -STA -File launcher.ps1
#
# Or double-click launcher.cmd, which does the same.
#
# Projects come from shell\projects.conf when it exists, otherwise from a scan of your home
# folder for git repositories. Accounts come from the wrapper functions in your PowerShell
# profile, so a wrapper you add there appears here with no edit to this file.
#
# NOTE: written on Linux and not executed on Windows. If a line misbehaves, say so and it
# gets fixed rather than worked around.

Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$ConfPath = Join-Path $PSScriptRoot 'projects.conf'

# ---------------------------------------------------------------- discovery

function Get-Projects {
  $rows = @()
  if (Test-Path $ConfPath) {
    foreach ($line in Get-Content $ConfPath) {
      if ($line -match '^\s*#' -or -not $line.Trim()) { continue }
      $p = $line -split '\|'
      $dir = ($p[1].Trim() -replace '^\$HOME', $HOME) -replace '/', '\'
      $rows += [pscustomobject]@{ Name = $p[0].Trim(); Dir = $dir }
    }
  }
  if (-not $rows) {
    # No config: anything in the home folder that is a git repository.
    foreach ($d in Get-ChildItem -Path $HOME -Directory -ErrorAction SilentlyContinue) {
      if (Test-Path (Join-Path $d.FullName '.git')) {
        $rows += [pscustomobject]@{ Name = $d.Name; Dir = $d.FullName }
      }
    }
  }
  $rows
}

function Get-Accounts {
  # 'claude' is the default config folder. Everything else is a wrapper in the profile.
  $rows = @([pscustomobject]@{ Name = 'claude'; Note = 'main account' })
  if (Test-Path $PROFILE) {
    foreach ($line in Get-Content $PROFILE) {
      if ($line -match 'function\s+(claude-[A-Za-z0-9_-]+)') {
        $fn = $Matches[1]
        $folder = ''
        if ($line -match 'CLAUDE_CONFIG_DIR\s*=\s*"([^"]+)"') { $folder = Split-Path -Leaf $Matches[1] }
        $rows += [pscustomobject]@{ Name = $fn; Note = $folder }
      }
    }
  }
  $rows
}

function Get-Marks([string]$dir) {
  # One short line per project: uncommitted work, and whether the branch is behind.
  if (-not (Test-Path (Join-Path $dir '.git'))) { return 'not a repository' }
  $bits = @()
  $dirty = @(git -C $dir status --porcelain 2>$null).Count
  if ($dirty -gt 0) { $bits += "$dirty uncommitted" }
  $behind = git -C $dir rev-list --count 'HEAD..@{u}' 2>$null
  if ($behind -and $behind -ne '0') { $bits += "$behind behind" }
  $asks = Join-Path $dir 'ASKS.md'
  if (Test-Path $asks) {
    $open = @(Select-String -Path $asks -Pattern '\| open \|' -ErrorAction SilentlyContinue).Count
    if ($open -gt 0) { $bits += "$open open asks" }
  }
  if ($bits) { $bits -join ' | ' } else { 'clean' }
}

# ---------------------------------------------------------------- window

$projects = @(Get-Projects)
$accounts = @(Get-Accounts)

$form = New-Object System.Windows.Forms.Form
$form.Text = 'Launcher'
$form.Size = New-Object System.Drawing.Size(760, 460)
$form.StartPosition = 'CenterScreen'

$lblP = New-Object System.Windows.Forms.Label
$lblP.Text = 'Project'; $lblP.Location = '20,15'; $lblP.AutoSize = $true
$form.Controls.Add($lblP)

$lstP = New-Object System.Windows.Forms.ListBox
$lstP.Location = '20,38'; $lstP.Size = New-Object System.Drawing.Size(420, 240)
foreach ($p in $projects) { [void]$lstP.Items.Add($p.Name) }
if ($lstP.Items.Count) { $lstP.SelectedIndex = 0 }
$form.Controls.Add($lstP)

$lblA = New-Object System.Windows.Forms.Label
$lblA.Text = 'Account'; $lblA.Location = '460,15'; $lblA.AutoSize = $true
$form.Controls.Add($lblA)

$lstA = New-Object System.Windows.Forms.ListBox
$lstA.Location = '460,38'; $lstA.Size = New-Object System.Drawing.Size(260, 240)
foreach ($a in $accounts) {
  $label = if ($a.Note) { "$($a.Name)   ($($a.Note))" } else { $a.Name }
  [void]$lstA.Items.Add($label)
}
if ($lstA.Items.Count) { $lstA.SelectedIndex = 0 }
$form.Controls.Add($lstA)

$status = New-Object System.Windows.Forms.Label
$status.Location = '20,290'; $status.Size = New-Object System.Drawing.Size(700, 40)
$form.Controls.Add($status)

function Update-Status {
  $i = $lstP.SelectedIndex
  if ($i -lt 0) { $status.Text = ''; return }
  $p = $projects[$i]
  $status.Text = "$($p.Dir)`r`n$(Get-Marks $p.Dir)"
}
$lstP.Add_SelectedIndexChanged({ Update-Status })

function Selected-Project { if ($lstP.SelectedIndex -ge 0) { $projects[$lstP.SelectedIndex] } }
function Selected-Account { if ($lstA.SelectedIndex -ge 0) { $accounts[$lstA.SelectedIndex].Name } }

function New-Button([string]$text, [string]$loc, [int]$width, [scriptblock]$onClick) {
  $b = New-Object System.Windows.Forms.Button
  $b.Text = $text; $b.Location = $loc
  $b.Size = New-Object System.Drawing.Size($width, 34)
  $b.Add_Click($onClick)
  $form.Controls.Add($b)
  $b
}

$btnGo = New-Button 'Open session' '20,345' 160 {
  $p = Selected-Project; $a = Selected-Account
  if (-not $p -or -not $a) { return }
  Start-Process powershell -ArgumentList '-NoExit', '-Command',
    "Set-Location -LiteralPath '$($p.Dir)'; Write-Host '$($p.Name) / $a' -ForegroundColor Cyan; $a"
}
$btnGo.Font = New-Object System.Drawing.Font($btnGo.Font, [System.Drawing.FontStyle]::Bold)

[void](New-Button 'Shell here' '190,345' 120 {
  $p = Selected-Project
  if ($p) { Start-Process powershell -ArgumentList '-NoExit', '-Command', "Set-Location -LiteralPath '$($p.Dir)'" }
})

[void](New-Button 'Open folder' '320,345' 120 {
  $p = Selected-Project
  if ($p) { Start-Process explorer.exe $p.Dir }
})

[void](New-Button 'ASKS.md' '450,345' 110 {
  $p = Selected-Project
  if (-not $p) { return }
  $f = Join-Path $p.Dir 'ASKS.md'
  if (Test-Path $f) { Start-Process notepad.exe $f }
  else { [System.Windows.Forms.MessageBox]::Show('No ASKS.md in this project.') | Out-Null }
})

[void](New-Button 'Refresh' '570,345' 110 { Update-Status })

Update-Status
[void]$form.ShowDialog()
