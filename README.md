# objc-types-decoder

A type decoder for Objective-C types.

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

