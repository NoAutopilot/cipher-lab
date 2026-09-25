#!/usr/bin/env python3
"""Presence and one documented test call per credential the CLAUDE.md Access playbook names.

  python3 tools/key_livecheck.py [--json] [--force] [--cooldown SECONDS] [--ia-login] [--out PATH]

Why (brief .claude/briefs/runs/2026-09-25-parent-keyprobe-tool.md): the owner adds keys and
logins to the environment and nobody notices until a worker happens to try one -- GOOGLE_BOOKS_KEY
sat unused from 20 to 25 Sept 2026 (a `country=US` parameter was all it needed), IA_USER/IA_PASS
worked from 23 Sept with no borrow attempted until 25 Sept, CORE_API_KEY was probed only when the
owner asked. This makes the check mechanical instead of relying on someone remembering to try.

Never prints a credential value, and never its length (CLAUDE.md's credential handling rule):
presence is `os.environ` truthiness only. An error body that could echo a key back (a bad request
that reflects its own query string, for instance) is redacted before being shown.

Two different things are being tested, and they get different defaults:

* The six API-key hosts (Google Books, OpenAlex, Semantic Scholar, Europeana, DPLA, CORE) are
  ordinary rate-limited GET/POST-with-header requests, not logins -- tools/print_check.py already
  repeats exactly this shape of call on every run it makes. These are tested live by default,
  each with the one call CLAUDE.md's Access playbook documents and the cloud fix it records
  (Google Books `country=US`, CORE's `v3/search/works/` trailing slash, Europeana `wskey=`, DPLA
  `api_key=`, OpenAlex/Semantic Scholar's bearer/x-api-key headers). A short result cache
  (default 900s, `--cooldown` to change, `--force` to bypass) keeps several sessions probing
  inside the same window from hammering every host afresh -- CLAUDE.md's good-citizen rule still
  applies to a tool that is meant to run unattended at the top of every check-in.
* DECODE, JSTOR and Internet Archive logins are a different kind of call: CLAUDE.md's good-citizen
  rule says "never automate a login beyond the single attempt rule", and a probe that runs
  automatically at the top of every check-in and every worker brief naming a host would itself BE
  the automated repeated login the rule forbids if it fired one every time. So these three are
  presence-only by default. DECODE and JSTOR stay presence-only unconditionally: DECODE's own
  Access playbook entry reserves its one login attempt per session for a worker that actually
  needs the record ("never a login attempt, since the playbook allows one attempt per session by
  a worker who needs it"); JSTOR is Cloudflare-blocked from the cloud entirely, so a login there
  would only ever fail and teaches nothing. IA's xauthn login is a genuine per-attempt login too
  (its own Access-playbook history warns it "rate-limits/locks out repeated failed logins" on
  bad credentials), so `--ia-login` is required to run it live -- pass it only from a session that
  has decided this IS its one login attempt this session and specifically needs to confirm IA
  still works; never add `--ia-login` to a check-in script or an unattended brief, or it becomes
  the automatic repeated login again.

Output: a Markdown table to stdout (or JSON with --json) and, always, KEYS-STATUS.md at the repo
root (--out to write elsewhere), with a first line `keys: N present, M working, last probe
<UTC time>` that tools/room.py --start surfaces, and a "Changes since last probe" section against
the previous KEYS-STATUS.md, if one exists, so a key going from absent/failing to present/working
is visible without a diff.

Not the same tool as tools/key_probe.py (parent 7d, 25 Sept 2026 22:44 UTC): that one checks, by
NAME only, which credential variables this container carries against KEYS.md and keeps the two
accounts' registers in sync (`--sync`); it never makes a network call. This one is the other half
-- for the credentials that have a documented API call, does the call actually succeed. Both are
useful and neither replaces the other; a fresh session runs both (`tools/room.py --start` already
runs key_probe.py --sync; run this one when a brief names an external host, per CLAUDE.md's
Access playbook "Key probe" paragraph).

Exit code is always 0: a failing or absent credential is a table row, never a crash (a dead host,
a network block, or a missing key must not stop a check-in that calls this first).

Test: python3 tools/tests/test_key_livecheck.py (offline: monkeypatched os.environ, a stubbed HTTP
layer -- no network -- and a temp KEYS-STATUS.md/cache path).
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_PATH = os.path.join(ROOT, "tools", ".key_livecheck_cache.json")
STATUS_PATH = os.path.join(ROOT, "KEYS-STATUS.md")
UA = "cipher-lab research script (contact via repository)"
DELAY = 1.5  # seconds between live calls to different hosts (CLAUDE.md good-citizen rule)


def _env(*names):
    for n in names:
        v = os.environ.get(n, "")
        if v.strip():
            return v.strip()
    return ""


def default_http(url, method="GET", headers=None, data=None, timeout=30):
    """Real network call. Returns (status_code_or_None, body_bytes). Never raises."""
    req = urllib.request.Request(url, method=method, headers=dict(headers or {}, **{"User-Agent": UA}), data=data)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.getcode(), r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        return None, str(e).encode("utf-8", "replace")


def redact(text, secrets):
    for s in secrets:
        if s:
            text = text.replace(s, "[REDACTED]")
    return text


def _json_or_none(body):
    try:
        return json.loads(body)
    except (ValueError, TypeError):
        return None


# ---------------------------------------------------------------- test functions
# Each takes (value(s), http) and returns (ok: bool or None, detail: str). ok=None means "no
# live test defined" (presence-only, or no documented call exists yet). detail never contains a
# credential value -- values passed in are redacted out of any echoed error body.

def test_google_books(key, http):
    shown = "https://www.googleapis.com/books/v1/volumes?q=cipher&country=US&maxResults=1"
    code, body = http(shown + f"&key={urllib.parse.quote(key)}")
    d = _json_or_none(body)
    if code == 200 and d is not None:
        return True, f'HTTP 200, totalItems={d.get("totalItems")} ({shown}&key=...)'
    return False, redact(f"HTTP {code}: {body[:200].decode('utf-8','replace')}", [key])


def test_openalex(key, http):
    url = "https://api.openalex.org/works?search=cipher&per-page=1"
    code, body = http(url, headers={"Authorization": f"Bearer {key}"})
    d = _json_or_none(body)
    if code == 200 and d is not None:
        return True, f'HTTP 200, meta.count={d.get("meta", {}).get("count")} ({url})'
    return False, redact(f"HTTP {code}: {body[:200].decode('utf-8','replace')}", [key])


def test_s2(key, http):
    url = "https://api.semanticscholar.org/graph/v1/paper/search?limit=1&query=cipher"
    code, body = http(url, headers={"x-api-key": key})
    d = _json_or_none(body)
    if code == 200 and d is not None:
        return True, f'HTTP 200, total={d.get("total")} ({url})'
    return False, redact(f"HTTP {code}: {body[:200].decode('utf-8','replace')}", [key])


def test_europeana(key, http):
    shown = "https://api.europeana.eu/record/v2/search.json?query=cipher&rows=1"
    code, body = http(shown + f"&wskey={urllib.parse.quote(key)}")
    d = _json_or_none(body)
    if code == 200 and d is not None:
        ok = d.get("success") is True
        return ok, f'HTTP 200, success={d.get("success")}, totalResults={d.get("totalResults")} ({shown}&wskey=...)'
    return False, redact(f"HTTP {code}: {body[:200].decode('utf-8','replace')}", [key])


def test_dpla(key, http):
    shown = "https://api.dp.la/v2/items?q=cipher&page_size=1"
    code, body = http(shown + f"&api_key={urllib.parse.quote(key)}")
    d = _json_or_none(body)
    if code == 200 and d is not None:
        return True, f'HTTP 200, count={d.get("count")} ({shown}&api_key=...)'
    return False, redact(f"HTTP {code}: {body[:200].decode('utf-8','replace')}", [key])


def test_core(key, http):
    # CLAUDE.md, 25 Sept 2026 probe: without the trailing slash on v3/search/works/ the API
    # answers 301 to an HTML redirect instead of running the search.
    url = "https://api.core.ac.uk/v3/search/works/?q=cipher&limit=1"
    code, body = http(url, headers={"Authorization": f"Bearer {key}"})
    d = _json_or_none(body)
    if code == 200 and d is not None:
        return True, f'HTTP 200, totalHits={d.get("totalHits")} ({url})'
    return False, redact(f"HTTP {code}: {body[:200].decode('utf-8','replace')}", [key])


def test_ddb(key, http):
    return None, ('no documented test call yet -- CLAUDE.md as of 25 Sept 2026: "not visible ... '
                  're-probe from a fresh session, and check the variable name"; presence only')


def test_ape(key, http):
    return None, "no documented test call yet -- CLAUDE.md: institution-gated API, no confirmed endpoint or key set"


def test_ia_login(user, password, http):
    shown = "https://archive.org/services/xauthn/?op=login"
    data = urllib.parse.urlencode({"email": user, "password": password}).encode()
    code, body = http(shown, method="POST", data=data,
                       headers={"Content-Type": "application/x-www-form-urlencoded"})
    d = _json_or_none(body)
    if d is None:
        return False, redact(f"HTTP {code}, non-JSON response ({shown})", [user, password])
    ok = bool(d.get("success"))
    detail = f"HTTP {code}, success={ok}"
    if not ok:
        detail += f' ({d.get("values", {}).get("reason", d.get("error", "unknown"))})'
    return ok, redact(detail + f" ({shown})", [user, password])


# ---------------------------------------------------------------- credential registry

SINGLE_KEYS = [
    dict(id="google_books", label="Google Books (googleapis.com/books/v1)",
         env=("GOOGLE_BOOKS_KEY",), test=test_google_books),
    dict(id="openalex", label="OpenAlex (api.openalex.org)",
         env=("OPENALEX_KEY", "OPENALEX_API_KEY"), test=test_openalex),
    dict(id="s2", label="Semantic Scholar (api.semanticscholar.org)",
         env=("S2_KEY", "S2_API_KEY", "SEMANTIC_SCHOLAR_API_KEY"), test=test_s2),
    dict(id="europeana", label="Europeana (api.europeana.eu)",
         env=("EUROPEANA_API_KEY",), test=test_europeana),
    dict(id="dpla", label="DPLA (api.dp.la)",
         env=("DPLA_API_KEY",), test=test_dpla),
    dict(id="core", label="CORE (api.core.ac.uk)",
         env=("CORE_API_KEY",), test=test_core),
    dict(id="ddb", label="Deutsche Digitale Bibliothek (api.deutsche-digitale-bibliothek.de)",
         env=("DDB_API_KEY",), test=test_ddb),
    dict(id="ape", label="Archives Portal Europe",
         env=("APE_API_KEY",), test=test_ape),
]

# (id, label, env_user, env_pass, live test fn or None, note)
PAIR_KEYS = [
    dict(id="ia", label="Internet Archive login (archive.org xauthn)",
         env=("IA_USER", "IA_PASS"), test=test_ia_login, live_flag="ia_login",
         note="presence by default -- pass --ia-login for a worker's one live login attempt this session"),
    dict(id="decode", label="DECODE (de-crypt.org)",
         env=("DECODE_USER", "DECODE_PASS"), test=None, live_flag=None,
         note="presence-only always -- the playbook reserves the one login attempt per session for a worker that needs it"),
    dict(id="jstor", label="JSTOR (jstor.org)",
         env=("JSTOR_USER", "JSTOR_PASS"), test=None, live_flag=None,
         note="presence-only always -- Cloudflare blocks the cloud entirely, a login would only fail"),
]

# HathiTrust needs no key at all for the routes this repo uses (bibliographic API, HTRC Extracted
# Features) -- only a full Chrome User-Agent string, which is not a credential. No HATHI_* variable
# is named anywhere in CLAUDE.md's Access playbook; noted here so its absence from this table is
# not mistaken for an oversight.
NO_KEY_NEEDED = [
    dict(id="hathitrust", label="HathiTrust bibliographic/HTRC APIs",
         note="no credential -- needs a Chrome User-Agent string only, not a key (CLAUDE.md Access playbook item 1)"),
]


def load_cache():
    try:
        with open(CACHE_PATH, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, ValueError):
        return {}


def save_cache(c):
    try:
        os.makedirs(os.path.dirname(CACHE_PATH), exist_ok=True)
        with open(CACHE_PATH, "w", encoding="utf-8") as f:
            json.dump(c, f)
    except OSError:
        pass


def parse_previous_status(path):
    """Best-effort read of a prior KEYS-STATUS.md's table -> {label: (present, works_summary)}."""
    prev = {}
    try:
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return prev
    for line in lines:
        if not line.startswith("| ") or line.startswith("| Credential") or set(line.strip()) <= {"|", "-", " "}:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3:
            prev[cells[0]] = (cells[1], cells[2])
    return prev


