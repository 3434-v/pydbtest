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

### 15. account_readContract
#### 作用：读取智能合约（无数据被修改）

def openWallet(api_name, params):
    '''
    打开钱包
    :param api_name: account_readContracts
    :param params:发交易的账户地址;合约地址;合约接口
    :return: 无
    示例代码
    curl -H "Content-Type: application/json" -X post --data '{"jsonrpc":"2.0","method":"account_readContract","params":["0xec61c03f719a5c214f60719c3f36bb362a202125","0xecfb51e10aa4c146bf6c12eee090339c99841efc","0x6d4ce63c"],"id":1}' http://127.0.0.1:15645
    '''

    try:
        result = request_Api(api_name, params)
        print("读取合约成功，返回值为{}".format(result))
        return result
    except Exception as e:
        print("读取合约失败，返回值为{}".format(e))
        return -1


if __name__ == '__main__':
    api_name = "account_readContract"
    params = ["0x72fbad34459b1d0f9984dd295261887c661ee841","0x95301c042871b5467b5a0466c5a1e41cf0c78762","0xb05784b8"]
    openWallet(api_name, params)
