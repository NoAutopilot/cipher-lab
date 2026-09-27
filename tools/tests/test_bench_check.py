#!/usr/bin/env python3
"""Offline test for tools/bench_check.py. Throwaway git repo in a temp dir; no real repo paths.
Run: python3 tools/tests/test_bench_check.py"""
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import bench_check as bc

fails = 0


def check(name, ok):
    global fails
    print('PASS' if ok else 'FAIL', name)
    fails += not ok


HEADER = "# BENCHMARK.tsv -- frozen at commit {sha} (test). Rows are APPENDED, never edited in place.\n"
COLS = "case_id\tsplit\tfamily\ttruth\tciphertext_path\tkey_path\tplaintext_path\n"


def write_tsv(d, sha, rows):
    (d / 'BENCHMARK.tsv').write_text(HEADER.format(sha=sha) + COLS + '\n'.join(rows) + '\n')


with tempfile.TemporaryDirectory() as d:
    d = Path(d)

    def git(*a):
        subprocess.run(['git', '-C', str(d), *a], check=True, capture_output=True)

    git('init', '-q')
    git('config', 'user.email', 't@t')
    git('config', 'user.name', 't')
    (d / 'ciphers' / 'a').mkdir(parents=True)
    (d / 'ciphers/a/ciphertext.tsv').write_text('1 2 3\n')
    (d / 'ciphers/a/key.tsv').write_text('1\tx\n2\ty\n')
    git('add', '.')
    git('commit', '-qm', 'freeze point')
    sha1 = subprocess.run(['git', '-C', str(d), 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()

    # ---- a clean benchmark: no problems ----
    write_tsv(d, sha1, [
        "case1\tdev\tfam-a\tpositive\tciphers/a/ciphertext.tsv\tciphers/a/key.tsv\t",
        "case2\teval\tfam-b\tpositive\tciphers/a/ciphertext.tsv\tciphers/a/key.tsv\t",
    ])
    ok, problems, sha, n = bc.check(d / 'BENCHMARK.tsv', root=d)
    check('a clean benchmark passes', ok and not problems and n == 2)

    # ---- family in both splits ----
    write_tsv(d, sha1, [
        "case1\tdev\tfam-a\tpositive\tciphers/a/ciphertext.tsv\tciphers/a/key.tsv\t",
        "case2\teval\tfam-a\twrong-key\tciphers/a/ciphertext.tsv\tciphers/a/key.tsv\t",
    ])
    ok, problems, sha, n = bc.check(d / 'BENCHMARK.tsv', root=d)
    check('family in both splits fails', not ok and any('fam-a' in p and 'both splits' in p for p in problems))

    # ---- missing truth label ----
    write_tsv(d, sha1, [
        "case1\tdev\tfam-a\t\tciphers/a/ciphertext.tsv\tciphers/a/key.tsv\t",
    ])
    ok, problems, sha, n = bc.check(d / 'BENCHMARK.tsv', root=d)
    check('missing truth label fails', not ok and any('no truth label' in p for p in problems))

    # ---- eval path changed since the freeze sha ----
    (d / 'ciphers/a/ciphertext.tsv').write_text('1 2 3 4 5\n')  # modify after the freeze commit
    git('add', '.')
    git('commit', '-qm', 'edit after freeze')
    write_tsv(d, sha1, [
        "case1\teval\tfam-a\tpositive\tciphers/a/ciphertext.tsv\tciphers/a/key.tsv\t",
    ])
    ok, problems, sha, n = bc.check(d / 'BENCHMARK.tsv', root=d)
    check('eval path changed since freeze fails', not ok and any('changed since the freeze commit' in p for p in problems))

    # ---- a dev path changing since the freeze is NOT checked (only eval rows are protected) ----
    write_tsv(d, sha1, [
        "case1\tdev\tfam-a\tpositive\tciphers/a/ciphertext.tsv\tciphers/a/key.tsv\t",
    ])
    ok, problems, sha, n = bc.check(d / 'BENCHMARK.tsv', root=d)
    check('a changed dev path is not flagged (only eval is frozen-protected)', ok and not problems)

    # ---- a path that did not exist at the freeze sha (written in the same freeze commit) is skipped, not failed
    (d / 'ciphers/a/new_synth.json').write_text('{}')
    write_tsv(d, sha1, [
        "case1\teval\tfam-a\tsynthetic\tciphers/a/new_synth.json\t\t",
    ])
    ok, problems, sha, n = bc.check(d / 'BENCHMARK.tsv', root=d)
    check('a path new since the freeze sha is skipped, not failed', ok and not problems)

    # ---- a directory path (trailing /) and a free-text path (contains a space) are skipped ----
    write_tsv(d, sha1, [
        "case1\teval\tfam-a\tpositive\tciphers/a/\t\tTomokiyo's printed dump, not a file",
    ])
    ok, problems, sha, n = bc.check(d / 'BENCHMARK.tsv', root=d)
    check('a directory path and a free-text path are skipped, not failed', ok and not problems)

    # ---- missing frozen-header line raises ----
    (d / 'BENCHMARK.tsv').write_text(COLS + "case1\tdev\tfam-a\tpositive\t\t\t\n")
    raised = False
    try:
        bc.check(d / 'BENCHMARK.tsv', root=d)
    except SystemExit:
        raised = True
    check('missing frozen-header line raises SystemExit', raised)

print(f"{'OK' if not fails else 'FAILED'}: {fails} failure(s)")
sys.exit(1 if fails else 0)
