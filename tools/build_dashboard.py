#!/usr/bin/env python3
"""Build dashboard.html (and docs/index.html) from status.json and the repository's own files.

Rewritten 24 Sept 2026 on the owner's request ("rethink from the ground up"). The board is a research desk with three
views, one question each:
  Readings    what did we find, does it matter, who do we tell (one row per classed reading, opening into its dossier)
  Your desk   what only the owner can do (send, click, decide), with the text ready to copy
  The machine lanes, funnel, targets, workers, log

Inputs: status.json (headline, targets, workers, lanes, results, log, stages), N4-READINGS.md (what each reading says,
rating, links), outreach/*.md (drafts with status/subject/to/targets/links headers), SECOND-OPINIONS-QUEUE.tsv,
JSTOR-QUEUE.tsv, ASKS.md. Nothing personal is read or written. Ticks on the desk are saved to the artifact's own store
(db capability) with a localStorage fallback.
"""
import html
import json
import os
import re
from collections import Counter

E = html.escape
REPO = "https://github.com/NoAutopilot/cipher-lab/tree/main/"
d = json.load(open("status.json", encoding="utf-8"))
results = d.get("results", [])
targets_all = d["targets"]
workers_all = d["workers"]
lanes = d.get("lanes", [])
stages = d["stages"]
headline = d.get("headline", "")

# ---------------------------------------------------------------- loaders

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
        if st in ("done", "dropped", "lapsed", "sent", "answered", "closed"):
            continue
        rows.append({"row": int(row), "raised": raised, "what": what, "action": action, "who": who, "status": status})
    return rows


def parse_headers(txt):
    head, lines, k = {}, txt.split("\n"), 0
    while k < len(lines) and re.match(r"^[a-z]+:\s", lines[k]):
        m = re.match(r"^([a-z]+):\s*(.*)$", lines[k])
        head[m.group(1)] = m.group(2).strip()
        k += 1
    body = "\n".join(lines[k:]).strip()
    if body.startswith("---"):
        body = body.split("\n", 1)[1].strip() if "\n" in body else ""
    return head, body


def load_drafts():
    out = []
    if not os.path.isdir("outreach"):
        return out
    for fn in sorted(os.listdir("outreach")):
        if not fn.endswith(".md"):
            continue
        head, body = parse_headers(open(os.path.join("outreach", fn), encoding="utf-8").read())
        st = head.get("status", "")
        kind = ("ready" if st.startswith("ready") else "drafted" if st.startswith("drafted") else "sent" if re.match(r"^(sent|posted)", st)
                else "done" if re.match(r"^(done|answered|superseded)", st) else "other")
        if kind in ("other", "done"):
            continue
        links = {}
        for part in head.get("links", "").split(";"):
            if "=" in part:
                k, v = part.split("=", 1)
                links[k.strip()] = v.strip()
        targets = [t.strip().strip("`") for t in re.split(r"[,;]\s*", head.get("targets", "")) if t.strip()]
        out.append({"slug": fn[:-3], "status": st, "kind": kind, "subject": head.get("subject", ""), "to": head.get("to", ""),
                    "text": body, "targets": targets, "links": links, "checked": head.get("checked", "")})
    return out


def load_jstor():
    q = done = 0
    if not os.path.exists("JSTOR-QUEUE.tsv"):
        return q, done
    for i, line in enumerate(open("JSTOR-QUEUE.tsv", encoding="utf-8")):
        if i == 0 or not line.strip():
            continue
        c = line.rstrip("\n").split("\t")
        st = c[3].strip() if len(c) > 3 else ""
        if st == "queued":
            q += 1
        elif st.startswith("done"):
            done += 1
    return q, done


def load_second_opinions():
    out = {}
    if not os.path.exists("SECOND-OPINIONS-QUEUE.tsv"):
        return out
    for i, line in enumerate(open("SECOND-OPINIONS-QUEUE.tsv", encoding="utf-8")):
        if i == 0 or not line.strip():
            continue
        c = line.rstrip("\n").split("\t") + [""] * 7
        row = {"label": c[0].strip(), "folder": c[1].strip(), "status": c[4].strip(), "pr": c[5].strip(), "outcome": c[6].strip()}
        if row["status"].startswith("withdrawn"):
            continue
        out.setdefault(row["folder"], []).append(row)
    return out


def load_memo():
    out = []
    if not os.path.exists("N4-READINGS.md"):
        return out
    txt = open("N4-READINGS.md", encoding="utf-8").read()
    for sec in re.split(r"\n(?=## )", txt):
        m = re.match(r"## (ciphers/[\w.-]+)\s*(.*)", sec)
        if not m:
            continue
        body = sec.split("\n", 1)[1] if "\n" in sec else ""
        rating = ""
        mr = re.search(r"^rating:\s*(.+)$", body, re.M)
        if mr:
            rating = mr.group(1).strip()
        links = {}
        ml = re.search(r"^links:\s*(.+)$", body, re.M)
        if ml:
            for part in ml.group(1).split(";"):
                if "=" in part:
                    k, v = part.split("=", 1)
                    links[k.strip()] = v.strip()
        text = re.sub(r"^(rating|links):.*$", "", body, flags=re.M).strip()
        out.append({"folder": m.group(1), "head": m.group(2).strip(), "text": text, "rating": rating, "links": links})
    return out


def md_linkify(s):
    """Turn every '[text](url)' in s into an anchor; escape the rest."""
    out, last = [], 0
    for m in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", s):
        out.append(E(s[last:m.start()]))
        out.append(f'<a href="{E(m.group(2))}">{E(m.group(1))}</a>')
        last = m.end()
    out.append(E(s[last:]))
    return "".join(out)


def load_table(path, min_cells):
    """Pipe-table rows as lists of cell strings, skipping the header and separator lines."""
    if not os.path.exists(path):
        return []
    out = []
    for line in open(path, encoding="utf-8"):
        if not line.startswith("| ") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
        if len(cells) < min_cells or cells[0] in ("Date", "#"):
            continue
        out.append(cells)
    return out


