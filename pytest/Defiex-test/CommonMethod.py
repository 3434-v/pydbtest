import requests
import re
import json
import sqlitesave as save
import pymysqlsave as mysave
import hashlib
import time
import random
from tqdm import tqdm
"""
静态方法：静态方法是访问不了类或实例中的任何属性，
它已经脱离了类，一般会用在一些工具包中
@staticmethod

类方法：只能访问类变量，不能访问实例变量 使用场景：一般是需要去访问写死的变量，才会用到类方法装饰器
@classmethod

属性方法：将方法变成静态属性
@property   #定义属性方法
@eat.setter  #定义一个可以传参的方法
"""


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
    # print(url + data_str)
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
        # print(message[0][parameter])

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
def context(type_select: int) -> str:
    # type_select：1 环境 2：测试用例
    with open('deploy.json', 'r', encoding='utf8') as depl:
        depl_dict = json.load(depl)
    depl.close()
    message_dict = {
        1: depl_dict["environment"],
        2: depl_dict["test_msg"]
    }
    # print(message_dict[type_select])
    return message_dict[type_select]


# 正则表达式提取函数
def extract(regular: str, msg: str) -> str:
    message = ''.join(re.findall('"{}": "(.*?)",'.format(regular), msg))
    return message


# 访问链接获取函数
def gain_url(urlname: str) -> str:
    with mysave.MysqlSave() as execute:
        url_header_list = execute.select(
            ['url'], 'domain', {'name': context(1)}
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
                'environment': context(1)
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
                'md5_password': md5pas, 'environment': context(1),
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
            "pwd": hashlib.md5(passwords.encode('utf-8')).hexdigest(), "code": 'xwwwwx',
            "channel": {
                "plat": "h5", "share_id": shareid, "activityid": "1",
                "invitecode": invitecode
            }
        }
        response = deamds(url, data)

        if response['msg'] == 'OK':
            response = response['info']
            share_id = ''.join(re.findall('"share_id": "(.*?)",', response['channel']))
            message = {
                'username': username,
                # 'channel': str(response['channel']),
                'channel': share_id,
                'nickname': response['nickname'],
                'gettime': currenttime(),
                'createtime': response['createtime'],
                'environment': context(1)
            }
            execute.insert('registermsg', message)
            userlogin(username, passwords)
            # 新用户默认获取充币地址
            Topup_withdrawal(username).get_recharge_site()
            return username


# 用户token获取函数
def usertoken(username: str) -> str:
    # print(username)
    # 每次从新获取token
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
            'environment': context(1)
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
    with mysave.MysqlSave() as executes:
        testmsg = executes.select(['*'], tablename, {'id': context(2)})
        return testmsg[0]


# 建仓价算法
def formula(name: str):
    testmsg = testdata()
    coefficient = '0.0'
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
    c_money = ''.join(re.findall('"LP": "(.*?)",', response))
    # 交易系数
    deal_coefficient = create_money * pry
    if deal_coefficient > 2000:
        coefficient = 0.5
    elif 1000 <= deal_coefficient <= 2000:
        coefficient = random.randint(1, 4) / 10
    elif deal_coefficient < 1000:
        coefficient = 0.1
    if granary == 'btc':
        basics = 0.0005
    else:
        basics = 0.0008
    # 点差
    spread = basics * coefficient
    # print(spread)
    if direction == '1':
        if granary == 'btc':
            count_monry = round(float(c_money) * (1.0 - spread), 4)
        else:
            count_monry = round(float(c_money) * (1.0 - spread), 4)
        spot = count_monry - (spratio_ratio * create_money + 0.0 + formalities_ratio * pry * create_money) * (
                count_monry / (pry * create_money))
        spot1 = count_monry + (slratio_ratio * create_money - 0.0 - formalities_ratio * pry * create_money) * (
                count_monry / (pry * create_money))
        return round(spot, 4), round(spot1, 4), str(count_monry)
    else:
        if granary == 'btc':
            count_monry = round(float(c_money) * (1.0 + spread), 4)
        else:
            count_monry = round(float(c_money) * (1.0 + spread), 4)
        spot = count_monry + (spratio_ratio * create_money + 0.0 + formalities_ratio * pry * create_money) * (
                count_monry / (pry * create_money))
        spot1 = count_monry - (slratio_ratio * create_money - 0.0 - formalities_ratio * pry * create_money) * (
                count_monry / (pry * create_money))
        return round(spot, 4), round(spot1, 4), str(count_monry)


