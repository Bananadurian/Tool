# /usr/bin/env python
import requests
import json

def get_url(url):
    headers = {User-Agent: 'Mozilla/5.0(iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
    r = requests.get(url = url,headers = headers,timeout = 30)
    if r.status_code != 200:
        raise Exception('network error:{}'.format(r.status_code))
    return json.loads(r.content)

def run():
    with open('1.txt','r') as f:
        while True:
            orderId = f.readline()
            if orderId:
                r = 'http://api.lieyou.com/api/order/testCloseOrder?orderId={}&cache=no'.format(orderId)
                print(r)
            else:
                break

if __name__=='__main__':
    run()
    
