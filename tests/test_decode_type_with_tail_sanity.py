import pytest

from objc_types_decoder.decode import decode_with_tail


@pytest.mark.parametrize('encoded, decoded, tail', [
    ('labcd', 'long', 'abcd'),
    ('{?=i},hey you', 'struct { int x0; }', ',hey you'),
    ('(?=i),hey you', 'union { int x0; }', ',hey you'),
    ('[4^f]| Baby just say yes!', 'float * x[4]', '| Baby just say yes!'),
])
def test_with_tail(encoded, decoded, tail):
    assert decode_with_tail(encoded) == (decoded, tail)


@pytest.mark.parametrize('encoded, decoded', [
    ('l', 'long'),
    ('{?=i}', 'struct { int x0; }'),
    ('(?=i)', 'union { int x0; }'),
    ('[4^f]', 'float * x[4]'),
])
def test_without_tail(encoded, decoded):
    assert decode_with_tail(encoded) == (decoded, '')
