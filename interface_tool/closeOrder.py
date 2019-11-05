#! /usr/bin/env python
import requests
import json

def get_url(url):
    headers = {'User-Agent':'Mozilla/5.0(iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
    r = requests.get(url = url,headers = headers,timeout = 30)
    if r.status_code != 200:
        raise Exception('network error:{}'.format(r.status_code))
    return json.loads(r.content)

def read_file():
    with open('1.txt') as f:
        temp = []
        id = f.readlines()
        for id in id:
            temp.append(id.strip('\n'))
        orderId = []
        for temp in temp:
            if temp != '':
                orderId.append(temp.strip())
    return orderId

def run():
    orderId = read_file()
    for orderId in orderId:
        url = 
        result = get_url(url)
        print('orderId:{} result:{}'.format(orderId,result['msg']))


if __name__=='__main__':
    try:
        a = read_file()
        print(a)
    except Exception as e:
        print(e)
        input('Enter Pass')
