#! /usr/bin/env python
import requests
from time import strftime,localtime
import pytest
import json

def login(bid='10000000342'):
    session = requests.session()
    headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}
    r = session.get(url ='http://api.lieyou.com/base/api/test_login?bid={}'.format(bid),headers = headers,timeout=15)
    #print(type(json.loads(r.content)))
    #print(r.status_code)
    if r.status_code != 200:
        raise Exception('neterror:{}'.format(r.status_code))
    print(json.loads(r.content)['msg'])
    return session

def get_url(url):
    session = login()
    r = session.get(url=url,timeout=15)
    return json.loads(r.content)

def run():
    r = get_url('http://api.lieyou.com/api/home/home_idols_list_v2?appLoginBid=10000000342&packageChannel=offical&os=1&appName=lieyou&appver=3.0.3&page=1&bid=10000000342&versionCode=79')
    print(r)

if __name__=='__main__':
    run()
