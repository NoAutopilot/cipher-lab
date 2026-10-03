#!/usr/bin/env python3
"""tool_shelf.py: which tool we already built fits this problem, and how far has it been proven? (TOOL-SHELF, 3 Oct 2026)

    python3 tools/tool_shelf.py "unseparated digit cipher no key"     best-matching shelf rows, grade first
    python3 tools/tool_shelf.py --top 8 "find cipher pages in a volume"
    python3 tools/tool_shelf.py --markdown                            the shelf table SYSTEM.md carries
    python3 tools/tool_shelf.py --check                               every tools/*.py|js and tools/families/*.py has a
                                                                      shelf row with a valid grade (nonzero otherwise)
    python3 tools/tool_shelf.py --underused [NEXT-STEPS.tsv]          tools cited by 0-1 target folders whose use-when
                                                                      matches an open/partial target's written next step
                                                                      (keyword match on NEXT-STEPS.tsv's truncated cells:
                                                                      a lead for the orchestrator to check, not a fit)

Why: the owner asked on 3 Oct 2026 what else we had built that would help, and an audit found shared tools never used on
the targets they fit (glyph_atlas.py on Birago/Florence; seg_homophonic.py, key_crossmatch.py, cipher_page_detector.py on
the Birago numerical system). Owner, same day: "just because these exist doesn't mean they're good." So the shelf records
evidence, not existence. Each row of tools/data/tool_shelf.tsv carries:

  grade     proven           passed a known-answer (or calibration) test on real material
            controlled-only  passed only a synthetic matched control
            weak             a known-answer or control result on file that falls short of the tool's purpose
            untested         no control or known-answer result found on file
            retired          closed by rule 3's third-attempt clause for the hypothesis it was built for
            n/a              not a solver or reader (a gate, fetcher, register or corpus model): nothing to grade
  evidence  the best known-answer or control result on file, citing the NOTES/HYPOTHESES/LEDGER line
  use_when  the problem a briefer has, in the briefer's words (the match target)

The folder count ("cited by N folders") is computed live from ciphers/*/ (*.md, *.py, *.tsv, *.json, *.sh) so it does
not go stale. Matching is a plain keyword score: use_when words count 3, the tool name 2, its docstring's first 600
characters 1, after lower-casing and dropping stop words. An untested tool is printed with "run its known-answer check
before trusting it"; weak and retired rows say so before anything else.

Scope (CLAUDE.md Usage 8a): this is a finder, not a gate. It must offer a tool for a problem phrased the way a briefer
phrases it (tests: "unseparated digit cipher" -> seg_homophonic.py, "key on disk might read another ciphertext" ->
key_crossmatch.py), and it must NOT hide a weak or untested tool's grade behind a good match (test: cipher_page_detector.py
prints "weak" first). --check fails on a tool with no row; it does not judge whether a grade is right -- the evidence
cell is the claim, and its citation is what a reader checks.

Offline; reads files only. Test: tools/tests/test_tool_shelf.py.
"""
import argparse
import ast
import csv
import glob
import os
import re
import sys

GRADES = ("proven", "controlled-only", "weak", "untested", "retired", "n/a")
ADVICE = {
    "untested": "run its known-answer check before trusting it",
    "weak": "its known-answer/control result falls short of its purpose: read the evidence before using it",
    "retired": "retired by rule 3: a different instrument or new material is needed",
}
STOP = set("""a an and or the of to in on for with from by is are be it its this that as at into no not any
my our we i how which what does do can one two plus vs per before after""".split())
CITE_EXT = ("*.md", "*.py", "*.tsv", "*.json", "*.sh")


def words(text):
    return [w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOP and len(w) > 1]


def stem(w):
    for suf in ("ing", "es", "s", "ed"):
        if len(w) > len(suf) + 3 and w.endswith(suf):
            return w[: -len(suf)]
    return w


# words too common in next-step cells to count as a match for --underused (every step mentions a key or a page)
GENERIC = {stem(w) for w in """cipher ciphertext key keys letter letters text leaf leaves page pages sign signs code codes
number numbers read reading run value values target known one word words line lines""".split()}


def stems(text):
    return {stem(w) for w in words(text)}


