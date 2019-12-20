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
    with open('data.txt') as f:
        orderId = []
        line = f.readlines()
        for line in line:
            temp_id = line.strip()
            if temp_id != '' and temp_id.isdigit() and len(temp_id)==7:
                orderId.append(temp_id)
    return orderId

def run():
    orderId = read_file()
    for orderId in orderId:
        url = 'http://api.lieyou.com/api/order/testCloseOrder?orderId={}&cache=no'.format(orderId)
        result = get_url(url)
        print('orderId:{} result:{}'.format(orderId,result['msg']))


if __name__=='__main__':
    try:
        run()
        input('Enter Pass')
    except Exception as e:
        print(e)
        input('Enter Pass')
