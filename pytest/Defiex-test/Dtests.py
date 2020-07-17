import requests
import re
import time
import random
import json
import sqlitesave as save
from pymysqlsave import MysqlSave as mysave
from mongosave import TestMongoDB
from CommonMethod import deamds, \
    formatting, context, extract,\
    userlogin, usertoken, gain_url


class supernode(object):

    def __init__(self, granarys_index):
        self.granarys_index = granarys_index

    # 获取实时行情价
    def Get_price(self):
        with save.SqlSave() as execute:
            url = self.Get_url('行情')
            granarys = formatting(execute.select('granary', 'test_msg', 'id', self.granarys_index))
            data = {
                "symbol": granarys
            }

            # 实际行情价格
            comey = deamds(url, data)["LP"]
            # Cmoney = ''.join(re.findall('"LP": "(.*?)",', str(response.text)))
            return comey

    def get_time(self):
        otherStyleTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # print(otherStyleTime)
        return otherStyleTime

    def Get_url(self, urlname: str) -> str:

        with save.SqlSave() as execute:
            url_header_list = execute.select('url', 'environment', 'name', select)
            url_end_list = execute.select('url', 'url', 'urlname', urlname)
            url_header = ''.join(
                [url_header for url_tuple in url_header_list if len(url_header_list) != 0 for url_header in url_tuple])
            url_end = ''.join(
                [url_end for url_tuple in url_end_list if len(url_end_list) != 0 for url_end in url_tuple])
            urls = url_header + url_end
        return urls

    def Get_token(self, name: str) -> str:
        # self.Login(name)
        with save.SqlSave() as execute:
            token = formatting(execute.select('token', 'Name_ResponseMsg', 'name', name))
            return token

    def random_name(self, types: str) -> str:
        # 1手机、2邮箱
        msg = {True: 1, False: 0}[types == '1']
        index = random.randint(100, 9999)
        name = '166' + str(index)
        if msg:
            return name
        else:
            return name + '@test.com'

    # 登录s
    def Login(self, name: str) -> None:

        with save.SqlSave() as execute:

            url = self.Get_url('登录')
            data = execute.select('*', 'general', 'name', name)
            if len(data) == 0:
                # 给予的默认密码
                password = 'b49a9e2a50d24396e08ca047a09588a7'
                execute.general(name, password, select)
        name = data[0][1]
        password = data[0][2]
        data = {
            "username": name,
            "pwd": password
        }
        response = deamds(url, data)
        print(response)
        token = response["info"]["token"]
        userid = response["info"]["userid"]
        invitecode = response["info"]["invitecode"]
        try:
            with save.SqlSave() as execute:
                execute.Name_ResponseMsg(name, userid, token, invitecode, select)
                execute.handle_log('insert->Name_ResponseMsg')
        except:
            with save.SqlSave() as execute:
                execute.update('Name_ResponseMsg', token, name)
                execute.handle_log('update->Name_ResponseMsg')

    # 注册
    def Register(self, sharename: str) -> str:
        with save.SqlSave() as execute:
            msg = execute.join_table(select)
            url = self.Get_url('注册')
            register_type = '2'
            name = self.random_name(register_type)
            # name = names
            # password = 'b49a9e2a50d24396e08ca047a09588a7'
            password = '25d55ad283aa400af464c76d713c07ad'
            shareid = execute.select('userid', 'Name_ResponseMsg', 'name', sharename)
            print(shareid)
            requestcode = execute.select('invitecode', 'Name_ResponseMsg', 'name', sharename)
            share_id = {True: formatting(shareid), False: '0'}[len(shareid) != 0]
            request_code = {True: formatting(requestcode), False: ' '}[len(requestcode) != 0]
            data = {
                "username": name, "type": register_type, "countryid": "191", "pwd": password, "code": msg[0][6],
                "channel": {
                    "plat": "h5", "share_id": share_id, "activityid": "1", "invitecode": request_code
                }
            }
            deamds(url, data)
            execute.multilevel(name, request_code, share_id)
            execute.general(name, password, select)
            execute.handle_log('insert->general')
            message = {
                "Name": name,
                "Password": password,
                "Environment": select
            }

        print('------------')
        self.Login(name)
        return name

    # 获取管理端token
    def admin_token(self) -> str:
        with save.SqlSave() as execute:
            code_msg = execute.join_table(select)
            url = self.Get_url('管理端登录')
            data = {
                "user": code_msg[0][4],
                "pwd": code_msg[0][5]
            }
            response = json.dumps(deamds(url, data))
            login_token = ' '.join(re.findall('"token": "(.*?)"', response))
        return login_token

    # 管理端审核kyc
    def check_kyc(self, name: str) -> str:
        with save.SqlSave() as execute:
            login_token = self.admin_token()
            userid = execute.select('userid', 'Name_ResponseMsg', 'name', name)
            data = {
                "type": 10003,
                "userid": userid[0][0],
                "state": 0, "token": login_token
            }
            urls = self.Get_url('管理端kyc审核')
            response = json.dumps(deamds(urls, data))
            msg = ' '.join(re.findall('"msg": "(.*?)"', response))
            return msg

    # kyc认证
    def kyc(self, name: str) -> str:
        self.Login(name)
        with save.SqlSave() as execute:
            url = self.Get_url('kyc')
            token_msg = execute.select('token', 'Name_ResponseMsg', 'name', name)
            # ,"idimg2":"https://test.trade.idefiex.com/api/pic/downloadimgkyc.do?134.jpg","idimg3":"https://test.trade.idefiex.com/api/pic/downloadimgkyc.do?134.jpg"}
            data = {
                "token": token_msg[0][0], "countryid": "44",
                "idtype": "2", "name": "1128222", "idnumber": name,
                "idimg1": "https://test.trade.idefiex.com/api/pic/downloadimgkyc.do?134.jpg",
                "idimg2": "https://test.trade.idefiex.com/api/pic/downloadimgkyc.do?134.jpg",
                "idimg3": "https://test.trade.idefiex.com/api/pic/downloadimgkyc.do?134.jpg"
            }
            response = json.dumps(deamds(url, data))
            state = ' '.join(re.findall('"state": "(.*?)"', response))
        return state

    # 超级节点申请
    def super_apply(self, name: str) -> str:
        with save.SqlSave() as execute:
            url = self.Get_url('超级节点申请')
            # token_msg = execute.select('token','Name_ResponseMsg','name',name)
            code_msg = execute.join_table(select)
            data = {
                "token": self.Get_token(name),
                "code": code_msg[0][6]
            }
            response = json.dumps(deamds(url, data))
            msg = ' '.join(re.findall('"msg":"(.*?)"', response))
        return msg

    # 管理端添加money
    def add_money(self, name: str, money: int) -> str:
        self.Login(name)
        moneys = money * 100
        # reward 1:赠金 0:现金
        reward = '0'
        with save.SqlSave() as execute:
            urls = self.Get_url('管理端添加money')
            userid = formatting(execute.select('userid', 'Name_ResponseMsg', 'name', name))
            print(userid)
            data = {
                "type": 10201, "userid": userid,
                "money": str(moneys), "remark": "测试",
                "token": self.admin_token(), "reward": reward
            }
            response = json.dumps(deamds(urls, data))
            msg = extract('msg', response)
            return msg

    # 超级节点申请流程
    def SuperNode(self) -> None:
        name = self.Register('')
        with save.SqlSave() as execute:
            msg = self.super_apply(name)
            old_msg = execute.select('msg', 'supermsg', 'explain', 'kyc未认证')
            msgs = {True: 1, False: 0}[msg == old_msg[0][0]]
            if msgs:
                state = self.kyc(name)
            msgs = {True: 1, False: 0}[state == '2']
            if msgs:
                msg = self.check_kyc(name)
            msgs = {True: 1, False: 0}[msg == 'OK']
            if msgs:
                msg = self.super_apply(name)
            old_msg = execute.select('msg', 'supermsg', 'explain', '资金不足')
            msgs = {True: 1, False: 0}[msg == old_msg[0][0]]
            if msgs:
                msg = self.add_money(name, 20000)
            msgs = {True: 1, False: 0}[msg == 'OK']
            if msgs:
                self.super_apply(name)
            execute.supernode(name, select)
            execute.handle_log('insert->supernode')

    # 分页查询所有持仓记录
    def keep_granary(self, name: str) -> str:

        url = self.Get_url('分页查询所有持仓记录')
        data = {
            "token": self.Get_token(name),
            "page": "1", "count": "20"
        }
        response = json.dumps(deamds(url, data))
        try:
            totalcount = ''.join(re.findall('"totalcount": "(.*?)",', response))
            return totalcount
        except:
            pass

    # 分页查询所有平仓记录
    def flatgranary_record(self, name: str) -> str:

        url = self.Get_url('分页查询所有平仓记录')
        data = {
            "token": self.Get_token(name),
            "page": "1", "count": "20", "symbol": ""
        }
        response = json.dumps(deamds(url, data))
        try:
            totalcount = ''.join(re.findall('"totalcount": "(.*?)",', response))
            return totalcount
        except:
            pass

    def formula(self, name: str):
        with save.SqlSave() as execute:
            message = execute.select('*', 'test_msg', 'id', self.granarys_index)
            spratio_ratio = float(message[0][1])
            slratio_ratio = float(message[0][2])
            create_money = float(message[0][3])
            pry = float(message[0][4])
            formalities_ratio = float(message[0][5])
            granary = message[0][7]

            url = self.Get_url('行情')
            granarys = formatting(execute.select('granary', 'test_msg', 'id', self.granarys_index))
            data = {
                "symbol": granarys
            }
            response = json.dumps(deamds(url, data))
            # print(response.text)
            # 实际行情价格
            Cmoney = ''.join(re.findall('"LP": "(.*?)",', response))
            direction = formatting(execute.select('direction', 'test_msg', 'id', self.granarys_index))

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
                # print(count_monry,spot,spot1)
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
                # print(count_monry,spot,spot1)
                return round(spot, 4), round(spot1, 4), str(count_monry)

            # execute.test_msg(spratio_ratio,slratio_ratio,create_money,pry,formalities_ratio,'2')

    # 预计止盈止损
    def predict_money(self, name: str) -> None:
        with save.SqlSave() as execute:
            message = execute.select('*', 'test_msg', 'id', self.granarys_index)
            spratio_ratio = float(message[0][1])
            slratio_ratio = float(message[0][2])
            create_money = float(message[0][3])
            pry = float(message[0][4])
            direction = formatting(execute.select('direction', 'test_msg', 'id', self.granarys_index))
            formalities_ratio = float(message[0][5])
            # "spprice": "8875.85"
            # "openprice": "8837.37"
            spot, spot1, count_monry = self.formula(name)
            # spot = 43.565
            # spot1 = 43.262
            # count_monry = '43.374'
            # 盈利
            if direction == '2':
                # print((float(count_monry) * create_money * pry))
                sort_monry = ((spot - float(count_monry)) / float(count_monry)) * create_money * pry - (
                        formalities_ratio * pry * create_money) - 0.0
                desc_money = ((float(count_monry) - spot1) / float(count_monry)) * create_money * pry + (
                        formalities_ratio * pry * create_money) + 0.0
                # print((float(count_monry) - spot1))
                print(sort_monry, desc_money)
            else:
                # print((float(count_monry) * create_money * pry))
                sort_monry = ((float(count_monry) - spot) / float(count_monry)) * create_money * pry - (
                        formalities_ratio * pry * create_money) - 0.0
                desc_money = ((spot1 - float(count_monry)) / float(count_monry)) * create_money * pry + (
                        formalities_ratio * pry * create_money) + 0.0
                print(sort_monry, desc_money)

    def fund_predict_money(self, name: str) -> None:
        with save.SqlSave() as execute:
            message = execute.select('*', 'test_msg', 'id', self.granarys_index)
            spratio_ratio = float(message[0][1])
            slratio_ratio = float(message[0][2])
            create_money = float(message[0][3])
            pry = float(message[0][4])
            direction = formatting(execute.select('direction', 'test_msg', 'id', self.granarys_index))
            formalities_ratio = float(message[0][5])
            # "spprice": "8875.85"
            # "openprice": "8837.37"
            spot, spot1, count_monry = self.formula(name)
            spot = 43.237
            spot1 = 8954.73
            count_monry = '43.396'
            # 盈利
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

    # #实际赚取
    def gainmonry(self, name: str) -> float:
        # 数量 = 建仓花费 * 杠杠 / 建仓价 
        # gain = （行情价 - 建仓价） * 数量
        with save.SqlSave() as execute:
            create_pricelist = execute.select('openprice', 'granary', 'name', name)
            create_price = float(create_pricelist[len(create_pricelist) - 1][0])
            # print(create_price)
            message = execute.select('*', 'test_msg', 'id', self.granarys_index)
            create_money = float(message[0][3])
            pry = float(message[0][4])
            count = (create_money * pry) / create_price
            # print(count)
            url = self.Get_url('行情')
            granarys = formatting(execute.select('granary', 'test_msg', 'id', self.granarys_index))
            data = {
                "symbol": granarys
            }
            response = json.dumps(deamds(url, data))
            # 实际行情价格
            Cmoney = float(''.join(re.findall('"LP": "(.*?)",', response)))
            # Cmoney = 221.63
            if message[0][6] == '1':
                gain = (create_price - Cmoney) * count
            else:
                gain = (Cmoney - create_price) * count
            # print(gain)

            return gain

    # 赠金建仓
    def fund_granary(self, name: str) -> None:
        # self.Login(name)
        # self.flat_granary(name)
        with save.SqlSave() as execute:
            message = execute.select('*', 'test_msg', 'id', self.granarys_index)
            spratio_ratio = float(message[0][1])
            slratio_ratio = float(message[0][2])
            create_money = float(message[0][3])
            pry = float(message[0][4])
            formalities_ratio = float(message[0][5])
            url = self.Get_url('行情')
            granarys = formatting(execute.select('granary', 'test_msg', 'id', self.granarys_index))
            data = {
                "symbol": granarys
            }
            response = json.dumps(deamds(url, data))
            # 实际行情价格
            Cmoney = float(''.join(re.findall('"LP": "(.*?)",', response)))
            direction = formatting(execute.select('direction', 'test_msg', 'id', self.granarys_index))
            if direction == '1':
                count_monry = round(float(Cmoney) * (1.0 - 0.0008), 4)
                spot = count_monry - (spratio_ratio * create_money + 0.0) * (count_monry / (pry * create_money))
                spot1 = count_monry + (slratio_ratio * create_money - 0.0) * (count_monry / (pry * create_money))
                print(count_monry, spot, spot1)
            elif direction == '2':
                count_monry = round(float(Cmoney) * (1.0 + 0.0008), 4)
                spot = count_monry + (spratio_ratio * create_money + 0.0) * (count_monry / (pry * create_money))
                spot1 = count_monry - (slratio_ratio * create_money - 0.0) * (count_monry / (pry * create_money))
                print(count_monry, spot, spot1)

            urls = self.Get_url('赠金建仓')
            granarys = formatting(execute.select('granary', 'test_msg', 'id', self.granarys_index))
            directions = formatting(execute.select('direction', 'test_msg', 'id', self.granarys_index))
            # money,money2,cmoney = self.formula(name)
            top_money = str(spot)
            data = {
                "token": self.Get_token(name), "symbol": granarys,
                "type": directions, "amount": str(create_money),
                "lever": str(pry), "topprice": top_money
            }
            response = json.dumps(deamds(urls, data))
            orderid = extract('orderid', response)
            balanceold = extract('balanceold', response)
            balance = extract('balance', response)
            openprice = extract('openprice', response)
            openfee = extract('openfee', response)
            forceprice = extract('forceprice', response)
            spratio = extract('spratio', response)
            spprice = extract('spprice', response)
            slratio = extract('slratio', response)
            slprice = extract('slprice', response)
            execute.granary(name, granarys, orderid, select,
                            balanceold, balance, openprice,
                            openfee, forceprice, directions
                            )
            # time.sleep(5)

    # 现金建仓
    def create_granary(self, name: str) -> None:
        print('------------')
        self.Login(name)
        with save.SqlSave() as execute:
            urls = self.Get_url('建仓')
            # granary = ['btc','eth','eos','ltc','bch','etc','xrp','bsv']
            granarys = formatting(
                execute.select(
                    'granary', 'test_msg', 'id', self.granarys_index
                )
            )
            # 1空2多
            # direction = ['1','2'] 
            directions = formatting(
                execute.select(
                    'direction', 'test_msg', 'id', self.granarys_index
                )
            )
            # index = random.randint(0,7)
            # indexs = random.randint(0,1)
            money, money2, cmoney = self.formula(name)
            # indexs = 1
            message = execute.select(
                '*', 'test_msg', 'testcase', self.granarys_index
            )
            amount = message[0][3]
            lever = message[0][4]
            top_money = str(float(money))
            bot_money = str(float(money2))
            # print(top_money,bot_money)
            data = {
                "token": self.Get_token(name), "symbol": granarys, "type": directions,
                "amount": amount, "lever": lever, "topprice": top_money,
                "botprice": bot_money
            }
            response = json.dumps(deamds(urls, data))
            orderid = extract('orderid', response)
            balanceold = extract('balanceold', response)
            balance = extract('balance', response)
            openprice = extract('openprice', response)
            openfee = extract('openfee', response)
            forceprice = extract('forceprice', response)
            spratio = extract('spratio', response)
            spprice = extract('spprice', response)
            slratio = extract('slratio', response)
            slprice = extract('slprice', response)
            message = execute.select(
                '*', 'test_msg', 'id', self.granarys_index
            )
            print(openprice, cmoney)
            if openprice == cmoney:
                testcase2 = {True: 1, False: 0}[message[0][1] == spratio]
                testcase3 = {True: 1, False: 0}[message[0][2] == spprice]
                testcase4 = {True: 1, False: 0}[message[0][3] == slratio]
                testcase5 = {True: 1, False: 0}[message[0][4] == slprice]
                testcase6 = {True: 1, False: 0}[orderid == cmoney]
                testcase_msg = {True: 'True', False: 'False'}[
                    testcase2 == testcase3 == testcase4 == testcase5 == testcase6]
                msg = '{},{}'.format(orderid, cmoney)
                execute.testcase(testcase_msg, msg)
            else:
                pass
            execute.granary(name, granarys, orderid, select,
                            balanceold, balance, openprice,
                            openfee, forceprice, directions
                            )

    #
    def select_msg(self, name: str) -> None:
        with save.SqlSave() as execute:
            orderid_list = execute.select('orderid', 'granary', 'name', name)
            url = 'http://47.90.62.21:9003/api/trade/queryholdorder.do?p={"token":"' + self.Get_token(
                name) + '","orderid":"' + orderid_list[len(orderid_list) - 1][0] + '"}'
            response = requests.get(url)
            print(response.text)
            # 资金费用
            fundfee = self.extract('"fundfee": "(.*?)",', response)
            # 建仓费用
            openprice = self.extract('"openprice":"(.*?)",', response)

    # 平仓
    def flat_granary(self, name: str) -> None:
        # self.Login(name)
        with save.SqlSave() as execute:
            url = self.Get_url('平仓')
            orderid_list = execute.select('orderid', 'granary', 'name', name)
            # token_msg = execute.select('token','Name_ResponseMsg','name',name)
            msg = {True: 1, False: 0}[len(orderid_list) != 0]
            orderid = orderid_list[len(orderid_list) - 1][0]
            data = {
                "token": self.Get_token(name),
                "orderid": orderid
            }
            response = json.dumps(deamds(url, data))
            # execute.delete('granary','orderid',orderid[0])
            # print(response.text)
            pl = extract('pl', response)
            print(orderid, pl, self.gainmonry(name))

    # 修改止盈止损
    def update_ratio(self, name: str) -> None:
        self.Login(name)
        # self.fund_granary(name)
        # self.create_granary(name)
        with save.SqlSave() as execute:
            # self.create_granary(name)
            url = self.Get_url('修改止盈止损')
            orderid_list = execute.select('orderid', 'granary', 'name', name)
            openprice_list = execute.select('openprice', 'granary', 'name', name)
            # token_msg = execute.select('token','Name_ResponseMsg','name',name)
            forceprice_list = execute.select('forceprice', 'granary', 'name', name)
            direction_list = execute.select('direction', 'granary', 'name', name)
            # top_money = float(forceprice_list[len(forceprice_list) - 1][0]) - 6.0
            if direction_list[len(direction_list) - 1][0] == '1':
                top_money = float(openprice_list[len(openprice_list) - 1][0]) - 20.0
                bot_money = float(forceprice_list[len(forceprice_list) - 1][0]) + 9.0
            else:
                top_money = float(openprice_list[len(openprice_list) - 1][0]) + 20.0
                bot_money = float(forceprice_list[len(forceprice_list) - 1][0]) + 9.0
            data = {
                "token": self.Get_token(name), "orderid": orderid_list[len(orderid_list) - 1][0],
                "topprice": str(top_money), "botprice": str(bot_money)
            }
            response = json.dumps(deamds(url, data))

    # 多级关系建立->3
    def broker_invite(self) -> None:
        self.Register(self.Register(self.Register('')))

    # 金额比例验证
    def count(self, name: str) -> None:
        url = self.Get_url('行情')
        data = {
            "symbol": "btc"
        }
        response = json.dumps(deamds(url, data))
        # 实际行情价格
        Cmoney = extract('LP', response)
        self.create_granary(name)
        with save.SqlSave() as execute:
            openprice = execute.select('openprice', 'granary', 'name', name)
            # print(openprice[len(openprice)-1][0])
            # 建仓价格
            realmonry = float(openprice[len(openprice) - 1][0])
            # print(float(openprice[len(openprice)-1][0]) - float(Cmoney))
            # price = realmonry - float(Cmoney)
            direction = execute.select('direction', 'granary', 'name', name)
            if direction[len(direction) - 1][0] == '1':
                count_monry = float(Cmoney) * (1.0 - 0.0002)
            else:
                count_monry = float(Cmoney) * (1.0 + 0.0002)
            # 验证点差
            testcase1 = {True: 1, False: 0}[realmonry == round(count_monry, 2)]
            # print(realmonry,round(count_monry,2))
            # print(testcase1)
            if testcase1 == 1:
                state = 'True'
                msg = "{} = {}".format(realmonry, round(count_monry, 2))
                execute.testcase(state, msg)
            else:
                state = 'False'
                msg = "真实:{},建仓:{},计算:{}".format(Cmoney, realmonry, round(count_monry, 2))
                execute.testcase(state, msg)

    # 现金限价建仓
    def current_granary(self, name: str, types: str) -> None:
        # self.Login(name)
        with save.SqlSave() as execute:
            message = execute.select('*', 'test_msg', 'testcase', self.granarys_index)
            symobl = message[0][7]
            direction = message[0][6]
            amount = message[0][3]
            lever = message[0][4]
            price = self.Get_price()
            # select 参数 1:限价单 2：强制转换的市价单
            typeselect = int(types)
            if typeselect == 2:
                if direction == '1':
                    # 2涨，1跌
                    price_money = str(float(price) - 0.1)
                elif direction == '2':
                    print(float(price))
                    price_money = str(float(price) + 0.1)
                print(price, price_money)
                url = self.Get_url('现金限价建仓')
                data = {
                    "token": self.Get_token(name), "symbol": symobl, "type": direction,
                    "amount": amount, "lever": lever, "price": price_money
                }
                response = json.dumps(deamds(url, data))
                orderid = extract('orderid', response)
                balanceold = extract('balanceold', response)
                balance = extract('balance', response)
                openprice = extract('openprice', response)
                openfee = extract('openfee', response)
                forceprice = extract('forceprice', response)
                spratio = extract('spratio', response)
                spprice = extract('spprice', response)
                slratio = extract('slratio', response)
                slprice = extract('slprice', response)
                execute.granary(name, symobl, orderid, select, balanceold,
                                balance, openprice, openfee, forceprice, direction)

            elif select == 1:
                if direction == '1':
                    price_money = str(float(price) + 0.1)
                elif direction == '2':
                    price_money = str(float(price) - 0.1)
                # self.Login(name)
                print(price, price_money)
                url = self.Get_url('现金限价建仓')
                data = {
                    "token": self.Get_token(name), "symbol": symobl,
                    "type": direction, "amount": amount, "lever": lever,
                    "price": price_money
                }
                response = json.dumps(deamds(url, data))
                orderid = extract('orderid', response)
                balanceold = extract('balanceold', response)
                balance = extract('balance', response)
                wttime = extract('wttime', response)
                # curprice = self.extract('"curprice": "(.*?)"',response)
                execute.current_granary(name, balanceold, balance, orderid, wttime, price_money, message[0][8])

    # 分页查询所有限价单记录
    def Select_CurrentGranary(self, name: str) -> None:
        # self.Login(name)
        url = self.Get_url('分页查询所有限价单记录')
        data = {
            "token": self.Get_token(name),
            "page": "1", "count": "20"
        }
        response = json.dumps(deamds(url, data))

    # 限价单撤单
    def delete_CurrentGranary(self, name: str) -> None:
        self.Login(name)
        url = self.Get_url('限价单撤单')
        with save.SqlSave() as execute:
            orderid = formatting(execute.select('orderid', 'current_granary', 'name', name))
            print(orderid)
            data = {
                "token": self.Get_token(name),
                "orderid": orderid
            }
            response = json.dumps(deamds(url, data))

    # 余额、冻结赠金
    def get_frostmoney(self, name: str) -> None:
        self.Login(name)
        url = self.Get_url('获取冻结赠金')
        data = {
            "token": self.Get_token(name)
        }
        response = json.dumps(deamds(url, data))

    # 获取存储充币地址
    def get_TopUpSite(self, name: str) -> None:
        # 币种类型 1:OMNI_USDT 3:ERC20_USDT …
        site_list = ['1', '3', '4']
        site_msg = []
        # site_type = '3'
        url = self.Get_url('获取充币地址')
        for site_type in site_list:
            data = {
                "token": self.Get_token(name),
                "type": site_type
            }
            response = json.dumps(deamds(url, data))
            addr = extract('addr', response)
            site_msg.append(addr)
        with save.SqlSave() as execute:
            execute.TopUpSite(name, site_msg[1], site_msg[0], site_msg[2])

    # 提币以及信息获取
    def Withdraw_msg(self, name: str) -> None:
        self.Login(name)
        # ERC-20
        addr = '0x777D76e24da310D91B0C3b48767E898772F198F7'
        money_type = '3'
        # OMNI
        # addr = '3EkaqUNdowvetHDzkYgA6woXcBRkPuULRT'
        # money_type = '1'

        url = self.Get_url('提币')
        amount = '2'
        data = {
            "token": self.Get_token(name), "type": money_type,
            "amount": amount, "addr": addr, "code": "xwwwwx"
        }
        response = json.dumps(deamds(url, data))
        bank_order_id = extract('bank_order_id', response)
        admin_url = self.Get_url('管理端审核提币')
        admin_data = {
            "type": 10204, "orderid": bank_order_id,
            "verify": 1, "token": self.admin_token()
        }
        admin_response = json.dumps(deamds(admin_url, admin_data))
        time.sleep(20)
        self.Withdraw_recode(name)

    # 获取提币纪录
    def Withdraw_recode(self, name: str) -> None:
        self.Login(name)
        url = self.Get_url('获取提币纪录')
        # http://47.90.62.21:9003/api/trade/queryoutorderall.do?p={"page":"1","count":"20"}
        data = {
            "token": self.Get_token(name),
            "page": "1", "count": "20"
        }
        response = json.dumps(deamds(url, data))
        txid = extract('txid', response)
        with save.SqlSave() as execute:
            execute.Withdraw_recod(name, txid)

    # 获取充值纪录
    def Top_msg(self, name: str) -> None:
        url = self.Get_url('获取充值纪录')
        data = {
            "token": self.Get_token(name),
            "page": "1", "count": "20"
        }
        response = json.dumps(deamds(url, data))

    # 分享图盈亏百分比计算
    def share_count(self):
        pass


