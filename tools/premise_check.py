#!/usr/bin/env python3
"""Premise check before a LIKELY/SPLIT session is spawned: does the material the shortlist row's premise
cells name actually sit on disk, and is the item already counted? (RETRO-2026-10-02-account4 proposal 5,
applied 2 Oct 2026; CLAUDE.md Usage 8a -- a rule broken more than twice becomes a tool.)

    python3 tools/premise_check.py <slug> --row-text "<head_start cell>" [--new] [--no-decode]
                                   [--key PATH ...] [--needs-images] [--leaf f.21v] [--repo-root DIR]

Why it exists. In one window (1-2 Oct 2026, account-4) four sessions -- LIKELY-2, LIKELY-4, LIKELY-7 and
SPLIT-matignon -- spent USD 19.77 on rows of `ciphers/_triage/likely-solves-2026-10-02.tsv` whose `head_start`
cell named material that was not on disk or an item already counted: LIKELY-4's "sibling folder
decode-1168-modena-costabili-1492 is partial with a key" named a folder holding only NOTES.md and no key file;
SPLIT-matignon's 0 of 31 hits had an image on disk; LIKELY-2's f.21v and f.87 were already in NEAR.md's "Why
it left" table. Each was a fact a script can read before `create_session`; none was read.

This is the PARENT's pre-spawn check of the shortlist row's premise cells against the folder. The worker-side
counterpart is `.claude/briefs/check-solved.md`'s "## Premise check" section (account 3, 12:47 UTC 2 Oct 2026:
the adversarial pre-reading pass -- decipherments the folder already mentions, other solvers' working files,
neighbouring leaves, recipient-side editions), which `tools/intake_gate_check.py` requires in NOTES.md before
an open/partial target's first test. The two do not overlap: this tool asks "is what the row says is on disk,
on disk, and is the item not already counted"; that section asks "has anyone already read it".

Checks, in order; exit 1 names the FIRST failure (so the parent fixes one thing and re-runs):
  (a) `ciphers/<slug>/` exists, and a non-empty ciphertext file is on disk (`ciphertext.txt`/`.tsv` at the
      root, or any `*ciphertext*.txt|tsv` / `*_ct.txt|tsv` under a subfolder -- ceppo-nevers keeps per-leaf
      files under harvest/ and witness/) -- the step decodes unless `--no-decode` says the first cheap test
      is a print or catalogue check, or the row text itself says the step transcribes or fetches the text
      first (crops, blind passes, iiif_lines, reconcile, "transcription"), which passes with a note.
  (b) every path the row text names (`keys/...`, `ciphers/...`, `tools/...`, `specs/...`, any `*.tsv`,
      `*.txt`, `*.json`) and every `--key PATH` exists, resolved against the repo root and then the target
      folder; and every sibling folder the row names alongside the word "key" (LIKELY-4's shape) exists and
      holds a key file (a non-empty `*key*.tsv|txt|json` anywhere up to three levels down -- pro3055-clinton-
      1779 keeps `passes/key_2894.tsv`; decode-1168-modena-costabili-1492 holds only NOTES.md).
  (c) with `--needs-images`: `images/manifest.json` exists in the folder and lists the leaf named by `--leaf`
      (or the first `f.N`/`ff.N` token in the row text).
  (d) the slug is not in NEAR.md's "Why it left" table -- a row whose first cell starts with the slug and
      either names the same leaf or names no leaf at all (a whole-target row).

Must catch (row kinds this tool exists for): a `head_start` cell naming a key path or sibling key that is not
on disk (LIKELY-4); a SPLIT nomination whose hits' leaf has no image in the manifest (SPLIT-matignon); a
leaf already counted in NEAR.md "Why it left" (LIKELY-2: ceppo-nevers f.21v, f.87); a folder whose
ciphertext.txt is empty while the step decodes.
Must NOT block: a `new` row with no folder yet (`--new`; likely-phase2.md step 2 creates it -- checks (b) and
(d) still run on the row text and slug, (a) and (c) report "new row"); a target whose NEAR.md rows name
other leaves than the one this step reads (ceppo-nevers f.35 while f.21v and f.87 are counted); a print-check
first test with no ciphertext on disk (`--no-decode`); a row that names a path only inside a web URL.
Offline test: tools/tests/test_premise_check.py (temp repo root via `--repo-root`).
"""
import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# a path-looking token in free text: a repo-relative path under one of the named top folders, or any bare
# file name with a data extension; trailing punctuation is stripped. Tokens inside a URL are ignored (b).
PATH_RE = re.compile(
    r'(?<![\w/:.])((?:ciphers|keys|tools|specs|sources|images)/[\w./\-]+|[\w\-]+(?:/[\w\-]+)*\.(?:tsv|txt|json))',
    re.IGNORECASE,
)
URL_RE = re.compile(r'https?://\S+|\b[\w.-]+\.(?:com|org|fr|uk|net|edu|gov|de|pt|es|it|nl)/\S*', re.IGNORECASE)
SLUG_RE = re.compile(r'\b([a-z0-9]+(?:-[a-z0-9]+){2,})\b')
LEAF_RE = re.compile(r'\bff?\.\s?(\d+[rv]?)\b|\bfolio\s+(\d+[rv]?)\b', re.IGNORECASE)
KEY_NAME_RE = re.compile(r'key.*\.(?:tsv|txt|json)$|\.key$', re.IGNORECASE)
CT_NAME_RE = re.compile(r'ciphertext.*\.(?:txt|tsv)$|_ct\.(?:txt|tsv)$', re.IGNORECASE)
TRANSCRIBES_RE = re.compile(r'\b(?:crops?|blind (?:sonnet )?pass(?:es)?|iiif_lines|reconcil\w*|transcri\w*|thumbnails?)\b',
                            re.IGNORECASE)
