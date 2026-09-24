#!/usr/bin/env python3
"""Render status.json into dashboard.html, the one-page project board.

Usage: python3 tools/build_dashboard.py   (from the repo root)
Then publish dashboard.html. The board and STATUS.md must say the same thing; status.json is the source.

Layout (redesigned 24 Sept 2026 for the owner): where we stand in one line; the novelty ladder N0-N5 with every
classed reading on its rung and what the next rung needs; the scoreboard by kind of result; the owner's card
(emails and clicks, tick boxes, JSTOR queue); the pipeline funnel by stage; the lanes; results by kind; targets
grouped by who holds them; change log; queue.
"""
import html
import re
import json
import os
from collections import Counter

d = json.load(open("status.json", encoding="utf-8"))
E = html.escape
REPO = "https://github.com/NoAutopilot/cipher-lab/tree/main/"

def load_asks():
    rows = []
    if not os.path.exists("ASKS.md"):
        return rows
    for line in open("ASKS.md", encoding="utf-8"):
        if not line.startswith("| ") or line.startswith("| # ") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
        if len(cells) < 7 or not cells[0].isdigit():
            continue
        row, raised, _proj, what, action, who, status = cells[:7]
        st = status.split(":")[0].split("(")[0].strip().lower()
        if st in ("done", "dropped", "lapsed"):
            continue
        rows.append({"row": int(row), "raised": raised, "what": what, "action": action, "who": who, "status": status})
    return rows

def load_emails():
    out = []
    if not os.path.isdir("outreach"):
        return out
    for fn in sorted(os.listdir("outreach")):
        if not fn.endswith(".md"):
            continue
        txt = open(os.path.join("outreach", fn), encoding="utf-8").read()
        head = {}
        for line in txt.split("\n")[:8]:
            m = re.match(r"^(to|subject|checked|status):\s*(.*)$", line)
            if m:
                head[m.group(1)] = m.group(2).strip()
        st = head.get("status", "")
        if not (st == "ready" or st.startswith("drafted")):
            continue
        if "## Text" in txt:
            body = txt.split("## Text", 1)[1].split("\n## ", 1)[0].strip()
        else:
            lines = txt.split("\n")
            k = 0
            while k < len(lines) and re.match(r"^(to|subject|checked|status):", lines[k]):
                k += 1
            body = "\n".join(lines[k:]).strip()
        out.append({"slug": fn[:-3], "to": head.get("to", ""), "subject": head.get("subject", ""), "checked": head.get("checked", ""), "text": body, "status": st})
    return out

def load_jstor_queue():
    if not os.path.exists("JSTOR-QUEUE.tsv"):
        return 0, 0
    q = done = 0
    for i, line in enumerate(open("JSTOR-QUEUE.tsv", encoding="utf-8")):
        if i == 0 or not line.strip():
            continue
        cells = line.rstrip("\n").split("\t")
        st = cells[3].strip() if len(cells) > 3 else ""
        if st == "queued": q += 1
        elif st.startswith("done"): done += 1
    return q, done

def load_second_opinions():
    """SECOND-OPINIONS-QUEUE.tsv rows keyed by folder: label, status (queued/posted/checked/withdrawn), pr, outcome."""
    out = {}
    if not os.path.exists("SECOND-OPINIONS-QUEUE.tsv"):
        return out
    for i, line in enumerate(open("SECOND-OPINIONS-QUEUE.tsv", encoding="utf-8")):
        if i == 0 or not line.strip():
            continue
        c = line.rstrip("\n").split("\t")
        c += [""] * (7 - len(c))
        row = {"label": c[0].strip(), "folder": c[1].strip(), "status": c[4].strip(), "pr": c[5].strip(), "outcome": c[6].strip()}
        out.setdefault(row["folder"], []).append(row)
    return out

def so_rows_for(r):
    """Second-opinion rows for a result: by folder, narrowed by a label token (F29R, F30, 126, 53) found in the title.
    Only readings carry the chip (kinds solve and reading); corrections, datasets and catches do not."""
    if r.get("kind") in ("contribution", "correction", "dataset", "negative", "catch"):
        return []
    folder = r["link"].replace(REPO, "").strip("/")
    rows = [x for x in second_opinions.get(folder, []) if not x["status"].startswith("withdrawn")]
    if len(rows) > 1:
        t = r["title"].lower()
        narrowed = []
        for x in rows:
            toks = [k.lower() for k in x["label"].split("-")[2:] if re.search(r"\d", k)]
            ok = False
            for k in toks:
                if k[0] == "f" and k[1:2].isdigit():
                    ok = ok or re.search(r"f\.?\s?" + re.escape(k[1:]) + r"(?![0-9])", t) is not None
                else:
                    ok = ok or re.search(r"(?<![0-9])" + re.escape(k) + r"(?![0-9])", t) is not None
            if ok:
                narrowed.append(x)
        rows = narrowed or rows
    return rows

