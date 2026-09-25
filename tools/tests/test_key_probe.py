"""Offline test for tools/key_probe.py: names only, platform names ignored, no value ever printed. Runs under pytest or plain python."""
import importlib.util, io, pathlib, contextlib
spec = importlib.util.spec_from_file_location("key_probe", pathlib.Path(__file__).resolve().parents[1] / "key_probe.py")
kp = importlib.util.module_from_spec(spec); spec.loader.exec_module(kp)


def test_probe_names_only():
    env = {"DECODE_USER": "x", "NEW_THING_KEY": "y", "GH_TOKEN": "z", "USER": "root", "EMPTY_KEY": "", "PATH": "/bin", "GIT_CONFIG_KEY_0": "a"}
    present, unset, undoc = kp.probe(env)
    assert present == ["DECODE_USER", "NEW_THING_KEY"], present
    assert "DECODE_PASS" in unset and "DECODE_USER" not in unset
    assert undoc == ["NEW_THING_KEY"], undoc


def test_no_value_leaks_in_output():
    saved = kp.os.environ
    kp.os.environ = {"DECODE_USER": "hunter2-value", "OTHER_SECRET": "s3cr3t-value"}
    try:
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            kp.main(["--quiet"])
        out = buf.getvalue()
    finally:
        kp.os.environ = saved
    assert "hunter2" not in out and "s3cr3t" not in out and "OTHER_SECRET" in out, out


if __name__ == "__main__":
    test_probe_names_only(); test_no_value_leaks_in_output(); print("ok")
