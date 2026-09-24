#!/usr/bin/env python3
"""ROOM.md helper: append one line and push it safely.

Usage:
  tools/room.py "role: target" "signal text"        append a timestamped line, commit, rebase, push (retries)
  tools/room.py --start                             worker start: fetch, checkout -B main origin/main, sanity check
  tools/room.py --push [paths...]                   commit the named paths (already staged or listed) and push with the
                                                    same rebase-and-retry loop, keeping both sides of a ROOM.md conflict
  tools/room.py --digest "YYYY-MM-DD HH:MM"         print only ROOM.md lines at or after SINCE whose signal starts
                                                    with nomination:, for LANE, flag:, done:, handoff, or retract,
                                                    or contains allowed_warning, rejected, or a bare N0-N5 class
                                                    token, plus one summary line "K of N lines matched". Read-only:
                                                    nothing is dropped from ROOM.md itself, only what is printed.

Why: on 24 Sept 2026 six commits were spent fixing ROOM.md conflict markers and one worker replaced the file with a
four-line stub from a stale clone. This script appends with >>, never rewrites, resolves a ROOM.md conflict by
keeping both sides, refuses to push a ROOM.md that shrank, and retries the fetch-rebase-push loop up to five times.
--digest was added from RETRO-2026-09-24d (subject 3): an orchestrator checking in across several live lanes had no
way to read ROOM.md short of the full, growing file, unlike a worker's own "last 30 lines" rule.
"""
import os, re, subprocess, sys, time

ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()
ROOM = os.path.join(ROOT, "ROOM.md")

def sh(*args, check=True, quiet=True):
    r = subprocess.run(args, cwd=ROOT, capture_output=True, text=True)
    if check and r.returncode != 0 and not quiet:
        sys.stderr.write(r.stderr)
    return r

def utc():
    return time.strftime("%Y-%m-%d %H:%M", time.gmtime())

def start():
    sh("git", "fetch", "-q", "origin", "main")
    r = sh("git", "status", "--porcelain")
    if r.stdout.strip():
        print("working tree has changes; not resetting. Commit or stash them first."); return 2
    unpushed = sh("git", "log", "--oneline", "origin/main..HEAD")
    if unpushed.stdout.strip():
        stamp = time.strftime("%Y%m%d%H%M%S", time.gmtime())
        branch = f"preserve/{stamp}-unpushed-local-history"
        sh("git", "branch", branch, "HEAD")
        print(f"local HEAD had commits not on origin/main; saved to {branch} before resetting. Push it or ask.")
    sh("git", "checkout", "-q", "-B", "main", "origin/main")
    n = sum(1 for _ in open(ROOM, encoding="utf-8"))
    if n < 50:
        print(f"ROOM.md has only {n} lines on origin/main; that is a stub, not the room. Stop and flag it."); return 3
    print(f"on main at {sh('git','rev-parse','--short','HEAD').stdout.strip()}, ROOM.md {n} lines")
    return 0

def keep_both(path):
    """Resolve a real git conflict block by keeping both sides.

    Markers must be anchored to the start of a line (Lesson of 24 Sept 2026: an
    unanchored match also fires on ROOM.md prose that merely quotes marker text,
    e.g. a flag line describing "an unclosed <<<<<<< HEAD", splicing unrelated
    lines together and losing content between them).
    """
    t = open(path, encoding="utf-8").read()
    t2 = re.sub(r"^<<<<<<< [^\n]*\n(.*?)^=======\n(.*?)^>>>>>>> [^\n]*\n", lambda m: m.group(1) + m.group(2), t, flags=re.S | re.M)
    open(path, "w", encoding="utf-8").write(t2)

def room_ok():
    """Refuse to push a ROOM.md shorter than origin's or carrying conflict markers."""
    cur = open(ROOM, encoding="utf-8").read()
    if re.search(r"^(<<<<<<<|=======|>>>>>>>)", cur, re.M):
        return "conflict markers in ROOM.md"
    o = sh("git", "show", "origin/main:ROOM.md").stdout
    if len(cur.splitlines()) < len(o.splitlines()) - 2:
        return f"ROOM.md would shrink ({len(cur.splitlines())} < {len(o.splitlines())} lines on origin)"
    return None

def push(message, paths):
    if paths:
        sh("git", "add", "--", *paths)
    if not sh("git", "diff", "--cached", "--quiet").returncode:
        print("nothing staged"); return 0
    c = sh("git", "commit", "-q", "-m", message)
    if c.returncode: sys.stderr.write(c.stderr); return 1
    for i in range(5):
        sh("git", "fetch", "-q", "origin", "main")
        rb = sh("git", "rebase", "--autostash", "FETCH_HEAD")
        if rb.returncode:
            st = sh("git", "status", "--porcelain").stdout
            if "UU ROOM.md" in st or "AA ROOM.md" in st:
                keep_both(ROOM); sh("git", "add", "ROOM.md")
            other = [l[3:] for l in st.splitlines() if l.startswith(("UU", "AA")) and not l.endswith("ROOM.md")]
            if other:
                sh("git", "rebase", "--abort")
                print("conflict outside ROOM.md in: " + ", ".join(other) + "; resolve by hand"); return 4
            env = dict(os.environ, GIT_EDITOR="true")
            subprocess.run(["git", "rebase", "--continue"], cwd=ROOT, env=env, capture_output=True)
        bad = room_ok()
        if bad:
            print("refusing to push: " + bad); return 5
        p = sh("git", "push", "-q", "-u", "origin", "main")
        if p.returncode == 0:
            print("pushed " + sh("git", "rev-parse", "--short", "HEAD").stdout.strip()); return 0
        time.sleep(3 + 2 * i)
    print("push failed five times"); return 6

def _digest_matches(rest):
    """Whether a ROOM.md line's signal text (everything after 'TIMESTAMP | actor | ') belongs in a digest."""
    prefixes = ("nomination:", "for LANE", "flag:", "done:", "handoff", "retract")
    contains = ("allowed_warning", "rejected")
    if rest.startswith(prefixes):
        return True
    if any(c in rest for c in contains):
        return True
    if re.search(r"\bN[0-5]\b", rest):
        return True
    return False

def filter_lines(lines, since):
    """Pure filter used by --digest and its test: lines is an iterable of raw ROOM.md lines."""
    kept = []
    for line in lines:
        line = line.rstrip("\n")
        if not line.strip():
            continue
        parts = line.split(" | ", 2)
        if len(parts) < 3:
            continue
        ts, actor, rest = parts
        if ts < since:
            continue
        if _digest_matches(rest):
            kept.append(line)
    return kept

def digest(a):
    if not a:
        print('--digest requires a SINCE argument, e.g. --digest "2026-09-24 09:00"'); return 1
    since = a[0]
    with open(ROOM, encoding="utf-8") as f:
        all_lines = [l for l in f if l.strip()]
    kept = filter_lines(all_lines, since)
    for line in kept:
        print(line)
    print(f"{len(kept)} of {len(all_lines)} lines matched")
    return 0

def main(a):
    if not a or a[0] in ("-h", "--help"):
        print(__doc__); return 0
    if a[0] == "--start":
        return start()
    if a[0] == "--push":
        msg = os.environ.get("MSG", "update")
        return push(msg, a[1:])
    if a[0] == "--digest":
        return digest(a[1:])
    if len(a) < 2:
        print(__doc__); return 1
    line = f"{utc()} | {a[0]} | {a[1]}".replace("\n", " ")
    with open(ROOM, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    return push("ROOM: " + a[1][:60], ["ROOM.md"])

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