WALK_DEPTH = 3


def strip_punct(tok):
    return tok.rstrip(".,;:)]'\"")


def leaf_of(text):
    """The first f.N / ff.N / folio N token in text, normalised to e.g. '21v' or '87' (lower-case), or None."""
    if not text:
        return None
    m = LEAF_RE.search(text)
    if not m:
        return None
    return (m.group(1) or m.group(2)).lower()


def normalise_leaf(label):
    """'f.21v' / 'ff.21v' / 'folio 21v' / '21v' -> '21v'."""
    if label is None:
        return None
    label = label.strip()
    return leaf_of(label) or re.sub(r'^(?:ff?\.?\s*|folio\s+)', '', label, flags=re.IGNORECASE).lower()


def named_paths(row_text):
    """Path-looking tokens in the row text, URLs removed, order kept, duplicates dropped."""
    if not row_text:
        return []
    text = URL_RE.sub(" ", row_text)
    out = []
    for m in PATH_RE.finditer(text):
        tok = strip_punct(m.group(1))
        if tok and tok not in out:
            out.append(tok)
    return out


def named_sibling_folders(row_text, ciphers_dir, slug):
    """Slug-like tokens in the row text (three or more hyphenated parts) other than the target's own slug,
    with whether the text mentions a key at all."""
    if not row_text:
        return [], False
    text = URL_RE.sub(" ", row_text)
    sibs = []
    for m in SLUG_RE.finditer(text):
        tok = m.group(1)
        if tok == slug or tok in sibs:
            continue
        # only folder-shaped tokens: a word that is or could be a ciphers/ folder name (has a digit or 'decode')
        if not re.search(r'\d', tok):
            continue
        sibs.append(tok)
    mentions_key = re.search(r'\bkeys?\b', text, re.IGNORECASE) is not None
    return sibs, mentions_key


def find_file(folder, name_re, depth=WALK_DEPTH):
    """First non-empty file under folder (up to `depth` levels) whose name matches name_re, or None;
    hidden dirs and the images/ tree are skipped."""
    base_depth = folder.rstrip(os.sep).count(os.sep)
    for dirpath, dirnames, filenames in os.walk(folder):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith(".") and d != "images")
        if dirpath.count(os.sep) - base_depth >= depth:
            dirnames[:] = []
        for fn in sorted(filenames):
            if name_re.search(fn):
                full = os.path.join(dirpath, fn)
                if os.path.isfile(full) and os.path.getsize(full) > 0:
                    return full
    return None


def folder_has_key(folder):
    return find_file(folder, KEY_NAME_RE)


