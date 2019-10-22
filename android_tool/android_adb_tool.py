#! /usr/bin/env python
import os
import re
import subprocess

'''
os.system('adb devices') #os.system是不支持读取操作的
out = os.popen('adb --version').read() #os.popen支持读取操作,返回一个文件操作对象
print(out)
'''
def package_name(key):
    name=['com.feiteng.lieyou']
    return name[key]

def adb(command):
    '调用cmd,输入命令'
    f = os.popen(command)
    result = f.read()
    f.close()
    return result

def apk_path():
    path=input('please input apk file path:\n')
    return path

def get_device_state():
    '获取设备状态'
    #os.system('adb wait-for-device')
    temp = re.compile(r'\w*').findall(adb('adb get-state'))
    if temp[0] == "device":
        pass
    else:
        print('Check your device drive (Re-Plug?)')
        os.system('adb wait-for-device')

def get_appname_or_activity(key):
    '获取当前活动APP的包名和Aciviy,key==0 AppName，key==1 Activity'
    #regex = re.compile(r'[a-zA-Z0-9\.]+/[a-zA-Z0-9\.]+')
    try:
        result = adb('adb shell dumpsys window | findstr mCurrentFocus')
        re = re.compile(r'(com.*)/(.*)}')
        temp = re.findall(result)
    except Exception:
        result = adb('adb shell dumpsys window w |findstr \/ |findstr name=')
        re = re.compile(r'(com.*)/(.*)\)')
        temp = re.findall(result)
    if len(temp)==0:
        print('No AppName or Activity found')
    else:
        return temp[0][key]

def install_apk():
    print('Installing...')
    print(adb('adb install -r '+apk_path))

def uninstall_apk(AppName='com.feiteng.lieyou'):
    print('Uninstalling...')
    print(adb('adb uninstall {}'.format(AppName)))  

def screencap(file_name='screen'):
    print('is talking a screenshot...')
    adb('adb shell screencap -p /sdcard/{}.png'.format(file_name))
    adb('adb pull /sdcard/{}.png C:\\Users\\Administrator\\Desktop'.format(file_name))
    adb('adb shell rm /sdcard/{}.png'.format(file_name))

def screen_record(time='10'):
    print('screen recording...')
    adb('adb shell screenrecord --time-limit {} /sdcard/demo.mp4'.format(time))
    """
    --time-limit 时长参数，默认180s，自定义10s: --time-limit 10
    --size       分辨率参数，默认屏幕尺寸，自定义: --size 1280*720
    --bit-rate   比特率参数，默认4Mbps,自定义6Mbps: --bit-rate 6000000 
    """
    adb('adb pull /sdcard/demo.mp4 C:\\Users\\Administrator\\Desktop')
    adb('adb shell rm /sdcard/demo.mp4')
       
def clear_app_cache(AppName='com.feiteng.lieyou'):
    adb('adb shell pm clear {}'.format(AppName))

def main():
    pass
    
if __name__=='__main__':
    get_device_state()
    print(get_appname_or_activity())

