#!/usr/bin/env python3
"""Shared loader for the settled drafts (H27)."""
def settled_lines(root, prefix, drop_clear=False):
    """H27 (29 Sept 2026): lines of the settled three-pass drafts (c1, c2, c34) for pages starting with prefix; falls back to passA.tsv.
    drop_clear (H43, 29 Sept 2026): skip the positions listed in clear_spans.tsv (clear digits and capitals written inside
    the cipher text, which the drafts carry as ids); default off so every earlier row reproduces unchanged."""
    import csv, os, collections
    by = collections.OrderedDict()
    srcs = [os.path.join(root, f) for f in ('ciphertext_c1_draft.tsv', 'ciphertext_c2_draft.tsv', 'ciphertext_c34_draft.tsv') if os.path.exists(os.path.join(root, f))]
    seen = set(); skip = set()
    if drop_clear:
        skip = {(r['line'], r['position']) for r in csv.DictReader(open(os.path.join(root, 'clear_spans.tsv')), delimiter='\t')}
    for src in srcs:
        for r in csv.DictReader(open(src), delimiter='\t'):
            if r['line'].startswith(prefix) and (r['line'], r['position']) not in skip: by.setdefault(r['line'], []).append(r['sign'].rstrip('?')); seen.add(r['line'].split('_')[0])
    for r in csv.DictReader(open(os.path.join(root, 'passA.tsv')), delimiter='\t'):
        if r['line'].startswith(prefix) and r['line'].split('_')[0] not in seen: by.setdefault(r['line'], []).append(r['sign'])
    keys = sorted(by, key=lambda k: (0 if k.startswith('c4a0') else 1 if k.startswith('c4a') else 2 if k.startswith('c4b') else 3, k))
    return collections.OrderedDict((k, by[k]) for k in keys)