# 经纪人接口类
class Broker(object):
    # 查询经纪人汇总信息
    def select_broker_allmessage(self, brokername: str) -> None:
        url = gain_url('查询经纪人汇总信息')
        data = {
            "token": usertoken(brokername)
        }
        response = json.dumps(deamds(url, data))

    # 查询经纪人每日信息
    def select_broker_everydaymsg(self, brokername: str) -> None:
        url = gain_url('查询经纪人每日信息')
        data = {
            "token": usertoken(brokername)
        }
        response = json.dumps(deamds(url, data))

    # 查询经纪人返利金额的可取余额
    def select_broker_canmoney(self, brokername: str) -> None:
        url = gain_url('查询经纪人返利金额的可取余额')
        data = {
            "token": usertoken(brokername)
        }
        response = json.dumps(deamds(url, data))

    # 返佣提现到交易账户余额
    def brokerage_turn_balance(self, brokername: str) -> None:
        url = gain_url('返佣提现到交易账户余额')
        data = {
            "token": usertoken(brokername)
        }
        response = json.dumps(deamds(url, data))

    # 查询经纪人的提拥流水
    def brokerage_water(self, brokername: str) -> None:
        url = gain_url('返佣提现到交易账户余额')
        data = {
            "token": usertoken(brokername),
            "page": "1", "count": "20"
        }
        response = json.dumps(deamds(url, data))

    # 查询经纪人的最近注册的好友
    def broker_bull(self, brokername: str) -> None:
        url = gain_url('查询经纪人的最近注册的好友')
        data = {
            "token": usertoken(brokername)
        }
        response = json.dumps(deamds(url, data))

    # 查询经纪人最近时间段各项信息
    def select_broker_timemsg(self, brokername: str) -> None:

        """
        day: 0全部 默认1当天 7当周 30当月
        data : 默认1注册好友 2充值金额 3手续费
        order : 排序方式 默认1降序 2升序
        """
        day, data = '1', '1'
        url = gain_url('查询经纪人最近时间段各项信息')
        datas = {
            "token": usertoken(brokername),
            "day": day, "data": data,
            "order": "1", "page": "1", "count": "20"
        }
        response = json.dumps(deamds(url, datas))

    # 查询经纪人某天返利明细
    def select_someday_message(self, brokername: str) -> None:
        tradedate = '1578499200'
        url = gain_url('查询经纪人某天返利明细')
        data = {
            "token": usertoken(brokername),
            "tradedate": tradedate,
            "page": "1", "count": "20"
        }
        response = json.dumps(deamds(url, data))


