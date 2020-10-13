#! /usr/bin/env python
import requests
from time import strftime,localtime
import pytest
import json

def login(bid='10000706843'):
    session = requests.session()
    headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}
    r = session.get(url ='http://api.lieyou.com/base/api/test_login?bid={}'.format(bid),headers = headers,timeout=15)
    if r.status_code != 200:
        raise Exception('neterror:{}'.format(r.status_code))
    print(json.loads(r.content)['msg'])
    return session

def get_url(url):
    session = login()
    r = session.get(url=url,timeout=15)
    return json.loads(r.content)

def run():
    r = get_url('http://api.lieyou.com/api/blog/hotspot_category_recommendation_list?lng=113.371476&os=1&appName=lieyou&appver=3.0.3&socialityTags=0&versionCode=79&queueMark=0&appLoginBid=10000706843&packageChannel=offical&page=1&lat=23.123186&categoryId=1')
    result = []
    for i in range(len(r['data']['blogList'])):
        try:
            temp =  r['data']['blogList'][i]['user']['isHunter']
            result.append(str(temp))
        except KeyError:pass
    return result

def value():
    pa = run()
    return pa

@pytest.mark.parametrize('ishunter',value())
def test_one(ishunter):
    assert ishunter == '0'

if __name__=='__main__':
    file_name = strftime('%y%m%d%H%M%S',localtime())
    pytest.main(['requests_demo.py','-q','-s','--html={}.html'.format(file_name)])
    #print(run())