# 预计盈亏计算
def fun_predict_money() -> None:

    spot = 10966.68
    spot1 = 10972.16
    count_monry = '10972.16'
    # 盈利
    test_dict = testdata()
    create_money = float(test_dict['create_money'])
    pry = float(test_dict['pry'])
    direction = str(test_dict['direction'])
    # print(test_dict)
    if direction == '2':
        # print((float(count_monry) * create_money * pry))
        sort_monry = ((spot - float(count_monry)) / float(count_monry)) * create_money * pry - 0.0
        desc_money = ((float(count_monry) - spot1) / float(count_monry)) * create_money * pry + 0.0
        # print((float(count_monry) - spot1))
        print(sort_monry, desc_money)
    else:
        # print((float(count_monry) * create_money * pry))
        sort_monry = ((float(count_monry) - spot) / float(count_monry)) * create_money * pry - 0.0
        desc_money = ((spot1 - float(count_monry)) / float(count_monry)) * create_money * pry + 0.0
        print(sort_monry, desc_money)

    # sort_money = create_money + ()

# fun_predict_money()


# 现金建仓
def create_granary(username: str) -> None:
    testmsg = testdata()
    url = gain_url('建仓')
    money, money2, c_money = formula(username)
    # print(money, money2, c_money)
    top_money = str(float(money))
    bot_money = str(float(money2))
    spratio_ratio = float(testmsg['spratio_ratio'])
    slratio_ratio = float(testmsg['slratio_ratio'])
    print("币种:{}---止盈:{}-止损:{},止盈比例:{}-止损比例:{},建仓价格:{}".format(
        testmsg['granary'], money, money2, spratio_ratio, slratio_ratio, c_money
    )
    )
    data = {
        "token": usertoken(username), "symbol": testmsg['granary'],
        "type": testmsg['direction'], "amount": testmsg['create_money'],
        "lever": testmsg['pry'], "topprice": top_money,
        "botprice": bot_money
    }
    response = deamds(url, data)['info']
    print("币种:{}---止盈:{}-止损:{},止盈比例:{}-止损比例:{},建仓价格:{}".format(
        testmsg['granary'],
        response['spprice'], response['slprice'],
        response['spratio'], response['slratio'], response['openprice']
        )
    )
    response['username'] = username
    response['testcase'] = testmsg['id']
    # 问题待修改，没有正确存值
    # with mysave.MysqlSave() as execute:
    #     execute.insert('granary_message', response)


# 平仓
def flat_granary(username: str) -> None:
    url = gain_url('平仓')
    with mysave.MysqlSave() as execute:
        orderid_list = execute.select(
            ['orderid'], 'granary_message', {'username': username}
        )
        for dictmsg in orderid_list:
            orderid = dictmsg['orderid']
            data = {
                "token": usertoken(username),
                "orderid": orderid
            }
            resoonse = deamds(url, data)
            condition = {
                "orderid": orderid
            }
            if resoonse['msg'] in 'OK':
                execute.delete('granary_message', condition)
            elif resoonse['msg'] in "参数错误":
                execute.delete('granary_message', condition)


# 分页查询所有持仓记录
def keep_granary(username: str) -> str:
    url = gain_url('分页查询所有持仓记录')
    data = {
        "token": usertoken(username),
        "page": "1", "count": "20"
    }
    response = json.dumps(deamds(url, data))
    totalcount = ''.join(re.findall('"totalcount": "(.*?)",', response))
    return totalcount


# username = '389863294@qq.com'
# keep_granary(username)


# 分页查询所有平仓记录
def flatgranary_record(username: str) -> str:
    url = gain_url('分页查询所有平仓记录')
    data = {
        "token": usertoken(username),
        "page": "1", "count": "20", "symbol": ""
    }
    response = json.dumps(deamds(url, data))
    totalcount = ''.join(re.findall('"totalcount": "(.*?)",', response))
    return totalcount


# 插点
def vertex():
    orderid = '8476'
    userid = '11374499021'
    symbol = 'btc'
    price = '1228604'
    url = gain_url('插点')
    data = {
        "type": 10359, "id": orderid, "userid": userid,
        "symbol": symbol, "price": price, "token": admintoken(),
    }
    response = deamds(url, data)


