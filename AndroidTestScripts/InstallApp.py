#! /usr/bin/env python
import os
import re
from utils import get_device_state, install_apk
from time import sleep

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
    result = install_apk(get_apk_path())    
    if re.search('success',result):
        for i in range(5,0,-1)
            print(' {}s后自动退出'.format(i), end = '')
            print('\b'*16, end = '', flush = True)
            sleep(1)
        # 可使用 os._exit() sys.exit() 退出
    else:
        input('Enter Pass')
