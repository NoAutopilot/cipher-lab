#!/usr/bin/env python3
"""TXE4-1 reader prep (PREREG-txeng4-1.md 'Fixed inputs'): one scratch directory per pass, holding ONLY task.txt, the arm's
sheet copy and the 26 test crops; the task text is the committed SHEET-VIV / SHEET-VIV-C reader_task.txt with LINES_HERE,
FILECOUNT, OUTPUT_PATH and the two repository paths (sheet, crops dir) replaced by the scratch copies. The diffs against the
originals are written beside this script (task_<ARM>.diff). Arms H and Hx are not prepared: the purity gate failed.
  python3 benchmark-tx/txeng4/1/prep.py D1 W1 D2 W2
"""
import difflib, os, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
SCR = '/tmp/claude-0/-home-user-cipher-lab/418d81d6-5d23-5452-a42d-0fa425085382/scratchpad/r'
T = os.path.join(REPO, 'ciphers/fr16104-vivonne-spain-1572')
LINES = ['L%02d' % n for n in (2, 4, 8, 10, 16, 18, 20, 24, 28, 30, 32, 34, 36)]
TASK = {'D': os.path.join(REPO, 'benchmark-tx/txeng2/sheetviv/reader_task.txt'),
        'W': os.path.join(REPO, 'benchmark-tx/txeng2/sheetvivc/reader_task.txt')}
SHEET = {'D': (os.path.join(T, 'glyphs/sheet_tomokiyo_v1.png'), 'sheet_tomokiyo_v1.png'),
         'W': (os.path.join(REPO, 'benchmark-tx/txeng2/viv102base/sheet_SIGNS_dv1.md'), 'sheet_SIGNS_dv1.md')}


def prep(run):
    arm = run[:-1]
    d = os.path.join(SCR, run)
    os.makedirs(d, exist_ok=True)
    src, name = SHEET[arm]
    shutil.copy(src, os.path.join(d, name))
    for ln in LINES:
        for s in (1, 2):
            fn = f'c105_f102r_{ln}_s{s}.jpg'
            shutil.copy(os.path.join(T, 'images', fn), os.path.join(d, fn))
    orig = open(TASK[arm]).read()
    task = orig.replace(src, os.path.join(d, name))
    task = task.replace('/home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/images/', d + '/')
    task = task.replace('LINES_HERE', ' '.join(LINES)).replace('FILECOUNT', '26').replace('OUTPUT_PATH', os.path.join(d, 'read.tsv'))
    assert '/home/user/cipher-lab' not in task, 'a repository path survived'
    open(os.path.join(d, 'task.txt'), 'w').write(task)
    open(os.path.join(HERE, f'task_{run}.txt'), 'w').write(task)
    diff = ''.join(difflib.unified_diff(orig.splitlines(True), task.splitlines(True), 'reader_task.txt', f'task_{run}.txt'))
    open(os.path.join(HERE, f'task_{run}.diff'), 'w').write(diff)
    print(run, d, len(os.listdir(d)), 'files')


if __name__ == '__main__':
    for run in sys.argv[1:]:
        prep(run)