def run_probe(http=default_http, now=None, cache=None, force=False, cooldown=900, do_ia_login=False, sleep=time.sleep):
    """Pure-ish core: returns a list of row dicts. `http` and `sleep` are injectable for the offline test."""
    now = now if now is not None else time.time()
    cache = cache if cache is not None else load_cache()
    rows = []
    first_live_call = True

    def maybe_sleep():
        nonlocal first_live_call
        if not first_live_call:
            sleep(DELAY)
        first_live_call = False

    for spec in SINGLE_KEYS:
        value = _env(*spec["env"])
        present = bool(value)
        row = {"id": spec["id"], "label": spec["label"], "present": present, "env": spec["env"]}
        if not present:
            row.update(works=False, detail="not present", checked_live=False)
            rows.append(row)
            continue
        cached = cache.get(spec["id"])
        if not force and cached and (now - cached.get("t", 0)) < cooldown:
            row.update(works=cached["ok"], detail=cached["detail"] + f" (cached, {int(now - cached['t'])}s old)",
                       checked_live=False)
            rows.append(row)
            continue
        maybe_sleep()
        ok, detail = spec["test"](value, http)
        if ok is not None:
            cache[spec["id"]] = {"t": now, "ok": ok, "detail": detail}
        row.update(works=ok, detail=detail, checked_live=True)
        rows.append(row)

    for spec in PAIR_KEYS:
        u = os.environ.get(spec["env"][0], "").strip()
        p = os.environ.get(spec["env"][1], "").strip()
        present = bool(u) and bool(p)
        row = {"id": spec["id"], "label": spec["label"], "present": present, "env": spec["env"]}
        live_wanted = spec["live_flag"] == "ia_login" and do_ia_login
        if not present:
            row.update(works=False, detail="not present", checked_live=False)
        elif spec["test"] is None or not live_wanted:
            row.update(works=None, detail=f"not attempted -- {spec['note']}", checked_live=False)
        else:
            maybe_sleep()
            ok, detail = spec["test"](u, p, http)
            row.update(works=ok, detail=detail, checked_live=True)
        rows.append(row)

    for spec in NO_KEY_NEEDED:
        rows.append({"id": spec["id"], "label": spec["label"], "present": None, "works": None,
                      "detail": spec["note"], "checked_live": False, "env": ()})

    save_cache(cache)
    return rows


