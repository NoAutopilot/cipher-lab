#!/usr/bin/env python3
"""ROOM.md helper: append one line and push it safely.

Usage:
  tools/room.py "role: target" "signal text"        append a timestamped line, commit, rebase, push (retries)
  tools/room.py --start                             worker start: fetch, checkout -B main origin/main, sanity check
  tools/room.py --push [paths...]                   commit the named paths (already staged or listed) and push with the
                                                    same rebase-and-retry loop, keeping both sides of a ROOM.md conflict
                                                    and refusing to push if the rebase dropped a STATUS.md/QUEUE.md section
  tools/room.py --digest "YYYY-MM-DD HH:MM"         print only ROOM.md lines at or after SINCE whose signal starts
                                                    with nomination:, for LANE, flag:, done:, handoff, or retract,
                                                    or contains allowed_warning, rejected, or a bare N0-N5 class
                                                    token, plus one summary line "K of N lines matched". Read-only:
                                                    nothing is dropped from ROOM.md itself, only what is printed.

Why: on 24 Sept 2026 six commits were spent fixing ROOM.md conflict markers and one worker replaced the file with a
four-line stub from a stale clone. This script appends with >>, never rewrites, resolves a ROOM.md conflict by
keeping both sides, refuses to push a ROOM.md that shrank, and retries the fetch-rebase-push loop up to five times.
Warnings (25 Sept 2026, UPDATES.md): a done line naming a test, negative or FAIL without the word control, or any
line carrying a dollar figure, is still appended but prints a WARNING first (rule 3; COMMON item 1).
Section guard (25 Sept 2026, LEDGER.md:810, LANE B3): unlike ROOM.md, a non-conflicting 3-way merge on STATUS.md or
QUEUE.md can silently drop a whole '## ' section neither side's diff touched. --push now snapshots both files'
headings before the rebase and refuses to push if one vanished, naming the lost section, same shape as the
ROOM.md shrink guard.
--digest was added from RETRO-2026-09-24d (subject 3): an orchestrator checking in across several live lanes had no
way to read ROOM.md short of the full, growing file, unlike a worker's own "last 30 lines" rule.
"""
import os
import sys, re, subprocess, sys, time

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
    # Cascade (25 Sept 2026, UPDATES.md): every session's first command shows the changes instituted across
    # accounts since its brief was written, so a rule change never depends on a brief being rewritten.
    try:
        rows = [l for l in open("UPDATES.md", encoding="utf-8") if l.startswith("| 2")]
        if rows:
            print(f"UPDATES.md: {len(rows)} instituted changes; the last {min(3, len(rows))}:")
            for l in rows[-3:]:
                cells = [c.strip() for c in l.split("|")]
                print(f"  {cells[1]} -- {cells[3][:160]}")
    except FileNotFoundError:
        pass
    try:
        near = [l for l in open("NEAR.md", encoding="utf-8") if l.startswith("| ") and not l.startswith("| Target") and not l.startswith("|---")]
        if near:
            print(f"NEAR.md: {len(near)} near-solve rows -- a target there is never closed-negative (rule 5): " + ", ".join(l.split("|")[1].strip().split(" ")[0] for l in near))
    except FileNotFoundError:
        pass
    # Key probe (25 Sept 2026, UPDATES.md): names only, so a session sees at once which credentials its container
    # carries and which the repo has not documented yet (a key added on one account was missed by the other).
    try:
        out = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "key_probe.py"), "--sync"], capture_output=True, text=True, timeout=20, cwd=ROOT).stdout
        # Prefix (25-26 Sept 2026, RETRO-2026-09-26a): key_probe.py's "keys: N credential names set" (name-
        # presence against the documented list) and key_livecheck.py's "keys: N present, M working" (live test
        # calls) below it read as two different counts for the same word with no cue why -- name the tool.
        print("key_probe.py --sync: " + out.strip())
        # Announce (25 Sept 2026, owner's ask): a requested key that has appeared, or an undocumented one, is posted to
        # ROOM.md by the first fresh session that sees it, so both parents learn of it without the owner writing anything.
        acct = os.environ.get("CIPHERLAB_ACCOUNT") or "unlabelled"
        news = [l.split(": ", 1)[1] for l in out.splitlines() if l.startswith("KEY NOW SET: ")]
        undoc = [l.split(": ", 1)[1] for l in out.splitlines() if l.startswith("KEY UNDOCUMENTED: ")]
        if news or undoc:
            sig = []
            if news: sig.append("key now set on account " + acct + ": " + ", ".join(news) + " (KEYS.md row flipped to set; for both parents)")
            if undoc: sig.append("flag: undocumented key present on account " + acct + ": " + ", ".join(undoc) + " (KEYS.md row added; document before use)")
            with open(ROOM, "a", encoding="utf-8") as f:
                f.write(f"{utc()} | key probe (tools/room.py --start, account {acct}) | " + "; ".join(sig) + "\n")
            push("KEYS.md: key probe on account " + acct, ["KEYS.md", "ROOM.md"])
        elif sh("git", "diff", "--quiet", "--", "KEYS.md").returncode:
            push("KEYS.md: seen column, account " + acct, ["KEYS.md"])
    except Exception as e:  # never block a start on the probe
        print(f"key probe skipped: {e}")
    # Key livecheck (25 Sept 2026, KEYPROBE-TOOL): every session sees the last live-call probe so a
    # key that went from absent/failing to present/working is not sitting unused in ASKS.md. Distinct
    # from key_probe.py above (that one is name-presence only, never a network call).
    try:
        line = next(l for l in open("KEYS-STATUS.md", encoding="utf-8") if l.startswith("keys: "))
        print("key_livecheck.py: " + line.strip() + " -- run it fresh before filing an ASKS.md/LOCAL-QUEUE.tsv row")
    except (FileNotFoundError, StopIteration):
        print("KEYS-STATUS.md missing or has no 'keys: ' line -- run python3 tools/key_livecheck.py")
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

