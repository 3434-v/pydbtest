import requests
import json
import re
import datetime
import time


def DD_robot(details: str) -> str:
    robot_url = 'https://oapi.dingtalk.com/robot/send?'
    robot_token = robot_url + 'access_token=e3b164110ecbe8fb57099cbe4f8d22b8fde03b71d8ba985e6b81eeca1ab6b726'
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    message = '~:' + details
    text_data = {
        "msgtype": "text",
        "text": {"content": message},
        "at": {
            "atMobiles": ["18770185021"],
            "isAtAll": True
        }
    }

    senddatas = json.dumps(text_data)
    senddata = senddatas.encode("utf-8")
    response = requests.post(robot_token, data=senddata, headers=header)
    # 将请求发回的数据构建成为文件格式
    return str(response.text)


def WX_robot(detail: str) -> str:
    count = 0
    header = {
        'Host': 'service.weiyoubot.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'Content-Length': '76',
        'Origin': 'http://weiyouzhushou.cn',
        'Connection': 'keep-alive',
        'Referer': 'http://weiyouzhushou.cn/',
    }
    url_header = 'https://service.weiyoubot.cn/wyzs/api/v1/login/wy?'
    url = url_header + 'ac=18770185021&res=1536*864&brv=firefox_74.0&pn=web&platform=pc_web&nt=other'
    name = '16621573385'
    password = '31e81e792f81d74e1c05035c8b85e014db7963d6'
    data = {"name": name, "password": password}
    response = requests.post(url, json=data, headers=header)
    bottoken = ' '.join(re.findall('"access_token": "(.*?)"', str(response.text)))
    if bottoken != ' ':
        count = count + 1
    header = {
        'Host': 'service-ipad.weiyoubot.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'Content-Length': '230',
        'Origin': 'http://weiyouzhushou.cn',
        'Connection': 'keep-alive',
        'Referer': 'http://weiyouzhushou.cn/mainpage.html?action=mass_message',
    }
    message, token = detail, bottoken
    times = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    timearray = time.strptime(times, "%Y-%m-%d %H:%M:%S")
    timestamp = int(time.mktime(timearray))
    data = {
        "access_token": token,
        "data": {"trigger": {"timestamp": timestamp},
                 "resp": [{"content": message, "type": "text"}],
                 "title": message, "at_all": 1,
                 "groups": [{"gid": "5e96b54f021522257bd1ed69"}], "grouping": []}
    }
    url = 'https://service-ipad.weiyoubot.cn/wyzs/api/v1/ipad/massmessage/save'
    response = requests.post(url, json=data, headers=header)
    mmid = ' '.join(re.findall('"mmid": "(.*?)"', str(response.text)))
    if mmid != ' ':
        count = count + 1
    header = {
        'Host': 'service-ipad.weiyoubot.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'Content-Length': '94',
        'Origin': 'http://weiyouzhushou.cn',
        'Connection': 'keep-alive',
        'Referer': 'http://weiyouzhushou.cn/mainpage.html?action=mass_message',
    }
    url = 'https://service-ipad.weiyoubot.cn/wyzs/api/v1/ipad/massmessage/delete'
    data = {"access_token": token, "mmid": mmid, "type": 1}
    time.sleep(5)
    response = requests.post(url, json=data, headers=header)
    msg = ' '.join(re.findall('"msg": "delete (.*?) ok!"', str(response.text)))
    if msg == id:
        count = count + 1
    return str(count)
