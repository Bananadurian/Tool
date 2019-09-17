import os,re


def log_static(txtPath):
        keyName = {
              #preview&capture
              "APORTRAIT_Refocus Preview, end cost time":0,
               }

        print "*"*10 + txt + "*"*10
        
        tp = open(txtPath,"r").readlines()

        for key in keyName.keys():
            count = 0
            count1 = 0
            key_max,key_min =0,10000
            for line in tp:
                if key in line:
                    count = count +1
                    try:
                        value = float(re.search("time:([0-9]*)",line).group(1))
                    except:
                        value = float(re.search("time ([0-9]*)ms",line).group(1))
                    if (value >= 5): 
                     
                     count1 = count1 + 1 
                     if value > key_max:
                        key_max = value
                     elif value < key_min and value <> 0:
                        key_min = value
                     keyName[key]=keyName[key]+value

            if count ==0:
                print key,"\tNone"
            else:
                print "%s: \t average: %.2f\t max: %d\t min: %d\t"%(key,keyName[key]/float(count1),key_max,key_min)
            
        print "\n\n"

if __name__=="__main__":

    log_path = r"E:"

    if os.path.isfile(log_path):
        try:
            log_static(log_path,)
        except :
            print "Can't process the file:%s"%log_path
    else:
        for txt in os.listdir(log_path):
            if  not txt[-3:] == "txt":
                continue
            log_static(os.path.join(log_path,txt))




