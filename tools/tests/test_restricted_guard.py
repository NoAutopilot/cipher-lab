"""Offline test for tools/restricted_guard.py's allowed-lines rule (ASKS 156 option (a), 9 Oct 2026).
Must catch: a fingerprinted phrase on any line not in the allowed-lines file. Must not block: a line whose
whole-line fingerprint is listed. Run: python3 tools/tests/test_restricted_guard.py (exit 0 on pass)."""
import importlib.util, os, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("rg", os.path.join(HERE, "..", "restricted_guard.py"))
rg = importlib.util.module_from_spec(spec); spec.loader.exec_module(rg)

def run():
    with tempfile.TemporaryDirectory() as d:
        rg.ROOT = d
        os.makedirs(os.path.join(d, "tools"))
        phrase = "zzqx figure 17 4"
        fps = {rg.fp(phrase)}
        kept = "2026-01-01 00:00 | some lane | result zzqx figure 17 4 on the private tiles"
        repeat = "a later note repeating zzqx figure 17 4 in another file"
        open(os.path.join(d, "a.md"), "w").write(kept + "\n")
        open(os.path.join(d, "b.md"), "w").write(repeat + "\n")
        # no allowed-lines file: both lines are findings
        f = rg.scan(["a.md", "b.md"], fps)
        assert sorted(x[0] for x in f) == ["a.md", "b.md"], f
        # allow the kept line: a.md passes, b.md (the repeat) is still caught
        open(os.path.join(d, "tools", "restricted_allowed_lines.txt"), "w").write("# test\n" + rg.line_fp(kept) + "\n")
        f = rg.scan(["a.md", "b.md"], fps)
        assert [x[0] for x in f] == ["b.md"], f
        # the allowed line edited by one token is caught again
        open(os.path.join(d, "a.md"), "w").write(kept + " extra\n")
        f = rg.scan(["a.md"], fps)
        assert [x[0] for x in f] == ["a.md"], f
    print("test_restricted_guard: 3/3 ok")

if __name__ == "__main__":
    run()