def load_citations():
    out = []
    for cells in load_table("CITATIONS.md", 7):
        date, who, where, what, how, quote, evidence = cells[:7]
        out.append({"date": date, "who": who, "where": where, "what": what, "how": how, "quote": quote, "evidence": evidence})
    return out


def load_contrib_pending():
    """CONTRIBUTIONS.md rows sent and still awaiting a public reply."""
    out = []
    for cells in load_table("CONTRIBUTIONS.md", 8):
        date, item, cls, grade, recipient, channel, what, status = cells[:8]
        st = status.lower()
        if "sent" not in st or "reply pending" not in st:
            continue
        m = re.search(r"\b\d{1,2}\s+Sep\w*\s+\d{4}\b", status)
        out.append({"recipient": recipient, "sent": m.group(0) if m else date, "what": what})
    return out


asks = load_asks()
drafts = load_drafts()
jq, jdone = load_jstor()
second_opinions = load_second_opinions()
memo = load_memo()
citations = load_citations()
contrib_pending = load_contrib_pending()

# ---------------------------------------------------------------- helpers

def nclass(r):
    m = re.search(r"\bN([0-5])\b", r.get("grade", ""))
    return int(m.group(1)) if m else None


def audits(r):
    g = r.get("grade", "")
    if "two audits" in g or (nclass(r) or 0) >= 4 or r.get("kind") == "solve":
        return 2
    if "audit" in g.lower():
        return 1
    return 0


def folder_of(r):
    m = re.search(r"(ciphers/[\w.-]+)", r.get("link", ""))
    return m.group(1) if m else r["link"].replace(REPO, "").strip("/")


def item_tokens(s):
    return set(re.findall(r"\b(?:wvo\s*\d+|f\.\s*\d+[rv]?|e\d|p\d|bla\s*\d+|\d{4})\b", s.lower()))


def memo_for(r):
    f = folder_of(r)
    secs = [x for x in memo if x["folder"] == f]
    toks = item_tokens(r["title"])
    if len(secs) > 1 and toks:
        narrowed = [x for x in secs if item_tokens(x["head"]) & toks]
        secs = narrowed or secs
    return secs[:1]


def so_for(r):
    f = folder_of(r)
    rows = second_opinions.get(f, [])
    if len(rows) > 1:
        t = r["title"].lower()
        narrowed = []
        for x in rows:
            ok = False
            for k in [k.lower() for k in x["label"].split("-")[2:] if re.search(r"\d", k)]:
                if k[0] == "f" and k[1:2].isdigit():
                    ok = ok or re.search(r"f\.?\s?" + re.escape(k[1:]) + r"(?![0-9])", t) is not None
                else:
                    ok = ok or re.search(r"(?<![0-9])" + re.escape(k) + r"(?![0-9])", t) is not None
            if ok:
                narrowed.append(x)
        rows = narrowed or rows
    return rows[:1]


def drafts_for(r):
    f = folder_of(r)
    return [x for x in drafts if f in x["targets"]]


def who(x):
    """Short recipient name from the draft's file name: tomokiyo-gramont-danzay -> Tomokiyo, bourdeau-issue-thurloe -> Bourdeau issue."""
    head = x["slug"].split("-")[0]
    name = {"tomokiyo": "Tomokiyo", "huygens": "Huygens", "huntington": "Huntington", "bourdeau": "Bourdeau", "bowes": "Tomokiyo", "decode": "DECODE", "nls": "NLS"}.get(head, head.capitalize())
    return name + (" issue" if "issue" in x["slug"] else "")


STATE = {"ready": "ready to send", "drafted": "drafted", "sent": "sent, awaiting reply"}


def rating_kind(rating):
    if rating.startswith("adds substantive"):
        return "r-sub", "adds substantive information"
    if rating.startswith("confirms"):
        return "r-conf", "confirms or adds detail"
    if rating.startswith("form"):
        return "r-form", "form and key only"
    return "", ""


def short(t, n=90):
    return t if len(t) <= n else t[:n - 1].rstrip(" ,;:") + "…"


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower())[:48].strip("-")


def md_light(text):
    """The memo is markdown; keep it readable as text: bold markers become emphasis, list markers stay."""
    t = E(text)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?m)^### (.+)$", r"<h5>\1</h5>", t)
    t = re.sub(r"\n{2,}", "</p><p>", t)
    return "<p>" + t.replace("\n", "<br>") + "</p>"


def reflow(text):
    """Join the file's hard-wrapped lines inside a paragraph; keep blank lines, list items and lines that are only a URL."""
    out, buf = [], []
    def flush():
        if buf:
            out.append(" ".join(x.strip() for x in buf)); buf.clear()
    for line in text.split("\n"):
        st = line.strip()
        if not st:
            flush(); out.append("")
        elif st.startswith(("- ", "* ")):
            flush(); buf.append(st)
        elif re.match(r"^https?://\S+,?$", st) or st.startswith("Dear "):
            flush(); out.append(st)
        elif buf and buf[0].startswith(("- ", "* ")) and line.startswith("  "):
            buf.append(st)
        else:
            if buf and buf[0].startswith(("- ", "* ")):
                flush()
            buf.append(st)
    flush()
    return "\n".join(out)


def copy_field(uid, label, value, pre=False):
    """One labelled value with its own copy button (address, subject or body)."""
    if pre:
        shown = f'<pre class="mail">{E(value)}</pre>'
    elif re.match(r"^https?://\S+$", value.strip()):
        shown = f'<a class="val" href="{E(value.strip())}">{E(short(value.strip(), 80))}</a> <span class="muted small">(opens with title and body filled in; press Submit)</span>'
    else:
        shown = f'<code class="val">{E(value)}</code>'
    return (f'<div class="cf"><div class="cf-head"><span class="cf-label">{E(label)}</span>'
            f'<button type="button" class="copy" data-for="{uid}">Copy</button></div>{shown}<textarea id="{uid}" hidden>{E(value)}</textarea></div>')


