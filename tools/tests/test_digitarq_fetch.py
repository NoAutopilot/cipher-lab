#!/usr/bin/env python3
"""Offline test for tools/digitarq_fetch.py (no network): a fake curl
(tools/tests/fixtures/fake_digitarq_curl.py) serves a paginated 5-file list and a
1x1 JPEG for any fileId, exercising fetch_filelist's pagination and cmd_montage's
contact-sheet labeling against real image bytes.
Run: python3 tools/tests/test_digitarq_fetch.py"""
import argparse
import contextlib
import io
import os
import shutil
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import digitarq_fetch as df

FAKE_CURL = os.path.join(ROOT, "tools", "tests", "fixtures", "fake_digitarq_curl.py")

fails = 0


def check(ok, what):
    global fails
    fails += not ok
    print("PASS" if ok else "FAIL", what)


tmp = tempfile.mkdtemp()
try:
    files, n_requests = df.fetch_filelist("DOC123", tmp, page_size=2, delay=0, curl_bin=FAKE_CURL)
    check(len(files) == 5, "fetch_filelist paginates to all 5 rows")
    check(n_requests == 3, f"fetch_filelist made 3 paginated requests (got {n_requests})")
    check([f["name"] for f in files] == [f"m000{i}.jpg" for i in range(1, 6)],
          "filelist sorted by name")
    check(os.path.exists(os.path.join(tmp, "filelist.json")), "filelist.json written")

    for item in files[0::2]:
        df.curl_bytes(f"{df.HOST}/api/rdigital/thumb?fileId={item['id']}",
                       os.path.join(tmp, f"thumb_{item['name']}.jpg"), curl_bin=FAKE_CURL)
    thumb_files = sorted(f for f in os.listdir(tmp) if f.startswith("thumb_"))
    check(thumb_files == ["thumb_m0001.jpg.jpg", "thumb_m0003.jpg.jpg", "thumb_m0005.jpg.jpg"],
          f"stride-2 thumb selection ({thumb_files})")
    check(os.path.getsize(os.path.join(tmp, thumb_files[0])) > 0, "thumbnail bytes written")

    m_args = argparse.Namespace(montage=tmp, per_sheet=2, cols=2)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = df.cmd_montage(m_args)
    check(rc == 0, "cmd_montage exits 0")
    sheets = sorted(f for f in os.listdir(tmp) if f.startswith("montage_"))
    check(len(sheets) == 2, f"cmd_montage writes 2 sheets for 3 thumbs at per_sheet=2 (got {len(sheets)})")
finally:
    shutil.rmtree(tmp, ignore_errors=True)

print("digitarq_fetch:", "all tests pass" if not fails else f"{fails} failures")
sys.exit(1 if fails else 0)
