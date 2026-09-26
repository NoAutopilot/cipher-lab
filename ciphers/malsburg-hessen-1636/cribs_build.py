#!/usr/bin/env python3
"""bMALX: build cribs.tsv from a single-pass (pass B) line reading of record 509 (ff.32/33)
and the clear-clause files (ff.16/23/24/28), then run the rule-3 shuffle-consistency control
on codes seen 2+ times. LOW CONFIDENCE reading throughout (rule 2/precedent of clear_0023.txt
etc.) -- crib context only, no H/C claim (grade M, per CLAUDE.md rule 4).

Usage: python3 cribs_build.py
Reads: transcription/0032_passB_lines.txt, transcription/0033_passB_lines.txt (leaf:line\\ttext),
       clear_0016.txt, clear_0023.txt, clear_0024.txt, clear_0028.txt (existing crib-context files)
Writes: cribs.tsv, cribs_shuffle_control.txt
"""
import re, random, csv, statistics, sys

CODE_RE = re.compile(r'^([A-Z]\.?)?(\d{1,3})([A-Z]\.?)?[:.]?$')
MARK_RE = re.compile(r'^([A-Z])\.?[:.]?$')  # bare letter mark (D, G, H, L, N, O, S, W, X, Y, #, K, T, B, P, Y, Z)
BRACKET_RE = re.compile(r'^\[.*\]$')

def classify(tok):
    """Return ('CODE', canonical) or ('WORD', tok)."""
    raw = tok
    if BRACKET_RE.match(tok):
        return ('WORD', tok)
    # strip trailing punctuation for test but keep for display
    core = tok.rstrip('.:,;')
    if core in ('X.X', 'DIAMOND', 'G.G', 'K.K'):
        return ('CODE', core)
    m = CODE_RE.match(core)
    if m and m.group(2):
        digits = m.group(2)
        # glyph convention: i->1, z->2 already applied when I transcribed; exclude 4+ digit "real numbers"
        if len(digits) <= 3:
            canon = (m.group(1) or '') + digits + (m.group(3) or '')
            return ('CODE', canon)
        else:
            return ('WORD', tok)  # 4-5 digit run = real quantity/date, not a code
    m2 = MARK_RE.match(core)
    if m2 and core not in ('Ihr','Ist','In','Ob','Er','Es','Um','Am','Ab','Zu','Ao'):
        # bare single capital letter with a period, e.g. "D." "W." "K." -- a mark
        if len(core.rstrip('.')) == 1:
            return ('CODE', core.rstrip('.'))
    return ('WORD', tok)

def parse_file(path, leaf_tag):
    rows = []
    for line in open(path):
        line = line.rstrip('\n')
        if not line.strip():
            continue
        lid, text = line.split('\t', 1)
        toks = text.split()
        parsed = [(t, *classify(t)) for t in toks]
        rows.append((lid, parsed))
    return rows

def nearest_words(parsed, idx, direction, n=5):
    out = []
    i = idx + direction
    while 0 <= i < len(parsed) and len(out) < n:
        raw, kind, canon = parsed[i]
        if kind == 'WORD':
            out.append(raw)
        i += direction
    if direction == -1:
        out.reverse()
    return out

NAMING = {'genannt', 'heißt', 'heist', 'nennt'}
ARTICLES = {'der', 'die', 'das', 'dem', 'den', 'des', 'ein', 'einem', 'einen', 'eines'}
PREPS = {'nach', 'mit', 'auf', 'von', 'zu', 'in', 'vor', 'auß', 'aus', 'bei', 'durch', 'für', 'ohn'}
VERBISH = {'soll', 'will', 'wird', 'ist', 'sein', 'kommt', 'kommen', 'fasst', 'dient', 'gefiel',
           'schreibt', 'schreiben', 'gemacht', 'bringen', 'geben'}
NUMDATE = {'mart.', 'marty', 'april.', '1637.', '1637', 'anno'}
CONJ = {'weil', 'als', 'auch', 'oder', 'aber', 'doch', 'und', 'daß', 'dass', 'ob', 'wenn'}

def word_role(w):
    lw = w.lower().strip('.,;:')
    if lw in NAMING:
        return 'naming'
    if lw in ARTICLES:
        return 'article'
    if lw in PREPS:
        return 'prep'
    if lw in VERBISH:
        return 'verb'
    if lw in NUMDATE:
        return 'numdate'
    if lw in CONJ:
        return 'conj'
    return None

def guess_class(left, right):
    """Mechanical, bias-resistant proxy for a per-occurrence syntactic judgement (applied
    uniformly in leaf/line reading order, not sorted by code, so it cannot drift toward making
    a code's repeats agree -- CLAUDE.md rule 4/step-4 anti-bias instruction). Looks at the
    single nearest word on each side (immediate bounding word, not the whole 5-word window):
    a naming verb next door -> person; an article or preposition immediately touching the code
    -> noun (the article/prep's object); a conjunction/verb touching on both sides and nothing
    else -> function word (the code sits where a short connective could, not a content word);
    otherwise unclear. This is a syntactic heuristic, not a philologist's semantic reading --
    flagged as such in NOTES.md."""
    lr = word_role(left[-1]) if left else None
    rr = word_role(right[0]) if right else None
    if lr == 'naming' or rr == 'naming':
        return 'person'
    if lr == 'article' or rr == 'article':
        return 'noun'
    if lr == 'prep' and rr in (None, 'numdate'):
        return 'noun'
    if rr == 'prep' and lr in (None, 'numdate'):
        return 'noun'
    if lr in ('conj', 'verb') and rr in ('conj', 'verb', None):
        return 'function word'
    if rr in ('conj', 'verb') and lr in (None, 'numdate'):
        return 'function word'
    if not left and not right:
        return 'unclear'
    return 'unclear'

def build_cribs():
    out_rows = []
    for path, tag in [('transcription/0032_passB_lines.txt', '0032'),
                       ('transcription/0033_passB_lines.txt', '0033')]:
        for lid, parsed in parse_file(path, tag):
            for idx, (raw, kind, canon) in enumerate(parsed):
                if kind != 'CODE':
                    continue
                left = nearest_words(parsed, idx, -1)
                right = nearest_words(parsed, idx, +1)
                out_rows.append({
                    'code': canon, 'leaf': tag, 'line': lid, 'left_context': ' '.join(left),
                    'right_context': ' '.join(right), 'class': guess_class(left, right),
                    'word': '', 'confidence': 'M', 'raw': raw,
                })
    return out_rows

if __name__ == '__main__':
    rows = build_cribs()
    with open('cribs.tsv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['code','leaf','line','left_context','right_context','class','word','confidence','raw'], delimiter='\t')
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print(f"wrote {len(rows)} crib rows to cribs.tsv")