def folder_has_ciphertext(folder):
    for fn in ("ciphertext.txt", "ciphertext.tsv"):
        full = os.path.join(folder, fn)
        if os.path.isfile(full) and os.path.getsize(full) > 0:
            return full
    return find_file(folder, CT_NAME_RE)


def resolve(path, repo_root, target_dir):
    cands = [path if os.path.isabs(path) else os.path.join(repo_root, path)]
    if target_dir:
        cands.append(os.path.join(target_dir, path))
    for c in cands:
        if os.path.exists(c):
            return c
    return None


def near_rows(near_text):
    """(first_cell, leaf_or_None) per row of the 'Why it left' table in NEAR.md text; [] when absent."""
    lines = near_text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.startswith("|") and "why it left" in line.lower():
            start = i
            break
    if start is None:
        return []
    rows = []
    for line in lines[start + 1:]:
        if not line.startswith("|"):
            if rows:
                break
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or set(cells[0]) <= set("-: "):
            continue
        rows.append((cells[0], leaf_of(cells[0])))
    return rows


def manifest_lists_leaf(manifest_path, leaf):
    """True when the manifest text mentions the leaf as f<leaf>, f.<leaf>, "folio": "<leaf>" or a bare
    word <leaf> next to 'f' -- the repo's manifests are hand-written and vary (dict keyed by file name with
    a `folio` field; a `fetched` log; a list)."""
    with open(manifest_path, encoding="utf-8") as f:
        text = f.read()
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        data = None
    if isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, dict) and str(v.get("folio", "")).lower() == leaf:
                return True
            if re.search(rf'(?<![\w.])f\.?{re.escape(leaf)}(?![\w])', str(k), re.IGNORECASE):
                return True
    pat = re.compile(rf'(?<![\w])f\.?\s?{re.escape(leaf)}(?![\w])|"folio"\s*:\s*"{re.escape(leaf)}"', re.IGNORECASE)
    return pat.search(text) is not None


