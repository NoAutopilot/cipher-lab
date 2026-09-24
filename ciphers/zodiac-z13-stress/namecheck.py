"""Name matcher shared by enumerate.py and control.py: tries over names_given.txt and names_surname.txt.

A 'name7' hit: a given name of >= 4 letters followed at once by >= 1 letters that begin a listed surname, total >= 7
letters (ARTHUR+LA counts: LA begins LANE, LARSON, LAWSON); or a given name of >= 7 letters alone.
A 'name6' hit: a given name of >= 6 letters anywhere (the brief's control criterion).
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(f):
    return [l.strip() for l in open(os.path.join(HERE, f)) if l.strip() and not l.startswith("#")]


GIVEN = [g for g in _load("names_given.txt") if len(g) >= 4]
SURN = _load("names_surname.txt")


def trie(words):
    nodes = [{}]
    term = [None]
    for w in words:
        n = 0
        for c in w:
            if c not in nodes[n]:
                nodes[n][c] = len(nodes)
                nodes.append({})
                term.append(None)
            n = nodes[n][c]
        term[n] = w
    return nodes, term


GN, GT = trie(GIVEN)
SN, _ = trie(SURN)
DEPTH_S = {}


def feed(active, c, mode):
    """Advance a frozenset of partial matches by one letter. Returns (new_active, labels_hit)."""
    new, hits = set(), set()
    for a in list(active) + [("g", 0, "")]:
        if a[0] == "g":
            nx = GN[a[1]].get(c)
            if nx is None:
                continue
            w = a[2] + c
            new.add(("g", nx, w))
            if GT[nx]:
                g = GT[nx]
                if mode == "name6" and len(g) >= 6:
                    hits.add(g)
                if mode == "name7":
                    if len(g) >= 7:
                        hits.add(g)
                    new.add(("s", 0, g, ""))
        else:
            nx = SN[a[1]].get(c)
            if nx is None:
                continue
            frag = a[3] + c
            new.add(("s", nx, a[2], frag))
            if len(a[2]) + len(frag) >= 7:
                hits.add(a[2] + "+" + frag)
    return frozenset(new), hits


def feed_str(active, s, mode):
    hits = set()
    for c in s:
        active, h = feed(active, c, mode)
        hits |= h
    return active, hits


def names_in(s, mode):
    return feed_str(frozenset(), s, mode)[1]
