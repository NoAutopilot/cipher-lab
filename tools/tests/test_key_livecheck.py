#!/usr/bin/env python3
"""Offline test for tools/key_livecheck.py (no network; monkeypatched os.environ and a stubbed HTTP
layer). Checks: presence detection, live-test dispatch per credential kind, the cache/cooldown,
--force, IA's login gated behind do_ia_login, DECODE/JSTOR staying presence-only regardless, and
that no credential value ever appears in a rendered row or the Markdown output. Also (RETRO-2026-09-26g
item 4) a working->failing flip against `prev` retries once after a pause before being trusted: recovers
if the retry succeeds, reports "confirmed on retry" if it fails again, and never retries when there was no
prior "works: yes" to flip from.
Run: python3 tools/tests/test_key_livecheck.py"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import key_livecheck as kp

fails = 0


def check(ok, what):
    global fails
    fails += not ok
    print("PASS" if ok else "FAIL", what)


ALL_ENV = set()
for spec in kp.SINGLE_KEYS:
    ALL_ENV.update(spec["env"])
for spec in kp.PAIR_KEYS:
    ALL_ENV.update(spec["env"])

SECRET = "sekrit-value-should-never-appear-9f3a"


def clean_env():
    saved = {k: os.environ.pop(k, None) for k in ALL_ENV}
    return saved


def restore_env(saved):
    for k, v in saved.items():
        if v is None:
            os.environ.pop(k, None)
        else:
            os.environ[k] = v


class StubHTTP:
    """Records calls; returns a canned (code, body) per host, defaulting to a 200 JSON stub."""

    def __init__(self, responses=None):
        self.calls = []
        self.responses = responses or {}

    def __call__(self, url, method="GET", headers=None, data=None, timeout=30):
        self.calls.append((url, method, headers, data))
        for host_frag, resp in self.responses.items():
            if host_frag in url:
                return resp
        return 200, b'{"totalItems": 1, "success": true, "totalResults": 1, "count": 1, ' \
                     b'"meta": {"count": 1}, "total": 1, "totalHits": 1}'


saved = clean_env()
try:
    # 1. everything absent
    rows = kp.run_probe(http=StubHTTP(), cache={}, sleep=lambda s: None)
    by_id = {r["id"]: r for r in rows}
    check(all(r["present"] is False for r in rows if r["id"] not in ("hathitrust",)),
          "all credentials report present=False when unset")
    check(all(r["works"] is False for r in rows if r["id"] not in ("hathitrust",)),
          "all credentials report works=False when absent (never a crash)")
    check(by_id["hathitrust"]["present"] is None, "HathiTrust row is presence=n/a (no key needed)")

    # 2. present, live test succeeds -- and never leaks the value into detail
    os.environ["GOOGLE_BOOKS_KEY"] = SECRET
    os.environ["OPENALEX_KEY"] = SECRET
    os.environ["S2_KEY"] = SECRET
    os.environ["EUROPEANA_API_KEY"] = SECRET
    os.environ["DPLA_API_KEY"] = SECRET
    os.environ["CORE_API_KEY"] = SECRET
    stub = StubHTTP()
    rows = kp.run_probe(http=stub, cache={}, sleep=lambda s: None)
    by_id = {r["id"]: r for r in rows}
    for key_id in ("google_books", "openalex", "s2", "europeana", "dpla", "core"):
        check(by_id[key_id]["present"] is True, f"{key_id}: present=True when set")
        check(by_id[key_id]["works"] is True, f"{key_id}: works=True on a 200/success stub response")
        check(SECRET not in by_id[key_id]["detail"], f"{key_id}: detail never contains the credential value")
    check(all(SECRET not in json.dumps(c) for c in stub.calls[0:0]), "sanity: no-op")
    md = kp.render_markdown(rows, "2026-09-25 23:00")
    check(SECRET not in md, "rendered Markdown never contains a credential value")
    check("keys: 6 present, 6 working" in md, "summary line counts present/working credentials")

    # 3. an error body that echoes the key back gets redacted
    stub_err = StubHTTP({"googleapis.com": (400, f"bad request q=cipher&key={SECRET}".encode())})
    rows2 = kp.run_probe(http=stub_err, cache={}, sleep=lambda s: None)
    gb = next(r for r in rows2 if r["id"] == "google_books")
    check(gb["works"] is False, "google_books: works=False on HTTP 400")
    check(SECRET not in gb["detail"], "google_books: echoed key in an error body is redacted")
    check("[REDACTED]" in gb["detail"], "google_books: redaction marker present in the detail")

    # 4. cache/cooldown: a second run within the window does not call http again
    stub2 = StubHTTP()
    cache = {}
    kp.run_probe(http=stub2, cache=cache, sleep=lambda s: None)
    n_first = len(stub2.calls)
    kp.run_probe(http=stub2, cache=cache, sleep=lambda s: None, cooldown=900)
    check(len(stub2.calls) == n_first, "cached result reused inside the cooldown window (no new calls)")
    kp.run_probe(http=stub2, cache=cache, sleep=lambda s: None, force=True)
    check(len(stub2.calls) > n_first, "--force bypasses the cache and re-tests live")

    # 5. DECODE and JSTOR stay presence-only even with do_ia_login=True (only IA has a live flag)
    os.environ["DECODE_USER"] = "u"
    os.environ["DECODE_PASS"] = "p"
    os.environ["JSTOR_USER"] = "u"
    os.environ["JSTOR_PASS"] = "p"
    rows3 = kp.run_probe(http=StubHTTP(), cache={}, sleep=lambda s: None, do_ia_login=True)
    by_id3 = {r["id"]: r for r in rows3}
    check(by_id3["decode"]["present"] is True and by_id3["decode"]["works"] is None,
          "DECODE: present, works=None (presence-only), never a live login")
    check("presence-only always" in by_id3["decode"]["detail"], "DECODE: detail states presence-only always")
    check(by_id3["jstor"]["present"] is True and by_id3["jstor"]["works"] is None,
          "JSTOR: present, works=None (presence-only), never a live login")
    check(by_id3["ia"]["present"] is False, "IA: absent (IA_USER/IA_PASS not set in this sub-test)")

    # 6. IA login gated behind do_ia_login, and its own live test is exercised when present
    os.environ["IA_USER"] = "someone@example.com"
    os.environ["IA_PASS"] = SECRET
    stub_ia = StubHTTP({"xauthn": (200, b'{"success": true}')})
    rows4 = kp.run_probe(http=stub_ia, cache={}, sleep=lambda s: None, do_ia_login=False)
    ia_row = next(r for r in rows4 if r["id"] == "ia")
    check(ia_row["works"] is None and not ia_row["checked_live"], "IA: presence-only by default, no login fired")
    check(not any("xauthn" in c[0] for c in stub_ia.calls), "IA: no xauthn call made without --ia-login")

    rows5 = kp.run_probe(http=stub_ia, cache={}, sleep=lambda s: None, do_ia_login=True)
    ia_row2 = next(r for r in rows5 if r["id"] == "ia")
    check(ia_row2["works"] is True, "IA: --ia-login runs the live xauthn test and reports success")
    check(SECRET not in ia_row2["detail"], "IA: password never appears in the login test detail")
    check(any("xauthn" in c[0] for c in stub_ia.calls), "IA: xauthn call made once --ia-login is set")

    # a failed login reports works=False without leaking the password
    stub_ia_fail = StubHTTP({"xauthn": (401, b'{"success": false, "values": {"reason": "account_not_found"}}')})
    rows6 = kp.run_probe(http=stub_ia_fail, cache={}, sleep=lambda s: None, do_ia_login=True)
    ia_row3 = next(r for r in rows6 if r["id"] == "ia")
    check(ia_row3["works"] is False, "IA: failed login reports works=False")
    check("account_not_found" in ia_row3["detail"], "IA: failure reason surfaced")
    check(SECRET not in ia_row3["detail"], "IA: password never leaked on a failed login either")

    # 7. no documented call yet -> works=None, not a crash, not a false negative
    os.environ["DDB_API_KEY"] = SECRET
    rows7 = kp.run_probe(http=StubHTTP(), cache={}, sleep=lambda s: None)
    ddb = next(r for r in rows7 if r["id"] == "ddb")
    check(ddb["present"] is True and ddb["works"] is None, "DDB: present but no documented test -> works=None, not False")

    # 9b (RETRO-2026-09-26g item 4). a live flip from working to not-working retries once after a pause before
    # trusting it: a fake http failing once then succeeding recovers when prev shows the key was working; a fake
    # http failing every time reports works=False with a "confirmed on retry" detail.
    class FlipOnceHTTP:
        def __init__(self):
            self.calls, self.seen = [], set()

        def __call__(self, url, method="GET", headers=None, data=None, timeout=30):
            self.calls.append((url, method, headers, data))
            key = "googleapis.com" if "googleapis.com" in url else url
            if key not in self.seen:
                self.seen.add(key)
                return 400, b'{"error": "rate limited"}'
            return 200, b'{"totalItems": 1}'

    class AlwaysFailHTTP:
        def __init__(self):
            self.calls = []

        def __call__(self, url, method="GET", headers=None, data=None, timeout=30):
            self.calls.append((url, method, headers, data))
            return 400, b'{"error": "rate limited"}'

    os.environ["GOOGLE_BOOKS_KEY"] = SECRET
    gb_label = "Google Books (googleapis.com/books/v1)"
    prev_working = {gb_label: ("yes", "yes")}
    sleeps = []
    flip = FlipOnceHTTP()
    rows8b = kp.run_probe(http=flip, cache={}, sleep=lambda s: sleeps.append(s), prev=prev_working)
    gb8b = next(r for r in rows8b if r["id"] == "google_books")
    check(gb8b["works"] is True, "google_books: transient failure recovers on retry when prev was working")
    check("retry after transient failure" in gb8b["detail"], "google_books: detail notes the retry")
    gb_calls = [c for c in flip.calls if "googleapis.com" in c[0]]
    check(len(gb_calls) == 2, "google_books: exactly one retry call made on a working->failing flip")

    always_fail = AlwaysFailHTTP()
    rows8c = kp.run_probe(http=always_fail, cache={}, sleep=lambda s: None, prev=prev_working)
    gb8c = next(r for r in rows8c if r["id"] == "google_books")
    check(gb8c["works"] is False, "google_books: confirmed failure after retry when both calls fail")
    check("confirmed on retry" in gb8c["detail"], "google_books: detail says confirmed on retry")
    gb_calls_c = [c for c in always_fail.calls if "googleapis.com" in c[0]]
    check(len(gb_calls_c) == 2, "google_books: exactly one retry call made, not a loop")

    no_retry = AlwaysFailHTTP()
    rows8d = kp.run_probe(http=no_retry, cache={}, sleep=lambda s: None, prev={})
    gb8d = next(r for r in rows8d if r["id"] == "google_books")
    check(gb8d["works"] is False, "google_books: no prior 'works' -> no retry needed")
    gb_calls_d = [c for c in no_retry.calls if "googleapis.com" in c[0]]
    check(len(gb_calls_d) == 1, "google_books: no retry call when there was no working->failing flip to confirm")

    # 8. render_changes flags a transition
    prev = {"Google Books (googleapis.com/books/v1)": ("no", "no")}
    changes = kp.render_changes(rows, prev)
    check("Google Books" in changes and "no->yes" in changes, "render_changes reports an absent->present/working transition")

    # 9. exit code is always 0 even with nothing set (main() path), writing to a temp file
    import tempfile
    saved2 = clean_env()
    try:
        tmp_out = tempfile.mktemp(suffix=".md")
        rc = kp.main(["--out", tmp_out, "--cooldown", "0"])
        check(rc == 0, "main() exits 0 even when every credential is absent")
        check(os.path.exists(tmp_out), "main() writes the status file")
        text = open(tmp_out).read()
        check(text.startswith("# Keys status"), "status file has the expected header")
        check("keys: 0 present, 0 working" in text, "status file summary line reflects an all-absent run")
        os.remove(tmp_out)
    finally:
        restore_env(saved2)

finally:
    restore_env(saved)
    try:
        os.remove(kp.CACHE_PATH)
    except OSError:
        pass

print(f"\n{'FAILED' if fails else 'ALL PASS'} ({fails} failure(s))")
sys.exit(1 if fails else 0)
