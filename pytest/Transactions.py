import requests
import json
import re
import time

path = 'E:\\pyfile_version\\pytest\\Defiex-test\\'


# 读
def context() -> dict:
    # type_select：1 环境 2：测试用例
    with open(path + 'ErrorCount.json', 'r', encoding='utf8') as count:
        count_dict = json.load(count)
    count.close()
    # print(count_dict)
    return count_dict


# 写
def depict(message: dict):
    print('update->ErrorCount.json')
    count_str = ''
    for key, values in message.items():
        with open(path + 'ErrorCount.json', 'r', encoding='utf8') as count:
            count_dict = json.load(count)
            count_dict[key] = values
            count_str = json.dumps(count_dict)
        count.close()
        print(count_str)
    with open(path + 'ErrorCount.json', 'w+', encoding='utf8') as count:
        count.write(count_str)
    count.close()


def Get_ErrorMsg():
    url = 'https://pro.trade.idefiex.com/admin/getTransactions'
    response = requests.get(url)
    response_json = json.loads(str(response.text))
    Btc_count = len(response_json["BTC"]["depositList"])
    Eth_count = len(response_json["ETH"]["depositList"])
    Trx_count = len(response_json["TRX"]["depositList"])
    old_message = context()
    middle_message = {
        "BTC_Error": Btc_count,
        "ETH_Error": Eth_count,
        "TRC_Erroc": Trx_count
    }
    if old_message['BTC_Error'] < Btc_count:
        for index in range(Btc_count - old_message['BTC_Error']):
            print(response_json["BTC"]["depositList"][index])
        update_message = {'BTC_Error': Btc_count}
        depict(update_message)
    elif old_message['BTC_Error'] > Btc_count:
        print(middle_message)
        depict(middle_message)
    else:
        pass

    if old_message['ETH_Error'] < Eth_count:
        for index in range(Eth_count - old_message['ETH_Error']):
            print(response_json["ETH"]["depositList"][index])
        update_message = {'ETH_Error': Eth_count}
        depict(update_message)
    elif old_message['ETH_Error'] > Eth_count:
        depict(middle_message)
    else:
        pass

    if old_message['TRC_Erroc'] < Trx_count:
        for index in range(Trx_count - old_message['TRC_Erroc']):
            print(response_json["TRX"]["depositList"][index])
        update_message = {'TRC_Erroc': Trx_count}
        depict(update_message)
    elif old_message['TRC_Erroc'] > Trx_count:
        depict(middle_message)
    else:
        pass


Get_ErrorMsg()


