#! /usr/bin/env python
import requests
import json
import os

class InterfaceTool:
    def __init__(self,bid,password='asd123'):
        self.bid = bid
        self.password = password
        
    def get_url(self,url):
        headers={'User-Agent':'Mozilla/5.0(iPhone;CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}
        r = requests.get(url=url,headers=headers,timeout=15)
        if r.status_code != 200:
            raise Exception('network error:{}'.format(r.status_code))
        return json.loads(r.content)
        
    def set_password(self):
        '''设置密码'''
        flag = True
        while flag:
            result = self.get_url('http://passport.lieyou.com/lieyou/sdk/create_password?cache=no&bid={}&isNew=1&password={}'.format(self.bid,self.password))
            if result['code'] == 0:
                flag = False
        print(result['msg']+'\n')
        
    def relieve_bind_device(self):
        '''清除绑定设备'''
        result = self.get_url('http://passport.lieyou.com/goplay/api/relieve_bind_device?name=ccy123&bid={}&cache=no&clearMobile=1&type=byLoginBid'.format(self.bid))
        print(result['msg']+'\n')
        
    def modify_account_type(self):
        '''修改账号类型为测试号'''
        result = self.get_url('http://api.lieyou.com/admin/account_manage/do_account_type_data?bid={}&accountType=1'.format(self.bid))
        print(result['msg']+'\n')
        
    def unbind_mobile(self):
        '''解除绑定手机'''
        result = self.get_url('http://api.lieyou.com/admin/account_manage/do_relieve_mobile_data?bid={}&relieveReason=test'.format(self.bid))
        print(result['msg']+'\n')
    

if __name__=='__main__':
    print('='*35)
    print('{:10} {}'.format('Choose','Content'))
    print('-'*35)
    print(' {:<8}  {}'.format('1','解除手机绑定'))
    print(' {:<8}  {}'.format('2','修改账号为测试号'))
    print(' {:<8}  {}'.format('3','清除账号绑定设备'))
    print(' {:<8}  {}'.format('4','设置密码(默认asd123,可选,6-8位)'))
    print(' {:<8}{}'.format('其它','回车直接退出'))
    print('-'*35)

    try:
        while True:
            temp = input('choose+bid （+password可选)：\n').split('+')
            if len(temp)==2 and temp[1].isdigit() and len(temp[1])==11:
                choose = int(temp[0])
                bid = temp[1]
                print('choose:{},bid:{}'.format(choose,bid))
                tool = InterfaceTool(bid)
                if choose == 1:
                    tool.unbind_mobile()
                elif choose == 2:
                    tool.modify_account_type()
                elif choose == 3:
                    tool.relieve_bind_device()        
                elif choose == 4:
                    tool.set_password()
                else:
                    print('选项不存在\n')
                #break
            
            elif len(temp)==3 and temp[1].isdigit() and len(temp[1])==11:
                if 6 <= len(temp[2]) <= 8:
                    tool = InterfaceTool(temp[1],temp[2])
                    tool.set_password()   
                else:
                    print('密码长度不对，请重新输入!\n')
                #break
            elif temp[0] == '':
                print('退出成功')
                break
            else:
                print('输入格式错误，请重新输入！\n')
        #os.system('exit')
    except Exception as e:
        print(e)
    
