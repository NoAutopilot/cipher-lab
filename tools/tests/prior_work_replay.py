#!/usr/bin/env python3
"""prior_work_replay.py: the 45-case replay of tools/prior_work.py (review of PRIOR-WORK v1, 8 Oct 2026) as a
regression set, in place of the in-sample figures.

    python3 tools/tests/prior_work_replay.py [--ref 948992fd4] [--out results.jsonl] [--only L01,S05]

Cases: tools/tests/fixtures/prior_work/replay_cases.tsv -- 30 'leak' items (work that was spent on text already read:
print, gloss, own work, holder, modern decipherment) and 15 'surv' items (work that was right to do). Each runs as a
brief would name it: `prior_work.py <slug> --item-spec <spec> --step-type <step> --offline --dry-run --json --ref <ref>`
with the proxies pointed at 127.0.0.1:9 (nothing leaves the machine; nothing is written).

It prints, per case, the exit code and the specific rows (DONE, KNOWN, KNOWN-PART, LEAD, SUBSTANCE, KEY-SOURCE), then
the exit distributions per set and the survivors' hard false blocks (exit 2 KNOWN) and KNOWN rows. It reports and
never asserts: the repository moves, so the numbers belong in the review log beside the ref they were taken at, and a
non-zero exit is NOT recall (29/30 leak and 15/15 survivor items exited non-zero at a639de9a1, mostly from generic LOOK
and UNCHECKED holds). Scoring a catch as specific (its evidence names the real prior work) stays a reader's job.
Run time: about 3 to 5 minutes offline. Not run by test_prior_work.py (it reads the real repository at --ref).
"""
import argparse, collections, csv, json, os, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CASES = os.path.join(HERE, "fixtures", "prior_work", "replay_cases.tsv")
SPECIFIC = ("DONE", "KNOWN", "KNOWN-PART", "LEAD", "SUBSTANCE", "KEY-SOURCE")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ref", default="948992fd4b497124b659121f1f19b63b2e900288", help="ref the targets are read at")
    ap.add_argument("--out", help="also write one JSON line per case here (outside the repository)")
    ap.add_argument("--only", help="comma-separated case ids")
    ap.add_argument("--now", default="2026-10-08T16:45")
    a = ap.parse_args(argv)
    env = dict(os.environ, HTTPS_PROXY="http://127.0.0.1:9", HTTP_PROXY="http://127.0.0.1:9",
               https_proxy="http://127.0.0.1:9", http_proxy="http://127.0.0.1:9", NO_PROXY="", no_proxy="")
    cases = list(csv.DictReader(open(CASES, encoding="utf-8"), delimiter="\t"))
    if a.only:
        keep = set(a.only.split(","))
        cases = [c for c in cases if c["case"] in keep]
    out = open(a.out, "w", encoding="utf-8") if a.out else None
    exits = collections.defaultdict(collections.Counter)
    surv_known = []
    for c in cases:
        cmd = [sys.executable, os.path.join(REPO, "tools", "prior_work.py"), c["slug"], "--item-spec", c["spec"],
               "--step-type", c["step"], "--offline", "--dry-run", "--json", "--ref", a.ref, "--now", a.now,
               "--root", REPO]
        t = time.time()
        r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True, env=env, timeout=900)
        recs = [json.loads(l) for l in r.stdout.splitlines() if l.startswith("{")]
        rows = [x for it in recs for x in it["rows"]]
        spec = sorted({(x["verdict"], x["check"]) for x in rows if x["verdict"] in SPECIFIC})
        exits[c["set"]][r.returncode] += 1
        if c["set"] == "surv":
            surv_known += [(c["case"], x["route"], x["evidence"][:120]) for x in rows if x["verdict"] == "KNOWN"]
        print(f"{c['case']}\t{c['set']}\t{c['kind']}\t{c['slug']}\texit {r.returncode}\t{time.time() - t:.1f}s\t"
              + "; ".join(f"{v} {k}" for v, k in spec))
        if out:
            out.write(json.dumps(dict(case=c, exit=r.returncode, items=recs, stderr=r.stderr[-800:])) + "\n")
    for s, cnt in sorted(exits.items()):
        print(f"exits {s}: {dict(sorted(cnt.items()))}")
    print(f"survivors with a KNOWN row: {len({k for k, _, _ in surv_known})} (hard false blocks are the exit-2 survivors)")
    for k, route, ev in surv_known:
        print(f"  {k}\t{route}\t{ev}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
