#!/usr/bin/env python3
"""Look-alike pass for a symbol-cipher transcription read by two blind passes (LOOKALIKE-TOOL, 2 Oct 2026).

What it is for. Two blind machine passes over a symbol cipher disagree mostly on a few sign pairs that look alike
(on the Nevers/Birago 1572 sheet: T83/X_NEW, T60/T86, T18/T98, T24/T83). Instead of a third full pass, re-read only
the tiles where the readers split or whose label sits in a frequent confusion pair, against a sheet cut showing only the
candidate signs, and fold that re-read in by a fixed 2-of-3 rule. Promoted from ciphers/nevers-birago-fr3251-1572/harvest/
{confusion_1572.py, lookalike_packet.py, lookalike_reconcile.py} (NEVBIR-LOOKALIKE, 2 Oct 2026). Three subcommands:

  confusion AGREEMENT.tsv... --out confusion.tsv [--target LEAF ...]
      Label swaps (unordered pairs) with counts across every two-reader alignment written by reconcile_passes.py-style
      tools (columns idA, idB, status, passage, posA). Only rows with both labels and status 'split*' count; gaps do not.
      An off-sheet label (X_NEW) is a label like any other. Leaf name = the agreement file's parent folder.
  packet --agreement A.tsv --confusion confusion.tsv [--passc passC.tsv] --top 10 --crops DIR --sheet SHEET.png
         --sheet-map MAP.json --out DIR [--run NAME] [--cell 110 --cols 9]
      Flag every tile whose two readers split or whose passC label sits in a top-N pair; candidates per tile are A's,
      B's and passC's labels plus the label's two most frequent confusion partners. A passC row past the end of its
      passage in the alignment (one reader only, e.g. a re-cut line tail) is flagged 'single' with A = its label. Writes <run>_tiles.tsv,
      <run>_candidates.png (only the candidate cells of the blind sheet: ids, never values) and <run>_prompt.md
      (the value-blind re-read prompt: crop paths, tile ids, the passC label sequence for orientation, no key values).
  reconcile --tiles T.tsv --passc passC.tsv --reread R.tsv --out passD.tsv [--alt passD_alt.tsv] [--focus focus.tsv]
      The rule, fixed before any score is computed: a firm (H/M, not SPLIT) re-read that matches reader A or reader B
      settles the tile at 2-of-3 (the re-read label wins); anything else stays UNSETTLED and keeps the passC label (a third
      reader alone does not overturn two) and goes to focus.tsv (sid<TAB>question) for tools/sign_sorter.py --focus.
      --alt writes the secondary sequence taking every firm re-read label (a pointer only, never the primary).
      Residual disagreement = unsettled / all signs (a 2-of-3 figure, not the two-reader rate, and not true error).
  audit --passa A.tsv --passb B.tsv --passc C.tsv --confusion confusion.tsv --sample N [--plant 0.05] [--seed 1]
        [--k 3] [--include POS.tsv] [--crops-glob 'DIR/{line}_s?.jpg'] --sheet SHEET.png --sheet-map MAP.json --out DIR
      (TX-AGREEAUDIT, 4 Oct 2026; research/TRANSCRIPTION-PRACTICE-2026-10-04.md #2) Re-check signs BOTH readers agreed on,
      which confusion/packet never look at. Passes are (line, pos, sign) or (passage, pos, sign_id) TSVs; A and B are
      aligned per line to C (the committed read) by edit distance and a C position is 'agreed' when A, B and C carry the
      same label there. Draws N agreed positions at random (seeded), plus any --include positions (line, pos), and
      plants round(plant x items) known errors: the shown label at a planted position is swapped to its most frequent
      confusion partner. The prompt shows the reading as it stands (plants applied, audited positions bracketed) and,
      per item, the shown label plus its k-1 top confusion partners (and, for a plant, the original label) as ids in a
      random order -- a choice, never "is this X?". Writes <run>_audit_items.tsv (the hidden answer: planted, original,
      shown), <run>_audit_candidates.png and <run>_audit_prompt.md.
  audit-score --items I.tsv --reread R.tsv [--truth TRUTH.tsv] [--passc C.tsv --out-corrected OUT.tsv]
      The rule, fixed before any score: an item is FLAGGED when the re-read picks a label other than the shown one at
      H or M (an L, SPLIT or X_NEW answer is not a flag). Control: planted catch = flagged AND re-read == original;
      the audit is a non-test unless catch >= 0.80 (rule 3; exit 3 when it misses). With --truth (a BENCHMARK-TX truth
      file, line/pos/truth/status), reports flags on agreed-and-wrong vs agreed-and-right unplanted items and the
      paired count fixed / broken if every flag were applied; --out-corrected writes C with those relabels.
  windows (--tiles T.tsv | --items I.tsv) --passc C.tsv (--manifest M.json [--crop-pattern '*_{line}_s*'] | --crops-glob G)
          --out DIR [--run NAME] [--status split] [--half 6.5] [--scale 2] [--per 6] [--ink 110] [--ink-min 2] [--desc D.tsv]
      (N7-LKTOOL, 4 Oct 2026; promoted from ciphers/fr16104-vivonne-spain-1572/tx/viv53L_windows.py and viv54L_windows.py)
      The re-read instrument that worked when packet's and audit's prompts did not: those show whole line crops plus the
      passC labels, and drew 7/7 Sonnet re-reads on Vivonne inks 53/54 that copied passC instead of reading shapes (voided,
      about half of both jobs' spend). Here each tile (--tiles, rows of --status, default 'split') or audit item (--items)
      gets its own window: the line's segments are stitched on source x (manifest box[0]), the inked span a..b is the first
      and last column with >= --ink-min pixels darker than --ink, the sign's x is estimated as a + (pos - 0.5)(b - a)/n
      (n = the line's sign count in passC), and +-HALF sign widths are cut, upscaled, with red ticks at the estimate.
      Windows go --per to a montage captioned with the tile id ("passage.pos") or "item N"; the prompt gives the 3 labels
      before and after (to find the sign) and the candidates in ALPHABETICAL order, never the tile's own label. Writes
      DIR/win/<run>_NN.png, <run>_prompt.md and, for --tiles, <run>_tiles.tsv (the input rows filtered, same columns,
      for `reconcile --tiles`); for --items the answer rows are keyed by item for `audit-score --items <the audit items>`.
      Not for: estimating where a sign is on a badly sloped or unevenly spaced line (the x estimate assumes even spacing;
      the prompt tells the reader it can be off by 1-3 signs) -- re-cut such lines first (iiif_lines.py --follow-slope).
  ECHO WARNING (packet, audit): their default prompt shows the committed labels; --hide-passc withholds them (packet: no
  line sequences, candidates alphabetical; audit: [n:?] brackets). A re-read that agrees with passC everywhere is an echo,
  not a confirmation.
  (The brief named `reconcile --passA --passB`; reader A's and B's aligned labels reach reconcile through the tiles
  file the packet wrote from the agreement alignment, so the raw passes are not re-aligned here.)

Known-answer result (LOOKALIKE-TOOL, 2 Oct 2026, no.87 f.178r + f.179r against the clerk's clear sheet on canvas 182):
see LESSONS.md "Look-alike pass" for the before/after true error; read it before trusting a residual as reader error.

Must NOT be used for: settling the sign inventory itself (which shapes are one sign, which cell is a bad cut) -- when the
two passes split on more than about a tenth of signs because the alphabet is unsettled, that is the owner's sign sorter
(CLAUDE.md Usage 6), and this pass would only make three machine readers agree on a wrong sheet. Nor for a single-pass
transcription (no A/B split to vote on), nor as a source of S grades on its own: its residual is agreement, not truth.

Offline tests: python3 tools/tests/test_lookalike_pass.py; python3 tools/tests/test_lookalike_audit.py;
python3 tools/tests/test_lookalike_windows.py
"""
import argparse, collections, csv, json, os, sys
from pathlib import Path


