#!/usr/bin/env python3
"""Offline test for tools/key_design.py's keys_decode loader option (EST-REG, 14 Oct 2026).
Catches: a DECODE key sheet named <record>_key.tsv under ciphers/<t>/keys_decode/ (not seen by key_crossmatch's
key*.tsv glob); series-marked codes (20, 20=bar) kept apart; a kind=null row with no plaintext counted as a null;
two signs given the same description both kept. Must NOT change: a table without both 'series' and 'kind' columns keeps an empty value
empty and a repeated code overwritten as before; a keys_decode file not ending _key.tsv is not picked up.
Synthetic files in a temporary directory only; no network."""
import sys
import tempfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))
import key_design as kd  # noqa: E402

fails = 0


def check(name, cond):
    global fails
    print(('PASS ' if cond else 'FAIL ') + name)
    fails += not cond


with tempfile.TemporaryDirectory() as d:
    root = Path(d)
    kdir = root / 'ciphers' / 'demo-1645' / 'keys_decode'
    kdir.mkdir(parents=True)
    rows = ['code\tseries\tplaintext\tkind\tgrade',
            '20\tplain\tLe Pape\tnomenclator\tH', '20=bar\tbar\tEspagne\tnomenclator\tH',
            '20=dot\tdot\tEspagnols\tnomenclator\tH', '14\tplain\t\tnull\tH', '49\tplain\t\tblank\tH',
            'b crossed\tsign\tb\tletter\tH', 'b crossed\tsign\th\tletter\tH']
    f = kdir / '9999_key.tsv'
    f.write_text('\n'.join(rows) + '\n', encoding='utf-8')
    (kdir / 'listing_9999.tsv').write_text('record\tstatus\n9999\tN/A\n', encoding='utf-8')
    found = kd.extra_design_files([], root=root)
    check(f'keys_decode/*_key.tsv discovered, listing not ({[p.name for p in found]})',
          [p.name for p in found] == ['9999_key.tsv'])
    check('already-found file not listed twice', kd.extra_design_files([f], root=root) == [])
    key, why = kd.load_table(f)
    check(f'series-marked codes kept apart ({sorted(key) if key else why})',
          key and key['20'] == 'Le Pape' and key['20=bar'] == 'Espagne' and key['20=dot'] == 'Espagnols')
    check('kind=null with empty plaintext reads as a null', key['14'] == 'null')
    check('kind=blank stays empty', key['49'] == '')
    check('repeated sign description keeps both rows', key.get('b crossed') == 'b' and key.get('b crossed#2') == 'h')
    sig = kd.signature(key)
    check(f"signature counts the declared null ({sig['nulls_declared']})", sig['nulls_declared'] == 1)

    plain = root / 'key_plain.tsv'
    plain.write_text('code\tplaintext\n14\t\n31\tque\n31\tqui\n', encoding='utf-8')
    k2, _ = kd.load_table(plain)
    check(f'no kind column: empty stays empty, repeat overwrites as before ({k2})',
          k2 == {'14': '', '31': 'qui'})
    kindonly = root / 'key_kind.tsv'
    kindonly.write_text('code\tplaintext\tkind\n14\t\tnull\n31\tque\tword\n31\tqui\tword\n', encoding='utf-8')
    k3, _ = kd.load_table(kindonly)
    check(f'kind column without series: old reading kept ({k3})', k3 == {'14': '', '31': 'qui'})

print('ALL PASS' if not fails else f'{fails} FAIL')
sys.exit(1 if fails else 0)
