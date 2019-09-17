import os
import sys
import android_adb_tool as adb
"""
可通过运行带参数卸载指定apk
如： python *.py com.lieyou.feiteng 
"""
adb.get_device_state()    
if len(sys.argv)==2:
    adb.uninstall_apk(sys.argv[1])
else:
    adb.uninstall_apk()

if __name__=='__main__':
    input('Enter Pass')
