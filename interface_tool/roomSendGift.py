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
        with open('data.txt') as f:
            data = f.readlines()
        return data

    def room_send_gift(self):
        """
        语音房间送礼,送礼bid固定，被送礼bid=10000248288，房间11513，礼物=甜心，数量=10
        """
        bid = ['10000200342','10000248282','10000247871']
        login_bid=bid[0]
        session = self.login(login_bid)
        url = 'http://api.lieyou.com/api/voice_room/send_gift?os=1&appName=lieyou&appver=3.2.0&giftType=1&signStr=7d2f29a6f1e675d01574168333&roomId=11513&versionCode=85&giftId=51&appLoginBid=10000200342&packageChannel=offical&toBid=%5B%2210000248288%22%5D&giftNum=10&sendType=2&time=1574168333'
        r = session.get(url=url,timeout = 60)
        if r.status_code != 200:
            raise Exception('Network Error:{}'.format(r.status_code))
        print('bid={} toBid=10000248288 {} starValue=2000'.format(login_bid,json.loads(r.content)['msg']))

if __name__=='__main__':
    tool = Tool()
    try:
        tool.room_send_gift()
        input('Enter Pass')
    except Exception as e:
        print(e)
        input('Enter Pass')
