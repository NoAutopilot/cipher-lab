import importlib.util, pathlib
spec = importlib.util.spec_from_file_location("key_probe", pathlib.Path(__file__).resolve().parents[1] / "key_probe.py")
kp = importlib.util.module_from_spec(spec); spec.loader.exec_module(kp)


def test_probe_names_only():
    env = {"DECODE_USER": "x", "NEW_THING_KEY": "y", "GH_TOKEN": "z", "USER": "root", "EMPTY_KEY": "", "PATH": "/bin"}
    present, unset, undoc = kp.probe(env)
    assert present == ["DECODE_USER", "NEW_THING_KEY"]      # GH_TOKEN/USER ignored, empty not counted, PATH no match
    assert "DECODE_PASS" in unset and "DECODE_USER" not in unset
    assert undoc == ["NEW_THING_KEY"]


def test_no_value_leaks_in_output(capsys, monkeypatch):
    monkeypatch.setattr(kp.os, "environ", {"DECODE_USER": "hunter2-value", "OTHER_SECRET": "s3cr3t-value"})
    kp.main(["--quiet"]); out = capsys.readouterr().out
    assert "hunter2" not in out and "s3cr3t" not in out and "OTHER_SECRET" in out
