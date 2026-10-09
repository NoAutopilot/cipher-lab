#!/usr/bin/env python3
"""Restricted-material guard for this PUBLIC repository.

Some holders share material with the project on condition that it is never published (the first is the
Adirondack History Museum's Debosnys scans, 28 Sept 2026; see ciphers/debosnys-1883/RESTRICTED.md). That
material lives only in the private repository NoAutopilot/cipher-lab-private. This guard is the backstop that
stops it reaching this one by mistake.

It never stores the protected words themselves. tools/restricted_fingerprints.txt holds one-way fingerprints
(SHA-256, first 16 hex digits) of distinctive single words, short phrases and sign sequences taken from the
restricted material; the guard fingerprints the same units in every text file and reports any match. Only long
or invented words and multi-word phrases are fingerprinted, so a fingerprint cannot be reversed by guessing
common words.

Checks:
  1. fingerprint matches in any text file (words of 7+ letters, 2- to 4-word phrases, 4-sign runs in TSV
     "sign" columns);
  2. any path inside a directory named `restricted/` (git-ignored for local working copies);
  3. any image under ciphers/debosnys-1883/ that is not one of the published images listed, with its sha1,
     in ciphers/debosnys-1883/images/manifest.json.
Allowed lines (ASKS 156, owner's option (a), 9 Oct 2026): tools/restricted_allowed_lines.txt holds the
fingerprint of a whole line (normalised tokens joined by one space) that the owner chose to leave in place
in an append-only file (three ROOM.md lines of 8 Oct 2026 with figures from a private run). Check 1 skips a
line whose whole-line fingerprint is listed, so the fingerprints of those figures still catch a REPEAT
anywhere else. Must catch: the same figure phrase in any other file or a new line. Must not block: the
listed lines themselves. Offline test: tools/tests/test_restricted_guard.py.

Usage:
  python3 tools/restricted_guard.py              scan every tracked file (what CI runs)
  python3 tools/restricted_guard.py --outgoing   scan only files changed between origin/main and HEAD
  python3 tools/restricted_guard.py --fingerprint "some phrase"   print the fingerprints of a phrase
                                                  (for adding entries; never commit the phrase itself)
Exit 0 clean, 1 a finding (the file and line are printed, never the matched text).
"""
import hashlib, json, os, re, subprocess, sys, unicodedata

ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip() or "."
FP_FILE = os.path.join(ROOT, "tools", "restricted_fingerprints.txt")
IMG_EXT = (".png", ".jpg", ".jpeg", ".tif", ".tiff", ".gif", ".webp", ".bmp", ".pdf")
SKIP = {"tools/restricted_fingerprints.txt"}


def norm_tokens(text):
    t = unicodedata.normalize("NFKD", text)
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    return re.findall(r"[a-z0-9]+", t)


def fp(unit):
    return hashlib.sha256(unit.encode()).hexdigest()[:16]


def units(tokens):
    for i, w in enumerate(tokens):
        if len(w) >= 7:
            yield w
        for n in (2, 3, 4):
            if i + n <= len(tokens):
                yield " ".join(tokens[i:i + n])


def sign_units(line_signs):
    for i in range(len(line_signs) - 3):
        yield "SIGNS:" + "|".join(line_signs[i:i + 4])


def load_fps():
    try:
        return {l.split()[0] for l in open(FP_FILE) if l.strip() and not l.startswith("#")}
    except FileNotFoundError:
        return set()


def git_files(outgoing):
    if outgoing:
        # Compare against what origin actually has (FETCH_HEAD after an explicit fetch; clones made with a
        # single-branch refspec have no origin/main ref). Fail safe: if the diff cannot be computed, scan
        # every tracked file instead of passing on an empty list.
        subprocess.run(["git", "fetch", "-q", "origin", "main"], cwd=ROOT, capture_output=True)
        d = subprocess.run(["git", "diff", "--name-only", "--diff-filter=AMR", "FETCH_HEAD", "HEAD"],
                           cwd=ROOT, capture_output=True, text=True)
        if d.returncode == 0:
            return [f for f in d.stdout.splitlines() if f]
        out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True).stdout
    else:
        out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True).stdout
    return [f for f in out.splitlines() if f]


