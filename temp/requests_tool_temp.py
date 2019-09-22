#! /usr/bin/env python
import requests
import json

headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}
url = 'http://api.lieyou.com/api/sociality/macthing/get_macthing_list?'
params = 'appLoginBid=10000248288&packageChannel=offical&os=1&appName=lieyou&appver=3.0.0&page=1&versionCode=75'
cookies = {'UM_distinctid':'16a85ae9e011e5-0c0cbef4f76835-39395704-15f900-16a85ae9e0226d' \
           ,'lieyouAdminMenu':'1' \
           ,'s':'1' \
           ,'n':'%E6%B5%8B%E8%AF%95%E8%B4%A6%E5%8F%B7' \
           ,'b':'10000248288' \
           ,'t':'1568715742' \
           ,'at':'222f8695d5d7d3d216782316d3a65c52'}

#r = requests.get(url=url,headers=headers,params=params,cookies=cookies)

#print(r.status_code)
#temp = r.content.decode('utf-8')
#text = json.loads(r.content)

'''
f = open('result.txt','w')
json.dump(text,f,sort_keys=True,indent=4,ensure_ascii=False)
f.close()
'''

cookie = 'BAIDUID=7FA8A784B7459D6D70CF4851AEA4E11B:FG1; BIDUPSID=7FA8A784B7459D6D70CF4851AEA4E11B; PSTM=1561262054; BD_UPN=12314753; BDUSS=jJGYVpNRTFPeWFLLVFSTlEzR2pJZENZY2dkMHBjcnFsRzlyTElZQ2hGWnpYVGhkSVFBQUFBJCQAAAAAAAAAAAEAAADsVCkwy63R1M73t-cAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHPQEF1z0BBde; __cfduid=d8e5b6013efe85524c90c1c2cb4dcd2f51563616414; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; BD_CK_SAM=1; BD_HOME=1; yjs_js_security_passport=63e9b8fbcff981cc572619969768ec3eb36d9834_1569139026_js; BDPASSGATE=IlPT2AEptyoA_yiU4V_J3kIN8enzUvW4Af4ESEpTQlePdCyWmhHWAb-IXjLOUZm8AiTM-Y3fo_-zd5fCQjpfjKMThgMAfztqfFe6xqe25aTvL_NgzbIZCbDJOFkpzPXqav26z4wh1wRW4C9vfOHJpuo4ivKl73JQb4rc6VL2a_zXAlqR2WmJxlmEOolmO-0APNu594rXnEpZKS_1WfHyRi8ybVciEHwL-d_cjLIN2gLu6iUkQQ0tXBYfAGrG2yp3XQinGPa0xKao2-IwrpMoVkIP-UiVfuy; H_WISE_SIDS=126126_136262_132921_136550_134725_136244_128063_135687_125580_120166_136610_136366_132911_131246_132378_131517_118891_118876_118855_118826_118803_107317_136431_136091_135910_133351_135482_129654_136193_132250_124632_128967_135307_135813_133847_132552_135432_135874_134047_134752_129645_131423_135473_134600_133191_110085_134149_127969_131755_131951_135671_136415_135458_128196_135036_132467_134844_134353_136077; COOKIE_SESSION=0_0_0_0_0_0_0_0_0_0_0_0_0_1569148131%7C1%230_0_0_0_0_0_0_0_1569148131%7C1; lsv=globalTjs_3048728-globalTcss_5cbd11d-wwwTcss_1a9246b-searchboxless_366db37-globalBcss_aad48cc-sugcss_465b32a-wwwBcss_777000e-framejs_c9ac861-atomentryjs_0b0c978-globalBjs_1731240-sugjs_9addd63-wwwjs_983dd45-searchboxjs_ede4863; SE_LAUNCH=5%3A26152468; MSA_WH=375_812; MSA_PBT=146; MSA_ZOOM=1056; locale=zh; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1569148140; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1569148140; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1569148141; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1569148141; wpr=0; FC_MODEL=-1_0_1_0_0_1_0_6.77_1_0_0_-1_0_0_0_0_1_1569149818625_1569148131751%7C1%230_-1_-1_0_0_1569149818625_1569148131751%7C1; PSINO=6; H_PS_PSSID=29634_1463_21087_18559_20697_29523_29721_29567_29221_22157; BDSVRTM=0; WWW_ST=1569161923545'

cookie_temp = {i.split('=')[0]:i.split('=')[1] for i in cookie.split(';')   }
print (cookie_temp)













