import requests
import json,re,time
import time,datetime

robot_token = 'https://oapi.dingtalk.com/robot/send?access_token=064485b9bb99053b9dbfc077e9fe41079a0d2ed34c333f409d6e2c76311daf04'

header = {
            "Content-Type": "application/json",
            "Charset": "UTF-8"
        }

class DD_robot(object):

    def __init__(self,types):
        self.types = types
        # pass

    def __call__(self,func):
        def wrapper(*args,**kwargs):
            
            message =  '/:' + func(*args,**kwargs)
            text_data = {
                "msgtype": "text",
                "text": {"content": message},
                "at": {
                "atMobiles": ["18770185021"], 
                "isAtAll": True
                }
            }

            sendData = json.dumps(text_data) 
            sendData = sendData.encode("utf-8")  
            time.sleep(1)
            response = requests.post(robot_token, data=sendData, headers=header)
            # 将请求发回的数据构建成为文件格式
            print(response.text)


        return wrapper

# data = '111'

def remind(content):
    data = '1'
    @DD_robot(data)
    def post_message():
        message = content
        return message
    post_message()
    # return post_message

remind("jenkins")