def check(slug, row_text="", keys=(), needs_images=False, leaf=None, new=False, no_decode=False, repo_root=ROOT):
    """Pure check: returns (exit_code, lines). Exit 1 at the first failure, its line last."""
    ciphers_dir = os.path.join(repo_root, "ciphers")
    target_dir = os.path.join(ciphers_dir, slug)
    out = []
    leaf = normalise_leaf(leaf) if leaf else leaf_of(row_text)

    # (a) folder and ciphertext
    if not os.path.isdir(target_dir):
        if new:
            out.append(f"(a) new row: no ciphers/{slug}/ yet (the step creates it) -- ok")
            target_dir = None
        else:
            out.append(f"(a) FAIL: ciphers/{slug}/ does not exist (pass --new for a `new` shortlist row)")
            return 1, out
    else:
        ct = folder_has_ciphertext(target_dir)
        rel = os.path.relpath(ct, target_dir) if ct else None
        if no_decode:
            out.append(f"(a) ciphers/{slug}/ exists; ciphertext {rel or 'absent'}, not required (--no-decode) -- ok")
        elif ct is None and TRANSCRIBES_RE.search(row_text or ""):
            out.append(f"(a) ciphers/{slug}/ exists; no ciphertext file yet, and the row says the step transcribes "
                       f"or fetches it first ({TRANSCRIBES_RE.search(row_text).group(0)!r}) -- ok, note it is not on disk")
        elif ct is None:
            out.append(f"(a) FAIL: ciphers/{slug}/ has no non-empty ciphertext file (ciphertext.txt/.tsv or *ciphertext*/"
                       f"*_ct under a subfolder) and the step decodes (pass --no-decode only for a print/catalogue-only "
                       f"first test, or say in the row text that the step transcribes first)")
            return 1, out
        else:
            out.append(f"(a) ciphers/{slug}/ exists, {rel} {os.path.getsize(ct)} bytes -- ok")

    # (b) named paths and sibling keys
    paths = list(keys) + named_paths(row_text)
    for p in paths:
        r = resolve(p, repo_root, target_dir)
        if r is None:
            out.append(f"(b) FAIL: head_start names {p!r} and it is not on disk under the repo root or ciphers/{slug}/ "
                       f"(if it lives in another repository, the row must say the step fetches it first)")
            return 1, out
    sibs, mentions_key = named_sibling_folders(row_text, ciphers_dir, slug)
    for sib in sibs:
        sib_dir = os.path.join(ciphers_dir, sib)
        if not os.path.isdir(sib_dir):
            out.append(f"(b) FAIL: head_start names folder {sib!r} and ciphers/{sib}/ does not exist")
            return 1, out
        if mentions_key and folder_has_key(sib_dir) is None:
            out.append(f"(b) FAIL: head_start names sibling {sib!r} alongside a key, and ciphers/{sib}/ holds no non-empty "
                       f"*key*.tsv|txt|json file up to {WALK_DEPTH} levels down -- LIKELY-4's shape, 2 Oct 2026")
            return 1, out
    out.append(f"(b) {len(paths)} named path(s) on disk, {len(sibs)} sibling folder(s) present"
               + (" with a key file" if sibs and mentions_key else "") + " -- ok")

    # (c) images
    if needs_images:
        if target_dir is None:
            out.append("(c) new row: no folder, so no manifest to check yet -- ok")
        else:
            man = os.path.join(target_dir, "images", "manifest.json")
            if not os.path.isfile(man):
                out.append(f"(c) FAIL: --needs-images but ciphers/{slug}/images/manifest.json does not exist "
                           f"(SPLIT-matignon's shape: 0 of 31 hits had an image on disk)")
                return 1, out
            if leaf is None:
                out.append("(c) FAIL: --needs-images but no leaf named (pass --leaf f.N, or name f.N in --row-text)")
                return 1, out
            if not manifest_lists_leaf(man, leaf):
                out.append(f"(c) FAIL: images/manifest.json does not list leaf f.{leaf}")
                return 1, out
            out.append(f"(c) images/manifest.json lists f.{leaf} -- ok")
    else:
        out.append("(c) images not required for this step")

    # (d) NEAR.md "Why it left"
    near_path = os.path.join(repo_root, "NEAR.md")
    rows = []
    if os.path.isfile(near_path):
        with open(near_path, encoding="utf-8") as f:
            rows = near_rows(f.read())
    hits = [(cell, rl) for cell, rl in rows if cell.startswith(slug)]
    for cell, rl in hits:
        if leaf is None or rl is None or rl == leaf:
            out.append(f"(d) FAIL: already counted in NEAR.md 'Why it left': {cell[:100]!r}"
                       + (f" (this step reads f.{leaf})" if leaf else "")
                       + " -- LIKELY-2's shape, 2 Oct 2026")
            return 1, out
    if hits:
        out.append(f"(d) NEAR.md 'Why it left' has {len(hits)} row(s) for {slug} naming other leaves "
                   f"({', '.join('f.' + (rl or '?') for _, rl in hits)}), this step reads f.{leaf} -- ok")
    else:
        out.append(f"(d) not in NEAR.md 'Why it left' -- ok")
    return 0, out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug", help="ciphers/<slug> folder name (the shortlist row's folder cell, without ciphers/)")
    ap.add_argument("--row-text", default="", help="the row's head_start cell (and first_cheap_test, if useful)")
    ap.add_argument("--key", action="append", default=[], help="a key path the step applies; may repeat")
    ap.add_argument("--needs-images", action="store_true", help="the step reads an image: require the leaf in images/manifest.json")
    ap.add_argument("--leaf", help="the leaf the step reads (f.21v); default: the first f.N token in --row-text")
    ap.add_argument("--new", action="store_true", help="the shortlist row is `new`: no folder yet is not a failure")
    ap.add_argument("--no-decode", action="store_true", help="the first test reads no ciphertext (print/catalogue check)")
    ap.add_argument("--repo-root", default=ROOT, help=argparse.SUPPRESS)
    args = ap.parse_args(argv)
    slug = args.slug.rstrip("/")
    if slug.startswith("ciphers/"):
        slug = slug[len("ciphers/"):]
    code, lines = check(slug, args.row_text, args.key, args.needs_images, args.leaf, args.new, args.no_decode,
                        args.repo_root)
    print(f"premise_check {slug}: {'FAIL' if code else 'ok'}")
    for line in lines:
        print("  " + line)
    return code


if __name__ == "__main__":
    sys.exit(main())
