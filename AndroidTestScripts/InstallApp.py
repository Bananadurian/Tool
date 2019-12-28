#! /usr/bin/env python
import os
from utils import get_device_state, install_apk

def get_apk_path():
    '''
    获取指定文件夹最新的修改的apk文件路径

    '''
    file_dir = r'C:\Users\Administrator\Downloads'
    file_create_time = 0
    for temp_path in os.listdir(file_dir):
        file_path = os.path.join(file_dir,temp_path)
        if os.path.isfile(file_path) and os.path.splitext(file_path)[1] == '.apk':
            if os.path.getmtime(file_path) > file_create_time:
                file_create_time = os.path.getmtime(file_path)
                apk_file_path = file_path
    #print('apk_file_path:',apk_file_path)
    return apk_file_path

if __name__=='__main__':
    get_device_state()     
    install_apk(get_apk_path())
    #get_apk_path()
    input('Enter Pass')
