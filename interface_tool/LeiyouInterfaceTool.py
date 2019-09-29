#! /usr/bin/env python
import requests
import json
class InterfaceTool:
    def __init__(self,bid):
        self.bid = bid
        self.password = 'asd123'
        
    def get_url(self,url):
        headers={'User-Agent':'Mozilla/5.0(iPhone;CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}
        r = requests.get(url=url,headers=headers)
        if r.status_code != 200:
            raise Exception('network error:{}'.format(r.status_code))
        return json.loads(r.content)
        
    def set_password(self):
        '''设置密码'''
        #temp = input('bid,password(英文逗号分隔):')
        #bid = temp.split(',')[0]
        flag = True
        while flag:
            result = self.get_url('http://passport.lieyou.com/lieyou/sdk/create_password?cache=no&bid={}&isNew=1&password={}'.format(self.bid,self.password))
            if result['code'] == 0:
                flag = False
        print(result['msg'])
        
    def relieve_bind_device(self):
        '''清除绑定设备'''
        result = self.get_url('http://passport.lieyou.com/goplay/api/relieve_bind_device?name=ccy123&bid={}&cache=no&clearMobile=1&type=byLoginBid'.format(self.bid))
        print(result['msg'])
        
    def modify_account_type(self):
        '''修改账号类型为测试号'''
        result = self.get_url('http://api.lieyou.com/admin/account_manage/do_account_type_data?bid={}&accountType=1'.format(self.bid))
        print(result['msg'])
        
    def unbind_mobile(self):
        '''解除绑定手机'''
        result = self.get_url('http://api.lieyou.com/admin/account_manage/do_relieve_mobile_data?bid={}&relieveReason=test'.format(self.bid))
        print(result['msg'])
    

if __name__=='__main__':
    try:
        print(' 1.解除绑定手机\n 2.修改账号为测试号\n 3.清除账号设备绑定\n 4.设置密码(asd123)\n')
        temp = input('bid+choose：\n')
        bid = temp.split('+')[1]
        choose = int(temp.split('+')[0])
        print('bid:{},choose:{}'.format(bid,choose))
        tool = InterfaceTool(bid)
        if choose == 1:
            tool.unbind_mobile()
        elif choose == 2:
            tool.modify_account_type()
        elif choose == 3:
            tool.relieve_bind_device()
        else:
            tool.set_password()

        input('Enter Pass')
    except Exception as error:
        print(error)
    