def copy_block(uid, to, subject, text):
    """Three copy boxes: address, subject, body. `to` may be a non-address instruction; it is still copyable."""
    return ('<div class="cfs">' + copy_field(uid + "-to", "To", to) + copy_field(uid + "-subj", "Subject", subject)
            + copy_field(uid + "-body", "Body", reflow(text), pre=True) + '</div>')

# ---------------------------------------------------------------- readings

LADDER = [("N0", "already known"), ("N1", "text in print"), ("N2", "mapping new"),
          ("N3", "nothing found"), ("N4", "everywhere looked"), ("N5", "confirmed")]
classed = [r for r in results if nclass(r) is not None and r["kind"] not in ("dataset", "correction", "negative")]
classed.sort(key=lambda r: (-(nclass(r)), -audits(r), r["title"]))
counts = Counter(nclass(r) for r in classed)
counted = lambda r: nclass(r) >= 3 and audits(r) >= 2 and not r.get("qa_flag")  # a QA flag holds a result out until its lane clears it
n_unique = sum(1 for r in classed if counted(r))
KEYSRC = {"ours": ("k-ours", "our key", "We recovered the key ourselves: by cryptanalysis, by aligning a plain copy, or by identifying the codebook."),
          "period": ("k-period", "period key, rebuilt by us", "The key comes from a decipherment, key sheet or cipher book of the time, which we turned into a working key."),
          "published": ("k-pub", "published key", "The key was published by someone else (credited in AUDIT.md); we applied it.")}
n_first = sum(1 for r in classed if r.get("key") == "ours" and counted(r))


def reading_row(r, idx):
    n = nclass(r)
    a = audits(r)
    m = memo_for(r)
    so = so_for(r)
    dr = drafts_for(r)
    rid = f"rd-{idx}-{slug(r['title'])}"
    rating = m[0]["rating"] if m else ""
    rk, rlabel = rating_kind(rating)
    chips = ""
    ks = KEYSRC.get(r.get("key", ""))
    if ks:
        chips += f'<span class="chip {ks[0]}" title="{E(ks[2])}">{E(ks[1])}</span>'
    if r.get("text") == "known":
        chips += '<span class="chip k-known" title="The text itself was already in print; what is ours is the key.">text already in print</span>'
    if rlabel:
        chips += f'<span class="chip {rk}">{E(rlabel)}</span>'
    chips += f'<span class="chip c-aud">{["no audit", "one audit", "two audits"][a]}</span>'
    if r.get("qa_flag"):
        chips += f'<span class="chip qa-flag" title="{E(r["qa_flag"])}">QA flag open: not counted</span>'
    if so:
        st = so[0]["status"].split()[0]
        lab = {"queued": "second opinion queued", "posted": "second opinion posted", "checked": "second opinion checked"}.get(st, "")
        if lab:
            chips += f'<span class="chip so-{st}" title="{E(so[0]["label"] + ((": " + so[0]["outcome"]) if so[0]["outcome"] else ""))}">{lab}</span>'
    for x in dr:
        chips += f'<span class="chip out-{x["kind"]}">{E(who(x))}: {STATE[x["kind"]]}</span>'
    unique = ' unique' if counted(r) else ''
    # detail
    parts = [f'<div class="dz"><h4>What it is</h4><p>{E(r.get("line", ""))}</p><p class="mono muted">{E(r.get("grade", ""))}</p></div>']
    if m:
        parts.append(f'<div class="dz"><h4>What the passage says, and why it matters</h4>'
                     + (f'<p class="rating {rk}">{E(rating)}</p>' if rating else "")
                     + f'<div class="memo">{md_light(m[0]["text"])}</div></div>')
    for x in dr:
        sent_box = (f'<label class="sentbox" data-row="{E(x["slug"])}"><input type="checkbox"> Mark as sent</label>' if x["kind"] == "ready" else "")
        covers = ""
        if len(x["targets"]) > 1:
            names = [t.split("/")[-1] for t in x["targets"]]
            covers = f'<p class="muted small">One note covers {len(names)} readings ({E(", ".join(names))}); send it once and tick it once.</p>'
        parts.append(f'<div class="dz"><h4>Who to tell</h4><p><b>{E(x["to"])}</b> <span class="chip out-{x["kind"]}">{E(who(x))}: {STATE[x["kind"]]}</span></p>' + covers +
                     f'<p class="muted small">{E(x["status"])}</p>'
                     + copy_block(f"cp-{rid}-{slug(x['slug'])}", x["to"], x["subject"], x["text"]) + sent_box + '</div>')
    links = {"folder": r["link"], "audit": r["link"].rstrip("/") + "/AUDIT.md"}
    if m:
        links.update({k: v for k, v in m[0]["links"].items() if v and not v.lower().startswith("none")})
    parts.append('<div class="dz"><h4>Links a recipient can check</h4><p class="links">' + " ".join(f'<a href="{E(v)}">{E(k)}</a>' for k, v in links.items()) + '</p></div>')
    if not m and not dr and n >= 3:
        parts.append('<p class="muted small">The significance memo and the outreach note for this reading are not written yet.</p>')
    return (f'<li class="rrow{unique}" data-n="{n}"><button type="button" class="rhead" aria-expanded="false" aria-controls="{rid}">'
            f'<span class="ncls n{n}">N{n}</span><span class="rtitle">{E(r["title"])}</span><span class="rchips">{chips}</span></button>'
            f'<div class="rbody" id="{rid}" hidden>{"".join(parts)}</div></li>')


reading_rows = "".join(reading_row(r, i) for i, r in enumerate(classed))
legend = "".join(f'<button type="button" class="lg" data-n="{i}" aria-pressed="false"><span class="ncls n{i}">{code}</span><span>{name}</span><span class="num">{counts.get(i, 0)}</span></button>'
                 for i, (code, name) in reversed(list(enumerate(LADDER))))
