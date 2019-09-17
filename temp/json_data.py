#! /usr/bin/env python
'''
json.dumps() 编码
json.loads() 解码

json.dump() 读取文件编码
json.load() 读取文件解码
'''
import json
data = {'a':1,'b':2}
print('data:',data)
print('data to json:',json.dumps(data))
json1 = json.dumps(data)
print('json to data:',json.loads(json1))


