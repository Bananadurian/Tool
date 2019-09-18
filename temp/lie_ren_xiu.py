#! /usr/bin/env python
import requests
import json

headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}
url = 'http://api.lieyou.com/api/blog/hotspot_category_recommendation_list?'
params = 'queueMark=0&gameId=&appLoginBid=10000248288&packageChannel=offical&os=1&appName=lieyou&appver=3.0.0&page=1&socialityTags=0&categoryId=38&versionCode=75'
cookies = {'UM_distinctid':'16a85ae9e011e5-0c0cbef4f76835-39395704-15f900-16a85ae9e0226d' \
           ,'lieyouAdminMenu':'1' \
           ,'s':'1' \
           ,'n':'%E6%B5%8B%E8%AF%95%E8%B4%A6%E5%8F%B7' \
           ,'b':'10000248288' \
           ,'t':'1568715742' \
           ,'at':'222f8695d5d7d3d216782316d3a65c52'}

r = requests.get(url=url,headers=headers,params=params,cookies=cookies)

print(r.status_code)
#temp = r.content.decode('utf-8')
#print(type(text))
text = json.loads(r.content)
print(text['data']['blogList'][0]['user']['nickname'])
print(text['data']['queueMark'])









'''
for i in range(len(text['data']['list'])):
    print(text['data']['list'][i]['user']['isHunter'])
    assert text['data']['list'][i]['user']['isHunter'] == 0,'false'
'''
'''
f = open('result.txt','w',encoding='utf-8')
json.dump(text,f,sort_keys=True,indent=4,ensure_ascii=False)
f.close()
'''
