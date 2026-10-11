#!/usr/bin/env python3
"""Offline test (WT-MAIN, 11 Oct 2026): tools/room.py run from a linked worktree never moves branch `main` while
another worktree has it checked out. Seen 10-11 Oct 2026: a scratch worktree's `room.py --push` ended with
`git checkout -B main HEAD`, which git allows across worktrees; the main checkout's `main` moved 169 files ahead of
its index, so its next plain commit would have reverted all of them.
Must catch: --push and --start from a linked worktree while the main checkout is on `main` (main stays put, the
linked worktree ends detached at the pushed commit). Must not block: --push from the main checkout itself, which
still ends on `main` at the pushed commit, as before.
Builds a throwaway origin + clone + linked worktree under a temp dir; no network. Run: python3 tools/tests/test_room_worktree.py"""
import os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def git(cwd, *a):
    r = subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True)
    assert r.returncode == 0, (a, r.stderr)
    return r.stdout.strip()


def room(cwd, *a):
    return subprocess.run([sys.executable, os.path.join(cwd, "tools", "room.py"), *a], cwd=cwd, capture_output=True, text=True)


def setup(tmp):
    origin = os.path.join(tmp, "origin.git"); main = os.path.join(tmp, "main"); side = os.path.join(tmp, "side")
    subprocess.run(["git", "init", "-q", "--bare", "-b", "main", origin], check=True)
    subprocess.run(["git", "clone", "-q", origin, main], check=True, capture_output=True)
    for k, v in (("user.email", "t@example.invalid"), ("user.name", "t"), ("commit.gpgsign", "false")):
        git(main, "config", k, v)
    os.makedirs(os.path.join(main, "tools"))
    for f in ("room.py", "file_shrink_guard.py", "restricted_guard.py"):   # what --push imports or runs
        shutil.copy(os.path.join(HERE, "tools", f), os.path.join(main, "tools", f))
    with open(os.path.join(main, "ROOM.md"), "w") as f:
        f.write("# ROOM\n\n" + "".join(f"2026-10-11 00:{i:02d} | seed | line {i}\n" for i in range(60)))
    git(main, "add", "-A"); git(main, "commit", "-q", "-m", "seed"); git(main, "push", "-q", "-u", "origin", "main")
    git(main, "worktree", "add", "-q", "--detach", side, "HEAD")
    return origin, main, side


def test_push_from_linked_worktree_leaves_main_alone():
    with tempfile.TemporaryDirectory() as tmp:
        origin, main, side = setup(tmp)
        before = git(main, "rev-parse", "main")
        # the shape that broke: the linked worktree had been put on `main` too (an older room.py --start did that)
        subprocess.run(["git", "checkout", "-q", "-B", "main", "HEAD"], cwd=side, capture_output=True)
        r = room(side, "tester", "a line from the side worktree", "--push")
        assert "pushed" in r.stdout, (r.stdout, r.stderr)
        assert git(main, "rev-parse", "main") == before, "room.py moved the main checkout's main"
        assert git(main, "status", "--porcelain") == "", "the main checkout is dirty after a push from a linked worktree"
        pushed = git(origin, "rev-parse", "main")
        assert pushed != before and git(side, "rev-parse", "HEAD") == pushed
        assert subprocess.run(["git", "symbolic-ref", "-q", "HEAD"], cwd=side).returncode != 0, "linked worktree should end detached"


def test_start_from_linked_worktree_stays_detached():
    with tempfile.TemporaryDirectory() as tmp:
        origin, main, side = setup(tmp)
        before = git(main, "rev-parse", "main")
        r = room(side, "--start")
        assert git(main, "rev-parse", "main") == before
        assert subprocess.run(["git", "symbolic-ref", "-q", "HEAD"], cwd=side).returncode != 0, (r.stdout, r.stderr)


def test_push_from_main_checkout_still_ends_on_main():
    with tempfile.TemporaryDirectory() as tmp:
        origin, main, side = setup(tmp)
        r = room(main, "tester", "a line from the main checkout", "--push")
        assert "pushed" in r.stdout, (r.stdout, r.stderr)
        assert git(main, "symbolic-ref", "HEAD") == "refs/heads/main"
        assert git(main, "rev-parse", "main") == git(origin, "rev-parse", "main")


if __name__ == "__main__":
    test_push_from_linked_worktree_leaves_main_alone()
    test_start_from_linked_worktree_stays_detached()
    test_push_from_main_checkout_still_ends_on_main()
    print("ok")