# 交易员接口类
class DealStaff(supernode):

    def __init__(self) -> None:
        pass

    # 查询最新资产
    def select_money(self, name: str) -> None:
        url = gain_url('查询最新资产')
        data = {
            "token": self.Get_token(name)
        }
        deamds(url, data)

    # 管理端审核交易员
    def check_trader(self, userid: str, state: str) -> None:
        admin_token = self.admin_token()
        # state 1:审核通过 0:审核失败
        # state = '1'
        url = gain_url('交易员审核')
        data = {
            "type": 10211, "token": admin_token,
            "userid": userid, "state": state
        }
        deamds(url, data)

    # 交易员申请开通
    def apply(self, name: str) -> json:
        url = gain_url('交易员申请开通')
        data = {
            "token": self.Get_token(name),
            "language": "zh_CN"
        }
        response = deamds(url, data)
        return response

    # 交易员详情查询
    def select_detail(self, name: str) -> None:
        with save.SqlSave() as execute:
            userid = formatting(execute.select('userid', 'Name_ResponseMsg', 'name', name))
            url = gain_url('交易员详情查询')
            data = {
                "planerid": userid,
                "language": "zh_CN"
            }
            deamds(url, data)

    # 交易员交易记录查询
    def deal_record(self, name: str) -> None:
        with save.SqlSave() as execute:
            userid = formatting(execute.select('userid', 'Name_ResponseMsg', 'name', name))
        url = gain_url('交易员交易记录查询')
        data = {
            "planerid": userid,
            "page": "1", "count": "20"
        }
        deamds(url, data)

    # 交易员跟单盈利查询
    def deal_gain(self, name: str) -> None:
        with save.SqlSave() as execute:
            userid = formatting(execute.select('userid', 'Name_ResponseMsg', 'name', name))
        url = gain_url('交易员跟单盈利查询')
        data = {
            "planerid": userid,
            "page": "1", "count": "20"
        }
        deamds(url, data)

    # 交易员列表查询
    def trader_list(self):
        url = gain_url('交易员列表查询')
        data = {
            "ordertype": "1"
        }
        planerid_str = json.dumps(deamds(url, data))
        planerid_list = re.findall('"planerid": "(.*?)"', planerid_str)
        return planerid_list

    # 用户跟单某个交易员
    def user_trader(self, name: str, planerid: str, referrerid: str):
        opentype = '1'
        openamount = '50'
        openamountdaymax = '500'
        openamountholdmax = '1000'
        openamountslrate = '0.5'
        url = gain_url('用户跟单某个交易员')
        data = {
            "token": self.Get_token(name), "planerid": planerid, "referrerid": referrerid,
            "opentype": opentype, "openamount": openamount, "openamountdaymax": openamountdaymax,
            "openamountholdmax": openamountholdmax, "openamountslrate": openamountslrate
        }
        deamds(url, data)

    # 用户跟单详情查询
    def user_detail(self, name: str):
        url = gain_url('用户跟单详情查询')
        data = {
            "token": self.Get_token(name)
        }
        deamds(url, data)

    # 用户修改跟单参数
    def user_remove_parameter(self, name: str, planerid: str):
        # 是否暂停1: 是0: 否
        pause = '1'
        openamount = '500'
        openamountdaymax = '1000'
        openamountholdmax = '2000'
        openamountslrate = '0.5'
        url = gain_url('用户修改跟单参数')
        data = {
            "token": self.Get_token(name),
            "planerid": planerid, "pause": pause, "opentype": "1",
            "openamount": openamount, "openamountdaymax": openamountdaymax,
            "openamountholdmax": openamountholdmax, "openamountslrate": openamountslrate
        }
        deamds(url, data)

    # 用户取消跟单某个交易员
    def cancel_deal(self, name: str, planerid: str):
        url = gain_url('用户取消跟单某个交易员')
        data = {
            "token": self.Get_token(name),
            "planerid": planerid
        }

        deamds(url, data)

    # 用户跟单历史查询
    def user_deal_history(self, name, planerid):
        url = gain_url('用户跟单历史查询')
        data = {
            "token": self.Get_token(name),
            "planerid": planerid
        }
        deamds(url, data)

    # 交易员修改信息
    def trader_remove_message(self, name, types: str):
        url = gain_url('交易员修改信息')
        # 1: 确认跟单规则 2: 带单开关 3: 个人描述 4: 标签
        # types = '2'
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
            info = 'AAABBBCCCDDDEEEFFFGGGHHHIIIJJJKKKVVVLLLMMM'
        print(info)
        data = {
            "token": self.Get_token(name),
            "type": types, "info": info
        }
        deamds(url, data)

    # 交易员跟单提成每日汇总查询
    def trader_everyday_royalties(self, name):
        url = gain_url('交易员跟单提成每日汇总查询')
        data = {
            "token": self.Get_token(name),
            "page": "1", "count": "20"
        }
        deamds(url, data)

    # 交易员跟单提成每日明细查询
    def everyday_detail(self, name, timestamp):
        url = gain_url('交易员跟单提成每日明细查询')
        data = {
            "token": self.Get_token(name),
            "tradedate": timestamp
        }
        deamds(url, data)

    # 推荐人详情查询
    def referrer_detail(self, name):
        url = gain_url('推荐人详情查询')
        data = {
            "token": self.Get_token(name)
        }
        deamds(url, data)

    # 推荐人跟单用户信息查询
    def referrer_user_detail(self, name):
        url = gain_url('推荐人跟单用户信息查询')
        data = {
            "token": self.Get_token(name)
        }
        deamds(url, data)

    # 推荐人每日提成汇总信息查询
    def referrer_everyday_collect(self, name):
        url = gain_url('推荐人每日提成汇总信息查询')
        data = {
            "token": self.Get_token(name)
        }
        deamds(url, data)

    # 推荐人每日提成明细查询
    def referrer_everyday_deduct(self, name, tradedate):
        url = gain_url('推荐人每日提成明细查询')
        data = {
            "token": self.Get_token(name),
            "tradedate": tradedate
        }
        deamds(url, data)

    # 交易员标签信息查询
    def trader_label(self):
        url = gain_url('交易员标签信息查询')
        data = {}
        deamds(url, data)


