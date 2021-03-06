import CommonMethod as pymethod
import json
import random
import re
import pymysqlsave as mysave
import time
import sys
from graphviz import Digraph
import uuid
from random import sample


# 交易员接口类
class DealStaff(object):
    """用于交易员接口"""

    def __init__(self) -> None:
        pass

    # 查询最新资产
    def select_money(self, name: str) -> None:
        url = pymethod.gain_url('查询最新资产')
        data = {
            "token": pymethod.usertoken(name)
        }
        pymethod.deamds(url, data)

    # 管理端审核交易员
    def check_trader(self, username: str, state: str) -> None:
        admin_token = pymethod.admintoken()
        # state 1:审核通过 0:审核失败
        # state = '1'
        userid = pymethod.selectnamemsg(username)
        url = pymethod.gain_url('交易员审核')
        data = {
            "type": 10211, "userid": userid,
            "state": state, "token": admin_token
        }
        pymethod.deamds(url, data)

    # 交易员申请开通
    def apply(self, name: str) -> json:
        url = pymethod.gain_url('交易员申请开通')
        data = {
            "token": pymethod.usertoken(name),
            "language": "zh_CN"
        }
        response = pymethod.deamds(url, data)
        return response

    # 交易员详情查询
    def select_detail(self, username: str) -> dict:
        userid = pymethod.selectnamemsg(username)
        url = pymethod.gain_url('交易员详情查询')
        data = {
            "planerid": userid,
            "language": "zh_CN"
        }
        return pymethod.deamds(url, data)

    # 交易员交易记录查询
    def deal_record(self, username: str) -> None:

        userid = pymethod.selectnamemsg(username)
        url = pymethod.gain_url('交易员交易记录查询')
        data = {
            "planerid": userid,
            "page": "1", "count": "20"
        }
        pymethod.deamds(url, data)

    # 交易员跟单盈利查询
    def deal_gain(self, username: str) -> None:

        userid = pymethod.selectnamemsg(username)
        url = pymethod.gain_url('交易员跟单盈利查询')
        data = {
            "planerid": userid,
            "page": "1", "count": "20"
        }
        pymethod.deamds(url, data)

    # 交易员列表查询
    def trader_list(self):
        url = pymethod.gain_url('交易员列表查询')
        data = {
            "ordertype": "1"
        }
        planerid_str = json.dumps(pymethod.deamds(url, data))
        planerid_list = re.findall('"planerid": "(.*?)"', planerid_str)
        return planerid_list

    # 用户跟单某个交易员
    def user_trader(self, username: str, planerid: str, referrerid: str):
        opentype = '2'
        openamount = '50'
        openamountdaymax = '500'
        openamountholdmax = '1000'
        openamountslrate = '0'
        url = pymethod.gain_url('用户跟单某个交易员')
        data = {
            "token": pymethod.usertoken(username), "planerid": planerid, "referrerid": referrerid,
            "opentype": opentype, "openamount": openamount, "openamountdaymax": openamountdaymax,
            "openamountholdmax": openamountholdmax, "openamountslrate": openamountslrate
        }
        pymethod.deamds(url, data)

    # 用户跟单详情查询
    def user_detail(self, name: str):
        url = pymethod.gain_url('用户跟单详情查询')
        data = {
            "token": pymethod.usertoken(name)
        }
        pymethod.deamds(url, data)

    # 用户修改跟单参数
    def user_remove_parameter(self, name: str, planerid: str):
        # 是否暂停1: 是0: 否
        pause = '1'
        openamount = '500'
        openamountdaymax = '1000'
        openamountholdmax = '2000'
        openamountslrate = '0.5'
        url = pymethod.gain_url('用户修改跟单参数')
        data = {
            "token": pymethod.usertoken(name),
            "planerid": planerid, "pause": pause, "opentype": "1",
            "openamount": openamount, "openamountdaymax": openamountdaymax,
            "openamountholdmax": openamountholdmax, "openamountslrate": openamountslrate
        }
        pymethod.deamds(url, data)

    # 用户取消跟单某个交易员
    def cancel_deal(self, name: str, planerid: str):
        url = pymethod.gain_url('用户取消跟单某个交易员')
        data = {
            "token": pymethod.usertoken(name),
            "planerid": planerid
        }

        pymethod.deamds(url, data)

    # 用户跟单历史查询
    def user_deal_history(self, name, planerid):
        url = pymethod.gain_url('用户跟单历史查询')
        data = {
            "token": pymethod.usertoken(name),
            "planerid": planerid
        }
        pymethod.deamds(url, data)

    # 交易员修改信息
    def trader_remove_message(self, name):
        url = pymethod.gain_url('交易员修改信息')
        # 1: 确认跟单规则 2: 带单开关 3: 个人描述 4: 标签
        types = '4'
        info = ''
        if types == '4':
            index = random.randint(801, 810)
            info = '1000' + str(index)
            # info = "['1000801']"
        elif types == '1':
            # 1:已确认0: 没有
            info = '1'
        elif types == '2':
            # 1:关闭 0:打开
            info = '1'
        elif types == '3':
            info = '一个没赚过的交易员'
        print(info)
        data = {
            "token": pymethod.usertoken(name),
            "type": types, "info": info
        }
        pymethod.deamds(url, data)

    # 交易员跟单提成每日汇总查询
    def trader_everyday_royalties(self, name):
        url = pymethod.gain_url('交易员跟单提成每日汇总查询')
        data = {
            "token": pymethod.usertoken(name),
            "page": "1", "count": "20"
        }
        pymethod.deamds(url, data)

    # 交易员跟单提成每日明细查询
    def everyday_detail(self, name, timestamp):
        url = pymethod.gain_url('交易员跟单提成每日明细查询')
        data = {
            "token": pymethod.usertoken(name),
            "tradedate": timestamp
        }
        pymethod.deamds(url, data)

    # 推荐人详情查询
    def referrer_detail(self, name):
        url = pymethod.gain_url('推荐人详情查询')
        data = {
            "token": pymethod.usertoken(name)
        }
        pymethod.deamds(url, data)

    # 推荐人跟单用户信息查询
    def referrer_user_detail(self, name):
        url = pymethod.gain_url('推荐人跟单用户信息查询')
        data = {
            "token": pymethod.usertoken(name)
        }
        pymethod.deamds(url, data)

    # 推荐人每日提成汇总信息查询
    def referrer_everyday_collect(self, name):
        url = pymethod.gain_url('推荐人每日提成汇总信息查询')
        data = {
            "token": pymethod.usertoken(name)
        }
        pymethod.deamds(url, data)

    # 推荐人每日提成明细查询
    def referrer_everyday_deduct(self, name, tradedate):
        url = pymethod.gain_url('推荐人每日提成明细查询')
        data = {
            "token": pymethod.usertoken(name),
            "tradedate": tradedate
        }
        pymethod.deamds(url, data)

    # 交易员标签信息查询
    def trader_label(self):
        url = pymethod.gain_url('交易员标签信息查询')
        data = {}
        pymethod.deamds(url, data)


