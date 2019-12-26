#! /usr/bin/env python 
import requests
import json
from time import localtime,strftime,sleep

def login(bid):
    session = requests.session()
    headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML,like Gecko)Version/10.0 Mobile/14E304 Safari/602.1'}
    url = 'http://api.lieyou.com/base/api/test_login?bid={}'.format(bid)
    res = session.get(url = url,headers = headers)
    if res.status_code != 200:
        raise Exception('Network Error:'.format(res.status_code))
    print(json.loads(res.content)['msg'])
    return session

def get_url(url):
    headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML,like Gecko)Version/10.0 Mobile/14E304 Safari/602.1'}
    cookies = {'UM_distinctid':'16a85ae9e011e5-0c0cbef4f76835-39395704-15f900-16a85ae9e0226d' \
              ,'lieyouAdminMenu':'1' \
              ,'s':'1' \
              ,'n':'%E6%B5%8B%E8%AF%95%E8%B4%A6%E5%8F%B7' \
              ,'b':'10000248288' \
              ,'t':'1568715742' \
              ,'at':'222f8695d5d7d3d216782316d3a65c52'}
    res = requests.get(url = url,headers = headers,cookies = cookies)
    if res.status_code != 200:
        raise Exception('Network Error')
    return json.loads(res.content)
    
def session_get_url(session,url):
    res = session.get(url)
    if res.status_code != 200:
        raise Exception('Network Error')
    return json.loads(res.content)

def main(pageNum,login_bid):
    queueMark = 0
    session = login(login_bid)
    for page in range(1,pageNum+1):
        #游记热门标签url,可以修改分类id获取不同的分类
        hot_category_url = 'http://api.lieyou.com/api/blog/hotspot_category_recommendation_list?os=1&socialityTags=0&versionCode=91\
        &appLoginBid={}&page={}&queueMark={}&categoryId=30'.format(login_bid,page,queueMark)
        #话题热门，可修改话题ID
        hot_topic_url = 'http://api.lieyou.com/api/topic/get_topic_blog_list?versionCode=91&os=1&topicType=0&pageSize=20\
        &appLoginBid={}&page={}&queueMark={}&topicId=72'.format(login_bid,page,queueMark)
        #猎人秀，可修改游戏ID
        lierenxiu_url = 'http://api.lieyou.com/api/blog/hotspot_category_recommendation_list?versionCode=91&os=1&socialityTags=0&categoryId=38\
        &appLoginBid={}&page={}&queueMark={}&gameId=1'.format(login_bid,page,queueMark)
        
        #res = get_url(url)
        res = session_get_url(session,hot_category_url)
        #res = session_get_url(session,hot_topic_url)
        #res = session_get_url(session,lierenxiu_url)

        queueMark = res['data']['queueMark']
        try:
            for i in range(len(res['data']['blogList'])):
                nickname = res['data']['blogList'][i]['user']['nickname']
                #ishunter = res['data']['blogList'][i]['user']['isHunter']
                bid = res['data']['blogList'][i]['user']['bid']
                did = res['data']['blogList'][i]['blog']['did']
                createtime =strftime('%Y-%m-%d %H:%M:%S',localtime(res['data']['blogList'][i]['blog']['createTime']))
                #assert ishunter == 0,'存在猎人'
                temp = 'page={:<3}id={:<3}{:^11d}{:^14d}{:^22s}{}'.format(page,i,did,bid,createtime,nickname)
                #print(temp)
                f.write(temp+'\n')
        except Exception: pass
        sleep(1)
        
if __name__=='__main__':
    try:
        f = open('{}.txt'.format(strftime('%Y%m%d%H%M%S',localtime())),'a',encoding='utf-8')
        date = strftime('%Y%m%d%H%M%S',localtime())
        print(date)
        main(10,10017370853)
    except Exception as e:
        print(e)
    finally:
        f.close()