others = [r for r in results if r not in classed]
KIND = {"contribution": "handed on", "correction": "correction", "catch": "caught before spending", "negative": "negative with a control",
        "dataset": "dataset or tool", "reading": "reading", "recovery": "recovery", "cryptanalysis": "cryptanalysis", "solve": "solve"}
other_rows = "".join(f'<li><span class="chip k">{E(KIND.get(r["kind"], r["kind"]))}</span> <a href="{E(r["link"])}">{E(short(r["title"], 110))}</a> <span class="muted small">{E(r["date"])}</span></li>' for r in others)

# ---------------------------------------------------------------- your desk

ready = [x for x in drafts if x["kind"] == "ready"]
drafted = [x for x in drafts if x["kind"] == "drafted"]
sent = [x for x in drafts if x["kind"] == "sent"]
you_targets = [t for t in targets_all if t.get("state") == "you"]


def desk_item(x):
    uid = f"desk-{slug(x['slug'])}"
    waiting = x["kind"] != "ready"
    return (f'<li class="task{" waiting" if waiting else ""}" data-row="{E(x["slug"])}" id="ask-{E(x["slug"])}">'
            f'<input type="checkbox" id="tick-{E(x["slug"])}" aria-label="done"{" disabled" if waiting else ""}>'
            f'<div><div class="tsubj">{E(x["subject"])}</div><div class="tto">To: {E(x["to"])}</div>'
            + (f'<div class="tmeta warn">{E(x["status"])}</div>' if waiting else (f'<div class="tmeta ask-meta">{E(x["status"])}</div>'))
            + copy_block(uid, x["to"], x["subject"], x["text"]) + '</div></li>')


desk_ready = "".join(desk_item(x) for x in ready) or '<li class="muted">nothing waiting on you right now</li>'
desk_waiting = "".join(desk_item(x) for x in drafted)
desk_sent = "".join(f'<li class="task sentrow"><span class="dot on"></span><div><div class="tsubj">{E(x["subject"])}</div><div class="tto">To: {E(x["to"])}</div><div class="tmeta">{E(x["status"])}</div></div></li>' for x in sent)
desk_targets = "".join(f'<li class="task"><input type="checkbox" disabled><div><div class="tsubj">{E(t["name"])} <span class="mono muted">{E(t.get("ref", ""))}</span></div><div class="tto">{E(t.get("next", ""))}</div></div></li>' for t in you_targets)
asks_rows = "".join(f'<li><span class="mono muted">row {a["row"]}</span> {E(short(a["what"], 140))} <span class="muted small">· {E(a["status"][:70])}</span></li>' for a in asks)

# ---------------------------------------------------------------- the machine

live_workers = sum(1 for w in workers_all if w["state"] == "running") + sum(int(l.get("live", 0)) for l in lanes)
lane_rows = "".join(f'<li><div class="lname">{E(l["name"])} <span class="num">{int(l.get("live", 0))} live</span></div><div class="lfocus">{E(l.get("focus", ""))}</div></li>' for l in lanes)
stage_counts = Counter(int(t["stage"]) for t in targets_all)
maxc = max(stage_counts.values()) if stage_counts else 1
funnel = "".join(f'<div class="frow"><div class="flab"><span class="mono muted">{i+1}</span> {E(s)}</div><div class="fbar"><div class="ffill" style="width:{int(100*stage_counts.get(i+1,0)/maxc)}%"></div></div><div class="fn num">{stage_counts.get(i+1,0)}</div></div>' for i, s in enumerate(stages))
targets_sorted = sorted(targets_all, key=lambda t: (-int(t["stage"]), t["name"]))
target_rows = "".join(f'<tr><td><a href="{E(REPO + t["folder"])}">{E(t["name"])}</a><div class="muted small mono">{E(t.get("ref", ""))}</div></td><td class="num">{int(t["stage"])}</td><td>{E(stages[int(t["stage"])-1])}</td><td>{E(t.get("holder", ""))}</td><td>{E(short(t.get("next", ""), 120))}</td></tr>' for t in targets_sorted)
worker_rows = "".join(f'<li><span class="dot {"on" if w["state"] == "running" else "off"}"></span><span>{E(w["title"])}</span><span class="muted small">{E(w["state"])}</span></li>' for w in workers_all if w["state"] == "running") or '<li class="muted">no parent workers running</li>'
log_rows = "".join(f'<li><span class="when mono muted">{E(x["when"])}</span><span>{E(x["what"])}</span></li>' for x in d.get("log", [])[:12])

# ---------------------------------------------------------------- hall of fame


def citation_card(c):
    return (f'<li class="fcard"><div class="fmeta"><span class="fdate mono muted">{E(c["date"])}</span>'
            f'<span class="fwho">{E(c["who"])}</span></div>'
            f'<p class="fwhere">{md_linkify(c["where"])} &rarr; {md_linkify(c["what"])}</p>'
            f'<blockquote class="fquote">{E(c["quote"])}</blockquote>'
            f'<p class="fhow muted small">{E(c["how"])}</p></li>')


fame_cards = "".join(citation_card(c) for c in citations) or '<li class="muted">nothing public yet</li>'
pending_rows = "".join(f'<li><span class="mono muted">{E(p["sent"])}</span> <b>{E(p["recipient"])}</b> &mdash; {E(short(p["what"], 100))}</li>' for p in contrib_pending)

# ---------------------------------------------------------------- side quests

sidequests = d.get("sidequests", [])
SQ_ORDER = {"waiting on you": 0, "running": 1, "blocked": 2, "queued": 3, "done": 4}
sidequests_sorted = sorted(sidequests, key=lambda s: (SQ_ORDER.get(s.get("state", ""), 5), s.get("title", "")))
sq_counts = Counter(s.get("state", "") for s in sidequests)
sq_count_line = f"{len(sidequests)} items: " + ", ".join(
    f"{sq_counts[st]} {st}" for st in ("waiting on you", "running", "blocked", "queued", "done") if sq_counts.get(st))


