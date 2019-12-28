#! /usr/bin/env python
import os

"""
获取指定文件路径下的所有文件名
"""
# os.path.getmtime() 获取文件最后修改时间
# os.path.getctime() 获取文件最后创建时间
# os.path.join 拼接文件路径
# os.path.isfile 判断是否是文件
# os.path.isdir 判断是否是路径
# os.path.splitext()  将路径拆分为文件名+扩展名

# os.walk 模块
file_path = r'C:\Users\Administrator\Downloads'
def oswalk(path):
    for root,dirs,files in os.walk(file_path):
        print('root:',root)  # 获取当前目录路径
        print('dirs:',dirs)  # 获取当前路径子目录
        print('files:',files)  # 获取当前路径非子目录文件

# os.listdir 模块
def listdir(path):
    file_time = 0
    for files in os.listdir(path):
        #print(files)
        #print(type(files))
        file_path = os.path.join(path,files)  # os.path.join 拼接文件路径
        #print('caifen:',os.path.splitext(file_path))
        if os.path.isfile(file_path) and os.path.splitext(file_path)[1] == '.apk':  # os.path.isfile 判断是否是文件 os.path.splitext 判断是否是apk安装包
            print('file_path:',file_path)
            print(os.path.getmtime(file_path))
            file_time_temp = os.path.getmtime(file_path)
            if file_time_temp > file_time:
                file_time = file_time_temp
                file_name = file_path
    print('file_name:',file_name)
            #list_name.append(file_path)
    #print(list_name)     
        #if os.path.isdir(file_path):   # os.path.isdir 判断是否是路径
        #    print('file_path1:',file_path)
        

                
'''
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path,list_name)
        else:
            list_name.append(file_path)
'''
listdir(file_path)