# 交易员
def dealtest1():
    deal = DealStaff()
    run = supernode('1')
    name = run.Register('')
    time.sleep(2)
    # 0: 申请成功 1851: 余额不足 1852: kyc没通过 1853: 正在跟单别的交易员 1854: 已开通 1855: 审核中
    # 开通流程
    if deal.apply(name)["code"] == '1851':
        run.add_money(name, 50)
        if deal.apply(name)["code"] == '1852':
            run.kyc(name)
            run.check_kyc(name)
            deal.apply(name)
            run.get_frostmoney(name)
    # 验证申请成功后列表是否存在
    trader = deal.trader_list()
    with save.SqlSave() as execute:
        userid = formatting(execute.select('userid', 'Name_ResponseMsg', 'name', name))
        if userid in trader:
            # 审核通过
            state = '1'
            deal.check_trader(userid, state)
            execute.trader(name, userid, select, state)


# 用户、交易员、推荐人三级关系建立
def dealtest4():
    deal = DealStaff()
    run = supernode('1')
    # 1、注册三个新账户分别拿出name、userid
    name_dict = {}
    for index in range(3):
        with save.SqlSave() as executes:
            name = run.Register('')
            userid = formatting(executes.select('userid', 'Name_ResponseMsg', 'name', name))
            name_dict[index] = [name, userid]
    print(name_dict)
    with save.SqlSave() as executes:
        executes.trader_test(
            name_dict[0][0], name_dict[0][1],
            name_dict[1][0], name_dict[1][1],
            name_dict[2][0], name_dict[2][1]
        )
    # deal.check_trader(dealid, '1')


