import os
import re

def cmdexe(cmd):
    f = os.popen(cmd)
    result = f.read()
    f.close()
    return result

if __name__=='__main__':
    print(' 1.设备型号\n 2.当前链接设备\n 3.系统版本\n 4.屏幕分辨率\n 5.设备CPU\n \
6.设备序列号\n')
    os.system('adb wait-for-device')
    flag = 1
    while flag:
        choose = input('Choose:')
        if choose == '1':
            print(cmdexe('adb shell getprop ro.product.model'))
        elif choose == '2':
            print(cmdexe('adb get-serialno'))
        elif choose == '3':
            print(cmdexe('adb shell getprop ro.build.version.release'))
        elif choose == '4':
            print(cmdexe('adb shell wm size'))
        elif choose == '5':
            print(cmdexe('adb shell cat /proc/cpuinfo'))
        elif choose == '6':
            result = cmdexe('adb shell service call iphonesubinfo 1')
            regex = re.compile(r'\'([\d.]+)')
            temp = regex.findall(result)
            temp1=''.join(temp)
            regex1 = re.compile(r'[^.]+')
            imel = regex1.findall(temp1)
            print(''.join(imel))
        else:
            break
