#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: chain_getAliasByAddress.py
@time: 2020/1/8 5:24 下午
@desc:
'''

from stake_last_all_api.API import request_Api

''''

7. chain_getAliasByAddress
作用：根据地址获取地址对应的别名
参数：

待查询地址
返回值：地址别名
示例代码
请求：
curl http://39.98.39.224:35645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getAliasByAddress","params":["0x9aD84792B8B88fA11Ac9DcE0615D8D3DA0A269d4"], "id": 3}' -H "Content-Type:application/json"
响应：
{"jsonrpc":"2.0","id":3,"result":"AAAAA"}

'''
def getBalance(api_name, params):
    try:
        result = request_Api(api_name, params)
        print("查询地址别名成功，别名为{}".format(result))
        return result
    except Exception as e:
        print("查询地址别名失败，api返回错误，返回值为{}".format(e))
        return -1
if __name__ == '__main__':
    api_name = "chain_getAliasByAddress"
    params = ["0x9ec31b099f48e20e40698f928ae1b75e114965a9"]
    getBalance(api_name, params)