SO_STATE = {"queued": ("so-q", "second opinion queued"), "posted": ("so-p", "second opinion posted"), "checked": ("so-c", "second opinion checked")}
def so_chip(r):
    out = ""
    for x in so_rows_for(r):
        st = x["status"].split()[0] if x["status"] else ""
        if st not in SO_STATE:
            continue
        cls, txt = SO_STATE[st]
        tip = x["label"] + (f", PR #{x['pr']}" if x["pr"] else "") + (f": {x['outcome']}" if x["outcome"] else "")
        icon = {"queued": "&#9711;", "posted": "&#9993;", "checked": "&#10003;"}[st]
        out += f' <span class="so {cls}" title="{E(tip)}">{icon} {E(txt)}' + (f' <span class="muted">({E(x["outcome"])})</span>' if st == "checked" and x["outcome"] else "") + '</span>'
    return out

asks = load_asks()
emails = load_emails()
second_opinions = load_second_opinions()
jq, jdone = load_jstor_queue()
stages = d["stages"]
NS = len(stages)
results = d.get("results", [])
targets_all = d["targets"]
workers_all = d["workers"]
lanes = d.get("lanes", [])

# ---------- the ladder ----------
LADDER = [
    ("N0", "Already known", "plaintext and decipherment of this item were in print"),
    ("N1", "Text in print", "plaintext published; ours is an independent re-decipherment"),
    ("N2", "Mapping new", "plaintext known elsewhere, no prior mapping of this cipher"),
    ("N3", "Nothing found", "no prior plaintext or decipherment after the logged search"),
    ("N4", "Everywhere looked", "the principal editions, catalogues and project pages all covered"),
    ("N5", "Confirmed", "by the holding archive or a specialist"),
]
def nclass(r):
    m = re.search(r"\bN([0-5])\b", r.get("grade", ""))
    return int(m.group(1)) if m else None
def audits(r):
    g = r.get("grade", "")
    n = nclass(r)
    # An N4 or N5 is set only after the adversarial second audit (CLAUDE.md rule 10 and the Outreach gates), so it
    # always counts as two audits even when the verifier's grade text no longer says so (fix of 24 Sept 2026 13:25 UTC,
    # when nine N4 rows showed as one unique solve). A row of kind "solve" is by policy N3 or better after two audits.
    if n is not None and n >= 4: return 2
    if r.get("kind") == "solve": return 2
    if "two audits" in g: return 2
    if "single audit" in g or "one audit" in g: return 1
    return 1 if n is not None else 0
rungs = {i: [] for i in range(6)}
for r in results:
    # Any classed reading sits on the ladder, whatever its kind label (a recovery by alignment that reached N4 is a
    # unique solve by the policy; fix of 24 Sept 2026 13:28 UTC). Catches (N0/N1 found-solved) stay on their rung too.
    if nclass(r) is not None and r["kind"] not in ("dataset", "correction", "negative"):
        rungs[nclass(r)].append(r)
def short(t, n=70):
    return t if len(t) <= n else t[:n-1].rstrip(" ,;:") + "…"
ladder_cols = ""
for i, (code, name, desc) in reversed(list(enumerate(LADDER))):
    items = ""
    for r in rungs[i]:
        a = audits(r)
        a_txt = {0: "no audit", 1: "one audit", 2: "two audits"}[a]
        gap = r.get("gap", "")
        cls = "rung-item" + (" unique" if (i >= 3 and a >= 2) else "")
        slug = re.sub(r"[^a-z0-9]+", "-", r["title"].lower())[:40].strip("-")
        audit = r["link"].rstrip("/") + "/AUDIT.md"
        chip = so_chip(r)
        items += (f'<li class="{cls}"><a href="{E(r["link"])}">{E(short(r["title"], 96))}</a>'
                  f'<span class="rung-meta">{E(a_txt)}' + (f' · <b>next rung needs:</b> {E(short(gap, 140))}' if gap else '') + '</span>' + chip + '</li>')
    hi = " hi" if i >= 3 else ""
    empty = '<li class="muted empty">nothing here yet</li>'
    ladder_cols += (f'<div class="rung{hi}"><div class="rung-head"><div><span class="rung-code">{code}</span> <span class="rung-name">{E(name)}</span></div>'
                    f'<div class="rung-desc muted">{E(desc)}</div><div class="rung-count muted">{len(rungs[i])} reading{"s" if len(rungs[i]) != 1 else ""}</div></div>'
                    f'<ul class="rung-list">{items or empty}</ul></div>')
n_unique = sum(1 for i in (3, 4, 5) for r in rungs[i] if audits(r) >= 2)
n_climbing = sum(len(rungs[i]) for i in range(6)) - n_unique
n_pending = sum(1 for t in targets_all if t["stage"] == 8)