def traderuser():
    deal = DealStaff()
    username = pymethod.register('')
    # username = '1663700630@test.com'
    if deal.apply(username)['code'] == '1851':
        pymethod.addmoney(username, 10000)
        if deal.apply(username)['code'] == '1852':
            pymethod.kyc(username)
            pymethod.checkkyc(username)
            deal.apply(username)
            deal.check_trader(username, '1')
            time.sleep(2)
            tradermsg = deal.select_detail(username)["info"]
            if len(tradermsg) != 0 and tradermsg['status'] == '1':
                del tradermsg['nickname']
                del tradermsg['headimg']
                del tradermsg['opentimestoday']
                del tradermsg['shareratio']
                del tradermsg['status']
                del tradermsg['member']
                del tradermsg['createdays']
                del tradermsg['desc']
                with mysave.MysqlSave() as execute:
                    print(tradermsg)
                    create_message = []
                    for key in tradermsg.keys():
                        create_message.append(key + ' varchar(30)')
                    # execute.create('traderuser', create_message)
                    result = execute.select(
                        ['planerid'], 'traderuser', {'planerid': pymethod.selectnamemsg(username)}
                    )
                    if len(result) == 0:
                        execute.insert('traderuser', tradermsg)
                    else:
                        execute.update(
                            'traderuser', tradermsg, {'planerid': pymethod.selectnamemsg(username)}
                        )

                    # 分表操作，代码误删
                    # execute.create('traderuser1', create_message[0: 11])
                    # execute.create('traderuser2', create_message[11:])
                    # tradermsg1 = {index: tradermsg[index] for index in list(tradermsg.keys())[0: 11]}
                    # tradermsg2 = {index: tradermsg[index] for index in list(tradermsg.keys())[11:]}
                    # execute.insert('traderuser1', tradermsg1)
                    # execute.insert('traderuser2', tradermsg2)