# 提币以及信息获取
def Withdraw_msg(username: str) -> None:
    # ERC-20
    addr = '0x777D76e24da310D91B0C3b48767E898772F198F7'
    money_type = '3'
    # OMNI
    # addr = '3EkaqUNdowvetHDzkYgA6woXcBRkPuULRT'
    # money_type = '1'
    url = gain_url('提币')
    amount = '2'
    data = {
        "token": usertoken(username), "type": money_type,
        "amount": amount, "addr": addr, "code": "xwwwwx"
    }
    response = deamds(url, data)['info']
    bank_order_id = response['bank_order_id']
    admin_url = gain_url('管理端审核提币')
    admin_data = {
        "type": 10204, "orderid": bank_order_id,
        "verify": 1, "token": admintoken()
    }
    admin_response = deamds(admin_url, admin_data)


# 归集
def Collection(index: int, address: str):
    address_type_list = ['ETH', 'TRX', 'BTC']
    url = gain_url('归集')
    data = {
        "chainCode": address_type_list[index],
        "address": address,
        "symbol": "USDT"
    }
    data = json.dumps(data)
    response = requests.post(url, data=data)
    print(response.text)


# 提币
def Withdraw(username: str, index: int):
    url = gain_url('提币')
    erc20_address = ''
    trc20_address = ''
    omni_address = ''
    if context(1) in "测试环境":
        erc20_address = '0x0e50f970F169A43a93D9c3c4697B3cb91128F993'
        trc20_address = 'TGbNUPe5fFUda32cz8GXQDsbTugiAEdp7n'
        omni_address = '1c9qJ6bxKZHtdnyHzxtUbik9zemfjGUfJ'
    elif context(1) in "预发布环境":
        erc20_address = '0x777D76e24da310D91B0C3b48767E898772F198F7'
        trc20_address = 'TGbNUPe5fFUda32cz8GXQDsbTugiAEdp7n'
        omni_address = '1c9qJ6bxKZHtdnyHzxtUbik9zemfjGUfJ'
    # [地址， 提币金额， 类型]
    message_dict = {
        1: [erc20_address, '2', '3'],
        2: [trc20_address, '1', '4'],
        3: [omni_address, '5', '1']
    }
    data = {
        "token": usertoken(username), "type": message_dict[index][2],
        "amount": message_dict[index][1], "addr": message_dict[index][0],
        "code": "xwwwwx"
    }
    msg = deamds(url, data)['info']
    with mysave.MysqlSave() as execute:
        message = {
            'username': username,
            'orderid': msg['orderid'],
            'bank_order_id': msg['bank_order_id'],
            'time': currenttime(),
            'environment': context(1)
        }
        execute.insert('Withdraw', message)
    admin_url = gain_url('管理端审核提币')
    admin_data = {
        "type": 10204, "orderid": msg['bank_order_id'],
        "verify": 1, "token": admintoken()
    }
    deamds(admin_url, admin_data)

# Withdraw('389863294@qq.com', 2)


# 获取提币纪录
def Withdraw_recode(username: str) -> None:
    url = gain_url('获取提币纪录')
    data = {
        "token": usertoken(username),
        "page": "1", "count": "20"
    }
    deamds(url, data)


# 发券
def send_ticket(userid: str, ticket_type: int) -> None:
    # tx:0赠金 1：现金
    url = gain_url('发券')
    data = {
        "type": 10362,
        "userid": userid,
        "coupon": {
            "amount": "100.00", "lever": "10",
            "tx": str(ticket_type), "count": "1",
            "timeoutuse": "1"
        },
        "token": admintoken()
    }
    deamds(url, data)


# send_ticket('11374499021', 0)

# send_ticket('11374499021', 1)


# 市价券建仓
def create_ticket(username: str, couponid: str):
    url = gain_url('市价券建仓')
    data = {
        "token": usertoken(username),
        "symbol": "btc", "type": "2",
        "couponid": couponid, "topprice": "0"
    }
    deamds(url, data)


# 查询任务信息
def select_task_msg(username: str):
    url = gain_url('查询任务信息')
    data = {
        "token": usertoken(username)
    }
    deamds(url, data)


# select_task_msg('389863294@qq.com')


# 1016
def select_userid(email: str):
    url = gain_url('发券')
    data = {
        "type": 1016,
        "email": email,
        "token": admintoken()
    }
    deamds(url, data)


# 510
def select_tasks():
    url = gain_url('发券')
    data = {
        "type": 510,
        "tasktype": "2",
        "token": admintoken()
    }
    deamds(url, data)


# 1017
def select_email(userid: str):
    url = gain_url('发券')
    data = {
        "type": 1017,
        "userid": userid,
        "token": admintoken()
    }
    deamds(url, data)


# USDT汇率
def exchange_usdt():
    url = gain_url('USDT汇率')
    data = {}
    deamds(url, data)