def _read(p):
    return list(csv.DictReader(open(p, newline=''), delimiter='\t'))


def _write(p, rows, fields=None):
    with open(p, 'w', newline='') as o:
        w = csv.DictWriter(o, fieldnames=fields or list(rows[0]), delimiter='\t', lineterminator='\n')
        w.writeheader(); w.writerows(rows)


def confusion(files, out, targets=()):
    cnt, tgt, tot = collections.Counter(), collections.Counter(), 0
    ex = collections.defaultdict(list)
    for f in files:
        leaf = Path(f).parent.name
        for r in _read(f):
            a, b, st = r.get('idA', ''), r.get('idB', ''), r.get('status', '')
            if not a or not b:
                continue
            tot += 1
            if not st.startswith('split') or a == b:
                continue
            k = tuple(sorted((a, b)))
            cnt[k] += 1
            if leaf in targets:
                tgt[k] += 1
            if len(ex[k]) < 4:
                ex[k].append(f"{leaf}:{r.get('passage', '')}.{r.get('posA', '')}")
    rows = [dict(label_a=k[0], label_b=k[1], n=n, n_target=tgt[k], examples=' '.join(ex[k]))
            for k, n in sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))]
    _write(out, rows, ['label_a', 'label_b', 'n', 'n_target', 'examples'])
    return dict(pairs_read=tot, swaps=sum(cnt.values()), distinct=len(cnt))


ECHO_NOTE = '<!-- operator note (N7-LKTOOL, 4 Oct 2026): this prompt shows the committed label sequence and whole line crops; it drew\n7/7 Sonnet re-reads that echoed passC on Vivonne inks 53/54 (voided). Prefer `windows` (per-tile crops, label hidden) or\n--hide-passc, and treat a re-read that agrees with passC everywhere as an echo, not a confirmation. -->\n'


PROMPT = """# Look-alike re-read, {run} (value-blind)

You are re-reading {n} sign tiles of a symbol-cipher transcription. Two earlier readers disagreed on some of them, or
gave a label that is often confused with another. You see only the line crops and a sheet of the candidate sign shapes,
labelled by id. You are never told what any sign means; do not guess letters or words.

Line crops (read these images): {crops}
Candidate sheet (ids only): {sheet}

For each tile below, find the sign at that passage and position ({orient}'before'/'after' are the neighbouring
labels) and pick the candidate id whose shape it is. Labels shown anywhere here are earlier readers' and may be wrong:
judge the shape in the image, never copy a label.
Answer one TSV row per tile, header: passage<TAB>pos<TAB>label<TAB>conf<TAB>second<TAB>note
  label  one of the tile's candidates, X_NEW if none fits, or SPLIT:a|b if you cannot choose between two
  conf   H (clear), M (probable), L (guess); second = your runner-up id or empty; note = the shape feature you used.

Tiles (passage, pos, candidates, before | after):
{tiles}
{seqs}"""