# 券服务
class Ticket(object):

    # 领取券
    def get_ticket(self, username: str):
        url = pymethod.gain_url('领取券')
        data = {
            "token": pymethod.usertoken(username),
            "channeltype": "1", "channelid": "1",
            "couponid": "1"
        }
        pymethod.deamds(url, data)

    # 查询可用券数量
    def select_ticket_count(self, username: str):
        url = pymethod.gain_url('查询可用券数量')
        data = {
            "token": pymethod.usertoken(username)
        }
        pymethod.deamds(url, data)

    # 查询可用券明细
    def ticket_detail(self, username: str) -> str:
        url = pymethod.gain_url('查询可用券明细')
        data = {
            "token": pymethod.usertoken(username)
        }
        couponid = pymethod.deamds(url, data)['info']['datas'][0]['couponid']
        return couponid



def New_Task():
    run = Ticket()
    # 1
    username = pymethod.register('')
    run.select_ticket_count(username)
    run.get_ticket(username)
    couponid = run.ticket_detail(username)
    # 2
    pymethod.create_ticket(username, couponid)
    # 3


# 9个任务一键完成
def ticket_test():
    # 前置条件，数据库中建仓价为10000
    run = Ticket()
    # username = pymethod.register('')
    username = pymethod.register('')
    username_id = pymethod.selectnamemsg(username)
    pymethod.send_ticket(username_id, 0)
    time.sleep(5)
    couponid = run.ticket_detail(username)
    pymethod.create_ticket(username, couponid)
    pymethod.kyc(username)
    pymethod.checkkyc(username)
    pymethod.addmoney(username, 100000)
    pymethod.create_granary(username)
    pymethod.register(username)
    time.sleep(3)
    pymethod.create_granary(username)


def ticket_test2():
    run = Ticket()
    # username = pymethod.register('')
    username = '1667811120@test.com'
    username_id = pymethod.selectnamemsg(username)
    # pymethod.send_ticket(username_id, 0)
    # pymethod.vertex()
    # lever_name = pymethod.register(username)
    lever_name = '1668156046@test.com'
    # pymethod.addmoney(lever_name, 1000)
    # pymethod.create_granary(lever_name)
    pymethod.kyc(lever_name)
    pymethod.checkkyc(lever_name)


def ticket_test3():

    username = '1667695074@test.com'
    username_id = pymethod.selectnamemsg(username)
    pymethod.send_ticket(username_id, 1)


def ticket_test4():
    # pymethod.register('')
    username = '166256053@test.com'
    username_id = pymethod.selectnamemsg(username)
    pymethod.send_ticket(username_id, 1)


def testcase():
    deal = DealStaff()
    for index in range(1):
        username = pymethod.register('')
        pymethod.addmoney(username, 500000)
        deal.user_trader(
            username, '14186191497', '11470525726'
        )
    # deal.select_detail('166651289@test.com')


def testcase2():
    deal = DealStaff()
    deal.select_detail('1664001394@test.com')
    # pymethod.addmoney('1664001394@test.com', 1000)
    deal.user_deal_history('1668159165@test.com', '11739860537')
    # deal.user_detail('1668159165@test.com')


# def traderuser1():
#     deal = DealStaff()
#     deal.check_trader(username, '1')


def testcase3():
   pass


