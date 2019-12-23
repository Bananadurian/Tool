import requests
import json
from time import localtime,strftime

def login(bid):
    seesion = requests.session()
    headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML,like Gecko)Version/10.0 Mobile/14E304 Safari/602.1'}
    url = 'http://api.lieyou.com/base/api/test_login?bid={}'.format(bid)
    res = session.get(url = url,headers = headers)
    if res.status_code != 200:
        raise Exception('Network Error:'.format(res.status_code))
    print(json.loads(res.content)['msg'])
    return session

def get_url(url):
    headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML,like Gecko)Version/10.0 Mobile/14E304 Safari/602.1'}
    cookies = {'UM_distinctid':'16a85ae9e011e5-0c0cbef4f76835-39395704-15f900-16a85ae9e0    226d' \
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
    
def main():
    url = 'http://api.lieyou.com/api/blog/hotspot_category_recommendation_list?lng=113.371506&os=1&appName=lieyou&appver=3.0.0&socialityTags=0&versionCode=78&appLoginBid=10000248288&packageChannel=offical&page=1&lat=23.123453&categoryId=23&queueMark=0'
    res = get_url(url)
    f = open('{}.txt'.format(strftime('%y%m%d%H%M%S',localtime())),'a',encoding='utf-8')
    try:
        for i in range(len(res['data']['blogList'])):
            nickname = res['data']['blogList'][i]['user']['nickname']
            ishunter = res['data']['blogList'][i]['user']['isHunter']
            bid = res['data']['blogList'][i]['user']['bid']
            did = res['data']['blogList'][i]['blog']['did']
            #assert ishunter == 0,'存在猎人'
            temp = 'id={:>2}, ishunter={}, {:10d} {:12d}, {}'.format(i,ishunter,did,bid,nickname)
            print(temp)
            f.write(temp+'\n')
    except Exception: pass
    finally:
        f.close()

if __name__=='__main__':
    try:
        date = strftime('%y%m%d%H%M%S',localtime())
        print(date)
        main()
    except Exception as e:
        print(e)
