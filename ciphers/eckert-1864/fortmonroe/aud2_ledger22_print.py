#!/usr/bin/env python3
"""AUD2-LEDGER-22 (9 Oct 2026, account 4): phrase grep for E291/E292 (eckert-1864) over four IA djvu texts fetched once to SCRATCH_DIR
(warofrebellion363unit = OR I/36 pt 3; warofrebellion432unit = OR I/43 pt 2; warofrebellion422unit = OR I/42 pt 2; warofrebellion421unit =
OR I/42 pt 1). Usage: aud2_ledger22_print.py SCRATCH_DIR > aud2_ledger22_print.out. A miss is a search result (rule 10), not a novelty verdict."""
import os, re, sys
P = {
 'warofrebellion363unit': [r'Bickford', r'Caldwell', r'Coldwell', r'card', r'Eckert'],
 'warofrebellion432unit': [r'M\. ?R\. Morgan', r'Colonel Morgan', r'Coggins', r'herd', r'Harper.s Ferry, (Va|W)\.?.{0,30}September 16'],
 'warofrebellion422unit': [r'Coggins', r'2,486', r'1,200 head', r'M\. ?P\. Small', r'Colonel Small', r'Thomas Wilson', r'Colonel Wilson'],
 'warofrebellion421unit': [r'2,486', r'Coggins', r'Thomas Wilson', r'cattle'],
}
for vol, pats in P.items():
    t = re.sub(r'\s+', ' ', open(os.path.join(sys.argv[1], vol + '.txt'), errors='ignore').read())
    for p in pats:
        ms = list(re.finditer(p, t, re.I))
        print(f'## {vol}\t{p}\t{len(ms)}')
        for m in ms[:8]:
            print('   ', t[max(0, m.start() - 220):m.end() + 220])