def fmt_bool(v):
    return {True: "yes", False: "no", None: "n/a"}[v]


def render_markdown(rows, stamp):
    present_n = sum(1 for r in rows if r["present"] is True)
    working_n = sum(1 for r in rows if r["works"] is True)
    lines = [
        f"# Keys status ({stamp} UTC)",
        "",
        f"keys: {present_n} present, {working_n} working, last probe {stamp} UTC",
        "",
        "Generated by `python3 tools/key_livecheck.py` (CLAUDE.md Access playbook credentials). "
        "Values are never printed or logged, only presence (`os.environ`) and one documented "
        "test call's result per credential.",
        "",
        "| Credential | Present | Works | Detail |",
        "|---|---|---|---|",
    ]
    for r in rows:
        lines.append(f"| {r['label']} | {fmt_bool(r['present'])} | {fmt_bool(r['works'])} | {r['detail']} |")
    return "\n".join(lines) + "\n"


def render_changes(rows, prev):
    changes = []
    for r in rows:
        old = prev.get(r["label"])
        if old is None:
            continue
        old_present, old_works = old
        new_present, new_works = fmt_bool(r["present"]), fmt_bool(r["works"])
        if old_present != new_present or old_works != new_works:
            changes.append(f"- {r['label']}: present {old_present}->{new_present}, works {old_works}->{new_works}")
    if not changes:
        return "\n## Changes since last probe\n\nnone\n"
    return "\n## Changes since last probe\n\n" + "\n".join(changes) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true", help="print JSON to stdout instead of the Markdown table")
    ap.add_argument("--force", action="store_true", help="ignore the result cache, re-test every present key live")
    ap.add_argument("--cooldown", type=int, default=900, help="seconds a cached live result is reused (default 900)")
    ap.add_argument("--ia-login", action="store_true", dest="ia_login",
                     help="also run IA's live xauthn login test -- this session's one login attempt; never in an unattended check-in")
    ap.add_argument("--out", default=STATUS_PATH, help="where to write the Markdown status file (default KEYS-STATUS.md)")
    a = ap.parse_args(argv)

    prev = parse_previous_status(a.out)
    rows = run_probe(force=a.force, cooldown=a.cooldown, do_ia_login=a.ia_login)
    stamp = time.strftime("%Y-%m-%d %H:%M", time.gmtime())
    md = render_markdown(rows, stamp) + render_changes(rows, prev)
    with open(a.out, "w", encoding="utf-8") as f:
        f.write(md)

    if a.json:
        print(json.dumps({"stamp": stamp, "rows": rows}, indent=2))
    else:
        print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