# ---------- scoreboard ----------
rc = Counter(x["kind"] for x in results)
n_handed = rc.get("contribution", 0)
n_corr = rc.get("correction", 0) + rc.get("catch", 0)
n_neg = rc.get("negative", 0)
n_data = rc.get("dataset", 0)
live_workers = sum(1 for w in workers_all if w["state"] == "running") + sum(int(l.get("live", 0)) for l in lanes)
n_you = sum(1 for t in targets_all if t["state"] == "you")
n_asks_you = sum(1 for a in asks if "owner" in a["who"].lower() or "you" in a["who"].lower())
headline = d.get("headline") or (
    f"{n_unique} unique solve{'s' if n_unique != 1 else ''} at N3 or better after two audits, {n_climbing} more reading{'s' if n_climbing != 1 else ''} on the ladder, "
    f"{n_handed} finding{'s' if n_handed != 1 else ''} handed on, {n_corr} corrections and catches. {live_workers} workers live."
)

# ---------- your card ----------
NL = chr(10)
def card_li(m):
    drafted = m["status"] != "ready"
    licls = ' class="drafted"' if drafted else ""
    dis = " disabled" if drafted else ""
    return (f'<li data-row="{E(m["slug"])}" id="ask-{E(m["slug"])}"{licls}><input type="checkbox" aria-labelledby="ask-what-{E(m["slug"])}"{dis}><div>'
            + (f'<div class="ask-meta warn">{E(m["status"])}</div>' if drafted else "")
            + f'<div class="ask-what" id="ask-what-{E(m["slug"])}"><span class="muted">Subject:</span> {E(m["subject"])}</div>'
            f'<div class="ask-action"><b>To:</b> {E(m["to"])}</div>'
            + (f'<div class="ask-meta"><span class="ok">&#10003; checked</span> {E(m["checked"])}</div>' if m["checked"] else "")
            + f'<details><summary>Text to send</summary><pre class="mail">Subject: {E(m["subject"])}{NL}{NL}{E(m["text"])}</pre><button type="button" class="copy" data-for="mail-{E(m["slug"])}">Copy subject and text</button><textarea id="mail-{E(m["slug"])}" hidden>Subject: {E(m["subject"])}{NL}{NL}{E(m["text"])}</textarea></details>'
            f'</div></li>')
card_items = "".join(card_li(m) for m in emails)
jstor_line = (f'<b>{jq}</b> JSTOR quer{"y" if jq == 1 else "ies"} waiting for your runner' + (f', {jdone} answered' if jdone else '') +
              ' (<a href="' + REPO + 'JSTOR-QUEUE.tsv">JSTOR-QUEUE.tsv</a>, runner brief in <a href="' + REPO + 'tools/jstor_runner_brief.md">tools/jstor_runner_brief.md</a>).') if jq or jdone else ''
other_asks = [a for a in asks if not any(k in a["what"].lower() for k in ("history purge", "decode login"))]
asks_items = "".join(f'<li><span class="mono muted">row {a["row"]}</span> {E(short(a["what"], 110))} <span class="muted">· {E(a["status"][:60])}</span></li>' for a in other_asks)

# ---------- funnel ----------
stage_counts = Counter(t["stage"] for t in targets_all)
maxc = max(stage_counts.values()) if stage_counts else 1
funnel = "".join(
    f'<div class="f-row"><div class="f-lab"><span class="k-num">{i+1}</span>{E(s)}</div><div class="f-bar"><div class="f-fill" style="width:{int(100*stage_counts.get(i+1,0)/maxc)}%"></div></div><div class="f-n num">{stage_counts.get(i+1,0)}</div></div>'
    for i, s in enumerate(stages)
)
holders = Counter(t["holder"] for t in targets_all)
holder_line = ", ".join(f"{v} with {('you' if k == 'You' else k.lower())}" for k, v in holders.most_common())

# ---------- lanes ----------
lane_cards = "".join(
    f'<div class="lane"><div class="lane-name">{E(l["name"])}</div><div class="lane-live"><span class="num">{E(str(l.get("live", "")))}</span> live</div><div class="lane-focus muted">{E(l.get("focus", ""))}</div></div>'
    for l in lanes
)

# ---------- results by kind ----------
KIND = {"solve": ("Unique solves", "k-solve"), "reading": ("Readings with a class", "k-reading"), "contribution": ("Handed on", "k-contrib"),
        "correction": ("Corrections", "k-corr"), "catch": ("Caught before spending", "k-catch"), "negative": ("Negatives with a control", "k-neg"), "dataset": ("Datasets and tools", "k-data")}
def result_li(x):
    return (f'<li><span class="rk {KIND[x["kind"]][1]}">{E(KIND[x["kind"]][0].rstrip("s") if x["kind"] in ("solve","correction","dataset") else KIND[x["kind"]][0])}</span>'
            f'<div><div class="r-title">{E(x["title"])} <span class="muted">{E(x["grade"])}</span>{so_chip(x)}</div><div class="r-line">{E(x["line"])}</div>'
            f'<div class="r-meta"><span class="mono muted">{E(x["date"])}</span> · <a href="{E(x["link"])}">{E(x["link"].replace(REPO, ""))}</a></div></div></li>')
result_groups = ""
for k in ("solve", "reading", "contribution", "correction", "catch", "negative", "dataset"):
    xs = [x for x in results if x["kind"] == k]
    if not xs: continue
    opened = " open" if k in ("solve", "reading", "contribution") else ""
    result_groups += f'<details class="rg"{opened}><summary><span class="rk {KIND[k][1]}">{E(KIND[k][0])}</span> <span class="num">{len(xs)}</span></summary><ul class="results">{"".join(result_li(x) for x in xs)}</ul></details>'

