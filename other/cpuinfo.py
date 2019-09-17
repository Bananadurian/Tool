import os
import time

CMD = "cmd.exe /c {0}"
resultTxt = open('result.txt','a+')

while True:
    TIME = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    resultTxt.write(TIME+':    ')
    cpuinfo = os.popen(CMD.format('adb shell cat sys/devices/system/cpu/present'))
    #print cpuinfo
    result= cpuinfo.readline().strip()
    resultTxt.write('cpu:'+result+'    ')

    for i in range(int(result[-1])+1):
        frequence = os.popen(CMD.format('adb shell cat sys/devices/system/cpu/cpu%s/cpufreq/scaling_cur_freq'%i)).readline().strip()
        output = " %s"%(frequence)
        print (output)

    print ("\n")
        #resultTxt.write(output+'    ')
    #resultTxt.write('\n')
   # resultTxt.flush()
        
