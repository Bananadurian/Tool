import sys
import os
import android_adb_tool as adb
'清空APP缓存，默认猎游APP'

adb.get_device_state()
if len(sys.argv)==2:
    adb.clear_app_cache(sys.argv[1])
else:
    adb.clear_app_cache()

if __name__=='__main__':
    input('Enter Pass')
