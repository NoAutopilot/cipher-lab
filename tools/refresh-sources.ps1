# Re-download the Cryptiana index page and show what changed since the last snapshot.
# Run from the repo root in PowerShell:  .\tools\refresh-sources.ps1
# Then commit if the diff is real:       git add sources; git commit -m "Refresh Cryptiana snapshot"

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$web  = Join-Path $root "sources\cryptiana\web"
$blog = Join-Path $root "sources\cryptiana\blog"

$pages = @(
  @{ url = "https://cryptiana.web.fc2.com/code/unsolved.htm"; out = Join-Path $web "unsolved.htm" },
  @{ url = "https://cryptiana.blogspot.com/";                 out = Join-Path $blog "index.html" }
)

foreach ($p in $pages) {
  Write-Host "Fetching $($p.url)"
  curl.exe -s -L -o $p.out $p.url
  Start-Sleep -Milliseconds 500
}

Write-Host ""
Write-Host "Changed files:"
git -C $root status --short sources/
Write-Host ""
Write-Host "Headings added or removed on unsolved.htm (Solved markers move here):"
git -C $root diff --unified=0 -- sources/cryptiana/web/unsolved.htm |
  Select-String -Pattern '^[+-].*<H[234]>' -CaseSensitive:$false |
  ForEach-Object { $_.Line -replace '<[^>]+>', '' }
