import requests
import re
import json
import sqlitesave as save
import pymysqlsave as mysave
import hashlib
import time
import random


# 公共reques请求函数
def deamds(url: str, data: dict) -> dict:
    # loads()：将json数据转化成dict数据
    # dumps()：将dict数据转化成json数据
    # load()：读取json文件数据，转成dict数据
    # dump()：将dict数据转化成json数据后写入json文件
    # time.sleep(1)
    data = json.dumps(data)
    data_json = json.loads(data)
    data_json["language"] = 'zh_CN'
    data_str = json.dumps(data_json)
    response = requests.get(url + data_str)
    print(url + data_str)
    print(response.text)
    return json.loads(str(response.text))


# sql格式转换函数
def formatting(message: list) -> str:
    msg = ''.join([msg for msg_tuple in message if len(message) != 0 for msg in msg_tuple])
    return msg


# mysql_dict格式转换函数
def mysqldict(message: list, parameter: str) -> str:
    if len(message) == 0:
        print('未查询到数据')
    else:
        print(message[0][parameter])

        return message[0][parameter]


# 账号生成
def randomname(types: str) -> str:
    # 1手机、2邮箱
    msg = {True: 1, False: 0}[types == '1']
    index = random.randint(100, 9999999)
    name = '166' + str(index)
    if msg:
        return name
    else:
        return name + '@test.com'


# 获取当前时间
def currenttime():
    falsetime = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
    return falsetime


# 读取deploy.json文件中配置的环境
def context() -> str:
    with open('deploy.json', 'r', encoding='utf8') as depl:
        depl_dict = json.load(depl)
    depl.close()
    select = depl_dict["environment"]
    print(select)
    return select


# 正则表达式提取函数
def extract(regular: str, msg: str) -> str:
    message = ''.join(re.findall('"{}": "(.*?)",'.format(regular), msg))
    return message


# 访问链接获取函数
def gain_url(urlname: str) -> str:
    with mysave.MysqlSave() as execute:
        url_header_list = execute.select(
            ['url'], 'domain', {'name': context()}
        )
        url_end_list = execute.select(
            ['url'], 'path', {'urlname': urlname}
        )
        # print(url_end_list)
        urls = url_header_list[0]['url'] + url_end_list[0]['url']
        # print(urls)
        return urls


def exist(tablename: str) -> int:
    with save.SqlSave() as execute:
        state = execute.table_exist(tablename)
        return state


# 用户登录函数
def userlogin(username: str, passwords: str) -> None:
    tablename = 'usermessage'
    md5pas = hashlib.md5(passwords.encode('utf-8')).hexdigest()
    url = gain_url('登录')
    data = {
        "username": username,
        "pwd": md5pas
    }
    response = deamds(url, data)
    if response['msg'] == 'OK':
        response = response["info"]
        with mysave.MysqlSave() as execute:
            message = {
                'username': username, 'email': response['email'],
                'phone': response['phone'],
                'userid': response['userid'], 'kyc': response['kyc'],
                'invitecode': response['invitecode'], 'token': response['token'],
                'nickname': response['nickname'], 'gettime': currenttime(),
                'environment': context()
            }
            condition = {
                'username': username
            }
            result = execute.select(['userid'], tablename, condition)
            if len(result) == 0:
                execute.insert(tablename, message)
            else:
                execute.update(tablename, message, condition)


# 注册
def register(sharename: str) -> str:
    tablename = 'usermessage'
    url = gain_url('注册')
    registertype = '2'
    username = randomname(registertype)
    passwords = '12345678'
    md5pas = hashlib.md5(passwords.encode('utf-8')).hexdigest()
    with mysave.MysqlSave() as execute:
        execute.insert(
            'user', {
                'username': username, 'password': passwords,
                'md5_password': md5pas, 'environment': context(),
                'time': currenttime()
            }
        )
        sharemsg = execute.select(
            ['userid', 'invitecode'], tablename,
            {'username': sharename}
        )
        shareid = {True: mysqldict(sharemsg, 'userid'), False: '0'}[len(sharemsg) != 0]
        invitecode = {True: mysqldict(sharemsg, 'invitecode'), False: ' '}[len(sharemsg) != 0]
        data = {
            "username": username, "type": registertype, "countryid": "191",
            "pwd": hashlib.md5(passwords.encode('utf-8')).hexdigest(), "code": 'xww',
            "channel": {
                "plat": "h5", "share_id": shareid, "activityid": "1",
                "invitecode": invitecode
            }
        }
        response = deamds(url, data)
        if response['msg'] == 'OK':
            response = response['info']
            message = {
                'username': username,
                'channel': str(response['channel']),
                'nickname': response['nickname'],
                'gettime': currenttime(),
                'createtime': response['createtime'],
                'environment': context()
            }
            execute.insert('registermsg', message)
            userlogin(username, passwords)
            return username


# 用户token获取函数
def usertoken(username: str) -> str:
    passwords = '12345678'
    userlogin(username, passwords)
    tablename = 'usermessage'
    with mysave.MysqlSave() as execute:
        selectfield = ['token']
        condition = {
            'username': username
        }
        token = execute.select(selectfield, tablename, condition)
    return mysqldict(token, 'token')


# 管理端token获取
def admintoken() -> str:
    url = gain_url('管理端登录')
    with mysave.MysqlSave() as execute:
        selectlist = ['username', 'password', 'code']
        condition = {
            'environment': context()
        }
        adminmsg = execute.select(selectlist, 'adminuser', condition)
        username = mysqldict(adminmsg, 'username')
        passwords = mysqldict(adminmsg, 'password')
        code = mysqldict(adminmsg, 'code')
        data = {
            "user": username,
            "pwd": passwords
        }
        response = deamds(url, data)['info']
        return response['token']


