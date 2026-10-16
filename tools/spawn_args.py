#!/usr/bin/env python3
"""Print, or check, the arguments of a `create_session` call so a worker is never spawned without its
repository (16 Oct 2026, mission "Close the Learning Loop"; RETRO-2026-09-25l section 3, RETRO-2026-10-12 P3).

Why a tool and not a sentence: the rule "every create_session passes source_url and source_revision" has been
written in prose three times (.claude/briefs/README.md "Spawning a session", parent.md "Spawning", LEARN-2026-
09-26-1252) and was still broken five times in one batch on 12 Oct 2026 (MQS-SHEETS A1, MQS-SORTER B, MQS-NAMES
C, MQS-CROSSWORD D, TXE2-PAIR3: each spawned with no repository, each archived having done nothing) and three
times on 25 Sept 2026 (LEDGER rows 799/818/819). A hand-typed call omits a field; a printed one does not.

Usage:
  tools/spawn_args.py --job JOB_ID [--title T] [--reason "one line"] [--account A]
      Reads JOB_ID's WORK-QUEUE.tsv row (brief, model, cap, box) and prints the JSON object to pass to
      create_session: source_url, source_revision, model id, permission_mode, title ("LIVE ..."), tags and a
      prompt that opens with the brief path and the one-line reason (parent.md "Spawning": rule text stays in
      the brief). Paste it; do not retype it.
  tools/spawn_args.py --brief PATH --model "Opus 5.5" [--job NAME] [--cap N] [--box MIN] ...
      Same without a queue row.
  tools/spawn_args.py --check ARGS.json
      Validates a pasted/saved argument object: exit 1 (and the missing field named) when source_url,
      source_revision, model, prompt or a title starting with LIVE is absent, or when source_url is not this
      repository. Exit 0 otherwise.

Catches (test tools/tests/test_spawn_args.py): an argument object with no source_url; one with a title not
starting with LIVE; a model name below the Opus floor for an Opus/Fable job is NOT this tool's business
(tools/brief_price_check.py checks caps). Must not block: a complete object; a --job call for a queued row.
"""
import argparse
import csv
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUEUE = os.path.join(ROOT, "WORK-QUEUE.tsv")
SOURCE_URL = "https://github.com/NoAutopilot/cipher-lab"
SOURCE_REVISION = "main"
MODEL_IDS = {
    "opus": "claude-opus-5-5",
    "opus 5.5": "claude-opus-5-5",
    "sonnet": "claude-sonnet-5",
    "sonnet 5": "claude-sonnet-5",
    "sonnet 5.5": "claude-sonnet-5-5",
    "fable": "claude-fable-5-1",
    "fable 5.1": "claude-fable-5-1",
    "haiku": "claude-haiku-5-5",
}
REQUIRED = ("source_url", "source_revision", "model", "prompt", "title")


def model_id(name):
    key = (name or "").strip().lower()
    if key.startswith("claude-"):
        return key
    return MODEL_IDS.get(key) or MODEL_IDS.get(key.split()[0] if key else "", None)


def load_row(job_id, path=QUEUE):
    with open(path, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            if r.get("job_id") == job_id:
                return r
    return None


def build(job, brief, model, cap, box, account, title=None, reason=None):
    mid = model_id(model)
    if not mid:
        raise SystemExit(f"spawn_args: unknown model {model!r} (known: {sorted(MODEL_IDS)})")
    account = account or os.environ.get("CIPHERLAB_ACCOUNT", "")
    acct = f"account {account}" if account else "this account"
    title = title or f"LIVE {job} worker ({acct})"
    reason = reason or f"job {job} of {brief}"
    prompt = (
        f"You are worker {job}. Your brief is the section for {job} in {brief}: read it first, then CLAUDE.md, "
        f"then `python3 tools/room.py --start` and the last 30 lines of ROOM.md. Reason for the job: {reason}. "
        f"Cap USD {cap} of usage, box {box} minutes from your claim line; stop before a unit that would cross 80% of either. "
        f"Claim in ROOM.md before any edit and end every claim/halfway/done line with your usage self-report. "
        f"Commit by explicit path, `git pull --rebase origin main`, push to main; done line and a five-line report when you stop."
    )
    return {
        "source_url": SOURCE_URL,
        "source_revision": SOURCE_REVISION,
        "model": mid,
        "permission_mode": "auto",
        "title": title,
        "tags": [f"cipherlab-account{account}" if account else "cipherlab", f"job:{job}"],
        "prompt": prompt,
    }


def check_args(obj):
    """Return a list of problems (empty when the object is complete)."""
    problems = []
    if not isinstance(obj, dict):
        return ["not a JSON object"]
    for k in REQUIRED:
        if not obj.get(k):
            problems.append(f"missing {k}")
    if obj.get("source_url") and obj["source_url"].rstrip("/") != SOURCE_URL:
        problems.append(f"source_url is {obj['source_url']!r}, not {SOURCE_URL}")
    if obj.get("title") and not str(obj["title"]).startswith("LIVE"):
        problems.append("title must start with LIVE (parent.md, owner 26 Sept 2026)")
    if obj.get("permission_mode") == "plan":
        problems.append("permission_mode plan stalls an unattended worker")
    return problems


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--job")
    ap.add_argument("--brief")
    ap.add_argument("--model")
    ap.add_argument("--cap")
    ap.add_argument("--box")
    ap.add_argument("--account")
    ap.add_argument("--title")
    ap.add_argument("--reason")
    ap.add_argument("--queue", default=QUEUE)
    ap.add_argument("--check", metavar="ARGS.json")
    a = ap.parse_args(argv)

    if a.check:
        with open(a.check, encoding="utf-8") as f:
            obj = json.load(f)
        problems = check_args(obj)
        if problems:
            print("spawn_args: REFUSE --", "; ".join(problems))
            return 1
        print("spawn_args: ok -- source_url, source_revision, model, prompt and a LIVE title are all present")
        return 0

    if a.brief and a.model:
        obj = build(a.job or os.path.basename(a.brief), a.brief, a.model, a.cap or "?", a.box or "?", a.account, a.title, a.reason)
    elif a.job:
        row = load_row(a.job, a.queue)
        if row is None:
            print(f"spawn_args: no WORK-QUEUE.tsv row {a.job!r}")
            return 1
        obj = build(a.job, row["brief"], row["model"], row["cap_usd"], row["box_min"], a.account or row.get("account"), a.title, a.reason)
    else:
        ap.error("give --job JOB_ID (a queued row) or --brief PATH --model M, or --check ARGS.json")
    problems = check_args(obj)
    assert not problems, problems  # the builder cannot produce an incomplete call
    print(json.dumps(obj, indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
