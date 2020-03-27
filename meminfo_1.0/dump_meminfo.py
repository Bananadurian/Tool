import os


def get_device_state():
    """
    获取设备状态
    """
    with os.popen('adb get-state') as f:
        res = f.read()
        if res.strip() == "device":
            pass
        else:
            print('Check your device drive (Re-Plug?)')
            os.system('adb wait-for-device')


def get_pid():
    """
    通过包名获取对应的pid
    """

    package_name = input('please input package_name:\n')
    command = 'adb shell ps | findstr {}'.format(package_name)
    pid = 0
    with os.popen(command) as f:
        data = f.readline()
        if package_name in data:
            pid = data.split()[1]
            print('pid=',pid)
        
        else:
            print("Didn't find '{}' pid".format(package_name))
        
    return pid


def dump_meminfo(pid):
    print('Ctrl+C停止')
    os.system('adb shell top -q -p {} > dump_meminfo.txt'.format(pid))


def main():
    get_device_state()
    pid = get_pid()
    if pid != 0:
        dump_meminfo(pid)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print('Dump meminfo stopped!')



