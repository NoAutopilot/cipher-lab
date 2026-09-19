#!/usr/bin/env python3
"""Render status.json into dashboard.html, the one-page project board.

Usage: python3 tools/build_dashboard.py   (from the repo root)
Then publish dashboard.html. The board and STATUS.md must say the same thing; status.json is the source.
"""
import html
import json

d = json.load(open("status.json", encoding="utf-8"))
E = html.escape
stages = d["stages"]
N = len(stages)

def chip(state):
    label = {"waiting": "Waiting on archive", "active": "Worker on it", "queued": "Queued", "blocked": "Blocked", "you": "Needs you", "solved": "Solved"}[state]
    return f'<span class="chip chip-{state}">{label}</span>'

def target_row(t):
    segs = "".join(
        f'<span class="seg {"on" if i < t["stage"] else ""} {"cur" if i == t["stage"] - 1 else ""}" title="{E(s)}"></span>'
        for i, s in enumerate(stages)
    )
    folder = f'<a class="mono" href="https://github.com/NoAutopilot/cipher-lab/tree/main/{E(t["folder"])}">{E(t["folder"])}</a>' if t["folder"] else '<span class="mono muted">no folder yet</span>'
    return f'''
    <article class="target state-{t["state"]}">
      <div class="t-head">
        <h3>{E(t["name"])} <span class="year">{E(t["year"])}</span></h3>
        {chip(t["state"])}
      </div>
      <div class="t-ref mono">{E(t["ref"])}</div>
      <div class="pipe" role="img" aria-label="Stage {t["stage"]} of {N}: {E(stages[t["stage"]-1])}">
        <div class="segs">{segs}</div>
        <div class="stage-label"><b>Stage {t["stage"]} of {N}</b> {E(stages[t["stage"]-1])} <span class="muted">· held by {E(t["holder"])}</span></div>
      </div>
      <p class="next"><b>Next:</b> {E(t["next"])}</p>
      <p class="note muted">{E(t["note"])} {folder}</p>
    </article>'''

targets = "".join(target_row(t) for t in d["targets"])
n_active = sum(1 for t in d["targets"] if t["state"] in ("waiting", "active"))
n_requests = sum(1 for t in d["targets"] if t["stage"] == 5)
n_you = sum(1 for t in d["targets"] if t["state"] == "you")
n_solved = sum(1 for t in d["targets"] if t["state"] == "solved")