def load_shelf(root):
    path = os.path.join(root, "tools", "data", "tool_shelf.tsv")
    with open(path, newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def tool_files(root):
    out = []
    for pat in ("tools/*.py", "tools/*.js", "tools/families/*.py"):
        for p in sorted(glob.glob(os.path.join(root, pat))):
            rel = os.path.relpath(p, os.path.join(root, "tools"))
            if os.path.basename(rel) != "__init__.py":
                out.append(rel)
    return out


def docstring(root, tool):
    p = os.path.join(root, "tools", tool)
    if not p.endswith(".py") or not os.path.exists(p):
        return ""
    try:
        return ast.get_docstring(ast.parse(open(p, encoding="utf-8").read())) or ""
    except (SyntaxError, ValueError):
        return ""


def citation_counts(root, tools):
    """{tool: number of ciphers/<folder>/ that mention the tool's basename (families: 'families/<name>' or the name)}."""
    counts = {t: set() for t in tools}
    keys = {t: (os.path.basename(t),) if not t.startswith("families/") else (t, "--family " + t[9:-3]) for t in tools}
    files = []
    for ext in CITE_EXT:
        files += glob.glob(os.path.join(root, "ciphers", "*", "**", ext), recursive=True)
    for p in files:
        folder = os.path.relpath(p, os.path.join(root, "ciphers")).split(os.sep)[0]
        try:
            text = open(p, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        for t, ks in keys.items():
            if folder not in counts[t] and any(k in text for k in ks):
                counts[t].add(folder)
    return {t: len(v) for t, v in counts.items()}


def score(row, query, doc):
    q = stems(query)
    if not q:
        return 0
    return (3 * len(q & stems(row["use_when"])) + 2 * len(q & stems(row["tool"].replace("_", " ")))
            + len(q & stems(doc[:600])))


def render(row, n):
    grade = row["grade"]
    line = "[%s] %s  (cited by %d folders, %s)\n    use when: %s\n    evidence: %s\n    last: %s" % (
        grade, row["tool"], n, row["kind"], row["use_when"], row["evidence"], row["last_outcome"])
    if grade in ADVICE:
        line = line.replace("[%s] " % grade, "[%s] -- %s -- " % (grade, ADVICE[grade]), 1)
    return line


def cmd_query(root, query, top, instruments_only):
    shelf = load_shelf(root)
    scored = []
    for row in shelf:
        if instruments_only and row["grade"] == "n/a":
            continue
        s = score(row, query, docstring(root, row["tool"]))
        if s > 0:
            scored.append((s, row))
    scored.sort(key=lambda x: (-x[0], x[1]["tool"]))
    if not scored:
        print("no shelf row matches %r: say so in the brief before writing a private script" % query)
        return 1
    counts = citation_counts(root, [r["tool"] for _, r in scored[:top]])
    for s, row in scored[:top]:
        print(render(row, counts[row["tool"]]))
    return 0


def cmd_markdown(root):
    shelf = load_shelf(root)
    counts = citation_counts(root, [r["tool"] for r in shelf])
    print("| Tool | Grade | Use when | Folders citing | Best evidence on file |")
    print("|---|---|---|---|---|")
    order = {g: i for i, g in enumerate(GRADES)}
    for r in sorted(shelf, key=lambda r: (order.get(r["grade"], 9), r["tool"])):
        if r["grade"] == "n/a":
            continue
        cell = lambda s: s.replace("|", "\\|")
        print("| `%s` | %s | %s | %d | %s |" % (r["tool"], r["grade"], cell(r["use_when"]), counts[r["tool"]],
                                                 cell(r["evidence"])))
    na = sorted(r["tool"] for r in shelf if r["grade"] == "n/a")
    print("\nGrade n/a (gates, fetchers, registers, corpus models; `--check` keeps every tool on the shelf): "
          + ", ".join("`%s`" % t for t in na) + ".")
    return 0


def cmd_check(root):
    shelf = load_shelf(root)
    have = {r["tool"]: r for r in shelf}
    bad = 0
    for t in tool_files(root):
        if t not in have:
            print("MISSING shelf row: %s" % t)
            bad += 1
    for r in shelf:
        if r["grade"] not in GRADES:
            print("BAD grade %r: %s" % (r["grade"], r["tool"]))
            bad += 1
        if r["grade"] not in ("n/a", "untested") and r["evidence"].strip() in ("", "-"):
            print("NO evidence for grade %s: %s" % (r["grade"], r["tool"]))
            bad += 1
        if not os.path.exists(os.path.join(root, "tools", r["tool"])):
            print("STALE shelf row (no such file): %s" % r["tool"])
            bad += 1
    if bad:
        return 1
    print("tool_shelf: %d rows, every tool shelved, grades valid" % len(shelf))
    return 0


def cmd_underused(root, nsteps, max_cites=1, min_hits=2):
    shelf = [r for r in load_shelf(root) if r["kind"] in ("instrument", "scorer", "access") and r["grade"] != "retired"]
    counts = citation_counts(root, [r["tool"] for r in shelf])
    with open(nsteps, newline="") as f:
        rows = [r for r in csv.DictReader((l for l in f if not l.startswith("#")), delimiter="\t")
                if r.get("status") in ("open", "partial")]
    found = 0
    for r in sorted(shelf, key=lambda r: r["tool"]):
        if counts[r["tool"]] > max_cites:
            continue
        uw = stems(r["use_when"]) - GENERIC
        hits = []
        for t in rows:
            k = len(uw & stems((t.get("next_step") or "") + " " + (t.get("parallel") or "")))
            if k >= min_hits:
                hits.append((k, t["folder"]))
        if hits:
            hits.sort(key=lambda x: (-x[0], x[1]))
            found += 1
            print("%s [%s] cited by %d: %s" % (r["tool"], r["grade"], counts[r["tool"]],
                                              ", ".join(f for _, f in hits[:6]) + (" (+%d)" % (len(hits) - 6)
                                                                                    if len(hits) > 6 else "")))
    if not found:
        print("no under-used tool matches an open/partial next step")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("query", nargs="*", help="the problem, in words")
    ap.add_argument("--root", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--top", type=int, default=5)
    ap.add_argument("--instruments", action="store_true", help="skip grade n/a rows (gates, fetchers, registers)")
    ap.add_argument("--markdown", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--underused", nargs="?", const="NEXT-STEPS.tsv", default=None, metavar="NEXT-STEPS.tsv")
    ap.add_argument("--min-hits", type=int, default=2, help="--underused: shared non-generic use-when words needed (2)")
    a = ap.parse_args(argv)
    if a.check:
        return cmd_check(a.root)
    if a.markdown:
        return cmd_markdown(a.root)
    if a.underused is not None:
        p = a.underused if os.path.isabs(a.underused) else os.path.join(a.root, a.underused)
        return cmd_underused(a.root, p, min_hits=a.min_hits)
    if not a.query:
        ap.print_help()
        return 2
    return cmd_query(a.root, " ".join(a.query), a.top, a.instruments)


if __name__ == "__main__":
    sys.exit(main())
