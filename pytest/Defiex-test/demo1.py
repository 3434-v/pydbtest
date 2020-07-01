import requests
import re
import time
import datetime
import random
import os.path
import hashlib
import json
import sqlitesave as save

from mongosave import TestMongoDB
from CommonMethod import UnifyWays
# import mongosave.TestMongoDB as TestMongoDB

# 环境选择
pynosql = TestMongoDB('localhost:27017/', 'test_defiex')


class delete_format(object):

    def msg_format(self, msg_list):
        msg = ''.join([msg for msg_tuple in msg_list if len(msg_list) != 0 for msg in msg_tuple])
        return msg


formatting = delete_format()


# class UnifyWay(object):
#
#     def deamd(self, url, data):
#         response = requests.get(url + data)
#         print(url + data)
#         print(response.text)


class supernode(object):

    def __init__(self, granarys_index):
        self.granarys_index = granarys_index

    def extract(self, regular, msg):
        message = ''.join(re.findall(regular, str(msg.text)))
        return message

    # 获取实时行情价
    def Get_price(self):
        with save.SqlSave() as execute:
            url = self.Get_url('行情')
            granarys = formatting.msg_format(execute.select('granary', 'test_msg', 'id', self.granarys_index))
            data = '{"symbol":"' + granarys + '"}'
            urls = url + data
            response = requests.get(urls)
            # 实际行情价格
            Cmoney = ''.join(re.findall('"LP": "(.*?)",', str(response.text)))
            return Cmoney

    def get_time(self):
        otherStyleTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # print(otherStyleTime)
        return otherStyleTime

    def Get_url(self, urlname):

        with save.SqlSave() as execute:
            url_header_list = execute.select('url', 'environment', 'name', select)
            url_end_list = execute.select('url', 'url', 'urlname', urlname)
            url_header = ''.join(
                [url_header for url_tuple in url_header_list if len(url_header_list) != 0 for url_header in url_tuple])
            url_end = ''.join(
                [url_end for url_tuple in url_end_list if len(url_end_list) != 0 for url_end in url_tuple])
            urls = url_header + url_end
        return urls

    def Get_token(self, name):
        # self.Login(name)
        with save.SqlSave() as execute:
            token_msg_list = execute.select('token', 'Name_ResponseMsg', 'name', name)
            token = ''.join(
                token for token_tuple in token_msg_list if len(token_msg_list) != 0 for token in token_tuple)
        return token

    def random_name(self, types):
        # 1手机、2邮箱
        msg = {True: 1, False: 0}[types == '1']
        index = random.randint(100, 999999999)
        name = '166' + str(index)
        if msg:
            return name
        else:
            return name + '@qq.com'

    # 登录
    def Login(self, name):

        with save.SqlSave() as execute:

            url = self.Get_url('登录')
            data = execute.select('*', 'general', 'name', name)
            if len(data) == 0:
                # 给予的默认密码
                password = 'b49a9e2a50d24396e08ca047a09588a7'
                execute.general(name, password, select)
                execute.handle_log('insert->general')
            execute.handle_log('GetTable->url、environment、general')
        name = data[0][1]
        password = data[0][2]
        data = '{"username":"' + name + '","pwd":"' + password + '"}'
        urls = url + data
        response = requests.get(urls)
        # print(response.text)
        token = ' '.join(re.findall('"token": "(.*?)"', str(response.text)))
        userid = ' '.join(re.findall('"userid": "(.*?)"', str(response.text)))
        invitecode = ' '.join(re.findall('"invitecode": "(.*?)"', str(response.text)))
        # sql存储
        # message = {"Name":name,"Userid":userid,"Toekn":token,"Invitecode":invitecode,"Environment":select,"GetTime":self.get_time()}
        # pynosql.update('AccountMessage',name,message)
        # nosql存储
        pynosql.insert('AccountMessage', json.loads(str(response.text)))
        try:
            with save.SqlSave() as execute:
                execute.Name_ResponseMsg(name, userid, token, invitecode, select)
                execute.handle_log('insert->Name_ResponseMsg')
        except:
            with save.SqlSave() as execute:
                execute.update('Name_ResponseMsg', token, name)
                execute.handle_log('update->Name_ResponseMsg')
        # except:
        #     with save.SqlSave() as execute:
        #         url_end = execute.select('url','url','urlname','登录')
        #         url_header = execute.select('url','environment','name',select)
        #         url = url_header[0][0] + url_end[0][0]
        #         password = 'yangxun19990728'

    # 注册
    def Register(self, sharename):
        with save.SqlSave() as execute:
            msg = execute.join_table(select)
            url = self.Get_url('注册')
            # index = random.randint(100,999999999)
            register_type = '2'
            name = self.random_name(register_type)
            password = 'b49a9e2a50d24396e08ca047a09588a7'
            shareid = execute.select('userid', 'Name_ResponseMsg', 'name', sharename)
            print(shareid)
            requestcode = execute.select('invitecode', 'Name_ResponseMsg', 'name', sharename)
            share_id = {True: formatting.msg_format(shareid), False: '0'}[len(shareid) != 0]
            request_code = {True: formatting.msg_format(requestcode), False: ' '}[len(requestcode) != 0]
            data = '{"username":"' + name + '","type":"' + register_type + '","countryid":"191","pwd":"' + password + '","code":"' + \
                   msg[0][6] + '","channel":{"plat":"h5","share_id":"' + share_id + '","activityid":"1","invitecode":"' + request_code + '"}}'
            requests.get(url + data)
            print(url+data)
            execute.multilevel(name, request_code, share_id)
            execute.general(name, password, select)
            execute.handle_log('insert->general')
            message = {"Name": name, "Password": password, "Environment": select}
            pynosql.insert('Register_account', message)
        self.Login(name)
        return name

    # 获取管理端token
    def admin_token(self):
        with save.SqlSave() as execute:
            code_msg = execute.join_table(select)
            urls = self.Get_url('管理端登录')
            data = '{"user":"' + code_msg[0][4] + '","pwd":"' + code_msg[0][5] + '"}'
            response = requests.get(urls + data)
            login_token = ' '.join(re.findall('"token": "(.*?)"', str(response.text)))
        return login_token

    # 管理端审核kyc
    def check_kyc(self, name):
        with save.SqlSave() as execute:
            login_token = self.admin_token()
            userid = execute.select('userid', 'Name_ResponseMsg', 'name', name)
            data = '{"type":10003,"userid":"' + userid[0][0] + '","state":0,"token":"' + login_token + '"}'
            urls = self.Get_url('管理端kyc审核')
            response = requests.get(urls + data)
            msg = ' '.join(re.findall('"msg": "(.*?)"', str(response.text)))
            return msg

    # kyc认证
    def kyc(self, name):
        self.Login(name)
        with save.SqlSave() as execute:
            url = self.Get_url('kyc')
            token_msg = execute.select('token', 'Name_ResponseMsg', 'name', name)
            # ,"idimg2":"https://test.trade.idefiex.com/api/pic/downloadimgkyc.do?134.jpg","idimg3":"https://test.trade.idefiex.com/api/pic/downloadimgkyc.do?134.jpg"}
            data = '{"token":"' + token_msg[0][
                0] + '","countryid":"44","idtype":"2","name":"1128222","idnumber":"' + name + '","idimg1":"https://test.trade.idefiex.com/api/pic/downloadimgkyc.do?134.jpg","idimg2":"https://test.trade.idefiex.com/api/pic/downloadimgkyc.do?134.jpg","idimg3":"https://test.trade.idefiex.com/api/pic/downloadimgkyc.do?134.jpg"}'
            response = requests.get(url + data)
            print(response.text)
            state = ' '.join(re.findall('"state": "(.*?)"', str(response.text)))
        return state

    # 超级节点申请
    def super_apply(self, name):
        with save.SqlSave() as execute:
            url = self.Get_url('超级节点申请')
            # token_msg = execute.select('token','Name_ResponseMsg','name',name)
            code_msg = execute.join_table(select)
            data = '{"token":"' + self.Get_token(name) + '","code":"' + code_msg[0][6] + '"}'
            response = requests.get(url + data)
            print(response.text)
            msg = ' '.join(re.findall('"msg":"(.*?)"', str(response.text)))
        return msg

    # 管理端添加money
    def add_money(self, name, money):
        # self.Login(name)
        moneys = money * 100
        # reward 1:赠金 0:现金
        reward = '0'
        with save.SqlSave() as execute:
            urls = self.Get_url('管理端添加money')
            userid = execute.select('userid', 'Name_ResponseMsg', 'name', name)

            data = '{"type":10201,"userid":"' + userid[0][
                0] + '","money":'+str(moneys)+',"remark":"测试","token":"' + self.admin_token() + '","reward":"'+reward+'"}'
            response = requests.get(urls + data)
            msg = ' '.join(re.findall('msg": "(.*?)"', str(response.text)))
            print(response.text)
            return msg

    # 超级节点申请流程
    def SuperNode(self):
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
    def keep_granary(self, name):

        url = self.Get_url('分页查询所有持仓记录')
        data = '{"token":"' + self.Get_token(name) + '","page":"1","count":"20"}'
        urls = url + data
        response = requests.get(urls)
        try:
            totalcount = ''.join(re.findall('"totalcount": "(.*?)",', str(response.text)))
            return totalcount
        except:
            pass

    # 分页查询所有平仓记录
    def flatgranary_record(self, name):

        url = self.Get_url('分页查询所有平仓记录')
        data = '{"token":"' + self.Get_token(name) + '","page":"1","count":"20","symbol":""}'
        urls = url + data
        response = requests.get(urls)
        try:
            totalcount = ''.join(re.findall('"totalcount": "(.*?)",', str(response.text)))
            return totalcount
        except:
            pass

    def formula(self, name):
        with save.SqlSave() as execute:
            message = execute.select('*', 'test_msg', 'id', self.granarys_index)
            spratio_ratio = float(message[0][1])
            slratio_ratio = float(message[0][2])
            create_money = float(message[0][3])
            pry = float(message[0][4])
            formalities_ratio = float(message[0][5])
            granary = message[0][7]

            url = self.Get_url('行情')
            granarys = formatting.msg_format(execute.select('granary', 'test_msg', 'id', self.granarys_index))
            data = '{"symbol":"' + granarys + '"}'
            urls = url + data
            response = requests.get(urls)
            # print(response.text)
            # 实际行情价格
            Cmoney = ''.join(re.findall('"LP": "(.*?)",', str(response.text)))
            direction = formatting.msg_format(execute.select('direction', 'test_msg', 'id', self.granarys_index))

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
    def predict_money(self, name):
        with save.SqlSave() as execute:
            message = execute.select('*', 'test_msg', 'id', self.granarys_index)
            spratio_ratio = float(message[0][1])
            slratio_ratio = float(message[0][2])
            create_money = float(message[0][3])
            pry = float(message[0][4])
            direction = formatting.msg_format(execute.select('direction', 'test_msg', 'id', self.granarys_index))
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

    def fund_predict_money(self, name):
        with save.SqlSave() as execute:
            message = execute.select('*', 'test_msg', 'id', self.granarys_index)
            spratio_ratio = float(message[0][1])
            slratio_ratio = float(message[0][2])
            create_money = float(message[0][3])
            pry = float(message[0][4])
            direction = formatting.msg_format(execute.select('direction', 'test_msg', 'id', self.granarys_index))
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
    def gainmonry(self, name):
        # 数量 = 建仓花费 * 杠杠 / 建仓价 
        # gain = （行情价 - 建仓价） * 数量
        with save.SqlSave() as execute:
            create_pricelist = execute.select('openprice', 'granary', 'name', name)
            create_price = float(create_pricelist[len(create_pricelist) - 1][0])
            # print(create_price)
            # create
            message = execute.select('*', 'test_msg', 'id', self.granarys_index)
            create_money = float(message[0][3])
            pry = float(message[0][4])
            count = (create_money * pry) / create_price
            # print(count)
            url = self.Get_url('行情')
            granarys = formatting.msg_format(execute.select('granary', 'test_msg', 'id', self.granarys_index))
            data = '{"symbol":"' + granarys + '"}'
            urls = url + data
            response = requests.get(urls)
            # print(response.text)
            # 实际行情价格
            Cmoney = float(''.join(re.findall('"LP": "(.*?)",', str(response.text))))
            # Cmoney = 221.63
            if message[0][6] == '1':
                gain = (create_price - Cmoney) * count
            else:
                gain = (Cmoney - create_price) * count
            # print(gain)

            return gain

    # 赠金建仓
    def fund_granary(self, name):
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
            granarys = formatting.msg_format(execute.select('granary', 'test_msg', 'id', self.granarys_index))
            data = '{"symbol":"' + granarys + '"}'
            urls = url + data
            response = requests.get(urls)
            print(response.text)
            # 实际行情价格
            Cmoney = float(''.join(re.findall('"LP": "(.*?)",', str(response.text))))
            direction = formatting.msg_format(execute.select('direction', 'test_msg', 'id', self.granarys_index))
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
            granarys = formatting.msg_format(execute.select('granary', 'test_msg', 'id', self.granarys_index))
            directions = formatting.msg_format(execute.select('direction', 'test_msg', 'id', self.granarys_index))
            # money,money2,cmoney = self.formula(name)
            top_money = str(spot)
            data = '{"token":"' + self.Get_token(
                name) + '","symbol":"' + granarys + '","type":"' + directions + '","amount":"' + str(
                create_money) + '","lever":"' + str(pry) + '","topprice":"' + top_money + '"}'
            print(data)
            response = requests.get(urls + data)
            print(response.text)
            orderid = self.extract('"orderid": "(.*?)"', response)
            balanceold = self.extract('"balanceold": "(.*?)",', response)
            balance = self.extract('"balance": "(.*?)",', response)
            openprice = self.extract('"openprice": "(.*?)",', response)
            openfee = self.extract('"openfee": "(.*?)",', response)
            forceprice = self.extract('"forceprice": "(.*?)"', response)
            spratio = self.extract('"spratio": "(.*?)",', response)
            spprice = self.extract('"spprice": "(.*?)",', response)
            slratio = self.extract('"slratio": "(.*?)",', response)
            slprice = self.extract('"slprice": "(.*?)",', response)

            execute.granary(name, granarys, orderid, select, balanceold, balance, openprice, openfee, forceprice,
                            directions)
            # time.sleep(5)

    # 现金建仓
    def create_granary(self, name):
        # self.Login(name)
        with save.SqlSave() as execute:
            urls = self.Get_url('建仓')
            # granary = ['btc','eth','eos','ltc','bch','etc','xrp','bsv']
            granarys = formatting.msg_format(execute.select('granary', 'test_msg', 'id', self.granarys_index))
            # 1空2多
            # direction = ['1','2'] 
            directions = formatting.msg_format(execute.select('direction', 'test_msg', 'id', self.granarys_index))
            # index = random.randint(0,7)
            # indexs = random.randint(0,1)
            money, money2, cmoney = self.formula(name)
            # indexs = 1
            message = execute.select('*', 'test_msg', 'testcase', self.granarys_index)
            amount = message[0][3]
            lever = message[0][4]
            top_money = str(float(money))
            bot_money = str(float(money2))
            # print(top_money,bot_money)
            data = '{"token":"' + self.Get_token(
                name) + '","symbol":"' + granarys + '","type":"' + directions + '","amount":"' + amount + '","lever":"' + lever + '","topprice":"' + top_money + '","botprice":"' + bot_money + '"}}'
            print(urls + data)
            response = requests.get(urls + data)
            # print(data)
            print(response.text)
            orderid = self.extract('"orderid": "(.*?)"', response)
            balanceold = self.extract('"balanceold": "(.*?)",', response)
            balance = self.extract('"balance": "(.*?)",', response)
            openprice = self.extract('"openprice": "(.*?)",', response)
            openfee = self.extract('"openfee": "(.*?)",', response)
            forceprice = self.extract('"forceprice": "(.*?)",', response)
            spratio = self.extract('"spratio": "(.*?)",', response)
            spprice = self.extract('"spprice": "(.*?)",', response)
            slratio = self.extract('"slratio": "(.*?)",', response)
            slprice = self.extract('"slprice": "(.*?)",', response)
            message = execute.select('*', 'test_msg', 'id', self.granarys_index)
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

            execute.granary(name, granarys, orderid, select, balanceold, balance, openprice, openfee, forceprice,
                            directions)

    #
    def select_msg(self, name):
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
    def flat_granary(self, name):
        # self.Login(name)
        with save.SqlSave() as execute:
            url = self.Get_url('平仓')
            orderid_list = execute.select('orderid', 'granary', 'name', name)
            # token_msg = execute.select('token','Name_ResponseMsg','name',name)
            msg = {True: 1, False: 0}[len(orderid_list) != 0]

            orderid = orderid_list[len(orderid_list) - 1][0]
            data = '{"token":"' + self.Get_token(name) + '","orderid":"' + orderid + '"}'
            response = requests.get(url + data)
            # execute.delete('granary','orderid',orderid[0])
            # print(response.text)
            pl = self.extract('"pl": "(.*?)"', response)
            print(orderid, pl, self.gainmonry(name))
            # print(pl)

            # if msg:
            #     for orderid in orderid_list:
            #         data = '{"token":"'+self.Get_token(name)+'","orderid":"'+orderid[0]+'"}'
            #         response = requests.get(url + data)
            #         execute.delete('granary','orderid',orderid[0])
            #         print(response.text)

            # else:
            #     # self.create_granary(name)
            #     # self.flat_granary(name)
            #     pass

    # 修改止盈止损
    def update_ratio(self, name):
        self.Login(name)
        # self.fund_granary(name)
        # self.create_granary(name)
        with save.SqlSave() as execute:
            # self.create_granary(name)
            url = self.Get_url('修改止盈止损')
            # ratio = ['0.00','0.05','0.10','0.15','0.20','0.25','0.30','0.35','0.40','0.45','0.50','0.65','0.70','0.85','0.90','0.95','1.00']
            # ratio_index = random.randint(0,len(ratio))s
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
            data = '{"token":"' + self.Get_token(name) + '","orderid":"' + orderid_list[len(orderid_list) - 1][
                0] + '","topprice":"' + str(top_money) + '","botprice":"' + str(bot_money) + '"}'
            response = requests.get(url + data)
            print(url + data)
            print(response.text)

            # for orderid_tuple in orderid_list:
            #     for orderid in orderid_tuple:
            #         data = '{"token":"'+self.Get_token(name)+'","orderid":"'+orderid+'","topprice":"'+top_money+'","botprice":"'+bot_money+'"}'
            #         time.sleep(3)
            #         response = requests.get(url + data)
            #         print(url + data)
            #         print(response.text)

    # 多级关系建立
    def broker_invite(self):
        self.Register(self.Register(self.Register('')))

    # 金额比例验证
    def count(self, name):
        url = self.Get_url('行情')
        data = '{"symbol":"btc"}'
        urls = url + data
        response = requests.get(urls)
        # 实际行情价格
        Cmoney = ''.join(re.findall('"LP": "(.*?)",', str(response.text)))
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
    def current_granary(self, name, types):
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
                data = '{"token":"' + self.Get_token(
                    name) + '","symbol":"' + symobl + '","type":"' + direction + '","amount":"' + amount + '","lever":"' + lever + '","price":"' + price_money + '"}'
                response = requests.get(url + data)
                print(url + data)
                print(response.text)
                orderid = self.extract('"orderid": "(.*?)"', response)
                balanceold = self.extract('"balanceold": "(.*?)",', response)
                balance = self.extract('"balance": "(.*?)",', response)
                openprice = self.extract('"openprice": "(.*?)",', response)
                openfee = self.extract('"openfee": "(.*?)",', response)
                forceprice = self.extract('"forceprice": "(.*?)",', response)
                spratio = self.extract('"spratio": "(.*?)",', response)
                spprice = self.extract('"spprice": "(.*?)",', response)
                slratio = self.extract('"slratio": "(.*?)",', response)
                slprice = self.extract('"slprice": "(.*?)",', response)
                execute.granary(name, symobl, orderid, select, balanceold, balance, openprice, openfee, forceprice,
                                direction)

            elif select == 1:
                if direction == '1':
                    price_money = str(float(price) + 0.1)
                elif direction == '2':
                    price_money = str(float(price) - 0.1)
                # self.Login(name)
                print(price, price_money)
                url = self.Get_url('现金限价建仓')
                data = '{"token":"' + self.Get_token(
                    name) + '","symbol":"' + symobl + '","type":"' + direction + '","amount":"' + amount + '","lever":"' + lever + '","price":"' + price_money + '"}'
                response = requests.get(url + data)
                print(url + data)
                print(response.text)
                orderid = self.extract('"orderid": "(.*?)"', response)
                balanceold = self.extract('"balanceold": "(.*?)"', response)
                balance = self.extract('"balance": "(.*?)"', response)
                wttime = self.extract('"wttime": "(.*?)"', response)
                # curprice = self.extract('"curprice": "(.*?)"',response)
                execute.current_granary(name, balanceold, balance, orderid, wttime, price_money, message[0][8])

    # 分页查询所有限价单记录
    def Select_CurrentGranary(self, name):
        # self.Login(name)
        url = self.Get_url('分页查询所有限价单记录')
        data = '{"token":"' + self.Get_token(name) + '","page":"1","count":"20"}'
        response = requests.get(url + data)
        print(url + data)
        print(response.text)

    # 限价单撤单
    def delete_CurrentGranary(self, name):
        self.Login(name)
        url = self.Get_url('限价单撤单')
        with save.SqlSave() as execute:
            orderid = formatting.msg_format(execute.select('orderid', 'current_granary', 'name', name))
            print(orderid)
            data = '{"token":"' + self.Get_token(name) + '","orderid":"' + orderid + '"}'
            response = requests.get(url + data)
            print(url + data)
            print(response.text)

    # 余额、冻结赠金
    def get_frostmoney(self, name):
        self.Login(name)
        url = self.Get_url('获取冻结赠金')
        data = '{"token":"' + self.Get_token(name) + '"}'
        response = requests.get(url + data)
        print(response.text)

    # 获取存储充币地址
    def get_TopUpSite(self, name):
        # 币种类型 1:OMNI_USDT 3:ERC20_USDT …
        site_list = ['1', '3', '4']
        site_msg = []
        # site_type = '3'
        url = self.Get_url('获取充币地址')
        for site_type in site_list:
            data = '{"token":"' + self.Get_token(name) + '","type":"' + site_type + '"}'
            response = requests.get(url + data)
            addr = ''.join(re.findall('"addr": "(.*?)"', str(response.text)))
            site_msg.append(addr)
        with save.SqlSave() as execute:
            execute.TopUpSite(name, site_msg[1], site_msg[0], site_msg[2])

    # 提币以及信息获取
    def Withdraw_msg(self, name):
        self.Login(name)
        # ERC-20
        addr = '0x777D76e24da310D91B0C3b48767E898772F198F7'
        money_type = '3'
        # OMNI
        # addr = '3EkaqUNdowvetHDzkYgA6woXcBRkPuULRT'
        # money_type = '1'

        url = self.Get_url('提币')
        amount = '2'
        data = '{"token":"' + self.Get_token(
            name) + '","type":"' + money_type + '","amount":"' + amount + '","addr":"' + addr + '","code":"xwwwwx"}'
        response = requests.get(url + data)
        print(response.text)
        bank_order_id = ' '.join(re.findall('"bank_order_id": "(.*?)"', str(response.text)))
        admin_url = self.Get_url('管理端审核提币')
        admin_data = '{"type":10204,"orderid":"' + bank_order_id + '","verify":1,"token":"' + self.admin_token() + '"}'
        admin_response = requests.get(admin_url + admin_data)
        time.sleep(20)
        self.Withdraw_recode(name)
        print(admin_response.text)

    # 获取提币纪录
    def Withdraw_recode(self, name):
        self.Login(name)
        url = self.Get_url('获取提币纪录')
        # http://47.90.62.21:9003/api/trade/queryoutorderall.do?p={"page":"1","count":"20"}
        data = '{"token":"' + self.Get_token(name) + '","page":"1","count":"20"}'
        response = requests.get(url + data)
        print(response.text)
        txid = ' '.join(re.findall('"txid": "(.*?)"', str(response.text)))
        with save.SqlSave() as execute:
            execute.Withdraw_recod(name, txid)

    # 获取充值纪录
    def Top_msg(self, name):
        url = self.Get_url('获取充值纪录')
        data = '{"token":"' + self.Get_token(name) + '","page":"1","count":"20"}'
        response = requests.get(url + data)
        print(response.text)

    # 分享图盈亏百分比计算
    def share_count(self):
        pass


