#!/usr/bin/env python3
"""Key probe: which credential variables this container carries, by NAME only, against KEYS.md, the register.

Usage:
  tools/key_probe.py              print present / documented-but-unset / present-but-undocumented names
  tools/key_probe.py --quiet      one line (tools/room.py --start prints it)
  tools/key_probe.py --sync       also update KEYS.md: a `requested` row whose name is now set becomes `set`, every
                                  present row records this account and time in `seen`, a present name with no row
                                  gets one marked "undocumented (document before use)". Prints "KEY NOW SET: NAME"
                                  per newly set requested key and "KEY UNDOCUMENTED: NAME" per new row; exit 0.
                                  Does not commit; room.py --start commits and announces in ROOM.md.
  tools/key_probe.py --help

Why (owner, 25 Sept 2026, about 22:40 UTC): secrets added to one account's environment for a worker there were missed
by the other account's sessions, and nothing told an agent that a key it had asked for had been added. KEYS.md is the
register; this probe is the check; room.py --start is the announcement. A variable added after a session started is
invisible to that session, and the two accounts' environments are configured separately, so a key is added on both.
This script reads names only: it never prints, logs or compares a value (CLAUDE.md access playbook, handling rule).
The account label comes from CIPHERLAB_ACCOUNT (`ytbiz` or `owner`); until the owner sets it the probe still flips
requested rows and adds undocumented ones but writes nothing to `seen`, since it cannot say which account saw the key.
"""
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEYS = os.path.join(ROOT, "KEYS.md")
PATTERN = re.compile(r"(KEY|USER|PASS|TOKEN|SECRET|CLIENT_ID|CREDENTIAL|_ACCOUNT$)", re.I)
# Platform and shell variables that match the pattern but are not the owner's service credentials.
IGNORE = re.compile(r"^(USER|LOGNAME|USERNAME|GH_TOKEN|GITHUB_TOKEN|MAX_THINKING_TOKENS|GIT_CONFIG_|CLAUDE_|ANTHROPIC_|CCR_|NODE_|NPM_|SSH_|SUDO_|XDG_)")


def read_register(path=KEYS):
    """Return (header_lines, rows) where each row is a dict with the six columns, plus the raw line index."""
    lines = open(path, encoding="utf-8").read().split("\n")
    rows = []
    for i, l in enumerate(lines):
        if l.startswith("| ") and not l.startswith("| name") and not l.startswith("|---"):
            c = [x.strip() for x in l.strip().strip("|").split("|")]
            if len(c) >= 6:
                rows.append({"i": i, "name": c[0], "purpose": c[1], "tool": c[2], "requested": c[3], "status": c[4], "seen": c[5]})
    return lines, rows


def row_line(r):
    return f"| {r['name']} | {r['purpose']} | {r['tool']} | {r['requested']} | {r['status']} | {r['seen']} |"


def present_names(env):
    return sorted(n for n in env if PATTERN.search(n) and not IGNORE.match(n) and env.get(n))


def probe(environ=None, path=KEYS):
    env = os.environ if environ is None else environ
    present = present_names(env)
    _, rows = read_register(path)
    documented = [r["name"] for r in rows]
    documented_unset = [n for n in documented if not env.get(n)]
    undocumented = [n for n in present if n not in documented]
    return present, documented_unset, undocumented


def sync(environ=None, path=KEYS, account=None, now=None):
    """Update the register in place. Returns (newly_set, new_undocumented)."""
    env = os.environ if environ is None else environ
    account = account or env.get("CIPHERLAB_ACCOUNT") or "unlabelled"
    now = now or time.strftime("%Y-%m-%dT%H:%M", time.gmtime())
    lines, rows = read_register(path)
    present = set(present_names(env))
    newly_set, new_undoc, changed = [], [], False
    for r in rows:
        if r["name"] in present:
            if r["status"] == "requested":
                r["status"] = "set"; newly_set.append(r["name"]); changed = True
            if account != "unlabelled" and not re.search(rf"(^|,\s*){re.escape(account)}@", r["seen"]):
                r["seen"] = (r["seen"] + ", " if r["seen"] else "") + f"{account}@{now}"; changed = True
            lines[r["i"]] = row_line(r)
    known = {r["name"] for r in rows}
    for n in sorted(present - known):
        lines.append(row_line({"name": n, "purpose": "undocumented (document before use)", "tool": "none yet",
                               "requested": f"found by probe, {now[:10]}", "status": "set", "seen": "" if account == "unlabelled" else f"{account}@{now}"}))
        new_undoc.append(n); changed = True
    if changed:
        open(path, "w", encoding="utf-8").write("\n".join(lines).rstrip("\n") + "\n")
    return newly_set, new_undoc


def main(argv):
    if "--help" in argv or "-h" in argv:
        print(__doc__); return 0
    if "--sync" in argv:
        newly, undoc = sync()
        for n in newly: print(f"KEY NOW SET: {n}")
        for n in undoc: print(f"KEY UNDOCUMENTED: {n}")
    present, unset, undoc = probe()
    if "--quiet" in argv or "--sync" in argv:
        line = f"keys: {len(present)} credential names set (account {os.environ.get('CIPHERLAB_ACCOUNT') or 'unlabelled'})"
        if unset: line += f"; requested or documented but unset here: {', '.join(unset)}"
        if undoc: line += f"; SET BUT NOT IN KEYS.md (document before use): {', '.join(undoc)}"
        print(line); return 0
    print("set (names only):", ", ".join(present) or "none")
    print("documented but unset:", ", ".join(unset) or "none")
    print("set but not in KEYS.md:", ", ".join(undoc) or "none")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
