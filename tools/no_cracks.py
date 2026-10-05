#!/usr/bin/env python3
"""No cracks: one row per live target saying what its next step is, what blocks it, who has to act
(agent, owner or outside) and which owner-board card carries it -- so a target whose next step needs
the owner, or that waits on a reply we asked for, never lives only in a NOTES.md nobody re-reads.

Built 5 Oct 2026 (NO-CRACKS, account 3; owner: "for all of these, what's blocking them / next step, and
if it requires a human, add to my kanban ... nothing slipping through the cracks. Systematize.").

Inputs (all read from disk, nothing fetched):
  PROGRESS.tsv      every row (one per leaf/letter; several rows may share a folder)
  NEXT-STEPS.tsv    every open/partial/blocked folder (regenerate first: python3 tools/next_steps.py)
  ASKS.md           rows whose status is desk/backlog/open/drafted/waiting/queued, mapped to folders by
                    `ciphers/<folder>` or the bare folder slug in the row
  LOCAL-QUEUE.tsv   rows the runner left `blocked`/`bounced` (the runner could not do them: owner)
  SEND-QUEUE.tsv    `redraft` rows (agent: a fresh gate-7 pass) and `sent` rows (outside: a reply)
  --board FILE      the desk board's "cards" collection exported to JSON (a list of cards, a dict
                    id -> card, or {"cards": [...]}; fields id, lane, title, detail, link, asks[],
                    folders[]). Cards in lane `done` never count as carrying an open step.

Output: NO-CRACKS.tsv (columns COLUMNS below) and, with --cards-json, proposed new board cards for the
`who=owner` rows that no card carries, grouped by action (all sorter piles in one card, all copy orders
in one card, ...) per .claude/briefs/parent.md "Owner desk asks" (title <= 60 chars, one link, one
action, one thing back). The tool never writes the board itself; the parent reviews and writes cards.

who:
  owner    the next step needs a person: a payment/order/quote, an email or form send, a judgement
           (sign sorter, eye check, decision), a desk read the runner could not do (Cloudflare,
           sign-in), a credential; or an ASKS row at desk/drafted, or a LOCAL-QUEUE row the runner
           bounced/blocked, names the folder.
  outside  the step waits on an archive's or a person's reply (sent, awaiting, waiting on ...). No
           action card is needed, but when we asked (an ASKS `waiting` row, a SEND-QUEUE `sent`
           row, or the text says sent/awaiting) a waiting card must exist.
  agent    everything else (a worker can run it).
  none     the row is finished: a PROGRESS row with stage S done, or a found-solved/solved/
           closed-negative folder whose NOTES name no next step.

flags (exit 1 when any is present, unless --report-only):
  MISSING  no non-done card carries the folder although one is needed: who=owner; or a reply is owed
           (an ASKS `waiting` row or a SEND-QUEUE `sent` row -- a waiting card must exist, whatever
           `who` is); or an ASKS `desk`/`drafted` row names the folder (an owner ask on record) even
           when the next step itself is agent work. A MISSING row whose ask is stale (sent, done) is
           fixed in ASKS.md, not with a card; one already covered by a card that does not name it is
           fixed by adding the folder to that card's `folders` field.
  NO-NEXT  no next step anywhere (NEXT-STEPS empty, no "## While waiting" action, and the folder's
           NOTES.md name none) and the row
           is not finished. Fix: write "next: <step>, ~$X" into the folder's NOTES.md.

Card matching (a card "carries" a folder) -- any of: the folder in card.folders; `ciphers/<folder>`
or the slug itself in the card's title/detail/link; card.asks sharing an ASKS row number with the
folder's own ASKS rows; or one of the folder's alias tokens (distinctive slug words of 5+ letters
that no other folder shares, plus the PROGRESS name's first word) as a whole word in the card's
title/detail.

What this must catch (CLAUDE.md Usage 8a, tests in tools/tests/test_no_cracks.py): a folder whose
next step says "order the copy" / "send the form" / "sort the signs" with no board card for it is
MISSING; a folder with no next step at all is NO-NEXT; a LOCAL-QUEUE row the runner bounced makes its
folder owner even when the NOTES text reads as agent work.
What it must NOT block: an agent-runnable step with no card (agents need no card -- e.g. "run
print_check on the decoded phrases"); a finished PROGRESS row (stage S done) with no next step; a
folder carried only by a card in lane `todo`/`later`/`waiting` (any non-done lane counts).
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import next_steps as ns  # noqa: E402

COLUMNS = ("folder", "name", "status", "next_step", "blocker", "who", "board_card_id", "flags", "refs")

OPEN_ASK = re.compile(r"^\W*(desk|backlog|open|drafted|waiting|queued)\b", re.I)
OWNER_ASK = re.compile(r"^\W*(desk|drafted)\b", re.I)
WAIT_ASK = re.compile(r"^\W*waiting\b", re.I)
FINISHED_STATUS = ("solved", "found-solved", "closed-negative")

# Owner-action kinds, in priority order. Each: (key, regex on the next-step text, card title, link, action, back).
OWNER_KINDS = (
    ("sorter", re.compile(r"\bsign sorter\b|\bsorter\b|\bsort (the )?(signs|marks|piles)\b|\bpiles\b", re.I),
     "Sort piles: {n} target(s)", "https://github.com/noautopilot/cipher-lab/blob/main/tools/sign_sorter.py",
     "Open each target's sorter page and settle its piles", "the sorter export (piles.json) per target"),
    ("desk-read", re.compile(r"cloudflare|sign-in|signed in|log in to|login wall|desk[- ]browser|desk read|owner'?s browser|academia\.edu|lent book", re.I),
     "Desk reads the runner could not do: {n} target(s)", "https://github.com/noautopilot/cipher-lab/blob/main/LOCAL-QUEUE.tsv",
     "Open each bounced LOCAL-QUEUE row's page and read the named lines", "a screenshot or the quoted text"),
    ("order", re.compile(r"copy order|\border\b|\bquote\b|\bpayment\b|\bpay\b|reproduction|digiti[sz]ation request|REQUEST\.md", re.I),
     "Copy orders / quotes: {n} target(s)", "https://github.com/noautopilot/cipher-lab/blob/main/ASKS.md",
     "Place (or approve) the copy order named in each target's REQUEST.md", "the order/quote confirmation"),
    ("send", re.compile(r"\bemail\b|\bsend\b|\bform\b|\bwrite to\b|\bletter to\b", re.I),
     "Send drafts: {n} target(s)", "https://github.com/noautopilot/cipher-lab/blob/main/SEND-QUEUE.tsv",
     "Send the checked draft for each target", "the date sent"),
    ("eye", re.compile(r"eye[- ]check|by eye|hand comparison|\bjudg(e)?ment\b", re.I),
     "Eye checks: {n} target(s)", "https://github.com/noautopilot/cipher-lab/blob/main/ASKS.md",
     "Look at the named crop and answer the one question", "your answer in chat"),
    ("decision", re.compile(r"(?<!orchestrator )(?<!lane )\bdecide\b|(?<!orchestrator )(?<!lane )\bdecision\b|\bwaive\b|owner'?s call|owner decides", re.I),
     "Decisions: {n} target(s)", "https://github.com/noautopilot/cipher-lab/blob/main/ASKS.md",
     "Answer yes/no on each named question", "one word per question"),
    ("credential", re.compile(r"credential|api key|\bkey request\b|_KEY\b|password", re.I),
     "Credentials: {n} item(s)", "https://github.com/noautopilot/cipher-lab/blob/main/KEYS.md",
     "Add the named variable in both accounts' environment settings", "'done'"),
)
OWNER_HINT = re.compile(r"\bthe owner\b|\bowner[- ]side\b|\bthe person\b|needs-person|waiting on you", re.I)
OUTSIDE = re.compile(r"\bawait(s|ing)?\b|waiting (on|for)\b.*\b(reply|answer|quote|archive|library|museum|PDF|estimate)"
                     r"|\breply\b.*\b(pending|due)\b|\bsent\b.*\b(await|wait)", re.I)
RUNNABLE_FIRST = re.compile(r"^\s*(Verdict:\s*keep going|one action that depends on nobody)", re.I)
STOP_TOKENS = {"nevers", "birago", "letter", "letters", "cipher", "ciphers", "printed", "decode", "paget",
               "villeroy", "revol", "brienne", "estrades", "hessen", "heinsius", "thurloe", "mayenne",
               "noailles", "nassau", "eckert", "royal", "dupuy", "colbert", "baluze", "clair", "clairambault"}


def read(path):
    return open(path, encoding="utf-8", errors="replace").read() if os.path.exists(path) else ""


def read_tsv(path):
    text = read(path)
    lines = [l for l in text.splitlines() if l.strip() and not l.startswith("#")]
    if not lines:
        return []
    head = lines[0].split("\t")
    return [dict(zip(head, l.split("\t") + [""] * (len(head) - len(l.split("\t"))))) for l in lines[1:]]


def folders_in(text, known):
    """Folders named in free text: `ciphers/<f>` or the bare slug (whole token)."""
    out = set(re.findall(r"ciphers/([a-z0-9][a-z0-9_.-]*[a-z0-9])", text))
    for f in known:
        if f in text and re.search(r"(?<![a-z0-9-])" + re.escape(f) + r"(?![a-z0-9-])", text):
            out.add(f)
    return out & set(known)


ASK_TEXT = {}  # row number -> "project | what is needed | exact action", for owner_kind() on an ask


def parse_asks(text, known):
    """({folder: [(row_num, status_cell)]}, {row_num: status_cell}) for open ASKS.md rows."""
    out, status_of = {}, {}
    ASK_TEXT.clear()
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 7 or not cells[0].isdigit():
            continue
        status = cells[-1]
        if not OPEN_ASK.match(status):
            continue
        status_of[int(cells[0])] = status
        ASK_TEXT[int(cells[0])] = " ".join(cells[2:5])
        for f in folders_in(line, known):
            out.setdefault(f, []).append((int(cells[0]), status))
    return out, status_of


def parse_local_queue(rows, known):
    """({folder: [(id, status)]} for rows the runner left blocked/bounced, set of queued row ids)."""
    out, queued = {}, set()
    for r in rows:
        st = r.get("status", "")
        if re.match(r"\s*(blocked|bounced)", st, re.I):
            for f in folders_in(r.get("target", ""), known):
                out.setdefault(f, []).append((r.get("id", ""), st))
        elif re.match(r"\s*queued", st, re.I):
            queued.add(r.get("id", ""))
    return out, queued


def parse_send_queue(rows, known):
    out = {}
    for r in rows:
        st = r.get("status", "").strip()
        if st in ("redraft", "sent", "queued"):
            for f in folders_in(r.get("target", ""), known):
                out.setdefault(f, []).append((r.get("id", ""), st, r.get("result", "")))
    return out


def load_board(path):
    if not path:
        return []
    data = json.loads(read(path) or "[]")
    if isinstance(data, dict) and "cards" in data:
        data = data["cards"]
    if isinstance(data, dict):
        data = [dict(v, id=v.get("id") or k) for k, v in data.items()]
    return [c for c in data if (c.get("lane") or "").lower() != "done"]


def alias_tokens(folders, names):
    """{folder: set(tokens)}: slug words of 5+ letters unique to one folder, plus the PROGRESS name's first word."""
    words = {f: {w for w in re.split(r"[-_.]", f) if len(w) >= 5 and w.isalpha() and w not in STOP_TOKENS}
             for f in folders}
    count = {}
    for ws in words.values():
        for w in ws:
            count[w] = count.get(w, 0) + 1
    out = {f: {w for w in ws if count[w] == 1} for f, ws in words.items()}
    for f, nm in names.items():
        first = re.split(r"[\s,(]", nm.strip())[0].lower() if nm.strip() else ""
        if len(first) >= 5 and first.isalpha() and first not in STOP_TOKENS and count.get(first, 0) <= 1:
            out.setdefault(f, set()).add(first)
    return out


