import sys
from android_adb_tool import get_device_state, clear_app_cache
'清空APP缓存，默认猎游APP'

get_device_state()
if len(sys.argv)==2:
    clear_app_cache(sys.argv[1])
else:
    clear_app_cache()

if __name__=='__main__':
    input('Enter Pass')
