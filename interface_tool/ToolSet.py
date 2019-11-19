#! /usr/bin/env python
import requests
import json

class Tool:
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0(iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML,like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
    
    def login(self,login_bid):
        session = requests.session()
        r = session.get(url = 'http://api.lieyou.com/base/api/test_login?bid={}'.format(login_bid),headers = self.headers,timeout = 60 )
        if r.status_code != 200:
            raise Exception('Network Error:'.format(r.status_code))
        print(json.loads(r.content)['msg'])
        return session

    def get_url(self,url):
        r = requests.get(url = url,headers = self.headers,timeout = 60)
        if r.status_code != 200:
            raise Exception('Network Error:{}'.format(r.status_code))
        return json.loads(r.content)
    
    def read_file(self):
        with open('1.txt') as f:
            data = f.readlines()
        return data

    def close_order(self):
        line = self.read_file()
        orderId = []
        for line in line:
            temp_id = line.strip()
            if temp_id != '' and temp_id.isdigit() and len(temp_id) == 7:
                orderId.append(temp_id)
        for orderId in orderId:
            url = 'http://api.lieyou.com/api/order/testCloseOrder?orderId={}&cache=no'.format(orderId)
            result = self.get_url(url)
            print('orderId:{} {}'.format(orderId,result['msg']))

    def im_send_gift(self,login_bid):
        session = self.login(login_bid)
        line = self.read_file()
        toBid = []
        for line in line:
            temp_toBid = line.strip()
            if temp_toBid != '' and temp_toBid.isdigit() and len(temp_toBid) == 11:
                toBid.append(temp_toBid)
        for toBid in toBid:
            url = 'http://api.lieyou.com/api/gift/send?os=1&appName=lieyou&appver=3.2.0&giftType=1&roomId=0&versionCode=85&scene=1&giftId=51&appLoginBid={}&packageChannel=offical&toBid={}&giftNum=10'.format(login_bid,toBid)
            r = session.get(url=url,timeout = 60)
            if r.status_code != 200:
                raise Exception('Network Error:{}'.format(r.status_code))
            print('toBid:{} code:{}'.format(toBid,json.loads(r.content)['code']))

    def room_send_gift(self,login_bid):
        session = self.login(login_bid)
        line = self.read_file()
        toBid = []
        for line in line:
            temp_toBid = line.strip()
            if temp_toBid != '' and temp_toBid.isdigit() and len(temp_toBid) == 11:
                toBid.append(temp_toBid)
        for toBid in toBid:
            url = 'http://api.lieyou.com/api/voice_room/send_gift?os=1&appName=lieyou&appver=3.2.0&giftType=1&signStr=7d2f29a6f1e675d01574168333&roomId=11513&versionCode=85&giftId=51&appLoginBid=10000200342&packageChannel=offical&toBid=%5B%2210000248288%22%5D&giftNum=10&sendType=2&time=1574168333'
            r = session.get(url=url,timeout = 60)
            if r.status_code != 200:
                raise Exception('Network Error:{}'.format(r.status_code))
            print('toBid:{} code:{}'.format(toBid,json.loads(r.content)['code']))

if __name__=='__main__':
    tool = Tool()
    try:
        tool.im_send_gift(10000248288)
        input('Enter Pass')
    except Exception as e:
        print(e)
        input('Enter Pass')