def card_asks(c):
    """ASKS row numbers a card names: its asks[] plus "ASKS 116, 125, 129-136" in its text."""
    nums = {int(a) for a in (c.get("asks") or []) if str(a).isdigit()}
    text = " ".join(str(c.get(k, "")) for k in ("title", "detail", "linkLabel"))
    for m in re.finditer(r"\bASKS\s+((?:rows?\s+)?\d+(?:\s*-\s*\d+)?(?:\s*(?:,|and)\s*\d+(?:\s*-\s*\d+)?)*)", text):
        for a, b in re.findall(r"(\d+)(?:\s*-\s*(\d+))?", m.group(1)):
            lo, hi = int(a), int(b or a)
            if hi - lo <= 40:
                nums.update(range(lo, hi + 1))
    return nums


def cards_for(folder, cards, aliases, ask_nums, runner_wait=False):
    hits = []
    for c in cards:
        text = " ".join(str(c.get(k, "")) for k in ("title", "detail", "link", "linkLabel"))
        low = text.lower()
        if folder in (c.get("folders") or []) or folder in low:
            hits.append(c["id"]); continue
        if ask_nums and card_asks(c) & ask_nums:
            hits.append(c["id"]); continue
        if runner_wait and re.search(r"\brunner\b", str(c.get("title", "")).lower()) and "local-queue" in low:
            hits.append(c["id"]); continue
        if any(re.search(r"\b" + re.escape(t) + r"\b", low) for t in aliases.get(folder, ())):
            hits.append(c["id"])
    return hits