def published_debosnys_images():
    allowed = {}
    try:
        m = json.load(open(os.path.join(ROOT, "ciphers/debosnys-1883/images/manifest.json")))
        allowed = {("ciphers/debosnys-1883/images/" + i["file"]): i.get("sha1") for i in m.get("images", [])}
    except Exception:
        pass
    try:
        for l in open(os.path.join(ROOT, "tools", "restricted_allowlist.txt")):
            if l.strip() and not l.startswith("#"):
                sha, path = l.split()[:2]
                allowed[path] = sha
    except FileNotFoundError:
        pass
    return allowed


def allowed_lines():
    out = set()
    try:
        for l in open(os.path.join(ROOT, "tools", "restricted_allowed_lines.txt")):
            if l.strip() and not l.startswith("#"):
                out.add(l.split()[0])
    except FileNotFoundError:
        pass
    return out


def line_fp(line):
    return fp("LINE:" + " ".join(norm_tokens(line)))


def scan(files, fps):
    findings = []
    allowed = published_debosnys_images()
    skip_lines = allowed_lines()
    for f in files:
        if f in SKIP:
            continue
        path = os.path.join(ROOT, f)
        if not os.path.isfile(path):
            continue
        if "/restricted/" in "/" + f:
            findings.append((f, 0, "path inside a restricted/ directory"))
            continue
        if f.lower().endswith(IMG_EXT):
            if f.startswith("ciphers/debosnys-1883/"):
                sha = hashlib.sha1(open(path, "rb").read()).hexdigest()
                if allowed.get(f) != sha:
                    findings.append((f, 0, "image in the Debosnys folder that is not a listed published image"))
            continue
        try:
            text = open(path, encoding="utf-8").read()
        except (UnicodeDecodeError, OSError):
            continue
        if not fps:
            continue
        lines = text.splitlines()
        for n, line in enumerate(lines, 1):
            if skip_lines and line_fp(line) in skip_lines:
                continue
            for u in units(norm_tokens(line)):
                if fp(u) in fps:
                    findings.append((f, n, "matches a restricted fingerprint"))
                    break
        if f.endswith(".tsv") and lines:
            head = lines[0].split("\t")
            if "sign" in head:
                si = head.index("sign")
                li = head.index("line") if "line" in head else None
                seqs = {}
                for n, line in enumerate(lines[1:], 2):
                    cols = line.split("\t")
                    if len(cols) > si:
                        seqs.setdefault(cols[li] if li is not None and len(cols) > li else "", []).append((n, cols[si]))
                for seq in seqs.values():
                    signs = [s for _, s in seq]
                    for i, u in enumerate(sign_units(signs)):
                        if fp(u) in fps:
                            findings.append((f, seq[i][0], "sign run matches a restricted fingerprint"))
                            break
    return findings


def main(argv):
    if argv[:1] == ["--line-fingerprint"]:
        print(line_fp(" ".join(argv[1:])))
        return 0
    if argv[:1] == ["--fingerprint"]:
        phrase = " ".join(argv[1:])
        if phrase.startswith("SIGNS:"):
            print(fp(phrase)); return 0
        for u in sorted(set(units(norm_tokens(phrase)))):
            print(fp(u))
        return 0
    fps = load_fps()
    files = git_files("--outgoing" in argv)
    found = scan(files, fps)
    if found:
        print(f"restricted_guard: {len(found)} finding(s) -- restricted material must stay in the private repository:")
        for f, n, why in found:
            print(f"  {f}:{n}: {why}")
        return 1
    print(f"restricted_guard: clean ({len(files)} files, {len(fps)} fingerprints)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
