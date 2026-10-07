#!/usr/bin/env python3
"""next_steps_fresh.py: is a NEXT-STEPS.tsv `runnable` row's named step already done? (FRESH-0914, 7 Oct 2026)

Why: three batches in a row (B0709-A1, B0709-A4, BKLOG-0507 item 3) finished in under ten minutes because the
NEXT-STEPS.tsv rows they were handed were stale -- the step had been run and the target's Verdict line never
updated. This is the mechanical half of the freshness check (Usage 2: a script reads, a model judges the hits).

For every row tools/next_steps.py classes `runnable`:
  1. the step text is the folder's own Verdict line (or prose next step), read with next_steps.py's own parsers;
  2. its anchor time is `git blame`'s author time for the NOTES.md line that carries it (the step was last
     restated then);
  3. evidence after the anchor: ROOM.md lines naming the folder with a `done` signal stamped later, and NOTES.md
     paragraphs whose lines were all written (git blame) after the anchor;
  4. each evidence chunk is scored by overlap with the step's keywords (identifiers such as f.174r, L04, K01,
     worker tags such as NEVBI-174V, and content words of 6+ letters that are not rule-5 boilerplate);
  5. a row is `stale?` when some later chunk shares >= MIN_HITS keywords and >= MIN_SHARE of them, else `fresh`.

`stale?` is a lead for a person or orchestrator to read (the TSV quotes the chunk), never an edit on its own.
Must flag: a step whose identifiers reappear in a later done line (tests: a Verdict naming 'f.174r L04 85' and a
later done line 'f.174r L04 85 fixed'). Must NOT flag: a later done line about the same folder that shares only
boilerplate words (gap, verdict, internal, cheapest) or one identifier.

Usage:
  python3 tools/next_steps_fresh.py [--out FILE.tsv] [--min-hits 3] [--min-share 0.3]
  python3 tools/tests/test_next_steps_fresh.py
"""
import argparse, os, re, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import next_steps as ns

MIN_HITS = 3
MIN_SHARE = 0.3
STOP = set("""verdict internal cheapest keep going parked remaining escalation gaps further before after should
would could which their there these those within without against between second through number numbers until
another already update updated during because blocked target folder notes passes reading readings control
controls disk only person worker brief briefs suggestion follow-up following unchanged depends nobody""".split())
ID_RE = re.compile(r"\b(?:f\.?\s?\d+[rv]?|ff\.\s?\d+|[A-Z]\d{2,3}|[A-Z][A-Z0-9]{2,}(?:-[A-Z0-9]+)+|no\.\s?\d+|\d{3,}[a-z]?)\b")
WORD_RE = re.compile(r"[a-zà-ÿ]{6,}")
# the worker that restated the Verdict posts its own done line a minute or two later; that is not evidence
ROOM_MARGIN_S = 30 * 60
ROOM_RE = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}) \| ([^|]*) \| (.*)$")


def norm_id(t):
    return re.sub(r"\s+", "", t.lower())


def keywords(text):
    text = re.sub(r"https?://\S+", " ", text)
    ids = {norm_id(m.group(0)) for m in ID_RE.finditer(text)}
    words = {w for w in WORD_RE.findall(text.lower()) if w not in STOP}
    return ids | words


def overlap(kw, chunk):
    have = keywords(chunk)
    hits = sorted(kw & have)
    return hits, (len(hits) / len(kw) if kw else 0.0)


def is_stale(kw, chunk, min_hits=MIN_HITS, min_share=MIN_SHARE):
    hits, share = overlap(kw, chunk)
    return len(hits) >= min_hits and share >= min_share, hits, share


def blame_times(path):
    """{line_number: author_time (unix)} for every line of path, from one `git blame --porcelain` call."""
    try:
        out = subprocess.run(["git", "blame", "--line-porcelain", str(path)], cwd=ROOT, capture_output=True,
                             text=True, check=True).stdout
    except Exception:
        return {}
    times, cur, n = {}, None, 0
    for line in out.splitlines():
        if re.match(r"^[0-9a-f]{40} ", line):
            n = int(line.split()[2])
        elif line.startswith("author-time "):
            cur = int(line.split()[1])
        elif line.startswith("\t"):
            times[n] = cur
    return times


