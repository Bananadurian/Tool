#! /usr/bin/env python
import requests
import json

headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}
url = 'http://api.lieyou.com/api/sociality/macthing/get_macthing_list?'
params = 'appLoginBid=10014298374&packageChannel=google_play&os=1&appName=lieyou&appver=3.0.0&page=1&versionCode=75'
cookies = {'UM_distinctid':'16a85ae9e011e5-0c0cbef4f76835-39395704-15f900-16a85ae9e0226d' \
           ,'lieyouAdminMenu':'1' \
           ,'s':'1' \
           ,'n':'%E6%B5%8B%E8%AF%95%E8%B4%A6%E5%8F%B7' \
           ,'b':'10014298374' \
           ,'t':'1568283263' \
           ,'at':'80f8a33ed04a59be30440a3c297358ce'}

r = requests.get(url=url,headers=headers,params=params,cookies=cookies)

print(r.status_code)
#print(r.content)
print(json.loads(r.content))