def ask_kind(ask_status, text=""):
    """The owner-action kind of a folder's open owner asks, read from the asks' own row text."""
    cells = " ".join(ASK_TEXT.get(n, "") for n, st in ask_status.items() if OWNER_ASK.match(st))
    return owner_kind(cells) or owner_kind(text) or "decision"


def owner_kind(text):
    for key, pat, *_ in OWNER_KINDS:
        if pat.search(text):
            return key
    return None


NOBODY = re.compile(r"depends? on (nobody|no one|no-one)|nothing depends on anyone|agent[- ]only|disk only|script only", re.I)
ASKS_REF = re.compile(r"\bASKS(?:\.md)?\s+(?:rows?\s+)?(\d+)", re.I)
LQ_REF = re.compile(r"\b(?:LOCAL-QUEUE(?:\.tsv)?\s+(?:row\s+)?|LQ\s+)?\b(L\d{1,3})\b")


def step_clause(step, gaps_text=""):
    """The part of the next-step text that names the step itself: the "cheapest next:" clause of a
    rule-5 "keep going" Verdict, the gap lines of a "parked" Verdict, otherwise the whole text."""
    m = re.search(r"cheapest next:\s*(.*)", step, re.I)
    if m:
        return re.split(r";\s*then\b|\bthen gap\b", m.group(1))[0]
    if re.match(r"\s*Verdict:\s*parked", step, re.I) and gaps_text:
        return step + "\n" + gaps_text
    return step


