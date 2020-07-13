import CommonMethod as pymethod
import json
import random
import re
import pymysqlsave as mysave
import time


# 交易员接口类
class DealStaff(object):

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
    def user_trader(self, name: str, planerid: str, referrerid: str):
        opentype = '1'
        openamount = '50'
        openamountdaymax = '500'
        openamountholdmax = '1000'
        openamountslrate = '0.5'
        url = pymethod.gain_url('用户跟单某个交易员')
        data = {
            "token": pymethod.usertoken(name), "planerid": planerid, "referrerid": referrerid,
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
        pymethod.addmoney(username, 50)
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
    deal = DealStaff()
    username = '389863294@qq.com'
    trader = '1664001394@test.com'
    referrer = '389863294@qq.com'
    # deal.select_detail(username)
    username1 = '1661996720@test.com'
    # pymethod.addmoney(username1, 10000)
    # username2 = '1662909762@test.com'
    # deal.user_detail(username1)
    # pymethod.create_granary(username)
    # pymethod.register(username)
    levername = '1662558092@test.com'

    # pymethod.addmoney(levername, 100000000)
    # pymethod.create_granary(levername)
    # pymethod.register('')
    # deal.user_trader(username, '11739860537', '11374499021')
    # deal.user_detail(username)
    # deal.deal_gain(username)

    # deal.everyday_detail(username, '20200709')
    # deal.trader_everyday_royalties(username)
    # print(pymethod.register(''))
    # username = pymethod.register('')
    # pymethod.userlogin(username, 'a12345678')
    # pymethod.addmoney(username, 100000)
    # pymethod.kyc(username)
    # pymethod.checkkyc(username)
    # deal.deal_record(username)
    # deal.trader_remove_message(username)
    # deal.select_detail(username)
    # pymethod.create_granary(username)



    # deal.apply(username)
    # deal.check_trader(username, '1')
    # deal.select_detail(username)
    # deal.trader_label()
    # pymethod.kyc(username)
    # pymethod.checkkyc(username)
    # deal.user_deal_history(username, '14186191497')
    # deal.trader_remove_message(username)


def testcase4():
    deal = DealStaff()
    deal_username = '166669752@test.com'
    deal_userid = '13660864396'
    new_username = '166415477@test.com'
    # deal.user_trader(new_username, deal_userid, '')
    # pymethod.addmoney(deal_username, 10000)
    # pymethod.create_granary(deal_username)
    tj_username = '1661863403@test.com'
    username = '1665029587@test.com'
    # pymethod.create_granary(deal_username)
    

if __name__ == "__main__":
    # traderuser()
    # pymethod.userlogin('18770185021', 'yangxun19990728')
    # testcase()
    # pymethod.addmoney('1662163795@test.com', 10000)
    # testcase2()
    # testcase3()
    testcase4()
    # pymethod.duserlogin('389863294@qq.com', 'yangxun19990728')
    # pymethod.create_granary('389863294@qq.com')

