# PREREG addendum LVN-L05W (15 Oct 2026, 15:4x UTC by date -u, account 4, LANE DEFAULT-A4-1441-15) -- written before any blind read

Same PREREG as LVN-L05 (`lvnl05/PREREG-LVN-L05.md`, 7e90dde79): same six targets, same six H controls, same X/Y order (h, t25, t141 target=X;
t80, t35, tfut target=Y), same gate (>= 5/6 controls exactly as committed), same rulings and apply path. One change only, the one LVN-L05 named:
crops re-cut wider (`lvnl05/cut_w.py`, scratch only) so each holds the token plus a neighbour each side (word crops with their neighbours).
Because a crop now holds several tokens, the reader reads every token left to right and the scored token is fixed by position here
(index in the reader's list, 1-based; a token the reader marks as clipped at the left edge is dropped before counting):
h_head tokens 1-2; h_ctl 2 (28); t80 2; t80_ctl 2 (8); t25 2; t25_ctl 2 (82); t35 2; t35_ctl 2 (31); t141 1; t141_ctl 2 (21); tfut 2; tfut_ctl 2 (tout).
If the gate fails again: log it, apply nothing, do not re-cut a third time (lane brief). Stop at 80% of cap 2 or of box (16:15 UTC).