# 用户、交易员、推荐人三级关系操作
def dealtest5():
    deal = DealStaff()
    run = supernode('1')
    with save.SqlSave() as executes:
        name_list = executes.trader_test_select('1', 'trader_test')
        user = name_list[0][1]
        userid = name_list[0][2]
        dealuser = name_list[0][3]
        dealuserid = name_list[0][4]
        recommenduser = name_list[0][5]
        recommenduserid = name_list[0][6]
        # deal.add_money(user, 1000000)
        # deal.add_money(dealuser, 1000000)
        # deal.add_money(recommenduser, 1000000)
        # deal.apply(dealuser)
        # run.kyc(dealuser)
        # run.check_kyc(dealuser)
        # deal.check_trader(dealuserid, '1')
        # deal.trader_list()
        # deal.select_detail(dealuser)
        # 跟单
        # deal.user_trader(user, dealuserid, recommenduserid)
        # deal.referrer_detail(recommenduser)
        # deal.referrer_user_detail(recommenduser)

        # 交易员建平仓
        run.create_granary(dealuser)
        # time.sleep(3)
        # run.flat_granary(dealuser)

        # 交易员信息查询
        # deal.trader_everyday_royalties(dealuser)
        # deal.everyday_detail(dealuser, '1593744020')
        # deal.deal_record(dealuser)
        # deal.deal_gain(dealuser)
        # deal.trader_label()
        # deal.trader_remove_message(dealuser)
        # deal.select_detail(dealuser)

        # 用户跟单信息
        # deal.user_deal_history(user, userid)
        # deal.user_detail(user)

        # 用户修改跟单操作
        # deal.user_remove_parameter(user, userid)

        # 推荐人信息查询
        # deal.referrer_detail(recommenduser)
        # deal.referrer_user_detail(recommenduser)
        # deal.referrer_everyday_collect(recommenduser)
        # deal.referrer_everyday_deduct(recommenduser, '1593744020')

        # 查询持仓、平仓记录
        # time.sleep(2)
        # deal.deal_gain(dealuser)
        # run.keep_granary(user)
        # run.flatgranary_record(user)
        # run.keep_granary(dealuser)
        # run.flatgranary_record(dealuser)


