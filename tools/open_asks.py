#!/usr/bin/env python3
"""open_asks.py -- list the ROOM.md lines addressed to a role that the role has not yet answered.

The owner's direction (27 Sept 2026): no parent parks waiting on the other account. Every check-in of either
parent starts with `python3 tools/open_asks.py --me <role>` and answers each line it prints, with a decision, in
that same check-in (parent.md "No parking"). An ask is "open" until a later ROOM.md line by the addressed role
exists; any later line by that role counts, so a parent that answers in its check-in line clears its list.

Usage:
  python3 tools/open_asks.py --me "owner-account parent"      # what SUPPLY owes
  python3 tools/open_asks.py --me "parent 7k"                 # what SOLVE's current parent owes
  python3 tools/open_asks.py --me "LANE NEV" --hours 12
Exit 0 always; the list is for reading, not gating. `--hours` bounds the look-back (default 24).
"""
import argparse
import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from orphan_check import ROLE_RE, actor_matches_role, parse_room_lines, role_key  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def me_key(me):
    low = me.strip().lower()
    if low in ("owner-account parent", "the owner-account parent", "supply"):
        return ("parent", "owner")
    return role_key(me if low.startswith(("parent", "lane", "the ")) else "parent " + me)


def matches_me(ask_key, my_key):
    """An ask 'for the parent' reaches both parents; 'for parent 7k' reaches only that tag."""
    if ask_key[0] != my_key[0]:
        return False
    if ask_key[1] is None or my_key[1] is None:
        return True
    return ask_key[1] == my_key[1]


def open_asks(room_lines, me, now, hours):
    my_key = me_key(me)
    since = now - datetime.timedelta(hours=hours)
    out = []
    for i, l in enumerate(room_lines):
        if l["ts_dt"] is None or l["ts_dt"] < since:
            continue
        if actor_matches_role(l["actor"], my_key):
            continue  # my own lines are not asks of me
        sig = l["signal"]
        low = sig.lower().strip()
        if low.startswith("claim:") or (low.startswith("done:") and "for " not in low[:60]):
            continue
        for m in ROLE_RE.finditer(sig):
            ask_key = role_key(m.group(1))
            tail = sig[m.end():m.end() + 20].lower()
            if ask_key == ("parent", None) and tail.startswith(" (owner account)"):
                ask_key = ("parent", "owner")
            if not matches_me(ask_key, my_key):
                continue
            answered = any(
                later["ts_dt"] is not None and later["ts_dt"] > l["ts_dt"]
                and actor_matches_role(later["actor"], my_key)
                for later in room_lines[i + 1:]
            )
            if answered:
                break
            age_h = (now - l["ts_dt"]).total_seconds() / 3600
            out.append((age_h, l["ts"], l["actor"], sig[:160]))
            break
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--me", required=True, help='the role you are: "owner-account parent", "parent 7k", "LANE NEV"')
    ap.add_argument("--room-file", default=os.path.join(ROOT, "ROOM.md"))
    ap.add_argument("--hours", type=float, default=24.0)
    ap.add_argument("--now", help="override 'now', e.g. '2026-09-27 07:00' (UTC)")
    args = ap.parse_args()
    now = (datetime.datetime.strptime(args.now, "%Y-%m-%d %H:%M") if args.now
           else datetime.datetime.utcnow().replace(second=0, microsecond=0))
    rows = open_asks(parse_room_lines(args.room_file), args.me, now, args.hours)
    if not rows:
        print(f"open_asks: nothing open for {args.me!r} in the last {args.hours:g}h")
        return
    print(f"open_asks: {len(rows)} line(s) addressed to {args.me!r} without a later line from you -- answer each with a decision in this check-in:")
    for age_h, ts, actor, sig in rows:
        flag = "  OVER 1h" if age_h > 1 else ""
        print(f"  {ts} | {actor} | {age_h:.1f}h ago{flag} | {sig}")


if __name__ == "__main__":
    main()
