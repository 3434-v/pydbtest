
import requests
import re,json,os
import random
import time
from apscheduler.schedulers.background import BlockingScheduler
import traceback
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
log = log_treatment()

class Deal(object):

    def __init__(self,url,fs_data,js_data,money,password):

        self.url = url
        self.fs_data = fs_data
        self.js_data = js_data
        self.money = money
        self.password = password

    def account_unlockAccount(self):
        try:
            for fs_index in self.fs_data:
                payload = '{"jsonrpc":"2.0","method":"account_unlockAccount","params":["'+fs_index+'","'+self.password+'"],"id":3}'
                response = requests.post(self.url,data=payload,headers=header)
                response.raise_for_status()

        except Exception as ero:
            log.log_text(str(ero.args))

    def account_deals(self,):
        self.account_unlockAccount()
        try:
            for fs_index in self.fs_data:
                for js_index in self.js_data:
                    payload = '{"jsonrpc":"2.0","method":"account_transfer","params":["'+fs_index+'","'+js_index+'","'+hex(self.money)+'","0x110","0x300000",""],"id":3}'
                    response = requests.post(self.url,data=payload,headers=header)
                    response.raise_for_status()
                    print(response.text)

        except Exception as ero:
            log.log_text(str(ero.args))


if __name__ == "__main__":

    url = 'http://39.98.39.224:35645'
    fs_data = ['0xd6e1b15eDDd2e93FE48e62583FD32C22044e7B6f']
    js_data = ['0xd3EE25DB3F3eb7b266c347f97504f442ADb91846']
    money = 100
    password = '1234567'
    run = Deal(url,fs_data,js_data,money,password)
    run.account_deals()
    scheduler = BlockingScheduler()
    scheduler.add_job(run.account_deals, 'interval',max_instances=10, seconds=10)
    try:
        scheduler.start()
    except:
        pass