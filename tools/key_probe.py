#!/usr/bin/env python3
"""Key probe: which credential variables this container carries, by NAME only, against the list the repo documents.

Usage:
  tools/key_probe.py            print present / documented-but-unset / present-but-undocumented names
  tools/key_probe.py --quiet    one line (used by tools/room.py --start)
  tools/key_probe.py --help

Why (owner, 25 Sept 2026, about 22:40 UTC): secrets added to one account's environment for a worker there were missed
by the other account's sessions, because nothing listed what a container actually carries. A variable added after a
session started is invisible to that session (CLAUDE.md, key probe 25 Sept), and the two accounts' environments are
configured separately, so a key must be added on both. This script reads names only: it never prints, logs or
compares a value (CLAUDE.md access playbook, handling rule).

DOCUMENTED is the list CLAUDE.md's access playbook names. A name present here and absent there is a prompt to
document it (what it is for, which tool reads it), never to use it blind.
"""
import os
import re
import sys

DOCUMENTED = [
    "DECODE_USER", "DECODE_PASS", "IA_USER", "IA_PASS", "GOOGLE_BOOKS_KEY", "JSTOR_USER", "JSTOR_PASS",
    "OPENALEX_KEY", "S2_KEY", "EUROPEANA_API_KEY", "DPLA_API_KEY", "DDB_API_KEY", "APE_API_KEY", "CORE_API_KEY",
    "NARA_API_KEY", "REDDIT_CLIENT_ID", "REDDIT_CLIENT_SECRET",
    "AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "CLOUDSDK_AUTH_ACCESS_TOKEN",
]
PATTERN = re.compile(r"(KEY|USER|PASS|TOKEN|SECRET|CLIENT_ID|CREDENTIAL)", re.I)
# Platform and shell variables that match the pattern but are not the owner's service credentials.
IGNORE = re.compile(r"^(USER|LOGNAME|USERNAME|GH_TOKEN|GITHUB_TOKEN|MAX_THINKING_TOKENS|CLAUDE_|ANTHROPIC_|CCR_|NODE_|NPM_|SSH_|SUDO_|XDG_)")


def probe(environ=None):
    env = os.environ if environ is None else environ
    present = sorted(n for n in env if PATTERN.search(n) and not IGNORE.match(n) and env.get(n))
    documented_unset = [n for n in DOCUMENTED if not env.get(n)]
    undocumented = [n for n in present if n not in DOCUMENTED]
    return present, documented_unset, undocumented


def main(argv):
    if "--help" in argv or "-h" in argv:
        print(__doc__)
        return 0
    present, unset, undoc = probe()
    if "--quiet" in argv:
        line = f"keys: {len(present)} credential names set"
        if unset:
            line += f"; documented but unset: {', '.join(unset)}"
        if undoc:
            line += f"; SET BUT NOT IN CLAUDE.md (document before use): {', '.join(undoc)}"
        print(line)
        return 0
    print("set (names only):", ", ".join(present) or "none")
    print("documented but unset:", ", ".join(unset) or "none")
    print("set but not documented in CLAUDE.md:", ", ".join(undoc) or "none")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
