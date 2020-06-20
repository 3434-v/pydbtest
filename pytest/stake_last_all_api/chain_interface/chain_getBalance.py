#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_chain_getBalance.py
@time: 2020/1/8 5:22 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''3. chain_getBalance'''


def getBalance(api_name, params):
    '''
    查询地址余额
    :param api_name: chain_getAliasByAddress
    :param params:待查询地址
    :return: 地址中的账号余额
    示例代码
    curl http://39.98.39.224:35645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getBalance","params":["0x9aD84792B8B88fA11Ac9DcE0615D8D3DA0A269d4"], "id": 3}' -H "Content-Type:application/json"
    '''

    try:
        result = request_Api(api_name, params)
        print("查询地址余额成功，地址为{}".format(result))
        return result
    except Exception as e:
        print("查询地址余额失败，api返回错误，返回值为{}".format(e))
        return -1


if __name__ == '__main__':
    api_name = "chain_getBalance"
    # params = ["0x9aD84792B8B88fA11Ac9DcE0615D8D3DA0A269d4"]
    # params = ["0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c"]
    # params = ["0xB490Ffa71d9d1D9f4472FBc46eE6e4FFd2bb486b"]
    # params = ["0xBb6F539027D6A767D8eca16806804A85A5b82ea6"]
    # params = ["0x7b1cAdA0C9c25Eb2E1dE5e5A03a407D11c45b3DE"]
    # params = ["0xe70ae3477f31689f54436bc739961a62ed0a0abb"]
    # params = ["0xAa9f9063000e783924CC0A507bb51936dDD018ab"]
    # params = ["0xD4c338A8ED1D4Ca705FD9f1E22c535610c87a87d"]
    params = ["0x6ddf4bd80c274711d8022e9251323377ba09a2d9"]



    getBalance(api_name, params)