def sq_card(s):
    st = s.get("state", "")
    chip = f'<span class="chip sq-{slug(st)}">{E(st)}</span>'
    sess = f' <span class="mono muted small">{E(s["session"])}</span>' if s.get("session") else ""
    link = s.get("link", "")
    link_html = f' <a href="{E(REPO + link if not link.startswith("http") else link)}">{E(link)}</a>' if link else ""
    return (f'<li class="sqcard"><div class="sqhead">{chip}<span class="sqtitle">{E(s.get("title", ""))}</span>'
            f'<span class="muted small">asked {E(s.get("asked", ""))}</span>{sess}</div>'
            f'<p>{E(s.get("result", ""))}</p><p class="muted"><b>Next:</b> {E(s.get("next", ""))}</p>'
            f'<p class="links">{link_html}</p></li>')


sq_cards = "".join(sq_card(s) for s in sidequests_sorted) or '<li class="muted">nothing this pass</li>'
sq_waiting = [s for s in sidequests if s.get("state") == "waiting on you"]
desk_sq_waiting = "".join(f'<li>{E(s.get("title", ""))} <span class="muted small">&mdash; {E(short(s.get("next", ""), 100))}</span></li>' for s in sq_waiting)

# ---------------------------------------------------------------- page

CSS = """
:root{
  --ground:#F6F5F1; --surface:#FFFFFF; --ink:#1F2328; --muted:#6A7178; --line:#DCDFE3; --accent:#2E6F6A; --accent-soft:#E3EFEE;
  --good:#2F7D4F; --good-soft:#E4F1E8; --warn:#B4741A; --warn-soft:#F7ECD9; --focus:#2E6F6A;
}
@media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){
  --ground:#15181C; --surface:#1C2127; --ink:#E6E8EB; --muted:#98A0A8; --line:#2C333B; --accent:#5FB3AB; --accent-soft:#1F3634;
  --good:#6ABF85; --good-soft:#1E3327; --warn:#D9A24A; --warn-soft:#3A2E17; --focus:#5FB3AB; color-scheme:dark; } }
:root[data-theme="dark"]{
  --ground:#15181C; --surface:#1C2127; --ink:#E6E8EB; --muted:#98A0A8; --line:#2C333B; --accent:#5FB3AB; --accent-soft:#1F3634;
  --good:#6ABF85; --good-soft:#1E3327; --warn:#D9A24A; --warn-soft:#3A2E17; --focus:#5FB3AB; color-scheme:dark; }
*{box-sizing:border-box}
body{background:var(--ground);color:var(--ink);font-family:"Public Sans","Segoe UI",system-ui,sans-serif;font-size:16px;line-height:1.5;padding-block:20px 60px;padding-inline:clamp(16px,4vw,40px)}
.wrap{max-width:960px;margin-inline:auto;min-width:0}
h1,h2,h3,h4{font-family:"Literata",Georgia,serif;font-weight:500;text-wrap:balance;margin:0}
h1{font-size:1.9rem;line-height:1.15} h2{font-size:1.35rem;margin-bottom:10px} h3{font-size:1.05rem;margin:22px 0 8px} h4{font-size:0.95rem;margin-bottom:4px}
h5{font-size:0.9rem;margin:10px 0 2px;font-family:inherit;font-weight:600}
p{margin:0 0 8px} a{color:var(--accent);text-underline-offset:2px}
.mono{font-family:"JetBrains Mono",ui-monospace,Menlo,monospace;font-size:0.85em} .muted{color:var(--muted)} .small{font-size:0.85rem}
.num{font-variant-numeric:tabular-nums}
header{display:grid;gap:8px;margin-bottom:14px}
.headline{font-size:1.02rem;max-width:68ch}
.strip{display:flex;flex-wrap:wrap;gap:8px 18px;font-size:0.85rem;color:var(--muted);align-items:baseline}
.strip b{color:var(--ink);font-weight:600}
nav.tabs{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--ground);display:flex;gap:4px;border-bottom:1px solid var(--line);margin:8px 0 18px;padding-top:6px}
nav.tabs button{appearance:none;background:none;border:0;border-bottom:2px solid transparent;color:var(--muted);font:inherit;font-weight:600;padding:8px 12px;cursor:pointer;margin-bottom:-1px}
nav.tabs button[aria-selected="true"]{color:var(--ink);border-bottom-color:var(--accent)}
nav.tabs button:focus-visible,.rhead:focus-visible,.copy:focus-visible,.lg:focus-visible{outline:2px solid var(--focus);outline-offset:2px}
section[hidden]{display:none}
.legend{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0 14px}
.lg{appearance:none;font:inherit;font-size:0.82rem;display:inline-flex;gap:6px;align-items:center;background:var(--surface);border:1px solid var(--line);border-radius:4px;padding:4px 8px;color:var(--ink);cursor:pointer}
.lg[aria-pressed="true"]{border-color:var(--accent);background:var(--accent-soft)}
.lg .num{color:var(--muted)}
.ncls{font-family:"JetBrains Mono",ui-monospace,monospace;font-weight:600;font-size:0.8rem;padding:1px 6px;border-radius:3px;background:var(--line);color:var(--ink)}
.ncls.n4,.ncls.n5{background:var(--good-soft);color:var(--good)} .ncls.n3{background:var(--accent-soft);color:var(--accent)}
.readings{list-style:none;margin:0;padding:0;border-top:1px solid var(--line)}
.rrow{border-bottom:1px solid var(--line)}
.rrow.unique .rtitle{font-weight:600}
.rhead{appearance:none;width:100%;background:none;border:0;color:inherit;font:inherit;text-align:left;display:grid;grid-template-columns:44px minmax(0,1fr);gap:6px 12px;align-items:start;padding:12px 4px;cursor:pointer}
.rhead:hover{background:var(--surface)}
.rtitle{text-wrap:pretty} .rchips{grid-column:2;display:flex;flex-wrap:wrap;gap:6px}
.chip{display:inline-block;font-size:0.74rem;font-weight:600;padding:2px 7px;border-radius:3px;background:var(--line);color:var(--ink);letter-spacing:0.01em}
.chip.r-sub{background:var(--good-soft);color:var(--good)} .chip.r-conf{background:var(--accent-soft);color:var(--accent)} .chip.r-form,.chip.c-aud{background:transparent;border:1px solid var(--line);color:var(--muted)} .chip.qa-flag{background:transparent;border:1px solid var(--warn,#b45309);color:var(--warn,#b45309)}
.chip.k-ours{background:var(--good);color:#fff} .chip.k-period{background:var(--accent-soft);color:var(--accent)} .chip.k-pub{background:transparent;border:1px solid var(--line);color:var(--muted)} .chip.k-known{background:transparent;border:1px dashed var(--line);color:var(--muted)}
.chip.so-queued{color:var(--muted);border:1px dashed var(--line);background:transparent} .chip.so-posted{background:var(--warn-soft);color:var(--warn)} .chip.so-checked{background:var(--good-soft);color:var(--good)}
.chip.out-ready{background:var(--good);color:#fff} .chip.out-sent{background:var(--accent-soft);color:var(--accent)} .task.sentrow{grid-template-columns:12px minmax(0,1fr);opacity:0.85} .chip.out-drafted{background:var(--warn-soft);color:var(--warn)} .chip.k{background:var(--accent-soft);color:var(--accent)}
.rbody{padding:4px 4px 18px 56px;display:grid;gap:14px;font-size:0.95rem}
@media (max-width:600px){.rbody{padding-left:4px}}
.dz p{max-width:70ch} .memo p{max-width:70ch} .rating{font-weight:600} .rating.r-sub{color:var(--good)} .rating.r-conf{color:var(--accent)} .rating.r-form{color:var(--muted)}
.links a{margin-right:12px}
.sentbox{display:inline-flex;gap:8px;align-items:center;margin-top:10px;font-weight:600;cursor:pointer} .sentbox input{width:18px;height:18px;accent-color:var(--good)} .sentbox.done{color:var(--good)}
.cfs{display:grid;gap:10px;margin-top:8px}
.cf{background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:8px 10px}
.cf-head{display:flex;justify-content:space-between;align-items:center;gap:10px;margin-bottom:4px}
.cf-label{font-size:0.74rem;font-weight:600;text-transform:uppercase;letter-spacing:0.06em;color:var(--muted)}
.val{font-family:inherit;font-size:0.95rem;overflow-wrap:anywhere;user-select:all}
.cf .mail{margin:0;border:0;padding:6px 0 0;background:transparent}
.mail{white-space:pre-wrap;overflow-wrap:anywhere;font-family:inherit;font-size:0.9rem;background:var(--surface);border:1px solid var(--line);border-radius:4px;padding:12px 14px;margin:8px 0;max-height:420px;overflow:auto}
.copy{appearance:none;font:inherit;font-size:0.8rem;font-weight:600;background:var(--accent);color:#fff;border:0;border-radius:4px;padding:5px 10px;cursor:pointer;flex:none}
.others{list-style:none;margin:0;padding:0;display:grid;gap:6px;font-size:0.92rem}
.tasks{list-style:none;margin:0;padding:0;display:grid;gap:10px}
.task{display:grid;grid-template-columns:24px minmax(0,1fr);gap:12px;align-items:start;background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:12px 14px}
.task.waiting{border-style:dashed} .task.done{opacity:0.55} .task.done .tsubj{text-decoration:line-through}
.task input{width:20px;height:20px;margin-top:3px;accent-color:var(--good);cursor:pointer}
.tsubj{font-weight:600} .tto{font-size:0.9rem} .tmeta{font-size:0.82rem;color:var(--muted);margin-top:2px} .warn{color:var(--warn)}
.asks{list-style:none;margin:8px 0 0;padding:0;display:grid;gap:4px;font-size:0.88rem}
.lanes{list-style:none;margin:0;padding:0;display:grid;gap:8px}
.lanes li{background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:10px 12px} .lname{font-weight:600;display:flex;justify-content:space-between;gap:10px} .lfocus{font-size:0.9rem;margin-top:2px}
.funnel{display:grid;gap:4px;margin-top:8px}
.frow{display:grid;grid-template-columns:220px minmax(0,1fr) 36px;gap:10px;align-items:center;font-size:0.9rem}
@media (max-width:600px){.frow{grid-template-columns:150px minmax(0,1fr) 30px}}
.fbar{height:10px;background:var(--line);border-radius:3px;overflow:hidden} .ffill{height:100%;background:var(--accent)}
.tablewrap{overflow-x:auto;margin-top:8px} table{border-collapse:collapse;width:100%;font-size:0.9rem;min-width:640px}
th,td{text-align:left;vertical-align:top;padding:8px 8px;border-bottom:1px solid var(--line)} th{font-size:0.78rem;text-transform:uppercase;letter-spacing:0.05em;color:var(--muted)}
.workers,.log{list-style:none;margin:0;padding:0;display:grid;gap:6px;font-size:0.92rem}
.workers li{display:grid;grid-template-columns:10px minmax(0,1fr) auto;gap:10px;align-items:baseline}
.dot{width:8px;height:8px;border-radius:50%;display:inline-block} .dot.on{background:var(--good)} .dot.off{background:var(--line)}
.log li{display:grid;grid-template-columns:96px minmax(0,1fr);gap:10px} .when{white-space:nowrap}
.note{font-size:0.85rem;color:var(--muted);margin-top:10px}
.fcards{list-style:none;margin:10px 0 0;padding:0;display:grid;gap:10px}
.fcard{background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:12px 14px}
.fmeta{display:flex;justify-content:space-between;gap:10px;align-items:baseline;flex-wrap:wrap}
.fwho{font-weight:600}
.fwhere{margin-top:4px}
.fquote{margin:8px 0;padding-left:10px;border-left:3px solid var(--accent);font-style:italic;max-width:70ch}
.pending{list-style:none;margin:8px 0 0;padding:0;display:grid;gap:4px;font-size:0.88rem}
.sqcards{list-style:none;margin:10px 0 0;padding:0;display:grid;gap:10px}
.sqcard{background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:12px 14px}
.sqhead{display:flex;flex-wrap:wrap;gap:8px;align-items:baseline}
.sqtitle{font-weight:600}
.chip.sq-running{background:var(--accent-soft);color:var(--accent)} .chip.sq-done{background:var(--good-soft);color:var(--good)}
.chip.sq-waiting-on-you{background:var(--warn-soft);color:var(--warn)} .chip.sq-blocked{background:var(--warn-soft);color:var(--warn)}
.chip.sq-queued{background:transparent;border:1px dashed var(--line);color:var(--muted)}
.sqdesk{list-style:none;margin:8px 0 0;padding:0;display:grid;gap:4px;font-size:0.9rem}
@media (prefers-reduced-motion:no-preference){.ffill{transition:width .3s}}
"""

