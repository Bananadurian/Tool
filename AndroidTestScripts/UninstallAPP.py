#! /usr/bin/env python
import sys
from utils import get_device_state,uninstall_apk

"""
可通过运行带参数卸载指定apk
如： python *.py com.lieyou.feiteng 
"""
get_device_state()    
if len(sys.argv)==2:
    uninstall_apk(sys.argv[1])
else:
    uninstall_apk()

if __name__=='__main__':
    input('Enter Pass')
