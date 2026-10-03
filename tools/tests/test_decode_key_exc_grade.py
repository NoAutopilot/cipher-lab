"""Offline test: decode_key.grade_tokens keeps an exception's own grade on a low-confidence sign only when
decode.json sets exception_grade_overrides_conf (3 Oct 2026, BIR-OPEN)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import decode_key as d


def run(job):
    recs = [dict(kind='sign', folio='f1', line='L1', pos='1', sign='T1', conf='M', raw='T1', gloss=''),
            dict(kind='sign', folio='f1', line='L1', pos='2', sign='T1', conf='M', raw='T1', gloss='')]
    key = {'T1': dict(value='a', grade=None, source='', note='')}
    exc = {('f1', 'L1', '1'): ('e', 'S')}
    return [r['grade'] for r in d.grade_tokens(recs, key, exc, None, job)]


def test_default_downgrades():
    assert run({}) == ['M', 'M']


def test_override_keeps_exception_grade_only():
    assert run({'exception_grade_overrides_conf': True}) == ['S', 'M']


if __name__ == '__main__':
    test_default_downgrades(); test_override_keeps_exception_grade_only(); print('ok')
