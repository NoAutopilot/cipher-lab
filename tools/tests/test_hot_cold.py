#!/usr/bin/env python3
"""Offline pytest test for tools/hot_cold.py and next_steps.py --hot-only (SYS1-HC, 5 Oct 2026).

Fixture folders under tmp_path; no network, no dependence on the real ciphers/ tree.
Each MUST-NOT case below is one the docstring of tools/hot_cold.py names (CLAUDE.md Usage 8a).

Run: /root/.local/bin/pytest tools/tests/test_hot_cold.py -q
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import hot_cold as hc  # noqa: E402
import next_steps as ns  # noqa: E402


def mk(root, folder, notes="Status: open\n", files=None):
    d = root / "ciphers" / folder
    d.mkdir(parents=True, exist_ok=True)
    (d / "NOTES.md").write_text(notes, encoding="utf-8")
    for name, text in (files or {}).items():
        p = d / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
    return d


def rows_by_folder(root):
    return {r["folder"]: r for r in hc.classify(str(root))}


# ---- what it catches -------------------------------------------------------------------------------------------

def test_structured_sources_make_hot(tmp_path):
    mk(tmp_path, "audit-period", files={"AUDIT.md": "Key source: `period` -- rebuilt from the key sheet.\n"})
    mk(tmp_path, "h-graded", files={"key.tsv": "code\tvalue\tgrade\n1\ta\tH\n2\tb\tH\n3\tc\tH\n"})
    mk(tmp_path, "gloss-c", files={"key.tsv": "code\tvalue\tgrade\tsource\n1\ta\tC\tgloss\n2\tb\tC\tgloss\n3\tc\tC\tgloss\n"})
    mk(tmp_path, "tomo-header", files={"key.tsv": "# Tomokiyo's reconstruction, cryptiana nevers.htm\nsign\tvalue\n"})
    mk(tmp_path, "subdir-key", files={"key/key_x.tsv": "# Bergenroth's 19th-c. reconstruction\nsign\tvalue\n"})
    mk(tmp_path, "progress-b")
    (tmp_path / "PROGRESS.tsv").write_text("# c\nname\tfolder\tksrc\nX\tprogress-b\tb+o\nY\tours-only\to\n",
                                           encoding="utf-8")
    mk(tmp_path, "ours-only")
    mk(tmp_path, "fs", notes="found-solved\n\nRead by someone else in 2020.\n")
    r = rows_by_folder(tmp_path)
    assert r["audit-period"]["hot_cold"] == "HOT" and r["audit-period"]["kind"] == "key"
    assert r["h-graded"]["kind"] == "key"
    assert r["gloss-c"]["kind"] == "gloss"
    assert r["tomo-header"]["kind"] == "key"
    assert r["subdir-key"]["kind"] == "key"
    assert r["progress-b"]["kind"] == "key" and "PROGRESS.tsv" in r["progress-b"]["evidence"]
    assert r["fs"]["kind"] == "key" and "found-solved" in r["fs"]["evidence"]


def test_affirmative_notes_sentences_make_hot(tmp_path):
    mk(tmp_path, "a", notes="Status: open\n\nThe volume carries a contemporary decipherment on f.12 beside the cipher.\n")
    mk(tmp_path, "b", notes="Status: open\n\n- Key: Le Tellier-Marca Cipher (sources/cryptiana/web/louisxiv0.htm).\n")
    mk(tmp_path, "c", notes="blocked\n\nR4 note: status set blocked -- the key (BnF fr.3642) is not on Gallica.\n")
    mk(tmp_path, "d", notes="open\n\nCipher no.60 (key transcribed by Daniel Bourdeau, CC BY 4.0).\n")
    r = rows_by_folder(tmp_path)
    assert r["a"]["kind"] == "decipherment"
    assert r["b"]["kind"] == "key"
    assert r["c"]["kind"] == "key", "a located shelfmarked key is HOT even if not online"
    assert r["d"]["kind"] == "key"
    assert "NOTES.md" in r["a"]["evidence"]


def test_pool_link_to_hot_member(tmp_path):
    mk(tmp_path, "member", files={"AUDIT.md": "Key: `published` (Tomokiyo).\n"})
    mk(tmp_path, "sib", notes="Status: open\n\nThis letter uses the same cipher as member, Tomokiyo no.60.\n")
    r = rows_by_folder(tmp_path)
    assert r["sib"]["hot_cold"] == "HOT" and r["sib"]["kind"] == "pool:member"


def test_pools_tsv_group(tmp_path):
    mk(tmp_path, "p1", files={"AUDIT.md": "Key: `period`\n"})
    mk(tmp_path, "p2")
    (tmp_path / "POOLS.tsv").write_text("group\tletters\tyears\tshelfmarks_arks\n g\t2\t1600\tp1; p2\n", encoding="utf-8")
    assert rows_by_folder(tmp_path)["p2"]["kind"] == "pool:p1"


# ---- what it must NOT count ------------------------------------------------------------------------------------

def test_bare_or_negated_key_mentions_stay_cold(tmp_path):
    neg = ("Status: open\n\n"
           "No decipherment, gloss or clear copy is mentioned anywhere in the folder.\n\n"
           "The key is lost; we looked for a period key in the volume.\n\n"
           "If a period key exists it would sit in fr.3642.\n\n"
           "Not found: a key, a decipherment, a clear copy or a Beilage.\n\n"
           "Nothing in second-opinions/ names a decipherment, gloss or clear copy.\n\n"
           "Some of which will have contemporary decipherments.\n\n"
           "**Item 44 as a deciphered copy of item 43?** Not on this evidence.\n\n"
           "The blocker is Ranzo's table or a clear copy.\n\n"
           "~~key printed (Bongars' cipher no.3)~~ -- wrong.\n\n"
           "A clear copy of letters that the envoy had sent in cipher. It is not a decipherment of this letter.\n\n"
           "The cipher uses a key; the key is a nomenclator.\n")
    mk(tmp_path, "neg", notes=neg)
    r = rows_by_folder(tmp_path)
    assert r["neg"]["hot_cold"] == "COLD", r["neg"]["evidence"]


def test_ours_key_is_not_a_key_source(tmp_path):
    mk(tmp_path, "ours", files={
        "AUDIT.md": "**Key: ours. Text: not known in print.**\n",
        "key.tsv": "code\tletter\tgrade\tsource\n1\ta\tS\tY8 anneal\n2\tb\tS\tY8 anneal\n3\tc\tM\tM2 correction\n",
    })
    mk(tmp_path, "numbering", files={
        "key.tsv": "# Working key for Tomokiyo's sign numbers, recovered by crib-matching the fragments\n"
                   "sign\tvalue\tgrade\n1\ta\tS\n"})
    mk(tmp_path, "anneal", files={"key.tsv": "# Best-scoring key of the joint anneal. NOT A READING\nr\tg\n"})
    r = rows_by_folder(tmp_path)
    for f in ("ours", "numbering", "anneal"):
        assert r[f]["hot_cold"] == "COLD", (f, r[f]["evidence"])


def test_pool_link_needs_hot_member_and_pool_word(tmp_path):
    mk(tmp_path, "coldmember")
    mk(tmp_path, "hotmember", files={"AUDIT.md": "Key: `period`\n"})
    mk(tmp_path, "x", notes="Status: open\n\nSame cipher as coldmember.\n\nSee also hotmember for the dates.\n\n"
                            "Sibling-key trial (hotmember's key) -- not applicable, not run.\n\n"
                            "Is hotmember's key the same cipher Tomokiyo names here?\n")
    assert rows_by_folder(tmp_path)["x"]["hot_cold"] == "COLD"


# ---- file, --check, next_steps --hot-only ----------------------------------------------------------------------

def test_render_and_check(tmp_path):
    mk(tmp_path, "a", files={"AUDIT.md": "Key: `period`\n"})
    mk(tmp_path, "b")
    out = tmp_path / "HOT-COLD.tsv"
    tool = os.path.join(ROOT, "tools", "hot_cold.py")
    assert subprocess.run([sys.executable, tool, "--root", str(tmp_path), "--check"], capture_output=True).returncode == 1
    p = subprocess.run([sys.executable, tool, "--root", str(tmp_path)], capture_output=True, text=True)
    assert p.returncode == 0 and "HOT 1 / COLD 1 / total 2" in p.stdout
    text = out.read_text(encoding="utf-8")
    assert text.startswith("# HOT-COLD.tsv") and "folder\thot_cold\tkind\tevidence\tpool\n" in text
    assert subprocess.run([sys.executable, tool, "--root", str(tmp_path), "--check"], capture_output=True).returncode == 0
    assert hc.load_hot(str(out)) == {"a"}


def test_next_steps_hot_only_filters_and_default_unchanged(tmp_path):
    hcfile = tmp_path / "HOT-COLD.tsv"
    hcfile.write_text("# c\nfolder\thot_cold\tkind\tevidence\tpool\nhot1\tHOT\tkey\tx\t\ncold1\tCOLD\t\t\t\n",
                      encoding="utf-8")
    assert ns.hot_folders(str(hcfile)) == {"hot1"}
    rows = [{"folder": "hot1"}, {"folder": "cold1"}, {"folder": "unlisted"}]
    assert ns.hot_only_rows(rows, ns.hot_folders(str(hcfile))) == [{"folder": "hot1"}]
    # end to end on fixture folders: --hot-only prints only the HOT folder and writes no --out file
    for f in ("hot1", "cold1"):
        mk(tmp_path, f, notes="# t\n\nStatus: open\n\nNext step: run the family on the control.\n")
    out = tmp_path / "NEXT-STEPS.tsv"
    tool = os.path.join(ROOT, "tools", "next_steps.py")
    common = ["--ciphers-dir", str(tmp_path / "ciphers"), "--ledger", str(tmp_path / "L.md"),
              "--near", str(tmp_path / "N.md"), "--out", str(out)]
    p = subprocess.run([sys.executable, tool, *common, "--hot-only", str(hcfile)], capture_output=True, text=True)
    assert p.returncode == 0
    body = [l.split("\t")[0] for l in p.stdout.splitlines()[1:] if not l.startswith("#")]
    assert body == ["hot1"] and not out.exists()
    p2 = subprocess.run([sys.executable, tool, *common, "--hot-only", str(tmp_path / "nope.tsv")], capture_output=True)
    assert p2.returncode == 2
    subprocess.run([sys.executable, tool, *common], capture_output=True, check=True)
    assert [l.split("\t")[0] for l in out.read_text().splitlines()[1:] if not l.startswith("#")] == ["cold1", "hot1"]