def classify(clause, ask_status, lq_blocked, lq_queued, sq):
    """(who, kind, needs_card) for one folder. ask_status: {row: status cell} of the folder's open ASKS rows
    plus any ASKS row the clause cites. `waiting` is True when we asked someone outside and a reply is
    owed (a SEND-QUEUE `sent` row or an ASKS `waiting` row): a waiting card must then exist whatever
    `who` is, since an agent step and an owed reply can run side by side. An ASKS `desk`/`drafted` row
    on the folder (an owner ask on record) likewise needs a card even when the next step is agent work."""
    sent = any(st == "sent" for _, st, _ in sq)
    waiting = sent or any(WAIT_ASK.match(s) for s in ask_status.values())
    text = clause or ""
    if lq_blocked:
        return "owner", "desk-read", waiting
    if any(st == "redraft" for _, st, _ in sq):
        return "agent", None, waiting
    if sent and (not text.strip() or re.match(r"\s*Verdict:\s*parked", text, re.I)):
        return "outside", None, True  # parked behind a request we already sent: the reply is the step
    owner_ask = not sent and any(OWNER_ASK.match(s) for s in ask_status.values())
    bare = re.sub(r"^[\s\-*#]*(?:[A-Z]:\s*)?(?:\*\*[^*]*\*\*\s*)?", "", text)
    if owner_ask and (not text.strip() or re.match(r"\s*Verdict:\s*parked", text, re.I)):
        return "owner", ask_kind(ask_status, text), True
    if NOBODY.search(text) or re.match(r"(file|queue|draft|write|run|grep)\b", bare, re.I):
        return "agent", None, waiting or owner_ask
    for n in ASKS_REF.findall(text):
        st = ask_status.get(int(n), "")
        if WAIT_ASK.match(st):
            return "outside", None, True
        if st:
            return "owner", owner_kind(st + " " + text) or "decision", waiting or owner_ask
    if any(l in lq_queued for l in LQ_REF.findall(text)) or OUTSIDE.search(text):
        return "outside", None, True
    if OWNER_HINT.search(text) or owner_kind(text):
        return "owner", owner_kind(text) or "decision", waiting or owner_ask
    if waiting and (not text.strip() or re.match(r"\s*Verdict:\s*parked", text, re.I)):
        return "outside", None, True
    return "agent", None, waiting or owner_ask


