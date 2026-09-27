from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse,json,subprocess

D=Path(__file__).resolve().parent
B=D.parent/'codex-2026-09-27b'
exe=Path('/tmp/armstrong_variant_solver')
ap=argparse.ArgumentParser();ap.add_argument('stage',choices=['controls','target']);a=ap.parse_args()
subprocess.run(['g++','-O3','-std=c++17',str(D/'variant_solver.cpp'),'-o',str(exe)],check=True)
(D/'results').mkdir(exist_ok=True)
def solve(name,mode,prior=None):
    cmd=[str(exe),str(D/'lm.bin'),f'{name}.seq',f'{name}.alt',mode,'1000','90000',
         '.3',str(202609274 if name=='control4' else 202609275 if name=='control5' else 202609276),f'results/{name}-{mode}.tsv']
    if prior:cmd.append(str(prior))
    subprocess.run(cmd,cwd=D,check=True)
def control(seed):
    name=f'control{seed}';solve(name,'hard');solve(name,'soft',D/f'results/{name}-hard.tsv')
if a.stage=='controls':
    with ThreadPoolExecutor(max_workers=2) as ex:list(ex.map(control,[4,5]))
    subprocess.run(['python',str(D/'evaluate.py')],cwd=D,check=True)
else:
    gate=json.loads((D/'control_results.json').read_text())
    assert gate['target_gate_passed'], 'Known-answer error-correction gate failed'
    solve('target','soft',B/'glyph_strong.tsv')