# 用户跟单交易员
def dealtest2():
    deal = DealStaff()
    run = supernode('1')
    withname = '389863294@qq.com'
    planerid = '12241273568'
    referrerid = '0'
    deal.user_trader(withname, planerid, referrerid)
    deal.trader_list()
    deal.cancel_deal(withname, planerid)
    deal.user_remove_parameter(withname, planerid)
    deal.user_detail(withname)


# 交易员信息修改
def dealtest3():
    deal = DealStaff()
    run = supernode('1')
    # withname = '389863294@qq.com'
    # run.kyc()
    # run.Login(withname)
    # dealname = '166453511870@qq.com'
    # deal.trader_remove_message(dealname)
    # userid = '12241273568'
    # deal.trader_label()
    # deal.select_detail(withname)
    # deal.check_trader(userid)


# 特定经纪人比例
def broker():
    deal = DealStaff()
    run = supernode('1')
    bro = Broker()
    # brokername = '166437696110@qq.com'
    # run.Register(brokername)
    # run.Withdraw_msg()
    run.SuperNode()



# 限价单转市价单--->平仓
def test1():
    for index in range(1, 9):
        run = supernode(str(index))
        name = run.Register('')
        run.add_money(name)
        # run.create_granary(name)
        types = 2
        run.current_granary(name, types)
        time.sleep(3)
        run.flat_granary(name)


# 限价委托单--->撤单
def test2():
    for index in range(1, 9):
        run = supernode(str(index))
        name = run.Register('')
        run.add_money(name)
        types = 1
        run.current_granary(name, types)
        time.sleep(3)
        run.delete_CurrentGranary(name)


def TestCreate():
    name = '166971840546@qq.com'
    for index in range(1, 9):
        run = supernode(str(index))
        run.create_granary(name)
        # run.Register('')
        # run.flatgranary_record(name)
        time.sleep(3)
        # run.current_granary(name)
        # time.sleep(3)
        # run.fund_granary(name)


if __name__ == "__main__":
    select = context()
    # run.create_granary(name)
    # dealtest3()
    broker()
    # dealtest1()
    # dealtest3()
    # dealtest4()
    # dealtest5()
    # name = '389863294@qq.com'

    # run = supernode('1')
    # for index in range(10):
        # name = 'preview' + str(index) + '@test.com'
        # run.add_money(name, 10000)
        # run.Register('', name)
        # time.sleep(1)

    # run.Login('166704969518@qq.com')
    # run = supernode('1')
    # run.Login(name)
    # run.Register('')
    # run.add_money(name, 1000)
    # run.create_granary(name)
