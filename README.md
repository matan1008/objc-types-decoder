# objc-types-decoder

[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/matan1008/objc-types-decoder.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/matan1008/objc-types-decoder/context:python)


A type decoder for Objective-C types.

It translates the encoded Objective-C type notation, the notation that the `@encode` function returns, into a readable
form that tries to be as close as possible to the original type definition.

For example, lets look at the following `@encode`:

```objective-c
NSLog(@"%s", @encode(float **)); // "^^f" will be printed.
```

Using our decoder, we can "reverse" the process:

```python
from objc_types_decoder.decode import decode

print(decode('^^f'))  # 'float * *' will be printed.
```

## Installation

In order to install this package, just use a regular `pip` installation:

```shell
pip install objc_types_decoder
```

## Usage

In order to use the decoder, just run the main with your desired encoded type:

```shell
>> py -m objc_types_decoder ^f
float *
```

You can also decode by importing it in your python code:

```python
>> from objc_types_decoder.decode import decode
>> decode('{NSObject=#}')
'struct NSObject { Class x0; }'
```

Sometimes, you might want to keep the tail of the parsed data. For this case, you can use `decode_with_tail`.

```python
>> from objc_types_decoder.decode import decode_with_tail
>> decode_with_tail('fyour boat')
('float', 'your boat')
```

