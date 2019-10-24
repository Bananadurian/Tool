#import os
import sys
import android_adb_tool as adb
'''
截图文件名可以通过运行py的时候带参数修改，默认为sceen
如：python *.py sceen1
'''
adb.get_device_state()
if len(sys.argv)==2:
    adb.screencap(sys.argv[1])
else:
    adb.screencap()

if __name__=='__main__':
    input('Enter Pass')