def folder_fallback(ciphers_dir, folder):
    """(status, next_step) read from the folder's NOTES.md with next_steps.py's own extractors."""
    text = read(os.path.join(ciphers_dir, folder, "NOTES.md"))
    if not text:
        return "", ""
    status = ns.first_status_word(text) or ""
    if not status:
        m = re.search(r"\*\*Status:?\*\*:?\s*([a-z-]+)", text, re.I)
        status = m.group(1).lower() if m else ""
    verdict, _ = ns.verdict_step(text)
    step = verdict or ns.one_line(ns.extract_next_step(text))
    return status, step


def build(root, board_path, ciphers_dir=None):
    ciphers_dir = ciphers_dir or os.path.join(root, "ciphers")
    progress = read_tsv(os.path.join(root, "PROGRESS.tsv"))
    nexts = {r["folder"]: r for r in read_tsv(os.path.join(root, "NEXT-STEPS.tsv"))
             if r.get("status") in ns.TARGET_STATUSES}
    known = sorted(set(os.listdir(ciphers_dir)) if os.path.isdir(ciphers_dir) else set())
    known = sorted(set(known) | set(nexts) | {r["folder"] for r in progress})
    asks, ask_status_all = parse_asks(read(os.path.join(root, "ASKS.md")), known)
    lq, lq_queued = parse_local_queue(read_tsv(os.path.join(root, "LOCAL-QUEUE.tsv")), known)
    sq = parse_send_queue(read_tsv(os.path.join(root, "SEND-QUEUE.tsv")), known)
    cards = load_board(board_path)

    targets = []  # (folder, name, progress_row or None)
    for r in progress:
        targets.append((r["folder"], r.get("name", ""), r))
    seen = {r["folder"] for r in progress}
    for f in sorted(nexts):
        if f not in seen:
            targets.append((f, "", None))
    names = {}
    for f, nm, _ in targets:
        names.setdefault(f, nm)
    aliases = alias_tokens([t[0] for t in targets], names)

    rows = []
    for folder, name, prow in targets:
        notes = read(os.path.join(ciphers_dir, folder, "NOTES.md"))
        if folder in nexts:
            status, step, blocker = nexts[folder]["status"], nexts[folder]["next_step"], nexts[folder]["blocker"]
        else:
            status, step = folder_fallback(ciphers_dir, folder)
            blocker = ns.classify_blocker(step) if step else "needs-triage"
        if not step.strip() and notes:
            ww = ns.extract_while_waiting(notes)
            step = ("While waiting: " + ns.one_line(ww)) if ww and ww.strip() else ""
        gaps_text = ns.verdict_step(notes)[1] if notes and re.match(r"\s*Verdict:\s*parked", step, re.I) else ""
        f_asks, f_lq, f_sq = asks.get(folder, []), lq.get(folder, []), sq.get(folder, [])
        refs = ([f"ASKS {n}" for n, _ in f_asks] + [f"LQ {i}" for i, _ in f_lq] + [f"SEND {i}:{s}" for i, s, _ in f_sq])
        owner_ask_cells = " ".join(st for _, st in f_asks if OWNER_ASK.match(st))
        finished = not step.strip() and ((prow is not None and prow.get("S", "").strip() == "x") or status in FINISHED_STATUS)
        flags = []
        clause = step_clause(step, gaps_text)
        if finished and not (f_asks or f_lq):
            who, kind, asked = "none", None, False
            step = step or f"none ({status or 'stage S done'})"
        else:
            if not step.strip():
                flags.append("NO-NEXT")
            ask_status = dict(ask_status_all)
            who, kind, asked = classify(clause, {n: ask_status_all[n] for n, _ in f_asks} | {
                int(n): ask_status[int(n)] for n in ASKS_REF.findall(clause) if int(n) in ask_status},
                f_lq, lq_queued, f_sq)
        runner_wait = who == "outside" and any(l in lq_queued for l in LQ_REF.findall(clause))
        clause_asks = {int(n) for n in ASKS_REF.findall(clause)}
        hits = cards_for(folder, cards, aliases, {n for n, _ in f_asks} | clause_asks, runner_wait)
        card = ",".join(dict.fromkeys(hits))
        if not card:
            if who == "owner" or asked:
                card = "MISSING"
                flags.append("MISSING")
            else:
                card = "-"
        rows.append({"folder": folder, "name": name, "status": status, "next_step": " ".join(step.split()),
                     "blocker": blocker, "who": who, "board_card_id": card, "flags": ",".join(flags),
                     "refs": "; ".join(refs),
                     "_kind": kind if who == "owner" else
                     (ask_kind({n: st for n, st in f_asks}) if owner_ask_cells and not any(
                         st == "sent" for _, st, _ in f_sq) else "waiting")})
    return rows


