from time import sleep
import threading


def demo(words='hello default', time=1):
    sleep(time)
    print(words)


def main():
    t1 = threading.Thread(target=demo)
    t2 = threading.Thread(target=demo, args=('aaaa',3))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    main()
    print(threading.enumerate())
    print('main执行结束')
