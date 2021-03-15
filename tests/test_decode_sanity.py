import pytest

from objc_types_decoder.decode import decode


@pytest.mark.parametrize('encoded, decoded', [
    ('c', 'char'),
    ('i', 'int'),
    ('s', 'short'),
    ('l', 'long'),
    ('q', 'long long'),
    ('C', 'unsigned char'),
    ('I', 'unsigned int'),
    ('S', 'unsigned short'),
    ('L', 'unsigned long'),
    ('Q', 'unsigned long long'),
    ('f', 'float'),
    ('d', 'double'),
    ('B', 'BOOL'),
    ('v', 'void'),
    ('*', 'char *'),
    ('@', 'id'),
    ('#', 'Class'),
    (':', 'SEL'),
])
def test_decoding_simple_types(encoded, decoded):
    assert decode(encoded) == decoded


def test_decoding_block():
    assert decode('@?') == 'id /* block */'


@pytest.mark.parametrize('encoded, decoded', [
    ('{example=@*i}', 'struct example { id x0; char * x1; int x2; }'),
    ('{NSObject=#}', 'struct NSObject { Class x0; }'),
    ('{example=}', 'struct example { }'),
    ('{example}', 'struct example'),
    ('{?=}', 'struct { }'),
    ('{?=i}', 'struct { int x0; }'),
    ('^{tmp=I[2:]b16b16*^{__CFString}}',
     'struct tmp { unsigned int x0; SEL x1[2]; int x2 : 16; int x3 : 16; char * x4; struct __CFString * x5; } *'),
    ('^{tmp=I[2:]I}', 'struct tmp { unsigned int x0; SEL x1[2]; unsigned int x2; } *'),
    ('{bStruct={aStruct=iq@}{aStruct=iq@}}', 'struct bStruct { struct aStruct { int x0; long long x1; id x2; } x0;'
                                             ' struct aStruct { int x0; long long x1; id x2; } x1; }'),
])
def test_decoding_struct(encoded, decoded):
    assert decode(encoded) == decoded


@pytest.mark.parametrize('encoded, decoded', [
    ('^{example=@*i}', 'struct example { id x0; char * x1; int x2; } *'),
    ('^jf', 'float complex *'),
])
def test_decoding_pointer(encoded, decoded):
    assert decode(encoded) == decoded


@pytest.mark.parametrize('encoded, decoded', [
    ('jd', 'double complex'),
])
def test_decoding_complex(encoded, decoded):
    assert decode(encoded) == decoded


@pytest.mark.parametrize('encoded, decoded', [
    ('b16', 'int x : 16'),
])
def test_decoding_bitfield(encoded, decoded):
    assert decode(encoded) == decoded


@pytest.mark.parametrize('encoded, decoded', [
    ('[12^f]', 'float * x[12]'),
    ('[4]', 'void * x[4]'),
])
def test_decoding_array(encoded, decoded):
    assert decode(encoded) == decoded


@pytest.mark.parametrize('encoded, decoded', [
    ('(example=^v*i)', 'union example { void * x0; char * x1; int x2; }'),
    ('(NSObject=#)', 'union NSObject { Class x0; }'),
    ('(example=)', 'union example { }'),
    ('(example)', 'union example'),
    ('(?=)', 'union { }'),
    ('(?=i)', 'union { int x0; }'),
    ('^(tmp=I[2:]b16b16*^(Data))',
     'union tmp { unsigned int x0; SEL x1[2]; int x2 : 16; int x3 : 16; char * x4; union Data * x5; } *'),
    ('^(tmp=I[2:]I)', 'union tmp { unsigned int x0; SEL x1[2]; unsigned int x2; } *'),
    ('(bStruct={aStruct=iq@}(aStruct=iq@))', 'union bStruct { struct aStruct { int x0; long long x1; id x2; } x0;'
                                             ' union aStruct { int x0; long long x1; id x2; } x1; }'),
])
def test_decoding_union(encoded, decoded):
    assert decode(encoded) == decoded
