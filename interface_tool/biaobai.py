#! /usr/bin/env python
import requests
import json
import random

class Tool:
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0(iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML,like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
    
    def login(self,login_bid):
        session = requests.session()
        r = session.get(url = 'http://api.lieyou.com/base/api/test_login?bid={}'.format(login_bid),headers = self.headers,timeout = 60 )
        if r.status_code != 200:
            raise Exception('Network Error:'.format(r.status_code))
        print('{}{}'.format(login_bid,json.loads(r.content)['msg']))
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

    def im_send_gift(self,login_bid):
        """
        IM发送礼物，login_bid=送礼bid,被送礼bid则从文件data.txt读取
        """
        session = self.login(login_bid)
        line = self.read_file()
        toBid = []
        for line in line:
            temp_toBid = line.strip()
            if temp_toBid != '' and temp_toBid.isdigit() and len(temp_toBid) == 11:
                toBid.append(temp_toBid)
        for toBid in toBid:
            url = 'http://api.lieyou.com/api/gift/send?os=2&versionCode=214&appLoginBid={}&appName=lieyou&giftId=186&giftNum=1&toBid={}&scene=1&professWordId=3'.format(login_bid,toBid)
            r = session.get(url=url,timeout = 60)
            if r.status_code != 200:
                raise Exception('Network Error:{}'.format(r.status_code))
            print('bid={} toBid={} code:{}'.format(login_bid,toBid,json.loads(r.content)['code']))


if __name__=='__main__':
    tool = Tool()
    try:
        #tool.close_order()
        tool.im_send_gift(10000248288)
        #tool.room_send_gift()
        #input('Enter Pass')
    except Exception as e:
        print(e)
        input('Enter Pass')
