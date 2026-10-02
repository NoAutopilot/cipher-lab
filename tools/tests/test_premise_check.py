#!/usr/bin/env python3
"""Offline test for tools/premise_check.py (RETRO-2026-10-02-account4 proposal 5, 2 Oct 2026).

Builds a throwaway repo root (ciphers/ folders, NEAR.md with a "Why it left" table) and pins, per the tool's
docstring: must catch (a) a decoding step with an empty ciphertext.txt, (b) a head_start naming a key path not
on disk and a sibling folder named with "key" that holds no key file (LIKELY-4), (c) a SPLIT row whose leaf has
no image in the manifest (SPLIT-matignon), (d) a leaf already in NEAR.md "Why it left" (LIKELY-2); must NOT block
a `new` row with no folder, a target whose NEAR.md rows name other leaves, a print-check first test with
`--no-decode`, and a path that appears only inside a URL.
Run: python3 tools/tests/test_premise_check.py"""
import json
import os
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import premise_check as pc  # noqa: E402

fails = 0


def expect(label, got, code, needle=None):
    global fails
    gcode, lines = got
    ok = gcode == code and (needle is None or any(needle in line for line in lines))
    fails += not ok
    print(("PASS" if ok else "FAIL"), label, f"-> code={gcode} last={lines[-1][:110]!r}")


def write(path, text=""):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


