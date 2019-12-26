#! /usr/bin/env python
import os
from time import strftime,localtime

print('Ctrl+C停止')
file_name = strftime('%y%m%d%H%M%S',localtime())
os.system('adb wait-for-device')
os.system('adb logcat -c')
os.system(r'adb logcat >C:\Users\Administrator\Desktop\{}.txt'.format(file_name))