# 误删
def testcase4():
    deal = DealStaff()
    username_1 = '1664989478@test.com'
    username_2 = '1666935223@test.com'
    recommend_username_1 = '1662635580@test.com'
    recommend_id = '12371813944'
    trader_username = '1666873112@test.com'
    trader_id = '11911215051'
    # username = pymethod.register('')
    # pymethod.addmoney(username_2, 10000)
    # deal.user_trader(username_2, trader_id, '')
    # pymethod.create_granary(trader_username)
    # deal.referrer_everyday_collect(recommend_username_1)
    # deal.referrer_everyday_deduct(recommend_username_1, '20200713')
    # deal.trader_everyday_royalties(trader_username)
    # deal.everyday_detail(trader_username, '20200713')


# 交易员、推荐人、用户三级关系返佣情况
def testcase5():
    # traderuser()
    deal = DealStaff()
    trade_username = '1664356591@test.com'
    trade_id = '12249017041'
    recommend_username = '1669220738@test.com'
    recommend_id = '10018171820'
    username = '1669803935@test.com'
    user_id = '10644991607'
    username_2 = '1664198692@test.com'
    username_3 = '1663651527@test.com'
    # pymethod.register('')
    # 查询实时资产
    # deal.select_money(trade_username)
    # pymethod.addmoney(recommend_username, 1000)
    # deal.select_money(recommend_username)
    # pymethod.addmoney(username, 1000)
    # deal.select_money(username)
    # deal.user_trader(username_3, trade_id, '')
    # pymethod.addmoney(username_3, 1000)
    # pymethod.create_granary(trade_username)
    # pymethod.addmoney(username_2, 1000)


def testcase6():
    deal = DealStaff()
    trader_user = '1666230669@test.com'
    trader_id = pymethod.selectnamemsg(trader_user)
    tjr_user = '1663784103@test.com'
    tjr_id = pymethod.selectnamemsg(tjr_user)
    xj_user = '1663894119@test.com'
    # for index in range(1):
    #     username = pymethod.register('')
    #     pymethod.addmoney(username, 1000)
    #     deal.user_trader(username, trader_id, tjr_id)

    # pymethod.create_granary(trader_user)


def testcase7():
    deal = DealStaff()
    trader_username = '1665147@test.com'
    username = '389863294@qq.com'
    pymethod.create_granary(username)
    # username = pymethod.register('')
    # pymethod.addmoney(username, 1000)
    # deal.user_trader(username, trader_id, '')
    # deal.user_remove_parameter('1664846527@test.com', trader_id)
    # deal.cancel_deal('1668737377@test.com', trader_id)
    # deal.user_trader('1668737377@test.com', trader_id, '')
    # pymethod.register('')
    # pymethod.create_granary(username)
    # pymethod.flat_granary(username
    # deal.check_trader('12', '1')

# os.path.realpath(_file_)——返回真实路径
#
# os.path.split()——返回路径的目录和文件名
#
# os.getcwd()——得到当前工作的目录


# 协程
def testcase8():
    import asyncio

    async def display(username):
        pymethod.flat_granary(username)
    user_list = [
        '389863294@qq.com'
    ]
    coroutines = [display(username) for username in user_list]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(coroutines))
    loop.close()


# 单进程
def testcase9():
    def download_task(filename):
        print("开始下载{}...".format(filename))
        time_to_download = random.randint(5, 10)
        time.sleep(time_to_download)
        print("{}下载完成！耗费{}秒".format(filename, time_to_download))

    def main():
        start = time.time()
        download_task("test1")
        download_task("test2")
        end = time.time()
        print("总耗时:{}".format(end - start))

    main()


# 多进程
def testcase10():
    from multiprocessing import Process
    from os import getpid

    def download_task(filename):
        print("启动下载进程, 编号[{}]".format(getpid()))
        print("开始下载{}...".format(filename))
        time_to_download = random.randint(5, 10)
        time.sleep(time_to_download)
        print("{}下载完成！耗费{}秒".format(filename, time_to_download))

    def main():
        start = time.time()
        task1 = Process(target=download_task, args=('test1', ))
        task1.start()
        task2 = Process(target=download_task, args=('test2', ))
        task2.start()
        task1.join()
        task2.join()
        end = time.time()
        print("总耗时:{}".format(end - start))
    main()