def headings(path):
    """'## ' section headings of path, or None if the file does not exist."""
    if not os.path.exists(path):
        return None
    return set(re.findall(r"^## .*$", open(path, encoding="utf-8").read(), re.M))

def headings_from_ref(ref, relpath):
    """'## ' section headings of relpath as committed at ref, or None if the path does not exist there.

    Mirrors headings()'s contract but reads a committed ref instead of the local working tree (25-26 Sept
    2026, RETRO-2026-09-26a): a34cd00 (22:12, LANE ZX2) dropped two STATUS.md sections in the session's own
    local edit, before any commit or rebase, so a snapshot taken from the working tree after that edit never
    saw the sections at all -- comparing against origin/main catches a self-inflicted drop the same way it
    catches a rebase mis-merge.
    """
    r = sh("git", "show", f"{ref}:{relpath}")
    if r.returncode:
        return None
    return set(re.findall(r"^## .*$", r.stdout, re.M))

def headings_ok(before):
    """Refuse to push if a rebase silently dropped a '## ' section from STATUS.md or QUEUE.md.

    room_ok() protects ROOM.md by name; a non-conflicting 3-way merge on any other shared file has no
    equivalent guard (LEDGER.md:810, LANE B3, 25 Sept 2026: "STATUS.md sections can be dropped by another
    session's room.py --push merge"). `before` maps path -> its heading set snapshotted before the rebase.
    """
    for path, before_headings in before.items():
        if not before_headings:
            continue
        after_headings = headings(path)
        if after_headings is None:
            return f"{os.path.basename(path)} disappeared"
        lost = before_headings - after_headings
        if lost:
            return f"{os.path.basename(path)} lost section(s): " + "; ".join(sorted(lost))
    return None

def push(message, paths):
    if paths:
        sh("git", "add", "--", *paths)
    if not sh("git", "diff", "--cached", "--quiet").returncode:
        print("nothing staged"); return 0
    # Snapshot origin's own headings BEFORE this commit is created (25-26 Sept 2026, RETRO-2026-09-26a):
    # a34cd00 (22:12, LANE ZX2) dropped two STATUS.md sections in the session's own local edit, before any
    # commit or rebase -- headings_ok()'s post-commit, pre-rebase snapshot already reflected the drop, so it
    # could not flag it. Comparing against origin/main directly catches a self-inflicted drop the same way it
    # catches a rebase mis-merge.
    sh("git", "fetch", "-q", "origin", "main")
    watched = {p: headings_from_ref("origin/main", os.path.relpath(p, ROOT))
               for p in (os.path.join(ROOT, "STATUS.md"), os.path.join(ROOT, "QUEUE.md"))}
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
        bad = headings_ok(watched)
        if bad:
            print("refusing to push: " + bad); return 7
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

def warnings_for(role, signal):
    """Warnings printed before a line is appended (25 Sept 2026, UPDATES.md; the line is still appended).

    - a done line that reports a test, negative or FAIL without the word control: CLAUDE.md rule 3 (a negative
      means nothing without a matched control number beside it; nine done lines broke this on 25 Sept 2026)
    - a dollar figure anywhere in the line: cost figures come from the orchestrator's get_session, not the
      worker's own sense of it (README common tail item 1), and `$8` inside double quotes vanishes anyway."""
    w = []
    sig = signal.strip()
    if sig.lower().startswith("done:") and re.search(r"\btests?\b|\btested\b|\bnegatives?\b|\bfail(s|ed|ing)?\b|closed-negative",
                                                     sig, re.I) and not re.search(r"\bcontrols?\b", sig, re.I):
        w.append("WARNING: done line reports a test or negative without a control number (rule 3)")
    text = f"{role} | {signal}"
    if re.search(r"\$\s?\d|\bdollars\b|\bUSD\b", text, re.I):
        w.append("WARNING: cost figures in ROOM lines are the orchestrator's to read (COMMON item 1)")
    return w


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
    if a[0].startswith("-"):
        # 26 Sept 2026 (V7-QA4): "--append" and other unknown flags were written into ROOM.md as the role
        # (23 lines by then); the role is a name, so an unknown flag is refused before anything is appended.
        print(f"room.py: unknown option {a[0]!r}; usage: tools/room.py \"role: target\" \"signal text\"",
              file=sys.stderr)
        return 2
    if len(a) < 2:
        print(__doc__); return 1
    for w in warnings_for(a[0], a[1]):
        print(w)
    line = f"{utc()} | {a[0]} | {a[1]}".replace("\n", " ")
    with open(ROOM, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    return push("ROOM: " + a[1][:60], ["ROOM.md"])

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
