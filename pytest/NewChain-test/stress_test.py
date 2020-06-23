import requests
from locust import HttpLocust,TaskSet,task,wait_time,between
import os
import re,json
import random

class deal(TaskSet):

    header = {
			'Content-Type': "application/json",
			'cache-control': "no-cache",
			'Postman-Token': "27a29181-18f4-4549-80c2-d23196a7df15"
		}
 
    @task(1)
    def deals(self):
        url = 'http://39.98.39.224:35645'
        money = 100 * (10**18)
        fs_data = ['0x1A61B43d6e53954735dd300D5090599A17F8E4db']
        js_data = ['0x07332150A19Bc85E0416b19F2F6ee255BA34126B','0x14aF424238BD4eA60C356c967D5709AB3f8224ed']
        for fs_index in fs_data:
            for js_index in js_data:
                payload = '{"jsonrpc":"2.0","method":"account_transfer","params":["'+fs_index+'","'+js_index+'","'+hex(money)+'","0x110","0x300000",""],"id":3}'
                with self.client.post(url,data=payload,headers=self.header,catch_response=True) as response:
                    response.failure(response.text)

             
class websitUser(HttpLocust):

    task_set = deal
    # min_wait = 3000  # 单位为毫秒
    # max_wait = 6000  # 单位为毫秒
    wait_time = between(3, 6)



        