def anchor_line(lines, step):
    probe = re.sub(r"^Verdict:\s*", "", step).strip()[:60].rstrip("…")
    for i in range(len(lines) - 1, -1, -1):
        if probe and probe in lines[i]:
            return i + 1
    return None


def later_paragraphs(lines, times, anchor_t, anchor_n):
    """NOTES.md paragraphs every line of which was written after anchor_t (git blame), excluding the anchor."""
    paras, cur = [], []
    for i, l in enumerate(lines, 1):
        if not l.strip():
            if cur:
                paras.append(cur); cur = []
            continue
        cur.append(i)
    if cur:
        paras.append(cur)
    out = []
    for p in paras:
        if anchor_n in p:
            continue
        if all((times.get(i) or 0) > anchor_t for i in p):
            out.append("\n".join(lines[i - 1] for i in p))
    return out


def room_done_lines(room_lines, folder, after_t):
    out = []
    for l in room_lines:
        m = ROOM_RE.match(l)
        if not m or folder not in m.group(3):
            continue
        t = datetime.strptime(m.group(1), "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc).timestamp()
        if t > after_t + ROOM_MARGIN_S and re.search(r"\bdone\b", m.group(3)):
            out.append(l)
    return out


def check_row(folder, room_lines, min_hits, min_share):
    path = ROOT / "ciphers" / folder / "NOTES.md"
    text = path.read_text(encoding="utf-8", errors="replace")
    verdict, _ = ns.verdict_step(text)
    step = verdict or ns.extract_next_step(text)
    lines = text.splitlines()
    n = anchor_line(lines, step)
    times = blame_times(path)
    anchor_t = times.get(n) if n else None
    if anchor_t is None:
        return dict(folder=folder, verdict="no-anchor", anchor="", kind="", hits="", share="",
                    evidence=re.sub(r"\s+", " ", step)[:160])
    kw = keywords(step)
    best = None
    for kind, chunks in (("room", room_done_lines(room_lines, folder, anchor_t)),
                         ("notes", later_paragraphs(lines, times, anchor_t, n))):
        for c in chunks:
            stale, hits, share = is_stale(kw, c, min_hits, min_share)
            score = (stale, len(hits), share)
            if best is None or score > best[0]:
                best = (score, kind, hits, share, c)
    anchor = datetime.fromtimestamp(anchor_t, timezone.utc).strftime("%Y-%m-%d %H:%M")
    if best is None:
        return dict(folder=folder, verdict="fresh", anchor=anchor, kind="", hits="", share="", evidence="")
    (stale, _, _), kind, hits, share, c = best
    return dict(folder=folder, verdict="stale?" if stale else "fresh", anchor=anchor, kind=kind,
                hits=",".join(hits), share=f"{share:.2f}", evidence=re.sub(r"\s+", " ", c)[:300])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=None, help="write the TSV here (default stdout)")
    ap.add_argument("--min-hits", type=int, default=MIN_HITS)
    ap.add_argument("--min-share", type=float, default=MIN_SHARE)
    a = ap.parse_args()
    rows = ns.build_rows(str(ROOT / "ciphers"), (ROOT / "LEDGER.md").read_text(encoding="utf-8", errors="replace"),
                         (ROOT / "NEAR.md").read_text(encoding="utf-8", errors="replace"))
    room = (ROOT / "ROOM.md").read_text(encoding="utf-8", errors="replace").splitlines()
    cols = ["folder", "verdict", "anchor", "kind", "hits", "share", "evidence"]
    out = ["\t".join(cols)]
    res = [check_row(r["folder"], room, a.min_hits, a.min_share) for r in rows if r["blocker"] == "runnable"]
    for r in res:
        out.append("\t".join(str(r[c]).replace("\t", " ") for c in cols))
    text = "\n".join(out) + "\n"
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    n_stale = sum(r["verdict"] == "stale?" for r in res)
    print(f"{len(res)} runnable rows: {n_stale} stale?, {len(res) - n_stale} fresh/no-anchor", file=sys.stderr)


if __name__ == "__main__":
    main()