# 交易员接口类
class DealStaff(supernode):

    def __init__(self):

        self.unify = UnifyWays()

    # sqlite数据格式化处理
    def formatting(self, message):
        msg = ''.join([msg for msg_tuple in message if len(message) != 0 for msg in msg_tuple])
        return msg

    # 管理端审核交易员
    def check_trader(self, userid):
        admin_token = self.admin_token()
        url = self.Get_url('交易员审核')
        data = '{"type":10211, "token":"'+admin_token+'", "userid":"'+userid+'", "state":"1"}'
        self.unify.deamds(url, data)

    # 交易员申请开通
    def apply(self, name):
        url = self.Get_url('交易员申请开通')
        data = '{"token":"' + self.Get_token(name) + '", "language":"zh_CN"}'
        response = self.unify.deamds(url, data)
        return response

    # 交易员详情查询
    def select_detail(self, name):
        with save.SqlSave() as execute:
            userid = self.formatting(execute.select('userid', 'Name_ResponseMsg', 'name', name))
            url = self.Get_url('交易员详情查询')
            data = '{"planerid":"' + userid + '", "language":"zh_CN"}'
            self.unify.deamds(url, data)

    # 交易员交易记录查询sf
    def deal_record(self, name):
        url = self.Get_url('交易员交易记录查询')
        data = '{"planerid":"12076521935","page":"1","count":"20"}'
        self.unify.deamds(url, data)

    # 交易员跟单盈利查询
    def deal_gain(self, name):
        url = self.Get_url('交易员跟单盈利查询')
        data = '{"planerid":"12076521935","page":"1","count":"20"}'
        self.unify.deamds(url, data)

    # 交易员列表查询
    def trader_list(self):
        url = self.Get_url('交易员列表查询')
        data = '{"ordertype":"1"}'
        planerid_str = json.dumps(self.unify.deamds(url, data))
        planerid_list = re.findall('"planerid": "(.*?)"', planerid_str)
        return planerid_list

    # 用户跟单某个交易员
    def user_trader(self, name, planerid, referrerid):
        url = self.Get_url('用户跟单某个交易员')
        data = '{"token":"'+self.Get_token(name)+'","planerid":"'+planerid+'","referrerid":"'+referrerid+'",' \
               '"opentype":"1","openamount":"50.00","openamountdaymax":"0","openamountholdmax":"0",' \
               '"openamountslrate":"0"} '
        self.unify.deamds(url, data)

    # 用户跟单详情查询
    def user_detail(self, name):
        url = self.Get_url('用户跟单详情查询')
        data = '{"token":"'+self.Get_token(name)+'"}'
        self.unify.deamds(url, data)

    # 用户修改跟单参数
    def user_remove_parameter(self):
        url = self.Get_url('用户修改跟单参数')
        data = '{"token":"d9077bd0010e42471ea423f91644edb8","planerid":"12321423523","pause":"1","opentype":"1",' \
               '"openamount":"50.00","openamountdaymax":"500.00","openamountholdmax":"300.00",' \
               '"openamountslrate":"0.60"} '
        self.unify.deamds(url, data)

    # 用户取消跟单某个交易员
    def cancel_deal(self):
        url = self.Get_url('用户取消跟单某个交易员')
        data = '{"token":"d9077bd0010e42471ea423f91644edb8","planerid":"12321423523"}'
        self.unify.deamds(url, data)

    # 用户跟单历史查询
    def user_deal_history(self):
        url = self.Get_url('用户跟单历史查询')
        data = '{"token":"d9077bd0010e42471ea423f91644edb8","planerid":"42133897219"}'
        self.unify.deamds(url, data)

    # 交易员修改信息
    def trader_remove_message(self):
        url = self.Get_url('交易员修改信息')
        data = '{"token":"d9077bd0010e42471ea423f91644edb8","type":"1","info":"内容"}'
        self.unify.deamds(url, data)

    # 交易员跟单提成每日汇总查询
    def trader_everyday_royalties(self):
        url = self.Get_url('交易员跟单提成每日汇总查询')
        data = '{"token":"d9077bd0010e42471ea423f91644edb8","page":"1","count":"20"}'
        self.unify.deamds(url, data)

    # 交易员跟单提成每日明细查询
    def everyday_detail(self):
        url = self.Get_url('交易员跟单提成每日明细查询')
        data = '{"token":"d9077bd0010e42471ea423f91644edb8","tradedate":"152132138900"}'
        self.unify.deamds(url, data)

    # 推荐人详情查询
    def referrer_detail(self):
        url = self.Get_url('推荐人详情查询')
        data = '{"token":"d9077bd0010e42471ea423f91644edb8"}'
        self.unify.deamds(url, data)

    # 推荐人跟单用户信息查询
    def referrer_user_detail(self):
        url = self.Get_url('推荐人跟单用户信息查询')
        data = '{"token":"d9077bd0010e42471ea423f91644edb8"}'
        self.unify.deamds(url, data)

    # 推荐人每日提成汇总信息查询
    def referrer_everyday_collect(self):
        url = self.Get_url('推荐人每日提成汇总信息查询')
        data = '{"token":"d9077bd0010e42471ea423f91644edb8"}'
        self.unify.deamds(url, data)

    # 推荐人每日提成明细查询
    def referrer_everyday_deduct(self):
        url = self.Get_url('推荐人每日提成明细查询')
        data = '{"token":"d9077bd0010e42471ea423f91644edb8"}'
        self.unify.deamds(url, data)

    # 交易员标签信息查询
    def trader_label(self):
        url = self.Get_url('交易员标签信息查询')
        data = '{"language":"en"}'
        self.unify.deamds(url, data)


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
    # 验证开通后列表是否存在
    trader = deal.trader_list()
    with save.SqlSave() as execute:
        userid = UnifyWays().formatting(execute.select('userid', 'Name_ResponseMsg', 'name', name))
        if userid in trader:
            deal.check_trader(userid)
            execute.trader(name, userid, select)


# 用户跟单交易员
def dealtest2():
    deal = DealStaff()
    run = supernode('1')
    withname = '389863294@qq.com'
    planerid = '12913441377'
    referrerid = '0'
    # deal.user_trader(withname, planerid, referrerid)
    # deal.trader_list()
    deal.user_detail(withname)

# 特定经纪人比例
def broker():
    run = supernode('1')
    name = '166422582748@qq.com'
    # name = run.Register(name)
    run.add_money(name)
    # run.get_frostmoney(name)
    run.create_granary(name)
    # time.sleep(2)
    # run.flat_granary(name)


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
    select = '测试环境'
    # broker()
    # dealtest1()
    dealtest2()