JS = """
(function () {
  var tabs = Array.prototype.slice.call(document.querySelectorAll('nav.tabs button'));
  var secs = Array.prototype.slice.call(document.querySelectorAll('section.view'));
  function show(id) {
    tabs.forEach(function (b) { b.setAttribute('aria-selected', b.dataset.view === id ? 'true' : 'false'); });
    secs.forEach(function (s) { s.hidden = s.id !== id; });
    try { localStorage.setItem('view', id); } catch (e) {}
  }
  tabs.forEach(function (b) { b.addEventListener('click', function () { show(b.dataset.view); history.replaceState(null, '', '#' + b.dataset.view); }); });
  var start = 'readings';
  try { var h = (location.hash || '').replace('#', ''); if (h && document.getElementById(h)) start = h; else { var v = localStorage.getItem('view'); if (v && document.getElementById(v)) start = v; } } catch (e) {}
  show(start);
  Array.prototype.forEach.call(document.querySelectorAll('.rhead'), function (b) {
    b.addEventListener('click', function () {
      var open = b.getAttribute('aria-expanded') === 'true';
      b.setAttribute('aria-expanded', open ? 'false' : 'true');
      document.getElementById(b.getAttribute('aria-controls')).hidden = open;
    });
  });
  var active = null;
  Array.prototype.forEach.call(document.querySelectorAll('.lg'), function (b) {
    b.addEventListener('click', function () {
      var n = b.dataset.n; active = (active === n) ? null : n;
      Array.prototype.forEach.call(document.querySelectorAll('.lg'), function (x) { x.setAttribute('aria-pressed', x.dataset.n === active ? 'true' : 'false'); });
      Array.prototype.forEach.call(document.querySelectorAll('.rrow'), function (r) { r.hidden = active !== null && r.dataset.n !== active; });
    });
  });
  Array.prototype.forEach.call(document.querySelectorAll('.copy'), function (b) {
    b.addEventListener('click', function () {
      var t = document.getElementById(b.dataset.for); if (!t) return;
      var done = function () { var o = b.textContent; b.textContent = 'Copied'; setTimeout(function () { b.textContent = o; }, 1500); };
      if (navigator.clipboard && navigator.clipboard.writeText) { navigator.clipboard.writeText(t.value).then(done, function () { t.hidden = false; t.select(); }); }
      else { t.hidden = false; t.select(); }
    });
  });
  var status = document.getElementById('tick-status');
  var items = Array.prototype.slice.call(document.querySelectorAll('[data-row]'));
  function paint(row, done, when) {
    Array.prototype.forEach.call(document.querySelectorAll('[data-row]'), function (el) {
      if (el.dataset.row !== row) return;
      var inp = el.querySelector('input'); if (inp) inp.checked = !!done; el.classList.toggle('done', !!done);
      var meta = el.querySelector('.ask-meta');
      if (done && when && meta && meta.textContent.indexOf('ticked') < 0) meta.textContent += ' · ticked ' + when;
      if (el.classList.contains('sentbox')) el.lastChild.textContent = done ? (' Sent' + (when ? ' ' + when : '')) : ' Mark as sent';
    });
  }
  function local(row, v) { try { if (v === undefined) return JSON.parse(localStorage.getItem('ask-' + row) || 'null'); localStorage.setItem('ask-' + row, JSON.stringify(v)); } catch (e) { return null; } }
  items.forEach(function (li) { var r = li.dataset.row; var v = local(r); if (v) paint(r, v.done, v.when); });
  var db = null;
  items.forEach(function (li) {
    var inp = li.querySelector('input'); if (!inp || inp.disabled) return;
    inp.addEventListener('change', function (ev) {
      var r = li.dataset.row; var done = ev.target.checked; var when = new Date().toISOString().slice(0, 10);
      var v = { row: r, done: done, when: done ? when : '' };
      paint(r, done, v.when); local(r, v);
      if (db) db.doc('emails/' + r).set(v).catch(function () { if (status) status.textContent = 'Ticks are saved on this device only.'; });
    });
  });
  if (!window.claude || !window.claude.use) { if (status) status.textContent = 'Ticks are saved on this device only.'; return; }
  window.claude.use('db').then(function (ns) {
    if (!ns) { if (status) status.textContent = 'Ticks are saved on this device only.'; return; }
    db = ns;
    db.collection('emails').onSnapshot(function (snap) {
      snap.docs.forEach(function (doc) { if (!doc.exists) return; var v = doc.data(); paint(v.row, v.done, v.when); local(v.row, v); });
      if (status) status.textContent = 'Ticks are saved on this page; the orchestrator reads them.';
    }, function () { if (status) status.textContent = 'Ticks are saved on this device only.'; });
  });
})();
"""