def proposed_cards(rows):
    groups = {}
    for r in rows:
        if "MISSING" not in r["flags"]:
            continue
        key = r["_kind"] or "waiting"
        groups.setdefault(key, []).append(r)
    out = []
    meta = {k: (t, l, a, b) for k, _, t, l, a, b in OWNER_KINDS}
    meta["waiting"] = ("Waiting on replies: {n} target(s)", "https://github.com/noautopilot/cipher-lab/blob/main/ASKS.md",
                       "Nothing to do; forward any reply that arrives", "the reply, when it comes")
    for key, rs in sorted(groups.items()):
        title, link, action, back = meta.get(key, meta["decision"])
        if len(rs) == 1:
            link = f"https://github.com/noautopilot/cipher-lab/blob/main/ciphers/{rs[0]['folder']}/NOTES.md"
        out.append({
            "id": f"nc-{key}",
            "lane": "waiting" if key == "waiting" else "todo",
            "title": title.format(n=len(rs))[:60],
            "link": link,
            "action": action,
            "back": back,
            "folders": [r["folder"] for r in rs],
            "detail": "; ".join(f"{r['folder']}: {r['next_step'][:140]}" for r in rs),
            "refs": sorted({x for r in rs for x in r["refs"].split("; ") if x}),
            "addedBy": "no_cracks.py",
        })
    return out


def render(rows):
    lines = ["\t".join(COLUMNS)]
    for r in rows:
        lines.append("\t".join(str(r[c]).replace("\t", " ") for c in COLUMNS))
    return "\n".join(lines) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--board", help="board cards export (JSON); without it every owner row is MISSING")
    ap.add_argument("--root", default=ROOT)
    ap.add_argument("--out", default=None, help="default <root>/NO-CRACKS.tsv")
    ap.add_argument("--cards-json", help="write proposed new cards (who=owner/outside rows with no card) here")
    ap.add_argument("--report-only", action="store_true", help="always exit 0")
    a = ap.parse_args(argv)
    rows = build(a.root, a.board)
    out = a.out or os.path.join(a.root, "NO-CRACKS.tsv")
    with open(out, "w", encoding="utf-8") as f:
        f.write(render(rows))
    if a.cards_json:
        with open(a.cards_json, "w", encoding="utf-8") as f:
            json.dump(proposed_cards(rows), f, indent=1, ensure_ascii=False)
            f.write("\n")
    count = lambda pred: sum(1 for r in rows if pred(r))
    missing = count(lambda r: "MISSING" in r["flags"])
    nonext = count(lambda r: "NO-NEXT" in r["flags"])
    print(f"no_cracks: {len(rows)} rows; owner {count(lambda r: r['who'] == 'owner')}, "
          f"outside {count(lambda r: r['who'] == 'outside')}, agent {count(lambda r: r['who'] == 'agent')}, "
          f"none {count(lambda r: r['who'] == 'none')}; MISSING {missing}, NO-NEXT {nonext} -> {out}")
    for r in rows:
        if r["flags"]:
            print(f"  {r['flags']:<16} {r['who']:<7} {r['folder']}")
    return 0 if a.report_only or not (missing or nonext) else 1


if __name__ == "__main__":
    sys.exit(main())
