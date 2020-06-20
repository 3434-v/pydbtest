#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: account_openWallet.py
@time: 2020/1/8 5:40 下午
@desc:
'''

from stake_last_all_api.API import request_Api

### 16. account_estimateGas
#### 作用：估算交易需要多少gas

def openWallet(api_name, params):
    '''
    打开钱包
    :param api_name: account_estimateGas
    :param params:发起转账的地址;金额;备注/data;接收者的地址
    :return: 无
    示例代码
    curl -H "Content-Type: application/json" -X post --data '{"jsonrpc":"2.0","method":"account_estimateGas","params":["0xec61c03f719a5c214f60719c3f36bb362a202125","0xecfb51e10aa4c146bf6c12eee090339c99841efc","0x6d4ce63c","0x110","0x30000"],"id":1}' http://127.0.0.1:15645
    '''

    try:
        result = request_Api(api_name, params)
        print("获取Gas估值成功，返回值为{}".format(result))
        return result
    except Exception as e:
        print("获取Gas估值失败，返回值为{}".format(e))
        return -1


if __name__ == '__main__':
    api_name = "account_estimateGas"
    params = ["0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c","0xDE0B6B3A7640000","0x6d4ce63c","0x9aD84792B8B88fA11Ac9DcE0615D8D3DA0A269d4"]
    openWallet(api_name, params)
