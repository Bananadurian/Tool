#! /usr/bin/env python
import os
import re
import subprocess

'''
os.system('adb devices') #os.system是不支持读取操作的
out = os.popen('adb --version').read() #os.popen支持读取操作
print(out)
'''
def package_name(key):
    name=['com.feiteng.lieyou']
    return name[key]

def execmd(cmd):
    '调用cmd,输入命令'
    f=os.popen(cmd)
    text=f.read()
    f.close()
    return text

def apk_path():
    path=input('please input apk file path:\n')
    return path

def get_device_state():
    '获取设备状态'
    #os.system('adb wait-for-device')
    temp1 = re.compile(r'\w*').findall(execmd('adb get-state'))
    if temp1[0] == "device":
        pass
    else:
        print('Check your device drive (Re-Plug?)')
        os.system('adb wait-for-device')

def get_appname_or_activity(key):
    '获取当前活动APP的包名和Aciviy,key==0 AppName，key==1 Activity'
    #regex = re.compile(r'[a-zA-Z0-9\.]+/[a-zA-Z0-9\.]+')
    try:
        result1 = execmd('adb shell dumpsys window | findstr mCurrentFocus')
        regex = re.compile(r'(com.*)/(.*)}')
        temp = regex.findall(result1)
    except Exception:
        result2 = execmd('adb shell dumpsys window w |findstr \/ |findstr name=')
        regex = re.compile(r'(com.*)/(.*)\)')
        temp = regex.findall(result2)
    if len(temp)==0:
        print('No AppName or Activity found')
    else:
        return temp[0][key]

def install_apk():
    cmd = 'adb install -r '+apk_path()
    print('Installing...')
    print(execmd(cmd))

def uninstall_apk(AppName='com.feiteng.lieyou'):
    # cmd = 'adb uninstall '+package_name(0)
    cmd = 'adb uninstall {}'
    print('Uninstalling...')
    print(execmd(cmd.format(AppName)))  

def screencap(file_name='screen'):
    print('is talking a screenshot...')
    execmd('adb shell screencap -p /sdcard/{}.png'.format(file_name))
    execmd('adb pull /sdcard/{}.png C:\\Users\\Administrator\\Desktop'.format(file_name))
    execmd('adb shell rm /sdcard/{}.png'.format(file_name))

def screen_record(time='10'):
    print('screen recording...')
    execmd('adb shell screenrecord --time-limit {} /sdcard/demo.mp4'.format(time))
    """
    --time-limit 时长参数，默认180s，自定义10s: --time-limit 10
    --size       分辨率参数，默认屏幕尺寸，自定义: --size 1280*720
    --bit-rate   比特率参数，默认4Mbps,自定义6Mbps: --bit-rate 6000000 
    """
    execmd('adb pull /sdcard/demo.mp4 C:\\Users\\Administrator\\Desktop')
    execmd('adb shell rm /sdcard/demo.mp4')
       
def clear_app_cache(AppName='com.feiteng.lieyou'):
    execmd('adb shell pm clear {}'.format(AppName))

def main():
    a=1
    
if __name__=='__main__':
    get_device_state()
    screen_record()