# 产品配置(游客)
def configmsg_visitor():
    url = gain_url('产品配置(游客)')
    data = {

    }
    deamds(url, data)


# 行情
def market(chain: str) -> float:
    url = gain_url('行情')
    data = {
        # 默认全部转换成小写
        "symbol": chain.lower()
    }
    response_dict = deamds(url, data)['info']
    newest = float(response_dict['LP'])
    return newest


# 充值提现
class Topup_withdrawal(object):
    def __init__(self, username):
        self.username = username
        self.token = usertoken(username)
        # self.token = ''

    # 产品配置
    def configmsg(self):
        url = gain_url('产品配置')
        data = {
            "token": self.token
        }
        deamds(url, data)

    # 获取充币地址
    def get_recharge_site(self):
        url = gain_url('获取充币地址')
        chaincode_list = ['BTC', 'ETH', 'TRX']
        site_list = []
        for chain_index in chaincode_list:
            data = {
                "token": self.token,
                "chaincode": chain_index,     # 链名称 BTC/ETH/TRX
                "coincode": chain_index      # 币名称 USDT/BTC/ETH
            }
            response_dict = deamds(url, data)
            site_list.append(response_dict['info']['addr'])
        with mysave.MysqlSave() as execute:
            message = {
                "username": self.username,
                "orderid": selectnamemsg(self.username),
                "BTC": site_list[0],
                "ETH": site_list[1],
                "TRX": site_list[2],
                "environment": context(1),
                "get_time": currenttime()
                }
            execute.insert('recharge_site', message)

    # 提币
    def withdrawal(self, index: int):
        url = gain_url('提币')
        # 充值类型
        withdrawal_dict = {
            1: ['ETH', 'USDT', '100', '0x0e50f970F169A43a93D9c3c4697B3cb91128F993'],
            2: ['BTC', 'USDT', '1', '3EkaqUNdowvetHDzkYgA6woXcBRkPuULRT'],
            3: ['TRX', 'USDT', '1', 'TGbNUPe5fFUda32cz8GXQDsbTugiAEdp7n'],
            4: ['ETH', 'ETH', '0.05123212', '0x0e50f970F169A43a93D9c3c4697B3cb91128F993'],
            5: ['BTC', 'BTC', '0.001', '3EkaqUNdowvetHDzkYgA6woXcBRkPuULRT']
        }
        data = {
            "token": self.token,
            "chaincode": withdrawal_dict[index][0], "coincode": withdrawal_dict[index][1],
            "amount": withdrawal_dict[index][2], "addr": withdrawal_dict[index][3],
            "code": "xwwwwx"
        }
        deamds(url, data)

    # 获取充值纪录
    def get_topup_record(self):
        url = gain_url('获取充值纪录')
        data = {
            "token": self.token,
            "page": "1", "count": "20"
        }
        deamds(url, data)

    # 获取提币纪录
    def get_withdrawal_record(self):
        url = gain_url('获取提币纪录')
        data = {
            "token": self.token,
            "page": "1", "count": "20"
        }
        deamds(url, data)

    # 预期计算汇率
    def expect_exchaneg(self, msg_list: list) -> float:
        market_index = ''
        if msg_list[0] in 'USDT':
            market_index = msg_list[1]
        elif msg_list[0] in "BTC" or "ETH":
            market_index = msg_list[0]
        newset = market(market_index)
        if msg_list[0] in "USDT":
            exchange_rate = round((1.0 / newset), 8) * (1 - 0.002)
            exchange_money = exchange_rate * float(msg_list[2])
            print(exchange_money)
            return exchange_rate
        else:
            exchange_rate = round((newset / 1.0), 8) * (1 - 0.002)
            exchange_btc = exchange_rate * float(msg_list[2])
            print(exchange_btc)
            return exchange_rate

    # 兑币
    def exchange(self, index: int):
        # detail参数解析  0,coinfrom  1:cointo  2:amount
        detail_dict = {
            1: ['USDT', 'BTC', '1000'],
            2: ['USDT', 'ETH', '1000'],
            3: ['BTC', 'USDT', '1'],
            4: ['ETH', 'USDT', '1'],
        }
        url = gain_url('兑币')
        data = {
            "token": self.token,
            "coinfrom": detail_dict[index][0], "cointo": detail_dict[index][1],
            "amount": detail_dict[index][2]
        }
        old_usdt_balance, old_btc_balance, old_eth_balance = self.select_allmoney()
        response_dict = deamds(url, data)['info']
        exchange_rate = self.expect_exchaneg(detail_dict[index])
        time.sleep(3)
        new_usdt_balance, new_btc_balance, new_eth_balance = self.select_allmoney()
        # USDT兑换BTC 计算
        if index == 1:
            btc_balance = float(detail_dict[index][2]) * exchange_rate + old_btc_balance
            if new_btc_balance == round(btc_balance, 6):
                usdt_balance = float(old_usdt_balance) - float(detail_dict[index][2]) * 1
                print("提现前BTC:{}、USDT:{} \n提现金额:{} 提现后BTC:{}、USDT:{}".format(
                    old_btc_balance, old_usdt_balance, detail_dict[index][2], btc_balance, usdt_balance
                ))
        # USDT兑换ETH 计算
        elif index == 2:
            eth_balance = float(detail_dict[index][2]) * exchange_rate + old_eth_balance
            if new_eth_balance == round(eth_balance, 4):
                usdt_balance = float(old_usdt_balance) - float(detail_dict[index][2]) * 1
                print("提现前ETH:{}、USDT:{} \n提现金额:{} 提现后ETH:{}、USDT:{}".format(
                    old_eth_balance, old_usdt_balance, detail_dict[index][2], eth_balance, usdt_balance
                ))
        # BTC兑换USDT 计算
        elif index == 3:
            usdts_balance = (float(detail_dict[index][2]) * exchange_rate) + old_usdt_balance
            btcs_balance = (float(old_btc_balance) - float(detail_dict[index][2]))
            print("USDT:实际值:{}-计算值:{}".format(new_usdt_balance, usdts_balance))
            print("BTC:实际值:{}-计算值:{}".format(new_btc_balance, btcs_balance))
        # ETH兑换USDT 计算
        elif index == 4:
            usdts_balance = (float(detail_dict[index][2]) * exchange_rate) + old_usdt_balance
            eths_balance = (float(old_eth_balance) - float(detail_dict[index][2]))
            print("USDT:实际值:{}-计算值:{}".format(new_usdt_balance, usdts_balance))
            print("ETH:实际值:{}-计算值:{}".format(new_eth_balance, eths_balance))

    # 查询币的兑换记录
    def select_exchange_detail(self):
        url = gain_url('查询币的兑换记录')
        data = {
            "token": self.token,
            "page": "1", "count": "20"
        }
        response_dict = deamds(url, data)

    # 获取所有余额
    def select_allmoney(self) -> list:
        url = gain_url('获取冻结赠金')
        data = {
            "token": self.token
        }
        data_list = deamds(url, data)['info']['datas']
        usdt_balance = float(data_list[0]['balance'])
        btc_balance = float(data_list[1]['balance'])
        eth_balance = float(data_list[2]['balance'])
        balance_list = [usdt_balance, btc_balance, eth_balance]
        # print("USDT:{}--BTC:{}--ETH:{}".format(balance_list[0], balance_list[1], balance_list[2]))
        return balance_list

    # USDT汇率
    def exchange_rate(self):
        url = gain_url('USDT汇率')
        data = {

        }
        deamds(url, data)