# ---------- targets ----------
def chip(state):
    label = {"waiting": "Waiting on archive", "active": "Worker on it", "queued": "Queued", "blocked": "Blocked", "you": "Needs you", "solved": "Solved"}[state]
    return f'<span class="chip chip-{state}">{label}</span>'
KINDT = {"recovery": "Recovery", "cryptanalysis": "Cryptanalysis", "contribution": "Contribution", "undecided": "Kind undecided"}
def kind_chip(t):
    k = t.get("kind", "undecided")
    return f'<span class="chip chip-kind-{k}">{KINDT[k]}</span>'
def target_row(t):
    segs = "".join(f'<span class="seg {"on" if i < t["stage"] else ""} {"cur" if i == t["stage"] - 1 else ""}" title="{E(s)}"></span>' for i, s in enumerate(stages))
    folder = f'<a class="mono" href="{REPO}{E(t["folder"])}">{E(t["folder"])}</a>' if t["folder"] else ''
    return f'''
    <article class="target state-{t["state"]}">
      <div class="t-head"><h3>{E(t["name"])} <span class="year">{E(t["year"])}</span></h3><span class="chips">{kind_chip(t)} {chip(t["state"])}</span></div>
      <div class="t-ref mono">{E(t["ref"])}</div>
      <div class="segs">{segs}</div>
      <div class="stage-label"><b>Stage {t["stage"]} of {NS}</b> {E(stages[t["stage"]-1])} <span class="muted">· held by {E(t["holder"])} · waiting on {E(t["wait"]["on"])}</span></div>
      {('<p class="result"><b>Result so far:</b> ' + E(t["result"]) + '</p>') if t.get("result") else ''}
      <p class="next"><b>Next:</b> {E(t["next"])}</p>
      <details><summary>Note and unblock</summary><p class="note muted">{E(t["note"])}</p><p class="note muted"><b>What unblocks it:</b> {E(t["wait"]["unblock"])} · since {E(t["wait"]["since"])} · expected {E(t["wait"]["expected"])} {folder}</p></details>
    </article>'''
groups = [("Live now", [t for t in targets_all if t["state"] == "active"]),
          ("Needs you", [t for t in targets_all if t["state"] == "you"]),
          ("Waiting on an archive", [t for t in targets_all if t["state"] == "waiting"]),
          ("Queued", [t for t in targets_all if t["state"] == "queued"]),
          ("Blocked or closed", [t for t in targets_all if t["state"] in ("blocked", "solved")])]
target_groups = "".join(
    f'<details class="tg"{" open" if name in ("Live now", "Needs you") else ""}><summary>{E(name)} <span class="num">{len(ts)}</span></summary><div class="targets">{"".join(target_row(t) for t in ts)}</div></details>'
    for name, ts in groups if ts
)

workers = "".join(
    f'<li class="w-{E(w["state"].split(",")[0].split(" ")[0])}"><span class="dot"></span><div><div class="w-title">{E(w["title"])}</div><div class="muted">{E(w["job"])}</div></div><span class="w-state">{E(w["state"])}</span></li>'
    for w in workers_all
)
queue = "".join(
    f'<tr><td class="num">{q["rank"]}</td><td>{E(q["name"])}</td><td class="num">{E(q["year"])}</td><td class="num"><b>{q["total"]}</b><span class="muted">/39</span></td><td>{E(q["next"])}</td></tr>'
    for q in d["queue"]
)
log = "".join(f'<li><span class="mono muted when">{E(l["when"])}</span><span>{E(l["what"])}</span></li>' for l in d["log"])

