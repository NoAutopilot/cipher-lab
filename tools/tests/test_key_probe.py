"""Offline tests for tools/key_probe.py and tools/key_request.py: names only, no value printed, register sync. Runs under pytest or plain python."""
import importlib.util, io, os, pathlib, contextlib, tempfile, shutil
HERE = pathlib.Path(__file__).resolve().parents[1]
def load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
kp = load("key_probe")

REG = """# reg
| name | purpose | read by | requested (by, date, ASKS) | status | seen (account@UTC) |
|---|---|---|---|---|---|
| DECODE_USER | login | tools/x | owner | set | owner@2026-09-25T10:00 |
| DDB_API_KEY | ddb | scouts | ASKS 47 | requested | |
"""

def _tmp_register():
    d = tempfile.mkdtemp(); p = os.path.join(d, "KEYS.md"); open(p, "w").write(REG); return d, p

def test_probe_names_only():
    d, p = _tmp_register()
    try:
        env = {"DECODE_USER": "x", "NEW_THING_KEY": "y", "GH_TOKEN": "z", "USER": "root", "EMPTY_KEY": "", "PATH": "/bin", "GIT_CONFIG_KEY_0": "a"}
        present, unset, undoc = kp.probe(env, p)
        assert present == ["DECODE_USER", "NEW_THING_KEY"], present
        assert unset == ["DDB_API_KEY"], unset
        assert undoc == ["NEW_THING_KEY"], undoc
    finally: shutil.rmtree(d)

def test_sync_flips_requested_and_adds_undocumented():
    d, p = _tmp_register()
    try:
        env = {"DECODE_USER": "x", "DDB_API_KEY": "now-set", "NEW_THING_KEY": "y"}
        newly, undoc = kp.sync(env, p, account="ytbiz", now="2026-09-25T22:50")
        assert newly == ["DDB_API_KEY"] and undoc == ["NEW_THING_KEY"], (newly, undoc)
        txt = open(p).read()
        assert "| DDB_API_KEY | ddb | scouts | ASKS 47 | set | ytbiz@2026-09-25T22:50 |" in txt
        assert "owner@2026-09-25T10:00, ytbiz@2026-09-25T22:50" in txt
        assert "| NEW_THING_KEY | undocumented (document before use) |" in txt
        assert "now-set" not in txt and "x |" not in txt.replace("| DECODE_USER | login | tools/x |", "")
        # second sync on the same account changes nothing
        assert kp.sync(env, p, account="ytbiz", now="2026-09-25T23:00") == ([], [])
        assert "23:00" not in open(p).read()
    finally: shutil.rmtree(d)

def test_no_value_leaks_in_output():
    d, p = _tmp_register()
    saved_env, saved_keys = kp.os.environ, kp.KEYS
    kp.os.environ = {"DECODE_USER": "hunter2-value", "OTHER_SECRET": "s3cr3t-value"}; kp.KEYS = p
    try:
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf): kp.main(["--quiet"])
        out = buf.getvalue()
        assert "hunter2" not in out and "s3cr3t" not in out and "OTHER_SECRET" in out, out
    finally:
        kp.os.environ = saved_env; kp.KEYS = saved_keys; shutil.rmtree(d)

if __name__ == "__main__":
    test_probe_names_only(); test_sync_flips_requested_and_adds_undocumented(); test_no_value_leaks_in_output(); print("ok")