# 根据username查询信息
def selectnamemsg(username: str) -> str:
    tablename = 'usermessage'
    with mysave.MysqlSave() as execute:
        data = execute.select(
            ['userid'], tablename, {'username': username}
        )

        return mysqldict(data, 'userid')


# 管理端添加money
def addmoney(username: str, money: int) -> str:
    token = admintoken()
    moneys = money * 100
    # reward 1:赠金 0:现金
    reward = '0'
    urls = gain_url('管理端添加money')
    userid = selectnamemsg(username)
    print(userid)
    data = {
        "type": 10201, "userid": userid,
        "money": str(moneys), "remark": "测试",
        "token": token, "reward": reward
    }
    response = json.dumps(deamds(urls, data))
    msg = extract('msg', response)
    return msg


# kyc认证
def kyc(username: str) -> str:
    usertoken(username)
    with save.SqlSave() as execute:
        url = gain_url('kyc')
        token = usertoken(username)
        # ,"idimg2":"https://test.trade.idefiex.com/api/pic/downloadimgkyc.do?134.jpg","idimg3":"https://test.trade.idefiex.com/api/pic/downloadimgkyc.do?134.jpg"}
        data = {
            "token": token, "countryid": "44",
            "idtype": "2", "name": "1128222", "idnumber": username,
            "idimg1": "https://test.trade.idefiex.com/api/pic/downloadimgkyc.do?134.jpg",
            "idimg2": "https://test.trade.idefiex.com/api/pic/downloadimgkyc.do?134.jpg",
            "idimg3": "https://test.trade.idefiex.com/api/pic/downloadimgkyc.do?134.jpg"
        }
        response = json.dumps(deamds(url, data))
        state = ' '.join(re.findall('"state": "(.*?)"', response))
        return state


# 管理端审核kyc
def checkkyc(username: str) -> str:
    login_token = admintoken()
    userid = selectnamemsg(username)
    data = {
        "type": 10003,
        "userid": userid,
        "state": 0, "token": login_token
    }
    urls = gain_url('管理端kyc审核')
    response = json.dumps(deamds(urls, data))
    msg = ' '.join(re.findall('"msg": "(.*?)"', response))
    return msg


# 建仓数据测试用例
def testdata() -> dict:
    tablename = 'creategranary_test'
    with mysave.MysqlSave() as execute:
        testmsg = execute.select(['*'], tablename, {'id': '1'})
        return testmsg[0]


def formula(name: str):
    testmsg = testdata()
    spratio_ratio = float(testmsg['spratio_ratio'])
    slratio_ratio = float(testmsg['slratio_ratio'])
    create_money = float(testmsg['create_money'])
    pry = float(testmsg['pry'])
    formalities_ratio = float(testmsg['formalities_ratio'])
    granary = testmsg['granary']
    direction = testmsg['direction']
    url = gain_url('行情')
    data = {
        "symbol": granary
    }
    response = json.dumps(deamds(url, data))
    # 实际行情价格
    # realityprice
    Cmoney = ''.join(re.findall('"LP": "(.*?)",', response))
    # 交易系数
    Deal_coefficient = create_money * pry
    if Deal_coefficient > 2000:
        coefficient = 0.5
    elif 1000 <= Deal_coefficient <= 2000:
        coefficient = random.randint(1, 4) / 10
    elif Deal_coefficient < 1000:
        coefficient = 0.1
    if granary == 'btc':
        basics = 0.0005
    else:
        basics = 0.0008
    # 点差
    spread = basics * coefficient
    print(spread)
    if direction == '1':
        if granary == 'btc':
            count_monry = round(float(Cmoney) * (1.0 - spread), 4)
        else:
            count_monry = round(float(Cmoney) * (1.0 - spread), 4)
        spot = count_monry - (spratio_ratio * create_money + 0.0 + formalities_ratio * pry * create_money) * (
                count_monry / (pry * create_money))
        spot1 = count_monry + (slratio_ratio * create_money - 0.0 - formalities_ratio * pry * create_money) * (
                count_monry / (pry * create_money))
        return round(spot, 4), round(spot1, 4), str(count_monry)
    else:
        if granary == 'btc':
            count_monry = round(float(Cmoney) * (1.0 + spread), 4)
        else:
            count_monry = round(float(Cmoney) * (1.0 + spread), 4)
        spot = count_monry + (spratio_ratio * create_money + 0.0 + formalities_ratio * pry * create_money) * (
                count_monry / (pry * create_money))
        spot1 = count_monry - (slratio_ratio * create_money - 0.0 - formalities_ratio * pry * create_money) * (
                count_monry / (pry * create_money))
        return round(spot, 4), round(spot1, 4), str(count_monry)


# 现金建仓
def create_granary(username: str) -> None:
    testmsg = testdata()
    url = gain_url('建仓')
    money, money2, cmoney = formula(username)
    print(cmoney)
    top_money = str(float(money))
    bot_money = str(float(money2))

    data = {
        "token": usertoken(username), "symbol": testmsg['granary'],
        "type": testmsg['direction'], "amount": testmsg['create_money'],
        "lever": testmsg['pry'], "topprice": top_money,
        "botprice": bot_money
    }
    response = json.dumps(deamds(url, data))
    print(response)

# gain_url('交易员列表查询')
# brokername = '389863294@qq.com'
# password = 'yangxun19990728'
# userlogin(brokername, password)
# usertoken(brokername)
# register(brokername)
# exist('Name_ResponseMsg')
# admintoken()

# class UnifyWays(object):
#     pass