def packet(agreement, conf_path, passc, top, crops, sheet, sheet_map, out, run, cell=110, cols=9, hide_passc=False):
    from PIL import Image
    conf = _read(conf_path)
    toplabs = {x for r in conf[:top] for x in (r['label_a'], r['label_b'])}
    partners = collections.defaultdict(list)
    for r in conf:
        partners[r['label_a']].append(r['label_b']); partners[r['label_b']].append(r['label_a'])
    al, pc = _read(agreement), _read(passc)
    merged = [r for r in al if r.get('merged', '') not in ('', 'NONE')]
    tiles, used, j = [], set(), 0
    for i, c in enumerate(pc, 1):
        lab = c['sign_id']
        if j < len(merged) and merged[j]['passage'] == c['passage']:
            r = merged[j]; j += 1
            if r['merged'] != lab:
                sys.exit(f'packet: passC row {i} {c["passage"]}.{c["pos"]}={lab} does not follow the agreement '
                         f'merged column ({r["passage"]} {r["merged"]}); pass the passC built from this agreement')
            A, B, st = r['idA'], r['idB'], r['status']
            split = st != 'agree'
        else:   # a passC row past the end of its passage in the alignment: read by one reader only (e.g. a re-cut tail)
            A, B, st, split, r = lab, '', 'single', True, {}
        if not split and lab not in toplabs:
            continue
        cand = [x for x in dict.fromkeys([A, B, lab] + partners[lab][:2]) if x]
        used.update(cand)
        ctx = ' '.join(p['sign_id'] for p in pc[max(0, i - 4):i - 1] if p['passage'] == c['passage'])
        ctx2 = ' '.join(p['sign_id'] for p in pc[i:i + 3] if p['passage'] == c['passage'])
        tiles.append(dict(run=run, passage=c['passage'], pos=c['pos'], passC=lab, A=A, B=B, status=st,
                          why='single' if st == 'single' else ('split' if split else 'top-pair'),
                          candidates=','.join(cand), before=ctx, after=ctx2,
                          noteA=r.get('noteA', ''), noteB=r.get('noteB', '')))
    if j != len(merged):
        sys.exit(f'packet: agreement merged {len(merged)} signs, passC matched only {j}')
    os.makedirs(out, exist_ok=True)
    fields = ['run', 'passage', 'pos', 'passC', 'A', 'B', 'status', 'why', 'candidates', 'before', 'after', 'noteA', 'noteB']
    _write(os.path.join(out, f'{run}_tiles.tsv'), tiles, fields)
    order = [c['id'] for c in json.load(open(sheet_map))]
    ids = sorted(t for t in used if t in order)
    cand_png = os.path.join(out, f'{run}_candidates.png')
    if ids:
        sh = Image.open(sheet); nc = min(8, len(ids))
        im = Image.new('RGB', (nc * cell, ((len(ids) + nc - 1) // nc) * cell), 'white')
        for n, t in enumerate(ids):
            k = order.index(t); gx, gy = (k % cols) * cell, (k // cols) * cell
            im.paste(sh.crop((gx, gy, gx + cell, gy + cell)), ((n % nc) * cell, (n // nc) * cell))
        im.save(cand_png)
    seqs = collections.OrderedDict()
    for p in pc:
        seqs.setdefault(p['passage'], []).append(p['sign_id'])
    crop_list = sorted(str(p.resolve()) for p in Path(crops).glob('*.jpg') if 'debug' not in p.name) if crops else []
    cfmt = (lambda c: ','.join(sorted(c.split(',')))) if hide_passc else (lambda c: c)
    txt = PROMPT.format(run=run, n=len(tiles), crops=', '.join(crop_list) or '(none given)', sheet=os.path.abspath(cand_png),
                        orient='' if hide_passc else 'the passC sequence of the line is given for orientation; ',
                        tiles='\n'.join(f"{t['passage']}\t{t['pos']}\t{cfmt(t['candidates'])}\t{t['before']} | {t['after']}"
                                        for t in tiles),
                        seqs='' if hide_passc else '\nLine sequences (passC, for orientation only):\n' +
                        '\n'.join(f'{k}: {" ".join(v)}' for k, v in seqs.items()) + '\n')
    open(os.path.join(out, f'{run}_prompt.md'), 'w').write(('' if hide_passc else ECHO_NOTE) + txt)
    return dict(signs=len(pc), tiles=len(tiles), split=sum(t['why'] == 'split' for t in tiles), cands=len(ids))


def reconcile(tiles_p, passc, reread, out, alt_out=None, focus_out=None, run=None):
    pc, tiles = _read(passc), _read(tiles_p)
    rr = {(r['passage'], r['pos']): r for r in _read(reread)}
    tk = {(t['passage'], t['pos']): t for t in tiles}
    missing = [k for k in tk if k not in rr]
    if missing:
        sys.exit(f'reconcile: {len(missing)} flagged tiles have no re-read row, e.g. {missing[0]}')
    run = run or (tiles[0]['run'] if tiles else 'run')
    outr, alt, focus, uns, changed = [], [], [], 0, 0
    for c in pc:
        k = (c['passage'], c['pos']); lab, conf, note, q = c['sign_id'], c.get('conf', ''), 'passC', ''
        alt_lab = None
        if k in tk:
            t, r = tk[k], rr[k]
            rl, rc = r['label'].strip(), r['conf'].strip()
            firm = rc in ('H', 'M') and not rl.startswith('SPLIT')
            if firm and rl in (t['A'], t['B']):
                note = 'lookalike 2-of-3' if t['why'] == 'split' else 'lookalike confirms'
                lab, conf = rl, rc
            else:
                uns += 1; note = 'lookalike UNSETTLED'
                parts = rl.replace('SPLIT:', '').split('|')
                cands = sorted({x for x in (t['A'], t['B'], t['passC'], *parts, r.get('second', '')) if x})
                q = (f"{c['passage']}.{c['pos']}: readers {t['A'] or '-'}/{t['B'] or '-'}, look-alike {rl} ({rc}); "
                     f"which of {', '.join(cands)}?")
                focus.append((f"{run}_{c['passage']}_{c['pos']}", q))
            if firm:
                alt_lab = rl
            if lab != c['sign_id']:
                changed += 1
        outr.append(dict(passage=c['passage'], pos=c['pos'], sign_id=lab, conf=conf, note=note, question=q))
        alt.append(dict(passage=c['passage'], pos=c['pos'], sign_id=alt_lab or lab, conf=conf, note=note))
    _write(out, outr)
    if alt_out:
        _write(alt_out, alt)
    if focus_out:
        with open(focus_out, 'w') as o:
            for sid, q in focus:
                o.write(f'{sid}\t{q}\n')
    return dict(signs=len(pc), flagged=len(tiles), relabelled=changed, unsettled=uns,
                residual=round(uns / max(1, len(pc)), 3))


def _norm(p, prefix=''):
    """(line, pos, sign) rows from a pass TSV in either column convention."""
    out = []
    for r in _read(p):
        ln = r.get('line') or (prefix + r['passage'])
        out.append((ln, int(r['pos']), (r.get('sign') or r.get('sign_id') or '').strip()))
    return out


def _lines(rows):
    d = collections.OrderedDict()
    for ln, pos, s in rows:
        d.setdefault(ln, []).append((pos, s))
    return d


def _align(ref, hyp):
    """Edit-distance alignment; returns, per ref index, the hyp label aligned to it (None when ref is unmatched)."""
    n, m = len(ref), len(hyp)
    D = [[0.0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        D[i][0] = i
    for j in range(1, m + 1):
        D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i - 1][j - 1] + (ref[i - 1] != hyp[j - 1]), D[i - 1][j] + 1, D[i][j - 1] + 1)
    out, i, j = [None] * n, n, m
    while i > 0 and j > 0:
        if D[i][j] == D[i - 1][j - 1] + (ref[i - 1] != hyp[j - 1]):
            out[i - 1] = hyp[j - 1]; i -= 1; j -= 1
        elif D[i][j] == D[i - 1][j] + 1:
            i -= 1
        else:
            j -= 1
    return out


def agreed_positions(passa, passb, passc):
    """[(line, pos, label, agreed?)] over C, with agreed = A, B and C identical at that aligned position."""
    A, B, C = _lines(passa), _lines(passb), _lines(passc)
    res = []
    for ln, seq in C.items():
        ref = [s for _, s in seq]
        a = _align(ref, [s for _, s in A.get(ln, [])]) if ln in A else [None] * len(ref)
        b = _align(ref, [s for _, s in B.get(ln, [])]) if ln in B else [None] * len(ref)
        for (pos, s), x, y in zip(seq, a, b):
            res.append((ln, pos, s, bool(s) and x == s and y == s))
    return res


AUDIT_PROMPT = """# Proofreading audit, {run} (value-blind)

You are proofreading {n} signs of a symbol-cipher transcription against the manuscript. The reading below is what the
transcription currently says; some of it may be wrong. For each bracketed position, look at the sign in the line crop
and pick, from the listed candidate ids, the one whose shape it is -- whether or not it is the label the reading shows;
never copy a label from the reading.
You are never told what any sign means; do not guess letters or words.

Line crops (read these images; s1, s2, s3 are left, middle, right thirds of one line): {crops}
Candidate sheet (ids only): {sheet}

Answer one TSV row per item, header: item<TAB>label<TAB>conf<TAB>second<TAB>note
  label  one of the item's candidates, X_NEW if none fits, or SPLIT:a|b if you cannot choose between two
  conf   H (clear), M (probable), L (guess); second = your runner-up id or empty; note = the shape feature you used.

Items (item, line, pos, candidates in random order, reading before | after):
{items}

The reading (bracketed [item:label] = positions to audit):
{seqs}
"""


def audit(passa, passb, passc, conf_path, sample, plant, seed, k, include, crops_glob, sheet, sheet_map, out, run,
          cell=110, cols=9, lines=None, hide_passc=False):
    import random, re
    rng = random.Random(seed)
    A, B, C = _norm(passa), _norm(passb), _norm(passc)
    if lines:
        C = [x for x in C if re.fullmatch(lines, x[0])]
    ag = agreed_positions(A, B, C)
    partners = collections.defaultdict(list)
    for r in _read(conf_path):
        partners[r['label_a']].append(r['label_b']); partners[r['label_b']].append(r['label_a'])
    pool = [(ln, pos, s) for ln, pos, s, ok in ag if ok]
    forced = set()
    if include:
        forced = {(r['line'], int(r['pos'])) for r in _read(include)}
    picked = [x for x in pool if (x[0], x[1]) in forced]
    rest = [x for x in pool if (x[0], x[1]) not in forced]
    picked += rng.sample(rest, min(sample, len(rest)))
    rng.shuffle(picked)
    plantable = [i for i, x in enumerate(picked) if partners[x[2]] and (x[0], x[1]) not in forced]
    nplant = min(len(plantable), int(round(plant * len(picked))))
    plants = set(rng.sample(plantable, nplant))
    items, shown_map = [], {}
    for n, (ln, pos, s) in enumerate(picked, 1):
        shown = partners[s][0] if (n - 1) in plants else s
        cand = [shown] + [p for p in partners[shown] if p != shown][:k - 1]
        if s not in cand:
            cand.append(s)
        cand = list(dict.fromkeys(cand)); rng.shuffle(cand)
        items.append(dict(run=run, item=n, line=ln, pos=pos, original=s, shown=shown, planted=int((n - 1) in plants),
                          forced=int((ln, pos) in forced), candidates=','.join(cand)))
        shown_map[(ln, pos)] = (n, shown)
    os.makedirs(out, exist_ok=True)
    _write(os.path.join(out, f'{run}_audit_items.tsv'), items)
    seqs, lines_used = collections.OrderedDict(), []
    for ln, pos, s in C:
        if (ln, pos) in shown_map:
            n, sh = shown_map[(ln, pos)]
            seqs.setdefault(ln, []).append(f'[{n}:?]' if hide_passc else f'[{n}:{sh}]')
        else:
            seqs.setdefault(ln, []).append(s)
    used_lines = list(dict.fromkeys(it['line'] for it in sorted(items, key=lambda t: (t['line'], t['pos']))))
    ctx = {}
    for ln in used_lines:
        seq = seqs[ln]
        for i, tok in enumerate(seq):
            m = re.match(r'\[(\d+):', tok)  # an audit bracket; a transcription's own [PLAIN:...] token is not one
            if m:
                ctx[int(m.group(1))] = (' '.join(seq[max(0, i - 3):i]), ' '.join(seq[i + 1:i + 4]))
    ids = sorted({c for it in items for c in it['candidates'].split(',')})
    order = [c['id'] for c in json.load(open(sheet_map))]
    cand_png = os.path.join(out, f'{run}_audit_candidates.png')
    have = [t for t in ids if t in order]
    if have:
        from PIL import Image
        sh = Image.open(sheet); nc = min(8, len(have))
        im = Image.new('RGB', (nc * cell, ((len(have) + nc - 1) // nc) * cell), 'white')
        for n, t in enumerate(have):
            kk = order.index(t); gx, gy = (kk % cols) * cell, (kk // cols) * cell
            im.paste(sh.crop((gx, gy, gx + cell, gy + cell)), ((n % nc) * cell, (n // nc) * cell))
        im.save(cand_png)
    import glob as _g
    crops = []
    for ln in used_lines:
        crops += sorted(str(Path(x).resolve()) for x in _g.glob(crops_glob.format(line=ln))) if crops_glob else []
    txt = AUDIT_PROMPT.format(
        run=run, n=len(items), crops=', '.join(crops) or '(none given)', sheet=os.path.abspath(cand_png),
        items='\n'.join(f"{it['item']}\t{it['line']}\t{it['pos']}\t{it['candidates']}\t{ctx[it['item']][0]} | "
                        f"{ctx[it['item']][1]}" for it in sorted(items, key=lambda t: t['item'])),
        seqs='\n'.join(f'{ln}: {" ".join(seqs[ln])}' for ln in used_lines))
    open(os.path.join(out, f'{run}_audit_prompt.md'), 'w').write(('' if hide_passc else ECHO_NOTE) + txt)
    return dict(signs=len(C), agreed=len(pool), items=len(items), forced=len(picked) - min(sample, len(rest)),
                planted=nplant, lines=len(used_lines), crops=len(crops), cands=len(have))


WIN_PROMPT = """# Look-alike re-read by window, {run} (value-blind)

{n} {what}. Each has its own window image: open the montages below IN ORDER ({per} windows each, captioned in blue with the
{cap}). In each window the red ticks top and bottom mark the ESTIMATED position of the sign (the estimate can be off by 1-3
signs). Find the sign using the labels of the 3 signs before and after it, then decide which candidate's SHAPE it is.{plant}
The candidate list is alphabetical; nothing tells you which is "right". You are never told what any sign means; do not guess
letters or words.

Montages: {pngs}

Answer one TSV row per {unit}, header: {header}
  label = one candidate id, X_NEW if none fits, SPLIT:a|b if you cannot choose; conf H clear / M probable / L guess (use L
  whenever you could not find the sign in its window); second = runner-up or empty; note = the shape feature you SAW.

{listhead}
{rows}
"""


def _line_strips(manifest, crops_glob, pattern):
    """line id -> callable returning the stitched grey strip. With a manifest (tools/iiif_lines.py manifest.json:
    'iiif_lines' entries with 'crop' relative to the manifest's folder and 'box' = source x0,y0,x1,y1), a line's
    segments are those whose file name matches PATTERN.format(line=ID) and are pasted at their source x offset; without
    one, CROPS_GLOB.format(line=ID) segments are abutted in name order."""
    import fnmatch, glob as _g
    from PIL import Image
    ents = []
    if manifest:
        m = json.load(open(manifest)); base = os.path.dirname(os.path.abspath(manifest))
        ents = [(e['box'][0] if e.get('box') else None, os.path.join(base, e['crop'])) for e in m.get('iiif_lines', m)
                if 'debug' not in e['crop']]

    def build(ln):
        if manifest:
            segs = [(x, f) for x, f in ents if fnmatch.fnmatch(os.path.basename(f), pattern.format(line=ln))]
            segs = sorted(segs) if all(x is not None for x, _ in segs) else [(None, f) for _, f in sorted(segs, key=lambda t: t[1])]
        else:
            segs = [(None, f) for f in sorted(_g.glob(crops_glob.format(line=ln))) if 'debug' not in f]
        if not segs:
            sys.exit(f'windows: no crop segments found for line {ln}')
        ims, off = [], 0
        x0 = segs[0][0]
        for x, f in segs:
            im = Image.open(f).convert('L')
            ims.append(((x - x0) if x is not None else off, im)); off += im.width
        S = Image.new('L', (max(o + im.width for o, im in ims), max(im.height for _, im in ims)), 255)
        for o, im in ims:
            S.paste(im, (o, 0))
        return S
    return build


def _ink_extent(S, ink, ink_min):
    """First and last column of S with at least INK_MIN pixels darker than INK (the inked span of the line)."""
    W, H = S.size
    data = S.tobytes()
    cols = [x for x in range(W) if sum(1 for y in range(H) if data[y * W + x] < ink) >= ink_min]
    return (cols[0], cols[-1]) if cols else (0, W)


def _window(S, a, b, nsigns, pos, half, scale):
    """Window of +-HALF sign widths around the estimated x of sign POS (1-based) of NSIGNS spread evenly over the inked
    span a..b, upscaled SCALE x, with red ticks top and bottom at the estimate."""
    from PIL import ImageDraw
    sw = (b - a) / max(1, nsigns)
    x = a + (pos - 0.5) * sw
    lo, hi = int(max(0, x - half * sw)), int(min(S.width, x + half * sw))
    w = S.crop((lo, 0, hi, S.height)).convert('RGB')
    w = w.resize((w.width * scale, w.height * scale))
    dr = ImageDraw.Draw(w); tx = int((x - lo) * scale)
    dr.line((tx, 0, tx, 14), fill='red', width=3); dr.line((tx, w.height - 14, tx, w.height), fill='red', width=3)
    return w


def _montages(wins, d, stem, per):
    from PIL import Image, ImageDraw, ImageFont
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 22)
    except OSError:
        font = ImageFont.load_default()
    pngs = []
    for k in range(0, len(wins), per):
        grp = wins[k:k + per]
        M = Image.new('RGB', (max(w.width for _, w in grp), sum(w.height + 34 for _, w in grp)), 'white')
        dr = ImageDraw.Draw(M); y = 0
        for tid, w in grp:
            dr.text((6, y + 4), tid, fill='blue', font=font); M.paste(w, (0, y + 32)); y += w.height + 34
        p = os.path.join(d, f'{stem}{k // per + 1:02d}.png'); M.save(p); pngs.append(os.path.abspath(p))
    return pngs


def _desc(p):
    """id -> shape description from a TSV (id<TAB>description) or a JSON object; empty without a file."""
    if not p:
        return {}
    if p.endswith('.json'):
        return json.load(open(p))
    return {r[0]: r[1] for r in csv.reader(open(p, newline=''), delimiter='\t') if len(r) >= 2 and not r[0].startswith('#')}


def windows(passc, out, tiles=None, items=None, manifest=None, crops_glob='', pattern='*_{line}_s*', run=None,
            status='split', half=6.5, scale=2, per=6, ink=110, ink_min=2, desc=None):
    if bool(tiles) == bool(items):
        sys.exit('windows: give exactly one of --tiles (a packet tiles file) or --items (an audit items file)')
    if not manifest and not crops_glob:
        sys.exit('windows: give --manifest (iiif_lines manifest.json) or --crops-glob')
    C = _norm(passc)
    nline, seqs = collections.Counter(), collections.defaultdict(list)
    for ln, pos, s in C:
        nline[ln] += 1; seqs[ln].append(s)
    D = _desc(desc)
    build, strips, wins, rows = _line_strips(manifest, crops_glob, pattern), {}, [], []

    def win(ln, pos):
        if ln not in nline:
            sys.exit(f'windows: line {ln} is not in the passC file')
        if ln not in strips:
            S = build(ln); strips[ln] = (S,) + _ink_extent(S, ink, ink_min)
        S, a, b = strips[ln]
        return _window(S, a, b, nline[ln], pos, half, scale)

    def cands(field):   # alphabetical, so the order never singles out the current reading
        cs = sorted({x for x in field.split(',') if x})
        return '; '.join(f"{c} = {D.get(c, c.strip('{}') + ' (free description)')}" if D else c for c in cs)
    os.makedirs(os.path.join(out, 'win'), exist_ok=True)
    if tiles:
        T = _read(tiles)
        sel = [t for t in T if status == 'all' or t['status'] in status.split(',')]
        run = run or ((T[0]['run'] + '_win') if T and T[0].get('run') else 'win')
        tout = os.path.join(out, f'{run}_tiles.tsv')
        if os.path.abspath(tout) == os.path.abspath(tiles):
            sys.exit('windows: --run would overwrite the input tiles file; pick another --run')
        for t in sel:
            wins.append((f"{t['passage']}.{t['pos']}", win(t['passage'], int(t['pos']))))
            rows.append(f"{t['passage']}\t{t['pos']}\tbefore: {t['before']} | after: {t['after']}\tcandidates: "
                        f"{cands(t['candidates'])}")
        if sel:
            _write(tout, sel, list(T[0]))
        what, cap, unit, header = ('tiles', 'tile id passage.pos', 'tile',
                                   'passage<TAB>pos<TAB>label<TAB>conf<TAB>second<TAB>note')
        listhead, plant, n = 'Tiles (passage, pos, context, candidates):', '', len(sel)
    else:
        I = sorted(_read(items), key=lambda r: int(r['item']))
        run = run or ((I[0]['run'] + '_audit_win') if I and I[0].get('run') else 'audit_win')
        shown = {(it['line'], int(it['pos'])): it['shown'] for it in I}
        for it in I:
            ln, pos = it['line'], int(it['pos'])
            wins.append((f"item {it['item']}", win(ln, pos)))
            seq = [shown.get((ln, i + 1), s) for i, s in enumerate(seqs[ln])]
            rows.append(f"{it['item']}\tbefore: {' '.join(seq[max(0, pos - 4):pos - 1])} | after: "
                        f"{' '.join(seq[pos:pos + 3])}\tcandidates: {cands(it['candidates'])}")
        what, cap, unit, header = ('items', 'item number ("item N")', 'item',
                                   'item<TAB>label<TAB>conf<TAB>second<TAB>note')
        listhead, n = 'Items (item, context, candidates):', len(I)
        plant = ' Some items are deliberately wrong in the reading around them; judge only the shape.'
    pngs = _montages(wins, os.path.join(out, 'win'), f'{run}_', per) if wins else []
    txt = WIN_PROMPT.format(run=run, n=n, what=what, per=per, cap=cap, plant=plant, pngs=', '.join(pngs) or '(none)',
                            unit=unit, header=header, listhead=listhead, rows='\n'.join(rows))
    open(os.path.join(out, f'{run}_prompt.md'), 'w').write(txt)
    return dict(mode='tiles' if tiles else 'items', windows=len(wins), montages=len(pngs), lines=len(strips), run=run)


def _truthset(p):
    rows = csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t')
    return {(r['line'], int(r['pos'])): r for r in rows}


def audit_score(items_p, reread_p, truth=None, passc=None, out_corrected=None, gate=0.80):
    items = _read(items_p)
    rr = {int(r['item']): r for r in _read(reread_p)}
    miss = [it['item'] for it in items if int(it['item']) not in rr]
    if miss:
        sys.exit(f'audit-score: {len(miss)} items have no re-read row, e.g. item {miss[0]}')
    T = _truthset(truth) if truth else {}
    res = collections.Counter(); fixes = {}
    for it in items:
        r = rr[int(it['item'])]
        lab, cf = r['label'].strip(), r['conf'].strip()
        flag = cf in ('H', 'M') and not lab.startswith('SPLIT') and lab != 'X_NEW' and lab != it['shown']
        if it['planted'] == '1':
            res['planted'] += 1
            res['planted_flagged'] += flag
            res['planted_caught'] += flag and lab == it['original']
            continue
        res['unplanted'] += 1; res['unplanted_flagged'] += flag
        if flag:
            fixes[(it['line'], int(it['pos']))] = lab
        t = T.get((it['line'], int(it['pos'])))
        if t and t['status'] == 'scored':
            ts = set(t['truth'].split('|'))
            right = it['original'] in ts
            key = 'right' if right else 'wrong'
            res[f'agreed_{key}'] += 1; res[f'agreed_{key}_flagged'] += flag
            if flag:
                now = lab in ts
                res['fixed'] += (not right) and now
                res['broken'] += right and not now
                res['flag_wrong_to_wrong'] += (not right) and not now
    catch = res['planted_caught'] / res['planted'] if res['planted'] else 0.0
    out = dict(res, catch=round(catch, 3), gate=gate, control='PASS' if catch >= gate else 'NON-TEST (catch below gate)')
    if res['agreed_right']:
        out['false_flag_rate'] = round(res['agreed_right_flagged'] / res['agreed_right'], 3)
    if res['fixed'] + res['broken']:
        from math import comb
        n, x = res['fixed'] + res['broken'], res['fixed']
        out['sign_test_p'] = round(sum(comb(n, i) for i in range(x, n + 1)) / 2 ** n, 4)
    if passc and out_corrected:
        rows = _norm(passc)
        with open(out_corrected, 'w') as o:
            o.write('line\tpos\tsign\n')
            for ln, pos, s in rows:
                o.write(f'{ln}\t{pos}\t{fixes.get((ln, pos), s)}\n')
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest='cmd', required=True)
    c = sp.add_parser('confusion', help='label swaps across two-reader alignments')
    c.add_argument('agreement', nargs='+'); c.add_argument('--out', required=True)
    c.add_argument('--target', action='append', default=[], help='leaf folder name counted in n_target (repeatable)')
    p = sp.add_parser('packet', help='flag tiles, cut the candidate sheet, write the value-blind prompt (ECHO-PRONE: prefer windows or --hide-passc)')
    p.add_argument('--agreement', required=True); p.add_argument('--confusion', required=True)
    p.add_argument('--passc', help='default: passC.tsv beside the agreement file')
    p.add_argument('--top', type=int, default=10); p.add_argument('--crops', default='')
    p.add_argument('--sheet', required=True); p.add_argument('--sheet-map', required=True)
    p.add_argument('--out', required=True); p.add_argument('--run')
    p.add_argument('--cell', type=int, default=110); p.add_argument('--cols', type=int, default=9)
    p.add_argument('--hide-passc', action='store_true', help='drop the passC line sequences and list candidates '
                   'alphabetically (the default prompt is ECHO-PRONE: 7/7 Sonnet re-reads copied passC, N7-VIV53L/54L)')
    r = sp.add_parser('reconcile', help='fold the re-read in by the fixed 2-of-3 rule')
    r.add_argument('--tiles', required=True); r.add_argument('--passc', required=True)
    r.add_argument('--reread', required=True); r.add_argument('--out', required=True)
    r.add_argument('--alt'); r.add_argument('--focus'); r.add_argument('--run')
    au = sp.add_parser('audit', help='re-check signs both readers agreed on, with planted known errors (TX-AGREEAUDIT; ECHO-PRONE: prefer windows --items or --hide-passc)')
    au.add_argument('--passa', required=True); au.add_argument('--passb', required=True)
    au.add_argument('--passc', required=True); au.add_argument('--confusion', required=True)
    au.add_argument('--sample', type=int, required=True); au.add_argument('--plant', type=float, default=0.05)
    au.add_argument('--seed', type=int, default=1); au.add_argument('--k', type=int, default=3)
    au.add_argument('--include', help='TSV of (line, pos) always audited, never planted')
    au.add_argument('--crops-glob', default='', help="e.g. 'harvest/*/{line}_s?.jpg'")
    au.add_argument('--sheet', required=True); au.add_argument('--sheet-map', required=True)
    au.add_argument('--out', required=True); au.add_argument('--run', default='audit')
    au.add_argument('--cell', type=int, default=110); au.add_argument('--cols', type=int, default=9)
    au.add_argument('--lines', help='regex on line ids: audit only these lines (one vision call per line group)')
    au.add_argument('--hide-passc', action='store_true', help='bracket audited positions as [n:?], not [n:label] (the '
                    'default prompt is ECHO-PRONE, N7-VIV53L/54L; planted catch then tests reading, not disagreeing)')
    w = sp.add_parser('windows', help='per-tile window montages, label hidden: the re-read instrument that did not echo')
    w.add_argument('--tiles', help='a packet <run>_tiles.tsv (re-read tiles; writes the filtered <run>_tiles.tsv for reconcile)')
    w.add_argument('--items', help='an audit <run>_audit_items.tsv (audit windows; score with audit-score as usual)')
    w.add_argument('--passc', required=True, help='the committed sequence (line/pos/sign or passage/pos/sign_id): sign counts per line')
    w.add_argument('--manifest', help='tools/iiif_lines.py manifest.json: segments stitched on their source x (box[0])')
    w.add_argument('--crop-pattern', default='*_{line}_s*', help="file-name glob of a line's segments in the manifest "
                   "(default '*_{line}_s*'; e.g. '*_f173r_{line}_s*' when line ids omit the page)")
    w.add_argument('--crops-glob', default='', help="without --manifest: 'DIR/{line}_s?.jpg', segments abutted in name order")
    w.add_argument('--out', required=True); w.add_argument('--run', help="default: the input's run + '_win' / '_audit_win'")
    w.add_argument('--status', default='split', help="tiles statuses to window, comma-separated, or 'all' (default split: "
                   "a one-reader gap has no A/B pair for the 2-of-3 rule)")
    w.add_argument('--half', type=float, default=6.5, help='window half-width in estimated sign widths (default 6.5)')
    w.add_argument('--scale', type=int, default=2, help='upscale factor (default 2)')
    w.add_argument('--per', type=int, default=6, help='windows per montage image (default 6)')
    w.add_argument('--ink', type=int, default=110, help='grey level below which a pixel is ink (default 110)')
    w.add_argument('--ink-min', type=int, default=2, help='ink pixels for a column to count as inked (default 2)')
    w.add_argument('--desc', help='candidate shape descriptions: TSV id<TAB>description, or a JSON object')
    sc = sp.add_parser('audit-score', help='score an audit re-read: planted catch gate, flags vs a truth file')
    sc.add_argument('--items', required=True); sc.add_argument('--reread', required=True)
    sc.add_argument('--truth'); sc.add_argument('--passc'); sc.add_argument('--out-corrected')
    sc.add_argument('--gate', type=float, default=0.80)
    a = ap.parse_args(argv)
    if a.cmd == 'windows':
        res = windows(a.passc, a.out, a.tiles, a.items, a.manifest, a.crops_glob, a.crop_pattern, a.run, a.status,
                      a.half, a.scale, a.per, a.ink, a.ink_min, a.desc)
        print(json.dumps(res)); return res
    if a.cmd == 'audit':
        res = audit(a.passa, a.passb, a.passc, a.confusion, a.sample, a.plant, a.seed, a.k, a.include, a.crops_glob,
                    a.sheet, a.sheet_map, a.out, a.run, a.cell, a.cols, a.lines, a.hide_passc)
        print(json.dumps(res)); return res
    if a.cmd == 'audit-score':
        res = audit_score(a.items, a.reread, a.truth, a.passc, a.out_corrected, a.gate)
        print(json.dumps(res))
        if res['control'] != 'PASS':
            sys.exit(3)
        return res
    if a.cmd == 'confusion':
        res = confusion(a.agreement, a.out, set(a.target))
    elif a.cmd == 'packet':
        passc = a.passc or os.path.join(os.path.dirname(a.agreement), 'passC.tsv')
        res = packet(a.agreement, a.confusion, passc, a.top, a.crops, a.sheet, a.sheet_map, a.out,
                     a.run or Path(a.agreement).parent.name, a.cell, a.cols, a.hide_passc)
    else:
        res = reconcile(a.tiles, a.passc, a.reread, a.out, a.alt, a.focus, a.run)
    print(json.dumps(res))
    return res


if __name__ == '__main__':
    main()
