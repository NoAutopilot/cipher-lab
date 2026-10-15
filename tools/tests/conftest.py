"""pytest adapter for tools/tests (SORTER-FIX-R12-R16, 15 Oct 2026).

Most files here are scripts: they run their checks at import and end in sys.exit(0 or 1), so `python3 -m pytest tools/tests ...`
used to stop at collection with "caught unexpected SystemExit" and ran nothing. A file with no top-level `def test_` is collected
here as one item that runs `python3 FILE` from the repository root and passes on exit 0 (a failure shows the last 40 lines of its
output); so is a file that also defines `def test_` but ends in a bare module-level sys.exit. Other files with `def test_` functions are collected by pytest as usual. Item names are the file stem, so `-k sorter` selects
every file whose name holds "sorter". Catches: a script test failing under pytest. Must NOT: import a script test (its sys.exit
would end the collection), or change how a pytest-style file is collected.
"""
import os
import re
import subprocess
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _is_script(path):
    try:
        src = open(path, encoding='utf-8', errors='ignore').read()
    except OSError:
        return False
    # no pytest functions, or a bare module-level sys.exit (the file runs its checks at import, whatever else it defines)
    return not re.search(r'^def test_', src, re.M) or bool(re.search(r'^sys\.exit\(', src, re.M))


def pytest_pycollect_makemodule(module_path, parent):
    if os.path.basename(str(module_path)).startswith('test_') and _is_script(str(module_path)):
        return ScriptFile.from_parent(parent, path=module_path)
    return None


class ScriptFile(pytest.File):
    def collect(self):
        yield ScriptItem.from_parent(self, name=self.path.stem)


class ScriptItem(pytest.Item):
    def runtest(self):
        r = subprocess.run([sys.executable, str(self.path)], cwd=ROOT, capture_output=True, text=True, timeout=1800)
        if r.returncode != 0:
            tail = '\n'.join((r.stdout + r.stderr).splitlines()[-40:])
            raise AssertionError(f'{self.path.name} exited {r.returncode}:\n{tail}')

    def repr_failure(self, excinfo):
        return str(excinfo.value)

    def reportinfo(self):
        return self.path, 0, self.name
