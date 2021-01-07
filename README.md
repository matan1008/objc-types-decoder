# objc-types-decoder
A type decoder for Objective-C types.

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