with tempfile.TemporaryDirectory() as tmp:
    C = os.path.join(tmp, "ciphers")
    # a healthy target: ciphertext, a key, a manifest listing f.21v (dict-with-folio shape) and f.11r (key shape)
    write(os.path.join(C, "good-target-1570", "ciphertext.txt"), "12 34 56\n")
    write(os.path.join(C, "good-target-1570", "keys", "key_good.tsv"), "12\ta\n")
    write(os.path.join(C, "good-target-1570", "images", "manifest.json"), json.dumps({
        "f11r_canvas12.jpg": {"folio": "11r", "canvas": 12},
        "f21v_canvas23.jpg": {"folio": "21v", "canvas": 23},
    }))
    # a sibling folder with only NOTES.md (LIKELY-4's decode-1168 shape) and one with a key
    write(os.path.join(C, "sib-nokey-1492", "NOTES.md"), "Status: partial\n")
    write(os.path.join(C, "sib-key-1492", "NOTES.md"), "Status: partial\n")
    write(os.path.join(C, "sib-key-1492", "key.tsv"), "1\ta\n")
    # an empty-ciphertext target and a manifest-less target
    write(os.path.join(C, "empty-ct-1600", "ciphertext.txt"), "")
    write(os.path.join(C, "no-images-1586", "ciphertext.txt"), "1 2 3\n")
    write(os.path.join(tmp, "NEAR.md"), "\n".join([
        "# NEAR", "", "## Left", "",
        "| Target | Why it left | Date |", "|---|---|---|",
        "| whole-target-1646 (f.10, 735 tokens) | counted | 2 Oct |",
        "| good-target-1570 f.21v (Birago to Nevers, 12 Oct 1570) | counted | 29 Sept |",
        "| good-target-1570 f.87 (Birago to Nevers, 9 May 1571) | counted | 29 Sept |",
        "", "## After", "",
    ]) + "\n")
    # the NEAR.md row "whole-target-1646 (f.10 ...)" names leaf f.10 -> a step on f.10 is caught, f.9 passes
    write(os.path.join(C, "whole-target-1646", "ciphertext.txt"), "1 2\n")

    # ceppo-nevers shape: per-leaf ciphertext under a subfolder, no root ciphertext.txt
    write(os.path.join(C, "subdir-ct-1570", "harvest", "f11r_ciphertext.tsv"), "1\t2\n")
    # pro3055 shape: key material two levels down, not at the root
    write(os.path.join(C, "sib-deepkey-1779", "NOTES.md"), "Status: partial\n")
    write(os.path.join(C, "sib-deepkey-1779", "passes", "key_2894.tsv"), "1\ta\n")
    write(os.path.join(C, "no-ct-yet-1492", "NOTES.md"), "Status: open\n")

    R = dict(repo_root=tmp)
    # must NOT block: ciphertext under a subfolder; a sibling whose key sits in passes/; a step that transcribes first
    expect("ciphertext under harvest/ passes (a)", pc.check("subdir-ct-1570", "f.35", **R), 0, "harvest/f11r_ciphertext.tsv")
    expect("sibling key two levels down", pc.check("good-target-1570", "a: sibling sib-deepkey-1779 holds key material; f.35", **R), 0, "with a key file")
    expect("no ciphertext, step transcribes first (crops, blind passes)",
           pc.check("no-ct-yet-1492", "iiif_lines crops, 2 blind passes + reconcile, then decode", **R), 0, "transcribes or fetches it first")
    expect("no ciphertext, row mentions a public transcription",
           pc.check("no-ct-yet-1492", "b: DECODE status with a public Transcription document", **R), 0, "transcribes or fetches it first")
    expect("no ciphertext, step just decodes", pc.check("no-ct-yet-1492", "apply the key", **R), 1, "(a) FAIL")
    # must NOT block: a healthy row reading a leaf not counted in NEAR.md, key path on disk
    expect("healthy row, f.35, key on disk",
           pc.check("good-target-1570", "a: keys/key_good.tsv on disk; f.35 no.18 next", needs_images=False, **R), 0, "(d) NEAR.md")
    # must catch (d): a leaf already counted
    expect("LIKELY-2 shape: f.21v already in Why it left",
           pc.check("good-target-1570", "f.21v no.11 with keys/key_good.tsv", **R), 1, "(d) FAIL")
    expect("LIKELY-2 shape via --leaf", pc.check("good-target-1570", "", leaf="ff.87", **R), 1, "(d) FAIL")
    # must NOT block: a whole-target NEAR row that itself names a leaf (f.10) does not block a step on f.9
    expect("NEAR row names f.10, step reads f.9", pc.check("whole-target-1646", "f.9 opening", **R), 0, "(d) NEAR.md")
    expect("NEAR row names f.10, step reads f.10", pc.check("whole-target-1646", "f.10 tokens", **R), 1, "(d) FAIL")
    expect("NEAR row names f.10, step names no leaf", pc.check("whole-target-1646", "apply the key", **R), 1, "(d) FAIL")
    # must catch (b): a key path not on disk; a sibling named with 'key' holding no key file
    expect("key path not on disk", pc.check("good-target-1570", "a: keys/key_missing.tsv (Tomokiyo) on disk; f.35", **R), 1, "(b) FAIL")
    expect("LIKELY-4 shape: sibling folder with no key",
           pc.check("good-target-1570", "a: sibling folder sib-nokey-1492 is partial with a key; f.35", **R), 1, "holds no non-empty")
    expect("sibling folder with a key passes",
           pc.check("good-target-1570", "a: sibling folder sib-key-1492 is partial with a key; f.35", **R), 0, "(b) 0 named path(s)")
    expect("sibling folder that does not exist",
           pc.check("good-target-1570", "a: sibling folder sib-ghost-1492 holds the key; f.35", **R), 1, "does not exist")
    # must NOT block: a path that appears only inside a URL
    expect("path only inside a URL",
           pc.check("good-target-1570", "transcription free at https://github.com/x/y/blob/main/keys/key129.txt; f.35", **R), 0, "(b) 0 named path(s)")
    # bare file name resolved against the target folder
    expect("bare key file name resolves in the folder", pc.check("sib-key-1492", "apply key.tsv to it", no_decode=True, **R), 0, "(b) 1 named path(s)")
    # must catch (a): empty ciphertext when the step decodes; must NOT block with --no-decode
    expect("empty ciphertext, step decodes", pc.check("empty-ct-1600", "apply the key", **R), 1, "(a) FAIL")
    expect("empty ciphertext, print check only", pc.check("empty-ct-1600", "print check first", no_decode=True, **R), 0, "(d) not in NEAR.md")
    # must NOT block: a `new` row with no folder; must catch a missing folder without --new
    expect("new row, no folder", pc.check("brand-new-1780", "b/c: Saberton 2010 may print the deciphers", new=True, **R), 0, "(a) new row")
    expect("missing folder without --new", pc.check("brand-new-1780", "", **R), 1, "(a) FAIL")
    expect("new row with --needs-images reports, does not fail",
           pc.check("brand-new-1780", "f.12", new=True, needs_images=True, **R), 0, "(c) new row")
    # must catch (c): SPLIT-matignon's shape -- no manifest; a manifest without the leaf; no leaf named
    expect("SPLIT-matignon shape: no manifest", pc.check("no-images-1586", "f.78v hits", needs_images=True, **R), 1, "(c) FAIL")
    expect("manifest lacks the leaf", pc.check("good-target-1570", "f.99 hits", needs_images=True, **R), 1, "does not list leaf f.99")
    expect("manifest lists the leaf (folio field)", pc.check("good-target-1570", "f.11r hits", needs_images=True, **R), 0, "(c) images/manifest.json lists f.11r")
    expect("needs-images but no leaf named", pc.check("good-target-1570", "the hits", needs_images=True, **R), 1, "no leaf named")
    # --key paths are checked like named paths
    expect("--key present", pc.check("good-target-1570", "f.35", keys=["keys/key_good.tsv"], **R), 0, "(b) 1 named path(s)")
    expect("--key absent", pc.check("good-target-1570", "f.35", keys=["keys/nope.tsv"], **R), 1, "(b) FAIL")

if fails:
    print(f"{fails} failure(s)")
    sys.exit(1)
print("ok: premise_check catches an empty ciphertext, a missing key path, a sibling folder without a key, a leaf "
      "missing from the manifest and a leaf already in NEAR.md 'Why it left', and does not block a new row, a "
      "no-decode print check, a URL-only path or a target whose NEAR.md rows name other leaves")