page = f'''<title>Cipher Lab Board</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,500;6..72,600&family=Source+Sans+3:wght@400;600&family=JetBrains+Mono:wght@400;500&display=swap">
<style>
:root {{
  --ground:#F4F5F7; --surface:#FFFFFF; --ink:#1B2230; --muted:#5F6978; --line:#D9DEE6; --accent:#2F4BC7; --accent-soft:#E4E9FA;
  --good:#1F8A4C; --good-soft:#E3F3E8; --warn:#A8690F; --warn-soft:#FBF0DC; --bad:#B42318; --bad-soft:#FCE4E1; --info:#2F4BC7; --info-soft:#E4E9FA; --idle:#6B7482; --idle-soft:#E9ECF0;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --ground:#11151C; --surface:#1A2029; --ink:#E7EAF0; --muted:#98A2B1; --line:#2A3240; --accent:#8EA2F5; --accent-soft:#232C48;
  --good:#5CC98A; --good-soft:#173324; --warn:#E0A64A; --warn-soft:#3A2B10; --bad:#F08578; --bad-soft:#3F1B18; --info:#8EA2F5; --info-soft:#232C48; --idle:#98A2B1; --idle-soft:#242B36;
}} }}
:root[data-theme="dark"] {{
  --ground:#11151C; --surface:#1A2029; --ink:#E7EAF0; --muted:#98A2B1; --line:#2A3240; --accent:#8EA2F5; --accent-soft:#232C48;
  --good:#5CC98A; --good-soft:#173324; --warn:#E0A64A; --warn-soft:#3A2B10; --bad:#F08578; --bad-soft:#3F1B18; --info:#8EA2F5; --info-soft:#232C48; --idle:#98A2B1; --idle-soft:#242B36;
}}
body {{ background:var(--ground); color:var(--ink); font-family:"Source Sans 3", "Segoe UI", system-ui, sans-serif; font-size:16px; line-height:1.45; padding-block:24px 48px; padding-inline:clamp(16px, 4vw, 40px); }}
.wrap {{ max-width:1120px; margin-inline:auto; display:grid; gap:26px; }}
h1,h2,h3 {{ font-family:"Newsreader", Georgia, serif; font-weight:600; margin:0; text-wrap:balance; }}
h1 {{ font-size:2rem; }} h2 {{ font-size:1.35rem; margin-bottom:10px; }} h3 {{ font-size:1.15rem; }}
.mono {{ font-family:"JetBrains Mono", ui-monospace, Menlo, monospace; font-size:0.85em; }}
.muted {{ color:var(--muted); }} .num {{ font-variant-numeric:tabular-nums; white-space:nowrap; }}
a {{ color:var(--accent); text-decoration:none; }} a:hover, a:focus-visible {{ text-decoration:underline; outline:none; }}
header {{ display:grid; gap:6px; border-bottom:1px solid var(--line); padding-bottom:12px; }}
header .top {{ display:flex; flex-wrap:wrap; align-items:baseline; justify-content:space-between; gap:8px 24px; }}
.headline {{ font-family:"Newsreader", Georgia, serif; font-size:1.2rem; }}
.panel {{ background:var(--surface); border:1px solid var(--line); border-radius:6px; padding:16px 18px; }}
.how {{ font-size:0.92rem; margin:0 0 10px; }}
/* ladder */
.ladder {{ display:grid; gap:10px; }}
@media (max-width:760px) {{ .rung {{ grid-template-columns:minmax(0,1fr); }} }}
.rung, .rung-item, .tile, .card li, .lanes > *, .results li > * {{ min-width:0; }} .rung-item a, .r-title, .r-line, .rung-meta {{ overflow-wrap:anywhere; }}
.rung {{ border:1px solid var(--line); border-radius:6px; padding:12px 14px; background:var(--ground); display:grid; grid-template-columns:190px minmax(0,1fr); gap:14px; align-items:start; }}
.rung-count {{ font-size:0.78rem; margin-top:6px; }}
.rung.hi {{ background:var(--good-soft); border-color:var(--good); }}
.rung-head {{ display:grid; gap:2px; }} .rung-code {{ font-family:"JetBrains Mono", monospace; font-weight:600; font-size:1.05rem; }} .rung-name {{ font-weight:600; }}
.rung-desc {{ font-size:0.8rem; line-height:1.3; }}
.rung-list {{ list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(auto-fill, minmax(280px, 1fr)); gap:8px; }}
.rung-item {{ background:var(--surface); border:1px solid var(--line); border-radius:4px; padding:6px 8px; font-size:0.9rem; display:grid; gap:2px; }}
.rung-item.unique {{ border-color:var(--good); box-shadow:0 0 0 2px var(--good-soft); }}
.xc-text {{ white-space:pre-wrap; overflow-wrap:anywhere; font-size:0.72rem; max-height:220px; overflow:auto; }}
.rung-meta {{ font-size:0.78rem; color:var(--muted); }} .empty {{ font-size:0.85rem; }}
/* tiles */
.tiles {{ display:grid; grid-template-columns:repeat(auto-fit, minmax(150px, 1fr)); gap:12px; }} .wrap > * {{ min-width:0; }}
.tile {{ background:var(--surface); border:1px solid var(--line); border-radius:6px; padding:14px 16px; }}
.tile .n {{ font-family:"Newsreader", Georgia, serif; font-size:2.2rem; line-height:1; font-variant-numeric:tabular-nums; }}
.tile .l {{ color:var(--muted); font-size:0.85rem; text-transform:uppercase; letter-spacing:0.06em; margin-top:6px; }} .tile .sub {{ font-size:0.85rem; margin-top:4px; }}
.tile.good .n {{ color:var(--good); }}
/* card */
.card {{ list-style:none; margin:0; padding:0; display:grid; gap:8px; }}
.card li {{ display:grid; grid-template-columns:22px 1fr; gap:12px; align-items:start; padding:10px 12px; border:1px solid var(--line); border-radius:6px; background:var(--surface); }}
.card li.done {{ opacity:0.55; }} .card li.drafted {{ opacity:0.8; border-style:dashed; }} .warn {{ color:#b26a00; font-weight:600; }} .card li.done .ask-what {{ text-decoration:line-through; }}
.card input[type=checkbox] {{ width:20px; height:20px; margin-top:2px; accent-color:var(--good); cursor:pointer; }}
.ask-what {{ font-weight:600; }} .ask-action {{ font-size:0.92rem; margin-top:2px; }} .ask-meta {{ font-size:0.8rem; color:var(--muted); margin-top:4px; }}
.card-note {{ font-size:0.85rem; color:var(--muted); margin:8px 0 0; }}
.ok {{ color:var(--good); font-weight:600; }} .mail {{ white-space:pre-wrap; font-family:inherit; font-size:0.92rem; background:var(--ground); padding:10px 12px; border-radius:4px; margin:8px 0; }}
details summary {{ cursor:pointer; color:var(--accent); font-size:0.92rem; margin-top:4px; }} .copy {{ font:inherit; font-size:0.85rem; padding:4px 10px; border:1px solid var(--line); border-radius:4px; background:var(--surface); color:var(--ink); cursor:pointer; }}
.asks {{ list-style:none; margin:10px 0 0; padding:0; display:grid; gap:4px; font-size:0.9rem; }}
/* funnel + lanes */
.two {{ display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:24px; }} @media (max-width:760px) {{ .two {{ grid-template-columns:1fr; }} }}
.f-row {{ display:grid; grid-template-columns:200px 1fr 36px; gap:10px; align-items:center; font-size:0.9rem; padding:3px 0; }}
.f-bar {{ height:10px; background:var(--idle-soft); border-radius:3px; overflow:hidden; }} .f-fill {{ height:100%; background:var(--accent); }}
.k-num {{ display:inline-block; width:1.6em; color:var(--muted); font-variant-numeric:tabular-nums; }}
.lanes {{ display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; }}
.lane {{ border:1px solid var(--line); border-radius:6px; padding:10px 12px; background:var(--ground); }} .lane-name {{ font-weight:600; }} .lane-live {{ font-size:1.4rem; font-family:"Newsreader", Georgia, serif; }} .lane-focus {{ font-size:0.85rem; }}
/* results */
.rg summary {{ font-size:1rem; color:var(--ink); margin:6px 0; }}
.results {{ list-style:none; margin:0; padding:0; display:grid; gap:10px; }}
.results li {{ display:grid; grid-template-columns:150px minmax(0,1fr); gap:12px; align-items:start; padding:10px 0; border-top:1px solid var(--line); }}
.rk {{ font-size:0.75rem; font-weight:600; text-transform:uppercase; letter-spacing:0.05em; padding:3px 8px; border-radius:999px; white-space:nowrap; justify-self:start; margin-top:2px; }}
.k-solve {{ background:var(--good-soft); color:var(--good); }} .k-reading {{ background:var(--info-soft); color:var(--info); }} .k-contrib {{ background:var(--warn-soft); color:var(--warn); }} .k-corr {{ background:var(--accent-soft); color:var(--accent); }} .k-catch {{ background:var(--idle-soft); color:var(--idle); }} .k-neg {{ background:var(--idle-soft); color:var(--idle); }} .k-data {{ background:var(--idle-soft); color:var(--idle); }}
.so {{ display:inline-block; font-size:0.72rem; font-weight:600; padding:2px 7px; border-radius:6px; margin:2px 0 0 0; vertical-align:middle; white-space:normal; line-height:1.3; border:1px solid var(--line); }}
.so-q {{ color:#7a7a7a; }} .so-p {{ color:#1d5fa8; border-color:#1d5fa8; }} .so-c {{ color:#1b7a3d; border-color:#1b7a3d; }}
.r-title {{ font-weight:600; }} .r-line {{ font-size:0.92rem; margin-top:2px; }} .r-meta {{ font-size:0.8rem; margin-top:4px; }}
@media (max-width:600px) {{ .results li {{ grid-template-columns:1fr; gap:4px; }} }}
/* targets */
.tg summary {{ font-size:1.1rem; color:var(--ink); margin:8px 0; font-family:"Newsreader", Georgia, serif; }}
.targets {{ display:grid; gap:12px; margin:8px 0 16px; }}
.target {{ background:var(--surface); border:1px solid var(--line); border-left:4px solid var(--idle); border-radius:6px; padding:14px 16px; display:grid; gap:6px; }}
.target.state-waiting {{ border-left-color:var(--warn); }} .target.state-active {{ border-left-color:var(--info); }} .target.state-blocked {{ border-left-color:var(--bad); }} .target.state-solved {{ border-left-color:var(--good); }} .target.state-you {{ border-left-color:var(--accent); }}
.t-head {{ display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:8px; }}
.year {{ color:var(--muted); font-weight:500; font-size:0.9em; margin-left:6px; }}
.chip {{ font-size:0.78rem; font-weight:600; text-transform:uppercase; letter-spacing:0.05em; padding:3px 9px; border-radius:999px; white-space:nowrap; }}
.chips {{ display:flex; gap:6px; flex-wrap:wrap; }}
.chip-kind-recovery {{ background:var(--good-soft); color:var(--good); }} .chip-kind-cryptanalysis {{ background:var(--accent-soft); color:var(--accent); }} .chip-kind-contribution {{ background:var(--warn-soft); color:var(--warn); }} .chip-kind-undecided {{ background:var(--idle-soft); color:var(--idle); }}
.chip-waiting {{ background:var(--warn-soft); color:var(--warn); }} .chip-active {{ background:var(--info-soft); color:var(--info); }} .chip-queued {{ background:var(--idle-soft); color:var(--idle); }} .chip-blocked {{ background:var(--bad-soft); color:var(--bad); }} .chip-you {{ background:var(--accent-soft); color:var(--accent); }} .chip-solved {{ background:var(--good-soft); color:var(--good); }}
.result {{ margin:0; padding:8px 12px; border-left:3px solid var(--good); background:var(--good-soft); border-radius:3px; }}
.segs {{ display:grid; grid-template-columns:repeat({NS}, 1fr); gap:3px; margin-top:4px; }}
.seg {{ height:8px; border-radius:2px; background:var(--idle-soft); }} .seg.on {{ background:var(--accent); }} .seg.cur {{ outline:2px solid var(--accent); outline-offset:1px; }}
.state-waiting .seg.on {{ background:var(--warn); }} .state-waiting .seg.cur {{ outline-color:var(--warn); }} .state-blocked .seg.on {{ background:var(--bad); }} .state-blocked .seg.cur {{ outline-color:var(--bad); }} .state-solved .seg.on {{ background:var(--good); }}
.stage-label {{ font-size:0.9rem; }} .next {{ margin:0; }} .note {{ margin:4px 0 0; font-size:0.9rem; }}
/* workers, log, queue */
.workers, .log {{ list-style:none; margin:0; padding:0; display:grid; gap:10px; }}
.workers li {{ display:grid; grid-template-columns:10px 1fr auto; gap:10px; align-items:start; }}
.dot {{ width:10px; height:10px; border-radius:50%; margin-top:6px; background:var(--idle); }} .w-running .dot {{ background:var(--info); }} .w-done .dot {{ background:var(--good); }}
.w-title {{ font-weight:600; }} .w-state {{ font-size:0.78rem; text-transform:uppercase; letter-spacing:0.05em; color:var(--muted); }}
.log li {{ display:grid; grid-template-columns:110px 1fr; gap:10px; }} .when {{ white-space:nowrap; }}
.tablewrap {{ overflow-x:auto; }} table {{ border-collapse:collapse; width:100%; font-size:0.95rem; }}
th, td {{ text-align:left; padding:7px 10px; border-bottom:1px solid var(--line); vertical-align:top; }} th {{ color:var(--muted); font-size:0.78rem; text-transform:uppercase; letter-spacing:0.05em; font-weight:600; }}
@media (prefers-reduced-motion: no-preference) {{ .seg, .f-fill {{ transition:background .2s, width .3s; }} }}
</style>
<div class="wrap">
  <header>
    <div class="top"><h1>Cipher Lab Board</h1><div class="muted">Updated {E(d["updated"])}</div></div>
    <div class="headline">{E(headline)}</div>
  </header>

  <section class="panel" id="ladder">
    <h2>The novelty ladder</h2>
    <p class="how muted">Every reading a separate verifier has classed, on its rung. Only a verifier moves a card, from its AUDIT.md, and only after trying to find the text in print. A unique solve is N3 or better after two audits (outlined). "Next rung needs" is what the last auditor said still stands between the reading and the rung above.</p>
    <div class="ladder">{ladder_cols}</div>
    {('<p class="how muted" style="margin-top:10px">Plus ' + str(n_pending) + ' target' + ('s' if n_pending != 1 else '') + ' at stage 8, read but not yet classed.</p>') if n_pending else ''}
  </section>

  <section class="tiles" aria-label="Scoreboard">
    <div class="tile good"><div class="n">{n_unique}</div><div class="l">Unique solves</div><div class="sub muted">N3 or better, two audits</div></div>
    <div class="tile"><div class="n">{n_climbing}</div><div class="l">Climbing the ladder</div><div class="sub muted">readings with a class below the bar</div></div>
    <div class="tile"><div class="n">{n_handed}</div><div class="l">Handed on</div><div class="sub muted">to a list keeper, a library or an archive</div></div>
    <div class="tile"><div class="n">{n_corr}</div><div class="l">Corrections and catches</div><div class="sub muted">catalogue fixes; solved items caught before money was spent</div></div>
    <div class="tile"><div class="n">{n_neg + n_data}</div><div class="l">Negatives and datasets</div><div class="sub muted">controlled negatives, tools, sweeps</div></div>
    <div class="tile"><div class="n">{live_workers}</div><div class="l">Workers live</div><div class="sub muted">{len(lanes)} lanes</div></div>
    <div class="tile"><div class="n">{n_you + len(emails)}</div><div class="l">On your card</div><div class="sub muted">{len(emails)} to tick, {n_you} targets need a decision</div></div>
  </section>

  <section class="panel" id="your-card">
    <h2>Your card</h2>
    <ul class="card">{card_items or '<li class="muted">nothing to send or click right now</li>'}</ul>
    <p class="card-note">Each item was checked against the gates (class assigned, rule-10 wording, no personal data, links public). Tick it once done; the tick is saved on this page and the orchestrator logs the date. <span id="card-status"></span></p>
    {('<p class="card-note">' + jstor_line + '</p>') if jstor_line else ''}
    {('<details><summary>Other open asks, no rush (' + str(len(other_asks)) + ')</summary><ul class="asks">' + asks_items + '</ul></details>') if other_asks else ''}
  </section>

  <div class="two">
    <section class="panel">
      <h2>Pipeline</h2>
      <p class="how muted">Targets by stage. {E(holder_line)}.</p>
      {funnel}
    </section>
    <section class="panel">
      <h2>Lanes</h2>
      <p class="how muted">Each lane owns its hosts and its targets; readings flow to the verification lane.</p>
      <div class="lanes">{lane_cards or '<div class="muted">no lanes recorded</div>'}</div>
    </section>
  </div>

  <section class="panel" id="results">
    <h2>Results so far</h2>
    <p class="how muted">Every kind the README counts. A reading below N3 is still a checked text; a correction or a catch is a contribution to whoever keeps the catalogue; a negative with a matched control and a dataset handed on count too.</p>
    {result_groups}
  </section>

  <section>
    <h2>Targets</h2>
    {target_groups}
  </section>

  <div class="two">
    <section class="panel">
      <h2>Change log</h2>
      <ul class="log">{log}</ul>
    </section>
    <section class="panel">
      <h2>Workers</h2>
      <ul class="workers">{workers}</ul>
      <p class="how muted">Sessions started for one job each. They push to the repo, report, and stop.</p>
    </section>
  </div>

  <section class="panel">
    <h2>Queue, top of the ranking</h2>
    <div class="tablewrap"><table><thead><tr><th>Rank</th><th>Target</th><th>Year</th><th>Score</th><th>Next step</th></tr></thead><tbody>{queue}</tbody></table></div>
    <p class="how muted">Score out of 39. Full list with rationale in <a href="https://github.com/NoAutopilot/cipher-lab/blob/main/QUEUE.md">QUEUE.md</a>.</p>
  </section>
</div>
<script>
(function () {{
  var list = document.querySelector('.card'); var status = document.getElementById('card-status');
  if (!list) return;
  var items = Array.prototype.slice.call(list.querySelectorAll('li[data-row]'));
  function paint(row, done, when) {{
    var li = document.getElementById('ask-' + row); if (!li) return;
    li.querySelector('input').checked = !!done; li.classList.toggle('done', !!done);
    var meta = li.querySelector('.ask-meta');
    if (done && when && meta && meta.textContent.indexOf('ticked') < 0) meta.textContent += ' · ticked ' + when;
  }}
  function local(row, v) {{ try {{ if (v === undefined) return JSON.parse(localStorage.getItem('ask-' + row) || 'null'); localStorage.setItem('ask-' + row, JSON.stringify(v)); }} catch (e) {{ return null; }} }}
  items.forEach(function (li) {{ var r = li.dataset.row; var v = local(r); if (v) paint(r, v.done, v.when); }});
  var db = null;
  items.forEach(function (li) {{
    li.querySelector('input').addEventListener('change', function (ev) {{
      var r = li.dataset.row; var done = ev.target.checked; var when = new Date().toISOString().slice(0, 10);
      var v = {{ row: r, done: done, when: done ? when : '' }};
      paint(r, done, v.when); local(r, v);
      if (db) db.doc('emails/' + r).set(v).catch(function () {{ if (status) status.textContent = 'Saved on this device only.'; }});
    }});
  }});
  Array.prototype.forEach.call(document.querySelectorAll('.copy'), function (b) {{ b.addEventListener('click', function () {{ var t = document.getElementById(b.dataset.for); if (t && navigator.clipboard) navigator.clipboard.writeText(t.value).then(function () {{ b.textContent = 'Copied'; }}); }}); }});
  if (!window.claude || !window.claude.use) {{ if (status) status.textContent = 'Saved on this device only.'; return; }}
  window.claude.use('db').then(function (ns) {{
    if (!ns) {{ if (status) status.textContent = 'Saved on this device only.'; return; }}
    db = ns;
    db.collection('emails').onSnapshot(function (snap) {{
      snap.docs.forEach(function (doc) {{ if (!doc.exists) return; var v = doc.data(); paint(v.row, v.done, v.when); local(v.row, v); }});
      if (status) status.textContent = 'Saved on this page.';
    }}, function () {{ if (status) status.textContent = 'Saved on this device only.'; }});
  }});
}})();
</script>
'''
open("dashboard.html", "w", encoding="utf-8").write(page)
os.makedirs("docs", exist_ok=True)
open("docs/index.html", "w", encoding="utf-8").write(page)
print(f"dashboard.html and docs/index.html written: {len(page)} bytes, {len(targets_all)} targets, {len(workers_all)} workers, {len(results)} results, {n_unique} unique")
