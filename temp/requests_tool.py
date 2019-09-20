#! /usr/bin/env python
import requests
import json

class RequestsGetUrl:
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) Ap    pleWebKit/60    3.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}
        self.cookies = {'UM_distinctid':'16a85ae9e011e5-0c0cbef4f76835-39395704-15f900-16a85ae9e0    226d' \
              ,'lieyouAdminMenu':'1' \
              ,'s':'1' \
              ,'n':'%E6%B5%8B%E8%AF%95%E8%B4%A6%E5%8F%B7' \
              ,'b':'10000248288' \
              ,'t':'1568715742' \
              ,'at':'222f8695d5d7d3d216782316d3a65c52'}
                
        self.url_temp = 'http://api.lieyou.com/api/blog/hotspot_category_recommendation_list?gameId=&appLoginBid=10000248288&packageChannel=offical&os=1&appName=lieyou&appver=3.0.0&socialityTags=0&categoryId=38&versionCode=75&page={}'
        self.queueMark = '&queueMark=0'
    def get_url_list(self,page_num):
        return [self.url_temp.format(i) for i in range(1,page_num+1)]
    
    def parse_url(self,url):
        r = requests.get(url,headers = self.headers,cookies = self.cookies)
        print(r.status_code)
        return json.loads(r.content)

    def save_file(self,content):
        with open('res.txt','a',encoding='utf-8') as f:
            f.write(content+'\n')

    def run(self,times):
        #构造url
        for url_list_temp in self.get_url_list(times):
            url = url_list_temp + self.queueMark
            res = self.parse_url(url)
            self.queueMark = '&queueMark={}'.format(res['data']['queueMark'])
            for i in range(len(res['data']['blogList'])):
                temp = res['data']['blogList'][i]['user']['nickname']
                self.save_file(temp)

class SessionGetUrl:
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) Ap    pleWebKit/60    3.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}
    def parse_url(self,url):
        session = requests.session()
        r = session.get(url,headers = self.headers)
        return json.loads(r.content)
    def run(self):
        '''
        login_result = self.parse_url('http://api.lieyou.com/base/api/test_login?bid=10000247871')   #login
        print(login_result['msg'])
        res = self.parse_url('http://api-cloud.lieyou.com/api/home/my_home?appLoginBid=10000247871&packageChannel=offical&os=1&appName=lieyou&appver=3.0.0&bid=10000247871&versionCode=75')
        print(res['msg'])
        '''
        session = requests.session()
        login_result = session.get('http://api.lieyou.com/base/api/test_login?bid=10000247871',headers= self.headers)   #login
        print(json.loads(login_result.content)['msg'])
        res = session.get('http://api-cloud.lieyou.com/api/home/my_home?appLoginBid=10000247871&packageChannel=offical&os=1&appName=lieyou&appver=3.0.0&bid=10000247871&versionCode=75',headers= self.headers)
        print(json.loads(res.content)['msg'])

        
if __name__=='__main__':
    #result = RequestsGetUrl()
    #result.run(3)
    result = SessionGetUrl()
    result.run()
