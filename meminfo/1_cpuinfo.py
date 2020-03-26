import os
from openpyxl import Workbook

"""
def adb(command):
    f =  os.popen(command)  # os.popen 返回一个文件操作对象
    res = f.read()
    f.close()
    return res
"""

def read_file():
    """
    读取dump数据
    """
    with open('2.txt') as f:
        data_list = []
        while True:  
            line = f.readline()
            if not line:
                break
            content = line.split()  # 已空格划分，生成列表
            try:
                if len(content) == 12:
                    del content[0]  # 删除第一个元素
                else:
                    del content[:2]
                content.pop()  # 删除最后一个元素
            except IndexError:
                pass
            if content:
                #print(content)
                data_list.append(content)
        return data_list

def save_report():
    """
    生成excel表格
    """
    wb = Workbook()
    ws = wb.active
    rows = read_file()
    title = ['USER','PR','NI','VIRT','RES','SHR','S','%CPU','%MEM','TIME+']
    ws.append(title)
    for row in rows:
        ws.append(row)
    wb.save('1.xlsx')

def main():
    save_report()

if __name__ == '__main__':
    main()
