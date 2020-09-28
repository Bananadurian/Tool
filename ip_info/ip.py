import requests
import json
import csv
"""
ip判断调用的是第三方接口
接口：http://ip-api.com/json/153.120.0.0?lang=zh-CN
@qjf
20200928
"""


def ip_info(ip_address):
    url = 'http://ip-api.com/json/{}?lang=zh-CN'.format(ip_address)
    r = requests.get(url=url)
    data = json.loads(r.content)
    ip_info = '{} {} {}'.format(data['country'], data['regionName'], data['city'])
    return ip_info


def ip_info1(ip_address):
    url = 'https://www.matools.com/ip'
    data = {'inputIP': ip_address}
    r = requests.post(url=url, data=data)
    data = json.loads(r.content)
    ip_info = '{:<25}{}'.format(data['ip'], data['adr'])
    return ip_info


def local_txt_ip_info():
    with open('ip.txt') as f:
        ip_list = []
        while True:
            ip = f.readline()
            if not ip:
                break
            ip_list.append(ip.strip())
        # print(ip_list)
    for ip in ip_list:
        info = ip_info1(ip)
        print(info)


def local_csv_ip_info():
    with open('ip1.csv') as f:
        data = csv.reader(f)
        ip_list = list(data)
        for ip in ip_list[1:]:
            info = ip_info1(ip)
            print(info)


def main():
    ip = '153.120.0.0'
    # print(ip_info1(ip))
    # local_txt_ip_info()
    local_csv_ip_info()


if __name__ == '__main__':
    main()

