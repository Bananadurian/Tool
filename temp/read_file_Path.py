#! /usr/bin/env python
import os

"""
获取指定文件路径下的所有文件名
"""

file_path = r'C:\Users\Administrator\Downloads\InstallApp'
for root,dirs,files in os.walk(file_path):
    print(root)
    print(dirs)
    print(files)

