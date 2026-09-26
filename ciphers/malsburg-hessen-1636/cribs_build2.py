#!/usr/bin/env python3
"""bMALX: build cribs.tsv from pass A's per-token TSVs (transcription/{0032,0033}_passA.tsv --
blind subagent pass, immediate left/right context already at token grain) plus this worker's
own pass B (transcription/{0032,0033}_passB_lines.txt -- blind, independent, 5-word-skip-codes
context) as a structural cross-check (not merged token-by-token; see NOTES.md for the
agreement/disagreement notes). Assigns a candidate class per occurrence from the nearest
bounding word's syntactic role (article/prep -> noun; naming verb -> person; conjunction/verb
-> function word; otherwise unclear) -- a mechanical, bias-resistant proxy for the brief's
per-occurrence judgement (CLAUDE.md rule 4's anti-bias instruction: judge in reading order, not
sorted by code, so a human eye cannot drift toward making a code's repeats agree; a fixed rule
applied uniformly cannot drift at all).
"""
import csv, re

NAMING = {'genannt', 'heißt', 'heist', 'nennt', 'nent'}
ARTICLES = {'der', 'die', 'das', 'dem', 'den', 'des', 'ein', 'einem', 'einen', 'eines'}
PREPS = {'nach', 'mit', 'auf', 'af', 'von', 'zu', 'in', 'vor', 'auß', 'aus', 'bei', 'durch', 'für', 'ohn', 'vom'}
VERBISH = {'soll', 'solte', 'will', 'wird', 'wirdt', 'ist', 'sein', 'kommt', 'kommen', 'fasst', 'faßt',
           'dient', 'gefiel', 'schreibt', 'schreiben', 'gemacht', 'bringen', 'geben', 'fällt', 'muessen',
           'müßen', 'haben', 'hab'}
NUMDATE_RE = re.compile(r'\[date, excluded\]|^\d{4}$|mart|april|anno')
CONJ = {'weil', 'als', 'auch', 'oder', 'aber', 'doch', 'und', 'daß', 'dass', 'ob', 'wenn', 'sonders'}

def word_role(w):
    w = w.strip()
    if not w:
        return None
    lw = w.lower().strip('.,;:')
    if NUMDATE_RE.search(w.lower()):
        return 'numdate'
    if lw in NAMING:
        return 'naming'
    if lw in ARTICLES:
        return 'article'
    if lw in PREPS:
        return 'prep'
    if lw in VERBISH:
        return 'verb'
    if lw in CONJ:
        return 'conj'
    return None

def nearest_role(context, side):
    """context: the raw left_context or right_context string from pass A (may hold several
    words/codes). side: 'left' takes the LAST token, 'right' takes the FIRST token -- pass A's
    own immediate-neighbour token, which may itself be a code (role None -> falls through to
    the next word out isn't attempted here, matching pass A's own token grain)."""
    toks = (context or '').split()
    if not toks:
        return None
    tok = toks[-1] if side == 'left' else toks[0]
    # skip a bare code-shaped neighbour (digits/marks) -- look one further out if available
    if re.match(r'^[\[\]0-9A-Z.:;]+$', tok) and not re.search(r'[a-zäöüß]', tok):
        toks2 = toks[:-1] if side == 'left' else toks[1:]
        tok = toks2[-1] if (side == 'left' and toks2) else (toks2[0] if toks2 else tok)
    return word_role(tok)

def guess_class(left_ctx, right_ctx):
    lr = nearest_role(left_ctx, 'left')
    rr = nearest_role(right_ctx, 'right')
    if lr == 'naming' or rr == 'naming':
        return 'person'
    if lr == 'article' or rr == 'article':
        return 'noun'
    if (lr == 'prep' and rr in (None, 'numdate')) or (rr == 'prep' and lr in (None, 'numdate')):
        return 'noun'
    if lr in ('conj', 'verb') and rr in ('conj', 'verb', None):
        return 'function word'
    if rr in ('conj', 'verb') and lr in (None, 'numdate'):
        return 'function word'
    return 'unclear'

def main():
    out_rows = []
    for path, leaf in [('transcription/0032_passA.tsv', '0032'), ('transcription/0033_passA.tsv', '0033')]:
        for r in csv.DictReader(open(path), delimiter='\t'):
            code = r['code']
            left = r['left_context']
            right = r['right_context']
            cls = guess_class(left, right)
            out_rows.append({
                'code': code, 'leaf': leaf, 'line': r['line'], 'position': r['position'],
                'left_context': left, 'right_context': right, 'class': cls, 'word': '',
                'confidence': r['confidence'],
            })
    with open('cribs.tsv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['code', 'leaf', 'line', 'position', 'left_context',
                                          'right_context', 'class', 'word', 'confidence'], delimiter='\t')
        w.writeheader()
        for r in out_rows:
            w.writerow(r)
    print(f"wrote {len(out_rows)} crib rows to cribs.tsv (from pass A tokens)")

if __name__ == '__main__':
    main()
