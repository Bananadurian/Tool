#! /usr/bin/env python
import os

"""
获取指定文件路径下的所有文件名
"""

#os.walk 模块
file_path = r'C:\Users\Administrator\Downloads\InstallApp'
def oswalk(path):
    for root,dirs,files in os.walk(file_path):
        print('root:',root)  #获取当前目录路径
        print('dirs:',dirs)  #获取当前路径子目录
        print('files:',files) #获取当前路径非子目录文件


def listdir(path):
    for files in os.listdir(path):
        print(files)
        #print(type(files))
        #file_path = os.path.join(path,files)
        if os.path.isfile(file_path):
            print('file_path:',file_path)
        
        if os.path.isdir(file_path):
            print('file_path:',file_path)
        '''
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path,list_name)
        else:
            list_name.append(file_path)
        '''
listdir(file_path)