def testcase11():
    pymethod.register('')


def logging(level):
    def outwrapper(func):
        def wrapper(*args, **kwargs):
            print("[{0}]: enter {1}()".format(level, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return outwrapper


@logging(level="INFO")
def hello(a, b, c):
    print(a, b, c)


class logging(object):
    def __init__(self, level):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("[{0}]: enter {1}()".format(self.level, func.__name__))
            return func(*args, **kwargs)
        return wrapper


@logging(level="TEST")
def hello(a, b, c):
    print(a, b, c)


"""
def run_time(func):
    print("正在运行方法:{}".format(func.__name__))
    state = time.time()
    func(1)
    time.sleep(1)
    end = time.time()
    print("time:{}".format(end - state))
    return func


@run_time
def contexts(type_select: int) -> str:
    # type_select：1 环境 2：测试用例
    with open('deploy.json', 'r', encoding='utf8') as depl:
        depl_dict = json.load(depl)
    depl.close()
    message_dict = {
        1: depl_dict["environment"],
        2: depl_dict["test_msg"]
    }
    print(message_dict[type_select])
    return message_dict[type_select]
"""


def rebate():
    """ 级别建立:
    A-->B-->C-->D
     -->B2
    """

    testA = '1669130247@test.com'
    testB = '1663239847@test.com'
    testB2 = ''
    testB3 = ''
    testC = '16637726@test.com'
    testC2 = ''
    testD = '1665713293@test.com'
    testE = '1668026284@test.com'
    testE = pymethod.register(testD)


# 多级关系生成
def arithmetic(counter):
    # usernames = pymethod.register('')
    usernames = '1665914277@test.com'
    user_list = []
    for index in range(counter):
        user_list.append(usernames)
        usernames = pymethod.register(usernames)
        pymethod.addmoney(usernames, 10000)
        for index in range(2):
            pymethod.Binary_options(usernames).create_granary()
        # pymethod.create_granary(usernames)
        # pymethod.code(usernames).nativate_code()
    user_list.append(usernames)
    print(user_list)
    return user_list


# 开关闭合问题-->code返佣
def code_test(users_list: list):
    # 1、先生成一个5级列表,0->对应1级头
    # users_list = arithmetic(6)
    for user_index in users_list:
        pymethod.addmoney(user_index, 100000)
        pymethod.code(user_index).nativate_code()
        pymethod.kyc(user_index)
        pymethod.checkkyc(user_index)
        pymethod.create_granary(user_index)


def get_codetodaybalance_codetodaycount(users_list: list):
    codetodaybalance_list = []
    codetodaycount_list = []
    for user_index in users_list:
        code_response = pymethod.code(user_index).select_all_message()
        # 今日返佣金额
        codetodaybalance = code_response['info']['codetodaybalance']
        # 今日卖出份数
        codetodaycount = code_response['info']['codetodaycount']
        codetodaybalance_list.append(codetodaybalance)
        codetodaycount_list.append(codetodaycount)
    return codetodaybalance_list, codetodaycount_list


# code返佣计算
def count_code_money():
    users_list = arithmetic(6)
    # old_codetodaybalance_list, old_codetodaycount_list = get_codetodaybalance_codetodaycount(users_list)
    code_test(users_list)
    # new_codetodaybalance_list, new_codetodaycount_list = get_codetodaybalance_codetodaycount(users_list)
    # money_list = [50, 25, 12.5, 6.25, 3.12]


# 二元期权返佣计算
def share_option():
    arithmetic(6)


if __name__ == "__main__":
    # share_option()
    username = '1665914277@test.com'
    pymethod.addmoney(username, 10000)
    # username = pymethod.register('')
    # pymethod.register(username)
    # pymethod.addmoney(username, 100)
    # usernames = '1661065167@test.com'
    # user = pymethod.register(usernames)
    # pymethod.addmoney(user, 10000)
    # pymethod.Binary_options(user).create_granary()