workers = "".join(
    f'<li class="w-{w["state"]}"><span class="dot"></span><div><div class="w-title">{E(w["title"])}</div><div class="muted">{E(w["job"])}</div></div><span class="w-state">{E(w["state"])}</span></li>'
    for w in d["workers"]
)
queue = "".join(
    f'<tr><td class="num">{q["rank"]}</td><td>{E(q["name"])}</td><td class="num">{E(q["year"])}</td><td class="num"><b>{q["total"]}</b><span class="muted">/39</span></td><td>{E(q["next"])}</td></tr>'
    for q in d["queue"]
)
log = "".join(f'<li><span class="mono muted when">{E(l["when"])}</span><span>{E(l["what"])}</span></li>' for l in d["log"])
stage_key = "".join(f'<li><span class="k-num">{i+1}</span>{E(s)}</li>' for i, s in enumerate(stages))

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
.wrap {{ max-width:1080px; margin-inline:auto; display:grid; gap:28px; }}
h1,h2,h3 {{ font-family:"Newsreader", Georgia, serif; font-weight:600; margin:0; text-wrap:balance; }}
h1 {{ font-size:2rem; }} h2 {{ font-size:1.35rem; margin-bottom:12px; }} h3 {{ font-size:1.2rem; }}
.mono {{ font-family:"JetBrains Mono", ui-monospace, Menlo, monospace; font-size:0.85em; }}
.muted {{ color:var(--muted); }}
a {{ color:var(--accent); text-decoration:none; }} a:hover, a:focus-visible {{ text-decoration:underline; outline:none; }}
header {{ display:flex; flex-wrap:wrap; align-items:baseline; justify-content:space-between; gap:8px 24px; border-bottom:1px solid var(--line); padding-bottom:12px; }}
header .upd {{ color:var(--muted); }}
.tiles {{ display:grid; grid-template-columns:repeat(auto-fit, minmax(150px, 1fr)); gap:12px; }}
.tile {{ background:var(--surface); border:1px solid var(--line); border-radius:6px; padding:14px 16px; }}
.tile .n {{ font-family:"Newsreader", Georgia, serif; font-size:2.2rem; line-height:1; font-variant-numeric:tabular-nums; }}
.tile .l {{ color:var(--muted); font-size:0.85rem; text-transform:uppercase; letter-spacing:0.06em; margin-top:6px; }}
.targets {{ display:grid; gap:14px; }}
.target {{ background:var(--surface); border:1px solid var(--line); border-left:4px solid var(--idle); border-radius:6px; padding:16px 18px; display:grid; gap:8px; }}
.target.state-waiting {{ border-left-color:var(--warn); }} .target.state-active {{ border-left-color:var(--info); }} .target.state-blocked {{ border-left-color:var(--bad); }} .target.state-solved {{ border-left-color:var(--good); }} .target.state-you {{ border-left-color:var(--accent); }}
.t-head {{ display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:8px; }}
.year {{ color:var(--muted); font-weight:500; font-size:0.9em; margin-left:6px; }}
.chip {{ font-size:0.78rem; font-weight:600; text-transform:uppercase; letter-spacing:0.05em; padding:3px 9px; border-radius:999px; white-space:nowrap; }}
.chip-waiting {{ background:var(--warn-soft); color:var(--warn); }} .chip-active {{ background:var(--info-soft); color:var(--info); }} .chip-queued {{ background:var(--idle-soft); color:var(--idle); }} .chip-blocked {{ background:var(--bad-soft); color:var(--bad); }} .chip-you {{ background:var(--accent-soft); color:var(--accent); }} .chip-solved {{ background:var(--good-soft); color:var(--good); }}
.segs {{ display:grid; grid-template-columns:repeat({N}, 1fr); gap:3px; margin-top:4px; }}
.seg {{ height:10px; border-radius:2px; background:var(--idle-soft); }}
.seg.on {{ background:var(--accent); }} .seg.cur {{ outline:2px solid var(--accent); outline-offset:1px; }}
.state-waiting .seg.on {{ background:var(--warn); }} .state-waiting .seg.cur {{ outline-color:var(--warn); }}
.state-blocked .seg.on {{ background:var(--bad); }} .state-blocked .seg.cur {{ outline-color:var(--bad); }}
.state-solved .seg.on {{ background:var(--good); }}
.stage-label {{ font-size:0.9rem; margin-top:6px; }}
.next {{ margin:0; }} .note {{ margin:0; font-size:0.92rem; }}
.two {{ display:grid; grid-template-columns:1fr 1fr; gap:24px; }} @media (max-width:760px) {{ .two {{ grid-template-columns:1fr; }} }}
.panel {{ background:var(--surface); border:1px solid var(--line); border-radius:6px; padding:16px 18px; }}
.workers, .log, .key {{ list-style:none; margin:0; padding:0; display:grid; gap:10px; }}
.workers li {{ display:grid; grid-template-columns:10px 1fr auto; gap:10px; align-items:start; }}
.dot {{ width:10px; height:10px; border-radius:50%; margin-top:6px; background:var(--idle); }} .w-running .dot {{ background:var(--info); }} .w-done .dot {{ background:var(--good); }}
.w-title {{ font-weight:600; }} .w-state {{ font-size:0.78rem; text-transform:uppercase; letter-spacing:0.05em; color:var(--muted); }}
.log li {{ display:grid; grid-template-columns:110px 1fr; gap:10px; }} .when {{ white-space:nowrap; }}
.tablewrap {{ overflow-x:auto; }} table {{ border-collapse:collapse; width:100%; font-size:0.95rem; }}
th, td {{ text-align:left; padding:7px 10px; border-bottom:1px solid var(--line); vertical-align:top; }} th {{ color:var(--muted); font-size:0.78rem; text-transform:uppercase; letter-spacing:0.05em; font-weight:600; }}
.num {{ font-variant-numeric:tabular-nums; white-space:nowrap; }}
.key {{ grid-template-columns:repeat(auto-fit, minmax(190px, 1fr)); gap:6px 14px; font-size:0.9rem; }} .k-num {{ display:inline-block; width:1.6em; color:var(--muted); font-variant-numeric:tabular-nums; }}
.how {{ font-size:0.95rem; }}
@media (prefers-reduced-motion: no-preference) {{ .seg {{ transition:background .2s; }} }}
</style>
<div class="wrap">
  <header>
    <div><h1>Cipher Lab Board</h1><div class="muted">Where every target stands, who holds it, and what happens next.</div></div>
    <div class="upd">Updated {E(d["updated"])}</div>
  </header>

  <section class="tiles" aria-label="Summary">
    <div class="tile"><div class="n">{n_active}</div><div class="l">Targets in motion</div></div>
    <div class="tile"><div class="n">{n_requests}</div><div class="l">Archive requests out</div></div>
    <div class="tile"><div class="n">{n_you}</div><div class="l">Waiting on you</div></div>
    <div class="tile"><div class="n">{n_solved}</div><div class="l">Solved</div></div>
  </section>

  <section>
    <h2>Targets</h2>
    <div class="targets">{targets}</div>
  </section>

  <section class="panel">
    <h2>The nine stages</h2>
    <ul class="key">{stage_key}</ul>
    <p class="how muted">A target is <b>solved</b> only when one fixed key reads every group, unchanged, into coherent text that checks against the world: a name in cipher that also stands in clear, or a printed account of the same events. Anything less is reported as partial.</p>
  </section>

  <div class="two">
    <section class="panel">
      <h2>Workers</h2>
      <ul class="workers">{workers}</ul>
      <p class="how muted">Workers are sessions the orchestrator starts for one job each. They push to the repo, report, and stop. You never need to open them.</p>
    </section>
    <section class="panel">
      <h2>Change log</h2>
      <ul class="log">{log}</ul>
    </section>
  </div>

  <section class="panel">
    <h2>Queue, top of the ranking</h2>
    <div class="tablewrap"><table>
      <thead><tr><th>Rank</th><th>Target</th><th>Year</th><th>Score</th><th>Next step</th></tr></thead>
      <tbody>{queue}</tbody>
    </table></div>
    <p class="how muted">Score out of 39: language fit, material online, key lead, size, competition, historical weight. Full list with rationale in <a href="https://github.com/NoAutopilot/cipher-lab/blob/main/QUEUE.md">QUEUE.md</a>.</p>
  </section>
</div>
'''
open("dashboard.html", "w", encoding="utf-8").write(page)
print(f"dashboard.html written: {len(page)} bytes, {len(d['targets'])} targets, {len(d['workers'])} workers")
