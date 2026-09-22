# Running Claude Code on Windows

Written 22 September 2026, after setting up three accounts on one Windows 10 machine.
Everything here was learned the hard way; follow it and the setup takes ten minutes
instead of two hours.

## One-time setup

### 1. Use PowerShell, not Command Prompt

Press the Windows key, type `powershell`, press Enter. Do **not** open `cmd`.

| Prompt | Shell | Works? |
|---|---|---|
| `C:\Users\you>` | Command Prompt | no — `$HOME`, `$PROFILE` and the wrappers are all PowerShell |
| `PS C:\Users\you>` | PowerShell | yes |

If you land in Command Prompt anyway, type `powershell` and press Enter.

### 2. Create the profile

A PowerShell "profile" is a file that runs every time a shell starts. On a fresh
machine neither the file nor its folder exists, so create both:

    New-Item -ItemType File -Path $PROFILE -Force

### 3. Add one wrapper per account

Write the first one with `Set-Content` and every one after it with `Add-Content`.
`Set-Content` overwrites; using it twice silently destroys the first account's wrapper.

    Set-Content $PROFILE 'function claude-work { $env:CLAUDE_CONFIG_DIR = "$HOME\.claude-work"; claude @args; Remove-Item Env:\CLAUDE_CONFIG_DIR }'
    Add-Content $PROFILE 'function claude-three { $env:CLAUDE_CONFIG_DIR = "$HOME\.claude-three"; claude @args; Remove-Item Env:\CLAUDE_CONFIG_DIR }'

Then reload: `. $PROFILE` (period, space, `$PROFILE`).

Do not edit the profile in Notepad. Notepad saves failed silently here twice; the
one-line `Set-Content`/`Add-Content` form has never failed.

The function name is a label you pick. The folder name is what actually separates the
accounts, and it must be unique per account. Name both after the person, not `three`.

### 4. Sign each one in

Run the wrapper (`claude-work`). Because its config folder starts empty it runs the
first-run wizard and asks for a login method. Pick 1 for a subscription account.

If the browser does not open, the terminal prints a URL and the hint `(c to copy)`.
Press `c`, paste into a browser, sign in, copy the authorization code the page returns,
and right-click in the terminal to paste it back.

**Use an incognito window** if the browser already holds another Claude session, or the
sign-in silently reconnects the account you already have.

## The console traps

These cost hours. All of them are the old Windows console (`conhost`), not Claude Code.

**Ctrl+V does nothing. Right-click pastes.** No clicking into position first — the
console has no click-to-place cursor.

**Left-clicking freezes the window.** A left-click or drag puts the console into
selection mode and *all keyboard input stops*. The tell is the title bar: it changes
from `claude` to **`Select claude`**. Press **Esc** to get out. Never left-click inside
the window.

**Pastes join lines together.** Multi-line pastes arrive as `--versionmkdir` or
`claudedir`. Paste one line at a time, or just type short commands by hand — `read
ASKS.md` is twelve characters and beats any paste.

**Permanent fixes**, in increasing order of how much they help:
- Title bar → Properties → Options → tick "Use Ctrl+Shift+C/V as Copy/Paste". Note the
  **Shift**; plain Ctrl+V never works here.
- Use **Windows Terminal** instead (Start → `terminal`). Plain Ctrl+V works, pastes
  arrive intact, and you get named tabs so you can label one MAIN and one BIZ.

## Daily use

Claude Code only sees the folder you start it from. Starting it in your home folder
gives you a session that knows nothing about the project.

    cd $HOME\cipher-lab
    claude

Header should read `~\cipher-lab`. That is the check.

For another account, same two lines with its wrapper on the second.

## Telling the accounts apart

Three checks, weakest to strongest:

    Get-Content $PROFILE                              # which accounts are configured
    Get-ChildItem $HOME\.claude*\.credentials.json    # which have credentials on disk
    /status                                           # inside a session: the actual email

Only the third is conclusive. A credentials file can exist and be a dead stub — ours was
524 bytes and the account was not signed in. The reliable signal at launch:

| First two seconds | Meaning |
|---|---|
| straight to the Claude interface | connected |
| "Select login method" | **not** connected, whatever the files say |

## What this does and does not give you

It gives each person their own login, their own rate-limit window, and their own
sessions, all on one machine, all able to reach this repository.

It does **not** connect the accounts to each other. No account can see or start another
account's sessions — that is a hard wall, not a gap in the setup. Coordination is
pull-based through `hub-seed/ASSIGNMENTS.md`: one orchestrator writes a row, another
account picks it up on its own next wake. A shared queue, never a dispatcher.
