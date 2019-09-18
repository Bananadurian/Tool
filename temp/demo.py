#! /usr/bin/env python
import requests
import json

headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/60    3.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}

cookies = {'UM_distinctid':'16a85ae9e011e5-0c0cbef4f76835-39395704-15f900-16a85ae9e0226d' \
              ,'lieyouAdminMenu':'1' \
              ,'s':'1' \
              ,'n':'%E6%B5%8B%E8%AF%95%E8%B4%A6%E5%8F%B7' \
              ,'b':'10000248288' \
              ,'t':'1568715742' \
              ,'at':'222f8695d5d7d3d216782316d3a65c52'}

url = 'http://api.lieyou.com/api/blog/hotspot_category_recommendation_list?'
params = 'gameId=&appLoginBid=10000248288&packageChannel=offical&os=1&appName=lieyou&appver=3.0.0&socialityTags=0&categoryId=38&versionCode=75'
queueMark = '&queueMark=0'

for page_num in range(1,5):
    page = '&page={}'.format(page_num)
    params = params+page+queueMark
    #print(params)

    r = requests.get(url=url,headers=headers,cookies=cookies,params=params)
    print('Status code=',r.status_code)
    result = json.loads(r.content)
    
    for i in range(len(result['data']['blogList'])):
        #print(result['data']['blogList'][i]['user']['nickname'])
        text = str(result['data']['blogList'][0]['user']['bid']) +':'+ result['data']['blogList'][i]['user']['nickname']
        print(text)

        f = open('result1.txt','a')
        f.write(text+'\n')
        f.close()
        
    queueMark = '&queueMark={}'.format(result['data']['queueMark'])
    print(queueMark)
