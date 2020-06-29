
import requests
import re,json,os,sys
import random
import time
from apscheduler.schedulers.background import BlockingScheduler
import traceback
import contextlib
header = {
			'Content-Type': "application/json",
			'cache-control': "no-cache",
			'Postman-Token': "27a29181-18f4-4549-80c2-d23196a7df15"
		}

#日志处理类
class log_treatment(object):

    #获取错误时间、返回路径
    def false_time(self):

        falsetime = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        path = os.path.abspath(__file__)
        paths = os.path.split(path)
        log_name =paths[0] +  "\\"+falsetime + '.log'
        print(log_name)
        return log_name
    
    #创建错误文件
    def log_text(self,text):

        self.path = self.false_time()
        self.filename = text
        with open(self.path,'a+') as log:
            log.write(text)
            log.write('\n')
        log.close()

class Deal(log_treatment):

    def __init__(self):
        self.fs_data = ''
        self.js_data = ''
        self.url = ''
        self.password = ''

    #重启
    def Reset_Python(self):
        print('reset--->python')
        python = sys.executable
        os.execl(python,python,*sys.argv)

    #随机函数
    def RangeMoney(self):
        money = random.randint(1,101) * (10 ** 18)
        return money

    #解锁账号
    def account_unlockAccount(self):
        try:
            for fs_index in self.fs_data:
                payload = '{"jsonrpc":"2.0","method":"account_unlockAccount","params":["'+fs_index+'","'+self.password+'"],"id":3}'
                response = requests.post(self.url,data=payload,headers=header)
                response.raise_for_status()
                # print(response.text)

        except Exception as ero:
            self.log_text(str(ero.args))

    #发送交易
    def account_deals(self):
        self.read_site()
        self.account_unlockAccount()
        money = self.RangeMoney()
        try:
            for fs_index in self.fs_data:
                for js_index in self.js_data:
                    payload = '{"jsonrpc":"2.0","method":"account_transfer","params":["'+fs_index+'","'+js_index+'","'+hex(money)+'","0x110","0x300000",""],"id":3}'
                    response = requests.post(self.url,data=payload,headers=header)
                    print(payload)
                    response.raise_for_status()
                    print(response.text)

        except Exception as ero:
            self.log_text(str(ero.args))
            # print(ero.args)
    
    def read_site(self):

        with open('message.json','r',encoding='utf8') as msg:
            msg_dict = json.load(msg)
        msg.close()
        self.fs_data = msg_dict['fs_data']
        self.js_data = msg_dict['js_data']
        self.url = msg_dict['url']
        self.password = msg_dict['password']
        # print(msg_dict)

if __name__ == "__main__":

    run = Deal()
    # run.account_deals()
    scheduler = BlockingScheduler()
    scheduler.add_job(run.account_deals, 'interval', seconds=5)
    try:
        scheduler.start()
    except:
        run.Reset_Python()