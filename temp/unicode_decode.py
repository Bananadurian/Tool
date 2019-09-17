#! /usr/bin/env python
#方法a encode之后再decode
a = '\u6c42\u6210\u529f'.encode('utf-8').decode('utf-8')
#方法b 直接打印
b = '\u6c42\u6210\u529f'
print(type(a))
print(a)
print('b:',b)