page = f'''<title>Cipher Lab Board</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Literata:opsz,wght@7..72,400;7..72,500&family=Public+Sans:wght@400;600&family=JetBrains+Mono:wght@400;600&display=swap">
<style>{CSS}</style>
<div class="wrap">
<header>
  <h1>Cipher Lab Board</h1>
  <p class="headline">{E(headline)}</p>
  <div class="strip"><span>Updated <b>{E(d["updated"])}</b></span><span><b>{n_unique}</b> readings at N3 or better after two audits</span><span><b>{n_first}</b> with our own key and no earlier decipherment found</span><span><b>{len(lanes)}</b> lanes, <b>{live_workers}</b> workers live</span><span><b>{len(ready)}</b> to send</span><span><b>{jq}</b> JSTOR rows queued</span></div>
</header>
<nav class="tabs" aria-label="Views">
  <button type="button" data-view="readings" aria-selected="true">Readings</button>
  <button type="button" data-view="desk" aria-selected="false">Your desk</button>
  <button type="button" data-view="machine" aria-selected="false">The machine</button>
  <button type="button" data-view="fame" aria-selected="false">Hall of fame</button>
  <button type="button" data-view="sidequests" aria-selected="false">Side quests</button>
</nav>

<section class="view" id="readings">
  <h2>Readings, by how far the verifier could take them</h2>
  <p class="muted small" style="max-width:70ch">One row per reading a separate verifier has classed. N4 means the principal editions, catalogues and project pages were searched and no prior decipherment was located; it is not a claim that the letter was never read. Open a row for the passage, the rating, who to tell and the text to send.</p>
  <p class="muted small" style="max-width:70ch">Whose key: <span class="chip k-ours">our key</span> we recovered it ourselves; <span class="chip k-period">period key, rebuilt by us</span> from a decipherment, key sheet or cipher book of the time; <span class="chip k-pub">published key</span> someone else's, which we applied. A reading with our key at N3 or better is the nearest honest thing to a first: no earlier decipherment was found, and the key is our own work.</p>
  <div class="legend">{legend}</div>
  <ul class="readings">{reading_rows}</ul>
  <h3>Also this week</h3>
  <ul class="others">{other_rows}</ul>
</section>

<section class="view" id="desk" hidden>
  <h2>Your desk</h2>
  <p class="muted small">Only what a cloud session cannot do: send, post, pay, decide. Tick when done; the tick is the record.</p>
  <h3>Send now</h3>
  <ul class="tasks">{desk_ready}</ul>
  {('<h3>Waiting on one more step</h3><ul class="tasks">' + desk_waiting + '</ul>') if desk_waiting else ''}
  {('<h3>Sent, awaiting reply</h3><ul class="tasks">' + desk_sent + '</ul>') if desk_sent else ''}
  {('<details><summary><b>' + str(len(you_targets)) + ' copy orders parked until funding</b> <span class="muted small">(each a decision and a payment; open to see them)</span></summary><ul class="tasks" style="margin-top:10px">' + desk_targets + '</ul></details>') if desk_targets else ''}
  {('<h3>Side quests waiting on you</h3><ul class="sqdesk">' + desk_sq_waiting + '</ul>') if desk_sq_waiting else ''}
  <p class="note" id="tick-status"></p>
  <p class="note"><b>{jq}</b> JSTOR rows queued for the runner on your machine{(", " + str(jdone) + " answered") if jdone else ""} (<a href="{REPO}tools/jstor_runner_brief.md">runner brief</a>).</p>
  {('<details><summary>Other open asks, no rush (' + str(len(asks)) + ')</summary><ul class="asks">' + asks_rows + '</ul></details>') if asks else ''}
</section>

<section class="view" id="machine" hidden>
  <h2>The machine</h2>
  <h3>Lanes</h3>
  <ul class="lanes">{lane_rows or '<li class="muted">no lane running</li>'}</ul>
  <h3>Pipeline, targets per stage</h3>
  <div class="funnel">{funnel}</div>
  <h3>Targets</h3>
  <div class="tablewrap"><table><thead><tr><th>Target</th><th>Stage</th><th></th><th>Holder</th><th>Next</th></tr></thead><tbody>{target_rows}</tbody></table></div>
  <h3>Parent workers</h3>
  <ul class="workers">{worker_rows}</ul>
  <h3>Log</h3>
  <ul class="log">{log_rows}</ul>
</section>

<section class="view" id="fame" hidden>
  <h2>Hall of fame</h2>
  <p class="muted small" style="max-width:70ch">Public citations of this project's work by someone outside the repository: a credit, a link, a correction adopted, co-authorship or a reply that became public. CITATIONS.md is the record; the owner is never named (rule 9), the repository is.</p>
  <p class="strip"><b>{len(citations)}</b> public citations since 23 Sept 2026</p>
  <ul class="fcards">{fame_cards}</ul>
  {('<h3>Pending</h3><p class="muted small">Sent, awaiting a reply that has not gone public.</p><ul class="pending">' + pending_rows + '</ul>') if pending_rows else ''}
</section>

<section class="view" id="sidequests" hidden>
  <h2>Side quests</h2>
  <p class="muted small" style="max-width:70ch">Owner-added items from tonight's run that don't fit the readings, desk or machine views: one card each, ordered waiting on you first, then running, blocked, queued, done.</p>
  <p class="strip"><b>{sq_count_line}</b></p>
  <ul class="sqcards">{sq_cards}</ul>
</section>
</div>
<script>{JS}</script>
'''
open("dashboard.html", "w", encoding="utf-8").write(page)
os.makedirs("docs", exist_ok=True)
open("docs/index.html", "w", encoding="utf-8").write(page)
print(f"dashboard.html and docs/index.html written: {len(page)} bytes, {len(targets_all)} targets, {len(workers_all)} workers, {len(results)} results, {n_unique} unique")
