"""RUN2-NXTB reconciliation step 1 (4 Oct 2026): settle the systematic c516 splits by rule, before any decode.
Two kinds of rule, applied identically to both blind passes (passA.tsv, passB.tsv -> passA_rules.tsv, passB_rules.tsv):
 TABLE: a shape the worker matched to one cell of Tomokiyo's table image by looking at crops c516b_L01/L08 beside it
        (row 1 under each letter: n1 = swash 'zp', p1 = cursive 4, r1 = crossed triple bar, t1 = alpha/fish,
        u1 = omega-hook; row 2: p2 = epsilon, n2 = A-crossed, r2 = e-loop; o2 = pi-like, o3 = phi; 'de' = 8; z1 = 10)
        or a label convention already ruled by NX-RECUT (cup-on-stem = s2, loop-S = e3, cross-topped box = W:roy).
 CLASS: two descriptions of one unnamed shape merged into one class token X:<name> (no table cell claimed).
Every token a rule touched is grade M; no token is graded H by a rule. q1 -> n1 and W:par -> p1 are global rulings
(the readers used them for the swash zp and the cursive 4); a genuine q1 or crossed-box 'par' would be mislabelled -- M."""
import re, sys
RULES = [  # (regex on the bare token without trailing '?', label, kind)
    (r'\?\{8\}', 'W:de', 'TABLE'), (r'W:de', 'W:de', 'TABLE'),
    (r'\?\{(psi|psi-cup|bar-psi)\}', 's2', 'TABLE'),
    (r'\?\{(H-hash|hash3|III|3-bar-hash|H-bar|hash-bar)\}', 'r1', 'TABLE'),
    (r'\?\{small-hash\}', 'o1/e2', 'TABLE'),
    (r'q1', 'n1', 'TABLE'), (r'W:par', 'p1', 'TABLE'), (r'\?\{4-bar\}', 'p1', 'TABLE'),
    (r'\?\{(S|S-hook|s-hook|S-tail|f-S|fs-swash|omega-S|bar-S|3-S|S-cross)\}', 'e3', 'TABLE'),
    (r'\?\{(alpha|alpha-tail|d-alpha|alpha-hook|alpha-bar)\}', 't1', 'TABLE'),
    (r'\?\{(omega-hook|o-hook|circle-hook|omega|angle-omega)\}', 'u1', 'TABLE'),
    (r'\?\{(A|A-caret|A-bar)\}', 'n2', 'TABLE'),
    (r'\?\{(pi|bar-pi)\}', 'o2', 'TABLE'), (r'\?\{(box-cross)\}', 'W:roy', 'TABLE'),
    (r'\?\{(inf|inf-dash)\}', 'l1', 'TABLE'), (r'\?\{e-loop\}', 'r2', 'TABLE'),
    (r'\?\{(phi-tail|q-loop)\}', 'o3', 'TABLE'), (r'\?\{10\}', 'z1', 'TABLE'),
    (r'\?\{(2\+|2-cross)\}', 'X:2+', 'CLASS'), (r'\?\{2\+o\}', 'X:2+o', 'CLASS'),
    (r'\?\{(h-flag|h-bar|pi-bar|h-y|Ч|Ч-tail)\}', 'X:hbar', 'CLASS'),
    (r'\?\{(bar-gamma|L-bar-hook|Gamma|Gamma-bar|L-hook|L-bar|corner-hook|gamma-hook)\}', 'X:Lhook', 'CLASS'),
    (r'\?\{(Y-hook|Y-open|y-loop|tilde-y)\}', 'X:Yhook', 'CLASS'),
    (r'\?\{(theta-ticks)\}', 'X:theta-ticks', 'CLASS'),
]
def rule(tok):
    bare = tok.rstrip('?') if not tok.startswith('?{') else tok
    for rx, lab, kind in RULES:
        if re.fullmatch(rx, bare): return lab + '?', kind     # trailing ? keeps every ruled token below H
    return tok, None
for p in ('A', 'B'):
    out = open(f'pass{p}_rules.tsv', 'w'); n = 0
    out.write('# RUN2-NXTB pass %s after recon_rules.py (rule-touched tokens carry ?)\n' % p)
    for line in open(f'pass{p}.tsv'):
        if line.startswith('#') or not line.strip(): continue
        lid, toks = line.rstrip('\n').split('\t')
        new = []
        for t in toks.split():
            r, k = rule(t); n += k is not None; new.append(r)
        out.write(lid + '\t' + ' '.join(new) + '\n')
    print(p, 'tokens ruled', n)