# 二元期权
class Binary_options(object):
    def __init__(self, username):
        self.testdict = testdata()
        self.token = usertoken(username)
        self.symbol = self.testdict['granary']
        self.type = self.testdict['direction']
        self.amount = self.testdict['create_money']
        self.endtime = int(time.time()) + 60

    # 二元期权市价现金建仓
    def create_granary(self):
        url = gain_url('二元期权市价现金建仓')
        data = {
            "token": self.token, "symbol": self.symbol,
            "type": self.type, "amount": self.amount,
            "endtime": self.endtime
        }
        deamds(url, data)

    # 二元期权持仓单查询
    def keep_granary(self):
        url = gain_url('二元期权持仓单查询')
        data = {
            "token": self.token
        }
        deamds(url, data)

    def flat_granary(self):
        url = gain_url('二元期权平仓单查询')
        data = {
            "token": self.token,
            "page": "1", "count": "20"
        }
        deamds(url, data)


# 1U夺宝
class snatch_treasure(object):
    def __init__(self, username):
        self.token = usertoken(username)

    # 用户购买历史记录
    def purchase_history(self):
        url = 'http://192.168.31.24:7071/treasure/user/purchased/list'
        header = {
            'token': self.token
        }
        response = requests.get(url, headers=header)
        print(response.text)


if __name__ == "__main__":
    user = '389863294@qq.com'
    test = snatch_treasure(user)
    test.purchase_history()
    # execute = Binary_options(user)
    # run = Topup_withdrawal(user)
    # run.withdrawal(4)
    # run.get_recharge_site()

