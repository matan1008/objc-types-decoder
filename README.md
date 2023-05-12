# objc-types-decoder

[![Python application](https://github.com/matan1008/objc-types-decoder/workflows/Python%20application/badge.svg)](https://github.com/matan1008/objc-types-decoder/actions/workflows/python-app.yml "Python application action")
[![Pypi version](https://img.shields.io/pypi/v/objc-types-decoder.svg)](https://pypi.org/project/objc-types-decoder/ "PyPi package")
[![Downloads](https://static.pepy.tech/personalized-badge/objc-types-decoder?period=total&units=none&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/objc-types-decoder)


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

